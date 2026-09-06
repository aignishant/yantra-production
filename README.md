# Yantra

**Production LLM engineering — transformer internals, fine-tuning and alignment, vision and speech,
retrieval, agents and protocols, and the delivery shell that ships all of it.**
229 days · 25 phases · 400 concepts · one system.

This repository teaches production LLM engineering by building one system and refusing to let any
part of it look finished when it is not. Every concept has an identifier, every identifier is
assigned to exactly one day, and every day is a hub plus one document per subtopic — each opening
where someone who has never met the idea can stand, and ending at what breaks in a real system.

Nothing carries a time estimate. No version, citation or benchmark number is written from memory.
A day is not finished until a check that could have gone red went green instead.

## What gets built

| Service | What it is | Phase |
| --- | --- | --- |
| `yantra-med` | Clinical assistant: QLoRA SFT then DPO, served by vLLM with hot-swappable adapters | 8 |
| `yantra-edge` | Distilled reasoning model, quantized to GGUF, answering on CPU | 10 |
| `yantra-lex` | Legal document intelligence: ColPali, Neo4j, BM25, RRF fusion, RAGAS-gated | 16 |
| `yantra-ops` | DevOps multi-agent system: LangGraph supervisor, MCP sub-agents, A2A, human approval on writes | 21 |
| `yantra-ship` | The LLMOps shell: eval-gated CI, cost and latency guards, blue/green with auto-rollback | 23 |

The system-level test, and what the capstone defends: **a prompt change in any service must be
blocked by the pipeline when it makes that service worse, and must reach a live endpoint when it
does not — without a human deciding which of those two happened.**

## Where to start

| You want | Open |
| --- | --- |
| The contract everything obeys | [`docs/00_MASTER_PLAN.md`](docs/00_MASTER_PLAN.md) |
| **The day map, to correct before day 1** | [`docs/00_MASTER_PLAN.md`](docs/00_MASTER_PLAN.md) §17 |
| Where the work actually is | [`docs/PROGRESS.md`](docs/PROGRESS.md) — the last row |
| What each day teaches | [`docs/WIKI.md`](docs/WIKI.md) |
| Where a concept is taught | [`docs/CURRICULUM_INDEX.md`](docs/CURRICULUM_INDEX.md) |
| What is written and what is not | [`docs/TRACKER.md`](docs/TRACKER.md) |
| **What to run without a GPU, and how to switch later** | [`docs/HARDWARE.md`](docs/HARDWARE.md) |
| Why something is the way it is | [`docs/adr/`](docs/adr/) |
| Which source module a day came from | [`docs/01_ROADMAP_COVERAGE.md`](docs/01_ROADMAP_COVERAGE.md) |

## The commands

```bash
python granth.py status        # how many days are complete, and what is next
python granth.py brief N       # what day N must cover, and whether N is allowed yet
python granth.py start N       # open day N in reading order
python granth.py depth N       # check day N against the depth contract
python granth.py index         # regenerate the derived documents
python granth.py check         # lint + format + tests + depth + index freshness
python granth.py done N        # refuse, then check, regenerate and commit
python granth.py doctor        # config, plan markers, ledgers, duplicate IDs
```

## The daily loop

```bash
python granth.py brief 7    # 1. the assignment — and whether day 7 is allowed yet
/day-yantra 7               # 2. write it
python granth.py depth 7    # 3. check it against the contract
                            # 4. do the work; break it on purpose; watch the check go red
python granth.py done 7     # 5. finish — refuses unless ticked and the row is pasted
```

## Before you write day 1

Two things are worth correcting now, because both are expensive to change once folders exist:

1. **The day map** (plan §17). 229 days at four sittings a week runs past a year. Plan §22.4 lists
   the scope levers in the order they cost least.
2. **The budget and infrastructure policy** (plan §4). The *hardware* half is now settled: plan
   §4.1 makes a laptop with no GPU the default and puts the accelerated path behind one flag
   (`YANTRA_PROFILE`, see [`docs/HARDWARE.md`](docs/HARDWARE.md) and
   [`ADR-0005`](docs/adr/ADR-0005-the-hardware-profile.md)). The *money* half is still open: §4
   assumes a rentable GPU from phase 6 and an AWS account from phase 8. If your constraint is free
   tiers only, say so before day 0 — it changes base-model choices in phases 6–9 and the deployment
   target in phases 8, 16 and 21.

## Requirements

Python 3.11+ for the toolchain (`tomllib` is stdlib from 3.11); Python 3.12 and `uv` for the
curriculum itself; `git` if you want `done N` to commit for you. The toolchain has no dependencies
on purpose: a repository that teaches you something should not need a package install before it can
check itself.

## Licence

The curriculum documents are yours. The plan derives from a published course roadmap; see
[`docs/01_ROADMAP_COVERAGE.md`](docs/01_ROADMAP_COVERAGE.md) for the mapping and
[`docs/adr/ADR-0001-the-plan-as-adopted.md`](docs/adr/ADR-0001-the-plan-as-adopted.md) for the
decisions taken in translating it.
