# Paper conventions and vacuum checks

This package checks the final paper's vacuum equations and spin-connection
identities. See the [derivation](../../references/paper_scope_and_provenance.md)
for the component definitions.

From the repository root, with SymPy 1.14.0:

~~~bash
python3 -B computations/paper_conventions/checks.py
~~~

The default is read-only. The explicit report command writes only this
package's outputs:

~~~bash
python3 -B computations/paper_conventions/checks.py --write-log
~~~

The [requirements](requirements.txt) may be installed in an external
environment. The program does not need the original source folder or
manuscript at runtime.

| Check | Meaning and scope |
|---|---|
| 125 contorsion antisymmetry components | The dependent spin connection is metric-compatible with the paper's contracted rank-one Majorana flip. |
| 125 torsion-constraint components | Its two-fermion contribution solves R(P) = 0 with the recorded coefficient. All bilinear symbols remain free. |
| 10 vacuum identities | The MS5 Weyl density, its first variations and the three scalar/metric tadpoles give the paper's tau dependence. The nonzero second N derivative is retained. |
| 3 negative controls | A wrong Majorana flip, a missing contorsion term and a wrong SUSY N coefficient each leave a nonzero symbolic residual. |

The MS5 action projection is imported from the existing
[item-23 input](../generic_ads5_massless/action_inputs.py), with its
[term correspondence](../generic_ads5_massless/SOURCE_MAP.md).
Differentiation is performed before applying the supersymmetric
configuration; g, alpha, beta, zeta and the modulus remain symbolic.
This is a new bounded consistency check of that projection, not a
second full action derivation. The torsion proof uses abstract free
bilinears and does not sample spinor components.

The [source manifest](source_manifest.json) records the current inputs and
implementation hashes, checked before the algebra runs.

The [JSON report](outputs/verification.json) lists all residuals,
negative-control witnesses, assumptions, versions and input hashes.
The [short log](outputs/verification.log) records the group counts.
These checks do not compute item-26 roots or multiplet assignments,
classify critical spectra, establish boundary unitarity or prove
nonlinear supersymmetry of the full action.
