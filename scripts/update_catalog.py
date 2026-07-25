from __future__ import annotations

import argparse
import urllib.error
from datetime import datetime, timedelta, timezone

from catalog_lib import (
    cli_token,
    github_api_repo_url,
    github_repo_key,
    http_json,
    load_catalog,
    now_iso,
    packagist_search_url,
    positive_int,
    save_tool,
)


def update_from_github(tool: dict, token: str | None) -> bool:
    repo_key = github_repo_key(tool.get("repository") or tool.get("website"))
    if not repo_key:
        return False
    try:
        repo = http_json(github_api_repo_url(repo_key), token=token)
    except (urllib.error.HTTPError, urllib.error.URLError, TimeoutError) as exc:
        print(f"GitHub skipped {tool['slug']}: {exc}")
        return False
    tool["repository"] = repo.get("html_url") or tool.get("repository")
    tool["stars"] = int(repo.get("stargazers_count") or 0)
    tool["repo_updated_at"] = repo.get("pushed_at") or repo.get("updated_at")
    if repo.get("description"):
        tool["description"] = repo["description"].strip()
    if repo.get("homepage") and not tool.get("website"):
        tool["website"] = repo["homepage"]
    tags = list(tool.get("quality_tags") or [])
    if repo.get("archived") and "archived" not in tags:
        tags.append("archived")
    for topic in repo.get("topics") or []:
        if topic in {"static-analysis", "code-quality", "phpstan", "php", "security"} and topic not in tags:
            tags.append(topic)
    tool["quality_tags"] = sorted(tags)
    return True


def update_from_packagist(tool: dict) -> bool:
    if tool.get("packagist"):
        return False
    repo_key = github_repo_key(tool.get("repository"))
    queries = [repo_key, tool.get("name")]
    for query in [q for q in queries if q]:
        try:
            search = http_json(packagist_search_url(query))
        except (urllib.error.HTTPError, urllib.error.URLError, TimeoutError):
            continue
        for result in search.get("results", []):
            result_repo_key = github_repo_key(result.get("repository"))
            if repo_key and result_repo_key == repo_key:
                tool["packagist"] = result.get("url")
                return True
        if search.get("results") and "/" in str(query):
            result = search["results"][0]
            if result.get("url"):
                tool["packagist"] = result["url"]
                return True
    return False


def parse_iso(value: str | None) -> datetime | None:
    if not value:
        return None
    return datetime.fromisoformat(value.replace("Z", "+00:00"))


def is_stale(tool: dict, max_age_hours: int) -> bool:
    updated = parse_iso(tool.get("metadata_updated_at"))
    if not updated:
        return True
    return datetime.now(timezone.utc) - updated > timedelta(hours=max_age_hours)


def main() -> None:
    parser = argparse.ArgumentParser(description="Refresh public metadata in common/catalog/*.yaml")
    parser.add_argument("--limit", type=positive_int, default=0, help="Maximum number of tools to update. 0 means all.")
    parser.add_argument("--skip-packagist", action="store_true")
    parser.add_argument("--max-age-hours", type=positive_int, default=20, help="Skip entries refreshed more recently than this.")
    parser.add_argument("--force", action="store_true", help="Refresh even if metadata_updated_at is recent.")
    args = parser.parse_args()

    tools = load_catalog()
    token = cli_token()
    updated = 0
    for tool in tools:
        if args.limit and updated >= args.limit:
            break
        needs_packagist = not args.skip_packagist and not tool.get("packagist") and tool.get("repository")
        if not args.force and not needs_packagist and not is_stale(tool, args.max_age_hours):
            continue
        should_refresh_github = args.force or is_stale(tool, args.max_age_hours)
        changed = update_from_github(tool, token) if should_refresh_github else False
        if not args.skip_packagist:
            changed = update_from_packagist(tool) or changed
        if changed:
            tool["metadata_updated_at"] = now_iso()
            save_tool(tool)
            updated += 1
            print(f"Updated {tool['slug']}")
    print(f"Refreshed {updated} catalog entries")


if __name__ == "__main__":
    main()
