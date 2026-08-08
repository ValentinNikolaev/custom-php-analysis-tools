from __future__ import annotations

import argparse
import copy
import functools
import urllib.error
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from dataclasses import dataclass
from datetime import datetime, timedelta, timezone

from catalog_lib import (
    cli_token,
    github_api_latest_release_url,
    github_api_repo_url,
    github_repo_key,
    http_json,
    load_catalog,
    now_iso,
    packagist_package_metadata_url,
    packagist_package_url,
    packagist_search_url,
    positive_int,
    save_tool,
)


RELEASE_FIELDS = (
    "latest_release_name",
    "latest_release_tag",
    "latest_release_url",
    "latest_release_published_at",
)
DEFAULT_GITHUB_MAX_AGE_HOURS = 24
CHECK_TIMESTAMP_FIELDS = {
    "metadata_updated_at",
    "latest_release_checked_at",
    "packagist_checked_at",
    "website_checked_at",
}


@dataclass(frozen=True)
class SourceResult:
    changed: bool
    checked: bool


@dataclass(frozen=True)
class PackageVersionResult:
    changed: bool
    checked: bool
    package_valid: bool


@dataclass(frozen=True)
class RefreshPlan:
    github: bool
    packagist: bool
    website: bool
    github_release: bool = False

    @property
    def has_work(self) -> bool:
        return self.github or self.github_release or self.packagist or self.website


@dataclass(frozen=True)
class ToolRefreshResult:
    tool: dict
    content_changed: bool
    github_checked: bool
    packagist_checked: bool
    website_checked: bool
    save_needed: bool
    github_release_checked: bool = False


def update_github_release(tool: dict, repo_key: str, token: str | None) -> SourceResult:
    old_values = tuple(tool.get(field) for field in RELEASE_FIELDS)
    try:
        release = http_json(github_api_latest_release_url(repo_key), token=token)
    except urllib.error.HTTPError as exc:
        if exc.code != 404:
            print(f"  GitHub release skipped {tool['slug']}: {exc}")
            return SourceResult(changed=False, checked=False)
        for field in RELEASE_FIELDS:
            tool.pop(field, None)
        return SourceResult(changed=old_values != (None,) * len(RELEASE_FIELDS), checked=True)
    except (urllib.error.URLError, TimeoutError) as exc:
        print(f"  GitHub release skipped {tool['slug']}: {exc}")
        return SourceResult(changed=False, checked=False)

    name = str(release.get("name") or release.get("tag_name") or "").strip()
    url = release.get("html_url")
    if not name or not url:
        print(f"  GitHub release skipped {tool['slug']}: release has no name/tag or public URL")
        return SourceResult(changed=False, checked=False)

    tool["latest_release_name"] = name
    tool["latest_release_tag"] = str(release.get("tag_name") or "").strip()
    tool["latest_release_url"] = url
    tool["latest_release_published_at"] = release.get("published_at") or release.get("created_at")
    print(
        f"  GitHub release: {tool['slug']} | name={name} | "
        f"tag={tool['latest_release_tag']} | published_at={tool.get('latest_release_published_at')}"
    )
    return SourceResult(
        changed=old_values != tuple(tool.get(field) for field in RELEASE_FIELDS),
        checked=True,
    )


def update_from_github(tool: dict, token: str | None) -> SourceResult:
    repo_key = github_repo_key(tool.get("repository") or tool.get("website"))
    if not repo_key:
        print(f"  GitHub: {tool['slug']} has no public GitHub repository URL")
        return SourceResult(changed=False, checked=False)
    original = copy.deepcopy(tool)
    try:
        repo = http_json(github_api_repo_url(repo_key), token=token)
    except (urllib.error.HTTPError, urllib.error.URLError, TimeoutError) as exc:
        print(f"GitHub skipped {tool['slug']}: {exc}")
        return SourceResult(changed=False, checked=False)
    tool["repository"] = repo.get("html_url") or tool.get("repository")
    tool["stars"] = int(repo.get("stargazers_count") or 0)
    tool["repo_updated_at"] = repo.get("pushed_at") or repo.get("updated_at")
    license_data = repo.get("license") or {}
    license_id = str(license_data.get("spdx_id") or "").strip()
    if license_id and license_id not in {"NOASSERTION", "OTHER"} and not tool.get("license"):
        tool["license"] = license_id
    if repo.get("description"):
        upstream_description = repo["description"].strip()
        tool["upstream_description"] = upstream_description
        if not tool.get("description"):
            tool["description"] = upstream_description
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
    return SourceResult(changed=tool != original, checked=True)


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


def clear_packagist_metadata(tool: dict) -> bool:
    old_values = (tool.get("packagist"), tool.get("latest_version"), tool.get("latest_version_released_at"))
    tool["packagist"] = None
    tool["latest_version"] = ""
    tool["latest_version_released_at"] = None
    return old_values != (None, "", None)


@functools.lru_cache(maxsize=512)
def canonical_github_repo_key(repo_key: str, token: str | None) -> str:
    try:
        repo = http_json(github_api_repo_url(repo_key), token=token, retries=0)
        return str(repo.get("full_name") or repo_key).casefold()
    except (urllib.error.HTTPError, urllib.error.URLError, TimeoutError):
        pass
    request = urllib.request.Request(
        f"https://github.com/{repo_key}",
        method="HEAD",
        headers={"User-Agent": "custom-php-analysis-tools-updater"},
    )
    try:
        with urllib.request.urlopen(request, timeout=15) as response:
            redirected_key = github_repo_key(response.geturl())
            return (redirected_key or repo_key).casefold()
    except (urllib.error.HTTPError, urllib.error.URLError, TimeoutError):
        return repo_key.casefold()


def github_repositories_match(expected_key: str | None, candidate_key: str | None, token: str | None) -> bool:
    if not expected_key or not candidate_key:
        return False
    if expected_key.casefold() == candidate_key.casefold():
        return True
    return canonical_github_repo_key(expected_key, token) == canonical_github_repo_key(candidate_key, token)


def package_repository_key(versions: list[dict]) -> str | None:
    for version in versions:
        source = version.get("source") or {}
        if isinstance(source, dict):
            repo_key = github_repo_key(source.get("url"))
            if repo_key:
                return repo_key
    return None


def packagist_repository_matches(
    package_name: str,
    expected_repo_key: str,
    versions: list[dict],
    token: str | None,
) -> bool | None:
    source_repo_key = package_repository_key(versions)
    if source_repo_key and github_repositories_match(expected_repo_key, source_repo_key, token):
        return True
    try:
        metadata = http_json(packagist_package_metadata_url(package_name), retries=0)
    except (urllib.error.HTTPError, urllib.error.URLError, TimeoutError) as exc:
        print(f"  Packagist validation skipped: {package_name} | {exc}")
        return None
    package_repo_key = github_repo_key((metadata.get("package") or {}).get("repository"))
    return github_repositories_match(expected_repo_key, package_repo_key, token)


def update_packagist_version(tool: dict, token: str | None = None) -> PackageVersionResult:
    package_name = packagist_package_name(tool.get("packagist"))
    if not package_name:
        return PackageVersionResult(changed=False, checked=False, package_valid=False)
    try:
        data = http_json(packagist_package_url(package_name))
    except (urllib.error.HTTPError, urllib.error.URLError, TimeoutError) as exc:
        print(f"  Packagist version skipped {tool['slug']}: {exc}")
        return PackageVersionResult(changed=False, checked=False, package_valid=True)
    versions = data.get("packages", {}).get(package_name, [])
    expected_repo_key = github_repo_key(tool.get("repository"))
    if expected_repo_key:
        repository_matches = packagist_repository_matches(package_name, expected_repo_key, versions, token)
        if repository_matches is None:
            return PackageVersionResult(changed=False, checked=False, package_valid=True)
        if not repository_matches:
            package_repo_key = package_repository_key(versions)
            print(
                f"  Packagist rejected: {tool['slug']} | package={package_name} | "
                f"repository={package_repo_key or 'unknown'} does not match {expected_repo_key}"
            )
            return PackageVersionResult(
                changed=clear_packagist_metadata(tool),
                checked=True,
                package_valid=False,
            )
    if not versions:
        return PackageVersionResult(changed=False, checked=True, package_valid=True)
    latest = next(
        (
            item
            for item in versions
            if is_stable_version(item.get("version_normalized") or item.get("version") or "")
        ),
        versions[0],
    )
    old_values = (
        tool.get("latest_version"),
        tool.get("latest_version_released_at"),
        tool.get("supported_php"),
        tool.get("installation"),
    )
    tool["latest_version"] = latest.get("version") or ""
    tool["latest_version_released_at"] = latest.get("time")
    requirements = latest.get("require") or {}
    if isinstance(requirements, dict) and requirements.get("php") and not tool.get("supported_php"):
        tool["supported_php"] = str(requirements["php"])
    if not tool.get("installation"):
        dev_flag = "" if tool.get("artifact_type") == "library" else " --dev"
        tool["installation"] = f"composer require{dev_flag} {package_name}"
    print(
        f"  Packagist version: {tool['slug']} | package={package_name} | "
        f"latest={tool['latest_version']} | released_at={tool.get('latest_version_released_at')}"
    )
    return PackageVersionResult(
        changed=old_values
        != (
            tool.get("latest_version"),
            tool.get("latest_version_released_at"),
            tool.get("supported_php"),
            tool.get("installation"),
        ),
        checked=True,
        package_valid=True,
    )


def update_from_packagist(tool: dict, token: str | None = None) -> SourceResult:
    original = copy.deepcopy(tool)
    repo_key = github_repo_key(tool.get("repository"))
    if tool.get("packagist"):
        version_result = update_packagist_version(tool, token)
        if not version_result.checked:
            return SourceResult(changed=tool != original, checked=False)
        if version_result.package_valid:
            return SourceResult(changed=tool != original, checked=True)
    if not tool.get("packagist"):
        queries = [repo_key, tool.get("name")]
        found = False
        attempted = False
        all_searches_succeeded = True
        for query in [q for q in queries if q]:
            attempted = True
            try:
                search = http_json(packagist_search_url(query))
            except (urllib.error.HTTPError, urllib.error.URLError, TimeoutError):
                all_searches_succeeded = False
                continue
            for result in search.get("results", []):
                result_repo_key = github_repo_key(result.get("repository"))
                if github_repositories_match(repo_key, result_repo_key, token):
                    tool["packagist"] = result.get("url")
                    print(f"  Packagist: {tool['slug']} | {tool['packagist']}")
                    changed = True
                    found = True
                    break
            if found:
                break
    if not tool.get("packagist"):
        return SourceResult(changed=tool != original, checked=attempted and all_searches_succeeded)
    version_result = update_packagist_version(tool, token)
    return SourceResult(changed=tool != original, checked=version_result.checked)


def public_url(tool: dict) -> str | None:
    url = tool.get("public_url") or tool.get("website")
    if url:
        tool["public_url"] = url
    return url


def check_website(tool: dict, checked_at: str | None = None) -> SourceResult:
    url = public_url(tool)
    if not url:
        print(f"  Website: {tool['slug']} has no public URL")
        return SourceResult(changed=False, checked=False)

    headers = {"User-Agent": "custom-php-analysis-tools-updater"}
    status_code = 0
    error = ""
    status = "temporarily_unreachable"
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
            if 200 <= status_code < 400:
                status = "available"
            elif status_code in {401, 403, 429}:
                status = "bot_blocked"
            elif status_code in {404, 410}:
                status = "unavailable"
            elif status_code >= 500:
                status = "temporarily_unreachable"
            else:
                status = "unavailable"
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
    tool["website_checked_at"] = checked_at or now_iso()
    tool["website_error"] = error
    print(f"  Website: {tool['slug']} | {status} | status_code={status_code} | url={url} | error={error}")
    return SourceResult(changed=old_values != (status, status_code, error), checked=True)


def parse_iso(value: str | None) -> datetime | None:
    if not value:
        return None
    return datetime.fromisoformat(value.replace("Z", "+00:00"))


def timestamp_is_stale(value: str | None, max_age_hours: int, reference_time: datetime | None = None) -> bool:
    checked = parse_iso(value)
    if not checked:
        return True
    current = reference_time or datetime.now(timezone.utc)
    return current - checked >= timedelta(hours=max_age_hours)


def is_stale(tool: dict, max_age_hours: int, reference_time: datetime | None = None) -> bool:
    return timestamp_is_stale(tool.get("metadata_updated_at"), max_age_hours, reference_time)


def github_release_is_stale(
    tool: dict,
    max_age_hours: int,
    reference_time: datetime | None = None,
) -> bool:
    checked_at = (
        tool.get("latest_release_checked_at")
        if "latest_release_checked_at" in tool
        else tool.get("metadata_updated_at")
    )
    return timestamp_is_stale(checked_at, max_age_hours, reference_time)


def packagist_is_stale(tool: dict, max_age_hours: int, reference_time: datetime | None = None) -> bool:
    return timestamp_is_stale(tool.get("packagist_checked_at"), max_age_hours, reference_time)


def website_is_stale(tool: dict, max_age_hours: int, reference_time: datetime | None = None) -> bool:
    return timestamp_is_stale(tool.get("website_checked_at"), max_age_hours, reference_time)


def worker_count(value: str) -> int:
    count = positive_int(value)
    if count < 1:
        raise argparse.ArgumentTypeError("must be at least 1")
    return count


def select_tools(tools: list[dict], requested_slugs: list[str]) -> list[dict]:
    if not requested_slugs:
        return tools
    requested = {slug.strip() for value in requested_slugs for slug in value.split(",") if slug.strip()}
    available = {str(tool.get("slug")) for tool in tools}
    missing = sorted(requested - available)
    if missing:
        raise ValueError("unknown catalog slug(s): " + ", ".join(missing))
    return [tool for tool in tools if tool.get("slug") in requested]


def refresh_plan(tool: dict, args: argparse.Namespace, reference_time: datetime | None = None) -> RefreshPlan:
    has_github_repository = bool(github_repo_key(tool.get("repository") or tool.get("website")))
    has_packagist_source = bool(tool.get("packagist") or tool.get("repository"))
    has_website = bool(tool.get("public_url") or tool.get("website"))
    return RefreshPlan(
        github=has_github_repository and (args.force or is_stale(tool, args.max_age_hours, reference_time)),
        packagist=(
            not args.skip_packagist
            and has_packagist_source
            and (args.force or packagist_is_stale(tool, args.packagist_max_age_hours, reference_time))
        ),
        website=(
            not args.skip_website
            and has_website
            and (args.force or website_is_stale(tool, args.website_max_age_hours, reference_time))
        ),
        github_release=(
            has_github_repository
            and (args.force or github_release_is_stale(tool, args.max_age_hours, reference_time))
        ),
    )


def refresh_tool(
    tool: dict,
    plan: RefreshPlan,
    token: str | None,
    checked_at: str,
) -> ToolRefreshResult:
    original = copy.deepcopy(tool)
    refreshed = copy.deepcopy(tool)
    github_checked = False
    github_release_checked = False
    packagist_checked = False
    website_checked = False

    print(
        f"Checking: {refreshed['slug']} | github={'yes' if plan.github else 'no'} | "
        f"release={'yes' if plan.github_release else 'no'} | "
        f"packagist={'yes' if plan.packagist else 'no'} | website={'yes' if plan.website else 'no'}"
    )
    if plan.github:
        github_result = update_from_github(refreshed, token)
        github_checked = github_result.checked
        if github_checked:
            refreshed["metadata_updated_at"] = checked_at
    if plan.github_release and not (plan.github and not github_checked):
        repo_key = github_repo_key(refreshed.get("repository") or refreshed.get("website"))
        if repo_key:
            release_result = update_github_release(refreshed, repo_key, token)
            github_release_checked = release_result.checked
            if github_release_checked:
                refreshed["latest_release_checked_at"] = checked_at
            elif "latest_release_checked_at" not in refreshed:
                refreshed["latest_release_checked_at"] = None
    if plan.packagist:
        packagist_result = update_from_packagist(refreshed, token)
        packagist_checked = packagist_result.checked
        if packagist_checked:
            refreshed["packagist_checked_at"] = checked_at
    if plan.website:
        website_result = check_website(refreshed, checked_at=checked_at)
        website_checked = website_result.checked

    original_content = {key: value for key, value in original.items() if key not in CHECK_TIMESTAMP_FIELDS}
    refreshed_content = {key: value for key, value in refreshed.items() if key not in CHECK_TIMESTAMP_FIELDS}

    return ToolRefreshResult(
        tool=refreshed,
        content_changed=refreshed_content != original_content,
        github_checked=github_checked,
        packagist_checked=packagist_checked,
        website_checked=website_checked,
        save_needed=refreshed != original,
        github_release_checked=github_release_checked,
    )


def refresh_tools(
    work_items: list[tuple[dict, RefreshPlan]],
    token: str | None,
    checked_at: str,
    workers: int,
) -> list[ToolRefreshResult]:
    if not work_items:
        return []

    def run_refresh(item: tuple[dict, RefreshPlan]) -> ToolRefreshResult:
        return refresh_tool(item[0], item[1], token, checked_at)

    with ThreadPoolExecutor(max_workers=min(workers, len(work_items))) as executor:
        return list(executor.map(run_refresh, work_items))


def main() -> None:
    parser = argparse.ArgumentParser(description="Refresh public metadata in common/catalog/*.yaml")
    parser.add_argument("--limit", type=positive_int, default=0, help="Maximum number of tools to check. 0 means all.")
    parser.add_argument(
        "--slug",
        action="append",
        default=[],
        help="Refresh only the named slug; repeat the option or pass a comma-separated list.",
    )
    parser.add_argument("--workers", type=worker_count, default=8, help="Maximum concurrent tool checks.")
    parser.add_argument("--skip-packagist", action="store_true")
    parser.add_argument(
        "--max-age-hours",
        type=positive_int,
        default=DEFAULT_GITHUB_MAX_AGE_HOURS,
        help="Skip GitHub repository and release checks newer than this.",
    )
    parser.add_argument(
        "--packagist-max-age-hours",
        type=positive_int,
        default=20,
        help="Skip Packagist checks newer than this.",
    )
    parser.add_argument("--website-max-age-hours", type=positive_int, default=20, help="Skip website checks newer than this.")
    parser.add_argument("--skip-website", action="store_true")
    parser.add_argument("--force", action="store_true", help="Refresh all available sources regardless of freshness.")
    parser.add_argument(
        "--max-failed-checks",
        type=positive_int,
        default=10,
        help="Fail when more source checks than this budget could not be completed.",
    )
    args = parser.parse_args()

    try:
        tools = select_tools(load_catalog(), args.slug)
    except ValueError as exc:
        parser.error(str(exc))
    token = cli_token()
    reference_time = datetime.now(timezone.utc)
    checked_at = reference_time.replace(microsecond=0).isoformat().replace("+00:00", "Z")
    work_items: list[tuple[dict, RefreshPlan]] = []
    skipped_recent = 0
    for tool in tools:
        plan = refresh_plan(tool, args, reference_time)
        if not plan.has_work:
            skipped_recent += 1
            print(
                f"Recent: {tool['slug']} | metadata_updated_at={tool.get('metadata_updated_at')} | "
                f"latest_release_checked_at={tool.get('latest_release_checked_at')} | "
                f"packagist_checked_at={tool.get('packagist_checked_at')} | "
                f"website_checked_at={tool.get('website_checked_at')}"
            )
            continue
        work_items.append((tool, plan))

    if args.limit:
        work_items = work_items[: args.limit]

    results = refresh_tools(work_items, token, checked_at, args.workers)

    saved = 0
    content_changed = 0
    for result in results:
        if result.save_needed:
            save_tool(result.tool)
            saved += 1
            content_changed += int(result.content_changed)
            print(f"Updated {result.tool['slug']}")
        else:
            print(f"No change: {result.tool['slug']}")

    failed_checks = sum(
        int(plan.github and not result.github_checked)
        + int(plan.github_release and not result.github_release_checked)
        + int(plan.packagist and not result.packagist_checked)
        + int(plan.website and not result.website_checked)
        for (_, plan), result in zip(work_items, results)
    )
    print(
        "Refresh summary: "
        f"checked={len(results)}, saved={saved}, content_changed={content_changed}, "
        f"recent_skips={skipped_recent}, no_change={len(results) - saved}, failed_checks={failed_checks}, "
        f"website_checked={sum(result.website_checked for result in results)}, catalog_total={len(tools)}"
    )
    if failed_checks > args.max_failed_checks:
        raise SystemExit(
            f"Refresh failed: {failed_checks} source checks exceeded the budget of {args.max_failed_checks}"
        )


if __name__ == "__main__":
    main()
