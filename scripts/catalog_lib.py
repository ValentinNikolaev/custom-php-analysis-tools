from __future__ import annotations

import argparse
import json
import os
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
CATALOG_DIR = ROOT / "common" / "catalog"
EDITOR_CHOICE_FILE = ROOT / "common" / "editor-choice.yaml"
EDITOR_CHOICE_COPY_FILE = ROOT / "common" / "editor-choice-copy.yaml"
CATEGORY_ORDER = [
    "Bugs finders",
    "Coding standards",
    "Architecture rules",
    "DIY",
    "Fixers",
    "Metrics",
    "SaaS",
    "Misc",
]


def now_iso() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def slugify(value: str) -> str:
    value = value.lower()
    value = re.sub(r"[^a-z0-9]+", "-", value)
    return value.strip("-") or "tool"


def yaml_quote(value: str) -> str:
    return json.dumps(value, ensure_ascii=False)


def dump_yaml(data: dict[str, Any]) -> str:
    lines: list[str] = []
    for key, value in data.items():
        if isinstance(value, str):
            lines.append(f"{key}: {yaml_quote(value)}")
        elif isinstance(value, bool):
            lines.append(f"{key}: {'true' if value else 'false'}")
        elif isinstance(value, int):
            lines.append(f"{key}: {value}")
        elif value is None:
            lines.append(f"{key}: null")
        elif isinstance(value, list):
            if not value:
                lines.append(f"{key}: []")
            else:
                lines.append(f"{key}:")
                for item in value:
                    if isinstance(item, str):
                        lines.append(f"  - {yaml_quote(item)}")
                    else:
                        lines.append(f"  - {json.dumps(item, ensure_ascii=False)}")
        elif isinstance(value, dict):
            if not value:
                lines.append(f"{key}: {{}}")
            else:
                lines.append(f"{key}:")
                for sub_key, sub_value in value.items():
                    if isinstance(sub_value, str):
                        lines.append(f"  {sub_key}: {yaml_quote(sub_value)}")
                    elif isinstance(sub_value, bool):
                        lines.append(f"  {sub_key}: {'true' if sub_value else 'false'}")
                    elif isinstance(sub_value, int):
                        lines.append(f"  {sub_key}: {sub_value}")
                    elif sub_value is None:
                        lines.append(f"  {sub_key}: null")
                    else:
                        lines.append(f"  {sub_key}: {json.dumps(sub_value, ensure_ascii=False)}")
        else:
            lines.append(f"{key}: {json.dumps(value, ensure_ascii=False)}")
    return "\n".join(lines) + "\n"


def parse_scalar(value: str) -> Any:
    value = value.strip()
    if value == "null":
        return None
    if value == "true":
        return True
    if value == "false":
        return False
    if re.fullmatch(r"-?\d+", value):
        return int(value)
    if value.startswith(('"', "[", "{")):
        return json.loads(value)
    return value


def load_yaml(path: Path) -> dict[str, Any]:
    data: dict[str, Any] = {}
    current_key: str | None = None
    for raw_line in path.read_text(encoding="utf-8").splitlines():
        if not raw_line.strip() or raw_line.strip().startswith("#"):
            continue
        if raw_line.startswith("  - ") and current_key:
            data.setdefault(current_key, []).append(parse_scalar(raw_line[4:]))
            continue
        if raw_line.startswith("  ") and current_key:
            sub_key, sub_value = raw_line.strip().split(":", 1)
            container = data.setdefault(current_key, {})
            if isinstance(container, list) and not container:
                container = {}
                data[current_key] = container
            if not isinstance(container, dict):
                raise ValueError(f"Expected a mapping for {current_key!r} in {path}")
            container[sub_key] = parse_scalar(sub_value)
            continue
        key, value = raw_line.split(":", 1)
        key = key.strip()
        value = value.strip()
        if value == "":
            data[key] = []
            current_key = key
        else:
            data[key] = parse_scalar(value)
            current_key = None
    return data


def load_catalog() -> list[dict[str, Any]]:
    tools = [load_yaml(path) for path in sorted(CATALOG_DIR.glob("*.yaml"))]
    return sorted(tools, key=lambda item: (category_rank(item.get("category")), item.get("name", "").lower()))


def save_tool(tool: dict[str, Any]) -> None:
    CATALOG_DIR.mkdir(parents=True, exist_ok=True)
    path = CATALOG_DIR / f"{tool['slug']}.yaml"
    ordered: dict[str, Any] = {}
    for key in [
        "slug",
        "name",
        "category",
        "description",
        "best_for",
        "delivery",
        "editor_reason",
        "website",
        "public_url",
        "website_status",
        "website_status_code",
        "website_checked_at",
        "website_error",
        "repository",
        "latest_release_name",
        "latest_release_tag",
        "latest_release_url",
        "latest_release_published_at",
        "packagist",
        "latest_version",
        "latest_version_released_at",
        "stars",
        "repo_updated_at",
        "metadata_updated_at",
        "editor_choice",
        "quality_tags",
        "source",
        "notes",
    ]:
        if key in tool:
            ordered[key] = tool[key]
    path.write_text(dump_yaml(ordered), encoding="utf-8")


def category_rank(category: str | None) -> int:
    try:
        return CATEGORY_ORDER.index(category or "")
    except ValueError:
        return len(CATEGORY_ORDER)


def normalize_github_url(url: str | None) -> str | None:
    if not url:
        return None
    match = re.search(r"github\.com[:/]+([^/\s]+)/([^/\s#?]+)", url)
    if not match:
        return None
    owner = match.group(1)
    repo = re.sub(r"\.git$", "", match.group(2))
    return f"https://github.com/{owner}/{repo}"


def github_repo_key(url: str | None) -> str | None:
    normalized = normalize_github_url(url)
    if not normalized:
        return None
    return normalized.removeprefix("https://github.com/")


def http_json(url: str, token: str | None = None, retries: int = 2) -> Any:
    headers = {
        "Accept": "application/vnd.github+json, application/json",
        "User-Agent": "custom-php-analysis-tools-updater",
    }
    if token and "api.github.com" in url:
        headers["Authorization"] = f"Bearer {token}"
    request = urllib.request.Request(url, headers=headers)
    for attempt in range(retries + 1):
        try:
            with urllib.request.urlopen(request, timeout=30) as response:
                return json.loads(response.read().decode("utf-8"))
        except urllib.error.HTTPError as exc:
            if exc.code in {403, 429} and attempt < retries:
                time.sleep(2 + attempt * 3)
                continue
            raise
        except urllib.error.URLError:
            if attempt < retries:
                time.sleep(2 + attempt * 3)
                continue
            raise


def github_api_repo_url(repo_key: str) -> str:
    return f"https://api.github.com/repos/{repo_key}"


def github_api_latest_release_url(repo_key: str) -> str:
    return f"https://api.github.com/repos/{repo_key}/releases/latest"


def packagist_search_url(query: str) -> str:
    return "https://packagist.org/search.json?" + urllib.parse.urlencode({"q": query})


def packagist_package_url(package_name: str) -> str:
    return f"https://repo.packagist.org/p2/{package_name}.json"


def packagist_package_metadata_url(package_name: str) -> str:
    return f"https://packagist.org/packages/{package_name}.json"


def read_editor_choice_slugs() -> set[str]:
    if not EDITOR_CHOICE_FILE.exists():
        return set()
    data = load_yaml(EDITOR_CHOICE_FILE)
    return set(data.get("slugs", []))


def read_editor_choice_copy() -> dict[str, dict[str, str]]:
    if not EDITOR_CHOICE_COPY_FILE.exists():
        return {}
    data = load_yaml(EDITOR_CHOICE_COPY_FILE)
    recommended = data.get("recommended_for") or {}
    reasons = data.get("why_it_stands_out") or {}
    if not isinstance(recommended, dict) or not isinstance(reasons, dict):
        raise ValueError(
            f"{EDITOR_CHOICE_COPY_FILE} must contain recommended_for and why_it_stands_out mappings"
        )
    slugs = set(recommended) | set(reasons)
    return {
        slug: {
            "recommended_for": str(recommended.get(slug) or "").strip(),
            "why_it_stands_out": str(reasons.get(slug) or "").strip(),
        }
        for slug in slugs
    }


def write_editor_choice_slugs(slugs: list[str]) -> None:
    EDITOR_CHOICE_FILE.parent.mkdir(parents=True, exist_ok=True)
    EDITOR_CHOICE_FILE.write_text(dump_yaml({"slugs": slugs}), encoding="utf-8")


def cli_token() -> str | None:
    return os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN")


def positive_int(value: str) -> int:
    number = int(value)
    if number < 0:
        raise argparse.ArgumentTypeError("must be non-negative")
    return number
