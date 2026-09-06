---
plan: yantra
version: "v1.1.0"
supersedes: none
source_roadmap: "Production LLM Engineering — RAG, Agents & Fine-Tuning V1.0"
tracks: 9
ids: 400
days: 229
phases: 25
doc_architecture: "hub + parts/ + sources/ (see §20)"
generated: "TODO(me): date this file the day you accept it"
---

# 🔧 MASTER PLAN v1.1.0 — Project **Yantra**

## Production LLM Engineering — **fine-tuning · retrieval · agents · LLMOps**

> **Yantra** (यन्त्र) is an instrument assembled from parts that only work together. That is what
> this curriculum builds: not five demos, but one system whose fine-tuned model, distilled model,
> retrieval service and agent fleet all ship through the same gate.
>
> 📌 **Purpose:** the single source of truth. Every other document in this repository points back
> here. Where anything disagrees with this file, this file is wrong or the other document is —
> resolve it with an amendment, never by ignoring one of them.

---

## 📑 Table of Contents

| §  | Section |
| --- | --- |
| 1  | 🎬 The vision — one system, nine threads |
| 2  | 🧭 Core principles — rules we never break |
| 3  | 🏗️ The product — what Yantra actually is |
| 4  | 💸 Budget & infrastructure policy — **§4.1 is the hardware profile** |
| 5  | ⚙️ Baseline & the verification rules |
| 6  | 🧶 The nine tracks & the ID scheme |
| 7–15 | The tracks, one section each |
| 16 | 🗺️ The 25 phases |
| 17 | 🗓️ The 229-day map |
| 18 | 🚦 Phase gates & the freshness check |
| 19 | 📒 Ledgers & traceability |
| **20** | **📐 The depth contract — how a day is written** |
| 21 | ✍️ The style guide |
| 22 | 🔀 Deviations from the source roadmap |

---

## 1 · 🎬 The vision — one system, nine threads

By Day 228 you will have **fine-tuned, distilled, retrieved, orchestrated, secured, evaluated and
deployed** a production LLM system, and you will be able to defend every decision inside it. The
goal is a demonstrably competent and hireable production LLM engineer, with a public repository as
the proof.

Three commitments shape everything below.

1. **One system, not five demos.** The source roadmap ships five projects. This plan treats the
   fifth — the eval-gated CI/CD shell — as the thing the other four live inside. A fine-tuned
   medical model that is not behind the gate is homework; the same model deployed blue/green with
   an auto-rollback alarm is a service. Every concept lands as a change to Yantra.
2. **The repository is the memory, not the chat.** Ledgers and day documents mean any capable
   agent — this session, a different model next year, or a person — can pick up exactly where the
   last one stopped, and can see what went wrong as well as what worked.
3. **Reality outranks the plan.** Serving engines, adapter formats, agent protocols and provider
   free tiers all move faster than this document. The freshness check (§18) and the amend-first
   rule (Principle 12) exist because that will keep happening.

### 1.1 Stated non-goals — decisions, not blind spots

| Excluded | Why |
| --- | --- |
| Pre-training a foundation model from scratch | The compute is not available and the skill does not transfer. TF-56..59 teach the scaling laws that decide the size; FT-07 teaches continued pre-training, which is the part you will actually do. |
| Building a vector database, a serving engine or an inference kernel | You will read PagedAttention and Flash Attention closely enough to explain them (TF-42, TF-51) and then use the implementations, because that is what production does. |
| Training a frontier reasoning model with RL at scale | FT-72..76 teaches the recipe and R1-Zero's result; the run itself is a compute problem, not a curriculum problem. |
| A front-end for any of the five services | Every service ends at an HTTP API with a traced call. A UI teaches nothing this plan is about. |
| Multi-cloud portability | One cloud, done properly, beats three done shallowly. The deployment track is AWS because the source roadmap's agent runtime is. |

---

## 2 · 🧭 Core principles — rules we never break

1. **Doc-first.** The day document is written before any code; the code follows the doc.
2. **One day, one commit.** Traceable, append-only history.
3. **Simple language and a concrete example, always.** A concept that cannot be explained plainly
   with an example is a concept that is not yet understood. §21 enforces this.
4. **Build first, adopt after.** Hand-roll the mechanism once — attention, the KV cache, the tool
   executor loop, KL divergence, the RRF fusion — *then* reach for the framework, so the framework
   is a convenience and never a mystery. This is why Day 13 writes attention before Day 27 uses
   vLLM, and why Day 165 writes an executor loop before Day 171 uses LangGraph.
5. **Every concept is load-bearing.** If removing it would not break Yantra, it does not get a day.
6. **Verify the whole system after every step.** Each day ends with the full check suite green, not
   just today's snippet.
7. **Never invent a fact.** Versions, model strings, API surfaces, benchmark numbers and citations
   are looked up **live on the day they are used**, with a dated ledger row. A lookup that fails
   leaves a `TODO` containing the exact command — never a guess. A remembered citation is an
   invented citation.
8. **Measure, then claim.** No day asserts a speedup, a quality gain or a cost saving it has not
   measured on its own machine. "Roughly 2× faster" with no benchmark is a rumour with a number
   attached.
9. **Secrets never touch git.** `.env` and `.gitignore` exist before the first key does. The
   repository goes public at the capstone, so the discipline is real.
10. **Fail honestly.** Errors surface, escalate and are logged. Never fabricate an output to cover
    a failed run — this applies to the writer of the day as much as to the agents being built.
11. **Evals are tests.** A behaviour change without a green evalset does not merge. Every day ends
    with at least one check that can go **red**.
12. **If reality changes, the plan is amended first.** A renamed API, a superseded spec, a provider
    that dropped its free tier → amend the plan and log it in `docs/CHANGELOG_PLAN.md`, *then*
    continue. Days are never silently patched.
13. **Blast radius before capability.** Every new power — code execution, browsing, a write to a
    production system, a payment — arrives together with its containment story. This is why SEC IDs
    sit inside the agent phases rather than in a chapter at the end.
14. **Depth over density.** A day is a hub plus one document per subtopic (§20), never one long
    page. A wall of text is not depth; it is depth's disguise.
15. **A day is a unit of subject, not a unit of time.** No document carries a duration, an
    "estimated hours" field, or a suggested pace. A topic is finished when it is understood — in
    one sitting or in five. **Nothing is ever trimmed to fit a clock**; a day that is running long
    gets another part, not a shorter explanation.
16. **Assume no prior knowledge, finish at production.** Every subtopic opens where a reader who
    has never met the idea can stand, defines its jargon on first use — including jargon from
    earlier days, with a link back — and ends where a professional stands: what breaks at scale,
    what a senior reviewer says, what an interviewer probes.

> Principles 14–16 are made concrete by **§20, the depth contract**, and are enforced mechanically
> by the depth checker and by reading.

---

## 3 · 🏗️ The product — what Yantra actually is

One repository, one CI pipeline, four services behind it.

| Service | What it is | Phase it is born in | The track that feeds it |
| --- | --- | --- | --- |
| `yantra-med` | A domain-adapted clinical assistant: QLoRA SFT then DPO on Llama-3.1-8B-Instruct, served by vLLM with hot-swappable adapters per request | 8 | `FT` |
| `yantra-edge` | A distilled reasoning model quantized to GGUF, answering on CPU at a fraction of the teacher's serving cost | 10 | `FT` |
| `yantra-lex` | A legal document intelligence service: ColPali page-image retrieval, Neo4j graph, BM25, RRF fusion, cross-encoder reranking, RAGAS-gated | 16 | `RAG`, `VIS`, `SEC` |
| `yantra-ops` | A DevOps multi-agent system: a LangGraph supervisor delegating to MCP-backed sub-agents, with A2A peer delegation and human approval on every write | 21 | `AGT`, `SEC` |

And the shell they all live in:

| `yantra-ship` | The LLMOps layer: golden test suites, eval-gated CI stages, cost and latency regression guards, multi-stage container builds, blue/green deploys with auto-rollback | 23 | `OPS` |

**The system-level test is one sentence, and it is what the capstone defends:** a prompt change in
any one of the four services must be blocked by the pipeline when it makes that service worse, and
must reach a live endpoint when it does not — without a human deciding which of those two happened.

Everything in this plan is either a component of that sentence or the understanding required to
build the component. §1.1 lists what that excludes.

---

## 4 · 💸 Budget & infrastructure policy

This is the section most likely to be wrong for **your** situation, and it is the one to correct
first. The source roadmap assumes access to a mid-tier GPU and an AWS account. This plan states
what each phase actually needs so the cost is visible before it is incurred, never discovered
halfway through a training run.

| Resource | Where it first becomes non-optional | Substitution if you do not have it |
| --- | --- | --- |
| A GPU with ≥16 GB VRAM | Phase 2 (Day 15, first real fine-tune) | `YANTRA_PROFILE=laptop` runs the day at CPU scale (§4.1). Colab / Kaggle free tiers carry Phases 1–4 comfortably; rent by the hour from Phase 6 |
| A GPU with ≥24 GB VRAM | Phase 6 (Day 49, QLoRA on an 8B base) | **No honest laptop path** (§4.1). Rent hourly. Unsloth (FT-67) exists precisely to lower this floor — the day teaches the number, not the vibe |
| An AWS account | Phase 8 (Day 77, the first SageMaker endpoint) | Phases 1–7 need none. From Phase 8, keep a spend alarm before the first deploy, not after |
| A managed vector DB | Phase 16 (Day 149, Qdrant) | Qdrant, Elasticsearch and Neo4j all run in Docker locally; the plan assumes local until the project phase |
| Paid frontier API access | Phase 5 (Day 44, judge-scored synthetic data) | Free tiers with rate-limit handling. Any day that calls a model states its request budget in the hub's §6 |

**Three rules follow from this table and are binding:**

1. **Every hub declares a request budget** (§20.5, hub section 6): model calls, per provider, in
   requests per minute and per day. `0` is a valid answer and must be stated.
2. **Every day that spends money says so, in the hub, before the first command.** A day that will
   rent a GPU says which GPU, for roughly what, and what the cheaper path costs in capability.
3. **Rate-limit handling is curriculum, not friction.** Every call path handles HTTP 429 with
   `retry-after` and backoff from the first day it makes a call. This is not defensive
   programming; it is the same code the production services will need.

### 4.1 The hardware profile — the correction this section asked for

v1.0.0 closed this section with a warning to correct it before Day 0. It has been corrected, and
[`ADR-0005`](adr/ADR-0005-the-hardware-profile.md) records why. **The default hardware assumption
of this curriculum is a laptop with no GPU.** The accelerated path is the documented alternative,
not the baseline.

One environment variable selects between them, read by exactly one module, `yantra/hardware.py`:

| `YANTRA_PROFILE` | What it means | When you use it |
| --- | --- | --- |
| `laptop` | **The default.** No accelerator. Smaller base models, shorter sequences, fewer steps — the same mechanism at a scale a CPU finishes | Every day, unless you have rented or bought something |
| `gpu` | A resident or rented accelerator, CUDA available | The day you have one, and every day after |
| `auto` | Detect at import | Opt-in only, on a rented box that may be either |

`auto` is never the default, because a profile resolved by detection cannot be read off the command
line, and a measurement whose profile cannot be read is a measurement that cannot be attributed.

**Switching is one variable and one re-sync.** A CPU-only wheel does not become a CUDA wheel by
setting an environment variable, so the install moves too — and `yantra/hardware.py` **refuses to
run** under `YANTRA_PROFILE=gpu` on a torch build with no CUDA rather than falling back to CPU. The
refusal is the load-bearing half: a silent fallback is how a laptop number gets recorded as a GPU
number. [`docs/HARDWARE.md`](HARDWARE.md) carries the switch procedure and the failure text.

**Three further rules follow, binding on every day from 1 to 228:**

4. **A day that touches an accelerator states both paths in its §6 budget** — what the laptop path
   costs in *capability*, and what the accelerated path costs in *money*. Neither line is optional
   and neither is a range: the laptop path names the base model and the scale it runs at.
5. **Every measured number carries the profile that produced it**, in the document and in the
   `PROGRESS.md` row. A number without a profile is not a number (Principle 8).
6. **The laptop path is a smaller true version of the day, never a mocked one.** Same mechanism,
   same code path, same check going red — fewer steps, a smaller base, a shorter sequence. A day
   whose laptop path skips the mechanism does not have a laptop path; it has a stub, and the honest
   form of that is a `TODO(me)` in the hub saying the day needs an accelerator.

**The days that have no honest laptop path** say so in their hubs rather than pretend: Day 49
(QLoRA on an 8B base), Day 77 (the first managed endpoint) and Day 149 (the managed vector store).
Their parts are still readable and their mechanisms are still hand-rolled at laptop scale; it is the
day's headline measurement that waits for the hardware.

> ⚠️ **Still open:** the *free-tier* half of this section. §4's table assumes hourly GPU rental from
> Phase 6 and an AWS account from Phase 8. If those are also out of reach, that is a second
> amendment — it changes base-model choices in Phases 6–9 and the deployment target in Phases 8, 16
> and 21, and changing them later means amending four phase gates.

---

## 5 · ⚙️ Baseline & the verification rules

This curriculum sits on a stack that moves. Rather than pin versions in a document that will be
read for a year, the plan pins **the verification behaviour** and puts the versions in a dated
ledger.

**The rules, in force from Day 0:**

1. **Never invent a version.** Any day that installs something states the version it verified and
   how it verified it, or leaves a `TODO` containing the exact lookup command. The row lands in
   `docs/PINS.md` the same day, with the date observed.
2. **Never invent an API surface.** Any part that uses a library symbol names the documentation
   page checked *that day*, inline, next to the code: *"Verified against `<url>` on YYYY-MM-DD."*
   This binds hardest on the fast-moving surfaces — the serving engines, LangGraph, the agent
   runtime, and the two agent protocols.
3. **Never invent a citation.** A paper is looked up live, its title copied from the record rather
   than from memory, and the identifier lands in `docs/SOURCES.md` with the date it was checked.
   **Cite by title and identifier, never by author.** A wrong version number fails loudly the next
   time someone installs; a plausible identifier attached to the wrong title survives for years.
4. **Never invent a benchmark number.** Every latency, throughput, memory or quality figure in a
   day is one you measured, with the command that produced it shown. A number you read somewhere
   is a citation, and gets cited.
5. **The four moving surfaces get re-checked at every phase gate** (§18): serving engines and
   quantization formats; the agent protocols; the cloud agent runtime; and provider free tiers.

**What this replaces.** It replaces a version table that would be wrong within a month. `PINS.md`
is the version table, it is dated, and it is append-only — so when something breaks you can see
what was true when the day was written.

---

## 6 · 🧶 The nine tracks & the ID scheme

Every concept in this plan has an ID. A day **closes** an ID when the concept is built into — or
demonstrably exercised against — Yantra and the day's checks are green. `docs/TRACEABILITY.md` is
regenerated from the day hubs; **any open ID from a completed phase is a bug**, not a backlog item.

<!-- granth:tracks:start -->
| Track | Prefix | Count | Thread |
| --- | --- | --- | --- |
| Transformer Internals & Efficiency | `TF` | 66 | Architecture from tokens to experts: attention, positional schemes, the KV cache, attention variants, scaling laws, MoE. |
| Fine-Tuning, Alignment & Compression | `FT` | 90 | The whole post-training pipeline: CPT, data, PEFT, SFT, preference alignment, evaluation, quantization, reasoning, distillation. |
| Vision, Multimodal & Speech | `VIS` | 24 | ViTs, contrastive and self-supervised vision encoders, VLM architecture, speech-to-text and Whisper fine-tuning. |
| Embeddings & Retrieval | `RAG` | 46 | The embedding taxonomy, MRL, chunking, lexical and learned-sparse retrieval, fusion, reranking, multimodal and graph retrieval, caching. |
| Agents, Protocols & Orchestration | `AGT` | 82 | LangChain and LCEL, Pydantic and function calling, MCP, LangGraph, A2A, AgentCore, observability. |
| Prompt & Context Engineering | `CTX` | 14 | Prompt anatomy and robustness, structured generation, context window management, memory architectures, compression. |
| LLMOps, Evaluation & CI/CD | `OPS` | 22 | Evaluation harnesses, benchmarking, judges, prompt regression, trace testing, eval-gated pipelines, cost and latency guards. |
| Safety & Security | `SEC` | 12 | PII masking, input/output guardrails, prompt injection defence, identity and secrets, policy-based access control, sandboxing. |
| The Five Shipped Services | `PRJ` | 44 | MedScript AI, EdgeReason, LexisGraph, AutoOps and ShipLLM — the milestones that put every other track into a running system. |

**Total: 400 concept IDs across 229 days (1.75 per day).**
<!-- granth:tracks:end -->

> 🅿️ Some IDs are **parked**: you learn the map, you do not build the thing. A parked ID is marked
> 🅿️ in the day hub and closes normally. Parking is a decision that gets written down, not a way
> of quietly skipping something.

The per-ID meaning lives in the day map (§17): **each day's row is the authoritative statement of
what its IDs mean.** Sections 7–15 give each track's arc and call out the decisions inside it.

---

## 7 · 🧮 Track A — Transformer Internals & Efficiency (`TF-01..66`)

**Arc.** Tokens before embeddings, embeddings before attention, attention before architectures, and
architectures before anything is fine-tuned. Then the same machine again from the serving side:
what it costs to run, and every trick the field invented to make it cost less.

The track splits at Day 19. Everything before it answers *how does a transformer work*; everything
after answers *why does it cost that much, and what did we change*. That boundary matters because
the second half is only teachable once the first half is in your hands: MQA is a sentence if you
have not written multi-head attention, and a decision with a measured price if you have.

**Three decisions worth naming:**

- **Tokenization gets five days** (TF-03..07), which is more than most treatments give it, because
  tokenizer choices surface later as unexplained failures — a fine-tune that will not learn digits,
  a RAG chunk boundary that splits a clause, a multilingual cost that nobody budgeted.
- **Attention is written by hand before it is optimized** (Principle 4). Days 13–14 produce a block
  that trains. Days 19–27 then make it fast, and every optimization is measured against the
  hand-rolled baseline rather than against a claim.
- **MoE closes the track rather than opening the fine-tuning one** (TF-60..66), because its subject
  is a scaling decision, and scaling laws (TF-56..59) are the two days before it.

---

## 8 · 🎯 Track B — Fine-Tuning, Alignment & Compression (`FT-01..90`)

The largest track, and the spine of Phases 5–10. It runs the whole post-training pipeline in the
order a practitioner runs it: understand the lifecycle, build the data, adapt the model, align it,
evaluate it, shrink it, serve it — then do the same thing again in the other direction, compressing
a large model into a small one.

**Arc.** Lifecycle and data (FT-01..24) → parameter-efficient adaptation and alignment (FT-25..48)
→ evaluation, quantization and serving (FT-49..68) → reasoning, small models and distillation
(FT-69..90).

**Four decisions worth naming:**

- **Data comes before method** — twelve days of lifecycle, formats, loss masking and synthetic
  generation (Days 34–45) before the first LoRA. This inverts the usual order deliberately. A
  QLoRA run on a bad dataset teaches you how to run QLoRA; the failure it produces teaches nothing,
  because you cannot tell the method from the data.
- **Loss masking gets its own day** (FT-13, FT-14, Day 41) with a deliberate broken run. It is the
  single most common silent fine-tuning bug, it produces a model that trains without error and
  answers badly, and it is invisible in a loss curve.
- **Evaluation is inside the track, not after it** (FT-49..53). A fine-tune you cannot measure is a
  fine-tune you cannot defend, and the judge you build on Day 60 is the same judge the CI gate uses
  on Day 219.
- **Distillation is taught as the mirror of fine-tuning**, not as an appendix. The student–teacher
  paradigm (FT-81) is the same optimization problem seen from the other side, and Days 85–88 build
  the loss from scratch so that Project 02 is an application rather than a first encounter.

---

## 9 · 👁️ Track C — Vision, Multimodal & Speech (`VIS-01..24`)

**Arc.** CNN to ViT (VIS-01..09) → pre-trained vision encoders (VIS-10..13) → VLM architecture
(VIS-14..18) → speech and Whisper (VIS-19..24).

This track exists in this plan for one concrete reason: **Project 03 retrieves over page images**.
ColPali (RAG-38) is a vision-language model doing retrieval, and a reader who has not built a patch
embedding cannot debug it when the retrieval quality drops on scanned pages. So the track is placed
immediately before the retrieval phases, not filed as optional enrichment.

Speech (VIS-19..24) is the one part of the track that does not feed a Yantra service. It is kept
because the source roadmap teaches it, because Whisper fine-tuning is the cleanest small example of
the encoder–decoder fine-tune from Day 17 applied to a real domain, and because it is a genuinely
common production ask. It is the first candidate to cut if the plan needs compressing (§22).

---

## 10 · 🔍 Track D — Embeddings & Retrieval (`RAG-01..46`)

**Arc.** The embedding taxonomy and Matryoshka representations (RAG-01..12) → RAG from scratch,
chunking, and the three retrieval families (RAG-13..20) → fusion, transformation, reranking and
evaluation (RAG-21..32) → quantization at scale, multimodal, graph, vectorless and cached
(RAG-33..46).

**Three decisions worth naming:**

- **Embeddings are taught before RAG, not inside it** (Days 115–120). Retrieval quality is an
  embedding property first and a pipeline property second, and a reader who meets embeddings as
  "the thing before the vector store" never goes back to fine-tune one.
- **BM25 gets a full day** (RAG-18, Day 130) and is measured against dense retrieval on your own
  corpus. The hybrid result on Day 133 is only interesting if the lexical baseline was real.
- **Evaluation arrives before the clever variants** (RAG-27..28 on Day 136, before Self-RAG and
  Corrective RAG on Day 137). Adaptive retrieval strategies are indistinguishable from each other
  without a metric, and the RAGAS gate is what makes Project 03's router a decision rather than a
  preference.

---

## 11 · 🤖 Track E — Agents, Protocols & Orchestration (`AGT-01..82`)

The second-largest track. It carries LangChain as the orchestration layer, the whole function-calling
and MCP foundation, LangGraph, and the production agent stack — A2A, the cloud agent runtime,
memory, identity and observability.

**Arc.** LangChain and LCEL (AGT-01..12) → Pydantic, function calling and the executor loop
(AGT-13..27) → MCP (AGT-28..37) → LangGraph (AGT-38..54) → observability, A2A, AgentCore
(AGT-55..82).

**Three decisions worth naming:**

- **LangChain is taught with the embeddings track** (Days 121–126, Phase 13) rather than in the
  agent phases. Its load-bearing use in Yantra is `yantra-lex`'s serving layer — LCEL chains and
  LangSmith tracing — and teaching it there means the RAG phases can use it instead of hand-rolling
  a serving layer twice.
- **The tool executor loop is hand-rolled before LangGraph** (AGT-24..25 on Day 165, LangGraph from
  Day 171). Principle 4 again, and it is the difference between an engineer who can debug a stuck
  ReACT loop and one who can only restart it.
- **MCP and A2A are taught as answers to different questions**, and the day that compares them
  (AGT-65, Day 186) is the point of both. MCP is the boundary between an agent and its tools; A2A
  is the boundary between an agent and another agent. Conflating them produces architectures that
  cannot be secured, which is why SEC-07..08 sit inside this track's phase rather than beside it.

---

## 12 · 💬 Track F — Prompt & Context Engineering (`CTX-01..14`)

The smallest track, and deliberately placed early — Phase 12, before retrieval and before agents.

**This is a reordering of the source roadmap and it is on purpose.** The roadmap puts prompt and
context engineering in modules 22–23, after the agent modules. Read in that order, every RAG day
and every agent day has to gesture at prompt structure and context-window management without having
taught them. Moving them to Phase 12 means the retrieval phases can talk about *context
construction* using a vocabulary the reader owns, and the agent phases can talk about memory
architectures rather than introducing them.

The cost of the move is recorded in `docs/adr/ADR-0002` and in §22.

**Arc.** Prompt anatomy and shot count (CTX-01..03) → reasoning and structured generation
(CTX-04..06) → robustness, chaining and self-refinement (CTX-07..10) → the context window, memory
architectures and compression (CTX-11..14).

Day 112 (CTX-07, CTX-08) builds a prompt robustness test that can go red. That test is not a
teaching exercise — it becomes the golden baseline PromptFoo checks against on Day 218.

---

## 13 · 📦 Track G — LLMOps, Evaluation & CI/CD (`OPS-01..22`)

**Arc.** Harness fundamentals and benchmarking (OPS-01..04) → agent-native evaluation and judges
(OPS-05..08) → prompt regression, golden datasets and trace testing (OPS-09..13) → harness patterns
and agent CI/CD (OPS-14..20) → deployment strategy (OPS-21..22).

This track is concentrated in Phase 22 rather than spread thin, for one reason: **an evaluation
harness is only teachable against systems that exist.** By Day 206 there are four services with
real failure modes, real cost profiles and real prompts worth regression-testing. Teaching harness
engineering on a toy in Phase 3 would produce a chapter nobody could apply.

Two IDs live outside the phase — OPS-21 and OPS-22, on Days 223–224 — because blue/green deployment
and auto-rollback are only meaningful with something deployed to roll back.

---

## 14 · 🛡️ Track H — Safety & Security (`SEC-01..12`)

Twelve IDs, and **none of them are in a security phase**. Six sit in the RAG phases (SEC-01..06,
Days 145–147) and six in the agent phases (SEC-07..12, Days 191–197).

That placement is Principle 13 expressed as a plan structure. A security chapter at the end teaches
security as a review step; security IDs inside the phase that creates the exposure teach it as part
of building the thing. PII masking is taught where documents are indexed. Guardrails are taught
where a retrieval pipeline starts answering. Identity, policy and sandboxing are taught where an
agent first gets a credential and a write.

| IDs | Subject | Sits inside |
| --- | --- | --- |
| `SEC-01..02` | PII detection and masking before retrieval | Phase 15, with the RAG indexing days |
| `SEC-03..04` | Input and output guardrails | Phase 15, with the RAG serving days |
| `SEC-05..06` | Prompt injection: the attack, then the defence | Phase 15, immediately before Project 03 |
| `SEC-07..08` | Agent identity, delegated access, secrets | Phase 19, with AgentCore Identity |
| `SEC-09..10` | Policy-based access control and tool-call interception | Phase 20, before the agent gets write access |
| `SEC-11..12` | Threat modelling and sandboxed execution | Phase 20, immediately before Project 04 |

**Every SEC day carries the attack before the defence.** A guardrail you have not got past is a
guardrail you cannot evaluate.

---

## 15 · 🚢 Track I — The Five Shipped Services (`PRJ-01..44`)

Forty-four IDs across five project phases. A `PRJ` ID is not a concept — it is a **milestone in a
running service**, and it closes when that milestone is deployed and traced, not when it is
understood.

| Project | IDs | Phase | Days | The thing that must be true at the gate |
| --- | --- | --- | --- | --- |
| 01 · MedScript AI | `PRJ-01..08` | 8 | 70–77 | A live endpoint serving two adapters, and a report comparing base vs SFT vs SFT+DPO |
| 02 · EdgeReason | `PRJ-09..15` | 10 | 89–95 | A GGUF student on `llama-server`, with an ablation table and a latency benchmark against the teacher |
| 03 · LexisGraph | `PRJ-16..24` | 16 | 148–156 | An adaptive router across three retrievers, passing a RAGAS faithfulness gate on golden QA pairs |
| 04 · AutoOps | `PRJ-25..32` | 21 | 198–205 | Incident → reviewed GitHub issue → human approval, end to end, with policies enforced |
| 05 · ShipLLM | `PRJ-33..40` | 23 | 217–224 | A prompt change blocked by an eval gate, and a deployment rolled back automatically |
| Capstone | `PRJ-41..44` | 24 | 225–228 | One request traced through every service; the cost model; the public repository |

**A project phase is written to the same depth contract as every other phase.** It is not a
"now build it" week. Each day still has parts, still opens where a reader can stand, still ends in
production, and still carries a deliberate failure. The difference is that its subject is a
component of a running system rather than an idea.

**The capstone (`PRJ-41..44`) is not a fifth project.** It is the defence: the whole-system trace,
the cost model, the public audit, and the interview answers. It is the day the repository stops
being a curriculum and becomes evidence.

---

## 16 · 🗺️ The 25 phases

A phase is a block of days that share a subject and end in one thing that must be true. The gate is
not a quiz — it is an artifact or a measurement, and it is either there or it is not.

<!-- granth:phases:start -->
| Phase | Days | Theme | Gate |
| --- | --- | --- | --- |
| **0** | 0 | Foundry | `granth.py check` green; one commit; no secret in git |
| **1** | 1–12 | The transformer, taken apart | A decoder block you wrote passes a shape-and-gradient test |
| **2** | 13–18 | Attention in code, and three fine-tunes | Three fine-tuned checkpoints, three honest loss curves |
| **3** | 19–27 | Inference optimization & attention variants | Measured tokens/sec before and after the cache, on your own machine |
| **4** | 28–33 | Positional schemes, scaling laws & MoE | A compute-optimal size argument you can defend with numbers |
| **5** | 34–45 | The post-training lifecycle & data | A domain SFT dataset on the Hub, deduplicated and loss-masked |
| **6** | 46–58 | PEFT, SFT & preference alignment | One base model, two adapters, a measured preference win |
| **7** | 59–69 | Eval, quantization & multi-adapter serving | A quantized checkpoint served with two hot-swappable adapters |
| **8** | 70–77 | Project 01 · MedScript AI | Live endpoint; SFT vs SFT+DPO comparison report |
| **9** | 78–88 | Reasoning, SLMs & knowledge distillation | A student that closes most of the gap at a fraction of the cost |
| **10** | 89–95 | Project 02 · EdgeReason | GGUF model on llama-server; ablation table; latency benchmark |
| **11** | 96–107 | Vision transformers, VLMs & speech | A fine-tuned Whisper and a VLM you can explain end to end |
| **12** | 108–114 | Prompt & context engineering | A prompt suite with a robustness test that can go red |
| **13** | 115–126 | Embeddings & LangChain orchestration | An MRL-backed retrieval API traced in LangSmith |
| **14** | 127–137 | RAG foundations & advanced retrieval | Hybrid retrieval beating dense-only on your own eval set |
| **15** | 138–147 | Multimodal, graph & secured RAG | A RAGAS faithfulness gate you cannot pass by luck |
| **16** | 148–156 | Project 03 · LexisGraph | Adaptive router across ColPali, BM25 and Neo4j; RAGAS gate green |
| **17** | 157–170 | Agent foundations, function calling & MCP | An MCP server and client you wrote, talking to each other |
| **18** | 171–179 | LangGraph: stateful & multi-agent workflows | A graph that survives a kill -9 and resumes at the interrupt |
| **19** | 180–192 | Production agents: A2A, AgentCore & observability | Two agents discovering and delegating to each other over A2A |
| **20** | 193–197 | Agent supervision, policy & guardrails | A destructive tool call blocked by policy, in a trace |
| **21** | 198–205 | Project 04 · AutoOps | Incident to reviewed GitHub issue, with a human approval, in one run |
| **22** | 206–216 | Harness engineering, evals & agent CI/CD | A pull request blocked by a failing eval, with the delta commented |
| **23** | 217–224 | Project 05 · ShipLLM | Blue/green deploy with an auto-rollback you triggered on purpose |
| **24** | 225–228 | Capstone | One request traced through every service; the cost model; the public repo |
<!-- granth:phases:end -->

**Every phase gate also includes the freshness check (§18.2).** Phase 0 has nothing pinned yet, so
its freshness check is empty — but it still has a gate.

---

## 17 · 🗓️ The 229-day map

> The authoritative day → ID assignment. A day closes **exactly** these IDs — no more, no fewer.
> Day 0 closes none by design: it is the machine, the skeleton and the driver, which are
> preconditions for the curriculum rather than part of it.
>
> ⚠️ **This is the section to correct before Day 1 is written.** Changing a day map after twenty
> days exist means renaming twenty folders and re-opening every ID that moved. Correcting it now
> costs one conversation. See §22 for the levers.

<!-- granth:day-map:start -->
### Phase 0 — Foundry (Day 0)

*the machine, the skeleton, the driver*

| Day | Title | IDs closed |
| --- | --- | --- |
| 0 | Toolchain and skeleton — one owner for the environment, a repo that cannot leak a key, and a first run of the gate that refuses a half-finished day | — |

### Phase 1 — The transformer, taken apart (Days 1–12)

*tokenization, embeddings, attention, the three architectures*

| Day | Title | IDs closed |
| --- | --- | --- |
| 1 | What a language model actually is — the modelling objective, and next-token prediction followed end to end | TF-01, TF-02 |
| 2 | Text to numbers — the tokenizer boundary and the taxonomy (word, subword, character, byte) | TF-03 |
| 3 | Byte Pair Encoding, trained from scratch on your own corpus | TF-04 |
| 4 | WordPiece and SentencePiece — likelihood-driven merges and the language-agnostic case | TF-05, TF-06 |
| 5 | Tokenizer pathologies — vocabulary size, digits, code, whitespace and the multilingual tax | TF-07 |
| 6 | Embeddings — discrete symbols into continuous space; the embedding matrix and weight tying | TF-08, TF-09 |
| 7 | Positional encoding — why order has to be injected, and the sinusoidal original | TF-10 |
| 8 | The attention mechanism from first principles — query, key, value; scaled dot-product | TF-11, TF-12 |
| 9 | Self-attention and the causal mask — what a decoder is allowed to see | TF-13, TF-14 |
| 10 | Multi-head attention — why more than one head, and what heads specialise into | TF-15, TF-16 |
| 11 | The transformer block — residuals, layer norm, the feed-forward network, pre-norm vs post-norm | TF-17, TF-18, TF-19 |
| 12 | Three architectures — encoder-only, decoder-only, encoder–decoder, cross-attention, and how to choose | TF-20, TF-21, TF-22, TF-23, TF-24 |

### Phase 2 — Attention in code, and three fine-tunes (Days 13–18)

*hand-rolled attention; DistilBERT, DistilGPT, T5*

| Day | Title | IDs closed |
| --- | --- | --- |
| 13 | Coding attention I — a single head forward, and the mask in code | TF-25, TF-26 |
| 14 | Coding attention II — batched multi-head, and a block that actually trains | TF-27, TF-28 |
| 15 | Fine-tuning DistilBERT on custom data — the classification head and tokenizer alignment | TF-29, TF-30 |
| 16 | Fine-tuning DistilGPT on custom data — causal LM collation and the label shift | TF-31, TF-32 |
| 17 | Fine-tuning T5 on custom data — seq2seq collation, prefixes and generation config | TF-33, TF-34 |
| 18 | The training loop that tells the truth — loss curves, overfitting, seeds and determinism | TF-35 |

### Phase 3 — Inference optimization & attention variants (Days 19–27)

*KV cache, Flash, MQA/GQA/MLA, PagedAttention*

| Day | Title | IDs closed |
| --- | --- | --- |
| 19 | The naive decoding problem — quadratic recompute, measured rather than asserted | TF-36, TF-37 |
| 20 | The KV cache — what it stores and why the second token is cheap | TF-38, TF-39 |
| 21 | KV cache memory math — batch, sequence, layers, precision, and the number that ends the argument | TF-40, TF-41 |
| 22 | Flash Attention — IO-awareness, tiling, and why the speedup is not in the FLOPs | TF-42, TF-43 |
| 23 | PyTorch SDPA — the unified attention API and its backend selection | TF-44 |
| 24 | Multi-Query Attention — one KV head, and what it costs in quality | TF-45, TF-46 |
| 25 | Grouped-Query Attention — the compromise that shipped | TF-47, TF-48 |
| 26 | Multi-Head Latent Attention — compressing the cache instead of sharing it | TF-49, TF-50 |
| 27 | PagedAttention, continuous batching and vLLM — the serving-side answer | TF-51, TF-52, TF-53 |

### Phase 4 — Positional schemes, scaling laws & MoE (Days 28–33)

*RoPE, Chinchilla, sparse experts*

| Day | Title | IDs closed |
| --- | --- | --- |
| 28 | RoPE — rotary embeddings, and what happens when you push past the trained context | TF-54, TF-55 |
| 29 | Scaling laws for neural language models — the power law and what it predicts | TF-56, TF-57 |
| 30 | Chinchilla — compute-optimal training, and the models that were trained wrong | TF-58, TF-59 |
| 31 | The dense scaling wall and the Mixture-of-Experts idea | TF-60, TF-61 |
| 32 | MoE architecture — the router, the experts, and load balancing against expert collapse | TF-62, TF-63, TF-64 |
| 33 | Training and serving MoE; sparse vs soft variants; when dense still wins | TF-65, TF-66 |

### Phase 5 — The post-training lifecycle & data (Days 34–45)

*CPT, formats, loss masking, synthetic data*

| Day | Title | IDs closed |
| --- | --- | --- |
| 34 | The two-phase lifecycle — pre-training vs post-training, and what pre-training produces | FT-01, FT-02 |
| 35 | Why a base model is not useful out of the box — CLM, MLM and Prefix-LM recapped | FT-03, FT-04 |
| 36 | Data curation and filtering at scale — quality heuristics, dedup, contamination | FT-05, FT-06 |
| 37 | Continued pre-training for domain adaptation — and when to skip it for SFT | FT-07, FT-08 |
| 38 | The compute budget problem, applied to your own run | FT-09 |
| 39 | Multi-Token Prediction — predicting more than one step ahead | FT-10 |
| 40 | Dataset formats and chat templates — instruction pairs, ChatML, LLaMA-3, Mistral | FT-11, FT-12 |
| 41 | Loss masking — what it is, and exactly what breaks without it | FT-13, FT-14 |
| 42 | Deduplication and filtering pipelines you can run | FT-15, FT-16 |
| 43 | Synthetic data I — why data is the leverage point; the taxonomy; Self-Instruct and Alpaca | FT-17, FT-18, FT-19 |
| 44 | Synthetic data II — preference pairs, LLM-as-Judge scoring, and distilabel/Argilla | FT-20, FT-21, FT-22 |
| 45 | Model collapse and data poisoning — the two ways a synthetic pipeline rots | FT-23, FT-24 |

### Phase 6 — PEFT, SFT & preference alignment (Days 46–58)

*LoRA, QLoRA, DoRA, SFT, RLHF, DPO*

| Day | Title | IDs closed |
| --- | --- | --- |
| 46 | The intrinsic dimensionality insight — why a low-rank update is enough | FT-25 |
| 47 | LoRA — the math, rank, alpha, and which modules to target | FT-26, FT-27 |
| 48 | LoRA in practice with PEFT — adapters on disk, merged and unmerged | FT-28 |
| 49 | QLoRA — 4-bit NF4, double quantization, paged optimizers | FT-29, FT-30, FT-31 |
| 50 | DoRA — decomposing magnitude from direction | FT-32 |
| 51 | AdaLoRA and LoRA+ — adaptive rank, and separate learning rates for A and B | FT-33, FT-34 |
| 52 | Supervised fine-tuning as stage 1 — SFTTrainer, end to end | FT-35, FT-36 |
| 53 | Instruction tuning — FLAN, Alpaca, OpenHermes and what a good instruction set looks like | FT-37, FT-38 |
| 54 | Chat and conversational fine-tuning — multi-turn data without leakage | FT-39 |
| 55 | Chain-of-thought fine-tuning — training the reasoning trace, not just the answer | FT-40 |
| 56 | Domain-specific fine-tuning — best practices and catastrophic forgetting | FT-41, FT-42 |
| 57 | Why SFT alone is not enough — RLHF with PPO: reward model, critic, KL penalty | FT-43, FT-44, FT-45 |
| 58 | DPO — direct preference optimization without a reward model; GRPO and ORPO in one page | FT-46, FT-47, FT-48 |

### Phase 7 — Eval, quantization & multi-adapter serving (Days 59–69)

*judges, GPTQ/AWQ/GGUF, vLLM, SGLang*

| Day | Title | IDs closed |
| --- | --- | --- |
| 59 | Why evaluation belongs inside the fine-tuning loop — and the three benchmark families | FT-49, FT-50 |
| 60 | LLM-as-judge — MT-Bench, Chatbot Arena, and calibrating a judge you can trust | FT-51, FT-52 |
| 61 | Designing a domain evaluation that can fail | FT-53 |
| 62 | Post-training quantization I — GPTQ | FT-54, FT-55 |
| 63 | Post-training quantization II — AWQ, bitsandbytes NF4, FP8 | FT-56, FT-57 |
| 64 | Merging LoRA adapters before serving — and when not to | FT-58 |
| 65 | vLLM as a serving engine — paged KV, scheduling, and the OpenAI-compatible surface | FT-59, FT-60 |
| 66 | SGLang, and serving many LoRA adapters from one base model | FT-61, FT-62 |
| 67 | GGUF and llama.cpp — the CPU path | FT-63, FT-64 |
| 68 | Speculative decoding — a draft model that pays for itself | FT-65 |
| 69 | The tooling landscape — TRL, Unsloth, Axolotl, LLaMA-Factory, and managed fine-tuning | FT-66, FT-67, FT-68 |

### Phase 8 — Project 01 · MedScript AI (Days 70–77)

*the medical post-training pipeline, shipped*

| Day | Title | IDs closed |
| --- | --- | --- |
| 70 | Project 01 kickoff — the medical post-training pipeline, the datasets, and their licences | PRJ-01 |
| 71 | Synthetic medical instruction data with distilabel | PRJ-02 |
| 72 | The SFT dataset — deduplication, chat format, loss masking, pushed to the Hub | PRJ-03 |
| 73 | Stage 1 — QLoRA SFT on Llama-3.1-8B-Instruct | PRJ-04 |
| 74 | Stage 2 — DPO preference alignment over one epoch | PRJ-05 |
| 75 | Evaluation — ROUGE-L, BERTScore, and a judge on medical accuracy, safety and tone | PRJ-06 |
| 76 | The multi-adapter vLLM server and FastAPI adapter routing | PRJ-07 |
| 77 | Containerise, deploy to a SageMaker endpoint, trace it — and the phase gate | PRJ-08 |

### Phase 9 — Reasoning, SLMs & knowledge distillation (Days 78–88)

*CoT, R1-Zero, student-teacher, KL*

| Day | Title | IDs closed |
| --- | --- | --- |
| 78 | What a reasoning model is, and how it differs from a standard LLM | FT-69, FT-70 |
| 79 | Chain-of-thought as the foundation — prompted, then trained | FT-71 |
| 80 | The reasoning training recipe — verifiable rewards and the RL loop | FT-72, FT-73 |
| 81 | R1-Zero — skipping supervised fine-tuning entirely, and what it cost | FT-74, FT-75 |
| 82 | Distilling reasoning without RL | FT-76 |
| 83 | What a Small Language Model is, and why cost, latency and privacy make it the default | FT-77, FT-78 |
| 84 | The SLM design philosophy — and pruning as the other lever | FT-79, FT-80 |
| 85 | The student–teacher paradigm — and what 'knowledge' actually means here | FT-81, FT-82 |
| 86 | Hard labels, soft labels and temperature scaling | FT-83, FT-84 |
| 87 | The KL divergence loss and attention transfer | FT-85, FT-86 |
| 88 | A distillation pipeline end to end — teacher data, student design, training, and choosing the scale | FT-87, FT-88, FT-89, FT-90 |

### Phase 10 — Project 02 · EdgeReason (Days 89–95)

*distillation to CPU inference, shipped*

| Day | Title | IDs closed |
| --- | --- | --- |
| 89 | Project 02 kickoff — teacher and student selection, GSM8K and MATH | PRJ-09 |
| 90 | Teacher logit extraction and soft-label storage at temperature | PRJ-10 |
| 91 | KL divergence and attention transfer, implemented from scratch | PRJ-11 |
| 92 | The custom training loop, and loss curves that are actually read | PRJ-12 |
| 93 | The ablation study — which loss term earned its place | PRJ-13 |
| 94 | GGUF conversion across quantisation levels | PRJ-14 |
| 95 | llama-server on CPU — tokens/sec and first-token latency against the teacher; the gate | PRJ-15 |

### Phase 11 — Vision transformers, VLMs & speech (Days 96–107)

*ViT, CLIP/SigLIP/DINOv2, VLMs, Whisper*

| Day | Title | IDs closed |
| --- | --- | --- |
| 96 | From CNN to Vision Transformer — the conceptual bridge | VIS-01, VIS-02 |
| 97 | An image as a sequence of patches — patch embedding in code | VIS-03, VIS-04 |
| 98 | The CLS token and positional encoding for 2D inputs | VIS-05, VIS-06 |
| 99 | The transformer encoder running on visual tokens | VIS-07 |
| 100 | Attention maps — what a ViT actually looks at | VIS-08 |
| 101 | CNN vs ViT — inductive bias, data hunger, and the core tradeoff | VIS-09 |
| 102 | CLIP — contrastive language–image pre-training | VIS-10, VIS-11 |
| 103 | SigLIP and DINOv2 — a sigmoid loss, and self-supervised vision | VIS-12, VIS-13 |
| 104 | Visual Language Models — the three-component architecture | VIS-14, VIS-15 |
| 105 | The aligner/projector — how visual tokens enter the LLM's embedding space | VIS-16, VIS-17, VIS-18 |
| 106 | Speech AI and speech-to-text foundations; the Whisper architecture | VIS-19, VIS-20 |
| 107 | Whisper in practice — the API, an STT pipeline, dataset preparation, and fine-tuning on custom audio | VIS-21, VIS-22, VIS-23, VIS-24 |

### Phase 12 — Prompt & context engineering (Days 108–114)

*prompt anatomy, CoT, compression, memory*

| Day | Title | IDs closed |
| --- | --- | --- |
| 108 | Anatomy of a prompt — instruction, context, input, output format; zero-, one- and few-shot | CTX-01, CTX-02 |
| 109 | System prompt design and role assignment | CTX-03 |
| 110 | Chain-of-thought and step-back prompting | CTX-04, CTX-05 |
| 111 | Structured generation — JSON mode, XML tags, and grammars | CTX-06 |
| 112 | Prompt sensitivity and fragility — a robustness test that goes red | CTX-07, CTX-08 |
| 113 | Prompt chaining, decomposition, meta-prompting and self-refinement loops | CTX-09, CTX-10 |
| 114 | The context window — anatomy, recency bias, memory architectures, and compression with LLMLingua and RECOMP | CTX-11, CTX-12, CTX-13, CTX-14 |

### Phase 13 — Embeddings & LangChain orchestration (Days 115–126)

*taxonomy, MRL, LCEL, LangSmith*

| Day | Title | IDs closed |
| --- | --- | --- |
| 115 | The embedding taxonomy — dense, sparse, and what each one preserves | RAG-01, RAG-02, RAG-03 |
| 116 | Quantized and binary embeddings — float32 to int8 to one bit | RAG-04, RAG-05 |
| 117 | Multi-vector embeddings — one document, many vectors | RAG-06 |
| 118 | Matryoshka Representation Learning — flexible dimensions at query time | RAG-07, RAG-08 |
| 119 | MRL embeddings in production — the truncation decision | RAG-09 |
| 120 | Embedding fine-tuning — strategies, hard negatives, and doing it on your own corpus | RAG-10, RAG-11, RAG-12 |
| 121 | LangChain architecture and the model abstraction | AGT-01, AGT-02 |
| 122 | LCEL — composition, streaming, and the runnable interface | AGT-03, AGT-04 |
| 123 | Output parsers and structured output in LangChain | AGT-05 |
| 124 | Tool calling, memory and conversation history | AGT-06, AGT-07 |
| 125 | Document loaders, text splitters and vector stores | AGT-08, AGT-09 |
| 126 | Callbacks, tracing and LangSmith; deploying a LangChain API safely | AGT-10, AGT-11, AGT-12 |

### Phase 14 — RAG foundations & advanced retrieval (Days 127–137)

*chunking, BM25, SPLADE, ColBERT, rerankers*

| Day | Title | IDs closed |
| --- | --- | --- |
| 127 | Vanilla RAG, end to end and by hand | RAG-13, RAG-14 |
| 128 | Choosing an embedding model for retrieval — and measuring the choice | RAG-15 |
| 129 | Chunking strategies and what each one destroys | RAG-16, RAG-17 |
| 130 | BM25 and why lexical retrieval refuses to die | RAG-18 |
| 131 | SPLADE — learned sparse retrieval | RAG-19 |
| 132 | ColBERT-style late interaction and MaxSim | RAG-20 |
| 133 | Hybrid RAG and Reciprocal Rank Fusion | RAG-21, RAG-22 |
| 134 | Query transformations — rewriting, decomposition, HyDE | RAG-23, RAG-24 |
| 135 | Rerankers — cross-encoders and the precision they buy | RAG-25, RAG-26 |
| 136 | RAG evaluation with RAGAS — faithfulness, relevancy, context precision and recall | RAG-27, RAG-28 |
| 137 | Self-RAG, Corrective RAG, Adaptive RAG and Agentic RAG — the LLM deciding when to retrieve | RAG-29, RAG-30, RAG-31, RAG-32 |

### Phase 15 — Multimodal, graph & secured RAG (Days 138–147)

*quantization, ColPali, Neo4j, guardrails*

| Day | Title | IDs closed |
| --- | --- | --- |
| 138 | Vector quantization for scale — scalar, binary and product quantization | RAG-33, RAG-34, RAG-35 |
| 139 | Document parsing without OCR — layout detection and structure-aware chunking | RAG-36, RAG-37 |
| 140 | The ColPali paradigm — retrieving over page images | RAG-38, RAG-39 |
| 141 | Vision-language embeddings and VL rerankers | RAG-40, RAG-41 |
| 142 | Graph RAG with Neo4j — entities, relationships and multi-hop questions | RAG-42, RAG-43 |
| 143 | Vectorless retrieval — PageIndex | RAG-44 |
| 144 | Caching and semantic caching in a RAG pipeline | RAG-45, RAG-46 |
| 145 | PII masking with Presidio, before retrieval | SEC-01, SEC-02 |
| 146 | Input and output guardrails with NeMo Guardrails | SEC-03, SEC-04 |
| 147 | Prompt injection against a RAG system — the attack, then the defence | SEC-05, SEC-06 |

### Phase 16 — Project 03 · LexisGraph (Days 148–156)

*enterprise legal RAG, shipped*

| Day | Title | IDs closed |
| --- | --- | --- |
| 148 | Project 03 kickoff — CUAD, the legal corpus, and the retrieval contract | PRJ-16 |
| 149 | ColPali indexing into Qdrant with MaxSim scoring | PRJ-17 |
| 150 | Elasticsearch BM25 over the same corpus | PRJ-18 |
| 151 | Entity extraction with an LLM and Pydantic, into a Neo4j graph | PRJ-19 |
| 152 | Reciprocal Rank Fusion across all three retrievers | PRJ-20 |
| 153 | Cross-encoder reranking on the fused candidates | PRJ-21 |
| 154 | The adaptive query router — visual, exact-clause, relational, or all three | PRJ-22 |
| 155 | Presidio and NeMo Guardrails wired into the pipeline | PRJ-23 |
| 156 | The RAGAS faithfulness gate on golden QA pairs; FastAPI + LCEL + Docker | PRJ-24 |

### Phase 17 — Agent foundations, function calling & MCP (Days 157–170)

*Pydantic, schemas, executor loop, MCP*

| Day | Title | IDs closed |
| --- | --- | --- |
| 157 | Pydantic — models, fields and validators | AGT-13, AGT-14 |
| 158 | Nested models, type coercion, custom validators and settings management | AGT-15, AGT-16 |
| 159 | Why function calling exists — the LLM-to-tool communication problem | AGT-17 |
| 160 | Function schema design — JSON Schema, descriptions and parameter typing | AGT-18, AGT-19 |
| 161 | The function-calling request–response lifecycle | AGT-20 |
| 162 | Parallel function calling — several tool calls in one response | AGT-21 |
| 163 | Forced and constrained tool choice — required, none, and naming a tool | AGT-22 |
| 164 | Structured output vs function calling — the difference, and when each is right | AGT-23 |
| 165 | Building a tool executor loop from scratch | AGT-24, AGT-25 |
| 166 | Function calling across providers — OpenAI, Anthropic, Google, and the universal contract | AGT-26, AGT-27 |
| 167 | Why MCP exists — tool fragmentation; hosts, clients and servers | AGT-28, AGT-29 |
| 168 | MCP primitives — tools, resources and prompts | AGT-30, AGT-31 |
| 169 | MCP transport — stdio and SSE; building a server from scratch | AGT-32, AGT-33, AGT-34 |
| 170 | Building an MCP client; authentication, authorization and trust boundaries | AGT-35, AGT-36, AGT-37 |

### Phase 18 — LangGraph: stateful & multi-agent workflows (Days 171–179)

*state, routing, ReACT, HITL, persistence*

| Day | Title | IDs closed |
| --- | --- | --- |
| 171 | LangGraph foundations and the core graph model | AGT-38, AGT-39 |
| 172 | State management — schemas, reducers and what belongs in state | AGT-40, AGT-41 |
| 173 | Nodes, edges and conditional routing | AGT-42, AGT-43 |
| 174 | Tool calling and the ReACT pattern as a graph | AGT-44, AGT-45 |
| 175 | Human-in-the-loop — interrupts before a write | AGT-46, AGT-47 |
| 176 | Memory and persistence across sessions — checkpointers | AGT-48, AGT-49 |
| 177 | Multi-agent systems — supervisor and workers, and the shared-state contract | AGT-50, AGT-51 |
| 178 | Streaming and observability out of a running graph | AGT-52 |
| 179 | LangGraph Platform; orchestrating several MCP servers from one graph | AGT-53, AGT-54 |

### Phase 19 — Production agents: A2A, AgentCore & observability (Days 180–192)

*agent cards, runtime, memory, identity*

| Day | Title | IDs closed |
| --- | --- | --- |
| 180 | Agent observability with LangSmith and Logfire | AGT-55, AGT-56 |
| 181 | Why A2A exists — the multi-agent interoperability problem | AGT-57, AGT-58 |
| 182 | Agent Cards — capability discovery and the well-known endpoint | AGT-59 |
| 183 | The A2A task model — submitted, working, completed, failed, streaming | AGT-60 |
| 184 | A2A transport — HTTP, SSE and the JSON-RPC message structure | AGT-61 |
| 185 | Building an A2A-compliant agent server | AGT-62, AGT-63 |
| 186 | Building an A2A client; A2A vs MCP and how they compose | AGT-64, AGT-65 |
| 187 | Bedrock AgentCore and the agentic stack; Runtime, microVM isolation and session windows | AGT-66, AGT-67 |
| 188 | Strands Agents; framework-agnostic deployment of a LangGraph agent to AgentCore | AGT-68, AGT-69 |
| 189 | AgentCore Memory — short-term, long-term and cross-session persistence | AGT-70, AGT-71 |
| 190 | AgentCore Gateway — exposing APIs, Lambda functions and MCP servers as tools | AGT-72, AGT-73 |
| 191 | AgentCore Identity — IAM roles per agent, OAuth, user-delegated access and secrets | AGT-74, SEC-07, SEC-08 |
| 192 | AgentCore Browser and Code Interpreter; deploying with the CLI, CodeBuild, ECR and an ARM64 runtime | AGT-75, AGT-76, AGT-77 |

### Phase 20 — Agent supervision, policy & guardrails (Days 193–197)

*supervisor patterns, Cedar, sandboxes*

| Day | Title | IDs closed |
| --- | --- | --- |
| 193 | Multi-agent orchestration at scale — supervisor patterns that survive contact | AGT-78, AGT-79 |
| 194 | AgentCore Observability — CloudWatch, X-Ray, OTEL and third-party monitoring | AGT-80, AGT-81 |
| 195 | Cedar policies and real-time tool-call interception | SEC-09, SEC-10 |
| 196 | Agent threat modelling — blast radius before capability | SEC-11 |
| 197 | Sandboxed tool execution — E2B, Modal, Docker | SEC-12, AGT-82 |

### Phase 21 — Project 04 · AutoOps (Days 198–205)

*the DevOps multi-agent system, shipped*

| Day | Title | IDs closed |
| --- | --- | --- |
| 198 | Project 04 kickoff — the supervisor graph, the sub-agents and the shared state | PRJ-25 |
| 199 | The GitHub agent as a FastMCP server | PRJ-26 |
| 200 | The CloudWatch agent as a FastMCP server | PRJ-27 |
| 201 | The Code Review and Monitoring agents | PRJ-28 |
| 202 | A2A peer delegation between the sub-agents | PRJ-29 |
| 203 | HITL interrupts and exact checkpoint resume from SQLite | PRJ-30 |
| 204 | Deploying to the cloud agent runtime — gateway, memory, identity | PRJ-31 |
| 205 | Cedar policies, observability, and the incident-to-issue demo | PRJ-32 |

### Phase 22 — Harness engineering, evals & agent CI/CD (Days 206–216)

*Inspect AI, PromptFoo, eval gating*

| Day | Title | IDs closed |
| --- | --- | --- |
| 206 | Why ad-hoc testing fails — evaluation harness fundamentals | OPS-01, OPS-02 |
| 207 | LLM benchmarking with lm-evaluation-harness — MMLU, GSM8K, TruthfulQA | OPS-03, OPS-04 |
| 208 | Agent-native evaluation with Inspect AI — Task, Solver, Scorer | OPS-05, OPS-06 |
| 209 | LLM-as-Judge pipelines — model-graded scoring, calibration and bias | OPS-07, OPS-08 |
| 210 | Prompt regression and snapshot testing with PromptFoo | OPS-09, OPS-10 |
| 211 | Golden datasets — building them, versioning them, and keeping them honest | OPS-11 |
| 212 | Trace-based testing and flaky-test detection | OPS-12, OPS-13 |
| 213 | Agent state, checkpointing and ReAct harness patterns — iteration guards, fallbacks, token budgets | OPS-14, OPS-15 |
| 214 | Multi-agent execution harnesses — the supervisor–worker contract as a test | OPS-16 |
| 215 | Agent CI/CD — GitHub Actions and eval gating on pull requests | OPS-17, OPS-18 |
| 216 | Cost and latency regression guards | OPS-19, OPS-20 |

### Phase 23 — Project 05 · ShipLLM (Days 217–224)

*the LLMOps shell over all four services*

| Day | Title | IDs closed |
| --- | --- | --- |
| 217 | Project 05 kickoff — the monorepo, the golden test suite and the gate contract | PRJ-33 |
| 218 | Stages 1–2 — lint, unit tests, and prompt regression against the golden baseline | PRJ-34 |
| 219 | Stage 3 — the per-service evaluation score gate | PRJ-35 |
| 220 | Stage 4 — cost and performance regression guard, and the score delta posted on the PR | PRJ-36 |
| 221 | Stage 5 — multi-stage container builds and the registry push | PRJ-37 |
| 222 | Stage 6 — smoke tests on staging with golden cases | PRJ-38 |
| 223 | Blue/green deployment with gradual traffic shifting | PRJ-39, OPS-21 |
| 224 | Auto-rollback on an error-rate breach, and the LLM metrics dashboard | PRJ-40, OPS-22 |

### Phase 24 — Capstone (Days 225–228)

*the whole system, defended*

| Day | Title | IDs closed |
| --- | --- | --- |
| 225 | One request, traced through every service in the system | PRJ-41 |
| 226 | The cost model — what the whole system costs per thousand requests | PRJ-42 |
| 227 | The public repository audit, and the README a stranger reads | PRJ-43 |
| 228 | The defence — the demo, and the answers to the questions it invites | PRJ-44 |

<!-- granth:day-map:end -->

---

## 18 · 🚦 Phase gates & the freshness check

### 18.1 A phase is green only when

1. Every day in the phase has its row in `docs/PROGRESS.md`, with checks green.
2. The traceability report shows **no open IDs** from this or any earlier phase.
3. `granth.py check` passes on the whole repository — lint, format, tests, **the §20 depth contract for
   every written day**, and index freshness.
4. Every day in the phase has a `parts/` directory. A day with no `parts/` is not written (§20.2),
   so a phase containing one cannot be green.
5. The freshness check (§18.2) passes.
6. Every deviation is recorded: an ADR for anything structural, `docs/CHANGELOG_PLAN.md` for plan
   text.

**Never skip a day, merge two days, or reorder days without an ADR.** The ADR is the point: it
makes you notice the cost before paying it.

> A gate is never passed because time ran out (Principle 15). `granth.py done N` is gated on a ticked
> checklist and green checks, and on nothing else.

### 18.2 The freshness check — four surfaces, re-checked every gate

These four move faster than this document, and each has broken a curriculum before.

| Surface | What to re-check | What a change forces |
| --- | --- | --- |
| **Serving & quantization** | Release notes for the serving engine and quantization tooling in use since the last gate | A changed adapter or quantization format → amend before the next serving day |
| **Agent protocols** | The MCP and A2A specification revisions | A spec revision → re-read the affected days' sources before writing further protocol days |
| **Cloud agent runtime** | The runtime's API surface and its deployment path | A renamed surface → amend, then update the affected `PINS.md` rows |
| **Provider free tiers & model availability** | Every model string the plan pins, and its rate limits | A model that lost its free tier or was deprecated → amend §4 and the affected hubs first |

A freshness check that finds nothing is still recorded — one line in `docs/PROGRESS.md` for the
gate, with the date. A gate with no dated freshness row has not had one.

---

## 19 · 📒 Ledgers & traceability

All ledgers live in `docs/`. **Four are written by hand and are append-only; four are generated.**
Do not confuse them — editing a generated file only means the next `granth.py index` silently overwrites
you, and if a generated index ever disagrees with a day, **the day is right and the index is
stale**.

| File | Nature | Rule |
| --- | --- | --- |
| `docs/PROGRESS.md` | Append-only | One row per completed day. **The last row is where we are.** |
| `docs/PINS.md` | Append-only | Every version, model string, quota and limit — with the date observed and the day that observed it. No invented versions (Principle 7). |
| `docs/SOURCES.md` | Append-only | Every citation: title, identifier, URL, the date the record was checked, the parts citing it. **By title and identifier, never by author.** |
| `docs/GLOSSARY.md` | Append-only | Every term, defined once, with the part that introduced it. This is what makes "define jargon on first use, including jargon from earlier days" mechanical rather than heroic. |
| `docs/PROVENANCE.md` | Append-only | Every third-party dependency, model or dataset: source, licence, audit date — recorded **before** it runs. Datasets matter here as much as packages: several in Phases 8 and 16 carry research-only licences. |
| `docs/CHANGELOG_PLAN.md` | Append-only | Every amendment to this plan (Principle 12). |
| `docs/TRACEABILITY.md` | Generated | Every ID and whether it is closed. An open ID in a completed phase is a bug. |
| `docs/CURRICULUM_INDEX.md` | Generated | Where do I learn `RAG-27`? The ID → day cross-table, read out of §17. |
| `docs/TRACKER.md` | Generated | What is written, **how many parts each day has**, and what is pending. A thin day is visible from this table alone. |
| `docs/WIKI.md` + `docs/wiki/` | Generated | One row per day, one page per day, plus an entity index for "which day taught X?" |

ADRs are `docs/adr/ADR-NNNN-<slug>.md`. **An ADR is never rewritten** — a decision that turns out
wrong is superseded by a later ADR, and the original stays exactly as it was. An ADR set you can
edit always looks like it was right from the start.

**`docs/PROGRESS.md` is the honest part of the repository.** Leave the bad days in it, with the
notes saying what went wrong. A ledger with no failures in it is a ledger nobody has been honest
in, and readers can tell.

---

## 20 · 📐 The depth contract — how a day is written

> **Why this section exists.** The failure mode this contract prevents is a day that looks
> finished. One long page under one heading, covering an entire subject, with an "estimated hours"
> field at the top telling the reader how fast to go past it. A reader cannot revisit *one* idea
> without re-reading four; there is no way to tell a thinly-covered subtopic from a missing one;
> and the duration field silently authorises the worst edit in technical writing — cutting an
> explanation because the day is running long.
>
> This section states exactly what "covered properly" means, so that it can be reviewed by reading
> and partly checked by a script. It is Principles 14, 15 and 16, made concrete.

### 20.1 The three commitments

Everything below follows from three sentences.

**One idea per document.** A subtopic that cannot be read alone, understood without scrolling past
a different subtopic, and explained back out loud is not one subtopic — it is several, badly
stacked. **If a document needs the word "also" to introduce its second half, it is two documents.**

**No clocks.** Nothing in a day folder carries a time estimate, a duration, an "estimated hours"
field, or a suggested pace — not in frontmatter, not in prose, not in the checklist. A topic takes
as long as it takes. **Content is never trimmed to fit a schedule**, and a day is never declared
finished because a duration elapsed. The day number is an index into the subject, nothing more.

**Zero to production, in one document.** Each part starts where a reader who has never heard of the
idea can stand, and ends where a working professional stands: how the idea appears in a real
system, what a senior engineer does differently from the tutorial version, what fails at scale or
under concurrency, and what a reviewer or an interviewer will probe. Strong fundamentals and
advanced technique are not separate tracks — they are the beginning and the end of the same page.

### 20.2 The folder shape

Every day, without exception, is a folder of this shape:

```
days/day-NNN-<day-slug>/
├── LESSON.md          # the hub — orients and assembles; it never teaches
├── CHECKLIST.md       # the definition of done; python granth.py done refuses until ticked
├── parts/             # THE TEACHING — one document per subtopic
│   ├── 01-<slug>/
│   │   ├── 1.1-<slug>.md
│   │   └── 1.2-<slug>.md
│   └── 02-<slug>/
│       └── 2.1-<slug>.md
├── sources/           # one document per primary source (§20.4.2), read AFTER the parts
│   └── 01-<source-slug>.md
└── lab/               # the learner's own work — gitignored
```

`parts/` is mandatory. **A day with no `parts/` directory is, by definition, not written.**

**Every folder name carries its subject.** `days/day-137/` and `parts/02/` are addresses, not
answers, and 229 days of them are indistinguishable in a file tree, a `git log` or an editor's tab
bar. So the number is followed by a short kebab-case slug naming what is inside.

| Folder | Shape | Slug from | Length |
| --- | --- | --- | --- |
| the day | `day-NNN-<slug>` | the hub's `title`, minus articles | 1–4 words |
| a section | `NN-<slug>` | the section's heading in the hub's §2 map | 1–3 words |

**The number is the identity; the slug is a label on it.** Every tool resolves a day by number and
accepts whatever slug follows, so renaming a folder to a better slug can never break the driver.
Day numbers are zero-padded to three digits, because this plan runs past 99.

### 20.3 The numbering rule

Part numbers are **`<section>.<subtopic>`**, both scoped to the day.

- The **section** groups subtopics that share one mental model — usually one ID, one stage of a
  pipeline, or one phase of a mechanism.
- The **subtopic** is the reading order inside that section. It starts at `1`, never `0`, and has
  no gaps.

The hub's §2 map declares what each section *is*; an unexplained numbering is a bug in the
document. A two-ID day typically runs `1.x` = first ID, `2.x` = second ID, `3.x` = the synthesis
where they meet. A pipeline day uses sections as stages. A project day uses them as components in
build order.

The folder number and the number before the dot must agree: `parts/02-kv-cache/2.3-<slug>.md` is
correct; `parts/02-kv-cache/3.1-<slug>.md` is a bug the depth check rejects.

**Links between parts are relative.** A sibling is its filename; across sections it goes up one
level (`../01-<slug>/1.5-<slug>.md`); the hub is `../../LESSON.md`.

### 20.4 What a part document must contain

Every file in `parts/` carries all eleven of these, **in this order**. Three are **conditional** —
*The source behind it*, *Line by line*, and *The source in one demo*. The other eight are
unconditional.

| # | Section | The rule |
| --- | --- | --- |
| 1 | **Frontmatter** | `day`, `part`, `title`, `ids`, `level`, `prerequisites`, `prev`, `next`, plus `sources` (identifiers this part cites) or, on a source part, `source` (the one it teaches). Machine-read. **No duration field of any kind.** |
| 2 | **One-line answer** | The subtopic's claim in a single sentence, before anything else. A reader who reads only this line has learned something true. |
| 3 | **The story** | A concrete scene before any abstraction: a person, a machine, a failure, a decision. It comes **first**, in plain words, with **no jargon at all**. Four rules: **(a)** a scene the reader has plausibly lived in — a parcel and a courier, a repair-shop job card, a used car checked by a mechanic. Not a nautical chart or a theatre programme. If the reader must first be told what the setting *is*, the analogy is carrying the explanation instead of hooking it. **(b)** simple words, short sentences. **(c)** load-bearing — the scene holds the actual failure the part teaches, and every later section reaching back for it must still fit. **(d)** one metaphor family per day. |
| 4 | **The idea in plain language** | The concept itself, assuming the reader has never met it. Every term defined the first time it appears — **including terms from earlier days**, with a link to the part that introduced them, never an assumption of recall. No code. |
| 5 | **Why Yantra needs it** | The concrete later day that breaks without this. *"You meet this again on Day 149, where ColPali writes patch vectors into a multi-vector index"* is the shape. Never "this is important". |
| 6 | **The source behind it** | **Conditional — present exactly when the idea has a public, citable origin a reader could go and read**: a paper, a numbered spec revision, a formal technical report. It is **an address, not an explanation** — the explanation is a source part of its own. Three things: the citation block (exact title · identifier · year · URL — **no author names**), one sentence on what it claimed, and a link to the source part that teaches it. A part whose subject is a tool, a command or an SDK surface has no source and does not carry this section. |
| 7 | **The mechanism** | How it actually works: the runnable code, the protocol exchange written out, or the diagram. Nothing skipped as "obvious". Mermaid whenever the concept is spatial, sequential, or a state machine. |
| 8 | **Line by line** | Every non-obvious token of every code block explained — and *why it is that line and not another*. Written as a `**Line by line:**` list **immediately after each code block**, so the reader never scrolls to find the explanation of what they are looking at. Blocks showing error output, a bare check command, or a diagram are exempt. **An unexplained line is a bug in the document.** **Conditional:** a part carrying no code needing a walkthrough does not carry this section. |
| 9 | **The source in one demo** | **Conditional — source parts only.** A small end-to-end project that implements the source's contribution **and nothing else**: the whole file tree, every file's contents, the one command that runs it, and the output it prints. It carries an **ablation switch** — one flag that turns the idea off — and shows **both runs' output**. A demo that cannot be switched off has proved that code ran, not that this idea did something. |
| 10 | **When it breaks** | The **real** error text, reproduced verbatim — the traceback, the CUDA OOM, the HTTP status, the JSON-RPC error body. What it says, what it actually means, and the smallest fix. This is what the reader meets at 11pm; the happy path is not. **If you have not seen the error, cause it.** |
| 11 | **In production** | Where this idea shows up in a real system and what changes there: the version a professional writes instead of the teaching version, what degrades at scale or under concurrency, the failure mode that only appears with real traffic, the review comment a senior engineer leaves, and the question an interviewer asks to find out whether you have actually used it. **This is the section that makes the document professional rather than introductory. It is not optional.** |
| 12 | **Check yourself** | One command the reader can run right now, plus one question they must answer **out loud** without scrolling up. |

Three further rules with no section of their own:

- **The one-idea test.** If a part needs "also" to introduce its second half, split it.
- **The standalone test.** A part must be readable cold. If it depends on an earlier idea, **name
  that part and link it** — never assume the reader remembers Day 20 on Day 190.
- **The no-shortcut test.** "For now, just accept that" is banned unless it links forward to the
  part that explains it. **A deferred explanation must have an address.**

#### 20.4.1 Yantra's four additional part rules

1. **Never invent an API.** Any part using a library symbol names the documentation page checked
   that day, inline, next to the code.
2. **Never invent a version.** Any part that installs something states the version it verified and
   how, or leaves a `TODO` with the exact lookup command. The row lands in `PINS.md` the same day.
3. **Never invent a measurement.** Any part claiming a speedup, a memory saving, a quality delta or
   a cost must show the command that produced the number and the machine it ran on. A number
   without a command is a rumour.
4. **Name the licence.** Any part that introduces a dataset or a pre-trained checkpoint states its
   licence and whether it permits the use this curriculum makes of it. The row lands in
   `PROVENANCE.md` before the download.

#### 20.4.2 The source part — one document per primary source

Section 6 gives the reader an address. **This is the document at it.**

A source is an idea, and §20.1 says one idea gets one document. Folding a paper into a section of
the part that uses it breaks that rule twice over: the part now teaches two things, and the paper
gets whatever space is left after the mechanism — which is how a curriculum ends up citing a
document it never explains.

**One document per source**, named `NN-<source-slug>.md`, numbered in reading order from `01`,
living in `days/day-NNN-<slug>/sources/` beside `parts/` and not inside it.

**Read them after the parts, not before.** The hub's map says so and the last part's *next* points
at them. That is Principle 4 at the scale of a day: hand-roll the mechanism, *then* read the
proposal. A reader who has just written attention by hand can be told which half of the paper they
reinvented and which half the field dropped; a reader who meets the paper first has nothing to hang
it on.

A source part carries all eleven sections. Section 6 never fires on it. Section 9 — *The source in
one demo* — is **required**, and it is the section easiest to get wrong, so it has four rules:

1. **Only the source's feature.** Not a small app that happens to use the idea — a small project
   whose *entire reason to exist* is the idea. The test is subtractive: if a file could be deleted
   and the claim still lands, delete it.
2. **End to end, and actually runnable.** One command, stated. Its real output, pasted. **If the
   demo needs a GPU or a live model and has not been run, the output block is a `TODO(me)` naming
   the exact command — never an invented transcript.** A missing output is completed by one run
   and is obvious to everyone; a fabricated one is undetectable and poisons the part it sits in.
3. **An ablation switch.** One flag that turns the contribution off, with **both runs' output**.
4. **Costed.** The demo states what it costs to run — free tier, local, or rented, with the number.

**A source is taught once in the whole curriculum.** 229 days will cite the same handful of
documents repeatedly. The day that **first** needs a source carries its part; every later day cites
it in section 6 and links to that part.

### 20.5 What the hub (`LESSON.md`) must contain

The hub is **orientation and assembly, never the teaching itself.** It carries no `Line by line:`
walkthrough. Required, in this order:

1. **Frontmatter** — `day`, `phase`, `phase_name`, `title`, `ids`, `principles`, `kind`,
   `plan_version`, `parts` (the count), `generated`, `status`, `commit`.
2. **Yesterday / today / tomorrow** — one line each, as a blockquote. No time estimate.
3. **`## §1 Where we are`** — the day's whole idea as a scene, in plain language, before any code
   and before any jargon.
4. **`## §2 The map`** — a table of every part: number, linked title, what it answers, and its
   `level`. Grouped by section, with one line saying what each section means for this day. **No
   minutes column, ever.**
5. **`## §3 Setup — run this`** — every command the day needs, with versions pinned and verified
   that day.
6. **`## §4 Build brief`** — the files to create, with `TODO(me)` markers left **unsolved**. These
   are the reader's; that is the difference between a curriculum and a tutorial.
7. **`## §5 The check that must be able to fail`** — the eval or test that is RED before the TODOs
   are done (Principle 11).
8. **`## §6 Budget`** — model calls per provider in RPM/RPD, GPU hours, and money.
   `0` is an answer; state it (§4).
9. **`## §7 Traps`** — the mistakes that eat an evening.
10. **`## §8 Verify before you build`** — the documentation URLs actually fetched on the day of
    writing (Principle 7).
11. **`## §9 Say it out loud`** — one paragraph, spoken voice, honest, tied to what was
    built. War stories with numbers beat adjectives.
12. **`## §10 Done when`** — pointer to `CHECKLIST.md`. Defined by understanding and green checks,
    **never by elapsed time**.
13. **`## §11 Ledger & commit`** — the verbatim rows that end the day: the `PROGRESS.md` row, any
    `PINS.md`, `SOURCES.md`, `GLOSSARY.md` or `PROVENANCE.md` rows, and the commit message
    `day NNN: <title> — closes <IDs>`. **The hub ends with these.**

### 20.6 The `level` field — how a day climbs

| `level` | The reader at the end of this part |
| --- | --- |
| `foundation` | Knows what the thing *is* and could define it to someone else without using the word itself. |
| `working` | Can use it correctly on their own problem, and recognises its error messages on sight. |
| `production` | Knows what changes when it runs in a real system — scale, concurrency, quota, failure, review — and can defend the choice. |

A day that is all `foundation` is a tutorial. A day that opens at `production` has skipped the
reader. Most days run `foundation → working → production`.

### 20.7 How finely to split

Split by **idea boundaries, never by length or pace**. A part is finished when its one idea is
fully explained — including its production face — and not before.

| Day kind | Split by |
| --- | --- |
| `setup` | one tool, one file, or one command per part |
| `concept` | one claim per part, each with its evidence |
| `lab` (1 ID) | mechanism → behaviour → edge case → failure mode → production use |
| `lab` (2–3 IDs) | one section per ID, plus a synthesis section where they meet |
| `project` | one component per part, in build order |
| `gate` | one acceptance criterion per part |
| **any day whose ideas came from papers** | **one source part per paper**, in `sources/` — added to whatever the row above gives you, never replacing it |

There is deliberately **no target part count and no target length**. If a subject needs four parts
it gets four; if it needs twenty-two it gets twenty-two, and the day simply spans more sittings.
The only wrong answers are a part that carries two ideas and a part that stops before production.

**Every day carries at least one part whose subject is a deliberate failure** — the loss-masked run
that trains fine and answers badly, the injection that gets through, the checkpoint that does not
resume, the eval gate that lets a regression past. Usually at `production` level, where breaking
the thing on purpose is the whole point of the document.

### 20.8 What "in depth" is not

The failure modes this contract exists to prevent, stated so they can be caught in review:

- **Splitting without deepening.** Cutting one long page into six shorter pages changes nothing.
  Each part must *gain* the story, the mechanism, the real failure text and the production face it
  did not have.
- **A mechanism section that is a code dump.** Code with no walkthrough is a listing.
- **A *When it breaks* section with an invented error.** Reconstructed error text is worse than no
  error text, because it teaches the reader to expect a message they will never see.
- **An *In production* section that is a paragraph of advice.** It needs the specific: the number,
  the review comment, the thing that degrades.
- **A hub that teaches.** If the hub explains the mechanism, the parts have nothing left to do.
- **A part with no reader.** Written for the person who already knows it.

### 20.9 Enforcement

Mechanically checked, per day, by `granth.py depth NNN`:

- the folder shape and the numbering, with no gaps;
- every required section present, in contract order;
- a walkthrough after every code block carrying logic;
- a declared `level` on every part, and a day that climbs;
- citations well-formed and present in `SOURCES.md`, and no source taught twice;
- at least one part declaring `failure: true`;
- **no clock, anywhere** — no duration field, no "should take", no pace;
- a hub that assembles rather than teaches;
- the hub's IDs matching §17 exactly.

**Never argue with a depth failure.** Every rule it checks exists because its absence produced a
document nobody could learn from. The checker is a floor, not a standard — a day can pass `depth`
and still read badly, which is what the audit pass is for.

---

## 21 · ✍️ The style guide

### 21.1 The register

Write for a competent engineer who has never met this specific idea. Not for a beginner, and not
for someone who already knows it.

1. **Plain words first.** Say "the model runs out of memory" before you say "OOM under the KV
   cache's linear growth in sequence length". Then say both.
2. **Short sentences.** A sentence carrying three clauses is usually three sentences.
3. **Define jargon on first use, every time, including your own.** "Loss masking", "late
   interaction", "adapter", "trajectory" — all of them get defined the first time each part uses
   them, with a link if an earlier part introduced them.
4. **No enthusiasm as evidence.** "Powerful", "revolutionary", "game-changing" and "seamlessly" are
   deleted on sight. A measured number is the only adjective that survives review.
5. **No person names, no brand-as-praise.** Cite by title and identifier. Tool names are required
   and fine; naming a researcher is not, and a public repository is where that gets noticed.

### 21.2 The scene format

Every part opens with a scene the reader could have been standing in. Not an analogy that needs
explaining before it explains — a situation. A courier who cannot find the flat number. A mechanic
who checks the same six things on every car. A night shift that gets a page at 3am about a queue
that will not drain. One metaphor family per day: two parts reaching for the same setting read as
one idea repeated, so check the day's other parts and the hub's §1 before choosing.

### 21.3 Code and commands

- Every code block gets a `**Line by line:**` walkthrough immediately after it.
- Commands are copy-pasteable and their real output is shown.
- No pseudo-code where real code fits. No `...` standing in for a line the reader needs.
- Every model call handles rate limiting from the first day one is made.

### 21.4 Facts

- Versions, model strings, API surfaces, limits: looked up live, dated, and put in `PINS.md`.
- Citations: looked up live, by title and identifier, and put in `SOURCES.md`.
- Measurements: produced by a command shown in the document, on a machine the document names.
- Anything unverifiable: a `TODO` containing the exact command that would verify it. **Never a
  guess wearing a confident tone.**

### 21.5 The two things that are never written

**A clock.** Not in frontmatter, not in prose, not in a checklist, not as "quick" or "a short
detour". Principle 15.

**A fabricated result.** No invented benchmark number, no reconstructed traceback, no transcript
from a run that did not happen. Principle 10 outranks the shape of the document: a missing output
is completed by one run and is obvious to everyone; a fabricated one is undetectable.

---

## 22 · 🔀 Deviations from the source roadmap

The source roadmap is a syllabus: twenty-four modules and five projects, sequenced for delivery.
This plan is a build order. Four things changed, and each is a decision that can be reversed.

### 22.1 Prompt and context engineering moved earlier

**Roadmap:** modules 22–23, after the agent modules. **Plan:** Phase 12, Days 108–114, before
retrieval and agents.

Every RAG day and every agent day needs prompt structure and context-window vocabulary. Taught
afterwards, those days gesture at ideas they have not introduced. Recorded in `ADR-0002`. Reverse
it by moving Phase 12 to sit between Phases 22 and 23 — it touches no other phase's IDs, which is
why this was the safe reordering to make.

### 22.2 Security distributed into the phases that create the exposure

**Roadmap:** guardrails, PII and policy appear inside the RAG and agent modules. **Plan:** twelve
`SEC` IDs placed at the exact days where a new exposure is created (§14), never in a security
chapter.

Recorded in `ADR-0003`. This is Principle 13 as a plan structure and is the one deviation not
recommended for reversal.

### 22.3 The five projects are one system

**Roadmap:** five projects, the fifth of which wraps the other four. **Plan:** the same, made
structural — `yantra-ship` is the repository, and the four services live inside it from the day
each is born rather than being retrofitted in Phase 23.

The consequence is that Phase 8 already writes a Dockerfile and a smoke test, because Phase 23 will
need them. Retrofitting CI across four services written without it is a week of work that teaches
nothing.

### 22.4 The calendar

The roadmap estimates **7 months at 8 hours a week**. This plan is **229 days**, and a day is a
unit of subject, not of time (Principle 15) — so the honest statement is: at four sittings a week
this runs past a year; at six, closer to nine months.

That gap is real and it is not a mistake in either document. A roadmap week of video is not the
same unit as a day that is written, built, broken on purpose, and defended. **If the calendar is a
hard constraint, cut scope rather than depth** — cutting depth produces days that look finished,
which is the exact failure the whole contract exists to prevent.

**The three levers, in the order they cost least:**

| Lever | Days saved | What you lose |
| --- | --- | --- |
| Park the speech IDs (`VIS-19..24`, Days 106–107) | 2 | Whisper fine-tuning. Nothing else in the plan depends on it (§9). |
| Park MoE to awareness level (`TF-60..66`, Days 31–33) | 3 | The ability to reason about sparse-model serving. Read-only treatment keeps the vocabulary. |
| Merge the vision track to encoder-only (`VIS-01..13`, drop `VIS-14..18`) | 2 | VLM architecture as a build; ColPali on Day 140 then arrives as a black box. Costly — take the first two levers first. |

Anything beyond that is a genuine scope decision, not a trim, and it needs an ADR before Day 1
rather than a quiet edit on Day 90.

---

*End of plan. Amendments go in `docs/CHANGELOG_PLAN.md` with a version bump; structural decisions
go in `docs/adr/`. Never edit a written day to match an amended plan without recording both.*
