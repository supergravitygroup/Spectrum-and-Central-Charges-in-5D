"""Compare exact source and collected 48-component graded Euler operators.

FC10-FC13 explain the frame, degree bound and restoration of general g,x.
This component check supplements those explicit covariant derivations.
"""

import sympy as sp

from src.fermion_operator import bilinear_matrices, FIELD_COMPONENTS
from src.reporting import OUTPUTS, write_json

GROUP_NAMES = [
    "Weyl", "LOG29to62", "LOG315plus", "implicitSigmaL", "implicitN", "candidate",
]


def evaluate_graded_operators():
    """B(s)-B(4-s)^T is the Grassmann Euler matrix with the AdS measure."""
    bilinears = {s: bilinear_matrices(s) for s in range(5)}
    reports, operators = [], []
    for exponent in range(5):
        right = bilinears[exponent]
        adjoint = bilinears[4 - exponent]
        graded = {name: right[name] - adjoint[name].T for name in right}
        difference = graded["total"] - graded["candidate"]
        residuals = [sp.simplify(entry) for entry in difference.flat]
        nonzero = [(i, str(value)) for i, value in enumerate(residuals) if value != 0]
        if nonzero:
            raise AssertionError((exponent, nonzero[:10]))
        reports.append({"radial_exponent": exponent, "exact_zero_entries": len(residuals)})
        operators.append(graded)
        print(f"PASS exact 48 x 48 graded kernel at exponent {exponent}", flush=True)
    return reports, operators


def interpolate_component_groups(operators):
    """Interpolate at four values; check each individual group at the fifth."""
    radial_variable = sp.Symbol("s")
    groups = {}
    for row in range(FIELD_COMPONENTS):
        for column in range(FIELD_COMPONENTS):
            polynomials = []
            for name in GROUP_NAMES:
                samples = [(s, operators[s][name][row, column]) for s in range(4)]
                polynomial = sp.expand(sp.interpolate(samples, radial_variable))
                fifth_residual = polynomial.subs(radial_variable, 4) - operators[4][name][row, column]
                if sp.expand(fifth_residual) != 0:
                    raise AssertionError((name, row, column, "degree bound"))
                polynomials.append(polynomial)
            if not any(value != 0 for value in polynomials):
                continue
            if sp.expand(sum(polynomials[:-1]) - polynomials[-1]) != 0:
                raise AssertionError((row, column, "source collection"))
            key = tuple(str(value) for value in polynomials)
            groups.setdefault(key, []).append((row, column))
    return groups


def write_component_table(groups):
    lines = [
        "# Fermionic component coefficient sums", "",
        "Every nonzero coefficient pattern of the 48-component graded Euler operator is listed below. "
        "The first five columns are independent source groups; their sum is the sixth. "
        "Unlisted entries vanish in all groups. See [FC10–FC13](../../details/fermionic_reduction.md) "
        "for the covariant interpretation and restoration of general parameters.", "",
        r"Let $`s=z\partial_z`$. Components 0–39 are $`\Psi_a^i`$ in five blocks of eight, "
        r"ordered $`(i=1,\alpha=0,1,2,3;i=2,\alpha=0,1,2,3)`$. Components 40–47 are $`\zeta^i`$. "
        "The row is the left variation and the column is the field.", "",
        "| Entries | Weyl | LOG 29–62 | LOG 315–827 | Implicit sigma/L | Implicit N | Collected |",
        "|---|---|---|---|---|---|---|",
    ]
    for polynomials, entries in groups.items():
        labels = ", ".join(f"({row},{column})" for row, column in entries)
        values = " | ".join(f"$`{sp.latex(sp.sympify(value))}`$" for value in polynomials)
        lines.append(f"| {labels} | {values} |")
    lines.extend([
        "", "Each group is interpolated from four exponents and checked at a fifth. "
        "The cubic and quadratic powers cancel in the sum. "
        "This is a local operator check; boundary conditions are not selected.", "",
    ])
    (OUTPUTS / "fermion_component_sums.md").write_text("\n".join(lines), encoding="utf-8")


def main():
    reports, operators = evaluate_graded_operators()
    groups = interpolate_component_groups(operators)
    write_json("fermion_operator.json", {
        "status": "PASS_SCOPED_FERMION_OPERATOR",
        "frame": "AdS5 Poincare orthonormal frame, curvature k=-1",
        "sample": "g=1,x=sqrt(2),m=1/2,u=3; homogeneous radial jets",
        "operation": "graded transpose with measure z^-5; (z*d_z)^adjoint=4-z*d_z",
        "polynomial_degree_at_most": 3,
        "checks": reports,
        "interpretation": "bulk quadratic Euler representative after source collection; not global boundary norm",
        "source_action": "GB-FINAL-DENSITY only",
    })
    write_json("fermion_component_groups.json", {
        "basis": "components 0..39: Psi_a, a=0..4, within block (i=1 spinor0..3,i=2 spinor0..3); 40..47: zeta; upper doublets",
        "radial_variable": "s=z*d_z",
        "groups": [{"entries": entries, "polynomials": list(values)} for values, entries in groups.items()],
    })
    write_component_table(groups)
    nonzero_entries = sum(len(entries) for entries in groups.values())
    print(f"Fermion operator: {len(groups)} patterns, {nonzero_entries} nonzero matrix entries.", flush=True)


if __name__ == "__main__":
    main()
