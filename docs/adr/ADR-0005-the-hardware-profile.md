# ADR-0005 — The curriculum runs laptop-first, and every accelerated day ships two paths behind one flag

- **Date:** 2026-09-07
- **Day:** between days 0 and 1
- **Phase:** 0
- **Status:** accepted
- **Amends:** `00_MASTER_PLAN.md` v1.0.0 → v1.1.0, §4 (adds §4.1); day 1 §3
- **Related:** ADR-0001, ADR-0004

## Context

Plan §4 opens by saying it is "the section most likely to be wrong for **your** situation, and it
is the one to correct first," and closes with a warning to correct it before day 0. That warning
has now been taken up: **the machine this curriculum is being worked through has no GPU.** Not "a
small one" — none.

The plan already anticipated the *access* half of this. §4's table says Colab and Kaggle carry
phases 1–4 and that a GPU is rented by the hour from phase 6. What it did not say is what the
**documents and the code** do about it, and that gap is the expensive one. Left alone it produces
one of two failures, and both are already latent in the repository as written:

1. **Days become unrunnable.** Day 15 is the first real fine-tune. If its commands assume a
   resident GPU, the day is read rather than done, its check never goes red, and `done 15` is
   either refused forever or ticked dishonestly. A curriculum whose middle third can only be read
   has stopped being a curriculum somewhere around day 15.

2. **Numbers stop being attributable.** Principle 8 says measure, then claim. The KV-cache
   speedup, the quantization quality delta, the student-versus-teacher tokens/sec — every one of
   them is a different number on a laptop than on a rented accelerator, and neither is wrong. What
   is wrong is a `PROGRESS.md` row that does not say which machine produced it. Sixty days later
   there is no way to tell, and the ledger's numbers are decoration.

The compounding is the reason this is decided now rather than at day 15. Day 1 already pins its
torch install to a CPU-only index:

```bash
uv add torch --index-url https://download.pytorch.org/whl/cpu
```

That line is correct today and becomes a trap the moment a GPU arrives, because a CPU-only wheel
does not become a CUDA wheel by setting an environment variable — it has to be reinstalled. Every
day written between now and that reinstall will hard-code whichever assumption its author held.
Fifteen days of that is a fifteen-file edit. A hundred and fifty days of it is a rewrite.

## Decision

**The default hardware assumption of this curriculum is a laptop with no GPU.** The GPU path is
the documented alternative, not the baseline. One environment variable selects between them:

```
YANTRA_PROFILE=laptop    # the default, and what the days are written against
YANTRA_PROFILE=gpu       # a resident or rented accelerator
YANTRA_PROFILE=auto      # opt-in detection; never the default (see below)
```

It resolves through exactly one module, `yantra/hardware.py`, which every day that touches an
accelerator imports rather than reimplementing. The module returns a device, a dtype and the
handful of scale knobs a day is allowed to vary — nothing else changes between paths.

**The load-bearing half is the refusal, not the switch.** `YANTRA_PROFILE=gpu` on a machine whose
torch has no CUDA raises and names the command that fixes it. It does not fall back to CPU. A
silent fallback is precisely how a laptop number gets recorded as a GPU number, which is the
failure mode this ADR exists to prevent — and it is the failure mode a fallback *feels* helpful
enough to cause.

`auto` exists because it is genuinely convenient on a rented box that may be either. It is not the
default for the same reason: a resolved-by-magic profile cannot be read off the command line, so a
measurement taken under it cannot be attributed without going back to the machine, which by then
has been returned.

**Three rules follow, and they bind every day from 1 to 228.** They are written into plan §4.1
rather than only here:

1. A day that touches an accelerator states **both** paths in its §6 budget — what the laptop path
   costs in capability, and what the GPU path costs in money.
2. Every measured number carries the profile that produced it, in the document and in the ledger
   row. A number without a profile is not a number.
3. The laptop path is a **smaller true version** of the day, never a mocked one. Fewer steps, a
   smaller base model, a shorter sequence — the same mechanism, the same code path, the same check
   going red. A day whose laptop path skips the mechanism has no laptop path; it has a stub, and
   the honest form of that is a `TODO(me)` saying the day needs an accelerator.

## Options considered

| Option | Why not |
| --- | --- |
| **Do nothing — keep §4's substitution column** | It answers "where do I get a GPU" and not "what does the day do without one". The substitution column is advice; the days need a contract. It also leaves day 1's CPU-pinned install as an untracked assumption. |
| **Write the days GPU-first, add a CPU path when it hurts** | "When it hurts" is day 15, and by then fifteen days have hard-coded the assumption in their setup blocks, their build briefs and their expected outputs. The edit is cheapest now and gets more expensive every day. |
| **Rent an accelerator from day 1 and write GPU-only** | Spends money on days 1–14 that plan §4 already establishes need none, and makes the whole curriculum unavailable whenever the rental is not running. It also deletes the `yantra-edge` service's entire premise, which is CPU inference. |
| **Detect the device automatically everywhere, no flag** | Convenient and unattributable. Two runs of the same command on two machines produce two numbers and one ledger row, and nothing in the repository can tell them apart. This is `auto`, and it is why `auto` is opt-in. |
| **A `gpu` extra with no runtime flag — the install decides everything** | Covers the wheel and nothing else. Batch size, sequence length, step count and dtype are runtime choices, and a day that varies them by editing its own source is a day that cannot be re-run on the other path. |

## Consequences

**Better.** Every day from 1 to 228 is runnable on the machine that exists today. The moment an
accelerator appears, the switch is one variable and one re-sync, and the code refuses to let that
be done half-way. Ledger numbers become attributable, which is the difference between Principle 8
being a rule and being a slogan.

**Worse — and this row is not decoration.** Every accelerated day now costs more to write: two
budget lines instead of one, two sets of scale knobs, and a laptop path that has to be run before
it can be documented. The laptop path is genuinely slower, and some days will be far slower for a
number that is only interesting as a ratio. Three days in the plan — 49 (QLoRA on an 8B base), 77
(the first managed endpoint) and 149 (the managed vector store) — have no honest laptop path at
all, and will say so in their hubs rather than pretend.

**The new failure mode this creates:** a day whose laptop path quietly stops exercising the
mechanism — the batch size drops to 1, the step count drops to 2, and the thing being taught no
longer happens. What catches it is rule 3 above plus the day's own check: if the check still goes
red for the right reason on the laptop path, the mechanism is still there. If it can only go red
on an accelerator, the day says so.

**Revisit if:** a resident accelerator becomes the working machine for good, at which point the
default flips and `laptop` becomes the documented alternative — the mechanism is symmetric and the
flip is this file plus one line of `granth.toml`. Or if the two paths ever diverge enough that a
day needs two different explanations rather than two different numbers, which would mean the
profile is carrying more than scale and should be split.
