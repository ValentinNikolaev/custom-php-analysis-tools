#!/usr/bin/env sh
set -eu

cd "$(dirname "$0")/.."
python scripts/update_catalog.py "$@"
