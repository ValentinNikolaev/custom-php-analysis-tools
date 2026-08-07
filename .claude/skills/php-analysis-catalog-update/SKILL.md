---
name: php-analysis-catalog-update
description: Refresh the PHP static-analysis catalog YAML metadata from public GitHub and Packagist sources. Use when updating stars, repository updated_at timestamps, package links, descriptions, or candidate tool metadata in this repository.
---

<!-- Generated from .codex/skills/php-analysis-catalog-update/SKILL.md; do not edit directly. -->

# PHP Analysis Catalog Update

Use deterministic scripts; do not rewrite catalog entries by hand unless fixing a specific bad field.

## Workflow

1. Run `python scripts/update_catalog.py`.
2. The scheduled workflow runs every 6 hours. Successful GitHub repository and release checks stay fresh for 24 hours, so intermediate runs only retry stale or failed sources. If a local unauthenticated run reaches the GitHub rate limit, rerun later or use `GITHUB_TOKEN`.
3. For candidate discovery, run `python scripts/discover_tools.py --write --limit 5`; review `common/candidates/*.yaml` before promoting anything into `common/catalog`.
4. Run `python scripts/generate_editor_choice.py` and `python scripts/generate_readme.py` after metadata changes.

## Notes

- `common/catalog/*.yaml` is the source of truth.
- `repo_updated_at` comes from GitHub repository `pushed_at`/`updated_at`.
- `metadata_updated_at` records when this repository last fetched metadata.
- Discovery intentionally writes review candidates outside the published catalog.
