---
name: php-analysis-catalog-generate
description: Generate README.md and EDITORS-CHOICE.md from common/catalog YAML files for the PHP static-analysis tools catalog. Use when Markdown outputs are stale or catalog entries have changed.
---

# PHP Analysis Catalog Generate

Generate docs from YAML only. Avoid editing generated Markdown directly unless repairing generator output.

## Workflow

1. Run `python scripts/generate_editor_choice.py`.
2. Run `python scripts/generate_readme.py`.
3. Inspect `git diff -- README.md EDITORS-CHOICE.md EDITOR-CHOISE.md common/editor-choice.yaml`.
4. If the selection looks wrong, review and edit the manually approved membership in `common/editor-choice.yaml`, its copy, and the editorial evidence; then regenerate.

## Output Rules

- `README.md` shows editors' choice and the full catalog grouped by category.
- `EDITORS-CHOICE.md` is deterministic and does not call an LLM or external model API.
- `EDITOR-CHOISE.md` remains as a compatibility redirect for the former misspelled path.
