# PINS — append-only

Every version, model string, quota and limit this curriculum depends on, **with the date it was
observed and the day that observed it**. Principle 7: never invent a version. A lookup that fails
leaves a `TODO` containing the exact command, never a guess.

**Why dated rows and not a version table:** a version table is wrong within a month and gives no
way to tell what was true when a day was written. These rows do.

| Pinned | Value | How verified | Date observed | Day | Why |
| --- | --- | --- | --- | --- | --- |
| uv | 0.12.3 | `uv --version` | 2026-09-07 | 0 | owns the environment |
| Python | 3.12.10 | `python --version` | 2026-09-07 | 0 | the interpreter selected by this Windows workspace |
| ruff | 0.16.6 | `uv run ruff --version` | 2026-09-07 | 0 | lint + format, both gate steps |
| — | — | — | — | — | *no pins yet — Day 0 adds the toolchain rows* |
