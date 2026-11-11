---
title: Full fermionic gauged Weyl-squared density from the calculated map
created: 2026-09-21
status: full-covariant map insertion with the stated algebraic checks
reference_id: GAUGED-WEYL2-MAP-DENSITY-v1
base_map: UNG-WEYL2-FERMIONIC-MAP-v1
inherited_conventions: UNG-WEYL2-OP58-CONVENTIONS-v5
gauged_extension: CO-GAUGED-DW-FULL-COVARIANTS-v1
assumptions: [A1, A2, A3, A4, A5, A6]
---

# Full fermionic gauged Weyl-squared calculation

<a id="1-problem-and-target"></a>

## Problem and Target

The gauged Weyl-squared density uses the calculated Weyl-to-linear map and the Coomans–Özkan realization of the gauged Dilaton-Weyl multiplet. The derivation first determines the full gauged composites, then inserts the Weyl linear multiplet into the defining-vector density. The final result is GA24, with every linear-multiplet slot explicitly multiplied out.

**A1.** Use FM01–FM04 of the [anchored map](linear_multiplet.md),
including the adopted $`8/3`$ coefficient of the composite spinor. The map
is an input to the density insertion; the algebraic checks below concern
its substitution, coefficient collection and gauged realization.

**A2.** Work gauge-unfixed in five dimensions, off shell in the target DW
field content, on a patch $`\sigma\ne0`$. The parameter g is real and
constant. No weak-g expansion, physical-fermion truncation, auxiliary
elimination or background equation is used in the action derivation.

**A3.** The source vector-multiplet constraint equations construct the
DW multiplet. Solving them for Y, T, chi and D is part of the change of
multiplet description, not the use of an equation of motion to remove an
independent field of the final higher-derivative action.

**A4.** Keep the same local vector–linear density representative as WA24.
Do not perform a fermionic integration by parts. Retain its full P/E
bridge and all derivatives in their original order.

**A5.** The endpoint is the complete action in the paper's **full
supercovariant notation**. T, chi, D and all hatted objects mean the explicit
gauged definitions derived below. No unspecified fermion remainder is
allowed. This is not a claim that every defined covariant has been
multiplied into a single polynomial of ordinary partial derivatives.

**A6.** Keep the CO compensator orientation and parameter g when converting
source formulas. The subscript c only identifies its role; it introduces
no minus sign, rescaling or gauge choice. The original ungauged conventions
and action are preserved.

The two-derivative action retains
$`O(\text{three fermions})`$ in chi and $`O(\text{four fermions})`$ in D.
The present calculation uses their full covariant completion from the
primary Weyl-multiplet constraint equations.

<a id="2-convention-ledger"></a>

## Convention Ledger

<!-- ASSERT_CONVENTION: natural_units=hbar=c=1, metric_signature=(-,+,+,+,+), source_lock=UNG-WEYL2-OP58-CONVENTIONS-v5, gauged_extension=CO-GAUGED-DW-FULL-COVARIANTS-v1 -->

$`a,b,c,\ldots,m,n,p=0,\ldots,4`$ are tangent indices; $`\mu,\nu,\ldots`$
are world indices; $`i,j=1,2`$. Use $`\eta=(-,+,+,+,+)`$,
$`\varepsilon^{01234}=+1`$, $`\varepsilon_{01234}=-1`$,
$`\gamma^{01234}=i\mathbf1`$, and unit-weight (anti)symmetrization.
$`\{\gamma^a,\gamma^b\}=2\eta^{ab}`$ and
$`\gamma^{a_1\ldots a_r}=\gamma^{[a_1}\cdots\gamma^{a_r]}`$.
Repeated antisymmetric pairs are full sums, without an implicit $`1/2`$.

The Majorana bar is linear: $`\bar\zeta^i=(\zeta^i)^T\mathsf C`$,
$`\mathsf C^T=-\mathsf C`$, $`(\gamma_a)^T\mathsf C=\mathsf C\gamma_a`$.
Spinors and SUSY parameters are odd; parameter-contracted transformations
and covariant derivatives are even. No left/right fermionic functional
variation of the final action is performed. The contracted flips are
$`\bar u v=-\bar v u`$, $`\bar u\gamma_a v=-\bar v\gamma_a u`$ and
$`\bar u\gamma_{ab}v=+\bar v\gamma_{ab}u`$; for fixed upper SU(2) indices
the corresponding signs are $`+,+,-`$.

$`X_i=X^j\epsilon_{ji}`$, $`\epsilon_{12}=\epsilon^{12}=1`$, and suppressed
bilinears mean $`\bar u\Gamma v=\bar u^i\Gamma v_i`$. In particular
$`\bar\psi^i\psi^j`$ is a symmetric, even triplet. Both lowered indices of
a symmetric tensor are lowered separately, in this same order.

$`\psi^i`$ is the dilatino, $`\psi_\mu^i`$ the gravitino and $`\phi_\mu^i`$
the dependent S connection. The independent compensator is
$`(L_c^{ij},\varphi_c^i,E_c^a,N_c)`$; its potential is $`E_{c\,\mu\nu\rho}`$.
The Weyl composite is $`(L_W^{ij},\varphi_W^i,E_W^a,N_W)`$.
**The c and W multiplets are different.**

All curvatures use master G/R, including the operational $`+8\bar\psi e\gamma\chi`$
term of $`\widehat R'(M)`$. The Riemann sign is
$`[\nabla_\mu,\nabla_\nu]X^\rho=R^\rho{}_{\sigma\mu\nu}X^\sigma`$.
$`e=\det e_\mu{}^a>0`$ and the world epsilon is $`e^{-1}[\mu\nu\rho\sigma\lambda]`$.
The source coupling has $`w(g)=0`$ before compensator gauge fixing.
The curvature normalization remains $`\sigma\widehat C^2/8`$.
Fourier/state normalization and renormalization conventions do not enter.

The source conversion is only
$`F_{\mu\nu}\to G_{\mu\nu}`$ for the defining vector and
$`(L,\varphi,E,N)\to(L_c,\varphi_c,E_c,N_c)`$ for its compensator.
The two notations for the dual H agree because
$`-\varepsilon_{abcde}\widehat H^{edc}/6 =+\varepsilon_{abcde}\widehat H^{cde}/6`$.
No metric, epsilon, coupling or compensator sign is reversed.

<a id="3-definitions-and-required-identities"></a>

## Definitions and Required Identities

<a id="31-primary-source-inputs-and-their-exact-scope"></a>

### Primary source inputs and their exact scope

The local Weyl-multiplet paper, W(5.10)–(5.14), printed p.27/PDF p.28,
gives the following **full supercovariant** improved-vector constraints.
We write its scalar constraint as $`\mathcal C`$ to distinguish it from
$`C_\mu`$; $`S^{ij},\Gamma^i,\mathcal C,\mathcal H_a`$ below are temporary
source constraint names, not additional physical fields:

```math
\begin{aligned}
S^{ij}&=2\sigma Y^{ij}-\frac i2\bar\psi^i\psi^j,\\
\Gamma^i&=i\sigma\mathord{\not{\mathcal D}}\psi^i
+\frac i2\mathord{\not{\mathcal D}}\sigma\psi^i
-\frac14\gamma\!\cdot\!\widehat G\psi^i
+Y^{ij}\psi_j+2\sigma\gamma\!\cdot\!T\psi^i-8\sigma^2\chi^i,\\
\mathcal C&=-\frac14\widehat G_{ab}\widehat G^{ab}
-\frac12\bar\psi\mathord{\not{\mathcal D}}\psi
+\sigma\Box^c\sigma+\frac12(\mathcal D_a\sigma)(\mathcal D^a\sigma)
+Y^{ij}Y_{ij}+i\bar\psi\gamma\!\cdot\!T\psi\\
&\quad-16i\sigma\bar\psi\chi-\frac{104}{3}\sigma^2T_{ab}T^{ab}
+8\sigma\widehat G_{ab}T^{ab}-4\sigma^2D,\\
\mathcal H_a&=-\frac18\varepsilon_{abcde}\widehat G^{bc}\widehat G^{de}
-\mathcal D^b\left(8\sigma^2T_{ba}-\sigma\widehat G_{ba}
-\frac i4\bar\psi\gamma_{ba}\psi\right).
\end{aligned}\tag{GC01}
```

Their Q laws, W(5.11),(5.13), are

```math
\begin{aligned}
\delta_Q S^{ij}&=i\bar\epsilon^{(i}\Gamma^{j)},\\
\delta_Q\Gamma^i&=-\frac i2\gamma^a\mathcal D_aS^{ij}\epsilon_j
-\frac i2\gamma^a\mathcal H_a\epsilon^i
+\frac12\mathcal C\epsilon^i-\gamma\!\cdot\!T S^{ij}\epsilon_j.
\end{aligned}\tag{GC02}
```

These have precisely the same component normalization as the compensator
Q laws in master L01. CO(5.2) fixes the gauged lowest constraint as
$`S^{ij}+gL_c^{ij}=0`$. This will determine the spinor and scalar deformations
without importing the cubic/quartic omissions of the truncated CO formulas.
The source constraints are W(5.10)–(5.14), printed p.27/PDF p.28,
listed in the [bibliography](../../../references/bibliography.md).

CO(5.5)–(5.8), PDF/printed pp.16–17, fixes the form sector:

```math
\begin{aligned}
G_{\mu\nu}&=2\partial_{[\mu}C_{\nu]},\qquad
\widehat G_{\mu\nu}=G_{\mu\nu}-\bar\psi_{[\mu}\gamma_{\nu]}\psi
+\frac i2\sigma\bar\psi_{[\mu}\psi_{\nu]},\\
\widehat H_{\mu\nu\rho}&=3\partial_{[\mu}B_{\nu\rho]}
+\frac32 C_{[\mu}G_{\nu\rho]}+\frac g2E_{c\,\mu\nu\rho}
-\frac34\sigma^2\bar\psi_{[\mu}\gamma_\nu\psi_{\rho]}
-\frac{3i}{2}\sigma\bar\psi_{[\mu}\gamma_{\nu\rho]}\psi,\\
\delta C_\mu&=\partial_\mu\Lambda,\qquad
\delta E_{c\,\mu\nu\rho}=3\partial_{[\mu}\Lambda_{\nu\rho]},\qquad
\delta B_{\mu\nu}=2\partial_{[\mu}\Lambda_{\nu]}
-\frac12\Lambda G_{\mu\nu}-\frac g2\Lambda_{\mu\nu}.
\end{aligned}\tag{GC03}
```

The last line is an ordinary bosonic form gauge transformation, not an
adoption of the quarantined literal SUSY potential laws in master L04.

<a id="32-the-density-bridge-and-gauged-defining-vector"></a>

### The density, bridge and gauged defining vector

Master A01–A02 gives

```math
\begin{aligned}
e^{-1}\mathcal L_{VL}={}&Y^{ij}L_{ij}+i\bar\lambda\varphi
-\frac12\bar\psi_m^i\gamma^m\lambda^jL_{ij}+A_aP^a
+\rho N+\frac\rho2\bar\psi_m\gamma^m\varphi
+\frac{i\rho}{4}\bar\psi_m^i\gamma^{mn}\psi_n^jL_{ij}.
\end{aligned}\tag{GA01}
```

```math
P^a=E^a+\frac i2\bar\psi_b\gamma^{ba}\varphi
+\frac14\bar\psi_b^i\gamma^{abc}\psi_c^jL_{ij}.
\tag{GA02}
```

The first three defining-vector identifications remain
$`(\rho,A_\mu,\lambda^i)=(\sigma,C_\mu,\psi^i)`$.
Section 4.1 derives its fourth slot exactly, including its fermionic part.
The same full density is used at nonzero g; the gauging enters its
composite vector and background fields.

<a id="4-detailed-derivation"></a>

## Detailed Derivation

<a id="41-solve-the-lowest-gauged-constraint-and-vary-it"></a>

### Solve the lowest gauged constraint and vary it

<!-- ASSERT_CONVENTION: source_lock=UNG-WEYL2-OP58-CONVENTIONS-v5, gauged_extension=CO-GAUGED-DW-FULL-COVARIANTS-v1 -->

From CO(5.2) and GC01,

```math
2\sigma Y^{ij}-\frac i2\bar\psi^i\psi^j+gL_c^{ij}=0
\quad\Longrightarrow\quad
Y^{ij}=\frac{i}{4\sigma}\bar\psi^{(i}\psi^{j)}
-\frac{g}{2\sigma}L_c^{ij}.
\tag{GA03}
```

The factor $`1/(2\sigma)`$ multiplies both terms on the right of the
first equation. The scalar fixed-index flip makes the spinor bilinear
symmetric, so its written symmetrization changes no coefficient.
Since g is constant, GC02 and L01 give

```math
\delta_Q(S^{ij}+gL_c^{ij})
=i\bar\epsilon^{(i}\Gamma^{j)}+ig\bar\epsilon^{(i}\varphi_c^{j)}
=i\bar\epsilon^{(i}(\Gamma^{j)}+g\varphi_c^{j)}).
\tag{GC04}
```

The next constraint is therefore $`\Gamma^i+g\varphi_c^i=0`$.
Vary it and display every compensator term:

```math
\begin{aligned}
\delta_Q(\Gamma^i+g\varphi_c^i)={}&
-\frac i2\gamma^a\mathcal D_aS^{ij}\epsilon_j
-\frac i2\gamma^a\mathcal H_a\epsilon^i
+\frac12\mathcal C\epsilon^i-\gamma\!\cdot\!T S^{ij}\epsilon_j\\
&-\frac{ig}{2}\gamma^a\mathcal D_aL_c^{ij}\epsilon_j
-\frac{ig}{2}\gamma^aE_{ca}\epsilon^i
+\frac g2N_c\epsilon^i-g\gamma\!\cdot\!T L_c^{ij}\epsilon_j\\
={}&-\frac i2\gamma^a\mathcal D_a(S^{ij}+gL_c^{ij})\epsilon_j
-\frac i2\gamma^a(\mathcal H_a+gE_{ca})\epsilon^i
+\frac12(\mathcal C+gN_c)\epsilon^i
-\gamma\!\cdot\!T(S^{ij}+gL_c^{ij})\epsilon_j.
\end{aligned}\tag{GC05}
```

Thus the scalar and vector constraints are $`\mathcal C+gN_c=0`$ and
$`\mathcal H_a+gE_{ca}=0`$. This argument uses the full source covariants;
it does not discard higher fermions when adding the compensator multiplet.

It also checks the defining-vector Y law. Applying the chain rule to GA03
and comparing with the independent-vector transformation gives

```math
\begin{aligned}
2\sigma(\delta_QY^{ij}_{\rm composite}-\delta_QY^{ij}_{\rm vector})
&=-i\bar\epsilon^{(i}(\Gamma^{j)}+g\varphi_c^{j)})=0,\\
\delta_SY^{ij}_{\rm composite}&=\frac i2\bar\eta^{(i}\psi^{j)}.
\end{aligned}\tag{GC06}
```

For the first line, the variations of $`2\sigma Y^{ij}`$ other than
$`2\sigma\delta Y^{ij}`$ and those of $`-i\bar\psi^i\psi^j/2`$ are the
same on both sides of the defining constraint, leaving exactly the displayed
difference. For the second line, $`\delta_S\sigma=\delta_SL_c=0`$ and
$`\delta_S\psi^i=\sigma\eta^i`$: the two varied spinors in
$`i\bar\psi^{(i}\psi^{j)}/(4\sigma)`$ give
$`i(\bar\eta^{(i}\psi^{j)}+\bar\psi^{(i}\eta^{j)})/4 =i\bar\eta^{(i}\psi^{j)}/2`$ by the fixed-index scalar flip.

<a id="42-solve-the-spinor-constraint-including-its-cubic-term"></a>

### Solve the spinor constraint, including its cubic term

Move $`-8\sigma^2\chi^i`$ to the other side of
$`\Gamma^i+g\varphi_c^i=0`$ and divide each term by $`8\sigma^2`$:

```math
\begin{aligned}
\chi^i={}&\frac i{8\sigma}\mathord{\not{\mathcal D}}\psi^i
+\frac i{16\sigma^2}\mathord{\not{\mathcal D}}\sigma\psi^i
-\frac1{32\sigma^2}\gamma\!\cdot\!\widehat G\psi^i
+\frac1{8\sigma^2}Y^{ij}\psi_j
+\frac1{4\sigma}\gamma\!\cdot\!T\psi^i
+\frac g{8\sigma^2}\varphi_c^i,\\
\frac1{8\sigma^2}Y^{ij}\psi_j
&=\frac i{32\sigma^3}(\bar\psi^i\psi^j)\psi_j
-\frac g{16\sigma^3}L_c^{ij}\psi_j.
\end{aligned}\tag{GC07}
```

The bilinear in the last line is even, so it commutes through $`\psi_j`$.
The full spinor composite, with no cubic remainder, is consequently

```math
\begin{aligned}
\chi^i={}&\frac i{8\sigma}\mathord{\not{\mathcal D}}\psi^i
+\frac i{16\sigma^2}\mathord{\not{\mathcal D}}\sigma\psi^i
-\frac1{32\sigma^2}\gamma\!\cdot\!\widehat G\psi^i
+\frac1{4\sigma}\gamma\!\cdot\!T\psi^i
+\frac i{32\sigma^3}\psi_j\bar\psi^i\psi^j\\
&-\frac g{16\sigma^3}L_c^{ij}\psi_j
+\frac g{8\sigma^2}\varphi_c^i.
\end{aligned}\tag{GC08}
```

The last two terms reproduce the gauged part of CO(5.3), with its Y
substitution performed. The cubic term is supplied by the full GC01,
not inferred from the truncated two-derivative action.

<a id="43-solve-the-scalar-constraint-and-expand-every-y-product"></a>

### Solve the scalar constraint and expand every Y product

In $`\mathcal C+gN_c=0`$, move $`-4\sigma^2D`$ to the other side and divide
by $`4\sigma^2`$. The source coefficients become
$`-1/16,-1/8,1/4,1/8,1/4, i/4,-4i,-26/3,2,g/4`$, with the displayed
powers of sigma:

```math
\begin{aligned}
D={}&\frac1{4\sigma}\Box^c\sigma
+\frac1{8\sigma^2}(\mathcal D_a\sigma)(\mathcal D^a\sigma)
-\frac1{16\sigma^2}\widehat G_{ab}\widehat G^{ab}
-\frac1{8\sigma^2}\bar\psi\mathord{\not{\mathcal D}}\psi
+\frac1{4\sigma^2}Y^{ij}Y_{ij}\\
&+\frac i{4\sigma^2}\bar\psi\gamma^{ab}\psi T_{ab}
-\frac{4i}{\sigma}\bar\psi\chi-\frac{26}{3}T_{ab}T^{ab}
+\frac2\sigma\widehat G_{ab}T^{ab}+\frac g{4\sigma^2}N_c.
\end{aligned}\tag{GC09}
```

Lower Y with the two epsilon tensors before multiplying. Both terms in
Y are even, and the lower triplet contraction is symmetric. Hence

```math
\begin{aligned}
Y^{ij}Y_{ij}
={}&\left(\frac i{4\sigma}\bar\psi^i\psi^j-\frac g{2\sigma}L_c^{ij}\right)
\left(\frac i{4\sigma}\bar\psi_i\psi_j-\frac g{2\sigma}L_{c\,ij}\right)\\
={}&-\frac1{16\sigma^2}(\bar\psi^i\psi^j)(\bar\psi_i\psi_j)
-\frac{ig}{8\sigma^2}(\bar\psi^i\psi^j)L_{c\,ij}
-\frac{ig}{8\sigma^2}L_c^{ij}(\bar\psi_i\psi_j)
+\frac{g^2}{4\sigma^2}L_c^{ij}L_{c\,ij}\\
={}&-\frac1{16\sigma^2}(\bar\psi^i\psi^j)(\bar\psi_i\psi_j)
-\frac{ig}{4\sigma^2}L_{c\,ij}\bar\psi^i\psi^j
+\frac{g^2}{4\sigma^2}L_c^{ij}L_{c\,ij}.
\end{aligned}\tag{GC10}
```

The first sign is $`i^2=-1`$. The two mixed terms have the same sign:
$`L_c^{ij}\bar\psi_i\psi_j=L_{c\,ij}\bar\psi^i\psi^j`$, since lowering
both indices contributes two epsilon tensors. No odd spinors are swapped.
Multiplying GC10 by $`1/(4\sigma^2)`$ and inserting it into GC09 gives

```math
\begin{aligned}
D={}&\frac1{4\sigma}\Box^c\sigma
+\frac1{8\sigma^2}(\mathcal D_a\sigma)(\mathcal D^a\sigma)
-\frac1{16\sigma^2}\widehat G_{ab}\widehat G^{ab}
-\frac1{8\sigma^2}\bar\psi\mathord{\not{\mathcal D}}\psi
-\frac1{64\sigma^4}(\bar\psi^i\psi^j)(\bar\psi_i\psi_j)
-\frac{4i}{\sigma}\bar\psi\chi\\
&+\left(-\frac{26}{3}T_{ab}+\frac2\sigma\widehat G_{ab}
+\frac i{4\sigma^2}\bar\psi\gamma_{ab}\psi\right)T^{ab}
+\frac g{4\sigma^2}N_c
-\frac{ig}{16\sigma^4}L_{c\,ij}\bar\psi^i\psi^j
+\frac{g^2}{16\sigma^4}L_c^{ij}L_{c\,ij}.
\end{aligned}\tag{GC11}
```

This includes the quartic term required by the g=0 master D01 and both
mixed Y products. The chi, box and gaugino derivative in this formula
are themselves the full gauged quantities; their fermions are not omitted.

<a id="44-solve-the-tensor-relation-and-check-the-form-gauge-symmetry"></a>

### Solve the tensor relation and check the form gauge symmetry

CO(5.6) is $`\varepsilon_{abcde}\widehat H^{cde}/6 =8\sigma^2T_{ab}-\sigma\widehat G_{ab}-i\bar\psi\gamma_{ab}\psi/4`$.
Move its last two terms across and divide by $`8\sigma^2`$:

```math
T_{ab}=\frac1{8\sigma^2}\left(\sigma\widehat G_{ab}
+\frac16\varepsilon_{abcde}\widehat H^{cde}
+\frac i4\bar\psi\gamma_{ab}\psi\right),
\qquad
T_{ab}\big|_{\text{explicit }gE_c}=\frac g{96\sigma^2}
\varepsilon_{abcde}E_c{}^{cde}.
\tag{GC12}
```

In the last expression the subscript c on E labels the compensator;
the superscript letters are its three tangent indices. The coefficient
is $`(1/8)(1/6)(1/2)=1/96`$, from GC03. Write the bosonic form definitions
with $`B=B_{\mu\nu}dx^\mu\wedge dx^\nu/2`$ and
$`E_c=E_{c\,\mu\nu\rho}dx^\mu\wedge dx^\nu\wedge dx^\rho/3!`$:

```math
\begin{aligned}
H&=dB+\frac12C\wedge G+\frac g2E_c,\qquad G=dC,\\
dH&=\frac12G\wedge G+\frac g2dE_c,\\
\delta H&=d\left(d\Lambda_1-\frac12\Lambda G-\frac g2\Lambda_2\right)
+\frac12d\Lambda\wedge G+\frac g2d\Lambda_2\\
&=-\frac12d\Lambda\wedge G-\frac12\Lambda\,dG
-\frac g2d\Lambda_2+\frac12d\Lambda\wedge G+\frac g2d\Lambda_2=0.
\end{aligned}\tag{GC13}
```

The last equality uses $`dG=d^2C=0`$ and $`d^2\Lambda_1=0`$.
In components, dividing the four-form equation by four gives
$`\partial_{[\mu}H_{\nu\rho\sigma]} =3G_{[\mu\nu}G_{\rho\sigma]}/4 +g\partial_{[\mu}E_{c\,\nu\rho\sigma]}/2`$.
This checks the source factors independently. Its supercovariant form is
CO(5.5), interpreted with the complete constrained-vector realization.
No SUSY potential-law repair is assumed in this bosonic gauge check.

<a id="45-propagate-the-gauging-through-derivatives-and-connections"></a>

### Propagate the gauging through derivatives and connections

<!-- ASSERT_CONVENTION: source_lock=UNG-WEYL2-OP58-CONVENTIONS-v5, gauged_extension=CO-GAUGED-DW-FULL-COVARIANTS-v1 -->

Start with the full vector derivative, CO(2.16)/master V02, and insert GA03:

```math
\begin{aligned}
\mathcal D_\mu\sigma&=(\partial_\mu-b_\mu)\sigma-\frac i2\bar\psi_\mu\psi,\\
\mathcal D_\mu\psi^i&=\left(\partial_\mu-\frac32b_\mu
+\frac14\omega_\mu{}^{ab}\gamma_{ab}\right)\psi^i-V_\mu{}^{ij}\psi_j
+\frac14\gamma\!\cdot\!\widehat G\psi_\mu^i
+\frac i2\mathord{\not{\mathcal D}}\sigma\psi_\mu^i\\
&\quad+\frac i{4\sigma}\psi_{\mu j}\bar\psi^i\psi^j
-\frac g{2\sigma}L_c^{ij}\psi_{\mu j}
-\sigma\gamma\!\cdot\!T\psi_\mu^i-\sigma\phi_\mu^i.
\end{aligned}\tag{GC14}
```

The connection term $`-gL_c^{ij}\psi_{\mu j}/(2\sigma)`$ is necessary
even if a later gauge sets the dilatino to zero. For clarity, insert all
terms of GC14 into the first term of GC08, not just its ordinary derivative:

```math
\begin{aligned}
\chi^i={}&\frac i{8\sigma}\gamma^\mu
\left[\left(\partial_\mu-\frac32b_\mu+\frac14\omega_\mu{}^{ab}\gamma_{ab}\right)\psi^i-V_\mu{}^{ij}\psi_j\right]
+\frac i{32\sigma}\gamma^\mu\gamma\!\cdot\!\widehat G\psi_\mu^i
-\frac1{16\sigma}\gamma^\mu\mathord{\not{\mathcal D}}\sigma\psi_\mu^i\\
&-\frac1{32\sigma^2}\gamma^\mu\psi_{\mu j}\bar\psi^i\psi^j
-\frac{ig}{16\sigma^2}L_c^{ij}\gamma^\mu\psi_{\mu j}
-\frac i8\gamma^\mu\gamma\!\cdot\!T\psi_\mu^i-\frac i8\gamma^\mu\phi_\mu^i\\
&+\frac i{16\sigma^2}\mathord{\not{\mathcal D}}\sigma\psi^i
-\frac1{32\sigma^2}\gamma\!\cdot\!\widehat G\psi^i
+\frac1{4\sigma}\gamma\!\cdot\!T\psi^i
+\frac i{32\sigma^3}\psi_j\bar\psi^i\psi^j
-\frac g{16\sigma^3}L_c^{ij}\psi_j+\frac g{8\sigma^2}\varphi_c^i.
\end{aligned}\tag{GC15}
```

The coefficients on the first two lines are respectively
$`(i/8)(1/4)=i/32`$, $`(i/8)(i/2)=-1/16`$,
$`(i/8)(i/4)=-1/32`$, $`(i/8)(-g/2)=-ig/16`$, and
$`(i/8)(-1)=-i/8`$. No gamma matrices have been silently commuted.

The exact box, matter derivatives and dependent connections follow.
Every T, chi and D on their right means GC12, GC08 and GC11, respectively.
This is where gauging enters hatted quantities whose formula has no
explicit g. No curvature is evaluated using ungauged chi or T.

```math
\Box^c\sigma=(\partial^a-2b^a+\omega_b{}^{ba})\mathcal D_a\sigma
-\tfrac i2\bar\psi_a\mathcal D^a\psi
-2\sigma\bar\psi_a\gamma^a\chi
+\tfrac12\bar\psi_a\gamma^a\gamma\!\cdot\!T\psi
+\tfrac12\bar\phi_a\gamma^a\psi+2f_a{}^a\sigma.
\tag{GC16}
```

```math
\begin{aligned}
\mathcal D_\mu T_{ab}&=\partial_\mu T_{ab}-b_\mu T_{ab}
+2\omega_\mu{}^c{}_{[a}T_{b]c}-\tfrac i2\bar\psi_\mu\gamma_{ab}\chi
+\tfrac{3i}{32}\bar\psi_\mu\widehat R_{ab}(Q),\\
\mathcal D_\mu\chi^i&=(\partial_\mu-\tfrac32b_\mu+\tfrac14\omega_\mu{}^{ab}\gamma_{ab})\chi^i
-V_\mu{}^{ij}\chi_j-\tfrac14\psi_\mu^iD
+\tfrac1{64}\gamma\!\cdot\!\widehat R^{ij}(V)\psi_{\mu j}\\
&\quad-\tfrac i8\gamma^{ab}\mathord{\not{\mathcal D}}T_{ab}\psi_\mu^i
+\tfrac i8\gamma^a\mathcal D^bT_{ab}\psi_\mu^i
+\tfrac14\gamma^{abcd}T_{ab}T_{cd}\psi_\mu^i
-\tfrac16T^2\psi_\mu^i-\tfrac14\gamma\!\cdot\!T\phi_\mu^i,\\
\mathcal D_\mu D&=(\partial_\mu-2b_\mu)D
-\bar\psi_\mu\mathord{\not{\mathcal D}}\chi
+\tfrac{5i}{3}\bar\psi_\mu\gamma\!\cdot\!T\chi+i\bar\phi_\mu\chi.
\end{aligned}\tag{GC17}
```

```math
\begin{aligned}
\omega_\mu{}^{ab}={}&2e^{\nu[a}\partial_{[\mu}e_{\nu]}{}^{b]}
-e^{\nu[a}e^{b]\rho}e_{\mu c}\partial_\nu e_\rho{}^c
+2e_\mu{}^{[a}b^{b]}+\tfrac12\bar\psi^{[a}\gamma^{b]}\psi_\mu
+\tfrac14\bar\psi^a\gamma_\mu\psi^b,\\
\widehat R'_{\mu\nu}{}^i(Q)={}&2\partial_{[\mu}\psi_{\nu]}^i
+\tfrac12\omega_{[\mu}{}^{ab}\gamma_{ab}\psi_{\nu]}^i+b_{[\mu}\psi_{\nu]}^i
-2V_{[\mu}{}^{ij}\psi_{\nu]j}+2i\gamma\!\cdot\!T\gamma_{[\mu}\psi_{\nu]}^i,\\
\phi_\mu^i={}&\tfrac i3\gamma^a\widehat R'_{\mu a}{}^i(Q)
-\tfrac i{24}\gamma_\mu\gamma^{ab}\widehat R'_{ab}{}^i(Q),\\
\widehat R_{\mu\nu}{}^i(Q)={}&\widehat R'_{\mu\nu}{}^i(Q)-2i\gamma_{[\mu}\phi_{\nu]}^i.
\end{aligned}\tag{GC18}
```

```math
\begin{aligned}
V_{\mu\nu}{}^{ij}&=2\partial_{[\mu}V_{\nu]}{}^{ij}
-2V_{[\mu}{}^{k(i}V_{\nu]k}{}^{j)},\\
\widehat R_{\mu\nu}{}^{ij}(V)&=V_{\mu\nu}{}^{ij}
-3i\bar\phi_{[\mu}^{(i}\psi_{\nu]}^{j)}
-8\bar\psi_{[\mu}^{(i}\gamma_{\nu]}\chi^{j)}
-i\bar\psi_{[\mu}^{(i}\gamma\!\cdot\!T\psi_{\nu]}^{j)}.
\end{aligned}\tag{GC19}
```

```math
\begin{aligned}
\widehat R'_{\mu\nu}{}^{ab}(M)={}&R_{\mu\nu}{}^{ab}(\omega)
+i\bar\phi_{[\mu}\gamma^{ab}\psi_{\nu]}
+i\bar\psi_{[\mu}\gamma^{[a}\gamma\!\cdot\!T\gamma^{b]}\psi_{\nu]}\\
&+\bar\psi_{[\mu}\gamma^{[a}\widehat R_{\nu]}{}^{b]}(Q)
+\tfrac12\bar\psi_{[\mu}\gamma_{\nu]}\widehat R^{ab}(Q)
+8\bar\psi_{[\mu}e_{\nu]}{}^{[a}\gamma^{b]}\chi,\\
\mathcal R_{\mu\nu}&=\widehat R'_{\mu\rho}{}^{ab}(M)e_b{}^\rho e_{\nu a},
\qquad \mathcal R=\mathcal R_\mu{}^\mu,\\
f_\mu{}^a&=-\tfrac16\mathcal R_\mu{}^a+\tfrac1{48}e_\mu{}^a\mathcal R,\\
\widehat R_{\mu\nu}{}^{ab}(M)&=\widehat R'_{\mu\nu}{}^{ab}(M)
+8f_{[\mu}{}^{[a}e_{\nu]}{}^{b]},\qquad
\widehat C_{abcd}=e_a{}^\mu e_b{}^\nu\widehat R_{\mu\nu cd}(M).
\end{aligned}\tag{GC20}
```

```math
\mathcal D_\mu\Phi=\partial_\mu\Phi
-\delta_D(b_\mu)\Phi-\delta_M(\omega_\mu)\Phi
-\delta_U(V_\mu)\Phi-\delta_Q(\psi_\mu)\Phi
-\delta_S(\phi_\mu)\Phi-\delta_K(f_\mu)\Phi,\qquad
\mathcal D_a=e_a{}^\mu\mathcal D_\mu.
\tag{GC21}
```

Here $`R_{\mu\nu}{}^{ab}(\omega)=2\partial_{[\mu}\omega_{\nu]}{}^{ab} +2\omega_{[\mu}{}^{ac}\omega_{\nu]c}{}^b`$ and the full derivative is a
derivation on tensor products. In GC21, $`\Phi`$ means the actual field
being differentiated. The second derivative of T acts on the first
derivative's tangent index and its S/K laws as well as on its tensor indices.
It cannot be replaced by a bosonic second derivative.

For the gravitino curvature, the full first derivative appearing in the
final result is explicitly the bosonic derivative (weight 3/2, both lower
Lorentz indices and the SU(2) doublet connection) plus these terms:

```math
\begin{aligned}
\mathcal D_\mu\widehat R_{ab}{}^i(Q)={}&
\left(\partial_\mu-\frac32b_\mu+\frac14\omega_\mu{}^{cd}\gamma_{cd}\right)\widehat R_{ab}{}^i(Q)
+\omega_{\mu a}{}^c\widehat R_{cb}{}^i(Q)
+\omega_{\mu b}{}^c\widehat R_{ac}{}^i(Q)-V_\mu{}^{ij}\widehat R_{ab\,j}(Q)\\
&-\frac16\left(\gamma_{ab}{}^{cd}-\gamma^{cd}\gamma_{ab}
-\frac12\gamma_{ab}\gamma^{cd}\right)\widehat R_{cd}{}^i{}_j(V)\psi_\mu^j
-\frac14\widehat C_{ab}{}^{cd}\gamma_{cd}\psi_\mu^i\\
&-2i\left[\mathcal D_{[a}(\gamma\!\cdot\!T)\gamma_{b]}
-\frac13\gamma_{[b}\mathcal D_{a]}(\gamma\!\cdot\!T)
-\frac13\gamma_{[a}\mathord{\not{\mathcal D}}(\gamma\!\cdot\!T)\gamma_{b]}
-\frac13\gamma_{ab}\gamma_d\mathcal D_cT^{cd}\right]\psi_\mu^i\\
&+8T_{ab}\phi_\mu^i-\frac{16}{3}T_{[a}{}^c\gamma_{b]c}\phi_\mu^i
-\frac43\gamma_{abcd}T^{cd}\phi_\mu^i.
\end{aligned}\tag{GC22}
```

This is minus master R05 with $`(\epsilon,\eta)=(\psi_\mu,\phi_\mu)`$
added to the bosonic derivative, so the signs of all three S terms are
reversed relative to R05. There is no K term for this primary curvature.

For example, the derivative of the two explicit compensator terms in
GC08 is not zero and contains five contributions:

```math
\begin{aligned}
\mathcal D_\mu\left(-\frac g{16\sigma^3}L_c^{ij}\psi_j
+\frac g{8\sigma^2}\varphi_c^i\right)
={}&\frac{3g}{16\sigma^4}(\mathcal D_\mu\sigma)L_c^{ij}\psi_j
-\frac g{16\sigma^3}(\mathcal D_\mu L_c^{ij})\psi_j
-\frac g{16\sigma^3}L_c^{ij}\mathcal D_\mu\psi_j\\
&-\frac g{4\sigma^3}(\mathcal D_\mu\sigma)\varphi_c^i
+\frac g{8\sigma^2}\mathcal D_\mu\varphi_c^i.
\end{aligned}\tag{GC23}
```

Here $`\mathcal D_\mu\sigma^{-n}=-n\sigma^{-n-1}\mathcal D_\mu\sigma`$;
there is no Grassmann minus from the even derivative. The required
compensator derivatives are

```math
\begin{aligned}
\mathcal D_\mu L_c^{ij}&=(\partial_\mu-3b_\mu)L_c^{ij}
+2V_\mu{}^{(i}{}_kL_c^{j)k}-i\bar\psi_\mu^{(i}\varphi_c^{j)},\\
\mathcal D_\mu\varphi_c^i&=\left(\partial_\mu-\frac72b_\mu
+\frac14\omega_\mu{}^{ab}\gamma_{ab}\right)\varphi_c^i-V_\mu{}^{ij}\varphi_{c\,j}
+\frac i2\mathord{\not{\mathcal D}}L_c^{ij}\psi_{\mu j}
+\frac i2\gamma^aE_{ca}\psi_\mu^i\\
&\quad-\frac12N_c\psi_\mu^i+\gamma\!\cdot\!T L_c^{ij}\psi_{\mu j}
-3L_c^{ij}\phi_{\mu j}.
\end{aligned}\tag{GC24}
```

GC23 exhibits the terms supplied when the complete chi definition is
differentiated. It is not an additional correction to add a second time
to GC17. GC17 already defines the full Standard-Weyl derivative, evaluated
with the gauged composites. This distinction prevents double counting.

The dependencies are finite: GC03 and GC12 determine T; GC18 then
fixes phi and R(Q); GC14–GC15 fix chi; GC19–GC20 fix R(V), f and C;
GC16 and GC11 determine D. GC17/GC21–GC24 fix all displayed derivatives.
The curvature expressions must use this same chain throughout.

<a id="46-why-no-power-of-the-gauging-is-dropped"></a>

### Why no power of the gauging is dropped

Hold the original DW and compensator fields fixed while counting explicit
g factors. The equations above give these maximal polynomial degrees:

| Quantity | Maximum power of g | Reason |
|---|---:|---|
| T, Y, phi, R(Q), chi | 1 | GC03, GA03, GC12, GC14–GC18 are affine in g |
| R(V), f, C | 1 | GC19–GC20 are linear in T, phi, R(Q), chi |
| D | 2 | Y² and T² in GC09; all other terms have degree at most1 |
| $`\mathcal D T`$ | 1 | GC17 is linear in T, chi, R(Q) |
| $`\mathcal D\chi`$ | 2 | GC17 contains D, T² and T phi |
| $`\mathcal D R(Q)`$ | 2 | GC22 contains T phi; its other terms have degree at most1 |
| $`\mathcal D\mathcal D T`$ | at most2 | Differentiating GC17 introduces $`\mathcal D\chi`$, $`\mathcal D R(Q)`$ and S/K connection products |

Consequently the final action has degree at most4 in g. The highest
possible powers occur in D², DT² and the quartic T terms; this is an
exact finite polynomial, not a truncation through order g². We retain
full covariants to avoid replacing a readable action by thousands of
primitive-field products. Every g dependence of those covariants is
specified in GC03–GC24. Section5 gives an explicit sector with nonzero
g³ and g⁴, making their retention testable.

<a id="47-insert-the-defining-vector-into-every-density-term"></a>

### Insert the defining vector into every density term

<!-- ASSERT_CONVENTION: metric_signature=(-,+,+,+,+), source_lock=UNG-WEYL2-OP58-CONVENTIONS-v5 -->

Substitute GA02 and GA03 in GA01, using the gauged composites GC03–GC24, and put the Weyl composite linear
multiplet in its four slots. The result before expanding the map is

```math
\begin{aligned}
e^{-1}\mathcal L_{\sigma C^2,g}^{\rm map}={}&\sigma N_W+C_aE_W^a+i\bar\psi\varphi_W
+\frac\sigma2\bar\psi_m\gamma^m\varphi_W
+\frac i2C_m\bar\psi_n\gamma^{nm}\varphi_W\\
&+\left(\frac{i}{4\sigma}\bar\psi^{(i}\psi^{j)}-\frac g{2\sigma}L_c^{ij}\right)L_{W\,ij}
-\frac12\bar\psi_m^i\gamma^m\psi^jL_{W\,ij}
+\frac{i\sigma}{4}\bar\psi_m^i\gamma^{mn}\psi_n^jL_{W\,ij}
+\frac14C_m\bar\psi_n^i\gamma^{mnp}\psi_p^jL_{W\,ij}.
\end{aligned}\tag{GA04}
```

This accounts for all terms of the density: two descendant couplings,
three spinor couplings, and four triplet couplings. In particular the
fifth and ninth terms arise from GA02, and the sixth uses the composite
Y of GA03. No term has been inferred from the bosonic action.

<a id="48-lower-the-su2-indices-before-multiplying-the-map"></a>

### Lower the SU(2) indices before multiplying the map

FM01 gives

```math
L_{W\,ij}=\frac i4\overline{\widehat R}_{ab(i}(Q)\widehat R_{j)}{}^{ab}(Q)
+\frac{256i}{3}\bar\chi_{(i}\chi_{j)}
+\frac{16}{3}\widehat R_{ab\,ij}(V)T^{ab}.
\tag{GA05}
```

Both indices have been lowered with $`\varepsilon_{ki}\varepsilon_{lj}`$;
there is no extra sign or factor two. Since $`L_{W\,ij}=L_{W\,ji}`$,
$`\bar\psi^{(i}\psi^{j)}L_{W\,ij}=\bar\psi^i\psi^jL_{W\,ij}`$:
the two terms in the symmetrization agree after relabeling $`i,j`$.
The symmetrizations on the curvature and chi bilinears in GA05 are
retained throughout the multiplication.

The two SU(2)-curvature terms in the lowered spinor obey

```math
\begin{aligned}
(\varphi_W)_i\big|_{\widehat R(V)}
&=\varepsilon_{ki}\left[\frac12\widehat R^{ab\,k}{}_{\ell}(V)
 \widehat R_{ab}{}^\ell(Q)-\frac83\widehat R^{ab\,k}{}_{\ell}(V)\gamma_{ab}\chi^\ell\right]\\
&=\frac12\widehat R^{ab}{}_{ij}(V)\widehat R_{ab}{}^j(Q)
-\frac83\widehat R^{ab}{}_{ij}(V)\gamma_{ab}\chi^j.
\end{aligned}\tag{GA06}
```

Indeed $`\widehat R^{ab\,k}{}_{\ell}(V)=\widehat R^{ab\,kr}(V)\varepsilon_{r\ell}`$,
so $`\varepsilon_{ki}\widehat R^{ab\,kr}(V)\varepsilon_{rj} =\widehat R^{ab}{}_{ij}(V)`$. This fixes the actual SU(2) contractions
in all six curvature terms obtained from the three spinor couplings.

<a id="49-multiply-the-scalar-component-by-sigma"></a>

### Multiply the scalar component by $`\sigma`$

<!-- ASSERT_CONVENTION: source_lock=UNG-WEYL2-OP58-CONVENTIONS-v5 -->

Insert all fifteen terms of FM04 in the first term of GA04. Since
$`\sigma`$ is even, it stays at the left of each product with no sign
change. In particular the four explicit fermionic coefficients become
$`3\sigma/4`$, $`-2i\sigma`$, $`-160i\sigma/3`$, and $`-256\sigma/3`$:

```math
\begin{aligned}
\sigma N_W={}&\frac{1}{8}\sigma \widehat C_{abcd}\widehat C^{abcd}+\frac{64}{3}\sigma D^2\\
 &+\frac{1024}{9}\sigma DT_{ab}T^{ab}-\frac{16}{3}\sigma \widehat C_{abcd}T^{ab}T^{cd}\\
 &-\frac{1}{3}\sigma \widehat R_{ab}{}^{ij}(V)\widehat R^{ab}{}_{ij}(V)-\frac{64}{3}\sigma (\mathcal D_aT_{bc})(\mathcal D^aT^{bc})\\
 &+\frac{64}{3}\sigma (\mathcal D_bT_{ac})(\mathcal D^aT^{bc})-\frac{128}{3}\sigma T_{ab}\mathcal D^b\mathcal D_cT^{ac}\\
 &-\frac{128}{3}\sigma \varepsilon_{abcde}T^{ab}T^{cd}\mathcal D_fT^{ef}+1024\sigma T_{ab}T^{bc}T_{cd}T^{da}\\
 &-\frac{2816}{27}\sigma (T_{ab}T^{ab})^2+\frac{3}{4}\sigma \overline{\widehat R_{ab}(Q)}\gamma^c\mathcal D_c\widehat R^{ab}(Q)\\
 &-2i\sigma T^{ab}\overline{\widehat R_{ca}(Q)}\widehat R^c{}_{b}(Q)-\frac{160i}{3}\sigma T^{ab}\overline{\widehat R_{ab}(Q)}\chi\\
 &-\frac{256}{3}\sigma \bar\chi\gamma^a\mathcal D_a\chi
\end{aligned}
\tag{GA07}
```

The ordered derivative in the eighth term remains
$`\mathcal D^b\mathcal D_cT^{ac}`$. No commutator or field equation has
been applied to it.

<a id="410-multiply-the-vector-component-by-c_a"></a>

### Multiply the vector component by $`C_a`$

In the second term of GA04 insert FM03. Contract its free index with
$`C_a`$. The factor $`C_a`$ stays outside every derivative, because this
operation is multiplication of the density, not integration by parts:

```math
\begin{aligned}
C_aE_W^a={}&\frac{1}{16}C_a\varepsilon^{abcde}\widehat C_{bcfg}\widehat C_{de}{}^{fg}-\frac{1}{12}C_a\varepsilon^{abcde}\widehat R(V)_{bc}{}^{ij}\widehat R(V)_{de\,ij}\\
 &+C_a\mathcal D_b\Big[4\widehat C^{ab}{}_{cd}T^{cd}-\frac{64}{3}DT^{ab}-\frac{128}{9}T^{ab}T_{cd}T^{cd}\\
 &\hspace{20mm}-\frac{512}{3}T^a{}_cT^{cd}T^b{}_d+8i\overline{\widehat R(Q)^{ab}}\chi-\frac{64i}{3}\bar\chi\gamma^{ab}\chi\Big]-32C_a\varepsilon^a{}_{bcde}\mathcal D^b\Big[\frac23T^{cf}\mathcal D_fT^{de}+T^c{}_f\mathcal D^dT^{ef}\Big]\\
 &-C_aT^{cd}\overline{\widehat R(Q)_{ec}}\gamma^a\widehat R(Q)^e{}_d+3C_aT_c{}^d\overline{\widehat R(Q)_e{}^a}\gamma^c\widehat R(Q)^e{}_d\\
 &+16C_aT^c{}_d\overline{\widehat R(Q)^a{}_c}\gamma^d\chi+\frac{16}{3}C_aT^{cd}\overline{\widehat R(Q)_{cd}}\gamma^a\chi\\
 &+\frac{i}{2}C_a\overline{\widehat R(Q)_{cd}}\mathcal D^a\widehat R(Q)^{cd}+\frac{3i}{2}C_a\overline{\widehat R(Q)_{cd}}\mathcal D^c\widehat R(Q)^{da}
\end{aligned}
\tag{GA08}
```

The differentiated fermion bilinears inside the bracket are included.
Their product rules, and those of every other product in this current,
are displayed in Section 4.13 below.

<a id="411-calculate-the-three-spinor-couplings-term-by-term"></a>

### Calculate the three spinor couplings term by term

<!-- ASSERT_CONVENTION: source_lock=UNG-WEYL2-OP58-CONVENTIONS-v5 -->

The eleven FM02 terms occur in their original order. The following table
shows each numerical multiplication. In the middle column $`\sigma`$ is
written with the fields in GA10; in the last column $`C_m`$ is written with
the fields in GA11. Thus the numerical factors to multiply are
$`i`$, $`1/2`$, and $`i/2`$, respectively.

| FM02 term and coefficient | $`i`$ times the coefficient | $`1/2`$ times the coefficient | $`i/2`$ times the coefficient |
|---|---|---|---|
| 1: $`-1/8`$ | $`-i/8`$ | $`-1/16`$ | $`-i/16`$ |
| 2: $`-4i`$ | $`-4i^2=4`$ | $`-2i`$ | $`-2i^2=2`$ |
| 3: $`128/3`$ | $`128i/3`$ | $`64/3`$ | $`64i/3`$ |
| 4: $`8i`$ | $`8i^2=-8`$ | $`4i`$ | $`4i^2=-4`$ |
| 5: $`8i`$ | $`8i^2=-8`$ | $`4i`$ | $`4i^2=-4`$ |
| 6: $`-64i/3`$ | $`-64i^2/3=64/3`$ | $`-32i/3`$ | $`-32i^2/3=32/3`$ |
| 7: $`1024/9`$ | $`1024i/9`$ | $`512/9`$ | $`512i/9`$ |
| 8: $`128i/3`$ | $`128i^2/3=-128/3`$ | $`64i/3`$ | $`64i^2/3=-64/3`$ |
| 9: $`8/3`$ | $`8i/3`$ | $`4/3`$ | $`4i/3`$ |
| 10: $`1/2`$ | $`i/2`$ | $`1/4`$ | $`i/4`$ |
| 11: $`-8/3`$ | $`-8i/3`$ | $`-4/3`$ | $`-4i/3`$ |

In FM02 terms6 and7 the coefficients $`\mathcal D_aT_{bc}`$ and $`T^2`$
are Grassmann even. Moving them to the right of $`\chi`$ therefore gives
$`\gamma^{ab}\gamma^c(\mathcal D_aT_{bc})\chi =\gamma^{ab}\gamma^c\chi\mathcal D_aT_{bc}`$ and
$`T^2\chi=\chi T^2`$, with no sign change.

For the dilatino coupling, place $`\bar\psi`$ before each singlet spinor
term and use the lowered contractions GA06 for the last two terms:

```math
\begin{aligned}
i\bar\psi\varphi_W={}&-\frac{i}{8}\bar\psi\gamma_{cd}\widehat R_{ab}(Q)\widehat C^{abcd}+4\bar\psi\gamma_c\widehat R_{ab}(Q)\mathcal D^aT^{bc}\\
 &+\frac{128i}{3}\bar\psi\chi D-8\bar\psi\gamma_c\mathcal D^c\widehat R_{ab}(Q)T^{ab}\\
 &-8\bar\psi\gamma_a\mathcal D^c\widehat R_{bc}(Q)T^{ab}+\frac{64}{3}\bar\psi\gamma^{ab}\gamma^c\chi\mathcal D_aT_{bc}\\
 &+\frac{1024i}{9}\bar\psi\chi T^2-\frac{128}{3}\bar\psi\gamma_a\mathcal D_b\chi T^{ab}\\
 &+\frac{8i}{3}\bar\psi\gamma_{ab}\widehat R_{cd}(Q)T^{ab}T^{cd}+\frac{i}{2}\bar\psi^i\widehat R^{ab}{}_{ij}(V)\widehat R_{ab}{}^j(Q)\\
 &-\frac{8i}{3}\bar\psi^i\widehat R^{ab}{}_{ij}(V)\gamma_{ab}\chi^j
\end{aligned}
\tag{GA09}
```

For the fourth term of GA04, multiply each FM02 spinor from the left
by $`\bar\psi_m\gamma^m`$, using the middle coefficient column:

```math
\begin{aligned}
\frac\sigma2\bar\psi_m\gamma^m\varphi_W={}&-\frac{1}{16}\sigma\bar\psi_m\gamma^m\gamma_{cd}\widehat R_{ab}(Q)\widehat C^{abcd}-2i\sigma\bar\psi_m\gamma^m\gamma_c\widehat R_{ab}(Q)\mathcal D^aT^{bc}\\
 &+\frac{64}{3}\sigma\bar\psi_m\gamma^m\chi D+4i\sigma\bar\psi_m\gamma^m\gamma_c\mathcal D^c\widehat R_{ab}(Q)T^{ab}\\
 &+4i\sigma\bar\psi_m\gamma^m\gamma_a\mathcal D^c\widehat R_{bc}(Q)T^{ab}-\frac{32i}{3}\sigma\bar\psi_m\gamma^m\gamma^{ab}\gamma^c\chi\mathcal D_aT_{bc}\\
 &+\frac{512}{9}\sigma\bar\psi_m\gamma^m\chi T^2+\frac{64i}{3}\sigma\bar\psi_m\gamma^m\gamma_a\mathcal D_b\chi T^{ab}\\
 &+\frac{4}{3}\sigma\bar\psi_m\gamma^m\gamma_{ab}\widehat R_{cd}(Q)T^{ab}T^{cd}+\frac{1}{4}\sigma\bar\psi_m^i\gamma^m\widehat R^{ab}{}_{ij}(V)\widehat R_{ab}{}^j(Q)\\
 &-\frac{4}{3}\sigma\bar\psi_m^i\gamma^m\widehat R^{ab}{}_{ij}(V)\gamma_{ab}\chi^j
\end{aligned}
\tag{GA10}
```

For the fifth term of GA04, the bridge fixes the order $`\gamma^{nm}`$.
Multiply each FM02 term from the left by $`C_m\bar\psi_n\gamma^{nm}`$,
using the last coefficient column:

```math
\begin{aligned}
\frac i2C_m\bar\psi_n\gamma^{nm}\varphi_W={}&-\frac{i}{16}C_m\bar\psi_n\gamma^{nm}\gamma_{cd}\widehat R_{ab}(Q)\widehat C^{abcd}+2C_m\bar\psi_n\gamma^{nm}\gamma_c\widehat R_{ab}(Q)\mathcal D^aT^{bc}\\
 &+\frac{64i}{3}C_m\bar\psi_n\gamma^{nm}\chi D-4C_m\bar\psi_n\gamma^{nm}\gamma_c\mathcal D^c\widehat R_{ab}(Q)T^{ab}\\
 &-4C_m\bar\psi_n\gamma^{nm}\gamma_a\mathcal D^c\widehat R_{bc}(Q)T^{ab}+\frac{32}{3}C_m\bar\psi_n\gamma^{nm}\gamma^{ab}\gamma^c\chi\mathcal D_aT_{bc}\\
 &+\frac{512i}{9}C_m\bar\psi_n\gamma^{nm}\chi T^2-\frac{64}{3}C_m\bar\psi_n\gamma^{nm}\gamma_a\mathcal D_b\chi T^{ab}\\
 &+\frac{4i}{3}C_m\bar\psi_n\gamma^{nm}\gamma_{ab}\widehat R_{cd}(Q)T^{ab}T^{cd}+\frac{i}{4}C_m\bar\psi_n^i\gamma^{nm}\widehat R^{ab}{}_{ij}(V)\widehat R_{ab}{}^j(Q)\\
 &-\frac{4i}{3}C_m\bar\psi_n^i\gamma^{nm}\widehat R^{ab}{}_{ij}(V)\gamma_{ab}\chi^j
\end{aligned}
\tag{GA11}
```

This accounts for all thirty-three spinor products. No gamma matrix has
been moved past another matrix, and no odd spinor has been interchanged
with another odd spinor. Consequently the only new minus signs in these
three steps are the displayed $`i^2=-1`$ signs. Terms containing $`\chi`$
or $`\widehat R(Q)`$ keep their full definitions AD02 and AD05.

<a id="412-calculate-the-four-triplet-couplings"></a>

### Calculate the four triplet couplings

The three coefficients in GA05 are $`i/4`$, $`256i/3`$, and $`16/3`$.
For the composite Y term the numerical products are

```math
\frac i4\frac i4=-\frac1{16},\qquad
\frac i4\frac{256i}{3}=-\frac{64}{3},\qquad
\frac i4\frac{16}{3}=\frac{4i}{3}.
```

The gauged part has the three additional numerical products

```math
\left(-\frac g{2\sigma}\right)\frac i4=-\frac{ig}{8\sigma},\qquad
\left(-\frac g{2\sigma}\right)\frac{256i}{3}=-\frac{128ig}{3\sigma},\qquad
\left(-\frac g{2\sigma}\right)\frac{16}{3}=-\frac{8g}{3\sigma}.
```

The original three products multiply $`\sigma^{-1}\bar\psi^i\psi^j`$;
the three new ones multiply $`L_c^{ij}`$. Putting all six terms together gives

```math
\begin{aligned}
\left(\frac i{4\sigma}\bar\psi^{(i}\psi^{j)}-\frac g{2\sigma}L_c^{ij}\right)L_{W\,ij}={}&-\frac{1}{16}\sigma^{-1}(\bar\psi^i\psi^j)\big(\overline{\widehat R}_{ab(i}(Q)\widehat R_{j)}{}^{ab}(Q)\big)-\frac{64}{3}\sigma^{-1}(\bar\psi^i\psi^j)\big(\bar\chi_{(i}\chi_{j)}\big)\\
 &+\frac{4i}{3}\sigma^{-1}(\bar\psi^i\psi^j)\big(\widehat R_{ab\,ij}(V)T^{ab}\big)\\
 &-\frac{ig}{8\sigma}L_c^{ij}\overline{\widehat R}_{ab(i}(Q)\widehat R_{j)}{}^{ab}(Q)-\frac{128ig}{3\sigma}L_c^{ij}\bar\chi_{(i}\chi_{j)}-\frac{8g}{3\sigma}L_c^{ij}\widehat R_{ab\,ij}(V)T^{ab}
\end{aligned}
\tag{GA12}
```

For the gravitino–dilatino term, the products are
$`(-1/2)(i/4)=-i/8`$, $`(-1/2)(256i/3)=-128i/3`$, and
$`(-1/2)(16/3)=-8/3`$. Keeping the external spinors in density order gives

```math
\begin{aligned}
-\frac12\bar\psi_m^i\gamma^m\psi^jL_{W\,ij}={}&-\frac{i}{8}(\bar\psi_m^i\gamma^m\psi^j)\big(\overline{\widehat R}_{ab(i}(Q)\widehat R_{j)}{}^{ab}(Q)\big)-\frac{128i}{3}(\bar\psi_m^i\gamma^m\psi^j)\big(\bar\chi_{(i}\chi_{j)}\big)\\
 &-\frac{8}{3}(\bar\psi_m^i\gamma^m\psi^j)\big(\widehat R_{ab\,ij}(V)T^{ab}\big)
\end{aligned}
\tag{GA13}
```

For the two-gravitino term, multiply by $`i\sigma/4`$.
The three numerical products are again $`-1/16,-64/3,4i/3`$;
now the external bilinear is $`\bar\psi_m^i\gamma^{mn}\psi_n^j`$:

```math
\begin{aligned}
\frac{i\sigma}{4}\bar\psi_m^i\gamma^{mn}\psi_n^jL_{W\,ij}={}&-\frac{1}{16}\sigma(\bar\psi_m^i\gamma^{mn}\psi_n^j)\big(\overline{\widehat R}_{ab(i}(Q)\widehat R_{j)}{}^{ab}(Q)\big)-\frac{64}{3}\sigma(\bar\psi_m^i\gamma^{mn}\psi_n^j)\big(\bar\chi_{(i}\chi_{j)}\big)\\
 &+\frac{4i}{3}\sigma(\bar\psi_m^i\gamma^{mn}\psi_n^j)\big(\widehat R_{ab\,ij}(V)T^{ab}\big)
\end{aligned}
\tag{GA14}
```

For the remaining bridge term, multiply by $`C_m/4`$.
Here $`(1/4)(i/4)=i/16`$, $`(1/4)(256i/3)=64i/3`$, and
$`(1/4)(16/3)=4/3`$; there is no extra $`i`$ in its density prefactor:

```math
\begin{aligned}
\frac14C_m\bar\psi_n^i\gamma^{mnp}\psi_p^jL_{W\,ij}={}&\frac{i}{16}C_m(\bar\psi_n^i\gamma^{mnp}\psi_p^j)\big(\overline{\widehat R}_{ab(i}(Q)\widehat R_{j)}{}^{ab}(Q)\big)+\frac{64i}{3}C_m(\bar\psi_n^i\gamma^{mnp}\psi_p^j)\big(\bar\chi_{(i}\chi_{j)}\big)\\
 &+\frac{4}{3}C_m(\bar\psi_n^i\gamma^{mnp}\psi_p^j)\big(\widehat R_{ab\,ij}(V)T^{ab}\big)
\end{aligned}
\tag{GA15}
```

These are all fifteen triplet products, including the three new compensator couplings. In particular the source's
$`16Y_{ij}\widehat R_{ab}{}^{ij}(V)T^{ab}/3`$ becomes the third and sixth terms
of GA12 after the defining-vector identification. Its fermionic value
must be retained even though Eq. (5.18) leaves it written with $`Y_{ij}`$.

<a id="413-display-the-differentiated-products-retained-in-ga08"></a>

### Display the differentiated products retained in GA08

$`\mathcal D`$ is an even derivation. It therefore obeys an ordinary
plus-sign Leibniz rule even when both factors are odd. Metric compatibility
gives $`\mathcal D_bT^2=2T^{cd}\mathcal D_bT_{cd}`$. The six products
inside the first bracket of GA08 expand as follows:

```math
\begin{aligned}
4\mathcal D_b(\widehat C^{ab}{}_{cd}T^{cd})
&=4(\mathcal D_b\widehat C^{ab}{}_{cd})T^{cd}+4\widehat C^{ab}{}_{cd}\mathcal D_bT^{cd},\\
-\frac{64}{3}\mathcal D_b(DT^{ab})
&=-\frac{64}{3}(\mathcal D_bD)T^{ab}-\frac{64}{3}D\mathcal D_bT^{ab},\\
-\frac{128}{9}\mathcal D_b(T^{ab}T_{cd}T^{cd})
&=-\frac{128}{9}(\mathcal D_bT^{ab})T^2-\frac{256}{9}T^{ab}T^{cd}\mathcal D_bT_{cd},\\
-\frac{512}{3}\mathcal D_b(T^a{}_cT^{cd}T^b{}_d)
&=-\frac{512}{3}(\mathcal D_bT^a{}_c)T^{cd}T^b{}_d
-\frac{512}{3}T^a{}_c(\mathcal D_bT^{cd})T^b{}_d
-\frac{512}{3}T^a{}_cT^{cd}\mathcal D_bT^b{}_d,\\
8i\mathcal D_b(\overline{\widehat R(Q)^{ab}}\chi)
&=8i(\mathcal D_b\overline{\widehat R(Q)^{ab}})\chi
+8i\overline{\widehat R(Q)^{ab}}\mathcal D_b\chi,\\
-\frac{64i}{3}\mathcal D_b(\bar\chi\gamma^{ab}\chi)
&=-\frac{64i}{3}(\mathcal D_b\bar\chi)\gamma^{ab}\chi
-\frac{64i}{3}\bar\chi\gamma^{ab}\mathcal D_b\chi
=-\frac{128i}{3}\bar\chi\gamma^{ab}\mathcal D_b\chi.
\end{aligned}\tag{GA16}
```

Only in the last equality did we exchange odd spinors: the bivector
flip from C04 gives $`(\mathcal D_b\bar\chi)\gamma^{ab}\chi =+\bar\chi\gamma^{ab}\mathcal D_b\chi`$. Thus the two terms add.
For the epsilon-current bracket, the two product rules give four terms:

```math
\begin{aligned}
-32\varepsilon^a{}_{bcde}\mathcal D^b\!\left[
\frac23T^{cf}\mathcal D_fT^{de}+T^c{}_f\mathcal D^dT^{ef}\right]
={}&-\frac{64}{3}\varepsilon^a{}_{bcde}(\mathcal D^bT^{cf})\mathcal D_fT^{de}
-\frac{64}{3}\varepsilon^a{}_{bcde}T^{cf}\mathcal D^b\mathcal D_fT^{de}\\
&-32\varepsilon^a{}_{bcde}(\mathcal D^bT^c{}_f)\mathcal D^dT^{ef}
-32\varepsilon^a{}_{bcde}T^c{}_f\mathcal D^b\mathcal D^dT^{ef}.
\end{aligned}\tag{GA17}
```

Multiplying GA16 and GA17 by $`C_a`$ supplies every differentiated term
of GA08. The other eight terms of GA08 are already displayed separately.
The final expression retains the equivalent product-derivative form,
so that the current and its original derivative order remain readable.

<a id="5-consistency-checks"></a>

## Consistency Checks

<a id="51-full-composite-and-defining-vector-checks"></a>

### Full-composite and defining-vector checks

GC04–GC06 display the Q consistency of the deformed constraints and the
Q/S defining-vector Y law. GC07–GC11 solve the spinor/scalar constraints
without a cubic/quartic truncation. Substituting GC08 in GC01 makes
$`\Gamma^i+g\varphi_c^i`$ vanish term by term, because each of its six
positive terms is cancelled by $`-8\sigma^2\chi^i`$.

For example, its gauged terms cancel as

```math
-\frac g{2\sigma}L_c^{ij}\psi_j
-8\sigma^2\left(-\frac g{16\sigma^3}L_c^{ij}\psi_j
+\frac g{8\sigma^2}\varphi_c^i\right)+g\varphi_c^i
=0.
\tag{GC25}
```

For the scalar constraint, the three Y² terms are cancelled by the
three corresponding terms of $`-4\sigma^2D`$:

```math
\begin{aligned}
&-\frac1{16\sigma^2}(\bar\psi^i\psi^j)(\bar\psi_i\psi_j)
-\frac{ig}{4\sigma^2}L_{c\,ij}\bar\psi^i\psi^j
+\frac{g^2}{4\sigma^2}L_c^{ij}L_{c\,ij}\\
&\quad-4\sigma^2\left[-\frac1{64\sigma^4}(\bar\psi^i\psi^j)(\bar\psi_i\psi_j)
-\frac{ig}{16\sigma^4}L_{c\,ij}\bar\psi^i\psi^j
+\frac{g^2}{16\sigma^4}L_c^{ij}L_{c\,ij}\right]=0,\\
&gN_c-4\sigma^2\left(\frac g{4\sigma^2}N_c\right)=0.
\end{aligned}\tag{GC26}
```

Every remaining term of $`\mathcal C`$ is cancelled by the matching GC09
coefficient times $`-4\sigma^2`$. This is an algebraic check of the displayed
solution, separate from the source-based transformation argument GC04–GC05.

<a id="52-ungauged-limit-and-comparison-to-our-earlier-work"></a>

### Ungauged limit and comparison of component densities

Set g to zero before imposing any gauge. The following terms disappear:

```math
\begin{gathered}
Y^{ij}:\ -\frac g{2\sigma}L_c^{ij},\qquad
\widehat H:\ \frac g2E_c,\qquad
\mathcal D_\mu\psi^i:\ -\frac g{2\sigma}L_c^{ij}\psi_{\mu j},\\
\chi^i:\ -\frac g{16\sigma^3}L_c^{ij}\psi_j
+\frac g{8\sigma^2}\varphi_c^i,\qquad
D:\ \frac g{4\sigma^2}N_c-\frac{ig}{16\sigma^4}L_{c\,ij}\bar\psi^i\psi^j
+\frac{g^2}{16\sigma^4}L_c^{ij}L_{c\,ij}.
\end{gathered}\tag{GC27}
```

The remaining formulas are exactly V03/H01/W04/D01–D02. Since GC18–GC22
are the same full definitions evaluated in these composites, their g=0
values agree with those definitions. The three gauging terms of GA12 vanish and
every other coefficient and ordered tensor body is that of WA07–WA15.
Thus the **same local density**, without an integration by parts, obeys

```math
\left.e^{-1}\mathcal L_{\sigma C^2,g}^{\rm map}\right|_{g=0}
=e^{-1}\mathcal L_{\sigma C^2}^{\rm map}\quad\text{of WA24}.
\tag{GC28}
```

For the gauge evaluation in this subsection, restrict to $`\sigma=1`$, $`b_\mu=0`$, $`\psi^i=0`$.
Do not set $`\mathcal D_\mu\psi^i`$ to zero. GC14–GC16 give

```math
\begin{aligned}
\left.\mathcal D_\mu\psi^i\right|&=
\frac14\gamma\!\cdot\!\widehat G\psi_\mu^i
-\gamma\!\cdot\!T\psi_\mu^i-\phi_\mu^i
-\frac g2L_c^{ij}\psi_{\mu j},\\
\left.\chi^i\right|&=\frac i8\gamma^\mu
\left(\frac14\gamma\!\cdot\!\widehat G\psi_\mu^i
-\gamma\!\cdot\!T\psi_\mu^i-\phi_\mu^i
-\frac g2L_c^{ij}\psi_{\mu j}\right)+\frac g8\varphi_c^i,\\
\left.D\right|&=\frac12f_a{}^a-\frac i8\bar\psi_a\mathcal D^a\psi
-\frac12\bar\psi_a\gamma^a\chi
-\frac1{16}\widehat G_{ab}\widehat G^{ab}
-\frac{26}{3}T_{ab}T^{ab}+2\widehat G_{ab}T^{ab}
+\frac g4N_c+\frac{g^2}{16}L_c^{ij}L_{c\,ij}.
\end{aligned}\tag{GC29}
```

These are the full covariant derivative, chi and D entries. On setting
$`L_c^{ij}=\delta^{ij}L_c/\sqrt2`$, its explicit chi gauging term is
$`-igL_c\delta^{ij}\gamma^\mu\psi_{\mu j}/(16\sqrt2) +g\varphi_c^i/8`$, with the SU(2) lowering order specified above.
The formulas here retain the full hats and dependent connections; the
action GA24 itself has not been gauge fixed.

<a id="53-a-nonzero-g³g⁴-check"></a>

### A nonzero g³/g⁴ check

To test the higher powers, evaluate the polynomial on flat constant
bosonic test fields with $`\sigma=s\ne0`$, $`G=H=0`$, $`V=0`$, $`T=0`$ and
all fermions zero. Choose $`E_{c\,\mu\nu\rho}=0`$ and constant $`L_c,N_c`$.
This is an algebraic test configuration, not an asserted vacuum or a use
of field equations. Then the only nonzero Weyl-map contribution to the
density is $`64sD^2/3`$, with

```math
D=\frac g{4s^2}N_c+\frac{g^2}{16s^4}L_c^{ij}L_{c\,ij}.
\tag{GC30}
```

Multiply the two terms before collecting:

```math
\begin{aligned}
\frac{64s}{3}D^2
&=\frac{64s}{3}\left[
\frac{g^2}{16s^4}N_c^2
+2\frac{g^3}{64s^6}N_cL_c^{ij}L_{c\,ij}
+\frac{g^4}{256s^8}(L_c^{ij}L_{c\,ij})^2\right]\\
&=\frac{4g^2}{3s^3}N_c^2
+\frac{2g^3}{3s^5}N_cL_c^{ij}L_{c\,ij}
+\frac{g^4}{12s^7}(L_c^{ij}L_{c\,ij})^2.
\end{aligned}\tag{GC31}
```

The g³ and g⁴ terms are therefore present in GA24 even though they are
packaged inside its fully defined D². None has been dropped as a small-g
approximation. At g=0 this entire test configuration has zero density.

<a id="54-dimensions-parity-indices-boundaries-and-checks-not-performed"></a>

### Dimensions, parity, indices and boundary conventions

The weights are $`w(\sigma,T,C_a)=1`$, $`w(\psi,\chi,R(Q))=3/2`$,
$`w(\psi_a)=1/2`$, $`w(D,C_{abcd},R(V),Y)=2`$, $`w(L_c)=3`$,
$`w(\varphi_c)=7/2`$, $`w(E_c^a,N_c)=4`$, and $`w(g)=0`$.
For the new composite terms, explicitly,

```math
\begin{aligned}
w(\sigma^{-1}gL_c)&=-1+3=2,&
w(g\sigma^{-3}L_c\psi)&=-3+3+\frac32=\frac32,\\
w(g\sigma^{-2}\varphi_c)&=-2+\frac72=\frac32,&
w(g\sigma^{-2}N_c)&=-2+4=2,\\
w(g\sigma^{-4}L_c\bar\psi\psi)&=-4+3+3=2,&
w(g^2\sigma^{-4}L_c^{ij}L_{c\,ij})&=-4+6=2.
\end{aligned}\tag{GC32}
```

Each new density term has weight $`-1+3+3=5`$, the same as every term
of the old density; $`w(e)=-5`$. These are the conformal dimensions before
fixing the compensating scale. The three new density contractions pair
the symmetric upper $`ij`$ of $`L_c`$ with the symmetric lower pair of the
curvature or chi bilinear, or with $`R(V)_{ij}`$. They are Lorentz scalars
and Grassmann even. GC10 explicitly checks that raising/lowering both
triplet indices introduces no extra sign. Five dimensions imposes no
Weyl chirality projection.

The product rules in GA16–GA17 preserve derivative order, and no local
density is changed by a boundary term. GC13 verifies the ordinary gauged
form symmetry. The source superconformal transformation argument verifies
the defining-vector identification subject to the displayed constraints.
The algebraic checks below concern coefficient collection, source-map
transcription, the gauged composites and the displayed form symmetry.

<a id="55-reproducible-independent-algebraic-checks"></a>

### Reproducible independent algebraic checks

The cited output (standalone file unavailable) is
[component check commands and output scope](../../../computations/weyl_fermionic/README.md).
It checks the exact new rational coefficients, the unchanged source-map
coefficients and tensor bodies, collection of all nine contributions,
the same-representative g=0 limit, and GC31. A four-generator Grassmann
calculation tests the full Y² expression, the spinor/scalar constraint
solutions and the new compensator contraction with nonzero quartic terms.
The source reports that all exact checks passed; six independent Grassmann samples gave maximum
relative residual $`3.26\times10^{-16}`$ (rounded upward), with nonzero
quartic coefficients in Y² and D. The checker tests those algebraic
statements, not nonlinear closure.

<a id="6-final-result"></a>

## Final Result

All nine evaluated density contributions GA07–GA15 add to the following
single expression. **T, chi, D, the curvatures and every derivative in
this formula are the gauged objects GC03–GC24.** They have explicit
full definitions above; neither their bosonic restrictions nor the old
truncated gauged composites are used. The Weyl linear components, Y and
P have all been eliminated from the displayed density.

```math
\fbox{$\displaystyle{\begin{aligned}
e^{-1}\mathcal L_{\sigma C^2,g}^{\rm map}={}&\frac{1}{8}\sigma \widehat C_{abcd}\widehat C^{abcd}+\frac{64}{3}\sigma D^2+\frac{1024}{9}\sigma DT_{ab}T^{ab}-\frac{16}{3}\sigma \widehat C_{abcd}T^{ab}T^{cd}\\
 &-\frac{1}{3}\sigma \widehat R_{ab}{}^{ij}(V)\widehat R^{ab}{}_{ij}(V)-\frac{64}{3}\sigma (\mathcal D_aT_{bc})(\mathcal D^aT^{bc})+\frac{64}{3}\sigma (\mathcal D_bT_{ac})(\mathcal D^aT^{bc})-\frac{128}{3}\sigma T_{ab}\mathcal D^b\mathcal D_cT^{ac}\\
 &-\frac{128}{3}\sigma \varepsilon_{abcde}T^{ab}T^{cd}\mathcal D_fT^{ef}+1024\sigma T_{ab}T^{bc}T_{cd}T^{da}-\frac{2816}{27}\sigma (T_{ab}T^{ab})^2+\frac{3}{4}\sigma \overline{\widehat R_{ab}(Q)}\gamma^c\mathcal D_c\widehat R^{ab}(Q)\\
 &-2i\sigma T^{ab}\overline{\widehat R_{ca}(Q)}\widehat R^c{}_{b}(Q)-\frac{160i}{3}\sigma T^{ab}\overline{\widehat R_{ab}(Q)}\chi-\frac{256}{3}\sigma \bar\chi\gamma^a\mathcal D_a\chi+\frac{1}{16}C_a\varepsilon^{abcde}\widehat C_{bcfg}\widehat C_{de}{}^{fg}\\
 &-\frac{1}{12}C_a\varepsilon^{abcde}\widehat R(V)_{bc}{}^{ij}\widehat R(V)_{de\,ij}+C_a\mathcal D_b\Big[4\widehat C^{ab}{}_{cd}T^{cd}-\frac{64}{3}DT^{ab}-\frac{128}{9}T^{ab}T_{cd}T^{cd}-\frac{512}{3}T^a{}_cT^{cd}T^b{}_d+8i\overline{\widehat R(Q)^{ab}}\chi-\frac{64i}{3}\bar\chi\gamma^{ab}\chi\Big]\\
 &-32C_a\varepsilon^a{}_{bcde}\mathcal D^b\Big[\frac23T^{cf}\mathcal D_fT^{de}+T^c{}_f\mathcal D^dT^{ef}\Big]-C_aT^{cd}\overline{\widehat R(Q)_{ec}}\gamma^a\widehat R(Q)^e{}_d+3C_aT_c{}^d\overline{\widehat R(Q)_e{}^a}\gamma^c\widehat R(Q)^e{}_d+16C_aT^c{}_d\overline{\widehat R(Q)^a{}_c}\gamma^d\chi\\
 &+\frac{16}{3}C_aT^{cd}\overline{\widehat R(Q)_{cd}}\gamma^a\chi+\frac{i}{2}C_a\overline{\widehat R(Q)_{cd}}\mathcal D^a\widehat R(Q)^{cd}+\frac{3i}{2}C_a\overline{\widehat R(Q)_{cd}}\mathcal D^c\widehat R(Q)^{da}-\frac{i}{8}\bar\psi\gamma_{cd}\widehat R_{ab}(Q)\widehat C^{abcd}\\
 &+4\bar\psi\gamma_c\widehat R_{ab}(Q)\mathcal D^aT^{bc}+\frac{128i}{3}\bar\psi\chi D-8\bar\psi\gamma_c\mathcal D^c\widehat R_{ab}(Q)T^{ab}-8\bar\psi\gamma_a\mathcal D^c\widehat R_{bc}(Q)T^{ab}\\
 &+\frac{64}{3}\bar\psi\gamma^{ab}\gamma^c\chi\mathcal D_aT_{bc}+\frac{1024i}{9}\bar\psi\chi T^2-\frac{128}{3}\bar\psi\gamma_a\mathcal D_b\chi T^{ab}+\frac{8i}{3}\bar\psi\gamma_{ab}\widehat R_{cd}(Q)T^{ab}T^{cd}\\
 &+\frac{i}{2}\bar\psi^i\widehat R^{ab}{}_{ij}(V)\widehat R_{ab}{}^j(Q)-\frac{8i}{3}\bar\psi^i\widehat R^{ab}{}_{ij}(V)\gamma_{ab}\chi^j-\frac{1}{16}\sigma\bar\psi_m\gamma^m\gamma_{cd}\widehat R_{ab}(Q)\widehat C^{abcd}-2i\sigma\bar\psi_m\gamma^m\gamma_c\widehat R_{ab}(Q)\mathcal D^aT^{bc}\\
 &+\frac{64}{3}\sigma\bar\psi_m\gamma^m\chi D+4i\sigma\bar\psi_m\gamma^m\gamma_c\mathcal D^c\widehat R_{ab}(Q)T^{ab}+4i\sigma\bar\psi_m\gamma^m\gamma_a\mathcal D^c\widehat R_{bc}(Q)T^{ab}-\frac{32i}{3}\sigma\bar\psi_m\gamma^m\gamma^{ab}\gamma^c\chi\mathcal D_aT_{bc}\\
 &+\frac{512}{9}\sigma\bar\psi_m\gamma^m\chi T^2+\frac{64i}{3}\sigma\bar\psi_m\gamma^m\gamma_a\mathcal D_b\chi T^{ab}+\frac{4}{3}\sigma\bar\psi_m\gamma^m\gamma_{ab}\widehat R_{cd}(Q)T^{ab}T^{cd}+\frac{1}{4}\sigma\bar\psi_m^i\gamma^m\widehat R^{ab}{}_{ij}(V)\widehat R_{ab}{}^j(Q)\\
 &-\frac{4}{3}\sigma\bar\psi_m^i\gamma^m\widehat R^{ab}{}_{ij}(V)\gamma_{ab}\chi^j-\frac{i}{16}C_m\bar\psi_n\gamma^{nm}\gamma_{cd}\widehat R_{ab}(Q)\widehat C^{abcd}+2C_m\bar\psi_n\gamma^{nm}\gamma_c\widehat R_{ab}(Q)\mathcal D^aT^{bc}+\frac{64i}{3}C_m\bar\psi_n\gamma^{nm}\chi D\\
 &-4C_m\bar\psi_n\gamma^{nm}\gamma_c\mathcal D^c\widehat R_{ab}(Q)T^{ab}-4C_m\bar\psi_n\gamma^{nm}\gamma_a\mathcal D^c\widehat R_{bc}(Q)T^{ab}+\frac{32}{3}C_m\bar\psi_n\gamma^{nm}\gamma^{ab}\gamma^c\chi\mathcal D_aT_{bc}+\frac{512i}{9}C_m\bar\psi_n\gamma^{nm}\chi T^2\\
 &-\frac{64}{3}C_m\bar\psi_n\gamma^{nm}\gamma_a\mathcal D_b\chi T^{ab}+\frac{4i}{3}C_m\bar\psi_n\gamma^{nm}\gamma_{ab}\widehat R_{cd}(Q)T^{ab}T^{cd}+\frac{i}{4}C_m\bar\psi_n^i\gamma^{nm}\widehat R^{ab}{}_{ij}(V)\widehat R_{ab}{}^j(Q)-\frac{4i}{3}C_m\bar\psi_n^i\gamma^{nm}\widehat R^{ab}{}_{ij}(V)\gamma_{ab}\chi^j\\
 &-\frac{1}{16}\sigma^{-1}(\bar\psi^i\psi^j)\big(\overline{\widehat R}_{ab(i}(Q)\widehat R_{j)}{}^{ab}(Q)\big)-\frac{64}{3}\sigma^{-1}(\bar\psi^i\psi^j)\big(\bar\chi_{(i}\chi_{j)}\big)+\frac{4i}{3}\sigma^{-1}(\bar\psi^i\psi^j)\big(\widehat R_{ab\,ij}(V)T^{ab}\big)-\frac{i}{8}g\sigma^{-1}L_c^{ij}\overline{\widehat R}_{ab(i}(Q)\widehat R_{j)}{}^{ab}(Q)\\
 &-\frac{128i}{3}g\sigma^{-1}L_c^{ij}\bar\chi_{(i}\chi_{j)}-\frac{8}{3}g\sigma^{-1}L_c^{ij}\widehat R_{ab\,ij}(V)T^{ab}-\frac{i}{8}(\bar\psi_m^i\gamma^m\psi^j)\big(\overline{\widehat R}_{ab(i}(Q)\widehat R_{j)}{}^{ab}(Q)\big)-\frac{128i}{3}(\bar\psi_m^i\gamma^m\psi^j)\big(\bar\chi_{(i}\chi_{j)}\big)\\
 &-\frac{8}{3}(\bar\psi_m^i\gamma^m\psi^j)\big(\widehat R_{ab\,ij}(V)T^{ab}\big)-\frac{1}{16}\sigma(\bar\psi_m^i\gamma^{mn}\psi_n^j)\big(\overline{\widehat R}_{ab(i}(Q)\widehat R_{j)}{}^{ab}(Q)\big)-\frac{64}{3}\sigma(\bar\psi_m^i\gamma^{mn}\psi_n^j)\big(\bar\chi_{(i}\chi_{j)}\big)+\frac{4i}{3}\sigma(\bar\psi_m^i\gamma^{mn}\psi_n^j)\big(\widehat R_{ab\,ij}(V)T^{ab}\big)\\
 &+\frac{i}{16}C_m(\bar\psi_n^i\gamma^{mnp}\psi_p^j)\big(\overline{\widehat R}_{ab(i}(Q)\widehat R_{j)}{}^{ab}(Q)\big)+\frac{64i}{3}C_m(\bar\psi_n^i\gamma^{mnp}\psi_p^j)\big(\bar\chi_{(i}\chi_{j)}\big)+\frac{4}{3}C_m(\bar\psi_n^i\gamma^{mnp}\psi_p^j)\big(\widehat R_{ab\,ij}(V)T^{ab}\big)
\end{aligned}}$}
\tag{GA24}
```

The action is

```math
S_{\rm Weyl^2,g}^{\rm map}
=\int d^5x\,e\left(e^{-1}\mathcal L_{\sigma C^2,g}^{\rm map}\right).
\tag{GA25}
```

The result contains 73 grouped outer terms, or 87 contributions after
the displayed product rules and the chi bivector flip. This counts terms
in this representation, not independent operators or primitive DW-field
monomials. The complete gauging is encoded by the three new explicit
compensator couplings together with GC03–GC24 throughout the formula.
The g³/g⁴ example GC31 shows why retaining those definitions matters.

<a id="7-convention-dependence-and-remaining-uncertainties"></a>

## Convention Dependence and Scope

The result is an exact **full-covariant map insertion**, under A1–A6, with no physical-fermion or coupling expansion. Its source normalization is the Özkan–Pang $`\sigma\widehat C^2/8`$ normalization; no conversion to another total-action convention is claimed. The gauged extension changes the realization of the fields, not the coefficients of FM01–FM04.

The full chi and D formulas were recovered using the improved-vector
constraint multiplet, GC01–GC05, including the cubic and quartic terms.
GA24 is the density obtained by inserting the specified Weyl composite
map, with the source normalization and assumptions A1–A6 retained.

The exact supercovariant presentation retains the fermion content of the
defined covariants and the ordered derivatives used in the density.

Source trail: local Coomans–Özkan (2.15)–(2.17), (5.2)–(5.8); local Weyl-multiplet paper (5.10)–(5.14), printed p.27/PDF p.28; local Özkan–Pang GB (3.1), (5.8), (5.16)–(5.18); companion OPall(3.1)–(3.2) for P/E; master C/G/W/R/L/V/A and the derived map FM01–FM04. The earlier gauged calculation's source conventions and gauge-slice formulas were consulted; its explicitly truncated action was not used as a full-fermion input.
