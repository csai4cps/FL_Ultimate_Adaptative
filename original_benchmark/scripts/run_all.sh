#!/usr/bin/env bash
set -euo pipefail
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

bash "$SCRIPT_DIR/run_onoff.sh"
bash "$SCRIPT_DIR/run_backdoor.sh"
bash "$SCRIPT_DIR/run_sybil.sh"
bash "$SCRIPT_DIR/run_model_replacement.sh"
