"""02. Insert the effective vector into the seven BF contractions, note05 (5.1).

The ordinary field-strength representative is used after the cancellation in
(4.49). No auxiliary equation of the target theory is imposed.
"""
import sympy as sp
from src.common import ROOT, OUTPUT, L, N, g, expression, read_json, write_json
from src.ordered_density import Term, multiply, collect

DISPLAY = {
    "trace_Y_linear": r"\delta^{ij}Y_{\mathrm{linear}\,ij}",
    "bar_lambda_varphi": r"\bar\lambda_{\mathrm{linear}}{}^i\varphi_i",
    "psi_gamma_lambda": r"\delta_{ij}\bar\psi_a{}^i\gamma^a\lambda_{\mathrm{linear}}{}^j",
    "F_linear": r"F_{\mathrm{linear}\,\mu\nu}", "E2": r"E^{\mu\nu}",
    "G": r"G_{\mu\nu}",
    "varphi_bilinear": r"\delta_{ij}\bar\varphi^i\varphi^j",
    "psi_gamma_varphi": r"\bar\psi_a{}^i\gamma^a\varphi_i",
    "psi_gamma2_psi": r"\delta_{ij}\bar\psi_a{}^i\gamma^{ab}\psi_b{}^j",
}


def substitutions():
    return {
        "trace_Y_eff": [Term(1, ("trace_Y_linear",)), Term(-sp.sqrt(2) * g**2 * L)],
        "F_eff": [Term(1, ("F_linear",)), Term(2 * g, ("G",))],
        "rho_eff": [
            Term(2 * N / L + 2 * g),
            Term(sp.I / (sp.sqrt(2) * L**2), ("varphi_bilinear",)),
        ],
    }


def assemble(recipe, density_factor=-2):
    maps = substitutions()
    terms = []
    for insertion in recipe:
        product = [Term(expression(insertion["coefficient"]) * density_factor)]
        for factor in insertion["factors"]:
            product = multiply(product, maps.get(factor, [Term(1, (factor,))]))
        terms.extend(product)
    return collect(terms)


def run():
    rows = assemble(read_json(ROOT / "inputs/bf_density.json"))
    data = [{"coefficient": str(row.coefficient), "factors": list(row.word),
             "explicit_degree": row.degree} for row in rows]
    write_json(OUTPUT / "bf_density.json", data)
    text = [
        "# Two-derivative action\n",
        "## Recomputed outer BF insertion\n",
        "The following terms sum to the density after effective-slot substitution. "
        "Retained Y, lambda and F components include supercovariant completions. "
        "The ordered-word calculation is not an elementary expansion of every Pauli term.\n",
    ]
    for row in rows:
        text.append("```math\n" + sp.latex(row.coefficient) + " "
                    + " ".join(DISPLAY[name] for name in row.word) + "\n```\n")
    text.append("## Component definitions\n\n"
                "The [current component action](../../../common/two_derivative_action/README.md) "
                "and [construction](../../../common/two_derivative_action/details/construction.md) "
                "give the full covariants and index conventions.\n")
    (OUTPUT / "action.md").write_text("\n".join(text))
    return data
