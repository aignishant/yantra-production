"""The part budget and the plan-version comparison — plan §20.10, ADR-0007.

`granth.py depth` on the two written days cannot exercise these: both days are grandfathered and
both sit under the ceiling. Without this file the budget is a rule nobody has ever seen fire.
"""

from __future__ import annotations

import granth


def report(day: int, parts: int, sources: int) -> granth.Report:
    r = granth.Report(day=day)
    r.parts, r.sources = parts, sources
    return r


def budget(day: int, parts: int, sources: int = 0, **overrides: object) -> list[str]:
    """Run the budget check alone and return its failures."""
    cfg = granth.Config(**overrides)  # type: ignore[arg-type]
    r = report(day, parts, sources)
    granth.check_part_budget(cfg, day, r, f"days/day-{day:03d}-x")
    return r.failures


def test_three_parts_is_the_target_and_passes() -> None:
    assert budget(day=42, parts=3) == []


def test_the_ceiling_itself_passes() -> None:
    assert budget(day=42, parts=4) == []


def test_one_document_over_the_ceiling_fails() -> None:
    failures = budget(day=42, parts=5)
    assert len(failures) == 1
    assert "5 documents" in failures[0]
    assert "§20.10" in failures[0]


def test_a_source_part_counts_against_the_budget() -> None:
    """Three parts and a source is four documents. A fourth part makes it five."""
    assert budget(day=42, parts=3, sources=1) == []
    assert len(budget(day=42, parts=4, sources=1)) == 1


def test_days_before_the_cutoff_are_grandfathered() -> None:
    """Day 1 is seven parts, written under plan v2.0.0. It must not fail (ADR-0007)."""
    assert budget(day=1, parts=7) == []
    assert budget(day=0, parts=6) == []


def test_the_cutoff_day_itself_is_bound() -> None:
    assert len(budget(day=2, parts=7)) == 1


def test_the_budget_can_be_switched_off() -> None:
    assert budget(day=42, parts=22, max_parts=0) == []


def test_version_tuple_orders_plan_versions() -> None:
    assert granth.version_tuple("v2.0.0") < granth.version_tuple("v2.1.0")
    assert granth.version_tuple("v2.1.0") == granth.version_tuple("v2.1.0")
    assert granth.version_tuple("v10.0.0") > granth.version_tuple("v9.0.0")


def test_an_unparseable_version_is_never_treated_as_older() -> None:
    """A day claiming a version nobody can parse must fail loudly, not pass as grandfathered."""
    assert granth.version_tuple("") > granth.version_tuple("v2.1.0")
    assert granth.version_tuple("draft") > granth.version_tuple("v2.1.0")


def test_the_story_is_no_longer_a_section_of_its_own() -> None:
    """ADR-0007 merged it into 'the idea in plain language'. Two headings meant two openings."""
    assert "the story" not in granth.PART_SECTIONS
    assert "the idea in plain language" in granth.PART_SECTIONS
    assert len(granth.PART_SECTIONS) == 10
