---
day: 1
phase: 1
phase_name: "The engagement"
title: "What a forward deployed AI engineer actually owns"
ids: [FDE-01, FDE-02]
kind: craft
plan_version: "v2.0.0"
parts: 7
generated: "2026-09-07"
status: written
commit: ""
---

> **Yesterday:** a repository that cannot leak a key, and a gate that refuses a half-finished day.
> **Today:** what this whole curriculum is accountable for — the gap nobody else owns, and the
> definition of done that is not "it's deployed".
> **Tomorrow:** the demo-to-production gap, taken apart on the vendor chatbot the client already
> paid for and switched off.

## §1 Where we are

Day 0 built the machine. Today is the first day of the curriculum proper, and it does not touch a
model, because the first decision in any AI engagement is not technical and gets made whether or
not anyone notices making it.

One image runs through the whole day. A parcel travels six hundred miles and stops two miles from
your door, on a shelf, because the flat number will not go into a handheld and nobody wrote down
the door code. Six hundred miles worked. You have no parcel.

That is the shape of most AI work that fails. The model is the six hundred miles. The two miles are
the domain nobody encoded, the system the answer never reached, the permission nobody scoped, and
the number nobody took before starting. Those two miles are the job, and today names them, then
turns the second half — *when am I finished?* — into a document that a check can refuse.

You will write one artifact today, `docs/ENGAGEMENT.md`, and you will watch a test reject your
first attempt at it. That rejection is the day's deliberate failure and it is scheduled, not
accidental.

## §2 The map

### 1 · The last mile

The mental model: the demo is a prefix, not a small version — and the six stages after it belong to
nobody by default.

| Part | Title | What it answers | Level |
| --- | --- | --- | --- |
| [1.1](parts/01-the-last-mile/1.1-the-parcel-that-reached-the-depot.md) | The parcel that reached the depot | Why is a working model not a working system? | foundation |
| [1.2](parts/01-the-last-mile/1.2-the-four-things-nobody-else-owns.md) | The four things nobody else owns | What exactly sits in the gap, and how do I test whether anyone owns it? | foundation |
| [1.3](parts/01-the-last-mile/1.3-the-other-side-of-the-table.md) | The other side of the table | What does "forward deployed" actually change about my position? | working |

### 2 · The definition of done

The mental model: three finish lines, and only the third one has the business as its subject.

| Part | Title | What it answers | Level |
| --- | --- | --- | --- |
| [2.1](parts/02-the-definition-of-done/2.1-deployed-is-not-adopted.md) | Deployed is not adopted | Why can a dashboard be entirely green over a dead service? | working |
| [2.2](parts/02-the-definition-of-done/2.2-the-number-that-decides.md) | The number that decides | What are the five parts of a success criterion that can be wrong? | working |
| [2.3](parts/02-the-definition-of-done/2.3-the-success-criterion-that-cannot-fail.md) | The criterion that cannot fail ⚠️ | Why write the rule as a check instead of remembering it? | production |

⚠️ **2.3 is today's deliberate failure.** You run the check against an unfilled brief and watch two
assertions go red before you fix them.

### 3 · Accountability

The mental model: the two halves join into one falsifiable, bounded sentence that ends.

| Part | Title | What it answers | Level |
| --- | --- | --- | --- |
| [3.1](parts/03-the-accountability/3.1-the-sentence-you-sign.md) | The sentence you sign | What is this curriculum accountable to, and where is each clause discharged? | production |

**No `sources/` today.** `Hidden Technical Debt in Machine Learning Systems` (NeurIPS 2015) was
looked up live and is genuinely on point, but the record carries no arXiv identifier and no DOI, so
it fails plan §5 rule 3 — cite by title *and* identifier. It is not cited rather than cited loosely.
`docs/SOURCES.md` gains no row today, exactly as on day 0.

## §3 Setup

Nothing to install. Day 0's environment is the environment, and today adds no dependency.

```bash
uv run python -c "import sys; print(sys.executable)"
```

Confirm the path ends in `.venv`. If it does not, day 0's environment is not the one you are in,
and everything below runs against the wrong interpreter — day 0 part 1.2 has the mechanism.

## §4 Build brief

Two files. One is already in the repository; the other is yours to write.

**Provided, and worth reading before you write:**

- `docs/ENGAGEMENT.md` — the scaffold. Five sections, a `status:` line, an append-only amendment
  table.
- `tests/test_engagement_brief.py` — the check. Five assertions on the *shape* of the brief. It
  cannot tell whether any figure is true; part 2.3 explains why that boundary is deliberate.

**Yours:**

- `TODO(me)`: fill in all five sections of `docs/ENGAGEMENT.md` against the client fixed in
  plan §3 — the mid-size general insurer. Use the five parts from part 2.2 for the criterion.
- `TODO(me)`: mark today's baseline `(provisional)`. You have not measured it and day 3 will.
  Writing a number you have not measured without saying so is the exact failure principle 7 exists
  to prevent.
- `TODO(me)`: in *What this engagement will not do*, write at least three lines. Part 1.3's
  unbounded-engagement message is what this section is for.

**Not yours today:** the real baseline. Day 3 measures it. Do not go looking for a figure to make
the brief feel finished.

## §5 The check that must be able to fail

```bash
uv run python -m pytest tests/test_engagement_brief.py -q
```

**Run it before you edit anything.** Expect two failures: five `TODO(me)` markers remaining, and a
success criterion carrying zero numbers. Part 2.3 has the verbatim output to compare against.

Then fill in the brief and run it again. Green is the day's check.

**One honest note about this check,** carried from part 2.3: three of its five assertions pass
against the untouched scaffold, and one of those — the owner-and-exit test — passes only because
the guidance blockquote is long. That is a hole. Day 3 tightens it. A check you have not yet found
the hole in is a check you have not used.

## §6 Budget

| Line | Today |
| --- | --- |
| Model calls | **0.** No provider is contacted today. Day 33 is the first paid call. |
| GPU hours | **0.** |
| Money | **$0.** |
| Lane (§4.2) | Not applicable — today touches no infrastructure. |
| Hardware profile (§4.1) | Not applicable — today runs no accelerator code and records no measurement, so no profile is stated. Day 61 is the first day that needs one. |

## §7 Traps

- **Writing the brief before reading 2.2.** The check will pass a criterion with two numbers in it
  and no meaning. The check is a floor, not the standard.
- **Filling in a baseline you did not measure.** The most tempting error of the day. Mark it
  `(provisional)` or leave the shape and no figure — never a confident number you invented.
- **Naming a person as the owner.** Roles only. This document outlives the engagement and people
  leave. Plan §21 forbids person names throughout for the same reason.
- **Treating "nobody" as a failure.** If no role owns the number, write *nobody*. Part 1.2: an
  unowned responsibility that has been named is a scope item; one that has not been named is why
  the project will be late.
- **Skipping the red run.** Fixing the brief first and then running the check once, green, teaches
  nothing. A check nobody has seen fail has verified nothing — day 0 part 3.2.

## §8 Verify before you build

Nothing is pinned today, so there is no version to observe. What was verified:

| What | How | Date | Result |
| --- | --- | --- | --- |
| The day is next in order | `python granth.py brief 1` | 2026-09-07 | Passes; day 0 is the last `PROGRESS.md` row |
| `Hidden Technical Debt in Machine Learning Systems` | Fetched the NeurIPS proceedings record | 2026-09-07 | Title and year confirmed; **no arXiv ID, no DOI** → fails §5 rule 3, so not cited |
| The check can fail | `uv run python -m pytest tests/test_engagement_brief.py -q` | 2026-09-07 | Two assertions red against the scaffold; output pasted verbatim in part 2.3 |

## §9 Say it out loud

Answer without scrolling, in your own words:

1. Name the six stages that come after the model produces a correct answer, and say who assumes
   each one is handled.
2. Name the four things in the gap, and the first-meeting question that reveals whether anyone owns
   each.
3. Name the three finish lines. Which one has a human being as its subject?
4. Say the five parts of a success criterion. Which one expires if you do not take it now?
5. Say the day's sentence in full, and name the day in this plan where each of its three completion
   clauses becomes true or false.

If question 5 is the hard one, that is the right one to be stuck on — it is the contract for the
next 180 days.

## §10 Done when

Every box in [`CHECKLIST.md`](CHECKLIST.md) is ticked, the check is green, and the brief's five
sections are filled with a criterion that could be wrong.

## §11 Ledger & commit

**`docs/GLOSSARY.md`** — five new terms:

```text
| demo | A system shown on inputs chosen by the person showing it | day 1 part 1.1 | 1 |
| production | A system running on inputs nobody chose, at a volume nobody supervises | day 1 part 1.1 | 1 |
| adoption | Production, plus the intended people using it instead of what they used before | day 1 part 2.1 | 1 |
| baseline | What a number was before the work started, measured rather than recalled | day 1 part 2.2 | 1 |
| exit condition | How long a target must hold, and what must be true of your involvement when it does | day 1 part 2.2 | 1 |
```

**`docs/PROGRESS.md`** — one row:

```text
| 1 | What a forward deployed AI engineer actually owns | FDE-01, FDE-02 | 2026-09-07 | green | Brief drafted; baseline provisional until day 3. Owner-and-exit assertion passes on guidance length — tighten on day 3. |
```

**`docs/PINS.md`** — no row. Nothing was installed.
**`docs/SOURCES.md`** — no row. See §2.
**`docs/PROVENANCE.md`** — no row. No dataset or checkpoint was downloaded.

**Commit:**

```text
day 001: what a forward deployed AI engineer actually owns — closes FDE-01, FDE-02
```

Then, and only then:

```bash
python granth.py done 1
```

It refuses while any checklist box is unticked or the `PROGRESS.md` row is absent. Today is the
first day it has anything real to refuse.
