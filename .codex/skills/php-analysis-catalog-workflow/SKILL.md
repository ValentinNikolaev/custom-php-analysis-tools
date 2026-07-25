---
name: php-analysis-catalog-workflow
description: "Run the full low-token PHP analysis catalog maintenance workflow: import catalog if missing, refresh metadata, discover candidates, regenerate Markdown files, validate, then commit and push changes."
---

# PHP Analysis Catalog Workflow

Prefer this skill when the user asks for the complete daily/update workflow.

## Workflow

1. Run `python scripts/full_workflow.py`.
2. Review `common/candidates/*.yaml`; promote only relevant tools into `common/catalog/*.yaml`.
3. Run `python scripts/full_workflow.py --skip-discovery` after any manual promotion or cleanup.
4. Validate with `git diff --check` and `git status --short`.
5. Commit and push when requested by the user or by the workflow instruction.

## Daily Automation

`.github/workflows/update-catalog.yml` runs daily at 03:17 UTC and also supports manual `workflow_dispatch`. It commits changes only when generated files or catalog data differ.

## Token Budget

Use scripts as the source of execution truth. Do not paste catalog contents into the conversation; inspect specific YAML files only when diagnosing bad metadata or promoting candidates.
