# Step 8 — Checks of the new quadratic calculation

<!-- ASSERT_CONVENTION: natural_units=true, metric_signature=(-,+,+,+,+), curvature=GB04, action_lock=GB-FERMION-ACTION-0+2-v1, convention_lock=GB-FERMION-SPECTRUM-CONVENTIONS-v1, coupling_dimension=-2, fermion_bar=linear_Majorana -->

Generic reduction uses $`0<x<2`$; the endpoint $`x=2`$ is assessed directly in the raw quadratic action. Global boundary modes and renormalized boundary norms are outside this scope.

## 8.1 Algebra and dimensions

The scalar potential is differentiated independently in the checker. It verifies $`F_0=1`$, $`F'_0=c/x`$, $`K_0=c/x^2`$, the three coefficients in (6.17), and the constant-conformal metric Hessian. It also checks the reduction in Step 11 and the ungauged/two-derivative limits. Each term in (6.18) has dimension two: $`[h]=[\ell]=[x]=[c]=0`$, $`[n]=[g]=1`$, $`[k]=2`$, $`[\lambda]=-2`$.

The trace and divergence identities in (7.5) follow using the same commutator convention as (6.14). Mixed variation of $`c\ell r/x`$ with respect to $`h`$ and $`\ell`$ gives adjoint operators $`cP/x`$ and $`c\delta R/x`$. Equation (7.2) displays their boundary difference. The $`\ell,n`$ off-diagonal entries both equal $`-8cg/x`$; there is no asymmetric Hessian entry.

## 8.2 An independent trace expansion

For constant $`h=s\bar g`$, the original curvature invariants have powers $`(1+ts)^{3/2}`$ and $`(1+ts)^{1/2}`$ after multiplication by the measure; the potential has power $`(1+ts)^{5/2}`$. The exact Taylor coefficients are $`3/8,-1/8,15/8`$. Inserting the branch values yields $`-15kc\,s^2`$, while (6.18) gives $`-c(5s)(6ks)/2=-15kc\,s^2`$. This checks the measure and zero-derivative metric terms by a distinct expansion.

## 8.3 Scope of verification

The scalar–metric, form and fermionic checks are separate calculations. Their results and exact reproduction paths are collected below; no single projected block is used to certify another.

## 8.4 Complete sector checks

The [source ledger](SOURCE_TERM_LEDGER.md) routes all 1184 higher-derivative outer terms. The two-derivative action is expanded explicitly in §6.3, §6.8 and the companion's F1–F22. Vanishing background coefficients are used only after checking possible implicit descendants. In particular zero gauge-fixed $`\psi`$ and constant $`L^{ij}`$ do not set their covariant derivatives to zero.

The [form check](../support/part2_form_derivative_check.md) independently calculates the K-connection terms, derivative transfers, current mixings and the complete form coefficients. The [fermionic descendant check](../support/part2_fermion_descendant_check.md) derives the weight and Q/S/K terms in the second derivatives and $`\Box^cN`$. The two-slot Clifford operator is independently evaluated by [the exact component script](../../calculations/fermion_operator.py): all $`48^2`$ entries agree at five exact radial test values. The [component table](FERMION_COMPONENT_SUMS.md) shows the polynomial arithmetic rather than hiding this last collection.

The maximum derivative order before collection is three. Four exact values determine every cubic polynomial; the fifth checks that interpolation. The Lorentz-covariant derivative symbol is tested without imposing equations or gravitino constraints, and the spin and tensor connection terms retain the AdS curvature commutators. The parameter-restoration argument is FC10–FC15. The scalar–metric/form checks and the fermionic shift, Noether, residual-gauge and reconstruction checks are reproducible through [the reduction script](../../checks/reference_reduction.py).

For the graded Hessian $`K(s)=B(s)-B(4-s)^T`$, $`K(s)+K(4-s)^T=0`$ follows by substitution; this checks both varied slots and the radial measure adjoint. The covariant bosonic identity is $`\nabla^\mu\mathcal E_{\mu\nu}=0`$, and the fermionic one is (10.9). Reconstruction in Step 11 tests the full equations, including the independent spinor equation and the constrained three-form variation.

## 8.5 Verification scope

The local bulk checks identify the endpoint as loss of quadratic control. They do not establish global normalizability, boundary flux or a renormalized AdS inner product.
