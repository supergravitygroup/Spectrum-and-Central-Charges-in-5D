"""Failure-detecting tests for exact BF propagation and the gauged limit."""
from fractions import Fraction
import unittest
from src.expressions import Coefficient
from calculations.linear_multiplet import load_multiplet
from calculations.density import assemble
from checks.actions import compare_expected, check_gauged_limit


class ContractTests(unittest.TestCase):
    def test_majorana_coefficients_are_complex_linear(self):
        imaginary = Coefficient(Fraction(1), True)
        self.assertEqual((imaginary * imaginary).record(), ["-1", 0])

    def test_wrong_adopted_spinor_coefficient_is_detected(self):
        multiplet = load_multiplet()
        coefficient, body = multiplet["phi"][8]
        multiplet["phi"][8] = (Coefficient(2 * coefficient.value), body)
        with self.assertRaises(AssertionError):
            compare_expected(assemble(multiplet), "ungauged")

    def test_wrong_gauged_correction_is_detected(self):
        multiplet = load_multiplet()
        gauged = assemble(multiplet, gauged=True)
        gauged["blocks"]["Y"][-1][0][0] = "0"
        with self.assertRaises(AssertionError):
            compare_expected(gauged, "gauged")

    def test_zero_coupling_limit_detects_non_gauged_change(self):
        multiplet = load_multiplet()
        ungauged = assemble(multiplet)
        gauged = assemble(multiplet, gauged=True)
        gauged["blocks"]["sigma_N"][0][0][0] = "0"
        with self.assertRaises(AssertionError):
            check_gauged_limit(ungauged, gauged)

    def test_valid_densities_and_nested_derivatives(self):
        multiplet = load_multiplet()
        self.assertTrue(any(r"\mathcalD_b\Big[" in body for _, body in multiplet["E"]))
        ungauged, gauged = assemble(multiplet), assemble(multiplet, gauged=True)
        compare_expected(ungauged, "ungauged")
        compare_expected(gauged, "gauged")
        check_gauged_limit(ungauged, gauged)



if __name__ == "__main__":
    unittest.main()
