# Total gauged two-derivative plus R² action: orders zero, one and two

Date: 2026-09-15. Lock: `TOTAL-R2-FLUXLESS-GENERAL-S0S1S2-v2`.

**Action version.** Both starting densities are the stated component fermionic constructions. The two-derivative action is `2DER-GDW-P-PSI0-OZKAN1608-QUADRATIC-FERMION-v2`; the R-square action uses its canonical BF source version. Gold's bosonic action is a comparison reference and is not an input to this expansion.

## 1. Problem and Target

Calculate precisely the three coefficients

```math
S(\epsilon)=S^{(0)}+\epsilon S^{(1)}+\epsilon^2S^{(2)}+O(\epsilon^3),\qquad
S^{(n)}=\int d^5x\,\bar e\,\ell^{(n)},
\tag{1.1}
```

for the total action

```math
S=\int d^5x\,e\left(\ell_{2\partial}+\lambda\ell_{R^2}\right),
\qquad \lambda\equiv\lambda_{R^2}.
\tag{1.2}
```

The total action is expanded about a fluxless maximally symmetric background with **general $`L_0,N_0,k`$**. The coefficients in (1.1) do not contain an extra $`1/n!`$. No background equation is imposed. In particular $`S^{(1)}`$ is retained, not assumed to vanish. This note stops at the action coefficients; it derives no fluctuation equations, masses, constraints, eigenmodes or spectrum.

### 1.1 Source anchors and representation

Our two-derivative file's superscript “Gold” labels its established normalization; the action itself is our calculated full fermionic density. The R² coefficient ledger is the already verified equivalent representation of our note-11 action in terms of its component maps. Reusing that ledger does not replace our action by a literature action. The inherited source qualifications, operational Majorana convention and project curvature repair are retained.

### 1.2 Assumptions and permitted operations

1. $`L_0>0`$ and $`L_0,N_0,k`$ are spacetime constants. All fields are expanded in a formal dimensionless even parameter $`\epsilon`$.
2. The inherited conformal gauge is $`\sigma=1`$, $`b_\mu=0`$, $`\psi^i_{\rm defining}=0`$, $`L_{ij}=L\delta_{ij}/\sqrt2`$. The original gravitino $`\psi_\mu^i`$ and linear fermion $`\varphi^i`$ remain.
3. Work locally in a fluxless patch with vanishing background potentials and $`SU(2)`$ connection. No Wilson-line background is added.
4. The connection is the dependent supergravity connection. Its fermion contorsion is included. No independent Palatini fluctuation is introduced.
5. No auxiliary field is eliminated and no fluctuation gauge is imposed. The vector $`E_a`$ remains the constrained descendant of the independent three-form.
6. The source is known through two physical fermions. Terms with four or more fermions start at $`\epsilon^4`$ on this zero-fermion background, so they cannot affect (1.1). Omitted mixed cubic terms start at $`\epsilon^3`$.
7. Starting from our actions, only the displayed bosonic potential-strength and scalar-kinetic integrations by parts are used. Retain the two-derivative $`-2\Box L`$ and the gauged triplet's $`g^2L\Box L/2`$ contribution. No extra boundary adjustment is made to adopt Gold's bosonic representative. For integrated equalities between representatives take compactly supported fluctuations or retain the stated surface integrals.

## 2. Convention Ledger

<!-- ASSERT_CONVENTION: natural_units=hbar=c=1; metric_signature=(-++++); curvature=R2-GOLD12-OFFSHELL-v1; coupling=lambda_R2_mass_dimension_minus_2; position_space_no_Fourier_transform -->

Spacetime and tangent indices run over $`0,\ldots,4`$; $`i,j=1,2`$. All indices in expansion coefficients are raised with the background metric or frame metric. The curvature conventions are

```math
R^\rho{}_{\sigma\mu\nu}
=2\partial_{[\mu}\Gamma^\rho_{\nu]\sigma}
+2\Gamma^\rho_{[\mu|\lambda|}\Gamma^\lambda_{\nu]\sigma},\qquad
R_{\mu\nu}=R^\rho{}_{\mu\rho\nu},
\tag{2.1}
```

```math
\bar R_{\mu\nu\rho\sigma}
=k(\bar g_{\mu\rho}\bar g_{\nu\sigma}-\bar g_{\mu\sigma}\bar g_{\nu\rho}),\qquad
\bar R_{\mu\nu}=4k\bar g_{\mu\nu},\qquad \bar R=20k.
\tag{2.2}
```

Brackets and parentheses have unit weight. In an oriented frame, $`\varepsilon^{01234}=+1`$, $`\varepsilon_{01234}=-1`$. Gamma matrices obey

```math
\{\gamma_a,\gamma_b\}=2\eta_{ab},\qquad
\gamma^{a_1\cdots a_p}=\gamma^{[a_1}\cdots\gamma^{a_p]},\qquad
\gamma^{abcde}=i\varepsilon^{abcde}.
\tag{2.3}
```

The spinors are odd symplectic Majorana fields. The operational source bar is $`\bar\xi=\xi^TC`$ and preserves scalar $`i`$ in the displayed algebra. $`C^T=-C`$ and $`\gamma_a^TC=C\gamma_a`$. Thus

```math
\overline{c\gamma^{a_1\cdots a_p}\xi}
=c(-1)^{p(p-1)/2}\bar\xi\gamma^{a_1\cdots a_p},\qquad
\overline{M_1M_2\xi}=\bar\xi\,\widetilde M_2\widetilde M_1.
\tag{2.4}
```

The fixed-index bilinear flip signs are $`t_0=t_1=+1`$, $`t_2=t_3=-1`$; an invariant $`SU(2)`$ contraction contributes the additional NW–SE sign. The calculation below preserves fermion order, so no unrecorded spinor flip or Fierz identity is used. No fermionic functional derivatives are taken.

```math
X^i=\varepsilon^{ij}X_j,\qquad X_i=X^j\varepsilon_{ji},\qquad
\varepsilon^{12}=\varepsilon_{12}=1,\qquad
L_{ij}=\frac L{\sqrt2}\delta_{ij}.
\tag{2.5}
```

In particular the alignment tensor with two equal-variance indices is different from an invariant mixed Kronecker delta. An identity used explicitly in the final displays is

```math
L_i{}^jX_j
=\frac{L_0}{\sqrt2}\delta_{ir}\varepsilon^{js} \delta_s{}^r X^t\varepsilon_{tj}
=-\frac{L_0}{\sqrt2}\delta_{it}X^t.
\tag{2.6}
```

Engineering dimensions on this fixed compensator slice are

```math
[L]=[h_{\mu\nu}]=[C_\mu]=[B_{\mu\nu}]=[E_{\mu\nu\rho}]=0,\quad
[N]=[g]=[G]=[H]=[E_a]=[V_a^{ij}]=1,\quad
[\psi_\mu]=[\varphi]=\tfrac12,\quad [k]=2,\quad [\lambda]=-2.
\tag{2.7}
```

Both terms in (1.2) therefore have engineering dimension two; any common gravitational normalization is the one already implicit in the source actions.

## 3. Definitions and Required Identities

### 3.1 Background and independent fluctuations

Use the linear path in independent fields

```math
\begin{aligned}
g_{\mu\nu}(\epsilon)&=\bar g_{\mu\nu}+\epsilon h_{\mu\nu},&
L(\epsilon)&=L_0+\epsilon\delta L,&N(\epsilon)&=N_0+\epsilon\delta N,\\
C_\mu(\epsilon)&=\epsilon C_\mu,&B_{\mu\nu}(\epsilon)&=\epsilon B_{\mu\nu},&
E_{\mu\nu\rho}(\epsilon)&=\epsilon E_{\mu\nu\rho},\\
V_\mu(\epsilon)&=\epsilon V_\mu,&V'_\mu{}^{ij}(\epsilon)&=\epsilon V'_\mu{}^{ij},&
\psi_\mu^i(\epsilon)&=\epsilon\psi_\mu^i,\quad
\varphi^i(\epsilon)=\epsilon\varphi^i.
\end{aligned}
\tag{3.1}
```

On the right, zero-background field names denote their first-order amplitudes, not new multiplets. There are no independent second-order field amplitudes in this Taylor path. The trace/traceless split is $`V_\mu^{ij}=V'_\mu{}^{ij}+\delta^{ij}V_\mu/2`$, with $`\delta_{ij}V'_\mu{}^{ij}=0`$.

The symbol $`\bar{\mathcal D}`$ denotes the induced derivative with the **background** Lorentz, world and $`SU(2)`$ connections. For example

```math
\bar{\mathcal D}_\mu\psi_\nu^i
=\partial_\mu\psi_\nu^i-\bar\Gamma^\rho_{\mu\nu}\psi_\rho^i
+\tfrac14\bar\omega_\mu{}^{ab}\gamma_{ab}\psi_\nu^i,
\qquad
\bar\Box=\bar g^{\mu\nu}\bar{\mathcal D}_\mu\bar{\mathcal D}_\nu.
\tag{3.2}
```

The nonlinear action still uses the full supercovariant $`\mathcal D`$. Equation (3.2) is only its background connection part. Its nonzero first- and second-order $`Q,S,K`$ completions are inserted explicitly in Section 4.5. In particular neither $`\mathcal D\psi^{\rm defining}`$ nor a conformal box on a constant compensator is set to zero.

At first order the ordinary strengths and constrained vector are

```math
\begin{aligned}
G_{\mu\nu}&=2\bar{\mathcal D}_{[\mu}C_{\nu]},\\
H_{\mu\nu\rho}&=3\bar{\mathcal D}_{[\mu}B_{\nu\rho]}+\frac g2E_{\mu\nu\rho},\\
H^{ab}&=-\frac1{12}\varepsilon^{abcde}H_{cde},\\
E^a&=-\frac1{12}\varepsilon^{abcde}\bar{\mathcal D}_bE_{cde}.
\end{aligned}
\tag{3.3}
```

Every strength in the quadratic bosonic endpoint means (3.3). These are not independent replacements for $`C,B,E_3`$. The divergence of $`E^a`$ vanishes: in differential-form language its dual is proportional to $`dE_3`$, and $`d^2E_3=0`$.

### 3.2 Metric, frame, measure and Hodge star

Multiply the inverse-metric series into $`g_{\mu\nu}(\epsilon)`$:

```math
g^{\mu\nu}=\bar g^{\mu\nu}-\epsilon h^{\mu\nu}
+\epsilon^2h^\mu{}_\rho h^{\rho\nu}+O(\epsilon^3),\qquad
(1+\epsilon h)(1-\epsilon h+\epsilon^2h^2)=1+O(\epsilon^3).
\tag{3.4}
```

Here the last equality is a matrix identity. With $`h=\bar g^{\mu\nu}h_{\mu\nu}`$,

```math
\begin{aligned}
\log(e/\bar e)&=\tfrac12\mathop{\mathrm{tr}}\nolimits\log(1+\epsilon\bar g^{-1}h)
=\tfrac\epsilon2h-\tfrac{\epsilon^2}4h_{\mu\nu}h^{\mu\nu}+O(\epsilon^3),\\
\frac e{\bar e}&=1+\frac\epsilon2h
+\epsilon^2\left(\frac18h^2-\frac14h_{\mu\nu}h^{\mu\nu}\right)+O(\epsilon^3).
\end{aligned}
\tag{3.5}
```

The square of the first-order logarithm supplies the $`h^2/8`$ term. A symmetric frame parametrization is

```math
e_\mu{}^a=\bar e_\nu{}^a\left(\delta^\nu_\mu+\frac\epsilon2h_\mu{}^\nu
-\frac{\epsilon^2}8h_\mu{}^\rho h_\rho{}^\nu\right)+O(\epsilon^3),
\quad
e_a{}^\mu=\left(\delta^\mu_\nu-\frac\epsilon2h^\mu{}_\nu
+\frac{3\epsilon^2}8h^\mu{}_\rho h^\rho{}_\nu\right)\bar e_a{}^\nu+O(\epsilon^3).
\tag{3.6}
```

This parametrizes the Lorentz frame; it is not a transverse or trace condition on $`h_{\mu\nu}`$. The ordinary linear spin connection follows by varying the torsion-free frame postulate:

```math
\delta\omega_\mu{}^{ab}
=\frac12\bar e^{a\nu}\bar e^{b\rho}
\left(\bar{\mathcal D}_\rho h_{\mu\nu}-\bar{\mathcal D}_\nu h_{\mu\rho}\right).
\tag{3.7}
```

Its insertion between two first-order fermions has order three. The bilinear contorsion instead enters the background-coefficient curvature terms already at order two; it is retained in (4.34).

For a lower $`p`$-form $`X_p`$ the Hodge variation follows from the measure and the $`p`$ inverse metrics in its definition:

```math
\delta(*X)=*\left(\delta X+\tfrac h2X
-\sum_{r=1}^{p}h^{\nu}{}_{\mu_r}
X_{\mu_1\cdots\mu_{r-1}\nu\mu_{r+1}\cdots\mu_p}\right).
\tag{3.8}
```

Since each background form is zero, a metric variation of a first-order strength has order two and its product with another first-order strength has order three. Thus the **background** Hodge star suffices in every quadratic strength term. This argument does not discard the linear $`gE_3/2`$ in $`H_3`$.

### 3.3 Connection and curvature coefficients

Insert (3.4) into the metric-compatible connection difference:

```math
\begin{aligned}
\Gamma^{(1)\rho}_{\mu\nu}
&=\tfrac12\left(\bar{\mathcal D}_\mu h^\rho{}_\nu
+\bar{\mathcal D}_\nu h^\rho{}_\mu-\bar{\mathcal D}^\rho h_{\mu\nu}\right),\\
\Gamma^{(2)\rho}_{\mu\nu}
&=-\tfrac12 h^{\rho\lambda}
\left(\bar{\mathcal D}_\mu h_{\lambda\nu}
+\bar{\mathcal D}_\nu h_{\lambda\mu}-\bar{\mathcal D}_\lambda h_{\mu\nu}\right).
\end{aligned}
\tag{3.9}
```

The connection difference is a tensor. Expanding (2.1) without commuting any derivatives gives

```math
\begin{aligned}
R^{(1)}_{\mu\nu}&=\bar{\mathcal D}_\rho\Gamma^{(1)\rho}_{\mu\nu}
-\bar{\mathcal D}_\nu\Gamma^{(1)\rho}_{\mu\rho},\\
R^{(2)}_{\mu\nu}&=\bar{\mathcal D}_\rho\Gamma^{(2)\rho}_{\mu\nu}
-\bar{\mathcal D}_\nu\Gamma^{(2)\rho}_{\mu\rho}
+\Gamma^{(1)\rho}_{\rho\lambda}\Gamma^{(1)\lambda}_{\mu\nu}
-\Gamma^{(1)\rho}_{\nu\lambda}\Gamma^{(1)\lambda}_{\mu\rho},\\
R^{(1)}&=\bar{\mathcal D}_\mu\bar{\mathcal D}_\nu h^{\mu\nu}-\bar\Box h-4kh,\\
R^{(2)}&=\bar g^{\mu\nu}R^{(2)}_{\mu\nu}
-h^{\mu\nu}R^{(1)}_{\mu\nu}+4k h_{\mu\nu}h^{\mu\nu}.
\end{aligned}
\tag{3.10}
```

The last $`4k h_{\mu\nu}h^{\mu\nu}`$ is the second inverse-metric term contracted with $`\bar R_{\mu\nu}`$. Equations (3.9)–(3.10) are the explicit definitions of $`R^{(1)},R^{(2)}`$ used in the endpoint; they are geometric expansion coefficients, not additional fields.

For the ordinary scalar box,

```math
\Box L=\epsilon\bar\Box\delta L+\epsilon^2\left[
-h^{\mu\nu}\bar{\mathcal D}_\mu\bar{\mathcal D}_\nu\delta L
-\left(\bar{\mathcal D}_\mu h^{\mu\nu}-\tfrac12\bar{\mathcal D}^\nu h\right)
\bar{\mathcal D}_\nu\delta L\right]+O(\epsilon^3).
\tag{3.11}
```

This follows by varying the inverse metric and the trace of $`\Gamma^{(1)}`$. It is not a replacement for a full conformal box; the latter's additional terms are treated below.

## 4. Detailed Derivation

<!-- ASSERT_CONVENTION: natural_units=hbar=c=1; metric_signature=(-++++); curvature=R2-GOLD12-OFFSHELL-v1; coupling=lambda_R2_mass_dimension_minus_2; position_space_no_Fourier_transform -->

### 4.1 Start with our two full fermionic actions

Our earlier two-derivative calculation, Eqs. (4.47), (5.1) and (5.10), gives the following full density at the retained fermion order. The primed slots here are the same earlier composite vector used in this R² project; they are shorthand only in this starting expression and are inserted below:

```math
\begin{aligned}
\ell_{2\partial}\doteq-2\Bigl\{&L^{ij}(Y'_{ij}-g^2L_{ij})
+i\bar\lambda'^i\varphi_i-\tfrac12L_{ij}\bar\psi_a^i\gamma^a\lambda'^j
+\tfrac12(F'_{ab}+2gG_{ab})E^{ab}\\
&+(\rho'+2g)\left(N+\tfrac12\bar\psi_a^i\gamma^a\varphi_i
+\tfrac i4L_{ij}\bar\psi_a^i\gamma^{ab}\psi_b^j\right)\Bigr\}.
\end{aligned}
\tag{OS.1}
```

The $`-g^2L_{ij}`$ and $`+2g`$ are our already calculated effective-slot shifts, not new choices. In particular $`2gY_{ij}^{\rm defining}=2g(-gL_{ij}/2)=-g^2L_{ij}`$. The full definitions of $`Y',\lambda',\rho',F'`$ are exactly the earlier computed ones. The bosonic restriction of (OS.1) is consequently

```math
\ell_{2\partial,\rm B}
=-2L^{ij}Y'_{ij}+2g^2L^2
-(F'_{ab}+2gG_{ab})E^{ab}-2N\rho'-4gN.
\tag{OS.2}
```

No bosonic formula from Gold has been inserted in this equation. The spinor terms vanish because the elementary fermions have been set to zero for this restriction, not because their supercovariant derivatives were prematurely set to zero in the full action.

For R², use our note-11 action and its previously derived 42-group representation in our Step-4 Eq. (47), with the component definitions already inserted and checked in note 10. The **complete list** of its bosonic source contributions is:

| Our source group | Bosonic contribution |
|---|---|
| 1 | $`Y'^{ij}Y'_{ij}`$ |
| 2 | $`-g\rho'Y'^{ij}L_{ij}`$ |
| 11 | $`-A'_a(\partial_b\rho')G^{ab}/2`$ |
| 12 | $`-A'_a\rho'\mathcal D_b^{\rm B}G^{ab}/2`$ |
| 13 | $`-A'_a\mathcal D_b^{\rm B}F'^{ab}/2`$ |
| 14 | $`8A'_a(\partial_b\rho')T^{ab}`$ |
| 15 | $`8A'_a\rho'\mathcal D_b^{\rm B}T^{ab}`$ |
| 16 | $`-\varepsilon^{abcde}A'_aF'_{bc}G_{de}/8`$ |
| 26 | $`\rho'\Box_c\rho'/2`$ |
| 27 | $`(\rho')^2f_a{}^a`$ |
| 28 | $`-\rho'F'_{ab}G^{ab}/4`$ |
| 29 | $`4(\rho')^2G_{ab}T^{ab}`$ |
| 30 | $`4\rho'F'_{ab}T^{ab}`$ |
| 31 | $`-4(\rho')^2D`$ |
| 32 | $`-104(\rho')^2T^{ab}T_{ab}/3`$ |

All other groups contain odd slots and vanish in this bosonic restriction. They remain in the full action and are expanded individually in Section 4.6. Thus this table and that fermion ledger cover our entire retained action.

Use the component definitions already established in our note 10, Eqs. (8), (18), (20), B5–B7, B20–B27. In the bosonic restriction they read

```math
\begin{aligned}
\rho'&=2N/L,&A'_a&=2E_a/L+\sqrt2 V_a,\\
T_{ab}&=G_{ab}/8-H_{ab}/4,&f_a{}^a&=-R/16,\\
D&=\tfrac12f_a{}^a-\tfrac1{16}G^2-\tfrac{26}{3}T^2+2GT
+\tfrac14gN+\tfrac1{16}g^2L^2,\\
\Box_c\rho'&=\Box\rho'+2f_a{}^a\rho',&
\Box_cL_{ij}&=(\mathcal D^{\rm B})^2L_{ij}+6f_a{}^aL_{ij}.
\end{aligned}
\tag{OS.3}
```

Here $`\mathcal D^{\rm B}`$ is the bosonic restriction of the source derivative, including the triplet's $`SU(2)`$ connection. The two conformal-box connection terms in (OS.3) remain even on constant scalars. Our primed triplet is

```math
\begin{aligned}
Y'^{ij}={}&L^{-1}(\mathcal D^{\rm B})^2L^{ij}
+\frac{L^{ij}}L\left(6f_a{}^a+\frac83T^2+4D\right)
-L^{-3}(N^2+E^2)L^{ij}\\
&-2L^{-3}E^aL^{k(i}\mathcal D_a^{\rm B}L_k{}^{j)}
-L^{-3}L_{kl}\mathcal D_a^{\rm B}L^{k(i}\mathcal D^{{\rm B}a}L^{j)l}.
\end{aligned}
\tag{OS.4}
```

We now do the coefficient algebra directly. First square and contract our $`T`$:

```math
T^2=\frac{G^2}{64}-\frac{GH}{16}+\frac{H^2}{16},\quad
GT=\frac{G^2}{8}-\frac{GH}{4},\quad
F'T=\frac{F'G}{8}-\frac{F'H}{4}.
\tag{OS.5}
```

Substituting (OS.3) in the triplet background combination gives

```math
\begin{aligned}
6f+\frac83T^2+4D
&=8f-\frac14G^2-32T^2+8GT+gN+\frac14g^2L^2\\
&=-\frac R2+\left(-\frac14-\frac12+1\right)G^2
+(2-2)GH-2H^2+gN+\frac14g^2L^2\\
&=-\frac R2+\frac14G^2-2H^2+gN+\frac14g^2L^2.
\end{aligned}
\tag{OS.6}
```

Thus the actual primed triplet, with its gauging terms intact, is

```math
\begin{aligned}
Y'^{ij}={}&L^{-1}(\mathcal D^{\rm B})^2L^{ij}
+\frac{L^{ij}}L\left(-\frac R2+\frac14G^2-2H^2+gN+\frac14g^2L^2\right)\\
&+L^{-3}\left[-(N^2+E^2)L^{ij}
-2E^aL^{k(i}\mathcal D_a^{\rm B}L_k{}^{j)}
-L_{kl}\mathcal D_a^{\rm B}L^{k(i}\mathcal D^{{\rm B}a}L^{j)l}\right].
\end{aligned}
\tag{4.3}
```

For source groups 11–15, combine the two product derivatives before integrating by parts:

```math
\begin{aligned}
11+12+13+14+15
&=-\tfrac12A'_a\mathcal D_b^{\rm B}\left[F'^{ab}+\rho'(G^{ab}-16T^{ab})\right]\\
&\doteq-\tfrac14(F')^2-\tfrac14\rho'F'G+4\rho'F'T.
\end{aligned}
\tag{OS.7}
```

Adding groups 28 and 30 changes the last two coefficients to $`-\rho'F'G/2+8\rho'F'T`$. The current in this operation is displayed in Section 4.8. For groups 26 and 27 insert the first box in (OS.3):

```math
\begin{aligned}
\tfrac12\rho'\Box_c\rho'+(\rho')^2f
&=\tfrac12\rho'\Box\rho'+2(\rho')^2f\\
&\doteq-\tfrac12(\partial\rho')^2+2(\rho')^2f
=-2\left[\partial(N/L)\right]^2+2(\rho')^2f.
\end{aligned}
\tag{OS.8}
```

All remaining tensor and scalar background slots combine as

```math
\begin{aligned}
2f+4GT-4D-\frac{104}{3}T^2
&=\frac14G^2-4GT-gN-\frac14g^2L^2\\
&=-\frac14G^2+GH-gN-\frac14g^2L^2,\\
-\tfrac12\rho'F'G+8\rho'F'T
&=\left(-\tfrac12+1\right)\rho'F'G-2\rho'F'H
=\frac NL GF'-\frac{4N}{L}HF'.
\end{aligned}
\tag{OS.9}
```

In the first line the $`2f`$, $`T^2`$ and $`D`$ coefficients cancel as $`2f-2f=0`$ and $`104/3-104/3=0`$; the $`GT`$ coefficient is $`4-8=-4`$. Multiplication by $`(\rho')^2=4N^2/L^2`$ gives each of the last four terms below. Therefore the bosonic density **derived from our R² action** is

```math
\begin{aligned}
\ell_{R^2,\rm B}\doteq{}&Y'^{ij}Y'_{ij}-2g\frac NL Y'^{ij}L_{ij}
-2\left[\partial(N/L)\right]^2-\tfrac14F'^{ab}F'_{ab}
+\frac NL G^{ab}F'_{ab}-\frac{4N}{L}H^{ab}F'_{ab}\\
&-\frac{N^2}{L^2}G^{ab}G_{ab}+4\frac{N^2}{L^2}H^{ab}G_{ab}
-4g\frac{N^3}{L^2}-g^2N^2
-\tfrac18\varepsilon^{abcde}A'_aF'_{bc}G_{de}.
\end{aligned}
\tag{4.2}
```

Equations (OS.2)–(OS.9) derive this expression without using a Gold action or a Gold bold composite. The surviving $`Y'`$ and $`F'`$ here are inserted in Sections 4.2–4.4. The Chern–Simons term starts at cubic fluctuation order and does not enter the displayed coefficients.

The same triplet insertion in our two-derivative expression (OS.2), using the aligned trace derived immediately below, gives

```math
\begin{aligned}
-2L^{ij}Y'_{ij}={}&LR+\frac{2N^2}{L}-2gLN-\tfrac12g^2L^3
-2\Box L+\frac{(\partial L)^2}{L}
+2LV'_a{}^{ij}V'{}^a_{ij}+4LH^2-\tfrac12LG^2+\frac{2E^2}{L},\\
-(F'_{ab}+2gG_{ab})E^{ab}
&\doteq-2E^a\left(\frac{2E_a}{L}+\sqrt2V_a+2gC_a\right).
\end{aligned}
\tag{OS.10}
```

Adding $`2g^2L^2-2N\rho'-4gN`$ from (OS.2), the coefficients of $`N^2/L`$ and $`E^2/L`$ are respectively $`2-4=-2`$ and $`2-4=-2`$. This yields

```math
\begin{aligned}
\ell_{2\partial,\rm B}\doteq{}&L\left(R-\tfrac12G^2+4H^2+2V'_a{}^{ij}V'{}^a_{ij}\right)
-2\Box L+L^{-1}(\partial L)^2\\
&-2L^{-1}E^2-2\sqrt2E^aV_a-2L^{-1}N^2-4gE^aC_a
-2gLN-4gN-\tfrac12g^2L^3+2g^2L^2.
\end{aligned}
\tag{4.1}
```

The $`-2\Box L`$ has deliberately been kept as it emerges from our full-component density. Its first- and second-order contributions are retained below.

### 4.2 Covariant compensator derivatives and the triplet square

For the proof only, write $`\alpha_{ij}=\delta_{ij}/\sqrt2`$, a fixed numerical orientation with $`\alpha_{ij}\alpha^{ij}=1`$, and write $`W_{aij}=(\mathcal D_a^{\rm B}\alpha)_{ij}`$. Neither symbol is a new physical field. They are removed in the final coefficients. Differentiating $`L_{ij}=L\alpha_{ij}`$ gives

```math
\mathcal D_a^{\rm B}L_{ij}=\alpha_{ij}\partial_aL+LW_{aij},\qquad
\alpha^{ij}W_{aij}=\tfrac12\mathcal D_a^{\rm B}(\alpha^{ij}\alpha_{ij})=0.
\tag{4.4}
```

Let $`J=\left(\begin{smallmatrix}0&1\\-1&0\end{smallmatrix}\right)`$ and use a symmetric traceless connection matrix $`V'=\left(\begin{smallmatrix}p&q\\q&-p\end{smallmatrix}\right)`$ at a fixed tangent index. Direct matrix multiplication gives

```math
W=\frac{JV'-V'J}{\sqrt2}
=\sqrt2\begin{pmatrix}q&-p\\-p&-q\end{pmatrix},\qquad
V'^{ij}V'_{ij}=-2(p^2+q^2),\qquad
W^{ij}W_{ij}=-4(p^2+q^2).
\tag{4.5}
```

These identities are polynomial identities in the source $`SU(2)`$ convention; they impose no extra reality condition on $`p,q`$. Therefore

```math
\begin{aligned}
(\mathcal D^{\rm B}L^{ij})(\mathcal D^{\rm B}L_{ij})
&=(\partial L)^2+2L^2V'_a{}^{ij}V'{}^a_{ij},\\
\alpha^{ij}(\mathcal D^{\rm B})^2L_{ij}
&=\Box L-LW_a{}^{ij}W^a_{ij}
=\Box L-2LV'_a{}^{ij}V'{}^a_{ij}.
\end{aligned}
\tag{4.6}
```

For the second line differentiate $`\alpha^{ij}\mathcal D_a^{\rm B}L_{ij}=\partial_aL`$ once more and subtract $`(\mathcal D^a\alpha^{ij})(\mathcal D_aL_{ij})`$.

The two contractions of our nonlinear triplet map, already derived in our note 10 Eq. (C11) and obtained by contracting its symmetric indices, are

```math
\begin{aligned}
L_{ij}L^{k(i}\mathcal D_a^{\rm B}L_k{}^{j)}&=0,\\
L_{ij}L_{kl}\mathcal D_a^{\rm B}L^{k(i}\mathcal D^{{\rm B}a}L^{j)l}
&=L^2(\partial L)^2-\tfrac12L^2(\mathcal D^{\rm B}L^{ij})(\mathcal D^{\rm B}L_{ij}).
\end{aligned}
\tag{4.7}
```

The first zero is the symmetric triplet contracted with its infinitesimal $`SU(2)`$ rotation, not a choice $`\mathcal DL=0`$. Divide the second line by $`L^4`$ and insert (4.6). The trace of (4.3) is then

```math
\begin{aligned}
\alpha_{ij}Y'^{ij}
={}&-\frac R2-\frac{N^2}{L^2}+\frac{\Box L}{L}
-\frac{(\partial L)^2}{2L^2}
-V'_a{}^{ij}V'{}^a_{ij}-2H^{ab}H_{ab}+\frac14G^{ab}G_{ab}-\frac{E^aE_a}{L^2}
+gN+\frac14g^2L^2.
\end{aligned}
\tag{4.8}
```

The $`V'^2`$ coefficient is $`-2+1=-1`$: the first contribution is the box in (4.6), and the second is the last contraction of (4.7). At first order the orthogonal triplet is $`\bar{\mathcal D}^aW_a^{ij}`$, so

```math
Y'^{ij}Y'_{ij}
=(\alpha_{ij}Y'^{ij})^2
+2\epsilon^2(\bar{\mathcal D}^aV'_a{}^{ij})(\bar{\mathcal D}^bV'_{b,ij})+O(\epsilon^3).
\tag{4.9}
```

The cross term is zero because $`\alpha_{ij}\bar{\mathcal D}^aW_a^{ij}=0`$ at first order. In (4.9) apply the matrix identity (4.5) with $`V'`$ replaced by its background divergence. This explains both the algebraic connection term and its derivative term.

The scalar derivative terms now come directly from the first two terms of our (4.2). Their coefficient is twice the constant-in-derivatives part of $`\alpha Y'-gN`$, namely $`-R/2-N^2/L^2+g^2L^2/4`$. Multiply this coefficient separately by $`\Box L/L`$ and $`-(\partial L)^2/(2L^2)`$ in (4.8), and add the square of $`\Box L/L`$. Through quadratic fluctuation order this gives

```math
\begin{aligned}
\left[Y'^2-2gN\alpha Y'\right]_{\text{scalar derivatives}}
={}&\left(-\frac RL-\frac{2N^2}{L^3}+\frac{g^2L}{2}\right)\Box L\\
&+\left(\frac R{2L^2}+\frac{N^2}{L^4}-\frac{g^2}{4}\right)(\partial L)^2
+\frac{(\Box L)^2}{L^2}+O(\epsilon^3).
\end{aligned}
\tag{4.10}
```

### 4.3 Scalar expansion: every coefficient before collection

First restrict our source slots to constant $`R,L,N`$ with zero flux. Equation (OS.3) gives $`\rho'=2N/L`$, $`f=-R/16`$, $`D=-R/32+gN/4+g^2L^2/16`$, and $`\alpha Y'=-R/2-N^2/L^2+gN+g^2L^2/4`$. Thus our source products give

```math
\begin{aligned}
F_{2\partial}
&=-2\left[L\left(-\frac R2-\frac{N^2}{L^2}+gN+\frac14g^2L^2-g^2L\right)
+\left(\frac{2N}{L}+2g\right)N\right],\\
F_{R^2}
&=\left(-\frac R2-\frac{N^2}{L^2}+gN+\frac14g^2L^2\right)^2
-2gN\left(-\frac R2-\frac{N^2}{L^2}+gN+\frac14g^2L^2\right)\\
&\quad+\frac{4N^2}{L^2}\left[2\left(-\frac R{16}\right)
-4\left(-\frac R{32}+\frac{gN}{4}+\frac{g^2L^2}{16}\right)\right].
\end{aligned}
\tag{OS.11}
```

In the last line $`-R/8+R/8=0`$, leaving $`-4gN^3/L^2-g^2N^2`$. Expanding the two squares and collecting gives the following polynomial $`F=F_{2\partial}+\lambda F_{R^2}`$. Set $`R_0=20k`$ only after this own-action substitution:

```math
\begin{aligned}
F(R,L,N)={}&LR-\frac{2N^2}{L}-2gLN-4gN-\frac12g^2L^3+2g^2L^2\\
&+\lambda\left[\frac{R^2}{4}+\frac{RN^2}{L^2}+\frac{N^4}{L^4}
-\frac14g^2RL^2-\frac52g^2N^2-\frac{4gN^3}{L^2}+\frac1{16}g^4L^4\right].
\end{aligned}
\tag{4.11}
```

$`F`$ is only the displayed polynomial used to organize Taylor algebra; it is not a field and is fully inserted in the endpoint. The inverse-power rule and the products needed here are

```math
\begin{aligned}
L^{-m}&=L_0^{-m}-\epsilon mL_0^{-m-1}\delta L
+\epsilon^2\tfrac{m(m+1)}2L_0^{-m-2}(\delta L)^2+O(\epsilon^3),\\
N^p&=N_0^p+\epsilon pN_0^{p-1}\delta N
+\epsilon^2\tfrac{p(p-1)}2N_0^{p-2}(\delta N)^2+O(\epsilon^3),\\
R^2&=400k^2+40\epsilon kR^{(1)}
+\epsilon^2\left[(R^{(1)})^2+40kR^{(2)}\right]+O(\epsilon^3),\\
\frac NL&=\frac{N_0}{L_0}+\epsilon\left(\frac{\delta N}{L_0}-\frac{N_0\delta L}{L_0^2}\right)
+\epsilon^2\left(\frac{N_0(\delta L)^2}{L_0^3}-\frac{\delta N\delta L}{L_0^2}\right)+O(\epsilon^3).
\end{aligned}
\tag{4.12}
```

For a source monomial $`aR^qN^pL^m`$, with integer $`m`$ possibly negative, its coefficients are explicitly

```math
\begin{aligned}
[aR^qN^pL^m]^{(0)}={}&aR_0^qN_0^pL_0^m,\\
[aR^qN^pL^m]^{(1)}={}&a qR_0^{q-1}N_0^pL_0^mR^{(1)}
+a pR_0^qN_0^{p-1}L_0^m\delta N+a mR_0^qN_0^pL_0^{m-1}\delta L,\\
[aR^qN^pL^m]^{(2)}={}&a qR_0^{q-1}N_0^pL_0^mR^{(2)}
+\frac{a q(q-1)}2R_0^{q-2}N_0^pL_0^m(R^{(1)})^2\\
&+a qpR_0^{q-1}N_0^{p-1}L_0^mR^{(1)}\delta N
+a qmR_0^{q-1}N_0^pL_0^{m-1}R^{(1)}\delta L\\
&+\frac{a p(p-1)}2R_0^qN_0^{p-2}L_0^m(\delta N)^2
+a pmR_0^qN_0^{p-1}L_0^{m-1}\delta N\delta L\\
&+\frac{a m(m-1)}2R_0^qN_0^pL_0^{m-2}(\delta L)^2.
\end{aligned}
\tag{4.13}
```

A term with zero integer prefactor is zero, including when its displayed power of $`R_0`$ or $`N_0`$ would otherwise be negative. Thus (4.13) is a polynomial rule valid also at $`k=0`$ or $`N_0=0`$; no division by either is made. The following table applies this rule to **each** source monomial. Entries are its zeroth, first and second Taylor coefficients, before the volume factor.

```math
\begin{aligned}
q_{1}&=\frac{L^{4} g^{4} \lambda}{16}\\
q_{1}^{(0)}&=\frac{L_0^{4} g^{4} \lambda}{16}\\
q_{1}^{(1)}&=\frac{L_0^{3} \left(\delta L\right) g^{4} \lambda}{4}\\
q_{1}^{(2)}&=\frac{3 L_0^{2} \left(\delta L\right)^{2} g^{4} \lambda}{8}
\end{aligned}
\tag{SM.1}
```

```math
\begin{aligned}
q_{2}&=- \frac{L^{3} g^{2}}{2}\\
q_{2}^{(0)}&=- \frac{L_0^{3} g^{2}}{2}\\
q_{2}^{(1)}&=- \frac{3 L_0^{2} \left(\delta L\right) g^{2}}{2}\\
q_{2}^{(2)}&=- \frac{3 L_0 \left(\delta L\right)^{2} g^{2}}{2}
\end{aligned}
\tag{SM.2}
```

```math
\begin{aligned}
q_{3}&=- \frac{L^{2} R g^{2} \lambda}{4}\\
q_{3}^{(0)}&=- 5 L_0^{2} g^{2} k \lambda\\
q_{3}^{(1)}&=\lambda \left(- \frac{L_0^{2} g^{2} \left(R^{(1)}\right)}{4} - 10 L_0 \left(\delta L\right) g^{2} k\right)\\
q_{3}^{(2)}&=\lambda \left(- \frac{L_0^{2} g^{2} \left(R^{(2)}\right)}{4} - \frac{L_0 \left(\delta L\right) g^{2} \left(R^{(1)}\right)}{2} - 5 \left(\delta L\right)^{2} g^{2} k\right)
\end{aligned}
\tag{SM.3}
```

```math
\begin{aligned}
q_{4}&=2 L^{2} g^{2}\\
q_{4}^{(0)}&=2 L_0^{2} g^{2}\\
q_{4}^{(1)}&=4 L_0 \left(\delta L\right) g^{2}\\
q_{4}^{(2)}&=2 \left(\delta L\right)^{2} g^{2}
\end{aligned}
\tag{SM.4}
```

```math
\begin{aligned}
q_{5}&=- 2 L N g\\
q_{5}^{(0)}&=- 2 L_0 N_0 g\\
q_{5}^{(1)}&=- 2 L_0 \left(\delta N\right) g - 2 N_0 \left(\delta L\right) g\\
q_{5}^{(2)}&=- 2 \left(\delta L\right) \left(\delta N\right) g
\end{aligned}
\tag{SM.5}
```

```math
\begin{aligned}
q_{6}&=L R\\
q_{6}^{(0)}&=20 L_0 k\\
q_{6}^{(1)}&=L_0 \left(R^{(1)}\right) + 20 \left(\delta L\right) k\\
q_{6}^{(2)}&=L_0 \left(R^{(2)}\right) + \left(\delta L\right) \left(R^{(1)}\right)
\end{aligned}
\tag{SM.6}
```

```math
\begin{aligned}
q_{7}&=- \frac{5 N^{2} g^{2} \lambda}{2}\\
q_{7}^{(0)}&=- \frac{5 N_0^{2} g^{2} \lambda}{2}\\
q_{7}^{(1)}&=- 5 N_0 \left(\delta N\right) g^{2} \lambda\\
q_{7}^{(2)}&=- \frac{5 \left(\delta N\right)^{2} g^{2} \lambda}{2}
\end{aligned}
\tag{SM.7}
```

```math
\begin{aligned}
q_{8}&=- 4 N g\\
q_{8}^{(0)}&=- 4 N_0 g\\
q_{8}^{(1)}&=- 4 \left(\delta N\right) g\\
q_{8}^{(2)}&=0
\end{aligned}
\tag{SM.8}
```

```math
\begin{aligned}
q_{9}&=\frac{R^{2} \lambda}{4}\\
q_{9}^{(0)}&=100 k^{2} \lambda\\
q_{9}^{(1)}&=10 k \lambda \left(R^{(1)}\right)\\
q_{9}^{(2)}&=\lambda \left(10 k \left(R^{(2)}\right) + \frac{\left(R^{(1)}\right)^{2}}{4}\right)
\end{aligned}
\tag{SM.9}
```

```math
\begin{aligned}
q_{10}&=- \frac{2 N^{2}}{L}\\
q_{10}^{(0)}&=- \frac{2 N_0^{2}}{L_0}\\
q_{10}^{(1)}&=- \frac{4 N_0 \left(\delta N\right)}{L_0} + \frac{2 N_0^{2} \left(\delta L\right)}{L_0^{2}}\\
q_{10}^{(2)}&=- \frac{2 \left(\delta N\right)^{2}}{L_0} + \frac{4 N_0 \left(\delta L\right) \left(\delta N\right)}{L_0^{2}} - \frac{2 N_0^{2} \left(\delta L\right)^{2}}{L_0^{3}}
\end{aligned}
\tag{SM.10}
```

```math
\begin{aligned}
q_{11}&=- \frac{4 N^{3} g \lambda}{L^{2}}\\
q_{11}^{(0)}&=- \frac{4 N_0^{3} g \lambda}{L_0^{2}}\\
q_{11}^{(1)}&=\lambda \left(- \frac{12 N_0^{2} \left(\delta N\right) g}{L_0^{2}} + \frac{8 N_0^{3} \left(\delta L\right) g}{L_0^{3}}\right)\\
q_{11}^{(2)}&=\lambda \left(- \frac{12 N_0 \left(\delta N\right)^{2} g}{L_0^{2}} + \frac{24 N_0^{2} \left(\delta L\right) \left(\delta N\right) g}{L_0^{3}} - \frac{12 N_0^{3} \left(\delta L\right)^{2} g}{L_0^{4}}\right)
\end{aligned}
\tag{SM.11}
```

```math
\begin{aligned}
q_{12}&=\frac{N^{2} R \lambda}{L^{2}}\\
q_{12}^{(0)}&=\frac{20 N_0^{2} k \lambda}{L_0^{2}}\\
q_{12}^{(1)}&=\lambda \left(\frac{N_0^{2} \left(R^{(1)}\right)}{L_0^{2}} + \frac{40 N_0 \left(\delta N\right) k}{L_0^{2}} - \frac{40 N_0^{2} \left(\delta L\right) k}{L_0^{3}}\right)\\
q_{12}^{(2)}&=\lambda \left(\frac{N_0^{2} \left(R^{(2)}\right)}{L_0^{2}} + \frac{2 N_0 \left(\delta N\right) \left(R^{(1)}\right)}{L_0^{2}} + \frac{20 \left(\delta N\right)^{2} k}{L_0^{2}} - \frac{2 N_0^{2} \left(\delta L\right) \left(R^{(1)}\right)}{L_0^{3}} - \frac{80 N_0 \left(\delta L\right) \left(\delta N\right) k}{L_0^{3}} + \frac{60 N_0^{2} \left(\delta L\right)^{2} k}{L_0^{4}}\right)
\end{aligned}
\tag{SM.12}
```

```math
\begin{aligned}
q_{13}&=\frac{N^{4} \lambda}{L^{4}}\\
q_{13}^{(0)}&=\frac{N_0^{4} \lambda}{L_0^{4}}\\
q_{13}^{(1)}&=\lambda \left(\frac{4 N_0^{3} \left(\delta N\right)}{L_0^{4}} - \frac{4 N_0^{4} \left(\delta L\right)}{L_0^{5}}\right)\\
q_{13}^{(2)}&=\lambda \left(\frac{6 N_0^{2} \left(\delta N\right)^{2}}{L_0^{4}} - \frac{16 N_0^{3} \left(\delta L\right) \left(\delta N\right)}{L_0^{5}} + \frac{10 N_0^{4} \left(\delta L\right)^{2}}{L_0^{6}}\right)
\end{aligned}
\tag{SM.13}
```

Adding the columns gives $`F_0`$, $`F_RR^{(1)}+F_L\delta L+F_N\delta N`$ and

```math
F_RR^{(2)}+\tfrac12F_{RR}(R^{(1)})^2+F_{RL}R^{(1)}\delta L+F_{RN}R^{(1)}\delta N
+\tfrac12F_{LL}(\delta L)^2+F_{LN}\delta L\delta N+\tfrac12F_{NN}(\delta N)^2.
\tag{4.14}
```

All $`F`$ derivatives in (4.14) mean derivatives of (4.11), evaluated at $`R=20k,L=L_0,N=N_0`$. Their explicit sums are:

```math
F_{0}=- \frac{L_0^{3} g^{2}}{2} + 2 L_0^{2} g^{2} - 2 L_0 N_0 g + 20 L_0 k - 4 N_0 g + \lambda \left(\frac{L_0^{4} g^{4}}{16} - 5 L_0^{2} g^{2} k - \frac{5 N_0^{2} g^{2}}{2} + 100 k^{2} - \frac{4 N_0^{3} g}{L_0^{2}} + \frac{20 N_0^{2} k}{L_0^{2}} + \frac{N_0^{4}}{L_0^{4}}\right) - \frac{2 N_0^{2}}{L_0}
\tag{FC.0}
```

```math
F_{R}=L_0 + \lambda \left(- \frac{L_0^{2} g^{2}}{4} + 10 k + \frac{N_0^{2}}{L_0^{2}}\right)
\tag{FC.R}
```

```math
F_{L}=- \frac{3 L_0^{2} g^{2}}{2} + 4 L_0 g^{2} - 2 N_0 g + 20 k + \lambda \left(\frac{L_0^{3} g^{4}}{4} - 10 L_0 g^{2} k + \frac{8 N_0^{3} g}{L_0^{3}} - \frac{40 N_0^{2} k}{L_0^{3}} - \frac{4 N_0^{4}}{L_0^{5}}\right) + \frac{2 N_0^{2}}{L_0^{2}}
\tag{FC.L}
```

```math
F_{N}=- 2 L_0 g - 4 g + \lambda \left(- 5 N_0 g^{2} - \frac{12 N_0^{2} g}{L_0^{2}} + \frac{40 N_0 k}{L_0^{2}} + \frac{4 N_0^{3}}{L_0^{4}}\right) - \frac{4 N_0}{L_0}
\tag{FC.N}
```

```math
F_{RR}=\frac{\lambda}{2}
\tag{FC.RR}
```

```math
F_{RL}=\lambda \left(- \frac{L_0 g^{2}}{2} - \frac{2 N_0^{2}}{L_0^{3}}\right) + 1
\tag{FC.RL}
```

```math
F_{RN}=\frac{2 N_0 \lambda}{L_0^{2}}
\tag{FC.RN}
```

```math
F_{LL}=- 3 L_0 g^{2} + 4 g^{2} + \lambda \left(\frac{3 L_0^{2} g^{4}}{4} - 10 g^{2} k - \frac{24 N_0^{3} g}{L_0^{4}} + \frac{120 N_0^{2} k}{L_0^{4}} + \frac{20 N_0^{4}}{L_0^{6}}\right) - \frac{4 N_0^{2}}{L_0^{3}}
\tag{FC.LL}
```

```math
F_{LN}=- 2 g + \lambda \left(\frac{24 N_0^{2} g}{L_0^{3}} - \frac{80 N_0 k}{L_0^{3}} - \frac{16 N_0^{3}}{L_0^{5}}\right) + \frac{4 N_0}{L_0^{2}}
\tag{FC.LN}
```

```math
F_{NN}=\lambda \left(- 5 g^{2} - \frac{24 N_0 g}{L_0^{2}} + \frac{40 k}{L_0^{2}} + \frac{12 N_0^{2}}{L_0^{4}}\right) - \frac{4}{L_0}
\tag{FC.NN}
```

Combining the $`-2\Box L`$ in our two-derivative density (4.1) with the mixed-triplet derivative terms (4.10) gives

```math
\left[-2+\lambda\left(-\frac RL-\frac{2N^2}{L^3}+\frac{g^2L}{2}\right)\right]\Box L
\equiv b(R,L,N)\Box L.
\tag{4.15}
```

Expand its coefficient:

```math
\begin{aligned}
b_0&=-2+\lambda\left(-\frac{20k}{L_0}-\frac{2N_0^2}{L_0^3}+\frac{g^2L_0}{2}\right),\\
b_1&=\lambda\left[-\frac{R^{(1)}}{L_0}
+\left(\frac{20k}{L_0^2}+\frac{6N_0^2}{L_0^4}+\frac{g^2}{2}\right)\delta L
-\frac{4N_0}{L_0^3}\delta N\right],\\
[e b\Box L/\bar e]^{(1)}&=b_0\bar\Box\delta L,\\
[e b\Box L/\bar e]^{(2)}&=b_1\bar\Box\delta L
-b_0h^{\mu\nu}\bar{\mathcal D}_\mu\bar{\mathcal D}_\nu\delta L
-b_0\left(\bar{\mathcal D}_\mu h^{\mu\nu}-\tfrac12\bar{\mathcal D}^\nu h\right)\bar{\mathcal D}_\nu\delta L
+\tfrac h2b_0\bar\Box\delta L.
\end{aligned}
\tag{4.16}
```

The three $`b_0`$ terms in the last line can be checked against the product rule:

```math
b_0\bar{\mathcal D}_\mu\left[\left(\tfrac h2\bar g^{\mu\nu}-h^{\mu\nu}\right)
\bar{\mathcal D}_\nu\delta L\right].
\tag{4.17}
```

They are retained in the local endpoint. The remaining scalar-gradient square is obtained from (4.12), with all products distributed:

```math
\begin{aligned}
-2\lambda[\partial(N/L)]^2\big|_{\epsilon^2}
={}&-\frac{2\lambda}{L_0^2}(\bar{\mathcal D}\delta N)^2
+\frac{4\lambda N_0}{L_0^3}\bar{\mathcal D}_a\delta N\bar{\mathcal D}^a\delta L
-\frac{2\lambda N_0^2}{L_0^4}(\bar{\mathcal D}\delta L)^2.
\end{aligned}
\tag{4.18}
```

The other gradient contributions are $`L_0^{-1}(\bar{\mathcal D}\delta L)^2`$ from our (4.1) and $`\lambda[(10k+N_0^2/L_0^2)/L_0^2-g^2/4](\bar{\mathcal D}\delta L)^2`$ from the explicitly multiplied triplet terms (4.10). Consequently their sum, including (4.18), is

```math
\begin{aligned}
&\left[\frac1{L_0}+\lambda\left(\frac{10k}{L_0^2}-\frac{N_0^2}{L_0^4}-\frac{g^2}{4}\right)\right](\bar{\mathcal D}\delta L)^2
-\frac{2\lambda}{L_0^2}(\bar{\mathcal D}\delta N)^2
+\frac{4\lambda N_0}{L_0^3}\bar{\mathcal D}_a\delta N\bar{\mathcal D}^a\delta L
+\frac{\lambda}{L_0^2}(\bar\Box\delta L)^2.
\end{aligned}
\tag{4.19}
```

The final term comes from $`(\Box L/L)^2`$ in (4.8).

### 4.4 Forms and connections: source ledger and strength insertion

The local potential and strength at first order are

```math
A'_a{}^{(1)}=\frac2{L_0}E_a+\sqrt2 V_a,\qquad
F'_{ab}{}^{(1)}=\frac4{L_0}\bar{\mathcal D}_{[a}E_{b]}+2\sqrt2\bar{\mathcal D}_{[a}V_{b]}.
\tag{4.20}
```

The nonlinear $`\mathcal DL\wedge\mathcal DL`$ orientation term in the parent map has order two and $`F'^{(0)}=0`$. It therefore cannot affect a quadratic product of strengths. The previously recorded orientation-sign comparison with Gold (12b) does not change any coefficient here.

The entire coefficient addition, before substituting (4.20), is

| Quadratic contraction | Our two-derivative source | Our mixed triplet block $`Y'^2-2gN\alpha Y'`$ | Other terms of our R² action | Total R² coefficient |
|---|---:|---:|---:|---:|
| $`G^{ab}G_{ab}`$ | $`-L_0/2`$ | $`-(10k+N_0^2/L_0^2)/2+g^2L_0^2/8`$ | $`-N_0^2/L_0^2`$ | $`-5k-3N_0^2/(2L_0^2)+g^2L_0^2/8`$ |
| $`H^{ab}H_{ab}`$ | $`4L_0`$ | $`4(10k+N_0^2/L_0^2)-g^2L_0^2`$ | $`0`$ | $`40k+4N_0^2/L_0^2-g^2L_0^2`$ |
| $`E^aE_a`$ | $`-2/L_0`$ | $`2(10k+N_0^2/L_0^2)/L_0^2-g^2/2`$ | $`0`$ | $`20k/L_0^2+2N_0^2/L_0^4-g^2/2`$ |
| $`V'_a{}^{ij}V'{}^a_{ij}`$ | $`2L_0`$ | $`2(10k+N_0^2/L_0^2)-g^2L_0^2/2`$ | $`0`$ | $`20k+2N_0^2/L_0^2-g^2L_0^2/2`$ |
| $`(\bar{\mathcal D}^aV'_a{}^{ij})(\bar{\mathcal D}^bV'_{b,ij})`$ | $`0`$ | $`2`$ | $`0`$ | $`2`$ |
| $`H^{ab}G_{ab}`$ | $`0`$ | $`0`$ | $`4N_0^2/L_0^2`$ | $`4N_0^2/L_0^2`$ |
| $`F'^{ab}F'_{ab}`$ | $`0`$ | $`0`$ | $`-1/4`$ | $`-1/4`$ |
| $`G^{ab}F'_{ab}`$ | $`0`$ | $`0`$ | $`N_0/L_0`$ | $`N_0/L_0`$ |
| $`H^{ab}F'_{ab}`$ | $`0`$ | $`0`$ | $`-4N_0/L_0`$ | $`-4N_0/L_0`$ |
| $`E^aV_a`$ | $`-2\sqrt2`$ | $`0`$ | $`0`$ | $`0`$ |
| $`E^aC_a`$ | $`-4g`$ | $`0`$ | $`0`$ | $`0`$ |

For the first four rows, the coefficient multiplying the quadratic correction in (4.8) is $`2(\alpha Y'_0-gN_0)=2(-10k-N_0^2/L_0^2+g^2L_0^2/4)`$. This directly gives the third column, including its gauging terms. All R² columns acquire the overall $`\lambda`$ in the total action.

Distribute the curl square and the two mixed products explicitly:

```math
\begin{aligned}
-\frac\lambda4(F'^{(1)})^2={}&-\frac{4\lambda}{L_0^2}(\bar{\mathcal D}_{[a}E_{b]})(\bar{\mathcal D}^{[a}E^{b]})
-2\lambda(\bar{\mathcal D}_{[a}V_{b]})(\bar{\mathcal D}^{[a}V^{b]})\\
&-\frac{4\sqrt2\lambda}{L_0}(\bar{\mathcal D}_{[a}E_{b]})(\bar{\mathcal D}^{[a}V^{b]}),\\
\frac{\lambda N_0}{L_0}G^{ab}F'_{ab}{}^{(1)}={}&\frac{4\lambda N_0}{L_0^2}G^{ab}\bar{\mathcal D}_{[a}E_{b]}
+\frac{2\sqrt2\lambda N_0}{L_0}G^{ab}\bar{\mathcal D}_{[a}V_{b]},\\
-\frac{4\lambda N_0}{L_0}H^{ab}F'_{ab}{}^{(1)}={}&-\frac{16\lambda N_0}{L_0^2}H^{ab}\bar{\mathcal D}_{[a}E_{b]}
-\frac{8\sqrt2\lambda N_0}{L_0}H^{ab}\bar{\mathcal D}_{[a}V_{b]}.
\end{aligned}
\tag{4.21}
```

The cross coefficient in the first line is $`-(\lambda/4)\,2(4/L_0)(2\sqrt2)=-4\sqrt2\lambda/L_0`$. No constraint or inverse differential operator has been used.

### 4.5 Fermions: expand the full supercovariant definitions

In the next intermediate equations a superscript $`(1)`$ on an odd composite and $`(2)_{\rm F}`$ on an even composite denote Taylor coefficients on the specified background. They are not independent fields. All are removed from the final action. The background values are

```math
\begin{aligned}
\rho'_0&=2N_0/L_0,&Y'_{0ij}&=\frac{\delta_{ij}}{\sqrt2}
\left(-10k-\frac{N_0^2}{L_0^2}+gN_0+\frac{g^2L_0^2}{4}\right),\\
f_0&=-5k/4,&D_0&=-5k/8+gN_0/4+g^2L_0^2/16,\\
T_{0ab}&=0,&\chi_0&=\phi_{0a}=A'_{0a}=F'_{0ab}=0.
\end{aligned}
\tag{4.22}
```

For example $`6f_0+4D_0=-10k+gN_0+g^2L_0^2/4`$, and the triplet map then adds $`-N_0^2/L_0^2`$. This derives the coefficient of $`Y'_0`$.

The first dependent S-connection is obtained by inserting the linear gravitino curvature in its defining projector:

```math
\begin{aligned}
\phi_a^{(1)i}
&=\frac i3\gamma^b(\bar{\mathcal D}_a\psi_b^i-\bar{\mathcal D}_b\psi_a^i)
-\frac i{24}\gamma_a\gamma^{bc}(\bar{\mathcal D}_b\psi_c^i-\bar{\mathcal D}_c\psi_b^i),\\
\gamma^a\phi_a^{(1)i}
&=i\left(\frac13-\frac5{24}\right)\gamma^{ab}
(\bar{\mathcal D}_a\psi_b^i-\bar{\mathcal D}_b\psi_a^i)
=\frac i4\gamma^{ab}\bar{\mathcal D}_a\psi_b^i.
\end{aligned}
\tag{4.23}
```

The $`1/4`$ is $`2(1/3-5/24)`$. The symmetric metric term in $`\gamma^a\gamma^b`$ contracts an antisymmetric curvature to zero. The source's defining-gaugino and linear-fermion derivatives then become

```math
\begin{aligned}
(\mathcal D_a\psi_i^{\rm defining})^{(1)}
&=\frac{gL_0}{2\sqrt2}\delta_{ij}\psi_a^j-\phi_{ai}^{(1)},\\
(\mathcal D_a\varphi_i)^{(1)}
&=\bar{\mathcal D}_a\varphi_i-\frac{N_0}{2}\psi_{ai}
+\frac{3L_0}{\sqrt2}\delta_{ij}\phi_a^{(1)j},\\
\chi^{(1)i}
&=\frac1{32}\gamma^{ab}\bar{\mathcal D}_a\psi_b^i
-\frac{igL_0}{16\sqrt2}\delta^{ij}\gamma^a\psi_{aj}
+\frac g8\varphi^i.
\end{aligned}
\tag{4.24}
```

The last equation follows from $`\chi^i=i\gamma^a\mathcal D_a\psi^{\rm defining\,i}/8+g\varphi^i/8`$, using (4.23) and raising the first line with epsilon. Thus gauging survives the zero defining-gaugino field value.

Insert (4.23)–(4.24) into the primed scalar and spinor maps. The results, in original fields, are

```math
\rho'{}^{(2)}_{\rm F}=\frac{i}{\sqrt2 L_0^2}\delta_{ij}\bar\varphi^i\varphi^j,
\tag{4.25}
```

```math
\begin{aligned}
\lambda'^{(1)}_i={}&-\frac{2i}{L_0}\gamma^a\bar{\mathcal D}_a\varphi_i
+\sqrt2\left(g-\frac{N_0}{L_0^2}\right)\delta_{ij}\varphi^j
+i\left(\frac{N_0}{L_0}-\frac{gL_0}{2}\right)\gamma^a\psi_{ai}
+\sqrt2\delta_{ij}\gamma^{ab}\bar{\mathcal D}_a\psi_b^j.
\end{aligned}
\tag{4.26}
```

For the derivative gravitino term the unreduced coefficient is $`-8i\delta_{ij}\gamma^a\phi_a^j/\sqrt2`$; (4.23) multiplies it by $`i/4`$, giving $`\sqrt2\delta_{ij}\gamma^{ab}\bar{\mathcal D}_a\psi_b^j`$. The algebraic gravitino coefficient is $`(-2i/L_0)(-N_0/2)-igL_0/2`$. The algebraic spinor coefficient is $`-\sqrt2N_0/L_0^2+\sqrt2g`$. These three products account for every nonzero term in (4.26).

Differentiating a primed spinor retains its Q- and S-connection terms:

```math
(\mathcal D_a\lambda'_i)^{(1)}
=\bar{\mathcal D}_a\lambda'^{(1)}_i-Y'_{0ij}\psi_a^j-\rho'_0\phi_{ai}^{(1)}.
\tag{4.27}
```

Equations (4.23), (4.26) and (4.22) explicitly define every term on the right. For instance the first derivative term is $`-2i\gamma^b\bar{\mathcal D}_a\bar{\mathcal D}_b\varphi_i/L_0`$; derivatives on the other three terms in (4.26) preserve exactly the written order. The final action below prints all of these products.

The remaining even completions needed by nonzero background coefficients are

```math
\begin{aligned}
(\mathcal D_a\rho')^{(2)}_{\rm F}
&=\bar{\mathcal D}_a\rho'{}^{(2)}_{\rm F}-\tfrac i2\bar\psi_a^i\lambda'^{(1)}_i,\\
(\Box_c\rho')^{(2)}_{\rm F}
&=\bar{\mathcal D}^a(\mathcal D_a\rho')^{(2)}_{\rm F}
-\tfrac i2\bar\psi_a^i(\mathcal D^a\lambda'_i)^{(1)}
-2\rho'_0\bar\psi_a^i\gamma^a\chi_i^{(1)}
+\tfrac12\bar\phi_a^{(1)i}\gamma^a\lambda'^{(1)}_i\\
&\quad+2f_0\rho'{}^{(2)}_{\rm F}+2\rho'_0 f^{(2)}_{\rm F}.
\end{aligned}
\tag{4.28}
```

The full triplet box is needed even though $`\partial L_0=0`$. The trace of its quadratic fermion coefficient is

```math
\begin{aligned}
\alpha_{ij}(\Box_c L^{ij})^{(2)}_{\rm F}
={}&-i\alpha_{ij}\bar{\mathcal D}^a(\bar\psi_a^{(i}\varphi^{j)})
+6L_0 f^{(2)}_{\rm F}
-i\alpha_{ij}\bar\psi^{a(i}(\mathcal D_a\varphi^{j)})^{(1)}\\
&-6L_0\bar\psi_a^i\gamma^a\chi_i^{(1)}
+\alpha_{ij}\bar\varphi^{(i}\gamma^a\phi_a^{(1)j)}.
\end{aligned}
\tag{4.29}
```

The two terms $`4\bar\psi^{a(i}\gamma_a\chi^{k)}L^j{}_k`$ and its $`i\leftrightarrow j`$ counterpart have zero contraction with the aligned $`\alpha_{ij}`$: their $`SU(2)`$ matrix product is antisymmetric whereas the indicated pair of odd spinor labels is symmetrized. The explicit $`-6L^{ij}\bar\psi\gamma\chi`$ remains in (4.29).

The trace of the two explicit $`N\varphi^2`$ terms in $`Y'`$ is

```math
\begin{aligned}
\alpha^{ij}\left[\frac{iN_0}{L_0^3}\bar\varphi_{(i}\varphi_{j)}
-\frac{3iN_0}{L_0^5}L_{0ij}L_0^{kl}\bar\varphi_k\varphi_l\right]
&=-\frac{2iN_0}{L_0^3}\alpha^{ij}\bar\varphi_i\varphi_j.
\end{aligned}
\tag{4.30}
```

Here $`\alpha^{ij}L_{0ij}=L_0`$ and $`L_0^{kl}=L_0\alpha^{kl}`$, so the coefficient is $`1-3=-2`$. The two explicit $`\chi\varphi`$ triplet terms cancel in the trace with coefficients $`-16i/L_0+16i/L_0=0`$. The trace of the derivative term, after $`\alpha^{ij}L_{0ki}=L_0\delta_k{}^j/2`$, is

```math
\alpha^{ij}\frac2{L_0^3}L_{0k(i}\bar\varphi^k\gamma^a(\mathcal D_a\varphi_{j)})^{(1)}
=\frac1{L_0^2}\bar\varphi^i\gamma^a(\mathcal D_a\varphi_i)^{(1)}.
\tag{4.31}
```

Combining these contractions gives

```math
\alpha^{ij}Y'^{(2)}_{{\rm F}ij}
=\frac1{L_0}\alpha_{ij}(\Box_cL^{ij})^{(2)}_{\rm F}
+4D^{(2)}_{\rm F}
-\frac{2iN_0}{L_0^3}\alpha^{ij}\bar\varphi_i\varphi_j
+\frac1{L_0^2}\bar\varphi^i\gamma^a(\mathcal D_a\varphi_i)^{(1)}.
\tag{4.32}
```

The curvature-composite completions entering this equation are

```math
D^{(2)}_{\rm F}=\tfrac12 f^{(2)}_{\rm F}
-\tfrac i8\bar\psi_a^i(\mathcal D^a\psi_i^{\rm defining})^{(1)}
-\tfrac12\bar\psi_a^i\gamma^a\chi_i^{(1)},
\tag{4.33}
```

```math
\begin{aligned}
K_\mu{}^{ab}&=\tfrac12\bar\psi^{[a i}\gamma^{b]}\psi_{\mu i}
+\tfrac14\bar\psi^{a i}\gamma_\mu\psi^b_i,\\
f^{(2)}_{\rm F}
&=-\tfrac1{16}\left(\bar{\mathcal D}_a K_b{}^{ab}-\bar{\mathcal D}_b K_a{}^{ab}\right)
-\tfrac i{16}\bar\phi_a^{(1)i}\gamma^{ab}\psi_{bi}
+\bar\psi_a^i\gamma^a\chi_i^{(1)}.
\end{aligned}
\tag{4.34}
```

This retains the project-corrected $`+\bar\psi\gamma\chi`$ trace. Expanding every derivative in (4.29), inserting (4.23)–(4.24), (4.33)–(4.34), and preserving the order of the two odd factors yields the following explicit trace. The first two terms, for example, come from the differentiated $`\bar\psi\varphi`$ in (4.29) and its explicit $`\bar\psi\mathcal D\varphi`$ term; the derivative on a product acts on each factor with a plus sign because $`\bar{\mathcal D}`$ is even.

```math
\begin{aligned}
\alpha^{ij}Y\prime{}^{(2)}_{{\rm F}ij}={}&- \frac{\sqrt{2} i}{2 L_0} \delta_{ij} (\bar{\mathcal D}_{a}\bar\psi^{ai}) \varphi^{j}\\
&- \frac{\sqrt{2} i}{L_0} \delta_{ij} \bar\psi_{a}{}^{i} (\bar{\mathcal D}^{a}\varphi^{j})\\
&- \frac{3}{8} (\bar{\mathcal D}_{a}\bar\psi^{ai}) \gamma^{b} \psi_{bi}\\
&- \frac{25}{24} \bar\psi_{a}{}^{i} \gamma^{b} (\bar{\mathcal D}^{a}\psi_{bi})
\end{aligned}
\tag{YT.1}
```

```math
\begin{aligned}
\phantom{\alpha^{ij}Y\prime{}^{(2)}_{{\rm F}ij}={}}&+\frac{1}{4} (\bar{\mathcal D}_{a}\bar\psi_{b}{}^{i}) \gamma^{a} \psi^{b}{}_{i}\\
&+\frac{11}{12} \bar\psi_{a}{}^{i} \gamma^{b} (\bar{\mathcal D}_{b}\psi^{a}{}_{i})\\
&+\frac{1}{8} (\bar{\mathcal D}_{a}\bar\psi_{b}{}^{i}) \gamma^{b} \psi^{a}{}_{i}\\
&+\frac{1}{8} \bar\psi_{a}{}^{i} \gamma^{a} (\bar{\mathcal D}_{b}\psi^{b}{}_{i})
\end{aligned}
\tag{YT.2}
```

```math
\begin{aligned}
\phantom{\alpha^{ij}Y\prime{}^{(2)}_{{\rm F}ij}={}}&+\frac{1}{6} (\bar{\mathcal D}_{a}\bar\psi_{b}{}^{i}) \gamma^{b} \gamma^{ac} \psi_{ci}\\
&- \frac{1}{6} (\bar{\mathcal D}_{a}\bar\psi_{b}{}^{i}) \gamma^{a} \gamma^{bc} \psi_{ci}\\
&+\frac{1}{6} (\bar{\mathcal D}_{a}\bar\psi_{b}{}^{i}) \gamma^{ab} \gamma^{c} \psi_{ci}\\
&+\frac{1}{12} \bar\psi_{a}{}^{i} \gamma^{a} \gamma^{bc} (\bar{\mathcal D}_{b}\psi_{ci})
\end{aligned}
\tag{YT.3}
```

```math
\begin{aligned}
\phantom{\alpha^{ij}Y\prime{}^{(2)}_{{\rm F}ij}={}}&- \frac{1}{12} \bar\psi_{a}{}^{i} \gamma^{a} \gamma^{bc} (\bar{\mathcal D}_{c}\psi_{bi})\\
&- \frac{\sqrt{2} i \left(L_0^{2} g - 2 N_0\right)}{8 L_0} \delta_{ij} \bar\psi_{a}{}^{i} \psi^{aj}\\
&+\frac{2 \sqrt{2} i}{3 L_0} \delta_{ij} \bar\varphi^{i} \gamma^{a} \gamma^{b} (\bar{\mathcal D}_{a}\psi_{b}{}^{j})\\
&- \frac{2 \sqrt{2} i}{3 L_0} \delta_{ij} \bar\varphi^{i} \gamma^{a} \gamma^{b} (\bar{\mathcal D}_{b}\psi_{a}{}^{j})
\end{aligned}
\tag{YT.4}
```

```math
\begin{aligned}
\phantom{\alpha^{ij}Y\prime{}^{(2)}_{{\rm F}ij}={}}&- \frac{5 \sqrt{2} i}{12 L_0} \delta_{ij} \bar\varphi^{i} \gamma^{ab} (\bar{\mathcal D}_{a}\psi_{b}{}^{j})\\
&+\frac{5 \sqrt{2} i}{12 L_0} \delta_{ij} \bar\varphi^{i} \gamma^{ab} (\bar{\mathcal D}_{b}\psi_{a}{}^{j})\\
&- \frac{\sqrt{2} i N_0}{L_0^{3}} \delta_{ij} \bar\varphi^{i} \varphi^{j}\\
&+\frac{1}{L_0^{2}} \bar\varphi^{i} \gamma^{a} (\bar{\mathcal D}_{a}\varphi_{i})
\end{aligned}
\tag{YT.5}
```

```math
\begin{aligned}
\phantom{\alpha^{ij}Y\prime{}^{(2)}_{{\rm F}ij}={}}&- \frac{N_0}{2 L_0^{2}} \bar\varphi^{i} \gamma^{a} \psi_{ai}
\end{aligned}
\tag{YT.6}
```

Only adjacent closed Clifford contractions are simplified in the displayed polynomials. The identities used follow from moving a contracted vector gamma through each antisymmetrized factor:

```math
\begin{aligned}
\gamma_a\gamma^a&=5,\qquad
\gamma_a\gamma^{ab}=(5-1)\gamma^b=4\gamma^b,\qquad
\gamma^{ab}\gamma_b=4\gamma^a,\\
\gamma_a\gamma^{b_1\cdots b_p}\gamma^a
&=(-1)^p(5-2p)\gamma^{b_1\cdots b_p},\qquad
\gamma^{ab}\gamma_{ab}=-5\cdot4=-20.
\end{aligned}
\tag{4.36}
```

In the sandwich identity, $`p`$ anticommutations give $`(-1)^p5`$ and the $`p`$ contractions give $`-2p(-1)^p`$. Open products such as $`\gamma^a\gamma^{bc}\gamma^{de}`$ are left in their explicit matrix order. Derivatives are not commuted; no curvature mass is guessed from a commutator.

### 4.6 Insert the fermion coefficients in every density term

This calculation uses the 42 scalar source groups of Step 4 Eq. (47), with the same fixed mixed-map coefficients. No extra $`C_{1BC}`$ factor is applied. Define $`y_0=-10k-N_0^2/L_0^2+gN_0+g^2L_0^2/4`$ only as the numerical background coefficient in $`Y'_0`$. The nontrivial product selections for the even source groups are

```math
\begin{aligned}
[Y'^{ij}Y'_{ij}]^{(2)}_{\rm F}
&=2y_0\alpha^{ij}Y'^{(2)}_{{\rm F}ij},\\
[-g\rho'Y'^{ij}L_{ij}]^{(2)}_{\rm F}
&=-gL_0\rho'_0\alpha^{ij}Y'^{(2)}_{{\rm F}ij}-gL_0y_0\rho'{}^{(2)}_{\rm F},\\
[\tfrac12\rho'\Box_c\rho']^{(2)}_{\rm F}
&=\tfrac12\rho'_0(\Box_c\rho')^{(2)}_{\rm F}+\rho'_0f_0\rho'{}^{(2)}_{\rm F},\\
[(\rho')^2 f]^{(2)}_{\rm F}
&=(\rho'_0)^2f^{(2)}_{\rm F}+2\rho'_0f_0\rho'{}^{(2)}_{\rm F},\\
[-4(\rho')^2D]^{(2)}_{\rm F}
&=-4(\rho'_0)^2D^{(2)}_{\rm F}-8\rho'_0D_0\rho'{}^{(2)}_{\rm F}.
\end{aligned}
\tag{4.37}
```

For a source term already containing two odd slots, both are replaced by their order-one formulas and each even multiplier by its background value. For example

```math
[-\tfrac12\bar\lambda'^i\not{\mathcal D}\lambda'_i]^{(2)}
=-\tfrac12\overline{\lambda'^{(1)i}}\gamma^a
\left[\bar{\mathcal D}_a\lambda'^{(1)}_i-y_0\alpha_{ij}\psi_a^j-\frac{2N_0}{L_0}\phi_{ai}^{(1)}\right].
\tag{4.38}
```

Use the four summands of (4.26), take their bars using (2.4), and multiply each against the differentiated four summands and the two connection terms in (4.38). The complete resulting products are printed for group 3 below; the same finite distributive operation is printed separately for every other nonzero source group. A barred derivative is not moved onto the second spinor.

The pure-fermion second-order two-derivative source follows from its full BF density:

```math
\begin{aligned}
\ell^{(2)}_{2\partial,\rm F}={}&
\left[-2L^{ij}Y'_{ij}-2i\bar\lambda'^i\varphi_i
+L_{ij}\bar\psi_a^i\gamma^a\lambda'^j-2N\rho'\right]^{(2)}_{\rm F}\\
&-\left(\frac{2N_0}{L_0}+2g\right)\bar\psi_a^i\gamma^a\varphi_i
-\frac i2\left(\frac{2N_0}{L_0}+2g\right)\frac{L_0}{\sqrt2}
\delta_{ij}\bar\psi_a^i\gamma^{ab}\psi_b^j.
\end{aligned}
\tag{4.39}
```

The defining-vector $`Y`$ contribution is bosonic. The ordinary $`E^{\mu\nu}F_{\mu\nu}`$ representative has no pure-fermion quadratic term on this zero-potential background. Equation (4.39) is only used to calculate the fermion coefficient; its bosonic part is already the normalized (4.1).

#### Two-derivative source block Y

Source summand: $`-2L^{ij}Y'_{ij}`$. Its pure-fermion quadratic contribution is

```math
\begin{aligned}
\ell^{(2)}_{TD,1,\rm F}={}&\sqrt{2} i \delta_{ij} (\bar{\mathcal D}_{a}\bar\psi^{ai}) \varphi^{j}\\
&+2 \sqrt{2} i \delta_{ij} \bar\psi_{a}{}^{i} (\bar{\mathcal D}^{a}\varphi^{j})\\
&+\frac{3 L_0}{4} (\bar{\mathcal D}_{a}\bar\psi^{ai}) \gamma^{b} \psi_{bi}\\
&+\frac{25 L_0}{12} \bar\psi_{a}{}^{i} \gamma^{b} (\bar{\mathcal D}^{a}\psi_{bi})
\end{aligned}
\tag{TD1.1}
```

```math
\begin{aligned}
\phantom{\ell^{(2)}_{TD,1,\rm F}={}}&- \frac{L_0}{2} (\bar{\mathcal D}_{a}\bar\psi_{b}{}^{i}) \gamma^{a} \psi^{b}{}_{i}\\
&- \frac{11 L_0}{6} \bar\psi_{a}{}^{i} \gamma^{b} (\bar{\mathcal D}_{b}\psi^{a}{}_{i})\\
&- \frac{L_0}{4} (\bar{\mathcal D}_{a}\bar\psi_{b}{}^{i}) \gamma^{b} \psi^{a}{}_{i}\\
&- \frac{L_0}{4} \bar\psi_{a}{}^{i} \gamma^{a} (\bar{\mathcal D}_{b}\psi^{b}{}_{i})
\end{aligned}
\tag{TD1.2}
```

```math
\begin{aligned}
\phantom{\ell^{(2)}_{TD,1,\rm F}={}}&- \frac{L_0}{3} (\bar{\mathcal D}_{a}\bar\psi_{b}{}^{i}) \gamma^{b} \gamma^{ac} \psi_{ci}\\
&+\frac{L_0}{3} (\bar{\mathcal D}_{a}\bar\psi_{b}{}^{i}) \gamma^{a} \gamma^{bc} \psi_{ci}\\
&- \frac{L_0}{3} (\bar{\mathcal D}_{a}\bar\psi_{b}{}^{i}) \gamma^{ab} \gamma^{c} \psi_{ci}\\
&- \frac{L_0}{6} \bar\psi_{a}{}^{i} \gamma^{a} \gamma^{bc} (\bar{\mathcal D}_{b}\psi_{ci})
\end{aligned}
\tag{TD1.3}
```

```math
\begin{aligned}
\phantom{\ell^{(2)}_{TD,1,\rm F}={}}&+\frac{L_0}{6} \bar\psi_{a}{}^{i} \gamma^{a} \gamma^{bc} (\bar{\mathcal D}_{c}\psi_{bi})\\
&+\frac{\sqrt{2} i \left(L_0^{2} g - 2 N_0\right)}{4} \delta_{ij} \bar\psi_{a}{}^{i} \psi^{aj}\\
&- \frac{4 \sqrt{2} i}{3} \delta_{ij} \bar\varphi^{i} \gamma^{a} \gamma^{b} (\bar{\mathcal D}_{a}\psi_{b}{}^{j})\\
&+\frac{4 \sqrt{2} i}{3} \delta_{ij} \bar\varphi^{i} \gamma^{a} \gamma^{b} (\bar{\mathcal D}_{b}\psi_{a}{}^{j})
\end{aligned}
\tag{TD1.4}
```

```math
\begin{aligned}
\phantom{\ell^{(2)}_{TD,1,\rm F}={}}&+\frac{5 \sqrt{2} i}{6} \delta_{ij} \bar\varphi^{i} \gamma^{ab} (\bar{\mathcal D}_{a}\psi_{b}{}^{j})\\
&- \frac{5 \sqrt{2} i}{6} \delta_{ij} \bar\varphi^{i} \gamma^{ab} (\bar{\mathcal D}_{b}\psi_{a}{}^{j})\\
&+\frac{2 \sqrt{2} i N_0}{L_0^{2}} \delta_{ij} \bar\varphi^{i} \varphi^{j}\\
&- \frac{2}{L_0} \bar\varphi^{i} \gamma^{a} (\bar{\mathcal D}_{a}\varphi_{i})
\end{aligned}
\tag{TD1.5}
```

```math
\begin{aligned}
\phantom{\ell^{(2)}_{TD,1,\rm F}={}}&+\frac{N_0}{L_0} \bar\varphi^{i} \gamma^{a} \psi_{ai}
\end{aligned}
\tag{TD1.6}
```

#### Two-derivative source block lambda

Source summand: $`-2i\bar\lambda'{}^i\varphi_i`$. Its pure-fermion quadratic contribution is

```math
\begin{aligned}
\ell^{(2)}_{TD,2,\rm F}={}&- \frac{4}{L_0} (\bar{\mathcal D}_{a}\bar\varphi^{i}) \gamma^{a} \varphi_{i}\\
&+\frac{2 \sqrt{2} i \left(L_0^{2} g - N_0\right)}{L_0^{2}} \delta_{ij} \bar\varphi^{i} \varphi^{j}\\
&- \frac{L_0^{2} g - 2 N_0}{L_0} \bar\psi_{a}{}^{i} \gamma^{a} \varphi_{i}\\
&- 2 \sqrt{2} i \delta_{ij} (\bar{\mathcal D}_{a}\bar\psi_{b}{}^{i}) \gamma^{ab} \varphi^{j}
\end{aligned}
\tag{TD2.1}
```

#### Two-derivative source block psi-lambda

Source summand: $`L_{ij}\bar\psi_a^i\gamma^a\lambda'{}^j`$. Its pure-fermion quadratic contribution is

```math
\begin{aligned}
\ell^{(2)}_{TD,3,\rm F}={}&- \sqrt{2} i \delta_{ij} \bar\psi_{a}{}^{i} \gamma^{a} \gamma^{b} (\bar{\mathcal D}_{b}\varphi^{j})\\
&- \frac{L_0^{2} g - N_0}{L_0} \bar\psi_{a}{}^{i} \gamma^{a} \varphi_{i}\\
&- \frac{\sqrt{2} i \left(L_0^{2} g - 2 N_0\right)}{4} \delta_{ij} \bar\psi_{a}{}^{i} \gamma^{a} \gamma^{b} \psi_{b}{}^{j}\\
&- L_0 \bar\psi_{a}{}^{i} \gamma^{a} \gamma^{bc} (\bar{\mathcal D}_{b}\psi_{ci})
\end{aligned}
\tag{TD3.1}
```

#### Two-derivative source block rho-N

Source summand: $`-2N\rho'`$. Its pure-fermion quadratic contribution is

```math
\begin{aligned}
\ell^{(2)}_{TD,4,\rm F}={}&- \frac{\sqrt{2} i N_0}{L_0^{2}} \delta_{ij} \bar\varphi^{i} \varphi^{j}
\end{aligned}
\tag{TD4.1}
```

#### Two-derivative source block rho-psi-varphi

Source summand: $`-(\rho'+2g)\bar\psi_a^i\gamma^a\varphi_i`$. Its pure-fermion quadratic contribution is

```math
\begin{aligned}
\ell^{(2)}_{TD,5,\rm F}={}&- \frac{2 \left(L_0 g + N_0\right)}{L_0} \bar\psi_{a}{}^{i} \gamma^{a} \varphi_{i}
\end{aligned}
\tag{TD5.1}
```

#### Two-derivative source block rho-psi-psi

Source summand: $`-\frac i2(\rho'+2g)L_{ij}\bar\psi_a^i\gamma^{ab}\psi_b^j`$. Its pure-fermion quadratic contribution is

```math
\begin{aligned}
\ell^{(2)}_{TD,6,\rm F}={}&- \frac{\sqrt{2} i \left(L_0 g + N_0\right)}{2} \delta_{ij} \bar\psi_{a}{}^{i} \gamma^{ab} \psi_{b}{}^{j}
\end{aligned}
\tag{TD6.1}
```

#### R² source group 1

Source summand: $`Y'^{ij}Y'_{ij}`$. Its pure-fermion quadratic contribution is

```math
\begin{aligned}
\ell^{(2)}_{RG,1,\rm F}={}&- \frac{\sqrt{2} i \left(L_0^{4} g^{2} + 4 L_0^{2} N_0 g - 40 L_0^{2} k - 4 N_0^{2}\right)}{4 L_0^{3}} \delta_{ij} (\bar{\mathcal D}_{a}\bar\psi^{ai}) \varphi^{j}\\
&- \frac{\sqrt{2} i \left(L_0^{4} g^{2} + 4 L_0^{2} N_0 g - 40 L_0^{2} k - 4 N_0^{2}\right)}{2 L_0^{3}} \delta_{ij} \bar\psi_{a}{}^{i} (\bar{\mathcal D}^{a}\varphi^{j})\\
&- \frac{3 \left(L_0^{4} g^{2} + 4 L_0^{2} N_0 g - 40 L_0^{2} k - 4 N_0^{2}\right)}{16 L_0^{2}} (\bar{\mathcal D}_{a}\bar\psi^{ai}) \gamma^{b} \psi_{bi}\\
&- \frac{25 \left(L_0^{4} g^{2} + 4 L_0^{2} N_0 g - 40 L_0^{2} k - 4 N_0^{2}\right)}{48 L_0^{2}} \bar\psi_{a}{}^{i} \gamma^{b} (\bar{\mathcal D}^{a}\psi_{bi})
\end{aligned}
\tag{RG1.1}
```

```math
\begin{aligned}
\phantom{\ell^{(2)}_{RG,1,\rm F}={}}&+\frac{L_0^{4} g^{2} + 4 L_0^{2} N_0 g - 40 L_0^{2} k - 4 N_0^{2}}{8 L_0^{2}} (\bar{\mathcal D}_{a}\bar\psi_{b}{}^{i}) \gamma^{a} \psi^{b}{}_{i}\\
&+\frac{11 \left(L_0^{4} g^{2} + 4 L_0^{2} N_0 g - 40 L_0^{2} k - 4 N_0^{2}\right)}{24 L_0^{2}} \bar\psi_{a}{}^{i} \gamma^{b} (\bar{\mathcal D}_{b}\psi^{a}{}_{i})\\
&+\frac{L_0^{4} g^{2} + 4 L_0^{2} N_0 g - 40 L_0^{2} k - 4 N_0^{2}}{16 L_0^{2}} (\bar{\mathcal D}_{a}\bar\psi_{b}{}^{i}) \gamma^{b} \psi^{a}{}_{i}\\
&+\frac{L_0^{4} g^{2} + 4 L_0^{2} N_0 g - 40 L_0^{2} k - 4 N_0^{2}}{16 L_0^{2}} \bar\psi_{a}{}^{i} \gamma^{a} (\bar{\mathcal D}_{b}\psi^{b}{}_{i})
\end{aligned}
\tag{RG1.2}
```

```math
\begin{aligned}
\phantom{\ell^{(2)}_{RG,1,\rm F}={}}&+\frac{L_0^{4} g^{2} + 4 L_0^{2} N_0 g - 40 L_0^{2} k - 4 N_0^{2}}{12 L_0^{2}} (\bar{\mathcal D}_{a}\bar\psi_{b}{}^{i}) \gamma^{b} \gamma^{ac} \psi_{ci}\\
&- \frac{L_0^{4} g^{2} + 4 L_0^{2} N_0 g - 40 L_0^{2} k - 4 N_0^{2}}{12 L_0^{2}} (\bar{\mathcal D}_{a}\bar\psi_{b}{}^{i}) \gamma^{a} \gamma^{bc} \psi_{ci}\\
&+\frac{L_0^{4} g^{2} + 4 L_0^{2} N_0 g - 40 L_0^{2} k - 4 N_0^{2}}{12 L_0^{2}} (\bar{\mathcal D}_{a}\bar\psi_{b}{}^{i}) \gamma^{ab} \gamma^{c} \psi_{ci}\\
&+\frac{L_0^{4} g^{2} + 4 L_0^{2} N_0 g - 40 L_0^{2} k - 4 N_0^{2}}{24 L_0^{2}} \bar\psi_{a}{}^{i} \gamma^{a} \gamma^{bc} (\bar{\mathcal D}_{b}\psi_{ci})
\end{aligned}
\tag{RG1.3}
```

```math
\begin{aligned}
\phantom{\ell^{(2)}_{RG,1,\rm F}={}}&- \frac{L_0^{4} g^{2} + 4 L_0^{2} N_0 g - 40 L_0^{2} k - 4 N_0^{2}}{24 L_0^{2}} \bar\psi_{a}{}^{i} \gamma^{a} \gamma^{bc} (\bar{\mathcal D}_{c}\psi_{bi})\\
&- \frac{\sqrt{2} i \left(L_0^{2} g - 2 N_0\right) \left(L_0^{4} g^{2} + 4 L_0^{2} N_0 g - 40 L_0^{2} k - 4 N_0^{2}\right)}{16 L_0^{3}} \delta_{ij} \bar\psi_{a}{}^{i} \psi^{aj}\\
&+\frac{\sqrt{2} i \left(L_0^{4} g^{2} + 4 L_0^{2} N_0 g - 40 L_0^{2} k - 4 N_0^{2}\right)}{3 L_0^{3}} \delta_{ij} \bar\varphi^{i} \gamma^{a} \gamma^{b} (\bar{\mathcal D}_{a}\psi_{b}{}^{j})\\
&- \frac{\sqrt{2} i \left(L_0^{4} g^{2} + 4 L_0^{2} N_0 g - 40 L_0^{2} k - 4 N_0^{2}\right)}{3 L_0^{3}} \delta_{ij} \bar\varphi^{i} \gamma^{a} \gamma^{b} (\bar{\mathcal D}_{b}\psi_{a}{}^{j})
\end{aligned}
\tag{RG1.4}
```

```math
\begin{aligned}
\phantom{\ell^{(2)}_{RG,1,\rm F}={}}&- \frac{5 \sqrt{2} i \left(L_0^{4} g^{2} + 4 L_0^{2} N_0 g - 40 L_0^{2} k - 4 N_0^{2}\right)}{24 L_0^{3}} \delta_{ij} \bar\varphi^{i} \gamma^{ab} (\bar{\mathcal D}_{a}\psi_{b}{}^{j})\\
&+\frac{5 \sqrt{2} i \left(L_0^{4} g^{2} + 4 L_0^{2} N_0 g - 40 L_0^{2} k - 4 N_0^{2}\right)}{24 L_0^{3}} \delta_{ij} \bar\varphi^{i} \gamma^{ab} (\bar{\mathcal D}_{b}\psi_{a}{}^{j})\\
&- \frac{\sqrt{2} i N_0 \left(L_0^{4} g^{2} + 4 L_0^{2} N_0 g - 40 L_0^{2} k - 4 N_0^{2}\right)}{2 L_0^{5}} \delta_{ij} \bar\varphi^{i} \varphi^{j}\\
&+\frac{L_0^{4} g^{2} + 4 L_0^{2} N_0 g - 40 L_0^{2} k - 4 N_0^{2}}{2 L_0^{4}} \bar\varphi^{i} \gamma^{a} (\bar{\mathcal D}_{a}\varphi_{i})
\end{aligned}
\tag{RG1.5}
```

```math
\begin{aligned}
\phantom{\ell^{(2)}_{RG,1,\rm F}={}}&- \frac{N_0 \left(L_0^{4} g^{2} + 4 L_0^{2} N_0 g - 40 L_0^{2} k - 4 N_0^{2}\right)}{4 L_0^{4}} \bar\varphi^{i} \gamma^{a} \psi_{ai}
\end{aligned}
\tag{RG1.6}
```

#### R² source group 2

Source summand: $`-g\rho'Y'^{ij}L_{ij}`$. Its pure-fermion quadratic contribution is

```math
\begin{aligned}
\ell^{(2)}_{RG,2,\rm F}={}&\frac{\sqrt{2} i N_0 g}{L_0} \delta_{ij} (\bar{\mathcal D}_{a}\bar\psi^{ai}) \varphi^{j}\\
&+\frac{2 \sqrt{2} i N_0 g}{L_0} \delta_{ij} \bar\psi_{a}{}^{i} (\bar{\mathcal D}^{a}\varphi^{j})\\
&+\frac{3 N_0 g}{4} (\bar{\mathcal D}_{a}\bar\psi^{ai}) \gamma^{b} \psi_{bi}\\
&+\frac{25 N_0 g}{12} \bar\psi_{a}{}^{i} \gamma^{b} (\bar{\mathcal D}^{a}\psi_{bi})
\end{aligned}
\tag{RG2.1}
```

```math
\begin{aligned}
\phantom{\ell^{(2)}_{RG,2,\rm F}={}}&- \frac{N_0 g}{2} (\bar{\mathcal D}_{a}\bar\psi_{b}{}^{i}) \gamma^{a} \psi^{b}{}_{i}\\
&- \frac{11 N_0 g}{6} \bar\psi_{a}{}^{i} \gamma^{b} (\bar{\mathcal D}_{b}\psi^{a}{}_{i})\\
&- \frac{N_0 g}{4} (\bar{\mathcal D}_{a}\bar\psi_{b}{}^{i}) \gamma^{b} \psi^{a}{}_{i}\\
&- \frac{N_0 g}{4} \bar\psi_{a}{}^{i} \gamma^{a} (\bar{\mathcal D}_{b}\psi^{b}{}_{i})
\end{aligned}
\tag{RG2.2}
```

```math
\begin{aligned}
\phantom{\ell^{(2)}_{RG,2,\rm F}={}}&- \frac{N_0 g}{3} (\bar{\mathcal D}_{a}\bar\psi_{b}{}^{i}) \gamma^{b} \gamma^{ac} \psi_{ci}\\
&+\frac{N_0 g}{3} (\bar{\mathcal D}_{a}\bar\psi_{b}{}^{i}) \gamma^{a} \gamma^{bc} \psi_{ci}\\
&- \frac{N_0 g}{3} (\bar{\mathcal D}_{a}\bar\psi_{b}{}^{i}) \gamma^{ab} \gamma^{c} \psi_{ci}\\
&- \frac{N_0 g}{6} \bar\psi_{a}{}^{i} \gamma^{a} \gamma^{bc} (\bar{\mathcal D}_{b}\psi_{ci})
\end{aligned}
\tag{RG2.3}
```

```math
\begin{aligned}
\phantom{\ell^{(2)}_{RG,2,\rm F}={}}&+\frac{N_0 g}{6} \bar\psi_{a}{}^{i} \gamma^{a} \gamma^{bc} (\bar{\mathcal D}_{c}\psi_{bi})\\
&+\frac{\sqrt{2} i N_0 g \left(L_0^{2} g - 2 N_0\right)}{4 L_0} \delta_{ij} \bar\psi_{a}{}^{i} \psi^{aj}\\
&- \frac{4 \sqrt{2} i N_0 g}{3 L_0} \delta_{ij} \bar\varphi^{i} \gamma^{a} \gamma^{b} (\bar{\mathcal D}_{a}\psi_{b}{}^{j})\\
&+\frac{4 \sqrt{2} i N_0 g}{3 L_0} \delta_{ij} \bar\varphi^{i} \gamma^{a} \gamma^{b} (\bar{\mathcal D}_{b}\psi_{a}{}^{j})
\end{aligned}
\tag{RG2.4}
```

```math
\begin{aligned}
\phantom{\ell^{(2)}_{RG,2,\rm F}={}}&+\frac{5 \sqrt{2} i N_0 g}{6 L_0} \delta_{ij} \bar\varphi^{i} \gamma^{ab} (\bar{\mathcal D}_{a}\psi_{b}{}^{j})\\
&- \frac{5 \sqrt{2} i N_0 g}{6 L_0} \delta_{ij} \bar\varphi^{i} \gamma^{ab} (\bar{\mathcal D}_{b}\psi_{a}{}^{j})\\
&- \frac{\sqrt{2} i g \left(L_0^{4} g^{2} + 4 L_0^{2} N_0 g - 40 L_0^{2} k - 20 N_0^{2}\right)}{8 L_0^{3}} \delta_{ij} \bar\varphi^{i} \varphi^{j}\\
&- \frac{2 N_0 g}{L_0^{2}} \bar\varphi^{i} \gamma^{a} (\bar{\mathcal D}_{a}\varphi_{i})
\end{aligned}
\tag{RG2.5}
```

```math
\begin{aligned}
\phantom{\ell^{(2)}_{RG,2,\rm F}={}}&+\frac{N_0^{2} g}{L_0^{2}} \bar\varphi^{i} \gamma^{a} \psi_{ai}
\end{aligned}
\tag{RG2.6}
```

#### R² source group 3

Source summand: $`-\frac12\bar\lambda'{}^i\not{\mathcal D}\lambda'_i`$. Its pure-fermion quadratic contribution is

```math
\begin{aligned}
\ell^{(2)}_{RG,3,\rm F}={}&\frac{2}{L_0^{2}} (\bar{\mathcal D}_{a}\bar\varphi^{i}) \gamma^{a} \gamma^{b} \gamma^{c} (\bar{\mathcal D}_{b}\bar{\mathcal D}_{c}\varphi_{i})\\
&+\frac{\sqrt{2} i \left(L_0^{2} g - N_0\right)}{L_0^{3}} \delta_{ij} (\bar{\mathcal D}_{a}\bar\varphi^{i}) \gamma^{a} \gamma^{b} (\bar{\mathcal D}_{b}\varphi^{j})\\
&+\frac{3 L_0^{2} g - 2 N_0}{6 L_0^{2}} (\bar{\mathcal D}_{a}\bar\varphi^{i}) \gamma^{a} \gamma^{b} \gamma^{c} (\bar{\mathcal D}_{b}\psi_{ci})\\
&+\frac{\sqrt{2} i}{L_0} \delta_{ij} (\bar{\mathcal D}_{a}\bar\varphi^{i}) \gamma^{a} \gamma^{b} \gamma^{cd} (\bar{\mathcal D}_{b}\bar{\mathcal D}_{c}\psi_{d}{}^{j})
\end{aligned}
\tag{RG3.1}
```

```math
\begin{aligned}
\phantom{\ell^{(2)}_{RG,3,\rm F}={}}&- \frac{\sqrt{2} i \left(L_0^{4} g^{2} + 4 L_0^{2} N_0 g - 40 L_0^{2} k - 4 N_0^{2}\right)}{8 L_0^{3}} \delta_{ij} (\bar{\mathcal D}_{a}\bar\varphi^{i}) \gamma^{a} \gamma^{b} \psi_{b}{}^{j}\\
&- \frac{2 N_0}{3 L_0^{2}} (\bar{\mathcal D}_{a}\bar\varphi^{i}) \gamma^{a} \gamma^{b} \gamma^{c} (\bar{\mathcal D}_{c}\psi_{bi})\\
&- \frac{5 N_0}{12 L_0^{2}} (\bar{\mathcal D}_{a}\bar\varphi^{i}) \gamma^{a} \gamma^{bc} (\bar{\mathcal D}_{b}\psi_{ci})\\
&+\frac{5 N_0}{12 L_0^{2}} (\bar{\mathcal D}_{a}\bar\varphi^{i}) \gamma^{a} \gamma^{bc} (\bar{\mathcal D}_{c}\psi_{bi})
\end{aligned}
\tag{RG3.2}
```

```math
\begin{aligned}
\phantom{\ell^{(2)}_{RG,3,\rm F}={}}&- \frac{\sqrt{2} i \left(L_0^{2} g - N_0\right)}{L_0^{3}} \delta_{ij} \bar\varphi^{i} \gamma^{a} \gamma^{b} (\bar{\mathcal D}_{a}\bar{\mathcal D}_{b}\varphi^{j})\\
&- \frac{\left(L_0^{2} g - N_0\right)^{2}}{L_0^{4}} \bar\varphi^{i} \gamma^{a} (\bar{\mathcal D}_{a}\varphi_{i})\\
&- \frac{\sqrt{2} i \left(L_0^{2} g - N_0\right) \left(3 L_0^{2} g - 2 N_0\right)}{12 L_0^{3}} \delta_{ij} \bar\varphi^{i} \gamma^{a} \gamma^{b} (\bar{\mathcal D}_{a}\psi_{b}{}^{j})\\
&- \frac{L_0^{2} g - N_0}{L_0^{2}} \bar\varphi^{i} \gamma^{a} \gamma^{bc} (\bar{\mathcal D}_{a}\bar{\mathcal D}_{b}\psi_{ci})
\end{aligned}
\tag{RG3.3}
```

```math
\begin{aligned}
\phantom{\ell^{(2)}_{RG,3,\rm F}={}}&+\frac{\left(L_0^{2} g - N_0\right) \left(L_0^{4} g^{2} + 4 L_0^{2} N_0 g - 40 L_0^{2} k - 4 N_0^{2}\right)}{8 L_0^{4}} \bar\varphi^{i} \gamma^{a} \psi_{ai}\\
&+\frac{\sqrt{2} i N_0 \left(L_0^{2} g - N_0\right)}{3 L_0^{3}} \delta_{ij} \bar\varphi^{i} \gamma^{a} \gamma^{b} (\bar{\mathcal D}_{b}\psi_{a}{}^{j})\\
&+\frac{5 \sqrt{2} i N_0 \left(L_0^{2} g - N_0\right)}{24 L_0^{3}} \delta_{ij} \bar\varphi^{i} \gamma^{ab} (\bar{\mathcal D}_{a}\psi_{b}{}^{j})\\
&- \frac{5 \sqrt{2} i N_0 \left(L_0^{2} g - N_0\right)}{24 L_0^{3}} \delta_{ij} \bar\varphi^{i} \gamma^{ab} (\bar{\mathcal D}_{b}\psi_{a}{}^{j})
\end{aligned}
\tag{RG3.4}
```

```math
\begin{aligned}
\phantom{\ell^{(2)}_{RG,3,\rm F}={}}&+\frac{L_0^{2} g - 2 N_0}{2 L_0^{2}} \bar\psi_{a}{}^{i} \gamma^{a} \gamma^{b} \gamma^{c} (\bar{\mathcal D}_{b}\bar{\mathcal D}_{c}\varphi_{i})\\
&+\frac{\sqrt{2} i \left(L_0^{2} g - 2 N_0\right) \left(L_0^{2} g - N_0\right)}{4 L_0^{3}} \delta_{ij} \bar\psi_{a}{}^{i} \gamma^{a} \gamma^{b} (\bar{\mathcal D}_{b}\varphi^{j})\\
&+\frac{\left(L_0^{2} g - 2 N_0\right) \left(3 L_0^{2} g - 2 N_0\right)}{24 L_0^{2}} \bar\psi_{a}{}^{i} \gamma^{a} \gamma^{b} \gamma^{c} (\bar{\mathcal D}_{b}\psi_{ci})\\
&+\frac{\sqrt{2} i \left(L_0^{2} g - 2 N_0\right)}{4 L_0} \delta_{ij} \bar\psi_{a}{}^{i} \gamma^{a} \gamma^{b} \gamma^{cd} (\bar{\mathcal D}_{b}\bar{\mathcal D}_{c}\psi_{d}{}^{j})
\end{aligned}
\tag{RG3.5}
```

```math
\begin{aligned}
\phantom{\ell^{(2)}_{RG,3,\rm F}={}}&- \frac{\sqrt{2} i \left(L_0^{2} g - 2 N_0\right) \left(L_0^{4} g^{2} + 4 L_0^{2} N_0 g - 40 L_0^{2} k - 4 N_0^{2}\right)}{32 L_0^{3}} \delta_{ij} \bar\psi_{a}{}^{i} \gamma^{a} \gamma^{b} \psi_{b}{}^{j}\\
&- \frac{N_0 \left(L_0^{2} g - 2 N_0\right)}{6 L_0^{2}} \bar\psi_{a}{}^{i} \gamma^{a} \gamma^{b} \gamma^{c} (\bar{\mathcal D}_{c}\psi_{bi})\\
&- \frac{5 N_0 \left(L_0^{2} g - 2 N_0\right)}{48 L_0^{2}} \bar\psi_{a}{}^{i} \gamma^{a} \gamma^{bc} (\bar{\mathcal D}_{b}\psi_{ci})\\
&+\frac{5 N_0 \left(L_0^{2} g - 2 N_0\right)}{48 L_0^{2}} \bar\psi_{a}{}^{i} \gamma^{a} \gamma^{bc} (\bar{\mathcal D}_{c}\psi_{bi})
\end{aligned}
\tag{RG3.6}
```

```math
\begin{aligned}
\phantom{\ell^{(2)}_{RG,3,\rm F}={}}&+\frac{\sqrt{2} i}{L_0} \delta_{ij} (\bar{\mathcal D}_{a}\bar\psi_{b}{}^{i}) \gamma^{ab} \gamma^{c} \gamma^{d} (\bar{\mathcal D}_{c}\bar{\mathcal D}_{d}\varphi^{j})\\
&+\frac{L_0^{2} g - N_0}{L_0^{2}} (\bar{\mathcal D}_{a}\bar\psi_{b}{}^{i}) \gamma^{ab} \gamma^{c} (\bar{\mathcal D}_{c}\varphi_{i})\\
&+\frac{\sqrt{2} i \left(3 L_0^{2} g - 2 N_0\right)}{12 L_0} \delta_{ij} (\bar{\mathcal D}_{a}\bar\psi_{b}{}^{i}) \gamma^{ab} \gamma^{c} \gamma^{d} (\bar{\mathcal D}_{c}\psi_{d}{}^{j})\\
&+(\bar{\mathcal D}_{a}\bar\psi_{b}{}^{i}) \gamma^{ab} \gamma^{c} \gamma^{de} (\bar{\mathcal D}_{c}\bar{\mathcal D}_{d}\psi_{ei})
\end{aligned}
\tag{RG3.7}
```

```math
\begin{aligned}
\phantom{\ell^{(2)}_{RG,3,\rm F}={}}&- \frac{L_0^{4} g^{2} + 4 L_0^{2} N_0 g - 40 L_0^{2} k - 4 N_0^{2}}{8 L_0^{2}} (\bar{\mathcal D}_{a}\bar\psi_{b}{}^{i}) \gamma^{ab} \gamma^{c} \psi_{ci}\\
&- \frac{\sqrt{2} i N_0}{3 L_0} \delta_{ij} (\bar{\mathcal D}_{a}\bar\psi_{b}{}^{i}) \gamma^{ab} \gamma^{c} \gamma^{d} (\bar{\mathcal D}_{d}\psi_{c}{}^{j})\\
&- \frac{5 \sqrt{2} i N_0}{24 L_0} \delta_{ij} (\bar{\mathcal D}_{a}\bar\psi_{b}{}^{i}) \gamma^{ab} \gamma^{cd} (\bar{\mathcal D}_{c}\psi_{d}{}^{j})\\
&+\frac{5 \sqrt{2} i N_0}{24 L_0} \delta_{ij} (\bar{\mathcal D}_{a}\bar\psi_{b}{}^{i}) \gamma^{ab} \gamma^{cd} (\bar{\mathcal D}_{d}\psi_{c}{}^{j})
\end{aligned}
\tag{RG3.8}
```

#### R² source group 4

Source summand: $`+i\bar\lambda'{}^i\gamma\!\cdot\!T\lambda'_i`$. Its pure-fermion quadratic contribution is

```math
\begin{aligned}
\ell^{(2)}_{RG,4,\rm F}={}&0
\end{aligned}
\tag{RG4.1}
```

#### R² source group 5

Source summand: $`-8i\rho'\bar\lambda'{}^i\chi_i`$. Its pure-fermion quadratic contribution is

```math
\begin{aligned}
\ell^{(2)}_{RG,5,\rm F}={}&- \frac{\sqrt{2} i N_0 g}{L_0} \delta_{ij} (\bar{\mathcal D}_{a}\bar\varphi^{i}) \gamma^{a} \gamma^{b} \psi_{b}{}^{j}\\
&- \frac{4 N_0}{3 L_0^{2}} (\bar{\mathcal D}_{a}\bar\varphi^{i}) \gamma^{a} \gamma^{b} \gamma^{c} (\bar{\mathcal D}_{b}\psi_{ci})\\
&+\frac{4 N_0}{3 L_0^{2}} (\bar{\mathcal D}_{a}\bar\varphi^{i}) \gamma^{a} \gamma^{b} \gamma^{c} (\bar{\mathcal D}_{c}\psi_{bi})\\
&+\frac{5 N_0}{6 L_0^{2}} (\bar{\mathcal D}_{a}\bar\varphi^{i}) \gamma^{a} \gamma^{bc} (\bar{\mathcal D}_{b}\psi_{ci})
\end{aligned}
\tag{RG5.1}
```

```math
\begin{aligned}
\phantom{\ell^{(2)}_{RG,5,\rm F}={}}&- \frac{5 N_0}{6 L_0^{2}} (\bar{\mathcal D}_{a}\bar\varphi^{i}) \gamma^{a} \gamma^{bc} (\bar{\mathcal D}_{c}\psi_{bi})\\
&- \frac{4 N_0 g}{L_0^{2}} (\bar{\mathcal D}_{a}\bar\varphi^{i}) \gamma^{a} \varphi_{i}\\
&+\frac{N_0 g \left(L_0^{2} g - N_0\right)}{L_0^{2}} \bar\varphi^{i} \gamma^{a} \psi_{ai}\\
&+\frac{2 \sqrt{2} i N_0 \left(L_0^{2} g - N_0\right)}{3 L_0^{3}} \delta_{ij} \bar\varphi^{i} \gamma^{a} \gamma^{b} (\bar{\mathcal D}_{a}\psi_{b}{}^{j})
\end{aligned}
\tag{RG5.2}
```

```math
\begin{aligned}
\phantom{\ell^{(2)}_{RG,5,\rm F}={}}&- \frac{2 \sqrt{2} i N_0 \left(L_0^{2} g - N_0\right)}{3 L_0^{3}} \delta_{ij} \bar\varphi^{i} \gamma^{a} \gamma^{b} (\bar{\mathcal D}_{b}\psi_{a}{}^{j})\\
&- \frac{5 \sqrt{2} i N_0 \left(L_0^{2} g - N_0\right)}{12 L_0^{3}} \delta_{ij} \bar\varphi^{i} \gamma^{ab} (\bar{\mathcal D}_{a}\psi_{b}{}^{j})\\
&+\frac{5 \sqrt{2} i N_0 \left(L_0^{2} g - N_0\right)}{12 L_0^{3}} \delta_{ij} \bar\varphi^{i} \gamma^{ab} (\bar{\mathcal D}_{b}\psi_{a}{}^{j})\\
&+\frac{2 \sqrt{2} i N_0 g \left(L_0^{2} g - N_0\right)}{L_0^{3}} \delta_{ij} \bar\varphi^{i} \varphi^{j}
\end{aligned}
\tag{RG5.3}
```

```math
\begin{aligned}
\phantom{\ell^{(2)}_{RG,5,\rm F}={}}&- \frac{\sqrt{2} i N_0 g \left(L_0^{2} g - 2 N_0\right)}{4 L_0} \delta_{ij} \bar\psi_{a}{}^{i} \gamma^{a} \gamma^{b} \psi_{b}{}^{j}\\
&- \frac{N_0 \left(L_0^{2} g - 2 N_0\right)}{3 L_0^{2}} \bar\psi_{a}{}^{i} \gamma^{a} \gamma^{b} \gamma^{c} (\bar{\mathcal D}_{b}\psi_{ci})\\
&+\frac{N_0 \left(L_0^{2} g - 2 N_0\right)}{3 L_0^{2}} \bar\psi_{a}{}^{i} \gamma^{a} \gamma^{b} \gamma^{c} (\bar{\mathcal D}_{c}\psi_{bi})\\
&+\frac{5 N_0 \left(L_0^{2} g - 2 N_0\right)}{24 L_0^{2}} \bar\psi_{a}{}^{i} \gamma^{a} \gamma^{bc} (\bar{\mathcal D}_{b}\psi_{ci})
\end{aligned}
\tag{RG5.4}
```

```math
\begin{aligned}
\phantom{\ell^{(2)}_{RG,5,\rm F}={}}&- \frac{5 N_0 \left(L_0^{2} g - 2 N_0\right)}{24 L_0^{2}} \bar\psi_{a}{}^{i} \gamma^{a} \gamma^{bc} (\bar{\mathcal D}_{c}\psi_{bi})\\
&- \frac{N_0 g \left(L_0^{2} g - 2 N_0\right)}{L_0^{2}} \bar\psi_{a}{}^{i} \gamma^{a} \varphi_{i}\\
&- N_0 g (\bar{\mathcal D}_{a}\bar\psi_{b}{}^{i}) \gamma^{ab} \gamma^{c} \psi_{ci}\\
&- \frac{2 \sqrt{2} i N_0}{3 L_0} \delta_{ij} (\bar{\mathcal D}_{a}\bar\psi_{b}{}^{i}) \gamma^{ab} \gamma^{c} \gamma^{d} (\bar{\mathcal D}_{c}\psi_{d}{}^{j})
\end{aligned}
\tag{RG5.5}
```

```math
\begin{aligned}
\phantom{\ell^{(2)}_{RG,5,\rm F}={}}&+\frac{2 \sqrt{2} i N_0}{3 L_0} \delta_{ij} (\bar{\mathcal D}_{a}\bar\psi_{b}{}^{i}) \gamma^{ab} \gamma^{c} \gamma^{d} (\bar{\mathcal D}_{d}\psi_{c}{}^{j})\\
&+\frac{5 \sqrt{2} i N_0}{12 L_0} \delta_{ij} (\bar{\mathcal D}_{a}\bar\psi_{b}{}^{i}) \gamma^{ab} \gamma^{cd} (\bar{\mathcal D}_{c}\psi_{d}{}^{j})\\
&- \frac{5 \sqrt{2} i N_0}{12 L_0} \delta_{ij} (\bar{\mathcal D}_{a}\bar\psi_{b}{}^{i}) \gamma^{ab} \gamma^{cd} (\bar{\mathcal D}_{d}\psi_{c}{}^{j})\\
&- \frac{2 \sqrt{2} i N_0 g}{L_0} \delta_{ij} (\bar{\mathcal D}_{a}\bar\psi_{b}{}^{i}) \gamma^{ab} \varphi^{j}
\end{aligned}
\tag{RG5.6}
```

#### R² source group 6

Source summand: $`-\frac i8\bar\lambda'{}^i\gamma\!\cdot\!\widehat G\lambda'_i`$. Its pure-fermion quadratic contribution is

```math
\begin{aligned}
\ell^{(2)}_{RG,6,\rm F}={}&0
\end{aligned}
\tag{RG6.1}
```

#### R² source group 7

Source summand: $`+\frac{ig}4\bar\lambda'{}^iL_{ij}\lambda'{}^j`$. Its pure-fermion quadratic contribution is

```math
\begin{aligned}
\ell^{(2)}_{RG,7,\rm F}={}&- \frac{\sqrt{2} i g}{2 L_0} \delta_{ij} (\bar{\mathcal D}_{a}\bar\varphi^{i}) \gamma^{a} \gamma^{b} (\bar{\mathcal D}_{b}\varphi^{j})\\
&- \frac{g \left(L_0^{2} g - N_0\right)}{2 L_0^{2}} (\bar{\mathcal D}_{a}\bar\varphi^{i}) \gamma^{a} \varphi_{i}\\
&- \frac{\sqrt{2} i g \left(L_0^{2} g - 2 N_0\right)}{8 L_0} \delta_{ij} (\bar{\mathcal D}_{a}\bar\varphi^{i}) \gamma^{a} \gamma^{b} \psi_{b}{}^{j}\\
&- \frac{g}{2} (\bar{\mathcal D}_{a}\bar\varphi^{i}) \gamma^{a} \gamma^{bc} (\bar{\mathcal D}_{b}\psi_{ci})
\end{aligned}
\tag{RG7.1}
```

```math
\begin{aligned}
\phantom{\ell^{(2)}_{RG,7,\rm F}={}}&+\frac{g \left(L_0^{2} g - N_0\right)}{2 L_0^{2}} \bar\varphi^{i} \gamma^{a} (\bar{\mathcal D}_{a}\varphi_{i})\\
&+\frac{\sqrt{2} i g \left(L_0^{2} g - N_0\right)^{2}}{4 L_0^{3}} \delta_{ij} \bar\varphi^{i} \varphi^{j}\\
&+\frac{g \left(L_0^{2} g - 2 N_0\right) \left(L_0^{2} g - N_0\right)}{8 L_0^{2}} \bar\varphi^{i} \gamma^{a} \psi_{ai}\\
&+\frac{\sqrt{2} i g \left(L_0^{2} g - N_0\right)}{4 L_0} \delta_{ij} \bar\varphi^{i} \gamma^{ab} (\bar{\mathcal D}_{a}\psi_{b}{}^{j})
\end{aligned}
\tag{RG7.2}
```

```math
\begin{aligned}
\phantom{\ell^{(2)}_{RG,7,\rm F}={}}&- \frac{\sqrt{2} i g \left(L_0^{2} g - 2 N_0\right)}{8 L_0} \delta_{ij} \bar\psi_{a}{}^{i} \gamma^{a} \gamma^{b} (\bar{\mathcal D}_{b}\varphi^{j})\\
&- \frac{g \left(L_0^{2} g - 2 N_0\right) \left(L_0^{2} g - N_0\right)}{8 L_0^{2}} \bar\psi_{a}{}^{i} \gamma^{a} \varphi_{i}\\
&- \frac{\sqrt{2} i g \left(L_0^{2} g - 2 N_0\right)^{2}}{32 L_0} \delta_{ij} \bar\psi_{a}{}^{i} \gamma^{a} \gamma^{b} \psi_{b}{}^{j}\\
&- \frac{g \left(L_0^{2} g - 2 N_0\right)}{8} \bar\psi_{a}{}^{i} \gamma^{a} \gamma^{bc} (\bar{\mathcal D}_{b}\psi_{ci})
\end{aligned}
\tag{RG7.3}
```

```math
\begin{aligned}
\phantom{\ell^{(2)}_{RG,7,\rm F}={}}&- \frac{g}{2} (\bar{\mathcal D}_{a}\bar\psi_{b}{}^{i}) \gamma^{ab} \gamma^{c} (\bar{\mathcal D}_{c}\varphi_{i})\\
&- \frac{\sqrt{2} i g \left(L_0^{2} g - N_0\right)}{4 L_0} \delta_{ij} (\bar{\mathcal D}_{a}\bar\psi_{b}{}^{i}) \gamma^{ab} \varphi^{j}\\
&- \frac{g \left(L_0^{2} g - 2 N_0\right)}{8} (\bar{\mathcal D}_{a}\bar\psi_{b}{}^{i}) \gamma^{ab} \gamma^{c} \psi_{ci}\\
&- \frac{\sqrt{2} i L_0 g}{4} \delta_{ij} (\bar{\mathcal D}_{a}\bar\psi_{b}{}^{i}) \gamma^{ab} \gamma^{cd} (\bar{\mathcal D}_{c}\psi_{d}{}^{j})
\end{aligned}
\tag{RG7.4}
```

#### R² source group 8

Source summand: $`+\frac g4\rho'\bar\psi_a{}^i\gamma^a\lambda'{}^jL_{ij}`$. Its pure-fermion quadratic contribution is

```math
\begin{aligned}
\ell^{(2)}_{RG,8,\rm F}={}&- \frac{\sqrt{2} i N_0 g}{2 L_0} \delta_{ij} \bar\psi_{a}{}^{i} \gamma^{a} \gamma^{b} (\bar{\mathcal D}_{b}\varphi^{j})\\
&- \frac{N_0 g \left(L_0^{2} g - N_0\right)}{2 L_0^{2}} \bar\psi_{a}{}^{i} \gamma^{a} \varphi_{i}\\
&- \frac{\sqrt{2} i N_0 g \left(L_0^{2} g - 2 N_0\right)}{8 L_0} \delta_{ij} \bar\psi_{a}{}^{i} \gamma^{a} \gamma^{b} \psi_{b}{}^{j}\\
&- \frac{N_0 g}{2} \bar\psi_{a}{}^{i} \gamma^{a} \gamma^{bc} (\bar{\mathcal D}_{b}\psi_{ci})
\end{aligned}
\tag{RG8.1}
```

#### R² source group 9

Source summand: $`-\frac12\bar\psi_a{}^i\gamma^a\lambda'{}^jY'_{ij}`$. Its pure-fermion quadratic contribution is

```math
\begin{aligned}
\ell^{(2)}_{RG,9,\rm F}={}&\frac{\sqrt{2} i \left(L_0^{4} g^{2} + 4 L_0^{2} N_0 g - 40 L_0^{2} k - 4 N_0^{2}\right)}{8 L_0^{3}} \delta_{ij} \bar\psi_{a}{}^{i} \gamma^{a} \gamma^{b} (\bar{\mathcal D}_{b}\varphi^{j})\\
&+\frac{\left(L_0^{2} g - N_0\right) \left(L_0^{4} g^{2} + 4 L_0^{2} N_0 g - 40 L_0^{2} k - 4 N_0^{2}\right)}{8 L_0^{4}} \bar\psi_{a}{}^{i} \gamma^{a} \varphi_{i}\\
&+\frac{\sqrt{2} i \left(L_0^{2} g - 2 N_0\right) \left(L_0^{4} g^{2} + 4 L_0^{2} N_0 g - 40 L_0^{2} k - 4 N_0^{2}\right)}{32 L_0^{3}} \delta_{ij} \bar\psi_{a}{}^{i} \gamma^{a} \gamma^{b} \psi_{b}{}^{j}\\
&+\frac{L_0^{4} g^{2} + 4 L_0^{2} N_0 g - 40 L_0^{2} k - 4 N_0^{2}}{8 L_0^{2}} \bar\psi_{a}{}^{i} \gamma^{a} \gamma^{bc} (\bar{\mathcal D}_{b}\psi_{ci})
\end{aligned}
\tag{RG9.1}
```

#### R² source group 10

Source summand: $`-\frac{3\rho'}4\bar\lambda'{}^i\gamma^a [\frac14\gamma\!\cdot\!\widehat G\psi_{ai} -\gamma\!\cdot\!T\psi_{ai}+\frac g2L_{ij}\psi_a{}^j-\phi_{ai}]`$. Its pure-fermion quadratic contribution is

```math
\begin{aligned}
\ell^{(2)}_{RG,10,\rm F}={}&\frac{3 \sqrt{2} i N_0 g}{4 L_0} \delta_{ij} (\bar{\mathcal D}_{a}\bar\varphi^{i}) \gamma^{a} \gamma^{b} \psi_{b}{}^{j}\\
&- \frac{3 N_0 g \left(L_0^{2} g - N_0\right)}{4 L_0^{2}} \bar\varphi^{i} \gamma^{a} \psi_{ai}\\
&+\frac{3 \sqrt{2} i N_0 g \left(L_0^{2} g - 2 N_0\right)}{16 L_0} \delta_{ij} \bar\psi_{a}{}^{i} \gamma^{a} \gamma^{b} \psi_{b}{}^{j}\\
&+\frac{3 N_0 g}{4} (\bar{\mathcal D}_{a}\bar\psi_{b}{}^{i}) \gamma^{ab} \gamma^{c} \psi_{ci}
\end{aligned}
\tag{RG10.1}
```

```math
\begin{aligned}
\phantom{\ell^{(2)}_{RG,10,\rm F}={}}&+\frac{N_0}{L_0^{2}} (\bar{\mathcal D}_{a}\bar\varphi^{i}) \gamma^{a} \gamma^{b} \gamma^{c} (\bar{\mathcal D}_{b}\psi_{ci})\\
&- \frac{N_0}{L_0^{2}} (\bar{\mathcal D}_{a}\bar\varphi^{i}) \gamma^{a} \gamma^{b} \gamma^{c} (\bar{\mathcal D}_{c}\psi_{bi})\\
&- \frac{5 N_0}{8 L_0^{2}} (\bar{\mathcal D}_{a}\bar\varphi^{i}) \gamma^{a} \gamma^{bc} (\bar{\mathcal D}_{b}\psi_{ci})\\
&+\frac{5 N_0}{8 L_0^{2}} (\bar{\mathcal D}_{a}\bar\varphi^{i}) \gamma^{a} \gamma^{bc} (\bar{\mathcal D}_{c}\psi_{bi})
\end{aligned}
\tag{RG10.2}
```

```math
\begin{aligned}
\phantom{\ell^{(2)}_{RG,10,\rm F}={}}&- \frac{\sqrt{2} i N_0 \left(L_0^{2} g - N_0\right)}{2 L_0^{3}} \delta_{ij} \bar\varphi^{i} \gamma^{a} \gamma^{b} (\bar{\mathcal D}_{a}\psi_{b}{}^{j})\\
&+\frac{\sqrt{2} i N_0 \left(L_0^{2} g - N_0\right)}{2 L_0^{3}} \delta_{ij} \bar\varphi^{i} \gamma^{a} \gamma^{b} (\bar{\mathcal D}_{b}\psi_{a}{}^{j})\\
&+\frac{5 \sqrt{2} i N_0 \left(L_0^{2} g - N_0\right)}{16 L_0^{3}} \delta_{ij} \bar\varphi^{i} \gamma^{ab} (\bar{\mathcal D}_{a}\psi_{b}{}^{j})\\
&- \frac{5 \sqrt{2} i N_0 \left(L_0^{2} g - N_0\right)}{16 L_0^{3}} \delta_{ij} \bar\varphi^{i} \gamma^{ab} (\bar{\mathcal D}_{b}\psi_{a}{}^{j})
\end{aligned}
\tag{RG10.3}
```

```math
\begin{aligned}
\phantom{\ell^{(2)}_{RG,10,\rm F}={}}&+\frac{N_0 \left(L_0^{2} g - 2 N_0\right)}{4 L_0^{2}} \bar\psi_{a}{}^{i} \gamma^{a} \gamma^{b} \gamma^{c} (\bar{\mathcal D}_{b}\psi_{ci})\\
&- \frac{N_0 \left(L_0^{2} g - 2 N_0\right)}{4 L_0^{2}} \bar\psi_{a}{}^{i} \gamma^{a} \gamma^{b} \gamma^{c} (\bar{\mathcal D}_{c}\psi_{bi})\\
&- \frac{5 N_0 \left(L_0^{2} g - 2 N_0\right)}{32 L_0^{2}} \bar\psi_{a}{}^{i} \gamma^{a} \gamma^{bc} (\bar{\mathcal D}_{b}\psi_{ci})\\
&+\frac{5 N_0 \left(L_0^{2} g - 2 N_0\right)}{32 L_0^{2}} \bar\psi_{a}{}^{i} \gamma^{a} \gamma^{bc} (\bar{\mathcal D}_{c}\psi_{bi})
\end{aligned}
\tag{RG10.4}
```

```math
\begin{aligned}
\phantom{\ell^{(2)}_{RG,10,\rm F}={}}&+\frac{\sqrt{2} i N_0}{2 L_0} \delta_{ij} (\bar{\mathcal D}_{a}\bar\psi_{b}{}^{i}) \gamma^{ab} \gamma^{c} \gamma^{d} (\bar{\mathcal D}_{c}\psi_{d}{}^{j})\\
&- \frac{\sqrt{2} i N_0}{2 L_0} \delta_{ij} (\bar{\mathcal D}_{a}\bar\psi_{b}{}^{i}) \gamma^{ab} \gamma^{c} \gamma^{d} (\bar{\mathcal D}_{d}\psi_{c}{}^{j})\\
&- \frac{5 \sqrt{2} i N_0}{16 L_0} \delta_{ij} (\bar{\mathcal D}_{a}\bar\psi_{b}{}^{i}) \gamma^{ab} \gamma^{cd} (\bar{\mathcal D}_{c}\psi_{d}{}^{j})\\
&+\frac{5 \sqrt{2} i N_0}{16 L_0} \delta_{ij} (\bar{\mathcal D}_{a}\bar\psi_{b}{}^{i}) \gamma^{ab} \gamma^{cd} (\bar{\mathcal D}_{d}\psi_{c}{}^{j})
\end{aligned}
\tag{RG10.5}
```

#### R² source group 11

Source summand: $`-\frac12A'_a(\mathcal D_b\rho')\widehat G^{ab}`$. Its pure-fermion quadratic contribution is

```math
\begin{aligned}
\ell^{(2)}_{RG,11,\rm F}={}&0
\end{aligned}
\tag{RG11.1}
```

#### R² source group 12

Source summand: $`-\frac12A'_a\rho'\mathcal D_b\widehat G^{ab}`$. Its pure-fermion quadratic contribution is

```math
\begin{aligned}
\ell^{(2)}_{RG,12,\rm F}={}&0
\end{aligned}
\tag{RG12.1}
```

#### R² source group 13

Source summand: $`-\frac12A'_a\mathcal D_b\widehat F'^{ab}`$. Its pure-fermion quadratic contribution is

```math
\begin{aligned}
\ell^{(2)}_{RG,13,\rm F}={}&0
\end{aligned}
\tag{RG13.1}
```

#### R² source group 14

Source summand: $`+8A'_a(\mathcal D_b\rho')T^{ab}`$. Its pure-fermion quadratic contribution is

```math
\begin{aligned}
\ell^{(2)}_{RG,14,\rm F}={}&0
\end{aligned}
\tag{RG14.1}
```

#### R² source group 15

Source summand: $`+8A'_a\rho'\mathcal D_bT^{ab}`$. Its pure-fermion quadratic contribution is

```math
\begin{aligned}
\ell^{(2)}_{RG,15,\rm F}={}&0
\end{aligned}
\tag{RG15.1}
```

#### R² source group 16

Source summand: $`-\frac18A'_a\varepsilon^{abcde}\widehat F'_{bc}\widehat G_{de}`$. Its pure-fermion quadratic contribution is

```math
\begin{aligned}
\ell^{(2)}_{RG,16,\rm F}={}&0
\end{aligned}
\tag{RG16.1}
```

#### R² source group 17

Source summand: $`-\frac i4A'_a\bar\lambda'{}^i\gamma^{ab} [\frac14\gamma\!\cdot\!\widehat G\psi_{bi} -\gamma\!\cdot\!T\psi_{bi}+\frac g2L_{ij}\psi_b{}^j-\phi_{bi}]`$. Its pure-fermion quadratic contribution is

```math
\begin{aligned}
\ell^{(2)}_{RG,17,\rm F}={}&0
\end{aligned}
\tag{RG17.1}
```

#### R² source group 18

Source summand: $`-\frac14A'_a\rho'\bar\psi_b{}^i\gamma^{ba}\gamma^c [\frac14\gamma\!\cdot\!\widehat G\psi_{ci} -\gamma\!\cdot\!T\psi_{ci}+\frac g2L_{ij}\psi_c{}^j-\phi_{ci}]`$. Its pure-fermion quadratic contribution is

```math
\begin{aligned}
\ell^{(2)}_{RG,18,\rm F}={}&0
\end{aligned}
\tag{RG18.1}
```

#### R² source group 19

Source summand: $`-\frac14A'_a\bar\psi_b{}^i\gamma^{ba}\not{\mathcal D}\lambda'_i`$. Its pure-fermion quadratic contribution is

```math
\begin{aligned}
\ell^{(2)}_{RG,19,\rm F}={}&0
\end{aligned}
\tag{RG19.1}
```

#### R² source group 20

Source summand: $`+\frac i2A'_a\bar\psi_b{}^i\gamma^{ba}\gamma\!\cdot\!T\lambda'_i`$. Its pure-fermion quadratic contribution is

```math
\begin{aligned}
\ell^{(2)}_{RG,20,\rm F}={}&0
\end{aligned}
\tag{RG20.1}
```

#### R² source group 21

Source summand: $`-4iA'_a\rho'\bar\psi_b{}^i\gamma^{ba}\chi_i`$. Its pure-fermion quadratic contribution is

```math
\begin{aligned}
\ell^{(2)}_{RG,21,\rm F}={}&0
\end{aligned}
\tag{RG21.1}
```

#### R² source group 22

Source summand: $`-\frac i{16}A'_a\bar\psi_b{}^i\gamma^{ba}\gamma\!\cdot\!\widehat G\lambda'_i`$. Its pure-fermion quadratic contribution is

```math
\begin{aligned}
\ell^{(2)}_{RG,22,\rm F}={}&0
\end{aligned}
\tag{RG22.1}
```

#### R² source group 23

Source summand: $`+\frac{ig}8A'_a\bar\psi_b{}^i\gamma^{ba}L_{ij}\lambda'{}^j`$. Its pure-fermion quadratic contribution is

```math
\begin{aligned}
\ell^{(2)}_{RG,23,\rm F}={}&0
\end{aligned}
\tag{RG23.1}
```

#### R² source group 24

Source summand: $`-\frac g8A'_a\rho'\bar\psi_b{}^i\gamma^{abc}\psi_c{}^jL_{ij}`$. Its pure-fermion quadratic contribution is

```math
\begin{aligned}
\ell^{(2)}_{RG,24,\rm F}={}&0
\end{aligned}
\tag{RG24.1}
```

#### R² source group 25

Source summand: $`+\frac14A'_a\bar\psi_b{}^i\gamma^{abc}\psi_c{}^jY'_{ij}`$. Its pure-fermion quadratic contribution is

```math
\begin{aligned}
\ell^{(2)}_{RG,25,\rm F}={}&0
\end{aligned}
\tag{RG25.1}
```

#### R² source group 26

Source summand: $`+\frac12\rho'\Box_c\rho'`$. Its pure-fermion quadratic contribution is

```math
\begin{aligned}
\ell^{(2)}_{RG,26,\rm F}={}&\frac{\sqrt{2} i N_0}{2 L_0^{3}} \delta_{ij} (\bar{\mathcal D}_{a}\bar{\mathcal D}^{a}\bar\varphi^{i}) \varphi^{j}\\
&+\frac{\sqrt{2} i N_0}{L_0^{3}} \delta_{ij} (\bar{\mathcal D}_{a}\bar\varphi^{i}) (\bar{\mathcal D}^{a}\varphi^{j})\\
&+\frac{\sqrt{2} i N_0}{2 L_0^{3}} \delta_{ij} \bar\varphi^{i} (\bar{\mathcal D}_{a}\bar{\mathcal D}^{a}\varphi^{j})\\
&- \frac{N_0}{L_0^{2}} (\bar{\mathcal D}_{a}\bar\psi^{ai}) \gamma^{b} (\bar{\mathcal D}_{b}\varphi_{i})
\end{aligned}
\tag{RG26.1}
```

```math
\begin{aligned}
\phantom{\ell^{(2)}_{RG,26,\rm F}={}}&- \frac{2 N_0}{L_0^{2}} \bar\psi_{a}{}^{i} \gamma^{b} (\bar{\mathcal D}^{a}\bar{\mathcal D}_{b}\varphi_{i})\\
&- \frac{\sqrt{2} i N_0 \left(L_0^{2} g - N_0\right)}{2 L_0^{3}} \delta_{ij} (\bar{\mathcal D}_{a}\bar\psi^{ai}) \varphi^{j}\\
&- \frac{\sqrt{2} i N_0 \left(L_0^{2} g - N_0\right)}{L_0^{3}} \delta_{ij} \bar\psi_{a}{}^{i} (\bar{\mathcal D}^{a}\varphi^{j})\\
&- \frac{N_0 \left(4 L_0^{2} g - 5 N_0\right)}{16 L_0^{2}} (\bar{\mathcal D}_{a}\bar\psi^{ai}) \gamma^{b} \psi_{bi}
\end{aligned}
\tag{RG26.2}
```

```math
\begin{aligned}
\phantom{\ell^{(2)}_{RG,26,\rm F}={}}&- \frac{N_0 \left(24 L_0^{2} g - 23 N_0\right)}{48 L_0^{2}} \bar\psi_{a}{}^{i} \gamma^{b} (\bar{\mathcal D}^{a}\psi_{bi})\\
&- \frac{\sqrt{2} i N_0}{2 L_0} \delta_{ij} (\bar{\mathcal D}_{a}\bar\psi^{ai}) \gamma^{bc} (\bar{\mathcal D}_{b}\psi_{c}{}^{j})\\
&- \frac{\sqrt{2} i N_0}{L_0} \delta_{ij} \bar\psi_{a}{}^{i} \gamma^{bc} (\bar{\mathcal D}^{a}\bar{\mathcal D}_{b}\psi_{c}{}^{j})\\
&+\frac{\sqrt{2} i N_0 \left(L_0^{4} g^{2} + 4 L_0^{2} N_0 g - 40 L_0^{2} k - 4 N_0^{2}\right)}{16 L_0^{3}} \delta_{ij} \bar\psi_{a}{}^{i} \psi^{aj}
\end{aligned}
\tag{RG26.3}
```

```math
\begin{aligned}
\phantom{\ell^{(2)}_{RG,26,\rm F}={}}&+\frac{11 N_0^{2}}{24 L_0^{2}} \bar\psi_{a}{}^{i} \gamma^{b} (\bar{\mathcal D}_{b}\psi^{a}{}_{i})\\
&+\frac{N_0^{2}}{24 L_0^{2}} \bar\psi_{a}{}^{i} \gamma^{a} \gamma^{bc} (\bar{\mathcal D}_{b}\psi_{ci})\\
&- \frac{N_0^{2}}{24 L_0^{2}} \bar\psi_{a}{}^{i} \gamma^{a} \gamma^{bc} (\bar{\mathcal D}_{c}\psi_{bi})\\
&+\frac{N_0}{3 L_0^{2}} (\bar{\mathcal D}_{a}\bar\psi_{b}{}^{i}) \gamma^{b} \gamma^{a} \gamma^{c} (\bar{\mathcal D}_{c}\varphi_{i})
\end{aligned}
\tag{RG26.4}
```

```math
\begin{aligned}
\phantom{\ell^{(2)}_{RG,26,\rm F}={}}&+\frac{\sqrt{2} i N_0 \left(L_0^{2} g - N_0\right)}{6 L_0^{3}} \delta_{ij} (\bar{\mathcal D}_{a}\bar\psi_{b}{}^{i}) \gamma^{b} \gamma^{a} \varphi^{j}\\
&+\frac{N_0 \left(L_0^{2} g - 2 N_0\right)}{12 L_0^{2}} (\bar{\mathcal D}_{a}\bar\psi_{b}{}^{i}) \gamma^{b} \gamma^{a} \gamma^{c} \psi_{ci}\\
&+\frac{\sqrt{2} i N_0}{6 L_0} \delta_{ij} (\bar{\mathcal D}_{a}\bar\psi_{b}{}^{i}) \gamma^{b} \gamma^{a} \gamma^{cd} (\bar{\mathcal D}_{c}\psi_{d}{}^{j})\\
&- \frac{N_0}{3 L_0^{2}} (\bar{\mathcal D}_{a}\bar\psi_{b}{}^{i}) \gamma^{a} \gamma^{b} \gamma^{c} (\bar{\mathcal D}_{c}\varphi_{i})
\end{aligned}
\tag{RG26.5}
```

```math
\begin{aligned}
\phantom{\ell^{(2)}_{RG,26,\rm F}={}}&- \frac{\sqrt{2} i N_0 \left(L_0^{2} g - N_0\right)}{6 L_0^{3}} \delta_{ij} (\bar{\mathcal D}_{a}\bar\psi_{b}{}^{i}) \gamma^{a} \gamma^{b} \varphi^{j}\\
&- \frac{N_0 \left(L_0^{2} g - 2 N_0\right)}{12 L_0^{2}} (\bar{\mathcal D}_{a}\bar\psi_{b}{}^{i}) \gamma^{a} \gamma^{b} \gamma^{c} \psi_{ci}\\
&- \frac{\sqrt{2} i N_0}{6 L_0} \delta_{ij} (\bar{\mathcal D}_{a}\bar\psi_{b}{}^{i}) \gamma^{a} \gamma^{b} \gamma^{cd} (\bar{\mathcal D}_{c}\psi_{d}{}^{j})\\
&+\frac{5 N_0}{12 L_0^{2}} (\bar{\mathcal D}_{a}\bar\psi_{b}{}^{i}) \gamma^{ab} \gamma^{c} (\bar{\mathcal D}_{c}\varphi_{i})
\end{aligned}
\tag{RG26.6}
```

```math
\begin{aligned}
\phantom{\ell^{(2)}_{RG,26,\rm F}={}}&+\frac{5 \sqrt{2} i N_0 \left(L_0^{2} g - N_0\right)}{24 L_0^{3}} \delta_{ij} (\bar{\mathcal D}_{a}\bar\psi_{b}{}^{i}) \gamma^{ab} \varphi^{j}\\
&+\frac{N_0 \left(5 L_0^{2} g - 6 N_0\right)}{48 L_0^{2}} (\bar{\mathcal D}_{a}\bar\psi_{b}{}^{i}) \gamma^{ab} \gamma^{c} \psi_{ci}\\
&+\frac{5 \sqrt{2} i N_0}{24 L_0} \delta_{ij} (\bar{\mathcal D}_{a}\bar\psi_{b}{}^{i}) \gamma^{ab} \gamma^{cd} (\bar{\mathcal D}_{c}\psi_{d}{}^{j})\\
&- \frac{5 \sqrt{2} i N_0 k}{2 L_0^{3}} \delta_{ij} \bar\varphi^{i} \varphi^{j}
\end{aligned}
\tag{RG26.7}
```

```math
\begin{aligned}
\phantom{\ell^{(2)}_{RG,26,\rm F}={}}&+\frac{N_0^{2}}{8 L_0^{2}} (\bar{\mathcal D}_{a}\bar\psi_{b}{}^{i}) \gamma^{a} \psi^{b}{}_{i}\\
&+\frac{N_0^{2}}{16 L_0^{2}} (\bar{\mathcal D}_{a}\bar\psi_{b}{}^{i}) \gamma^{b} \psi^{a}{}_{i}\\
&+\frac{N_0^{2}}{16 L_0^{2}} \bar\psi_{a}{}^{i} \gamma^{a} (\bar{\mathcal D}_{b}\psi^{b}{}_{i})\\
&+\frac{N_0^{2}}{12 L_0^{2}} (\bar{\mathcal D}_{a}\bar\psi_{b}{}^{i}) \gamma^{b} \gamma^{ac} \psi_{ci}
\end{aligned}
\tag{RG26.8}
```

```math
\begin{aligned}
\phantom{\ell^{(2)}_{RG,26,\rm F}={}}&- \frac{N_0^{2}}{12 L_0^{2}} (\bar{\mathcal D}_{a}\bar\psi_{b}{}^{i}) \gamma^{a} \gamma^{bc} \psi_{ci}
\end{aligned}
\tag{RG26.9}
```

#### R² source group 27

Source summand: $`+(\rho')^2 f_a{}^a`$. Its pure-fermion quadratic contribution is

```math
\begin{aligned}
\ell^{(2)}_{RG,27,\rm F}={}&- \frac{3 N_0^{2}}{16 L_0^{2}} (\bar{\mathcal D}_{a}\bar\psi^{ai}) \gamma^{b} \psi_{bi}\\
&- \frac{3 N_0^{2}}{16 L_0^{2}} \bar\psi_{a}{}^{i} \gamma^{b} (\bar{\mathcal D}^{a}\psi_{bi})\\
&+\frac{N_0^{2}}{8 L_0^{2}} (\bar{\mathcal D}_{a}\bar\psi_{b}{}^{i}) \gamma^{a} \psi^{b}{}_{i}\\
&+\frac{N_0^{2}}{8 L_0^{2}} \bar\psi_{a}{}^{i} \gamma^{b} (\bar{\mathcal D}_{b}\psi^{a}{}_{i})
\end{aligned}
\tag{RG27.1}
```

```math
\begin{aligned}
\phantom{\ell^{(2)}_{RG,27,\rm F}={}}&+\frac{N_0^{2}}{16 L_0^{2}} (\bar{\mathcal D}_{a}\bar\psi_{b}{}^{i}) \gamma^{b} \psi^{a}{}_{i}\\
&+\frac{N_0^{2}}{16 L_0^{2}} \bar\psi_{a}{}^{i} \gamma^{a} (\bar{\mathcal D}_{b}\psi^{b}{}_{i})\\
&+\frac{N_0^{2}}{12 L_0^{2}} (\bar{\mathcal D}_{a}\bar\psi_{b}{}^{i}) \gamma^{b} \gamma^{ac} \psi_{ci}\\
&- \frac{N_0^{2}}{12 L_0^{2}} (\bar{\mathcal D}_{a}\bar\psi_{b}{}^{i}) \gamma^{a} \gamma^{bc} \psi_{ci}
\end{aligned}
\tag{RG27.2}
```

```math
\begin{aligned}
\phantom{\ell^{(2)}_{RG,27,\rm F}={}}&+\frac{N_0^{2}}{12 L_0^{2}} (\bar{\mathcal D}_{a}\bar\psi_{b}{}^{i}) \gamma^{ab} \gamma^{c} \psi_{ci}\\
&+\frac{\sqrt{2} i N_0^{2} g}{8 L_0} \delta_{ij} \bar\psi_{a}{}^{i} \gamma^{a} \gamma^{b} \psi_{b}{}^{j}\\
&+\frac{N_0^{2}}{6 L_0^{2}} \bar\psi_{a}{}^{i} \gamma^{a} \gamma^{b} \gamma^{c} (\bar{\mathcal D}_{b}\psi_{ci})\\
&- \frac{N_0^{2}}{6 L_0^{2}} \bar\psi_{a}{}^{i} \gamma^{a} \gamma^{b} \gamma^{c} (\bar{\mathcal D}_{c}\psi_{bi})
\end{aligned}
\tag{RG27.3}
```

```math
\begin{aligned}
\phantom{\ell^{(2)}_{RG,27,\rm F}={}}&- \frac{5 N_0^{2}}{48 L_0^{2}} \bar\psi_{a}{}^{i} \gamma^{a} \gamma^{bc} (\bar{\mathcal D}_{b}\psi_{ci})\\
&+\frac{5 N_0^{2}}{48 L_0^{2}} \bar\psi_{a}{}^{i} \gamma^{a} \gamma^{bc} (\bar{\mathcal D}_{c}\psi_{bi})\\
&+\frac{N_0^{2} g}{2 L_0^{2}} \bar\psi_{a}{}^{i} \gamma^{a} \varphi_{i}\\
&- \frac{5 \sqrt{2} i N_0 k}{2 L_0^{3}} \delta_{ij} \bar\varphi^{i} \varphi^{j}
\end{aligned}
\tag{RG27.4}
```

#### R² source group 28

Source summand: $`-\frac14\rho'\widehat F'_{ab}\widehat G^{ab}`$. Its pure-fermion quadratic contribution is

```math
\begin{aligned}
\ell^{(2)}_{RG,28,\rm F}={}&0
\end{aligned}
\tag{RG28.1}
```

#### R² source group 29

Source summand: $`+4(\rho')^2\widehat G_{ab}T^{ab}`$. Its pure-fermion quadratic contribution is

```math
\begin{aligned}
\ell^{(2)}_{RG,29,\rm F}={}&0
\end{aligned}
\tag{RG29.1}
```

#### R² source group 30

Source summand: $`+4\rho'\widehat F'_{ab}T^{ab}`$. Its pure-fermion quadratic contribution is

```math
\begin{aligned}
\ell^{(2)}_{RG,30,\rm F}={}&0
\end{aligned}
\tag{RG30.1}
```

#### R² source group 31

Source summand: $`-4(\rho')^2D`$. Its pure-fermion quadratic contribution is

```math
\begin{aligned}
\ell^{(2)}_{RG,31,\rm F}={}&\frac{3 N_0^{2}}{8 L_0^{2}} (\bar{\mathcal D}_{a}\bar\psi^{ai}) \gamma^{b} \psi_{bi}\\
&+\frac{25 N_0^{2}}{24 L_0^{2}} \bar\psi_{a}{}^{i} \gamma^{b} (\bar{\mathcal D}^{a}\psi_{bi})\\
&- \frac{N_0^{2}}{4 L_0^{2}} (\bar{\mathcal D}_{a}\bar\psi_{b}{}^{i}) \gamma^{a} \psi^{b}{}_{i}\\
&- \frac{11 N_0^{2}}{12 L_0^{2}} \bar\psi_{a}{}^{i} \gamma^{b} (\bar{\mathcal D}_{b}\psi^{a}{}_{i})
\end{aligned}
\tag{RG31.1}
```

```math
\begin{aligned}
\phantom{\ell^{(2)}_{RG,31,\rm F}={}}&- \frac{N_0^{2}}{8 L_0^{2}} (\bar{\mathcal D}_{a}\bar\psi_{b}{}^{i}) \gamma^{b} \psi^{a}{}_{i}\\
&- \frac{N_0^{2}}{8 L_0^{2}} \bar\psi_{a}{}^{i} \gamma^{a} (\bar{\mathcal D}_{b}\psi^{b}{}_{i})\\
&- \frac{N_0^{2}}{6 L_0^{2}} (\bar{\mathcal D}_{a}\bar\psi_{b}{}^{i}) \gamma^{b} \gamma^{ac} \psi_{ci}\\
&+\frac{N_0^{2}}{6 L_0^{2}} (\bar{\mathcal D}_{a}\bar\psi_{b}{}^{i}) \gamma^{a} \gamma^{bc} \psi_{ci}
\end{aligned}
\tag{RG31.2}
```

```math
\begin{aligned}
\phantom{\ell^{(2)}_{RG,31,\rm F}={}}&- \frac{N_0^{2}}{6 L_0^{2}} (\bar{\mathcal D}_{a}\bar\psi_{b}{}^{i}) \gamma^{ab} \gamma^{c} \psi_{ci}\\
&- \frac{N_0^{2}}{12 L_0^{2}} \bar\psi_{a}{}^{i} \gamma^{a} \gamma^{bc} (\bar{\mathcal D}_{b}\psi_{ci})\\
&+\frac{N_0^{2}}{12 L_0^{2}} \bar\psi_{a}{}^{i} \gamma^{a} \gamma^{bc} (\bar{\mathcal D}_{c}\psi_{bi})\\
&+\frac{\sqrt{2} i N_0^{2} g}{2 L_0} \delta_{ij} \bar\psi_{a}{}^{i} \psi^{aj}
\end{aligned}
\tag{RG31.3}
```

```math
\begin{aligned}
\phantom{\ell^{(2)}_{RG,31,\rm F}={}}&- \frac{\sqrt{2} i N_0 \left(L_0^{2} g^{2} + 4 N_0 g - 10 k\right)}{2 L_0^{3}} \delta_{ij} \bar\varphi^{i} \varphi^{j}
\end{aligned}
\tag{RG31.4}
```

#### R² source group 32

Source summand: $`-\frac{104}{3}(\rho')^2T^2`$. Its pure-fermion quadratic contribution is

```math
\begin{aligned}
\ell^{(2)}_{RG,32,\rm F}={}&0
\end{aligned}
\tag{RG32.1}
```

#### R² source group 33

Source summand: $`+8i\rho'\bar\chi\lambda'`$. Its pure-fermion quadratic contribution is

```math
\begin{aligned}
\ell^{(2)}_{RG,33,\rm F}={}&- \frac{\sqrt{2} i N_0 g}{L_0} \delta_{ij} \bar\psi_{a}{}^{i} \gamma^{a} \gamma^{b} (\bar{\mathcal D}_{b}\varphi^{j})\\
&- \frac{N_0 g \left(L_0^{2} g - N_0\right)}{L_0^{2}} \bar\psi_{a}{}^{i} \gamma^{a} \varphi_{i}\\
&- \frac{\sqrt{2} i N_0 g \left(L_0^{2} g - 2 N_0\right)}{4 L_0} \delta_{ij} \bar\psi_{a}{}^{i} \gamma^{a} \gamma^{b} \psi_{b}{}^{j}\\
&- N_0 g \bar\psi_{a}{}^{i} \gamma^{a} \gamma^{bc} (\bar{\mathcal D}_{b}\psi_{ci})
\end{aligned}
\tag{RG33.1}
```

```math
\begin{aligned}
\phantom{\ell^{(2)}_{RG,33,\rm F}={}}&+\frac{4 N_0}{3 L_0^{2}} (\bar{\mathcal D}_{a}\bar\psi_{b}{}^{i}) \gamma^{b} \gamma^{a} \gamma^{c} (\bar{\mathcal D}_{c}\varphi_{i})\\
&+\frac{2 \sqrt{2} i N_0 \left(L_0^{2} g - N_0\right)}{3 L_0^{3}} \delta_{ij} (\bar{\mathcal D}_{a}\bar\psi_{b}{}^{i}) \gamma^{b} \gamma^{a} \varphi^{j}\\
&+\frac{N_0 \left(L_0^{2} g - 2 N_0\right)}{3 L_0^{2}} (\bar{\mathcal D}_{a}\bar\psi_{b}{}^{i}) \gamma^{b} \gamma^{a} \gamma^{c} \psi_{ci}\\
&+\frac{2 \sqrt{2} i N_0}{3 L_0} \delta_{ij} (\bar{\mathcal D}_{a}\bar\psi_{b}{}^{i}) \gamma^{b} \gamma^{a} \gamma^{cd} (\bar{\mathcal D}_{c}\psi_{d}{}^{j})
\end{aligned}
\tag{RG33.2}
```

```math
\begin{aligned}
\phantom{\ell^{(2)}_{RG,33,\rm F}={}}&- \frac{4 N_0}{3 L_0^{2}} (\bar{\mathcal D}_{a}\bar\psi_{b}{}^{i}) \gamma^{a} \gamma^{b} \gamma^{c} (\bar{\mathcal D}_{c}\varphi_{i})\\
&- \frac{2 \sqrt{2} i N_0 \left(L_0^{2} g - N_0\right)}{3 L_0^{3}} \delta_{ij} (\bar{\mathcal D}_{a}\bar\psi_{b}{}^{i}) \gamma^{a} \gamma^{b} \varphi^{j}\\
&- \frac{N_0 \left(L_0^{2} g - 2 N_0\right)}{3 L_0^{2}} (\bar{\mathcal D}_{a}\bar\psi_{b}{}^{i}) \gamma^{a} \gamma^{b} \gamma^{c} \psi_{ci}\\
&- \frac{2 \sqrt{2} i N_0}{3 L_0} \delta_{ij} (\bar{\mathcal D}_{a}\bar\psi_{b}{}^{i}) \gamma^{a} \gamma^{b} \gamma^{cd} (\bar{\mathcal D}_{c}\psi_{d}{}^{j})
\end{aligned}
\tag{RG33.3}
```

```math
\begin{aligned}
\phantom{\ell^{(2)}_{RG,33,\rm F}={}}&+\frac{5 N_0}{3 L_0^{2}} (\bar{\mathcal D}_{a}\bar\psi_{b}{}^{i}) \gamma^{ab} \gamma^{c} (\bar{\mathcal D}_{c}\varphi_{i})\\
&+\frac{5 \sqrt{2} i N_0 \left(L_0^{2} g - N_0\right)}{6 L_0^{3}} \delta_{ij} (\bar{\mathcal D}_{a}\bar\psi_{b}{}^{i}) \gamma^{ab} \varphi^{j}\\
&+\frac{5 N_0 \left(L_0^{2} g - 2 N_0\right)}{12 L_0^{2}} (\bar{\mathcal D}_{a}\bar\psi_{b}{}^{i}) \gamma^{ab} \gamma^{c} \psi_{ci}\\
&+\frac{5 \sqrt{2} i N_0}{6 L_0} \delta_{ij} (\bar{\mathcal D}_{a}\bar\psi_{b}{}^{i}) \gamma^{ab} \gamma^{cd} (\bar{\mathcal D}_{c}\psi_{d}{}^{j})
\end{aligned}
\tag{RG33.4}
```

```math
\begin{aligned}
\phantom{\ell^{(2)}_{RG,33,\rm F}={}}&+\frac{4 N_0 g}{L_0^{2}} \bar\varphi^{i} \gamma^{a} (\bar{\mathcal D}_{a}\varphi_{i})\\
&+\frac{2 \sqrt{2} i N_0 g \left(L_0^{2} g - N_0\right)}{L_0^{3}} \delta_{ij} \bar\varphi^{i} \varphi^{j}\\
&+\frac{N_0 g \left(L_0^{2} g - 2 N_0\right)}{L_0^{2}} \bar\varphi^{i} \gamma^{a} \psi_{ai}\\
&+\frac{2 \sqrt{2} i N_0 g}{L_0} \delta_{ij} \bar\varphi^{i} \gamma^{ab} (\bar{\mathcal D}_{a}\psi_{b}{}^{j})
\end{aligned}
\tag{RG33.5}
```

#### R² source group 34

Source summand: $`-5(\rho')^2\bar\psi_a{}^i\gamma^a\chi_i`$. Its pure-fermion quadratic contribution is

```math
\begin{aligned}
\ell^{(2)}_{RG,34,\rm F}={}&- \frac{5 \sqrt{2} i N_0^{2} g}{8 L_0} \delta_{ij} \bar\psi_{a}{}^{i} \gamma^{a} \gamma^{b} \psi_{b}{}^{j}\\
&- \frac{5 N_0^{2}}{6 L_0^{2}} \bar\psi_{a}{}^{i} \gamma^{a} \gamma^{b} \gamma^{c} (\bar{\mathcal D}_{b}\psi_{ci})\\
&+\frac{5 N_0^{2}}{6 L_0^{2}} \bar\psi_{a}{}^{i} \gamma^{a} \gamma^{b} \gamma^{c} (\bar{\mathcal D}_{c}\psi_{bi})\\
&+\frac{25 N_0^{2}}{48 L_0^{2}} \bar\psi_{a}{}^{i} \gamma^{a} \gamma^{bc} (\bar{\mathcal D}_{b}\psi_{ci})
\end{aligned}
\tag{RG34.1}
```

```math
\begin{aligned}
\phantom{\ell^{(2)}_{RG,34,\rm F}={}}&- \frac{25 N_0^{2}}{48 L_0^{2}} \bar\psi_{a}{}^{i} \gamma^{a} \gamma^{bc} (\bar{\mathcal D}_{c}\psi_{bi})\\
&- \frac{5 N_0^{2} g}{2 L_0^{2}} \bar\psi_{a}{}^{i} \gamma^{a} \varphi_{i}
\end{aligned}
\tag{RG34.2}
```

#### R² source group 35

Source summand: $`+\frac i4\rho'\bar\psi_a{}^i\gamma^a\not{\mathcal D}\lambda'_i`$. Its pure-fermion quadratic contribution is

```math
\begin{aligned}
\ell^{(2)}_{RG,35,\rm F}={}&\frac{N_0}{L_0^{2}} \bar\psi_{a}{}^{i} \gamma^{a} \gamma^{b} \gamma^{c} (\bar{\mathcal D}_{b}\bar{\mathcal D}_{c}\varphi_{i})\\
&+\frac{\sqrt{2} i N_0 \left(L_0^{2} g - N_0\right)}{2 L_0^{3}} \delta_{ij} \bar\psi_{a}{}^{i} \gamma^{a} \gamma^{b} (\bar{\mathcal D}_{b}\varphi^{j})\\
&+\frac{N_0 \left(3 L_0^{2} g - 2 N_0\right)}{12 L_0^{2}} \bar\psi_{a}{}^{i} \gamma^{a} \gamma^{b} \gamma^{c} (\bar{\mathcal D}_{b}\psi_{ci})\\
&+\frac{\sqrt{2} i N_0}{2 L_0} \delta_{ij} \bar\psi_{a}{}^{i} \gamma^{a} \gamma^{b} \gamma^{cd} (\bar{\mathcal D}_{b}\bar{\mathcal D}_{c}\psi_{d}{}^{j})
\end{aligned}
\tag{RG35.1}
```

```math
\begin{aligned}
\phantom{\ell^{(2)}_{RG,35,\rm F}={}}&- \frac{\sqrt{2} i N_0 \left(L_0^{4} g^{2} + 4 L_0^{2} N_0 g - 40 L_0^{2} k - 4 N_0^{2}\right)}{16 L_0^{3}} \delta_{ij} \bar\psi_{a}{}^{i} \gamma^{a} \gamma^{b} \psi_{b}{}^{j}\\
&- \frac{N_0^{2}}{3 L_0^{2}} \bar\psi_{a}{}^{i} \gamma^{a} \gamma^{b} \gamma^{c} (\bar{\mathcal D}_{c}\psi_{bi})\\
&- \frac{5 N_0^{2}}{24 L_0^{2}} \bar\psi_{a}{}^{i} \gamma^{a} \gamma^{bc} (\bar{\mathcal D}_{b}\psi_{ci})\\
&+\frac{5 N_0^{2}}{24 L_0^{2}} \bar\psi_{a}{}^{i} \gamma^{a} \gamma^{bc} (\bar{\mathcal D}_{c}\psi_{bi})
\end{aligned}
\tag{RG35.2}
```

#### R² source group 36

Source summand: $`+\frac12\rho'\bar\psi_a{}^i\gamma^a\gamma\!\cdot\!T\lambda'_i`$. Its pure-fermion quadratic contribution is

```math
\begin{aligned}
\ell^{(2)}_{RG,36,\rm F}={}&0
\end{aligned}
\tag{RG36.1}
```

#### R² source group 37

Source summand: $`-\frac1{16}\rho'\bar\psi_a{}^i\gamma^a\gamma\!\cdot\!\widehat G\lambda'_i`$. Its pure-fermion quadratic contribution is

```math
\begin{aligned}
\ell^{(2)}_{RG,37,\rm F}={}&0
\end{aligned}
\tag{RG37.1}
```

#### R² source group 38

Source summand: $`+\frac g8\rho'\bar\psi_a{}^i\gamma^aL_{ij}\lambda'{}^j`$. Its pure-fermion quadratic contribution is

```math
\begin{aligned}
\ell^{(2)}_{RG,38,\rm F}={}&- \frac{\sqrt{2} i N_0 g}{4 L_0} \delta_{ij} \bar\psi_{a}{}^{i} \gamma^{a} \gamma^{b} (\bar{\mathcal D}_{b}\varphi^{j})\\
&- \frac{N_0 g \left(L_0^{2} g - N_0\right)}{4 L_0^{2}} \bar\psi_{a}{}^{i} \gamma^{a} \varphi_{i}\\
&- \frac{\sqrt{2} i N_0 g \left(L_0^{2} g - 2 N_0\right)}{16 L_0} \delta_{ij} \bar\psi_{a}{}^{i} \gamma^{a} \gamma^{b} \psi_{b}{}^{j}\\
&- \frac{N_0 g}{4} \bar\psi_{a}{}^{i} \gamma^{a} \gamma^{bc} (\bar{\mathcal D}_{b}\psi_{ci})
\end{aligned}
\tag{RG38.1}
```

#### R² source group 39

Source summand: $`+\frac i4(\rho')^2\bar\psi_a{}^i\gamma^a\gamma^b [\frac14\gamma\!\cdot\!\widehat G\psi_{bi} -\gamma\!\cdot\!T\psi_{bi}+\frac g2L_{ij}\psi_b{}^j-\phi_{bi}]`$. Its pure-fermion quadratic contribution is

```math
\begin{aligned}
\ell^{(2)}_{RG,39,\rm F}={}&\frac{\sqrt{2} i N_0^{2} g}{4 L_0} \delta_{ij} \bar\psi_{a}{}^{i} \gamma^{a} \gamma^{b} \psi_{b}{}^{j}\\
&+\frac{N_0^{2}}{3 L_0^{2}} \bar\psi_{a}{}^{i} \gamma^{a} \gamma^{b} \gamma^{c} (\bar{\mathcal D}_{b}\psi_{ci})\\
&- \frac{N_0^{2}}{3 L_0^{2}} \bar\psi_{a}{}^{i} \gamma^{a} \gamma^{b} \gamma^{c} (\bar{\mathcal D}_{c}\psi_{bi})\\
&- \frac{5 N_0^{2}}{24 L_0^{2}} \bar\psi_{a}{}^{i} \gamma^{a} \gamma^{bc} (\bar{\mathcal D}_{b}\psi_{ci})
\end{aligned}
\tag{RG39.1}
```

```math
\begin{aligned}
\phantom{\ell^{(2)}_{RG,39,\rm F}={}}&+\frac{5 N_0^{2}}{24 L_0^{2}} \bar\psi_{a}{}^{i} \gamma^{a} \gamma^{bc} (\bar{\mathcal D}_{c}\psi_{bi})
\end{aligned}
\tag{RG39.2}
```

#### R² source group 40

Source summand: $`-\frac i4(\rho')^2\bar\psi_a{}^i [\frac14\gamma\!\cdot\!\widehat G\psi^a_i -\gamma\!\cdot\!T\psi^a_i+\frac g2L_{ij}\psi^{aj}-\phi^a_i]`$. Its pure-fermion quadratic contribution is

```math
\begin{aligned}
\ell^{(2)}_{RG,40,\rm F}={}&- \frac{\sqrt{2} i N_0^{2} g}{4 L_0} \delta_{ij} \bar\psi_{a}{}^{i} \psi^{aj}\\
&- \frac{N_0^{2}}{3 L_0^{2}} \bar\psi_{a}{}^{i} \gamma^{b} (\bar{\mathcal D}^{a}\psi_{bi})\\
&+\frac{N_0^{2}}{3 L_0^{2}} \bar\psi_{a}{}^{i} \gamma^{b} (\bar{\mathcal D}_{b}\psi^{a}{}_{i})\\
&+\frac{N_0^{2}}{24 L_0^{2}} \bar\psi_{a}{}^{i} \gamma^{a} \gamma^{bc} (\bar{\mathcal D}_{b}\psi_{ci})
\end{aligned}
\tag{RG40.1}
```

```math
\begin{aligned}
\phantom{\ell^{(2)}_{RG,40,\rm F}={}}&- \frac{N_0^{2}}{24 L_0^{2}} \bar\psi_{a}{}^{i} \gamma^{a} \gamma^{bc} (\bar{\mathcal D}_{c}\psi_{bi})
\end{aligned}
\tag{RG40.2}
```

#### R² source group 41

Source summand: $`-\frac{ig}8(\rho')^2\bar\psi_a{}^i\gamma^{ab}\psi_b{}^jL_{ij}`$. Its pure-fermion quadratic contribution is

```math
\begin{aligned}
\ell^{(2)}_{RG,41,\rm F}={}&- \frac{\sqrt{2} i N_0^{2} g}{4 L_0} \delta_{ij} \bar\psi_{a}{}^{i} \gamma^{ab} \psi_{b}{}^{j}
\end{aligned}
\tag{RG41.1}
```

#### R² source group 42

Source summand: $`+\frac i4\rho'\bar\psi_a{}^i\gamma^{ab}\psi_b{}^jY'_{ij}`$. Its pure-fermion quadratic contribution is

```math
\begin{aligned}
\ell^{(2)}_{RG,42,\rm F}={}&\frac{\sqrt{2} i N_0 \left(L_0^{4} g^{2} + 4 L_0^{2} N_0 g - 40 L_0^{2} k - 4 N_0^{2}\right)}{16 L_0^{3}} \delta_{ij} \bar\psi_{a}{}^{i} \gamma^{ab} \psi_{b}{}^{j}
\end{aligned}
\tag{RG42.1}
```

For a vanishing pure-fermion group the table states its source expression and the zero result. Such a zero follows from at least one vanishing even background factor ($`A'_0,T_0,G_0,F'_0`$ or an ordinary background derivative), combined with the displayed two odd slots; its bosonic second-order contribution, if any, is already in Sections 4.1–4.4. This does not delete those groups from the nonlinear action.

### 4.7 Multiply the volume and identify the first-order tadpoles

If the scalar density before the measure is $`q_0+\epsilon q_1+\epsilon^2q_2`$, multiplication by (3.5) gives, term by term,

```math
\ell^{(0)}=q_0,\qquad
\ell^{(1)}=q_1+\tfrac h2q_0,\qquad
\ell^{(2)}=q_2+\tfrac h2q_1
+\left(\tfrac18h^2-\tfrac14h_{\mu\nu}h^{\mu\nu}\right)q_0.
\tag{4.40}
```

For this action $`q_0=F_0`$ and $`q_1=F_RR^{(1)}+F_L\delta L+F_N\delta N+b_0\bar\Box\delta L`$. Pure-fermion bilinears and strength products first occur in $`q_2`$, so their measure is only $`\bar e`$ at this order.

Use $`R^{(1)}=\bar{\mathcal D}_\mu(\bar{\mathcal D}_\nu h^{\mu\nu}-\bar{\mathcal D}^\mu h)-4kh`$. Since $`F_R`$ and $`b_0`$ are constant background coefficients,

```math
\begin{aligned}
\ell^{(1)}={}&\left(\tfrac12F_0-4kF_R\right)h+F_L\delta L+F_N\delta N\\
&+\bar{\mathcal D}_\mu\left[F_R(\bar{\mathcal D}_\nu h^{\mu\nu}-\bar{\mathcal D}^\mu h)
+b_0\bar{\mathcal D}^\mu\delta L\right].
\end{aligned}
\tag{4.41}
```

The three bulk coefficients, with no imposed background equation, are explicitly

```math
\tfrac12F_0-4kF_R=- \frac{L_0^{3} g^{2}}{4} + L_0^{2} g^{2} - L_0 N_0 g + 6 L_0 k - 2 N_0 g + \lambda \left(\frac{L_0^{4} g^{4}}{32} - \frac{3 L_0^{2} g^{2} k}{2} - \frac{5 N_0^{2} g^{2}}{4} + 10 k^{2} - \frac{2 N_0^{3} g}{L_0^{2}} + \frac{6 N_0^{2} k}{L_0^{2}} + \frac{N_0^{4}}{2 L_0^{4}}\right) - \frac{N_0^{2}}{L_0}
\tag{TAD.h}
```

```math
F_L=- \frac{3 L_0^{2} g^{2}}{2} + 4 L_0 g^{2} - 2 N_0 g + 20 k + \lambda \left(\frac{L_0^{3} g^{4}}{4} - 10 L_0 g^{2} k + \frac{8 N_0^{3} g}{L_0^{3}} - \frac{40 N_0^{2} k}{L_0^{3}} - \frac{4 N_0^{4}}{L_0^{5}}\right) + \frac{2 N_0^{2}}{L_0^{2}}
\tag{TAD.L}
```

```math
F_N=- 2 L_0 g - 4 g + \lambda \left(- 5 N_0 g^{2} - \frac{12 N_0^{2} g}{L_0^{2}} + \frac{40 N_0 k}{L_0^{2}} + \frac{4 N_0^{3}}{L_0^{4}}\right) - \frac{4 N_0}{L_0}
\tag{TAD.N}
```

There is no first-order form, connection or fermion term because each such term contains at least two amplitudes and all corresponding background fields vanish. The nonzero scalar and metric coefficients are retained in the endpoint.

### 4.8 Boundary representative

Our elementary source and the bosonic expressions used in this revision differ only by the explicit potential and scalar-kinetic integrations by parts performed in (OS.7), (OS.8) and (OS.10). Their currents follow from

```math
\begin{aligned}
-\tfrac12A'_a\mathcal D_b^{\rm B}X^{ab}
&=-\tfrac14F'_{ab}X^{ab}-\tfrac12\mathcal D_b^{\rm B}(A'_aX^{ab}),\\
2\frac NL\Box\frac NL
&=-2\partial_a(N/L)\partial^a(N/L)
+2\mathcal D_a^{\rm B}\left[(N/L)\partial^a(N/L)\right],\\
\mathcal D_a^{\rm B}(L\partial^aL)
&=L\Box L+(\partial L)^2.
\end{aligned}
\tag{4.42}
```

where $`X^{ab}=F'^{ab}+\rho'(G^{ab}-16T^{ab})`$ in the bosonic restriction. In the first equality $`(\mathcal D_bA'_a)X^{ab}=-F'_{ab}X^{ab}/2`$, with the sign fixed by antisymmetry of $`X^{ab}`$. The bosonic source density minus (4.2) is $`\mathcal D_b^{\rm B}J^b_{\rm B}`$ with

```math
J^b_{\rm B}=-\tfrac12A'_a\left[F'^{ab}+\frac{2N}{L}(-G^{ab}+4H^{ab})\right]
+2\frac NL\partial^b\frac NL,
\tag{4.43}
```

The Chern–Simons term is unchanged in this conversion and starts at cubic order here. The current (4.43) has zero background value.

For completeness the bosonic two-derivative BF-to-(4.1) conversion has its own current. In the bosonic restriction define the existing two-form representative by $`E^{ab}=-\varepsilon^{abcde}E_{cde}/12`$, so $`\mathcal D_b^{\rm B}E^{ab}=E^a`$. The antisymmetry gives $`\mathcal D_a^{\rm B}E^{ab}=-E^b`$. Consequently, for $`A^{\rm eff}_a=2E_a/L+\sqrt2V_a+2gC_a`$,

```math
\begin{aligned}
-E^{ab}F^{\rm eff}_{ab}
&=-2E^aA^{\rm eff}_a-2\mathcal D_a^{\rm B}(E^{ab}A^{\rm eff}_b),\\
J^a_{2\partial,\rm B}
&=-2E^{ab}\left(\frac{2E_b}{L}+\sqrt2V_b+2gC_b\right).
\end{aligned}
\tag{4.44}
```

The change in $`S^{(n)}`$ between the raw bosonic BF representatives and those used here is $`\int d^5x\,\partial_a[e(J^a_{2\partial,\rm B}+\lambda J^a_{\rm B})]^{(n)}`$, for $`n=1,2`$. The sign follows directly from the first line of (4.44); no independent unconstrained two-form has been added. Within the final quadratic fermion densities no integration by parts is performed: their differentiated-bar terms, including contorsion divergences, are retained. All equalities between integrated source representatives are understood with these currents or with the compact-support condition of Section 1.2.

## 5. Consistency Checks

The component insertion check passes **184/184** exact algebra, index and dimension checks of the stated component insertion. The independent bosonic, determinant and limiting-case check passes **50/50** checks. The independent Clifford/Majorana/Grassmann check passes **120/120** checks, with maximum scaled residual $`3.66e-16`$.

The independent bosonic check reads the coefficients of our own source groups and directly inserts our $`\rho',Y',T,D,f,\Box_c`$ definitions in those products. It also inserts our earlier effective slots into our two-derivative full density (OS.1). It expands the rational factors in $`L_0+\epsilon\delta L`$, $`N_0+\epsilon\delta N`$ and multiplies the volume, then compares with the separately assembled coefficients in Sections 4.3–4.4 and 4.7. Its output stores the three coefficients separately for every surviving bosonic source group. Distinct derivative and strength contractions are independent probes; Gold's action and its bold composite are not computational inputs.

For the fermion check the two routes are (i) complete the full component maps and then restrict their elementary action to the background, and (ii) restrict each completed component map before taking the 42 source products. Their difference is zero in each scalar source group with the ordered spinor and derivative words preserved. The renderer additionally applies the explicit epsilon identity (2.6), never a mixed-delta identification.

Engineering dimensions are checked on every final fermion monomial: the two-derivative coefficient has dimension two and the R² coefficient has dimension four before multiplying $`\lambda`$. For example $`\lambda L_0^{-2}(\bar\Box\delta L)^2`$ has dimension $`-2+4=2`$, and $`\lambda N_0L_0^{-2}(\bar{\mathcal D}\bar\varphi)\gamma\gamma(\bar{\mathcal D}\varphi)`$ has dimension $`-2+1+3=2`$. All free-index checks are made after the complete scalar contraction, not on open component maps.

The explicitly checked two-derivative reference limit, used only as a check, is

```math
\left.(F_L,F_N,\tfrac12F_0-4kF_R)\right|_{\lambda=0,\,L_0=1,\,N_0=-3g/2,\,k=-g^2/2}=(0,0,0).
\tag{5.1}
```

The ungauged flat zero-$`N`$ check is

```math
\left.(F_0,F_L,F_N,\tfrac12F_0-4kF_R)\right|_{g=N_0=k=0}=(0,0,0,0),
\tag{5.2}
```

for any $`L_0>0`$ and $`\lambda`$. For a constant conformal metric perturbation $`h_{\mu\nu}=z\bar g_{\mu\nu}`$, the independent exact path is

```math
\frac e{\bar e}=(1+\epsilon z)^{5/2},\quad
R=\frac{20k}{1+\epsilon z},\quad
R^{(1)}=-20kz,\quad R^{(2)}=20kz^2.
\tag{5.3}
```

Expanding $`(1+\epsilon z)^{5/2}F(20k/(1+\epsilon z),L_0,N_0)`$ agrees with both metric orders in the endpoint. The determinant check also uses a non-diagonal Lorentzian perturbation, so it is not restricted to this conformal probe.

## 6. Final Result

Every coefficient below is evaluated at the general background $`(L_0,N_0,k)`$; all dynamical fluctuations are those of (3.1). A field with vanishing background is written without an additional $`(1)`$ superscript to keep its indices readable. The displayed densities are complete coefficients of $`\epsilon^n`$, including the volume factor. No primed vector component remains in them.

### 6.1 Zeroth order

```math
\begin{aligned}
\ell^{(0)}={}&\frac{L_0^{4} g^{4} \lambda}{16}\\
&- \frac{L_0^{3} g^{2}}{2}\\
&- 5 L_0^{2} g^{2} k \lambda\\
&+2 L_0^{2} g^{2}\\
&- 2 L_0 N_0 g
\end{aligned}
\tag{Z.1}
```

```math
\begin{aligned}
\phantom{\ell^{(0)}={}}&+20 L_0 k\\
&- \frac{5 N_0^{2} g^{2} \lambda}{2}\\
&- 4 N_0 g\\
&+100 k^{2} \lambda\\
&- \frac{2 N_0^{2}}{L_0}
\end{aligned}
\tag{Z.2}
```

```math
\begin{aligned}
\phantom{\ell^{(0)}={}}&- \frac{4 N_0^{3} g \lambda}{L_0^{2}}\\
&+\frac{20 N_0^{2} k \lambda}{L_0^{2}}\\
&+\frac{N_0^{4} \lambda}{L_0^{4}}
\end{aligned}
\tag{Z.3}
```

### 6.2 First order

```math
\begin{aligned}
\ell^{(1)}={}&\left[L_0 + \lambda \left(- \frac{L_0^{2} g^{2}}{4} + 10 k + \frac{N_0^{2}}{L_0^{2}}\right)\right]R^{(1)}\\
&+\left[- \frac{3 L_0^{2} g^{2}}{2} + 4 L_0 g^{2} - 2 N_0 g + 20 k + \lambda \left(\frac{L_0^{3} g^{4}}{4} - 10 L_0 g^{2} k + \frac{8 N_0^{3} g}{L_0^{3}} - \frac{40 N_0^{2} k}{L_0^{3}} - \frac{4 N_0^{4}}{L_0^{5}}\right) + \frac{2 N_0^{2}}{L_0^{2}}\right]\delta L
\end{aligned}
\tag{ONE.1}
```

```math
\begin{aligned}
\phantom{\ell^{(1)}={}}&+\left[- 2 L_0 g - 4 g + \lambda \left(- 5 N_0 g^{2} - \frac{12 N_0^{2} g}{L_0^{2}} + \frac{40 N_0 k}{L_0^{2}} + \frac{4 N_0^{3}}{L_0^{4}}\right) - \frac{4 N_0}{L_0}\right]\delta N\\
&+\left[- \frac{L_0^{3} g^{2}}{4} + L_0^{2} g^{2} - L_0 N_0 g + 10 L_0 k - 2 N_0 g + \lambda \left(\frac{L_0^{4} g^{4}}{32} - \frac{5 L_0^{2} g^{2} k}{2} - \frac{5 N_0^{2} g^{2}}{4} + 50 k^{2} - \frac{2 N_0^{3} g}{L_0^{2}} + \frac{10 N_0^{2} k}{L_0^{2}} + \frac{N_0^{4}}{2 L_0^{4}}\right) - \frac{N_0^{2}}{L_0}\right]h
\end{aligned}
\tag{ONE.2}
```

```math
\begin{aligned}
\phantom{\ell^{(1)}={}}&+\left[\lambda \left(\frac{L_0 g^{2}}{2} - \frac{20 k}{L_0} - \frac{2 N_0^{2}}{L_0^{3}}\right) - 2\right]\bar\Box\delta L
\end{aligned}
\tag{ONE.3}
```

Its bulk form and its explicit divergence are (4.41). In particular the three tadpoles displayed there are not set to zero.

### 6.3 Second order: explicit bosonic coefficient

```math
\begin{aligned}
\ell^{(2)}_{\rm B}={}&\left[L_0 + \lambda \left(- \frac{L_0^{2} g^{2}}{4} + 10 k + \frac{N_0^{2}}{L_0^{2}}\right)\right]R^{(2)}\\
&+\left[\frac{\lambda}{4}\right](R^{(1)})^2
\end{aligned}
\tag{B2.1}
```

```math
\begin{aligned}
\phantom{\ell^{(2)}_{\rm B}={}}&+\left[\lambda \left(- \frac{L_0 g^{2}}{2} - \frac{2 N_0^{2}}{L_0^{3}}\right) + 1\right]R^{(1)}\delta L\\
&+\left[\frac{2 N_0 \lambda}{L_0^{2}}\right]R^{(1)}\delta N
\end{aligned}
\tag{B2.2}
```

```math
\begin{aligned}
\phantom{\ell^{(2)}_{\rm B}={}}&+\left[- \frac{3 L_0 g^{2}}{2} + 2 g^{2} + \lambda \left(\frac{3 L_0^{2} g^{4}}{8} - 5 g^{2} k - \frac{12 N_0^{3} g}{L_0^{4}} + \frac{60 N_0^{2} k}{L_0^{4}} + \frac{10 N_0^{4}}{L_0^{6}}\right) - \frac{2 N_0^{2}}{L_0^{3}}\right](\delta L)^2\\
&+\left[- 2 g + \lambda \left(\frac{24 N_0^{2} g}{L_0^{3}} - \frac{80 N_0 k}{L_0^{3}} - \frac{16 N_0^{3}}{L_0^{5}}\right) + \frac{4 N_0}{L_0^{2}}\right]\delta L\delta N
\end{aligned}
\tag{B2.3}
```

```math
\begin{aligned}
\phantom{\ell^{(2)}_{\rm B}={}}&+\left[\lambda \left(- \frac{5 g^{2}}{2} - \frac{12 N_0 g}{L_0^{2}} + \frac{20 k}{L_0^{2}} + \frac{6 N_0^{2}}{L_0^{4}}\right) - \frac{2}{L_0}\right](\delta N)^2\\
&+\left[\frac{L_0}{2} + \lambda \left(- \frac{L_0^{2} g^{2}}{8} + 5 k + \frac{N_0^{2}}{2 L_0^{2}}\right)\right]hR^{(1)}
\end{aligned}
\tag{B2.4}
```

```math
\begin{aligned}
\phantom{\ell^{(2)}_{\rm B}={}}&+\left[- \frac{3 L_0^{2} g^{2}}{4} + 2 L_0 g^{2} - N_0 g + 10 k + \lambda \left(\frac{L_0^{3} g^{4}}{8} - 5 L_0 g^{2} k + \frac{4 N_0^{3} g}{L_0^{3}} - \frac{20 N_0^{2} k}{L_0^{3}} - \frac{2 N_0^{4}}{L_0^{5}}\right) + \frac{N_0^{2}}{L_0^{2}}\right]h\delta L\\
&+\left[- L_0 g - 2 g + \lambda \left(- \frac{5 N_0 g^{2}}{2} - \frac{6 N_0^{2} g}{L_0^{2}} + \frac{20 N_0 k}{L_0^{2}} + \frac{2 N_0^{3}}{L_0^{4}}\right) - \frac{2 N_0}{L_0}\right]h\delta N
\end{aligned}
\tag{B2.5}
```

```math
\begin{aligned}
\phantom{\ell^{(2)}_{\rm B}={}}&+\left[- \frac{L_0^{3} g^{2}}{16} + \frac{L_0^{2} g^{2}}{4} - \frac{L_0 N_0 g}{4} + \frac{5 L_0 k}{2} - \frac{N_0 g}{2} + \lambda \left(\frac{L_0^{4} g^{4}}{128} - \frac{5 L_0^{2} g^{2} k}{8} - \frac{5 N_0^{2} g^{2}}{16} + \frac{25 k^{2}}{2} - \frac{N_0^{3} g}{2 L_0^{2}} + \frac{5 N_0^{2} k}{2 L_0^{2}} + \frac{N_0^{4}}{8 L_0^{4}}\right) - \frac{N_0^{2}}{4 L_0}\right]h^2\\
&+\left[\frac{L_0^{3} g^{2}}{8} - \frac{L_0^{2} g^{2}}{2} + \frac{L_0 N_0 g}{2} - 5 L_0 k + N_0 g + \lambda \left(- \frac{L_0^{4} g^{4}}{64} + \frac{5 L_0^{2} g^{2} k}{4} + \frac{5 N_0^{2} g^{2}}{8} - 25 k^{2} + \frac{N_0^{3} g}{L_0^{2}} - \frac{5 N_0^{2} k}{L_0^{2}} - \frac{N_0^{4}}{4 L_0^{4}}\right) + \frac{N_0^{2}}{2 L_0}\right]h_{\mu\nu}h^{\mu\nu}
\end{aligned}
\tag{B2.6}
```

```math
\begin{aligned}
\phantom{\ell^{(2)}_{\rm B}={}}&+\left[- \frac{\lambda}{L_0}\right]R^{(1)}\bar\Box\delta L\\
&+\left[\lambda \left(\frac{g^{2}}{2} + \frac{20 k}{L_0^{2}} + \frac{6 N_0^{2}}{L_0^{4}}\right)\right]\delta L\bar\Box\delta L
\end{aligned}
\tag{B2.7}
```

```math
\begin{aligned}
\phantom{\ell^{(2)}_{\rm B}={}}&+\left[- \frac{4 N_0 \lambda}{L_0^{3}}\right]\delta N\bar\Box\delta L\\
&+\left[\lambda \left(- \frac{L_0 g^{2}}{2} + \frac{20 k}{L_0} + \frac{2 N_0^{2}}{L_0^{3}}\right) + 2\right]h^{\mu\nu}\bar{\mathcal D}_\mu\bar{\mathcal D}_\nu\delta L
\end{aligned}
\tag{B2.8}
```

```math
\begin{aligned}
\phantom{\ell^{(2)}_{\rm B}={}}&+\left[\lambda \left(- \frac{L_0 g^{2}}{2} + \frac{20 k}{L_0} + \frac{2 N_0^{2}}{L_0^{3}}\right) + 2\right](\bar{\mathcal D}_\mu h^{\mu\nu})\bar{\mathcal D}_\nu\delta L\\
&+\left[\lambda \left(\frac{L_0 g^{2}}{4} - \frac{10 k}{L_0} - \frac{N_0^{2}}{L_0^{3}}\right) - 1\right](\bar{\mathcal D}^\nu h)\bar{\mathcal D}_\nu\delta L
\end{aligned}
\tag{B2.9}
```

```math
\begin{aligned}
\phantom{\ell^{(2)}_{\rm B}={}}&+\left[\lambda \left(\frac{L_0 g^{2}}{4} - \frac{10 k}{L_0} - \frac{N_0^{2}}{L_0^{3}}\right) - 1\right]h\bar\Box\delta L\\
&+\left[\lambda \left(- \frac{g^{2}}{4} + \frac{10 k}{L_0^{2}} - \frac{N_0^{2}}{L_0^{4}}\right) + \frac{1}{L_0}\right](\bar{\mathcal D}\delta L)^2
\end{aligned}
\tag{B2.10}
```

```math
\begin{aligned}
\phantom{\ell^{(2)}_{\rm B}={}}&+\left[- \frac{2 \lambda}{L_0^{2}}\right](\bar{\mathcal D}\delta N)^2\\
&+\left[\frac{4 N_0 \lambda}{L_0^{3}}\right]\bar{\mathcal D}_a\delta N\bar{\mathcal D}^a\delta L
\end{aligned}
\tag{B2.11}
```

```math
\begin{aligned}
\phantom{\ell^{(2)}_{\rm B}={}}&+\left[\frac{\lambda}{L_0^{2}}\right](\bar\Box\delta L)^2\\
&+\left[- \frac{L_0}{2} + \lambda \left(\frac{L_0^{2} g^{2}}{8} - 5 k - \frac{3 N_0^{2}}{2 L_0^{2}}\right)\right]G^{ab}G_{ab}
\end{aligned}
\tag{B2.12}
```

```math
\begin{aligned}
\phantom{\ell^{(2)}_{\rm B}={}}&+\left[4 L_0 + \lambda \left(- L_0^{2} g^{2} + 40 k + \frac{4 N_0^{2}}{L_0^{2}}\right)\right]H^{ab}H_{ab}\\
&+\left[\lambda \left(- \frac{g^{2}}{2} + \frac{20 k}{L_0^{2}} + \frac{2 N_0^{2}}{L_0^{4}}\right) - \frac{2}{L_0}\right]E^aE_a
\end{aligned}
\tag{B2.13}
```

```math
\begin{aligned}
\phantom{\ell^{(2)}_{\rm B}={}}&+\left[2 L_0 + \lambda \left(- \frac{L_0^{2} g^{2}}{2} + 20 k + \frac{2 N_0^{2}}{L_0^{2}}\right)\right]V'_a{}^{ij}V'{}^a_{ij}\\
&+2\lambda(\bar{\mathcal D}^aV'_a{}^{ij})(\bar{\mathcal D}^bV'_{b\,ij})
\end{aligned}
\tag{B2.14}
```

```math
\begin{aligned}
\phantom{\ell^{(2)}_{\rm B}={}}&+\left[\frac{4 N_0^{2} \lambda}{L_0^{2}}\right]H^{ab}G_{ab}\\
&-2\sqrt2 E^aV_a
\end{aligned}
\tag{B2.15}
```

```math
\begin{aligned}
\phantom{\ell^{(2)}_{\rm B}={}}&-4gE^aC_a\\
&+\left[- \frac{4 \lambda}{L_0^{2}}\right](\bar{\mathcal D}_{[a}E_{b]})(\bar{\mathcal D}^{[a}E^{b]})
\end{aligned}
\tag{B2.16}
```

```math
\begin{aligned}
\phantom{\ell^{(2)}_{\rm B}={}}&-2\lambda(\bar{\mathcal D}_{[a}V_{b]})(\bar{\mathcal D}^{[a}V^{b]})\\
&+\left[- \frac{4 \sqrt{2} \lambda}{L_0}\right](\bar{\mathcal D}_{[a}E_{b]})(\bar{\mathcal D}^{[a}V^{b]})
\end{aligned}
\tag{B2.17}
```

```math
\begin{aligned}
\phantom{\ell^{(2)}_{\rm B}={}}&+\left[\frac{4 N_0 \lambda}{L_0^{2}}\right]G^{ab}\bar{\mathcal D}_{[a}E_{b]}\\
&+\left[\frac{2 \sqrt{2} N_0 \lambda}{L_0}\right]G^{ab}\bar{\mathcal D}_{[a}V_{b]}
\end{aligned}
\tag{B2.18}
```

```math
\begin{aligned}
\phantom{\ell^{(2)}_{\rm B}={}}&+\left[- \frac{16 N_0 \lambda}{L_0^{2}}\right]H^{ab}\bar{\mathcal D}_{[a}E_{b]}\\
&+\left[- \frac{8 \sqrt{2} N_0 \lambda}{L_0}\right]H^{ab}\bar{\mathcal D}_{[a}V_{b]}
\end{aligned}
\tag{B2.19}
```

In this expression $`R^{(1)},R^{(2)}`$ are the fully defined metric coefficients (3.9)–(3.10), and $`G,H,E`$ mean (3.3). Thus keeping those standard geometric expressions does not suppress a composite-vector substitution. All curl products originating from $`F'`$ have been distributed.

### 6.4 Second order: explicit two-derivative fermion coefficient

The following continued equality retains local differentiated-bar terms. It is not a gamma-trace gauge or an equation-of-motion representative.

```math
\begin{aligned}
\ell^{(2)}_{2\partial,\rm F}={}&\sqrt{2} i \delta_{ij} (\bar{\mathcal D}_{a}\bar\psi^{ai}) \varphi^{j}\\
&+2 \sqrt{2} i \delta_{ij} \bar\psi_{a}{}^{i} (\bar{\mathcal D}^{a}\varphi^{j})\\
&+\frac{3 L_0}{4} (\bar{\mathcal D}_{a}\bar\psi^{ai}) \gamma^{b} \psi_{bi}\\
&+\frac{25 L_0}{12} \bar\psi_{a}{}^{i} \gamma^{b} (\bar{\mathcal D}^{a}\psi_{bi})
\end{aligned}
\tag{F2D.1}
```

```math
\begin{aligned}
\phantom{\ell^{(2)}_{2\partial,\rm F}={}}&- \frac{L_0}{2} (\bar{\mathcal D}_{a}\bar\psi_{b}{}^{i}) \gamma^{a} \psi^{b}{}_{i}\\
&- \frac{11 L_0}{6} \bar\psi_{a}{}^{i} \gamma^{b} (\bar{\mathcal D}_{b}\psi^{a}{}_{i})\\
&- \frac{L_0}{4} (\bar{\mathcal D}_{a}\bar\psi_{b}{}^{i}) \gamma^{b} \psi^{a}{}_{i}\\
&- \frac{L_0}{4} \bar\psi_{a}{}^{i} \gamma^{a} (\bar{\mathcal D}_{b}\psi^{b}{}_{i})
\end{aligned}
\tag{F2D.2}
```

```math
\begin{aligned}
\phantom{\ell^{(2)}_{2\partial,\rm F}={}}&- \frac{L_0}{3} (\bar{\mathcal D}_{a}\bar\psi_{b}{}^{i}) \gamma^{b} \gamma^{ac} \psi_{ci}\\
&+\frac{L_0}{3} (\bar{\mathcal D}_{a}\bar\psi_{b}{}^{i}) \gamma^{a} \gamma^{bc} \psi_{ci}\\
&- \frac{L_0}{3} (\bar{\mathcal D}_{a}\bar\psi_{b}{}^{i}) \gamma^{ab} \gamma^{c} \psi_{ci}\\
&- \frac{7 L_0}{6} \bar\psi_{a}{}^{i} \gamma^{a} \gamma^{bc} (\bar{\mathcal D}_{b}\psi_{ci})
\end{aligned}
\tag{F2D.3}
```

```math
\begin{aligned}
\phantom{\ell^{(2)}_{2\partial,\rm F}={}}&+\frac{L_0}{6} \bar\psi_{a}{}^{i} \gamma^{a} \gamma^{bc} (\bar{\mathcal D}_{c}\psi_{bi})\\
&+\frac{\sqrt{2} i \left(L_0^{2} g - 2 N_0\right)}{4} \delta_{ij} \bar\psi_{a}{}^{i} \psi^{aj}\\
&- \frac{4 \sqrt{2} i}{3} \delta_{ij} \bar\varphi^{i} \gamma^{a} \gamma^{b} (\bar{\mathcal D}_{a}\psi_{b}{}^{j})\\
&+\frac{4 \sqrt{2} i}{3} \delta_{ij} \bar\varphi^{i} \gamma^{a} \gamma^{b} (\bar{\mathcal D}_{b}\psi_{a}{}^{j})
\end{aligned}
\tag{F2D.4}
```

```math
\begin{aligned}
\phantom{\ell^{(2)}_{2\partial,\rm F}={}}&+\frac{5 \sqrt{2} i}{6} \delta_{ij} \bar\varphi^{i} \gamma^{ab} (\bar{\mathcal D}_{a}\psi_{b}{}^{j})\\
&- \frac{5 \sqrt{2} i}{6} \delta_{ij} \bar\varphi^{i} \gamma^{ab} (\bar{\mathcal D}_{b}\psi_{a}{}^{j})\\
&+\frac{\sqrt{2} i \left(2 L_0^{2} g - N_0\right)}{L_0^{2}} \delta_{ij} \bar\varphi^{i} \varphi^{j}\\
&- \frac{2}{L_0} \bar\varphi^{i} \gamma^{a} (\bar{\mathcal D}_{a}\varphi_{i})
\end{aligned}
\tag{F2D.5}
```

```math
\begin{aligned}
\phantom{\ell^{(2)}_{2\partial,\rm F}={}}&+\frac{N_0}{L_0} \bar\varphi^{i} \gamma^{a} \psi_{ai}\\
&- \frac{4}{L_0} (\bar{\mathcal D}_{a}\bar\varphi^{i}) \gamma^{a} \varphi_{i}\\
&- \frac{2 L_0^{2} g + 2 L_0 g - N_0}{L_0} \bar\psi_{a}{}^{i} \gamma^{a} \varphi_{i}\\
&- 2 \sqrt{2} i \delta_{ij} (\bar{\mathcal D}_{a}\bar\psi_{b}{}^{i}) \gamma^{ab} \varphi^{j}
\end{aligned}
\tag{F2D.6}
```

```math
\begin{aligned}
\phantom{\ell^{(2)}_{2\partial,\rm F}={}}&- \sqrt{2} i \delta_{ij} \bar\psi_{a}{}^{i} \gamma^{a} \gamma^{b} (\bar{\mathcal D}_{b}\varphi^{j})\\
&- \frac{\sqrt{2} i \left(L_0^{2} g - 2 N_0\right)}{4} \delta_{ij} \bar\psi_{a}{}^{i} \gamma^{a} \gamma^{b} \psi_{b}{}^{j}\\
&- \frac{\sqrt{2} i \left(L_0 g + N_0\right)}{2} \delta_{ij} \bar\psi_{a}{}^{i} \gamma^{ab} \psi_{b}{}^{j}
\end{aligned}
\tag{F2D.7}
```

### 6.5 Second order: explicit R² fermion coefficient

The next continued equality is the coefficient of the invariant before multiplying $`\lambda`$. All its background scalar coefficients, primed maps and dependent connections have been inserted. The matrix products and the order of the covariant derivatives are explicit.

```math
\begin{aligned}
\ell^{(2)}_{R^2,\rm F}={}&- \frac{\sqrt{2} i \left(L_0^{4} g^{2} + 2 L_0^{2} N_0 g - 40 L_0^{2} k - 6 N_0^{2}\right)}{4 L_0^{3}} \delta_{ij} (\bar{\mathcal D}_{a}\bar\psi^{ai}) \varphi^{j}\\
&- \frac{\sqrt{2} i \left(L_0^{4} g^{2} + 2 L_0^{2} N_0 g - 40 L_0^{2} k - 6 N_0^{2}\right)}{2 L_0^{3}} \delta_{ij} \bar\psi_{a}{}^{i} (\bar{\mathcal D}^{a}\varphi^{j})\\
&- \frac{3 L_0^{4} g^{2} + 4 L_0^{2} N_0 g - 120 L_0^{2} k - 20 N_0^{2}}{16 L_0^{2}} (\bar{\mathcal D}_{a}\bar\psi^{ai}) \gamma^{b} \psi_{bi}\\
&- \frac{25 L_0^{4} g^{2} + 24 L_0^{2} N_0 g - 1000 L_0^{2} k - 148 N_0^{2}}{48 L_0^{2}} \bar\psi_{a}{}^{i} \gamma^{b} (\bar{\mathcal D}^{a}\psi_{bi})
\end{aligned}
\tag{FR2.1}
```

```math
\begin{aligned}
\phantom{\ell^{(2)}_{R^2,\rm F}={}}&+\frac{L_0^{4} g^{2} - 40 L_0^{2} k - 4 N_0^{2}}{8 L_0^{2}} (\bar{\mathcal D}_{a}\bar\psi_{b}{}^{i}) \gamma^{a} \psi^{b}{}_{i}\\
&+\frac{11 \left(L_0^{4} g^{2} - 40 L_0^{2} k - 4 N_0^{2}\right)}{24 L_0^{2}} \bar\psi_{a}{}^{i} \gamma^{b} (\bar{\mathcal D}_{b}\psi^{a}{}_{i})\\
&+\frac{L_0^{4} g^{2} - 40 L_0^{2} k - 4 N_0^{2}}{16 L_0^{2}} (\bar{\mathcal D}_{a}\bar\psi_{b}{}^{i}) \gamma^{b} \psi^{a}{}_{i}\\
&+\frac{L_0^{4} g^{2} - 40 L_0^{2} k - 4 N_0^{2}}{16 L_0^{2}} \bar\psi_{a}{}^{i} \gamma^{a} (\bar{\mathcal D}_{b}\psi^{b}{}_{i})
\end{aligned}
\tag{FR2.2}
```

```math
\begin{aligned}
\phantom{\ell^{(2)}_{R^2,\rm F}={}}&+\frac{L_0^{4} g^{2} - 40 L_0^{2} k - 4 N_0^{2}}{12 L_0^{2}} (\bar{\mathcal D}_{a}\bar\psi_{b}{}^{i}) \gamma^{b} \gamma^{ac} \psi_{ci}\\
&- \frac{L_0^{4} g^{2} - 40 L_0^{2} k - 4 N_0^{2}}{12 L_0^{2}} (\bar{\mathcal D}_{a}\bar\psi_{b}{}^{i}) \gamma^{a} \gamma^{bc} \psi_{ci}\\
&- \frac{8 L_0^{4} g^{2} - L_0^{2} N_0 g - 80 L_0^{2} k + 42 N_0^{2}}{48 L_0^{2}} (\bar{\mathcal D}_{a}\bar\psi_{b}{}^{i}) \gamma^{ab} \gamma^{c} \psi_{ci}\\
&+\frac{4 L_0^{4} g^{2} - 101 L_0^{2} N_0 g - 640 L_0^{2} k - 54 N_0^{2}}{96 L_0^{2}} \bar\psi_{a}{}^{i} \gamma^{a} \gamma^{bc} (\bar{\mathcal D}_{b}\psi_{ci})
\end{aligned}
\tag{FR2.3}
```

```math
\begin{aligned}
\phantom{\ell^{(2)}_{R^2,\rm F}={}}&- \frac{4 L_0^{4} g^{2} - 5 L_0^{2} N_0 g - 160 L_0^{2} k - 6 N_0^{2}}{96 L_0^{2}} \bar\psi_{a}{}^{i} \gamma^{a} \gamma^{bc} (\bar{\mathcal D}_{c}\psi_{bi})\\
&- \frac{\sqrt{2} i \left(L_0^{6} g^{3} - 3 L_0^{4} N_0 g^{2} - 40 L_0^{4} g k - 12 L_0^{2} N_0^{2} g + 120 L_0^{2} N_0 k + 12 N_0^{3}\right)}{16 L_0^{3}} \delta_{ij} \bar\psi_{a}{}^{i} \psi^{aj}\\
&+\frac{\sqrt{2} i \left(L_0^{4} g^{2} + 7 L_0^{2} N_0 g - 160 L_0^{2} k - 20 N_0^{2}\right)}{12 L_0^{3}} \delta_{ij} \bar\varphi^{i} \gamma^{a} \gamma^{b} (\bar{\mathcal D}_{a}\psi_{b}{}^{j})\\
&- \frac{\sqrt{2} i \left(2 L_0^{4} g^{2} - L_0^{2} N_0 g - 80 L_0^{2} k - 7 N_0^{2}\right)}{6 L_0^{3}} \delta_{ij} \bar\varphi^{i} \gamma^{a} \gamma^{b} (\bar{\mathcal D}_{b}\psi_{a}{}^{j})
\end{aligned}
\tag{FR2.4}
```

```math
\begin{aligned}
\phantom{\ell^{(2)}_{R^2,\rm F}={}}&+\frac{\sqrt{2} i \left(2 L_0^{4} g^{2} + 89 L_0^{2} N_0 g + 400 L_0^{2} k + 35 N_0^{2}\right)}{48 L_0^{3}} \delta_{ij} \bar\varphi^{i} \gamma^{ab} (\bar{\mathcal D}_{a}\psi_{b}{}^{j})\\
&+\frac{5 \sqrt{2} i \left(2 L_0^{4} g^{2} - L_0^{2} N_0 g - 80 L_0^{2} k - 7 N_0^{2}\right)}{48 L_0^{3}} \delta_{ij} \bar\varphi^{i} \gamma^{ab} (\bar{\mathcal D}_{b}\psi_{a}{}^{j})\\
&+\frac{\sqrt{2} i \left(L_0^{6} g^{3} + 16 L_0^{4} N_0 g^{2} + 40 L_0^{4} g k - 42 L_0^{2} N_0^{2} g + 160 L_0^{2} N_0 k + 16 N_0^{3}\right)}{8 L_0^{5}} \delta_{ij} \bar\varphi^{i} \varphi^{j}\\
&+\frac{11 L_0^{2} N_0 g - 40 L_0^{2} k - 6 N_0^{2}}{2 L_0^{4}} \bar\varphi^{i} \gamma^{a} (\bar{\mathcal D}_{a}\varphi_{i})
\end{aligned}
\tag{FR2.5}
```

```math
\begin{aligned}
\phantom{\ell^{(2)}_{R^2,\rm F}={}}&+\frac{L_0^{6} g^{3} + 4 L_0^{4} N_0 g^{2} - 20 L_0^{4} g k - 12 L_0^{2} N_0^{2} g + 60 L_0^{2} N_0 k + 6 N_0^{3}}{4 L_0^{4}} \bar\varphi^{i} \gamma^{a} \psi_{ai}\\
&+\frac{2}{L_0^{2}} (\bar{\mathcal D}_{a}\bar\varphi^{i}) \gamma^{a} \gamma^{b} \gamma^{c} (\bar{\mathcal D}_{b}\bar{\mathcal D}_{c}\varphi_{i})\\
&+\frac{\sqrt{2} i \left(L_0^{2} g - 2 N_0\right)}{2 L_0^{3}} \delta_{ij} (\bar{\mathcal D}_{a}\bar\varphi^{i}) \gamma^{a} \gamma^{b} (\bar{\mathcal D}_{b}\varphi^{j})\\
&+\frac{3 L_0^{2} g - 4 N_0}{6 L_0^{2}} (\bar{\mathcal D}_{a}\bar\varphi^{i}) \gamma^{a} \gamma^{b} \gamma^{c} (\bar{\mathcal D}_{b}\psi_{ci})
\end{aligned}
\tag{FR2.6}
```

```math
\begin{aligned}
\phantom{\ell^{(2)}_{R^2,\rm F}={}}&+\frac{\sqrt{2} i}{L_0} \delta_{ij} (\bar{\mathcal D}_{a}\bar\varphi^{i}) \gamma^{a} \gamma^{b} \gamma^{cd} (\bar{\mathcal D}_{b}\bar{\mathcal D}_{c}\psi_{d}{}^{j})\\
&- \frac{\sqrt{2} i \left(L_0^{4} g^{2} + 2 L_0^{2} N_0 g - 20 L_0^{2} k - 2 N_0^{2}\right)}{4 L_0^{3}} \delta_{ij} (\bar{\mathcal D}_{a}\bar\varphi^{i}) \gamma^{a} \gamma^{b} \psi_{b}{}^{j}\\
&- \frac{N_0}{3 L_0^{2}} (\bar{\mathcal D}_{a}\bar\varphi^{i}) \gamma^{a} \gamma^{b} \gamma^{c} (\bar{\mathcal D}_{c}\psi_{bi})\\
&- \frac{12 L_0^{2} g + 5 N_0}{24 L_0^{2}} (\bar{\mathcal D}_{a}\bar\varphi^{i}) \gamma^{a} \gamma^{bc} (\bar{\mathcal D}_{b}\psi_{ci})
\end{aligned}
\tag{FR2.7}
```

```math
\begin{aligned}
\phantom{\ell^{(2)}_{R^2,\rm F}={}}&+\frac{5 N_0}{24 L_0^{2}} (\bar{\mathcal D}_{a}\bar\varphi^{i}) \gamma^{a} \gamma^{bc} (\bar{\mathcal D}_{c}\psi_{bi})\\
&- \frac{\sqrt{2} i \left(L_0^{2} g - N_0\right)}{L_0^{3}} \delta_{ij} \bar\varphi^{i} \gamma^{a} \gamma^{b} (\bar{\mathcal D}_{a}\bar{\mathcal D}_{b}\varphi^{j})\\
&- \frac{L_0^{2} g - N_0}{L_0^{2}} \bar\varphi^{i} \gamma^{a} \gamma^{bc} (\bar{\mathcal D}_{a}\bar{\mathcal D}_{b}\psi_{ci})\\
&+\frac{g}{2} \bar\psi_{a}{}^{i} \gamma^{a} \gamma^{b} \gamma^{c} (\bar{\mathcal D}_{b}\bar{\mathcal D}_{c}\varphi_{i})
\end{aligned}
\tag{FR2.8}
```

```math
\begin{aligned}
\phantom{\ell^{(2)}_{R^2,\rm F}={}}&+\frac{\sqrt{2} i \left(L_0^{4} g^{2} - 5 L_0^{2} N_0 g - 20 L_0^{2} k - 2 N_0^{2}\right)}{4 L_0^{3}} \delta_{ij} \bar\psi_{a}{}^{i} \gamma^{a} \gamma^{b} (\bar{\mathcal D}_{b}\varphi^{j})\\
&+\frac{\left(L_0^{2} g - 2 N_0\right) \left(3 L_0^{2} g + 2 N_0\right)}{24 L_0^{2}} \bar\psi_{a}{}^{i} \gamma^{a} \gamma^{b} \gamma^{c} (\bar{\mathcal D}_{b}\psi_{ci})\\
&+\frac{\sqrt{2} i L_0 g}{4} \delta_{ij} \bar\psi_{a}{}^{i} \gamma^{a} \gamma^{b} \gamma^{cd} (\bar{\mathcal D}_{b}\bar{\mathcal D}_{c}\psi_{d}{}^{j})\\
&- \frac{\sqrt{2} i \left(L_0^{6} g^{3} + 14 L_0^{4} N_0 g^{2} - 12 L_0^{2} N_0^{2} g - 80 L_0^{2} N_0 k - 8 N_0^{3}\right)}{32 L_0^{3}} \delta_{ij} \bar\psi_{a}{}^{i} \gamma^{a} \gamma^{b} \psi_{b}{}^{j}
\end{aligned}
\tag{FR2.9}
```

```math
\begin{aligned}
\phantom{\ell^{(2)}_{R^2,\rm F}={}}&- \frac{N_0 \left(L_0^{2} g - 2 N_0\right)}{12 L_0^{2}} \bar\psi_{a}{}^{i} \gamma^{a} \gamma^{b} \gamma^{c} (\bar{\mathcal D}_{c}\psi_{bi})\\
&+\frac{\sqrt{2} i}{L_0} \delta_{ij} (\bar{\mathcal D}_{a}\bar\psi_{b}{}^{i}) \gamma^{ab} \gamma^{c} \gamma^{d} (\bar{\mathcal D}_{c}\bar{\mathcal D}_{d}\varphi^{j})\\
&+\frac{6 L_0^{2} g + 13 N_0}{12 L_0^{2}} (\bar{\mathcal D}_{a}\bar\psi_{b}{}^{i}) \gamma^{ab} \gamma^{c} (\bar{\mathcal D}_{c}\varphi_{i})\\
&+\frac{\sqrt{2} i \left(3 L_0^{2} g - 4 N_0\right)}{12 L_0} \delta_{ij} (\bar{\mathcal D}_{a}\bar\psi_{b}{}^{i}) \gamma^{ab} \gamma^{c} \gamma^{d} (\bar{\mathcal D}_{c}\psi_{d}{}^{j})
\end{aligned}
\tag{FR2.10}
```

```math
\begin{aligned}
\phantom{\ell^{(2)}_{R^2,\rm F}={}}&+(\bar{\mathcal D}_{a}\bar\psi_{b}{}^{i}) \gamma^{ab} \gamma^{c} \gamma^{de} (\bar{\mathcal D}_{c}\bar{\mathcal D}_{d}\psi_{ei})\\
&- \frac{\sqrt{2} i N_0}{6 L_0} \delta_{ij} (\bar{\mathcal D}_{a}\bar\psi_{b}{}^{i}) \gamma^{ab} \gamma^{c} \gamma^{d} (\bar{\mathcal D}_{d}\psi_{c}{}^{j})\\
&- \frac{\sqrt{2} i \left(4 L_0^{2} g - 15 N_0\right)}{16 L_0} \delta_{ij} (\bar{\mathcal D}_{a}\bar\psi_{b}{}^{i}) \gamma^{ab} \gamma^{cd} (\bar{\mathcal D}_{c}\psi_{d}{}^{j})\\
&+\frac{5 \sqrt{2} i N_0}{48 L_0} \delta_{ij} (\bar{\mathcal D}_{a}\bar\psi_{b}{}^{i}) \gamma^{ab} \gamma^{cd} (\bar{\mathcal D}_{d}\psi_{c}{}^{j})
\end{aligned}
\tag{FR2.11}
```

```math
\begin{aligned}
\phantom{\ell^{(2)}_{R^2,\rm F}={}}&- \frac{g \left(L_0^{2} g + 7 N_0\right)}{2 L_0^{2}} (\bar{\mathcal D}_{a}\bar\varphi^{i}) \gamma^{a} \varphi_{i}\\
&- \frac{4 L_0^{4} N_0 g^{2} + 10 L_0^{4} g k - L_0^{2} N_0^{2} g - 10 L_0^{2} N_0 k - N_0^{3}}{2 L_0^{4}} \bar\psi_{a}{}^{i} \gamma^{a} \varphi_{i}\\
&- \frac{\sqrt{2} i \left(6 L_0^{4} g^{2} + 17 L_0^{2} N_0 g + 25 N_0^{2}\right)}{24 L_0^{3}} \delta_{ij} (\bar{\mathcal D}_{a}\bar\psi_{b}{}^{i}) \gamma^{ab} \varphi^{j}\\
&+\frac{\sqrt{2} i N_0}{2 L_0^{3}} \delta_{ij} (\bar{\mathcal D}_{a}\bar{\mathcal D}^{a}\bar\varphi^{i}) \varphi^{j}
\end{aligned}
\tag{FR2.12}
```

```math
\begin{aligned}
\phantom{\ell^{(2)}_{R^2,\rm F}={}}&+\frac{\sqrt{2} i N_0}{L_0^{3}} \delta_{ij} (\bar{\mathcal D}_{a}\bar\varphi^{i}) (\bar{\mathcal D}^{a}\varphi^{j})\\
&+\frac{\sqrt{2} i N_0}{2 L_0^{3}} \delta_{ij} \bar\varphi^{i} (\bar{\mathcal D}_{a}\bar{\mathcal D}^{a}\varphi^{j})\\
&- \frac{N_0}{L_0^{2}} (\bar{\mathcal D}_{a}\bar\psi^{ai}) \gamma^{b} (\bar{\mathcal D}_{b}\varphi_{i})\\
&- \frac{2 N_0}{L_0^{2}} \bar\psi_{a}{}^{i} \gamma^{b} (\bar{\mathcal D}^{a}\bar{\mathcal D}_{b}\varphi_{i})
\end{aligned}
\tag{FR2.13}
```

```math
\begin{aligned}
\phantom{\ell^{(2)}_{R^2,\rm F}={}}&- \frac{\sqrt{2} i N_0}{2 L_0} \delta_{ij} (\bar{\mathcal D}_{a}\bar\psi^{ai}) \gamma^{bc} (\bar{\mathcal D}_{b}\psi_{c}{}^{j})\\
&- \frac{\sqrt{2} i N_0}{L_0} \delta_{ij} \bar\psi_{a}{}^{i} \gamma^{bc} (\bar{\mathcal D}^{a}\bar{\mathcal D}_{b}\psi_{c}{}^{j})\\
&+\frac{5 N_0}{3 L_0^{2}} (\bar{\mathcal D}_{a}\bar\psi_{b}{}^{i}) \gamma^{b} \gamma^{a} \gamma^{c} (\bar{\mathcal D}_{c}\varphi_{i})\\
&+\frac{5 \sqrt{2} i N_0 \left(L_0^{2} g - N_0\right)}{6 L_0^{3}} \delta_{ij} (\bar{\mathcal D}_{a}\bar\psi_{b}{}^{i}) \gamma^{b} \gamma^{a} \varphi^{j}
\end{aligned}
\tag{FR2.14}
```

```math
\begin{aligned}
\phantom{\ell^{(2)}_{R^2,\rm F}={}}&+\frac{5 N_0 \left(L_0^{2} g - 2 N_0\right)}{12 L_0^{2}} (\bar{\mathcal D}_{a}\bar\psi_{b}{}^{i}) \gamma^{b} \gamma^{a} \gamma^{c} \psi_{ci}\\
&+\frac{5 \sqrt{2} i N_0}{6 L_0} \delta_{ij} (\bar{\mathcal D}_{a}\bar\psi_{b}{}^{i}) \gamma^{b} \gamma^{a} \gamma^{cd} (\bar{\mathcal D}_{c}\psi_{d}{}^{j})\\
&- \frac{5 N_0}{3 L_0^{2}} (\bar{\mathcal D}_{a}\bar\psi_{b}{}^{i}) \gamma^{a} \gamma^{b} \gamma^{c} (\bar{\mathcal D}_{c}\varphi_{i})\\
&- \frac{5 \sqrt{2} i N_0 \left(L_0^{2} g - N_0\right)}{6 L_0^{3}} \delta_{ij} (\bar{\mathcal D}_{a}\bar\psi_{b}{}^{i}) \gamma^{a} \gamma^{b} \varphi^{j}
\end{aligned}
\tag{FR2.15}
```

```math
\begin{aligned}
\phantom{\ell^{(2)}_{R^2,\rm F}={}}&- \frac{5 N_0 \left(L_0^{2} g - 2 N_0\right)}{12 L_0^{2}} (\bar{\mathcal D}_{a}\bar\psi_{b}{}^{i}) \gamma^{a} \gamma^{b} \gamma^{c} \psi_{ci}\\
&- \frac{5 \sqrt{2} i N_0}{6 L_0} \delta_{ij} (\bar{\mathcal D}_{a}\bar\psi_{b}{}^{i}) \gamma^{a} \gamma^{b} \gamma^{cd} (\bar{\mathcal D}_{c}\psi_{d}{}^{j})\\
&+\frac{\sqrt{2} i N_0 \left(L_0^{4} g^{2} - 40 L_0^{2} k - 4 N_0^{2}\right)}{16 L_0^{3}} \delta_{ij} \bar\psi_{a}{}^{i} \gamma^{ab} \psi_{b}{}^{j}
\end{aligned}
\tag{FR2.16}
```

### 6.6 The three action coefficients together

```math
\boxed{\begin{aligned}
S^{(0)}&=\int d^5x\,\bar e\,\ell^{(0)},\\
S^{(1)}&=\int d^5x\,\bar e\,\ell^{(1)},\\
S^{(2)}&=\int d^5x\,\bar e\left[
\ell^{(2)}_{\rm B}+\ell^{(2)}_{2\partial,\rm F}
+\lambda\ell^{(2)}_{R^2,\rm F}\right].
\end{aligned}}
\tag{6.6}
```

Here each density is written out above. The remainder is $`O(\epsilon^3)`$ in the total fluctuation expansion. There is no pure-fermion term at order zero or one, and no mixed boson–two-fermion term at order two because the fermion background vanishes. The result retains the nonzero general-background tadpoles and every off-shell mixing term through the stated order.

## 7. Convention Dependence and Remaining Uncertainties

This is a Taylor expansion of the currently locked, constructed action through two physical fermions. It inherits the documented 2016-map, gauged-composite and project curvature-repair qualifications of notes 10–11 and of the two-derivative source. Its algebraic checks do not constitute a new local-supersymmetry or full reality proof of that nonlinear action.

No vacuum is claimed for arbitrary $`L_0,N_0,k`$. A subsequent use of the quadratic action for a physical spectrum requires handling the tadpoles and the remaining source-validation questions. Those questions are outside the scope of this quadratic-action note. No field is called auxiliary or propagating merely from its two-derivative status, and no fluctuation has been eliminated.
