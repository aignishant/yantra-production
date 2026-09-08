# Architecture Decision Records — Yantra

One file per structural decision: `ADR-NNNN-<kebab-slug>.md`, numbered from `0001`, **never
renumbered and never rewritten**. A decision that turns out wrong is **superseded** by a later ADR
that says so; the original stays exactly as it was written.

That rule is the whole value. An ADR set you can edit is a set that always looks like it was right
from the start, which teaches nothing. An ADR set you cannot edit records what was known at the
time, which is the only thing that makes the next decision easier.

## When an ADR is required

Write one for anything **structural** — a change to the shape of the work rather than to its
content:

- the day format, the ID scheme, the phase boundaries, the numbering rule
- skipping, merging, reordering or inserting a day (the plan forbids doing this without one)
- adopting, replacing or dropping a tool the whole project depends on
- a change in scope: something the plan promised and no longer will, or the reverse
- a constraint that turned out to be wrong

Do **not** write one for: a version bump (that is `PINS.md`), a wording change (that is
`CHANGELOG_PLAN.md`), or a decision inside a single day (that belongs in the day).

Rule of thumb: **if someone six months from now would ask "why on earth is it like this?", it
needs an ADR.** If they would not notice, it does not.

## The relationship to the changelog

`CHANGELOG_PLAN.md` records **what the plan now says**. An ADR records **why, and what else was
considered**. A structural change gets both, and the changelog entry links the ADR.

## The template

Copy `ADR-0000-template.md`. Every section is required; an ADR with no *Options considered* is a
justification written after the fact, not a decision record.

| # | Title | Date | Status |
| --- | --- | --- | --- |
| [0001](ADR-0001-the-plan-as-adopted.md) | The plan as adopted | 2026-09-06 | accepted |
| [0002](ADR-0002-prompt-and-context-moved-early.md) | Prompt and context engineering are taught before retrieval and agents | TODO(me) | accepted |
| [0003](ADR-0003-security-distributed-not-chaptered.md) | Security identifiers sit in the phases that create the exposure | TODO(me) | accepted |
| [0004](ADR-0004-day-zero-does-not-build-the-toolchain.md) | Day 0 uses the toolchain rather than building it | TODO(me) | accepted |
| [0005](ADR-0005-the-hardware-profile.md) | The curriculum runs laptop-first, behind one flag | 2026-09-07 | accepted |
| [0006](ADR-0006-the-merge.md) | Yantra and Setu become one 182-day curriculum | 2026-09-07 | accepted |
| [0007](ADR-0007-the-sitting-budget.md) | Four documents a day, the scene merged into the idea, signatures in the build brief | 2026-09-08 | accepted |
