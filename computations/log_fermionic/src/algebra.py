"""Small public interface to the retained, source-derived LOG algebra.

The component modules in src/kernels implement the ordered derivative and
Clifford reductions used by this interface.
"""
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
KERNEL_DIRECTORY = ROOT / "src" / "kernels"
sys.path.insert(0, str(KERNEL_DIRECTORY))

import log_step6_projection as projection  # noqa: E402
import canonicalize_log_two_fermi as reduction  # noqa: E402

rules = projection.b


def prepare_outputs():
    """All scratch files stay in this package's outputs directory."""
    for path in (
        reduction.OUT,
        projection.BASE / "sources/step7/supercovariant",
        ROOT / "outputs/descendants",
        ROOT / "outputs/standard_weyl",
        ROOT / "outputs/gauged",
    ):
        path.mkdir(parents=True, exist_ok=True)


def gauged_algebra():
    """Load gauge-specific identities only after the Standard-Weyl reduction."""
    prepare_outputs()
    import log_step7_supercovariant
    return log_step7_supercovariant
