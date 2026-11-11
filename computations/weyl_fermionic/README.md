# Weyl² component action

The Weyl-to-linear map and nine vector-linear insertions give the retained
ungauged and gauged component densities.

- [Final component derivations](derivations/README.md) give the map and reductions.
- [FM01–04 map](inputs/reference/notes/04_full_fermionic_weyl_linear_map.md)
  supplies the exact rational coefficients to [the insertion](calculations/density.py).
- [Ungauged density](outputs/ungauged_action.md) and
  [gauged density](outputs/gauged_action.md) have 70 and 73 grouped terms.
- [Current action](../../weyl2/action/README.md), [AdS5 spectrum](../../weyl2/ads5/README.md)
  and [paper checks](../ads5_paper_checks/README.md) give the final-paper route.

Covariant objects retain their implicit fermions. Grouped outer terms are not
counts of elementary fermion monomials. The working map uses $`8/3`$ in M08,
with its Q-variation derivation in the component notes.

The [component verification suite](checks/reference_suite.py) runs the Q/S,
Clifford/Grassmann, canonicalization and action-insertion checks against these
current documents and ledgers:

```bash
python3 -B computations/weyl_fermionic/checks/reference_suite.py
```

Run from the repository root with the package's NumPy and SymPy dependencies.
The suite stages its inputs and generated records in a temporary directory;
the retained actions and results are unchanged. Individual programs can be
selected with `--check verify_weyl_scalar_canonicalization`, for example.
The H50 sum uses the intermediate [explicit-term ledger](inputs/component_ledgers/HUMAN-NOTATION-LEDGER.json).
The checks cover the component expressions and intermediate coefficient
identities used by the final action.
