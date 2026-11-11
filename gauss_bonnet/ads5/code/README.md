# Gauss–Bonnet on AdS₅: calculations and coefficient data

This package supports the paper's selected AdS₅ branch with the complete
bosonic action and terms through two physical fermions. Read the
[analytic spectrum](../README.md), [calculation walkthrough](WALKTHROUGH.md)
and [equation-to-code map](SOURCE_MAP.md).

The [action inputs](inputs/action_sources.json), [component operator](src/fermion_operator.py),
[coefficient groups](outputs/fermion_component_groups.json),
[fermionic reduction](outputs/fermionic_reduction.json) and
[spectrum](outputs/spectrum.md) provide the calculation details.
The component operator is evaluated in the frame stated in
[the method note](../source_notes.md); the analytic covariance and homogeneity
argument restores the branch parameters. This finite component evaluation and
the symbolic reduction have distinct scopes.

## Package layout

| Directory | Content |
|---|---|
| `inputs/` | Component action, symbols and intermediate coefficients |
| `calculations/` | Modules arranged in physical order |
| `src/` | Clifford and covariant-derivative algebra |
| `checks/` | Input integrity, action readback and reduction checks |
| `expected/` | Fixed reference coefficients used only for comparison |
| `outputs/` | Current action coefficients, operators and spectrum |
| `derivations/` | Action, background, quadratic equations and physical reduction |
| `references/` | Conventions and component definitions |
| `environment/` | Dependency versions |

The [repository reproduction guide](../../../README.md#reproduction) lists the scoped
checks. The component input and quadratic expansion are specific to this
background; this package is not a general covariant tensor compiler.

## Run the calculation

Install the [pinned dependencies](environment/requirements.txt) in an external
activated environment. From the repository root, the stored-output comparison is:

```bash
(cd gauss_bonnet/ads5/code && python3 -B -m unittest checks.test_reproduction)
```

It ends with twelve tests and `OK`, and writes no scientific outputs. To
recompute the 48-component operator without writing output files, run:

```bash
cd gauss_bonnet/ads5/code
python3 -B - <<'PYCODE'
from calculations.fermion_operator import evaluate_graded_operators, interpolate_component_groups
reports, operators = evaluate_graded_operators()
groups = interpolate_component_groups(operators)
print('PASS component groups:', len(groups))
PYCODE
```

This takes several minutes and prints the five exact-kernel checks followed
by `PASS component groups: 60`. The [source map](SOURCE_MAP.md) explains the
fixed evaluation frame and analytic restoration of the general parameters.

The following modules deliberately regenerate records under this package's
`outputs/`. Run them in this order from `gauss_bonnet/ads5/code`:

```bash
python3 -B -m checks.provenance
python3 -B -m calculations.assemble_action
python3 -B -m checks.action_readback
python3 -B -m checks.source_checkpoint
python3 -B -m calculations.background
python3 -B -m calculations.bosonic_quadratic
python3 -B -m calculations.fermion_operator
python3 -B -m calculations.fermionic_reduction
python3 -B -m checks.reference_reduction
python3 -B -m calculations.spectrum
python3 -B -m calculations.supersymmetry
python3 -B -m calculations.representations
python3 -B -m unittest checks.test_reproduction
```

The integrity and checkpoint commands only read inputs; the calculation and
readback modules write their named reports. The current [spectrum table](outputs/spectrum.md),
[component sums](outputs/fermion_component_sums.md) and
[reduction record](outputs/fermionic_reduction.json) provide direct result entry points.

## Physical scope

The selected branch is

```math
a=\lambda_{\rm GB}g^2,\qquad
x=\frac{2}{1+\sqrt{1+2a}},\qquad
L_0=x,\quad N_0=-\frac32gx^2,\quad k=-\frac12g^2x^2.
```

The regular domain is real $`g\ne0`$, $`a>-1/2`$, $`0<x<2`$. The recorded spectrum has **12 bosonic and 12 fermionic local degrees of freedom**, positive local kinetic weights in the source reference convention, and a scalar at the AdS5 BF bound. At $`a=-1/2`$, $`x=2`$, the raw quadratic action vanishes; the generic count is not assigned to that endpoint.

The Python code uses source-specific analytic expansions documented in `derivations/`; it is not a general tensor engine deriving every covariant variation directly from raw action text. The [stage map](SOURCE_MAP.md) identifies the analytic inputs and code operations.

“Full fermionic” here means physical fermion order **0+2**, including implicit supercovariant contributions. The Weyl and two-derivative source qualifications remain attached to those inputs. Global boundary conditions, global frequencies, topological sectors, and renormalized boundary norms are outside this local calculation. Local Killing-spinor and representation checks do not establish nonlinear SUSY closure.

