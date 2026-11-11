"""Regression checks for portable certificate comparison and the full paper runner."""

import contextlib
from copy import deepcopy
import importlib.util
import io
from pathlib import Path
import sys
from types import SimpleNamespace
import unittest
from unittest.mock import patch

import numpy as np

from checks import assert_certificate_close

ROOT = Path(__file__).resolve().parents[2]
_spec = importlib.util.spec_from_file_location("paper_reproduce", ROOT / "reproduce.py")
reproduce = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(reproduce)


class CertificateComparisonTests(unittest.TestCase):
    def setUp(self):
        self.reference = {
            "root": [2.5, 0.0],
            "singular_values": [12.5, 1e-15, 0.0],
            "diagnostics": {"residual": 1e-17, "gap": 40.0, "accepted": True},
            "rank": 8, "multiplicity": 2, "resolved_extra_nullity": 2,
            "optional": None,
        }

    def test_roundoff_in_nested_floats_is_accepted(self):
        changed = deepcopy(self.reference)
        changed["root"][0] += 1e-10
        changed["singular_values"][1] = 2e-14
        changed["diagnostics"]["residual"] = 5e-14
        changed["diagnostics"]["gap"] += 1e-8
        assert_certificate_close(changed, self.reference)
        for floating in (np.float64, np.float32):
            with self.subTest(floating=floating.__name__):
                changed = deepcopy(self.reference)
                changed["root"][0] = floating(2.5)
                changed["diagnostics"]["gap"] = floating(40.0)
                changed["singular_values"][1] = floating(2e-14)
                assert_certificate_close(changed, self.reference)

    def test_discrete_values_are_exact(self):
        for key in ("rank", "multiplicity", "resolved_extra_nullity"):
            with self.subTest(key=key):
                changed = deepcopy(self.reference)
                changed[key] += 1
                with self.assertRaises(AssertionError):
                    assert_certificate_close(changed, self.reference)
        for value in (False, 1):
            changed = deepcopy(self.reference)
            changed["diagnostics"]["accepted"] = value
            with self.assertRaises(AssertionError):
                assert_certificate_close(changed, self.reference)
        changed = deepcopy(self.reference)
        changed["rank"] = 8.0
        with self.assertRaises(AssertionError):
            assert_certificate_close(changed, self.reference)
        for value in (0, False, np.int64(0), np.bool_(False)):
            changed = deepcopy(self.reference)
            changed["root"][1] = value
            with self.subTest(value=type(value).__name__), self.assertRaises(AssertionError):
                assert_certificate_close(changed, self.reference)

    def test_significant_float_changes_and_nonfinite_values_are_rejected(self):
        for value in (40.001, float("nan"), float("inf")):
            changed = deepcopy(self.reference)
            changed["diagnostics"]["gap"] = value
            with self.subTest(value=value), self.assertRaises(AssertionError):
                assert_certificate_close(changed, self.reference)
        changed = deepcopy(self.reference)
        changed["diagnostics"]["residual"] = 1e-8
        with self.assertRaises(AssertionError):
            assert_certificate_close(changed, self.reference)

    def test_missing_keys_and_entries_are_rejected(self):
        changed = deepcopy(self.reference)
        del changed["optional"]
        with self.assertRaises(AssertionError):
            assert_certificate_close(changed, self.reference)
        changed = deepcopy(self.reference)
        changed["singular_values"].pop()
        with self.assertRaises(AssertionError):
            assert_certificate_close(changed, self.reference)


class PaperRunnerTests(unittest.TestCase):
    def run_mock_packages(self, failed_index=None, cannot_start=False):
        commands = []

        def run(command, **kwargs):
            index = len(commands)
            commands.append((command, kwargs))
            if index == failed_index:
                if cannot_start:
                    raise OSError("simulated launch failure")
                kwargs["stdout"].write("simulated package failure details\n")
                return SimpleNamespace(returncode=7)
            kwargs["stdout"].write("simulated successful package output\n")
            return SimpleNamespace(returncode=0)

        stdout, stderr = io.StringIO(), io.StringIO()
        with patch.object(reproduce.subprocess, "run", side_effect=run):
            with contextlib.redirect_stdout(stdout), contextlib.redirect_stderr(stderr):
                status = reproduce.main([])
        return status, commands, stdout.getvalue().splitlines(), stderr.getvalue()

    def test_default_runs_all_nine_full_packages_with_current_python(self):
        status, commands, lines, diagnostics = self.run_mock_packages()
        self.assertEqual(status, 0)
        self.assertEqual(len(commands), 9)
        self.assertEqual(len(lines), 9)
        self.assertTrue(all(line.startswith("PASS ") for line in lines))
        self.assertNotIn("simulated successful", diagnostics)
        expected = [
            "r2_ads5_paper_checks", "ads5_paper_checks", "generic_ads5_massless",
            "central_charge_extremization", "paper_conventions",
            "composite_vector_correspondence", "gb_ads3_sigma2",
            "gb_ads3_sigma2_fermionic", "gb_ads3_sigma2_fermionic_spectrum",
        ]
        for (command, kwargs), package in zip(commands, expected):
            self.assertEqual(command[:2], [sys.executable, "-B"])
            self.assertEqual(Path(command[2]), ROOT / "computations" / package / "checks.py")
            self.assertEqual(command[3:], ["--norms"] if package == "gb_ads3_sigma2" else [])
            self.assertEqual(kwargs["cwd"], ROOT)
            self.assertFalse(kwargs["check"])

    def test_failure_is_reported_and_remaining_packages_still_run(self):
        for cannot_start in (False, True):
            with self.subTest(cannot_start=cannot_start):
                status, commands, lines, diagnostics = self.run_mock_packages(3, cannot_start)
                self.assertEqual(status, 1)
                self.assertEqual(len(commands), 9)
                self.assertEqual(len(lines), 9)
                self.assertTrue(lines[3].startswith("FAIL central_charge_extremization"))
                self.assertEqual(sum(line.startswith("PASS ") for line in lines), 8)
                self.assertIn("simulated launch failure" if cannot_start else
                              "simulated package failure details", diagnostics)


if __name__ == "__main__":
    unittest.main()
