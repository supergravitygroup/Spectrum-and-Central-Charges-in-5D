# Generic bosonic action with independent invariant couplings

**Date:** 2026-10-13. **Action identifier:** `GENERIC-COMBINATION-BOSONIC-v1`.

## 1. Problem and Target

The bosonic action combines the source-normalized two-derivative, Weyl, LOG and scalar-curvature-squared invariants. The four coefficients are independent: a dimensionless two-derivative coefficient $`c_2`$ and three dimensionful higher-derivative coefficients $`\alpha,\beta,\lambda`$. The paper uses the $`c_2=1`$ action. The expression is algebraically defined at $`c_2=0`$.

The inputs are the invariant constructions and their bosonic projections identified below. Each bosonic block retains its source normalization, composite definitions and boundary representative. The notation conversion and verification scope are summarized in [the source note](source_notes.md).

| Block | Calculated full invariant | Located bosonic calculation used here |
| --- | --- | --- |
| Two derivative | [Gauged two-derivative action](../common/two_derivative_action/details/construction.md), Eq. (5.10), with its existing factor $`-2`$ | Same file, §6.4; G-2D below |
| Weyl in OP normalization | [Gauged Weyl action](../weyl2/action/details/construction.md), GA24, GC03–GC24 | G-W and G-D7–G-D10 below |
| LOG | [Current calculated LOG action](../log/action/details/construction.md), SC7-52 | G-LOG below, with its stated bulk representative |
| Scalar curvature squared | [Canonical BF construction](../r2/action/details/construction.md) and [assembled action](../r2/action/details/source_action.md) | G-R2 and G-D12–G-D14 below |

The inherited compact bosonic expressions are **bulk representatives**. The equality to the full fermionic endpoints after setting fermions to zero is modulo the boundary transfers explicitly recorded in these input calculations. The present assembly introduces no new integration by parts. It defines the displayed bulk density exactly, and does not claim to supply a boundary variational principle or boundary counterterms.

## 2. Convention Ledger

The action uses [the common conventions](../common/conventions.md) and the [normalization definitions](action_inputs.md).

The formulas retain the source's epsilon glyphs: its spacetime
$`\epsilon^{abcde}`$ is the common dictionary's $`\varepsilon^{abcde}`$, and its
SU(2) $`\varepsilon^{ij}`$ is the common dictionary's $`\epsilon^{ij}`$. These are
notation correspondences; neither fixes a spacetime orientation component.

| Item | Setting |
| --- | --- |
| Dimension and signature | $`D=5`$, $`\eta_{ab}=\mathrm{diag}(-,+,+,+,+)`$; $`a,b,\mu,\nu=0,1,2,3,4`$ and $`i,j=1,2`$ |
| Orientation and brackets | $`\epsilon^{abcde}`$ is the symbolic Levi–Civita tensor, with Lorentzian contraction identities; brackets have unit weight |
| Spinor convention inherited before projection | $`\{\gamma^a,\gamma^b\}=2\eta^{ab}`$, $`\gamma^{abcde}=i\epsilon^{abcde}\mathbf1`$; fermions vanish in this bosonic density; the common fermion dictionary controls any extension |
| SU(2) indices | $`X^i=\varepsilon^{ij}X_j`$, $`X_i=X^j\varepsilon_{ji}`$, $`\varepsilon_{12}=\varepsilon^{12}=1`$; lower each index in its displayed order |
| Gauge and projection | $`\sigma=1`$, $`b_\mu=0`$, defining dilatino $`\psi^i=0`$, $`L^{ij}=\delta^{ij}L/\sqrt2`$; then set the physical gravitino $`\psi_\mu^i`$ and compensator spinor $`\varphi^i`$ to zero |
| Compensator patch | $`L>0`$, as in the calculated four-invariant bosonic inputs. No value or constancy of $`L`$ is imposed. $`L=0`$ is outside the coordinate patch; a signed-chart extension would require a separate statement |
| Independent bosons | $`e_\mu{}^a,C_\mu,B_{\mu\nu},E_{\mu\nu\rho},L,N,V_\mu,V'_\mu{}^{ij}`$ |
| Couplings | $`c_2,\alpha,\beta,\lambda,g`$ are real constants; no relation among them is imposed. $`g=0`$ is an allowed limit of the written action |
| Approximation and equations | Exact bosonic, finite higher-derivative action; no small-coupling expansion, auxiliary elimination, bosonic EOM or background ansatz |
| Overall normalization | $`1/(2\kappa_5^2)=1/(16\pi G_5)`$, with $`\kappa_5^2>0`$ as the overall sign convention |

The superscript $`(0)`$ on a block below means **zero physical fermions**, not a background evaluation or $`S^{(0)}`$ in a fluctuation expansion. The metric, fluxes, connections and compensators remain arbitrary.

The bosonic spin connection is the torsion-free $`\omega(e)`$. The inherited curvature convention is

```math
R_{\mu\nu}{}^{ab}=2\partial_{[\mu}\omega_{\nu]}{}^{ab}+2\omega_{[\mu}{}^{ac}\omega_{\nu]c}{}^b,
\qquad R_{\mu\nu}=R_{\mu\rho}{}^{ab}e_b{}^\rho e_{\nu a},\qquad R=g^{\mu\nu}R_{\mu\nu}.
\tag{G-C1}
```

Thus $`R_{\mu\nu\rho\sigma}=k(g_{\mu\rho}g_{\nu\sigma}-g_{\mu\sigma}g_{\nu\rho})`$ gives $`R_{\mu\nu}=4kg_{\mu\nu}`$ and $`R=20k`$. This fixes the convention and does not select a background.

## 3. Definitions and Required Identities

### 3.1 Forms and the independent constrained current

```math
G=dC,\qquad H_3=dB+\frac12C\wedge G+\frac g2E_3,
\qquad H^{ab}=-\frac1{12}\epsilon^{abcde}H_{cde},\qquad
E^a=-\frac1{12}\epsilon^{abcde}\nabla_bE_{cde}.
\tag{G-D1}
```

$`H_{ab}`$ is the indicated dual of the three-form strength, not another independent two-form. $`E^a`$ is the constrained current derived from the independent potential $`E_3`$, not an independently varied vector. The Bianchi identities are $`dG=0`$, $`dH_3=G\wedge G/2+g\,dE_3/2`$, and $`\nabla_aE^a=0`$. Every derivative of $`H`$ or $`E`$ in the density retains these potential definitions.

The strengths are preserved by the local form gauge transformations

```math
\delta C=d\xi,\qquad \delta E_3=d\Lambda_2,\qquad
\delta B=d\Lambda_1-\frac12\xi G-\frac g2\Lambda_2.
\tag{G-D2}
```

We use $`N=N_c`$, $`E_3=E_{c3}`$ and $`L^{ij}=L_c^{ij}`$ for the independent compensator. This drops a label, not a field.

### 3.2 R-symmetry connection and derivatives

```math
V_\mu{}^{ij}=V'_\mu{}^{ij}+\frac12\delta^{ij}V_\mu,\qquad
\delta_{ij}V'_\mu{}^{ij}=0,\qquad
V_{\mu\nu}{}^{ij}=2\partial_{[\mu}V_{\nu]}{}^{ij}-2V_{[\mu}{}^{k(i}V_{\nu]k}{}^{j)}.
\tag{G-D3}
```

$`V_{ab}^{ij}=e_a{}^\mu e_b{}^\nu V_{\mu\nu}^{ij}`$ is the full non-Abelian curvature. The coupling $`g`$ is not an extra prefactor on $`V_\mu{}^{ij}`$.

On Lorentz tensors without SU(2) indices, $`\nabla`$ is Levi–Civita. On the compensator triplet it also acts on both SU(2) indices:

```math
\begin{aligned}
\nabla_\mu L^{ij}&=\partial_\mu L^{ij}+2V_\mu{}^{(i}{}_kL^{j)k},\\
\nabla^2L^{ij}&=g^{\mu\nu}\left[\partial_\mu(\nabla_\nu L^{ij})-\Gamma^\rho_{\mu\nu}\nabla_\rho L^{ij}+2V_\mu{}^{(i}{}_k\nabla_\nu L^{j)k}\right],\\
\nabla_\mu L_{ij}&=\partial_\mu L_{ij}-2V_{\mu(i}{}^kL_{j)k}.
\end{aligned}\tag{G-D4}
```

The lower-triplet derivative (G-D4) follows by NW–SE index lowering; see the [derivative definitions](action_inputs.md).

In particular,

```math
\nabla_aL^{ij}=\frac{\delta^{ij}}{\sqrt2}\partial_aL+
\frac L{\sqrt2}\left(V'_a{}^i{}_k\delta^{jk}+V'_a{}^j{}_k\delta^{ik}\right).
\tag{G-D5}
```

Consequently, setting a background value of $`L`$ constant would not remove these connection contributions. No such background condition is used here.

The contraction notation is

```math
G^2=G_{ab}G^{ab},\quad H^2=H_{ab}H^{ab},\quad GH=G_{ab}H^{ab},\quad
T^2=T_{ab}T^{ab},\quad E^2=E_aE^a,\quad
V'^2=V'_a{}^{ij}V'{}^a{}_{ij},\quad (\partial L)^2=\partial_aL\partial^aL.
\tag{G-D6}
```

All antisymmetric contractions sum over both index orderings, with no implicit $`1/2`$. The four-tensor chains below keep their displayed order.

### 3.3 Dependent bosonic composites

The following are the already evaluated zero-fermion definitions, not independent fields or auxiliary-field solutions:

```math
\begin{aligned}
T_{ab}&=\frac{G_{ab}-2H_{ab}}8,&
f_{ab}&=-\frac16R_{ab}+\frac1{48}\eta_{ab}R,& f_a{}^a&=-\frac R{16},\\
D&=-\frac R{32}+\frac5{96}G^2+\frac1{24}GH-\frac{13}{24}H^2+\frac g4N+\frac{g^2}{16}L^2.
\end{aligned}\tag{G-D7}
```

The conformal curvature on this bosonic body is

```math
\mathsf C_{abcd}=R_{abcd}+2(f_{ac}\eta_{bd}-f_{bc}\eta_{ad}-f_{ad}\eta_{bc}+f_{bd}\eta_{ac}),\qquad
\mathsf C^2=R_{abcd}R^{abcd}-\frac43R_{ab}R^{ab}+\frac16R^2.
\tag{G-D8}
```

It is the ordinary five-dimensional Weyl tensor after the bosonic restriction. The resulting symmetry of $`f_{ab}`$ follows from its displayed torsionless Ricci expression; it is not imposed on a full fermionic $`f_{ab}`$.

The calculated Weyl current and the retained conformal second-derivative correction are:

```math
Q_W^{ab}=4\mathsf C^{ab}{}_{cd}T^{cd}-64DT^{ab}/3-128T^{ab}T^2/9-512T^a{}_cT^{cd}T^b{}_d/3,\tag{G-D9}
```

```math
\mathcal K_a{}_b{}^{cd}=2f_{ab}T^{cd}+2\delta_b^c f_a{}^eT^d{}_e-2f_a{}^cT^d{}_b-2\delta_b^d f_a{}^eT^c{}_e+2f_a{}^dT^c{}_b.\tag{G-D10}
```

Here $`Q_W^{ab}=-Q_W^{ba}`$. In particular the already evaluated ordered derivative is

```math
\left.\mathcal D_b\mathcal D_cT^{ac}\right|_{\mathrm{bos}}=
\nabla_b\nabla_cT^{ac}-4f_{bd}T^{ad}.
\tag{G-D11}
```

The $`f`$ and $`\mathcal K`$ terms survive $`b_\mu=0`$ and must remain in the Weyl block. First derivatives of the singlet $`T`$ are Levi–Civita derivatives; the explicitly displayed $`\mathcal K`$ corrects its second conformal derivative. No hidden supercovariant fermion remains.

### 3.4 Composite fields of the scalar-curvature-squared block

The project primed map, C8 and C14 of the calculated R2 action, gives:

```math
\boldsymbol{\mathcal G}_{ab}=4\nabla_{[a}(L^{-1}E_{b]})+2L^{-1}L_{ij}V_{ab}^{ij}-2L^{-3}L_k{}^l\nabla_{[a}L^{kp}\nabla_{b]}L_{lp}.\tag{G-D12}
```

```math
\begin{aligned}
\boldsymbol Y^{ij}={}&\tfrac14L^{-1}(4\nabla^2L^{ij}-2RL^{ij}-8H^2L^{ij}+G^2L^{ij})\\
&+L^{-3}[-N^2L^{ij}-E^2L^{ij}-2E^aL^{k(i}\nabla_aL_k{}^{j)}-L_{kl}\nabla^aL^{k(i}\nabla_aL^{j)l}].
\end{aligned}\tag{G-D13}
```

The bold strength $`\boldsymbol{\mathcal G}_{ab}`$ is distinct from the graviphoton $`G_{ab}`$. Its exact displayed index arrangement is the project's checked primed map. It has not been replaced by a differently ordered paper formula. The derivatives in these definitions mean (G-D4), including the R connection.

The bosonic primed variables, used only to identify the parent normalization, are

```math
\rho'_0=\frac{2N}{L},\qquad
Y'^{ij}_0=\boldsymbol Y^{ij}+\left(\frac{gN}{L}+\frac{g^2L}{4}\right)L^{ij},\qquad
F'_{0ab}=\boldsymbol{\mathcal G}_{ab}.
\tag{G-D14}
```

No primed variable is independently varied. For the ordinary scalar ratio,

```math
\partial_a(N/L)=\frac{\partial_aN}{L}-\frac{N\partial_aL}{L^2}.
\tag{G-D15}
```

## 4. Detailed Derivation

### 4.1 Linear assembly and bosonic projection

Let $`\ell_{2\partial}^{F},\ell_W^F,\ell_{\log}^F,\ell_{R^2}^F`$ denote the calculated fermionic input densities in the source table. The coefficients multiply whole superinvariants, not selected terms:

```math
\ell_{\mathrm{comb}}^F=c_2\ell_{2\partial}^F+\alpha\ell_W^F+\beta\ell_{\log}^F+\lambda\ell_{R^2}^F.
\tag{G-A1}
```

Set $`P_0X=X|_{\psi_\mu=\varphi=0}`$, including the corresponding zero-fermion values of the full dependent quantities. Since the couplings are commuting constants, evaluating the four summands gives

```math
\begin{aligned}
P_0\ell_{\mathrm{comb}}^F
&=P_0(c_2\ell_{2\partial}^F)+P_0(\alpha\ell_W^F)+P_0(\beta\ell_{\log}^F)+P_0(\lambda\ell_{R^2}^F)\\
&=c_2P_0\ell_{2\partial}^F+\alpha P_0\ell_W^F+\beta P_0\ell_{\log}^F+\lambda P_0\ell_{R^2}^F\\
&\simeq_{\partial}c_2\ell_{2\partial}^{(0)}+\alpha\ell_W^{(0)}+\beta\ell_{\log}^{(0)}+\lambda\ell_{R^2}.
\end{aligned}\tag{G-A2}
```

The first line evaluates a sum term by term; the second takes each constant outside the evaluation. The last line selects the *existing* bulk representatives reproduced below. The symbol $`\simeq_\partial`$ refers only to their inherited boundary conversions, not an EOM or approximation. There are no $`\alpha\beta`$, $`\alpha\lambda`$ or $`\beta\lambda`$ terms: no multiplication of invariant densities occurs in (G-A1).

Explicit fermion products have zero bosonic projection. The even hatted objects retain their computed bosonic parts, including the $`f`$ corrections in (G-D7)–(G-D11). Physical fermion order four or higher also vanishes at $`P_0`$, so the bosonic action has no residual $`O(\mathrm{fermion}^4)`$ remainder.

### 4.2 Complete two-derivative block

The factor $`-2`$ in our vector–linear construction is already included in this block. Its Einstein coefficient is $`+L`$; the assembled Einstein contribution is $`c_2LR`$.

```math
\begin{aligned}
\ell_{2\partial}^{(0)}={}&L(R-G^2/2+4H^2+2V'_a{}^{ij}V'^{a}_{ij})\\
&+L^{-1}(\partial L)^2-2L^{-1}E^2-2\sqrt2E_aV^a\\
&-2N^2/L-4gE_aC^a-2gLN-4gN-g^2L^3/2+2g^2L^2.
\end{aligned}
\tag{G-2D}
```


### 4.3 Complete Weyl block in the calculated OP normalization

This is the bosonic projection of GA24 with unit coefficient, including its differentiated currents and the conformal second-derivative corrections. All the symbols on its right-hand side are defined in Section 3.

```math
\begin{aligned}
\ell_W^{(0)}={}&\mathsf C^2/8+64D^2/3+1024DT^2/9-16\mathsf C_{abcd}T^{ab}T^{cd}/3-V_{ab}^{ij}V^{ab}_{ij}/3\\
&-64(\nabla_aT_{bc})(\nabla^aT^{bc})/3+64(\nabla_bT_{ac})(\nabla^aT^{bc})/3-128T_{ab}(\nabla^b\nabla_cT^{ac}-4f^b{}_dT^{ad})/3\\
&-128\epsilon_{abcde}T^{ab}T^{cd}\nabla_fT^{ef}/3+1024T_{ab}T^{bc}T_{cd}T^{da}-2816(T^2)^2/27\\
&+\epsilon^{abcde}C_a\mathsf C_{bcfg}\mathsf C_{de}{}^{fg}/16-\epsilon^{abcde}C_aV_{bc}^{ij}V_{deij}/12+C_a\nabla_bQ_W^{ab}\\
&-32C_a\epsilon^a{}_{bcde}\left\{\frac23[(\nabla^bT^{cf})(\nabla_fT^{de})+T^{cf}(\nabla^b\nabla_fT^{de}+\mathcal K^b{}_f{}^{de})]\right.\\
&\left.\qquad+(\nabla^bT^c{}_f)(\nabla^dT^{ef})+T^c{}_f[\nabla^b\nabla^dT^{ef}+\eta^{dk}\mathcal K^b{}_k{}^{ef}]\right\}-8gL^{ij}V_{abij}T^{ab}/3,
\end{aligned}\tag{G-W}
```


### 4.4 Complete LOG block

This is BL-FINAL of our calculated LOG bosonic reduction, with $`N_c\mapsto N`$ and $`E_{c\,a}\mapsto E_a`$. The once-applied Gold/component slot conversion is already included. In particular, no extra factor $`-2`$ is applied to this block.

```math
\boxed{\begin{aligned} \ell_{\log}^{(0)}={}& -\frac1{12}\epsilon^{abcde}C_aV_{bc}^{ij}V_{de\,ij} +\frac16V_{ab}^{ij}V^{ab}_{ij} +\frac{gL}{6\sqrt2}\delta_{ij}V_{ab}^{ij}G^{ab} +\frac{2gL}{3\sqrt2}\delta_{ij}V_{ab}^{ij}H^{ab} \\
 &-\frac16R_{ab}R^{ab}+\frac1{24}R^2 +\frac16R_{ab}G^{ac}G^b{}_c -\frac43R_{ab}G^{ac}H^b{}_c \\
 &+R\left(\frac g6N-\frac{g^2}{12}L^2 +\frac13G_{ab}H^{ab}-\frac13H_{ab}H^{ab}\right) \\
 &-\frac{g^2}{6}N^2+\frac{2g^3}{3}N L^2 +\frac{5g^4}{24}L^4 \\
 &+gN\left(-\frac13G_{ab}G^{ab}-\frac23G_{ab}H^{ab} +2H_{ab}H^{ab}\right) \\
 &+g^2L^2\left(\frac1{24}G_{ab}G^{ab} -\frac16G_{ab}H^{ab}-H_{ab}H^{ab}\right) \\
 &-\frac1{48}(G_{ab}G^{ab})^2 -\frac13(G_{ab}G^{ab})(G_{cd}H^{cd}) +\frac23(G_{ab}G^{ab})(H_{cd}H^{cd}) \\
 &+\frac43(G_{ab}H^{ab})^2 -\frac43(G_{ab}H^{ab})(H_{cd}H^{cd}) -2(H_{ab}H^{ab})^2 \\
 &-\frac1{24}G_{ab}G^{bc}G_{cd}G^{da} +G_{ab}G^{bc}G_{cd}H^{da} -\frac43G_{ab}G^{bc}H_{cd}H^{da} \\
 &-\frac83G_{ab}H^{bc}G_{cd}H^{da} +\frac{16}{3}G_{ab}H^{bc}H_{cd}H^{da} \\
 &-\frac16(\nabla_bG^{ab})(\nabla^cG_{ac}) +\frac23(\nabla_aH_{bc}) \left(\nabla^aH^{bc}+\nabla^bH^{ca}+\nabla^cH^{ab}\right) \\
 &-\frac{g^2}{4}\partial_aL\partial^aL-\frac{g^2}{2}L^2V_a^{\prime ij}V^{\prime a}_{ij} \\
 &+\frac1{48}(\nabla^bG_{ab})\epsilon^{acdef}G_{cd}G_{ef} +\frac13(\nabla^bG_{ab})\epsilon^{acdef}H_{cd}H_{ef} \\
 &-\frac16(\nabla^bG_{ab})\epsilon^{acdef}H_{cd}G_{ef} \\
 &+\frac1{12}(\epsilon^{abcde}G_{bc}G_{de}) (\epsilon_{a}{}^{fghi}H_{fg}H_{hi}) \\
 &+\frac g3E_a\nabla_bG^{ab} -\frac g{24}E_a\epsilon^{abcde}G_{bc}G_{de} -\frac{2g}{3}E_a\epsilon^{abcde}H_{bc}H_{de} +\frac{g^2}{3}E_aE^a. \end{aligned}}\tag{G-LOG}
```


### 4.5 Complete scalar-curvature-squared block

This is the calculated C13 bulk representative of the primed BF construction, with its project strength (G-D12), its triplet (G-D13), and unit coefficient of $`\boldsymbol Y^{ij}\boldsymbol Y_{ij}`$.

```math
\begin{aligned}
\ell_{R^2}={}&
\boldsymbol Y^{ij}\boldsymbol Y_{ij}
-2\nabla^a(NL^{-1})\nabla_a(NL^{-1}) \\
&-\frac18\epsilon_{abcde}C^a
\boldsymbol{\mathcal G}^{bc}\boldsymbol{\mathcal G}^{de}
+NL^{-1}G^{ab}\boldsymbol{\mathcal G}_{ab}
-N^2L^{-2}G^{ab}G_{ab} \\
&+4N^2L^{-2}H^{ab}G_{ab}
-\frac14\boldsymbol{\mathcal G}^{ab}\boldsymbol{\mathcal G}_{ab}
-4NL^{-1}H_{ab}\boldsymbol{\mathcal G}^{ab} \\
&+g^2\left(
\frac14L^{ij}\nabla^a\nabla_aL_{ij}
-\frac14RL^2-H^2L^2+\frac18G^2L^2
-\frac52N^2-\frac12E^aE_a
-\frac12\nabla^aL\nabla_aL
\right) \\
&-4gN^3L^{-2}+\frac1{16}g^4L^4 .
\end{aligned}
\tag{G-R2}
```


The mixed term is exactly $`(N/L)G^{ab}\boldsymbol{\mathcal G}_{ab}`$. Replacing the first strength by the composite one would change this invariant. Likewise, the $`L^{ij}\nabla^2L_{ij}`$ term retains connection contributions; it is not replaced by $`L\,\partial^2L`$.

### 4.6 Normalization dictionary

For a coefficient comparison only, isolate the terms quadratic in the metric curvature. This means selecting the curvature part $`D_R=-R/32`$ and the curvature part $`\boldsymbol Y_R^{ij}=-RL^{ij}/(2L)`$; it does not remove the curvature–matter terms from the full action.

For the Weyl block, insert $`D_R`$ into the two curvature-only contributions of (G-W):

```math
\begin{aligned}
\ell_W^{(0)}\big|_{\mathrm{curv}^2}
&=\frac18\mathsf C^2+\frac{64}{3}\left(-\frac R{32}\right)^2\\
&=\frac18\mathsf C^2+\frac{64}{3\cdot1024}R^2
=\frac18\mathsf C^2+\frac1{48}R^2\\
&=\frac18\left(R_{abcd}R^{abcd}-\frac43R_{ab}R^{ab}+\frac16R^2\right)+\frac1{48}R^2\\
&=\frac18R_{abcd}R^{abcd}-\frac16R_{ab}R^{ab}+\left(\frac1{48}+\frac1{48}\right)R^2\\
&=\frac18R_{abcd}R^{abcd}-\frac16R_{ab}R^{ab}+\frac1{24}R^2.
\end{aligned}\tag{G-N1}
```

The second line squares $`-1/32`$; the third inserts the established five-dimensional Weyl contraction (G-D8); the last two collect the scalar-curvature coefficient. The curvature identity is part of the inherited geometric dictionary, not a new field equation.

For LOG, the two pure-curvature terms are explicit in (G-LOG):

```math
\ell_{\log}^{(0)}\big|_{\mathrm{curv}^2}=-\frac16R_{ab}R^{ab}+\frac1{24}R^2.
\tag{G-N2}
```

For R2, the source-gauge contraction is

```math
L^{ij}L_{ij}=\frac{L^2}{2}\delta^{ij}\delta_{ij}=\frac{L^2}{2}(1+1)=L^2.
\tag{G-N3}
```

Insert it into the square of the curvature part of (G-D13):

```math
\ell_{R^2}\big|_{\mathrm{curv}^2}
=\left(-\frac R{2L}L^{ij}\right)\left(-\frac R{2L}L_{ij}\right)
=\frac{R^2}{4L^2}L^{ij}L_{ij}
=\frac{R^2}{4L^2}L^2=\frac14R^2.
\tag{G-N4}
```

All other displayed R2 terms are of different field content or at most linear in metric curvature. Their coefficients remain in (G-R2).

| Coefficient | Invariant multiplied | Pure metric-curvature normalization |
| --- | --- | --- |
| $`c_2`$ | Our calculated two-derivative block | $`LR`$ |
| $`\alpha`$ | Our Weyl GA24 block | $`\mathsf C^2/8+R^2/48`$ |
| $`\beta`$ | Our corrected LOG SC7-52 block | $`-R_{ab}R^{ab}/6+R^2/24`$ |
| $`\lambda`$ | Our R2 primed BF block | $`R^2/4`$ |

Multiplying these three curvature-squared rows by their respective couplings gives

```math
\begin{aligned}
\ell_{\mathrm{comb}}\big|_{\mathrm{curv}^2}
={}&\alpha\left(\frac18R_{abcd}R^{abcd}-\frac16R_{ab}R^{ab}+\frac1{24}R^2\right)
+\beta\left(-\frac16R_{ab}R^{ab}+\frac1{24}R^2\right)+\frac\lambda4R^2\\
={}&\frac\alpha8R_{abcd}R^{abcd}-\frac{\alpha+\beta}{6}R_{ab}R^{ab}
+\left(\frac{\alpha+\beta}{24}+\frac\lambda4\right)R^2.
\end{aligned}\tag{G-N5}
```

This table concerns terms quadratic in metric curvature. In the gauged action there are also terms linear in $`R`$ times $`N,L`$, strengths or derivatives. They are fully retained in the four blocks; (G-N5) is not a metric-only replacement action.

The already derived **full-invariant** normalization bridge is GB16–GB20 of the [Gauss–Bonnet construction](../gauss_bonnet/action/details/gb_splus_construction.md):

```math
\ell_{W,\mathrm{target}}=-2\ell_W^{(0)},\qquad
\ell_{\mathrm{GB}}=-2\ell_W^{(0)}-4\ell_{\log}^{(0)}.
\tag{G-N6}
```

Its bosonic specialization follows by applying $`P_0`$ to both sides of the existing full identity; the constant factors pass through $`P_0`$ as in (G-A2). Thus a target-normalized Weyl coefficient obeys

```math
\lambda_W\ell_{W,\mathrm{target}}=(-2\lambda_W)\ell_W^{(0)},
\qquad \alpha=-2\lambda_W,\qquad \lambda_W=-\frac\alpha2.
\tag{G-N7}
```

The GB subfamily is a **check**, not a restriction on the generic theory:

```math
\begin{aligned}
\alpha=-2\lambda_{\mathrm{GB}},\quad\beta=-4\lambda_{\mathrm{GB}},\quad\lambda=0
&\ \Longrightarrow\ 
\alpha\ell_W^{(0)}+\beta\ell_{\log}^{(0)}+\lambda\ell_{R^2}
=\lambda_{\mathrm{GB}}(-2\ell_W^{(0)}-4\ell_{\log}^{(0)})\\
&\ \Longrightarrow\ \ell_{\mathrm{comb}}=c_2\ell_{2\partial}^{(0)}+\lambda_{\mathrm{GB}}\ell_{\mathrm{GB}}.
\end{aligned}\tag{G-N8}
```

For the curvature square this gives the coefficients $`-\lambda_{\mathrm{GB}}/4`$, $`+\lambda_{\mathrm{GB}}`$ and $`-\lambda_{\mathrm{GB}}/4`$ respectively, since

```math
\frac{-2\lambda_{\mathrm{GB}}}{8}=-\frac{\lambda_{\mathrm{GB}}}{4},\qquad
-\frac{-2\lambda_{\mathrm{GB}}-4\lambda_{\mathrm{GB}}}{6}=\lambda_{\mathrm{GB}},\qquad
\frac{-2\lambda_{\mathrm{GB}}-4\lambda_{\mathrm{GB}}}{24}=-\frac{\lambda_{\mathrm{GB}}}{4}.
\tag{G-N9}
```

Therefore its pure metric-curvature square is $`-\lambda_{\mathrm{GB}}(R_{abcd}R^{abcd}-4R_{ab}R^{ab}+R^2)/4`$. The complete off-shell GB invariant still includes the other field terms.

## 5. Consistency Checks

### 5.1 Independent curvature coefficients

Let $`a_{\mathrm R},a_{\mathrm{Ric}},a_{\mathrm S}`$ denote the coefficients of $`R_{abcd}^2,R_{ab}^2,R^2`$ in (G-N5), solely for this comparison. Then

```math
\begin{pmatrix}a_{\mathrm R}\\a_{\mathrm{Ric}}\\a_{\mathrm S}\end{pmatrix}
=\begin{pmatrix}1/8&0&0\\-1/6&-1/6&0\\1/24&1/24&1/4\end{pmatrix}
\begin{pmatrix}\alpha\\\beta\\\lambda\end{pmatrix},\qquad
\det=\frac18\left(-\frac16\right)\frac14=-\frac1{192}\ne0.
\tag{G-K1}
```

Solving its first row gives $`\alpha=8a_{\mathrm R}`$. Multiplying the second row by $`-6`$ gives $`\alpha+\beta=-6a_{\mathrm{Ric}}`$ and hence $`\beta=-6a_{\mathrm{Ric}}-8a_{\mathrm R}`$. Substituting this sum into the third row gives $`a_{\mathrm S}=-a_{\mathrm{Ric}}/4+\lambda/4`$ and hence $`\lambda=4a_{\mathrm S}+a_{\mathrm{Ric}}`$. The inverse is therefore

```math
\alpha=8a_{\mathrm R},\qquad\beta=-8a_{\mathrm R}-6a_{\mathrm{Ric}},\qquad
\lambda=4a_{\mathrm S}+a_{\mathrm{Ric}}.
\tag{G-K2}
```

This establishes independence of the three curvature-squared coefficients. It is not a spectrum or ghost criterion.

### 5.2 Scalar ratio and retained derivative mixing

Squaring (G-D15) multiplies two two-term expressions. The four products are

```math
\begin{aligned}
-2\partial^a(N/L)\partial_a(N/L)
&=-2\left[\frac{\partial^aN\partial_aN}{L^2}
-\frac{N\partial^aN\partial_aL}{L^3}
-\frac{N\partial^aL\partial_aN}{L^3}
+\frac{N^2\partial^aL\partial_aL}{L^4}\right]\\
&=-\frac{2}{L^2}(\partial N)^2+\frac{4N}{L^3}\partial N\cdot\partial L-\frac{2N^2}{L^4}(\partial L)^2.
\end{aligned}\tag{G-K3}
```

The second equality uses commutativity of the bosonic scalar derivatives to add the two cross terms. Thus the compact ratio term retains both scalar gradients and their mixing; no scalar was eliminated.

### 5.3 Independent R2 parent check on constant-scalar data

Use the algebraic test $`G=H=E=V=V'=0`$, constant $`L,N`$ and arbitrary metric curvature $`R`$. This is not a solution claim. Put $`m=N/L`$ only in this check. From (G-D7), (G-D13) and (G-D14),

```math
f_a{}^a=-\frac R{16},\quad D=-\frac R{32}+\frac{gN}{4}+\frac{g^2L^2}{16},\quad
\boldsymbol Y^{ij}=\left(-\frac R{2L}-\frac{N^2}{L^3}\right)L^{ij},\quad
Y'^{ij}_0=\left(-\frac R{2L}-\frac{N^2}{L^3}+\frac{gN}{L}+\frac{g^2L}{4}\right)L^{ij}.
\tag{G-K4}
```

The original F0.1–F0.5 groups reduce to $`Y'_0{}^2-2gmY'_0{}^{ij}L_{ij}+m^2(8f_a{}^a-16D)`$. The first two terms are the square of the parent triplet minus its linear coupling. Expanding the gauging shift with $`u=gN/L`$ and $`v=g^2L/4`$, the shift-only coefficient is

```math
(u+v)^2-2u(u+v)=u^2+2uv+v^2-2u^2-2uv=-u^2+v^2.
\tag{G-K5}
```

The term linear in $`\boldsymbol Y`$ is $`[2(u+v)-2u]\boldsymbol Y^{ij}L_{ij}=2v\boldsymbol Y^{ij}L_{ij}`$. Using (G-K4) and $`L^{ij}L_{ij}=L^2`$ gives

```math
\begin{aligned}
Y'_0{}^2-2gmY'_0{}^{ij}L_{ij}
&=\left(\frac R2+\frac{N^2}{L^2}\right)^2
+\frac{g^2L}{2}\left(-\frac R{2L}-\frac{N^2}{L^3}\right)L^2
+\left(-\frac{g^2N^2}{L^2}+\frac{g^4L^2}{16}\right)L^2\\
&=\left(\frac R2+\frac{N^2}{L^2}\right)^2
-\frac{g^2RL^2}{4}-\frac{g^2N^2}{2}-g^2N^2+\frac{g^4L^4}{16}.
\end{aligned}\tag{G-K6}
```

The remaining parent term is

```math
\begin{aligned}
m^2(8f_a{}^a-16D)
&=\frac{N^2}{L^2}\left[-\frac R2+\frac R2-4gN-g^2L^2\right]\\
&=-\frac{4gN^3}{L^2}-g^2N^2.
\end{aligned}\tag{G-K7}
```

Adding (G-K6) and (G-K7) collects $`-g^2N^2/2-g^2N^2-g^2N^2=-5g^2N^2/2`$. The resulting parent polynomial is

```math
\left(\frac R2+\frac{N^2}{L^2}\right)^2-\frac{g^2RL^2}{4}
-\frac52g^2N^2-\frac{4gN^3}{L^2}+\frac1{16}g^4L^4.
\tag{G-K8}
```

Direct evaluation of (G-R2) on the same data gives (G-K8): its first term gives the square; its derivatives, strengths and $`E`$ terms vanish; its $`g^2`$ bracket contributes $`-g^2RL^2/4-5g^2N^2/2`$; and its final two terms contribute $`-4gN^3/L^2+g^4L^4/16`$. This is an independent source-group normalization check on a nontrivial field configuration, not a proof of all input invariant identities.

### 5.4 Dimensions, indices and gauge structure

After fixing the compensator scale,

```math
[\nabla]=[g]=[G]=[H]=[T]=[N]=[E]=[V_a]=1,\qquad
[R]=[D]=[f]=[V_{ab}^{ij}]=[\boldsymbol Y]=[\boldsymbol{\mathcal G}]=2,
\quad [L]=[C_a]=[B_{ab}]=[E_{abc}]=0.
\tag{G-K9}
```

The Weyl current has dimension three: $`[\mathsf C T]=2+1=3`$, $`[DT]=2+1=3`$, and $`[T^3]=1+1+1=3`$. Likewise $`[\mathcal K]=[fT]=2+1=3`$ and $`[\nabla\nabla T]=1+1+1=3`$. Consequently $`[C\nabla Q_W]=0+1+3=4`$ and $`[CT(\nabla\nabla T+\mathcal K)]=0+1+3=4`$.

The two-derivative monomial families have dimensions $`[LR]=2`$, $`[LG^2]=[LH^2]=[LV'^2]=2`$, $`[(\partial L)^2/L]=2`$, $`[E^2/L]=[N^2/L]=2`$, $`[EV]=2`$, $`[gEC]=1+1+0=2`$, $`[gLN]=[gN]=2`$ and $`[g^2L^3]=[g^2L^2]=2`$.

The higher-derivative monomial families exhaust the displayed blocks: curvature/composite squares have $`2+2=4`$; curvature times two strengths has $`2+1+1=4`$; four-strength products have $`1+1+1+1=4`$; paired differentiated strengths have $`(1+1)+(1+1)=4`$; $`TT\nabla T`$ and $`(\nabla G)GG`$ have $`1+1+(1+1)=4`$; Chern–Simons terms have $`[C]+2+2=4`$; and the explicit gauging families have $`[gNL^pG^2]=1+1+0+2=4`$, $`[g^2L^pG^2]=2+0+2=4`$, $`[g^2N^2]=4`$, $`[g^3NL^2]=4`$, $`[g^4L^4]=4`$, $`[gE\nabla G]=1+1+1+1=4`$, $`[gEGG]=1+1+1+1=4`$, $`[g^2E^2]=4`$, $`[g^2(\partial L)^2]=4`$ and $`[gN^3/L^2]=4`$. Here $`p`$ is any displayed power of the dimensionless $`L`$.

Finally $`[\partial(N/L)]=2`$, $`[g^2L^{ij}\nabla^2L_{ij}]=2+0+2+0=4`$ and $`[(N/L)G\boldsymbol{\mathcal G}]=1+1+2=4`$. Thus

```math
[c_2]=0,\qquad[\alpha]=[\beta]=[\lambda]=-2,\qquad
[\ell_{\mathrm{comb}}]=2,\qquad
[S]=[\kappa_5^{-2}]+[d^5x]+[e]+[\ell_{\mathrm{comb}}]=3-5+0+2=0.
\tag{G-K10}
```

Every block is a Lorentz scalar with all SU(2) indices contracted. The apparent extra fields $`T,D,f,\mathsf C,Q_W,\mathcal K,\boldsymbol Y,\boldsymbol{\mathcal G}`$ are defined composites, so the independent-field list is unchanged. All displayed coefficients are real in the inherited real bosonic section; complex component representations of SU(2) obey the inherited reality condition. No spinor reordering or Fierz identity occurs after $`P_0`$.

For the form strengths, inserting (G-D2) gives the actual cancellations

```math
\begin{aligned}
\delta G&=d^2\xi=0,&\delta(dE_3)&=d^2\Lambda_2=0,\\
\delta H_3&=d^2\Lambda_1-\tfrac12d\xi\wedge G-\tfrac12\xi\,dG-\tfrac g2d\Lambda_2+\tfrac12d\xi\wedge G+\tfrac g2d\Lambda_2=0.
\end{aligned}\tag{G-K11}
```

Here $`dG=0`$ is the Bianchi identity. In particular the compensator three-form term is necessary for the gauged tensor symmetry. The existing invariant gauge/boundary qualifications are inherited; this assembly is not a new nonlinear SUSY audit.

### 5.5 Limits and scope of reproducibility

Setting $`\alpha=\beta=\lambda=0`$ in (G-A2) gives $`\ell_{\mathrm{comb}}=c_2\ell_{2\partial}^{(0)}`$. Setting $`c_2=1`$ reproduces the already calculated generic bosonic combination. The three axes $`(\alpha,0,0)`$, $`(0,\beta,0)`$ and $`(0,0,\lambda)`$ select the individual calculated higher-derivative invariants with exactly their existing unit normalizations. None requires a coupling division.

The ungauged substitution acts on definitions as well as explicit terms: $`H_3\to dB+C\wedge G/2`$, $`D\to-R/32+5G^2/96+GH/24-13H^2/24`$, and every explicit positive power of $`g`$ disappears. There is no inverse power of $`g`$. The two-derivative block remains multiplied by $`c_2`$. No small-coupling or EFT limit is used.

The [assembly record](details/bosonic_assembly.json) records the transfer of the displayed blocks and composites, normalization factors, scalar-ratio expansion, R2 parent polynomial and shifted-triplet arithmetic. The [source note](source_notes.md) connects these inputs to their derivations. The [massless-sector reproduction guide](../computations/generic_ads5_massless/README.md) specifies the executable AdS5 checks. The nonlinear multiplet constructions are the stated source inputs.

## 6. Final Result

```math
\boxed{
S_{\mathrm{bos}}[c_2,\alpha,\beta,\lambda;g]
=\frac1{2\kappa_5^2}\int d^5x\,e\,
\left[c_2\ell_{2\partial}^{(0)}+\alpha\ell_W^{(0)}+\beta\ell_{\log}^{(0)}+\lambda\ell_{R^2}\right],
\qquad c_2,\alpha,\beta,\lambda\ \text{independent}.
}\tag{G-FINAL}
```

The complete four blocks are (G-2D), (G-W), (G-LOG) and (G-R2), with definitions (G-D1)–(G-D15). This specifies the full off-shell bosonic bulk action in the inherited field variables. The conventional coefficient choice $`c_2=1`$ recovers $`S_{2\partial}+\alpha S_{W,\mathrm{OP}}+\beta S_{\mathrm{LOG}}+\lambda S_{R^2}`$ with a common gravitational prefactor. All fields, fluxes and R-symmetry connections remain arbitrary in the stated compensator patch.

## 7. Convention Dependence and Remaining Uncertainties

The result uses our calculated action endpoints, their project repairs and their established bosonic bulk representatives. The independent Weyl-map checks and nonlinear fermionic SUSY/reality qualifications of the [component sources](source_notes.md#component-sources) remain inherited. They are not reopened as prerequisites or promoted to new certifications here.


The boundary representative is fixed to that of the accepted four bosonic blocks. Inherited surface terms are located in the two-derivative source §§3 and 6, LOG BC-03–BC-11/BL-39, and R2 C4–C5/C12. Equality to a different representative on a manifold with boundary requires retaining those surface terms or specifying appropriate boundary data. No such boundary problem is part of this assembly.

No background equations, solution catalogue, BPS fractions, kinetic signs or spectrum are asserted by this action document. Those require subsequent calculations from this fixed input.
