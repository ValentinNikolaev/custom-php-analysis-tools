from __future__ import annotations

import argparse
import re
import sys
from collections import defaultdict
from datetime import datetime
from pathlib import Path
from typing import Any
from urllib.parse import urlparse

from catalog_lib import (
    CATEGORY_IDS,
    CATEGORY_ORDER,
    ROOT,
    TOOL_FIELD_ORDER,
    github_repo_key,
    load_yaml,
)


CANDIDATE_DIR_NAME = "candidates"
SLUG_PATTERN = re.compile(r"[a-z0-9]+(?:-[a-z0-9]+)*")
ARTIFACT_TYPES = {
    "analyzer",
    "fixer",
    "ruleset",
    "extension",
    "library",
    "orchestrator",
    "metrics",
    "hosted-service",
    "runtime",
}
CATALOG_STATUSES = {"current", "historical", "adjacent"}
REVIEW_STATUSES = {"pending", "accepted", "rejected", "needs-info"}
WEBSITE_STATUSES = {
    "available",
    "bot_blocked",
    "temporarily_unreachable",
    "unavailable",
    "unknown",
}

CATALOG_REQUIRED_FIELDS = {
    "slug",
    "name",
    "category",
    "catalog_status",
    "description",
    "website",
    "public_url",
    "website_status",
    "website_status_code",
    "website_checked_at",
    "website_error",
    "repository",
    "packagist",
    "stars",
    "repo_updated_at",
    "metadata_updated_at",
    "quality_tags",
    "source",
    "notes",
}
CANDIDATE_REVIEW_FIELDS = {
    "review_status",
    "review_notes",
    "discovered_at",
    "last_reviewed_at",
}
CANDIDATE_OPTIONAL_FIELDS = {
    "reconsider_after",
    "discovery_queries",
    "last_discovered_at",
}
CANDIDATE_REQUIRED_FIELDS = (CATALOG_REQUIRED_FIELDS - {"catalog_status"}) | CANDIDATE_REVIEW_FIELDS
CATALOG_ALLOWED_FIELDS = set(TOOL_FIELD_ORDER)
CANDIDATE_ALLOWED_FIELDS = CATALOG_ALLOWED_FIELDS | CANDIDATE_REVIEW_FIELDS | CANDIDATE_OPTIONAL_FIELDS

STRING_FIELDS = {
    "slug",
    "name",
    "category",
    "artifact_type",
    "catalog_status",
    "product_status",
    "description",
    "upstream_description",
    "best_for",
    "delivery",
    "installation",
    "supported_php",
    "license",
    "pricing",
    "successor_of",
    "supersedes",
    "editor_reason",
    "title_icon",
    "title_icon_label",
    "website",
    "public_url",
    "website_status",
    "website_error",
    "latest_release_name",
    "latest_release_tag",
    "latest_version",
    "source",
    "notes",
    "review_status",
    "review_notes",
}
NULLABLE_STRING_FIELDS = {"repository", "packagist"}
LIST_FIELDS = {"use_cases", "ecosystems", "capabilities", "quality_tags", "discovery_queries"}
INTEGER_FIELDS = {"website_status_code", "stars"}
URL_FIELDS = {"website", "public_url", "repository", "packagist", "latest_release_url"}
DATE_FIELDS = {
    "reviewed_at",
    "website_checked_at",
    "latest_release_published_at",
    "latest_release_checked_at",
    "latest_version_released_at",
    "packagist_checked_at",
    "repo_updated_at",
    "metadata_updated_at",
    "discovered_at",
    "last_reviewed_at",
    "reconsider_after",
    "last_discovered_at",
}


def normalized_url(value: str) -> str:
    return value.strip().rstrip("/").casefold()


def is_valid_url(value: str) -> bool:
    parsed = urlparse(value)
    return parsed.scheme in {"http", "https"} and bool(parsed.netloc) and not any(char.isspace() for char in value)


def is_valid_iso_date(value: str) -> bool:
    try:
        if re.fullmatch(r"\d{4}-\d{2}-\d{2}", value):
            datetime.strptime(value, "%Y-%m-%d")
            return True
        parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
        return parsed.tzinfo is not None
    except ValueError:
        return False


def validate_scalar_types(path: Path, data: dict[str, Any], errors: list[str]) -> None:
    for field in STRING_FIELDS & data.keys():
        if not isinstance(data[field], str):
            errors.append(f"{path}: {field} must be a string")
    for field in NULLABLE_STRING_FIELDS & data.keys():
        if data[field] is not None and not isinstance(data[field], str):
            errors.append(f"{path}: {field} must be a string or null")
    for field in LIST_FIELDS & data.keys():
        value = data[field]
        if not isinstance(value, list) or any(not isinstance(item, str) or not item.strip() for item in value):
            errors.append(f"{path}: {field} must be a list of non-empty strings")
        elif len({item.casefold() for item in value}) != len(value):
            errors.append(f"{path}: {field} must not contain duplicate values")
    for field in INTEGER_FIELDS & data.keys():
        if type(data[field]) is not int:
            errors.append(f"{path}: {field} must be an integer")


def validate_entry(path: Path, data: dict[str, Any], *, candidate: bool) -> list[str]:
    errors: list[str] = []
    allowed = CANDIDATE_ALLOWED_FIELDS if candidate else CATALOG_ALLOWED_FIELDS
    required = CANDIDATE_REQUIRED_FIELDS if candidate else CATALOG_REQUIRED_FIELDS

    unknown = sorted(set(data) - allowed)
    if "editor_choice" in unknown:
        errors.append(
            f"{path}: editor_choice is a legacy second source; remove it and edit common/editor-choice.yaml instead"
        )
        unknown.remove("editor_choice")
    if unknown:
        errors.append(f"{path}: unknown fields: {', '.join(unknown)}")

    missing = sorted(required - set(data))
    if missing:
        errors.append(f"{path}: missing required fields: {', '.join(missing)}")

    if not candidate and data.get("catalog_status") in {"current", "adjacent"}:
        comparison_required = {"artifact_type", "use_cases", "ecosystems", "reviewed_at"}
        comparison_missing = sorted(comparison_required - set(data))
        if comparison_missing:
            errors.append(
                f"{path}: current/adjacent entries require comparison fields: "
                + ", ".join(comparison_missing)
            )
        for field in ("use_cases", "ecosystems"):
            if field in data and isinstance(data[field], list) and not data[field]:
                errors.append(f"{path}: current/adjacent entries require at least one {field} value")

    validate_scalar_types(path, data, errors)

    for field in {"slug", "name", "category", "description", "website", "public_url", "source"} & data.keys():
        if isinstance(data[field], str) and not data[field].strip():
            errors.append(f"{path}: {field} must not be empty")

    slug = data.get("slug")
    if isinstance(slug, str):
        if not SLUG_PATTERN.fullmatch(slug):
            errors.append(f"{path}: slug must use lower-case kebab-case")
        if path.stem != slug:
            errors.append(f"{path}: slug {slug!r} must match filename {path.stem!r}")

    category = data.get("category")
    if isinstance(category, str) and category not in CATEGORY_ORDER:
        errors.append(f"{path}: category must be one of {', '.join(CATEGORY_ORDER)}")
    artifact_type = data.get("artifact_type")
    if isinstance(artifact_type, str) and artifact_type not in ARTIFACT_TYPES:
        errors.append(f"{path}: artifact_type must be one of {', '.join(sorted(ARTIFACT_TYPES))}")
    catalog_status = data.get("catalog_status")
    if isinstance(catalog_status, str) and catalog_status not in CATALOG_STATUSES:
        errors.append(f"{path}: catalog_status must be one of {', '.join(sorted(CATALOG_STATUSES))}")
    review_status = data.get("review_status")
    if isinstance(review_status, str) and review_status not in REVIEW_STATUSES:
        errors.append(f"{path}: review_status must be one of {', '.join(sorted(REVIEW_STATUSES))}")
    if candidate and isinstance(data.get("review_notes"), str) and not data["review_notes"].strip():
        errors.append(f"{path}: review_notes must explain the current review state")
    website_status = data.get("website_status")
    if isinstance(website_status, str) and website_status not in WEBSITE_STATUSES:
        errors.append(f"{path}: website_status must be one of {', '.join(sorted(WEBSITE_STATUSES))}")

    status_code = data.get("website_status_code")
    if type(status_code) is int and not 0 <= status_code <= 599:
        errors.append(f"{path}: website_status_code must be between 0 and 599")
    stars = data.get("stars")
    if type(stars) is int and stars < 0:
        errors.append(f"{path}: stars must be non-negative")

    for field in URL_FIELDS & data.keys():
        value = data[field]
        if value is not None and (not isinstance(value, str) or not is_valid_url(value)):
            errors.append(f"{path}: {field} must be an absolute http(s) URL or null")
    for field in DATE_FIELDS & data.keys():
        value = data[field]
        if value is not None and (not isinstance(value, str) or not is_valid_iso_date(value)):
            errors.append(f"{path}: {field} must be an ISO 8601 date/timestamp with timezone or null")

    return errors


def duplicate_errors(entries: list[tuple[Path, dict[str, Any]]], namespace: str) -> list[str]:
    errors: list[str] = []
    for field in ("slug", "repository", "packagist"):
        seen: dict[str, Path] = {}
        for path, data in entries:
            value = data.get(field)
            if not value:
                continue
            if field == "repository":
                key = (github_repo_key(value) or normalized_url(value)).casefold()
            else:
                key = normalized_url(value) if field == "packagist" else str(value).casefold()
            if key in seen:
                errors.append(f"{path}: duplicate {namespace} {field} also used by {seen[key]}")
            else:
                seen[key] = path
    return errors


def load_entries(directory: Path, *, candidate: bool) -> tuple[list[tuple[Path, dict[str, Any]]], list[str]]:
    entries: list[tuple[Path, dict[str, Any]]] = []
    errors: list[str] = []
    for path in sorted(directory.glob("*.yaml")):
        try:
            data = load_yaml(path)
        except (ValueError, OSError) as exc:
            errors.append(f"{path}: cannot parse YAML: {exc}")
            continue
        entries.append((path, data))
        errors.extend(validate_entry(path, data, candidate=candidate))
    return entries, errors


def validate_overlap(
    catalog: list[tuple[Path, dict[str, Any]]], candidates: list[tuple[Path, dict[str, Any]]]
) -> list[str]:
    errors: list[str] = []
    catalog_values: dict[str, dict[str, Path]] = defaultdict(dict)
    for path, data in catalog:
        for field in ("slug", "repository", "packagist"):
            value = data.get(field)
            if not value:
                continue
            if field == "repository":
                key = (github_repo_key(value) or normalized_url(value)).casefold()
            elif field == "packagist":
                key = normalized_url(value)
            else:
                key = str(value).casefold()
            catalog_values[field][key] = path

    for path, data in candidates:
        for field in ("slug", "repository", "packagist"):
            value = data.get(field)
            if not value:
                continue
            if field == "repository":
                key = (github_repo_key(value) or normalized_url(value)).casefold()
            elif field == "packagist":
                key = normalized_url(value)
            else:
                key = str(value).casefold()
            if key in catalog_values[field]:
                errors.append(f"{path}: {field} overlaps catalog entry {catalog_values[field][key]}")
    return errors


def validate_rejected_candidates(
    root: Path, candidates: list[tuple[Path, dict[str, Any]]]
) -> list[str]:
    path = root / "common" / "rejected-candidates.yaml"
    if not path.exists():
        return []
    try:
        data = load_yaml(path)
    except (ValueError, OSError) as exc:
        return [f"{path}: cannot parse YAML: {exc}"]

    errors: list[str] = []
    if set(data) != {"reviewed_at", "rejections"}:
        errors.append(f"{path}: only reviewed_at and rejections are allowed")
    reviewed_at = data.get("reviewed_at")
    if not isinstance(reviewed_at, str) or not is_valid_iso_date(reviewed_at):
        errors.append(f"{path}: reviewed_at must be an ISO 8601 date/timestamp")
    rejections = data.get("rejections")
    if not isinstance(rejections, list):
        return errors + [f"{path}: rejections must be a list of mappings"]

    required = {"slug", "name", "repository", "reason", "rejected_at", "reconsider_after"}
    seen_slugs: dict[str, int] = {}
    seen_repositories: dict[str, int] = {}
    candidate_slugs = {str(item.get("slug")).casefold() for _, item in candidates if item.get("slug")}
    candidate_repositories = {
        (github_repo_key(item.get("repository")) or normalized_url(str(item.get("repository")))).casefold()
        for _, item in candidates
        if item.get("repository")
    }
    for index, rejection in enumerate(rejections, start=1):
        location = f"{path}: rejections[{index}]"
        if not isinstance(rejection, dict):
            errors.append(f"{location} must be a mapping")
            continue
        missing = sorted(required - set(rejection))
        unknown = sorted(set(rejection) - required)
        if missing:
            errors.append(f"{location} missing required fields: {', '.join(missing)}")
        if unknown:
            errors.append(f"{location} has unknown fields: {', '.join(unknown)}")
        for field in ("slug", "name", "repository", "reason", "rejected_at"):
            value = rejection.get(field)
            if not isinstance(value, str) or not value.strip():
                errors.append(f"{location}.{field} must be a non-empty string")
        slug = rejection.get("slug")
        if isinstance(slug, str):
            if not SLUG_PATTERN.fullmatch(slug):
                errors.append(f"{location}.slug must use lower-case kebab-case")
            slug_key = slug.casefold()
            if slug_key in seen_slugs:
                errors.append(f"{location}.slug duplicates rejections[{seen_slugs[slug_key]}]")
            else:
                seen_slugs[slug_key] = index
            if slug_key in candidate_slugs:
                errors.append(f"{location}.slug is still present in the active candidate queue")
        repository = rejection.get("repository")
        if isinstance(repository, str) and repository:
            if not is_valid_url(repository):
                errors.append(f"{location}.repository must be an absolute http(s) URL")
            repo_key = (github_repo_key(repository) or normalized_url(repository)).casefold()
            if repo_key in seen_repositories:
                errors.append(
                    f"{location}.repository duplicates rejections[{seen_repositories[repo_key]}]"
                )
            else:
                seen_repositories[repo_key] = index
            if repo_key in candidate_repositories:
                errors.append(f"{location}.repository is still present in the active candidate queue")
        for field in ("rejected_at", "reconsider_after"):
            value = rejection.get(field)
            if value is not None and (not isinstance(value, str) or not is_valid_iso_date(value)):
                errors.append(f"{location}.{field} must be an ISO 8601 date/timestamp or null")
    return errors


def validate_editor_choice(root: Path, catalog_by_slug: dict[str, dict[str, Any]]) -> list[str]:
    errors: list[str] = []
    choice_path = root / "common" / "editor-choice.yaml"
    copy_path = root / "common" / "editor-choice-copy.yaml"
    if not choice_path.exists():
        return [f"{choice_path}: missing canonical editor-choice file"]
    try:
        choice = load_yaml(choice_path)
    except (ValueError, OSError) as exc:
        return [f"{choice_path}: cannot parse YAML: {exc}"]
    if set(choice) != {"slugs"}:
        errors.append(f"{choice_path}: only the slugs field is allowed")
    slugs = choice.get("slugs")
    if not isinstance(slugs, list) or any(not isinstance(slug, str) for slug in slugs):
        return errors + [f"{choice_path}: slugs must be a list of strings"]
    if len(set(slugs)) != len(slugs):
        errors.append(f"{choice_path}: slugs must be unique")
    for slug in slugs:
        tool = catalog_by_slug.get(slug)
        if not tool:
            errors.append(f"{choice_path}: unknown catalog slug {slug!r}")
        elif (
            tool.get("catalog_status") in {"historical", "adjacent"}
            or tool.get("product_status") in {"retired", "discontinued"}
            or "archived" in set(tool.get("quality_tags") or [])
        ):
            errors.append(f"{choice_path}: {slug!r} is not a current catalog entry")

    if not copy_path.exists():
        return errors + [f"{copy_path}: missing editorial copy file"]
    try:
        copy = load_yaml(copy_path)
    except (ValueError, OSError) as exc:
        return errors + [f"{copy_path}: cannot parse YAML: {exc}"]
    recommended = copy.get("recommended_for")
    reasons = copy.get("why_it_stands_out")
    if set(copy) != {"recommended_for", "why_it_stands_out"}:
        errors.append(f"{copy_path}: only recommended_for and why_it_stands_out are allowed")
    if not isinstance(recommended, dict) or not isinstance(reasons, dict):
        return errors + [f"{copy_path}: recommended_for and why_it_stands_out must be mappings"]
    if set(recommended) != set(reasons):
        errors.append(f"{copy_path}: recommended_for and why_it_stands_out must cover the same slugs")
    for slug in set(recommended) | set(reasons):
        if slug not in catalog_by_slug:
            errors.append(f"{copy_path}: editorial copy references unknown catalog slug {slug!r}")
    for slug in slugs:
        if not str(recommended.get(slug) or "").strip():
            errors.append(f"{copy_path}: missing recommended_for copy for {slug!r}")
        if not str(reasons.get(slug) or "").strip():
            errors.append(f"{copy_path}: missing why_it_stands_out copy for {slug!r}")
    return errors


def validate_references(catalog: list[tuple[Path, dict[str, Any]]]) -> list[str]:
    slugs = {str(data.get("slug")) for _, data in catalog if data.get("slug")}
    errors: list[str] = []
    for path, data in catalog:
        for field in ("successor_of", "supersedes"):
            reference = data.get(field)
            if reference and reference not in slugs:
                errors.append(f"{path}: {field} references unknown catalog slug {reference!r}")
            elif reference and reference == data.get("slug"):
                errors.append(f"{path}: {field} must not reference the entry itself")
    return errors


def validate_repository(root: Path = ROOT) -> list[str]:
    catalog, errors = load_entries(root / "common" / "catalog", candidate=False)
    candidates, candidate_errors = load_entries(root / "common" / CANDIDATE_DIR_NAME, candidate=True)
    errors.extend(candidate_errors)
    if not catalog:
        errors.append(f"{root / 'common' / 'catalog'}: catalog must contain at least one YAML entry")
    errors.extend(duplicate_errors(catalog, "catalog"))
    errors.extend(duplicate_errors(candidates, "candidate"))
    errors.extend(validate_overlap(catalog, candidates))
    errors.extend(validate_rejected_candidates(root, candidates))
    errors.extend(validate_references(catalog))
    catalog_by_slug = {str(data.get("slug")): data for _, data in catalog if data.get("slug")}
    errors.extend(validate_editor_choice(root, catalog_by_slug))
    if set(CATEGORY_IDS) != set(CATEGORY_ORDER) or len(set(CATEGORY_IDS.values())) != len(CATEGORY_IDS):
        errors.append("catalog_lib.CATEGORY_IDS must define one unique stable ID for every category")
    return errors


def main() -> None:
    parser = argparse.ArgumentParser(description="Validate catalog, candidate, and editorial YAML sources.")
    parser.add_argument("--root", type=Path, default=ROOT, help="Repository root (primarily useful for tests).")
    args = parser.parse_args()
    errors = validate_repository(args.root.resolve())
    if errors:
        print(f"Catalog validation failed with {len(errors)} error(s):", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        raise SystemExit(1)
    catalog_count = len(list((args.root / "common" / "catalog").glob("*.yaml")))
    candidate_count = len(list((args.root / "common" / "candidates").glob("*.yaml")))
    print(f"Catalog validation passed: {catalog_count} catalog entries, {candidate_count} review candidates")


if __name__ == "__main__":
    main()
