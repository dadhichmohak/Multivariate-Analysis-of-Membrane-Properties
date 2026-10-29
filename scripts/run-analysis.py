#!/usr/bin/env python3
"""Execute an external notebook copy, preserving repository sources."""
import argparse
import json
import os
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
BASE = REPO / '.local'
for name, folder in {'JUPYTER_CONFIG_DIR': 'jupyter-config', 'JUPYTER_DATA_DIR': 'jupyter-data', 'JUPYTER_RUNTIME_DIR': 'jupyter-runtime', 'IPYTHONDIR': 'ipython', 'MPLCONFIGDIR': 'matplotlib'}.items():
    location = BASE / folder
    location.mkdir(parents=True, exist_ok=True)
    os.environ[name] = str(location)
os.environ['PATH'] = str(REPO / '.venv/bin') + os.pathsep + os.environ['PATH']
os.environ['OPENBLAS_NUM_THREADS'] = '1'
os.environ['OMP_NUM_THREADS'] = '1'

os.environ['JUPYTER_PATH'] = str(REPO / '.venv/share/jupyter') + os.pathsep + os.environ.get('JUPYTER_PATH', '')

import nbformat
from nbclient import NotebookClient
from nbclient.exceptions import CellExecutionError

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('--native', action='store_true', help='Diagnose the unchanged notebook from a clean kernel (currently fails).')
args = parser.parse_args()
output_dir = REPO / 'outputs'
output_dir.mkdir(exist_ok=True)
if not args.native:
    for artifact in ['readiness.json', 'MLR_analysis.executed.ipynb', 'MLR_analysis.html']:
        (output_dir / artifact).unlink(missing_ok=True)
notebook = nbformat.read(REPO / 'MLR_analysis.ipynb', as_version=4)
for cell in notebook.cells:
    if cell.cell_type == 'code':
        cell.outputs = []
        cell.execution_count = None

if not args.native:
    bootstrap = nbformat.v4.new_code_cell(f'''# Local input adapter for this generated copy only.
# Original notebook cells below are unchanged.
import pandas as pd
from unittest.mock import patch
from pathlib import Path
from IPython import get_ipython
get_ipython().run_line_magic('matplotlib', 'inline')
_local_data = Path({str(REPO / 'PS/MembranePROB2data.txt')!r})
_read_csv_original = pd.read_csv
dataset = _read_csv_original(_local_data, sep=r'\\s+', header=None)
def _read_csv_local(path, *args, **kwargs):
    if str(path) == '/content/drive/MyDrive/new.csv':
        path = _local_data
        kwargs.setdefault('sep', r'\\s+')
    return _read_csv_original(path, *args, **kwargs)
_input_adapter = patch.object(pd, 'read_csv', _read_csv_local)
_input_adapter.start()
''')
    notebook.cells.insert(0, bootstrap)
    notebook.cells.append(nbformat.v4.new_code_cell('''# Readiness assertions for the supplied dataset and notebook calculations.
import json
from sklearn.metrics import mean_squared_error
assert dataset.shape == (120, 9), dataset.shape
assert X.shape == (120, 8), X.shape
assert np.isfinite(dataset.to_numpy()).all()
assert len(r2_scores) == len(q2_scores) == 8
assert np.isfinite(r2_scores).all() and np.isfinite(q2_scores).all()
assert len(y_pred_cv) == 120 and np.isfinite(y_pred_cv).all()
assert len(residuals) == 120 and np.isfinite(residuals).all()
assert len(fitted_vals) == 120 and np.isfinite(fitted_vals).all()
assert r2_scores[-1] > 0 and q2_scores[-1] > 0
summary = {'samples': len(y), 'predictors': X.shape[1], 'training_r2': float(r2_scores[-1]), 'five_fold_q2': float(q2_scores[-1]), 'cv_rmse': float(np.sqrt(mean_squared_error(y, y_pred_cv))), 'predictor_counts_checked': len(q2_scores)}
print('MEMBRANE_READINESS=' + json.dumps(summary))
_input_adapter.stop()
'''))

notebook.metadata.kernelspec = {'name': 'python3', 'display_name': 'Python (Membrane)', 'language': 'python'}
client = NotebookClient(notebook, timeout=180, kernel_name='python3', resources={'metadata': {'path': str(REPO)}})
target = output_dir / ('native-diagnostic.ipynb' if args.native else 'MLR_analysis.executed.ipynb')
try:
    client.execute()
except CellExecutionError as error:
    nbformat.write(notebook, target)
    (output_dir / 'native-failure.txt' if args.native else output_dir / 'adapter-failure.txt').write_text(str(error))
    print(str(error))
    print(f'Diagnostic notebook saved to {target}')
    raise SystemExit(1)
nbformat.write(notebook, target)
if not args.native:
    images = sum('image/png' in output.get('data', {}) for cell in notebook.cells for output in cell.get('outputs', []))
    assert images >= 6, f'Expected regression diagnostic and CV plots; found {images}'
    found_readiness = False
    for cell in notebook.cells:
        for output in cell.get('outputs', []):
            for line in output.get('text', '').splitlines():
                if line.startswith('MEMBRANE_READINESS='):
                    found_readiness = True
                    report = json.loads(line.removeprefix('MEMBRANE_READINESS='))
                    report['plot_outputs'] = images
                    report['executed_code_cells'] = sum(c.get('execution_count') is not None for c in notebook.cells)
                    print(json.dumps(report, indent=2))
    assert found_readiness, 'Notebook readiness assertions did not produce their report'
    from nbconvert import HTMLExporter
    html, _ = HTMLExporter().from_notebook_node(notebook)
    (output_dir / 'MLR_analysis.html').write_text(html)
    (output_dir / 'readiness.json').write_text(json.dumps(report, indent=2) + '\n')
print(f'Executed notebook saved to {target}')
