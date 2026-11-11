"""Insert gauged composites, take ordered derivatives, then evaluate the gauge."""
from src.algebra import gauged_algebra


def substitute_and_collect(polynomial, slot):
    algebra = gauged_algebra()
    substituted = algebra.substitute(polynomial, 1 if slot == "phi" else 2)
    algebra.b.check(substituted, algebra.p.WEIGHTS[slot], algebra.p.FREE[slot])
    at_gauge = algebra.gauge_values(substituted)
    result, details = algebra.canonical(at_gauge, slot)
    degrees = algebra.audit(result, slot)
    again, _ = algebra.canonical(result, slot, "-idempotence")
    residual, _ = algebra.canonical(result - again, slot, "-residual")
    if residual.ts:
        raise AssertionError(f"{slot}: canonicalization is not idempotent")
    return result, {
        "substituted_terms": len(substituted.ts),
        "gauge_terms": len(at_gauge.ts),
        "canonical_terms": len(result.ts),
        "fermion_degrees": degrees,
        "idempotence_residual": 0,
        **details,
    }
