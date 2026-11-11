"""SC7-50–52: insert the computed multiplet into the retained-order BF density."""
import json
import re
from src.algebra import ROOT, gauged_algebra
from src.polynomials import encode

# Each operator fixes the contraction, including lowering L_ij with the declared
# right-lowering convention. External gravitini contribute to the degree limit.
DENSITY_OPERATORS = (
    ("N", "N_log", (1, 0), 0),
    ("L", "g L_c^{ij} L_log_ij", ("-1/2", 0), 0),
    ("E", "C_a E_log^a", (1, 0), 0),
    ("phi", "bar(psi_a) gamma^a phi_log", ("1/2", 0), 1),
    ("phi", "C_a bar(psi_b) gamma^{ba} phi_log", (0, "1/2"), 1),
    ("L", "bar(psi_a^i) gamma^{ab} psi_b^j L_log_ij", (0, "1/4"), 2),
    ("L", "C_a bar(psi_b^i) gamma^{abc} psi_c^j L_log_ij", ("1/4", 0), 2),
)


def displayed_body(body):
    for old, new in (
        (r"\widehat F", r"\widehat G"), (r"\rho", r"\sigma"),
        (r"\lambda", r"\psi"), ("R(M)", r"\widehat C"),
        ("R(Q)", r"\widehat R(Q)"), ("R(V)", r"\widehat R(V)"),
        (r"\Box ", r"\Box^c "),
    ):
        body = body.replace(old, new)
    return re.sub(r"g{2,}", lambda match: "g^{" + str(len(match[0])) + "}", body)


def density_blocks(multiplet):
    """Apply the physical fermion budget, then multiply exact BF coefficients."""
    algebra = gauged_algebra()
    blocks = []
    for slot, contraction, coefficient, external_degree in DENSITY_OPERATORS:
        component = algebra.p.retained(multiplet[slot], 2 - external_degree)
        factor = algebra.b.C(*(algebra.b.Q(value) for value in coefficient))
        blocks.append({
            "slot": slot,
            "contraction": contraction,
            "external_fermion_degree": external_degree,
            "terms_with_density_coefficient": encode(factor * component),
        })
    return blocks


def write_density(multiplet):
    algebra = gauged_algebra()
    (ROOT / "outputs/bf_density.json").write_text(json.dumps({
        "representation": "seven explicit contraction operators acting on computed slot tensors",
        "scope": "full supercovariants retained; through two physical fermions",
        "global_physical_fermion_projection": 2,
        "projection_note": (
            "The code filters explicit field parity. Implicit fermions in full "
            "supercovariants remain subject to the displayed global degree <= 2 "
            "projection when those covariants are expanded."
        ),
        "blocks": density_blocks(multiplet),
    }, ensure_ascii=False) + "\n")

    labels = {"L": r"L_{\log}^{ij}", "phi": r"\varphi_{\log}^{i}",
              "N": r"N_{\log}", "E": r"E_{\log}^{a}"}
    sections = [
        "# Recomputed LOG multiplet and BF density\n",
        "The full-primary descent supplies these component polynomials. "
        "Ordered derivatives are full supercovariant operators. "
        "Even slots retain degrees 0 and 2; the spinor retains degree 1.\n",
    ]
    for slot, polynomial in multiplet.items():
        for (power, degree), rows in sorted(algebra.q.grouped(polynomial, slot).items()):
            if power != 0:
                raise AssertionError("An unfixed scalar power survived gauge evaluation")
            sections.append(f"## {slot}: {degree} explicit fermions\n")
            for start in range(0, len(rows), 24):
                lines = []
                for offset, (coefficient, body) in enumerate(rows[start:start + 24]):
                    prefix = labels[slot] + f"[{degree}]={{}}&" if start == offset == 0 else "&"
                    lines.append(prefix + algebra.p.texcoef(coefficient) + displayed_body(body))
                sections.append("```math\n\\begin{aligned}\n" + "\\\\\n".join(lines)
                                + "\n\\end{aligned}\n```\n")
    sections.append(r"""
## Density insertion

The JSON output applies these seven operators term by term, including each
coefficient and the external-fermion degree. It keeps the contractions explicit;
it does not claim a further primitive-field expansion of the supercovariants.

```math
\begin{aligned}
e^{-1}\mathcal L_{\log}=\big[&
N_{\log}-\frac g2L_c^{ij}L_{\log ij}+C_aE_{\log}^a
+\frac12\bar\psi_a\gamma^a\varphi_{\log}
+\frac i2C_a\bar\psi_b\gamma^{ba}\varphi_{\log}\\
&+\frac i4\bar\psi_a^i\gamma^{ab}\psi_b^jL_{\log ij}
+\frac14C_a\bar\psi_b^i\gamma^{abc}\psi_c^jL_{\log ij}
\big]_{\le2}.
\end{aligned}
```

Source: S23 (3.2), (3.27), project SC7-50–52. Implicit fermions in covariants
are retained with the same degree prescription as the accepted source.
""")
    (ROOT / "outputs/action.md").write_text("\n".join(sections))
