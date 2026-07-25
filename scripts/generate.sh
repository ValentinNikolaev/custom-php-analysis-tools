#!/usr/bin/env sh
set -eu

cd "$(dirname "$0")/.."
python scripts/generate_editor_choice.py
python scripts/generate_readme.py
