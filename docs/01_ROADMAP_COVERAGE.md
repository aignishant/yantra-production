---
document: roadmap-coverage
plan_version: "v1.0.0"
amended: "TODO(me)"
---

# Roadmap coverage — every source module, and where it lands

This repository was planned from a 24-module, 5-project source roadmap. **This document is the
audit trail for that translation, and nothing else.** It is not a second plan: where this table and
`00_MASTER_PLAN.md` §17 disagree, **the plan is right and this document is stale.**

Two questions it exists to answer:

1. *Did anything get dropped?* Every module has a row. A module with no identifiers assigned would
   be a hole, and it would be visible here before it was visible anywhere else.
2. *Why is the order different?* The source roadmap is ordered by subject. This plan is ordered by
   dependency (plan Principle 4), which moves several modules. Every move is listed in §3 with its
   reason.

---

## 1 · Module coverage

| Source module | Lands in | Days | Identifiers | Count |
| --- | --- | --- | --- | --- |
| 01 · Transformer architecture & tokenization foundations | Phase 1 | Days 1–12 | `TF-01`…`TF-24` | 24 |
| 02 · Fine-tuning transformer architectures in practice | Phase 2 | Days 13–18 | `TF-25`…`TF-35` | 11 |
| 03 · Inference optimization, attention variants & scaling laws | Phase 3, 4 | Days 19–30 | `TF-36`…`TF-59` | 24 |
| 04 · LLM fine-tuning lifecycle & pre-training foundations | Phase 5 | Days 34–39 | `FT-01`…`FT-10` | 10 |
| 05 · Data preparation & synthetic dataset generation | Phase 5 | Days 40–45 | `FT-11`…`FT-24` | 14 |
| 06 · SFT, parameter-efficient methods & preference alignment | Phase 6 | Days 46–58 | `FT-25`…`FT-48` | 24 |
| 07 · Evaluation, quantization, deployment & fine-tuning tooling | Phase 7 | Days 59–69 | `FT-49`…`FT-68` | 20 |
| 08 · Mixture of Experts (MoE) architecture | Phase 4 | Days 31–33 | `TF-60`…`TF-66` | 7 |
| 09 · Reasoning models, chain-of-thought & RL-only training | Phase 9 | Days 78–82 | `FT-69`…`FT-76` | 8 |
| 10 · Small Language Models & knowledge distillation | Phase 9 | Days 83–88 | `FT-77`…`FT-90` | 14 |
| 11 · Vision foundations: from CNNs to Vision Transformers | Phase 11 | Days 96–103 | `VIS-01`…`VIS-13` | 13 |
| 12 · Visual Language Models (VLMs) | Phase 11 | Days 104–105 | `VIS-14`…`VIS-18` | 5 |
| 13 · Speech-to-text models & fine-tuning Whisper | Phase 11 | Days 106–107 | `VIS-19`…`VIS-24` | 6 |
| 14 · Embedding models: taxonomy, Matryoshka & fine-tuning | Phase 13 | Days 115–120 | `RAG-01`…`RAG-12` | 12 |
| 15 · LangChain for RAG: ecosystem, patterns & production | Phase 13 | Days 121–126 | `AGT-01`…`AGT-12` | 12 |
| 16 · Foundations of RAG: vanilla, embeddings, chunking & retrieval | Phase 14 | Days 127–132 | `RAG-13`…`RAG-20` | 8 |
| 17 · Advanced RAG: query transformations, rerankers & adaptive retrieval | Phase 14 | Days 133–137 | `RAG-21`…`RAG-32` | 12 |
| 18 · Vector quantization, multimodal RAG & emerging patterns | Phase 15 | Days 138–147 | `RAG-33`…`RAG-46` · `SEC-01`…`SEC-06` | 20 |
| 19 · Agent foundations: structured outputs, function calling & MCP | Phase 17 | Days 157–170 | `AGT-13`…`AGT-37` | 25 |
| 20 · LangGraph: stateful, multi-agent & human-in-the-loop workflows | Phase 18 | Days 171–179 | `AGT-38`…`AGT-54` | 17 |
| 21 · Production agents: observability, A2A & Bedrock AgentCore | Phase 19, 20 | Days 180–197 | `AGT-55`…`AGT-82` · `SEC-07`…`SEC-12` | 34 |
| 22 · Prompt engineering: structure, techniques & refinement | Phase 12 | Days 108–113 | `CTX-01`…`CTX-10` | 10 |
| 23 · Context engineering: memory, pruning & retrieval-augmented context | Phase 12 | Day 114 | `CTX-11`…`CTX-14` | 4 |
| 24 · Harness engineering: evaluation, benchmarking & agent CI/CD | Phase 22 | Days 206–216 | `OPS-01`…`OPS-20` | 20 |
| Project 01 · MedScript AI | Phase 8 | Days 70–77 | `PRJ-01`…`PRJ-08` | 8 |
| Project 02 · EdgeReason | Phase 10 | Days 89–95 | `PRJ-09`…`PRJ-15` | 7 |
| Project 03 · LexisGraph | Phase 16 | Days 148–156 | `PRJ-16`…`PRJ-24` | 9 |
| Project 04 · AutoOps | Phase 21 | Days 198–205 | `PRJ-25`…`PRJ-32` | 8 |
| Project 05 · ShipLLM | Phase 23 | Days 217–224 | `PRJ-33`…`PRJ-40` · `OPS-21`…`OPS-22` | 10 |

**396 of 400 identifiers fall inside a day range belonging to a named source module or project.**
The remaining four are the capstone (`PRJ-41`…`PRJ-44`, days 225–228), which is a defence rather
than a module: the whole-system trace, the cost model, the public audit, and the answers the
repository invites.

Note that the twelve `SEC` identifiers *are* counted above, because ADR-0003 places each one inside
the phase that creates its exposure — so they land within the day ranges of modules 18 and 21 even
though the roadmap treats them as sub-topics rather than units.

**Nothing in the roadmap is unassigned.** Every module above has at least one day.

---

## 2 · Where the plan adds material the roadmap does not enumerate

The roadmap lists topics. A curriculum built to the depth contract needs a few things it does not
list, because the contract requires a check that can go red and a failure that can be caused.

| Added | Where | Why |
| --- | --- | --- |
| Tokenizer pathologies (`TF-07`) | Day 5 | Tokenizer choices surface later as unexplained failures — digits a fine-tune will not learn, chunk boundaries that split a clause. |
| The training loop that tells the truth (`TF-35`) | Day 18 | Loss curves, seeds and determinism. Without it, every later "this improved things" claim is unfalsifiable. |
| Loss masking as its own day (`FT-13`, `FT-14`) | Day 41 | The most common silent fine-tuning bug: trains without error, answers badly, invisible in a loss curve. |
| Model collapse and data poisoning (`FT-23`, `FT-24`) | Day 45 | The roadmap names both as risks inside module 05; they are the failure day for the whole synthetic-data phase. |
| Blue/green and auto-rollback (`OPS-21`, `OPS-22`) | Days 223–224 | Named in project 05's tech stack but not as teachable units. They are the difference between a pipeline and a deployment. |
| The capstone (`PRJ-41`…`PRJ-44`) | Days 225–228 | Not a sixth project — the defence. The whole-system trace, the cost model, the public audit. |

---

## 3 · Where the order differs, and why

| Moved | Roadmap position | Plan position | Reason |
| --- | --- | --- | --- |
| Module 08 (MoE) | After module 07 | Phase 4, days 31–33 | Its subject is a scaling decision, so it follows the scaling-law days (`TF-56`…`TF-59`) rather than the serving days. |
| Modules 22–23 (prompt & context) | After the agent modules | Phase 12, days 108–114 | Retrieval and agent days need the vocabulary. ADR-0002. |
| Project 01 | After module 24 | Phase 8, days 70–77 | Its prerequisites close at day 69. Deferring it means the fine-tuning track is never exercised before the retrieval track begins. |
| Project 02 | After module 24 | Phase 10, days 89–95 | Same reason: distillation is taught days 83–88. |
| Project 03 | After module 24 | Phase 16, days 148–156 | Same reason: the retrieval track closes at day 147. |
| Project 04 | After module 24 | Phase 21, days 198–205 | Same reason: the agent track closes at day 197. |
| Security topics | Inside modules 18 and 21 | Phases 15, 19, 20 | Placed at the day that creates each exposure. ADR-0003. |

**Project 05 is not moved — it is dissolved.** The roadmap's fifth project wraps the other four
after they exist. This plan makes it the repository they are born in, so phase 8 already writes a
Dockerfile. Plan §22.3 and ADR-0001.

---

## 4 · What is deliberately not covered

Listed so that a reader can tell a decision from an omission. Full reasoning in plan §1.1.

| Not covered | Why |
| --- | --- |
| Pre-training a foundation model from scratch | The compute is not available and the skill does not transfer. The scaling laws that decide the size are taught; the run is not. |
| Building a vector database, serving engine or inference kernel | PagedAttention and Flash Attention are read closely enough to explain; the implementations are used. |
| Frontier-scale RL for reasoning | The recipe is taught; the run is a compute problem, not a curriculum problem. |
| A front end for any service | Every service ends at a traced HTTP API. |
| Multi-cloud portability | One cloud done properly. |
