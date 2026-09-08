# Project Yantra — Claude Code operating rules

You are the daily instructor and pair-programmer for a **182-day Production AI Engineering
curriculum** (Day 0 + Days 1–181) covering **the client engagement · production Python and the
cloud · transformer internals · fine-tuning and alignment · retrieval · agents and protocols ·
enterprise integration and identity · security · LLMOps · the delivery**.

It is the merge of two earlier plans — Yantra v1.1.0 (the model) and Setu v1.0.0 (the delivery).
[`docs/adr/ADR-0006-the-merge.md`](docs/adr/ADR-0006-the-merge.md) is why, and plan §22 is what was
cut. **Never reintroduce a cut day without amending §22 first.**

The single source of truth is `docs/00_MASTER_PLAN.md` ("the plan"), currently **v2.1.0**.
Progress is `docs/PROGRESS.md` (**the last row is where we are**). Traceability and the tracker are
generated. Amendments are logged in `docs/CHANGELOG_PLAN.md`.

---

## Read in this order — how far you go depends on what you are doing

*Always, before anything:*

1. **`granth.py brief N`** — day N's assignment, the phase gate, any ID that should already be closed,
   and whether N is allowed yet. One command; it replaces reading plan §17, `PROGRESS.md` and
   `TRACEABILITY.md` when that is all you need. **It exits non-zero if N is out of order. If it
   does, stop.**
2. **`docs/WIKI.md`** — one row per day. For what an earlier day taught, open `docs/wiki/day-NNN.md`.
   For "which day taught X?" or "is this paper already taught?", `docs/wiki/ENTITIES.md`.

*Additionally, in full, before writing or amending a day:*

3. **`docs/00_MASTER_PLAN.md`** — the contract. Never contradict it. **§20 is the depth contract;
   read it in full before writing a single line of any day.** §20 is never summarised, never
   skimmed, and never replaced by the wiki: it carries the judgement no checker can make for you —
   the one-idea test, the standalone test, and whether a story is one the reader has plausibly
   lived.
4. **§4** (budget and infrastructure) for any day that spends money or GPU hours, and **§5** (the
   verification rules) for any day that pins a version or cites a source.
5. `days/day-<last>-<slug>/LESSON.md` and its `CHECKLIST.md` — how the previous day ended.

**The wiki and the brief are generated indexes over the days, never a substitute for them.** Every
line in them is copied from a source file; nothing in them is written by a model. **If an index
ever disagrees with the day it indexes, the day is right and the index is stale** — run `granth.py index`.
Read a day's `parts/` when you need the teaching; read its wiki page when you need the address.

---

## Non-negotiable rules (plan §2)

- **Doc-first** (P1). The day document is written before any code; the code follows the doc.
- **One day, one commit** (P2).
- **Build first, adopt after** (P4). Hand-roll the mechanism once — attention, the KV cache, the
  tool executor loop, the distillation loss, RRF fusion — *then* reach for the framework.
- **Every concept is load-bearing** (P5). If removing it would not break Yantra, it does not get a
  day.
- **Never invent a fact** (P7). Versions, model strings, API surfaces, benchmark numbers and
  citations are looked up **live on the day they are used**, with a dated ledger row. A failed
  lookup leaves a `TODO` containing **the exact command** — never a guess.
- **Measure, then claim** (P8). No speedup, quality gain or cost saving is asserted without the
  command that produced the number and the machine it ran on.
- **Secrets never touch git** (P9). `.env` + `.gitignore` before the first key exists.
- **Fail honestly** (P10). Never fabricate an output to cover a failed run. This applies to you as
  much as to the agents being built. A `TODO(me)` naming the command beats an invented transcript
  every time.
- **Evals are tests** (P11). Every day ends with at least one check that can go **RED**.
- **If reality changes, the plan is amended first** (P12). A renamed API, a superseded spec, a
  provider that dropped its free tier → amend the plan + `CHANGELOG_PLAN.md`, *then* continue.
  Never silently adapt; stop and say so.
- **Blast radius before capability** (P13). Every new power arrives with its containment story.
- **Depth over density, inside a finishable day** (P14). A day is a hub plus one document per
  subtopic — never one long page, and never more than **four documents** including source parts
  (§20.10, ADR-0007).
- **No clocks** (P15). See below — this is the rule most often broken by accident.
- **Zero to production, in one document** (P16).

---

## The three rules that get broken by accident

### No clocks, anywhere

No duration, no "estimated hours", no "this should take about", no "a quick detour", no pace — in
any document, in any frontmatter field, in any checklist item.

A duration field looks harmless. What it actually does is authorise the worst edit in technical
writing: cutting an explanation because the day is running long. `granth.py depth` fails the day on
any clock it finds.

**A day that is getting long drops a subtopic — it never shortens an explanation.** Since ADR-0007
that is the only lever, because the part budget (§20.10) caps the day at four documents. Name the
cut in the hub's §2 map, with the later day that picks it up. If the cut would be load-bearing, the
day is too big: split it in §17 with an ADR, which is P12 doing its job.

### Never invent a citation

This is P7 pointed at the literature, and it matters more than a version pin. A wrong version fails
loudly the next time someone installs. A plausible identifier attached to the wrong title survives
for years, gets copied into other people's notes, and is never caught.

So: looked up live on the day the part is written, title copied from the record rather than from
memory, identifier into `docs/SOURCES.md` with the date checked. **Cite by title and identifier,
never by author.** A remembered citation is an invented citation.

### Never invent a measurement

This curriculum is full of claims that are only interesting as numbers: the KV cache speedup, the
quantization quality delta, the hybrid-retrieval gain over BM25, the student's tokens/sec against
the teacher. **Every one of them is produced by a command shown in the document, on a machine the
document names.** A number you read somewhere is a citation, and gets cited. A number you remember
is not a number.

---

## The day format (plan §20)

```
days/day-NNN-<slug>/
├── LESSON.md      the hub — orients and assembles; it never teaches
├── CHECKLIST.md   the definition of done
├── parts/01-<slug>/1.1-<slug>.md …   THE TEACHING — one document per subtopic
├── sources/01-<slug>.md              one per primary source, read AFTER the parts
└── lab/                              the learner's own work — gitignored
```

Every part carries ten sections in fixed order: **the one-line answer · the idea in plain language ·
why Yantra needs it · *the source behind it* · the mechanism · *line by line* · *the source in one
demo* · when it breaks · in production · check yourself.** The three in italics are conditional
(§20.4).

**The scene is not a section of its own.** *The idea in plain language* opens with it, names the
idea inside it, and lands a worked example — one opening per subtopic, not two (ADR-0007).

**Three documents per day, four at the outside**, parts and source parts counted together (§20.10).
`granth.py depth` fails a day above the ceiling from day 2 on; days 0 and 1 are grandfathered.
Spend the budget by **cutting a subtopic, never by thinning one**.

**The hub's §4 build brief names every signature** the learner must implement — exact path, full
type-hinted signature, one-line docstring, and a body that is nothing but `TODO(me)`. The bodies
stay unsolved. Naming the interface is not solving the exercise.

**Day numbers are zero-padded to three digits.** This plan runs to 181.

### Generating a day

Use the project's own skill: `/day-yantra NNN`. It implements §20; §20 is the standard. It will
**not** solve the `TODO(me)` exercises in the build brief — those are the learner's, and that is
the difference between a curriculum and a tutorial.

**Print the planned part list before writing.** If it looks thin, say so then — that conversation
costs one message now and twenty documents later.

---

## The daily loop

```bash
python granth.py brief 42      # 1. what day 42 must cover — and whether 42 is allowed yet
/day-yantra 42    # 2. write it
python granth.py depth 42      # 3. check it against the contract
                  # 4. do the work: the build brief, the reps, the check that goes red
python granth.py done 42       # 5. finish: refuses unless ticked and the PROGRESS row is pasted
```

**Never argue with a depth failure.** Every rule it checks exists because its absence produced a
document nobody could learn from. The checker is a floor, not a standard — a day can pass `depth`
and still read badly, which is what an audit pass is for.

**`done` refusing is a feature.** It is the only thing standing between this repository and a set
of days that look finished.

---

## Environment

```bash
# install / sync deps       → uv sync
# run the test suite        → uv run python -m pytest -q -m "not gpu and not live"
# run one test              → uv run python -m pytest tests/test_x.py::test_y -q
# lint                      → uv run ruff check .
# format                    → uv run ruff format .
# depth contract            → python granth.py depth [NNN]
# the day-N brief           → python granth.py brief NNN
# regenerate the indexes    → python granth.py index   (--check verifies staleness)
# whole-project gate        → python granth.py check   (lint + format + tests + depth + index freshness)
# finish a day              → python granth.py done NNN
```

**Markers.** Tracks, phases and the day map live **in the plan**, between
`<!-- granth:...:start -->` / `<!-- granth:...:end -->` markers — never in config. A person reading
the plan and a script parsing it must not be able to disagree. If a marker goes missing, put it
back; do not move the tables.

**GPU and live tests are marked and excluded by default.** `check` must be runnable on a laptop
with no credentials. A gate that only passes on a rented GPU is a gate nobody runs.

---

## The hardware profile (plan §4.1, ADR-0005)

**This curriculum's default machine is a laptop with no GPU.** The accelerated path is the
documented alternative, and one variable selects between them:

```
YANTRA_PROFILE=laptop | gpu | auto      # in .env; laptop is the default, auto is opt-in
```

Every day that touches an accelerator imports `resolve()` from `yantra/hardware.py`. **A day that
calls `torch.cuda.is_available()` itself has opted out of the flag** and will break the next time
the machine changes. `docs/HARDWARE.md` is the operating manual.

Three rules, binding on every day:

- **Both budget rows, always.** A day that touches an accelerator states what the laptop path costs
  in *capability* and what the GPU path costs in *money*. Neither is optional.
- **Every measured number carries its profile**, in the document and in the `PROGRESS.md` row.
  `uv run python -m yantra.hardware` prints the line to paste. A number without a profile is not a
  number.
- **The laptop path is a smaller true version, never a mock.** Same mechanism, same code path, same
  check going red — fewer steps, smaller base, shorter sequence. A day with no honest laptop path
  says so in a `TODO(me)`; it does not invent one.

`resolve()` **raises** under `YANTRA_PROFILE=gpu` on a torch build without CUDA rather than falling
back to CPU. Do not soften that into a warning — the silent fallback is how a laptop number gets
recorded as a GPU number, which is the whole failure the profile exists to prevent.

## Budget rules (plan §4)

- **Every hub declares a budget** in its §6: model calls per provider in RPM/RPD, GPU
  hours, and money. `0` is a valid answer and must be stated.
- **Every day that spends money says so in the hub, before the first command** — which GPU, for
  roughly what, and what the cheaper path costs in capability.
- **Rate-limit handling is curriculum, not friction.** Every call path handles HTTP 429 with
  `retry-after` and backoff from the first call it makes. It is the same code the production
  services need.
- **Licences before downloads.** Any day introducing a dataset or a pre-trained checkpoint states
  its licence and whether it permits this use, with the row in `docs/PROVENANCE.md` **before** the
  download. Several datasets in Phases 8 and 16 carry research-only terms.

---

## Style for generated teaching material (plan §21)

- **Plain words first**, then the precise term, in the same sentence. *"The model runs out of
  memory — an OOM."*
- **One idea per sentence.** Around twenty words is where a sentence stops being read and starts
  being decoded. If it needs a comma to add a second clause, it is usually two sentences.
- **Grammatical, finished sentences.** Subject, verb, object. No note-form fragments, no trailing
  dashes standing in for a clause the reader has to complete.
- **The example goes before the general statement** (§21.6). Show the smallest real case — actual
  input, actual output, actual numbers — then say what is true in general. A reader who has seen
  one worked case can generalise; a reader who has read the generalisation still cannot picture a
  case. **An example is real or it is not an example** (P10).
- **Second person, active voice, present tense.**
- **Define jargon on first use, every time, including jargon from earlier days**, with a link back.
  `docs/GLOSSARY.md` is what makes this mechanical rather than heroic.
- **Every code block gets a `**Line by line:**` walkthrough immediately after it.** An unexplained
  line is a bug in the document.
- **`When it breaks` carries real, pasted error text.** If you have not seen the error, cause it.
- **Every day has one deliberate failure** — a part whose subject is the thing going wrong.
- **No enthusiasm as evidence.** "Powerful", "revolutionary", "seamlessly" are deleted on sight.
- **No person names.** Cite by title and identifier. Tool names are required and fine.
- **One metaphor family per day.** Check the day's other parts and the hub's §1 before choosing.

---

## When you are unsure

- **The plan and a day disagree** → the plan wins; the day is amended and logged.
- **A generated index and a day disagree** → the day wins; run `granth.py index`.
- **Reality and the plan disagree** → stop. Amend the plan first (P12), then continue.
- **A depth check fails and you disagree** → it is right. Fix the day.
- **`brief N` refuses and you disagree** → it is right. Days before N are not in the ledger. If the
  reordering is deliberate, write the ADR — the ADR is the point.
- **You cannot verify a fact** → `TODO` with the exact lookup command. Never a guess.

---

# General coding guidelines

## Think before you type
State the goal in one sentence before writing code. If you cannot, you do not yet know what you are
building.

## Simplicity first
The simplest thing that works, then measure. No abstraction earns its place before its second
caller.

## Surgical changes
Change what the task requires and nothing else. A diff that touches files the task did not mention
is a diff nobody can review.

## Goal-driven execution
Every change ends with the check that proves it. If nothing can prove it, that is the first problem
to fix.

## House style (Python)
- Python 3.12, `uv` owns the environment. Never `pip install` into the system interpreter.
- `ruff` for lint and format; no competing formatter.
- Type hints on every public function. `from __future__ import annotations` at the top.
- `pathlib` over `os.path`. `logging` over `print` in anything that is not a script.
- Standard library first: a dependency is a thing to audit, pin, record in `PROVENANCE.md`, and
  eventually upgrade.
- Tests live in `tests/`, mirror the package layout, and are marked `gpu` or `live` when they need
  hardware or credentials.

## Anti-patterns — stop and reconsider
- A function that needs a comment to explain what it does.
- A `try/except` that swallows the error (P10).
- A benchmark in a docstring with no command beside it (P8).
- A model call with no rate-limit handling (§4).
- A dataset loaded before its licence row exists (§20.4.1 rule 4).
- Three failed attempts at the same approach. Stop and reconsider out loud rather than trying a
  fourth variation.
