<a id="step-13--spectral-critical-loci-and-limits"></a>

# Spectral critical loci and limits

<!-- ASSERT_CONVENTION: natural_units=true, metric_signature=(-,+,+,+,+), curvature=GB04, action_lock=GB-FERMION-ACTION-0+2-v1, convention_lock=GB-FERMION-SPECTRUM-CONVENTIONS-v1, coupling_dimension=-2, fermion_bar=linear_Majorana -->

Generic reduction uses $`0<x<2`$; the endpoint $`x=2`$ is assessed directly in the raw quadratic action. Global boundary modes and renormalized boundary norms are outside this scope.

<a id="131-the-endpoint-a-12"></a>

## The endpoint $`a=-1/2`$

Here $`x=2`$, $`c=0`$, $`N_0=-6g`$ and $`k=-2g^2`$. Direct substitution into (6.18) makes every scalar–metric quadratic coefficient zero:

```math
S^{(2)}_{h,\ell,n}\big|_{a=-1/2}=0,\qquad \mathcal E_{\mu\nu}=\mathcal E_\ell=\mathcal E_n=0.
\tag{13.1}
```

Consequently $`n=-2gx\ell`$ cannot be imposed at this endpoint; it was obtained by dividing by $`c`$. The generic canonical normalizations also fail. This is a loss of quadratic control in this block, not a proof that the nonlinear theory has no local degrees of freedom. Sections 13.4–13.5 establish the same zero for the other sectors.

<a id="132-two-derivative-and-small-coupling-limits"></a>

## Two-derivative and small-coupling limits

At $`\lambda\to0`$ with $`g`$ fixed, $`a\to0`$, $`x\to1`$, $`c\to1`$, $`k\to-g^2/2`$. Thus

```math
S^{(2)}_{H,\ell}\longrightarrow\frac1{2\kappa_5^2}\int\bar e\left[-\frac12H^{\mu\nu}\mathcal G^L_{\mu\nu}(H)-\frac13(\nabla\ell)^2+\frac23g^2\ell^2\right],\quad n\longrightarrow-2g\ell,\quad m_0^2\longrightarrow-2g^2.
\tag{13.2}
```

The exact root (6.1) expands as $`x=1-a/2+a^2/2+O(a^3)`$, $`c=1+a/2-a^2/2+O(a^3)`$, and $`k=-g^2[1-a+5a^2/4+O(a^3)]/2`$. These are expansions of the exact finite-action result; they are not used to manufacture or discard heavy roots.

<a id="133-ungaugedflat-limit-on-this-branch"></a>

## Ungauged/flat limit on this branch

Take $`g\to0`$ at fixed finite $`\lambda`$. Then $`a\to0`$, $`x\to1`$, $`N_0\to0`$, $`k\to0`$, and the branch reaches the $`L=1`$ member of GB-U. The scalar becomes massless and the metric equation becomes the flat massless graviton equation. This specified limit does not cover a scaling with $`a`$ fixed and $`\lambda\to\infty`$.

As $`a\to+\infty`$, $`x\to0^+`$ and the compensator patch boundary is approached only as a limit. It is not a finite-$`a`$ zero of $`c`$ and is not inserted as a regular background in formulae involving $`1/x`$.

No additional scalar–metric mass collision occurs in the interior: $`m_0^2/k=4`$ throughout, and the local kinetic factors are nonzero. The remaining sectors are included in §§13.4–13.5.

<a id="134-completion-of-the-bosonic-endpoint-and-limit-analysis"></a>

## Completion of the bosonic endpoint and limit analysis

Equation (6.30) has the same overall factor $`c`$ in every bosonic sector. Thus at $`a=-1/2`$ the **entire bosonic Hessian** vanishes, not just its metric projection. This is established without dividing by $`c`$. Generic constraints and the generic twelve-boson count fail there. The separate fermionic calculation (6.31) establishes the same overall factor.

For $`0<x<2`$ every bosonic algebraic denominator is a product of powers of $`x`$ and $`c`$, and both physical form sectors have kinetic factors proportional to $`c`$. There is no further bosonic rank change or norm zero in the interior. The scalar stays at $`m^2\mathcal L^2=-4`$, and all vector and graviton masses remain zero. The scalar bound is saturated throughout the branch, rather than crossed at an isolated coupling.

The two-derivative limit of (6.30) is obtained by $`x=c=1`$. In the fixed-$`\lambda`$ ungauged limit, $`g\to0`$ gives $`F(v)=0`$, while $`G`$ and $`H`$ remain independent massless form strengths. The multiplier still imposes $`p=0`$ because $`c/x\to1`$; it is not permissible to infer a new three-form polarization from the vanishing of $`g`$ alone.

<a id="135-full-fermionic-criticality-and-limiting-spectrum"></a>

## Full fermionic criticality and limiting spectrum

The raw (6.31), not its equations divided by $`c`$, gives

```math
\ell_B^{(2)}\big|_{x=2}=\ell_F^{(2)}\big|_{x=2}=0,\qquad S^{(2)}\big|_{a=-1/2}=0.
\tag{13.3}
```

Thus the background merger GB-E is also a complete quadratic kinetic degeneracy. Every Euler equation obtained at this order vanishes. The generic scalar/form eliminations and gravitino wave equation cannot be extended to that point. The linear theory alone does not determine the nonlinear physical count, interactions, a new gauge symmetry, or a weakly coupled spectrum there. There is no nonzero Jordan block from which to infer a new logarithmic bulk particle.

For every finite interior coupling, $`x>0`$ and $`c>0`$. The algebraic spinor shift has denominator $`x`$ only; the physical kinetic factors are positive multiples of $`c`$ or $`c/x^2`$. Neither fermionic operator has higher degree or additional roots, and $`|\mu_{1/2}|\mathcal L=1/2`$, $`|\mu_{3/2}|\mathcal L=3/2`$ stay fixed. Hence there is no extra isolated spectral critical locus in the interior. Scalar BF saturation is branch-wide and is distinct from the endpoint kinetic degeneracy.

At $`\lambda\to0`$ with $`g`$ fixed, $`x=c=1`$, $`m=g/(2\sqrt2)`$, and (11.12) is the directly derived two-derivative diagonal action. At small $`a`$, $`m=g[1-a/2+a^2/2+O(a^3)]/(2\sqrt2)`$. These are expansions of the exact light roots; no $`1/\lambda`$ heavy pole occurs in any sector on this branch.

At $`g\to0`$ with finite $`\lambda`$ fixed, $`m\to0`$, $`k\to0`$, $`x,c\to1`$. Both signed fermionic equations become massless flat-space equations, the gravitino gauge becomes $`\delta\Upsilon_a=\partial_a\epsilon`$, and the spinor remains independent. The scalar also becomes massless. All generic kinetic weights remain finite and nonzero. This limiting count is $`12`$ bosonic and $`12`$ fermionic local DoF.

Taking $`a\to+\infty`$ at fixed nonzero $`g`$ instead sends $`x\to0`$, $`m,k\to0`$, $`c\to2`$. The original compensator field normalizations contain $`1/x`$; $`x=0`$ lies outside the source gauge patch. It is a limiting family, not an additional finite-coupling regular vacuum or spectral critical point.
