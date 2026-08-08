# Machine-readable catalog

This directory contains generated, versioned exports of the canonical records
in `common/catalog/*.yaml`:

- `catalog.json` preserves the complete records and adds derived lifecycle and
  reader-facing category fields;
- `catalog.csv` provides a flat interoperability view, using `|` between values
  in list fields; and
- `build-manifest.json` records the schema version, source commit, snapshot
  timestamp, and artifact names.

Regenerate the files with:

```shell
python scripts/validate_catalog.py
python scripts/generate_exports.py --as-of 2026-08-08
```

Use an ISO-8601 `--as-of` value or `SOURCE_DATE_EPOCH` for reproducible derived
lifecycle fields. Catalog data is licensed under CC BY 4.0; see
[`DATA-LICENSE.md`](../DATA-LICENSE.md) for attribution guidance.
