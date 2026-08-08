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
    parser = argparse.ArgumentParser(
        description="Refresh, validate, and regenerate the PHP analysis tools catalog."
    )
    parser.add_argument("--skip-discovery", action="store_true")
    parser.add_argument("--skip-update", action="store_true")
    parser.add_argument("--skip-tests", action="store_true")
    parser.add_argument("--import-exakat", action="store_true", help="Import verified active tools from Exakat's catalog.")
    parser.add_argument("--discovery-limit", type=int, default=5)
    parser.add_argument("--update-limit", type=int, default=0)
    parser.add_argument("--as-of", help="ISO-8601 date passed to deterministic generators")
    args = parser.parse_args()

    if not (ROOT / "common" / "catalog").exists():
        run([sys.executable, "scripts/import_from_readme.py"])
    if args.import_exakat:
        run([sys.executable, "scripts/import_exakat_catalog.py", "--write"])
    update_args = [sys.executable, "scripts/update_catalog.py"]
    if args.update_limit:
        update_args.extend(["--limit", str(args.update_limit)])
    if not args.skip_update:
        run(update_args)
    if not args.skip_discovery:
        run([sys.executable, "scripts/discover_tools.py", "--write", "--limit", str(args.discovery_limit)])
    run([sys.executable, "scripts/validate_catalog.py"])
    generator_suffix = ["--as-of", args.as_of] if args.as_of else []
    run([sys.executable, "scripts/generate_editor_choice.py", *generator_suffix])
    run([sys.executable, "scripts/generate_readme.py", *generator_suffix])
    run([sys.executable, "scripts/generate_exports.py", *generator_suffix])
    run([sys.executable, "scripts/generate_site.py", "--output", "site-dist", *generator_suffix])
    run([sys.executable, "scripts/validate_catalog.py"])
    if not args.skip_tests:
        run([sys.executable, "-m", "unittest", "discover", "-s", "tests"])
    print("Workflow complete")


if __name__ == "__main__":
    main()
