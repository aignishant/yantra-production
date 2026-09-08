---
name: day-yantra
description: Generate the hub, the parts/ sub-documents, any source parts, the lab scaffold and the checklist for a given day of the Yantra plan
argument-hint: [day-number]
---

# Generate Day $ARGUMENTS of the Yantra plan (v2.1.0 — hub + `parts/` + `sources/`)

> **Read `docs/00_MASTER_PLAN.md` §20 before writing a single line.** It is the depth contract this
> skill implements. **This skill is the procedure; §20 is the standard.** Where they appear to
> disagree, §20 wins and this skill is amended.

## The four commitments (§20.1 — everything below follows from these)

1. **One idea per document.** If it needs "also" to introduce its second half, it is two documents.
2. **No clocks.** Never write a time estimate, a duration, an "estimated hours" field, or a pace —
   not in frontmatter, not in prose, not in the checklist. **Never trim an explanation because the
   day is getting long.**
3. **Zero to production, in one document.** Open where a reader who has never heard of the idea can
   stand. End where a professional stands: the real-system version, what breaks at scale or under
   concurrency, what a senior reviewer says, what an interviewer probes.
4. **A day is finishable — three documents, four at the outside** (§20.10), `parts/` and `sources/`
   counted together. This is the commitment that cuts, and it is the one this skill gets wrong most
   easily, because the other three all pull toward writing more.

**Commitments 2 and 4 together leave exactly one lever.** A day with more subtopics than budget
**cuts a subtopic and says so in the hub's §2 map**, naming the later day that picks it up. It does
not write six thin parts, and it does not write four that each carry an idea and a half. If the cut
would be load-bearing, the day is too big for the plan: stop, and split it in §17 with an ADR.

---

## Step 1 — gather

1. Run `python granth.py brief $ARGUMENTS`. **If it exits non-zero, stop and say so.** It means this day is not
   next, and a day written early is a day whose prerequisites were never taught. Reordering needs
   an ADR (plan §18.1).
2. Read the plan: **§2** (principles), **§4** (budget), **§5** (verification rules), **§17** (the
   day map — the authoritative ID list for day $ARGUMENTS), **§20** (the depth contract), **§21**
   (the style guide). Collect every ID slotted to this day, the phase theme, and the gate that
   phase feeds.
3. Read `docs/PROGRESS.md`. **Confirm $ARGUMENTS is exactly one more than the last row.** If not,
   stop.
4. Read `docs/TRACEABILITY.md`. Any open ID from a completed phase is a bug — report it, do not
   paper over it.
5. Read the previous day's `LESSON.md` and `CHECKLIST.md`. If the checklist has unticked boxes,
   warn and ask before proceeding. **Build on the code earlier days told the learner to write —
   never duplicate it, never silently rewrite it.**
6. Read `docs/GLOSSARY.md`. Every term already defined gets a **link back**, not a redefinition.
   Every new term this day introduces gets a row at the end.
7. Read `docs/SOURCES.md`. **A source is taught once in the whole curriculum.** If a paper this day
   leans on already has a source part, cite and link it; do not write a second one.

---

## Step 2 — verify reality before you write (Principles 7, 8, 12)

Do this **before** any prose, because what you find can change the day.

1. **Every version this day pins** — look it up live. Record the command and the result. Anything
   you cannot verify becomes a `TODO` containing **the exact lookup command**, never a guess.
2. **Every API surface this day uses** — fetch the current documentation page and note its URL and
   today's date, for the inline *"Verified against `<url>` on YYYY-MM-DD"* line.
3. **Every citation** — look it up live. Copy the title from the record. **Cite by title and
   identifier, never by author.** A remembered citation is an invented citation.
4. **Every dataset or checkpoint** — check the licence before the download, and write the
   `PROVENANCE.md` row first.
5. **If reality has moved** — a renamed API, a superseded spec, a model that lost its free tier —
   **stop.** Amend the plan and `CHANGELOG_PLAN.md` first, then come back. Never silently adapt the
   day around it.

---

## Step 3 — plan the split, and show it before writing prose

1. Decide the **sections**: one per ID, or one per pipeline stage, or one per component in build
   order (§20.7). State in one line what each section means *for this day* — that line goes in the
   hub's §2 map, and an unexplained numbering is a bug.
2. Decide the **parts** inside each section. Apply the one-idea test to each: can it be read alone,
   understood without scrolling past a different subtopic, and explained back out loud?
3. **Count the documents, and cut to four.** `parts/` and `sources/` together, three preferred
   (§20.10). List every subtopic the idea boundaries gave you, then say out loud which ones do not
   make it and why. The ones cut get a line in the hub's §2 map naming the later day that picks
   them up. **Never merge two ideas into one part to fit** — that breaks the one-idea test the step
   above just applied. **Never write a fourth part to fill the budget** — the ceiling is a limit,
   not a target.
4. Decide which part is **the deliberate failure** (§20.7). Every day has one. Name what will
   break and what error the reader will see.
5. Decide the **`level` ladder**: the day should climb `foundation → working → production`. With
   three parts that is usually one rung each.
6. Decide the **sources**, if any. One document per paper, in `sources/`, read after the parts —
   **and it spends one of the four documents**, so a day with a source part gets three in `parts/`.
7. Pick **one metaphor family for the whole day** — check the day's other parts and the hub's §1
   before choosing. Two parts reaching for the same setting read as one idea repeated.

**Print this plan and stop.** The learner reads it before you write — the document count, and the
list of subtopics you are cutting. If it looks thin, or if the cuts look wrong, that conversation
costs one message now and a rewritten day later.

---

## Step 4 — write the parts

Path: `days/day-NNN-<day-slug>/parts/<NN>-<section-slug>/<section>.<sub>-<slug>.md`, day number
zero-padded to three digits.

Each part carries all ten sections **in order** (§20.4). Three are conditional: *The source behind
it*, *Line by line*, *The source in one demo*.

**How every sentence is written (§21.6).** One idea per sentence, around twenty words. Grammatical,
finished sentences — subject, verb, object, no note-form fragments. Everyday word first and the
precise term second, in the same sentence. Second person, active voice, present tense. **And the
worked example before the general statement, every time** — real input, real output, real numbers,
then what is true in general. A paragraph describing the shape of a response teaches less than three
lines of the actual JSON. Simple English, never a simple idea.

**The sections that get written badly, and what good looks like:**

- **The idea in plain language** is **one section with one opening** — the old *story* heading was
  merged into it by ADR-0007, because two headings meant the scene got told, abandoned, and the idea
  restarted from cold underneath it. Three moves, no headings between them:
  **(a) the scene, first**, before any abstraction and with **no jargon at all** — a courier who
  cannot find the flat number, a mechanic checking the same six things on every car, a 3am page
  about a queue that will not drain. Not a nautical chart, not a theatre programme. **Test: could
  the reader have been standing in this scene?** If they must first be told what the setting *is*,
  the analogy is carrying the explanation instead of hooking it. It must be **load-bearing** — the
  scene holds the actual failure the part teaches, and every later section that reaches back for it
  must still fit.
  **(b) the idea, named inside that scene** rather than re-introduced under it. Every term defined
  on first use, including terms from earlier days, with a link to the part that introduced them.
  **(c) one worked example** — the smallest real case that is still true.
- **Why Yantra needs it** names **the concrete later day that breaks without this**, with a link.
  Never "this is important".
- **The mechanism** skips nothing as obvious. Mermaid whenever the concept is spatial, sequential,
  or a state machine.
- **Line by line** goes **immediately after each code block**, as a `**Line by line:**` list, and
  explains *why it is that line and not another*. Error output, bare check commands and diagrams
  are exempt. **An unexplained line is a bug in the document.**
- **When it breaks** carries **real, pasted error text** — the traceback, the CUDA OOM, the HTTP
  status, the JSON-RPC error body. **If you have not seen the error, cause it.** Never reconstruct
  one from memory: a reader who is taught to expect a message they will never see has been taught
  to distrust the document.
- **In production** is the section that gets dropped, and dropping it halves the document. It needs
  the specific: the version a professional writes instead of the teaching version, what degrades at
  scale or under concurrency, the review comment, the interview question. **Not optional.**
- **Check yourself** is one command the reader can run *right now*, plus one question they must
  answer **out loud** without scrolling up.

**Four Yantra-specific rules on top (§20.4.1):**

1. Name the documentation page checked today, inline, next to any library symbol.
2. State the verified version, or leave a `TODO` with the exact lookup command.
3. **Any number is produced by a command shown in the document, on a machine the document names.**
   A speedup with no benchmark is a rumour with a number attached.
4. State the licence of any dataset or checkpoint, with the `PROVENANCE.md` row written first.

**Never solve a `TODO(me)`.** Those are the learner's. That is the difference between a curriculum
and a tutorial.

---

## Step 5 — write the source parts, if any

`days/day-NNN-<slug>/sources/NN-<source-slug>.md`, numbered from `01` in reading order, beside
`parts/` and not inside it.

A source part carries the same ten sections. Section 5 never fires. Section 8 — **The source in
one demo** — is **required** and is the section easiest to get wrong:

1. **Only the source's feature.** A small project whose *entire reason to exist* is the idea. The
   test is subtractive: if a file could be deleted and the claim still lands, delete it. Two or
   three files is normal.
2. **End to end and actually runnable.** One command, stated. Its real output, pasted. **If it
   needs a GPU or a live model and has not been run, the output block is a `TODO(me)` naming the
   exact command — never an invented transcript.**
3. **An ablation switch** — one flag that turns the contribution off, with **both runs' output**.
   A demo that cannot be switched off has proved that code ran, not that this idea did something.
4. **Costed** — free tier, local, or rented, with the number.

On a source part the sections mean: *the scene* that opens the idea = the problem the field had **before this document
existed**; *when it breaks* = where the claim **does not hold** (the assumptions, the benchmark, the
scale it was never tried at); *in production* = **what survived and what did not**, and what
replaced the dropped half. A source part with no limits section has taught a press release.

---

## Step 6 — write the hub (`LESSON.md`)

The hub **orients and assembles; it never teaches.** No `Line by line:` walkthrough lives here. All
thirteen elements of §20.5, in order — and note three that are specific to this plan:

- **§4 Build brief — spell the code out to the signature.** For every file the day asks for: the
  exact path, then a code block carrying **every function and class the learner must write, with its
  full type-hinted signature and a one-line docstring saying what it returns and what it raises** —
  and a body that is nothing but `TODO(me): <what this must do>`. Then the one command that runs it.
  The learner must be able to read this section alone and know exactly what to implement, without
  going back through a part to reverse-engineer an interface the next day will call.
  **Never write a body.** Naming the interface is not solving the exercise; writing the body is.

- **§6 Budget** — model calls per provider in RPM/RPD, GPU hours, and money. `0` is an
  answer; state it. If the day rents a GPU, say which and roughly for what, and what the cheaper
  path costs in capability.
  **If the day touches an accelerator, the budget carries BOTH profiles** (plan §4.1 rule 4): a
  `YANTRA_PROFILE=laptop` row naming the base model and the scale it runs at and what is lost in
  capability, and a `YANTRA_PROFILE=gpu` row naming the accelerator and roughly what it costs.
  The laptop path is a smaller true version of the day — same mechanism, same code path, same
  check going red — never a mock (rule 6). A day with no honest laptop path says so in a
  `TODO(me)` instead of inventing one. Every measured number carries its profile (rule 5); the
  day imports `resolve()` from `yantra/hardware.py` rather than calling
  `torch.cuda.is_available()` itself. See `docs/HARDWARE.md`.
- **§11 Ledger & commit** — the verbatim rows the learner pastes: `PROGRESS.md`, plus any `PINS.md`,
  `SOURCES.md`, `GLOSSARY.md` and `PROVENANCE.md` rows, and the commit message
  `day NNN: <title> — closes <IDs>`. **The hub ends with these.** Ritual is the point: the
  repository is the memory, not the chat.

---

## Step 7 — the checklist (`CHECKLIST.md`)

The definition of done, as tickable boxes. Every part read. Every `Check yourself` run. The build
brief's `TODO(me)`s done. **The deliberate failure caused and watched go red, then fixed** — a
check nobody has seen fail has verified nothing. The ledger rows pasted. No box mentions a duration.

---

## Step 8 — verify

```bash
python granth.py depth NNN     # the contract
python granth.py index         # regenerate the derived documents
python granth.py check         # the whole gate
```

**Never argue with a depth failure.** Fix the day. Then hand back to the learner — `granth.py done NNN`
is theirs to run, and it will refuse until the checklist is ticked and the `PROGRESS.md` row is
pasted.

---

## Always

- **Stop rather than invent.** A `TODO` with the exact command beats a plausible guess, every time,
  in every section.
- **Stop rather than reorder.** If the day cannot be written in the order the plan assigns, that is
  an ADR, not an improvisation.
- **Report thinness honestly.** If a day's assigned IDs do not fill a day, or fill three, say so
  before writing. That is an amendment, and amendments are cheap before the folders exist.
