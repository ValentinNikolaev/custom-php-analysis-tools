from __future__ import annotations

from catalog_lib import CATEGORY_ORDER, ROOT, category_rank, load_catalog, read_editor_choice_slugs


def link_for(tool: dict) -> str:
    return tool.get("public_url") or tool.get("website") or tool.get("repository") or tool.get("packagist") or "#"


def tool_line(tool: dict, include_stats: bool = True) -> str:
    stats: list[str] = []
    if include_stats and tool.get("stars"):
        stats.append(f"{tool['stars']:,} stars")
    if include_stats and tool.get("repo_updated_at"):
        stats.append(f"updated {tool['repo_updated_at'][:10]}")
    if tool.get("latest_version"):
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


def section(title: str, tools: list[dict]) -> str:
    lines = [f"##### {title}", ""]
    lines.extend(tool_line(tool) for tool in tools)
    lines.append("")
    return "\n".join(lines)


def main() -> None:
    tools = load_catalog()
    editor_slugs = read_editor_choice_slugs()
    by_category = {
        category: [tool for tool in tools if tool.get("category") == category]
        for category in CATEGORY_ORDER
    }
    editor_tools = sorted(
        [tool for tool in tools if tool.get("slug") in editor_slugs],
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
        "The source of truth is `common/catalog/*.yaml`. Run `python scripts/full_workflow.py` to refresh metadata and regenerate this file.",
        "",
        "## Table of Contents",
        "",
    ]
    lines.extend(f"* [{category}](#{category.lower().replace(' ', '-')})" for category in CATEGORY_ORDER)
    lines.extend(["", "### Editors' Choice", ""])
    for category in CATEGORY_ORDER:
        grouped = [tool for tool in editor_tools if tool.get("category") == category]
        if grouped:
            lines.append(section(category, grouped))
    lines.extend(["### Whole list", ""])
    for category in CATEGORY_ORDER:
        grouped = by_category.get(category) or []
        if grouped:
            lines.append(section(category, grouped))
    (ROOT / "README.md").write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")
    print(f"Generated README.md from {len(tools)} catalog entries")


if __name__ == "__main__":
    main()
