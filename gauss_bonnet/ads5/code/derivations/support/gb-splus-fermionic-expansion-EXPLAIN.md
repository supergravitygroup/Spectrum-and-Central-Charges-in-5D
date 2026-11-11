---
concept: Evaluated two-derivative and Weyl fermionic quadratic terms for Gauss–Bonnet on AdS₅
date: 2026-09-29
mode: project-context
project_context: Full fermionic gauged GB; Step 6 supporting calculation
citation_status: source equations identified in the Literature Guide; K-invariance scope stated in the derivation
status: two-derivative and Weyl subcalculations completed; full LOG block outside this companion
convention_lock: GB-FERMION-SPECTRUM-CONVENTIONS-v1
---

# Fermionic expansion for Gauss–Bonnet on AdS₅: two-derivative and Weyl contributions

## Executive Summary

This calculation evaluates the complete purely fermionic quadratic contribution of the two-derivative and OP-normalized Weyl pieces already collected in the accepted GB density. It retains arbitrary gravitino and compensator spinor fluctuations, expands the dependent spinors and curvatures, keeps the Majorana and SU(2) signs explicit, and displays the source terms that vanish. The separately completed [LOG and implicit-covariant collection](../../../details/fermionic_reduction.md) combines these expressions into the complete GB fermionic quadratic action. No mass or degree-of-freedom count is inferred from these two pieces alone.

## Why This Matters Here

The bosonic background does not remove the fermions hidden in $`\Box^c\sigma`$, $`\Box^cL^{ij}`$ and the primed Lorentz curvature. In the two-derivative part those terms supply a substantial part of the Rarita–Schwinger kinetic term. In the Weyl part the bosonic backgrounds $`\bar D=\bar T=\bar C=\bar R(V)=0`$ remove many candidate terms, leaving four explicit bilinears. The cancellation against LOG is derived from its source terms in FC3–FC15 of that collection and displayed entry by entry in [the component sums](../spectrum/FERMION_COMPONENT_SUMS.md).

## Prerequisites and Dependencies

The action input is [the accepted full GB density](../../../../action/gb_splus_action.md), `GB-FINAL-DENSITY`, starting with its two-derivative braces and then the Weyl terms. Its §§3.1–3.2 supply `GB07`–`GB14`. The [component dictionary](../../references/COMPONENT_CONVENTIONS.md), R01–R03, R05, W04, L01–L02 and GC22 supplies the dependent connections and full derivatives. The accepted action §3.1 explicitly incorporates the contracted compensator box identity Eq. (4.32) of [the two-derivative definition document](../../../../../common/two_derivative_action/details/construction.md). Only that derivative identity is used from the donor; its final action and spectrum are not imported.

## Problem and Target

Set the independent bosonic fluctuations to zero to extract the fermion block of $`S^{(2)}`$. This is a parity decomposition of the quadratic action, not an assertion that bosonic modes are absent. Write the independent fermions as $`\psi_\mu=t\Psi_\mu`$ and $`\varphi=t\zeta`$, and use $`L=x`$, $`N=N_0=-3gx^2/2`$, $`k=-g^2x^2/2`$. No fluctuation gauge, auxiliary equation or fermionic field equation is imposed. Compactly supported fluctuations justify discarding only the boundary divergences displayed below.

The action coefficient $`S^{(2)}`$ includes its Taylor factor. The two-derivative result below is its density with the common $`1/(2\kappa_5^2)`$ omitted. The Weyl result already contains the GB combination's multiplier $`-2`$ relative to the OP action; it must be multiplied by $`\lambda_{\rm GB}`$ exactly once.

## Convention Ledger

<!-- ASSERT_CONVENTION: natural_units=true, metric_signature=(-,+,+,+,+), source_lock=GB-FERMION-SPECTRUM-CONVENTIONS-v1, fourier_convention=not_used, renormalization_scheme=not_applicable_classical -->

We use $`\eta=(-,+,+,+,+)`$, $`\varepsilon^{01234}=1`$, $`\gamma^{01234}=i`$, $`\{\gamma^a,\gamma^b\}=2\eta^{ab}`$ and unit-weight gamma antisymmetrization. Tangent and world indices run from 0 to 4; SU(2) indices run from 1 to 2. Spinors are Grassmann odd; spacetime differentiation and parameter-contracted variations are even. The linear Majorana bar obeys $`\overline{i\Psi}=i\bar\Psi`$. Fixed-upper bilinear flips have $`t_0=t_1=1`$, $`t_2=t_3=-1`$; a contracted flip acquires the additional minus. NW–SE lowering is $`\Psi_i=\Psi^j\varepsilon_{ji}`$.

For displaying this lowering, define $`J=\left(\begin{smallmatrix}0&-1\\1&0\end{smallmatrix}\right)`$, so $`(J\Psi)^i=\delta^{ij}\Psi_j`$, $`J^T=-J`$ and $`J^2=-1`$. The masses $`m=gx/(2\sqrt2)`$ and coefficient $`u=3x/\sqrt2`$ are temporary abbreviations used below; $`um=3gx^2/4=-N_0/2`$. All barred derivatives in the final expression are the background covariant derivatives, including the vector index of $`\Psi_a`$.

## Definitions and Required Identities

Denote the actual first-order primed and unprimed gravitino curvatures by $`\mathcal R'_{ab}`$ and $`\mathcal R_{ab}`$ in this companion only. Their complete linear definitions are

```math
\mathcal R'_{ab}{}^i=\bar\nabla_a\Psi_b^i-\bar\nabla_b\Psi_a^i,\qquad \phi_a^i=\frac i3\gamma^b\mathcal R'_{ab}{}^i-\frac i{24}\gamma_a\gamma^{bc}\mathcal R'_{bc}{}^i,\qquad \mathcal R_{ab}{}^i=\mathcal R'_{ab}{}^i-i\gamma_a\phi_b^i+i\gamma_b\phi_a^i.
\tag{F1}
```

The notation $`\mathcal R_{ab}`$ here is spinor-valued and should not be confused with the primed Ricci tensor in the accepted action. We write that latter object as $`\mathcal R^{\rm Ricci}_{ab}`$ below. The conventional constraint $`\gamma^a\mathcal R_{ab}=0`$ follows from the defining connection solution F1 and is not a gauge on $`\Psi_a`$.

The source-gauge dilatino descendant $`d_a^i=(\mathcal D_a\psi^i)^{(1)}`$ and the independent compensator derivative are

```math
d_a=-mJ\Psi_a-\phi_a,\qquad (\mathcal D_a\varphi)^{(1)}=\bar\nabla_a\zeta-\frac12N_0\Psi_a-uJ\phi_a=\bar\nabla_a\zeta+uJd_a.
\tag{F2}
```

For the second equality, $`uJd_a=-umJ^2\Psi_a-uJ\phi_a=um\Psi_a-uJ\phi_a=-N_0\Psi_a/2-uJ\phi_a`$. Thus it retains the connection terms even though $`L`$ and $`N`$ are constant.

Contracting the source connection gives

```math
\gamma^a\phi_a=\frac i3\gamma^a\gamma^b\mathcal R'_{ab}-\frac{5i}{24}\gamma^{bc}\mathcal R'_{bc}=i\left(\frac13-\frac5{24}\right)\gamma^{ab}\mathcal R'_{ab}=\frac i8\gamma^{ab}\mathcal R'_{ab}.
\tag{F3}
```

The symmetric piece $`\eta^{ab}\mathcal R'_{ab}`$ vanishes by antisymmetry. The source composite is consequently

```math
\chi^i=\frac i8\gamma^ad_a^i+\frac g8\zeta^i=\frac1{64}\gamma^{ab}(\bar\nabla_a\Psi_b^i-\bar\nabla_b\Psi_a^i)-\frac{igx}{16\sqrt2}(J\gamma^a\Psi_a)^i+\frac g8\zeta^i.
\tag{F4}
```

F1 and F4 specify every dependent fermion retained in the Weyl result. They contain no new independent fields.

## Detailed Derivation

### 1. Fluctuation order of the bosonic covariants

On the pure-fermion slice, $`G=dC=0`$ but $`\widehat G^{(2)}_{ab}=i\bar\Psi_{[a}\Psi_{b]}/2`$. Likewise $`\widehat H_3^{(2)}=-3\bar\Psi_{[a}\gamma_b\Psi_{c]}/4`$, and hence $`T^{(2)}=(\widehat G^{(2)}-2\widehat H_2^{(2)})/8`$. The ordinary current $`P`$ is zero, while accepted `GB13` gives

```math
E^{a(2)}=-\frac i2\bar\Psi_b\gamma^{ba}\zeta-\frac{x}{4\sqrt2}\delta_{ij}\bar\Psi_b^i\gamma^{abc}\Psi_c^j,\qquad (\mathcal D_aL^{ij})^{(2)}=-i\bar\Psi_a^{(i}\zeta^{j)}.
\tag{F5}
```

Each right-hand side has two fluctuating fermions, so a product of two such factors starts at $`t^4`$. The background conformal Weyl curvature and $`D`$ vanish, so $`\widehat C`$, $`\widehat R(V)`$ and $`D`$ also start at order $`t^2`$ on this slice. Fermions $`\chi,\phi,\mathcal R(Q),d`$ start at order $`t`$. These order statements are used term by term below.

### 2. The two conformal boxes and the primed Ricci trace

The accepted scalar box gives, at second fermion order,

```math
(\Box^c\sigma)^{(2)}=2f_a{}^{a(2)}-\frac i2\bar\Psi_a d^a-2\bar\Psi_a\gamma^a\chi,\qquad D^{(2)}=\frac12f_a{}^{a(2)}-\frac i8\bar\Psi_a d^a-\frac12\bar\Psi_a\gamma^a\chi.
\tag{F6}
```

No strength square enters F6 because each strength on this pure-fermion slice is already order two. The linear scalars $`L,N`$ are independent and are held at their backgrounds for this block.

The referenced Eq. (4.32), divided by $`L=x`$, evaluates the compensator-box term occurring in the action:

```math
\left(x^{-1}L_{ij}\Box^cL^{ij}\right)^{(2)}=\bar\nabla_a\left[-\frac i{\sqrt2}\delta_{ij}\bar\Psi^{ai}\zeta^j\right]+6xf_a{}^{a(2)}-\frac i{\sqrt2}\delta_{ij}\bar\Psi^{ai}(\mathcal D_a\varphi^j)^{(1)}-6x\bar\Psi_a\gamma^a\chi+\frac1{\sqrt2}\delta_{ij}\bar\zeta^i\gamma^a\phi_a^j.
\tag{F7}
```

The source $`V\mathcal DL`$ term is zero because the independent $`V`$ fluctuation is zero in this fermion block. The source $`\bar\varphi\gamma\widehat G\gamma\psi`$ and $`\bar\varphi\gamma\widehat H\gamma\psi`$ terms are order $`1+2+1=4`$. The first term in F7 comes from $`\bar\nabla_a\mathcal D^aL^{ij}`$ using F5, with the background connection acting on both spinors and their displayed tangent index.

The action multiplies the sum of F7 and $`4xD^{(2)}`$ by $`-2`$. The coefficients collect as follows:

```math
\begin{aligned}
-2\big[(6x+2x)f^{(2)}+(-6x-2x)\bar\Psi\gamma\chi-\tfrac i{\sqrt2}\delta\bar\Psi^a\mathcal D_a\varphi+\tfrac1{\sqrt2}\delta\bar\zeta\gamma^a\phi_a-\tfrac{ix}{2}\bar\Psi_ad^a\big]
={}&-16xf^{(2)}+16x\bar\Psi\gamma\chi+i\sqrt2\delta\bar\Psi^a\mathcal D_a\varphi-\sqrt2\delta\bar\zeta\gamma^a\phi_a+ix\bar\Psi_ad^a.
\end{aligned}\tag{F8}
```

Here $`f^{(2)}`$ means the trace $`f_a{}^{a(2)}`$, not the symmetric part of $`f_{ab}`$. The separated divergence from F7 is $`\bar\nabla_a[i\sqrt2\delta_{ij}\bar\Psi^{ai}\zeta^j]`$.

To evaluate the trace, use the accepted R03 Ricci contraction. Its $`i\bar\phi_{[\mu}\gamma^{ab}\Psi_{\nu]}`$ term gives $`i\bar\phi_a\gamma^{ab}\Psi_b`$: the two terms in the bracket become equal after $`a\leftrightarrow b`$ and $`\gamma^{ba}=-\gamma^{ab}`$. The first $`\Psi\mathcal R(Q)`$ term gives $`-\bar\Psi_b\gamma^a\mathcal R_a{}^b/2=0`$; the second gives $`\bar\Psi_a\gamma_b\mathcal R^{ab}/2=0`$. Both use the defining gamma-trace constraint, with the contracted index displayed. The independent $`\chi`$ trace is $`-16\bar\Psi_a\gamma^a\chi`$, accepted SC7A-03. Thus

```math
\mathcal R^{\rm Ricci(2)}=R(\omega)^{(2)}+i\bar\phi_a\gamma^{ab}\Psi_b-16\bar\Psi_a\gamma^a\chi,\qquad -16xf^{(2)}=x\mathcal R^{\rm Ricci(2)}.
\tag{F9}
```

The two $`\chi`$ contributions in F8–F9 add to $`(-16x+16x)\bar\Psi\gamma\chi=0`$. With fixed vielbein, the contorsion $`K_a{}^{bc}=\bar\Psi^{[b}\gamma^{c]}\Psi_a/2+\bar\Psi^b\gamma_a\Psi^c/4`$ is second order. Its curvature variation is $`2\bar\nabla_{[a}K_{b]}{}^{cd}`$, so its Ricci trace is $`\bar\nabla_aK_b{}^{ab}-\bar\nabla_bK_a{}^{ab}=2\bar\nabla_aK_b{}^{ab}`$ after interchanging $`a,b`$ in the second term. Therefore $`xR(\omega)^{(2)}=2x\bar\nabla_aK_b{}^{ab}`$ is a displayed divergence. The remaining box contribution is

```math
\ell^{(2)}_{\rm boxes}\doteq ix\bar\phi_a\gamma^{ab}\Psi_b+i\sqrt2\delta_{ij}\bar\Psi^{ai}(\mathcal D_a\varphi^j)^{(1)}-\sqrt2\delta_{ij}\bar\zeta^i\gamma^a\phi_a^j+ix\bar\Psi_ad^a.
\tag{F10}
```

### 3. Explicit terms inside the first two-derivative brace

Contract the source scalar bracket with $`(x/\sqrt2)\delta^{ij}`$. The two $`N\zeta\zeta`$ terms have coefficients $`iN_0/(\sqrt2x^2)`$ and $`-3iN_0/(\sqrt2x^2)`$. Their sum is $`-\sqrt2 iN_0\delta_{ij}\bar\zeta^i\zeta^j/x^2`$. Raising both lower SU(2) indices introduces $`J^TJ=1`$, so no extra sign appears in that contraction.

The two explicit $`\chi\zeta`$ terms have coefficients $`-16i/\sqrt2`$ and $`+16i/\sqrt2`$. Their sum is zero. The explicit kinetic term becomes $`x^{-1}\bar\zeta\not{\mathcal D}\varphi`$. Terms containing $`E\zeta\zeta`$, $`\mathcal DL\zeta\zeta`$ or a strength times $`\zeta\zeta`$ start at order four by F5. Consequently the surviving scalar-bracket terms, before multiplication by the outer $`-2`$, are

```math
\ell_A=\frac1x\bar\zeta\not{\mathcal D}\varphi-\frac{\sqrt2iN_0}{x^2}\delta_{ij}\bar\zeta^i\zeta^j.
\tag{F11}
```

The complete spinor written inside the action's barred slot reduces to the following upper-index expression. Directly raising the source lower-index expression with $`\varepsilon^{ij}`$ gives

```math
\lambda^i=-\frac{2i}{x}(\not{\mathcal D}\varphi)^i-i\sqrt2(J\gamma^ad_a)^i+\sqrt2\left(\frac{N_0}{x^2}-g\right)(J\zeta)^i=-\frac{2i}{x}\not{\bar\nabla}\zeta^i-4i\sqrt2(J\gamma^ad_a)^i+\sqrt2\left(\frac{N_0}{x^2}-g\right)(J\zeta)^i.
\tag{F12}
```

The coefficient in the second expression is $`2u/x+\sqrt2=6/\sqrt2+\sqrt2=4\sqrt2`$, using F2. No new composite map is assumed here: F12 is the linear evaluation of the spinor already printed in `GB-FINAL-DENSITY`.

The charge-conjugation identities imply $`\overline{\gamma^a\zeta}=\bar\zeta\gamma^a`$, while the linear bar leaves the factors of $`i`$ unchanged. The contraction of a barred $`J`$ is $`J^TJ=1`$. Substituting F12 in $`i\bar\lambda\zeta`$ therefore gives

```math
i\bar\lambda\zeta=\frac2x(\bar\nabla_a\bar\zeta)\gamma^a\zeta+4\sqrt2\delta_{ij}\bar d_a^i\gamma^a\zeta^j+i\sqrt2\left(\frac{N_0}{x^2}-g\right)\delta_{ij}\bar\zeta^i\zeta^j.
\tag{F13}
```

The first term is $`-(2/x)\bar\zeta\not{\bar\nabla}\zeta+(2/x)\bar\nabla_a(\bar\zeta\gamma^a\zeta)`$. In F11, $`\bar\zeta\gamma^a(Jd_a)`$ with its ordinary SU(2) contraction is $`-\delta_{ij}\bar\zeta^i\gamma^ad_a^j`$. Fixed-upper rank-one flip has positive sign, so it equals $`-\delta_{ij}\bar d_a^i\gamma^a\zeta^j`$. Thus adding F11 and F13 gives

```math
\ell_A+i\bar\lambda\zeta\doteq-\frac1x\bar\zeta\not{\bar\nabla}\zeta+\left(4\sqrt2-\frac3{\sqrt2}\right)\delta_{ij}\bar d_a^i\gamma^a\zeta^j-\sqrt2ig\delta_{ij}\bar\zeta^i\zeta^j=-\frac1x\bar\zeta\not{\bar\nabla}\zeta+\frac5{\sqrt2}\delta\bar d\gamma\zeta-\sqrt2ig\delta\bar\zeta\zeta.
\tag{F14}
```

The gravitino–$`\lambda`$ term inside the same brace is $`-x\delta_{ij}\bar\Psi_a^i\gamma^a\lambda^j/(2\sqrt2)`$. Substituting each of the three terms of F12 gives

```math
\ell_{\Psi\lambda}=\frac i{\sqrt2}\delta_{ij}\bar\Psi_a^i\gamma^a\not{\bar\nabla}\zeta^j+2ix\bar\Psi_a\gamma^a\gamma^bd_b+\left(\frac{gx}{2}-\frac{N_0}{2x}\right)\bar\Psi_a\gamma^a\zeta.
\tag{F15}
```

The source $`\rho N`$ product contains three quadratic terms:

```math
\ell_{\rho N}^{(2)}=\frac{N_0}{x}\bar\Psi_a\gamma^a\zeta+\frac{iN_0}{2\sqrt2}\delta_{ij}\bar\Psi_a^i\gamma^{ab}\Psi_b^j+\frac{iN_0}{\sqrt2x^2}\delta_{ij}\bar\zeta^i\zeta^j.
\tag{F16}
```

All terms multiplying the independent two-form $`E^{\mu\nu}`$ are zero on the pure-fermion slice, since it is the potential dual and is held at zero. It is not the bilinear-containing vector $`E_a`$ of F5. The $`\mathcal DL\mathcal DL`$, $`E^2`$, $`E\mathcal DL`$ and strength-square terms in the first bracket start at fourth order. This accounts for the bosonic-looking terms not included in F10–F16.

Finally, the explicit gauging brace outside the outer $`-2`$ contributes

```math
\ell_{g}^{(2)}=-2g\bar\Psi_a\gamma^a\zeta-\frac{igx}{\sqrt2}\delta_{ij}\bar\Psi_a^i\gamma^{ab}\Psi_b^j.
\tag{F17}
```

### 4. Collect and eliminate the dependent spinors

The total is F10 minus twice F14–F16 plus F17. The $`\zeta^2`$ coefficient becomes $`2\sqrt2ig-\sqrt2iN_0/x^2=2\sqrt2ig+3ig/\sqrt2=7ig/\sqrt2`$. The explicit $`\Psi\gamma\zeta`$ coefficient before evaluating the box terms is $`(N_0/x-gx)-2N_0/x-2g=-N_0/x-gx-2g`$. The explicit $`\Psi\gamma^{ab}\Psi`$ coefficient is $`-i(N_0+gx)/\sqrt2`$.

Insert F2 into the $`\mathcal D\varphi`$ term of F10. It gives $`i\sqrt2\delta\bar\Psi^a\bar\nabla_a\zeta+3ix\bar\Psi^ad_a`$. Combined with F10's last term, this is $`i\sqrt2\delta\bar\Psi^a\bar\nabla_a\zeta+4ix\bar\Psi^ad_a`$. Also insert $`\phi_a=-d_a-mJ\Psi_a`$ into the third term of F10. It gives $`+\sqrt2\delta\bar d_a\gamma^a\zeta-\sqrt2m\bar\Psi_a\gamma^a\zeta`$, where the second sign uses the contracted rank-one flip. The coefficient of $`\delta\bar d\gamma\zeta`$ is therefore $`-5\sqrt2+\sqrt2=-4\sqrt2`$.

For the remaining $`\phi`$ term, the same substitution gives

```math
ix\bar\phi_a\gamma^{ab}\Psi_b=-ix\bar d_a\gamma^{ab}\Psi_b-imx\delta_{ij}\bar\Psi_a^i\gamma^{ab}\Psi_b^j.
\tag{F18}
```

Now substitute $`d_a=-mJ\Psi_a-\phi_a`$ in all three gravitino terms $`4ix\bar\Psi^ad_a-4ix\bar\Psi_a\gamma^a\gamma^bd_b-ix\bar d_a\gamma^{ab}\Psi_b`$. Their algebraic part is

```math
4imx\delta\bar\Psi^a\Psi_a-4imx\delta\bar\Psi_a\gamma^a\gamma^b\Psi_b+imx\delta\bar\Psi_a\gamma^{ab}\Psi_b=-3imx\delta\bar\Psi_a\gamma^{ab}\Psi_b.
\tag{F19}
```

The scalar contraction cancels because $`\gamma^a\gamma^b=\gamma^{ab}+\eta^{ab}`$. Their differential part is $`4ix\bar\Psi_a\gamma^{ab}\phi_b+ix\bar\phi_a\gamma^{ab}\Psi_b`$. The contracted rank-two flip is positive, and relabeling $`a\leftrightarrow b`$ yields $`\bar\phi_a\gamma^{ab}\Psi_b=-\bar\Psi_a\gamma^{ab}\phi_b`$. The differential part is therefore $`3ix\bar\Psi_a\gamma^{ab}\phi_b`$.

Substitute F1. The first term has coefficient $`(3ix)(i/3)=-x`$ and the second has coefficient $`(3ix)(-i/24)=x/8`$. With $`\gamma^{ab}\gamma_b=4\gamma^a`$,

```math
3ix\bar\Psi_a\gamma^{ab}\phi_b=-x\bar\Psi_a\gamma^{ab}\gamma^c\mathcal R'_{bc}+\frac x2\bar\Psi_a\gamma^a\gamma^{cd}\mathcal R'_{cd}=-\frac x2\bar\Psi_a\gamma^{abc}\mathcal R'_{bc}=-x\bar\Psi_a\gamma^{abc}\bar\nabla_b\Psi_c.
\tag{F20}
```

For the middle equality, expand $`\gamma^{ab}\gamma^c=\gamma^{abc}+\eta^{bc}\gamma^a-\eta^{ac}\gamma^b`$ and $`\gamma^a\gamma^{cd}=\gamma^{acd}+\eta^{ac}\gamma^d-\eta^{ad}\gamma^c`$. The $`\eta^{bc}\mathcal R'_{bc}`$ term is zero. The remaining rank-one terms are $`x\bar\Psi^c\gamma^b\mathcal R'_{bc}+x\bar\Psi^c\gamma^d\mathcal R'_{cd}=0`$ after $`d\to b`$ and $`\mathcal R'_{cb}=-\mathcal R'_{bc}`$. The rank-three coefficients are $`-x+x/2=-x/2`$. Antisymmetry of $`\gamma^{abc}`$ then doubles the first derivative in $`\mathcal R'_{bc}`$, producing the last expression in F20.

The remaining mixed term is $`-4\sqrt2\delta\bar d_a\gamma^a\zeta=-4\sqrt2m\bar\Psi_a\gamma^a\zeta+4\sqrt2\delta\bar\phi_a\gamma^a\zeta`$. The first part is $`-2gx\bar\Psi\gamma\zeta`$. For the second, taking the linear Majorana bar of F3 gives $`\bar\phi_a\gamma^a=-i\overline{\mathcal R'_{ab}}\gamma^{ab}/8`$, because $`\overline{\gamma^{ab}\xi}=-\bar\xi\gamma^{ab}`$. Thus

```math
4\sqrt2\delta\bar\phi_a\gamma^a\zeta=-i\sqrt2\delta(\bar\nabla_a\bar\Psi_b)\gamma^{ab}\zeta\doteq+i\sqrt2\delta\bar\Psi_b\gamma^{ab}\bar\nabla_a\zeta=-i\sqrt2\delta\bar\Psi_a\gamma^{ab}\bar\nabla_b\zeta.
\tag{F21}
```

The boundary term isolated here is $`-i\sqrt2\bar\nabla_a(\delta_{ij}\bar\Psi_b^i\gamma^{ab}\zeta^j)`$. The other two mixed derivative terms combine as $`-i\sqrt2\delta\bar\Psi_a\gamma^a\gamma^b\bar\nabla_b\zeta+i\sqrt2\delta\bar\Psi_a\bar\nabla^a\zeta=-i\sqrt2\delta\bar\Psi_a\gamma^{ab}\bar\nabla_b\zeta`$. Together with F21 their coefficient is $`-2i\sqrt2`$.

The final algebraic coefficients can now be collected explicitly. The gravitino coefficient is $`-i(N_0+gx)/\sqrt2-imx-3imx=-i[N_0+gx+2gx^2]/\sqrt2=-igx(x+2)/(2\sqrt2)`$. The mixed coefficient is $`-N_0/x-gx-2g-\sqrt2m-4\sqrt2m=-N_0/x-(7/2)gx-2g=-2g(x+1)`$, using $`N_0=-3gx^2/2`$. The result is

```math
\begin{aligned}
\ell_{2\partial,F}^{(2)}\doteq{}&-x\bar\Psi_a\gamma^{abc}\bar\nabla_b\Psi_c+\frac2x\bar\zeta\not{\bar\nabla}\zeta-2\sqrt2i\delta_{ij}\bar\Psi_a^i\gamma^{ab}\bar\nabla_b\zeta^j\\
&-\frac{igx(x+2)}{2\sqrt2}\delta_{ij}\bar\Psi_a^i\gamma^{ab}\Psi_b^j-2g(x+1)\bar\Psi_a\gamma^a\zeta+\frac{7ig}{\sqrt2}\delta_{ij}\bar\zeta^i\zeta^j.
\end{aligned}\tag{F22}
```

### 5. Full derivative evaluation in the Weyl terms

GC22 writes $`\mathcal D_c\widehat R_{ab}(Q)`$ as the ordinary spinor/two-tensor derivative minus the Q/S transformations. The Q coefficients are $`\widehat R(V)`$, $`\widehat C`$ and $`\mathcal DT`$; each has zero bosonic value. The S coefficients are $`T`$; these also vanish. $`\widehat R(Q)`$ is K invariant, so its first full derivative in GC22 has no explicit $`f`$-connection term. Hence

```math
(\mathcal D_c\widehat R_{ab}(Q))^{(1)}=\bar\nabla_c\mathcal R_{ab},\qquad \bar\nabla_c\mathcal R_{ab}=\partial_c\mathcal R_{ab}+\tfrac14\bar\omega_c{}^{de}\gamma_{de}\mathcal R_{ab}+\bar\omega_{ca}{}^d\mathcal R_{db}+\bar\omega_{cb}{}^d\mathcal R_{ad}.
\tag{F23}
```

This is not a scalar or spinor-only derivative: both tensor-index connections are present. For $`\chi`$, W04 gives the Q correction $`-\Psi_c\bar D/4+\gamma\cdot\bar R(V)\Psi_c/64`$, the $`\mathcal DT`$ corrections, the quadratic-$`T`$ corrections and the S correction $`-\gamma\cdot\bar T\,\phi_c/4`$. Their background coefficients are respectively $`0,0,0,0,0`$. Therefore

```math
(\mathcal D_c\chi)^{(1)}=\bar\nabla_c\chi.
\tag{F24}
```

The four Weyl source contributions at order two are consequently

```math
\ell_{W\to\mathrm{GB},F}^{(2)}=-\frac32\overline{\mathcal R_{ab}}\not{\bar\nabla}\mathcal R^{ab}+\frac{512}{3}\bar\chi\not{\bar\nabla}\chi+\frac{igx}{4\sqrt2}\delta_{ij}\overline{\mathcal R_{ab}{}^i}\mathcal R^{abj}+\frac{256igx}{3\sqrt2}\delta_{ij}\bar\chi^i\chi^j.
\tag{F25}
```

The symmetrized lower-doublet slots in the last two source terms contract with symmetric $`L^{ij}=x\delta^{ij}/\sqrt2`$. The two symmetrized terms have equal contractions, cancelling their $`1/2`$; raising both lower indices again uses $`J^TJ=1`$. This gives exactly the displayed coefficients, with no extra factor of two.

For an entirely explicit curvature definition without $`\phi`$, substitute F1 once:

```math
\mathcal R_{ab}=\mathcal R'_{ab}+\frac13\gamma_a\gamma^c\mathcal R'_{bc}-\frac13\gamma_b\gamma^c\mathcal R'_{ac}-\frac1{12}\gamma_{ab}\gamma^{cd}\mathcal R'_{cd},\qquad \mathcal R'_{ab}=\bar\nabla_a\Psi_b-\bar\nabla_b\Psi_a.
\tag{F26}
```

The last coefficient is $`(-i)(-i)/24`$ multiplying $`(\gamma_a\gamma_b-\gamma_b\gamma_a)=2\gamma_{ab}`$, hence $`-2/24=-1/12`$. Together F4 and F26 make F25 an evaluated quadratic expression in the two independent fermions through familiar dependent curvatures; no unknown derivative law remains in this Weyl block.

## Consistency Checks

Every term of F22 has engineering dimension two: the derivative terms have $`1/2+1+1/2=2`$, and the algebraic terms have $`[g]+1/2+1/2=2`$. Every term of F25 has dimension four: $`[\mathcal R]=[\chi]=3/2`$ gives $`3/2+1+3/2=4`$, and the mass terms have $`1+3/2+3/2=4`$. Multiplication by $`\lambda_{\rm GB}`$ gives density dimension two. Each final term is even in Grassmann parity, with its source doublet contractions retained.

The explicit $`\Psi`$–$`\zeta`$ mixing in F22 supplies a useful two-derivative gauge check at $`a=0`$, where $`x=1`$ and that action itself has vanishing tadpoles. The accepted background gauge-preserving transformation is $`\delta\Psi_a=\bar\nabla_a\epsilon+im\gamma_aJ\epsilon`$, $`\delta\zeta=0`$, $`m=g/(2\sqrt2)`$. Vary the derivative mixing term and integrate its parameter derivative once. The antisymmetric gamma matrix selects the commutator, so its curvature contribution is

```math
2\sqrt2i\delta_{ij}\bar\epsilon^i\gamma^{ab}\bar\nabla_a\bar\nabla_b\zeta^j=\sqrt2i\delta_{ij}\bar\epsilon^i\gamma^{ab}[\bar\nabla_a,\bar\nabla_b]\zeta^j=-10\sqrt2ik\delta_{ij}\bar\epsilon^i\zeta^j.
\tag{F27}
```

Here $`[\bar\nabla_a,\bar\nabla_b]\zeta=k\gamma_{ab}\zeta/2`$ and $`\gamma^{ab}\gamma_{ab}=-5\cdot4=-20`$. The latter follows by expanding $`\gamma^{ab}=\gamma^a\gamma^b-\eta^{ab}`$: $`\gamma^a\gamma^b\gamma_a\gamma_b-2\gamma^a\gamma_a+5=(2-5)5-10+5=-20`$.

The mass part of $`\delta\Psi`$ in the derivative mixing yields $`-8\sqrt2m\bar\epsilon\not{\bar\nabla}\zeta`$, because $`\gamma_a\gamma^{ab}=4\gamma^b`$ and $`J^T=-J`$. Varying the algebraic mixing $`-4g\bar\Psi_a\gamma^a\zeta`$ gives $`+4g\bar\epsilon\not{\bar\nabla}\zeta-20igm\delta_{ij}\bar\epsilon^i\zeta^j`$ after integrating its derivative term. The two coefficients therefore vanish:

```math
-8\sqrt2m+4g=-8\sqrt2\frac{g}{2\sqrt2}+4g=0,\qquad -10\sqrt2ik-20igm=5\sqrt2ig^2-\frac{10ig^2}{\sqrt2}=0.
\tag{F28}
```

The boundary terms dropped in this check are $`-2\sqrt2i\bar\nabla_a(\delta_{ij}\bar\epsilon^i\gamma^{ab}\bar\nabla_b\zeta^j)-4g\bar\nabla_a(\bar\epsilon\gamma^a\zeta)`$. This is a check of the mixed block, not of the full GB Noether identity. At general $`x`$, the two-derivative action alone is not stationary on the selected AdS₅ branch, so the vanishing of its isolated gauge residual is not a required check.

Setting $`\Psi=0`$ directly in F4 yields $`\chi=g\zeta/8`$ and $`\mathcal R=0`$. F25 then reduces to $`[(512/3)(g^2/64)]\bar\zeta\not{\bar\nabla}\zeta+[(256igx)/(3\sqrt2)](g^2/64)\delta\bar\zeta\zeta=(8g^2/3)\bar\zeta\not{\bar\nabla}\zeta+[4ig^3x/(3\sqrt2)]\delta\bar\zeta\zeta`$. This gives a simple nontrivial coefficient check available for combination with the LOG contribution, without inferring the other entries from it.

## Final Result

The completed subcalculation is

```math
\boxed{S_{2\partial+W,F}^{(2)}\doteq\frac1{2\kappa_5^2}\int d^5x\,\bar e\left[\ell_{2\partial,F}^{(2)}+\lambda_{\rm GB}\ell_{W\to\mathrm{GB},F}^{(2)}\right],}
\tag{F29}
```

where the explicit six-term two-derivative expression is F22, the explicit four-term Weyl expression is F25, and their dependent fermions are fully specified by F1/F4/F26. This result retains arbitrary $`\Psi_a`$ and $`\zeta`$ and all first-order and third-order operators supplied by these pieces. It has not used a gamma-trace or divergence gauge and does not eliminate an independent fermion.

## Project-Specific Connection

The main Step 6 file adds the LOG explicit terms and its fermions concealed in bosonic covariants to these source contributions and collects all derivative orders. Step 7 varies that complete sum with both Majorana slots retained. The source-gauge derivative cancellations in F8–F10 and the full derivative evaluation in F23–F24 are useful intermediate checks of that larger calculation.

## Common Confusions and Failure Modes

The ordinary $`E^{\mu\nu}`$ potential dual is zero on this pure-fermion slice; the supercovariant $`E_a`$ is the bilinear F5 and is not zero. The source dilatino is zero but its descendant $`d_a`$ is F2. The primed Lorentz Ricci tensor was traced with its ordered indices in F9; no symmetry of its full $`f_{ab}`$ was assumed. Neither the four Weyl terms alone nor the two-derivative action evaluated at $`x\ne1`$ is the complete GB fermion theory.

## Literature Guide

### Foundational and practical inputs

Use the accepted action `GB-FINAL-DENSITY` and its definitions `GB07`–`GB14`, then the component dictionary R01–R03, W04, L02, GC22. The isolated additional derivative identity is the Eq. (4.32) explicitly incorporated by the accepted action §3.1. The earlier [method explanation](gb-splus-spectrum-method-EXPLAIN.md) provides the local source reading links and the detailed background Killing-spinor check. No external action or previously calculated fermionic spectrum has entered F22 or F25.

### Related calculations

The full LOG contribution, its higher ordered derivatives, the total GB fermionic equations, residual gauge reduction, eigenfields and local kinetic signs are recorded in the completed [main calculation](../spectrum/README.md). This companion's completed two-derivative and Weyl subcalculations do not stand in for them.

## Convention Dependence and Scope

The calculation uses the accepted source action and its linear Majorana/SU(2) conventions throughout. It establishes these two source contributions through quadratic fluctuation order for Gauss–Bonnet on AdS₅. The companion isolates these two source contributions; the combined action and its spectrum are given in the main calculation cited above. In particular, the Weyl block's third derivatives cannot be deleted on the expectation that the complete Gauss–Bonnet combination cancels them.

## Combined quadratic action

The main calculation supplies the independent LOG collection, cancellation coefficients, unprojected equations and local supersymmetry identity before selecting fluctuation gauges.

## Weyl Source-Term Coverage

The following ledger uses the source IDs from the accepted action assembly solely to locate terms. Coefficients are those already printed in the accepted density. A zero entry records the evaluated fluctuation-order reason; the four surviving entries point to F25. The ledger does not audit or reconstruct the input action.

Terms with two derivatives on $`T`$ also have zero bosonic descendants here: the backgrounds $`T`$, $`\mathcal DT`$, $`\chi`$, $`\widehat R(Q)`$ and the Q/S coefficients $`D`$, $`\widehat R(V)`$ and $`\widehat C`$ all vanish. Thus the extra derivatives do not create a nonzero degree-zero factor on this background.

| Source ID | Actual source structure | Quadratic contribution / reason |
|---|---|---|
| Weyl_sigma_N:1 | $`\widehat C_{abcd}\widehat C^{abcd}`$ | $`2+2=4`$ |
| Weyl_sigma_N:2 | $`D^2`$ | $`2+2=4`$ |
| Weyl_sigma_N:3 | $`DT_{ab}T^{ab}`$ | $`2+2+2=6`$ |
| Weyl_sigma_N:4 | $`\widehat C_{abcd}T^{ab}T^{cd}`$ | $`2+2+2=6`$ |
| Weyl_sigma_N:5 | $`\widehat R_{ab}{}^{ij}(V)\widehat R^{ab}{}_{ij}(V)`$ | $`2+2=4`$ |
| Weyl_sigma_N:6 | $`(\mathcal D_aT_{bc})(\mathcal D^aT^{bc})`$ | $`2+2=4`$ |
| Weyl_sigma_N:7 | $`(\mathcal D_bT_{ac})(\mathcal D^aT^{bc})`$ | $`2+2=4`$ |
| Weyl_sigma_N:8 | $`T_{ab}\mathcal D^b\mathcal D_cT^{ac}`$ | $`2+2=4`$ |
| Weyl_sigma_N:9 | $`\varepsilon_{abcde}T^{ab}T^{cd}\mathcal D_fT^{ef}`$ | $`2+2+2=6`$ |
| Weyl_sigma_N:10 | $`T_{ab}T^{bc}T_{cd}T^{da}`$ | $`2+2+2+2=8`$ |
| Weyl_sigma_N:11 | $`(T_{ab}T^{ab})^2`$ | $`4+4=8`$ |
| Weyl_sigma_N:12 | $`\overline{\widehat R_{ab}(Q)}\gamma^c\mathcal D_c\widehat R^{ab}(Q)`$ | F25, first term: $`1+1=2`$ |
| Weyl_sigma_N:13 | $`T^{ab}\overline{\widehat R_{ca}(Q)}\widehat R^c{}_{b}(Q)`$ | $`2+1+1=4`$ |
| Weyl_sigma_N:14 | $`T^{ab}\overline{\widehat R_{ab}(Q)}\chi`$ | $`2+1+1=4`$ |
| Weyl_sigma_N:15 | $`\bar\chi\gamma^a\mathcal D_a\chi`$ | F25, second term: $`1+1=2`$ |
| Weyl_C_E:1 | $`C_a\varepsilon^{abcde}\widehat C_{bcfg}\widehat C_{de}{}^{fg}`$ | $`C_a=0`$ on the pure-fermion slice, so the whole term is zero |
| Weyl_C_E:2 | $`C_a\varepsilon^{abcde}\widehat R(V)_{bc}{}^{ij}\widehat R(V)_{de\,ij}`$ | $`C_a=0`$ on the pure-fermion slice, so the whole term is zero |
| Weyl_C_E:3 | $`C_a\mathcal D_b\Big[4\widehat C^{ab}{}_{cd}T^{cd}-\frac{64}{3}DT^{ab}-\frac{128}{9}T^{ab}T_{cd}T^{cd}-\frac{512}{3}T^a{}_cT^{cd}T^b{}_d+8i\overline{\widehat R(Q)^{ab}}\chi-\frac{64i}{3}\bar\chi\gamma^{ab}\chi\Big]`$ | $`C_a=0`$ on the pure-fermion slice, so the whole term is zero |
| Weyl_C_E:4 | $`C_a\varepsilon^a{}_{bcde}\mathcal D^b\Big[\frac23T^{cf}\mathcal D_fT^{de}+T^c{}_f\mathcal D^dT^{ef}\Big]`$ | $`C_a=0`$ on the pure-fermion slice, so the whole term is zero |
| Weyl_C_E:5 | $`C_aT^{cd}\overline{\widehat R(Q)_{ec}}\gamma^a\widehat R(Q)^e{}_d`$ | $`C_a=0`$ on the pure-fermion slice, so the whole term is zero |
| Weyl_C_E:6 | $`C_aT_c{}^d\overline{\widehat R(Q)_e{}^a}\gamma^c\widehat R(Q)^e{}_d`$ | $`C_a=0`$ on the pure-fermion slice, so the whole term is zero |
| Weyl_C_E:7 | $`C_aT^c{}_d\overline{\widehat R(Q)^a{}_c}\gamma^d\chi`$ | $`C_a=0`$ on the pure-fermion slice, so the whole term is zero |
| Weyl_C_E:8 | $`C_aT^{cd}\overline{\widehat R(Q)_{cd}}\gamma^a\chi`$ | $`C_a=0`$ on the pure-fermion slice, so the whole term is zero |
| Weyl_C_E:9 | $`C_a\overline{\widehat R(Q)_{cd}}\mathcal D^a\widehat R(Q)^{cd}`$ | $`C_a=0`$ on the pure-fermion slice, so the whole term is zero |
| Weyl_C_E:10 | $`C_a\overline{\widehat R(Q)_{cd}}\mathcal D^c\widehat R(Q)^{da}`$ | $`C_a=0`$ on the pure-fermion slice, so the whole term is zero |
| Weyl_gravitino:1 | $`\bar\psi_m\gamma^m\gamma_{cd}\widehat R_{ab}(Q)\widehat C^{abcd}`$ | $`1+1+2=4`$ |
| Weyl_gravitino:2 | $`\bar\psi_m\gamma^m\gamma_c\widehat R_{ab}(Q)\mathcal D^aT^{bc}`$ | $`1+1+2=4`$ |
| Weyl_gravitino:3 | $`\bar\psi_m\gamma^m\chi D`$ | $`1+1+2=4`$ |
| Weyl_gravitino:4 | $`\bar\psi_m\gamma^m\gamma_c\mathcal D^c\widehat R_{ab}(Q)T^{ab}`$ | $`1+1+2=4`$ |
| Weyl_gravitino:5 | $`\bar\psi_m\gamma^m\gamma_a\mathcal D^c\widehat R_{bc}(Q)T^{ab}`$ | $`1+1+2=4`$ |
| Weyl_gravitino:6 | $`\bar\psi_m\gamma^m\gamma^{ab}\gamma^c\chi\mathcal D_aT_{bc}`$ | $`1+1+2=4`$ |
| Weyl_gravitino:7 | $`\bar\psi_m\gamma^m\chi T^2`$ | $`1+1+2+2=6`$ |
| Weyl_gravitino:8 | $`\bar\psi_m\gamma^m\gamma_a\mathcal D_b\chi T^{ab}`$ | $`1+1+2=4`$ |
| Weyl_gravitino:9 | $`\bar\psi_m\gamma^m\gamma_{ab}\widehat R_{cd}(Q)T^{ab}T^{cd}`$ | $`1+1+2+2=6`$ |
| Weyl_gravitino:10 | $`\bar\psi_m^i\gamma^m\widehat R^{ab}{}_{ij}(V)\widehat R_{ab}{}^j(Q)`$ | $`1+1+2=4`$ |
| Weyl_gravitino:11 | $`\bar\psi_m^i\gamma^m\widehat R^{ab}{}_{ij}(V)\gamma_{ab}\chi^j`$ | $`1+1+2=4`$ |
| Weyl_C_gravitino:1 | $`C_m\bar\psi_n\gamma^{nm}\gamma_{cd}\widehat R_{ab}(Q)\widehat C^{abcd}`$ | $`C_a=0`$ on the pure-fermion slice, so the whole term is zero |
| Weyl_C_gravitino:2 | $`C_m\bar\psi_n\gamma^{nm}\gamma_c\widehat R_{ab}(Q)\mathcal D^aT^{bc}`$ | $`C_a=0`$ on the pure-fermion slice, so the whole term is zero |
| Weyl_C_gravitino:3 | $`C_m\bar\psi_n\gamma^{nm}\chi D`$ | $`C_a=0`$ on the pure-fermion slice, so the whole term is zero |
| Weyl_C_gravitino:4 | $`C_m\bar\psi_n\gamma^{nm}\gamma_c\mathcal D^c\widehat R_{ab}(Q)T^{ab}`$ | $`C_a=0`$ on the pure-fermion slice, so the whole term is zero |
| Weyl_C_gravitino:5 | $`C_m\bar\psi_n\gamma^{nm}\gamma_a\mathcal D^c\widehat R_{bc}(Q)T^{ab}`$ | $`C_a=0`$ on the pure-fermion slice, so the whole term is zero |
| Weyl_C_gravitino:6 | $`C_m\bar\psi_n\gamma^{nm}\gamma^{ab}\gamma^c\chi\mathcal D_aT_{bc}`$ | $`C_a=0`$ on the pure-fermion slice, so the whole term is zero |
| Weyl_C_gravitino:7 | $`C_m\bar\psi_n\gamma^{nm}\chi T^2`$ | $`C_a=0`$ on the pure-fermion slice, so the whole term is zero |
| Weyl_C_gravitino:8 | $`C_m\bar\psi_n\gamma^{nm}\gamma_a\mathcal D_b\chi T^{ab}`$ | $`C_a=0`$ on the pure-fermion slice, so the whole term is zero |
| Weyl_C_gravitino:9 | $`C_m\bar\psi_n\gamma^{nm}\gamma_{ab}\widehat R_{cd}(Q)T^{ab}T^{cd}`$ | $`C_a=0`$ on the pure-fermion slice, so the whole term is zero |
| Weyl_C_gravitino:10 | $`C_m\bar\psi_n^i\gamma^{nm}\widehat R^{ab}{}_{ij}(V)\widehat R_{ab}{}^j(Q)`$ | $`C_a=0`$ on the pure-fermion slice, so the whole term is zero |
| Weyl_C_gravitino:11 | $`C_m\bar\psi_n^i\gamma^{nm}\widehat R^{ab}{}_{ij}(V)\gamma_{ab}\chi^j`$ | $`C_a=0`$ on the pure-fermion slice, so the whole term is zero |
| Weyl_Y:4 | $`gL_c^{ij}\overline{\widehat R}_{ab(i}(Q)\widehat R_{j)}{}^{ab}(Q)`$ | F25, third term: $`0+1+1=2`$ |
| Weyl_Y:5 | $`gL_c^{ij}\bar\chi_{(i}\chi_{j)}`$ | F25, fourth term: $`0+1+1=2`$ |
| Weyl_Y:6 | $`gL_c^{ij}\widehat R_{ab\,ij}(V)T^{ab}`$ | $`0+2+2=4`$ |
| Weyl_two_gravitinos:3 | $`(\bar\psi_m^i\gamma^{mn}\psi_n^j)\big(\widehat R_{ab\,ij}(V)T^{ab}\big)`$ | $`1+1+2+2=6`$ |
| Weyl_C_two_gravitinos:3 | $`C_m(\bar\psi_n^i\gamma^{mnp}\psi_p^j)\big(\widehat R_{ab\,ij}(V)T^{ab}\big)`$ | $`C_a=0`$ on the pure-fermion slice, so the whole term is zero |

## Addendum: Independent Diagonalization Check of the Proposed Total Raw Block

**Scope of the comparison.** This addendum checks the algebraic reduction of the total raw fermionic block proposed by the main calculation. The source-collection dependency is supplied by [FC3–FC15](../../../details/fermionic_reduction.md) and [the component sums](../spectrum/FERMION_COMPONENT_SUMS.md). The two-derivative and Weyl results F22 and F25 above do not alone establish this total block. The calculation here is conditional on the explicitly written raw expression, and its purpose is to check the subsequent algebraic reduction independently.

Let $`c=2-x`$, $`m=gx/(2\sqrt2)`$, with $`0<x<2`$. The proposed complete raw density, rewritten entirely with ordinary SU(2)-contracted bars, is

```math
\begin{aligned}
c^{-1}\ell_{F,\rm raw}^{(2)}={}&-\bar\Psi_a\gamma^{abc}\bar\nabla_b\Psi_c+\frac2{x^2}\bar\zeta\not{\bar\nabla}\zeta+\frac{2\sqrt2i}{x}\bar\Psi_a\gamma^{ab}J\bar\nabla_b\zeta\\
&+3im\bar\Psi_a\gamma^{ab}J\Psi_b-4g\bar\Psi_a\gamma^a\zeta-\frac{7ig}{\sqrt2x}\bar\zeta J\zeta.
\end{aligned}\tag{F30}
```

The conversion from symmetric doublet contraction is $`\bar A J B=\bar A^TJJB=-\bar A^TB=-\delta_{ij}\bar A^iB^j`$. The division by $`c`$ in F30 is only convenient on the open domain; the raw action at $`c=0`$ must be retained before this division.

Use the invertible algebraic field map

```math
\Psi_a=\Upsilon_a+\beta\gamma_aJ\zeta,\qquad \beta=\frac{i\sqrt2}{3x},\qquad \Upsilon_a=\Psi_a-\frac{i\sqrt2}{3x}\gamma_aJ\zeta.
\tag{F31}
```

It introduces no derivative and is invertible for the whole compensator patch $`x\ne0`$. It is a field redefinition, not a condition on the gamma trace.

The necessary gamma contractions follow from the Clifford algebra. First, $`\gamma^{ab}\gamma_b=\gamma^a\gamma^b\gamma_b-\gamma^a=(5-1)\gamma^a=4\gamma^a`$. Expanding $`\gamma^{abc}=\gamma^a\gamma^b\gamma^c-\eta^{ab}\gamma^c+\eta^{ac}\gamma^b-\eta^{bc}\gamma^a`$ and multiplying by $`\gamma_c`$ gives $`5\gamma^a\gamma^b-5\eta^{ab}+\gamma^b\gamma^a-\gamma^a\gamma^b=3(\gamma^a\gamma^b-\eta^{ab})=3\gamma^{ab}`$. Left contractions follow from the same displayed expansion, giving $`\gamma_a\gamma^{abc}=3\gamma^{bc}`$ and $`\gamma_a\gamma^{ab}=4\gamma^b`$. Hence

```math
\gamma_a\gamma^{abc}\gamma_c=12\gamma^b,\qquad \gamma_a\gamma^{ab}\gamma_b=20.
\tag{F32}
```

The two cross terms from the first term of F30 each have coefficient $`-3\beta`$ multiplying $`\bar\Upsilon_a\gamma^{ab}J\bar\nabla_b\zeta`$. For the first, substitute the shift in the right slot and use $`\gamma^{abc}\gamma_c=3\gamma^{ab}`$. For the second, substitute it in the barred left slot and use $`\gamma_a\gamma^{abc}=3\gamma^{bc}`$. Its successive forms are $`-3\beta\delta\bar\zeta\gamma^{bc}\bar\nabla_b\Upsilon_c\doteq+3\beta\delta(\bar\nabla_b\bar\zeta)\gamma^{bc}\Upsilon_c=-3\beta\delta\bar\Upsilon_c\gamma^{bc}\bar\nabla_b\zeta=+3\beta\delta\bar\Upsilon_a\gamma^{ab}\bar\nabla_b\zeta=-3\beta\bar\Upsilon_a\gamma^{ab}J\bar\nabla_b\zeta`$. The successive signs follow from derivative transfer, the fixed-upper rank-two flip $`t_2=-1`$, gamma antisymmetry after relabeling, and $`\delta\bar A B=-\bar A J B`$. The boundary term is $`-3\beta\bar\nabla_b(\delta_{ij}\bar\zeta^i\gamma^{bc}\Upsilon_c^j)`$. The sum of the two cross coefficients and the original mixed derivative coefficient is

```math
-6\beta+\frac{2\sqrt2i}{x}=-\frac{6i\sqrt2}{3x}+\frac{2i\sqrt2}{x}=0.
\tag{F33}
```

The quadratic shift in that first term gives $`-12\beta^2\bar\zeta\not{\bar\nabla}\zeta`$ by F32. The shift in the original mixed derivative term gives $`(8\sqrt2i\beta/x)\bar\zeta\not{\bar\nabla}\zeta`$, using the left rank-two contraction in F32 and $`J^TJ=1`$. Including the original spinor kinetic term yields

```math
-12\beta^2+\frac{8\sqrt2i\beta}{x}+\frac2{x^2}=\frac{24}{9x^2}-\frac{16}{3x^2}+\frac2{x^2}=\frac{8-16+6}{3x^2}=-\frac2{3x^2}.
\tag{F34}
```

There are two mixed terms from $`3im\bar\Psi_a\gamma^{ab}J\Psi_b`$. The right-slot shift gives $`3im\beta\bar\Upsilon_a\gamma^{ab}\gamma_bJ^2\zeta=-12im\beta\bar\Upsilon_a\gamma^a\zeta`$. The barred-slot shift gives $`3im\beta\delta\bar\zeta\gamma_a\gamma^{ab}J\Upsilon_b=12im\beta\bar\zeta\gamma^b\Upsilon_b=-12im\beta\bar\Upsilon_b\gamma^b\zeta`$. Here the last sign is the contracted rank-one flip: its extra SU(2) minus multiplies the fixed-upper value $`t_1=+1`$. Thus each mixed term has the same coefficient $`-12im\beta`$. Adding the original algebraic mixing gives

```math
-24im\beta-4g=\frac{24m\sqrt2}{3x}-4g=\frac{8\sqrt2}{x}\frac{gx}{2\sqrt2}-4g=0.
\tag{F35}
```

The double shift in the same mass term gives $`60im\beta^2\bar\zeta J\zeta`$, since the gamma contraction is 20. The shifted original mixing gives $`20g\beta\bar\zeta J\zeta`$: its raw $`-4g\beta`$ multiplies $`5\delta_{ij}\bar\zeta^i\zeta^j=-5\bar\zeta J\zeta`$. Including the original spinor mass, the coefficient is

```math
60im\beta^2+20g\beta-\frac{7ig}{\sqrt2x}=-\frac{40im}{3x^2}+\frac{80im}{3x^2}-\frac{42im}{3x^2}=-\frac{2im}{3x^2}.
\tag{F36}
```

The substitution $`g=2\sqrt2m/x`$ was made in the last two terms before their sum. Thus the checked diagonalization is

```math
\ell_{F,\rm diag}^{(2)}\doteq-c\left[\bar\Upsilon_a\left(\gamma^{abc}\bar\nabla_b-3im\gamma^{ac}J\right)\Upsilon_c+\frac2{3x^2}\bar\zeta\left(\not{\bar\nabla}+imJ\right)\zeta\right].
\tag{F37}
```

This is a result of the explicitly displayed conditional raw block F30. It does not assume a multiplet assignment. At $`x=2`$, the prefactor is zero and extracting equations by division by $`c`$ is invalid; F37 does not assert an endpoint spectrum.

An independent exact symbolic substitution of $`\beta=i\sqrt2/(3x)`$ and $`m=gx/(2\sqrt2)`$ into the four collected coefficients F33–F36 returned respectively $`0`$, $`-2/(3x^2)`$, $`0`$ and $`-i\sqrt2g/(6x)`$. The last equals $`-2im/(3x^2)`$, with exact difference zero. This checks the rational coefficient collection; the gamma and Majorana reductions that produced those coefficients are the hand derivation above. It does not test the separate source-to-F30 collection.

The spinor equation of the diagonal block retains its sign, $`(\not{\bar\nabla}+imJ)\zeta=0`$. For the vector-spinor operator in F37, define $`\theta=\gamma^a\Upsilon_a`$ and $`\sigma=\bar\nabla^a\Upsilon_a`$. Its gamma trace is $`3\gamma^{bc}\bar\nabla_b\Upsilon_c-12imJ\theta=0`$. Expanding $`\gamma^{bc}=\gamma^b\gamma^c-\eta^{bc}`$ gives $`\gamma^{bc}\bar\nabla_b\Upsilon_c=\not{\bar\nabla}\theta-\sigma`$, hence

```math
\sigma=\not{\bar\nabla}\theta-4imJ\theta.
\tag{F38}
```

Therefore, when a justified gamma-trace gauge sets $`\theta=0`$, the divergence is fixed by the equation to $`\sigma=0`$; it is not a second freely imposed independent gauge. Expanding the rank-three gamma as in F32 then gives $`\gamma^{abc}\bar\nabla_b\Upsilon_c=\gamma^a\not{\bar\nabla}\theta-\bar\nabla^a\theta+\not{\bar\nabla}\Upsilon^a-\gamma^a\sigma`$, and $`\gamma^{ac}\Upsilon_c=\gamma^a\theta-\Upsilon^a`$. On $`\theta=\sigma=0`$ the remaining equation is

```math
(\not{\bar\nabla}+3imJ)\Upsilon^a=0.
\tag{F39}
```

The gauge transformation inherited by this shift is $`\delta\Upsilon_a=(\bar\nabla_a+im\gamma_aJ)\epsilon`$ because the background has $`\delta\zeta=0`$. Its gamma trace is $`\delta\theta=(\not{\bar\nabla}+5imJ)\epsilon`$. Establishing the solvability and residual kernel of that gauge condition is a separate step in the main analysis; F38–F39 identify what follows once that gauge is justified. No norm or boundary admissibility is inferred solely from this algebraic reduction.

Source equations are cited alongside the displayed derivations. The accepted [component conventions](../../references/COMPONENT_CONVENTIONS.md) and [Part I catalogue](../../../background.md) fix this companion’s inherited inputs.
