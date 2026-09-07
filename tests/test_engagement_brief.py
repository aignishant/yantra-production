"""The engagement brief is a document that can be wrong.

Day 1 part 2.3. A success criterion with no baseline, no owner and no exit condition survives
every outcome, which is what makes it useless. This test refuses that shape.

It checks the *form* of `docs/ENGAGEMENT.md`, never its content: no test can tell whether 7.5 is
the real figure. Day 3 measures the baseline and day 5 turns the brief into a scoped SOW; this
test is what stops either of them being quietly skipped.
"""

from __future__ import annotations

import re
from pathlib import Path

import pytest

BRIEF = Path(__file__).resolve().parents[1] / "docs" / "ENGAGEMENT.md"

REQUIRED_HEADINGS = [
    "## The process",
    "## The success criterion",
    "## Who owns the number",
    "## The exit condition",
    "## What this engagement will not do",
]

VALID_STATUS = ("draft", "baselined", "signed")

STATUS = re.compile(r"^status:\s*(\S+)\s*$", re.M)
NUMBER = re.compile(r"\d+(?:\.\d+)?")
UNIT = re.compile(r"\b(days?|weeks?|per cent|percent|%|claims?|records?|calls?)\b", re.I)
UNFILLED = re.compile(r"TODO\(me\)")


@pytest.fixture(scope="module")
def brief() -> str:
    if not BRIEF.exists():
        pytest.fail(f"{BRIEF.name} does not exist - day 1 part 2.3 creates it")
    return BRIEF.read_text(encoding="utf-8")


def section(text: str, heading: str) -> str:
    """The learner's own answer under one `##` heading.

    Guidance lines are dropped. The scaffold's italic prompts and blockquotes are themselves full
    of numbers and units, and a check those could satisfy would pass a brief nobody had written.
    """
    start = text.index(heading) + len(heading)
    rest = text[start:]
    end = rest.find("\n## ")
    body = rest if end == -1 else rest[:end]
    kept = [ln for ln in body.splitlines() if not ln.lstrip().startswith(("*", ">", "|"))]
    return "\n".join(kept)


def test_every_required_heading_is_present(brief: str) -> None:
    missing = [h for h in REQUIRED_HEADINGS if h not in brief]
    assert not missing, f"the brief is missing {missing} - each one is a question that has an owner"


def test_status_is_declared_and_valid(brief: str) -> None:
    found = STATUS.search(brief)
    assert found, "no 'status:' line - a brief that will not say whether it is a draft is a draft"
    assert found.group(1) in VALID_STATUS, f"status {found.group(1)!r} is not one of {VALID_STATUS}"


def test_nothing_is_left_unfilled(brief: str) -> None:
    left = UNFILLED.findall(brief)
    assert not left, f"{len(left)} TODO(me) marker(s) remain - the brief is a scaffold, not a brief"


def test_the_success_criterion_can_be_wrong(brief: str) -> None:
    body = section(brief, "## The success criterion")
    numbers = NUMBER.findall(body)
    assert len(numbers) >= 2, (
        f"the criterion carries {len(numbers)} number(s); it needs at least two - "
        "a baseline and a target. One number is a level, and a level cannot be improved on."
    )
    assert UNIT.search(body), "the criterion names no unit - 'faster' is a direction, not a measure"


def test_the_number_has_an_owner_and_an_end(brief: str) -> None:
    for heading in ("## Who owns the number", "## The exit condition"):
        body = section(brief, heading).strip()
        assert len(body) > 20, f"{heading!r} is empty - an unowned number is one nobody defends"
