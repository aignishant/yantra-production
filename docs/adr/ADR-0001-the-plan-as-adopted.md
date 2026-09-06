# ADR-0001 — The plan is adopted as a 229-day, nine-track, single-system curriculum

- **Date:** TODO(me) — date this the day you accept the plan
- **Day:** before day 0
- **Phase:** —
- **Status:** accepted
- **Amends:** nothing — this is the founding record
- **Related:** `docs/00_MASTER_PLAN.md` v1.0.0, ADR-0002, ADR-0003, ADR-0004

## Context

This repository teaches production LLM engineering — transformer internals, fine-tuning and
alignment, vision and speech, retrieval, agents and protocols, and the delivery shell that ships
all of it — over 229 days, from a 24-module, 5-project source roadmap.

It exists because the obvious alternatives do not work:

- **Following the course as delivered** produces something that runs and understanding that
  evaporates the moment the inputs change. There is no artifact to defend and no record of why
  anything is as it is.
- **Reading documentation** covers the surface in the order the documentation was written, which is
  the vendor's order and not a learner's. Nothing forces the ideas to connect.
- **Building a project with no plan** teaches whatever the project happened to need, leaves the
  gaps invisible, and cannot tell a thin subject from a missing one.

The plan answers all three: a fixed day-to-concept map so gaps are visible; one system so every
concept is load-bearing; and a depth contract so a subject is either covered properly or
mechanically flagged as not covered at all.

The decisions below were taken together, at the start, because each is expensive to change once
days exist.

## Decision

**Nine tracks, 400 concept identifiers, 229 days, 25 phases, one system.**

- **Tracks** are `TF` (transformer internals), `FT` (fine-tuning and compression), `VIS` (vision
  and speech), `RAG` (embeddings and retrieval), `AGT` (agents and protocols), `CTX` (prompt and
  context engineering), `OPS` (LLMOps and CI/CD), `SEC` (safety and security), `PRJ` (the shipped
  services). Prefixes name a subject, not a module number, so a track can absorb a roadmap change
  without renumbering.
- **Every identifier is assigned to exactly one day**, and `granth.py doctor` proves it. An
  identifier in two days is a duplicate lesson; an identifier in none is a hole.
- **The five roadmap projects are one system, not five deliverables** (plan §3). The fifth project
  — the eval-gated CI shell — is the repository the other four live inside from the day each is
  born. The load-bearing half of this decision is that phase 8 already writes a Dockerfile and a
  smoke test: retrofitting CI across four services written without it is a week that teaches
  nothing.
- **A day is a unit of subject, not of time** (plan Principle 15). No document carries a duration.
  The calendar consequence is stated openly in plan §22.4 rather than hidden by shortening days.

## Options considered

| Option | Why not |
| --- | --- |
| **Follow the roadmap's module order and day count as given** | The roadmap is sequenced for delivery, not for dependency. Taken literally it teaches prompt engineering after the agent modules that need it, and treats five projects as five endpoints. |
| **Fewer, larger identifiers (~200) over ~120 days** | Matches the roadmap's stated pace, but at roughly 3.3 concepts a day the depth contract stops being satisfiable — days become surveys, which is the failure the contract exists to prevent. |
| **More, smaller identifiers (~600) over ~300 days** | Splits below the one-idea boundary. Identifiers stop naming concepts and start naming paragraphs, and the traceability report stops being readable. |
| **Track prefixes mirroring the roadmap's module numbers** | Couples the identifier scheme to a document that will be revised. A renumbered module would renumber the curriculum. |

## Consequences

**Better.** Gaps are visible before they are reached. Every concept has one home. The five projects
compose instead of stacking. The plan can absorb a roadmap revision by amending a track rather than
renumbering everything.

**Worse.** 229 days is longer than the roadmap's stated 7 months at any realistic pace, and the gap
is real (plan §22.4). Nine tracks is more than a reader can hold in their head at once, so the
per-track sections (plan §7–15) have to carry the arc that a shorter scheme would not need.

**New failure mode.** A day map this large invites quiet reordering when a day proves hard.
`granth.py brief N` exits non-zero when N is not next, which is what catches it — and reordering
then costs an ADR, which is the point.

**Revisit if:** the source roadmap is revised structurally, or the calendar proves binding, in
which case plan §22.4 lists the scope levers in the order they cost least. Cut scope, never depth.
