# Day 1 — definition of done

`python granth.py done 1` refuses to commit while any box below is unticked. That refusal is the
point: a day is finished when it is understood and the checks are green, and by nothing else.

No box here carries a time estimate, and none ever will.

## Read

- [x] `parts/01-the-last-mile/1.1-the-parcel-that-reached-the-depot.md` — read · ran its check · answered its question out loud
- [x] `parts/01-the-last-mile/1.2-the-four-things-nobody-else-owns.md` — read · ran its check · answered its question out loud
- [x] `parts/01-the-last-mile/1.3-the-other-side-of-the-table.md` — read · ran its check · answered its question out loud
- [x] `parts/02-the-definition-of-done/2.1-deployed-is-not-adopted.md` — read · ran its check · answered its question out loud
- [x] `parts/02-the-definition-of-done/2.2-the-number-that-decides.md` — read · ran its check · answered its question out loud
- [x] `parts/02-the-definition-of-done/2.3-the-success-criterion-that-cannot-fail.md` — read · ran its check · answered its question out loud
- [x] `parts/03-the-accountability/3.1-the-sentence-you-sign.md` — read · ran its check · answered its question out loud

## Build

- [x] `docs/ENGAGEMENT.md` — *The process* names one stage, one line of business, and the locations it runs at
- [x] `docs/ENGAGEMENT.md` — *The success criterion* carries all five parts: baseline, target, unit, owner, exit condition
- [x] The baseline is marked `(provisional)` — it has not been measured, and day 3 measures it
- [x] `docs/ENGAGEMENT.md` — *Who owns the number* names a **role**, never a person, or honestly says `nobody`
- [x] `docs/ENGAGEMENT.md` — *The exit condition* says how long the target must hold **and** what must be true of your own involvement
- [x] `docs/ENGAGEMENT.md` — *What this engagement will not do* carries at least three lines
- [x] `status:` is `draft` — day 3 flips it to `baselined`, day 5 to `signed`

## Check

- [x] **Break it on purpose, watch it go red, fix it.** Run `uv run python -m pytest tests/test_engagement_brief.py -q` **before** editing the brief; see two failures — five `TODO(me)` markers, and a criterion carrying zero numbers
- [x] The same command is green after the brief is filled in
- [x] Held the criterion up against the test in part 2.2: you can describe a state of the world in which it is definitely **not** met
- [x] `python granth.py depth 1` — green
- [x] `python granth.py check` — green across the whole repository

## Record

- [x] Five new terms have rows in `docs/GLOSSARY.md` (see the hub's §11)
- [x] No row added to `docs/PINS.md` — nothing was installed today
- [x] No row added to `docs/SOURCES.md` — nothing was cited today, and the hub's §2 says why
- [x] The `PROGRESS.md` row is pasted, and its `Notes` column records the check's known weak assertion
- [x] Committed as `day 001: what a forward deployed AI engineer actually owns — closes FDE-01, FDE-02`
