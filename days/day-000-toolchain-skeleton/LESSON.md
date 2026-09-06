---
day: 0
phase: 0
phase_name: "Foundry"
title: "Toolchain and skeleton"
ids: []
kind: setup
plan_version: "v1.0.0"
parts: 6
generated: "2026-09-07"
status: written
commit: ""
---

> **Yesterday:** nothing — this is the first day.
> **Today:** one tool owns the environment, the repository cannot leak a key, and the gate refuses
> a day that only looks finished.
> **Tomorrow:** the first real subject — what a language model actually is.

## §1 Where we are

Before anything is taught, the workshop has to be set up.

Not because setup is interesting, but because the three things it establishes are assumed silently
by all 228 days after it. The environment is reproducible, so a failure on day 73 is a failure of
your hyperparameters rather than of your install. The repository cannot leak a credential, because
by phase 19 there is an agent holding real ones. And the gate refuses, so a day that was rushed
does not get to look the same as a day that was understood.

Today is the day where the stakes are zero and the habits are cheap. Every one of these gets
expensive later: the environment when a training run costs money, the secrets when the repository
goes public, the gate when a pull request is blocking someone else.

**Day 0 closes no concept IDs.** That is deliberate and recorded in
[`ADR-0004`](../../docs/adr/ADR-0004-day-zero-does-not-build-the-toolchain.md) — the toolchain is a
precondition for the curriculum rather than part of it, and moving an ID here to make day 0 look
productive would put traceability out of step on the first day.

## §2 The map

### 1 · One owner for the environment

The rule: exactly one tool decides which interpreter you get and which packages it can see.

| Part | Title | What it answers | Level |
| --- | --- | --- | --- |
| [1.1](parts/01-one-owner/1.1-why-one-tool-owns-the-environment.md) | Why one tool owns the environment | Why is "it works on my machine" always the same bug? | foundation |
| [1.2](parts/01-one-owner/1.2-uv-and-the-venv-you-never-activate.md) | uv, and the venv you never activate | Why does this project never run `source .venv/bin/activate`? | working |

### 2 · A repository that cannot leak a key

The rule: the protection has to exist before the thing it protects.

| Part | Title | What it answers | Level |
| --- | --- | --- | --- |
| [2.1](parts/02-cannot-leak-a-key/2.1-the-skeleton-and-gitignore-first.md) | The skeleton, and .gitignore before .env exists | Why does the order these files are created in matter? | working |
| [2.2](parts/02-cannot-leak-a-key/2.2-the-secret-that-was-already-committed.md) | The secret that was already committed | What do you actually do when the key is already in history? | production |

### 3 · The gate

The rule: a day is finished when the checks are green and the checklist is ticked, and by nothing
else.

| Part | Title | What it answers | Level |
| --- | --- | --- | --- |
| [3.1](parts/03-the-gate/3.1-what-the-gate-checks.md) | What the gate checks | Why run five checks over the whole repository every time? | working |
| [3.2](parts/03-the-gate/3.2-the-refusal.md) | The refusal | Why is `done` refusing to commit the feature rather than the friction? | production |

**Part 2.2 is today's deliberate failure.** Cause it in a throwaway directory and watch every tool
report that nothing is wrong.

## §3 Setup

Versions verified on 2026-09-07; every one of them has a row in `docs/PINS.md`.

```bash
# 1. the environment's owner — check it is present and note the version
uv --version                      # expect 0.11.7 or newer

# 2. the interpreter uv will install and manage for this project
uv python install 3.12
python3 --version                 # the SYSTEM python — expect 3.12.3 here; not the one we use

# 3. the repository, in the order that matters (part 2.1)
git init
printf '.env\n.venv/\n__pycache__/\n' > .gitignore
git add .gitignore && git commit -m "gitignore before the first secret exists"

# 4. the project, and the quality tools
uv init --name yantra
uv add --dev ruff pytest          # expect ruff==0.16.6 or newer

# 5. prove nothing is activated
uv run python -c "import sys; print(sys.executable)"   # must end in .venv/bin/python3

# 6. the repository's own wiring
python granth.py doctor
```

## §4 Build brief

| File | What it must do |
| --- | --- |
| `.env.example` | `TODO(me)`: every variable name the project will need, with **empty** values. Committed. A new clone must be able to read this file and know what to set. |
| `pyproject.toml` | `TODO(me)`: add a `[tool.pytest.ini_options]` block registering the `gpu` and `live` markers, so `check` can exclude them without warning. |
| `tests/test_repository_wiring.py` | `TODO(me)`: one test asserting `.env` is **not** in `git ls-files`. It must pass now and fail if anyone ever commits it. |
| `lab/leak/` | `TODO(me)`: reproduce part 2.2 end to end. Commit a fake key, add `.gitignore` after, and confirm with `git log -p` that the key survives `git rm --cached`. This directory is gitignored. |

Leave every `TODO(me)` for yourself. The parts teach the mechanism; the reps are not written for
you.

## §5 The check that must be able to fail

The wiring test in `tests/test_repository_wiring.py` — the one asserting `.env` is untracked.

**Make it go red on purpose:** `git add -f .env && uv run pytest tests/test_repository_wiring.py`.
It must fail. Then `git rm --cached .env` and watch it go green again.

A check nobody has seen fail has verified nothing. That is not a slogan on day 0; it is the reason
this box exists in every checklist for the next 228 days.

## §6 Budget

| Resource | Today |
| --- | --- |
| Model calls | **0.** No provider is contacted, no key is needed, nothing is rate-limited. |
| GPU hours | **0.** Everything today runs on a laptop. |
| Money | **0.** |
| Downloads | The Python 3.12 toolchain and four small packages. Tens of megabytes. |

The first day that spends anything is day 15, the first real fine-tune. Plan §4 has the table.

## §7 Traps

- **`pip install` "just this once".** It will work, and it will not be in the lockfile. This is the
  single most common way an environment stops being reproducible (part 1.1).
- **`.gitignore` written after the first commit.** Every tool will tell you it is fine. None of
  them is lying; they are answering a different question (part 2.1).
- **`git rm .env` without `--cached`.** Deletes your actual credentials from disk. Recoverable
  only if you still have them somewhere else.
- **A bare `.env*` pattern in `.gitignore`.** It swallows `.env.example`, and the next person to
  clone has no idea which variables exist.
- **Editing a generated document in `docs/`.** `TRACEABILITY.md`, `CURRICULUM_INDEX.md`,
  `TRACKER.md`, `WIKI.md` and `wiki/` are outputs. The next `index` overwrites you without a word.
- **Testing an exit code through a pipe.** `python granth.py brief 5 | head; echo $?` reports
  `head`'s status, not the guard's. You will conclude the ordering guard is broken (part 3.2).

## §8 Verify before you build

| What | Where it was checked | Date | What it confirmed |
| --- | --- | --- | --- |
| `uv` version | `uv --version` on this machine | 2026-09-07 | `uv 0.11.7 (x86_64-unknown-linux-gnu)` |
| System Python | `python3 --version` | 2026-09-07 | `Python 3.12.3` |
| `ruff` version | `uv add ruff` resolution output | 2026-09-07 | `ruff==0.16.6` |
| PEP 668 refusal text | `pip install requests` against the system interpreter | 2026-09-07 | The `externally-managed-environment` error quoted verbatim in part 1.1 |
| Tracked-file ignore behaviour | `git check-ignore -v .env` on a tracked file | 2026-09-07 | Exits 1 and prints nothing — quoted in parts 2.1 and 2.2 |
| Repository wiring | `python granth.py doctor` | 2026-09-07 | 229 days, 400 IDs, each assigned to exactly one day |

`TODO(me)`: re-run each of these on the day you actually do day 0, and correct any that have moved.
A version copied from this table rather than observed is exactly the thing Principle 7 forbids.

## §9 Say it out loud

Day zero was setup, and I did it before any code because all three things it establishes are
assumed silently by everything after. One tool owns the environment — `uv` — so the environment is
a file rather than a history, which means a failure in a training run three months from now is a
failure of my hyperparameters and not of my install. The repository got its `.gitignore` before it
got its first secret, which sounds pedantic until you notice that `.gitignore` cannot untrack
anything: I committed a fake key on purpose and watched `git status` stay clean and `check-ignore`
print nothing while the key sat in the history. And the gate refuses — it will not commit a day
with an unticked checklist. I deliberately ran three commands that all exited non-zero, because a
check nobody has watched fail hasn't been tested, and I would rather learn that on a day where
nothing is at stake than on the day an eval gate is blocking someone else's pull request.

## §10 Done when

See [`CHECKLIST.md`](CHECKLIST.md). Defined by understanding and green checks, never by effort
spent.

## §11 Ledger & commit

**`docs/PROGRESS.md`:**

```text
| 0 | 2026-09-07 | — | 6 | <hash> | green | Setup day; closes no IDs by design (ADR-0004). |
```

**`docs/PINS.md`** — three rows, all observed today:

```text
| uv | 0.11.7 | `uv --version` | 2026-09-07 | 0 | owns the environment |
| Python | 3.12.3 (system) | `python3 --version` | 2026-09-07 | 0 | the interpreter NOT used; recorded to make the contrast visible |
| ruff | 0.16.6 | `uv add ruff` resolution output | 2026-09-07 | 0 | lint + format, both gate steps |
```

**`docs/GLOSSARY.md`** — one row per term defined for the first time today:

```text
| interpreter | The `python` program that reads and executes your file; a machine usually has several | day 0 part 1.1 | — |
| package | Code someone else wrote, installed into one specific interpreter rather than into the machine | day 0 part 1.1 | dependency |
| virtual environment | A directory holding one interpreter and its own packages, isolated from every other | day 0 part 1.1 | venv |
| lockfile | The record of exactly which package versions were installed, down to the hash | day 0 part 1.1 | `uv.lock` |
| repository | A directory git is tracking, whose history is append-only | day 0 part 2.1 | repo |
| tracked | A file git has been told to record every version of, forever | day 0 part 2.1 | — |
| check | A command that passes or fails with an exit code a script can read | day 0 part 3.1 | gate step |
```

**Commit:**

```text
day 0: toolchain and skeleton — closes no IDs
```
