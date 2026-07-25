param(
    [int] $Limit = 10,
    [switch] $Promote
)

$ErrorActionPreference = "Stop"

$Root = Resolve-Path (Join-Path $PSScriptRoot "..")
Push-Location $Root
try {
    $commandArgs = @("scripts/discover_tools.py", "--write", "--limit", "$Limit")
    if ($Promote) {
        $commandArgs += "--promote"
    }
    python @commandArgs
}
finally {
    Pop-Location
}
