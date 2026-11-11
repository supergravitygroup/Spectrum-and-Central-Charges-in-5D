# R² component action

The primed/unprimed vector-linear construction gives the current gauged R²
density up to quadratic order in the fermions. Couplings remain symbolic.

- [Derivations](derivations/README.md) connect the mixed multiplet, BF insertion,
  primed composite map and canonical action.
- [Canonical action](outputs/r2_action.md) and [tensor coefficients](outputs/r2_action.json)
  contain the final 365 ordered terms.
- [Coefficient collection](calculations/action.py) collects identical tensor
  words in the supplied [supercovariant ledger](expected/step6_supercovariant_collected_ledger.json).
- [Elementary and supercovariant maps](src/kernels/README.md) retain the exact
  algebra underlying those component expressions.
- [Current AdS5 derivation](../../r2/ads5/README.md) and
  [paper checks](../r2_ads5_paper_checks/README.md) cover the spectrum and critical endpoints.

The collection code checks the displayed canonical action; it does not replace
the component-map derivation with a coefficient fit.

## Reproduce the component checks

From the repository root, with SymPy and NumPy installed:

```sh
python3 -B computations/r2_fermionic/checks/run_component_checks.py
```

This runs the BF and mixed-map checks, Gold restriction, explicit
supercovariant insertion, tensor contractions and Majorana-aware collection
checks in a temporary directory. Both regenerated ledgers must agree with the
current expected tensor rows and groups; repository inputs and outputs are not
rewritten. The source hashes are checked against the component notes. The Step 3/4
checks verify the BF insertion and Gold restriction used by this action. The AdS spectrum checks remain in
[the paper-check package](../r2_ads5_paper_checks/README.md).
