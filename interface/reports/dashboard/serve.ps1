Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'

# Serve interface/reports so the dashboard can fetch JSON files (file:// blocks fetch() in most browsers).
Set-Location (Join-Path $PSScriptRoot '..')
python -m http.server 8000
