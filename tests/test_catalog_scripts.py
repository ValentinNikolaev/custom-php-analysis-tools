from __future__ import annotations

import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import discover_tools
from catalog_lib import dump_yaml, load_yaml
from generate_readme import lifecycle, sorted_for_table, tool_row


class CatalogScriptTests(unittest.TestCase):
    def test_yaml_round_trip_keeps_public_url_fields(self) -> None:
        data = {
            "slug": "sample",
            "name": "Sample",
            "public_url": "https://example.com",
            "website_status": "available",
            "website_status_code": 200,
            "website_checked_at": "2026-07-25T00:00:00Z",
            "website_error": "",
            "latest_version": "1.2.3",
            "latest_version_released_at": "2026-07-20T00:00:00+00:00",
            "quality_tags": ["php", "static-analysis"],
        }
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "sample.yaml"
            path.write_text(dump_yaml(data), encoding="utf-8")
            self.assertEqual(load_yaml(path), data)

    def test_discovery_static_analysis_query_uses_fifty_star_threshold(self) -> None:
        self.assertIn("topic:php topic:static-analysis stars:>50", discover_tools.QUERIES)
        self.assertNotIn("topic:php topic:static-analysis stars:>100", discover_tools.QUERIES)

    def test_lifecycle_badges_from_repo_update_age(self) -> None:
        self.assertIn("alive", lifecycle({"repo_updated_at": "2026-07-01T00:00:00Z"})[1])
        self.assertIn("dying", lifecycle({"repo_updated_at": "2026-03-01T00:00:00Z"})[1])
        self.assertIn("almost_dead", lifecycle({"repo_updated_at": "2025-12-01T00:00:00Z"})[1])
        self.assertIn("dead", lifecycle({"repo_updated_at": "2024-01-01T00:00:00Z"})[1])
        self.assertIn("unknown", lifecycle({})[1])

    def test_table_sorting_groups_status_before_stars(self) -> None:
        tools = [
            {"name": "Dead High Stars", "stars": 100000, "repo_updated_at": "2024-01-01T00:00:00Z"},
            {"name": "Alive Low Stars", "stars": 1, "repo_updated_at": "2026-07-01T00:00:00Z"},
            {"name": "Alive High Stars", "stars": 10, "repo_updated_at": "2026-07-01T00:00:00Z"},
        ]
        self.assertEqual(
            [tool["name"] for tool in sorted_for_table(tools)],
            ["Alive High Stars", "Alive Low Stars", "Dead High Stars"],
        )

    def test_tool_row_contains_status_star_and_links(self) -> None:
        row = tool_row(
            {
                "name": "PHP Stan",
                "description": "Static analysis",
                "public_url": "https://phpstan.org",
                "repository": "https://github.com/phpstan/phpstan",
                "packagist": "https://packagist.org/packages/phpstan/phpstan",
                "stars": 14042,
                "repo_updated_at": "2026-07-25T00:00:00Z",
                "latest_version": "2.2.5",
            }
        )
        self.assertIn("![Alive]", row)
        self.assertIn("14,042", row)
        self.assertIn("[GitHub](https://github.com/phpstan/phpstan)", row)
        self.assertIn("[Packagist](https://packagist.org/packages/phpstan/phpstan)", row)


if __name__ == "__main__":
    unittest.main()
