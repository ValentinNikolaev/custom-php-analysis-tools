from __future__ import annotations

import sys
import tempfile
import unittest
from datetime import datetime, timezone
from html.parser import HTMLParser
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

from catalog_lib import load_catalog  # noqa: E402
from generate_readme import is_dead  # noqa: E402
from generate_site import BUILD_MARKER, build_site, normalize_base_path, primary_url, safe_url, tool_card  # noqa: E402


class DocumentParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.ids: set[str] = set()
        self.hrefs: list[str] = []
        self.scripts: list[str] = []
        self.script_attributes: list[dict[str, str | None]] = []
        self.h1_count = 0

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        values = dict(attrs)
        if values.get("id"):
            self.ids.add(str(values["id"]))
        if tag == "a" and values.get("href"):
            self.hrefs.append(str(values["href"]))
        if tag == "script" and values.get("src"):
            self.scripts.append(str(values["src"]))
            self.script_attributes.append(values)
        if tag == "h1":
            self.h1_count += 1


class GenerateSiteTests(unittest.TestCase):
    REFERENCE_TIME = datetime(2026, 8, 6, tzinfo=timezone.utc)

    def build_in_temp(self) -> tuple[tempfile.TemporaryDirectory[str], Path]:
        directory = tempfile.TemporaryDirectory()
        output = Path(directory.name) / "site"
        build_site(output, reference_time=self.REFERENCE_TIME)
        return directory, output

    def test_build_contains_every_catalog_entry_and_required_assets(self) -> None:
        directory, output = self.build_in_temp()
        self.addCleanup(directory.cleanup)
        index = (output / "index.html").read_text(encoding="utf-8")

        for tool in load_catalog():
            self.assertIn(f'id="tool-{tool["slug"]}"', index)

        for relative_path in (
            "404.html",
            "assets/site.css",
            "assets/site.js",
            "assets/favicon.svg",
            ".nojekyll",
            BUILD_MARKER,
        ):
            self.assertTrue((output / relative_path).is_file(), relative_path)

    def test_home_page_has_valid_internal_anchors_and_one_h1(self) -> None:
        directory, output = self.build_in_temp()
        self.addCleanup(directory.cleanup)
        parser = DocumentParser()
        parser.feed((output / "index.html").read_text(encoding="utf-8"))

        self.assertEqual(parser.h1_count, 1)
        for href in parser.hrefs:
            if href.startswith("#"):
                self.assertIn(href[1:], parser.ids, href)
        self.assertEqual(
            parser.scripts,
            ["assets/site.js?v=2", "https://static.cloudflareinsights.com/beacon.min.js"],
        )
        self.assertEqual(parser.script_attributes[1].get("type"), "module")
        self.assertEqual(
            parser.script_attributes[1].get("data-cf-beacon"),
            '{"token":"1bc156f61a6c4baab33e1f9a082f72d4"}',
        )

    def test_generated_counts_distinguish_current_and_memorial_tools(self) -> None:
        directory, output = self.build_in_temp()
        self.addCleanup(directory.cleanup)
        index = (output / "index.html").read_text(encoding="utf-8")
        tools = load_catalog()
        current = sum(not is_dead(tool, self.REFERENCE_TIME) for tool in tools)
        memorial = sum(is_dead(tool, self.REFERENCE_TIME) for tool in tools)

        self.assertIn(f"<dt>{current}</dt><dd>current tools</dd>", index)
        self.assertIn(f"View {memorial} preserved projects", index)

    def test_memorial_cards_are_ordered_by_project_name(self) -> None:
        directory, output = self.build_in_temp()
        self.addCleanup(directory.cleanup)
        index = (output / "index.html").read_text(encoding="utf-8")
        memorial_tools = sorted(
            (tool for tool in load_catalog() if is_dead(tool, self.REFERENCE_TIME)),
            key=lambda tool: tool.get("name", "").casefold(),
        )
        positions = [index.index(f'id="tool-{tool["slug"]}"') for tool in memorial_tools]

        self.assertEqual(positions, sorted(positions))

    def test_custom_base_path_is_applied_to_not_found_assets_and_home_link(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory) / "site"
            build_site(output, reference_time=self.REFERENCE_TIME, base_path="/preview")
            not_found = (output / "404.html").read_text(encoding="utf-8")

        self.assertIn('href="/preview/assets/site.css?v=2"', not_found)
        self.assertIn('href="/preview/"', not_found)
        self.assertEqual(normalize_base_path("/preview"), "/preview/")
        with self.assertRaisesRegex(ValueError, "absolute URL path"):
            normalize_base_path("https://example.com/preview")

    def test_tool_content_is_escaped_and_unsafe_urls_are_rejected(self) -> None:
        card = tool_card(
            {
                "slug": "unsafe",
                "name": '<script>alert("name")</script>',
                "description": '<img src=x onerror=alert("description")>',
                "public_url": "javascript:alert(1)",
                "category": "Misc",
            },
            self.REFERENCE_TIME,
            1,
        )

        self.assertNotIn("<script>", card)
        self.assertNotIn("<img", card)
        self.assertNotIn("javascript:", card)
        self.assertIn("&lt;script&gt;", card)
        self.assertIsNone(safe_url("javascript:alert(1)"))
        self.assertIsNone(safe_url("https://user:secret@example.com"))
        self.assertIsNone(safe_url("http://127.0.0.1/private"))

    def test_unavailable_website_is_not_published_as_a_primary_or_resource_link(self) -> None:
        tool = {
            "slug": "offline",
            "name": "Offline tool",
            "description": "A tool with an unavailable website",
            "public_url": "https://offline.example.com",
            "website_status": "unavailable",
            "repository": "https://github.com/example/offline",
            "category": "Misc",
        }
        card = tool_card(tool, self.REFERENCE_TIME, 1)

        self.assertEqual(primary_url(tool), "https://github.com/example/offline")
        self.assertNotIn("https://offline.example.com", card)
        self.assertIn("Official website currently unavailable", card)

    def test_primary_link_priority_depends_on_category(self) -> None:
        links = {
            "website_status": "available",
            "website": "https://example.com/tool",
            "repository": "https://github.com/example/tool",
        }
        self.assertEqual(
            primary_url({**links, "category": "SaaS"}),
            "https://example.com/tool",
        )
        self.assertEqual(
            primary_url({**links, "category": "Misc"}),
            "https://github.com/example/tool",
        )

    def test_hosted_tool_without_repository_does_not_show_unknown_badge(self) -> None:
        card = tool_card(
            {
                "slug": "hosted",
                "name": "Hosted tool",
                "description": "A hosted tool without a repository",
                "website": "https://example.com/hosted",
                "category": "SaaS",
            },
            self.REFERENCE_TIME,
            1,
        )

        self.assertNotIn('class="status status--unknown"', card)
        self.assertNotIn('class="tool-meta"', card)
        self.assertEqual(
            primary_url({
                "website": "https://example.com/hosted",
                "category": "SaaS",
            }),
            "https://example.com/hosted",
        )

    def test_tool_title_can_include_a_local_type_icon(self) -> None:
        card = tool_card(
            {
                "slug": "plugin",
                "name": "IDE plugin",
                "description": "An IDE plugin",
                "repository": "https://github.com/example/plugin",
                "category": "Misc",
                "title_icon": "assets/tool-icons/plugin.png",
                "title_icon_label": "IDE plugin",
            },
            self.REFERENCE_TIME,
            1,
        )

        self.assertIn(
            '<img class="tool-title-icon" src="assets/tool-icons/plugin.png" '
            'alt="IDE plugin" title="IDE plugin">',
            card,
        )

    def test_tool_card_formats_latest_release_and_resource_links(self) -> None:
        card = tool_card(
            {
                "slug": "released",
                "name": "Released tool",
                "description": "A tool with a long release name",
                "repository": "https://github.com/example/released",
                "latest_release_tag": "2026.07.17-beta-release-with-a-long-name",
                "latest_release_url": "https://github.com/example/released/releases/tag/2026.07.17-beta",
                "category": "Misc",
            },
            self.REFERENCE_TIME,
            1,
        )

        self.assertIn('<dt><span aria-hidden="true">⭐</span> Stars</dt>', card)
        self.assertIn(
            '<dd title="2026.07.17-beta-release-with-a-long-name">'
            "2026.07.17-beta-release-with-a-long-name</dd>",
            card,
        )
        self.assertIn(">Source<span", card)
        self.assertNotIn(">Release<span", card)

    def test_release_link_remains_available_without_a_source_repository(self) -> None:
        card = tool_card(
            {
                "slug": "release-only",
                "name": "Release-only tool",
                "description": "A tool whose release is its only resource",
                "latest_release_url": "https://example.com/releases/1.0.0",
                "category": "Misc",
            },
            self.REFERENCE_TIME,
            1,
        )

        self.assertIn(">Release<span", card)

    def test_missing_latest_release_uses_a_dash(self) -> None:
        card = tool_card(
            {
                "slug": "unreleased",
                "name": "Unreleased tool",
                "description": "A tool without release data",
                "category": "Misc",
            },
            self.REFERENCE_TIME,
            1,
        )

        self.assertIn('<dt>Latest</dt><dd title="-">-</dd>', card)

    def test_tool_card_labels_commit_and_release_dates_explicitly(self) -> None:
        card = tool_card(
            {
                "slug": "dated",
                "name": "Dated tool",
                "description": "A tool with activity metadata",
                "repository": "https://github.com/example/dated",
                "category": "Misc",
                "repo_updated_at": "2026-08-05T12:00:00Z",
                "latest_release_tag": "v1.2.3",
                "latest_release_published_at": "2026-07-20T12:00:00Z",
            },
            self.REFERENCE_TIME,
            1,
        )

        self.assertIn("<dt>Last commit</dt><dd>05.08.26</dd>", card)
        self.assertIn("<dt>Last release</dt><dd>20.07.26</dd>", card)

    def test_generator_only_replaces_its_own_non_empty_output_directory(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory) / "site"
            output.mkdir()
            (output / "user-file.txt").write_text("keep", encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "Refusing to replace"):
                build_site(output, reference_time=self.REFERENCE_TIME)
            self.assertEqual((output / "user-file.txt").read_text(encoding="utf-8"), "keep")

            (output / BUILD_MARKER).write_text("generated", encoding="utf-8")
            build_site(output, reference_time=self.REFERENCE_TIME)
            self.assertFalse((output / "user-file.txt").exists())
            self.assertTrue((output / "index.html").is_file())


if __name__ == "__main__":
    unittest.main()
