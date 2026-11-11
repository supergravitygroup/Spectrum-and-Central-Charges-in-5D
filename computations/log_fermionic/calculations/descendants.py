"""S23 (3.24)–(3.26): differentiate the full primary before retaining degree <= 2."""
from src.algebra import projection, rules

SLOTS = ("L", "phi", "N", "E")


def component_descendants(primary):
    """Return one origin's four projected, retained-order component polynomials.

    `primary` is untruncated. In particular the second spinor derivative acts
    on every higher-fermion term that can contribute to the retained result.
    The epsilon contractions fix the source-to-component normalization.
    """
    first_derivative = rules.a.deriv(primary)
    second_derivative = rules.dpoly(first_derivative, "sZ", "uT")

    source_components = {
        "L": -2 * primary,
        "phi": (
            -2 * rules.I * rules.Q(1, 3)
            * rules.eps("-uJ", "-uR") * first_derivative
        ),
        "N": -rules.trace(second_derivative),
        "E": (
            rules.I * rules.Q(1, 12)
            * rules.field("G", "+lV", "+sZ", "+sE")
            * rules.eps("-uI", "-uT")
            * rules.eps("-uJ", "-uR")
            * second_derivative
        ),
    }
    return {
        slot: projection.project(
            projection.retained(value, 1 if slot == "phi" else 2)
        )
        for slot, value in source_components.items()
    }


def build_projected_multiplet():
    """Build from the source primary; do not read checkpoints or expected data."""
    result = {slot: rules.P() for slot in SLOTS}
    origins = []
    for name, primary in rules.make_inputs().items():
        components = component_descendants(primary)
        for slot, polynomial in components.items():
            rules.check(polynomial, projection.WEIGHTS[slot], projection.FREE[slot])
            result[slot].ts.extend(polynomial.ts)
        origins.append({
            "origin": name,
            "untruncated_primary_terms": len(primary.ts),
            "projected_terms": {
                slot: len(polynomial.ts) for slot, polynomial in components.items()
            },
        })
        print(f"  primary origin {name}: differentiated and projected", flush=True)
    return result, origins
