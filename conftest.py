"""Makes the repository root importable, so `tests/` can `import yantra` without an install.

This project has no `[build-system]` in `pyproject.toml` on purpose — `uv` treats it as a virtual
project, so `yantra/` is never installed into the venv. pytest inserts the directory holding the
root `conftest.py` onto `sys.path`, which is the whole reason this file exists. Nothing else
belongs in it: a conftest that grows fixtures is a conftest nobody can read.
"""

from __future__ import annotations
