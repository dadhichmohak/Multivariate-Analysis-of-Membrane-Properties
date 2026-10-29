#!/usr/bin/env bash
set -euo pipefail
repo="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$repo"
if ! command -v uv >/dev/null 2>&1; then
    echo 'Install uv first: https://docs.astral.sh/uv/getting-started/installation/' >&2
    exit 1
fi
export UV_CACHE_DIR="${UV_CACHE_DIR:-$repo/.cache/uv}"
export UV_PYTHON_INSTALL_DIR="${UV_PYTHON_INSTALL_DIR:-$repo/.cache/python}"
export IPYTHONDIR="$repo/.local/ipython"
export JUPYTER_CONFIG_DIR="$repo/.local/jupyter-config"
export JUPYTER_DATA_DIR="$repo/.local/jupyter-data"
export JUPYTER_RUNTIME_DIR="$repo/.local/jupyter-runtime"
export MPLCONFIGDIR="$repo/.local/matplotlib"
mkdir -p "$UV_CACHE_DIR" "$UV_PYTHON_INSTALL_DIR" "$IPYTHONDIR" "$JUPYTER_CONFIG_DIR" "$JUPYTER_DATA_DIR" "$JUPYTER_RUNTIME_DIR" "$MPLCONFIGDIR"
version="$(cat .python-version)"
uv python install "$version" --no-bin
if [ ! -x .venv/bin/python ]; then
    uv venv --python "$version" .venv
fi
.venv/bin/python - "$version" <<'PY'
import sys
assert '.'.join(map(str, sys.version_info[:3])) == sys.argv[1], 'Existing .venv has the wrong Python version; create a fresh environment.'
PY
# Use the existing proxy and CA trust, preserving TLS and artifact-hash verification.
uv pip sync --python .venv/bin/python --require-hashes requirements.lock
.venv/bin/python -m ipykernel install --sys-prefix --name python3 --display-name 'Python (Membrane)'
uv pip check --python .venv/bin/python
printf '\nSetup complete. Run: .venv/bin/python scripts/run-analysis.py\n'
