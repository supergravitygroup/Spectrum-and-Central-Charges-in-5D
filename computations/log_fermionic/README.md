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

To rebuild the gauged multiplet and BF density from the four stored
Standard-Weyl components, run explicitly:

```bash
(cd computations/log_fermionic && python3 -B -m calculations.rebuild_from_standard)
```

This command writes the gauged component JSON, action display, BF coefficients
and `outputs/downstream_summary.json`. It compares the retained component
inputs before the substitution and ends in `PASS: downstream rebuild`.
It does not recompute the full-primary descent; that derivation is given by
[the component notes](derivations/README.md) and
[descendant algebra](calculations/descendants.py).
