from __future__ import annotations

import re
from datetime import datetime, timezone
from urllib.parse import urlparse

from catalog_lib import (
    CATEGORY_ORDER,
    ROOT,
    category_rank,
    load_catalog,
    read_editor_choice_copy,
    read_editor_choice_slugs,
    slugify,
)


CATEGORY_TITLES = {
    "Bugs finders": "Bug finders",
    "Coding standards": "Coding standards",
    "Architecture rules": "Architecture rules",
    "DIY": "Libraries and building blocks",
    "Fixers": "Fixers and refactoring",
    "Metrics": "Metrics and architecture",
    "SaaS": "Hosted analysis services",
    "Misc": "Specialized tools",
}

CATEGORY_DESCRIPTIONS = {
    "Bugs finders": (
        "Tools that inspect PHP code without running it to identify type errors, defects, dependency problems, "
        "and potential vulnerabilities."
    ),
    "Coding standards": (
        "Linters and rule-enforcement tools for formatting, naming, documentation, and project-specific coding conventions."
    ),
    "Architecture rules": (
        "Ready-to-use tools that enforce dependency boundaries and architectural constraints in an application."
    ),
    "DIY": (
        "Parsers, reflection libraries, and control-flow components for developers building custom analysis rules or tools."
    ),
    "Fixers": (
        "Tools that automatically correct coding-standard violations, upgrade PHP syntax, or refactor existing code."
    ),
    "Metrics": (
        "Tools that measure complexity, coupling, dependencies, maintainability, churn, and other structural properties."
    ),
    "SaaS": (
        "Web-based services that analyze repositories through hosted scans, dashboards, or CI integrations."
    ),
    "Misc": (
        "Wrappers, baseliners, multi-language engines, and focused analysis tools that do not fit the primary categories."
    ),
}

EDITOR_MEDALS = {1: "🥇", 2: "🥈", 3: "🥉"}
GENERIC_EDITOR_REASON_MARKERS = (
    "high adoption and recent maintenance",
    "active community and recent maintenance",
    "recently maintained",
    "selected by the catalog",
)

STATUS_BADGE_COLORS = {
    "Active": "brightgreen",
    "Quiet": "yellow",
    "Inactive": "orange",
    "Unknown": "lightgrey",
}

RESOURCE_BADGES = {
    "github": "https://img.shields.io/badge/-181717?style=flat-square&logo=github&logoColor=white",
    "packagist": "https://img.shields.io/badge/-F5F5F5?style=flat-square&logo=packagist&logoColor=F28D1A",
    "website": "https://img.shields.io/badge/-4285F4?style=flat-square&logo=googlechrome&logoColor=white",
    "unavailable": "https://img.shields.io/badge/website-N%2FA-lightgrey?style=flat-square",
}


def md_escape(value: str) -> str:
    return value.replace("|", "\\|").replace("\n", " ")


def md_link_text_escape(value: str) -> str:
    escaped = value.replace("\\", "\\\\")
    for character in "[]*_`":
        escaped = escaped.replace(character, f"\\{character}")
    return md_escape(escaped)


def category_title(category: str) -> str:
    return CATEGORY_TITLES.get(category, category)


def category_anchor(category: str, prefix: str) -> str:
    return f"{prefix}-{slugify(category_title(category))}"


def latest_release_value(tool: dict) -> str:
    version = tool.get("latest_release_tag") or tool.get("latest_version") or tool.get("latest_release_name")
    if not version:
        return "—"
    value = md_link_text_escape(str(version))
    url = tool.get("latest_release_url")
    return f"[{value}]({url})" if url else value


def link_for(tool: dict) -> str:
    return tool.get("public_url") or tool.get("website") or tool.get("repository") or tool.get("packagist") or "#"


def stars_value(tool: dict) -> int:
    return int(tool.get("stars") or 0)


def parse_date(value: str | None) -> datetime | None:
    if not value:
        return None
    return datetime.fromisoformat(value.replace("Z", "+00:00"))


def lifecycle(tool: dict, reference_time: datetime | None = None) -> tuple[int, str]:
    if "archived" in set(tool.get("quality_tags") or []):
        return (3, "Archived")
    updated = parse_date(tool.get("repo_updated_at"))
    if not updated:
        return (4, "Unknown")
    reference_time = reference_time or datetime.now(timezone.utc)
    days = max((reference_time - updated).days, 0)
    if days >= 365:
        return (3, "Unmaintained")
    if days >= 183:
        return (2, "Inactive")
    if days >= 90:
        return (1, "Quiet")
    return (0, "Active")


def is_dead(tool: dict, reference_time: datetime | None = None) -> bool:
    return lifecycle(tool, reference_time)[0] == 3


def sorted_for_table(tools: list[dict], reference_time: datetime | None = None) -> list[dict]:
    reference_time = reference_time or datetime.now(timezone.utc)
    return sorted(
        tools,
        key=lambda item: (lifecycle(item, reference_time)[0], -stars_value(item), item.get("name", "").lower()),
    )


def short_text(value: str, limit: int = 110) -> str:
    value = re.sub(r"\s+", " ", value).strip()
    if len(value) <= limit:
        return value
    shortened = value[: limit - 1].rsplit(" ", 1)[0].rstrip(".,;:—-")
    return f"{shortened}…"


def purpose_value(tool: dict, limit: int = 110) -> str:
    value = tool.get("best_for") or tool.get("description") or "No description available."
    return md_escape(short_text(str(value), limit))


def format_date(value: str | None) -> str:
    parsed = parse_date(value)
    if not parsed:
        return ""
    return f"{parsed.strftime('%b')} {parsed.day}, {parsed.year}"


def status_value(tool: dict, reference_time: datetime | None = None) -> str:
    label = lifecycle(tool, reference_time)[1]
    color = STATUS_BADGE_COLORS.get(label, "lightgrey")
    lines = [f"![{label}](https://img.shields.io/badge/-{label}-{color}?style=flat-square)"]
    release = latest_release_value(tool)
    if release != "—":
        lines.append(release)
    updated = format_date(tool.get("repo_updated_at"))
    if updated:
        lines.append(f"<sub>Updated {updated}</sub>")
    return "<br>".join(lines)


def tool_name_value(tool: dict, position: int | None = None) -> str:
    name = f"[{md_escape(tool['name'])}]({link_for(tool)})"
    stars = stars_value(tool)
    if not stars:
        return name
    medal = EDITOR_MEDALS.get(position)
    ranking = f"{medal} " if medal else ""
    return f"{name}<br><sub>{ranking}⭐ {stars:,}</sub>"


def resources_value(tool: dict) -> str:
    links = []
    repository = tool.get("repository")
    if repository:
        links.append(f"[![GitHub]({RESOURCE_BADGES['github']})]({repository} \"GitHub source\")")
    if tool.get("packagist"):
        links.append(
            f"[![Packagist]({RESOURCE_BADGES['packagist']})]({tool['packagist']} \"Packagist package\")"
        )
    website = tool.get("public_url") or tool.get("website")
    website_host = urlparse(website).netloc.casefold() if website else ""
    website_is_github_duplicate = bool(repository and website_host in {"github.com", "www.github.com"})
    if website and website != repository and not website_is_github_duplicate and tool.get("website_status") != "unavailable":
        links.append(f"[![Website]({RESOURCE_BADGES['website']})]({website} \"Official website\")")
    if tool.get("website_status") == "unavailable":
        links.append(f"![Website unavailable]({RESOURCE_BADGES['unavailable']})")
    return " ".join(links) or "—"


def tool_line(tool: dict, include_stats: bool = True) -> str:
    stats: list[str] = []
    if include_stats and tool.get("stars"):
        stats.append(f"{tool['stars']:,} stars")
    if include_stats and tool.get("repo_updated_at"):
        stats.append(f"updated {tool['repo_updated_at'][:10]}")
    release = latest_release_value(tool)
    if release != "—":
        stats.append(f"latest {release}")
    if tool.get("website_status") == "unavailable":
        stats.append("site unavailable")
    if tool.get("repository"):
        stats.append(f"[repo]({tool['repository']})")
    if tool.get("packagist"):
        stats.append(f"[packagist]({tool['packagist']})")
    suffix = f" ({'; '.join(stats)})" if stats else ""
    return f"* [{tool['name']}]({link_for(tool)}) - {purpose_value(tool)}{suffix}"


def tool_row(tool: dict, reference_time: datetime | None = None, position: int | None = None) -> str:
    return (
        f"| {tool_name_value(tool, position)} | {purpose_value(tool, 88)} | "
        f"{status_value(tool, reference_time)} | {resources_value(tool)} |"
    )


def saas_row(tool: dict) -> str:
    service = f"[{md_escape(tool['name'])}]({link_for(tool)})"
    delivery = md_escape(short_text(str(tool.get("delivery") or "Hosted service"), 70))
    return f"| {service} | {purpose_value(tool, 88)} | {delivery} | {resources_value(tool)} |"


def apply_editor_choice_copy(tools: list[dict], copy: dict[str, dict[str, str]]) -> list[dict]:
    enriched: list[dict] = []
    missing: list[str] = []
    generic: list[str] = []
    for tool in tools:
        slug = str(tool.get("slug") or "")
        curated = copy.get(slug) or {}
        recommended_for = curated.get("recommended_for")
        why_it_stands_out = curated.get("why_it_stands_out")
        if not recommended_for or not why_it_stands_out:
            missing.append(slug or "<missing slug>")
            continue
        normalized_reason = why_it_stands_out.casefold()
        tool_name = str(tool.get("name") or "").strip().casefold()
        if (
            len(recommended_for.split()) < 5
            or len(why_it_stands_out.split()) < 8
            or (tool_name and tool_name in recommended_for.casefold())
            or any(marker in normalized_reason for marker in GENERIC_EDITOR_REASON_MARKERS)
        ):
            generic.append(slug)
            continue
        enriched.append(
            {
                **tool,
                "best_for": recommended_for,
                "editor_reason": why_it_stands_out,
            }
        )
    if missing:
        raise ValueError("Missing curated Editors' Choice copy for: " + ", ".join(sorted(missing)))
    if generic:
        raise ValueError(
            "Editors' Choice copy is too short, repeats the tool name, or uses a generated metadata fallback for: "
            + ", ".join(sorted(generic))
        )
    return enriched


def recommended_for_value(tool: dict) -> str:
    value = tool.get("best_for")
    if not value:
        raise ValueError(f"Missing curated recommendation for Editors' Choice tool: {tool.get('slug')}")
    return md_escape(str(value))


def editor_reason_value(tool: dict) -> str:
    value = tool.get("editor_reason")
    if not value:
        raise ValueError(f"Missing curated reason for Editors' Choice tool: {tool.get('slug')}")
    return md_escape(str(value))


def editor_row(tool: dict, position: int | None = None) -> str:
    return f"| {tool_name_value(tool, position)} | {recommended_for_value(tool)} | {editor_reason_value(tool)} |"


def memorial_row(tool: dict) -> str:
    name = f"[🕯️ {md_escape(tool['name'])}]({link_for(tool)})"
    contribution = md_escape(short_text(str(tool.get("description") or "A valued part of PHP's analysis-tooling history.")))
    category = md_escape(category_title(tool.get("category") or "Misc"))
    last_activity = format_date(tool.get("repo_updated_at")) or "Unknown"
    return f"| {name} | {contribution} | {category} | {last_activity} | {resources_value(tool)} |"


def memorial_section(tools: list[dict]) -> str:
    lines = [
        '<a id="in-memoriam"></a>',
        "",
        "## 🕯️ In Memoriam — PHP analysis pioneers",
        "",
        "These projects are no longer actively maintained, but their ideas, code, and communities made a lasting contribution to the PHP ecosystem. We preserve them here with gratitude and respect.",
        "",
        "| Project | Contribution | Category | Last activity | Legacy resources |",
        "|---|---|---|---|---|",
    ]
    lines.extend(
        memorial_row(tool)
        for tool in sorted(tools, key=lambda item: ((item.get("repo_updated_at") or ""), item.get("name", "").casefold()), reverse=True)
    )
    lines.append("")
    return "\n".join(lines)


def section(
    category: str,
    tools: list[dict],
    level: int = 3,
    reference_time: datetime | None = None,
    anchor_prefix: str | None = None,
) -> str:
    reference_time = reference_time or datetime.now(timezone.utc)
    lines: list[str] = []
    if anchor_prefix:
        lines.extend([f'<a id="{category_anchor(category, anchor_prefix)}"></a>', ""])
    lines.extend([f"{'#' * level} {category_title(category)}", "", CATEGORY_DESCRIPTIONS.get(category, ""), ""])
    if category == "SaaS":
        lines.extend(["| Service | Best for | Delivery | Link |", "|---|---|---|---|"])
        lines.extend(saas_row(tool) for tool in sorted(tools, key=lambda item: item.get("name", "").casefold()))
    else:
        lines.extend(["| Tool | Best for | Status | Links |", "|---|---|---|---|"])
        ranked_tools = sorted_for_table(tools, reference_time)
        lines.extend(tool_row(tool, reference_time, position) for position, tool in enumerate(ranked_tools, start=1))
    lines.append("")
    return "\n".join(lines)


def editor_section(
    category: str,
    tools: list[dict],
    level: int = 3,
    reference_time: datetime | None = None,
    anchor_prefix: str | None = None,
) -> str:
    reference_time = reference_time or datetime.now(timezone.utc)
    lines: list[str] = []
    if anchor_prefix:
        lines.extend([f'<a id="{category_anchor(category, anchor_prefix)}"></a>', ""])
    lines.extend(
        [
            f"{'#' * level} {category_title(category)}",
            "",
            CATEGORY_DESCRIPTIONS.get(category, ""),
            "",
            "| Tool | Recommended for | Why it stands out |",
            "|---|---|---|",
        ]
    )
    ranked_tools = sorted_for_table(tools, reference_time)
    lines.extend(editor_row(tool, position) for position, tool in enumerate(ranked_tools, start=1))
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
    editor_tools = apply_editor_choice_copy(
        sorted(
            [tool for tool in published_tools if tool.get("slug") in editor_slugs],
            key=lambda item: (category_rank(item.get("category")), item.get("name", "").lower()),
        ),
        read_editor_choice_copy(),
    )
    lines = [
        "![GitHub last commit](https://img.shields.io/github/last-commit/ValentinNikolaev/custom-php-analysis-tools)",
        "![visitors](https://visitor-badge.laobi.icu/badge?page_id=ValentinNikolaev.custom-php-analysis-tools)",
        "",
        "# Static analysis tools for PHP",
        "",
        "A generated catalog of PHP static analysis, code quality, coding standards, metrics, refactoring, and hosted analysis tools.",
        "",
        "Inspired by the pioneering [PHP Static Analysis Tools catalog by Exakat](https://github.com/exakat/php-static-analysis-tools) and its contributors.",
        "",
        "Catalog metadata comes from `common/catalog/*.yaml`; Editors' Choice copy comes from `common/editor-choice-copy.yaml`. Run `python scripts/full_workflow.py` to refresh metadata and regenerate this file.",
        "",
        "To review and import newly listed active projects from Exakat, run `python scripts/full_workflow.py --import-exakat`.",
        "",
        "## Table of contents",
        "",
        "- [Editors' Choice](#editors-choice)",
        "- [Complete catalog](#complete-catalog)",
    ]
    lines.extend(
        f"  - [{category_title(category)}](#{category_anchor(category, 'all')})"
        for category in CATEGORY_ORDER
        if by_category.get(category)
    )
    lines.extend(
        [
            "- [In Memoriam](#in-memoriam)",
            "",
            '<a id="editors-choice"></a>',
            "",
            "## Editors' Choice",
            "",
            "Category quotas and repository data select these active projects. A human or LLM writes the recommendation copy, followed by an editorial pass.",
            "",
            "⭐ shows GitHub stars; 🥇, 🥈, and 🥉 mark the first three repository entries in each section.",
            "",
        ]
    )
    for category in CATEGORY_ORDER:
        grouped = [tool for tool in editor_tools if tool.get("category") == category]
        if grouped:
            lines.append(editor_section(category, grouped, reference_time=reference_time, anchor_prefix="editors"))
    lines.extend(
        [
            '<a id="complete-catalog"></a>',
            "",
            "## Complete catalog",
            "",
            "Repository tables are sorted by activity, then GitHub stars. Hosted services are sorted alphabetically.",
            "",
            "⭐ shows GitHub stars; 🥇, 🥈, and 🥉 mark the first three repository entries in each section.",
            "",
            f"**Links:** ![GitHub]({RESOURCE_BADGES['github']}) GitHub · "
            f"![Packagist]({RESOURCE_BADGES['packagist']}) Packagist · "
            f"![Website]({RESOURCE_BADGES['website']}) official website · "
            f"![Website unavailable]({RESOURCE_BADGES['unavailable']}) unavailable website.",
            "",
            "**Activity:** Active = updated within 90 days; Quiet = 90–182 days; Inactive = 183–364 days; Unknown = no repository activity data. Projects inactive for at least a year move to In Memoriam.",
            "",
        ]
    )
    for category in CATEGORY_ORDER:
        grouped = by_category.get(category) or []
        if grouped:
            lines.append(section(category, grouped, reference_time=reference_time, anchor_prefix="all"))
    if dead_tools:
        lines.append(memorial_section(dead_tools))
    (ROOT / "README.md").write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")
    print(f"Generated README.md from {len(published_tools)} current and {len(dead_tools)} memorial catalog entries")


if __name__ == "__main__":
    main()
