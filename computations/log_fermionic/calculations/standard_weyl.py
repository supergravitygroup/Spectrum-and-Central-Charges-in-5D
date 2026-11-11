"""Collect dummy indices and Clifford products in the Standard-Weyl basis."""
from src.algebra import projection, reduction, rules


def canonicalize(polynomial, slot):
    rules.check(polynomial, projection.WEIGHTS[slot], projection.FREE[slot])
    tensor, tensor_zeros = reduction.collect_tensor(polynomial, slot)
    clifford, expanded, clifford_zeros = reduction.collect_clifford(tensor, slot)
    return clifford, {
        "projected_terms": len(polynomial.ts),
        "tensor_terms": len(tensor.ts),
        "clifford_terms": len(clifford.ts),
        "tensor_zeros": tensor_zeros,
        "clifford_zeros": clifford_zeros,
        "clifford_expansion_terms": expanded,
    }
