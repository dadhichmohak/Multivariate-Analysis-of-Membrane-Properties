#!/usr/bin/env bash
set -euo pipefail
umask 077
repo="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")/.." && pwd)"
base="$repo/.local"
export JUPYTER_CONFIG_DIR="$base/jupyter-config"
export JUPYTER_DATA_DIR="$base/jupyter-data"
export JUPYTER_RUNTIME_DIR="$base/jupyter-runtime"
export IPYTHONDIR="$base/ipython"
export MPLCONFIGDIR="$base/matplotlib"
export OPENBLAS_NUM_THREADS=1
export OMP_NUM_THREADS=1
export PATH="$repo/.venv/bin:$PATH"
export JUPYTER_PATH="$repo/.venv/share/jupyter${JUPYTER_PATH:+:$JUPYTER_PATH}"
mkdir -p "$JUPYTER_CONFIG_DIR" "$JUPYTER_DATA_DIR" "$JUPYTER_RUNTIME_DIR" "$IPYTHONDIR" "$MPLCONFIGDIR"
cd "$repo"
exec "$repo/.venv/bin/jupyter" lab --no-browser --ServerApp.ip=127.0.0.1 --ServerApp.port=8888 --ServerApp.port_retries=0 --ServerApp.root_dir="$repo" "$@"
