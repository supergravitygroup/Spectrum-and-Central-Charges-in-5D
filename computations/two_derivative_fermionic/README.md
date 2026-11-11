# Two-derivative component action

This package supplies the single-linear-multiplet map and vector-linear density
used in the [current two-derivative action](../../common/two_derivative_action/README.md).
The effective vector is $`V_{\mathrm{linear}}+2gV_{\mathrm{defining}}`$.

- [Component derivations](derivations/README.md) give the map and full density.
- [Ordered BF insertion](calculations/action.py) propagates exact coefficients
  without changing factor order or imposing auxiliary equations.
- [Action data](outputs/action.md) and [BF coefficients](outputs/bf_density.json)
  record the retained density up to quadratic order in the fermions.
- [Current AdS5 reduction](../../two_derivative/ads5/README.md) gives the spectrum.

The [common conventions](../../CONVENTIONS.md) and the
[index-lowering derivation](../../common/two_derivative_action/details/construction.md)
fix the lower-index triplet derivative. The supplied component map is the input
to the ordered insertion, rather than an output of a nonlinear SUSY calculation.

## Exact component checks

From the repository root, run:

```sh
python3 -B computations/two_derivative_fermionic/src/kernels/audit_exact_checks.py
```

The [exact checker](src/kernels/audit_exact_checks.py) verifies the symmetric
linear-map derivatives, gauging and background coefficients, five 48-component
fermion derivative kernels, algebraic kernel, and the local AdS5 spectrum.
It uses the current input manifest and retained component equations, and writes
no outputs. These are the existing finite component checks; nonlinear Pauli
terms and boundary symplectic norms are outside their scope.
