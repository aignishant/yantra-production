# ADR-0004 — Day 0 uses the toolchain rather than building it

- **Date:** TODO(me)
- **Day:** 0
- **Phase:** 0
- **Status:** accepted
- **Amends:** `00_MASTER_PLAN.md` §17, day 0's title
- **Related:** ADR-0001

## Context

An earlier draft of day 0 had the learner write the driver script — the brief, depth, index, check
and done verbs — as its subject. That is attractive: the first day builds the thing that checks
every later day, and nothing is a black box.

It is also wrong here, for a mechanical reason. `granth.py` is emitted by the skill that scaffolds
this repository, so it exists before day 0 does. A day whose build brief asks the learner to write
a file that is already on disk, already passing its own checks, teaches nothing and cannot have a
check that goes red.

## Decision

**Day 0's subject is the toolchain and the skeleton: one owner for the environment, a repository
that cannot leak a key, and a first run of the gate.** It closes no identifiers.

Day 0 is the only day in the plan that closes none, and the only one that installs no dependency
beyond the quality tools. Everything it establishes — `.gitignore` before `.env` exists, `uv`
owning the environment, a green `check`, a `done` that refuses — is a precondition every later day
assumes rather than part of the curriculum.

Its deliberate failure is the gate refusing: commit a day with an unticked checklist and watch
`done` reject it.

## Options considered

| Option | Why not |
| --- | --- |
| **Have day 0 write the driver** | The file already exists. A build brief that asks for it produces either a duplicate or a no-op, and neither can go red. |
| **Have day 0 close the first `TF` identifiers instead** | Then the environment work has no home and gets done half-way, in passing, on the day someone first hits a missing tool. |
| **Skip day 0 entirely** | Every later day assumes the skeleton. Assuming it silently is how a curriculum acquires a first day that cannot be reproduced. |

## Consequences

**Better.** Traceability stays honest — no identifier moved to make day 0 look productive.

**Worse.** The toolchain is a black box on day 0. A reader who wants to understand it reads
`granth.py`, which is one file and stdlib-only for exactly this reason, but that is reading rather
than building.

**Revisit if:** the toolchain is ever replaced by something project-specific, in which case
building it becomes a legitimate day 0 subject again.
