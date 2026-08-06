---
name: php-analysis-catalog-generate
description: Generate README.md and EDITOR-CHOISE.md from common/catalog YAML files for the PHP static-analysis tools catalog. Use when Markdown outputs are stale or catalog entries have changed.
---

<!-- Generated from .codex/skills/php-analysis-catalog-generate/SKILL.md; do not edit directly. -->

# PHP Analysis Catalog Generate

Generate docs from YAML only. Avoid editing generated Markdown directly unless repairing generator output.

## Workflow

1. Run `python scripts/generate_editor_choice.py`.
2. Run `python scripts/generate_readme.py`.
3. Inspect `git diff -- README.md EDITOR-CHOISE.md common/editor-choice.yaml`.
4. If the selection looks wrong, adjust `TARGETS` or scoring in `scripts/generate_editor_choice.py`, then regenerate.

## Output Rules

- `README.md` shows editors' choice and the full catalog grouped by category.
- `EDITOR-CHOISE.md` is deterministic and does not call an LLM or external model API.
- Keep `EDITOR-CHOISE.md` spelling for backward compatibility with the existing repo.
