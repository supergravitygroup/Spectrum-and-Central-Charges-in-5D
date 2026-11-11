"""Stop before analytic expansions if the regenerated action no longer matches.

The source-specific body reductions and covariant proofs must be revised after
an action change. Matching this checkpoint is a consistency gate, not a proof
of the nonlinear source action or a substitute for those derivations.
"""

import json

from src.reporting import PACKAGE, OUTPUTS


def check_action_checkpoint():
    actual = json.loads((OUTPUTS / "action_coefficients.json").read_text())
    expected = json.loads((PACKAGE / "expected/action_coefficients.json").read_text())
    if actual != expected:
        raise AssertionError(
            "Action changed. Review the source-to-quadratic derivations and component "
            "operators before accepting new checkpoints; see EDITING_GUIDE.md."
        )


def main():
    check_action_checkpoint()
    print("Source checkpoint: all 1184 coefficient/phase/tensor-body records match.")


if __name__ == "__main__":
    main()
