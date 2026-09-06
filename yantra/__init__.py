"""Yantra — the shared code the days import rather than reimplement.

Nothing lands here speculatively. A module in this package exists because a day needed it and a
second day would otherwise have copied it; the day that introduced it is named in its docstring.
"""

from __future__ import annotations

__all__ = ["hardware"]
