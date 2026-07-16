# GitHub Copilot CLI logging hook runner (Windows / PowerShell).
#
# Usage (from a hook definition): run-copilot-logger.ps1 <copilotEventName>
# The event payload arrives on stdin and is forwarded to log-interaction.py.
#
# This must never fail a Copilot session, so it always exits 0.

$ErrorActionPreference = 'SilentlyContinue'

$hookEvent = if ($args.Count -ge 1) { $args[0] } else { 'unknown' }
$here = Split-Path -Parent $MyInvocation.MyCommand.Path
$root = (Resolve-Path (Join-Path $here '..\..')).Path
$script = Join-Path $here 'log-interaction.py'

# Read the payload from stdin so it can be piped to whichever interpreter we pick.
$payload = [Console]::In.ReadToEnd()

# The logger is stdlib-only, so any interpreter works. Prefer the project venv,
# then a system Python, and only fall back to `uv run` last (it is slower).
$dotVenvPython = Join-Path $root '.venv\Scripts\python.exe'
$venvPython = Join-Path $root 'venv\Scripts\python.exe'

if (Test-Path $dotVenvPython) {
    $payload | & $dotVenvPython $script $hookEvent
}
elseif (Test-Path $venvPython) {
    $payload | & $venvPython $script $hookEvent
}
elseif (Get-Command python -ErrorAction SilentlyContinue) {
    $payload | & python $script $hookEvent
}
elseif (Get-Command python3 -ErrorAction SilentlyContinue) {
    $payload | & python3 $script $hookEvent
}
elseif (Get-Command uv -ErrorAction SilentlyContinue) {
    Push-Location $root
    try { $payload | & uv run python $script $hookEvent } finally { Pop-Location }
}

exit 0
