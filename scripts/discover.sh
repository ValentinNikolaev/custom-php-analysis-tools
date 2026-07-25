#!/usr/bin/env sh
set -eu

limit="${1:-10}"

cd "$(dirname "$0")/.."
python scripts/discover_tools.py --write --limit "$limit"
