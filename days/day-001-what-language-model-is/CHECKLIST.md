# Day 1 — definition of done

`python granth.py done 1` refuses to commit while any box below is unticked. That refusal is the
point: a day is finished when it is understood and the checks are green, and by nothing else.

No box here carries a time estimate, and none ever will.

## Read

- [ ] `parts/01-the-objective/1.1-a-distribution-over-the-next-token.md` — read · ran its check · answered its question out loud
- [ ] `parts/01-the-objective/1.2-why-one-objective-is-enough.md` — read · ran its check · answered its question out loud
- [ ] `parts/01-the-objective/1.3-cross-entropy-and-perplexity.md` — read · ran its check · answered its question out loud
- [ ] `parts/02-the-pass/2.1-from-string-to-logits.md` — read · ran its check · answered its question out loud
- [ ] `parts/02-the-pass/2.2-softmax-and-temperature.md` — read · ran its check · answered its question out loud
- [ ] `parts/02-the-pass/2.3-the-loop.md` — read · ran its check · answered its question out loud
- [ ] `parts/03-synthesis/3.1-the-model-has-no-plan.md` — read · ran its check · answered its question out loud

- [ ] `sources/01-language-models-are-few-shot-learners.md` — read **after** the parts · ran the demo · ran the ablation and saw the difference

## Build

- [ ] `lab/peek.py` — prints token list, logits shape, and top-5 next tokens for any prompt
- [ ] `lab/loop.py` — the generation loop by hand, with `--temperature`; `0` takes the greedy path
- [ ] `lab/score.py` — cross-entropy and perplexity; raises clearly on a single-token input instead of returning `nan`
- [ ] `lab/sources/few-shot/` — the demo reproduced, with `run.sh` showing both ablation runs
- [ ] `tests/test_generation.py` — greedy is byte-identical across runs; sampling is not

## Check

- [ ] The day's check is green: `uv run pytest tests/test_generation.py`
- [ ] **Break it on purpose, watch it go red, fix it.** Make the greedy path sample at `T=1.0`; the determinism assertion must fail
- [ ] **Break the ablation on purpose.** Make `SHOTS=0` and `SHOTS=4` build the same prompt; confirm the 2.3× difference vanishes
- [ ] Caused the context-overflow `IndexError` deliberately and recognised what it does *not* say
- [ ] Ran part 3.1's confabulation prompt and **pasted your own real output** into the part — not a transcript copied from anywhere
- [ ] `python granth.py depth 1` — green
- [ ] `python granth.py check` — green across the whole repository

## Record

- [ ] Every term defined for the first time today has a row in `docs/GLOSSARY.md` (eighteen — see the hub's §11)
- [ ] `docs/PINS.md` has torch, transformers and the `distilgpt2` config, **re-observed today** rather than copied
- [ ] `docs/SOURCES.md` has the arXiv:2005.14165 row with the date the record was checked
- [ ] `docs/PROVENANCE.md` has the `distilgpt2` licence row, written **before** the download
- [ ] The `docs/PROGRESS.md` row is pasted from the hub's §11
- [ ] Committed with the message from the hub's §11
