from __future__ import annotations

import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch


ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

import generate_editor_choice  # noqa: E402


class EditorialSelectionTests(unittest.TestCase):
    def test_generator_preserves_human_membership_and_corrects_public_filename(self) -> None:
        tool = {
            "slug": "sample",
            "name": "Sample Analyzer",
            "category": "Bugs finders",
            "public_url": "https://example.com",
            "repo_updated_at": "2026-08-01T00:00:00Z",
            "stars": 10,
            "catalog_status": "current",
        }
        copy = {
            "sample": {
                "recommended_for": "Teams needing focused checks for application defects",
                "why_it_stands_out": "Its project-aware rules cover a distinct and practical defect class.",
            }
        }
        with tempfile.TemporaryDirectory() as directory, patch.object(
            generate_editor_choice, "ROOT", Path(directory)
        ), patch.object(
            generate_editor_choice, "load_catalog", return_value=[tool]
        ), patch.object(
            generate_editor_choice, "read_editor_choice_slugs", return_value={"sample"}
        ), patch.object(
            generate_editor_choice, "read_editor_choice_copy", return_value=copy
        ), patch.object(sys, "argv", ["generate_editor_choice.py", "--as-of", "2026-08-08"]):
            generate_editor_choice.main()

            canonical = (Path(directory) / "EDITORS-CHOICE.md").read_text(encoding="utf-8")
            compatibility = (Path(directory) / "EDITOR-CHOISE.md").read_text(encoding="utf-8")

        self.assertIn("manually approved membership", canonical)
        self.assertIn("Sample Analyzer", canonical)
        self.assertIn("EDITORS-CHOICE.md", compatibility)
        self.assertNotIn("three alive projects", canonical)


if __name__ == "__main__":
    unittest.main()
