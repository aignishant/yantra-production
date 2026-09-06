# ADR-0003 — Security identifiers sit in the phases that create the exposure, not in a security chapter

- **Date:** TODO(me)
- **Day:** before day 0
- **Phase:** 15, 19, 20
- **Status:** accepted
- **Amends:** nothing — a decision taken while drafting v1.0.0
- **Related:** ADR-0001, `docs/00_MASTER_PLAN.md` §14, Principle 13

## Context

Twelve `SEC` identifiers cover PII masking, input and output guardrails, prompt injection defence,
agent identity and secrets, policy-based access control, and sandboxed execution.

There are two places they can go. A security phase — one block, taught together, easy to schedule.
Or distributed — each identifier placed at the day that first creates the exposure it addresses.

A security chapter teaches security as a review step: something done to a system after it works.
That is how the material is usually delivered and it is why guardrails get bolted onto pipelines
that were designed without them, and why an agent gets a credential several days before anyone
asks what it can do with it.

## Decision

**No security phase. Twelve identifiers placed at the day the exposure appears.**

- `SEC-01..02` (PII masking) → phase 15, with the days that index documents.
- `SEC-03..04` (guardrails) → phase 15, with the days that start answering.
- `SEC-05..06` (prompt injection) → phase 15, immediately before project 03.
- `SEC-07..08` (identity, delegated access, secrets) → phase 19, with AgentCore Identity.
- `SEC-09..10` (policy and tool-call interception) → phase 20, before the agent gets write access.
- `SEC-11..12` (threat modelling, sandboxing) → phase 20, immediately before project 04.

**Every `SEC` day carries the attack before the defence.** A guardrail you have not got past is a
guardrail you cannot evaluate — that is the load-bearing half, and it is what makes these days
labs rather than checklists.

## Options considered

| Option | Why not |
| --- | --- |
| **A security phase after the agent phases** | Teaches security as a review step. By the time it arrives, four services exist that were designed without it, and retrofitting is the lesson nobody learns from. |
| **A security phase before the agent phases** | Worse: the material has no system to attack yet, so every day is hypothetical. A prompt injection lab with nothing to inject is a reading. |
| **Both — foundations early, application late** | Doubles the surface for no gain, and splits ownership of every term across two phases. |

## Consequences

**Better.** Principle 13 becomes structural rather than aspirational. A reader meets PII masking
while holding the indexing pipeline that leaks, and meets Cedar policies while holding an agent
that can delete things.

**Worse.** There is no single place to send someone who asks "what does this curriculum say about
security". Plan §14 exists to be that place, and it is an index rather than a chapter — a real
cost, accepted.

**New failure mode.** Distributed identifiers are easier to quietly drop when a phase runs long,
because no phase is visibly "the security one". `granth.py doctor` catches an unassigned
identifier; nothing catches a thin one except reading, which is what the audit pass is for.

**Not recommended for reversal.** Of the deviations in plan §22, this is the one to keep.
