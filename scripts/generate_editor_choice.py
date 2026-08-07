from __future__ import annotations

from datetime import datetime, timezone

from catalog_lib import (
    CATEGORY_ORDER,
    ROOT,
    load_catalog,
    read_editor_choice_copy,
    write_editor_choice_slugs,
)
from generate_readme import apply_editor_choice_copy, editor_section, is_dead, lifecycle


TARGETS = {category: 3 for category in CATEGORY_ORDER if category != "SaaS"}
MINIMUM_REPOSITORY_STARS = 500


def parse_date(value: str | None) -> datetime | None:
    if not value:
        return None
    return datetime.fromisoformat(value.replace("Z", "+00:00"))


def score(tool: dict, reference_time: datetime | None = None) -> float:
    stars = int(tool.get("stars") or 0)
    updated = parse_date(tool.get("repo_updated_at"))
    age_bonus = 0.0
    if updated:
        reference_time = reference_time or datetime.now(timezone.utc)
        days = max((reference_time - updated).days, 0)
        age_bonus = max(0, 3650 - days) / 3650
    tag_bonus = 0.0
    tags = set(tool.get("quality_tags") or [])
    if "archived" in tags:
        tag_bonus -= 2.5
    if "static-analysis" in tags:
        tag_bonus += 0.3
    return stars ** 0.5 + age_bonus * 10 + tag_bonus


def is_alive(tool: dict, reference_time: datetime | None = None) -> bool:
    return not is_dead(tool, reference_time) and lifecycle(tool, reference_time)[0] == 0


def is_editor_choice_candidate(tool: dict, reference_time: datetime | None = None) -> bool:
    if not is_alive(tool, reference_time):
        return False
    if "historical-analysis-only" in set(tool.get("quality_tags") or []):
        return False
    return not tool.get("repository") or int(tool.get("stars") or 0) >= MINIMUM_REPOSITORY_STARS


def main() -> None:
    tools = load_catalog()
    reference_time = datetime.now(timezone.utc)
    selected: list[dict] = []
    for category in CATEGORY_ORDER:
        ranked = sorted(
            [
                tool
                for tool in tools
                if tool.get("category") == category and is_alive(tool, reference_time)
                and "historical-analysis-only" not in set(tool.get("quality_tags") or [])
            ],
            key=lambda item: (-score(item, reference_time), item.get("name", "").lower()),
        )
        preferred = [tool for tool in ranked if is_editor_choice_candidate(tool, reference_time)]
        fallback = [tool for tool in ranked if tool not in preferred]
        selected.extend((preferred + fallback)[: TARGETS.get(category, 0)])
    selected_slugs = [tool["slug"] for tool in selected]
    selected = apply_editor_choice_copy(selected, read_editor_choice_copy())
    write_editor_choice_slugs(selected_slugs)

    lines = [
        "# Static analysis tools for PHP",
        "",
        "This file is generated from `common/catalog/*.yaml` by `scripts/generate_editor_choice.py`.",
        "Selection is deterministic and limited to three alive projects per installable-tool category. It prefers repositories with at least 500 GitHub stars, fills sparse categories from the remaining active projects, then ranks by stars, repository freshness, and archive signals.",
        "A human or LLM writes the recommendations and reasons in `common/editor-choice-copy.yaml`, followed by an editorial pass. Generation fails when a selected tool lacks either field.",
        "⭐ shows GitHub stars; 🥇, 🥈, and 🥉 mark the first three entries in each section.",
        "",
    ]
    for category in CATEGORY_ORDER:
        grouped = [tool for tool in selected if tool.get("category") == category]
        if not grouped:
            continue
        lines.append(editor_section(category, grouped, level=2, reference_time=reference_time))
    (ROOT / "EDITOR-CHOISE.md").write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")
    print(f"Generated EDITOR-CHOISE.md with {len(selected)} tools")


if __name__ == "__main__":
    main()
