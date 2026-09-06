# ADR-0002 — Prompt and context engineering are taught before retrieval and agents

- **Date:** TODO(me)
- **Day:** before day 0
- **Phase:** 12
- **Status:** accepted
- **Amends:** nothing — a decision taken while drafting v1.0.0
- **Related:** ADR-0001, `docs/00_MASTER_PLAN.md` §12, §22.1

## Context

The source roadmap places prompt engineering and context engineering in modules 22–23, after the
agent modules and immediately before the harness module.

Read in that order, every retrieval day and every agent day has to reach for vocabulary the
curriculum has not yet taught. "Context construction" is the whole subject of the chunking days.
"Memory architecture" is the whole subject of the LangGraph persistence days. Taught afterwards,
those days either gesture at the ideas or define them in passing — and a term defined in passing is
a term defined twice, badly, in two places.

The compounding cost is small per day and large across the plan: roughly thirty days in phases
13–19 would each carry a paragraph explaining something phase 12 could have taught once.

## Decision

**The `CTX` track sits at phase 12, days 108–114, between the vision phases and the retrieval
phases.**

The load-bearing half is that `CTX` closes no identifier any other track depends on structurally —
it is a vocabulary track. That is what makes the move safe, and it is why this was the one
reordering worth making rather than one of several.

Day 112's prompt robustness test is deliberately built as an artifact rather than an exercise: it
becomes the golden baseline that the prompt regression stage checks against on day 218.

## Options considered

| Option | Why not |
| --- | --- |
| **Keep the roadmap order (modules 22–23 late)** | Thirty later days each carry an unowned definition. The terms end up defined in passing, in several places, differently. |
| **Split the track — prompt basics early, context engineering late** | Splits a track across 100 days for no gain. Context-window anatomy is exactly what the chunking days need; deferring the half that matters keeps the problem. |
| **Fold the material into the days that need it** | This is the status quo restated. It is how a curriculum ends up with no owner for a term, which the glossary ledger then cannot enforce. |

## Consequences

**Better.** Retrieval days can say "context construction" and link to the part that owns it. Agent
days can say "episodic memory" the same way. `docs/GLOSSARY.md` gets one row per term instead of
several.

**Worse.** Phase 12 arrives before the reader has built anything that badly needs prompt
robustness, so its motivation is thinner than it would be at module 22. The days must carry that
weight themselves by pointing forward — plan §20.4 section 5 ("why Yantra needs it") is doing real
work in this phase and must name the specific later day.

**Reversible.** Move phase 12 to sit between phases 22 and 23. It touches no other phase's
identifiers, which is the whole reason this was the safe move.
