---
plan: yantra
version: "v2.0.0"
supersedes: "Yantra v1.1.0 (229 days) · Setu v1.0.0 (180 days)"
source_roadmaps:
  - "Production LLM Engineering — RAG, Agents & Fine-Tuning V1.0"
  - "Becoming an AI Forward Deployed Engineer V1.0"
tracks: 13
ids: 373
days: 182
phases: 29
doc_architecture: "hub + parts/ + sources/ (see §20)"
generated: "2026-09-07"
---

# 🔧 MASTER PLAN v2.0.0 — Project **Yantra**

## Production AI Engineering, delivered — **the model · the platform · the system · the handover**

> **Yantra** (यन्त्र) is an instrument assembled from parts that only work together. That is what
> this curriculum builds: not a shelf of demos, but one system whose fine-tuned model, retrieval
> platform, agent fleet and delivery pipeline all ship through the same gate, to a named client,
> against a baselined number.
>
> 📌 **Purpose:** the single source of truth. Every other document in this repository points back
> here. Where anything disagrees with this file, this file is wrong or the other document is —
> resolve it with an amendment, never by ignoring one of them.

---

## 📑 Table of Contents

| §  | Section |
| --- | --- |
| 1  | 🎬 The vision — one system, thirteen threads |
| 2  | 🧭 Core principles — rules we never break |
| 3  | 🏗️ The product — what Yantra actually is |
| 4  | 💸 Budget & infrastructure policy — **§4.1 the hardware profile · §4.2 the two lanes** |
| 5  | ⚙️ Baseline & the verification rules |
| 6  | 🧶 The thirteen tracks & the ID scheme |
| 7–15 | The tracks, grouped by the thread they carry |
| 16 | 🗺️ The 29 phases |
| 17 | 🗓️ The 182-day map |
| 18 | 🚦 Phase gates & the freshness check |
| 19 | 📒 Ledgers & traceability |
| **20** | **📐 The depth contract — how a day is written** |
| 21 | ✍️ The style guide |
| 22 | 🔀 The merge — what was joined, what was cut, and why |

---

## 1 · 🎬 The vision — one system, thirteen threads

By Day 181 there is **one AI platform, delivered to one client, end to end** — discovered, scoped,
modelled, built, secured, deployed, evaluated, handed over and defended — and you can explain every
decision inside it, say what it costs, name what breaks it, and show the check that catches the
breakage.

This plan is the join of two earlier ones. **Yantra v1.1.0** taught the model: tokenizers,
attention, the KV cache, PEFT, preference alignment, quantization, distillation. **Setu v1.0.0**
taught the delivery: the engagement, production Python, the cloud, identity, integration,
guardrails, the handover. Run separately they cost 409 days and taught the same retrieval, agent,
security and observability material twice. Joined, they cost **182** — and the join is the point,
because neither half is defensible alone.

- A retrieval engineer who cannot fine-tune ships an API wrapper and calls it a platform.
- A model engineer who cannot deploy, secure and hand over ships a notebook and calls it a product.

Three things this plan is trying to prevent:

1. **The tutorial ceiling.** Following steps produces something that runs and understanding that
   evaporates the moment the inputs change. Every subtopic ends at the real-system version, not the
   toy one (Principle 16).
2. **The forgotten middle.** In a curriculum this long, Day 6 is forgotten by Day 140. Every term
   is defined on first use — *including terms from earlier days, with a link back* — and
   `docs/GLOSSARY.md` is a ledger rather than an afterthought.
3. **The unverifiable claim.** Notes written from memory rot silently. Every version, interface,
   citation and measurement is produced or looked up on the day it is used (Principles 7 and 8).

### 1.1 Stated non-goals — decisions, not blind spots

| Excluded | Why |
| --- | --- |
| Pre-training a foundation model from scratch | The compute is not available and the skill does not transfer. `TF-40..43` teach the scaling laws that decide the size; `FT-06` teaches continued pre-training, which is the part you will actually do. |
| Building a vector database, a serving engine or an inference kernel | You will read PagedAttention and Flash Attention closely enough to explain them (`TF-30`, `TF-35`) and then use the implementations, because that is what production does. |
| Training a frontier reasoning model with RL at scale | `FT-47..49` teach the recipe and what skipping supervised fine-tuning cost. The run itself is a compute problem, not a curriculum problem. |
| Speech and speech-to-text | Cut in the merge, recorded in [`ADR-0006`](adr/ADR-0006-the-merge.md). It fed no part of the delivered system, and v1.1.0 had already named it the first thing to cut. |
| A front end for any service | Every service ends at an HTTP API, a Slack surface and an approval screen. A polished web client is real work and is deliberately not this work. |
| Multi-cloud portability | One cloud done properly beats three done shallowly. AWS, because both source roadmaps deploy there. Azure and GCP appear only where a client would force the comparison. |
| A managed agent runtime as a taught product | Parked. Containment is taught through the mechanism — containers, policy, sandboxes, identity — rather than through one vendor's runtime, which dates faster than anything else here. |

---

## 2 · 🧭 Core principles — rules we never break

1. **Doc-first.** The day document is written before any code; the code follows the doc.
2. **One day, one commit.** Traceable, append-only history. The repository is the memory.
3. **Simple language and a concrete example, always.** A concept that cannot be explained plainly
   with an example is a concept that is not yet understood. §21 enforces this.
4. **Build first, adopt after.** Hand-roll the mechanism once — attention, the KV cache, the tool
   executor loop, the KL divergence loss, RRF fusion — *then* reach for the framework, so the
   framework is a convenience and never a mystery. This is why Day 61 writes attention before
   Day 65 uses vLLM, and why Day 119 writes an executor loop before Day 126 uses LangGraph.
5. **Every concept is load-bearing.** If removing it would not break the delivered system, it does
   not get a day. "Is this load-bearing?" has a mechanical answer here: delete it and see whether
   the artifact still works.
6. **Verify the whole system after every step.** Each day ends with the full check suite green, not
   just today's snippet.
7. **Never invent a fact.** Versions, model strings, API surfaces, limits and citations are looked
   up **live on the day they are used**, with a dated ledger row. A lookup that fails leaves a
   `TODO` containing the exact command — never a guess. A remembered citation is an invented
   citation.
8. **Measure, then claim.** No day asserts a speedup, a quality gain or a cost saving it has not
   measured on its own machine, with the command shown. "Roughly 2× faster" with no benchmark is a
   rumour with a number attached.
9. **Secrets never touch git.** `.env` and `.gitignore` exist before the first key does. The
   repository goes public at the defence, so the discipline is real.
10. **Fail honestly.** Errors surface, escalate and are logged. Never fabricate an output to cover
    a failed run — this applies to the writer of the day as much as to the agents being built.
11. **Evals are tests.** A behaviour change without a green evalset does not merge. Every day ends
    with at least one check that can go **red**.
12. **If reality changes, the plan is amended first.** A renamed API, a superseded spec, a provider
    that dropped its free tier → amend the plan and log it in `docs/CHANGELOG_PLAN.md`, *then*
    continue. Days are never silently patched.
13. **Blast radius before capability.** Every new power — code execution, a database write, a Jira
    transition, a payment — arrives together with its containment story. This is why `SEC` IDs sit
    inside the phases that create the exposure rather than in a chapter at the end.
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
17. **Two lanes, one contract.** Any day that spends money is written for both the $0 lane and the
    managed lane, and `In production` covers both. §4.2.

> Principles 14–16 are made concrete by **§20, the depth contract**, and are enforced mechanically
> by the depth checker and by reading.

---

## 3 · 🏗️ The product — what Yantra actually is

**One client, fixed on Day 3, and never a framing device.** A mid-size general insurer drowning in
claims paperwork: forty-two thousand claims a month, 7.5 days to settle one, four hundred policy
documents, three regional centres that triage inconsistently, and a failed vendor chatbot already
in the room. Every later day builds against *its* documents, *its* permissions model and *its* KPI.
The corpus is synthetic, generated on Day 4 and version-controlled, so a scan-quality problem is
reproducible instead of anecdotal. **No real client data, ever.**

One repository, one CI pipeline, four things shipped through it.

| Service | What it is | Phase | The tracks that feed it |
| --- | --- | --- | --- |
| `yantra-model` | A domain-adapted claims model: QLoRA SFT then DPO, judged against a calibrated evaluator, distilled to a GGUF student, served with hot-swappable adapters | 14 | `TF`, `FT` |
| `yantra-platform` | The retrieval platform: hybrid dense + BM25 + late-interaction search, a Neo4j graph, page-image retrieval over scans, an adaptive router, reranking, RAGAS-gated, RBAC-scoped, guardrailed, deployed to a private subnet | 25 | `RAG`, `VIS`, `ENT`, `SEC` |
| `yantra-agents` | A multi-agent compliance and operations system: a supervisor delegating to MCP-backed specialists, human approval on every write, trust boundaries that are enforced rather than documented | 26 | `AGT`, `SEC` |
| `yantra-ship` | The LLMOps shell over all three: golden suites, eval-gated CI, cost and latency regression guards, blue/green deploys with auto-rollback | 27 | `OPS` |

And the half that is not code, delivered alongside it: the discovery notes, the baselined KPI, the
scoped SOW, the data classification, the architecture diagram a CIO signs, the evaluation report,
the UAT runbook, the ROI deck, the runbooks, the handover, and the case study a hiring panel reads
to the end. That is the `FDE` track, and it is why this is a delivery rather than a build.

**The system-level test is one sentence, and it is what the defence defends:** a prompt, model or
retrieval change in any service must be blocked by the pipeline when it makes that service worse,
and must reach a live endpoint when it does not — without a human deciding which of those two
happened.

Everything in this plan is either a component of that sentence or the understanding required to
build the component. §1.1 lists what that excludes.

---

## 4 · 💸 Budget & infrastructure policy

The two source plans each solved half of this, and the merge keeps both halves because they answer
different questions. **§4.1, the hardware profile,** answers *what machine is this training day run
on.* **§4.2, the two lanes,** answers *who is paying for the infrastructure this day needs.* A day
can need an answer to one, both, or neither, and its hub says which.

| Resource | Where it first becomes non-optional | Substitution if you do not have it |
| --- | --- | --- |
| A GPU with ≥16 GB VRAM | Phase 11 (Day 76, QLoRA on a real base) | `YANTRA_PROFILE=laptop` runs the day at CPU scale (§4.1). Free notebook tiers carry Phases 8–10 comfortably; rent by the hour from Phase 11 |
| A GPU with ≥24 GB VRAM | Phase 14 (Day 92, the two-stage run on an 8B base) | **No honest laptop path** (§4.1). Rent hourly; the day teaches the number, not the vibe |
| A cloud account | Phase 6 (Day 39) | LocalStack carries the identity, storage and networking days in Lane A (§4.2). Fargate, RDS and a real VPC are Lane B. Arm a spend alarm before the first deploy, not after |
| A managed vector store | Phase 25 (Day 162) | Qdrant, Elasticsearch and Neo4j all run in Docker; the plan assumes local until the project phase |
| Paid frontier API access | Phase 5 (Day 33) | Free tiers with rate-limit handling. Any day that calls a model states its request budget in the hub |

**Four rules follow from this table and are binding:**

1. **Every hub declares a request budget** (§20.5, hub section 6): model calls, per provider, in
   requests per minute and per day. `0` is a valid answer and must be stated.
2. **Every day that spends money says so, in the hub, before the first command** — which resource,
   for roughly what, and what the cheaper path costs in capability.
3. **Rate-limit handling is curriculum, not friction.** Every call path handles HTTP 429 with
   `retry-after` and backoff from the first call it makes. This is not defensive programming; it is
   the same code the production services will need.
4. **Licences before downloads.** Any day introducing a dataset or a pre-trained checkpoint states
   its licence and whether it permits this use, with the row in `docs/PROVENANCE.md` **before** the
   download.

### 4.1 The hardware profile

**The default hardware assumption of this curriculum is a laptop with no GPU.** The accelerated
path is the documented alternative, not the baseline.
[`ADR-0005`](adr/ADR-0005-the-hardware-profile.md) records why.

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

**Three further rules follow, binding on every day from 1 to 181:**

5. **A day that touches an accelerator states both paths in its §6 budget** — what the laptop path
   costs in *capability*, and what the accelerated path costs in *money*. Neither line is optional
   and neither is a range: the laptop path names the base model and the scale it runs at.
6. **Every measured number carries the profile that produced it**, in the document and in the
   `PROGRESS.md` row. A number without a profile is not a number (Principle 8).
7. **The laptop path is a smaller true version of the day, never a mocked one.** Same mechanism,
   same code path, same check going red — fewer steps, a smaller base, a shorter sequence. A day
   whose laptop path skips the mechanism does not have a laptop path; it has a stub, and the honest
   form of that is a `TODO(me)` in the hub saying the day needs an accelerator.

**The days with no honest laptop path** say so in their hubs rather than pretend: Day 76 (QLoRA on
a real base), Day 92 (the two-stage project run) and Day 162 (the managed vector store). Their
parts are still readable and their mechanisms still hand-rolled at laptop scale; it is the day's
headline measurement that waits for the hardware.

### 4.2 The two lanes

Every day that touches paid infrastructure is written twice: **Lane A ($0)** and **Lane B
(managed)**. The lanes are not an appendix — they are part of the depth contract, and
`In production` must cover both.

| | Lane A — $0 | Lane B — managed |
| --- | --- | --- |
| Models | Free-tier provider quotas; open weights locally via Ollama, llama.cpp or vLLM | Paid provider APIs, a managed model service |
| Vectors | Qdrant in Docker; pgvector on local Postgres | A managed index |
| Graph | Neo4j Community in Docker | Neo4j Aura |
| Compute | Docker Compose on a laptop; LocalStack for cloud surfaces | ECS Fargate, RDS, a real VPC |
| Tracing | Langfuse self-hosted | LangSmith, Langfuse Cloud |
| CI | GitHub Actions free tier | the same, with paid runners |

Lane A exists because most people learning this cannot expense a cloud bill, and because an
engineer who has only ever run managed services cannot answer the question every client eventually
asks: *what does this cost us, and what happens if we bring it in-house?* Lane B exists because the
job is deploying into a client's real tenant, and LocalStack has never once billed anyone by
surprise.

**Where the lanes genuinely diverge, say so.** A NAT gateway bill, a Fargate cold start and a
managed index's p99 have no honest Lane A equivalent. On those days Lane A is explicitly an
*approximation*, the document names the behaviour it is not reproducing, and the ID still closes —
parking a thing in the open is the opposite of a gap.

---

## 5 · ⚙️ Baseline & the verification rules

This curriculum sits on a stack that moves. Rather than pin versions in a document that will be
read for a year, the plan pins **the verification behaviour** and puts the versions in a dated
ledger.

| What | Pinned to | Verified how | Re-checked |
| --- | --- | --- | --- |
| Python | 3.12, owned by `uv`; `tomllib` from stdlib | `uv run python --version` | every phase gate |
| Every runtime dependency | the lockfile, and a dated row in `docs/PINS.md` naming the day that added it | `uv lock --check`, plus the version command recorded in the pin row | every phase gate, and on any day that adds one |

**The rules, in force from Day 0:**

1. **Never invent a version.** Any day that installs something states the version it verified and
   how, or leaves a `TODO` containing the exact lookup command. The row lands in `docs/PINS.md`
   the same day, with the date observed.
2. **Never invent an API surface.** Any part that uses a library symbol, a flag, an endpoint or a
   field names the documentation page checked *that day*, inline, next to the code: *"Verified
   against `<url>` on YYYY-MM-DD."* This binds hardest on the fast-moving surfaces — the serving
   engines, LangGraph, MCP, the cloud console. If the live documentation disagrees with this plan,
   **stop and propose an amendment**; do not adapt silently.
3. **Never invent a citation.** A paper is looked up live, its title copied from the record rather
   than from memory, and the identifier lands in `docs/SOURCES.md` with the date it was checked.
   **Cite by title and identifier, never by author.** A wrong version number fails loudly the next
   time someone installs; a plausible identifier attached to the wrong title survives for years.
4. **Never invent a benchmark number.** Every latency, throughput, memory or quality figure in a
   day is one you measured, with the command that produced it shown and the machine named. A number
   you read somewhere is a citation, and gets cited.
5. **The five moving surfaces get re-checked at every phase gate** (§18): serving engines and
   quantization formats; MCP and the agent frameworks; the cloud surfaces; provider free tiers and
   model identifiers; and the guardrail and evaluation libraries.

**What this replaces.** It replaces a version table that would be wrong within a month. `PINS.md`
is the version table, it is dated, and it is append-only — so when something breaks you can see
what was true when the day was written.

---

## 6 · 🧶 The thirteen tracks & the ID scheme

Every concept in this plan has an ID. A day **closes** an ID when the concept is built into — or
demonstrably exercised against — the delivered system and the day's checks are green.
`docs/TRACEABILITY.md` is regenerated from the day hubs; **any open ID from a completed phase is a
bug**, not a backlog item.

<!-- granth:tracks:start -->
| Track | Prefix | Count | Thread |
| --- | --- | --- | --- |
| Software & backend engineering | `SE` | 34 | Python that survives a long-running process, async, Linux, FastAPI, testing, packaging, and the repository discipline every later track assumes. |
| Cloud, containers & delivery | `CLD` | 22 | Identity and networking, object storage and managed databases, secrets, Docker, Fargate, CI/CD, infrastructure as code, and the cost model you show the client. |
| Prompt & context engineering | `CTX` | 16 | The model as a pinned dependency: tokens, the meter, sampling, prompt anatomy, structured output, robustness, and the failure lab. |
| Transformer internals & efficiency | `TF` | 43 | Architecture from tokens to experts: tokenizers, embeddings, attention, the block, the KV cache, attention variants, RoPE, scaling laws, MoE. |
| Fine-tuning, alignment & compression | `FT` | 57 | The post-training pipeline in the order a practitioner runs it: lifecycle, data, PEFT, SFT, preference alignment, evaluation, quantization, serving, distillation. |
| Embeddings & retrieval | `RAG` | 43 | The embedding taxonomy, MRL, chunking, the three retrieval families, fusion, reranking, evaluation, adaptive retrieval, graph retrieval, caching. |
| Vision & multimodal | `VIS` | 9 | OCR and its failure modes, ViT, contrastive and self-supervised encoders, VLM architecture, and retrieval directly over page images. |
| Agents, protocols & orchestration | `AGT` | 38 | Function calling, the hand-rolled loop, tool design, MCP as a real boundary, LCEL, LangGraph, state, memory, supervisors and human-in-the-loop. |
| Enterprise integration & identity | `ENT` | 18 | The systems a client already runs — SQL, Oracle, SOAP, SFTP, Slack, Jira — and the OAuth, SSO, RBAC and audit trail that let AI touch them. |
| Security & governance | `SEC` | 15 | The threat model AI adds, injection and exfiltration, PII handling, guardrails as defence in depth, policy, sandboxing, and breaking your own system on purpose. |
| Observability, evaluation & LLMOps | `OPS` | 25 | Tracing, structured logs, token accounting, latency budgets, the gateway, evaluation harnesses, judges, golden sets, eval-gated CI, and deployment strategy. |
| FDE consulting craft | `FDE` | 17 | Discovery, the KPI, the SOW, stage gates, change management, handover, ROI, and the interview loop — the half of the job that is not code. |
| The delivered system | `PRJ` | 36 | `yantra-model`, `yantra-platform`, `yantra-agents` and `yantra-ship` — the milestones that put every other track into a running system. |

**Total: 373 concept IDs across 182 days (2.05 per day).**
<!-- granth:tracks:end -->

> 🅿️ Some IDs are **parked**: you learn the map, you do not build the thing. A parked ID is marked
> 🅿️ in the day hub and closes normally. Parking is a decision that gets written down, not a way of
> quietly skipping something.

The per-ID meaning lives in the day map (§17): **each day's row is the authoritative statement of
what its IDs mean.** Sections 7–15 give each track's arc and call out the decisions inside it.

---

## 7 · 🐍 Track SE — Software & backend engineering (`SE-01..34`)

**Arc.** The language under pressure (`SE-01..12`) → concurrency and the box it runs on
(`SE-13..24`) → the service boundary (`SE-25..34`).

This track is first for one reason: **everything after it writes Python that has to survive.** A
retrieval pipeline that leaks memory over a week, an agent whose exception vanishes inside a
`gather`, a container that runs as root — those are not AI problems, and they are what actually
takes an AI system down.

**Three decisions worth naming:**

- **Memory and the event loop get full days** (`SE-02`, `SE-13..19`) rather than a paragraph. The
  two most expensive bugs in a long-running AI service are a reference nobody released and a
  blocking SDK call inside the loop, and both are invisible in a test that runs once.
- **Pydantic is taught as a boundary, not a schema library** (`SE-05`, `SE-06`). It arrives on
  Day 10 and is then load-bearing on every structured-output day, every tool schema and every API
  model for the rest of the plan.
- **Tests come before the framework that needs them** (`SE-33`, `SE-34`). The contract test written
  on Day 29 is the same shape as the eval gate on Day 160.

---

## 8 · ☁️ Track CLD — Cloud, containers & delivery (`CLD-01..22`)

**Arc.** Identity and the network (`CLD-01..06`) → state and money (`CLD-07..11`) → images,
runtime and the pipeline (`CLD-12..22`).

**Two decisions worth naming:**

- **Networking before compute.** The VPC, the two firewalls and the egress path come before
  Fargate, because the failure everyone hits — *the service starts and cannot reach the model
  provider* — is a routing failure, and it is unreadable to anyone who met the private subnet after
  the container.
- **The budget alarm is armed on Day 46, before the first deploy on Day 51.** A cost model
  presented to a client after the first invoice is not a cost model; it is an apology.

---

## 9 · 💬 Track CTX — Prompt & context engineering (`CTX-01..16`)

The model as a **pinned dependency with a price and a rate limit**, met before it is opened up.

**This ordering is deliberate and it is the single biggest structural decision in the merge.**
Days 30–38 use the model as a black box — tokens, the meter, sampling, prompt anatomy, structured
output, the failure lab — and only then, from Day 53, does the plan take it apart. Every question
the black-box days raise (*why does it cost that? why did that number change? why did the JSON come
back truncated?*) is answered by a mechanism in Track TF. Teaching internals first inverts that and
produces a reader who can derive attention but cannot get a parse to hold.

**Arc.** The meter and the window (`CTX-01..04`) → the call and the provider layer (`CTX-05..07`)
→ prompt anatomy and reasoning (`CTX-08..11`) → structured output and robustness
(`CTX-12..16`).

Day 38 builds a prompt robustness test that goes red. That test is not a teaching exercise — it
becomes the golden baseline the CI gate checks against on Day 174.

---

## 10 · 🧮 Track TF — Transformer internals & efficiency (`TF-01..43`)

**Arc.** Tokens before embeddings, embeddings before attention, attention before architectures
(`TF-01..25`) → then the same machine from the serving side: what it costs to run, and every trick
the field invented to make it cost less (`TF-26..43`).

The track splits at Day 62. Everything before it answers *how does a transformer work*; everything
after answers *why does it cost that much, and what did we change*. That boundary matters because
the second half is only teachable once the first half is in your hands: grouped-query attention is
a sentence if you have not written multi-head attention, and a decision with a measured price if
you have.

**Three decisions worth naming:**

- **Tokenization gets three days** (`TF-03..08`), more than most treatments give it, because
  tokenizer choices surface later as unexplained failures — a fine-tune that will not learn digits,
  a chunk boundary that splits a clause, a multilingual cost nobody budgeted.
- **Attention is written by hand before it is optimized** (Principle 4). Day 61 produces a block
  that trains. Days 62–67 make it fast, and every optimization is measured against the hand-rolled
  baseline rather than against a claim.
- **Scaling laws and MoE close the track** (`TF-40..43`) rather than opening the fine-tuning one,
  because their subject is a sizing decision — the one you make *before* you spend money on
  Day 76.

---

## 11 · 🎯 Track FT — Fine-tuning, alignment & compression (`FT-01..57`)

The largest track and the spine of Phases 10–14. It runs the whole post-training pipeline in the
order a practitioner runs it: understand the lifecycle, build the data, adapt the model, align it,
evaluate it, shrink it, serve it — then the same thing in the other direction, compressing a large
model into a small one.

**Arc.** Lifecycle and data (`FT-01..15`) → parameter-efficient adaptation and alignment
(`FT-16..33`) → evaluation, quantization and serving (`FT-34..46`) → reasoning, small models and
distillation (`FT-47..57`).

**Four decisions worth naming:**

- **Data comes before method** — six days of lifecycle, formats, loss masking and synthetic
  generation before the first LoRA. This inverts the usual order deliberately. A QLoRA run on a bad
  dataset teaches you how to run QLoRA; the failure it produces teaches nothing, because you cannot
  tell the method from the data.
- **Loss masking gets its own day** (`FT-10`, `FT-11`, Day 72) with a deliberately broken run. It
  is the single most common silent fine-tuning bug, it produces a model that trains without error
  and answers badly, and it is invisible in a loss curve.
- **Evaluation is inside the track, not after it** (`FT-34..38`). A fine-tune you cannot measure is
  a fine-tune you cannot defend, and the judge built on Day 82 is the same judge the CI gate uses
  on Day 175.
- **Distillation is taught as the mirror of fine-tuning**, not as an appendix. The student–teacher
  paradigm is the same optimization problem seen from the other side, and Day 88 builds the loss
  from scratch so that the project phase is an application rather than a first encounter.

---

## 12 · 🔍 Tracks RAG & VIS — Retrieval, graph & multimodal (`RAG-01..43`, `VIS-01..09`)

**Arc.** The embedding taxonomy and MRL (`RAG-01..08`) → chunking and RAG by hand (`RAG-09..12`)
→ the three retrieval families and fusion (`RAG-13..23`) → evaluation and adaptive retrieval
(`RAG-24..33`) → the graph (`RAG-34..40`) → the page that is an image (`RAG-41..43`,
`VIS-01..09`).

**Four decisions worth naming:**

- **Embeddings are taught before RAG, not inside it** (Days 95–97). Retrieval quality is an
  embedding property first and a pipeline property second, and a reader who meets embeddings as
  "the thing before the vector store" never goes back to fine-tune one.
- **BM25 gets a full day** (`RAG-15`, Day 101) and is measured against dense retrieval on your own
  corpus. The hybrid result on Day 103 is only interesting if the lexical baseline was real.
- **Evaluation arrives before the clever variants** (`RAG-24..27` on Days 105–106, before Self-RAG
  and Corrective RAG on Day 107). Adaptive retrieval strategies are indistinguishable from each
  other without a metric.
- **The vision track exists for exactly one reason** — the client's claim bundles are scans, and
  page-image retrieval is a vision-language model doing retrieval. A reader who has not built a
  patch embedding cannot debug it when quality drops on rotated pages. Nine IDs, placed immediately
  before they are needed, and not one more.

---

## 13 · 🤖 Track AGT — Agents, protocols & orchestration (`AGT-01..38`)

**Arc.** Function calling and schema design (`AGT-01..07`) → the hand-rolled loop and where it
breaks (`AGT-08..12`) → MCP as a real boundary (`AGT-13..19`) → LCEL and LangGraph
(`AGT-20..30`) → context, supervisors and human-in-the-loop (`AGT-31..38`).

**Three decisions worth naming:**

- **The loop is hand-rolled on Day 119 and breaks on Day 120, and LangGraph does not appear until
  Day 126.** Principle 4, and it is the difference between an engineer who can debug a stuck ReAct
  loop and one who can only restart it.
- **MCP is taught as a boundary, not an import.** The point of `AGT-13..19` is that a tool
  boundary you can authenticate, authorize and audit is a different object from a Python function
  you called, and Day 124 makes the trust boundary explicit before any agent gets a credential.
- **Human-in-the-loop is a design day, not a feature day** (`AGT-36..38`). An approval surface a
  busy professional rubber-stamps is worse than no approval, because it launders the risk. That is
  taught where the approval gate is built, not in the security phase.

---

## 14 · 🛡️ Tracks ENT & SEC — Enterprise integration, identity & security (`ENT-01..18`, `SEC-01..15`)

**`ENT` is the track that makes this a job rather than a project.** The client already runs SQL
Server, an Oracle box, a SOAP endpoint from 2003, an SFTP drop, Slack and Jira. An AI system that
cannot reach them is a demo, and the reason most pilots die is not model quality — it is that
nobody could get the data out or the answer back in.

**`SEC` has fifteen IDs and none of them are in a security phase.** They sit inside the phases that
create the exposure:

| IDs | Subject | Sits inside |
| --- | --- | --- |
| `SEC-01` | MCP trust boundaries and authorization | Phase 18, where an agent first gets a tool |
| `SEC-02` | The query you must never let reach the database | Phase 20, with text-to-SQL |
| `SEC-03..07` | Threat model, injection, exfiltration, jailbreaks | Phase 22, before anything is exposed |
| `SEC-08..11` | PII, masking, and guardrails as defence in depth | Phase 22, with the request path |
| `SEC-12..13` | The red team, and the attempts put into CI | Phase 22, as the phase gate |
| `SEC-14..15` | Policy enforcement and sandboxed execution | Phase 26, before the agent gets write access |

**Every SEC day carries the attack before the defence.** A guardrail you have not got past is a
guardrail you cannot evaluate.

---

## 15 · 📦 Tracks OPS, FDE & PRJ — Operations, craft & the delivered system (`OPS-01..25`, `FDE-01..17`, `PRJ-01..36`)

**`OPS` is concentrated in Phases 23–24 for one reason: an evaluation harness is only teachable
against systems that exist.** By Day 150 there is a fine-tuned model and a retrieval platform with
real failure modes, real cost profiles and real prompts worth regression-testing. Teaching harness
engineering on a toy in Phase 4 would produce a chapter nobody could apply. Two IDs live outside
the phase — `OPS-24` and `OPS-25` on Day 177 — because blue/green and auto-rollback are only
meaningful with something deployed to roll back.

**`FDE` brackets the plan.** Eight IDs at the start (Days 1–5), because you cannot decide what is
load-bearing without a client, a process and a baselined number; nine at the end (Days 161–181),
because discovery, ROI and handover are only teachable once there is something to hand over.

**`PRJ` is not a set of concepts — it is a set of milestones in a running system**, and one closes
when the milestone is deployed and traced, not when it is understood.

| Deliverable | IDs | Phase | Days | The thing that must be true at the gate |
| --- | --- | --- | --- | --- |
| `yantra-model` | `PRJ-01..07` | 14 | 90–94 | A live endpoint serving two adapters, and a report comparing base vs SFT vs SFT+DPO with the judge's calibration shown |
| `yantra-platform` | `PRJ-08..17` | 25 | 161–167 | An adaptive router across three retrievers behind a private endpoint, passing a RAGAS gate, answering differently for two users with different roles |
| `yantra-agents` | `PRJ-18..26` | 26 | 168–173 | Findings traceable to evidence, human approval on every write, a blocked destructive call in a trace, per-audit cost known |
| `yantra-ship` | `PRJ-27..33` | 27 | 174–177 | A pull request blocked by a failing eval, and a deployment rolled back automatically |
| The defence | `PRJ-34..36` | 28 | 180–181 | One request traced through every service; the cost model; a stranger clones the repository and reaches a working system without asking you anything |

**A project phase is written to the same depth contract as every other phase.** It is not a "now
build it" week. Each day still has parts, still opens where a reader can stand, still ends in
production, and still carries a deliberate failure. The difference is that its subject is a
component of a running system rather than an idea.

---
## 16 · 🗺️ The 29 phases

A phase is a block of days that share a subject and end in one thing that must be true. The gate is
not a quiz — it is an artifact or a measurement, and it is either there or it is not.

<!-- granth:phases:start -->
| Phase | Days | Theme | Gate |
| --- | --- | --- | --- |
| **0** | 0 | Foundry | `granth.py check` green; one commit; no secret in git |
| **1** | 1–5 | The engagement — before any code | A scoped SOW for one real process, with a baselined KPI, a named owner and a stated exit condition |
| **2** | 6–14 | Python for production | A packaged, typed, logging service module installs clean from the lockfile on a bare box |
| **3** | 15–21 | Async, concurrency & Linux | A blocking third-party call runs inside the loop without stalling it, proved under load |
| **4** | 22–29 | Modern API development | The service streams, versions, and fails with a machine-readable body; tests go red first |
| **5** | 30–38 | The model as a dependency | Structured output parses on 200 consecutive real inputs, or fails loudly and is counted |
| **6** | 39–46 | Cloud fundamentals & networking | A private subnet reaches the model provider and nothing reaches it; budget alarm armed |
| **7** | 47–52 | Containers & CI/CD | A tagged image ships to a container runtime through a pipeline that refuses a red test |
| **8** | 53–61 | The transformer, taken apart | A decoder block you wrote passes a shape-and-gradient test and trains |
| **9** | 62–67 | Inference optimization & scale | Measured tokens/sec before and after the cache, on your own machine, with the profile named |
| **10** | 68–73 | Post-training: the lifecycle and the data | A domain SFT dataset, deduplicated and loss-masked, with the broken run kept beside it |
| **11** | 74–80 | PEFT, SFT & preference alignment | One base model, two adapters, a measured preference win |
| **12** | 81–85 | Evaluation, quantization & serving | A quantized checkpoint served with two hot-swappable adapters, and a judge you calibrated |
| **13** | 86–89 | Reasoning, small models & distillation | A student that closes most of the gap at a fraction of the cost |
| **14** | 90–94 | `yantra-model` — the domain model, shipped | Live endpoint; base vs SFT vs SFT+DPO report; the GGUF student benchmarked against the teacher |
| **15** | 95–104 | Embeddings & retrieval | Hybrid + rerank beats the vector-only baseline on a golden set, with the number recorded |
| **16** | 105–108 | Retrieval evaluation & adaptive RAG | A faithfulness gate you cannot pass by luck |
| **17** | 109–115 | Graph & multimodal retrieval | A relationship question the vector index cannot answer, and a scanned page it could not read, both answered and cited |
| **18** | 116–124 | Agents — tools, the loop & MCP | An MCP server and client you wrote, talking to each other across an authenticated boundary |
| **19** | 125–132 | LangGraph — state, memory & multi-agent | A graph that survives a `kill -9` and resumes at the interrupt with no duplicated side effect |
| **20** | 133–138 | Enterprise integration | A round trip through a SOAP endpoint and a Jira write, both idempotent under retry |
| **21** | 139–143 | Identity & access | Two users with different roles ask the same question and get correctly different answers |
| **22** | 144–149 | Security & guardrails | A documented red-team suite runs in CI; every attempt is contained and logged |
| **23** | 150–154 | Observability & the gateway | One trace explains a bad answer end to end, and cost is attributable per tenant |
| **24** | 155–160 | LLMOps — harness, evals & CI gating | A pull request blocked by a failing eval, with the score delta commented on it |
| **25** | 161–167 | `yantra-platform` — the retrieval platform, delivered | Deployed in a private subnet, RAGAS gate green, UAT signed off against the Phase 1 baseline |
| **26** | 168–173 | `yantra-agents` — the multi-agent system, delivered | Findings traceable to evidence, a destructive call blocked by policy in a trace, per-audit cost known |
| **27** | 174–177 | `yantra-ship` — the LLMOps shell and the deploy | Blue/green deploy with an auto-rollback you triggered on purpose |
| **28** | 178–181 | Handover, ROI & the defence | A stranger clones the repository and reaches a working system without asking you anything |
<!-- granth:phases:end -->

**Every phase gate also includes the freshness check (§18.2).** Phase 0 has nothing pinned yet, so
its freshness check is empty — but it still has a gate.

---

## 17 · 🗓️ The 182-day map

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

### Phase 1 — The engagement (Days 1–5)

*the client, the process, the number, the scope*

| Day | Title | IDs closed |
| --- | --- | --- |
| 1 | What a forward deployed AI engineer actually owns — the last mile between a model demo and a system a business runs on Monday | FDE-01, FDE-02 |
| 2 | The demo-to-production gap — why the vendor chatbot passed on sample documents and died on real scans | FDE-03 |
| 3 | Discovery — shadowing the work, mapping the process as it is rather than as the org chart says, and finding the KPI that pays | FDE-04, FDE-05 |
| 4 | Auditing the data before promising anything — five hundred records, and the versioned synthetic corpus every later day is built against | FDE-06 |
| 5 | The scoped SOW and the stage gates — POC, pilot, production, and the one sentence that stops scope creep six weeks later | FDE-07, FDE-08 |

### Phase 2 — Python for production (Days 6–14)

*the language under pressure*

| Day | Title | IDs closed |
| --- | --- | --- |
| 6 | Data structures as decisions — what list, dict, set and tuple actually cost at a million rows | SE-01 |
| 7 | Memory management — references, the cycle collector, and where a long-running service quietly leaks | SE-02 |
| 8 | Objects that model a domain — composition, protocols, and when a class is the wrong answer | SE-03 |
| 9 | Type hints a checker can enforce — and the annotation that lies | SE-04 |
| 10 | Pydantic as the boundary — validating everything that enters the process, exactly once | SE-05, SE-06 |
| 11 | Exceptions that carry context — the hierarchy, and never swallowing a traceback | SE-07 |
| 12 | File I/O, encodings, and the streaming read that does not eat the box | SE-08 |
| 13 | Packaging and environments — uv, the lockfile, and an install that reproduces on a stranger's machine | SE-09 |
| 14 | Project structure and structured logging — a layout that scales, and a log line an operator can grep at 3 a.m. | SE-10, SE-11, SE-12 |

### Phase 3 — Async, concurrency & Linux (Days 15–21)

*the loop, the GIL, and the box you did not build*

| Day | Title | IDs closed |
| --- | --- | --- |
| 15 | The event loop from the inside — what `await` actually suspends, and what it does not | SE-13, SE-14 |
| 16 | Coroutines and tasks — fan-out, gather, and the exception that vanishes without a trace | SE-15, SE-16 |
| 17 | Async context managers, and the connection that must be released even when the request dies | SE-17 |
| 18 | Concurrency vs parallelism — the GIL, and the executor bridge for the blocking SDK you cannot avoid | SE-18, SE-19 |
| 19 | The filesystem and the process table — navigating a box you did not build | SE-20 |
| 20 | Permissions, users, and the container that runs as root because nobody said otherwise | SE-21, SE-22 |
| 21 | Shell for operators and configuration precedence — `set -euo pipefail`, and proving where the value actually came from | SE-23, SE-24 |

### Phase 4 — Modern API development (Days 22–29)

*the service boundary*

| Day | Title | IDs closed |
| --- | --- | --- |
| 22 | HTTP semantics an API owner cannot get wrong — methods, status codes, and idempotency | SE-25 |
| 23 | FastAPI: the first endpoint, and exactly what the framework is doing on your behalf | SE-26 |
| 24 | Request and response models — schemas at both boundaries, and the field you must never echo | SE-27 |
| 25 | Dependency injection — the seam that makes a service testable instead of mockable | SE-28 |
| 26 | Errors that surface rather than swallow — handlers, and an error body a client can act on | SE-29 |
| 27 | Streaming responses and server-sent events — the first token in 300 ms, and the disconnect | SE-30 |
| 28 | Versioning and deprecation without breaking the client who never reads email; GraphQL and when it is genuinely the right answer | SE-31, SE-32 |
| 29 | Pytest that means something, contract tests, and the OpenAPI schema as the agreement between two teams | SE-33, SE-34 |

### Phase 5 — The model as a dependency (Days 30–38)

*tokens, the meter, the prompt, the parse*

| Day | Title | IDs closed |
| --- | --- | --- |
| 30 | Tokens and the meter — what you are actually billed for, measured rather than assumed | CTX-01 |
| 31 | The context window as a desk that gets wiped between every call — recency bias and the lost middle | CTX-02, CTX-03 |
| 32 | Sampling — temperature, top-p, and why "set it to zero" is stability, not reproducibility | CTX-04 |
| 33 | The first raw API call, pinned to a version you chose, behind a provider layer you can swap | CTX-05, CTX-06 |
| 34 | System prompts and instruction design that survives a model swap | CTX-07 |
| 35 | Anatomy of a prompt — zero-, one- and few-shot, and the examples that teach the wrong thing | CTX-08, CTX-09 |
| 36 | Chain-of-thought, step-back, decomposition and self-refinement — and the thinking-token tax nobody budgets for | CTX-10, CTX-11 |
| 37 | Structured output — JSON schema, Pydantic and grammars, and the parse that must not fail silently | CTX-12, CTX-13 |
| 38 | Prompt fragility and the failure lab — a robustness test that goes red, then truncation, refusal, rate limit and malformed JSON at 3 a.m. | CTX-14, CTX-15, CTX-16 |

### Phase 6 — Cloud fundamentals & networking (Days 39–46)

*identity, the network, state, and the bill*

| Day | Title | IDs closed |
| --- | --- | --- |
| 39 | The shared responsibility model — what the cloud is actually selling, and what stays yours | CLD-01 |
| 40 | Identity and roles — and the policy that is quietly too broad | CLD-02 |
| 41 | Least privilege in practice — scoping a role to one bucket, one prefix, one action | CLD-03 |
| 42 | The private network — subnets, route tables, and why the private one has no route out | CLD-04 |
| 43 | Security groups and network ACLs — the two firewalls everyone confuses | CLD-05 |
| 44 | Private connectivity — NAT gateways, service endpoints, and the egress line on the bill | CLD-06 |
| 45 | Object storage as the document lake, and a managed database with pooling from a service that scales horizontally | CLD-07, CLD-08 |
| 46 | Secrets in the cloud, the cost model, and the budget alarm you arm before the first deploy rather than after the first invoice | CLD-09, CLD-10, CLD-11 |

### Phase 7 — Containers & CI/CD (Days 47–52)

*the image, the runtime, the pipeline*

| Day | Title | IDs closed |
| --- | --- | --- |
| 47 | Images, layers and the build cache — a Dockerfile that rebuilds in seconds instead of minutes | CLD-12 |
| 48 | Multi-stage builds, and a runtime image with no compiler, no shell history and no credential in a layer | CLD-13, CLD-14 |
| 49 | Docker Compose — the whole stack on one laptop, including the parts you do not own | CLD-15 |
| 50 | Health checks, signals and the graceful shutdown a load balancer will actually respect | CLD-16, CLD-17 |
| 51 | The container runtime and its load balancer — task definitions, target groups, and diagnosing the task that keeps restarting | CLD-18, CLD-19 |
| 52 | The pipeline that refuses to ship red — build, test, promote, and a stack you can destroy and recreate without a runbook of clicks | CLD-20, CLD-21, CLD-22 |

### Phase 8 — The transformer, taken apart (Days 53–61)

*tokens, embeddings, attention, the block*

| Day | Title | IDs closed |
| --- | --- | --- |
| 53 | What a language model actually is — the modelling objective, and next-token prediction followed end to end | TF-01, TF-02 |
| 54 | Text to numbers — the tokenizer boundary, the taxonomy, and Byte Pair Encoding trained from scratch on your own corpus | TF-03, TF-04, TF-05 |
| 55 | WordPiece, SentencePiece and tokenizer pathologies — vocabulary size, digits, code, whitespace and the multilingual tax | TF-06, TF-07, TF-08 |
| 56 | Embeddings — discrete symbols into continuous space; the embedding matrix, weight tying, and why order has to be injected | TF-09, TF-10, TF-11 |
| 57 | The attention mechanism from first principles — query, key, value, and scaled dot-product | TF-12, TF-13 |
| 58 | Self-attention, the causal mask, and multi-head attention — what a decoder is allowed to see, and what heads specialise into | TF-14, TF-15, TF-16 |
| 59 | The transformer block — residuals, layer norm, the feed-forward network, and pre-norm vs post-norm | TF-17, TF-18, TF-19 |
| 60 | Three architectures — encoder-only, decoder-only, encoder–decoder, cross-attention, and how to choose | TF-20, TF-21, TF-22 |
| 61 | Coding attention — batched multi-head by hand, a block that actually trains, and a loss curve that tells the truth | TF-23, TF-24, TF-25 |

### Phase 9 — Inference optimization & scale (Days 62–67)

*the KV cache, Flash, the variants, the sizing argument*

| Day | Title | IDs closed |
| --- | --- | --- |
| 62 | The naive decoding problem — quadratic recompute measured rather than asserted — and the KV cache that fixes it | TF-26, TF-27, TF-28 |
| 63 | KV cache memory math, and Flash Attention — IO-awareness, tiling, and why the speedup is not in the FLOPs | TF-29, TF-30, TF-31 |
| 64 | Multi-Query, Grouped-Query and Multi-Head Latent Attention — sharing the cache, then compressing it | TF-32, TF-33, TF-34 |
| 65 | PagedAttention, continuous batching and vLLM — the serving-side answer; and PyTorch SDPA's backend selection | TF-35, TF-36, TF-37 |
| 66 | RoPE — rotary embeddings, and what happens when you push past the trained context | TF-38, TF-39 |
| 67 | Scaling laws, compute-optimal training, and Mixture-of-Experts — the sizing argument you make before you spend money | TF-40, TF-41, TF-42, TF-43 |

### Phase 10 — Post-training: the lifecycle and the data (Days 68–73)

*CPT, formats, loss masking, synthetic data*

| Day | Title | IDs closed |
| --- | --- | --- |
| 68 | The two-phase lifecycle — pre-training vs post-training, what pre-training produces, and why a base model is not useful out of the box | FT-01, FT-02, FT-03 |
| 69 | Data curation and filtering at scale — quality heuristics, deduplication, and benchmark contamination | FT-04, FT-05 |
| 70 | Continued pre-training for domain adaptation — and knowing when to skip it and go straight to SFT | FT-06, FT-07 |
| 71 | Dataset formats and chat templates — instruction pairs, the template that must match the base, and the mismatch that silently degrades everything | FT-08, FT-09 |
| 72 | Loss masking — what it is, and exactly what breaks without it, run broken on purpose | FT-10, FT-11 |
| 73 | Synthetic data — the taxonomy, self-instruction, preference pairs, judge-scored generation, and the two ways a synthetic pipeline rots | FT-12, FT-13, FT-14, FT-15 |

### Phase 11 — PEFT, SFT & preference alignment (Days 74–80)

*LoRA, QLoRA, SFT, DPO*

| Day | Title | IDs closed |
| --- | --- | --- |
| 74 | The intrinsic dimensionality insight, and LoRA — the math, rank, alpha, and which modules to target | FT-16, FT-17, FT-18 |
| 75 | LoRA in practice — adapters on disk, merged and unmerged, and what each costs at serving time | FT-19, FT-20 |
| 76 | QLoRA — 4-bit NF4, double quantization, and paged optimizers | FT-21, FT-22 |
| 77 | DoRA, AdaLoRA and LoRA+ — decomposing magnitude from direction, adaptive rank, and separate learning rates | FT-23, FT-24 |
| 78 | Supervised fine-tuning end to end — the trainer, instruction tuning, and multi-turn data without leakage | FT-25, FT-26, FT-27 |
| 79 | Chain-of-thought fine-tuning, domain adaptation, and catastrophic forgetting | FT-28, FT-29 |
| 80 | Why SFT alone is not enough — RLHF with PPO, then DPO without a reward model, with GRPO and ORPO in one page | FT-30, FT-31, FT-32, FT-33 |

### Phase 12 — Evaluation, quantization & serving (Days 81–85)

*judges, GPTQ/AWQ/GGUF, vLLM*

| Day | Title | IDs closed |
| --- | --- | --- |
| 81 | Why evaluation belongs inside the fine-tuning loop — and the three benchmark families | FT-34, FT-35 |
| 82 | LLM-as-judge — calibrating a judge you can trust, and designing a domain evaluation that can fail | FT-36, FT-37, FT-38 |
| 83 | Post-training quantization — GPTQ, AWQ, NF4 and FP8, with the quality delta measured rather than assumed | FT-39, FT-40, FT-41 |
| 84 | GGUF and llama.cpp — the CPU path; and merging adapters before serving, or deliberately not | FT-42, FT-43 |
| 85 | vLLM and SGLang — paged KV, the OpenAI-compatible surface, and many adapters served from one base | FT-44, FT-45, FT-46 |

### Phase 13 — Reasoning, small models & distillation (Days 86–89)

*CoT trained, student–teacher, KL*

| Day | Title | IDs closed |
| --- | --- | --- |
| 86 | What a reasoning model is — chain-of-thought prompted, then trained; verifiable rewards, and what skipping supervised fine-tuning cost | FT-47, FT-48, FT-49 |
| 87 | Small language models — why cost, latency and privacy make them the default, and pruning as the other lever | FT-50, FT-51 |
| 88 | The student–teacher paradigm — hard labels, soft labels, temperature scaling, and the KL divergence loss written from scratch | FT-52, FT-53, FT-54 |
| 89 | A distillation pipeline end to end — teacher data, student design, choosing the scale, and speculative decoding as the cheaper cousin | FT-55, FT-56, FT-57 |

### Phase 14 — `yantra-model` — the domain model, shipped (Days 90–94)

*the claims post-training pipeline, delivered*

| Day | Title | IDs closed |
| --- | --- | --- |
| 90 | Kickoff — the claims-domain post-training pipeline, the datasets, and their licences checked before a single download | PRJ-01 |
| 91 | The SFT dataset — synthetic generation, deduplication, chat formatting, loss masking, and the versioned artifact | PRJ-02 |
| 92 | Stage 1 QLoRA supervised fine-tuning, then Stage 2 DPO preference alignment over one epoch | PRJ-03, PRJ-04 |
| 93 | Evaluation — surface metrics, a calibrated judge on accuracy, safety and tone, and the distilled GGUF student benchmarked against its teacher | PRJ-05, PRJ-06 |
| 94 | The multi-adapter server, containerised, deployed and traced — and the phase gate | PRJ-07 |

### Phase 15 — Embeddings & retrieval (Days 95–104)

*the taxonomy, chunking, the three families, fusion*

| Day | Title | IDs closed |
| --- | --- | --- |
| 95 | Embeddings — what a vector actually encodes, the question it cannot represent, and the dense/sparse/multi-vector taxonomy | RAG-01, RAG-02, RAG-03 |
| 96 | Quantized and binary embeddings, and Matryoshka representation learning — float32 to int8 to one bit, and flexible dimensions at query time | RAG-04, RAG-05, RAG-06 |
| 97 | Embedding fine-tuning on your own corpus — hard negatives, and the gain measured against the off-the-shelf baseline | RAG-07, RAG-08 |
| 98 | Chunking — fixed, recursive and semantic, and exactly what each strategy destroys | RAG-09, RAG-10 |
| 99 | Vanilla RAG, end to end and by hand, with no framework anywhere near it | RAG-11, RAG-12 |
| 100 | Vector stores — self-hosted and managed, namespaces, and metadata that filters before it ranks | RAG-13, RAG-14 |
| 101 | BM25, and the queries where vectors lose badly | RAG-15 |
| 102 | Learned sparse and late interaction — SPLADE, ColBERT and MaxSim, and why one vector per document is not always enough | RAG-16, RAG-17 |
| 103 | Hybrid retrieval and reciprocal rank fusion; query rewriting, decomposition and HyDE | RAG-18, RAG-19, RAG-20 |
| 104 | Rerankers — the cross-encoder that fixes a top-k nobody would have shipped, and citations a compliance officer can audit line by line | RAG-21, RAG-22, RAG-23 |

### Phase 16 — Retrieval evaluation & adaptive RAG (Days 105–108)

*the golden set, the gate, the router, the cache*

| Day | Title | IDs closed |
| --- | --- | --- |
| 105 | Retrieval evaluation — a golden set, recall@k, and the number that has to move | RAG-24, RAG-25 |
| 106 | RAGAS and DeepEval — faithfulness, relevancy, context precision and recall, and what a single score hides | RAG-26, RAG-27 |
| 107 | Self-RAG, Corrective RAG, Adaptive and Agentic RAG — the model deciding when to retrieve, measured against the fixed pipeline | RAG-28, RAG-29, RAG-30 |
| 108 | Vector quantization at scale — scalar, binary and product quantization — and caching, including the semantic cache that returns the wrong answer fast | RAG-31, RAG-32, RAG-33 |

### Phase 17 — Graph & multimodal retrieval (Days 109–115)

*the relationship, and the page that is an image*

| Day | Title | IDs closed |
| --- | --- | --- |
| 109 | When the answer is a relationship — the question retrieval structurally cannot answer, the property-graph model, and Cypher | RAG-34, RAG-35 |
| 110 | Designing an enterprise schema, and building the graph out of documents nobody curated — entity extraction and resolution | RAG-36, RAG-37 |
| 111 | GraphRAG — retrieval that traverses instead of ranking; the hybrid router that picks and explains why; and the relationship that went stale in silence | RAG-38, RAG-39, RAG-40 |
| 112 | The document that defeats a text pipeline — scans, merged cells, rotated tables and charts — and what OCR costs at forty thousand pages a month | RAG-41, VIS-01 |
| 113 | From CNN to Vision Transformer — an image as a sequence of patches, the CLS token, attention maps, and the data-hunger tradeoff | VIS-02, VIS-03, VIS-04 |
| 114 | Contrastive and self-supervised vision encoders, and Visual Language Model architecture — the three components and the projector into the language model's embedding space | VIS-05, VIS-06, VIS-07 |
| 115 | Retrieval directly over page images — late interaction on patch vectors, table and chart extraction into a schema you can query, routing to the cheap path, and the page that fails every single time | VIS-08, VIS-09, RAG-42, RAG-43 |

### Phase 18 — Agents — tools, the loop & MCP (Days 116–124)

*function calling, the hand-rolled loop, the boundary*

| Day | Title | IDs closed |
| --- | --- | --- |
| 116 | Why function calling exists — the model-to-tool communication problem, and function schema design | AGT-01, AGT-02 |
| 117 | The function-calling lifecycle — the call, the result turn, parallel calls, and forced or constrained tool choice | AGT-03, AGT-04, AGT-05 |
| 118 | Structured output vs function calling — the difference, when each is right, and the universal contract across providers | AGT-06, AGT-07 |
| 119 | The think-act-observe loop, hand-rolled, with no framework anywhere near it | AGT-08, AGT-09 |
| 120 | Where the hand-rolled loop breaks — state, retries, and resuming after a crash | AGT-10 |
| 121 | Tool design — schemas, descriptions, and the tool an agent confidently misuses | AGT-11, AGT-12 |
| 122 | Why MCP exists — tool fragmentation, hosts, clients and servers, and the primitives | AGT-13, AGT-14 |
| 123 | MCP transports — stdio and streamable HTTP — and building a server from scratch, scoped to one job | AGT-15, AGT-16, AGT-17 |
| 124 | Building an MCP client; the connection that drops mid-call; and authentication, authorization and trust boundaries | AGT-18, AGT-19, SEC-01 |

### Phase 19 — LangGraph — state, memory & multi-agent (Days 125–132)

*the graph, the checkpoint, the supervisor, the approval*

| Day | Title | IDs closed |
| --- | --- | --- |
| 125 | LangChain and LCEL — the model abstraction, composition, streaming, and an honest account of when not to use it | AGT-20, AGT-21 |
| 126 | LangGraph foundations — state, nodes, edges, and the routing decision made explicit | AGT-22, AGT-23, AGT-24 |
| 127 | Tool nodes and the ReAct agent, assembled deliberately rather than imported | AGT-25, AGT-26 |
| 128 | Checkpointers — durable state, and the run that survives a `kill -9` with no duplicated side effect | AGT-27, AGT-28 |
| 129 | Memory — the thread, long-term stores, namespaces, and the honest question of what is worth remembering | AGT-29, AGT-30 |
| 130 | Context engineering for agents — selection, compaction, and the prompt that grew to eighty thousand tokens | AGT-31, AGT-32 |
| 131 | Supervisors, handoffs and parallel subgraphs — delegating without passing the whole context, a join that does not drop a finding, and agent-to-agent protocols when the other agent is not yours | AGT-33, AGT-34, AGT-35 |
| 132 | Human-in-the-loop — interrupts as a first-class state, an approval surface a busy professional will use rather than rubber-stamp, and a kill switch someone can find | AGT-36, AGT-37, AGT-38 |

### Phase 20 — Enterprise integration (Days 133–138)

*the systems the client already runs*

| Day | Title | IDs closed |
| --- | --- | --- |
| 133 | The integration inventory — finding out what the client actually runs, not what they say they run | ENT-01 |
| 134 | SQL as a tool — text-to-SQL, allowlists, a read-only role, a planner that refuses, and the query you must never let reach the database | ENT-02, ENT-03, SEC-02 |
| 135 | SQL Server and Oracle — dialects, drivers, and the DBA whose job is to say no | ENT-04 |
| 136 | SOAP, XML and file drops — WSDL, envelopes, a 2003 API that still runs payroll, and the SFTP batch that is genuinely the integration | ENT-05, ENT-06 |
| 137 | Slack and Jira as the interface — events, blocks, transitions, a bot that does not become noise, and writing back without corrupting someone's board | ENT-07, ENT-08 |
| 138 | Webhooks, retries and idempotency keys — surviving delivery you do not control, and the upstream that changed its schema at midnight | ENT-09, ENT-10 |

### Phase 21 — Identity & access (Days 139–143)

*who is asking, and what they may see*

| Day | Title | IDs closed |
| --- | --- | --- |
| 139 | Authentication and authorisation — the distinction that leaks data the moment it blurs | ENT-11 |
| 140 | OAuth 2.0 — the flows, the tokens, and the one you should actually be using | ENT-12, ENT-13 |
| 141 | OIDC, SSO and SAML — logging in with the client's identity provider rather than your own | ENT-14, ENT-15 |
| 142 | RBAC — roles, scopes, and a permission model that survives a reorganisation | ENT-16 |
| 143 | Document-level access control inside retrieval itself, and the audit log that proves who saw what to someone who assumes you are wrong | ENT-17, ENT-18 |

### Phase 22 — Security & guardrails (Days 144–149)

*the attack first, then the defence*

| Day | Title | IDs closed |
| --- | --- | --- |
| 144 | The threat model — what an AI system adds to an attack surface that already existed | SEC-03 |
| 145 | Prompt injection, direct and indirect — the document that is also an instruction | SEC-04, SEC-05 |
| 146 | Data exfiltration through a helpful assistant, and jailbreaks a longer system prompt does not stop | SEC-06, SEC-07 |
| 147 | PII — detection before the model ever sees it, masking, tokenisation, and the redaction that has to be reversible for the adjuster | SEC-08, SEC-09 |
| 148 | Guardrails as configuration — rails, provider-side filters, defence in depth, and an honest account of their limits with the latency cost measured | SEC-10, SEC-11 |
| 149 | The red-team day — break your own system on purpose, then put every attempt into CI so it stays broken | SEC-12, SEC-13 |

### Phase 23 — Observability & the gateway (Days 150–154)

*the trace that explains a bad answer*

| Day | Title | IDs closed |
| --- | --- | --- |
| 150 | Tracing an LLM system — spans, and the trace tree that finally explains a bad answer | OPS-01, OPS-02 |
| 151 | Structured logs and correlation IDs across a multi-step agent run | OPS-03 |
| 152 | Token accounting — attributing cost to a user, a tenant and a feature — and latency budgets that find where the time actually goes | OPS-04, OPS-05 |
| 153 | The LLM gateway — routing, fallbacks, and provider abstraction that survives an outage | OPS-06, OPS-07 |
| 154 | Rate limits, retries and backoff that is honest about failing; and online evals that catch the regression that shipped anyway | OPS-08, OPS-09 |

### Phase 24 — LLMOps — harness, evals & CI gating (Days 155–160)

*the eval that blocks a merge*

| Day | Title | IDs closed |
| --- | --- | --- |
| 155 | Why ad-hoc testing fails — evaluation harness fundamentals, and benchmarking with a standard harness | OPS-10, OPS-11 |
| 156 | Agent-native evaluation — task, solver and scorer, and evaluating a trajectory rather than a string | OPS-12, OPS-13 |
| 157 | LLM-as-judge pipelines at scale — model-graded scoring, calibration, and the biases a judge brings | OPS-14, OPS-15 |
| 158 | Prompt regression and snapshot testing; golden datasets — building them, versioning them, and keeping them honest | OPS-16, OPS-17, OPS-18 |
| 159 | Trace-based testing and flaky-test detection; harness patterns — iteration guards, fallbacks and token budgets | OPS-19, OPS-20 |
| 160 | Agent CI/CD — eval gating on a pull request, with cost and latency regression guards and the delta commented | OPS-21, OPS-22, OPS-23 |

### Phase 25 — `yantra-platform` — the retrieval platform, delivered (Days 161–167)

*hybrid, graph, visual, secured, deployed*

| Day | Title | IDs closed |
| --- | --- | --- |
| 161 | Kickoff — the engagement brief, the data classification, the architecture diagram a CIO signs and a security team does not reject, and what is out of scope | PRJ-08, FDE-09 |
| 162 | Hybrid retrieval over the client corpus, wired end to end for the first time | PRJ-09 |
| 163 | The graph and the page-image index — the relational question and the scanned bundle, both answered | PRJ-10 |
| 164 | The adaptive router across all three retrievers, with cross-encoder reranking on the fused candidates | PRJ-11, PRJ-12 |
| 165 | Secure text-to-SQL against the claims database, and OAuth with RBAC across the whole surface rather than just the front door | PRJ-13, PRJ-14 |
| 166 | PII masking and rails placed in the request path, with the latency cost measured and stated | PRJ-15 |
| 167 | Deployed to a private endpoint behind a scanned image; the faithfulness gate on golden QA pairs; and the evaluation report the client will actually read | PRJ-16, PRJ-17, FDE-10 |

### Phase 26 — `yantra-agents` — the multi-agent system, delivered (Days 168–173)

*supervisor, boundaries, approval, cost*

| Day | Title | IDs closed |
| --- | --- | --- |
| 168 | Kickoff — the compliance process mapped before a single agent is drawn, and the supervisor topology with the argument against having one | PRJ-18, FDE-11 |
| 169 | The specialist agents behind MCP servers, scoped to exactly what the audit needs and nothing more | PRJ-19, PRJ-20 |
| 170 | Trust boundaries and policy — deciding what each agent may touch, and proving it cannot touch the rest | PRJ-21, SEC-14 |
| 171 | Human approval on every write, and exact checkpoint resume after the process is killed mid-run | PRJ-22, PRJ-23 |
| 172 | Parallel audit execution with a join that must not silently lose a finding, and sandboxed tool execution for the step that runs code | PRJ-24, SEC-15 |
| 173 | The traceability dashboard — every finding back to its evidence — the per-audit unit economics, and the pilot gate reported honestly | PRJ-25, PRJ-26 |

### Phase 27 — `yantra-ship` — the LLMOps shell and the deploy (Days 174–177)

*the gate contract, and the rollback you trigger*

| Day | Title | IDs closed |
| --- | --- | --- |
| 174 | The monorepo, the golden suite and the gate contract — lint, unit tests, and prompt regression against the baseline built on Day 38 | PRJ-27, PRJ-28 |
| 175 | The per-service evaluation score gate, and the score delta posted on the pull request | PRJ-29, PRJ-30 |
| 176 | Multi-stage container builds, the registry push, and smoke tests on staging with golden cases | PRJ-31, PRJ-32 |
| 177 | Blue/green deployment with gradual traffic shifting, and an auto-rollback on an error-rate breach that you trigger on purpose | PRJ-33, OPS-24, OPS-25 |

### Phase 28 — Handover, ROI & the defence (Days 178–181)

*the day you stop being on call*

| Day | Title | IDs closed |
| --- | --- | --- |
| 178 | Change management for the users who never asked for any of this, and training and runbooks that survive your exit from the account | FDE-12, FDE-13 |
| 179 | The handoff to the client's own team, and the ROI presentation — model metrics translated into money a CFO recognises, against the Day 3 baseline | FDE-14, FDE-15 |
| 180 | One request traced through every service in the system, and the cost model per thousand requests | PRJ-34, PRJ-35 |
| 181 | The defence — the public repository a stranger can clone and run, the case-study write-up, and the interview loop: system design, the client case, and the coding round | PRJ-36, FDE-16, FDE-17 |
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
answers, and 182 days of them are indistinguishable in a file tree, a `git log` or an editor's tab
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
| 5 | **Why Yantra needs it** | The concrete later day that breaks without this. *"You meet this again on Day 115, where late interaction writes patch vectors into a multi-vector index"* is the shape. Never "this is important". |
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
  that part and link it** — never assume the reader remembers Day 20 on Day 170.
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

**A source is taught once in the whole curriculum.** 182 days will cite the same handful of
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

## 22 · 🔀 The merge — what was joined, what was cut, and why

This plan replaces two. Everything below is a decision someone can disagree with, which is why it
is written here rather than left as an absence in the day map.
[`ADR-0006`](adr/ADR-0006-the-merge.md) carries the structural record.

### 22.1 The arithmetic

| | Days | IDs |
| --- | --- | --- |
| Yantra v1.1.0 | 229 | 400 |
| Setu v1.0.0 | 180 | 181 |
| Run separately | **409** | 581 |
| **This plan** | **182** | **373** |

The 227 days saved come from three places, in descending order of honesty:

1. **Deduplication — about 85 days, and nothing is lost.** Both plans taught embeddings, chunking,
   BM25, hybrid retrieval, reranking, RAG evaluation, graph retrieval, page-image retrieval,
   function calling, the hand-rolled agent loop, MCP, LangGraph, checkpointing, human-in-the-loop,
   PII masking, guardrails, prompt injection, tracing, token accounting and eval-gated CI. Where
   both taught a subject, the deeper treatment won and the shallower one was deleted.
2. **Density — about 90 days.** The merged plan closes 2.05 IDs per day against Yantra's 1.75 and
   Setu's 1.0. Two adjacent ideas that each held a day now share one — WordPiece and SentencePiece
   with tokenizer pathologies, MQA with GQA and MLA, OIDC with SAML, the graph schema with entity
   resolution. **This is a real cost:** those days are heavier, and a heavy day gets another part
   rather than a shorter explanation (Principle 15).
3. **Cuts and parks — about 50 days.** Listed in §22.3, individually, with the reason.

### 22.2 The ordering decision that shapes everything

**The model is met as a dependency before it is taken apart.** Phase 5 (Days 30–38) uses it as a
black box; Phase 8 (Day 53) opens it.

Setu's order was foundation → API → cloud → containers → the model. Yantra's was the model → the
training → everything else. Neither works merged: Setu never opens the box, and Yantra writes
training code on Day 15 for a reader who has not yet met a lockfile, a type hint or a released
connection.

The merged order is: **the client, the language, the service, the model as a dependency, the
cloud, the pipeline, then the model taken apart.** Every question Phase 5 raises — *why does it
cost that? why did that number move? why did the JSON come back truncated?* — is answered by a
mechanism in Phase 8 or 9. Curiosity precedes the explanation, rather than the explanation
arriving before anyone has felt the need for it.

The cost of the move: Days 30–38 use tokenization, sampling and the context window before Phase 8
explains them. Those days state that explicitly and link forward, which §20.4's no-shortcut test
requires.

### 22.3 What was cut, and what it costs

| Cut or parked | From | Days saved | What it costs |
| --- | --- | --- | --- |
| **Speech, speech-to-text and Whisper fine-tuning** | Yantra `VIS-19..24` | 2 | Nothing in this system. It fed no service in either plan, and v1.1.0 already named it the first thing to cut. **If the client's next process is call-centre transcription, this is the first thing to add back.** |
| **A managed agent runtime as a taught product** | Yantra `AGT-66..77` | 6 | The most vendor-specific material in either plan, and the fastest to date. Its four real subjects — runtime isolation, agent memory, a tool gateway, agent identity — survive as mechanisms: containers and sandboxes (Days 47–52, 172), memory (Day 129), MCP as the gateway (Days 122–124), and OAuth with per-agent scoping (Days 140–142). What is lost is the console walkthrough. |
| **Agent-to-agent protocol as a six-day block** | Yantra `AGT-57..65` | 5 | Compressed into Day 131, alongside supervisors and handoffs, where the question it answers — *what if the other agent is not yours?* — actually arises. You will be able to explain the model and read a spec; you will not have built a compliant server. |
| **Five separate shipped services** | Yantra `PRJ`, Setu Phases 18–19 | ~20 | Yantra shipped five services to nobody; Setu shipped two systems to one client. Merged: four things shipped to one client. A second medical-domain fine-tune taught nothing the first did not. |
| **Vision internals as a twelve-day track** | Yantra `VIS-01..18` | 8 | Compressed to Days 113–114. You will build a patch embedding and explain a VLM's three components; you will not train one. Page-image retrieval (Day 115) is the load-bearing use, and it survives intact. |
| **The MoE and scaling-law block** | Yantra Days 28–33 | 4 | Compressed to Days 66–67. The sizing argument survives because it is what you use before spending money on Day 76. Training a sparse model does not. |
| **RLHF with PPO as a full day** | Yantra `FT-43..45` | 1 | Half of Day 80. You will be able to explain reward model, critic and KL penalty, and why DPO replaced it in practice. You will implement DPO, not PPO. |
| **Full separate days for GraphQL, SAML, IaC** | Setu | 3 | Each folded into an adjacent day as its second subject. All three are things a client forces on you rather than things you choose. |
| **Two separate discovery engagements** | Setu Phases 2, 18, 19 | 4 | One client, discovered once on Days 1–5, with a re-scoping day at the front of each project phase. Running two full discoveries teaches the second one nothing. |

**What was deliberately *not* cut,** despite the pressure: tokenization (three days), loss masking
(its own day, run broken), BM25 (a full day with a real baseline), the hand-rolled agent loop (two
days before any framework), the attack-before-defence rule in every `SEC` day, and the whole `FDE`
track. Each of those is the difference between someone who can use a thing and someone who can
debug it, sell it, or defend it.

### 22.4 The calendar

**182 days, one day at a time, is six months at seven days a week.** At six days a week it is seven
months; at five, closer to eight and a half.

There are no streaks and no counters in this repository, and missing a day costs nothing. What
costs something is doing two days in one sitting — that is one day of building and one day of
reading, and the reading one does not stick. The plan is sized so that the honest answer to "I am
behind" is *the next day is still the next day*.

### 22.5 If it still has to be shorter

The levers, cheapest first. Anything beyond the first two is a genuine scope decision and needs an
ADR **before Day 1**, not a quiet edit on Day 90.

| Lever | Days saved | What it costs |
| --- | --- | --- |
| Compress Phases 2–4 to the ~22-day version — keep async, Pydantic, FastAPI, dependency injection and testing; drop memory internals, the process table, shell scripting and GraphQL | 17 | Assumes you already write Python that survives a long-running process. If you do not, this is the worst lever on the list, because every later day writes that Python. |
| Drop the graph track (`RAG-34..40`, Days 109–111) | 3 | The relational question goes unanswered, and `yantra-platform` becomes a two-retriever router. A real loss, but a self-contained one. |
| Drop the distillation phase (`FT-52..57`, Days 88–89) | 2 | The student–teacher mirror of fine-tuning goes. `yantra-model` still ships; it just never gets small. |
| Merge Phases 20–21 into four days | 7 | Legacy integration and identity become awareness-level. This is the material that separates a demo from a delivery, so it is last on the list for a reason. |
