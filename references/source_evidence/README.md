# Component calculation evidence

This directory contains scientific source notes, coefficient-location records, and the source programs cited by the component derivations. [File identities and scope](manifest.json) identify the current component records.

The [main locator register](../bibliography.md) links each record to its referring calculation. The LOG derivation notes distinguish formal polynomial or operator identities from finite component tests. A recorded `PASS` or zero residual has only the scope specified by that source; it is not an unrestricted proof of a full supergravity action.

The LOG Python files use source-relative imports and inputs from the originating component-polynomial and intermediate-data tree, including symbolic component data and pickle files. These dependencies are not all included, so the selected programs and saved outputs do not provide standalone execution of the complete LOG workflow. The [LOG action](../../log/action/details/spectrum_input.md), (A28), (A32), (A34), and [quadratic derivation](../../log/ads5/quadratic_action.md), (Q31)–(Q40), (Q57), supply its analytic inputs and reduction independently of those file-availability limits. The separate [GB reproduction guide](../../gauss_bonnet/ads5/code/README.md) applies to the Gauss–Bonnet on AdS₅ workflow; it is not an execution guide for LOG.

## Scientific notes

- [Bosonic LOG density and boundary comparison](log/derivations/bosonic.md): (B-01)–(B-13), with the [complete equation companion](../../log/action/details/component_construction/results/gauged_full_fermionic_log/sources/certification_20260925/bosonic/EXACT_BOSONIC_COMPARISON.md).
- [Curved LOG primary and descendants](log/derivations/curved.md): source algebra and the recorded primarity/current identities.
- [Defining projector](log/derivations/defining-projector.md): relation between the projector definition and the calculated primary.
- [Form, potential, and BF interface](log/derivations/form-interface.md): (FI01)–(FI33), with the ordinary-current and supercovariant-current distinction.
- [Projection and component chain](log/derivations/projection.md): the retained-order component correspondence and its stated scope.
