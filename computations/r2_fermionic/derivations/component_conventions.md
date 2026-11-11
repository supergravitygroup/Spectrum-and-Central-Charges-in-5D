# Conventions and scope for the fermionic R² branch

**Status: inherited convention inputs, not a new action certification.**

The [shared conventions](../../../CONVENTIONS.md) fix the geometry, spinors and
index rules used below. The [component construction](../../../r2/action/details/construction.md)
states the map, BF insertion and normalization. Source symbols are retained
until the stated convention conversions are applied.

| Item | Working input | Source / limit |
|---|---|---|
| Dimension and supersymmetry | D=5, N=2 in the Özkan/Proeyen convention | Gold uses the label 5D N=1 for the same minimal eight-supercharge setting; do not change field content by counting the label |
| Signature | eta=diag(-,+,+,+,+) | Copied source ledger Sec. 2; handoff Sec. 2.1 |
| Curved/tangent indices | mu,nu and a,b = 0,…,4 | Same |
| SU(2) indices | i,j=1,2 | Distinct from vector-type labels B,C |
| Symmetrization | Unit weight, including factors 1/2 and 1/n! | Handoff Sec. 2.2; Proeyen App. A |
| Curvature | R^rho_{sigma mu nu}=2 partial_[mu Gamma^rho_{nu]sigma}+2 Gamma^rho_[mu\|lambda\| Gamma^lambda_{nu]sigma}; Ricci R_mu nu=R^rho_{mu rho nu} | Handoff Sec. 2.4; retain its sign consistently |
| Orientation | Orthonormal epsilon^{01234}=+1, epsilon_{01234}=-1 | Handoff Sec. 2.3; define coordinate symbol versus tensor explicitly in every density |
| Gamma matrices | {gamma_a,gamma_b}=2 eta_ab; gamma^{abcde}=i epsilon^{abcde}1 | Handoff Sec. 3.1; Proeyen App. A |
| Gamma dot | gamma·T=gamma^{ab}T_ab, no extra factorial | Handoff Sec. 3.1 |
| Fermions and SUSY parameters | Grassmann odd symplectic Majorana | Handoff Sec. 3.2; Proeyen App. A |
| Spinor bar | Operational Majorana bar; do not change to Dirac bar without phase conversion | Handoff Sec. 3.2 |
| Spinor flips | Fixed-index t0=t1=+1, t2=t3=-1; NW-SE-contracted flips include an additional minus sign | Handoff Sec. 3.3; no implicit reorderings |
| Units | hbar=c=1 bookkeeping | No scale or parameter value fixed |
| Coupling | lambda_R2 multiplies Gold Eq. (12a) in the eventual bosonic output convention; [lambda_R2]=-2 | `R2-GOLD12-OFFSHELL-v1`; map/BF conversion in the linked component construction |
| Vector labels | B,C in {1,2}, selected output A=1 | [Multiplet selection](../inputs/reference/r2/notes/multiplet_selection.json) |
| Fermion order | Full target; no automatic quadratic truncation | The action is retained up to quadratic order in the fermions |

The inherited NW-SE index convention is

```math
X^i=\varepsilon^{ij}X_j,\qquad
X_i=X^j\varepsilon_{ji},\qquad
\varepsilon_{12}=\varepsilon^{12}=1.
```

Never lower a single index by replacing epsilon with delta. Distinguish fixed-index flips from contracted flips and keep the order of every Grassmann factor.

## Gauge timing and dependencies

The current procedure is `notes/00_action_construction_framework.md`, lock `R2-PRIMED-BF-CONSTRUCTION-FRAMEWORK-v1`. Vector label 1 is primed (earlier linear-to-vector composite); label 2 is unprimed (Gold defining vector). The new linear output is primed. Both vector maps use the same original unprimed linear multiplet. Retain the two vector roles and their derivatives until the different maps are applied after BF insertion; no componentwise identification is prescribed. Every background T, chi and D occurrence is gauged Coomans, including inside supporting structures.

The later Gold-frame comparison gauge is

```math
\sigma=1,\quad b_\mu=0,\quad\psi^i=0,\quad
L^{ij}=\delta^{ij}L/\sqrt2,\quad
V_\mu{}^{ij}=V_\mu^{\prime ij}+\tfrac12\delta^{ij}V_\mu.
```

This is a target gauge declaration, not a substitution performed during setup. The gravitino psi_mu^i and seed compensator fermion varphi^i remain. Keep full SU(2) connections before expanding gauge-covariant derivatives; D psi need not vanish when psi=0.

The second-order superconformal spin connection, S connection phi_mu^i, and K connection f_mu^a are dependent. The spin connection still contains gravitino contorsion on the psi^i=0 slice. Do not replace it with Levi-Civita in a fermionic calculation. Keep ordinary field strengths distinct from hatted supercovariant completions.

The parent bosonic Gold convention uses H^{ab}=-epsilon^{abcde}H_cde/12 and the constrained three-form origin of E_a. These bosonic formulas are not substitutes for their full fermionic completions.

## Project corrections and unresolved conventions

## Authorized Step 4 gauge restriction

The lower-index derivative of the zero gaugino has +g L_ij psi_mu^j/2, while the upper-index expression has -g L^ij psi_mu_j/2, by NW–SE lowering. Its remaining terms are gamma-dot-hatted-G psi_mu/4 minus gamma-dot-T psi_mu minus phi_mu. Box_c sigma retains 2 f_a^a and its gravitino terms. Hatted G retains i bar-psi_[mu psi_nu]/2. All these are explicitly derived in Step 4. The gravitino, original linear fermion and primed gaugino are retained.

The machine `covariant_derivative_sign` entry explicitly points to Coomans (2.16)–(2.17), with scalar derivative `(partial_mu-b_mu)rho-i barpsi_mu lambda/2`, and the full spin/SU(2)/S/K connections already displayed in Steps 2 and 4. This records the existing source definition; it introduces no new derivative convention.

## Step 5 local alignment and potential

`R2-GOLD25-LOCAL-ALIGNMENT-v1`: in addition to Gold (7), $`L_{ij}=\delta_{ij}L/\sqrt2`$, $`L>0`$, with $`V_\mu{}^{ij}=V'_\mu{}^{ij}+\delta^{ij}V_\mu/2`$. Keep the full derivative displayed in Step 5; $`\varphi_i`$ and $`\psi_\mu{}^i`$ survive. The trace connection $`V_\mu`$ is distinct from the matrix of entries $`V_\mu{}^{ij}`$. No new physical alias is defined.

`R2-COMPOSITE-POTENTIAL-GOLD25-v1` fixes the exact local representative in Step 5. Its source proof and exhaustive Clifford/exterior coefficient checks preserve contorsion and all explicit fermion orders. A potential gauge gradient changes BF only by the explicitly displayed constrained-form boundary term. The formula is local and excludes $`L=0`$ and unaligned triplet directions.

`R2-PRIMED-COMPOSITE-INSERTION-v1` is the current scoped endpoint. It retains complete implicit common gauged slots; normalized full-action certification remains Step 6.

## Supercovariant action representation

The action is presented in `R2-PRIMED-SUPERCOVARIANT-EXPLICIT2-v1` and `notes/11_primed_insertion_supercovariant_two_fermions.md`. Only primed component definitions are inserted; their outer products are distributed and contractions collected. Supercovariant operators, their product arguments and full gauged background composites are retained. This representation does not expand elementary fields or connections. The displayed order is zero/two explicit fermions; full retained operators contain implicit completions. The elementary representation and the separate bosonic Eq. (C13) are retained as comparison records.

## Bilinear collection conventions (v2)

Unit-weight symmetrization acts before raising SU(2) indices. In particular, the fixed-index vector bilinear is symmetric and its epsilon-contracted identical-spinor singlet vanishes. The fixed-index scalar flip is positive, while the contracted scalar flip is negative. The general triplet identities use the same full covariant norm derivative $`L\mathcal D_aL=L^{ij}\mathcal D_aL_{ij}`$. No triplet derivative is discarded by alignment. Explicit epsilon is used where a displayed symmetry pair would otherwise mix variances; the order of Clifford matrices inside collected coefficients is retained. The checks use linked Majorana bars, unlike the independent-bar tensor samples.

## AdS spectrum conventions — 2026-09-15

Note 13 fixes $`k=-\ell^{-2}=-g^2L_0^2/2`$, $`N_0=-3gL_0^2/2`$, $`\beta=\lambda g^2=4(L_0-1)/(3L_0^2)`$, $`\Phi=4-3L_0`$ and $`x=\sqrt{(4-L_0)/(2(L_0-1))}`$. The positive-residue patch is $`x>2`$. Bosonic $`M=m^2\ell^2`$ is the representation mass, with curvature shifts retained in vector/TT operators; fermionic $`m\ell`$ is the signed Dirac parameter. The background derivative acts only after all nonlinear supercovariant completions have entered note12. Scalar/fermion normal coordinates are projections in their kinetic forms, not Euclidean projections. The $`q=\pm1`$ charge branches form one symplectic-Majorana doublet and are counted once. New field combinations and parent variables are defined with inverse maps in note13; they do not change the original multiplet assignment.
