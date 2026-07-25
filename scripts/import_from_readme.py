from __future__ import annotations

import re

from catalog_lib import ROOT, normalize_github_url, save_tool, slugify, write_editor_choice_slugs


LINK_RE = re.compile(r"\[([^\]]+)\]\(([^)]+)\)\s*-?\s*(.*)")


def clean_description(text: str) -> str:
    text = re.sub(r"<[^>]+>", "", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip(" .")


def parse_markdown_list(path, *, start_after_whole_list: bool) -> list[dict]:
    content = path.read_text(encoding="utf-8")
    if start_after_whole_list and "### Whole list" in content:
        content = content.split("### Whole list", 1)[1]
    category = "Misc"
    tools: list[dict] = []
    for raw_line in content.splitlines():
        line = raw_line.strip()
        heading = re.match(r"^#{2,6}\s+(.+)$", line)
        if heading:
            title = heading.group(1).strip()
            if title in {"Bugs finders", "Coding standards", "DIY", "Fixers", "Metrics", "SaaS", "Misc"}:
                category = title
            continue
        if not line.startswith("* ") and not line.startswith("["):
            continue
        line = line[2:] if line.startswith("* ") else line
        match = LINK_RE.search(line)
        if not match:
            continue
        name, url, description = match.groups()
        description = clean_description(description)
        slug = slugify(name)
        tools.append(
            {
                "slug": slug,
                "name": name.strip(),
                "category": category,
                "description": description,
                "website": url.strip(),
                "public_url": url.strip(),
                "repository": normalize_github_url(url.strip()),
                "website_status": "unknown",
                "website_status_code": 0,
                "website_checked_at": None,
                "website_error": "",
                "packagist": None,
                "latest_version": "",
                "latest_version_released_at": None,
                "stars": 0,
                "repo_updated_at": None,
                "metadata_updated_at": None,
                "editor_choice": False,
                "quality_tags": [],
                "source": "README.md",
                "notes": "",
            }
        )
    return tools


def main() -> None:
    whole_list = parse_markdown_list(ROOT / "README.md", start_after_whole_list=True)
    editor_tools = parse_markdown_list(ROOT / "EDITOR-CHOISE.md", start_after_whole_list=False)
    editor_slugs = {tool["slug"] for tool in editor_tools}
    seen: set[str] = set()
    for tool in whole_list:
        if tool["slug"] in seen:
            continue
        seen.add(tool["slug"])
        tool["editor_choice"] = tool["slug"] in editor_slugs
        save_tool(tool)
    write_editor_choice_slugs(sorted(editor_slugs))
    print(f"Imported {len(seen)} tools into common/catalog")


if __name__ == "__main__":
    main()
