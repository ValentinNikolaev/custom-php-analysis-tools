---
name: php-analysis-catalog-workflow
description: "Run the full low-token PHP analysis catalog maintenance workflow: import catalog if missing, refresh metadata, discover candidates, regenerate Markdown files, validate, then commit and push changes."
---

<!-- Generated from .codex/skills/php-analysis-catalog-workflow/SKILL.md; do not edit directly. -->

# PHP Analysis Catalog Workflow

Prefer this skill when the user asks for the complete daily/update workflow.

## Workflow

1. Run `python scripts/full_workflow.py`.
2. Review `common/candidates/*.yaml`; promote only relevant tools into `common/catalog/*.yaml`.
3. Run `python scripts/full_workflow.py --skip-discovery` after any manual promotion or cleanup.
4. Validate with `git diff --check` and `git status --short`.
5. Commit and push when requested by the user or by the workflow instruction.

## Daily Automation

`.github/workflows/update-catalog.yml` runs every six hours at minute 17 and also supports manual `workflow_dispatch`. Successful GitHub metadata remains fresh for 24 hours, so intermediate runs primarily retry stale or previously failed entries. The workflow commits changes only when generated files or catalog data differ.

## Token Budget

Use scripts as the source of execution truth. Do not paste catalog contents into the conversation; inspect specific YAML files only when diagnosing bad metadata or promoting candidates.
