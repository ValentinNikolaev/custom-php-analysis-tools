from __future__ import annotations

import csv
import json
import sys
import tempfile
import unittest
from datetime import datetime, timezone
from pathlib import Path
from unittest.mock import patch


ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

import generate_exports  # noqa: E402


class GenerateExportsTests(unittest.TestCase):
    REFERENCE_TIME = datetime(2026, 8, 8, tzinfo=timezone.utc)

    def test_exports_are_sorted_machine_readable_and_include_derived_status(self) -> None:
        tools = [
            {
                "slug": "zeta",
                "name": "Zeta",
                "category": "Misc",
                "artifact_type": "analyzer",
                "use_cases": ["security", "dead-code"],
                "catalog_status": "current",
                "repo_updated_at": "2026-08-01T00:00:00Z",
            },
            {
                "slug": "alpha",
                "name": "Alpha",
                "category": "Bugs finders",
                "artifact_type": "analyzer-extension",
                "catalog_status": "historical",
            },
        ]
        with tempfile.TemporaryDirectory() as directory, patch.object(
            generate_exports, "load_catalog", return_value=tools
        ), patch.object(generate_exports, "source_commit", return_value="abc123"):
            output = Path(directory)
            json_path, csv_path, manifest_path = generate_exports.build_exports(
                output, self.REFERENCE_TIME
            )

            payload = json.loads(json_path.read_text(encoding="utf-8"))
            self.assertEqual(payload["schema_version"], 1)
            self.assertEqual(payload["source_commit"], "abc123")
            self.assertEqual([tool["slug"] for tool in payload["tools"]], ["alpha", "zeta"])
            self.assertTrue(payload["tools"][0]["is_historical"])
            self.assertEqual(payload["tools"][1]["lifecycle"], "Active")

            with csv_path.open(encoding="utf-8", newline="") as handle:
                rows = list(csv.DictReader(handle))
            self.assertEqual([row["slug"] for row in rows], ["alpha", "zeta"])
            self.assertEqual(rows[1]["use_cases"], "security|dead-code")

            manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
            self.assertEqual(manifest["record_count"], 2)
            self.assertEqual(manifest["artifacts"], ["catalog.json", "catalog.csv"])


if __name__ == "__main__":
    unittest.main()
