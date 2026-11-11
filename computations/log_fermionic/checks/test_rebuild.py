"""Replay preflight must reject missing/bad input without erasing a saved result."""
import hashlib
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]


class ReplayPreflightTests(unittest.TestCase):
    def test_invalid_input_preserves_existing_outputs(self):
        for defect in ("missing", "malformed"):
            with self.subTest(defect=defect), tempfile.TemporaryDirectory() as temporary:
                work = Path(temporary) / "log"
                shutil.copytree(ROOT, work, ignore=shutil.ignore_patterns("__pycache__"))
                self.assertTrue((work / "outputs/downstream_summary.json").is_file())
                snapshots = {p.relative_to(work): hashlib.sha256(p.read_bytes()).hexdigest()
                             for p in (work / "outputs").rglob("*") if p.is_file()}
                source = work / "expected/N_standard.json"
                if defect == "missing":
                    source.unlink()
                else:
                    source.write_text("invalid JSON")
                result = subprocess.run([sys.executable, "-B", "-m", "calculations.rebuild_from_standard"],
                                        cwd=work, capture_output=True, text=True)
                self.assertNotEqual(result.returncode, 0, result.stdout)
                self.assertIn("Missing replay input" if defect == "missing" else "JSONDecodeError", result.stderr)
                after = {p.relative_to(work): hashlib.sha256(p.read_bytes()).hexdigest()
                         for p in (work / "outputs").rglob("*") if p.is_file()}
                self.assertEqual(snapshots, after)


if __name__ == "__main__":
    unittest.main()
