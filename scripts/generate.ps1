$ErrorActionPreference = "Stop"

$Root = Resolve-Path (Join-Path $PSScriptRoot "..")
Push-Location $Root
try {
    python scripts/generate_editor_choice.py
    python scripts/generate_readme.py
}
finally {
    Pop-Location
}
