"""The checks that keep the one-flag switch honest (plan §4.1, ADR-0005).

The interesting one is `test_gpu_profile_refuses_when_torch_has_no_cuda`. Everything else here is
wiring; that one is the reason the module exists. Delete the `raise` in `resolve()` and watch it
go red — a silent CPU fallback would pass every other test in this file.
"""

from __future__ import annotations

import os
import subprocess
import sys
from pathlib import Path

import pytest

from yantra.hardware import (
    DEFAULT_PROFILE,
    ENV_VAR,
    Profile,
    ProfileError,
    read_env_file,
    requested_profile,
    resolve,
)

ROOT = Path(__file__).resolve().parent.parent


def test_default_is_the_laptop() -> None:
    """No variable set anywhere means the laptop path, never detection.

    If this ever fails because the default became `auto`, read ADR-0005's options table first: a
    detected default is convenient and makes every measurement unattributable.
    """
    assert DEFAULT_PROFILE == "laptop"
    assert requested_profile(env={}) == "laptop"


def test_the_flag_selects_the_profile() -> None:
    assert resolve(env={ENV_VAR: "laptop"}).device == "cpu"
    assert resolve(env={ENV_VAR: "laptop"}).name == "laptop"


def test_an_unknown_profile_names_the_valid_ones() -> None:
    with pytest.raises(ProfileError, match="is not a profile"):
        requested_profile(env={ENV_VAR: "a100"})


def test_gpu_profile_refuses_when_torch_has_no_cuda(monkeypatch: pytest.MonkeyPatch) -> None:
    """The load-bearing check: a half-finished switch fails loudly instead of returning CPU.

    `cuda_available()` is forced to `False` — the shape of a machine where torch is installed but
    it is the CPU wheel, which is exactly this repository after day 1 on the laptop path.
    """
    monkeypatch.setattr("yantra.hardware.cuda_available", lambda: False)
    with pytest.raises(ProfileError) as caught:
        resolve(env={ENV_VAR: "gpu"})
    message = str(caught.value)
    assert "does not fall back to CPU" in message
    assert "uv add torch" in message, "the refusal must name the command that fixes it"


def test_gpu_profile_refuses_when_torch_is_absent(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr("yantra.hardware.cuda_available", lambda: None)
    with pytest.raises(ProfileError, match="torch is not installed"):
        resolve(env={ENV_VAR: "gpu"})


def test_auto_falls_back_quietly_because_it_was_asked_to(monkeypatch: pytest.MonkeyPatch) -> None:
    """`auto` is the one profile allowed to resolve downward — that is what opting in bought."""
    monkeypatch.setattr("yantra.hardware.cuda_available", lambda: False)
    assert resolve(env={ENV_VAR: "auto"}).name == "laptop"


def test_effective_batch_is_equal_across_profiles() -> None:
    """Plan §4.1 rule 6: the laptop path is the same optimization problem, run more slowly.

    If this fails, the two paths are training on different effective batch sizes and no number
    measured on one is comparable to the other.
    """
    laptop = resolve(env={ENV_VAR: "laptop"})
    gpu = _declared_gpu_profile()
    assert laptop.effective_batch == gpu.effective_batch


def _declared_gpu_profile() -> Profile:
    """The GPU profile's declared constants, read without requiring a GPU to read them."""
    from yantra.hardware import _GPU

    return _GPU


def test_describe_names_the_profile_for_the_ledger() -> None:
    """Plan §4.1 rule 5: a number without a profile is not a number."""
    line = resolve(env={ENV_VAR: "laptop"}).describe()
    assert line.startswith("laptop:")
    assert "device=cpu" in line


def test_env_file_is_read_without_a_dotenv_dependency(tmp_path: Path) -> None:
    env_file = tmp_path / ".env"
    env_file.write_text("# a comment\n\nYANTRA_PROFILE='gpu'\nNOT_A_PAIR\n", encoding="utf-8")
    assert read_env_file(env_file) == {ENV_VAR: "gpu"}


def test_the_module_runs_as_a_script() -> None:
    """`python -m yantra.hardware` is what you run before a measurement; it must not be broken."""
    result = subprocess.run(
        [sys.executable, "-m", "yantra.hardware"],
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=False,
        env=os.environ | {ENV_VAR: "laptop"},
    )
    assert result.returncode == 0, result.stderr
    assert "device=cpu" in result.stdout
