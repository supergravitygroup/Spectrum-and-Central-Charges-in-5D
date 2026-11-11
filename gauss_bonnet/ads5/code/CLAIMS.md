# Claims and their supporting records

The recorded checks for Gauss–Bonnet on AdS₅ concern the local quadratic calculation. The table states the mathematical scope of their reported PASS results; the [source and method record](../source_notes.md) distinguishes component evaluations, parameter restoration and symbolic reductions.

| Recorded claim | Derivation or evidence | Calculation | Scope |
|---|---|---|---|
| Assembly of the accepted 0+2 action | GB01–GB20 and the source ledger | Assembly, independent TeX readback, and expression/coefficient comparison | 52 Weyl, 297 covariant LOG, and 835 explicit LOG terms |
| Vanishing tadpoles for Gauss–Bonnet on AdS₅ | Steps 3–5 with arbitrary fluctuations | `background.py` and independent algebraic checks | Tensor reasons for vanishing first variations of other fields appear in the source ledger |
| Raw bosonic Hessian (6.30) | Step 6 and FD1–FD17 | Source sums, 12 coefficients, and 700 Lorentz-component equalities | Bianchi identities and the constrained three-form variation are retained |
| Raw fermionic Hessian (6.31) | FC1–FC15 and SF1–SF19 | 48×48 Euler matrix at five radial values; 60 polynomial groups and 576 nonzero entries; six coefficients | The fixed frame, interpolation, and restoration argument in FC10–FC13 remain source methods; they are not adopted as an unrestricted symbolic check |
| Reconstruction of eigenfields in the original equations | Steps 7 and 9–11 | Scalar/fermion reconstruction, gauge/Noether, three-form, and dualization checks | Local gauge quotient and regular domain $`0<x<2`$ |
| Positive local kinetic weights, BF saturation, and 12+12 local DoF | Steps 12–14 | Diagonal coefficients, symbolic positivity parametrization, little-group count, and dimensions | Signs are relative to the fixed positive Einstein/two-derivative reference; no global norm is selected |
| Raw $`S^{(2)}=0`$ at the endpoint | Step 13 | All 18 raw coefficients vanish at $`x=2`$ | This is not a statement of zero nonlinear DoF |
| Local kinematical SUSY 8/8 | E16–E22 and the flat real rank-eight Killing connection | Transformation and integrability residuals | Simply connected local patch |
| Compatibility with short gravity and vector representations | R1–R15 | Energies, shortening, and vector transformation | No full nonlinear SUSY closure claim |

## Source qualifications

The Weyl and two-derivative inputs retain their stated construction and check scopes. See [the two-derivative coefficient derivation](../../../common/two_derivative_action/details/gb_input_qualifications.md) and [action assumptions A1–A6](../../action/gb_splus_action.md). Interactions with four or more physical fermions lie outside the 0+2 action used for the Hessian on a bosonic background.

Global AdS boundary data, the choice of scalar logarithmic falloff, global normal frequencies, topology, and renormalized boundary norms are not part of these local claims.
