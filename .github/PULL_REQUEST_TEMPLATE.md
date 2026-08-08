## Summary

Describe what changed and why.

## Change Type

- [ ] Catalog entry or metadata correction
- [ ] New tool
- [ ] Generated site or documentation
- [ ] Script, test, or workflow
- [ ] Other

## Related Issue

Closes #

## Verification

List the commands you ran and their results.

```text
python scripts/validate_catalog.py
python -m unittest discover -s tests
git diff --check
```

## Checklist

- [ ] I changed the appropriate source file under `common/` rather than only editing generated output.
- [ ] I regenerated affected files and reviewed their diff.
- [ ] I regenerated `README.md`, Editors' Choice, machine-readable exports, and the site when catalog data changed.
- [ ] New or materially changed catalog claims include primary sources and an honest `reviewed_at` date.
- [ ] I followed the inclusion, lifecycle, recommendation, and conflict rules in `EDITORIAL-POLICY.md`.
- [ ] I added or updated tests when behavior changed.
- [ ] I kept the pull request focused on one logical change.
- [ ] I did not include secrets, credentials, or private vulnerability details.
- [ ] I disclosed any affiliation with a proposed tool in the summary.
