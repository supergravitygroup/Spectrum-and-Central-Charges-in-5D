<a id="step-12--local-kinetic-signs-stability-and-boundary-dependence"></a>

# Local kinetic signs, stability and boundary dependence

<!-- ASSERT_CONVENTION: natural_units=true, metric_signature=(-,+,+,+,+), curvature=GB04, action_lock=GB-FERMION-ACTION-0+2-v1, convention_lock=GB-FERMION-SPECTRUM-CONVENTIONS-v1, coupling_dimension=-2, fermion_bar=linear_Majorana -->

Generic reduction uses $`0<x<2`$; the endpoint $`x=2`$ is assessed directly in the raw quadratic action. Global boundary modes and renormalized boundary norms are outside this scope.

<a id="121-kinetic-normalization"></a>

## Kinetic normalization

With $`\kappa_5^2>0`$ as reference, the Einstein graviton coefficient in (11.3) is $`c=2-x`$. It is positive for $`0<x<2`$. The scalar normalization inside the common action factor is

```math
\ell_{\rm can}=\sqrt{\frac{2c}{3x^2}}\,\ell,\qquad \mathcal L^{(2)}_0=-\frac12(\nabla\ell_{\rm can})^2-\frac12m_0^2\ell_{\rm can}^2,\qquad m_0^2=4k.
\tag{12.1}
```

The normalization is singular at $`c=0`$, so it is not extended there. For two scalar solutions, varying this action gives the conserved bulk symplectic current

```math
\omega^\mu(\ell_1,\ell_2)=\frac1{2\kappa_5^2}\frac{2c}{3x^2}\left(\ell_1\nabla^\mu\ell_2-\ell_2\nabla^\mu\ell_1\right),\quad \nabla_\mu\omega^\mu=\frac c{3\kappa_5^2x^2}\left(\ell_1\Box\ell_2-\ell_2\Box\ell_1\right)=0.
\tag{12.2}
```

This coefficient establishes the local kinetic sign after mixing is removed. A global conserved inner product additionally requires suitable flux conditions and, when necessary, boundary counterterms. The Majorana bar in the fermion action is an algebraic pairing, not that physical inner product.

<a id="122-scalar-curvature-bound-and-local-falloffs"></a>

## Scalar curvature bound and local falloffs

Define the AdS radius $`\mathcal L`$ by $`k=-\mathcal L^{-2}`$. Then $`m_0^2\mathcal L^2=-4`$. To see the boundary exponents directly, use the local Poincaré metric $`ds^2=\mathcal L^2z^{-2}(dz^2+\eta_{mn}dx^m dx^n)`$. The radial scalar Laplacian is

```math
\Box\ell=\mathcal L^{-2}(z^2\partial_z^2-3z\partial_z+z^2\eta^{mn}\partial_m\partial_n)\ell,\qquad \ell\sim z^\Delta\ \Longrightarrow\ \Delta(\Delta-4)=m_0^2\mathcal L^2.
\tag{12.3}
```

For this scalar the indicial equation is $`(\Delta-2)^2=0`$, giving $`\ell\sim z^2[A(x^m)+B(x^m)\log z]`$. It lies at the AdS₅ scalar BF threshold. The repeated radial exponent does not imply an extra bulk degree of freedom or an additional root of the second-order wave equation. Whether the logarithmic coefficient is admitted depends on the boundary problem. No global stability or positive renormalized norm is claimed without specifying it.

The massless graviton has the positive local Einstein kinetic sign for $`c>0`$. The form and fermion local tests follow below.

<a id="123-form-kinetic-signs-and-the-dualization-sign"></a>

## Form kinetic signs and the dualization sign

After the multiplier constraint and gauge solution, the local bosonic form action is

```math
\mathcal L^{(2)}_{A,b}=-\frac c2G^2-\frac c3(db)_{\mu\nu\rho}(db)^{\mu\nu\rho}.
\tag{12.4}
```

The reference healthy actions are $`-F^2/4`$ and $`-H_3^2/12`$. Thus $`A_{\rm can}=\sqrt{2c}\,A`$ and $`b_{\rm can}=2\sqrt c\,b`$ have positive local signs for $`c>0`$. In particular the positive $`+4cH_2^2`$ before dualization is not a ghost: $`H_2`$ was a Hodge dual of a three-form strength, not an independently varied Maxwell field.

For a direct dual-vector norm calculation introduce an independent two-form $`Y`$ in a first-order action,

```math
\mathcal L_{\rm first}=4cY^2-8cY^{\mu\nu}F_{\mu\nu}(Q),\qquad \delta_Y\mathcal L_{\rm first}=8c(Y-F(Q))^{\mu\nu}\delta Y_{\mu\nu},\qquad \delta_Q\mathcal L_{\rm first}\doteq16c\nabla_\mu Y^{\mu\nu}\delta Q_\nu.
\tag{12.5}
```

The $`Q`$ equation imposes $`\nabla\cdot Y=0`$, locally $`Y=-*db/2`$, reproducing the two-form formulation up to its explicitly generated boundary term. Eliminating $`Y=F(Q)`$ gives $`4cF(Q)^2-8cF(Q)^2=-4cF(Q)^2`$, so $`Q_{\rm can}=4\sqrt c\,Q`$ has the healthy Maxwell sign. Substitution of the solution $`H=dQ`$ into $`+4cH^2`$ alone would omit the Legendre term and reverse this conclusion.

These two massless Maxwell fields have the ordinary local gauge-invariant propagation with positive kinetic signs. Their normal-mode frequencies, allowed asymptotic data and boundary symplectic norms remain dependent on a global boundary problem, which has not been selected.

<a id="124-fermionic-kinetic-signs-and-local-ads-parameters"></a>

## Fermionic kinetic signs and local AdS parameters

After the full mixing has been removed, (11.12) has kinetic weights $`c`$ and $`2c/(3x^2)`$ relative to $`-\bar\Upsilon\gamma\nabla\Upsilon`$ and $`-\bar\zeta\not\nabla\zeta`$. Fix the healthy two-derivative theory at $`x=c=1`$, $`\kappa_5^2>0`$, as the common fermionic sign reference. The canonically scaled fields are

```math
\Upsilon_{{\rm can},a}=\sqrt c\,\Upsilon_a,\qquad \zeta_{\rm can}=\sqrt{\frac{2c}{3x^2}}\,\zeta,\qquad Z_{3/2}=c>0,\quad Z_{1/2}=\frac{2c}{3x^2}>0.
\tag{12.6}
```

These positive rescalings preserve the reference local kinetic signs in the whole interior. Equivalently the symplectic currents obtained by varying the first-order derivative terms are the reference Rarita–Schwinger and Dirac currents multiplied by these weights. The algebraic Majorana bar alone does not define a Hermitian one-particle norm. This is a relative bulk sign result, not an assertion about a renormalized boundary inner product.

The signed parameters are real: $`\mu_{3/2,s}=3sm`$, $`\mu_{1/2,s}=sm`$, with $`|m|\mathcal L=1/2`$. The gravitino obeys the massless AdS gauge identity, so its magnitude $`|\mu_{3/2,s}|\mathcal L=3/2`$ is the gauge value, not an additional massive pole. The spinor magnitude is $`|\mu_{1/2,s}|\mathcal L=1/2`$ and has no imaginary local mass. To exhibit its falloffs, in the Poincaré frame $`\not\nabla=\mathcal L^{-1}[\gamma^z(z\partial_z-2)+z\gamma^m\partial_m]`$. For a radial eigenspinor $`\gamma^z\zeta_t=t\zeta_t`$, $`t=\pm1`$, the leading equation is

```math
[t(\Delta-2)+\mu_{1/2,s}\mathcal L]\zeta_t=0,\qquad \Delta=2-t\mu_{1/2,s}\mathcal L\in\left\{\frac32,\frac52\right\}.
\tag{12.7}
```

Both are local exponents. Which coefficient is fixed or fluctuating and whether boundary logarithms or alternative data are admitted requires an additional boundary prescription. At this stage the scalar saturates its curvature bound, the vectors and graviton have their gauge-invariant massless operators, and the fermionic signed parameters are real with positive relative bulk weights. No global stability claim is made for arbitrary boundary conditions.
