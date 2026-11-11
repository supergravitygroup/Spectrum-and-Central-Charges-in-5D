# Critical branches and supermultiplets

[Reading guide](../README.md). The equation labels and local symbols below follow the action conventions specified for this theory.

<a id="13-critical-branches-and-supermultiplet-structure"></a>

## Critical branches and supermultiplet structure

On the selected branch,

```math
L_0=\frac{2}{1+\sqrt{1-\alpha g^2/2}},\qquad
N_0=-\frac32gL_0^2,\qquad
\ell^{-2}=\frac12g^2L_0^2,
```

```math
\alpha g^2L_0^2=8(L_0-1),\qquad
0<L_0\le2,\qquad L_0\ne1,\qquad g\ne0.
```

Fermionic $`N_F`$ denotes the inverse algebraic residue, not a replacement for missing Hermitian conjugation. Representation assignments require boundary conditions preserving the stated falloffs.

The root function is determined by the couplings, not an additional free parameter:

```math
\Delta(\alpha,g)
=
\sqrt{\frac{2(4-L_0)}{L_0-1}}
=
2\sqrt{
\frac{1+2\sqrt{1-\alpha g^2/2}}
     {1-\sqrt{1-\alpha g^2/2}}
}.
```

For positive $`\alpha`$, $`\Delta\ge2`$.

## Critical conditions

The metric, vector, and fermion polynomials are

```math
\begin{aligned}
K_2(x)&=-\frac{\alpha}{12}x
 \left[x-\frac{6(4-3L_0)}{\alpha}\right],
&&x=\bar\Box-2k,\\
P_V(x)&=16(L_0-1)^2x^2
 +8g^2L_0^2(L_0-1)(L_0-4)x\\
&\quad+3g^4L_0^4(L_0-4)(3L_0-4),
&&x=\mathfrak M_1,\\
P_{3/2}(z)&=
\left(z+\frac32\right)
\left[4(L_0-1)(z^2-z)+3L_0-9\right],\\
P_{1/2}(z)&=
(2z+1)\left[4(L_0-1)(z^2+z)+3L_0-9\right]
\end{aligned}
```

where

```math
k=-\ell^{-2},\qquad
\mathfrak M_p=d\,\mathrm{div}+\mathrm{div}\,d,\qquad
z=t^{-1}\not{\bar\nabla},\qquad
t=igM,\qquad t^2=\ell^{-2}.
```

Their discriminants are

```math
\begin{aligned}
\mathop{\mathrm{disc}}\nolimits P_V
&=-512g^4L_0^4(L_0-4)(L_0-1)^3,\\
\mathop{\mathrm{disc}}\nolimits P_{3/2}
&=-1152(L_0-4)(L_0-1)(3L_0-4)^2,\\
\mathop{\mathrm{disc}}\nolimits P_{1/2}
&=-2048(L_0-4)^3(L_0-1)
\end{aligned}
```

The selected branch excludes $`L_0=4`$; $`L_0=1`$ corresponds to excluded $`\alpha=0`$.

The determinant of the scalar coefficient matrix in $`(r,l,n)`$ is

```math
\det\mathcal E_{\rm sc}(x)
=
-\frac{16(L_0-2)^2(L_0-1)}{3g^2L_0^6}
(x-4k)
\left[x-\frac{6(4-3L_0)}{\alpha}\right].
```

Thus $`L_0=2`$ changes the scalar-system rank, not merely a mass root. Determinant overall signs in differently ordered equation rows have no effect on these roots or ranks.

Combining root mergers and kinetic zeros gives

```math
\boxed{
\begin{array}{c|c|c}
L_0&\alpha g^2=8(L_0-1)/L_0^2&\text{Condition}\\ \hline
\frac43&\frac32&
\text{Double roots and Jordan chains}\\[2pt]
2&2&
\text{Additional linear gauge symmetries and rank change}
\end{array}}
```

## Generic physical content

The physical scalar combinations are

```math
\phi_0=\frac ng+\frac32L_0l,\qquad
\phi_M=\frac ng+2L_0l
```

with inverse

```math
l=\frac2{L_0}(\phi_M-\phi_0),\qquad
n=g(4\phi_0-3\phi_M)
```

The scalar contribution to the metric remains

```math
h_{\mu\nu}
=h^{TT}_{0\mu\nu}+h^{TT}_{M\mu\nu}
+\frac{\bar g_{\mu\nu}}{L_0^2}
 \left(\frac43\phi_0-\phi_M\right)
+2\bar\nabla_{(\mu}\xi_{\nu)}.
```

In the vector–form sector,

```math
\mathcal H^{abc}
=H_c^{abc}+\bar\varepsilon^{deabc}(da)_{de},
\qquad dH_c=0,\qquad
p=-\frac2g\mathfrak M_1a.
```

The potential $`a`$ represents the physical form sector and adds no fundamental field.

The two Maxwell combinations are

```math
\mathcal A_0=c_0+\frac{\sqrt2}{3gL_0}v_0,\qquad
\mathcal B_0=v_0
```

and the two massive-vector eigenvectors are

```math
\boxed{
\begin{pmatrix}c_\pm\\v_\pm\\a_\pm\end{pmatrix}
=
\begin{pmatrix}
\pm\Delta\\[2pt]
\dfrac{gL_0}{2\sqrt2}\Delta(\Delta\mp2)\\[2pt]
1
\end{pmatrix}a_\pm
}
```

The full reconstruction is

```math
\begin{aligned}
c&=c_0+c_++c_-,\\
v&=v_0+v_++v_-,\\
a&=\frac12c_0+\frac{v_0}{2\sqrt2gL_0}+a_++a_-
\end{aligned}
```

which preserves all form–vector mixing induced by $`g\ne0`$.

The fermionic reconstruction is

```math
\begin{aligned}
\zeta&=\frac tg(4\rho_++4\rho_--3\chi),\\
\Psi_a&=\Psi^{TT}_{0a}+\Psi^{TT}_{+a}+\Psi^{TT}_{-a}
+\gamma_a(\rho_++\rho_--\chi)
+\left(\bar\nabla_a+\frac t2\gamma_a\right)\epsilon .
\end{aligned}
```

The last term is local SUSY. The physical spinor $`\chi`$ differs from the Standard-Weyl composite $`\chi_1`$.

Use the bosonic wave equations

```math
\begin{aligned}
(\bar\Box-2k-m^2)h^{TT}&=0,\\
(\bar\Box-m^2)\phi&=0,\\
(\mathfrak M_1-m^2)A&=0,\qquad \mathrm{div}A=0,\\
(\mathfrak M_2-m_H^2)q&=0,\qquad
q=\mathrm{div}H_c,\qquad \mathrm{div}q=0
\end{aligned}
```

and fermionic equations

```math
(\not{\bar\nabla}-rt)F=0
```

so that

```math
\begin{aligned}
(\bar\Box-6k-r^2\ell^{-2})\Psi^{TT}&=0,\\
(\bar\Box-5k-r^2\ell^{-2})\chi_{\rm phys}&=0.
\end{aligned}
```

On the $`\sigma=\pm1`$ eigenspaces of $`t`$, the signed mass is $`m_D=\sigma r/\ell`$. These eigenspaces do not count as two new independent species.

The generic bosonic spectrum for $`L_0\ne4/3,2`$ is listed below.

| Physical field | $`(j_L,j_R)_{R}`$ | $`m^2`$ | $`E`$, $`\alpha>0`$ | Kinetic coefficient $`Z`$ | D.o.f. |
|---|---|---:|---:|---:|---:|
| $`h_0^{TT}`$ | $`(1,1)_0`$ | $`0`$ | $`4`$ | $`(4-3L_0)/2`$ | 5 |
| $`\mathcal B_0`$ | $`(\frac12,\frac12)_0`$ | $`0`$ | $`3`$ | $`2(4-3L_0)/(3g^2L_0^2)`$ | 3 |
| $`\phi_0`$ | $`(0,0)_0`$ | $`-2g^2L_0^2`$ | $`2`$ | $`8(2-L_0)/(3L_0^4)`$ | 1 |
| $`\mathcal A_0`$ | $`(\frac12,\frac12)_0`$ | $`0`$ | $`3`$ | $`6(2-L_0)`$ | 3 |
| $`h_M^{TT}`$ | $`(1,1)_0`$ | $`6(4-3L_0)/\alpha`$ | $`2+\Delta/2`$ | $`-(4-3L_0)/2`$ | 9 |
| $`\phi_M`$ | $`(0,0)_0`$ | $`6(4-3L_0)/\alpha`$ | $`2+\Delta/2`$ | $`-2(2-L_0)/L_0^4`$ | 1 |
| $`a_+`$ | $`(\frac12,\frac12)_0`$ | $`2(4-L_0)/\alpha+g^2L_0^2\Delta/2`$ | $`3+\Delta/2`$ | $`-\frac{4(4-L_0)}3(\Delta-2)(\Delta+4)`$ | 4 |
| $`a_-`$ | $`(\frac12,\frac12)_0`$ | $`2(4-L_0)/\alpha-g^2L_0^2\Delta/2`$ | $`1+\Delta/2`$ | $`-\frac{4(4-L_0)}3(\Delta+2)(\Delta-4)`$ | 4 |
| $`w^{ij}`$ | $`(\frac12,\frac12)_{+2}\oplus(\frac12,\frac12)_{-2}`$ | $`6(2-L_0)/\alpha`$ | $`2+\Delta/2`$ | $`-2\alpha/3`$ | 8 |
| $`q=\mathrm{div}H_c`$ | $`(1,0)_0\oplus(0,1)_0`$ | $`2(4-L_0)/\alpha`$ | $`2+\Delta/2`$ | $`-\alpha^2/[3(4-L_0)]`$ | 6 |

The coefficient $`Z`$ multiplies the standard second-order kinetic term in the displayed normalization. In $`p_\pm`$ normalization,

```math
p_\pm=-\frac{2m_\pm^2}{g}a_\pm,\qquad
Z_{p_\pm}=\frac{g^2}{4m_\pm^4}Z_{a_\pm}.
```

This conversion is not used where $`m_-^2=0`$.

For fermionic representations abbreviate

```math
\begin{aligned}
\mathcal R_{3/2}^{+}
&=(1,\tfrac12)_{+1}\oplus(\tfrac12,1)_{-1},\\
\mathcal R_{3/2}^{-}
&=(1,\tfrac12)_{-1}\oplus(\tfrac12,1)_{+1},\\
\mathcal R_{1/2}^{+}
&=(\tfrac12,0)_{+1}\oplus(0,\tfrac12)_{-1},\\
\mathcal R_{1/2}^{-}
&=(\tfrac12,0)_{-1}\oplus(0,\tfrac12)_{+1}
\end{aligned}
```

The $`R`$-charge convention gives $`Q_L`$ charge $`+1`$.

| Physical fermion | Representation | $`r`$, $`m_D=\sigma r/\ell`$ | $`E`$, $`\alpha>0`$ | Inverse algebraic residue $`N_F`$ | D.o.f. |
|---|---|---:|---:|---:|---:|
| $`\Psi_0^{TT}`$ | $`\mathcal R_{3/2}^{+}`$ | $`-3/2`$ | $`7/2`$ | $`-2(4-3L_0)`$ | 8 |
| $`\chi`$ | $`\mathcal R_{1/2}^{+}`$ | $`-1/2`$ | $`5/2`$ | $`6(2-L_0)`$ | 4 |
| $`\Psi_-^{TT}`$ | $`\mathcal R_{3/2}^{+}`$ | $`(1-\Delta)/2`$ | $`3/2+\Delta/2`$ | $`\frac{2(L_0-1)}3\Delta(\Delta-4)`$ | 12 |
| $`\rho_+`$ | $`\mathcal R_{1/2}^{-}`$ | $`(-1+\Delta)/2`$ | $`3/2+\Delta/2`$ | $`-\frac{8(L_0-1)}3\Delta(\Delta+2)`$ | 4 |
| $`\Psi_+^{TT}`$ | $`\mathcal R_{3/2}^{-}`$ | $`(1+\Delta)/2`$ | $`5/2+\Delta/2`$ | $`\frac{2(L_0-1)}3\Delta(\Delta+4)`$ | 12 |
| $`\rho_-`$ | $`\mathcal R_{1/2}^{+}`$ | $`(-1-\Delta)/2`$ | $`5/2+\Delta/2`$ | $`-\frac{8(L_0-1)}3\Delta(\Delta-2)`$ | 4 |

The tables give totals

```math
\boxed{n_B=44,\qquad n_F=44.}
```

## Local SUSY matching

The background conditions are

```math
\left(\bar\nabla_a+\frac t2\gamma_a\right)\epsilon=0,\qquad
\frac{N_0}{2}+\frac{3gL_0^2}{4}=0
```

and integrability follows from

```math
\left[
\bar\nabla_a+\frac t2\gamma_a,\,
\bar\nabla_b+\frac t2\gamma_b
\right]\epsilon
=\frac12(k+t^2)\gamma_{ab}\epsilon=0
```

Eight real Killing supersymmetries remain, with AdS superalgebra $`\mathfrak{su}(2,2|1)`$.

To distinguish the multiplets of the two equal-mass Maxwell fields, substitute the source expressions

```math
T^{(1)}_{ab}=\frac18\bigl((dc)_{ab}-2(da)_{ab}\bigr),\qquad
\eta=\left(-\gamma\!\cdot T+\frac14\gamma\!\cdot G\right)\epsilon
-\frac g2M\epsilon
```

into the linear-multiplet variation. In the pure Maxwell sector,

```math
\begin{aligned}
\delta\zeta
&=M\gamma\!\cdot\left(-4T+\frac34G\right)\epsilon\\
&=M\gamma\!\cdot\left(\frac14dc+da\right)\epsilon\\
&=\frac34M\gamma\!\cdot
d\left(c_0+\frac{\sqrt2}{3gL_0}v_0\right)\epsilon\\
&=\frac34M\gamma\!\cdot d\mathcal A_0\,\epsilon .
\end{aligned}
```

Thus $`\mathcal A_0`$ partners $`\chi`$, while $`\mathcal B_0`$ is absent from this variation.

The scalar transformations are

```math
\begin{aligned}
\delta l&=-2L_0\bar\epsilon(\rho_++\rho_-)
+\frac32L_0\bar\epsilon\chi,\\
\delta n&=3gL_0^2\bar\epsilon(\rho_++\rho_-)
-3gL_0^2\bar\epsilon\chi
\end{aligned}
```

and hence

```math
\boxed{
\delta\phi_0=-\frac34L_0^2\bar\epsilon\chi,\qquad
\delta\phi_M=-L_0^2\bar\epsilon(\rho_++\rho_-).
}
```

For TT gravitini use $`\Phi_a=-i\not{\bar\nabla}\Psi_a^{TT}/3`$ and $`\chi_1=0`$:

```math
\delta c_a=-\frac i2\bar\epsilon\Psi_a^{TT},\qquad
\delta v_a=\frac{igL_0}{4\sqrt2}(3-2r)
 \bar\epsilon\Psi_a^{TT}.
```

Therefore

```math
\frac{\delta v}{\delta c}
=\frac{gL_0}{2\sqrt2}(2r-3).
```

At the three gravitino roots,

```math
\begin{array}{c|c}
r&\delta v/\delta c\\ \hline
-\frac32&-3gL_0/\sqrt2\\
\frac{1+\Delta}{2}&gL_0(\Delta-2)/(2\sqrt2)\\
\frac{1-\Delta}{2}&-gL_0(\Delta+2)/(2\sqrt2)
\end{array}
```

The first row verifies $`\delta\mathcal A_0=0`$; the other rows reproduce the massive vector eigenvectors.

The generic matching is

```math
\boxed{
\begin{aligned}
\mathcal G&=\{\mathcal B_0,\Psi_0^{TT},h_0^{TT}\},
&&8_B+8_F,\\
\mathcal V&=\{\phi_0,\chi,\mathcal A_0\},
&&4_B+4_F,\\
\mathcal L_2&=
\{a_\pm,h_M^{TT},\phi_M,w,q,
  \Psi_\pm^{TT},\rho_\pm\},
&&32_B+32_F
\end{aligned}}
```

as displayed.

The long multiplet has lowest weight

```math
(E_*;\,j_L,j_R;\,R)
=
\left(1+\frac{\Delta}{2};\,\frac12,\frac12;\,0\right).
```

The exterior powers of the four raising supercharges are

```math
\wedge^2\!\left[(\tfrac12,0)_{+1}\oplus(0,\tfrac12)_{-1}\right]
=(0,0)_{+2}\oplus(\tfrac12,\tfrac12)_0\oplus(0,0)_{-2}
```

Their tensor product with the primary vector representation gives the following levels.

| Supercharge level | Energy | Fields | $`B/F`$ count |
|---|---:|---|---:|
| 0 | $`E_*`$ | $`a_-`$ | $`4_B`$ |
| 1 | $`E_*+\frac12`$ | $`\Psi_-^{TT},\rho_+`$ | $`16_F`$ |
| 2 | $`E_*+1`$ | $`h_M^{TT},\phi_M,q,w`$ | $`24_B`$ |
| 3 | $`E_*+\frac32`$ | $`\Psi_+^{TT},\rho_-`$ | $`16_F`$ |
| 4 | $`E_*+2`$ | $`a_+`$ | $`4_B`$ |

For example, the mass–energy checks are

```math
\begin{aligned}
m_-^2\ell^2&=(E_*-1)(E_*-3)=\frac{\Delta^2}{4}-\Delta,\\
m_M^2\ell^2&=(E_*+1)(E_*-3)=\frac{\Delta^2}{4}-4,\\
m_w^2\ell^2&=E_*(E_*-2)=\frac{\Delta^2}{4}-1,\\
m_H^2\ell^2&=(E_*-1)^2=\frac{\Delta^2}{4},\\
m_+^2\ell^2&=(E_*+1)(E_*-1)=\frac{\Delta^2}{4}+\Delta
\end{aligned}
```

These identities verify the bosonic levels and, together with the displayed field variations, support the local long-graviton assignment. The standard representation table is given in [Ceresole et al., Table 2](https://arxiv.org/html/hep-th/9905226v3); it is a comparison, not a substitute for these checks.

## Critical merger: non-diagonalizable extension

At $`\alpha g^2=3/2`$, $`L_0=4/3`$, $`\Delta=4`$,

the operators become

```math
K_2=-\frac{\alpha}{12}\mathfrak T_2^2,\qquad
\mathfrak T_2=\bar\Box-2k,
```

```math
K_{3/2}
=\frac{\alpha}{3}
\left(\not{\bar\nabla}+\frac32t\right)^2
\left(\not{\bar\nabla}-\frac52t\right)
```

The vector roots are

```math
m_-^2=0,\qquad m_+^2=\frac8{\ell^2}.
```

The double-root solution spaces are larger than their first-order kernels:

```math
\begin{aligned}
\mathfrak T_2h_0&=0,&
\mathfrak T_2h_1&=h_0,\\
Q\Psi_0&=0,&
Q\Psi_1&=\Psi_0,\qquad
Q=\not{\bar\nabla}+\frac32t.
\end{aligned}
```

The vector–form chain is

```math
\begin{pmatrix}c\\v\\a\end{pmatrix}_{J}
=
\begin{pmatrix}-4\\8\sqrt2g\\1\end{pmatrix}W_1
+
\begin{pmatrix}0\\0\\-\frac{27}{32g^2}\end{pmatrix}W_0,
\qquad
\mathfrak M_1W_1=W_0,\quad
\mathfrak M_1W_0=0
```

as displayed.

This is checked with the undifferentiated form equation. For the pencil $`K_V(x)`$ define

```math
P(x)=\mathop{\mathrm{diag}}\nolimits(x,x,1)K_V(x)
```

The two constant columns $`n_0,n_1`$ then satisfy

```math
P(0)n_0=0,\qquad P'(0)n_0+P(0)n_1=0.
```

Thus no spurious Maxwell solution is introduced by replacing the physical system with $`xK_V=0`$.

The critical field content is listed below.

| Sector | Wave equation / mass | Local d.o.f. |
|---|---|---:|
| Metric Jordan sector | $`\mathfrak T_2^2h^{TT}=0`$ | 14 |
| Vector–form Jordan sector | $`\mathfrak M_1^2W_1=0`$, with the coupled chain above | 7 |
| $`\mathcal A_0`$ | $`m^2=0`$ | 3 |
| $`\phi_0,\phi_M`$ | $`m^2\ell^2=-4,0`$ | $`1+1`$ |
| $`a_+`$ | $`m^2\ell^2=8`$ | 4 |
| $`w`$ | $`m^2\ell^2=3`$ | 8 |
| $`q`$ | $`m^2\ell^2=4`$ | 6 |
| Gravitino Jordan sector | $`Q^2\Psi^{TT}=0`$ | 20 |
| $`\Psi_+^{TT}`$ | $`r=5/2`$ | 12 |
| $`\chi,\rho_+,\rho_-`$ | $`r=-1/2,3/2,-5/2`$ | $`4+4+4`$ |

```math
\boxed{n_B=44,\qquad n_F=44.}
```

A Jordan pair has norm matrix

```math
G_J=
\begin{pmatrix}0&b\\b&c\end{pmatrix},
\qquad
\det G_J=-b^2
```

In the chosen chain normalizations,

```math
b_h=-\frac{\alpha}{12},\qquad
b_V=-\frac{24}{g^2},\qquad
b_\Psi=-\frac{4\alpha t}{3}.
```

The last coefficient is a formal fermionic bilinear. Nonzero bosonic $`b_h,b_V`$ show that ordinary zero-self-norm states are not in the radical of the pairing.

The remaining coefficients are

```math
\begin{gathered}
Z_{\mathcal A_0}=4,\quad
Z_{\phi_0}=\frac9{16},\quad
Z_{\phi_M}=-\frac{27}{64},\quad
Z_{a_+}=-\frac{512}{9},\\
Z_w=-\frac1{g^2},\qquad
Z_q=-\frac9{32g^4},\\
N_\chi=4,\qquad
N_{\Psi_+}=\frac{64}{9},\qquad
N_{\rho_+}=-\frac{64}{3},\qquad
N_{\rho_-}=-\frac{64}{9}.
\end{gathered}
```

At $`E_*=3`$ the long multiplet reaches a shortening threshold. At character level,

```math
\mathop{\mathrm{gr}}\nolimits\mathcal L_2(3)
=
\mathcal G\oplus\mathcal S\oplus\overline{\mathcal S},
```

```math
\mathcal S:
\left(\frac72;\,0,\frac12;\,+1\right),
\qquad
\overline{\mathcal S}:
\left(\frac72;\,\frac12,0;\,-1\right)
```

Each semishort gravitino multiplet carries $`12_B+12_F`$. This agrees with the $`A_1\bar A_1+A_2\bar L+L\bar A_2`$ recombination pattern in [Córdova–Dumitrescu–Intriligator, Eq. (2.30)](https://arxiv.org/pdf/1612.00809v1), with charge labels converted to the present $`Q_L=+1`$ convention.

The required longitudinal composition factors remain:

```math
\begin{aligned}
9&=5+4,
& D(4;1,1)&\ \leadsto\
D_{\rm massless}(4;1,1)+D(5;\tfrac12,\tfrac12),\\
4&=3+1,
& D(3;\tfrac12,\tfrac12)&\ \leadsto\
D_{\rm Maxwell}(3;\tfrac12,\tfrac12)+D(4;0,0),\\
12&=8+4,
& D(\tfrac72;\mathcal R_{3/2}^{+})&\ \leadsto\
D_{\rm massless}(\tfrac72;\mathcal R_{3/2}^{+})
+D(\tfrac92;\mathcal R_{1/2}^{+}).
\end{aligned}
```

These last terms are components of the critical solution space, not new fundamental fields.

The associated graded content is

```math
\mathcal V\oplus2\mathcal G
\oplus\mathcal S\oplus\overline{\mathcal S}
```

but the actual operator is not a diagonal sum of two independent graviton multiplets: the Jordan links remain. Removing logarithmic partners would reduce the $`44+44`$ solution space.

## Endpoint with rank change

At $`\alpha g^2=2`$, $`L_0=2`$, $`\Delta=2`$,

completion of the scalar square gives

```math
\begin{aligned}
\mathcal L_{\rm sc}^{(2)}
&=\frac{n+gl}{3g}\,r-\frac43(n+gl)^2\\
&=-\frac43\left(n+gl-\frac r{8g}\right)^2
+\frac{r^2}{48g^2}
\end{aligned}
```

The scalar Euler matrix has rank one:

```math
\mathcal E_L=g\mathcal E_N,\qquad
\mathcal E_{\rm trace}
=\frac{\bar\Box-10g^2}{2g}\mathcal E_N,
\qquad
n+gl=\frac r{8g}.
```

Its extra linear transformations are

```math
\delta l=\sigma,\qquad \delta n=-g\sigma
```

and

```math
\delta h_{\mu\nu}=2\omega\bar g_{\mu\nu},\qquad
\delta n=-\frac1g(\bar\Box+5k)\omega
```

consistent because

```math
\delta r=-8(\bar\Box+5k)\omega.
```

Neither of the two generic physical scalars remains.

The vector–form sector has extra direction

```math
\delta c=2\xi,\qquad
\delta\mathcal H^{abc}=\bar\varepsilon^{deabc}(d\xi)_{de}
```

with invariant combinations

```math
\mathcal H'=\mathcal H-\frac12\varepsilon\,dc,\qquad
a'=a-\frac12c,\qquad
p'=p-\frac1g j
```

as displayed.

The generic $`a_+`$ eigenvector becomes

```math
(c_+,v_+,a_+)=(2,0,1)a_+
```

which is entirely gauge. The apparent $`m_+^2=6g^2`$ root leaves the physical spectrum.

The surviving vector combinations are

```math
v=v_0+\frac1{\sqrt2}p',\qquad
a'=\frac{v_0}{4\sqrt2g}+\frac{p'}{4g}
```

The reduced determinant is

```math
\det K_{\rm red}(x)=\frac{x+2g^2}{9g^4}
```

and therefore

```math
\mathfrak M_1v_0=0,\qquad
(\mathfrak M_1+2g^2)p'=0
```

the surviving roots are those shown.

The additional fermionic transformation is

```math
\delta\Psi_a=\gamma_a\theta,\qquad
\delta\zeta=-\frac1g
\left(\not{\bar\nabla}-\frac52t\right)\theta
```

In $`\Psi_a=\Psi_a^{TT}+\gamma_a u+\text{Q-gauge}`$, the combination

```math
\eta_{\rm phys}
=\zeta+\frac1g\left(\not{\bar\nabla}-\frac52t\right)u
```

is invariant.

For the spin-half Hessian define

```math
P(z)=4(L_0-1)(z^2+z)+3L_0-9,\qquad
A(z)=8(L_0-1)z^2+7L_0-16
```

Its rank-controlling combination is

```math
(2z+3)A(z)-2(2z+1)P(z)
=-3(L_0-2)(2z-5)
```

At $`L_0=2`$ the matrix becomes

```math
-\frac{2t}{3}(2z-1)
\begin{pmatrix}2z+1\\-(2z+3)\end{pmatrix}
\begin{pmatrix}2z+1&-(2z+3)\end{pmatrix}
```

and has rank one. The remaining equation and inverse residue are

```math
\boxed{
\left(\not{\bar\nabla}-\frac12t\right)\eta_{\rm phys}=0,
\qquad N_{\eta_{\rm phys}}=\frac83
}
```

as displayed.

Here $`\ell^{-2}=2g^2`$. The complete physical endpoint table is below.

| Field | AdS weight and representation | Mass / signed root | $`Z`$ or $`N_F`$ | D.o.f. |
|---|---|---:|---:|---:|
| $`h_0^{TT}`$ | $`E=4,\ (1,1)_0`$ | $`m^2=0`$ | $`Z=-1`$ | 5 |
| $`v_0`$ | $`E=3,\ (\frac12,\frac12)_0`$ | $`m^2=0`$ | $`Z=-1/(3g^2)`$ | 3 |
| $`\Psi_0^{TT}`$ | $`E=7/2,\ \mathcal R_{3/2}^{+}`$ | $`r=-3/2`$ | $`N_F=4`$ | 8 |
| $`p'`$ | $`E=2,\ (\frac12,\frac12)_0`$ | $`m^2=-2g^2`$ | $`Z=1/(3g^2)`$ | 4 |
| $`h_{\rm PM}^{TT}`$ | $`E=3,\ (1,1)_0`$ | $`m^2=-6g^2=3k`$ | $`Z=1`$ | 8 |
| $`w`$ | $`E=3,\ (\frac12,\frac12)_{\pm2}`$ | $`m^2=0`$ | $`Z=-4/(3g^2)`$ | 6 |
| $`q=\mathrm{div}H'_c`$ | $`E=3,\ (1,0)_0\oplus(0,1)_0`$ | $`m^2=2g^2`$ | $`Z=-2/(3g^4)`$ | 6 |
| $`\Psi_-^{TT}`$ | $`E=5/2,\ \mathcal R_{3/2}^{+}`$ | $`r=-1/2`$ | $`N_F=-8/3`$ | 12 |
| $`\eta_{\rm phys}`$ | $`E=5/2,\ \mathcal R_{1/2}^{-}`$ | $`r=1/2`$ | $`N_F=8/3`$ | 4 |
| $`\Psi_+^{TT}`$ | $`E=7/2,\ \mathcal R_{3/2}^{-}`$ | $`r=3/2`$ | $`N_F=8`$ | 8 |

The partially massless spin-two field is quotiented by

```math
\delta h_{\mu\nu}^{\rm PM}
=(\bar\nabla_\mu\bar\nabla_\nu+k\bar g_{\mu\nu})\sigma
```

and has eight polarizations. Both $`w`$ vectors become Maxwell fields, and $`\Psi_+`$ becomes a second massless Rarita–Schwinger sector.

The multiplet content is

```math
\boxed{
\mathcal G_{8+8}\oplus\mathcal P_{24+24},
\qquad n_B=n_F=32
}
```

The nonunitary partially massless multiplet $`\mathcal P`$ has levels

```math
\begin{array}{c|c|c}
E&\text{Fields}&\text{D.o.f.}\\ \hline
2&p'&4_B\\
5/2&\Psi_-^{TT},\eta_{\rm phys}&16_F\\
3&h_{\rm PM}^{TT},w,q&20_B\\
7/2&\Psi_+^{TT}&8_F
\end{array}
```

as listed.

These extra gauge symmetries were verified for the quadratic action. They do not establish new nonlinear symmetries or additional preserved supercharges in the interacting theory.

## Norms and validity domains

For negative AdS masses, the highest-spin kinetic coefficient is insufficient. Longitudinal signs depend on

```math
Z_{\rm Proca,long}\propto Z\,m^2,\qquad
Z_{\rm FP,vector}\propto Z\,m^2,
```

```math
Z_{\rm FP,scalar}\propto
\frac{2Z}{3}m^2(m^2-3k)
```

Using these factors gives the domain table below.

| Region | Representation status | Bosonic norm signature |
|---|---|---:|
| $`0<\alpha g^2<3/2`$ | $`E_*>3`$; long multiplet has unitary weights but ghost kinetic sign | $`12_+,32_-`$ |
| $`\alpha g^2=3/2`$ | Jordan extensions, not a diagonal sum of short multiplets | In the full Jordan space, $`12_+,32_-`$ |
| $`3/2<\alpha g^2<2`$ | $`2<E_*<3`$; nonunitary long multiplet | $`12_+,32_-`$ |
| $`\alpha g^2=2`$ | Partially massless quotient, $`32+32`$ | $`8_+,24_-`$ |

In particular,

```math
Z_q=-\frac{\alpha^2}{3(4-L_0)}<0
\qquad
(0<L_0\le2,\ \alpha\ne0)
```

so no ghost-free region remains when every physical bulk mode is retained.

At positive coupling the BF expressions are

```math
\begin{aligned}
m_{\phi_M}^2\ell^2+4&=\frac{\Delta^2}{4},\\
m_w^2\ell^2+1&=\frac{\Delta^2}{4},\\
m_H^2\ell^2&=\frac{\Delta^2}{4},\\
m_\pm^2\ell^2+1&=\frac{(\Delta\pm2)^2}{4}
\end{aligned}
```

and nonnegative. Nevertheless, for $`2<\Delta<4`$,

```math
m_M^2<0,\qquad m_-^2<0,\qquad
|m_{\Psi_-}|\ell<\frac32
```

violates unitary representation bounds.

At negative coupling,

```math
0<L_0<1,\qquad \Delta^2<0,\qquad
m_{\phi_M}^2\ell^2<-4.
```

The vector masses are also complex conjugates. The real local system still has $`44+44`$ modes, but they cannot be interpreted as real positive-energy global AdS multiplets. Both conjugate roots remain included.

Two apparent singularities are not physical critical branches:

```math
\begin{array}{c|c|c}
L_0&\alpha g^2&\text{Result}\\ \hline
2/5&-30&
4/L_0+\alpha g^2/3=0;\ \text{coupled-system rank is unchanged}\\
22/19&114/121&
\phi_M\text{ of }r\text{ component vanishes; the physical scalar remains}
\end{array}
```

The first forbids division by a single diagonal $`n`$ coefficient, and the second invalidates a curvature-based projector, without removing physical modes.

The selected fixed-source reflecting prescription alone still does not determine

whether the BF logarithmic coefficient of $`\phi_0`$ is source or response; whether the critical Jordan/log responses are admitted; or which source is fixed for endpoint BF vector $`p'`$.

The results specify the local operators, critical ranks, algebraic residues, and superalgebra weights. The fermionic residues have their algebraic meaning; absolute Hermitian norms and a common global multiplet interpretation depend on the Hermitian pairing and a supersymmetric boundary domain.

<a id="14-supermultiplet-summary"></a>

## Supermultiplet summary

The selected AdS$`_5`$ background preserves $`SU(2,2|1)`$, with

```math
L_0=\frac{2}{1+\sqrt{1-\alpha g^2/2}},\qquad
E_* =1+\sqrt{\frac{4-L_0}{2(L_0-1)}}.
```

For $`0<\alpha g^2<2`$ and $`\alpha g^2\ne3/2`$:

| Supermultiplet | Field content in ascending energy order | AdS energies | Physical d.o.f. |
|---|---|---|---:|
| Massless graviton multiplet $`\mathcal G`$ | $`\mathcal B_0\ \to\ \Psi_0^{TT}\ \to\ h_0^{TT}`$ | $`3,\frac72,4`$ | $`8_B+8_F`$ |
| Short vector multiplet $`\mathcal V`$ | $`\phi_0\ \to\ \chi\ \to\ \mathcal A_0`$ | $`2,\frac52,3`$ | $`4_B+4_F`$ |
| Long spin-two multiplet $`\mathcal L_2`$ | $`a_-\ \to\ (\Psi_-^{TT},\rho_+)\ \to\ (h_M^{TT},\phi_M,w,q)\ \to\ (\Psi_+^{TT},\rho_-)\ \to\ a_+`$ | $`E_*,E_*+\frac12,E_*+1,E_*+\frac32,E_*+2`$ | $`32_B+32_F`$ |
| **Total** | $`\mathcal G\oplus\mathcal V\oplus\mathcal L_2`$ | | **$`44_B+44_F`$** |

The short-multiplet combinations are

```math
\mathcal A_0=c_0+\frac{\sqrt2}{3gL_0}v_0,\qquad
\mathcal B_0=v_0,\qquad
\phi_0=\frac ng+\frac32L_0l
```

and the long-multiplet scalar/form combinations are

```math
\phi_M=\frac ng+2L_0l,\qquad q=\mathrm{div}H_c
```

The field $`w`$ contains two vectors with $`R`$ charges $`\pm2`$.

At the critical points the table changes as follows.

| Parameter | Supermultiplet structure | Physical d.o.f. |
|---|---|---:|
| $`\alpha g^2=\frac32`$, $`L_0=\frac43`$ | $`\mathcal V`$ remains. The graviton and long spin-two sectors are linked by Jordan chains. The associated graded content is $`\mathcal V\oplus2\mathcal G\oplus\mathcal S\oplus\overline{\mathcal S}`$; each semishort gravitino multiplet $`\mathcal S`$, $`12_B+12_F`$ has the displayed count. **This is not a diagonal direct sum of the actual operator.** | **$`44_B+44_F`$** |
| $`\alpha g^2=2`$, $`L_0=2`$ | $`\mathcal G\oplus\mathcal P`$. The partially massless multiplet $`\mathcal P`$: $`p'\to(\Psi_-^{TT},\eta_{\rm phys})\to(h_{\rm PM}^{TT},w,q)\to\Psi_+^{TT}`$. Energies: $`2,\frac52,3,\frac72`$. | $`(8+24)_B+(8+24)_F=\mathbf{32_B+32_F}`$ |

```math
\alpha<0:\qquad E_*\notin\mathbb R.
```

For negative coupling the local count remains $`44_B+44_F`$, but complex roots do not form real positive-energy global AdS multiplets.

These tables summarize local spectrum matching. Global multiplet closure remains conditional because the BF/log source prescription and complete boundary symplectic data have not been fixed.

<a id="symbolic-consolidation-checks"></a>

## Symbolic consolidation checks

The following algebraic checks concern the displayed expressions and coefficient tables. Their scope is distinct from a full comparison of the fermionic source action and Hessian.

Write $`L=L_0`$ in this section. The branch equation is

```math
\alpha g^2L^2-8L+8=0
\quad\Longrightarrow\quad
\alpha=\frac{8(L-1)}{g^2L^2},
\qquad L\ne0,1,\quad g\ne0.
```

This substitution is a solution relation, not a normalization of a free parameter. It gives

```math
\begin{aligned}
B_0&=L-\frac{\alpha g^2L^2}{2}=4-3L,\\
Z&=\frac1L-\frac{\alpha g^2}{4}=\frac{2-L}{L^2},\\
\mu&=\frac{6(4-3L)}\alpha
 =\frac{3g^2L^2(4-3L)}{4(L-1)},\qquad
k=-\frac{g^2L^2}{2}.
\end{aligned}
```

For the scalar matrix in the operator-decomposition chapter, with row order $`(E_{\mathrm{tr}},E_l,E_n)`$, direct determinant expansion and factorization yield

```math
\begin{aligned}
\det K_S(x)
&=\frac{4(L-2)^2}{3L^6g^2}
 (2L^2g^2+x)
 (9L^3g^2-12L^2g^2+4Lx-4x)\\
&=\frac{16(L-2)^2(L-1)}{3L^6g^2}
 (x-4k)(x-\mu).
\end{aligned}
```

The scalar substitution is checked without dividing by $`F=4/L+\alpha g^2/3`$:

```math
\begin{gathered}
l=\frac2L(\phi_M-\phi_0),\qquad
n=g(4\phi_0-3\phi_M),\qquad
r=g^2\left(24\phi_0-\frac{19L-22}{L-1}\phi_M\right),\\
X_0=(x-4k)\phi_0,\qquad X_M=(x-\mu)\phi_M,\\
K_S(x)\begin{pmatrix}r\\l\\n\end{pmatrix}
=\begin{pmatrix}
(L-2)(-8X_0+6X_M)/L^2\\
4(L-2)(-X_0+X_M)/L^3\\
0
\end{pmatrix}.
\end{gathered}
```

At the equation-determined endpoint $`L=2`$, the same matrix has rank one, consistent with the separate endpoint gauge analysis. No conclusion there is obtained by dividing by $`L-2`$.

For the vector polynomial, direct use of $`b^2-4ac`$ gives

```math
\begin{aligned}
\mathop{\mathrm{disc}}\nolimits P_V
&=[8g^2L^2(L-1)(L-4)]^2\\
&\quad-4[16(L-1)^2][3g^4L^4(L-4)(3L-4)]\\
&=-512g^4L^4(L-4)(L-1)^3.
\end{aligned}
```

Let $`\Delta^2=2(4-L)/(L-1)`$. Substitution, expansion, and collection modulo this defining equation give

```math
\begin{gathered}
P_V\!\left[\frac{g^2L^2}{2}
 \left(\frac{\Delta^2}{4}\pm\Delta\right)\right]=0,\\
P_{3/2}\!\left(\frac{1\pm\Delta}{2}\right)=0,
\qquad
P_{1/2}\!\left(\frac{-1\pm\Delta}{2}\right)=0,\\
\mathop{\mathrm{disc}}\nolimits P_{3/2}
=-1152(L-4)(L-1)(3L-4)^2,\\
\mathop{\mathrm{disc}}\nolimits P_{1/2}
=-2048(L-4)^3(L-1).
\end{gathered}
```

These remainders were identically zero with $`g,L`$ symbolic. The critical values follow by solving the merger and rank conditions, then substituting into the branch equation:

```math
\begin{aligned}
3L-4=0&\ \Longrightarrow\ L=\frac43,
&\alpha g^2&=\frac{8(L-1)}{L^2}=\frac32,\\
2-L=0&\ \Longrightarrow\ L=2,
&\alpha g^2&=\frac{8(L-1)}{L^2}=2.
\end{aligned}
```

Finally the local polarization totals, independently of kinetic signs, agree with the multiplet counts:

```math
\begin{aligned}
N_B^{\mathrm{generic}}
 &=5+9+1+1+3+3+4+4+8+6=44,\\
N_F^{\mathrm{generic}}
 &=8+12+12+4+4+4=44,\\
44_B+44_F
 &=(8_B+8_F)+(4_B+4_F)+(32_B+32_F),\\
N_B^{L=2}&=5+8+6+3+4+6=32,\\
N_F^{L=2}&=8+8+12+4=32,\\
32_B+32_F&=(8_B+8_F)+(24_B+24_F).
\end{aligned}
```

The critical merger keeps the generic count through generalized solution chains; the endpoint reduces it through additional quadratic gauge directions. The multiplet count is a local quadratic result. Relative kinetic signs use the paper's reality convention as described in [the norm analysis](kinetic_norms.md); global boundary admissibility and nonlinear source invariance are separate questions.

