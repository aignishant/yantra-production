# HARDWARE — the one flag, and what it moves

The contract is plan [§4.1](00_MASTER_PLAN.md); the reasoning is
[ADR-0005](adr/ADR-0005-the-hardware-profile.md). This file is the operating manual: what to set,
what changes, what to do the day a GPU arrives, and what the two paths are *not* allowed to differ
in.

**The default assumption of this curriculum is a laptop with no GPU.** The accelerated path is the
documented alternative. That is the correct way round for the machine this repository is being
worked through, and it means every day from 1 to 228 is runnable today rather than readable today
and runnable later.

---

## The flag

One variable, in `.env`:

```
YANTRA_PROFILE=laptop
```

| Value | Device | What it is for |
| --- | --- | --- |
| `laptop` | `cpu` | **The default.** Smaller base model, shorter sequences, fewer steps |
| `gpu` | `cuda` | A resident or rented accelerator |
| `auto` | detected | Opt-in only, on a rented box that may be either |

Precedence is the process environment first, then `.env`, then the default. So a one-off run can
override the file without editing it:

```bash
YANTRA_PROFILE=gpu uv run python lab/train.py     # bash
$env:YANTRA_PROFILE='gpu'; uv run python lab/train.py   # PowerShell
```

**`auto` is deliberately not the default.** A profile resolved by detection cannot be read off the
command line, so a number measured under it cannot be attributed to a machine afterwards — and on
a rented box, "afterwards" is when the box no longer exists.

---

## What the profile actually decides

Everything a day is allowed to vary between paths, and nothing else:

| Knob | `laptop` | `gpu` | Why it moves |
| --- | --- | --- | --- |
| `device` | `cpu` | `cuda` | Where tensors live |
| `dtype` | `float32` | `bfloat16` | CPU bfloat16 is emulated on most consumer parts — it buys no memory that matters and costs accuracy the day is teaching |
| `model_tier` | `small` | `large` | The day maps the tier to a base model; the tier is not a model name, because the right model changes per day |
| `batch_size` | 1 | 8 | What fits in memory |
| `grad_accum` | 16 | 2 | **Chosen so `effective_batch` is 16 on both paths** |
| `max_seq_len` | 256 | 1024 | Attention is quadratic in sequence length; this is where a CPU day is won or lost |
| `max_steps` | 50 | 500 | How long the run is |
| `num_workers` | 0 | 4 | Dataloader processes; 0 avoids the spawn overhead that dominates a small CPU run |

**The equal effective batch is the important row.** `batch_size × grad_accum` is 16 on both paths,
so the laptop is solving *the same optimization problem more slowly* rather than an easier one.
A test asserts it (`test_effective_batch_is_equal_across_profiles`); if it ever goes red, the two
paths have stopped being comparable and any number measured on one no longer says anything about
the other.

Using it in a day:

```python
from yantra.hardware import resolve

profile = resolve()
model = model.to(profile.device)
for step in range(profile.max_steps):
    ...
```

**Line by line:**

- `from yantra.hardware import resolve` — one import, in every day that touches an accelerator. A
  day that calls `torch.cuda.is_available()` directly has opted out of the flag and will be found
  by the next machine change.
- `profile = resolve()` — reads the environment, then `.env`, then the default; checks the machine
  can honour what was asked; raises if it cannot. This is the entire switch.
- `model.to(profile.device)` — `"cpu"` or `"cuda"` as a plain string. Nothing in the day branches
  on which; the branch already happened, once, inside `resolve()`.
- `range(profile.max_steps)` — the scale knob, read rather than hard-coded. A literal `500` here is
  the bug this whole file exists to prevent, because it is invisible until the day someone runs it
  on the other machine.

---

## What the two paths may **not** differ in

Plan §4.1 rule 6. The laptop path is a *smaller true version* of the day:

- the same mechanism, hand-rolled the same way (Principle 4);
- the same code path — no `if cpu:` branch that skips the thing being taught;
- the same check going red for the same reason.

A laptop path that mocks the mechanism is not a laptop path. It is a stub, and the honest form of a
stub is a `TODO(me)` in the hub saying the day needs an accelerator. **Three days say exactly
that**: 49 (QLoRA on an 8B base), 77 (the first managed endpoint), 149 (the managed vector store).
Their parts are still read and their mechanisms still built at laptop scale; it is the day's
headline *measurement* that waits.

---

## Every number carries its profile

Plan §4.1 rule 5. Before measuring anything, run:

```bash
uv run python -m yantra.hardware
```

Observed on this machine, 2026-09-07, with no torch installed yet:

```text
laptop: device=cpu dtype=float32 tier=small batch=1x16(eff 16) seq=256 steps=50
torch installed: False
This is the laptop path. Any number measured here is a laptop number and says so in its ledger row (plan 4.1, rule 5).
```

That first line is what goes beside the number — in the part that quotes it, and in the
`docs/PROGRESS.md` row. A speedup measured on `laptop` and a speedup measured on `gpu` are both
true and are not the same claim. A ledger row that cannot say which one it holds is a row nobody
can use, and Principle 8 is what it stops being.

---

## The day a GPU arrives

**One flag and one re-sync.** It is not one thing, and pretending otherwise would be the first lie
in the file: a CPU-only wheel does not become a CUDA wheel by setting an environment variable.

1. Install the CUDA build of torch.

   ```bash
   uv remove torch
   uv add torch --index-url <the CUDA index for your driver>
   ```

   `TODO(me)`: the index URL depends on your driver and is **not** written here on purpose — plan
   §5 rule 1 forbids inventing a version, and a stale CUDA index is exactly that. Read it off
   `https://pytorch.org/get-started/locally/` on the day you switch, and add the dated row to
   [`PINS.md`](PINS.md) with the driver version beside it.

2. Flip the flag in `.env`:

   ```
   YANTRA_PROFILE=gpu
   ```

3. Confirm:

   ```bash
   uv run python -m yantra.hardware
   ```

   It must print `device=cuda`. If it raises instead, step 1 did not take.

**Do not re-run old days' numbers and overwrite the laptop rows.** Append. The laptop-versus-GPU
pair is one of the more useful things this repository will end up holding, and it only exists if
nobody tidies the first half away.

---

## When it breaks

**Setting the flag without the re-sync.** The most likely mistake, because step 2 is the easy one
and step 1 is the one that needs a browser. Verbatim, on this machine on 2026-09-07:

```text
ProfileError: YANTRA_PROFILE=gpu, but torch is not installed, so the profile cannot be honoured.
Install it for this profile first:
  uv remove torch && uv add torch --index-url <the CUDA index for your driver>
  TODO(me): read that index off https://pytorch.org/get-started/locally/ on the day you switch, and add the dated row to docs/PINS.md.
```

With the CPU wheel installed rather than absent, the wording changes and the point does not:

```text
ProfileError: YANTRA_PROFILE=gpu, but the installed torch reports no CUDA device.
This does not fall back to CPU on purpose: a laptop number recorded as a GPU number is the failure plan §4.1 exists to prevent.
```

**It raises rather than falling back, and that is the design.** A fallback here would feel helpful
and would silently produce the exact failure ADR-0005 was written to prevent. The refusal is the
load-bearing half of the mechanism, not a rough edge on it.

**A typo in the value.** `YANTRA_PROFILE=cuda` is not a profile:

```text
ProfileError: YANTRA_PROFILE='cuda' is not a profile. Valid values: laptop, gpu, auto. See docs/HARDWARE.md.
```

**`import yantra` fails in a script you wrote yourself.** `pyproject.toml` has no `[build-system]`,
so `uv` treats this as a virtual project and never installs `yantra/` into the venv. The root
`conftest.py` puts it on `sys.path` for pytest; a standalone script needs to be run from the
repository root, or with `PYTHONPATH=.` set.

---

## Making the check go red

The check that matters is `tests/test_hardware_profile.py::test_gpu_profile_refuses_when_torch_has_no_cuda`.

Break it on purpose: in `resolve()`, replace the `raise ProfileError(...)` for the
`gpu`-without-CUDA case with `return _with_torch_flag(_LAPTOP, has_cuda)` — the silent fallback.
Observed 2026-09-07:

```text
>       with pytest.raises(ProfileError) as caught:
E       Failed: DID NOT RAISE ProfileError
```

Every other test in the file still passes with that fallback in place. That is the point of having
this one: a silent fallback breaks nothing visible, which is what makes it dangerous.
