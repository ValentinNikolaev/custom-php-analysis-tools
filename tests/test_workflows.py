from __future__ import annotations

import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class WorkflowTests(unittest.TestCase):
    def test_pages_workflow_is_reusable_without_unconditional_update_trigger(self) -> None:
        workflow = (ROOT / ".github" / "workflows" / "pages.yml").read_text(encoding="utf-8")

        self.assertIn("  workflow_call:", workflow)
        self.assertIn("  workflow_dispatch:", workflow)
        self.assertNotIn("  workflow_run:", workflow)
        self.assertIn("      deploy:", workflow)
        self.assertIn("ref: ${{ inputs.ref || github.sha }}", workflow)
        self.assertIn("if: github.event_name != 'workflow_call' || inputs.deploy", workflow)
        self.assertIn("uses: actions/upload-pages-artifact@v4", workflow)
        self.assertIn("uses: actions/deploy-pages@v4", workflow)

    def test_catalog_workflow_deploys_only_after_a_commit(self) -> None:
        workflow = (ROOT / ".github" / "workflows" / "update-catalog.yml").read_text(encoding="utf-8")

        self.assertIn("catalog_changed: ${{ steps.publish.outputs.changed }}", workflow)
        self.assertIn("if: needs.update.outputs.catalog_changed == 'true'", workflow)
        self.assertIn("uses: ./.github/workflows/pages.yml", workflow)
        self.assertIn("      deploy: true", workflow)
        self.assertIn("      ref: master", workflow)
        self.assertIn('echo "changed=${changed}" >> "$GITHUB_OUTPUT"', workflow)

    def test_pull_requests_invoke_the_reusable_pages_build_without_deploying(self) -> None:
        workflow = (ROOT / ".github" / "workflows" / "pages-smoke.yml").read_text(encoding="utf-8")

        self.assertIn("  pull_request:", workflow)
        self.assertIn("uses: ./.github/workflows/pages.yml", workflow)
        self.assertIn("      deploy: false", workflow)
        self.assertIn("      ref: ${{ github.sha }}", workflow)


if __name__ == "__main__":
    unittest.main()
