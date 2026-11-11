"""Independent recorded checkpoints, physics invariants and fault detection.

Run after all calculation stages. Expected outputs never enter the calculations.
"""

import hashlib
import json
import re
import unittest
from unittest.mock import patch

import sympy as sp

from src.reporting import PACKAGE, OUTPUTS
from inputs.symbols import g, x, c
from inputs.fermionic_coefficients import gauss_bonnet_terms
from calculations.bosonic_quadratic import calculate as calculate_bosons
from calculations.fermionic_reduction import calculate as calculate_fermions
from calculations.spectrum import calculate as calculate_spectrum
from checks.provenance import validate_entries
from checks.source_checkpoint import check_action_checkpoint
from checks.action_readback import find_equation


def read_json(path):
    return json.loads(path.read_text())


class ReproductionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.bosons = calculate_bosons()
        cls.fermions = calculate_fermions()
        cls.spectrum = calculate_spectrum()

    def test_current_action_inputs(self):
        validate_entries(read_json(PACKAGE / "inputs/action_sources.json"), "path")

    def test_1184_action_records(self):
        check_action_checkpoint()
        self.assertEqual(len(read_json(OUTPUTS / "action_coefficients.json")), 1184)

    def test_full_action_expression_matches_original(self):
        original = PACKAGE.parent.parent / "action/gb_splus_action.md"
        original_final = find_equation(original.read_text(), "GB-FINAL-DENSITY")
        generated = find_equation((OUTPUTS / "action.md").read_text(), "GB-FINAL-DENSITY")
        self.assertEqual(generated.strip(), original_final.strip())

    def test_all_component_polynomials_match_original(self):
        self.assertEqual(
            read_json(OUTPUTS / "fermion_component_groups.json"),
            read_json(PACKAGE / "expected/part2_fermion_component_groups.json"),
        )
        self.assertEqual(
            read_json(OUTPUTS / "fermion_operator.json"),
            read_json(PACKAGE / "expected/part2_fermion_operator.json"),
        )

    def test_bosonic_raw_coefficients_against_step6(self):
        # Independent explicit checkpoint: Step 6, (6.18), (6.30).
        expected = {
            "h_Einstein_h": -c/2, "ell_r": c/x,
            "gradient_ell_squared": c/x**2, "ell_squared": -4*c*g**2,
            "ell_n": -8*c*g/x, "n_squared": -2*c/x**2,
            "G_squared": -c/2, "H_squared": 4*c, "p_squared": -2*c/x**2,
            "p_v": -2*sp.sqrt(2)*c/x, "p_A": -4*g*c, "vprime_squared": 2*c,
        }
        for name, value in expected.items():
            with self.subTest(name=name):
                self.assertEqual(sp.factor(self.bosons["raw_quadratic_coefficients"][name]-value), 0)

    def test_fermion_raw_coefficients_against_fc15(self):
        expected = {
            "gravitino_kinetic": -c, "spinor_kinetic": 2*c/x**2,
            "derivative_mixing_delta": -2*sp.sqrt(2)*sp.I*c/x,
            "gravitino_mass_delta": -3*sp.I*g*x*c/(2*sp.sqrt(2)),
            "algebraic_mixing": -4*g*c,
            "spinor_mass_delta": 7*sp.I*g*c/(sp.sqrt(2)*x),
        }
        for name, value in expected.items():
            with self.subTest(name=name):
                self.assertEqual(sp.factor(self.fermions["raw_quadratic_coefficients"][name]-value), 0)

    def test_all_raw_coefficients_vanish_at_endpoint(self):
        for result in [self.bosons, self.fermions]:
            for name, value in result["raw_quadratic_coefficients"].items():
                with self.subTest(name=name):
                    self.assertEqual(sp.simplify(value.subs(x, 2)), 0)
        self.assertIn("do not use", self.bosons["constraint_domain"])
        self.assertIn("not assigned", self.spectrum["endpoint"])

    def test_kinetic_weights_and_dof(self):
        expected_weights = [c, 2*c/(3*x**2), 2*c, 16*c, c, 2*c/(3*x**2)]
        for row, expected in zip(self.spectrum["spectrum"], expected_weights):
            self.assertEqual(sp.factor(row["kinetic_weight"]-expected), 0)
        self.assertEqual((self.spectrum["bosonic_dof"], self.spectrum["fermionic_dof"]), (12, 12))

    def test_raw_coefficient_dimensions(self):
        scale = sp.Symbol("mass_scale", positive=True)
        boson_dimensions = {
            "ell_squared": 2, "ell_n": 1, "p_A": 1,
        }
        for name, value in self.bosons["raw_quadratic_coefficients"].items():
            dimension = boson_dimensions.get(name, 0)
            self.assertEqual(sp.factor(value.subs(g, scale*g)-scale**dimension*value), 0)
        for name, value in self.fermions["raw_quadratic_coefficients"].items():
            dimension = int("mass" in name or name == "algebraic_mixing")
            self.assertEqual(sp.factor(value.subs(g, scale*g)-scale**dimension*value), 0)

    def test_wrong_fermion_coefficient_is_detected(self):
        changed = gauss_bonnet_terms()
        changed["derivative_mixing_delta"] += sp.I*g**2*x
        with patch("calculations.fermionic_reduction.gauss_bonnet_terms", return_value=changed):
            with self.assertRaises(AssertionError):
                calculate_fermions()

    def test_naive_dual_substitution_has_wrong_sign(self):
        naive = self.bosons["raw_quadratic_coefficients"]["H_squared"]
        legendre = self.bosons["dual_vector_coefficient"]
        self.assertEqual(sp.factor(naive + legendre), 0)
        self.assertNotEqual(sp.factor(naive - legendre), 0)

    def test_wrong_regenerated_source_is_rejected(self):
        actual = read_json(OUTPUTS / "action_coefficients.json")
        changed = [dict(row) for row in actual]
        changed[0]["coefficient"] = "999"
        with patch("checks.source_checkpoint.json.loads", side_effect=[changed, actual]):
            with self.assertRaises(AssertionError):
                check_action_checkpoint()


if __name__ == "__main__":
    unittest.main(verbosity=2)
