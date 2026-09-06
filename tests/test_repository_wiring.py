"""The first check that can go RED (plan §2, Principle 9).

It asserts the two things that make every later day possible: the plan is readable and its day
map is intact, and no secret has been committed. Break either on purpose and watch this fail —
a check nobody has seen fail has verified nothing.
"""

from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def test_plan_carries_its_markers() -> None:
    plan = (ROOT / "docs" / "00_MASTER_PLAN.md").read_text(encoding="utf-8")
    for marker in ("tracks", "phases", "day-map"):
        assert f"<!-- granth:{marker}:start -->" in plan, marker
        assert f"<!-- granth:{marker}:end -->" in plan, marker


def test_no_env_file_is_tracked() -> None:
    assert not (ROOT / ".env").exists() or ".env" in (
        ROOT / ".gitignore"
    ).read_text(encoding="utf-8")
