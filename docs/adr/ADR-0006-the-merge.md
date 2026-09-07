# ADR-0006 — Yantra and Setu become one 182-day curriculum, and the model is met as a dependency before it is taken apart

- **Date:** 2026-09-07
- **Day:** between days 0 and 1
- **Phase:** 0
- **Status:** accepted
- **Amends:** `00_MASTER_PLAN.md` v1.1.0 → v2.0.0 (§1–§17 and §22 rewritten; §18–§21 unchanged)
- **Supersedes:** the Setu plan (`setu-fde`, v1.0.0) in its entirety
- **Related:** ADR-0001, ADR-0002, ADR-0003, ADR-0005

## Context

Two curricula existed in parallel, built on the same toolchain, by the same person, for the same
career outcome.

- **Yantra v1.1.0** — 229 days, 400 IDs, nine tracks. Production LLM engineering: transformer
  internals, tokenizers, attention, the KV cache, PEFT, preference alignment, quantization,
  distillation, retrieval, agents, LLMOps, five shipped services.
- **Setu v1.0.0** — 180 days, 181 IDs, eight tracks. The forward deployed engineer: the client
  engagement, production Python, async, FastAPI, the cloud, containers, retrieval, agents, legacy
  integration, identity, guardrails, observability, two delivered systems, the handover.

Run one after the other they cost **409 days**. That is the number that forced this decision, and
it is worse than it looks, because a large part of it is paid twice for the same understanding.

**The overlap is not incidental — it is structural.** Both plans independently reached the
conclusion that a production AI engineer needs embeddings, chunking, BM25, hybrid retrieval,
reranking, retrieval evaluation, graph retrieval, page-image retrieval, function calling, a
hand-rolled agent loop, MCP, LangGraph, checkpointing, human-in-the-loop, PII masking, guardrails,
prompt injection defence, tracing, token accounting and eval-gated CI. About **130 IDs** teach the
same material on both sides. Teaching it twice does not teach it twice as well; it teaches it once
and then bores someone for two months.

**The non-overlap is the actual argument for merging rather than choosing.** Neither plan alone
describes an employable engineer:

- Setu's stated non-goal is *training or fine-tuning models*. It treats a model as "a pinned
  dependency with a price and a rate limit." That produces someone who can deploy, secure and hand
  over an API wrapper, and who is undifferentiated from every other integrator the moment a client
  asks why the model is wrong on their domain.
- Yantra ships five services to nobody. It has no client, no KPI, no SOW, no identity model, no
  legacy integration, no handover, and its Python, cloud and container knowledge is assumed rather
  than taught. That produces someone who can fine-tune a model and cannot get it into an
  organisation.

The market pays for the join. So does the interview loop that both plans end at.

## Decision

**One plan: `00_MASTER_PLAN.md` v2.0.0. 182 days (Day 0 plus Days 1–181), 373 IDs, thirteen tracks,
twenty-nine phases, four things shipped to one client.** The `setu-fde` repository is superseded and
becomes read-only source material.

Four decisions inside that, each of which could have gone the other way.

### 1 · The client is kept, and it is Setu's

Setu fixed a client before writing code: a mid-size general insurer, forty-two thousand claims a
month, a failed vendor chatbot already in the room. Yantra had five unrelated domains — medical,
reasoning, legal, DevOps, ops tooling — chosen to exercise techniques.

The insurer wins, because **it makes Principle 5 mechanical.** "Is this concept load-bearing?" has
a real answer when there is one artifact to delete it from and see what breaks. With five unrelated
services the honest answer is always "it is load-bearing for one of them," which is not a
constraint at all.

The cost: Yantra's medical fine-tune, legal RAG and DevOps agent scenarios are gone as *scenarios*.
Every technique they carried survives, pointed at claims documents instead.

### 2 · The model is met as a dependency before it is taken apart

This is the ordering decision, and it is the one most likely to be questioned.

Setu's order: foundation → API → cloud → containers → the model, as a black box, on day 55.
Yantra's order: the model, opened up, from day 1.

Neither survives the merge. Setu never opens the box — a permanent ceiling. Yantra writes training
code on Day 15 for a reader who has not yet met a lockfile, a type hint, or a connection that must
be released when a request dies, which contradicts its own Principle 16.

**The merged order is: the client (1–5) → the language (6–29) → the model as a dependency (30–38)
→ the cloud and the pipeline (39–52) → the model taken apart (53–94).**

The argument is pedagogical and it is the reason this ADR exists rather than a changelog line.
Phase 5 generates the questions Phase 8 answers. *Why does it cost that per call? Why did the same
prompt give a different answer? Why did the JSON come back truncated at exactly that point?* A
reader who has spent nine days being billed by the token and burned by a silent parse failure meets
tokenization, sampling and the context window as answers. A reader who meets them on Day 1 meets
them as trivia, and can derive scaled dot-product attention two months before they can get a parse
to hold.

The cost, stated plainly: Days 30–38 use tokenization, sampling and the context window before
Phase 8 explains them. §20.4's no-shortcut test applies — each of those days links forward to the
part that opens the mechanism, rather than saying "for now, just accept that."

### 3 · Both budget systems are kept, because they answer different questions

Yantra had `YANTRA_PROFILE` (laptop | gpu | auto) — *what machine is this training day run on.*
Setu had Lane A ($0) and Lane B (managed) — *who is paying for the infrastructure this day needs.*

The temptation was to collapse them into one "cheap vs expensive" axis. That would be wrong: a day
can be laptop-profile and Lane B (a local student model calling a managed vector store), or
gpu-profile and Lane A (a rented box running Qdrant in Docker). They are orthogonal, so both
survive, as §4.1 and §4.2, and a day states whichever applies to it.

### 4 · The cuts are enumerated in the plan, not absorbed silently

§22.3 lists every cut with the days it saved and what it costs, including the ones that hurt. The
alternative — quietly not writing those days — would leave the reader unable to tell a decision
from an oversight, which is the same failure mode as an uncited fact.

The largest cuts: speech and Whisper (2 days, feeds nothing here), a vendor agent runtime as a
taught product (6 days, the fastest-dating material in either plan), the agent-to-agent protocol
block (5 days, compressed to one day where the question actually arises), five services collapsed
to four deliverables (~20 days), and vision internals from twelve days to two (8 days).

## Consequences

**The plan is denser: 2.05 IDs per day against Yantra's 1.75 and Setu's 1.0.** This is a real cost
and it interacts with Principle 15. A denser day is a day with *more parts*, never a day with
shorter explanations. If a day in Phases 15 or 19 will not fit its subject at the depth §20
requires, the correct response is to split it into two days and amend this plan — not to compress
the teaching.

**`setu-fde` is superseded but not deleted.** Its day map is the reference for anything §22.5 puts
back, and its Phase 2 discovery days are the source for Days 1–5 here.

**`days/day-001-what-language-model-is/` was deleted.** It was written against v1.1.0's Day 1 and
is now Day 53's subject. Day 0 stays and its `PROGRESS.md` row stands: it built the toolchain, and
the toolchain did not change. Day 0 is the only day this plan inherits.

**The `PROGRESS.md` row for the v1.1.0 Day 1 is not removed** — the ledger is append-only
(Principle 2). There is no such row: Day 1 was written but never closed, which is why this
supersession costs one deleted folder rather than a re-opened ID.

**Every generated index is stale until `granth.py index` runs.** `TRACEABILITY.md`,
`CURRICULUM_INDEX.md`, `TRACKER.md` and `WIKI.md` all describe a 400-ID, 229-day plan that no
longer exists.

## Alternatives considered

**Run both plans in sequence (409 days).** Rejected on the arithmetic: fourteen months, with about
eighty days spent re-learning retrieval, agents, security and observability. The second pass through
a subject you already know is the most expensive kind of day there is, because it feels productive.

**Choose one and abandon the other.** Rejected in both directions, for the reason in Context:
Setu alone cannot fine-tune, Yantra alone cannot deliver. Either choice produces a specialist in
half a job, and both halves are commodity on their own.

**Keep both plans and interleave them day by day.** Rejected. It breaks Principle 14's one-subject
day and makes every phase gate meaningless — a gate exists because a block of days shares a
subject, and alternating between transformer internals and OAuth flows leaves nothing that must be
true at the end of anything.

**Merge but keep the 229-day length, taking the saving as extra depth.** Genuinely defensible, and
rejected only on the stated constraint: six months. It remains the right amendment if the calendar
changes — the levers in §22.5 run in the other direction too, and the first thing to buy back is
Phases 2–4 at full Setu depth, then vision internals.
