# LOG component action

This package gives the full primary, ordered spinor derivatives, Standard-Weyl
components, gauged composite substitution and vector-linear density through
two physical fermions.

- [Source map](SOURCE_MAP.md) and [component derivations](derivations/README.md)
  give the equations used in the descent.
- [Descendant algebra](calculations/descendants.py),
  [canonical reduction](calculations/standard_weyl.py),
  [gauged components](calculations/gauged_components.py) and
  [density insertion](calculations/density.py) expose the calculation stages.
- [Final component data](outputs/action.md) and [density coefficients](outputs/bf_density.json)
  contain $`L=13`$, $`\varphi=94`$, $`N=141`$ and $`E=373`$ canonical terms.
- [Current LOG action](../../log/action/README.md), [AdS5 reduction](../../log/ads5/README.md)
  and [paper checks](../ads5_paper_checks/README.md) connect these inputs to the spectrum.

The tensor kernels preserve derivative order and implicit supercovariant
fermions. Component counts describe the chosen canonical representation.

## Checks and downstream reproduction

From the repository root with this package's
[dependencies](environment/requirements.txt) installed:

```bash
(cd computations/log_fermionic && python3 -B -m checks.test_contract)
python3 -B computations/ads5_paper_checks/checks.py
```

The first command checks six component interfaces, ordered derivatives,
coefficient-fault detection and the BF fermion-degree budget; success ends in
`OK`. The second checks the documented Weyl/LOG AdS5 operators and prints
`PASS_SCOPED_EXACT`. Both commands leave the scientific outputs unchanged.

To replay the gauged multiplet and BF density from the distributed canonical
components `expected/{L,phi,N,E}_standard.json`, run explicitly in a working
copy whose outputs may be regenerated:

```bash
(cd computations/log_fermionic && python3 -B -m calculations.rebuild_from_standard)
```

This command writes the gauged component JSON, action display, BF coefficients
and `outputs/downstream_summary.json`. It validates all four inputs before deleting or replacing a saved summary,
records their fresh hashes and compares all seven BF blocks with the retained
coefficients and ordered terms. Success ends in `PASS: downstream replay`.
It does not recompute the full-primary descent; that derivation is given by
[the component notes](derivations/README.md) and
[descendant algebra](calculations/descendants.py).

This default explicitly adopts the canonical components as replay inputs.
Comparison with those same Standard-Weyl files is self-comparison, not an
independent test of their derivation. The historical phi/N/E input bytes have
not been recovered, and this command does not recreate that historical run.
An explicit `--historical-input-dir PATH` may supply alternative
`{L,phi,N,E}.json` files; their hashes are recorded, not presumed historical.
The root `reproduce.py --all` stages this replay in a temporary copy and
preserves the repository outputs. Its report includes the term counts of the
seven matched blocks. Negative preflight tests are available as
`python -B -m checks.test_rebuild` from this package directory.
