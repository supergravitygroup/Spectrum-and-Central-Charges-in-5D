"""Paths, exact scalar symbols and output helpers shared by the calculation."""
from pathlib import Path
import json
import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "outputs"
REFERENCE = ROOT / "inputs/reference"
ACTION_DIR = REFERENCE / "results/gauged_two_derivative_fermionic_action"
L = sp.Symbol("L", positive=True)
N, g, k = sp.symbols("N g k", real=True)
SYMBOLS = {"L": L, "N": N, "g": g, "k": k, "I": sp.I}


def expression(text):
    return sp.sympify(text, locals=SYMBOLS)


def read_json(path):
    return json.loads(path.read_text())


def write_json(path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")


def matrix_data(matrix):
    return [[str(sp.factor(value)) for value in matrix.row(i)] for i in range(matrix.rows)]


def equal(actual, expected, label):
    values = actual - expected
    if not isinstance(values, sp.MatrixBase):
        values = [values]
    if any(sp.simplify(value) != 0 for value in values):
        raise AssertionError(label)
