# Supersymmetric AdS3 × Sigma2: actions, spectra, norms and central charges

This chapter follows the regular Gauss–Bonnet BPS family through paper
Section 4: the background, bosonic and fermionic operators, their physical
modes, norm conditions and central charges. The bosonic calculation retains
symbolic couplings. The direct fermionic root census is numerical at the
specified samples; its scope is stated at the step where it is used.

| Step | Question, result and continuation |
|---|---|
| 1. [Action and background](action_inputs.md) | Which action, normalization, form identities and BPS branch enter the expansion? These are the inputs to both Hessians. |
| 2. [Bosonic quadratic matrices](quadratic_actions.md) | Expand in independent amplitudes before imposing fluctuation constraints. The saved matrices retain the gauge directions. |
| 3. [Constraints and physical divisors](quadratic_actions.md#exact-divisor-certificate), [generic levels](generic_levels.md) | Use maximal minors and the original constraints to distinguish physical roots from gauge factors; retain the stated invertibility domains. |
| 4. [Fermionic inputs](fermionic_action_inputs.md), [coupled action](fermionic_quadratic_action.md) | Keep gravitino–compensator mixing and full supercovariant derivatives when assembling the operator (paper citation 25). |
| 5. [Direct fermionic roots and multiplet comparison](fermionic_spectrum.md) | Extract roots from the coupled operator, then compare with independently specified bosonic predictions at fixed spin and charge (citation 26). |
| 6. [Norms and bounded towers](norms_and_multiplets.md), [Figure 3](../../../figures/README.md) | Residues determine bosonic norm signs; masses or multiplet matching alone do not determine them. The exact tower criterion has a separate [check](../../../computations/paper_extra_checks/README.md#spin-2-tower). |
| 7. [Special harmonic levels](special_levels.md), [exceptional backgrounds](../../../computations/paper_extra_checks/README.md#exceptional-backgrounds) | Revisit reduced rank, excluded loci and fixed-flux levels using their own equations; do not substitute them into a divided generic result. [Figure 2](../../../figures/README.md) displays the background domain. |
| 8. [Central charges](../../../generic_combination/ads5/anomalies_and_extremization.md#the-ads3-family) | Reduce the Chern–Simons terms with the background flux and extremize the current mixing. This uses the action and background, independently of the numerical root census. |

The [bosonic computation guide](../../../computations/gb_ads3_sigma2/README.md)
attaches commands and saved matrices to steps 2–3 and 6–7 (paper citation 24).
The [fermionic computation guide](../../../computations/gb_ads3_sigma2_fermionic_spectrum/README.md)
attaches commands and sample records to step 5. Follow the same sequence from
a paper equation or from the beginning; these are implementation links within
one calculation, not alternative reading routes.

At a generic level the neutral bosonic modes are three spin-2 states, ten
vectors and five scalars, with two additional charged vector modes. They
form three spin-2, five (1,0) and two flat long multiplets. The last two have
a fermionic lowest component; no fermionic Hessian is inferred from this
bosonic calculation.

The domain is L > 0, g > 0, nonzero k for the generic higher-derivative count,
and P1…P5 nonzero. The k = 0 degree degeneration is stated separately.
The two isolated points with mu ell_s = nu_f = 0 are excluded as in v109.
Simple-pole norm statements also require that the relevant roots have not
collided. Chiral, Einstein-coefficient-zero and projection-chart limits must
be read from the unreduced matrices. Global charged-harmonic multiplicities,
boundary conditions and nonlinear critical spectra are not determined here.
The dashes in paper Table 10 (`tab:light`) remain undetermined.

The same cited paper paragraph is also covered by the explicit
[E-term deletion spectrum](norms_and_multiplets.md) and the
[six standalone W, LOG and R² comparisons](generic_levels.md).
Their numerical evidence and precision guards are separate from the
symbolic GB family and are recorded in the
[product-check log](../../../computations/gb_ads3_sigma2/outputs/product_checks/verification.log).

## Scope of the fermionic calculation

Repository citation 25 in Section 4.6 supplies the
[complete coupled quadratic action](fermionic_quadratic_action.md) and
[source and derivative dictionary](fermionic_action_inputs.md).
Repository citation 26 in Section 4.6 supplies the separate [fermionic spectrum](fermionic_spectrum.md):
polynomial operators, numerical rank and root tests, and fixed-charge
matching with the bosonic multiplets above. Its numerical sample domain
and two-derivative limits are stated there; they do not convert the
bosonic evidence on this page into a fermion-norm calculation.
