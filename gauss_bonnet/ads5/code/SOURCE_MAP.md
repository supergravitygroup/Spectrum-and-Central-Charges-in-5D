# Source, derivation, and code map

The starting action is specified by [GB01, GB16–GB20, and GB-FINAL-DENSITY](../../action/gb_splus_action.md). Exact input identities are in SOURCE_LOCK; equations and component definitions are indexed in [COMPONENT_INDEX](references/COMPONENT_INDEX.md). The input equations and their supporting component derivations are included.

| Stage | Detailed mathematics | Code | Recorded operation |
|---|---|---|---|
| Full action | [GB01–GB20](../../action/gb_splus_action.md) | [assemble_action](calculations/assemble_action.py) | Reads 11 frozen inputs, distributes the -2/-4 coefficients, records gauge/fermion-order exclusions, and writes 1,184 terms |
| Independent source readback | [Coefficient ledger](outputs/action_coefficient_ledger.md) | [action_readback](checks/action_readback.py) | Uses a separate parser to compare generated TeX bodies, phases, coefficients, and the two-derivative expression |
| $`S^{(0)},S^{(1)}`$ | [First order](derivations/background/STEP_03_FIRST_ORDER_INGREDIENTS.md), [background density](derivations/background/STEP_04_ZEROTH_ORDER_ACTION.md), [catalogue](../background.md) | [background](calculations/background.py) | Source coefficients times analytic covariant body values; coefficients of arbitrary scalar/curvature fluctuations and box terms; Gauss–Bonnet on AdS₅ tadpoles |
| Bosonic $`S^{(2)}`$ | [Step 6](../quadratic_action.md), [FD1–FD17](derivations/support/part2_form_derivative_check.md) | [bosonic_quadratic](calculations/bosonic_quadratic.py) | Scalar/metric sums and Taylor derivatives; form derivative/current sums; 12 raw coefficients; auxiliary equation and dual Legendre sign |
| Fermionic covariant expansion | [FC1–FC15](../details/fermionic_reduction.md), [SF1–SF19](derivations/support/part2_fermion_descendant_check.md) | [component core](src/fermion_operator.py) | Explicit Clifford matrices, gravitino/spinor/dependent-connection derivatives, and five separately collected source groups |
| Component comparison | [FC10–FC13](../details/fermionic_reduction.md) | [operator runner](calculations/fermion_operator.py) | 48×48 graded Euler matrices; degree-at-most-three polynomials interpolated from four radial values and compared at a fifth, in a fixed parameter frame |
| Raw fermionic $`S^{(2)}`$ | [FC13–FC15](../details/fermionic_reduction.md) | [coefficient inputs](inputs/fermionic_coefficients.py), [fermionic_reduction](calculations/fermionic_reduction.py) | Sums the two-derivative and GB terms into six raw coefficients |
| Equations, gauge, constraints | [Step 7](derivations/spectrum/STEP_07_LINEARIZED_EQUATIONS.md), [Step 9](derivations/spectrum/STEP_09_FIELD_STATUS_AND_CONSTRAINTS.md), [Step 10](derivations/spectrum/STEP_10_GAUGES_AND_SECTOR_MAPS.md) | Reductions and [reference_reduction](checks/reference_reduction.py) | Field transformations, Noether relations, and reconstruction in the original fields |
| Eigenfields and spectrum | [Steps 11–14](../details/masses_and_eigenfields.md) | [spectrum](calculations/spectrum.py) | Masses, kinetic weights, local counts, BF condition, and limits from diagonal blocks |
| Local supersymmetry | [E16–E22](derivations/support/gb-splus-spectrum-method-EXPLAIN.md) | [supersymmetry](calculations/supersymmetry.py) | Algebraic relations in the accepted gauge-preserving rules and flat Killing connection |
| Representation comparison | [R1–R15](../details/multiplets.md) | [representations](calculations/representations.py) | Energies, shortening, and the $`A-2Q,A+4Q`$ transformation, after the masses have been obtained |

## Analytic inputs

The notes supply the covariant Taylor expansion, Lovelock metric Hessian, curvature commutators, Bianchi reductions, form currents, physical fermion-order classification, and variation/gauge arguments. Python does not independently derive every such identity from the raw textual action using a general tensor engine.

For example, `form_derivative_collection()` uses the three analytic current blocks FD8–FD12. `fermionic_coefficients.py` records the six bilinear coefficients of FC13–FC14. The component calculation tests FC13 through a separate construction; the accompanying derivation supplies the source expansion for FC14.

The [source-term ledger](derivations/spectrum/SOURCE_TERM_LEDGER.md) traces the relevant terms. The spectrum follows the selected AdS₅ branch, which continuously approaches the two-derivative vacuum as the Gauss–Bonnet coupling tends to zero.

## Local inputs

The [input manifest](inputs/action_sources.json) identifies the component
expressions read by the calculation. The source conventions
connect them to the literature and the paper's normalization.
