# Anomalies, a-maximization and c-extremization

This page follows the final supplied paper, Sections 3.6 and 4.4:
equations (3.65)–(3.67) and (4.14)–(4.16).
It uses the same action normalization as the
[central charges and massless vectors](central_charges_and_massless_vectors.md).
The [calculation and verification record](../../computations/central_charge_extremization/README.md)
are independent of the external manuscript at runtime.

## Five-dimensional source and anomaly normalization

In [the current action](../action.md), the G-2D terms
$`-2\sqrt2 E\cdot V-4gE\cdot C`$, with
$`E_a\supset\epsilon_{abcde}G^{bc}G^{de}/(8g)`$, give the first two
Chern–Simons terms below. G-W and G-LOG each supply
$`-\epsilon C\mathcal V\mathcal V/24`$; G-R2 supplies
$`-\epsilon C\boldsymbol{\mathcal G}\boldsymbol{\mathcal G}/8`$,
where $`\boldsymbol{\mathcal G}\simeq\sqrt2\mathcal V`$ in this CS sector.
G-W also supplies $`\epsilon CRR/16`$. Thus

```math
\begin{aligned}
e^{-1}\mathcal L_{\rm CS}
 &=-\frac12\epsilon CGG-\frac{\sqrt2}{4g}\epsilon VGG
   -\frac{\alpha+\beta+6\zeta}{24}\epsilon C\mathcal V\mathcal V
   +\frac\alpha{16}\epsilon CRR.
\end{aligned}
```

The other gauge-invariant epsilon terms do not enter this anomaly tensor.
Since $`\epsilon AFF=4A\wedge F\wedge F`$, symmetrization modulo total
derivatives gives, in the $`(C,V)`$ basis,

```math
\begin{aligned}
k_{CCC}&=-2,&k_{CCV}&=-\frac{\sqrt2}{3g},&
k_{CVV}&=-\frac{\alpha+\beta+6\zeta}{18},&k_{VVV}&=0.
\end{aligned}
```

Use the paper's charge-one R direction $`s=(\varepsilon,-2)`$ and its
inflow normalization $`\mathop{\mathrm{Tr}}\nolimits R^3=12\pi^2 k(s,s,s)/\kappa^2`$.
The mixed gravitational term gives

```math
\begin{aligned}
\mathop{\mathrm{Tr}}\nolimits R^3
 &=-\frac{8\pi^2\varepsilon}{\kappa^2}
 \left(3\varepsilon^2-\frac{3\sqrt2}{g}\varepsilon+
 \alpha+\beta+6\zeta\right),\\
\mathop{\mathrm{Tr}}\nolimits R&=-\frac{24\pi^2\alpha\varepsilon}{\kappa^2}.
\end{aligned}
```

The shared sign is fixed by the two-derivative $`a=c`$ normalization.
The trace convention is $`R^{ab}\wedge R_{ab}=-\mathop{\mathrm{tr}}\nolimits(R\wedge R)`$.

## Trial a and the flavor coefficient

With $`a(\varepsilon)=3(3\mathop{\mathrm{Tr}}\nolimits R^3-\mathop{\mathrm{Tr}}\nolimits R)/32`$,
$`\varepsilon=2\sqrt2y/(3g)`$ and $`\tau=(\beta+6\zeta)g^2`$,

```math
\begin{aligned}
\widehat a(y)&=\frac{2\sqrt2\pi^2}{g^3\kappa^2}
 \left(3y^2-2y^3-\frac34\tau y\right),\\
\widehat a'(1/L_0)&=-\frac{3\sqrt2\pi^2}{2g^3\kappa^2L_0^2}
 \left(\tau L_0^2-8L_0+8\right).
\end{aligned}
```

The check independently imports the existing current-action curvature
projection before imposing the vacuum equation and obtains the same
$`\widehat a`$. The extrema are precisely the vacuum roots. Their $`a,c`$
values agree with the current-action result, and the R direction obeys
$`C/V=-\sqrt2/(3gL_0)`$, so $`u=0`$.

For $`-(Z_u/4)(du)^2-(Z_v/4)(dv)^2`$, the backgrounds of the normalized
R and flavor currents are $`v=-2A_R,u=0`$ and $`u=A_F,v=0`$.
Using $`C_R=16c/3`$ gives

```math
\begin{aligned}
C_F&=\frac{16c}{3}\frac{Z_u}{4Z_v}
 =\frac{24\pi^2\ell}{\kappa^2}(2-L_0),\\
a''(\varepsilon_*)&=-\frac9{16}C_F,&
\widehat a''(1/L_0)&=-\frac{C_F}{2g^2}.
\end{aligned}
```

The initial ratio is taken on the regular chart; its simplified expression
retains the zeros explicitly. For g>0, the Einstein-connected root has
$`L_0<2`$ and is a maximum, the second root $`L_0'>2`$ is a minimum,
and at $`L_0=2`$ the extrema merge.

## The AdS3 family

For Gauss–Bonnet set $`(\alpha,\beta,\zeta)=(k/g^2,2k/g^2,0)`$.
Let $`f=(p,r)`$ and $`n=A_\Sigma f/(2\pi)`$. Reduction of the symmetric CS
tensor gives $`M_{IJ}=3k_{IJK}f^K`$, or

```math
M=\begin{pmatrix}
-6p-\sqrt2r/g&-\sqrt2p/g-kr/(2g^2)\\
-\sqrt2p/g-kr/(2g^2)&-kp/(2g^2)
\end{pmatrix}.
```

The trial central charge is
$`c_{\rm trial}(\varepsilon)=36\pi^2 k(n,s,s)/\kappa^2`$.
On the [regular BPS family](../../gauss_bonnet/product_backgrounds/supersymmetric_ads3_sigma2/action_inputs.md),
its stationary mixing for generic k is
$`\varepsilon_{2d}=\sqrt2P_2/(gP_3)=\ell_s`$.
For $`\chi=+1`$, $`\ell_s=\ell>0`$, and substitution gives exactly

```math
\begin{aligned}
c_L&=\frac{12\pi A_\Sigma}{\kappa^2}
 \frac{LX\ell}{2P_2P_4},&
c_R&=\frac{12\pi A_\Sigma}{\kappa^2}
 \frac{L(2-3k)P_2\ell}{P_4},\\
c_R-c_L&=\frac{12\pi A_\Sigma}{\kappa^2}\frac{k}{g^2}p.
\end{aligned}
```

The formulas use the existing P and X polynomials, not a fit at sample
points. Chirality reflection exchanges the two sides as in the paper.
At k=2/3 the trial is independent of mixing; evaluating it before division
still gives $`c_L`$, with $`c_R=0`$.

The same matrix M reproduces every entry of the previously reduced
[constant-level current matrix](../../computations/gb_ads3_sigma2/outputs/constant.json):
$`M_{\rm stored}=2T^TMT/(g^2\ell_s)`$, $`T=\mathop{\mathrm{diag}}\nolimits(1,g/\sqrt2)`$.
If $`q_R`$ is its extremized entry, restoring $`V=-2A_R`$ gives
$`k_R=8\pi A_\Sigma\ell q_R/\kappa^2`$ and $`c_L=3k_R`$.

## Universal twist

For genus $`\mathsf g>1`$, the universal-twist flux is
$`n=(\mathsf g-1)R_4`$, where $`R_4=(2\sqrt2/(3gL_0),-2)`$.
The flavor direction is $`F=(1,0)`$ and
$`k=4(L_0-1)/L_0^2`$ on the Gauss–Bonnet AdS5 vacuum.
Extremizing over the two-dimensional flavor mixing yields

```math
\begin{aligned}
\delta c&=-3(\mathsf g-1)
 \frac{(\mathop{\mathrm{Tr}}\nolimits R^2F)^2}{\mathop{\mathrm{Tr}}\nolimits RF^2}
 =\frac{8(\mathsf g-1)(c-a)^2}{3c},\\
c_L&=\frac{16}{3}(\mathsf g-1)(5a-3c)+\delta c,\\
c_R&=\frac{32}{3}(\mathsf g-1)a+\delta c.
\end{aligned}
```

These identities keep g and the coupling symbolic, with nonzero c for the
displayed division. On the Einstein-connected branch the constant and
linear terms of $`\delta c`$ vanish, giving the first-order agreement stated
in the paper. The computation does not extend the paper's twist analysis
to additional branches or boundary conditions.
