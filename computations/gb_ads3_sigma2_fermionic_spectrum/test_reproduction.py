"""Behavioral regressions for missing evidence, float64 replay and failures."""
import contextlib
from copy import deepcopy
import importlib.util
import io
import json
from pathlib import Path
import sys
import tempfile
from types import SimpleNamespace
import unittest
from unittest.mock import patch

import numpy as np
import checks
from certificates import assert_certificate_close, validate_root_certificates, ROUND_OFF
from polynomial import action_rank_certificate

ROOT = Path(__file__).resolve().parents[2]
_spec = importlib.util.spec_from_file_location("paper_reproduce", ROOT / "reproduce.py")
reproduce = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(reproduce)


class CertificateTests(unittest.TestCase):
    def setUp(self):
        self.data = checks.read(checks.OUT / "k0_H2_3_s13_np3_q+1.json")
        self.C = np.asarray([checks.unpack(x) for x in self.data["coefficients"]])
        self.cert = self.data["direct_root_checks"][0]

    def test_complete_evidence_and_recomputed_diagnostics_pass(self):
        validate_root_certificates(self.data, dimension=2)
        actual = action_rank_certificate(self.C, complex(*self.cert["root"]), 2, 1,
                                         self.cert["singular_values"], self.cert["action_interpolant_disagreement"])
        assert_certificate_close(actual, self.cert)

    def test_empty_truncated_and_misaligned_lists_fail_before_calculation(self):
        for certificates in ([], self.data["direct_root_checks"][:1], self.data["direct_root_checks"][::-1]):
            with self.subTest(length=len(certificates)), tempfile.TemporaryDirectory() as temporary:
                data = deepcopy(self.data)
                data["direct_root_checks"] = certificates
                path = Path(temporary) / "sector.json"
                path.write_text(json.dumps(data))
                # No source manifest is consulted: the per-root guard itself
                # must reject this, before calling extraction or the action.
                with patch.object(checks, "extract") as extraction:
                    with self.assertRaisesRegex(AssertionError, "root certificate"):
                        checks.fresh_sector(path)
                    extraction.assert_not_called()

    def test_schema_and_nonfinite_evidence_fail(self):
        for field in self.cert:
            changed = deepcopy(self.data)
            del changed["direct_root_checks"][0][field]
            with self.subTest(field=field), self.assertRaises(AssertionError):
                validate_root_certificates(changed)
        for value in (float("nan"), float("inf"), -1.0, True):
            changed = deepcopy(self.data)
            changed["direct_root_checks"][0]["rank_threshold_absolute"] = value
            with self.subTest(value=value), self.assertRaises(AssertionError):
                validate_root_certificates(changed)

    def test_wrong_multiplicity_fails(self):
        changed = deepcopy(self.data)
        changed["roots"][0]["multiplicity"] = 2
        with self.assertRaisesRegex(AssertionError, "multiplicity"):
            validate_root_certificates(changed)
        with self.assertRaises(ArithmeticError):
            action_rank_certificate(self.C, complex(*self.cert["root"]), 2, 2,
                                    self.cert["singular_values"], self.cert["action_interpolant_disagreement"])

    def test_invalid_rank_and_physical_threshold_fail(self):
        for sv, disagreement in (([0.0, 0.0], self.cert["action_interpolant_disagreement"]),
                                 (self.cert["singular_values"], 3e-9*self.cert["coefficient_evaluation_scale"]),
                                 ([2*self.cert["rank_threshold_absolute"], 0.0], self.cert["action_interpolant_disagreement"])):
            with self.subTest(sv=sv, disagreement=disagreement), self.assertRaises(ArithmeticError):
                action_rank_certificate(self.C, complex(*self.cert["root"]), 2, 1, sv, disagreement)

    def test_coefficient_scale_comparison_accepts_ratio_variation(self):
        changed = deepcopy(self.cert)
        changed["rank_threshold_absolute"] *= 1.008
        changed["retained_gap_over_error_budget"] /= 1.008
        changed["polynomial_rank_defect_residual"] += 1e-16*self.cert["coefficient_evaluation_scale"]
        changed["coefficient_scaled_root_solve_residual"] += 1e-16
        assert_certificate_close(changed, self.cert)
        for field in ("root", "singular_values"):
            bad = deepcopy(changed)
            bad[field][0] += 1e-10
            with self.subTest(field=field), self.assertRaises(AssertionError):
                assert_certificate_close(bad, self.cert)
        bad = deepcopy(changed)
        bad["polynomial_rank_defect_residual"] += 2*ROUND_OFF*self.cert["coefficient_evaluation_scale"]
        with self.assertRaises(AssertionError):
            assert_certificate_close(bad, self.cert)
        bad = deepcopy(changed)
        bad["retained_gap_over_error_budget"] *= 2
        with self.assertRaises(AssertionError):
            assert_certificate_close(bad, self.cert)

    def test_previously_failing_h2_record_recomputes(self):
        data, C = checks.load_sector(checks.OUT / "H2_3_1o1000_nm1_q+1.json")
        self.assertEqual(C.shape[1:], (10,10))
        validate_root_certificates(data, dimension=C.shape[1])
        for root, saved in zip(data["roots"], data["direct_root_checks"]):
            fresh = action_rank_certificate(C, complex(*root["root"]), C.shape[1]-2,
                                            root["multiplicity"], saved["singular_values"],
                                            saved["action_interpolant_disagreement"])
            assert_certificate_close(fresh, saved)


class RunnerTests(unittest.TestCase):
    def run_mock(self, failure=None, arguments=()):
        commands = []
        def run(command, **kwargs):
            commands.append(command)
            if failure is not None and len(commands) == 4:
                if failure == "launch":
                    raise OSError("simulated launch failure")
                kwargs["stdout"].write("simulated diagnostic\n")
                return SimpleNamespace(returncode=failure)
            return SimpleNamespace(returncode=0)
        stdout, stderr = io.StringIO(), io.StringIO()
        with patch.object(reproduce.subprocess, "run", side_effect=run):
            with contextlib.redirect_stdout(stdout), contextlib.redirect_stderr(stderr):
                status = reproduce.main(list(arguments))
        return status, commands, stdout.getvalue(), stderr.getvalue()

    def test_default_includes_full_spectrum_extra_checks_and_figures(self):
        status, commands, output, _ = self.run_mock()
        self.assertEqual(status, 0)
        self.assertEqual(len(commands), 14)
        for command in commands:
            self.assertEqual(command[:2], [sys.executable, "-B"])
        self.assertTrue(any("fermionic_spectrum/checks.py" in cmd[2] and "--stored-only" not in cmd for cmd in commands))
        for name in ("first_order_vs_PRL", "exceptional_points", "tower_norm_rule", "make_l0_family", "fig_towers"):
            self.assertIn("PASS " + name, output)

    def test_failure_unavailable_check_and_launch_error_propagate(self):
        for failure in (7, 77, "launch"):
            with self.subTest(failure=failure):
                status, commands, output, _ = self.run_mock(failure)
                self.assertEqual(status, 1)
                self.assertEqual(len(commands), 14)
                self.assertIn("NOT RUN central_charge_extremization" if failure == 77 else "FAIL central_charge_extremization", output)

    def test_extended_covers_components_and_replay(self):
        status, commands, output, _ = self.run_mock(arguments=("--all",))
        self.assertEqual(status, 0)
        for name in ("log_replay", "log_preflight_regressions", "weyl_components", "figure_01", "certificate_and_runner_regressions"):
            self.assertIn("PASS " + name, output)
        self.assertTrue(any("--recompute" in cmd for cmd in commands))


if __name__ == "__main__":
    unittest.main(verbosity=2)
