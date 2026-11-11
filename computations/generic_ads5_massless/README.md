# Generic AdS5 central charges and massless vectors

This package supplies the calculation behind citation-map item 23, namely
equation (3.63) (`eq:acgen`) and equation (3.64) (`eq:uvgen`) in draft v109. The
[result and derivation](../../generic_combination/ads5/central_charges_and_massless_vectors.md)
use the current repository action with all three four-derivative couplings
symbolic. The two-derivative coefficient is explicitly one.

| Target | Producer | Output | Verification |
| --- | --- | --- | --- |
| Equation (3.63) (`eq:acgen`): a and c | [derive.py](derive.py), curvature and background blocks | [results.json](outputs/results.json) | [verification.log](outputs/verification.log), `eq:acgen/*` |
| Equation (3.64) (`eq:uvgen`): u, v and their kinetic coefficients | [derive.py](derive.py), constrained vector block | [results.json](outputs/results.json) | [verification.log](outputs/verification.log), source representatives, two routes, congruence and `eq:uvgen/*` |

## Reproduce

Run from the repository root with Python and SymPy. The recorded run used
Python 3.14.1 and SymPy 1.14.0. No NumPy, external checkpoint, manuscript file,
network connection is needed.

```bash
python3 -B computations/generic_ads5_massless/checks.py
```

The default command reads the source lock and stored results, recomputes the
symbolic expressions, and prints the verification report. A failed identity,
changed source or stale result raises an error and exits unsuccessfully.
To regenerate only this package's two output files:

```bash
python3 -B computations/generic_ads5_massless/derive.py --write-results
python3 -B computations/generic_ads5_massless/checks.py --write-log
```

The log records this explicit regeneration command; a read-only rerun prints
the same report. `derive.py` without an option prints the results as JSON.

## Evidence and scope

- [SOURCE_MAP.md](SOURCE_MAP.md) derives the relevant projection from the
  current component action, including integrations by parts, the constrained
  current and the LOG Bianchi completion. It identifies each input group.
- [action_inputs.py](action_inputs.py) encodes those source groups with exact
  rational coefficients, separately from the expected final formulas.
- [checks.py](checks.py) compares the curvature inputs with the retained
  [constant-curvature blocks](background_blocks.py), checks the tadpoles, and compares the compact and rewritten vector
  actions. It keeps the Bianchi constraint by a multiplier in a second route,
  verifies agreement at symbolic spectral parameter, and checks a congruence
  with no division by coupling-dependent factors.
- The main calculation never assigns numbers to alpha, beta, zeta or g. The
  vacuum relation eliminates beta algebraically on g != 0, L0 > 0; it does not
  switch that invariant off. Named single-invariant limits are checked
  separately, with their remaining coupling and g still symbolic.
- The two-form pivot and the two light kinetic coefficients must be nonzero
  for the displayed inverse-pole interpretation. The undivided congruence
  retains their zeros explicitly. No complete spectrum at degenerate points,
  full generic fermionic Hessian, or product-background result is supplied.

The complete source projection is a documented analytic calculation, not an
automatic LaTeX-to-tensor compiler. The executable checks verify its encoded
identities and the ensuing algebra. They do not certify arbitrary other
component sectors or global boundary conditions.

## Input records

The [source manifest](source_manifest.json) records the final manuscript and
current scientific input hashes. Only the current repository inputs are runtime
dependencies.
