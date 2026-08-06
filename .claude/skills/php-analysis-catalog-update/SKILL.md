---
name: php-analysis-catalog-update
description: Refresh the PHP static-analysis catalog YAML metadata from public GitHub and Packagist sources. Use when updating stars, repository updated_at timestamps, package links, descriptions, or candidate tool metadata in this repository.
---

<!-- Generated from .codex/skills/php-analysis-catalog-update/SKILL.md; do not edit directly. -->

# PHP Analysis Catalog Update

Use deterministic scripts; do not rewrite catalog entries by hand unless fixing a specific bad field.

## Workflow

1. Run `python scripts/update_catalog.py`.
2. If GitHub rate limit is tight, rerun later or use `GITHUB_TOKEN`; the script skips entries refreshed in the last 20 hours.
3. For candidate discovery, run `python scripts/discover_tools.py --write --limit 5`; review `common/candidates/*.yaml` before promoting anything into `common/catalog`.
4. Run `python scripts/generate_editor_choice.py` and `python scripts/generate_readme.py` after metadata changes.

## Notes

- `common/catalog/*.yaml` is the source of truth.
- `repo_updated_at` comes from GitHub repository `pushed_at`/`updated_at`.
- `metadata_updated_at` records when this repository last fetched metadata.
- Discovery intentionally writes review candidates outside the published catalog.
