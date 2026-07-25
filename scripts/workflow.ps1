param(
    [switch] $SkipDiscovery,
    [int] $DiscoveryLimit = 5,
    [int] $UpdateLimit = 0
)

$ErrorActionPreference = "Stop"

$Root = Resolve-Path (Join-Path $PSScriptRoot "..")
Push-Location $Root
try {
    $commandArgs = @("scripts/full_workflow.py", "--discovery-limit", "$DiscoveryLimit")
    if ($SkipDiscovery) {
        $commandArgs += "--skip-discovery"
    }
    if ($UpdateLimit -gt 0) {
        $commandArgs += @("--update-limit", "$UpdateLimit")
    }
    python @commandArgs
}
finally {
    Pop-Location
}
