from __future__ import annotations

import argparse
import urllib.error
import urllib.request
from datetime import datetime, timedelta, timezone

from catalog_lib import (
    cli_token,
    github_api_repo_url,
    github_repo_key,
    http_json,
    load_catalog,
    now_iso,
    packagist_package_url,
    packagist_search_url,
    positive_int,
    save_tool,
)


def update_from_github(tool: dict, token: str | None) -> bool:
    repo_key = github_repo_key(tool.get("repository") or tool.get("website"))
    if not repo_key:
        print(f"  GitHub: {tool['slug']} has no public GitHub repository URL")
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
    print(
        f"  GitHub: {tool['slug']} | stars={tool['stars']} | "
        f"repo_updated_at={tool.get('repo_updated_at')} | repo={tool.get('repository')}"
    )
    return True


def packagist_package_name(url: str | None) -> str | None:
    if not url:
        return None
    marker = "packagist.org/packages/"
    if marker not in url:
        return None
    return url.split(marker, 1)[1].strip("/")


def is_stable_version(version: str) -> bool:
    lowered = version.lower()
    return not (lowered.startswith("dev-") or any(part in lowered for part in ["-dev", "alpha", "beta", "rc"]))


def update_packagist_version(tool: dict) -> bool:
    package_name = packagist_package_name(tool.get("packagist"))
    if not package_name:
        return False
    try:
        data = http_json(packagist_package_url(package_name))
    except (urllib.error.HTTPError, urllib.error.URLError, TimeoutError) as exc:
        print(f"  Packagist version skipped {tool['slug']}: {exc}")
        return False
    versions = data.get("packages", {}).get(package_name, [])
    if not versions:
        return False
    latest = next(
        (
            item
            for item in versions
            if is_stable_version(item.get("version_normalized") or item.get("version") or "")
        ),
        versions[0],
    )
    old_values = (tool.get("latest_version"), tool.get("latest_version_released_at"))
    tool["latest_version"] = latest.get("version") or ""
    tool["latest_version_released_at"] = latest.get("time")
    print(
        f"  Packagist version: {tool['slug']} | package={package_name} | "
        f"latest={tool['latest_version']} | released_at={tool.get('latest_version_released_at')}"
    )
    return old_values != (tool.get("latest_version"), tool.get("latest_version_released_at"))


def update_from_packagist(tool: dict) -> bool:
    changed = False
    repo_key = github_repo_key(tool.get("repository"))
    if not tool.get("packagist"):
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
                    print(f"  Packagist: {tool['slug']} | {tool['packagist']}")
                    changed = True
                    break
            if changed:
                break
            if search.get("results") and "/" in str(query):
                result = search["results"][0]
                if result.get("url"):
                    tool["packagist"] = result["url"]
                    print(f"  Packagist: {tool['slug']} | {tool['packagist']}")
                    changed = True
                    break
    return update_packagist_version(tool) or changed


def public_url(tool: dict) -> str | None:
    url = tool.get("public_url") or tool.get("website")
    if url:
        tool["public_url"] = url
    return url


def check_website(tool: dict) -> bool:
    url = public_url(tool)
    if not url:
        print(f"  Website: {tool['slug']} has no public URL")
        return False

    headers = {"User-Agent": "custom-php-analysis-tools-updater"}
    status_code = 0
    error = ""
    status = "unavailable"
    for method in ("HEAD", "GET"):
        request = urllib.request.Request(url, method=method, headers=headers)
        try:
            with urllib.request.urlopen(request, timeout=20) as response:
                status_code = int(response.status)
                status = "available" if 200 <= status_code < 400 else "unavailable"
                error = ""
                break
        except urllib.error.HTTPError as exc:
            status_code = int(exc.code)
            status = "available" if 200 <= status_code < 400 else "unavailable"
            error = f"HTTP {exc.code}"
            if method == "HEAD" and exc.code in {403, 405, 429}:
                continue
            break
        except (urllib.error.URLError, TimeoutError) as exc:
            error = str(exc.reason if isinstance(exc, urllib.error.URLError) else exc)
            if method == "HEAD":
                continue
            break

    old_values = (
        tool.get("website_status"),
        tool.get("website_status_code"),
        tool.get("website_error"),
    )
    tool["website_status"] = status
    tool["website_status_code"] = status_code
    tool["website_checked_at"] = now_iso()
    tool["website_error"] = error
    print(f"  Website: {tool['slug']} | {status} | status_code={status_code} | url={url} | error={error}")
    return old_values != (status, status_code, error)


def parse_iso(value: str | None) -> datetime | None:
    if not value:
        return None
    return datetime.fromisoformat(value.replace("Z", "+00:00"))


def is_stale(tool: dict, max_age_hours: int) -> bool:
    updated = parse_iso(tool.get("metadata_updated_at"))
    if not updated:
        return True
    return datetime.now(timezone.utc) - updated > timedelta(hours=max_age_hours)


def website_is_stale(tool: dict, max_age_hours: int) -> bool:
    checked = parse_iso(tool.get("website_checked_at"))
    if not checked:
        return True
    return datetime.now(timezone.utc) - checked > timedelta(hours=max_age_hours)


def main() -> None:
    parser = argparse.ArgumentParser(description="Refresh public metadata in common/catalog/*.yaml")
    parser.add_argument("--limit", type=positive_int, default=0, help="Maximum number of tools to update. 0 means all.")
    parser.add_argument("--skip-packagist", action="store_true")
    parser.add_argument("--max-age-hours", type=positive_int, default=20, help="Skip entries refreshed more recently than this.")
    parser.add_argument("--website-max-age-hours", type=positive_int, default=20, help="Skip website checks newer than this.")
    parser.add_argument("--skip-website", action="store_true")
    parser.add_argument("--force", action="store_true", help="Refresh even if metadata_updated_at is recent.")
    args = parser.parse_args()

    tools = load_catalog()
    token = cli_token()
    updated = 0
    skipped_recent = 0
    skipped_no_work = 0
    checked = 0
    website_checked = 0
    for tool in tools:
        if args.limit and updated >= args.limit:
            break
        checked += 1
        needs_packagist = not args.skip_packagist and (
            bool(tool.get("packagist")) or (not tool.get("packagist") and bool(tool.get("repository")))
        )
        needs_website = not args.skip_website and public_url(tool) and (args.force or website_is_stale(tool, args.website_max_age_hours))
        needs_metadata = args.force or is_stale(tool, args.max_age_hours)
        if not needs_metadata and not needs_packagist and not needs_website:
            skipped_recent += 1
            print(
                f"Recent: {tool['slug']} | metadata_updated_at={tool.get('metadata_updated_at')} | "
                f"website_checked_at={tool.get('website_checked_at')}"
            )
            continue
        print(
            f"Checking: {tool['slug']} | github={'yes' if needs_metadata else 'no'} | "
            f"packagist={'yes' if needs_packagist else 'no'} | website={'yes' if needs_website else 'no'}"
        )
        changed = update_from_github(tool, token) if needs_metadata else False
        if not args.skip_packagist:
            changed = update_from_packagist(tool) or changed
        if needs_website:
            changed = check_website(tool) or changed
            website_checked += 1
        if changed:
            tool["metadata_updated_at"] = now_iso()
            save_tool(tool)
            updated += 1
            print(f"Updated {tool['slug']}")
        else:
            skipped_no_work += 1
            print(f"No change: {tool['slug']}")
    print(
        "Refresh summary: "
        f"checked={checked}, refreshed={updated}, recent_skips={skipped_recent}, no_change={skipped_no_work}, "
        f"website_checked={website_checked}, catalog_total={len(tools)}"
    )


if __name__ == "__main__":
    main()
