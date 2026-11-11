# Step 9 — Field status and constraints

<!-- ASSERT_CONVENTION: natural_units=true, metric_signature=(-,+,+,+,+), curvature=GB04, action_lock=GB-FERMION-ACTION-0+2-v1, convention_lock=GB-FERMION-SPECTRUM-CONVENTIONS-v1, coupling_dimension=-2, fermion_bar=linear_Majorana -->

Generic reduction uses $`0<x<2`$; the endpoint $`x=2`$ is assessed directly in the raw quadratic action. Global boundary modes and renormalized boundary norms are outside this scope.

## 9.1 Algebraic scalar

The $`n`$ equation contains no derivative. At $`c\ne0`$ and finite $`x>0`$ its coefficient $`-4c/x^2`$ is invertible, so

```math
\mathcal E_n=-\frac{4c}{x^2}(n+2gx\ell)=0\quad\Longrightarrow\quad n=-2gx\ell.
\tag{9.1}
```

This conclusion comes from the GB quadratic action. Substituting it is equivalent to completing the square:

```math
-4cg^2\ell^2-\frac{8cg}{x}\ell n-\frac{2c}{x^2}n^2=-\frac{2c}{x^2}(n+2gx\ell)^2+4cg^2\ell^2.
\tag{9.2}
```

At $`c=0`$ the entire displayed scalar–metric block is zero. Equation (9.1) then cannot be imposed: no quadratic equation fixes $`n`$. Loss of quadratic control does not prove a new nonlinear gauge symmetry.

## 9.2 Metric constraints

The five identities $`\nabla^\mu\mathcal E_{\mu\nu}=0`$ are the linear diffeomorphism Noether identities. The trace mixes $`h`$ and $`\ell`$ through (7.5); it is not a reason to set $`\ell=0`$. The scalar propagates after diagonalization in Step 11. Its positive-looking gradient coefficient in the raw block does not determine its norm before metric mixing is removed.

## 9.3 Form, connection and fermion status

The constrained current $`p`$ is a derivative of the independent three-form. Its status must be read from the complete coupled form action. The cancellation of the two explicit $`\widehat R(V)^2`$ seed monomials, $`2/3-2/3=0`$, does not by itself prove that $`v`$ or $`v'`$ is algebraic: covariant compensator derivatives and mixed derivative terms also contain these fields. The analogous warning applies to the compensator spinor and longitudinal gravitino. Their status follows from the complete blocks, as recorded in §§9.4–9.5.

## 9.4 Form constraints from the completed bosonic block

For $`c\ne0`$, (7.7) imposes $`p=0`$ and $`v'=0`$. This follows from the full coefficient collection, not the labels of these fields in the two-derivative theory. The current $`p`$ has no surviving kinetic term; the apparent higher-derivative $`A\Box j_H`$ term canceled in (6.24)–(6.27). The trace connection $`v`$ is a multiplier before solving the three-form equation.

With $`p=0`$, the remaining form equations are $`j_G=0`$, $`dH=0`$, and $`F(v)=\sqrt2gx(2H-G)`$. They determine the curl of $`v`$, while its gradient is an abelian gauge freedom. The two-form and graviphoton each propagate. The independent three-form has no extra local initial data: $`p=0`$ implies $`de_3=0`$, and on a contractible patch $`e_3=d\Lambda_2`$ is a form gauge transformation. This local statement retains possible global cohomology sectors outside the chosen scope.

At $`c=0`$ all these raw equations vanish. The generic multiplier constraint $`p=0`$ and the solution $`v'=0`$ cannot be imported to that point.

## 9.5 Fermionic field status

The raw block (6.31) is first order in derivatives after the complete higher-derivative collection. Its gravitino derivative symbol has the local supersymmetry null directions verified in Step 10. The independent spinor has derivative mixing with the gamma trace; neither can be classified by its raw diagonal coefficient alone.

The algebraic, invertible change $`\Psi_a=\Upsilon_a+i\sqrt2\gamma_aJ\zeta/(3x)`$ in Step 11 separates a massless AdS gravitino and a first-order spinor. Its only denominator is $`x`$, which is nonzero throughout the branch. For $`c>0`$ the spinor kinetic coefficient is $`-2c/(3x^2)`$ and does not vanish. Thus $`\zeta`$ propagates. The gravitino gamma trace is a local gauge variable and its divergence is constrained by the gamma-traced equation; they are not two separately removable spinor modes.

The dependent $`\phi_a`$ and $`\chi`$ in Step 6 never become independent initial data. Their derivative appearances cancel to (6.31). At $`c=0`$ the complete fermionic quadratic action is zero, so neither the generic first-order equations nor their gauge-reduced count supplies a spectrum at the endpoint.
