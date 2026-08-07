from __future__ import annotations

import argparse
import html
import ipaddress
import shutil
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlparse

from catalog_lib import CATEGORY_ORDER, ROOT, category_rank, load_catalog, read_editor_choice_copy, read_editor_choice_slugs
from generate_readme import (
    apply_editor_choice_copy,
    category_title,
    is_dead,
    lifecycle,
    parse_date,
    sorted_for_table,
    stars_value,
)


SITE_SOURCE = ROOT / "site"
DEFAULT_OUTPUT = ROOT / "site-dist"
BUILD_MARKER = ".php-analysis-tools-site-build"
REPOSITORY_URL = "https://github.com/ValentinNikolaev/php-analysis-tools-catalog"
SITE_URL = "https://valentinnikolaev.github.io/php-analysis-tools-catalog/"
DEFAULT_BASE_PATH = "/php-analysis-tools-catalog/"


def escape(value: object) -> str:
    return html.escape(str(value), quote=True)


def safe_url(value: object) -> str | None:
    if not value:
        return None
    url = str(value).strip()
    parsed = urlparse(url)
    if parsed.scheme not in {"http", "https"} or not parsed.netloc or parsed.username or parsed.password:
        return None
    hostname = parsed.hostname
    if not hostname or hostname.casefold() == "localhost":
        return None
    try:
        address = ipaddress.ip_address(hostname)
    except ValueError:
        pass
    else:
        if not address.is_global:
            return None
    if any(part.casefold() == "localhost" for part in hostname.split(".")):
        return None
    return url


def primary_url(tool: dict) -> str:
    website_available = tool.get("website_status") != "unavailable"
    if tool.get("category") == "SaaS":
        keys = (
            ("public_url", "website", "repository", "packagist")
            if website_available
            else ("repository", "packagist")
        )
    else:
        keys = (
            ("repository", "public_url", "website", "packagist")
            if website_available
            else ("repository", "packagist")
        )
    for key in keys:
        url = safe_url(tool.get(key))
        if url:
            return url
    return REPOSITORY_URL


def resource_links(tool: dict) -> str:
    links: list[tuple[str, str]] = []
    repository = safe_url(tool.get("repository"))
    package = safe_url(tool.get("packagist"))
    website = (
        safe_url(tool.get("public_url") or tool.get("website"))
        if tool.get("website_status") != "unavailable"
        else None
    )
    release = safe_url(tool.get("latest_release_url"))

    if repository:
        links.append(("Source", repository))
    if package:
        links.append(("Package", package))
    if website and website.rstrip("/") != (repository or "").rstrip("/"):
        links.append(("Website", website))
    if release and not repository:
        links.append(("Release", release))

    if not links:
        return '<span class="resource-empty">No public link</span>'

    return "".join(
        f'<a class="resource-link" href="{escape(url)}">{escape(label)}<span aria-hidden="true"> ↗</span></a>'
        for label, url in links
    )


def latest_version(tool: dict) -> str:
    value = tool.get("latest_release_tag") or tool.get("latest_version") or tool.get("latest_release_name")
    return str(value or "-")


def normalized_iso_date(value: object) -> str:
    if not value:
        return ""
    return str(value).replace("Z", "+00:00")


def compact_date(value: str | None) -> str:
    parsed = parse_date(value)
    return parsed.strftime("%d.%m.%y") if parsed else ""


def title_icon(tool: dict) -> str:
    icon = str(tool.get("title_icon") or "").strip()
    label = str(tool.get("title_icon_label") or "Tool type").strip()
    if not icon.startswith("assets/tool-icons/") or "/../" in f"/{icon}/":
        return ""
    return (
        f'<img class="tool-title-icon" src="{escape(icon)}" '
        f'alt="{escape(label)}" title="{escape(label)}">'
    )


def status_badge(tool: dict, status: str) -> str:
    if tool.get("category") == "SaaS" and status == "Unknown":
        return ""
    return f'<span class="status status--{escape(status.casefold())}">{escape(status)}</span>'


def tool_card(tool: dict, reference_time: datetime, rank: int) -> str:
    status = lifecycle(tool, reference_time)[1]
    name = str(tool.get("name") or "Unnamed tool")
    slug = str(tool.get("slug") or "tool")
    category = str(tool.get("category") or "Misc")
    description = str(tool.get("best_for") or tool.get("description") or "No description available.")
    stars = stars_value(tool)
    updated = compact_date(tool.get("repo_updated_at")) or "Unknown"
    released = compact_date(
        tool.get("latest_release_published_at") or tool.get("latest_version_released_at")
    ) or "Unknown"
    updated_iso = normalized_iso_date(tool.get("repo_updated_at"))
    tags = " ".join(str(tag) for tag in tool.get("quality_tags") or [])
    search_text = " ".join((name, category_title(category), description, tags)).casefold()
    version = latest_version(tool)
    website_unavailable = tool.get("website_status") == "unavailable"
    show_repository_metadata = category != "SaaS" or safe_url(tool.get("repository")) is not None
    metadata = (
        f"""
  <dl class="tool-meta">
    <div><dt><span aria-hidden="true">⭐</span> Stars</dt><dd>{stars:,}</dd></div>
    <div><dt>Latest</dt><dd title="{escape(version)}">{escape(version)}</dd></div>
    <div><dt>Last commit</dt><dd>{escape(updated)}</dd></div>
    <div><dt>Last release</dt><dd>{escape(released)}</dd></div>
  </dl>"""
        if show_repository_metadata
        else ""
    )

    return f"""
<article class="tool-card" id="tool-{escape(slug)}"
  data-name="{escape(name.casefold())}"
  data-search="{escape(search_text)}"
  data-category="{escape(category)}"
  data-status="{escape(status)}"
  data-stars="{stars}"
  data-updated="{escape(updated_iso)}"
  data-rank="{rank}">
  <div class="tool-card__heading">
    <div>
      <span class="eyebrow">{escape(category_title(category))}</span>
      <h3><a href="{escape(primary_url(tool))}">{escape(name)}</a>{title_icon(tool)}</h3>
    </div>
    {status_badge(tool, status)}
  </div>
  <p class="tool-description">{escape(description)}</p>
  {metadata}
  {f'<p class="availability-note">Official website currently unavailable</p>' if website_unavailable else ''}
  <div class="resource-links" aria-label="Resources for {escape(name)}">{resource_links(tool)}</div>
</article>""".strip()


def editor_card(tool: dict, reference_time: datetime) -> str:
    name = str(tool.get("name") or "Unnamed tool")
    category = str(tool.get("category") or "Misc")
    recommended_for = str(tool.get("best_for") or "")
    reason = str(tool.get("editor_reason") or "")
    status = lifecycle(tool, reference_time)[1]

    return f"""
<article class="editor-card">
  <div class="editor-card__meta">
    <span class="eyebrow">{escape(category_title(category))}</span>
    {status_badge(tool, status)}
  </div>
  <h3><a href="{escape(primary_url(tool))}">{escape(name)}</a>{title_icon(tool)}</h3>
  <p class="editor-card__audience">{escape(recommended_for)}</p>
  <p>{escape(reason)}</p>
  <a class="text-link" href="#tool-{escape(tool.get('slug') or 'tool')}">View catalog details<span aria-hidden="true"> ↓</span></a>
</article>""".strip()


def category_options(tools: list[dict]) -> str:
    counts = {
        category: sum(1 for tool in tools if tool.get("category") == category)
        for category in CATEGORY_ORDER
    }
    return "\n".join(
        f'<option value="{escape(category)}">{escape(category_title(category))} ({counts[category]})</option>'
        for category in CATEGORY_ORDER
        if counts[category]
    )


def status_options(tools: list[dict], reference_time: datetime) -> str:
    status_order = ("Active", "Quiet", "Inactive", "Unknown")
    counts = {
        status: sum(1 for tool in tools if lifecycle(tool, reference_time)[1] == status)
        for status in status_order
    }
    return "\n".join(
        f'<option value="{escape(status)}">{escape(status)} ({counts[status]})</option>'
        for status in status_order
        if counts[status]
    )


def latest_catalog_update(tools: list[dict]) -> str:
    values = [str(tool.get("metadata_updated_at")) for tool in tools if tool.get("metadata_updated_at")]
    if not values:
        return "Unknown"
    latest = max(datetime.fromisoformat(value.replace("Z", "+00:00")) for value in values)
    return f"{latest.strftime('%b')} {latest.day}, {latest.year}"


def render_index(tools: list[dict], reference_time: datetime) -> str:
    template = (SITE_SOURCE / "index.html").read_text(encoding="utf-8")
    current_tools = [tool for tool in tools if not is_dead(tool, reference_time)]
    memorial_tools = [tool for tool in tools if is_dead(tool, reference_time)]
    catalog_tools = [tool for tool in current_tools if tool.get("category") != "SaaS"]
    hosted_tools = [tool for tool in current_tools if tool.get("category") == "SaaS"]
    ordered_tools = sorted_for_table(catalog_tools, reference_time)

    editor_slugs = read_editor_choice_slugs()
    editor_tools = apply_editor_choice_copy(
        sorted(
            [
                tool
                for tool in catalog_tools
                if tool.get("slug") in editor_slugs
            ],
            key=lambda item: (category_rank(item.get("category")), item.get("name", "").casefold()),
        ),
        read_editor_choice_copy(),
    )

    replacements = {
        "{{CANONICAL_URL}}": SITE_URL,
        "{{REPOSITORY_URL}}": REPOSITORY_URL,
        "{{CURRENT_COUNT}}": str(len(current_tools)),
        "{{TOOL_COUNT}}": str(len(catalog_tools)),
        "{{HOSTED_COUNT}}": str(len(hosted_tools)),
        "{{MEMORIAL_COUNT}}": str(len(memorial_tools)),
        "{{EDITOR_COUNT}}": str(len(editor_tools)),
        "{{CATEGORY_COUNT}}": str(len({tool.get("category") for tool in catalog_tools})),
        "{{LAST_UPDATED}}": escape(latest_catalog_update(tools)),
        "{{CATEGORY_OPTIONS}}": category_options(catalog_tools),
        "{{STATUS_OPTIONS}}": status_options(catalog_tools, reference_time),
        "{{EDITOR_CARDS}}": "\n".join(editor_card(tool, reference_time) for tool in editor_tools),
        "{{TOOL_CARDS}}": "\n".join(
            tool_card(tool, reference_time, rank) for rank, tool in enumerate(ordered_tools, start=1)
        ),
        "{{HOSTED_CARDS}}": "\n".join(
            tool_card(tool, reference_time, rank)
            for rank, tool in enumerate(
                sorted(hosted_tools, key=lambda item: item.get("name", "").casefold()),
                start=1,
            )
        ),
        "{{MEMORIAL_CARDS}}": "\n".join(
            tool_card(tool, reference_time, rank)
            for rank, tool in enumerate(
                sorted(
                    memorial_tools,
                    key=lambda item: item.get("name", "").casefold(),
                ),
                start=1,
            )
        ),
    }
    for token, value in replacements.items():
        template = template.replace(token, value)
    if "{{" in template or "}}" in template:
        raise ValueError("Unresolved placeholder remains in site/index.html")
    return template


def normalize_base_path(value: str) -> str:
    value = value.strip()
    if not value.startswith("/") or "://" in value or "?" in value or "#" in value:
        raise ValueError("Base path must be an absolute URL path")
    parts = [part for part in value.split("/") if part]
    if any(part in {".", ".."} for part in parts):
        raise ValueError("Base path cannot contain dot segments")
    return "/" + "/".join(parts) + "/" if parts else "/"


def render_not_found(base_path: str) -> str:
    template = (SITE_SOURCE / "404.html").read_text(encoding="utf-8")
    return template.replace("{{BASE_PATH}}", escape(base_path)).replace("{{REPOSITORY_URL}}", REPOSITORY_URL)


def validate_output(output: Path) -> None:
    required = (
        output / "index.html",
        output / "404.html",
        output / "assets" / "site.css",
        output / "assets" / "site.js",
        output / "assets" / "favicon.svg",
    )
    missing = [str(path.relative_to(output)) for path in required if not path.is_file()]
    if missing:
        raise ValueError("Missing generated site files: " + ", ".join(missing))

    index = (output / "index.html").read_text(encoding="utf-8")
    if index.count("<h1") != 1:
        raise ValueError("Generated home page must contain exactly one H1")
    if "{{" in index or "}}" in index:
        raise ValueError("Generated home page contains unresolved template placeholders")


def prepare_output(output: Path) -> None:
    if output.exists() and not output.is_dir():
        raise ValueError(f"Output path is not a directory: {output}")
    if output.exists() and any(output.iterdir()):
        marker = output / BUILD_MARKER
        if not marker.is_file():
            raise ValueError(
                f"Refusing to replace a non-empty directory not created by this generator: {output}"
            )
        shutil.rmtree(output)
    output.mkdir(parents=True, exist_ok=True)
    (output / BUILD_MARKER).write_text("Generated by scripts/generate_site.py\n", encoding="utf-8")


def build_site(
    output: Path = DEFAULT_OUTPUT,
    reference_time: datetime | None = None,
    base_path: str = DEFAULT_BASE_PATH,
) -> Path:
    reference_time = reference_time or datetime.now(timezone.utc)
    base_path = normalize_base_path(base_path)
    prepare_output(output)

    tools = load_catalog()
    (output / "index.html").write_text(render_index(tools, reference_time), encoding="utf-8")
    (output / "404.html").write_text(render_not_found(base_path), encoding="utf-8")
    shutil.copytree(SITE_SOURCE / "assets", output / "assets")
    (output / ".nojekyll").write_text("", encoding="utf-8")
    validate_output(output)
    return output


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Generate the GitHub Pages catalog site")
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT, help="Generated site directory")
    parser.add_argument(
        "--base-path",
        default=DEFAULT_BASE_PATH,
        help="Absolute URL path where the generated site will be served",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    output = build_site(args.output.resolve(), base_path=args.base_path)
    print(f"Generated GitHub Pages site in {output}")


if __name__ == "__main__":
    main()
