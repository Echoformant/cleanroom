#!/usr/bin/env bash
set -euo pipefail

# Serve interface/reports so the dashboard can fetch JSON files.
cd "$(dirname "$0")/.."
python3 -m http.server 8000
