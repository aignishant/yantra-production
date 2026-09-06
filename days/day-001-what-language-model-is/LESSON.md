---
day: 1
phase: 1
phase_name: "The transformer, taken apart"
title: "What a language model actually is"
ids: [TF-01, TF-02]
kind: mechanism
plan_version: "v1.0.0"
parts: 7
generated: "2026-09-07"
status: written
commit: ""
---

> **Yesterday:** a repository that cannot leak a key and a gate that refuses a half-finished day.
> **Today:** what a language model actually produces — a distribution over the next token — and
> what has to happen around it to turn that into text.
> **Tomorrow:** where tokens come from, and why the tokenizer is a boundary worth a week.

## §1 Where we are

Everything in the next 227 days is built on one mechanism, and it is smaller than its reputation.

Think of the three suggested words above a phone keyboard. Two things about that strip are the
whole of today. It offers *three*, ranked, rather than deciding what you meant — and the list it
ranked is much longer than three, with an entry for every word it knows. The strip is a display
decision made after the real work.

That is a language model. It takes the tokens so far and returns one number for every token in its
vocabulary, saying how likely each is to come next. It does not produce text. Text is what you get
when something outside the model picks from that list, appends the winner, and asks again.

Once that lands, three things stop being mysterious and start being engineering. Temperature is a
knob on how decisively you read the list. Generation cost is one full model call per token. And the
most important property of the whole system — that a model can be fluent, confident and wrong at
the same time — is not a defect to be patched but the direct consequence of an objective that
rewards plausible continuation and contains no representation of truth.

Today's model is `distilgpt2`, 82 million parameters, running on a laptop CPU. It is small enough
that its limitations are visible rather than hidden, which is the point: it will get the capital of
France wrong in front of you, in perfect English.

## §2 The map

### 1 · The objective — what the model is for

The mental model: one number per token, and one loss that measures how surprised it was.

| Part | Title | What it answers | Level |
| --- | --- | --- | --- |
| [1.1](parts/01-the-objective/1.1-a-distribution-over-the-next-token.md) | A distribution over the next token | What does a language model actually output? | foundation |
| [1.2](parts/01-the-objective/1.2-why-one-objective-is-enough.md) | Why one objective is enough | Why can it translate when nobody trained it to? | foundation |
| [1.3](parts/01-the-objective/1.3-cross-entropy-and-perplexity.md) | Cross-entropy and perplexity | What number says how good the prediction was? | working |

### 2 · The pass, followed end to end

The mental model: string → integers → vectors → one score per vocabulary token, then a loop.

| Part | Title | What it answers | Level |
| --- | --- | --- | --- |
| [2.1](parts/02-the-pass/2.1-from-string-to-logits.md) | From string to logits | What shape comes back, and why isn't it one row? | working |
| [2.2](parts/02-the-pass/2.2-softmax-and-temperature.md) | Softmax and temperature | How do raw scores become probabilities, and what does the dial do? | working |
| [2.3](parts/02-the-pass/2.3-the-loop.md) | The loop | Where does generation actually happen? | working |

### 3 · Synthesis — the two IDs meeting

The mental model: put the objective and the loop together and the system's defining failure follows.

| Part | Title | What it answers | Level |
| --- | --- | --- | --- |
| [3.1](parts/03-synthesis/3.1-the-model-has-no-plan.md) | The model has no plan | Why is fluent, confident and wrong the normal case? | production |

**Part 3.1 is today's deliberate failure**, and you will have caused it twice before reaching it —
both times while the code was working correctly.

### Sources — read this **after** the parts

| # | Source | Identifier |
| --- | --- | --- |
| [01](sources/01-language-models-are-few-shot-learners.md) | Language Models are Few-Shot Learners | `arXiv:2005.14165` |

Build the mechanism by hand first, then read the proposal. A reader who has already written the
loop can be told which half of this paper survived and which half the field corrected.

## §3 Setup

```bash
# CPU-only torch — no GPU is needed today or for the next fourteen days
uv add torch --index-url https://download.pytorch.org/whl/cpu
uv add transformers

# verify, and record both versions in docs/PINS.md
uv run python -c "import torch, transformers; print(torch.__version__, transformers.__version__)"
# expected on 2026-09-07: 2.14.0+cpu 5.16.1

# fetch the model once (~350MB); everything below is offline afterwards
uv run python -c "
from transformers import AutoModelForCausalLM, AutoTokenizer
AutoTokenizer.from_pretrained('distilgpt2'); AutoModelForCausalLM.from_pretrained('distilgpt2')
print('cached')"
```

`TODO(me)`: re-observe both versions on the day you do this and correct the `PINS.md` rows. A
version copied from this file rather than observed is exactly what Principle 7 forbids.

## §4 Build brief

| File | What it must do |
| --- | --- |
| `lab/peek.py` | `TODO(me)`: take any prompt on the command line and print its token list, the logits shape, and the top 5 next tokens with probabilities. This is your debugging tool for the next thirty days — write it properly. |
| `lab/loop.py` | `TODO(me)`: the generation loop by hand, with a `--temperature` flag. `0` must take the greedy path and never divide by zero. No `model.generate()` anywhere. |
| `lab/score.py` | `TODO(me)`: given a sentence, print its cross-entropy and perplexity. Assert the loss is finite and raise a clear error on a single-token input rather than returning `nan`. |
| `lab/sources/few-shot/` | `TODO(me)`: reproduce the source document's demo, including `run.sh`. Then break the ablation on purpose — make `SHOTS=0` and `SHOTS=4` produce the same prompt — and confirm the difference disappears. |
| `tests/test_generation.py` | `TODO(me)`: assert that greedy decoding from a fixed prompt is byte-identical across two runs, and that sampling at `T=1.0` is not. |

## §5 The check that must be able to fail

`tests/test_generation.py` — the determinism test.

**Make it go red on purpose:** change the greedy path to sample at `T=1.0`. The first assertion must
fail, because two runs will differ. Then put it back.

That test is not busywork: day 210 builds prompt regression testing on exactly this property, and a
regression suite running against a non-deterministic decoder reports noise as regressions forever.

## §6 Budget

| Resource | Today |
| --- | --- |
| Model calls to a provider | **0.** Everything runs locally; no API key is needed and nothing is rate-limited. |
| GPU hours | **0.** `distilgpt2` runs on a laptop CPU. |
| Money | **0.** |
| Downloads | torch CPU wheel (~200MB), transformers, and `distilgpt2` (~350MB), each once. |

The first day that needs a GPU is day 15. Plan §4 has the full table.

## §7 Traps

- **Forgetting the leading space.** `' Paris'` and `'Paris'` are different tokens. Scoring the
  wrong one gives a probability near zero and a wrong conclusion (parts 1.2, 2.1).
- **`model.eval()` omitted.** Dropout stays active and the same input gives slightly different
  logits, which will cost you an hour of reproducing a number that was never reproducible.
- **`softmax` on the wrong `dim`.** On a `(batch, seq, vocab)` tensor, `dim=1` normalises across
  positions and produces confident nonsense that runs perfectly (part 2.2).
- **`temperature=0` passed to the formula.** `logits / 0` gives `nan`, silently. Branch to `argmax`
  first (parts 2.2, 2.3).
- **Scoring a single token.** The loss is `nan` with no exception raised, and `nan` in a training
  loop corrupts weights while the progress bar keeps moving (part 1.3).
- **Comparing perplexity across tokenizers.** Two models that split text differently are answering
  different questions; the numbers are not on the same scale (part 1.3).
- **`torch.cat(..., dim=0)` in the loop.** Stacks a second sequence in the batch instead of
  extending the current one. It runs, generates nothing, and reports nothing (part 2.3).

## §8 Verify before you build

| What | Where it was checked | Date | What it confirmed |
| --- | --- | --- | --- |
| torch version | `import torch; torch.__version__` | 2026-09-07 | `2.14.0+cpu` |
| transformers version | `import transformers; transformers.__version__` | 2026-09-07 | `5.16.1` |
| `distilgpt2` context limit | `model.config.n_positions` | 2026-09-07 | `1024`, and the `IndexError` past it (part 1.1) |
| Vocabulary size | `probs.shape[0]` on the last-position distribution | 2026-09-07 | `50257` |
| Citation record | https://arxiv.org/abs/2005.14165 | 2026-09-07 | Title *Language Models are Few-Shot Learners*; arXiv:2005.14165; 2020; latest version v4, 22 Jul 2020 |
| Padding error text | `tok([...], return_tensors="pt")` on unequal lengths | 2026-09-07 | The `ValueError` quoted verbatim in part 2.1 |

## §9 Say it out loud

Day one was about what a language model actually returns, and the answer is a probability
distribution over the whole vocabulary — one number for every token it knows — not text. Text comes
from a loop outside the model: take the last position's scores, pick one token, append it, run the
whole thing again. I wrote that loop by hand rather than calling `generate()`, because the wasted
work is visible when you write it — every iteration recomputes every earlier position identically,
which is exactly what the KV cache fixes a couple of weeks from now. The thing that stuck with me
was running it on an 82-million-parameter model: asked for the capital of France, its top token was
"the" at about 12%, and twelve greedy steps produced "the capital of France is the capital of the
French Republic" — perfect grammar, circular, wrong, and no error anywhere. That is not a bug. The
objective rewards plausible continuation and has nothing in it that represents truth, so fluency
arrives long before correctness. Basically every system I build after this — retrieval, faithfulness
scoring, guardrails, human approval before writes — exists because of that one property.

## §10 Done when

See [`CHECKLIST.md`](CHECKLIST.md). Defined by understanding and green checks, never by effort
spent.

## §11 Ledger & commit

**`docs/PROGRESS.md`:**

```text
| 1 | 2026-09-07 | TF-01, TF-02 | 7 | <hash> | green | First real day; `distilgpt2` on CPU throughout. |
```

**`docs/PINS.md`:**

```text
| torch | 2.14.0+cpu | `torch.__version__` | 2026-09-07 | 1 | forward pass, softmax, tensor ops |
| transformers | 5.16.1 | `transformers.__version__` | 2026-09-07 | 1 | model and tokenizer loading |
| distilgpt2 | n_positions=1024, vocab=50257 | `model.config` | 2026-09-07 | 1 | the teaching model for phase 1 |
```

**`docs/SOURCES.md`:**

```text
| 1 | Language Models are Few-Shot Learners | arXiv:2005.14165 | https://arxiv.org/abs/2005.14165 | 2026-09-07 | day 1 sources/01 | day 1 part 1.2 |
```

**`docs/PROVENANCE.md`:**

```text
| distilgpt2 | pre-trained checkpoint | Hugging Face Hub | Apache-2.0 | yes — permits research and commercial use | 2026-09-07 | 1 |
| torch | package | PyPI (pytorch.org CPU index) | BSD-3-Clause | yes | 2026-09-07 | 1 |
| transformers | package | PyPI | Apache-2.0 | yes | 2026-09-07 | 1 |
```

`TODO(me)`: confirm the `distilgpt2` licence on its model card before the download, not after.

**`docs/GLOSSARY.md`:**

```text
| token | The unit a model reads and writes — usually a word fragment, often carrying a leading space | day 1 part 1.1 | — |
| vocabulary | The complete fixed set of tokens a model knows; nothing outside it can be read or written | day 1 part 1.1 | — |
| probability distribution | One number per option, all between 0 and 1, summing to 1 | day 1 part 1.1 | — |
| causal | Constrained to look only leftward: each position sees the tokens before it and none after | day 1 part 1.1 | autoregressive |
| training objective | The single thing a model is optimised to do; here, put probability on the token that came next | day 1 part 1.2 | — |
| in-context learning | Performing a task from examples in the prompt, with no weight update | day 1 part 1.2 | few-shot prompting |
| cross-entropy | The mean surprise, in nats, at the tokens that actually came next; the training loss | day 1 part 1.3 | loss |
| perplexity | exp(cross-entropy) — roughly how many equally likely options the model was choosing between | day 1 part 1.3 | — |
| nat | The unit of surprise when using the natural logarithm | day 1 part 1.3 | — |
| hidden state | The vector a model holds per position between its layers | day 1 part 2.1 | activation |
| logit | A raw unnormalised score, one per vocabulary token; not a probability | day 1 part 2.1 | — |
| softmax | The function turning scores into a distribution summing to 1, preserving order | day 1 part 2.2 | — |
| temperature | A number the logits are divided by before softmax; sharpens below 1, flattens above | day 1 part 2.2 | — |
| greedy decoding | Always taking the highest-probability token; deterministic | day 1 part 2.3 | argmax decoding |
| autoregressive generation | The loop outside the model: predict, append, repeat | day 1 part 2.3 | — |
| prefill | The first pass over the whole prompt; compute-bound | day 1 part 2.3 | — |
| decode | The per-token passes after prefill; memory-bandwidth-bound | day 1 part 2.3 | — |
| confabulation | A fluent, confident, unsupported output — the objective working, not failing | day 1 part 3.1 | hallucination |
```

**Commit:**

```text
day 1: what a language model actually is — closes TF-01, TF-02
```
