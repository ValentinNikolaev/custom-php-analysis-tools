# Scripts

Simple wrappers:

| Script | Purpose |
|---|---|
| `update.ps1` / `update.sh` | Refresh GitHub, Packagist, and public URL metadata. |
| `discover.ps1` / `discover.sh` | Search GitHub for candidate tools and write them to `common/candidates`. |
| `generate.ps1` / `generate.sh` | Regenerate `EDITOR-CHOISE.md` and `README.md` from catalog YAML. |
| `workflow.ps1` / `workflow.sh` | Run the complete catalog workflow. |

Examples:

```powershell
./scripts/update.ps1
./scripts/discover.ps1 -Limit 20
./scripts/generate.ps1
./scripts/workflow.ps1 -SkipDiscovery
```

```bash
./scripts/update.sh
./scripts/discover.sh 20
./scripts/generate.sh
./scripts/workflow.sh --skip-discovery
```
