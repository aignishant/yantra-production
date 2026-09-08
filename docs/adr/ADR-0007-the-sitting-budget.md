# ADR-0007 — A day is at most four documents, the scene and the idea are one section, and the build brief names every signature

- **Date:** 2026-09-08
- **Day:** between days 1 and 2
- **Phase:** 1
- **Status:** accepted
- **Amends:** `00_MASTER_PLAN.md` v2.0.0 → v2.1.0, §20.4 (sections 3 and 4 merge), §20.5 (§4 build brief), §20.7 (the part budget replaces "no target part count"), §20.8, §20.9 (enforcement), §20.10 (new), §21 (adds §21.6)
- **Related:** ADR-0001, ADR-0006

## Context

Two days are written. Day 0 is six parts. Day 1 is seven parts across three sections, and every one
of those parts carries eleven sections including a separate story and a separate plain-language
explanation of the same idea.

The learner works this curriculum in **roughly half an hour a day**. That number is not in any
document in `days/` and it never will be — Principle 15 stands untouched — but it is the real
constraint on the real machine, and the plan has been sized as if it did not exist. §20.7 says it
outright: *"There is deliberately no target part count and no target length. If a subject needs four
parts it gets four; if it needs twenty-two it gets twenty-two, and the day simply spans more
sittings."*

Twenty-two parts is not a day that spans more sittings. It is a day that never closes. The failure
that produces is worse than the one §20 was written to prevent, because it is invisible: a day sits
half-read for a week, the checklist never gets ticked, `done` keeps refusing — correctly — and the
ledger's last row stops moving. There is no row in `PROGRESS.md` that says *"this day was too big to
finish"*, so the plan learns nothing from it. **A day nobody finishes teaches less than a day that
dropped a subtopic.**

Three further things are true of the two written days, and each costs the reader:

1. **The story and the idea say the same thing twice.** §20.4 splits them because a scene must come
   before an abstraction. That ordering is right. Making them two headings is what is wrong: the
   scene gets told, then abandoned, and the idea gets re-explained from cold underneath it. The
   reader reads two openings to one subtopic.

2. **The prose explains where an example would show.** The register in §21.1 is correct and the
   sentences that implement it are long. A reader who has half an hour learns more from a worked
   example than from a paragraph about the example.

3. **The build brief says what to build, not what to write.** §20.5's §4 requires files and unsolved
   `TODO(me)` markers. Day 1's brief names `docs/ENGAGEMENT.md` and the sections it needs. What it
   does not carry, on a code day, is the signature the learner must implement against — so the
   learner reaches a later `TODO(me)` knowing the goal and not the interface, and either invents one
   the next day's code does not call, or goes back to the part to reverse-engineer it. Neither is
   the exercise.

## Decision

**Four documents is the ceiling for a day; three is the target.** Parts and source parts count
together, because a source part is a document the reader must read. A day whose assigned IDs cannot
be taught in four documents is a day that gets split in the plan — with an ADR — not a day that
quietly grows to nine.

**Sections 3 and 4 of the part contract become one section, `The idea in plain language`.** It opens
with the concrete scene, under the same rules §20.4's story already carried, and continues straight
into the idea without a second heading and without starting the explanation over. The heading name
is unchanged so that the two written days remain valid.

**The build brief names every signature.** For each file the day asks for: the exact path, every
function and class the learner must write with its full type-hinted signature and a one-line
docstring saying what it returns, and the command that runs it. **The bodies stay `TODO(me)`.**
Naming the interface is not solving the exercise; it is the difference between an exercise and a
guess at what the next day expects.

**The style guide gains §21.6, plain English and example-first.** One idea per sentence, everyday
words, and a worked example — real input, real output — before the general statement rather than
after it.

**The ceiling binds from Day 2.** Days 0 and 1 are read, understood and grandfathered; the checker
exempts every day below `max_parts_from_day`. Rewriting a day the learner has already read teaches
nobody anything.

## Options considered

| Option | Why not |
| --- | --- |
| **Do nothing — keep "no target part count"** | It is the status quo that produced a seven-part Day 1 for a half-hour sitting, and 180 more days of it. The rule was written to stop days being trimmed to fit a clock; it has instead made them impossible to finish. Depth that is never read is not depth. |
| **Keep the part count and let a day span several sittings** | This is what §20.7 already says, and it is what is failing. A day spanning five sittings has no definition of done that arrives, so the checklist stays unticked and the ledger stops. The gate then blocks the next day for a week — the gate working correctly on a badly sized day. |
| **Cut the eleven part sections instead of the part count** | Cheaper per document and much more expensive overall. The sections that would go are *When it breaks* and *In production* — the two that make the difference between a tutorial and a curriculum, and the two §20.8 names as the classic failure. Fewer documents each carrying all of it beats more documents each carrying half. |
| **A ceiling of five or six** | Too close to the current shape to change behaviour. Four forces the choice; five permits the drift back. |
| **Drop Principle 15 and write the half hour into the days** | This is the thing §20 exists to prevent. A duration inside a day authorises cutting an explanation to fit it. The budget belongs in the plan, where it sizes the split before the writing starts, and nowhere in `days/`. |

## Consequences

**Better.** A day fits the sitting it is actually worked in, so its checklist gets ticked and the
ledger keeps moving. One opening per subtopic instead of two. Examples in place of paragraphs. A
build brief the learner can implement against without guessing the interface.

**Worse, and this row is the honest one.** The ceiling is a real cut. Subtopics that would have had
a document of their own will now be folded into a neighbouring part or dropped, and the one-idea
test of §20.1 is applied at a coarser grain than it was written for. The heavy days — attention, the
KV cache, tokenization, DPO, hybrid retrieval — lose the room to give each mechanism its own page.
**This is a genuine loss of depth per day**, accepted because depth the learner never reaches is not
depth. The compensating rule is that a subtopic is **cut and named as cut**, never silently thinned:
a subtopic that would have been a part gets a line in the hub's §2 map saying which later day picks
it up, or it does not exist at all.

**The new failure mode.** Four documents becomes a target to hit rather than a ceiling not to
exceed, and days start carrying a fourth part that restates the third. What catches it: `depth`
counts documents but cannot read them, so this is an audit-pass problem, and §20.8 gains "splitting
to fill the budget" as a named failure beside "splitting without deepening".

**Revisit when** three consecutive phase gates pass with days that had to drop a load-bearing
subtopic to fit four documents. That is the plan saying the ceiling is one document too low, and it
is an amendment with its own ADR, not a quiet edit.
