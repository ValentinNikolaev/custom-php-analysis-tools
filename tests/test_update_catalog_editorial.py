from __future__ import annotations

import sys
import unittest
import urllib.error
from pathlib import Path
from unittest.mock import patch


ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

import update_catalog  # noqa: E402


class UpdateCatalogEditorialTests(unittest.TestCase):
    def test_slug_selection_is_explicit_and_rejects_typos(self) -> None:
        tools = [{"slug": "alpha"}, {"slug": "beta"}, {"slug": "gamma"}]
        self.assertEqual(
            update_catalog.select_tools(tools, ["beta,gamma"]),
            [{"slug": "beta"}, {"slug": "gamma"}],
        )
        with self.assertRaisesRegex(ValueError, "unknown catalog slug"):
            update_catalog.select_tools(tools, ["missing"])

    def test_github_description_is_provenance_not_an_editorial_overwrite(self) -> None:
        tool = {
            "slug": "sample",
            "repository": "https://github.com/example/sample",
            "description": "Editorial explanation of the PHP use case.",
        }
        payload = {
            "html_url": "https://github.com/example/sample",
            "stargazers_count": 42,
            "pushed_at": "2026-08-08T00:00:00Z",
            "description": "Upstream repository tagline.",
            "homepage": "https://example.com",
            "archived": False,
            "topics": ["php", "static-analysis"],
        }
        with patch.object(update_catalog, "http_json", return_value=payload):
            result = update_catalog.update_from_github(tool, token=None)

        self.assertTrue(result.checked)
        self.assertEqual(tool["description"], "Editorial explanation of the PHP use case.")
        self.assertEqual(tool["upstream_description"], "Upstream repository tagline.")

    def test_repository_license_and_packagist_constraints_feed_comparison_fields(self) -> None:
        tool = {
            "slug": "sample",
            "repository": "https://github.com/example/sample",
            "packagist": "https://packagist.org/packages/example/sample",
            "artifact_type": "analyzer",
        }
        repo = {
            "html_url": tool["repository"],
            "stargazers_count": 5,
            "pushed_at": "2026-08-08T00:00:00Z",
            "license": {"spdx_id": "MIT"},
            "topics": ["php"],
        }
        package = {
            "packages": {
                "example/sample": [
                    {
                        "version": "2.0.0",
                        "version_normalized": "2.0.0.0",
                        "time": "2026-08-01T00:00:00+00:00",
                        "require": {"php": "^8.2"},
                        "source": {"url": "https://github.com/example/sample.git"},
                    }
                ]
            }
        }
        with patch.object(update_catalog, "http_json", side_effect=[repo, package]):
            update_catalog.update_from_github(tool, token=None)
            result = update_catalog.update_packagist_version(tool, token=None)

        self.assertTrue(result.checked)
        self.assertEqual(tool["license"], "MIT")
        self.assertEqual(tool["supported_php"], "^8.2")
        self.assertEqual(tool["installation"], "composer require --dev example/sample")

    def test_access_block_does_not_claim_the_product_is_unavailable(self) -> None:
        tool = {"slug": "sample", "public_url": "https://example.com"}

        errors = [
            urllib.error.HTTPError(
                "https://example.com", 403, "forbidden", hdrs=None, fp=None
            )
            for _ in range(2)
        ]
        for error in errors:
            self.addCleanup(error.close)

        with patch.object(update_catalog.urllib.request, "urlopen", side_effect=errors):
            result = update_catalog.check_website(tool, checked_at="2026-08-08T00:00:00Z")

        self.assertTrue(result.checked)
        self.assertEqual(tool["website_status"], "bot_blocked")
        self.assertNotEqual(tool["website_status"], "unavailable")

    def test_network_failure_is_marked_transient(self) -> None:
        tool = {"slug": "sample", "public_url": "https://example.com"}
        error = urllib.error.URLError("temporary DNS failure")
        with patch.object(update_catalog.urllib.request, "urlopen", side_effect=error):
            update_catalog.check_website(tool, checked_at="2026-08-08T00:00:00Z")
        self.assertEqual(tool["website_status"], "temporarily_unreachable")


if __name__ == "__main__":
    unittest.main()
