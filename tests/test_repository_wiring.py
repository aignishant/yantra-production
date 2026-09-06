"""The first check that can go RED (plan §2, Principle 9).

It asserts the two things that make every later day possible: the plan is readable and its day
map is intact, and no secret has been committed. Break either on purpose and watch this fail —
a check nobody has seen fail has verified nothing.
"""

import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def test_plan_carries_its_markers() -> None:
    plan = (ROOT / "docs" / "00_MASTER_PLAN.md").read_text(encoding="utf-8")
    for marker in ("tracks", "phases", "day-map"):
        assert f"<!-- granth:{marker}:start -->" in plan, marker
        assert f"<!-- granth:{marker}:end -->" in plan, marker


def test_no_env_file_is_tracked() -> None:
    result = subprocess.run(
        ["git", "ls-files", "--error-unmatch", ".env"],
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=False,
    )
    assert result.returncode != 0, result.stdout
