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
    "topic:php topic:static-analysis stars:>100",
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
    for query in QUERIES:
        url = "https://api.github.com/search/repositories?q=" + query.replace(" ", "+") + "&sort=stars&order=desc&per_page=10"
        search = http_json(url, token=token)
        for repo in search.get("items", []):
            repo_key = repo.get("full_name")
            if repo_key in known:
                continue
            candidates.append(repo)
            known.add(repo_key)
            if len(candidates) >= args.limit:
                break
        if len(candidates) >= args.limit:
            break

    if not candidates:
        print("No new candidates found")
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
            "repository": repo["html_url"],
            "packagist": None,
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
        print(f"{'wrote' if args.write or args.promote else 'candidate'}: {tool['name']} - {tool['repository']}")


if __name__ == "__main__":
    main()
