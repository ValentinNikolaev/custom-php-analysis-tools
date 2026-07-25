from __future__ import annotations

import argparse

from catalog_lib import (
    ROOT,
    cli_token,
    github_repo_key,
    http_json,
    load_catalog,
    now_iso,
    slugify,
)


QUERIES = [
    "topic:php topic:static-analysis stars:>50",
    "topic:php topic:code-quality stars:>100",
    "php static analysis language:PHP stars:>100",
    "php code quality language:PHP stars:>100",
]


def main() -> None:
    parser = argparse.ArgumentParser(description="Discover candidate PHP analysis tools from public GitHub search.")
    parser.add_argument("--write", action="store_true", help="Write new candidates into common/candidates for review.")
    parser.add_argument("--promote", action="store_true", help="Write candidates directly into common/catalog.")
    parser.add_argument("--limit", type=int, default=10)
    args = parser.parse_args()

    known = {github_repo_key(tool.get("repository")) for tool in load_catalog()}
    known.discard(None)
    token = cli_token()
    candidates = []
    skipped_known = 0
    for query in QUERIES:
        print(f"Searching GitHub: {query}")
        url = "https://api.github.com/search/repositories?q=" + query.replace(" ", "+") + "&sort=stars&order=desc&per_page=10"
        search = http_json(url, token=token)
        print(f"  GitHub reported {search.get('total_count', 0)} matches; inspecting top {len(search.get('items', []))}")
        for repo in search.get("items", []):
            repo_key = repo.get("full_name")
            if repo_key in known:
                skipped_known += 1
                print(f"  known: {repo_key}")
                continue
            candidates.append(repo)
            known.add(repo_key)
            print(
                "  found: "
                f"{repo_key} | stars={repo.get('stargazers_count') or 0} | "
                f"updated={repo.get('pushed_at') or repo.get('updated_at')} | "
                f"topics={','.join(repo.get('topics') or [])}"
            )
            if len(candidates) >= args.limit:
                break
        if len(candidates) >= args.limit:
            break

    if not candidates:
        print(f"No new candidates found; skipped {skipped_known} already-known repositories")
        return

    output_dir = ROOT / "common" / ("catalog" if args.promote else "candidates")
    output_dir.mkdir(parents=True, exist_ok=True)
    for repo in candidates:
        tool = {
            "slug": slugify(repo["name"]),
            "name": repo["name"],
            "category": "Bugs finders",
            "description": repo.get("description") or "Discovered PHP analysis candidate.",
            "website": repo.get("homepage") or repo["html_url"],
            "public_url": repo.get("homepage") or repo["html_url"],
            "website_status": "unknown",
            "website_status_code": 0,
            "website_checked_at": None,
            "website_error": "",
            "repository": repo["html_url"],
            "packagist": None,
            "latest_version": "",
            "latest_version_released_at": None,
            "stars": repo.get("stargazers_count") or 0,
            "repo_updated_at": repo.get("pushed_at") or repo.get("updated_at"),
            "metadata_updated_at": now_iso(),
            "editor_choice": False,
            "quality_tags": sorted(set(repo.get("topics") or []) & {"php", "static-analysis", "code-quality", "security"}),
            "source": "github-search",
            "notes": "Review category and description before promoting.",
        }
        if args.write or args.promote:
            from catalog_lib import dump_yaml

            (output_dir / f"{tool['slug']}.yaml").write_text(dump_yaml(tool), encoding="utf-8")
        print(
            f"{'wrote' if args.write or args.promote else 'candidate'}: "
            f"{tool['name']} | {tool['repository']} | stars={tool['stars']} | file={output_dir / (tool['slug'] + '.yaml')}"
        )
    print(f"Discovery summary: {len(candidates)} candidates, {skipped_known} already-known repositories skipped")


if __name__ == "__main__":
    main()
