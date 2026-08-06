from __future__ import annotations

from datetime import datetime, timezone

from catalog_lib import CATEGORY_ORDER, ROOT, load_catalog, write_editor_choice_slugs
from generate_readme import editor_section, is_dead, lifecycle


TARGETS = {
    "Bugs finders": 9,
    "Coding standards": 2,
    "Architecture rules": 2,
    "DIY": 1,
    "Fixers": 2,
    "Metrics": 6,
    "Misc": 2,
}


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


def main() -> None:
    tools = load_catalog()
    reference_time = datetime.now(timezone.utc)
    selected: list[dict] = []
    for category in CATEGORY_ORDER:
        ranked = sorted(
            [tool for tool in tools if tool.get("category") == category and is_alive(tool, reference_time)],
            key=lambda item: (-score(item, reference_time), item.get("name", "").lower()),
        )
        selected.extend(ranked[: TARGETS.get(category, 0)])
    selected_slugs = [tool["slug"] for tool in selected]
    write_editor_choice_slugs(selected_slugs)

    lines = [
        "# Static analysis tools for PHP",
        "",
        "This file is generated from `common/catalog/*.yaml` by `scripts/generate_editor_choice.py`.",
        "Selection is deterministic and limited to alive projects only, then ranked by category quota, stars, repository freshness, and archive signals.",
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
