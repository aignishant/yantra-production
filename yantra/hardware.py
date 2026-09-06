"""The hardware profile — the one flag that moves this curriculum between a laptop and a GPU.

Introduced between days 0 and 1 by ADR-0005, and binding under plan §4.1. Every day that touches
an accelerator imports `resolve()` from here rather than reading `torch.cuda.is_available()` for
itself. Two reasons, and the second is the one that matters:

1. Switching machines is one variable, not a search through 228 days of hard-coded devices.
2. Every number this curriculum measures can name the profile that produced it. A speedup, a
   quality delta or a tokens/sec figure is a different number on each path and neither is wrong —
   what is wrong is a ledger row that cannot say which one it is (plan §2, Principle 8).

The refusal below is load-bearing. `YANTRA_PROFILE=gpu` on a torch build without CUDA raises; it
does not quietly return `cpu`. A silent fallback is exactly how a laptop number gets written down
as a GPU number, and it would feel helpful right up until the moment it made the ledger a lie.
"""

from __future__ import annotations

import logging
import os
from dataclasses import dataclass, replace
from pathlib import Path

log = logging.getLogger(__name__)

ENV_VAR = "YANTRA_PROFILE"
DEFAULT_PROFILE = "laptop"
VALID_PROFILES = ("laptop", "gpu", "auto")

#: Where `.env` lives, so a profile set in that file is honoured without a dotenv dependency.
REPO_ROOT = Path(__file__).resolve().parent.parent

#: The command that turns a CPU-only install into a CUDA one. The index URL is deliberately not
#: written here: it depends on the driver, and plan §5 rule 1 forbids inventing one.
GPU_SYNC_HINT = (
    "uv remove torch && uv add torch --index-url <the CUDA index for your driver>\n"
    "  TODO(me): read that index off https://pytorch.org/get-started/locally/ on the day you "
    "switch, and add the dated row to docs/PINS.md."
)


class ProfileError(RuntimeError):
    """Raised when the requested profile and the installed stack disagree.

    Never caught and downgraded to a warning inside this module. The whole point of the profile is
    that a half-finished switch fails loudly (plan §2, Principle 10).
    """


@dataclass(frozen=True)
class Profile:
    """A resolved hardware profile: where tensors live, and how large the day is allowed to be.

    The scale knobs are the only things a day may vary between paths. The mechanism, the code path
    and the check that goes red are identical on both — plan §4.1 rule 6.
    """

    name: str
    device: str
    dtype: str
    model_tier: str
    batch_size: int
    grad_accum: int
    max_seq_len: int
    max_steps: int
    num_workers: int
    torch_available: bool

    @property
    def effective_batch(self) -> int:
        """Samples per optimizer step — held equal across profiles on purpose.

        The laptop path fits a smaller micro-batch into memory and accumulates more of them, so it
        is solving the same optimization problem more slowly rather than a different, easier one.
        A run whose effective batch changed with the machine is not comparable to the other path.
        """
        return self.batch_size * self.grad_accum

    def describe(self) -> str:
        """One line naming the machine, for pasting beside any number this profile produced.

        Plan §4.1 rule 5: a number without a profile is not a number.
        """
        return (
            f"{self.name}: device={self.device} dtype={self.dtype} tier={self.model_tier} "
            f"batch={self.batch_size}x{self.grad_accum}(eff {self.effective_batch}) "
            f"seq={self.max_seq_len} steps={self.max_steps}"
        )


_LAPTOP = Profile(
    name="laptop",
    device="cpu",
    # float32 and not bfloat16: CPU bfloat16 is emulated on most consumer parts, so it buys no
    # memory that matters here and costs accuracy the day is trying to teach.
    dtype="float32",
    model_tier="small",
    batch_size=1,
    grad_accum=16,
    max_seq_len=256,
    max_steps=50,
    num_workers=0,
    torch_available=False,
)

_GPU = Profile(
    name="gpu",
    device="cuda",
    dtype="bfloat16",
    model_tier="large",
    batch_size=8,
    grad_accum=2,
    max_seq_len=1024,
    max_steps=500,
    num_workers=4,
    torch_available=True,
)


def read_env_file(path: Path | None = None) -> dict[str, str]:
    """Parse `KEY=value` lines out of `.env` without taking a dotenv dependency.

    Blank lines, `#` comments and lines with no `=` are skipped; surrounding quotes are stripped.
    A missing file is not an error — most machines set the variable in the shell instead.
    """
    target = path if path is not None else REPO_ROOT / ".env"
    if not target.is_file():
        return {}
    values: dict[str, str] = {}
    for raw in target.read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, _, value = line.partition("=")
        values[key.strip()] = value.strip().strip("\"'")
    return values


def requested_profile(env: dict[str, str] | None = None) -> str:
    """The profile name asked for, before any check that the machine can honour it.

    Precedence is process environment, then `.env`, then the default. That order lets a single run
    be overridden on the command line without editing the file everything else reads. Passing
    `env` explicitly replaces both sources, so a test never depends on the developer's own `.env`.
    """
    source = env if env is not None else {**read_env_file(), **os.environ}
    name = (source.get(ENV_VAR) or DEFAULT_PROFILE).strip().lower()
    if name not in VALID_PROFILES:
        raise ProfileError(
            f"{ENV_VAR}={name!r} is not a profile. Valid values: {', '.join(VALID_PROFILES)}. "
            f"See docs/HARDWARE.md."
        )
    return name


def cuda_available() -> bool | None:
    """`True` / `False` if torch can answer, `None` if torch is not installed at all.

    The three-way answer matters: "torch says no CUDA" is a misconfigured switch and must raise,
    while "no torch yet" is just day 0, where this module is imported by tests and nothing else.
    """
    try:
        import torch
    except ImportError:
        return None
    return bool(torch.cuda.is_available())


def resolve(env: dict[str, str] | None = None) -> Profile:
    """The whole flag, in one call: read the request, check the machine, return the profile.

    Raises `ProfileError` when `gpu` is requested and torch is installed without CUDA. It does not
    raise when torch is absent entirely — that is day 0, and a fresh clone must be able to run
    `granth.py check` before it has installed anything.
    """
    name = requested_profile(env)
    has_cuda = cuda_available()

    if name == "auto":
        resolved = _GPU if has_cuda else _LAPTOP
        log.info("%s=auto resolved to %r (cuda_available=%r)", ENV_VAR, resolved.name, has_cuda)
        return _with_torch_flag(resolved, has_cuda)

    if name == "gpu" and has_cuda is False:
        raise ProfileError(
            f"{ENV_VAR}=gpu, but the installed torch reports no CUDA device.\n"
            f"This does not fall back to CPU on purpose: a laptop number recorded as a GPU "
            f"number is the failure plan §4.1 exists to prevent.\n"
            f"Either finish the switch:\n  {GPU_SYNC_HINT}\n"
            f"or set {ENV_VAR}=laptop and run the day at CPU scale."
        )

    if name == "gpu" and has_cuda is None:
        raise ProfileError(
            f"{ENV_VAR}=gpu, but torch is not installed, so the profile cannot be honoured.\n"
            f"Install it for this profile first:\n  {GPU_SYNC_HINT}"
        )

    return _with_torch_flag(_GPU if name == "gpu" else _LAPTOP, has_cuda)


def _with_torch_flag(profile: Profile, has_cuda: bool | None) -> Profile:
    """Stamp the frozen profile with whether torch was importable at resolve time."""
    return replace(profile, torch_available=has_cuda is not None)


def main() -> None:
    """Print the resolved profile. Run before any measurement, paste the line beside the number."""
    profile = resolve()
    print(profile.describe())
    print(f"torch installed: {profile.torch_available}")
    if profile.name == "laptop":
        print(
            # Plain ASCII on purpose: a Windows console in cp1252 turns a section sign into a
            # replacement character, and a mangled reference is worse than a spelled-out one.
            "This is the laptop path. Any number measured here is a laptop number and says so in "
            "its ledger row (plan 4.1, rule 5)."
        )


if __name__ == "__main__":
    main()
