from __future__ import annotations

import argparse
from datetime import datetime, timezone

from catalog_lib import (
    CATEGORY_ORDER,
    ROOT,
    load_catalog,
    read_editor_choice_copy,
    read_editor_choice_slugs,
)
from generate_readme import apply_editor_choice_copy, editor_section, is_dead, lifecycle
from generate_readme import reference_time_from_values


TARGETS = {category: 1 for category in CATEGORY_ORDER if category != "SaaS"}
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
    parser = argparse.ArgumentParser(description="Generate the curated Editors' Choice document")
    parser.add_argument(
        "--as-of",
        help="ISO-8601 date used for reproducible lifecycle labels; SOURCE_DATE_EPOCH is also supported",
    )
    args = parser.parse_args()
    tools = load_catalog()
    reference_time = reference_time_from_values(args.as_of)
    selected_slugs = sorted(read_editor_choice_slugs())
    tools_by_slug = {str(tool.get("slug")): tool for tool in tools}
    missing = [slug for slug in selected_slugs if slug not in tools_by_slug]
    if missing:
        raise ValueError("Editors' Choice references unknown catalog entries: " + ", ".join(missing))
    selected = sorted(
        [tools_by_slug[slug] for slug in selected_slugs],
        key=lambda item: (CATEGORY_ORDER.index(item.get("category")), item.get("name", "").casefold()),
    )
    historical = [str(tool.get("slug")) for tool in selected if is_dead(tool, reference_time)]
    if historical:
        raise ValueError("Editors' Choice contains historical entries: " + ", ".join(historical))
    selected = apply_editor_choice_copy(selected, read_editor_choice_copy())

    lines = [
        "# Static analysis tools for PHP",
        "",
        "This file is generated from the manually approved membership in `common/editor-choice.yaml`, catalog records in `common/catalog/*.yaml`, and editorial copy in `common/editor-choice-copy.yaml`.",
        "Selection considers present-day PHP relevance, maintenance, documentation, adoption, and a distinct practical use case. Stars and repository freshness are supporting evidence, not an automatic ranking or per-category quota.",
        "Generation fails when a selected tool is historical or lacks a specific recommendation and rationale.",
        "⭐ shows GitHub stars.",
        "",
    ]
    for category in CATEGORY_ORDER:
        grouped = [tool for tool in selected if tool.get("category") == category]
        if not grouped:
            continue
        lines.append(editor_section(category, grouped, level=2, reference_time=reference_time))
    output = "\n".join(lines).rstrip() + "\n"
    (ROOT / "EDITORS-CHOICE.md").write_text(output, encoding="utf-8")
    (ROOT / "EDITOR-CHOISE.md").write_text(
        "# Editors' Choice moved\n\n"
        "This compatibility file preserves the repository's former misspelled path. "
        "See [EDITORS-CHOICE.md](EDITORS-CHOICE.md) for the generated curated shortlist.\n",
        encoding="utf-8",
    )
    noun = "tool" if len(selected) == 1 else "tools"
    print(f"Generated EDITORS-CHOICE.md with {len(selected)} {noun} and compatibility redirect")


if __name__ == "__main__":
    main()
