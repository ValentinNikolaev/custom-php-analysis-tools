from __future__ import annotations

from datetime import datetime, timezone

from catalog_lib import CATEGORY_ORDER, ROOT, category_rank, load_catalog, read_editor_choice_slugs


def md_escape(value: str) -> str:
    return value.replace("|", "\\|").replace("\n", " ")


def md_link_text_escape(value: str) -> str:
    escaped = value.replace("\\", "\\\\")
    for character in "[]*_`":
        escaped = escaped.replace(character, f"\\{character}")
    return md_escape(escaped)


def latest_release_value(tool: dict) -> str:
    name = tool.get("latest_release_name") or tool.get("latest_release_tag")
    url = tool.get("latest_release_url")
    if name and url:
        return f"[**{md_link_text_escape(str(name))}**]({url})"
    if name:
        return f"**{md_link_text_escape(str(name))}**"
    return md_escape(str(tool.get("latest_version") or "-"))


def link_for(tool: dict) -> str:
    return tool.get("public_url") or tool.get("website") or tool.get("repository") or tool.get("packagist") or "#"


def stars_value(tool: dict) -> int:
    return int(tool.get("stars") or 0)


def parse_date(value: str | None) -> datetime | None:
    if not value:
        return None
    return datetime.fromisoformat(value.replace("Z", "+00:00"))


def lifecycle(tool: dict, reference_time: datetime | None = None) -> tuple[int, str]:
    updated = parse_date(tool.get("repo_updated_at"))
    if not updated:
        return (4, "![Unknown](https://img.shields.io/badge/status-unknown-lightgrey)")
    reference_time = reference_time or datetime.now(timezone.utc)
    days = max((reference_time - updated).days, 0)
    if days >= 365:
        return (3, "![Dead](https://img.shields.io/badge/status-dead-red)")
    if days >= 183:
        return (2, "![Almost dead](https://img.shields.io/badge/status-almost_dead-orange)")
    if days >= 90:
        return (1, "![Dying](https://img.shields.io/badge/status-dying-yellow)")
    return (0, "![Alive](https://img.shields.io/badge/status-alive-brightgreen)")


def is_dead(tool: dict, reference_time: datetime | None = None) -> bool:
    return "archived" in set(tool.get("quality_tags") or []) or lifecycle(tool, reference_time)[0] == 3


def sorted_for_table(tools: list[dict], reference_time: datetime | None = None) -> list[dict]:
    reference_time = reference_time or datetime.now(timezone.utc)
    return sorted(
        tools,
        key=lambda item: (lifecycle(item, reference_time)[0], -stars_value(item), item.get("name", "").lower()),
    )


def tool_line(tool: dict, include_stats: bool = True) -> str:
    stats: list[str] = []
    if include_stats and tool.get("stars"):
        stats.append(f"{tool['stars']:,} stars")
    if include_stats and tool.get("repo_updated_at"):
        stats.append(f"updated {tool['repo_updated_at'][:10]}")
    if tool.get("latest_release_name") and tool.get("latest_release_url"):
        stats.append(
            f"latest release [{md_link_text_escape(str(tool['latest_release_name']))}]"
            f"({tool['latest_release_url']})"
        )
    elif tool.get("latest_version"):
        stats.append(f"latest {tool['latest_version']}")
    if tool.get("website_status") == "unavailable":
        stats.append("site unavailable")
    if tool.get("repository"):
        stats.append(f"[repo]({tool['repository']})")
    if tool.get("packagist"):
        stats.append(f"[packagist]({tool['packagist']})")
    suffix = f" ({'; '.join(stats)})" if stats else ""
    description = tool.get("description") or "No description available."
    return f"* [{tool['name']}]({link_for(tool)}) - {description}{suffix}"


def tool_row(tool: dict, reference_time: datetime | None = None) -> str:
    name = f"[{md_escape(tool['name'])}]({link_for(tool)})"
    description = md_escape(tool.get("description") or "No description available.")
    stars = f"{stars_value(tool):,}" if stars_value(tool) else "-"
    status = lifecycle(tool, reference_time)[1]
    updated = (tool.get("repo_updated_at") or "")[:10] or "-"
    latest = latest_release_value(tool)
    links = []
    if tool.get("repository"):
        links.append(f"[GitHub]({tool['repository']})")
    if tool.get("packagist"):
        links.append(f"[Packagist]({tool['packagist']})")
    if tool.get("website_status") == "unavailable":
        links.append("Site unavailable")
    return f"| {name} | {description} | {status} | {stars} | {updated} | {latest} | {'<br>'.join(links) or '-'} |"


def memorial_row(tool: dict) -> str:
    name = f"[🕯️ {md_escape(tool['name'])}]({link_for(tool)})"
    contribution = md_escape(tool.get("description") or "A valued part of PHP's analysis-tooling history.")
    category = md_escape(tool.get("category") or "Misc")
    last_activity = (tool.get("repo_updated_at") or "")[:10] or "Unknown"
    links = []
    if tool.get("repository"):
        links.append(f"[Source]({tool['repository']})")
    if tool.get("packagist"):
        links.append(f"[Packagist]({tool['packagist']})")
    return f"| {name} | {contribution} | {category} | {last_activity} | {'<br>'.join(links) or '-'} |"


def memorial_section(tools: list[dict]) -> str:
    lines = [
        '<a id="in-memoriam"></a>',
        "",
        "## 🕯️ In Memoriam — PHP Analysis Pioneers",
        "",
        "These projects are no longer actively maintained, but their ideas, code, and communities made a lasting contribution to the PHP ecosystem. We preserve them here with gratitude and respect.",
        "",
        "| Project | Contribution | Category | Last activity | Legacy links |",
        "|---|---|---|---|---|",
    ]
    lines.extend(
        memorial_row(tool)
        for tool in sorted(tools, key=lambda item: ((item.get("repo_updated_at") or ""), item.get("name", "").casefold()), reverse=True)
    )
    lines.append("")
    return "\n".join(lines)


def section(title: str, tools: list[dict], level: int = 5, reference_time: datetime | None = None) -> str:
    reference_time = reference_time or datetime.now(timezone.utc)
    lines = [f"{'#' * level} {title}", ""]
    lines.extend(
        [
            "| Tool | Description | Stars | Updated | Latest release | Links |",
            "|---|---|---|---:|---|---|---|",
        ]
    )
    lines[-2] = "| Tool | Description | Status | ⭐ Stars | Updated | Latest release | Links |"
    lines.extend(tool_row(tool, reference_time) for tool in sorted_for_table(tools, reference_time))
    lines.append("")
    return "\n".join(lines)


def main() -> None:
    tools = load_catalog()
    reference_time = datetime.now(timezone.utc)
    dead_tools = [tool for tool in tools if is_dead(tool, reference_time)]
    published_tools = [tool for tool in tools if not is_dead(tool, reference_time)]
    editor_slugs = read_editor_choice_slugs()
    by_category = {
        category: [tool for tool in published_tools if tool.get("category") == category]
        for category in CATEGORY_ORDER
    }
    editor_tools = sorted(
        [tool for tool in published_tools if tool.get("slug") in editor_slugs],
        key=lambda item: (category_rank(item.get("category")), item.get("name", "").lower()),
    )
    lines = [
        "![GitHub last commit](https://img.shields.io/github/last-commit/ValentinNikolaev/custom-php-analysis-tools)",
        "![visitors](https://visitor-badge.laobi.icu/badge?page_id=ValentinNikolaev.custom-php-analysis-tools)",
        "",
        "# Static analysis tools for PHP",
        "",
        "A generated catalog of PHP static analysis, code quality, coding standards, metrics, refactoring, and SaaS tools.",
        "",
        "Inspired by the pioneering [PHP Static Analysis Tools catalog by Exakat](https://github.com/exakat/php-static-analysis-tools) and its contributors.",
        "",
        "The source of truth is `common/catalog/*.yaml`. Run `python scripts/full_workflow.py` to refresh metadata and regenerate this file.",
        "",
        "To review and import newly listed active projects from Exakat, run `python scripts/full_workflow.py --import-exakat`.",
        "",
        "## Table of Contents",
        "",
    ]
    lines.extend(f"* [{category}](#{category.lower().replace(' ', '-')})" for category in CATEGORY_ORDER)
    lines.append("* [In Memoriam](#in-memoriam)")
    lines.extend(["", "### Editors' Choice", ""])
    for category in CATEGORY_ORDER:
        grouped = [tool for tool in editor_tools if tool.get("category") == category]
        if grouped:
            lines.append(section(category, grouped, reference_time=reference_time))
    lines.extend(["### Whole list", ""])
    for category in CATEGORY_ORDER:
        grouped = by_category.get(category) or []
        if grouped:
            lines.append(section(category, grouped, reference_time=reference_time))
    if dead_tools:
        lines.append(memorial_section(dead_tools))
    (ROOT / "README.md").write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")
    print(f"Generated README.md from {len(published_tools)} current and {len(dead_tools)} memorial catalog entries")


if __name__ == "__main__":
    main()
