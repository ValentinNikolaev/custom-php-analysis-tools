from __future__ import annotations

import argparse
import csv
import io
import json
import os
import subprocess
from datetime import datetime
from pathlib import Path
from typing import Any

from catalog_lib import CATEGORY_IDS, ROOT, load_catalog
from generate_readme import category_title, is_dead, lifecycle, reference_time_from_values


DEFAULT_OUTPUT = ROOT / "exports"
SCHEMA_VERSION = 1
CSV_FIELDS = (
    "slug",
    "name",
    "category",
    "category_id",
    "category_label",
    "artifact_type",
    "catalog_status",
    "lifecycle",
    "description",
    "best_for",
    "use_cases",
    "ecosystems",
    "capabilities",
    "license",
    "pricing",
    "installation",
    "supported_php",
    "website",
    "repository",
    "packagist",
    "latest_version",
    "latest_release_tag",
    "stars",
    "repo_updated_at",
    "reviewed_at",
    "successor_of",
    "supersedes",
)


def source_commit() -> str:
    if os.environ.get("GITHUB_SHA"):
        return str(os.environ["GITHUB_SHA"])
    try:
        result = subprocess.run(
            ["git", "rev-parse", "HEAD"],
            cwd=ROOT,
            check=True,
            capture_output=True,
            text=True,
        )
    except (OSError, subprocess.CalledProcessError):
        return "unknown"
    return result.stdout.strip() or "unknown"


def iso_z(value: datetime) -> str:
    return value.isoformat().replace("+00:00", "Z")


def export_record(tool: dict[str, Any], reference_time: datetime) -> dict[str, Any]:
    return {
        **tool,
        "category_id": CATEGORY_IDS.get(str(tool.get("category") or ""), "unknown"),
        "category_label": category_title(str(tool.get("category") or "Misc")),
        "lifecycle": lifecycle(tool, reference_time)[1],
        "is_historical": is_dead(tool, reference_time),
    }


def csv_value(value: Any) -> str | int:
    if value is None:
        return ""
    if isinstance(value, list):
        return "|".join(str(item) for item in value)
    if isinstance(value, dict):
        return json.dumps(value, ensure_ascii=False, sort_keys=True)
    if isinstance(value, bool):
        return "true" if value else "false"
    return value


def build_exports(output: Path, reference_time: datetime) -> tuple[Path, Path, Path]:
    output.mkdir(parents=True, exist_ok=True)
    records = [export_record(tool, reference_time) for tool in load_catalog()]
    records.sort(key=lambda item: str(item.get("slug") or ""))
    commit = source_commit()

    json_path = output / "catalog.json"
    json_path.write_text(
        json.dumps(
            {
                "schema_version": SCHEMA_VERSION,
                "as_of": iso_z(reference_time),
                "source_repository": "https://github.com/ValentinNikolaev/php-analysis-tools-catalog",
                "source_commit": commit,
                "data_license": "https://creativecommons.org/licenses/by/4.0/",
                "attribution": "PHP Analysis Tools Catalog by Valentin Nikolaev and contributors",
                "tool_count": len(records),
                "tools": records,
            },
            ensure_ascii=False,
            indent=2,
            sort_keys=True,
        )
        + "\n",
        encoding="utf-8",
    )

    buffer = io.StringIO(newline="")
    writer = csv.DictWriter(buffer, fieldnames=CSV_FIELDS, lineterminator="\n")
    writer.writeheader()
    for record in records:
        writer.writerow({field: csv_value(record.get(field)) for field in CSV_FIELDS})
    csv_path = output / "catalog.csv"
    csv_path.write_text(buffer.getvalue(), encoding="utf-8")

    manifest_path = output / "build-manifest.json"
    manifest_path.write_text(
        json.dumps(
            {
                "schema_version": SCHEMA_VERSION,
                "as_of": iso_z(reference_time),
                "source_commit": commit,
                "record_count": len(records),
                "artifacts": ["catalog.json", "catalog.csv"],
            },
            indent=2,
            sort_keys=True,
        )
        + "\n",
        encoding="utf-8",
    )
    return json_path, csv_path, manifest_path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Generate machine-readable catalog exports")
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument(
        "--as-of",
        help="ISO-8601 date used for reproducible derived fields; SOURCE_DATE_EPOCH is also supported",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    reference_time = reference_time_from_values(args.as_of)
    paths = build_exports(args.output.resolve(), reference_time)
    print("Generated " + ", ".join(str(path.relative_to(ROOT)) for path in paths))


if __name__ == "__main__":
    main()
