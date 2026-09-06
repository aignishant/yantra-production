# Day 0 — definition of done

`python granth.py done 0` refuses to commit while any box below is unticked. That refusal is the
point: a day is finished when it is understood and the checks are green, and by nothing else.

No box here carries a time estimate, and none ever will.

## Read

- [ ] `parts/01-one-owner/1.1-why-one-tool-owns-the-environment.md` — read · ran its check · answered its question out loud
- [ ] `parts/01-one-owner/1.2-uv-and-the-venv-you-never-activate.md` — read · ran its check · answered its question out loud
- [ ] `parts/02-cannot-leak-a-key/2.1-the-skeleton-and-gitignore-first.md` — read · ran its check · answered its question out loud
- [ ] `parts/02-cannot-leak-a-key/2.2-the-secret-that-was-already-committed.md` — read · ran its check · answered its question out loud
- [ ] `parts/03-the-gate/3.1-what-the-gate-checks.md` — read · ran its check · answered its question out loud
- [ ] `parts/03-the-gate/3.2-the-refusal.md` — read · ran its check · answered its question out loud

## Build

- [ ] `.env.example` — every variable name the project will need, with empty values, committed
- [ ] `pyproject.toml` — `gpu` and `live` pytest markers registered
- [ ] `tests/test_repository_wiring.py` — asserts `.env` is not in `git ls-files`
- [ ] `lab/leak/` — part 2.2 reproduced; confirmed with `git log -p` that the key survives `git rm --cached`

## Check

- [ ] `uv run python -c "import sys; print(sys.executable)"` ends in `.venv/bin/python3`
- [ ] `git check-ignore -v .env` names the rule in `.gitignore`
- [ ] The day's check is green: `uv run pytest tests/test_repository_wiring.py`
- [ ] **Break it on purpose, watch it go red, fix it.** `git add -f .env`, run the wiring test, see it fail, then `git rm --cached .env`
- [ ] All three refusals seen with a non-zero exit, unpiped: `brief 5`, `depth 0` before writing, `done 0` before writing
- [ ] `python granth.py doctor` — green
- [ ] `python granth.py depth 0` — green
- [ ] `python granth.py check` — green across the whole repository

## Record

- [ ] Every term defined for the first time today has a row in `docs/GLOSSARY.md` (seven of them — see the hub's §11)
- [ ] Every version observed today has a dated row in `docs/PINS.md` (three rows)
- [ ] The versions in the hub's §8 were **re-observed today**, not copied from the table
- [ ] No sources were cited today, so `docs/SOURCES.md` gains no row
- [ ] The `docs/PROGRESS.md` row is pasted from the hub's §11
- [ ] `git ls-files | grep -i env` returns **only** `.env.example`
- [ ] Committed with the message from the hub's §11
