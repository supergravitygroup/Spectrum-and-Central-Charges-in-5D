# Gauss–Bonnet on AdS₅: local spectrum from the full fermionic action

The nine step files below derive the complete local bosonic and fermionic quadratic spectrum from [GB-FINAL-DENSITY](../../../../action/gb_splus_action.md#6-final-result). The accepted action, fields and conventions are inputs. The [Part I catalogue](../../../background.md) supplies the selected background and its tadpole residuals. No unrestricted nonlinear equations or separate bosonic action are used.

The selected branch and domain are

```math
a=\lambda_{\rm GB}g^2\ge-\frac12,\qquad x=L_0=\frac2{1+\sqrt{1+2a}},\qquad c=2-x,\qquad N_0=-\frac32gx^2,\quad k=-\frac12g^2x^2,\quad g\ne0.
```

For finite $`a>-1/2`$, the physical local count is **12 bosonic + 12 fermionic**. Every reduced kinetic sign agrees with the healthy two-derivative reference. The scalar saturates the AdS₅ BF bound, and no extra higher-derivative pole survives on this branch. At $`a=-1/2`$, the entire raw quadratic action vanishes: this is loss of quadratic control, and the generic mode count cannot be assigned to that endpoint.

The scope is the local bulk spectrum. Boundary conditions are not needed to obtain these equations, masses, constraints or relative kinetic signs. Selecting global modes, allowed AdS falloffs, boundary symplectic flux or renormalized boundary norms would require an additional boundary problem. In particular, no choice has been made for the scalar's $`z^2\log z`$ data.

| Procedure step | Calculation file |
|---|---|
| 6. Complete raw quadratic action | [STEP_06_RAW_QUADRATIC_ACTION.md](../../../quadratic_action.md) |
| 7. Original unprojected equations | [STEP_07_LINEARIZED_EQUATIONS.md](STEP_07_LINEARIZED_EQUATIONS.md) |
| 8. New-calculation checks | [STEP_08_QUADRATIC_CHECKS.md](STEP_08_QUADRATIC_CHECKS.md) |
| 9. Field status and constraints | [STEP_09_FIELD_STATUS_AND_CONSTRAINTS.md](STEP_09_FIELD_STATUS_AND_CONSTRAINTS.md) |
| 10. Gauges and residual transformations | [STEP_10_GAUGES_AND_SECTOR_MAPS.md](STEP_10_GAUGES_AND_SECTOR_MAPS.md) |
| 11. Diagonalization, signed roots and original-field reconstruction | [STEP_11_ROOTS_AND_EIGENFIELDS.md](../../../details/masses_and_eigenfields.md) |
| 12. Local kinetic signs and stability tests | [STEP_12_NORMS_AND_STABILITY.md](../../../details/kinetic_norms.md) |
| 13. Critical endpoint and limits | [STEP_13_CRITICAL_LOCI_AND_LIMITS.md](../../../details/critical_branches.md) |
| 14. Physical DoF and final spectrum table | [STEP_14_SPECTRUM_AND_DOF.md](../../../spectrum.md) |

The full raw action is (6.30)–(6.32), the diagonal scalar–metric block is (11.3), the form solution is (10.5), and the diagonal fermionic action is (11.12). The final spectrum table includes eigenfields, operators, local signs, stability tests, boundary scope, DoF and the endpoint limitation.

## Detailed source calculations

- [SOURCE_TERM_LEDGER.md](SOURCE_TERM_LEDGER.md) routes all 1184 higher-derivative outer terms.
- [FERMIONIC_CALCULATIONS.md](../../../details/fermionic_reduction.md), FC1–FC15, expands all fermionic descendants and collects the Weyl and LOG terms.
- [FERMION_COMPONENT_SUMS.md](FERMION_COMPONENT_SUMS.md) displays the separate contributions and cancellation sums for every nonzero coefficient pattern of the 48-component graded operator.
- [Fermionic expansion explanation](../support/gb-splus-fermionic-expansion-EXPLAIN.md), F1–F39, derives the two-derivative and Weyl terms and independently checks the field shift.
- [Form derivative check](../support/part2_form_derivative_check.md) and [fermionic descendant check](../support/part2_fermion_descendant_check.md) contain the independent detailed coefficient checks.
- [Method explanation](../support/gb-splus-spectrum-method-EXPLAIN.md) explains fluctuation order, local boundary scope and the branch's Killing-spinor condition.

The [verification report](../../CLAIMS.md) records the exact reproducible checks. The checks concern the local perturbative calculation. The action-source qualifications remain applicable; this is not a nonlinear supersymmetry certificate.

The [representation check](../../../details/multiplets.md) matches the full energy/spin/charge content to one massless gravity multiplet and one massless vector multiplet, with explicit vector combinations $`A-2Q`$ and $`A+4Q`$. Its [exact checks](../../outputs/representations.json) pass.
