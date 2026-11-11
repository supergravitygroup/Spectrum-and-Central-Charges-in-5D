---
concept: Quadratic spectrum analysis for Gauss–Bonnet on AdS₅
date: 2026-09-29
mode: project-context
project_context: Full fermionic gauged GB action; Part II, Steps 6–14
citation_status: source equations and versions identified in the Literature Guide below
status: explanatory companion; not a certificate for the full spectrum
convention_lock: GB-FERMION-SPECTRUM-CONVENTIONS-v1
---

# Understanding the Gauss–Bonnet on AdS₅ quadratic calculation

## Executive Summary

The spectrum is obtained by expanding the accepted full fermionic action to second fluctuation order on the selected AdS₅ branch, retaining every independent bosonic and fermionic fluctuation, and varying that quadratic action before imposing new gauges. The bosonic and fermionic blocks separate by Grassmann parity, but mixing inside each block must be kept. Supercovariant quantities that look bosonic can contain the fermionic kinetic and mass terms. The calculation below explains these points in the project conventions, verifies the background Killing-spinor conditions, and gives an explicit independent reduction check for the proposed scalar–metric block.

## Why This Matters Here

The input is [the accepted GB action](../../../../action/gb_splus_action.md), especially `GB-FINAL-DENSITY`, with `GB01` fixing its normalization. The background is the selected AdS₅ branch, continuously connected to the two-derivative AdS₅ vacuum, identified in [the Part I catalogue](../../../background.md), Eqs. (5.23)–(5.24). The quadratic analysis begins at Step 6 of [the common procedure](../../WALKTHROUGH.md). The background equations and their vanishing tadpoles are inherited inputs.

Three operations have distinct purposes. Expanding the action gives the kinetic and mixing terms. Varying the unreduced quadratic action gives the equations that every mode must satisfy. Solving the constraints and quotienting gauge transformations gives physical modes. A cancellation in the metric projection does not establish a cancellation in the form or fermionic block.

## Prerequisites and Dependencies

The useful reading sequence is the branch [conventions](../../references/CONVENTIONS.md), `GB-C01`–`GB-C17`; the [component dictionary](../../references/COMPONENT_CONVENTIONS.md), W01, L01–L02, LOG-G02 and SC7-05–SC7-07; the accepted action, `GB06`–`GB14`; then the Part I catalogue. These give the fields and mathematical definitions used below. They are used as accepted inputs, without a new convention or action audit.

## Problem and Target

This companion explains which operations establish a branch spectrum and works out specific checks needed by the Gauss–Bonnet on AdS₅ calculation. The detailed complete source ledger, full raw quadratic action, all linearized equations and final mode table belong to the Part II step documents. A sector result in this companion does not certify those other blocks.

The assumptions used here are:

1. The action is the accepted finite action through two physical fermions, with no expansion in its curvature-squared coupling.
2. The selected AdS₅ background is bosonic, with the local maximally symmetric background and source gauge stated below.
3. Fluctuations of all independent fields remain arbitrary. Source gauge conditions are already part of the input; no new fluctuation gauge is used in the raw formulas.
4. Integrations by parts used for local equations have compactly supported variations. A displayed boundary term can be dropped for that purpose only.
5. The scalar–metric reduction in the worked example is a check of the explicitly displayed proposed quadratic block. Its independent potential checks and its conditional diagonalization are distinguished from the complete source expansion.

## Convention Ledger

<!-- ASSERT_CONVENTION: natural_units=true, metric_signature=(-,+,+,+,+), source_lock=GB-FERMION-SPECTRUM-CONVENTIONS-v1, fourier_convention=not_used, renormalization_scheme=not_applicable_classical -->

Indices $`\mu,\nu`$ and $`a,b`$ run from 0 to 4; $`i,j`$ run from 1 to 2. The metric has signature $`(-,+,+,+,+)`$, antisymmetrization has unit weight, and $`\varepsilon^{01234}=1`$, $`\varepsilon_{01234}=-1`$. The adopted curvature and Clifford definitions are

```math
R_{\mu\nu}{}^{ab}=2\partial_{[\mu}\omega_{\nu]}{}^{ab}+2\omega_{[\mu}{}^{ac}\omega_{\nu]c}{}^b,\qquad \bar R_{\mu\nu\rho\sigma}=k(\bar g_{\mu\rho}\bar g_{\nu\sigma}-\bar g_{\mu\sigma}\bar g_{\nu\rho}),\qquad \{\gamma^a,\gamma^b\}=2\eta^{ab},\quad\gamma^{01234}=i.
\tag{E1}
```

Thus $`\bar R_{\mu\nu}=4k\bar g_{\mu\nu}`$, $`\bar R=20k`$ and $`[\bar\nabla_\mu,\bar\nabla_\nu]\epsilon=k\gamma_{\mu\nu}\epsilon/2`$. These curvature conventions, including the last spinor commutator, are given in `GB-C03`–`GB-C05`.

The bar is linear: $`\bar\zeta^i=(\zeta^i)^T\mathsf C`$ and $`\overline{i\zeta}=i\bar\zeta`$. NW–SE lowering is $`X_i=X^j\varepsilon_{ji}`$, with $`\varepsilon_{12}=\varepsilon^{12}=1`$. Physical fermions and supersymmetry parameters are odd. Functional variations use independent real Grassmann coordinates and left derivatives. No chirality condition is imposed in five dimensions.

The overall action is $`S=(2\kappa_5^2)^{-1}\int e\ell_{\rm tot}`$, with $`\ell_{\rm tot}=\ell_{2\partial}+\lambda_{\rm GB}(-2\ell_{W,\mathrm{OP}}-4\ell_{\log})`$. Engineering dimensions are $`[\lambda_{\rm GB}]=-2`$, $`[g]=[N]=1`$, $`[L]=0`$, $`[\psi_\mu]=[\varphi]=1/2`$ and $`[\kappa_5^2]=-3`$.

## Definitions and Required Identities

Write $`a=\lambda_{\rm GB}g^2`$ and $`x=\bar L`$. The selected branch data are

```math
g\ne0,\qquad a\ge-\tfrac12,\qquad x=\frac{2}{1+\sqrt{1+2a}},\qquad ax^2+2x-2=0,\qquad \bar N=-\frac32gx^2,\qquad k=-\frac12g^2x^2,\qquad 0<x\le2.
\tag{E2}
```

All background strengths and fermions vanish. Locally the background potentials are chosen zero. Define $`\ell_{\rm AdS}`$ by $`k=-\ell_{\rm AdS}^{-2}`$; then $`\ell_{\rm AdS}=\sqrt2/(|g|x)`$. This notation keeps the AdS radius distinct from the fluctuation $`\ell`$ in $`L=x+t\ell`$.

The independent fields are $`e_\mu{}^a,C_\mu,B_{\mu\nu},L,N,V_\mu,V'_\mu{}^{ij},E_{\mu\nu\rho},\psi_\mu^i,\varphi^i`$. The connections $`\omega,\phi,f`$ and composites $`T,\chi,D,Y`$ are expanded from their definitions; they are not new independent variables.

For the explanatory calculations write $`g_{\mu\nu}=\bar g_{\mu\nu}+t h_{\mu\nu}`$, $`L=x+t\ell`$, $`N=\bar N+tn`$, $`\psi_\mu=t\psi_\mu^{(1)}`$ and $`\varphi=t\varphi^{(1)}`$. Below, a spinor appearing in a purely quadratic expression denotes its first-order fluctuation. The bookkeeping parameter $`t`$ is even.

## Core Explanation and Detailed Derivation

### 1. Why two physical fermions suffice, and why their implicit terms matter

An even action has an expansion in even physical fermion degree. Write its degree-zero, degree-two and degree-four contributions as $`S_B[\Phi_B]`$, $`S_{FF}[\Phi_B,\Psi,\Psi]`$ and $`S_{FFFF}[\Phi_B,\Psi,\Psi,\Psi,\Psi]`$. Multilinearity in the displayed fermion slots gives

```math
S_{FF}[\bar\Phi_B+tq_B,tq_F,tq_F]=t^2S_{FF}[\bar\Phi_B,q_F,q_F]+O(t^3),\qquad S_{FFFF}[\bar\Phi_B+tq_B,tq_F,tq_F,tq_F,tq_F]=O(t^4).
\tag{E3}
```

The four fermion factors supply $`t\times t\times t\times t=t^4`$. Changing a bosonic coefficient by $`tq_B`$ adds one power of $`t`$; it does not reduce that order. Therefore the known degree-zero and degree-two action is sufficient for both quadratic blocks on this bosonic background. This conclusion applies after the complete retained action has been constructed; it does not justify dropping terms prematurely while constructing composite descendants.

An even action contains no term with one bosonic and one fermionic fluctuation: such a product has odd parity. Thus $`S^{(2)}=S_B^{(2)}+S_F^{(2)}`$. This separation says nothing about mixing between $`\psi_\mu`$ and $`\varphi`$ or between $`h_{\mu\nu}`$, $`\ell`$ and $`n`$.

The action's `GB07` makes the role of implicit fermions concrete. Keeping only one fluctuating fermion on E2, its terms containing a fluctuating strength times a gravitino are at least second order and do not enter this first-order descendant. The result is

```math
\left(\mathcal D_b\psi^i\right)^{(1)}=-\frac{gx}{2\sqrt2}\delta^{ij}\psi_{bj}-\phi_b^{i(1)}.
\tag{E4}
```

Here $`\psi^i`$ on the left is the gauge-fixed dilatino, while $`\psi_b^i`$ on the right is the independent gravitino. The dilatino's value is zero; its full supercovariant descendant is E4.

The accepted GC18 connection formula and $`\bar T=\bar V=0`$ give

```math
\widehat R'^{(1)}_{bc}(Q)^i=\bar\nabla_b\psi_c^i-\bar\nabla_c\psi_b^i,\qquad \phi_b^{i(1)}=\frac i3\gamma^c(\bar\nabla_b\psi_c^i-\bar\nabla_c\psi_b^i)-\frac i{24}\gamma_b\gamma^{cd}(\bar\nabla_c\psi_d^i-\bar\nabla_d\psi_c^i).
\tag{E5}
```

Before inserting E4 in a contracted bilinear, lower its doublet index. Put $`m=gx/(2\sqrt2)`$. NW–SE lowering gives $`\psi_{b1}=-\psi_b^2`$ and $`\psi_{b2}=\psi_b^1`$, so E4 has upper components $`(\mathcal D_b\psi)^1=m\psi_b^2-\phi_b^1`$ and $`(\mathcal D_b\psi)^2=-m\psi_b^1-\phi_b^2`$. The lower components are $`(\mathcal D_b\psi)_1=-(\mathcal D_b\psi)^2=m\psi_b^1+\phi_b^2=m\psi_b^1-\phi_{b1}`$ and $`(\mathcal D_b\psi)_2=(\mathcal D_b\psi)^1=m\psi_b^2-\phi_b^1=m\psi_b^2-\phi_{b2}`$. Thus $`(\mathcal D_b\psi)_i=m\delta_{ij}\psi_b^j-\phi_{bi}`$. The actual bilinear in the scalar Hessian `GB08` therefore becomes

```math
-\frac i2\bar\psi_a\left(\mathcal D_b\psi\right)^{(1)}=-\frac{igx}{4\sqrt2}\delta_{ij}\bar\psi_a^i\psi_b^j+\frac i2\bar\psi_a\phi_b^{(1)}.
\tag{E6}
```

Substitute the two terms of E5 into the last term. The coefficients are $`(i/2)(i/3)=-1/6`$ and $`(i/2)(-i/24)=1/48`$. Therefore

```math
-\frac i2\bar\psi_a\left(\mathcal D_b\psi\right)^{(1)}=-\frac{igx}{4\sqrt2}\delta_{ij}\bar\psi_a^i\psi_b^j-\frac16\bar\psi_a\gamma^c\bar\nabla_b\psi_c+\frac16\bar\psi_a\gamma^c\bar\nabla_c\psi_b+\frac1{48}\bar\psi_a\gamma_b\gamma^{cd}\bar\nabla_c\psi_d-\frac1{48}\bar\psi_a\gamma_b\gamma^{cd}\bar\nabla_d\psi_c.
\tag{E7}
```

No fermion has been reordered in E6–E7, so no bilinear flip is used. This is one explicit contribution, not the complete scalar Hessian: its $`2f_{ab}`$ and $`-2\bar\psi_a\gamma_b\chi`$ contributions must also be retained in the main quadratic action. In particular, the full $`f_{ab}`$ cannot be made symmetric by importing a bosonic Ricci identity.

### 2. Why the three-form must be varied as a potential

Use the actual two-derivative term in `GB-FINAL-DENSITY`, $`-4g(G_{\mu\nu}E^{\mu\nu}/2)=-2gG_{\mu\nu}E^{\mu\nu}`$. At quadratic order its two factors are first-order bosonic fields. The accepted definition is $`E^{\mu\nu}=-\bar\varepsilon^{\mu\nu\rho\sigma\tau}E_{\rho\sigma\tau}/12`$. Substitution gives

```math
I^{(2)}=-2g\int\!d^5x\,\bar e\,G_{\mu\nu}E^{\mu\nu}=\frac g6\int\!d^5x\,\bar e\,\bar\varepsilon^{\mu\nu\rho\sigma\tau}G_{\mu\nu}E_{\rho\sigma\tau}.
\tag{E8}
```

Expand $`G_{\mu\nu}=\partial_\mu C_\nu-\partial_\nu C_\mu`$. Relabel $`\mu\leftrightarrow\nu`$ in the second summand: $`-\bar\varepsilon^{\mu\nu\rho\sigma\tau}\partial_\nu C_\mu=+\bar\varepsilon^{\mu\nu\rho\sigma\tau}\partial_\mu C_\nu`$. Thus

```math
I^{(2)}=\frac g3\int\!d^5x\,\bar e\,\bar\varepsilon^{\mu\nu\rho\sigma\tau}(\partial_\mu C_\nu)E_{\rho\sigma\tau},\qquad \delta_E I^{(2)}=\frac g3\int\!d^5x\,\bar e\,\bar\varepsilon^{\mu\nu\rho\sigma\tau}(\partial_\mu C_\nu)\delta E_{\rho\sigma\tau}.
\tag{E9}
```

For comparison with the current representative, expand the original antisymmetric contraction first:

```math
-2gG_{\mu\nu}E^{\mu\nu}=-4g(\partial_\mu C_\nu)E^{\mu\nu},\qquad \partial_\mu(\bar e C_\nu E^{\mu\nu})=\bar e(\partial_\mu C_\nu)E^{\mu\nu}+C_\nu\partial_\mu(\bar e E^{\mu\nu}).
\tag{E10}
```

Since $`P^\nu=\bar e^{-1}\partial_\mu(\bar eE^{\nu\mu})=-\bar e^{-1}\partial_\mu(\bar eE^{\mu\nu})`$, E10 implies

```math
I^{(2)}=-4g\int\!d^5x\,\bar e C_\nu P^\nu-4g\int\!d^5x\,\partial_\mu(\bar e C_\nu E^{\mu\nu}).
\tag{E11}
```

The second integral is a displayed boundary term. Varying the first with its actual constrained current gives

```math
\delta P^\mu=-\frac1{12}\bar\varepsilon^{\mu\nu\rho\sigma\tau}\partial_\nu\delta E_{\rho\sigma\tau},\qquad -4g\int\bar e C_\mu\delta P^\mu=\frac g3\int\bar e C_\mu\bar\varepsilon^{\mu\nu\rho\sigma\tau}\partial_\nu\delta E_{\rho\sigma\tau}.
\tag{E12}
```

The product rule yields the bulk expression $`-(g/3)\int\bar e\bar\varepsilon^{\mu\nu\rho\sigma\tau}(\partial_\nu C_\mu)\delta E_{\rho\sigma\tau}`$ and the boundary expression $`(g/3)\int\partial_\nu(\bar e C_\mu\bar\varepsilon^{\mu\nu\rho\sigma\tau}\delta E_{\rho\sigma\tau})`$. Relabeling $`\mu\leftrightarrow\nu`$ in the bulk gives E9, with its positive sign. Both forms of the calculation therefore give a curl equation. Treating $`P^\mu`$ as unconstrained would instead give the spurious isolated-term equation $`C_\mu=0`$. The complete three-form equation includes all other source terms; E9 is only this source term's contribution.

### 3. Two varied Majorana slots and the signed fermion equation

Let $`\theta^A`$ be independent odd real coordinates, with the discrete index also representing integration and differentiation when these are present. For the algebraic example $`I=\theta^AK_{AB}\theta^B/2`$, an even variation obeys the ordinary product rule:

```math
\delta I=\frac12\delta\theta^AK_{AB}\theta^B+\frac12\theta^AK_{AB}\delta\theta^B=\frac12\delta\theta^AK_{AB}\theta^B-\frac12\delta\theta^BK_{AB}\theta^A.
\tag{E13}
```

The minus sign moves one odd $`\delta\theta`$ across one odd $`\theta`$. Relabeling $`A\leftrightarrow B`$ in the second term gives

```math
\delta I=\frac12\delta\theta^A(K_{AB}-K_{BA})\theta^B.
\tag{E14}
```

For an antisymmetric Grassmann kernel, $`K_{BA}=-K_{AB}`$; the two slots then give $`(K_{AB}+K_{AB})/2=K_{AB}`$. In a differential bilinear, the corresponding transpose includes the explicitly performed integration by parts. The two contributions may not be removed by pretending that a Majorana bar is an independent physical fermion.

The linearity $`\overline{i\zeta}=i\bar\zeta`$ is an algebraic convention, not a statement about positivity of an inner product. Norms require the quadratic action or symplectic structure and a declared physical conjugation/reality realization. They cannot be read from that algebraic bar alone.

If a reduced fermionic eigenfield obeys $`(\not{\bar\nabla}+\mu)\Xi=0`$, multiplication by the opposite factor gives

```math
(\not{\bar\nabla}-\mu)(\not{\bar\nabla}+\mu)\Xi=((\not{\bar\nabla})^2+\mu\not{\bar\nabla}-\mu\not{\bar\nabla}-\mu^2)\Xi=((\not{\bar\nabla})^2-\mu^2)\Xi=0.
\tag{E15}
```

The cancellation requires constant $`\mu`$. The squared equation is also satisfied by a field obeying the opposite first-order equation. Therefore solving the squared equation does not select the original sign. The actual GB fermionic signed roots, constraints and eigenfields must be derived in the fermionic step documents.

### 4. A background Killing-spinor check in the accepted gauge

This check uses the accepted transformations W01, L01 and LOG-G02; it is a background calculation and does not recertify the nonlinear action. Define the displayed $`2\times2`$ matrix $`J`$ only to expose the SU(2) lowering operation:

```math
\epsilon_1=-\epsilon^2,\quad\epsilon_2=\epsilon^1,\qquad J=\begin{pmatrix}0&-1\\1&0\end{pmatrix},\qquad J^2=\begin{pmatrix}-1&0\\0&-1\end{pmatrix},\qquad L^{ij}\epsilon_j=\frac{x}{\sqrt2}(J\epsilon)^i.
\tag{E16}
```

On the background, LOG-G02b gives $`0=-Y^{ij}\epsilon_j+\eta^i`$, with $`Y^{ij}=-gL^{ij}/2`$. Therefore

```math
\eta^i=-\frac{gx}{2\sqrt2}(J\epsilon)^i,\qquad \eta_1=-\eta^2=\frac{gx}{2\sqrt2}\epsilon^1,\qquad \eta_2=\eta^1=\frac{gx}{2\sqrt2}\epsilon^2.
\tag{E17}
```

The terms proportional to $`\bar\nabla L`$, $`E_a`$ and $`T_{ab}`$ in L01 vanish because those background quantities are zero. The remaining compensator-spinor variation is

```math
\delta\varphi^i=\frac12\bar N\epsilon^i+3\bar L^{ij}\eta_j=-\frac34gx^2\epsilon^i+3\frac{x}{\sqrt2}\frac{gx}{2\sqrt2}\epsilon^i=\left(-\frac34+\frac34\right)gx^2\epsilon^i=0.
\tag{E18}
```

The source gauge is also preserved bosonically: $`\delta\sigma\propto\bar\epsilon\psi=0`$ fixes the dilatation compensation to zero; LOG-G02d gives $`\Lambda_{K\mu}=0`$ because $`\bar\phi_\mu=\bar\chi=\bar\psi_\mu=0`$; the inhomogeneous orientation variation $`i\bar\epsilon^{(i}\bar\varphi^{j)}`$ in LOG-G02e is zero, so the broken SU(2) compensator can be zero. No restriction on the spinor parameter is introduced by these bosonic gauge conditions.

W01 then gives the remaining equation

```math
0=\delta\psi_\mu^i=\bar\nabla_\mu\epsilon^i-i\gamma_\mu\eta^i=\bar\nabla_\mu\epsilon^i+\frac{igx}{2\sqrt2}\gamma_\mu(J\epsilon)^i.
\tag{E19}
```

Let $`q=gx/(2\sqrt2)`$ in the next two lines. This real constant has dimension one, and E19 is $`\bar\nabla_\mu\epsilon=-q\gamma_\mu iJ\epsilon`$. Covariant constancy of $`\gamma_\nu`$ and $`J`$ gives

```math
\bar\nabla_\mu\bar\nabla_\nu\epsilon=-q\gamma_\nu iJ\bar\nabla_\mu\epsilon=q^2\gamma_\nu\gamma_\mu(iJ)^2\epsilon=q^2\gamma_\nu\gamma_\mu\epsilon,
\tag{E20}
```

where $`(iJ)^2=i^2J^2=(-1)(-1)=1`$. Subtract the expression with $`\mu`$ and $`\nu`$ exchanged. The definition $`\gamma_{\mu\nu}=(\gamma_\mu\gamma_\nu-\gamma_\nu\gamma_\mu)/2`$ gives

```math
[\bar\nabla_\mu,\bar\nabla_\nu]\epsilon=q^2(\gamma_\nu\gamma_\mu-\gamma_\mu\gamma_\nu)\epsilon=-2q^2\gamma_{\mu\nu}\epsilon=-\frac14g^2x^2\gamma_{\mu\nu}\epsilon.
\tag{E21}
```

The curvature side of E1 is $`(k/2)\gamma_{\mu\nu}\epsilon=-(g^2x^2/4)\gamma_{\mu\nu}\epsilon`$, exactly E21. The connection in E19 therefore has zero curvature on this background and imposes no additional local algebraic projector on initial spinor data. On a simply connected local patch it has the eight real solutions allowed by the adopted symplectic-Majorana condition. A quotient or global boundary condition can restrict those solutions and has not been imposed here.

The dependent Standard-Weyl spinor has $`\delta\chi^i=\bar D\epsilon^i/4`$ on this background by W03. Its scalar is fixed by `GB11` and the accepted bosonic relation $`\Box^c\sigma=-R/8`$:

```math
\bar D=-\frac{\bar R}{32}+\frac g4\bar N+\frac{g^2x^2}{16}=\frac{10g^2x^2}{32}-\frac{3g^2x^2}{8}+\frac{g^2x^2}{16}=\frac{5-6+1}{16}g^2x^2=0.
\tag{E22}
```

Thus that dependent variation vanishes as well. This establishes the local kinematic Killing-spinor check in the accepted transformation system. It supplies no missing quadratic eigenvalue or norm.

### 5. An independent check of the scalar–metric block

The source potential extracted in Part I, Step 4, is

```math
V(L,N)=-\frac{2N^2}{L}-2gLN-4gN+2g^2L^2-\frac12g^2L^3+\lambda_{\rm GB}(-2g^2N^2-4g^3NL^2-g^4L^4).
\tag{E23}
```

This is used as an already displayed projection of the full accepted action, not as a separate bosonic action imported from a different source. The proposed new scalar–metric block has $`F(L)=L+aL^2/2`$ multiplying $`R`$, a scalar gradient coefficient $`1/L+a`$, and the curvature-squared coefficient $`\alpha=-\lambda_{\rm GB}/4`$. The complete source derivation of these derivative terms belongs to Step 6; the following calculation tests the resulting coefficients independently and derives their reduction if that block passes its source-coverage checks.

First insert the branch equation into $`F`$ and its derivative:

```math
F(x)=x+\frac12ax^2=x+(1-x)=1,\qquad F'(x)=1+ax=1+\frac{2(1-x)}x=\frac{2-x}x.
\tag{E24}
```

Write $`c=2-x`$. The candidate effective metric coefficient is $`F(x)+4\alpha k=1-\lambda_{\rm GB}k=1+ax^2/2=2-x=c`$. A useful independent check of this coefficient comes from a constant conformal perturbation $`h_{\mu\nu}=s\bar g_{\mu\nu}`$. The volume, scalar curvature and GB scalar scale as $`(1+ts)^{5/2}`$, $`(1+ts)^{-1}`$ and $`(1+ts)^{-2}`$ respectively. The second Taylor coefficients of the three density factors are $`3/8`$, $`-1/8`$ and $`15/8`$. Hence

```math
\ell^{(2)}_{h=s\bar g}=\left[\frac38F\bar R-\frac18\alpha\overline{\mathrm{GB}}+\frac{15}8V\right]s^2.
\tag{E25}
```

The accepted maximally symmetric contractions give $`\bar R=20k`$, $`\overline{\mathrm{GB}}=120k^2`$. The existing metric tadpole gives $`V=-12kF-24\alpha k^2`$. Substituting these three values into E25 gives

```math
\ell^{(2)}_{h=s\bar g}=\left[\left(\frac{60}8-\frac{180}8\right)Fk+\left(-\frac{120}8-\frac{360}8\right)\alpha k^2\right]s^2=(-15Fk-60\alpha k^2)s^2=-15kc\,s^2.
\tag{E26}
```

This checks the constant trace projection. It is not a substitute for the raw tensor derivation or an independent proof of its transverse-traceless part.

The potential checks are more direct. Differentiating each $`N`$-dependent term in E23 twice gives $`V_{NN}=-4/L-4a`$. The coefficient of $`n^2`$ includes its Taylor factor:

```math
\frac12V_{NN}\big|_{\rm branch}=-2\left(\frac1x+a\right)=-\frac{2(1+ax)}x=-\frac{2c}{x^2}.
\tag{E27}
```

For the mixed coefficient, differentiate $`V_N=-4N/L-2gL-4g-4aN-4agL^2`$ with respect to $`L`$ and then insert $`\bar N`$:

```math
V_{LN}=\frac{4N}{L^2}-2g-8agL,\qquad V_{LN}\big|_{\rm branch}=-6g-2g-8agx=-8g(1+ax)=-\frac{8gc}{x}.
\tag{E28}
```

For the $`\ell^2`$ coefficient, $`F''\bar R/2=-5ag^2x^2`$. The terms of $`V_{LL}/2`$ from $`-2N^2/L`$, $`2g^2L^2`$, $`-g^2L^3/2`$, $`-4agNL^2`$ and $`-ag^2L^4`$ are $`-2N^2/L^3`$, $`2g^2`$, $`-3g^2L/2`$, $`-4agN`$ and $`-6ag^2L^2`$. The two terms linear in $`L`$ and the two terms independent of $`L`$ have zero second derivative. Thus

```math
\left[\frac12F''\bar R+\frac12V_{LL}\right]_{\rm branch}=g^2\left[-5ax^2-\frac92x+2-\frac32x+6ax^2-6ax^2\right]=g^2(2-6x-5ax^2)=-4cg^2.
\tag{E29}
```

In the final transition, $`ax^2=2-2x`$ gives $`2-6x-5(2-2x)=-8+4x=-4c`$.

The block under examination is therefore

```math
\ell^{(2)}_{h,\ell,n}=-\frac c2h^{\mu\nu}\mathcal G^L_{\mu\nu}(h)+\frac cx\ell\,\delta R(h)+\frac c{x^2}(\bar\nabla\ell)^2-4cg^2\ell^2-\frac{8gc}{x}\ell n-\frac{2c}{x^2}n^2.
\tag{E30}
```

Here $`\mathcal G^L_{\mu\nu}=\delta R_{\mu\nu}-4kh_{\mu\nu}-\bar g_{\mu\nu}\delta R/2`$, and $`\delta R=\bar\nabla_\mu\bar\nabla_\nu h^{\mu\nu}-\bar\Box h-4kh`$. E30 has not imposed a metric gauge. The source derivation of its kinetic terms remains a requirement of the main Step 6 calculation.

At $`c\ne0`$, vary E30 with respect to $`n`$:

```math
\delta_n\ell^{(2)}=\left(-\frac{8gc}{x}\ell-\frac{4c}{x^2}n\right)\delta n,\qquad -\frac{4c}{x^2}(n+2gx\ell)=0,\qquad n=-2gx\ell.
\tag{E31}
```

The division is permitted for $`0<x<2`$. At $`x=2`$, $`c=0`$ and E31 is the zero equation, so this elimination is forbidden. Substitution into the three algebraic terms of E30 gives

```math
-4cg^2\ell^2-\frac{8gc}{x}\ell(-2gx\ell)-\frac{2c}{x^2}(-2gx\ell)^2=(-4+16-8)cg^2\ell^2=4cg^2\ell^2.
\tag{E32}
```

To remove metric–scalar mixing, set $`H_{\mu\nu}=h_{\mu\nu}+2\ell\bar g_{\mu\nu}/(3x)`$. The required conformal identities can be derived directly. For $`h_{\mu\nu}=s\bar g_{\mu\nu}`$ the linear connection is

```math
\delta\Gamma^\rho_{\mu\nu}=\tfrac12(\delta^\rho_\nu\partial_\mu s+\delta^\rho_\mu\partial_\nu s-\bar g_{\mu\nu}\partial^\rho s),\qquad \delta\Gamma^\rho_{\mu\rho}=\tfrac52\partial_\mu s.
\tag{E33}
```

Taking its two derivatives in $`\delta R_{\mu\nu}=\bar\nabla_\rho\delta\Gamma^\rho_{\mu\nu}-\bar\nabla_\nu\delta\Gamma^\rho_{\mu\rho}`$ gives

```math
\delta R_{\mu\nu}(s\bar g)=\bar\nabla_\mu\bar\nabla_\nu s-\tfrac12\bar g_{\mu\nu}\bar\Box s-\tfrac52\bar\nabla_\nu\bar\nabla_\mu s=-\tfrac32\bar\nabla_\mu\bar\nabla_\nu s-\tfrac12\bar g_{\mu\nu}\bar\Box s.
\tag{E34}
```

The equality of the two scalar Hessian orders uses torsion zero on the bosonic background. Contracting E34 and including $`\delta g^{\mu\nu}\bar R_{\mu\nu}=-20ks`$ gives $`\delta R=-4\bar\Box s-20ks`$. Inserting both contractions into the definition of $`\mathcal G^L`$ gives

```math
\mathcal G^L_{\mu\nu}(s\bar g)=-\tfrac32\bar\nabla_\mu\bar\nabla_\nu s+\tfrac32\bar g_{\mu\nu}\bar\Box s+6k\bar g_{\mu\nu}s,\qquad \bar g^{\mu\nu}\mathcal G^L_{\mu\nu}(h)=-\tfrac32\delta R(h).
\tag{E35}
```

For the trace in the second equation, $`\bar g^{\mu\nu}\delta R_{\mu\nu}=\delta R+4kh`$ gives $`(\delta R+4kh)-4kh-(5/2)\delta R=-(3/2)\delta R`$.

The quadratic Einstein bilinear is self-adjoint modulo its variational boundary term. In this conformal application, the needed equality follows by twice transferring the derivatives in $`H^{\mu\nu}\bar\nabla_\mu\bar\nabla_\nu s`$ and $`H\bar\Box s`$ onto $`H`$, with compact support. Explicitly, the product rules are $`\bar\nabla_\mu(H^{\mu\nu}\bar\nabla_\nu s)=(\bar\nabla_\mu H^{\mu\nu})\bar\nabla_\nu s+H^{\mu\nu}\bar\nabla_\mu\bar\nabla_\nu s`$ and $`\bar\nabla_\nu[s\bar\nabla_\mu H^{\mu\nu}]=(\bar\nabla_\nu s)\bar\nabla_\mu H^{\mu\nu}+s\bar\nabla_\nu\bar\nabla_\mu H^{\mu\nu}`$. Their difference isolates both boundary terms. The scalar-trace pair follows from $`\bar\nabla_\mu(H\bar\nabla^\mu s-s\bar\nabla^\mu H)=H\bar\Box s-s\bar\Box H`$. Applied to E35, these identities give $`\int\bar e H^{\mu\nu}\mathcal G^L_{\mu\nu}(s\bar g)=\int\bar e s\bar g^{\mu\nu}\mathcal G^L_{\mu\nu}(H)`$ modulo the displayed divergences.

Use $`s=-2\ell/(3x)`$ in $`h=H+s\bar g`$. The cross term from the metric bilinear is $`-cs\bar g^{\mu\nu}\mathcal G^L_{\mu\nu}(H)=(3c/2)s\delta R(H)=-(c/x)\ell\delta R(H)`$. Adding the original $`+(c/x)\ell\delta R(H)`$ gives zero. The remaining conformal part of that bilinear is

```math
-\frac c2s\bar g^{\mu\nu}\mathcal G^L_{\mu\nu}(s\bar g)=-3cs\bar\Box s-15ck s^2\doteq\frac{4c}{3x^2}(\bar\nabla\ell)^2-\frac{20ck}{3x^2}\ell^2.
\tag{E36}
```

Here the separated boundary term before dropping it is $`-3c\bar\nabla_\mu(s\bar\nabla^\mu s)`$. The conformal part of the mixing term is

```math
\frac cx\ell\delta R(s\bar g)=\frac{8c}{3x^2}\ell\bar\Box\ell+\frac{40ck}{3x^2}\ell^2\doteq-\frac{8c}{3x^2}(\bar\nabla\ell)^2+\frac{40ck}{3x^2}\ell^2.
\tag{E37}
```

The boundary term separated in E37 is $`(8c/3x^2)\bar\nabla_\mu(\ell\bar\nabla^\mu\ell)`$. The gradient coefficients in E30, E36 and E37 add to $`c(3+4-8)/(3x^2)=-c/(3x^2)`$. The algebraic coefficients add to $`4cg^2+20ck/(3x^2)=4cg^2-(10/3)cg^2=(2/3)cg^2`$. Therefore the conditional reduction of E30 is

```math
\ell^{(2)}_{H,\ell}\doteq-\frac c2H^{\mu\nu}\mathcal G^L_{\mu\nu}(H)-\frac{c}{3x^2}(\bar\nabla\ell)^2+\frac{2cg^2}{3}\ell^2,\qquad 0<x<2.
\tag{E38}
```

Vary the two scalar terms without suppressing the derivative transfer:

```math
\delta\ell^{(2)}_\ell=-\frac{2c}{3x^2}(\bar\nabla_\mu\ell)\bar\nabla^\mu\delta\ell+\frac{4cg^2}{3}\ell\delta\ell=\frac{2c}{3x^2}(\bar\Box\ell+2g^2x^2\ell)\delta\ell-\bar\nabla_\mu\left[\frac{2c}{3x^2}(\bar\nabla^\mu\ell)\delta\ell\right].
\tag{E39}
```

At $`c\ne0`$, the bulk equation is $`(\bar\Box-m_\ell^2)\ell=0`$, with $`m_\ell^2=-2g^2x^2=4k`$ and $`m_\ell^2\ell_{\rm AdS}^2=-4`$. Its local kinetic sign relative to positive Einstein normalization is positive because $`c/(3x^2)>0`$. These statements follow from E30 and its stated domain; the complete source derivation and full raw-equation reconstruction remain required before the main spectrum table promotes them to a sector PASS.

### 6. Why local mass data do not by themselves fix boundary modes

The scalar example explains the issue without imposing a boundary choice. In the Poincaré form $`ds^2=\ell_{\rm AdS}^2z^{-2}(dz^2+\eta_{mn}dx^m dx^n)`$, one has $`\bar e=\ell_{\rm AdS}^5z^{-5}`$ and $`\bar g^{zz}=z^2/\ell_{\rm AdS}^2`$. For a radial trial solution $`z^\Delta`$,

```math
\bar\Box z^\Delta=\frac{z^5}{\ell_{\rm AdS}^5}\partial_z\left(\ell_{\rm AdS}^3z^{-3}\Delta z^{\Delta-1}\right)=\frac{\Delta(\Delta-4)}{\ell_{\rm AdS}^2}z^\Delta.
\tag{E40}
```

At the E39 value, $`\Delta(\Delta-4)=-4`$, hence $`(\Delta-2)^2=0`$. The second radial solution is $`z^2\log z`$: its derivatives are $`2z\log z+z`$ and $`2\log z+3`$, and

```math
\left(z^2\partial_z^2-3z\partial_z+4\right)(z^2\log z)=z^2(2\log z+3)-3z(2z\log z+z)+4z^2\log z=(2-6+4)z^2\log z+(3-3)z^2=0.
\tag{E41}
```

The local equation admits both leading radial behaviors. Selecting allowed combinations, the boundary symplectic flux and any renormalized inner product requires boundary data. Thus the local result is useful without claiming that both behaviors belong to a specified global Hilbert space. The endpoint $`x=2`$ has a different issue: E30 itself vanishes in this block, so even the normalized equation E39 cannot be continued there by dividing by $`c`$.

## Consistency Checks

E7 has engineering dimension two: $`[g\bar\psi\psi]=1+1/2+1/2=2`$ and $`[\bar\psi\bar\nabla\psi]=1/2+1+1/2=2`$. Its free indices are precisely $`a,b`$; the contracted $`c,d`$ indices are paired. No Grassmann reordering entered that example.

E9 has a paired antisymmetric three-index potential variation; E11–E12 reproduce its coefficient and curl after the explicit integration by parts. Its BF density has dimension two because $`[g]=1`$, $`[G]=1`$ and the three-form potential has dimension zero: the term $`(g/2)E_3`$ in accepted `GB12` has the same dimension one as $`H_3`$, so $`[E_3]=[H_3]-[g]=1-1=0`$. The $`C\wedge G/2`$ and fermionic completions displayed in `GB12` do not enter the isolated quadratic BF example.

E19 has dimension $`[\epsilon]+1`$ in both terms. E21 compares curvature quantities of dimension two: $`[k]=[g^2]=2`$. E18 and E22 display the numerical cancellations and need no field equation beyond the imported branch values.

Every term of E30 has density dimension two: $`[h]=[\ell]=0`$, $`[n]=1`$ and $`[\mathcal G^L]=[\delta R]=2`$. The factor $`c`$ is dimensionless. At the two-derivative point $`a=0`$, E2 gives $`x=1`$, hence $`c=1`$, E31 gives $`n=-2g\ell`$ and E38 gives the scalar coefficients $`-1/3`$ and $`2g^2/3`$. Along the fixed-$`\lambda_{\rm GB}`$ ungauged limit $`g\to0`$, $`a\to0`$, $`x\to1`$, $`k\to0`$; E39 becomes $`\bar\Box\ell=0`$. This is a check of the displayed block, without importing a different model's spectrum.

An executed independent SymPy differentiation of E23, using $`\bar N=-3gx^2/2`$ and $`a=2(1-x)/x^2`$, returned:

```text
Fbar = 1
metric coefficient = 2 - x
ell squared = 4*g**2*(x - 2)
ell n = 8*g*(x - 2)/x
n squared = 2*(x - 2)/x**2
```

The first and last three lines check E24 and E27–E29 by a separate differentiation. The second line checks only the coefficient substitution $`F+4\alpha k`$; it does not independently derive the Lovelock tensor Hessian. E25–E26 give a separate nontrivial constant-metric scaling check. All integrations by parts in the worked reduction have explicit boundary divergences above.

## Final Result

The completed explanatory checks establish the following local background statement within the accepted transformation system:

```math
\boxed{\delta\varphi^i=0,\qquad \bar D=0,\qquad \left(\bar\nabla_\mu+\frac{igx}{2\sqrt2}\gamma_\mu J\right)\epsilon=0,\qquad k=-\frac12g^2x^2.}
\tag{E42}
```

For the scalar–metric quadratic block E30, E31–E39 give its explicit reduction on $`0<x<2`$, yielding $`m_\ell^2=4k`$; its normalization vanishes at $`x=2`$. This reduction takes E30 as its input. The [main calculation](../spectrum/README.md) supplies the source expansion, raw equations and complete local spectrum on the selected branch.

## Project-Specific Connection

The [spectrum derivation](../spectrum/README.md) presents the raw quadratic action, its equations and source coverage, followed by the field reduction, reconstructed eigenfields, kinetic signs and exceptional loci. In the examples here, E7 identifies a quadratic contribution, E9 gives its three-form variation, and E31 exhibits the branch dependence of an elimination. E42 specifies the local background supersymmetry used in the representation comparison.

## Common Confusions and Failure Modes

- A zero background strength leaves a nonzero fluctuating strength; it does not remove its potential from $`S^{(2)}`$.
- The constant $`L=x`$ still multiplies connection terms in $`\mathcal D_aL^{ij}`$, as shown explicitly by accepted `GB09`.
- $`\psi^i=0`$ is the source dilatino gauge. It is neither a gravitino gauge nor the statement $`\mathcal D_a\psi^i=0`$.
- A common determinant factor cannot be divided out until its own solutions and gauge interpretation have been established.
- Squaring a signed first-order spinor operator merges its two sign choices, as E15 demonstrates.
- The local algebraic Majorana bar and a physical positive inner product are different objects.
- Vanishing $`c`$ in a quadratic block means that block loses quadratic control. It does not by itself prove a nonlinear gauge symmetry or zero physical degrees of freedom.

## Literature Guide

### Foundational references

The working source here is the local [accepted full action](../../../../action/gb_splus_action.md), `GB01`, `GB06`–`GB14` and `GB-FINAL-DENSITY`. The background input is the [Part I catalogue](../../../background.md), Eqs. (5.23)–(5.24). These are the equations used directly in this companion.

### Practical working references

The [component dictionary](../../references/COMPONENT_CONVENTIONS.md), W01 and L01–L02, locates the common transformations at Özkan–Pang Eqs. (2.1), (2.18) and (2.19). Its LOG-G02a–e supplies the accepted gauged source-gauge compensation used in E17–E19. SC7-05–SC7-07 and GC18 supply the strengths and dependent connections. The source registry identifies the corrected paper as *Supersymmetric Completion of Gauss–Bonnet Combination in Five Dimensions*, arXiv:1301.6622v4; the [arXiv source](https://arxiv.org/abs/1301.6622v4) supplies the paper. The present calculation uses the inspected local component equations, including their explicitly recorded repairs, rather than assuming every formula is an unmodified quotation from that paper.

For the gauged realization, the same dictionary GG03–GG05 and GC01–GC24 locates Coomans–Özkan Eqs. (5.2)–(5.8). The source registry identifies arXiv:1210.4704v3; see the [arXiv source](https://arxiv.org/abs/1210.4704v3). Its alternate compensator gauge is not used as an action or mass input here.

## Convention Dependence and Scope

The source action and conventions are inputs to the kinematic Killing-spinor check. The scalar–metric reduction uses E30 as specified above. The [main calculation](../spectrum/README.md) contains the form, vector and fermion operators and their local mode analysis. Global boundary admissibility and renormalized norms depend on a specified boundary domain and boundary action.


