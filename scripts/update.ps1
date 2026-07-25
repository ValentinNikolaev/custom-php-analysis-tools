$ErrorActionPreference = "Stop"

$Root = Resolve-Path (Join-Path $PSScriptRoot "..")
Push-Location $Root
try {
    python scripts/update_catalog.py @args
}
finally {
    Pop-Location
}
