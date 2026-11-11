"""Compare fresh polynomials with accepted endpoints; never supply calculation input."""
from src.algebra import ROOT, gauged_algebra, reduction
from src.polynomials import load


def compare_standard(polynomial, slot):
    expected = load(ROOT / "expected" / f"{slot}_standard.json")
    difference = polynomial - expected
    tensor, _ = reduction.collect_tensor(difference, slot)
    difference, _, _ = reduction.collect_clifford(tensor, slot)
    if difference.ts:
        raise AssertionError(f"{slot}: Standard-Weyl residual {len(difference.ts)}")
    return 0


def compare_gauged(polynomial, slot):
    algebra = gauged_algebra()
    expected = load(ROOT / "expected" / f"{slot}_gauged.json")
    difference, _ = algebra.canonical(polynomial - expected, slot, "-accepted")
    if difference.ts:
        raise AssertionError(f"{slot}: gauged residual {len(difference.ts)}")
    return 0


def check_ordered_connection():
    algebra = gauged_algebra()
    antisymmetric = (
        algebra.F("fcon", "-lA", "-lB") - algebra.F("fcon", "-lB", "-lA")
    )
    if len(algebra.h.compact(antisymmetric).ts) != 2:
        raise AssertionError("The full f_ab connection was incorrectly symmetrized")
