from __future__ import annotations

import argparse
import re
import urllib.error
import urllib.request
import xml.etree.ElementTree as ET
from datetime import datetime, timedelta, timezone

from catalog_lib import (
    CATALOG_DIR,
    CATEGORY_ORDER,
    cli_token,
    github_api_repo_url,
    github_repo_key,
    http_json,
    load_catalog,
    normalize_github_url,
    now_iso,
    positive_int,
    save_tool,
)
from discover_tools import choose_output_slug
from update_catalog import canonical_github_repo_key, update_github_release


SOURCE_URL = "https://github.com/exakat/php-static-analysis-tools"
SOURCE_README_URL = f"https://raw.githubusercontent.com/exakat/php-static-analysis-tools/master/README.md"
LINK_RE = re.compile(r"^\s*\*\s+\[([^]]+)\]\(([^)]+)\)\s*[-–]\s*(.*)$")
HEADING_RE = re.compile(r"^#{2,3}\s+(.+)$")
EXTRA_CATEGORY_MAP = {"Visualization": "Misc", "Also supports PHP": "Misc"}
ATOM_NAMESPACE = {"atom": "http://www.w3.org/2005/Atom"}


def http_text(url: str) -> tuple[str, str]:
    request = urllib.request.Request(url, headers={"User-Agent": "custom-php-analysis-tools-updater"})
    with urllib.request.urlopen(request, timeout=30) as response:
        return response.read().decode("utf-8"), response.geturl()


def parse_source_readme(content: str) -> list[dict]:
    category = "Misc"
    entries: list[dict] = []
    for raw_line in content.splitlines():
        heading = HEADING_RE.match(raw_line)
        if heading:
            title = heading.group(1).strip()
            if title in CATEGORY_ORDER:
                category = title
            elif title in EXTRA_CATEGORY_MAP:
                category = EXTRA_CATEGORY_MAP[title]
            continue
        link = LINK_RE.match(raw_line)
        if not link:
            continue
        name, url, description = link.groups()
        repository = normalize_github_url(url)
        if not repository:
            continue
        entries.append(
            {
                "name": name.strip(),
                "repository": repository,
                "description": description.strip(),
                "category": category,
            }
        )
    return entries


def canonical_repository(entry: dict) -> tuple[str, datetime] | None:
    feed_url = entry["repository"].rstrip("/") + "/commits.atom"
    try:
        content, final_url = http_text(feed_url)
        feed = ET.fromstring(content)
        updated_text = feed.findtext("atom:updated", namespaces=ATOM_NAMESPACE)
        if not updated_text:
            return None
        updated = datetime.fromisoformat(updated_text.replace("Z", "+00:00"))
        repository = final_url.removesuffix("/commits.atom").rstrip("/")
        return repository, updated
    except (urllib.error.HTTPError, urllib.error.URLError, TimeoutError, ET.ParseError, ValueError):
        return None


def build_tool(entry: dict, repo: dict) -> dict:
    repository = repo.get("html_url") or entry["repository"]
    website = repo.get("homepage") or repository
    tags = sorted(set(repo.get("topics") or []) & {"php", "static-analysis", "code-quality", "security"})
    return {
        "name": entry["name"],
        "category": entry["category"],
        "description": (repo.get("description") or entry["description"]).strip(),
        "website": website,
        "public_url": website,
        "website_status": "unknown",
        "website_status_code": 0,
        "website_checked_at": None,
        "website_error": "",
        "repository": repository,
        "packagist": None,
        "latest_version": "",
        "latest_version_released_at": None,
        "stars": int(repo.get("stargazers_count") or 0),
        "repo_updated_at": repo.get("pushed_at") or repo.get("updated_at"),
        "metadata_updated_at": now_iso(),
        "editor_choice": False,
        "quality_tags": tags,
        "source": SOURCE_URL,
        "notes": "Imported from Exakat's PHP static-analysis tools catalog after active-project verification.",
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="Import active GitHub projects from Exakat's PHP analysis catalog.")
    parser.add_argument("--write", action="store_true", help="Write verified active projects into common/catalog.")
    parser.add_argument(
        "--include-releases",
        action="store_true",
        help="Fetch GitHub release metadata while importing. This uses one extra API request per project.",
    )
    parser.add_argument("--limit", type=positive_int, default=0, help="Maximum additions. 0 means all verified projects.")
    parser.add_argument(
        "--max-inactive-days",
        type=positive_int,
        default=365,
        help="Reject repositories with no default-branch activity within this many days.",
    )
    args = parser.parse_args()

    source, _ = http_text(SOURCE_README_URL)
    entries = parse_source_readme(source)
    known = {
        canonical_github_repo_key(key, token=None)
        for tool in load_catalog()
        if (key := github_repo_key(tool.get("repository")))
    }
    seen = set(known)
    token = cli_token()
    cutoff = datetime.now(timezone.utc) - timedelta(days=args.max_inactive_days)
    reserved_slugs: set[str] = set()
    added = 0
    skipped_known = 0
    skipped_dead = 0
    skipped_unknown = 0

    for entry in entries:
        canonical = canonical_repository(entry)
        if not canonical:
            skipped_unknown += 1
            continue
        repository, feed_updated = canonical
        repo_key = github_repo_key(repository)
        if not repo_key or repo_key.casefold() in seen:
            skipped_known += 1
            continue
        seen.add(repo_key.casefold())
        if feed_updated < cutoff:
            skipped_dead += 1
            continue
        try:
            repo = http_json(github_api_repo_url(repo_key), token=token)
        except (urllib.error.HTTPError, urllib.error.URLError, TimeoutError) as exc:
            print(f"skipped unverifiable: {repo_key} | {exc}")
            skipped_unknown += 1
            continue
        repo_updated_at = repo.get("pushed_at") or repo.get("updated_at")
        try:
            repo_updated = datetime.fromisoformat(repo_updated_at.replace("Z", "+00:00"))
        except (AttributeError, ValueError):
            skipped_unknown += 1
            continue
        if repo.get("archived") or repo_updated < cutoff:
            skipped_dead += 1
            continue

        tool = build_tool(entry, repo)
        slug, already_exists = choose_output_slug(
            {"name": entry["name"], "full_name": repo.get("full_name") or repo_key},
            CATALOG_DIR,
            reserved_slugs,
        )
        if already_exists:
            skipped_known += 1
            continue
        tool["slug"] = slug
        if args.include_releases:
            update_github_release(tool, repo_key, token)
        if args.write:
            save_tool(tool)
        print(
            f"{'added' if args.write else 'verified'}: {tool['name']} | {tool['repository']} | "
            f"updated={tool['repo_updated_at']} | file={CATALOG_DIR / (slug + '.yaml')}"
        )
        added += 1
        if args.limit and added >= args.limit:
            break

    print(
        f"Exakat import summary: added={added}, known={skipped_known}, dead={skipped_dead}, "
        f"unverifiable={skipped_unknown}, source_entries={len(entries)}"
    )


if __name__ == "__main__":
    main()
