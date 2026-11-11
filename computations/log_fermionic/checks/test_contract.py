"""Small behavioral tests for the exported interfaces and known failure modes."""
import unittest
from src.algebra import ROOT, rules, gauged_algebra
from src.polynomials import encode, decode, load
from calculations.density import density_blocks


class ContractTests(unittest.TestCase):
    def test_primary_is_not_prematurely_truncated(self):
        degrees = {
            sum(atom.parity for atom in factors)
            for primary in rules.make_inputs().values()
            for _, factors in primary.ts
        }
        self.assertIn(6, degrees)
        self.assertIn(4, degrees)

    def test_serialization_preserves_ordered_derivatives(self):
        polynomial = rules.I * rules.A("rho", ds=("-lA", "-lB"))
        self.assertEqual(encode(decode(encode(polynomial))), encode(polynomial))
        reversed_order = rules.I * rules.A("rho", ds=("-lB", "-lA"))
        self.assertNotEqual(encode(polynomial), encode(reversed_order))

    def test_gauge_does_not_erase_dilatino_descendants(self):
        algebra = gauged_algebra()
        undifferentiated = rules.P(rules.A("lam", ("-sE", "+uI")))
        differentiated = rules.P(rules.A("lam", ("-sE", "+uI"), ("-lA",)))
        self.assertFalse(algebra.gauge_values(undifferentiated).ts)
        self.assertTrue(algebra.gauge_values(differentiated).ts)

    def test_full_connection_remains_ordered(self):
        from checks.regression import check_ordered_connection
        check_ordered_connection()

    def test_wrong_endpoint_coefficient_is_detected(self):
        from checks.regression import compare_gauged
        polynomial = load(ROOT / "expected/L_gauged.json")
        coefficient, factors = polynomial.ts[0]
        polynomial.ts[0] = (2 * coefficient, factors)
        with self.assertRaises(AssertionError):
            compare_gauged(polynomial, "L")

    def test_density_external_fermion_budget(self):
        # Deliberately include a degree-two triplet contribution: it belongs in
        # Y*L, but inserting it into gravitino*gravitino*L would create degree 4.
        fermion = rules.A("lam", ("-sA", "+uI"))
        other = rules.A("lam", ("-sB", "+uJ"))
        multiplet = {"L": rules.P(1) + fermion * other,
                     "phi": rules.P(fermion), "N": rules.P(1), "E": rules.P(1)}
        blocks = density_blocks(multiplet)
        triplet_blocks = [block for block in blocks if block["slot"] == "L"]
        self.assertEqual(len(triplet_blocks[0]["terms_with_density_coefficient"]), 2)
        for block in triplet_blocks[1:]:
            terms = block["terms_with_density_coefficient"]
            self.assertEqual(len(terms), 1)
            self.assertEqual(terms[0]["factors"], [])


if __name__ == "__main__":
    unittest.main()
