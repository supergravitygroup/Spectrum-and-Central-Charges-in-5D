"""Small output and exact-residual helpers shared by calculation stages."""

import json
from pathlib import Path

import sympy as sp

PACKAGE = Path(__file__).resolve().parents[1]
OUTPUTS = PACKAGE / "outputs"


def write_json(filename, data):
    """Write generated data inside this package, never in the donor project."""
    OUTPUTS.mkdir(exist_ok=True)
    path = OUTPUTS / filename
    path.write_text(json.dumps(data, indent=2, default=str) + "\n", encoding="utf-8")
    return path


def check_zero(residuals, name, expression):
    """Save the evaluated residual, and stop on a nonzero expression."""
    residual = sp.factor(expression)
    residuals[name] = str(residual)
    if residual != 0:
        raise AssertionError(f"{name}: residual = {residual}")


def action_coefficients():
    """Read the regenerated action ledger, indexed by stable source IDs."""
    rows = json.loads((OUTPUTS / "action_coefficients.json").read_text())
    return {
        f"{row['source']}:{row['index']}":
        sp.Rational(row["coefficient"]) * sp.I ** row["phase_i"]
        for row in rows
    }
