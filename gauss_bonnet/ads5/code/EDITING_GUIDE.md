# Where expressions and their dependencies are recorded

Use the [walkthrough](WALKTHROUGH.md) to locate an expression and the [source map](SOURCE_MAP.md) to find its Python function. Calculations live in `calculate()` or named pure functions; output writing lives in `main()`. Imports do not generate outputs.

| Type of change | Starting file | Dependencies to review |
|---|---|---|
| Symbol or branch parametrization | [symbols.py](inputs/symbols.py) | Background domain, raw coefficients, endpoint, and limits |
| Action-source coefficient | `inputs/action_sources/` and manifest | Full action, term ledger, covariant expansions, and prior checkpoints |
| Scalar/metric expansion | [bosonic_quadratic.py](calculations/bosonic_quadratic.py), `scalar_metric_restriction()` | Step 6 (6.7)–(6.18), boundary current, and Taylor factors |
| Form derivative or current | `form_derivative_collection()` in the same file | FD1–FD17; the closed-form Bianchi identity applies to $`G`$ |
| Fermionic covariant derivative | [fermion_operator.py](src/fermion_operator.py), `linear_descendants()` | FC1–FC12, SF1–SF19, Clifford/doublet signs, and ordered second derivatives |
| Collected fermion coefficient | [fermionic_coefficients.py](inputs/fermionic_coefficients.py) | FC13–FC15 and the separate 48-component record |
| Field transformation or constraint | [fermionic_reduction.py](calculations/fermionic_reduction.py) and bosonic `calculate()` | Original equations, residual gauge, and $`c\ne0`$ |
| Spectrum presentation | [spectrum.py](calculations/spectrum.py) | Diagonal blocks remain the source; representation tables are not calculation inputs |

## Reduction and comparison scope

For the fermion field transformation, FC15 corresponds to the six expressions
in `inputs/fermionic_coefficients.py`. `calculations/fermionic_reduction.py`
sums them, solves for the mixing-removing shift, and reconstructs the original
equations. This checks a supplied coefficient representation; it does not
independently rederive FC13 from the full component action.

The [repository reproduction guide](../../../README.md#reproduction) specifies the scoped checks.

## Source changes and checkpoints

Frozen inputs define the source version of this calculation. The input manifest, term ledger, affected analytic expansions, and operator groups must remain consistent. Altering a hash or an `expected/` result to suppress a test failure is not verification.

`checks/source_checkpoint.py` stops before the quadratic stages when an action input changes. The component code uses the explicit bilinear expressions FC3/FC6/FC8/FC9, and the form code uses specific analytic current reductions. Neither automatically interprets an arbitrary new source monomial. A different background cannot be substituted merely by changing `x`.

## Sign and constraint conventions

- The Majorana bar is linear; Hermitian conjugation does not replace `.T`.
- The covariant derivative of the gauge-fixed dilatino need not vanish.
- $`G,H,p`$ remain constrained derivatives of their potentials in the variation.
- Two-form dualization retains the first-order Legendre term.
- The critical branch is separated before division by $`c=2-x`$; regular constraints do not apply at $`x=2`$.
- `expected/` contains fixed comparison coefficients, not inputs for calculating the spectrum.

Calculation outputs are written under `outputs/`; `expected/` supplies reference values for comparison.
