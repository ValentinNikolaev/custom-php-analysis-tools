from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def run(args: list[str]) -> None:
    print("+", " ".join(args))
    subprocess.run(args, cwd=ROOT, check=True)


def main() -> None:
    parser = argparse.ArgumentParser(description="Refresh catalog metadata, discover candidates, and regenerate Markdown files.")
    parser.add_argument("--skip-discovery", action="store_true")
    parser.add_argument("--discovery-limit", type=int, default=5)
    parser.add_argument("--update-limit", type=int, default=0)
    args = parser.parse_args()

    if not (ROOT / "common" / "catalog").exists():
        run([sys.executable, "scripts/import_from_readme.py"])
    update_args = [sys.executable, "scripts/update_catalog.py"]
    if args.update_limit:
        update_args.extend(["--limit", str(args.update_limit)])
    run(update_args)
    if not args.skip_discovery:
        run([sys.executable, "scripts/discover_tools.py", "--write", "--limit", str(args.discovery_limit)])
        run(update_args)
    run([sys.executable, "scripts/generate_editor_choice.py"])
    run([sys.executable, "scripts/generate_readme.py"])
    print("Workflow complete")


if __name__ == "__main__":
    main()
