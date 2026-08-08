from __future__ import annotations

import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from catalog_lib import dump_yaml
from validate_catalog import validate_repository


class CatalogValidationTests(unittest.TestCase):
    def make_repository(self) -> tuple[tempfile.TemporaryDirectory, Path]:
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        root = Path(temporary.name)
        (root / "common" / "catalog").mkdir(parents=True)
        (root / "common" / "candidates").mkdir(parents=True)
        self.write_tool(root, "sample")
        (root / "common" / "editor-choice.yaml").write_text(
            dump_yaml({"slugs": ["sample"]}), encoding="utf-8"
        )
        (root / "common" / "editor-choice-copy.yaml").write_text(
            dump_yaml(
                {
                    "recommended_for": {"sample": "Teams checking a PHP application"},
                    "why_it_stands_out": {"sample": "It reports focused, actionable findings."},
                }
            ),
            encoding="utf-8",
        )
        return temporary, root

    def tool_data(self, slug: str = "sample") -> dict:
        return {
            "slug": slug,
            "name": slug.title(),
            "category": "Bugs finders",
            "artifact_type": "analyzer",
            "use_cases": ["bug-finding"],
            "ecosystems": ["generic"],
            "catalog_status": "current",
            "reviewed_at": "2026-08-08",
            "description": "Finds defects in PHP code.",
            "website": f"https://example.com/{slug}",
            "public_url": f"https://example.com/{slug}",
            "website_status": "available",
            "website_status_code": 200,
            "website_checked_at": "2026-08-08T00:00:00Z",
            "website_error": "",
            "repository": f"https://github.com/example/{slug}",
            "packagist": None,
            "stars": 10,
            "repo_updated_at": "2026-08-08T00:00:00Z",
            "metadata_updated_at": "2026-08-08T00:00:00Z",
            "quality_tags": ["php", "static-analysis"],
            "source": "manual-review",
            "notes": "",
        }

    def write_tool(self, root: Path, slug: str, **overrides) -> None:
        data = self.tool_data(slug)
        data.update(overrides)
        (root / "common" / "catalog" / f"{slug}.yaml").write_text(dump_yaml(data), encoding="utf-8")

    def candidate_data(self, slug: str = "candidate") -> dict:
        data = self.tool_data(slug)
        data.update(
            {
                "website_status": "unknown",
                "website_status_code": 0,
                "website_checked_at": None,
                "review_status": "pending",
                "review_notes": "Needs editorial review.",
                "discovered_at": "2026-08-08T00:00:00Z",
                "last_reviewed_at": None,
            }
        )
        return data

    def test_valid_repository_passes(self) -> None:
        _, root = self.make_repository()
        self.assertEqual(validate_repository(root), [])

    def test_unknown_and_legacy_editor_choice_fields_are_rejected(self) -> None:
        _, root = self.make_repository()
        path = root / "common" / "catalog" / "sample.yaml"
        data = self.tool_data()
        data["editor_choice"] = True
        data["typo_field"] = "unexpected"
        path.write_text(dump_yaml(data), encoding="utf-8")
        errors = "\n".join(validate_repository(root))
        self.assertIn("legacy second source", errors)
        self.assertIn("unknown fields: typo_field", errors)

    def test_filename_types_category_url_and_date_are_strict(self) -> None:
        _, root = self.make_repository()
        path = root / "common" / "catalog" / "sample.yaml"
        data = self.tool_data()
        data.update(
            {
                "slug": "Wrong Slug",
                "category": "Everything",
                "stars": "many",
                "website": "example.com/no-scheme",
                "metadata_updated_at": "yesterday",
            }
        )
        path.write_text(dump_yaml(data), encoding="utf-8")
        errors = "\n".join(validate_repository(root))
        self.assertIn("lower-case kebab-case", errors)
        self.assertIn("must match filename", errors)
        self.assertIn("category must be one of", errors)
        self.assertIn("stars must be an integer", errors)
        self.assertIn("website must be an absolute http(s) URL", errors)
        self.assertIn("metadata_updated_at must be an ISO 8601", errors)

    def test_duplicate_repositories_and_candidate_overlap_are_rejected(self) -> None:
        _, root = self.make_repository()
        self.write_tool(root, "second", repository="https://github.com/example/sample")
        candidate = self.candidate_data()
        candidate["repository"] = "https://github.com/EXAMPLE/sample/"
        (root / "common" / "candidates" / "candidate.yaml").write_text(
            dump_yaml(candidate), encoding="utf-8"
        )
        errors = "\n".join(validate_repository(root))
        self.assertIn("duplicate catalog repository", errors)
        self.assertIn("repository overlaps catalog entry", errors)

    def test_candidate_review_state_is_required(self) -> None:
        _, root = self.make_repository()
        candidate = self.candidate_data()
        del candidate["review_status"]
        del candidate["review_notes"]
        (root / "common" / "candidates" / "candidate.yaml").write_text(
            dump_yaml(candidate), encoding="utf-8"
        )
        errors = "\n".join(validate_repository(root))
        self.assertIn("missing required fields: review_notes, review_status", errors)

    def test_current_entries_require_comparison_fields_but_historical_entries_do_not(self) -> None:
        _, root = self.make_repository()
        current = self.tool_data()
        for field in ("artifact_type", "use_cases", "ecosystems", "reviewed_at"):
            current.pop(field)
        (root / "common" / "catalog" / "sample.yaml").write_text(
            dump_yaml(current), encoding="utf-8"
        )
        errors = "\n".join(validate_repository(root))
        self.assertIn(
            "current/adjacent entries require comparison fields: artifact_type, ecosystems, reviewed_at, use_cases",
            errors,
        )

        current["catalog_status"] = "historical"
        (root / "common" / "catalog" / "sample.yaml").write_text(
            dump_yaml(current), encoding="utf-8"
        )
        historical_errors = "\n".join(validate_repository(root))
        self.assertNotIn("require comparison fields", historical_errors)

    def test_editor_choice_must_be_unique_and_reference_current_tools(self) -> None:
        _, root = self.make_repository()
        (root / "common" / "editor-choice.yaml").write_text(
            dump_yaml({"slugs": ["sample", "sample", "missing"]}), encoding="utf-8"
        )
        errors = "\n".join(validate_repository(root))
        self.assertIn("slugs must be unique", errors)
        self.assertIn("unknown catalog slug 'missing'", errors)

    def test_editorial_copy_mappings_must_match_and_reference_catalog(self) -> None:
        _, root = self.make_repository()
        (root / "common" / "editor-choice-copy.yaml").write_text(
            dump_yaml(
                {
                    "recommended_for": {"sample": "A use case", "ghost": "Unknown"},
                    "why_it_stands_out": {"sample": "A reason"},
                }
            ),
            encoding="utf-8",
        )
        errors = "\n".join(validate_repository(root))
        self.assertIn("must cover the same slugs", errors)
        self.assertIn("editorial copy references unknown catalog slug 'ghost'", errors)

    def test_rejected_candidate_registry_is_strict_and_disjoint_from_queue(self) -> None:
        _, root = self.make_repository()
        candidate = self.candidate_data("candidate")
        (root / "common" / "candidates" / "candidate.yaml").write_text(
            dump_yaml(candidate), encoding="utf-8"
        )
        (root / "common" / "rejected-candidates.yaml").write_text(
            dump_yaml(
                {
                    "reviewed_at": "2026-08-08",
                    "rejections": [
                        {
                            "slug": "candidate",
                            "name": "Candidate",
                            "repository": "https://github.com/example/candidate",
                            "reason": "Not relevant to PHP analysis.",
                            "rejected_at": "2026-08-08",
                            "reconsider_after": None,
                        },
                        {
                            "slug": "candidate",
                            "name": "Duplicate",
                            "repository": "https://github.com/example/candidate",
                            "reason": "Duplicate rejection.",
                            "rejected_at": "not-a-date",
                            "reconsider_after": None,
                            "unexpected": True,
                        },
                    ],
                }
            ),
            encoding="utf-8",
        )
        errors = "\n".join(validate_repository(root))
        self.assertIn("slug is still present in the active candidate queue", errors)
        self.assertIn("repository is still present in the active candidate queue", errors)
        self.assertIn("slug duplicates rejections[1]", errors)
        self.assertIn("repository duplicates rejections[1]", errors)
        self.assertIn("has unknown fields: unexpected", errors)
        self.assertIn("rejected_at must be an ISO 8601", errors)


if __name__ == "__main__":
    unittest.main()
