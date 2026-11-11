"""Nine BF contributions, with all coefficients propagated from FM01–04.

The contraction templates are hand-derived index/Grassmann contractions, not
precomputed output coefficients. Independent reference checks validate their
transcription and finite Grassmann realization. Derivative order is untouched.
"""
from fractions import Fraction
import json
import re
from calculations.linear_multiplet import ROOT
from src.expressions import Coefficient, clean

# (source slot, real rational magnitude, power of i)
INSERTIONS = {
    "sigma_N": ("N", "1", False),
    "C_E": ("E", "1", False),
    "dilatino": ("phi", "1", True),
    "gravitino": ("phi", "1/2", False),
    "C_gravitino": ("phi", "1/2", True),
    "Y": ("L", "1/4", True),
    "gravitino_dilatino": ("L", "-1/2", False),
    "two_gravitinos": ("L", "1/4", True),
    "C_two_gravitinos": ("L", "1/4", False),
}


def assemble(multiplet, gauged=False):
    templates = json.loads((ROOT / "inputs/contractions.json").read_text())
    blocks = {}
    for name, (slot, value, imaginary) in INSERTIONS.items():
        factor = Coefficient(Fraction(value), imaginary)
        if name == "sigma_N":
            bodies = [r"\sigma" + body for _, body in multiplet[slot]]
        elif name == "C_E":
            bodies = ["C_a" + body for _, body in multiplet[slot]]
        else:
            bodies = templates["blocks"][name]
        if len(bodies) != len(multiplet[slot]):
            raise ValueError(f"{name}: contraction/map term count mismatch")
        blocks[name] = [
            [(coefficient * factor).record(), clean(body)]
            for (coefficient, _), body in zip(multiplet[slot], bodies)
        ]
    if gauged:
        # Y^{ij} = i/(4 sigma) bar(psi^i) psi^j - g/(2 sigma) L_c^{ij}.
        factor = Coefficient(Fraction(-1, 2))
        blocks["Y"].extend([
            [(coefficient * factor).record(), clean(body)]
            for (coefficient, _), body in zip(
                multiplet["L"], templates["gauged_Y_additions"], strict=True
            )
        ])
    return {"order": list(INSERTIONS), "blocks": blocks}


def markdown_math(body):
    """Render internal compact tokens as standard TeX control words."""
    names = {
        "widehatR": r"\widehat{R}", "widehatC": r"\widehat{C}",
        "mathcalD": r"\mathcal{D}", "chiT": r"\chi T", "chiD": r"\chi D",
        "sigmaT": r"\sigma T", "sigmaD": r"\sigma D", "sigmaDT": r"\sigma D T",
    }
    return re.sub(r"\\([A-Za-z]+)", lambda m: names.get(m.group(1), m.group(0)), body)


def write_action(result, name):
    output = ROOT / "outputs" / f"{name}_action"
    output.with_suffix(".json").write_text(json.dumps(result, indent=2) + "\n")
    text = [
        f"# {name.capitalize()} Weyl density\n",
        "Recomputed exact coefficients from FM01–04 and the nine BF insertions. "
        "Full covariants and their implicit fermions are retained. "
        "This working action is not an independent multiplet-closure certificate.\n",
    ]
    for block in result["order"]:
        text.append(f"## {block}\n")
        rows = []
        for (value, imaginary), body in result["blocks"][block]:
            coefficient = Coefficient(Fraction(value), bool(imaginary))
            rows.append("&" + coefficient.latex() + markdown_math(body))
        text.append("```math\n\\begin{aligned}\n" + "\\\\\n".join(rows)
                    + "\n\\end{aligned}\n```\n")
    output.with_suffix(".md").write_text("\n".join(text))
