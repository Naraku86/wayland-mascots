#!/usr/bin/env bash
set -euo pipefail
exec python3 scripts/embed_assets.py "${ASSETS_DIR:-assets/new}"
