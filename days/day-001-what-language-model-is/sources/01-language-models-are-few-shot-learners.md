---
day: 1
title: "Language Models are Few-Shot Learners"
ids: [TF-01]
level: production
prerequisites: ["../parts/03-synthesis/3.1-the-model-has-no-plan.md"]
prev: "../parts/03-synthesis/3.1-the-model-has-no-plan.md"
next: ""
source: "arXiv:2005.14165"
---

> **Read this after the parts, not before.** You have already written the loop, read a
> distribution and measured a perplexity. Now read the document that claimed those mechanics were
> enough.

## One-line answer

It claimed that a large enough model trained only on next-token prediction can perform tasks it was
never trained for, given a handful of examples **in the prompt** and no weight updates at all — and
that the ability appears as a function of scale.

## The story

Before this document, adapting a language model to a task meant collecting a labelled dataset for
that task and fine-tuning on it. Thousands of examples, per task, every time.

That was not a technical inconvenience. It was the shape of the field. A model was a starting point
and the real work was the dataset, so every new task began with the same question: who is going to
label ten thousand examples, and who is paying for it? Teams with data won; teams with a good idea
and no data did not.

The uncomfortable comparison, which the paper makes in its opening, is that people do not work like
this. Show someone three examples of a task and they generally have it. Nothing in the machine
learning pipeline resembled that at all.

## The idea in plain language

The claim has two halves, and the second is the one that mattered.

**First half — in-context learning.** Put a few worked examples in the prompt, then the real
question. The model continues the pattern. No gradients, no optimiser, no new weights: the
"learning" happens entirely within one forward pass, using only the context window. The paper names
three settings by how many examples are given: **zero-shot** (a task description only),
**one-shot** (one example), and **few-shot** (typically ten to a hundred).

**Second half — it is a function of scale.** The paper trained models from 125 million parameters
up to 175 billion and measured the same tasks across all of them. The gap between zero-shot and
few-shot performance *widens* with size. Small models barely benefit from examples in the prompt.
Large ones benefit enormously.

That second half is what made it consequential. In-context learning was not a prompting trick that
someone found; it was a capability that appeared as models grew, which turned "make the model
bigger" from an engineering choice into a research direction. Day 29's scaling laws are the direct
continuation of this argument.

The word "few-shot" also has a history worth knowing. In earlier machine learning it meant training
on a small labelled set. Here it means **no training at all** — the examples live in the prompt and
are gone when the request ends. Same phrase, different mechanism.

## Why Yantra needs it

Part [1.2](../parts/01-the-objective/1.2-why-one-objective-is-enough.md) leans on this document for
its central claim, and the demo below is that part's ablation run properly.

Further out: day 108 turns prompting into a discipline, and few-shot is its main lever. Day 69 makes
the trade this paper creates — in-context examples cost tokens on every request forever, while a
fine-tune costs GPU hours once — and you cannot make that trade without knowing what the examples
buy.

## The mechanism

The paper's method is almost aggressively simple, which is part of why it landed.

The model is a decoder-only transformer trained on one objective — next-token prediction — with no
task-specific architecture anywhere. The largest is 175 billion parameters with a context window of
2048 tokens.

Evaluation is where the method actually is. For each task:

1. Take *k* examples from the task's training set.
2. Format them as text, one after another, with a consistent separator.
3. Append the real input, formatted the same way.
4. Run one forward pass and read the continuation.
5. Score it against the true answer.

Step 4 is the whole claim. There is no step where anything is trained. The model is frozen; *k* is
the only thing that changes. Because the examples must fit in the context window alongside the
question, *k* is bounded by context length — which is why later work on long contexts (day 28) is
partly a story about how many examples you can afford to show.

## The source in one demo

The claim, stripped to nothing but itself: does putting examples in the prompt raise the
probability of the correct answer, with no gradient update anywhere?

Two files. No framework, no argument parser, no web layer.

```text
lab/sources/few-shot/
├── fewshot.py
└── run.sh
```

`fewshot.py`:

```python
"""The paper's claim and nothing else.
Ablation: SHOTS=0 turns the idea off. SHOTS=4 turns it on. Nothing else differs.
"""
import os, torch
from transformers import AutoModelForCausalLM, AutoTokenizer

SHOTS = int(os.environ.get("SHOTS", "4"))          # the ablation switch

tok = AutoTokenizer.from_pretrained("distilgpt2")
model = AutoModelForCausalLM.from_pretrained("distilgpt2"); model.eval()

EXAMPLES = [("dog", "bark"), ("cat", "meow"), ("cow", "moo"), ("duck", "quack")]
TESTS    = [("sheep", " baa"), ("pig", " oink"), ("lion", " roar"), ("horse", " neigh")]

def prompt_for(word):
    shots = "".join(f"{a} => {b}\n" for a, b in EXAMPLES[:SHOTS])
    return f"{shots}{word} =>"

total = 0.0
print(f"SHOTS={SHOTS}")
for word, answer in TESTS:
    ids = tok(prompt_for(word), return_tensors="pt").input_ids
    with torch.no_grad():
        probs = torch.softmax(model(ids).logits[0, -1], dim=-1)
    prob = probs[tok(answer).input_ids[0]].item()
    total += prob
    print(f"  P({answer!r} | prompt) = {prob*100:7.4f}%")
print(f"mean = {total/len(TESTS)*100:.4f}%")
```

**Line by line:**

- `SHOTS` from the environment — the switch, and the reason this is a demonstration rather than an
  illustration. Everything else about the two runs is byte-identical.
- `EXAMPLES[:SHOTS]` — at `SHOTS=0` the slice is empty, so the prompt collapses to `"sheep =>"`
  with no branch anywhere. Prefer this over an `if`: a branch is a second code path, and a second
  code path is somewhere a difference other than the ablation can hide.
- `TESTS` disjoint from `EXAMPLES` — the four test animals never appear in the prompt. Testing on a
  shown example would measure copying, not in-context learning, and would produce a much larger and
  entirely meaningless effect.
- `probs[tok(answer).input_ids[0]]` — the probability of the correct **first** token, with its
  leading space. Reading a specific token's probability rather than the top of the list is what
  makes this a number instead of a judgement call.
- `mean` over four items — one item is an anecdote. Four is barely better, and the honest reading
  is in *When it breaks* below.

`run.sh`:

```bash
#!/usr/bin/env bash
set -euo pipefail
echo "=== ablation OFF ==="; SHOTS=0 uv run python fewshot.py
echo "=== ablation ON  ==="; SHOTS=4 uv run python fewshot.py
```

**Line by line:**

- `set -euo pipefail` — exit on error, on unset variables, and on a failure anywhere in a pipe.
  Without it a failed first run is invisible and you compare one result against nothing.
- Both runs in one script, always in this order — so the comparison cannot be made from a
  half-remembered earlier run.

Both outputs, in full:

```text
=== ablation OFF ===
SHOTS=0
  P(' baa'   | prompt) =  0.1369%
  P(' oink'  | prompt) =  0.1312%
  P(' roar'  | prompt) =  0.0002%
  P(' neigh' | prompt) =  0.0002%
mean = 0.0671%
=== ablation ON  ===
SHOTS=4
  P(' baa'   | prompt) =  0.4490%
  P(' oink'  | prompt) =  0.1505%
  P(' roar'  | prompt) =  0.0085%
  P(' neigh' | prompt) =  0.0100%
mean = 0.1545%
```

*Observed 2026-09-07 · `distilgpt2` (82M) · torch 2.14.0+cpu · transformers 5.16.1 · CPU only.*

**Cost:** zero. Local model, no API, roughly 350MB downloaded once, seconds of CPU.

The mean rises 0.0671% → 0.1545%, about 2.3×, and every one of the four items improves. Four
examples in the prompt changed the model's beliefs with no gradient update anywhere. With the
switch off, the effect vanishes — which is the only way to know the effect was the idea and not the
code.

## When it breaks

The demo reproduces the paper's **direction** and not its **magnitude**, and the honest statement
of the limit is the most useful thing in this document.

0.1545% is not a model that knows what a sheep says. It is a model that is slightly less wrong than
it was. The paper's headline results come from 175 billion parameters; this runs on 82 million,
roughly 2000× smaller. No prompt engineering closes that gap, because the gap *is* the paper's
finding: the benefit of in-context examples grows with scale, and at this scale there is very
little to have.

Three further limits, stated where the paper states them:

- **Sensitivity to format and order.** Results move with the choice of examples, their order and
  the separator. The paper reports this; it is not a small effect, and it is why day 112 permutes
  examples in its robustness test rather than trusting one arrangement.
- **The context window bounds *k*.** With 2048 tokens, examples compete with the input itself. On
  day 127 they will also compete with retrieved documents.
- **Contamination.** With a training set drawn from a large web crawl, some evaluation data was
  plausibly present in pre-training. The paper analyses this directly and reports it as a real
  caveat rather than a footnote — which is the standard day 36's decontamination work is held to.

**And this demo's own weakness, stated plainly:** four test items, one prompt format, one model. It
is enough to show a direction and not enough to make a claim about size. Reporting the 2.3× without
the absolute numbers would be exactly the overreach this curriculum's Principle 8 forbids.

## In production

**What survived.** In-context learning is now the default way to adapt a model, and it is
load-bearing across this entire curriculum: prompting as a discipline (day 108), the format
examples inside RAG prompts (day 127), the rubric examples that calibrate an LLM judge (day 209).
The framing that a frozen model plus a well-constructed prompt is a working system — rather than a
starting point awaiting a dataset — is this document's lasting contribution, and it is why prompt
engineering exists as a job at all.

**What did not.** Several things the paper's framing implied have not held:

- **Scale alone is not the answer.** The paper's arc points at bigger models; the field's answer
  turned out to be *better-trained* models. Day 30's Chinchilla result showed these models were
  substantially under-trained for their size, and later work put more of the gain into data and
  post-training than into parameters.
- **Raw few-shot prompting was largely superseded by instruction tuning.** The paper's models
  needed examples to infer the task. Instruction-tuned models (day 53) follow a described task
  zero-shot, so the many-shot prompts this paper depends on are now a specialised tool rather than
  the standard interface. The mechanism survived; the ergonomics were replaced.
- **The confabulation problem is not addressed here at all.** Nothing in in-context learning makes
  an answer true. Everything in part
  [3.1](../parts/03-synthesis/3.1-the-model-has-no-plan.md) applies unchanged to a few-shot prompt,
  and the retrieval and evaluation tracks in this plan exist because prompting alone did not solve
  it.

**The interview question.** *"What did GPT-3 actually demonstrate?"* The answer that shows you have
read it rather than heard about it: not that a big model is good at things, but that in-context
learning improves with scale — and the honest follow-up is that the scaling recipe it implied was
corrected two years later.

## Check yourself

- **Run:** the demo with `SHOTS=0`, `2` and `4`. Expect the mean to rise each time. Then swap one
  example for a deliberately inconsistent format — `dog: bark` among the `=>` lines — and watch the
  effect shrink.
- **Say out loud:** What did this document claim that survived, what did it imply that was later
  corrected, and why does the demo's 2.3× improvement not mean the idea works well at this size?
