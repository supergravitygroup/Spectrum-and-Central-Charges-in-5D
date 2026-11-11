<a id="step-11--constrained-kernels-and-eigenfields"></a>

# Constrained kernels and eigenfields

<!-- ASSERT_CONVENTION: natural_units=true, metric_signature=(-,+,+,+,+), curvature=GB04, action_lock=GB-FERMION-ACTION-0+2-v1, convention_lock=GB-FERMION-SPECTRUM-CONVENTIONS-v1, coupling_dimension=-2, fermion_bar=linear_Majorana -->

Generic reduction uses $`0<x<2`$; the endpoint $`x=2`$ is assessed directly in the raw quadratic action. Global boundary modes and renormalized boundary norms are outside this scope.

<a id="111-removing-the-scalarmetric-mixing"></a>

## Removing the scalar–metric mixing

For any scalar $`u`$, inserting $`h_{\mu\nu}=u\bar g_{\mu\nu}`$ into (6.14) gives

```math
r(u\bar g)=-4\Box u-20ku,\qquad \mathcal G^L_{\mu\nu}(u\bar g)=-\frac32P_{\mu\nu}u.
\tag{11.1}
```

Put $`h=H+\beta\ell\bar g`$. The metric action's cross term is $`-c\beta H^{\mu\nu}\mathcal G^L_{\mu\nu}(\ell\bar g)=3c\beta\ell r(H)/2`$, using (7.2). Adding the original mixing leaves $`(3c\beta/2+c/x)\ell r(H)`$. Thus $`\beta=-2/(3x)`$ produces the map (10.2).

After the algebraic solution (9.1), the three gradient coefficients and the two conformal potential corrections are

```math
\begin{aligned}
(\nabla\ell)^2:&\quad 3c\beta^2+\frac{4c\beta}{x}+\frac c{x^2}=\frac c{x^2}\left(\frac43-\frac83+1\right)=-\frac c{3x^2},\\
\ell^2:&\quad -15ck\beta^2-\frac{20ck\beta}{x}+4cg^2=\frac{20ck}{3x^2}+4cg^2=\frac23cg^2.
\end{aligned}
\tag{11.2}
```

For example $`\int\ell\Box\ell=-\int(\nabla\ell)^2+\int\nabla_\mu(\ell\nabla^\mu\ell)`$ supplies the sign of the conformal terms. The diagonalized subblock is

```math
\boxed{S^{(2)}_{H,\ell}=\frac1{2\kappa_5^2}\int\bar e\left[-\frac c2H^{\mu\nu}\mathcal G^L_{\mu\nu}(H)-\frac c{3x^2}(\nabla\ell)^2+\frac23cg^2\ell^2\right].}
\tag{11.3}
```

In particular the scalar has a negative Lorentzian gradient coefficient, as required for a positive local kinetic sign with signature $`-++++`$ and $`c>0`$.

<a id="112-roots-and-reconstruction"></a>

## Roots and reconstruction

The scalar equation is

```math
\frac{2c}{3x^2}(\Box+2g^2x^2)\ell=0,\qquad (\Box-m_0^2)\ell=0,\qquad m_0^2=-2g^2x^2=4k.
\tag{11.4}
```

The scalar eigenfield in original variables is $`(h_{\mu\nu},\ell,n)=(-2\bar g_{\mu\nu}\ell/(3x),\ell,-2gx\ell)`$, with $`H=0`$. It reconstructs every equation in the scalar–metric block:

```math
\mathcal G^L_{\mu\nu}(h)=\frac1xP_{\mu\nu}\ell,\quad r(h)=\frac{8}{3x}\Box\ell+\frac{40k}{3x}\ell,\quad \mathcal E_\ell=\frac{2c}{3x^2}(\Box-4k)\ell,\quad\mathcal E_n=0.
\tag{11.5}
```

The metric equation vanishes before imposing the scalar wave equation. The scalar reconstruction is not just a root of a determinant.

For the graviton eigenfield choose $`\ell=n=0`$, $`h=H`$. In its transverse-traceless representative the ordered derivatives in (6.14) give $`r_{\mu\nu}=5kH_{\mu\nu}-\Box H_{\mu\nu}/2`$, hence

```math
\mathcal G^L_{\mu\nu}(H)=-\frac12(\Box-2k)H_{\mu\nu},\qquad (\Box-2k)H_{\mu\nu}=0.
\tag{11.6}
```

This is the massless spin-two equation in the stated curvature convention; the $`2k`$ is a curvature shift, not a Fierz–Pauli mass. Both remaining scalar equations vanish because $`r(H)=0`$.

No inverse $`\Box`$ or common differential factor was divided out. Pure metric gauges are quotiented using Step 10. The form and fermion reconstructions follow below.

<a id="113-both-physical-form-eigenfields-and-their-reconstruction"></a>

## Both physical form eigenfields and their reconstruction

For $`c>0`$, take any pair of Maxwell solutions $`A,Q`$ with $`\nabla^\mu F_{\mu\nu}(A)=\nabla^\mu F_{\mu\nu}(Q)=0`$. Reconstruct the original fields by (10.5), with $`b`$ solving $`db=2*dQ`$. Existence follows locally from $`d*dQ=0`$. Then

```math
p=0,\quad j_G=0,\quad dH=d^2Q=0,\quad j_H=j_{dQ}=0,\quad 4gH-\frac{\sqrt2}{x}F(v)-2gG=4gH-2g(2H-G)-2gG=0.
\tag{11.7}
```

Thus every form equation (7.7), (7.9), (7.10), including the original three-form equation, is satisfied. The two independent eigenfields can be chosen as $`(A,Q)=(A,0)`$ with $`v=-\sqrt2gxA`$, and $`(A,Q)=(0,Q)`$ with $`v=2\sqrt2gxQ`$. There is no independent mode of $`v`$ left after its curl and gauge freedom are fixed.

In Lorenz gauge, both vectors obey

```math
\nabla^\mu F_{\mu\nu}(A)=(\Box-4k)A_\nu=0,\qquad \nabla^\mu F_{\mu\nu}(Q)=(\Box-4k)Q_\nu=0.
\tag{11.8}
```

The $`4k`$ is the Ricci curvature shift in Maxwell's operator. Both physical masses are zero. No heavy form root or extra higher-derivative vector pole remains on this branch. This result follows from the full bosonic block and its constraints; it supplies no fermionic pole.

<a id="114-fermionic-field-shift-with-every-coefficient"></a>

## Fermionic field shift with every coefficient

Write (6.31) with $`\delta\bar A B=-\bar A J B`$. For $`\Psi_a=\Upsilon_a+\beta\gamma_aJ\zeta`$, the bar in the contracted pairing shifts by $`\bar\Psi_a=\bar\Upsilon_a-\beta\bar\zeta\gamma_aJ`$. In particular $`\beta`$ is not complex conjugated. The Clifford reductions needed are $`\gamma^{abc}\gamma_c=3\gamma^{ab}`$, $`\gamma_a\gamma^{abc}\gamma_c=12\gamma^b`$, $`\gamma^{ab}\gamma_b=4\gamma^a`$, $`\gamma_a\gamma^{ab}\gamma_b=20`$. The contracted flip and one derivative transfer collect the two cross terms of each diagonal bilinear.

The derivative mixing and algebraic mixing coefficients become

```math
-6\beta+\frac{2\sqrt2i}{x}=0,\qquad -24im\beta-4g=0,\qquad \beta=\frac{i\sqrt2}{3x},\quad m=\frac{gx}{2\sqrt2}.
\tag{11.9}
```

The second equation is satisfied by the same shift; it is not an independent adjustment. The three spinor kinetic contributions, from the shifted Rarita–Schwinger term, the derivative mixing and the original spinor term, add as

```math
-12\beta^2+\frac{8\sqrt2i\beta}{x}+\frac2{x^2}=\frac1{x^2}\left(\frac83-\frac{16}3+2\right)=-\frac2{3x^2}.
\tag{11.10}
```

The corresponding $`\bar\zeta J\zeta`$ mass contributions are

```math
60im\beta^2+20g\beta-\frac{7ig}{\sqrt2x}=\frac{im}{3x^2}(-40+80-42)=-\frac{2im}{3x^2}.
\tag{11.11}
```

Thus the fully diagonal quadratic fermionic action is

```math
\boxed{\ell_F^{(2)}=-c\left[\bar\Upsilon_a(\gamma^{abc}\nabla_b\Upsilon_c-3im\gamma^{ab}J\Upsilon_b)+\frac2{3x^2}\bar\zeta(\not\nabla+imJ)\zeta\right].}
\tag{11.12}
```

This exact algebraic change uses no inverse wave operator and is valid for all finite $`x>0`$. At $`c=0`$ it still changes variables, but it does not produce a nonzero kinetic form.

<a id="115-signed-operators-and-reconstruction-in-every-raw-fermion-equation"></a>

## Signed operators and reconstruction in every raw fermion equation

In the local transverse gamma-traceless representative of Step 10, expand $`\gamma^{abc}=\gamma^a\gamma^b\gamma^c-\eta^{ab}\gamma^c+\eta^{ac}\gamma^b-\eta^{bc}\gamma^a`$. The first, second and fourth terms give derivatives of the gamma trace or divergence, leaving $`\not\nabla\Upsilon^a`$. Also $`\gamma^{ab}\Upsilon_b=-\Upsilon^a`$. Hence

```math
(\not\nabla+3imJ)\Upsilon_a=0,\qquad \gamma^a\Upsilon_a=\nabla^a\Upsilon_a=0,\qquad(\not\nabla+imJ)\zeta=0.
\tag{11.13}
```

On the complexified doublet define $`P_s=(1+s\,iJ)/2`$, $`s=\pm1`$. Since $`(iJ)^2=1`$, these obey $`P_s^2=P_s`$, $`P_+P_-=0`$, and $`iJP_s=sP_s`$. The signed first-order equations are

```math
(\not\nabla+\mu_{3/2,s})\Upsilon_{a,s}=0,\qquad (\not\nabla+\mu_{1/2,s})\zeta_s=0,\qquad \mu_{3/2,s}=3sm,\quad\mu_{1/2,s}=sm.
\tag{11.14}
```

They are kept signed; a squared equation would conflate the charge-related solution spaces. Symplectic Majorana reality relates the two $`s`$ descriptions, which are not two independent doublets. The AdS gravitino parameter $`3m`$ is a curvature mass of a gauge-invariant massless gravitino, as (10.6)–(10.9) establish.

For reconstruction set $`\Psi_a=\Upsilon_a+\beta\gamma_aJ\zeta`$. Directly in (7.13), the derivative and mass cross coefficients cancel by (11.9), and

```math
\mathcal F_\Psi^a=E_\Upsilon^a,\qquad \mathcal F_\zeta=\beta\gamma_aJ E_\Upsilon^a+\frac2{3x^2}(\not\nabla+imJ)\zeta.
\tag{11.15}
```

For the second equality insert (10.7). The coefficients are $`3\beta=i\sqrt2/x`$, $`12im\beta=-2g`$, $`4i\sqrt2\beta/x+2/(3x^2)=-2/x^2`$, and $`10g\beta+2im/(3x^2)=7ig/(\sqrt2x)`$, exactly the four entries in $`\mathcal F_\zeta`$.

A pure gravitino mode has $`\zeta=0`$, $`\Psi=\Upsilon`$. A pure physical spinor has $`\Upsilon=0`$, $`\Psi_a=\beta\gamma_aJ\zeta`$. Both solve both original equations. Setting the original $`\Psi`$ to zero for the second mode would miss its mixing. Bosonic equations are identically satisfied with bosonic fluctuations zero, and conversely, because the quadratic action has no mixed odd block.
