# Step 7 — Linearized equations from the quadratic action

<!-- ASSERT_CONVENTION: natural_units=true, metric_signature=(-,+,+,+,+), curvature=GB04, action_lock=GB-FERMION-ACTION-0+2-v1, convention_lock=GB-FERMION-SPECTRUM-CONVENTIONS-v1, coupling_dimension=-2, fermion_bar=linear_Majorana -->

Generic reduction uses $`0<x<2`$; the endpoint $`x=2`$ is assessed directly in the raw quadratic action. Global boundary modes and renormalized boundary norms are outside this scope.

## 7.1 Derivative transfers

Formal self-adjointness of $`\mathcal G^L`$ under compactly supported variations gives

```math
\delta\left(-\frac c2\int\bar e\,h^{\mu\nu}\mathcal G^L_{\mu\nu}(h)\right)=-c\int\bar e\,\delta h^{\mu\nu}\mathcal G^L_{\mu\nu}(h).
\tag{7.1}
```

The two varied slots give equal integrals; this cancels the Taylor $`1/2`$. For the scalar–curvature mixing, transfer its two derivatives:

```math
\int\bar e\,\ell\,\delta r=\int\bar e\,\delta h^{\mu\nu}(\nabla_\mu\nabla_\nu-\bar g_{\mu\nu}\Box-4k\bar g_{\mu\nu})\ell+\int\partial_\mu(\bar e\,J^\mu),
\tag{7.2}
```

```math
J^\mu=\ell\nabla_\nu\delta h^{\mu\nu}-(\nabla_\nu\ell)\delta h^{\mu\nu}-\ell\nabla^\mu\delta h+(\nabla^\mu\ell)\delta h.
\tag{7.3}
```

Also $`\delta[(\nabla\ell)^2]=2\nabla_\mu\ell\nabla^\mu\delta\ell=-2\Box\ell\,\delta\ell+2\nabla_\mu(\delta\ell\nabla^\mu\ell)`$. These transfers require no global boundary condition: they define bulk Euler equations with compactly supported test variations.

## 7.2 Unprojected equations in this block

With $`P_{\mu\nu}=\nabla_\mu\nabla_\nu-\bar g_{\mu\nu}\Box-4k\bar g_{\mu\nu}`$, independent variation of (6.18) gives

```math
\boxed{\mathcal E_{\mu\nu}=-c\mathcal G^L_{\mu\nu}(h)+\frac c xP_{\mu\nu}\ell=0,\qquad \mathcal E_\ell=\frac c x r-\frac{2c}{x^2}\Box\ell-8cg^2\ell-\frac{8cg}{x}n=0,\qquad \mathcal E_n=-\frac{8cg}{x}\ell-\frac{4c}{x^2}n=0.}
\tag{7.4}
```

This is a tensor equation, not merely its transverse-traceless projection. No division by $`c`$ was made. The full metric equation is given by this block once the absence of quadratic scalar–form mixing is established in the remaining source collection.

To check its divergence, the scalar commutator gives $`\Box\nabla_\nu\ell-\nabla_\nu\Box\ell=4k\nabla_\nu\ell`$. Therefore $`\nabla^\mu P_{\mu\nu}\ell=0`$, and hence $`\nabla^\mu\mathcal E_{\mu\nu}=0`$. For its trace use $`\bar g^{\mu\nu}\mathcal G^L_{\mu\nu}=-3r/2`$:

```math
\bar g^{\mu\nu}\mathcal E_{\mu\nu}=\frac{3c}{2}r-\frac c x(4\Box+20k)\ell=0.
\tag{7.5}
```

The trace equation is derived from (7.4), and is not an additional independent equation.

## 7.3 Three-form variation must remain constrained

The form block will use $`p^\mu=\nabla_\nu e^{\mu\nu}`$ with $`e^{\mu\nu}=-\bar\varepsilon^{\mu\nu\rho\sigma\tau}e_{\rho\sigma\tau}/12`$. Thus $`\nabla_\mu p^\mu=0`$ identically. If a current term has variation $`\delta S=\int\bar e\,J_\mu\delta p^\mu`$, then

```math
\delta S=-\int\bar e\,(\nabla_\nu J_\mu)\delta e^{\mu\nu}+\int\partial_\nu(\bar e\,J_\mu\delta e^{\mu\nu})=\int\bar e\,\nabla_{[\mu}J_{\nu]}\delta e^{\mu\nu}+\hbox{boundary}.
\tag{7.6}
```

An unconstrained equation $`J_\mu=0`$ would be stronger than the potential equation and is not justifyd. The $`H_3=d b+g e_3/2`$ dependence supplies additional terms when this formula is applied to the complete block; (7.6) alone is not that equation.

The remaining original-field equations are derived in §§7.4–7.5.

## 7.4 Complete bosonic form and connection equations

Vary the form block (6.30) without changing its independent fields. For $`A`$, $`\delta G_{\mu\nu}=2\nabla_{[\mu}\delta A_{\nu]}`$ gives $`-cG^{\mu\nu}\delta G_{\mu\nu}=-2c\nabla_\mu(G^{\mu\nu}\delta A_\nu)+2c j_G^\nu\delta A_\nu`$. The $`pA`$ term adds $`-4gc p^\nu\delta A_\nu`$. Varying $`v`$ and $`v'`$ is algebraic. Therefore

```math
\mathcal E_A^\mu=2c j_G^\mu-4gc p^\mu=0,\qquad \mathcal E_v^\mu=-\frac{2\sqrt2c}{x}p^\mu=0,\qquad \mathcal E_{v'}^{\mu ij}=4c v'^{\mu ij}=0.
\tag{7.7}
```

For the independent three-form use its invertible background dual $`e^{\mu\nu}`$, with $`\delta H^{\mu\nu}=g\delta e^{\mu\nu}/2`$ when $`b`$ is held fixed. The derivative of the $`p`$ terms is

```math
J_\mu=-\frac{4c}{x^2}p_\mu-\frac{2\sqrt2c}{x}v_\mu-4gc A_\mu,\qquad \delta\mathcal L_{p}=J_\mu\nabla_\nu\delta e^{\mu\nu}\doteq\nabla_{[\mu}J_{\nu]}\delta e^{\mu\nu}.
\tag{7.8}
```

The $`4cH^2`$ term adds $`4gcH_{\mu\nu}\delta e^{\mu\nu}`$. Hence the evaluated potential equation is

```math
\boxed{\mathcal E_{e_2\mu\nu}=c\left[4gH_{\mu\nu}-\frac{2}{x^2}F_{\mu\nu}(p)-\frac{\sqrt2}{x}F_{\mu\nu}(v)-2gG_{\mu\nu}\right]=0.}
\tag{7.9}
```

For $`b`$, $`\delta H^{\mu\nu}=-\bar\varepsilon^{\mu\nu\rho\sigma\tau}\nabla_\rho\delta b_{\sigma\tau}/4`$. Thus $`8cH_{\mu\nu}\delta H^{\mu\nu}=-2c\bar\varepsilon^{\mu\nu\rho\sigma\tau}H_{\mu\nu}\nabla_\rho\delta b_{\sigma\tau}\doteq2c\bar\varepsilon^{\mu\nu\rho\sigma\tau}\nabla_\rho H_{\mu\nu}\delta b_{\sigma\tau}`$ and

```math
\mathcal E_b^{\sigma\tau}=2c\bar\varepsilon^{\mu\nu\rho\sigma\tau}\nabla_\rho H_{\mu\nu}=0.
\tag{7.10}
```

Equations (7.4), (7.7), (7.9), (7.10) are the complete unprojected bosonic linearized equations. The fermionic equations are derived in §7.5. The $`A`$ and $`v`$ divergences vanish identically because $`\nabla\cdot j_G=\nabla\cdot p=0`$. The form gauge identity follows by inserting $`\delta b=-g\Lambda_2/2`$, $`\delta e_3=d\Lambda_2`$ in the displayed variations: the induced $`\delta H_3`$ is zero and $`\delta p`$ is zero by $`d^2\Lambda_2=0`$.

## 7.5 Original gravitino and spinor equations

For two odd Majorana fields the second varied slot must be transferred to the first using the source flip signs and one integration by parts per derivative. For example the diagonal Rarita–Schwinger term gives

```math
\delta(-c\bar\Psi_a\gamma^{abc}\nabla_b\Psi_c)=-c\delta\bar\Psi_a\gamma^{abc}\nabla_b\Psi_c-c\bar\Psi_a\gamma^{abc}\nabla_b\delta\Psi_c\doteq-2c\delta\bar\Psi_a\gamma^{abc}\nabla_b\Psi_c.
\tag{7.11}
```

Likewise $`\delta(2c\bar\zeta\not\nabla\zeta/x^2)\doteq4c\delta\bar\zeta\not\nabla\zeta/x^2`$. Put $`\theta=\gamma^a\Psi_a`$, $`\sigma=\nabla^a\Psi_a`$. The mixed derivative term, written as $`2\sqrt2ic\bar\Psi_a\gamma^{ab}J\nabla_b\zeta/x`$, contributes

```math
\delta\ell_{\rm mix,der}\doteq\frac{2\sqrt2ic}{x}\delta\bar\Psi_a\gamma^{ab}J\nabla_b\zeta-\frac{2\sqrt2ic}{x}\delta\bar\zeta J(\not\nabla\theta-\sigma),\qquad \gamma^{ab}\nabla_b\Psi_a=\sigma-\not\nabla\theta.
\tag{7.12}
```

The mixed mass varies as $`\delta(-4gc\bar\Psi_a\gamma^a\zeta)=-4gc\delta\bar\Psi_a\gamma^a\zeta+4gc\delta\bar\zeta\theta`$. This uses the contracted rank-one flip; it is not a complex conjugation of the Majorana bar. The diagonal $`J`$ masses each give their two-slot factor. Collecting the variations defines

```math
\begin{aligned}
\delta S_F^{(2)}&\doteq-\frac{2c}{2\kappa_5^2}\int\bar e\,[\delta\bar\Psi_a\mathcal F_\Psi^a+\delta\bar\zeta\mathcal F_\zeta],\\
\mathcal F_\Psi^a&=\gamma^{abc}\nabla_b\Psi_c-3im\gamma^{ab}J\Psi_b-\frac{i\sqrt2}{x}\gamma^{ab}J\nabla_b\zeta+2g\gamma^a\zeta,\\
\mathcal F_\zeta&=\frac{i\sqrt2}{x}J(\not\nabla\theta-\sigma)-2g\theta-\frac2{x^2}\not\nabla\zeta+\frac{7ig}{\sqrt2x}J\zeta.
\end{aligned}
\tag{7.13}
```

The unprojected equations are $`c\mathcal F_\Psi^a=c\mathcal F_\zeta=0`$. The displayed definition of $`\mathcal F`$ does not justify dropping $`c`$ at $`c=0`$. These equations, together with (7.4), (7.7), (7.9), (7.10), cover all original independent fields. Their traces, divergences and gauge identities are derived in Step 10, after the raw variation.
