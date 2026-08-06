---
name: php-analysis-catalog-context
description: Use when maintaining, generating, validating, or reviewing the PHP static-analysis tools catalog.
type: project
related:
  - MEMORY.md
last_updated: 2026-08-06
---

<!-- Generated from .codex/memory/project-context.md; do not edit directly. -->

# PHP analysis catalog context

## Purpose and source of truth

- This repository is a generated catalog of PHP static-analysis, code-quality, coding-standard, metrics, refactoring, and hosted-analysis tools.
- `common/catalog/*.yaml` is the canonical catalog data. Treat `README.md` and `EDITOR-CHOISE.md` as generated outputs; change the YAML or generator scripts instead of hand-editing generated tables.
- `common/editor-choice.yaml` stores the selected tool slugs used by the generators.
- `common/candidates/*.yaml` is a review queue produced by discovery. A candidate must be reviewed before promotion into `common/catalog/`.

## Repository layout

- `scripts/catalog_lib.py` owns the small YAML reader/writer, catalog paths, category order, URL normalization, and HTTP helpers.
- `scripts/update_catalog.py` refreshes GitHub, Packagist, release, and website metadata. It accepts `GITHUB_TOKEN` or `GH_TOKEN` for GitHub API access.
- `scripts/discover_tools.py` discovers candidate repositories without automatically promoting them.
- `scripts/generate_readme.py` and `scripts/generate_editor_choice.py` produce the Markdown catalog views.
- `scripts/full_workflow.py` orchestrates import-if-missing, optional Exakat import, metadata refresh, discovery, and both generators.
- `tests/test_catalog_scripts.py` covers serialization, metadata matching, discovery, lifecycle classification, sorting, and Markdown rendering.
- `.codex/skills/` contains focused Codex workflows for updating metadata, generating Markdown, and running the complete maintenance workflow.

## Maintenance workflow

Run the complete refresh from the repository root:

```powershell
python scripts/full_workflow.py
```

Review new `common/candidates/*.yaml` files. After manually promoting or cleaning candidates, regenerate without another discovery pass:

```powershell
python scripts/full_workflow.py --skip-discovery
```

Use `python scripts/full_workflow.py --import-exakat` only when intentionally importing verified active entries from Exakat's catalog. Network-backed refreshes can change many YAML files and generated tables.

## Verification

Run tests and repository checks before handing off catalog changes:

```powershell
python -m unittest discover -s tests
git diff --check
git status --short
```

Inspect generated diffs for accidental candidate promotion, mismatched repository/package metadata, and unexpected churn. Commit or push only when explicitly requested.

## Automation

- `.github/workflows/update-catalog.yml` runs at 03:17 and 15:17 UTC and supports manual dispatch.
- The workflow uses Python 3.12, runs the unit tests, refreshes metadata, discovers up to ten candidates, regenerates both Markdown outputs, and commits changes when the working tree differs.
- The workflow has `contents: write`; changes to its commands or generated-file boundaries affect automatic commits to the checked-out branch.
