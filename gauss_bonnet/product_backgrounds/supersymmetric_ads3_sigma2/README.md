# Supersymmetric AdS3 × Sigma2: bosonic quadratic spectrum

This chapter supplies the calculations cited in paper Section 4.2
(repository citation 24). It gives the bosonic quadratic matrices,
their physical divisors, special harmonic levels and primary-norm evidence
for the regular Gauss–Bonnet BPS family. The executable
[calculation package](../../../computations/gb_ads3_sigma2/README.md) keeps the
couplings symbolic.

| Step | Result |
|---|---|
| [Action inputs](action_inputs.md) | Current-source correspondence, normalization, form identities and BPS branch |
| [Quadratic actions](quadratic_actions.md) | Every amplitude and matrix, gauge null directions, exact physical-divisor certificate |
| [Generic levels](generic_levels.md) | Cubic, quintic, partner factors, charged modes and both chiralities |
| [Special levels](special_levels.md) | Fixed-flux constant reduction, sphere j=1, torus, harmonic one-forms and quadratic differentials |
| [Norms and multiplets](norms_and_multiplets.md) | Signed propagator residues, double flat root, analytic sign rules, finite-sample coverage |
| [Exceptional backgrounds and tower criterion](../../../computations/paper_extra_checks/README.md) | Checks of the statements in Sections 4.1, 4.3 and 4.5; no exceptional-family spectrum |
| [Figures 2 and 3](../../../figures/README.md) | Background-family plot and bosonic towers from the existing formulas and data |

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

## Fermionic continuation

Repository citation 25 in Section 4.6 supplies the
[complete coupled quadratic action](fermionic_quadratic_action.md) and
[source and derivative dictionary](fermionic_action_inputs.md).
Repository citation 26 in Section 4.6 supplies the separate [fermionic spectrum](fermionic_spectrum.md):
polynomial operators, numerical rank and root tests, and fixed-charge
matching with the bosonic multiplets above. Its numerical sample domain
and two-derivative limits are stated there; they do not convert the
bosonic evidence on this page into a fermion-norm calculation.
