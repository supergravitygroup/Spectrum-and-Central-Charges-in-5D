# General action, normalizations, independent fields and fermionic scope

The sources' general action record is the following combination for **the bosonic sector and terms up to quadratic order in the fermions**. The source-discrepancy checks below identify the component blocks and algebraic identities compared:

```math
\boxed{
S_{\mathrm{record},\le2}
=\frac1{2\kappa_5^2}\int d^5x\,e\,
\Big[
\ell_{2\partial}
+\alpha\,\ell_{\mathrm{Weyl}^2}
+\beta\,\ell_{\mathrm{LOG}}
+\zeta\,\ell_{R^2}
\Big]_{\le2}.
}
```

Here $`\ell=e^{-1}\mathcal L`$; $`\alpha,\beta,\zeta,g,\kappa_5`$ is symbolic and $`g\neq0`$. No coupling expansion is made. $`[\ ]_{\le2}`$ specifies the sources' shared fermionic scope; it does not set higher-fermion terms of the full action to zero. Coupling names and the common prefactor agree with the [combined source](../common/details/component_action.md).

## Working conventions

The [root CONVENTIONS.md](../common/details/source_conventions.md) is authoritative for the working conventions:

```math
\begin{gathered}
D_{\rm spacetime}=5,\qquad
\eta_{ab}=(-,+,+,+,+),\qquad e=\det e_\mu{}^a=\sqrt{-g},\\
X_{[ab]}=\tfrac12(X_{ab}-X_{ba}),\qquad
\{\gamma^a,\gamma^b\}=2\eta^{ab},\qquad
\gamma^{abcde}=i\varepsilon^{abcde}\mathbf1,\\
\gamma\!\cdot\!X=\gamma^{a_1\cdots a_p}X_{a_1\cdots a_p}
\quad(1/p!\ \text{not included}),\\
\epsilon_{12}=\epsilon^{12}=1,\qquad
X^i=\epsilon^{ij}X_j,\qquad X_i=X^j\epsilon_{ji},\qquad
\bar X\Gamma Y=\bar X^i\Gamma Y_i .
\end{gathered}
```

Fermion-interchange signs include the additional NW–SE sign when passing from the open-index to the contracted rule:

```math
\begin{aligned}
\bar X^i\gamma_{(n)}Y^j&=t_n\bar Y^j\gamma_{(n)}X^i,
& (t_0,\ldots,t_5)&=(+,+,-,-,+,+),\\
\bar X^i\gamma_{(n)}Y_i
&=\epsilon_{ji}t_n\bar Y^j\gamma_{(n)}X^i
=-t_n\bar Y^j\gamma_{(n)}X_j .
\end{aligned}
```

No numerical orientation is selected. The coordinate epsilon tensor and density symbol are distinguished:

```math
\epsilon^{\mu\nu\rho\sigma\lambda}
=e\,\varepsilon^{\mu\nu\rho\sigma\lambda}.
```

Field strengths remain in three-form notation:

```math
\boxed{
G_{\mu\nu}=2\partial_{[\mu}C_{\nu]},\qquad
H_{\mu\nu\rho}
=3\partial_{[\mu}B_{\nu\rho]}
+\frac32C_{[\mu}G_{\nu\rho]}
+\frac g2E_{\mu\nu\rho}.
}
```

The normalized two-form in the sources is explicitly replaced everywhere by $`-\varepsilon_{abcde}H^{cde}/12`$. Normalization check:

```math
\begin{aligned}
\left(-\frac1{12}\varepsilon_{abcde}H^{cde}\right)
\left(-\frac1{12}\varepsilon^{abfgh}H_{fgh}\right)
&=-\frac{2!\,3!}{144}H_{cde}H^{cde}\\
&=-\frac1{12}H_{cde}H^{cde}.
\end{aligned}
```

Thus, the squared dual two-form with factor $`+4L`$ in the two-derivative source becomes, in the working notation,

```math
\boxed{-\frac L3H_{abc}H^{abc}}
```

as stated.

## Existing gauge and independent fields

The conditions **already imposed** in the sources' Poincaré actions are

```math
\sigma=1,\qquad \psi^i=0,\qquad b_\mu=0,\qquad
L_{ij}=\frac L{\sqrt2}\delta_{ij},
\qquad
V_\mu^{ij}=V_\mu^{\prime\,ij}+\frac12\delta^{ij}V_\mu
```

They do not transfer automatically to ungauge-fixed maps. $`L`$ is not fixed; inverse powers require the local condition $`L\neq0`$. The $`L>0`$, $`g>0`$ or specific $`L`$ values used on special source backgrounds are not imposed on the general action.

In this existing representation, the independent fields are:

```math
\boxed{
\begin{aligned}
\Phi_{\mathrm B}
&=\{e_\mu{}^a,C_\mu,B_{\mu\nu},E_{\mu\nu\rho},
L,N,V_\mu,V_\mu^{\prime\,ij}\},\\
\Phi_{\mathrm F}
&=\{\psi_\mu^i,\varphi^i\}.
\end{aligned}}
```

Before gauge fixing, $`\sigma,\psi^i,b_\mu`$ is restored; $`L^{ij}`$ replaces $`L`$, and $`V_\mu^{ij}`$ replaces $`(V_\mu,V_\mu^{\prime\,ij})`$. Fields are not counted twice:

```math
\begin{aligned}
L^{ij}L_{ij}
&=\frac{L^2}{2}\delta^{ij}\delta_{ij}=L^2,\\
\delta_{ij}V_\mu^{ij}
&=\frac12\delta_{ij}\delta^{ij}V_\mu=V_\mu,\\
E^\mu
&=-\frac1{12}\varepsilon^{\mu\nu\rho\sigma\lambda}
\mathcal D_\nu E_{\rho\sigma\lambda}.
\end{aligned}
```

In the last equality, $`E^\mu`$ and $`E_{\mu\nu\rho}`$ are two representations of the same linear-multiplet component. $`\omega_\mu{}^{ab},\phi_\mu^i,f_\mu{}^a`$ are dependent connections; $`T_{ab},D,\chi^i,Y^{ij}`$ are Dilaton–Weyl composites. The composite multiplets used in the Weyl, LOG and $`R^2`$ constructions add no independent fields. This distinction agrees with the [field inventory](../log/action/details/independent_fields.md).

## Source normalizations of the densities

To determine normalizations, let $`\ell_{\rm VL}[V;\mathbb L]`$ denote the unit vector–linear density in the sources. $`V_{\rm def}`$ is the defining vector, and $`V_{\rm lin}`$ is the composite vector of the independent linear multiplet:

| Sector | Source density and multiplier |
|---|---|
| Two derivatives | $`\ell_{2\partial}=-2\,\ell_{\rm VL}[V_{\rm lin}+2gV_{\rm def};\mathbb L]`$ |
| Weyl squared | $`\ell_{\mathrm{Weyl}^2}=\ell_{\rm VL}[V_{\rm def};\mathbb L_W]`$; $`N_W\supset \widehat C^2/8+64D^2/3`$ |
| LOG | $`\ell_{\mathrm{LOG}}=\ell_{\rm VL}[V_{\rm def};\mathbb L_{\log}]`$; no second multiplier is applied to the converted LOG components |
| $`R^2`$ | Unit BF density; the mixed map's $`C_{112}=C_{121}=1/2`$ weights are applied once |

The $`-2`$ in the two-derivative sector is not an overall normalization for the other invariants. Relevant inputs are the [two-derivative density](../common/two_derivative_action/details/construction.md), [Weyl map](../weyl2/action/details/linear_multiplet.md), [LOG density](../log/action/details/construction.md) and [$`R^2`$ BF construction](../r2/action/details/construction.md).

## Symbolic normalization check

Below, $`\supset`$ selects only the coefficient of the specified curvature monomial; it does not set other fields to zero or truncate a sector. From the dependent-connection definition

```math
\begin{aligned}
f_{ab}&\supset-\frac16R_{ab}+\frac1{48}g_{ab}R,\\
f_a{}^a&\supset
\left(-\frac16+\frac5{48}\right)R=-\frac1{16}R,\\
\Box^c\sigma&\supset2f_a{}^a=-\frac18R,\\
D&\supset\frac14\Box^c\sigma=-\frac1{32}R .
\end{aligned}
```

The curvature coefficient in the composite vector's triplet is calculated from the [two explicit map terms](../r2/action/details/construction.md):

```math
\begin{aligned}
Y_{{\rm lin}\,ij}
&\supset
\frac1L\Box^cL_{ij}+\frac4L L_{ij}D,\\
\Box^cL_{ij}&\supset6f_a{}^aL_{ij}
=-\frac38RL_{ij},\\
Y_{{\rm lin}\,ij}
&\supset\frac{L_{ij}}L
\left(-\frac38R-\frac18R\right)
=-\frac{R}{2L}L_{ij}.
\end{aligned}
```

Thus the two-derivative and $`R^2`$ normalizations follow directly:

```math
\boxed{
\begin{aligned}
\ell_{2\partial}
&\supset-2L^{ij}
\left(-\frac{R}{2L}L_{ij}\right)=LR,\\
\ell_{R^2}
&\supset Y_{\rm lin}^{ij}Y_{{\rm lin}\,ij}
\supset\frac{R^2}{4L^2}L^{ij}L_{ij}
=\frac14R^2.
\end{aligned}}
```

In the Weyl-squared density, the $`D^2`$ contribution must also be retained:

```math
\begin{aligned}
\ell_{\mathrm{Weyl}^2}
&\supset\frac18C_{abcd}C^{abcd}+\frac{64}{3}D^2\\
&\supset\frac18C_{abcd}C^{abcd}
+\frac{64}{3}\frac{R^2}{32^2}\\
&=\boxed{\frac18C_{abcd}C^{abcd}+\frac1{48}R^2}.
\end{aligned}
```

Therefore $`512/3=(64/3)/(1/8)`$ is only a relative coefficient; the actual coefficient of $`D^2`$ is $`64/3`$.

The pure-curvature square in LOG comes from these two structures in the [scalar component](../log/action/details/construction.md):

```math
\ell_{\mathrm{LOG}}
\supset\frac56(\Box^c\sigma)^2
-\frac32(\mathcal D_a\mathcal D_b\sigma)
             (\mathcal D^a\mathcal D^b\sigma).
```

```math
\begin{aligned}
\mathcal D_a\mathcal D_b\sigma
&\supset2f_{ab}=-\frac13R_{ab}+\frac1{24}g_{ab}R,\\
(\mathcal D_a\mathcal D_b\sigma)^2
&\supset
\frac19R_{ab}R^{ab}
-\frac1{36}R^2+\frac5{576}R^2\\
&=\frac19R_{ab}R^{ab}-\frac{11}{576}R^2,\\
\ell_{\mathrm{LOG}}
&\supset\frac5{384}R^2
-\frac16R_{ab}R^{ab}+\frac{11}{384}R^2\\
&=\boxed{-\frac16R_{ab}R^{ab}+\frac1{24}R^2}.
\end{aligned}
```

The root file's Weyl decomposition is used to compare the three invariants in the same curvature basis. Temporarily define

```math
A_{abcd}=g_{ac}R_{bd}-g_{bc}R_{ad}-g_{ad}R_{bc}+g_{bd}R_{ac},
\qquad
U_{abcd}=g_{ac}g_{bd}-g_{ad}g_{bc}
```

In five dimensions, direct contractions give

```math
\begin{gathered}
R_{abcd}A^{abcd}=4R_{ab}R^{ab},\qquad
R_{abcd}U^{abcd}=2R,\\
A_{abcd}A^{abcd}=12R_{ab}R^{ab}+4R^2,\qquad
A_{abcd}U^{abcd}=16R,\qquad U_{abcd}U^{abcd}=40
\end{gathered}
```

and therefore

```math
\begin{aligned}
C_{abcd}C^{abcd}
&=\left(R_{abcd}-\frac13A_{abcd}+\frac R{12}U_{abcd}\right)^2\\
&=R_{abcd}R^{abcd}
+\left(\frac{12}{9}-\frac83\right)R_{ab}R^{ab}\\
&\quad+\left(\frac49+\frac{40}{144}+\frac13-\frac{16}{18}\right)R^2\\
&=R_{abcd}R^{abcd}-\frac43R_{ab}R^{ab}+\frac16R^2.
\end{aligned}
```

The resulting pure-curvature coefficients are:

| Density | Pure-curvature normalization |
|---|---|
| $`\ell_{2\partial}`$ | $`LR`$ |
| $`\ell_{\mathrm{Weyl}^2}`$ | $`\frac18R_{abcd}R^{abcd}-\frac16R_{ab}R^{ab}+\frac1{24}R^2`$ |
| $`\ell_{\mathrm{LOG}}`$ | $`-\frac16R_{ab}R^{ab}+\frac1{24}R^2`$ |
| $`\ell_{R^2}`$ | $`\frac14R^2`$ |

In the total density:

```math
\boxed{
\ell_{\rm general}\supset
LR+\frac{\alpha}{8}R_{abcd}R^{abcd}
-\frac{\alpha+\beta}{6}R_{ab}R^{ab}
+\left(\frac{\alpha+\beta}{24}+\frac{\zeta}{4}\right)R^2.
}
```

This expression displays only the normalizations; the invariants' $`G,H,L,N,E,V`$ and fermion dependence remains in their respective densities.

## Fermionic scope and verification boundaries

The sources have distinct fermionic scopes:

| Input | Recorded scope and verification boundary |
|---|---|
| Two-derivative 2016-map action | Complete in bosons; physical fermion degree $`0,2`$. An explicit $`O(\mathrm{fermi}^4)`$ remainder is present. |
| Gauged Weyl squared | Full supercovariant map substitution; the construction checks do not establish independent full-multiplet laws or nonlinear SUSY invariance. The spectrum uses the specified component density and its background-specific quadratic reduction. |
| Active LOG | Physical fermion degree $`0,2`$; higher-fermion completion is outside scope. |
| $`R^2`$ from BF | Physical fermion degree $`0,2`$; implicit higher-fermion terms do not extend the correctness claim. |

In particular, the discrepancy between the spinor coefficient $`8/3`$ used in the [Weyl map](../weyl2/action/details/linear_multiplet.md) and the recorded alternative $`16/3`$ was resolved in favor of $`8/3`$ by the independent $`T^2\widehat R(Q)`$ coefficient calculation below. This single-coefficient check is not a full map or action SUSY check. The root file's [map-completeness boundary](../common/details/source_conventions.md) is retained. Source labels ‘verified/certified’ have not replaced independent verification.

Since hatted objects contain implicit fermions, for example

```math
B=B^{(0)}+B^{(2)}+\cdots,\qquad
[B^2]_{\le2}=(B^{(0)})^2+2B^{(0)}B^{(2)}
```

A term with no explicit spinors is not necessarily purely bosonic. Moreover, in the existing gauge

```math
\begin{aligned}
\widehat G_{\mu\nu}
&=G_{\mu\nu}+\frac i2\bar\psi_{[\mu}\psi_{\nu]},\\
\widehat H_{\mu\nu\rho}
&=H_{\mu\nu\rho}-\frac34\bar\psi_{[\mu}\gamma_\nu\psi_{\rho]},\\
\mathcal D_a\psi^i
&=\left(\frac14\widehat G_{bc}-T_{bc}\right)\gamma^{bc}\psi_a^i
-\frac g2L^{ij}\psi_{aj}-\phi_a^i
\end{aligned}
```

is retained; $`\psi^i=0`$ does not set the last line to zero.

## Reconciliation of connection and derivative conventions

Connection signs used in convention conversions are also fixed by the root file:

```math
\begin{aligned}
\nabla_\mu T_{ab}
&=\partial_\mu T_{ab}
-\omega_\mu{}^c{}_aT_{cb}-\omega_\mu{}^c{}_bT_{ac}\\
&=\partial_\mu T_{ab}+2\omega_\mu{}^c{}_{[a}T_{b]c},\\
\left.\mathcal D_\mu\chi^i\right|_{b}
&=-w(\chi)b_\mu\chi^i=-\frac32b_\mu\chi^i.
\end{aligned}
```

In $`\widehat R'(M)`$, the working term is $`+8\bar\psi_{[\mu}e_{\nu]}{}^{[a}\gamma^{b]}\chi`$. Conversion from the $`-8`$ expression with the same index order also transforms the dependent connection:

```math
\Delta f_\mu{}^a=2\bar\psi_\mu\gamma^a\chi,\qquad
\Delta\widehat R(M)
=\Delta\widehat R'(M)+8\Delta f_{[\mu}{}^{[a}e_{\nu]}{}^{b]}=0.
```

The torsionful connection is $`\omega_\pm=\omega\pm\widehat H`$, and the derivative is the full $`\mathcal D`$. Explicit conjugation rules and bar phases unspecified by the root file are not silently imported from subsidiary sources.

```math
\boxed{
S_{\rm full}=S_{\mathrm{record},\le2}+S_{\mathrm{fermi}\ge4},
\qquad
S_{\mathrm{fermi}\ge4}\ \text{is not fully determined by these inputs}.
}
```

The normalizations were fixed by the symbolic coefficient calculations above; this does not verify SUSY invariance or full fermionic completion of every component.

## Independent symbolic checks of source discrepancies

In this section, $`[X]_{\mathfrak m}`$ selects the specified independent monomial coefficient in $`X`$; it does not set other fields to zero. No numerical value has been assigned to any free coupling, field component or ratio. Inverse powers of $`L`$ and $`\sigma`$ are used only on the domains $`L\ne0`$, $`\sigma\ne0`$. No new gauge, background or auxiliary-field equation is imposed.

| Discrepancy | Independent-check result | Scope |
|---|---|---|
| $`NL^{-5}L_{k(i}L_{j)m}\bar\varphi^k\varphi^m`$ in the linear–vector map | $`-3i`$ instead of $`-4/3`$ | $`\delta\rho`$, $`\delta\lambda`$ and scalar Clifford projection |
| $`\gamma_{ab}T^{ab}T^{cd}\widehat R_{cd}(Q)`$ in the Weyl spinor | $`8/3`$; $`16/3`$ leaves a residual | This monomial of $`\delta L_W`$ |
| Epsilon tensor versus density symbol | $`\epsilon=e\varepsilon`$; an extra $`e^{-1}`$ cannot accompany the tensor | Local density |
| $`C\cdot P`$ and $`C\cdot E`$ | There are two explicit fermionic-completion differences | Local BF density |
| $`(\mathord{\not{\mathcal D}}\rho)\lambda`$ in the mixed map | $`i/4`$ | The written symmetric two-vector sum |
| LOG H3.9 | $`+i/4`$ | $`W^{-3}\lambda\lambda\nabla X`$ in the six-spinor-derivative definition |
| The two $`K`$ coefficients in LOG $`[S,\nabla_a]`$ | $`+i/8,-i/4`$ | $`K`$ component of the $`S,\nabla_\alpha,\nabla_\beta`$ Jacobi identity |
| $`w^2D`$ in the LOG scalar | Projection $`-23/8`$ of the raw $`Y`$ polynomial | Transformation check of two source expressions |
| LOG $`R^{\mathrm S}ww`$ | The supplied raw polynomial produces $`3/8`$; its difference from $`1/4`$ is $`1/8`$ | Local polynomial equality with explicit divergence |
| Algebraic mixing in the gravitino shift | $`8as`$ in the linear Majorana-bar representation | Algebra of the field transformation used in the source |

<a id="1-the-nvarphi2-coefficient-of-the-linearvector-map"></a>

### The $`N\varphi^2`$ coefficient of the linear–vector map

The linear–vector map coefficient follows from the transformations below.

Temporary definitions:

```math
B_{ij}:=\bar\varphi_i\varphi_j=B_{ji},\qquad
Q_\varphi:=L^{ij}B_{ij},\qquad L^2=L^{ij}L_{ij}.
```

Scalar-map definition and root transformations:

```math
\rho_L=2NL^{-1}+iL^{-3}Q_\varphi,\quad
\delta L_{ij}=i\bar\epsilon_{(i}\varphi_{j)},\quad
\delta\varphi^i\big|_N=\tfrac12N\epsilon^i,\quad
\delta\rho_L=\tfrac i2\bar\epsilon^i\lambda_{Li}.
```

First vary the norm and bilinear:

```math
\delta L=L^{-1}L^{ij}\delta L_{ij},\qquad
(\delta Q_\varphi)_N=N L^{ij}\bar\epsilon_i\varphi_j.
```

Therefore,

```math
\begin{aligned}
(\delta\rho_L)_{N\epsilon\varphi}
&=-2NL^{-2}\delta L+iL^{-3}(\delta Q_\varphi)_N\\
&=(-2i+i)NL^{-3}L^{ij}\bar\epsilon_i\varphi_j,\\
(\delta\rho_L)_{\epsilon\varphi^3}
&=-3iL^{-4}\delta L\,Q_\varphi+iL^{-3}\delta L^{ij}B_{ij}\\
&=3L^{-5}L^{ij}\bar\epsilon_i\varphi_jQ_\varphi
-L^{-3}\bar\epsilon^i\varphi^kB_{ki}.
\end{aligned}
```

The $`i\bar\epsilon^i/2`$ coefficients of these two equalities:

```math
\lambda_{Li}\big|_{N\varphi,\varphi^3}
=-2NL^{-3}L_{ij}\varphi^j
-6iL^{-5}L_{ij}\varphi^jQ_\varphi
+2iL^{-3}\varphi^kB_{ki}.
```

Cubic terms must be retained: $`\delta\varphi|_N`$ lowers them to degree $`N\varphi^2`$. Since the lower-index vector transformation has $`\delta\lambda_{Li}\supset Y_{Lij}\epsilon^j`$, the scalar Clifford coefficient is selected using $`\mathop{\mathrm{tr}}\nolimits_{\rm spin}/4`$. The four contributions evaluated separately are:

```math
\begin{aligned}
A_i&=6NL^{-4}\delta L\,L_{ij}\varphi^j,\\
B_i^{\rm var}&=-2NL^{-3}\delta L_{ij}\varphi^j,\\
C_i&=-6iL^{-5}L_{ij}\,\delta_N(\varphi^jQ_\varphi),\\
D_i^{\rm var}&=2iL^{-3}\delta_N(\varphi^kB_{ki}).
\end{aligned}
```

Here $`\delta_N`$ denotes only the substitution $`\delta\varphi=N\epsilon/2`$. Since the product variation is even, the Leibniz rule has no extra minus sign; Grassmann signs are retained when moving $`\epsilon`$ to the left. For example, $`\delta_N(\varphi^jQ_\varphi)=(N\epsilon^j/2)Q_\varphi+\varphi^j\delta_N Q_\varphi`$. The four results from the identity-matrix component of the root Fierz identity are:

```math
\begin{array}{c|cc}
 & iNL^{-3}B_{ij}&iNL^{-5}L_{ij}Q_\varphi\\\hline
\mathsf P_0 A&3/4&-3/2\\
\mathsf P_0 B^{\rm var}&-1/4&0\\
\mathsf P_0 C&-3/4&-3/2\\
\mathsf P_0 D^{\rm var}&5/4&0\\\hline
\text{total}&1&-3
\end{array}
```

These coefficients were also checked individually using a general antisymmetric spinor-pairing matrix and all symbolic Grassmann components; reduction used only the identity $`L^2=L^{ij}L_{ij}`$.

```math
Y_{Lij}\big|_{N\varphi^2}
=iNL^{-3}B_{ij}-3iNL^{-5}L_{ij}Q_\varphi.
```

For the basis used in the source, define $`K_{ij}:=L_{k(i}L_{j)m}\bar\varphi^k\varphi^m`$. The two-dimensional $`SU(2)`$ algebra gives:

```math
K_{ij}=L_{ij}Q_\varphi-\frac{L^2}{2}B_{ij},\qquad
L^{ij}K_{ij}=\frac{L^2}{2}Q_\varphi.
```

This identity is verified for general $`L_{ij}=\left(\begin{smallmatrix}u&v\\v&w\end{smallmatrix}\right)`$ and general symmetric $`B_{ij}`$ by expanding the matrix product using $`L^2=2(uw-v^2)`$; $`u,v,w`$ remains symbolic. Thus, in the original fields

```math
\boxed{
Y_{Lij}\big|_{N\varphi^2}
=-\frac i2NL^{-3}\bar\varphi_{(i}\varphi_{j)}
-3iNL^{-5}L_{k(i}L_{j)m}\bar\varphi^k\varphi^m .}
```

This result keeps $`L`$ and $`g`$ symbolic and imposes no AdS relation.

<a id="2-the-83163-difference-in-the-weyl-spinor"></a>

### The $`8/3`$–$`16/3`$ difference in the Weyl spinor

The comparison concerns the spinor coefficients in the [local Weyl map](../weyl2/action/details/linear_multiplet.md) and [Özkan–Pang (5.8)](https://arxiv.org/abs/1301.6622). The primary reference for the curvature relations is [Bergshoeff et al., (3.18)–(3.23)](https://arxiv.org/html/hep-th/0104113); the required $`T\widehat R(Q)`$ part is recalculated below from the definition and Bianchi identity.

Temporarily write $`\mathcal R_{ab}:=\widehat R_{ab}(Q)`$ and $`A:=\gamma^{ab}T_{ab}`$. The root constraint is $`\gamma^a\mathcal R_{ab}=0`$. For an arbitrary two-form spinor $`U_{ab}`$, the projection satisfying this constraint is

```math
(\Pi U)_{ab}=U_{ab}
+\frac13\gamma_a\gamma^cU_{bc}
-\frac13\gamma_b\gamma^cU_{ac}
-\frac1{12}\gamma_{ab}\gamma^{cd}U_{cd}
```

Indeed, Clifford multiplication gives $`\gamma^a(\Pi U)_{ab}=0`$; if $`\gamma^aU_{ab}=0`$, the three additional terms vanish. Also, $`\Pi(\gamma_a v_b-\gamma_bv_a)=0`$.

One must also check that no independent $`T^2\epsilon`$ contribution survives in $`\delta\mathcal R`$. $`\delta\psi_a|_T=iA\gamma_a\epsilon`$ and $`\widehat R'_{ab}(Q)|_T=2iA\gamma_{[a}\psi_{b]}`$ give this candidate contribution as

```math
U_{ab}^{(T^2)}=-A\gamma_aA\gamma_b+A\gamma_bA\gamma_a
```

In the Clifford expansion

```math
\begin{aligned}
A\gamma_aA&=V_a{}^b\gamma_b+Z_a,\\
V_a{}^b&=-2T_{cd}T^{cd}\delta_a{}^b-8T_{ac}T^{cb},\\
Z_a&=\gamma_a{}^{bcde}T_{bc}T_{de}.
\end{aligned}
```

$`V_{ab}`$ is symmetric; in five dimensions, $`Z_a`$ is central in spinor space. Hence

```math
U_{ab}^{(T^2)}=\gamma_av_b-\gamma_bv_a,
\quad v_a=-V_a{}^b\gamma_b+Z_a,
\quad \Pi U^{(T^2)}=0.
```

Now let $`S_{ab}:=[\widehat R_{ab}(S)]_{T\mathcal R}`$. When taking the covariant exterior derivative of the $`Q`$ curvature,

```math
d_\omega(A\gamma\wedge\psi)
=d_\omega A\wedge\gamma\wedge\psi-A\gamma\wedge d_\omega\psi,
\quad
d_\omega(\gamma\wedge\phi)=-\gamma\wedge d_\omega\phi
```

the signs fix the algebraic $`T\mathcal R`$ part of the Bianchi identity:

```math
\gamma_aS_{bc}+\gamma_bS_{ca}+\gamma_cS_{ab}
=F_{abc},\qquad
F_{abc}:=A(\gamma_a\mathcal R_{bc}+\gamma_b\mathcal R_{ca}+\gamma_c\mathcal R_{ab}).
```

This equation is invertible. With the definitions $`K_{bc}:=\gamma^aF_{abc}`$, $`k_c:=\gamma^bK_{bc}`$, $`s_c:=\gamma^bS_{bc}`$,

```math
\begin{aligned}
K_{bc}&=S_{bc}+\gamma_bs_c-\gamma_cs_b,\\
k_c&=4s_c+\gamma_c\gamma^ds_d,\qquad
\gamma^ck_c=9\gamma^cs_c,\\
S_{bc}&=K_{bc}-\frac14(\gamma_bk_c-\gamma_ck_b)
+\frac1{18}\gamma_{bc}\gamma^dk_d.
\end{aligned}
```

Substituting the explicit expression for $`F`$ and using $`\gamma^a\mathcal R_{ab}=0`$, this inversion gives the algebraic part:

```math
\begin{aligned}
S_{ab}={}&-\frac83\gamma_{ab}T^{cd}\mathcal R_{cd}
+12\gamma_dT^{cd}\gamma_{[a}\mathcal R_{b]c}
-3A\mathcal R_{ab}-8T^c{}_{[a}\mathcal R_{b]c}.
\end{aligned}
```

The back-substitution checks are the identities

```math
\gamma_aS_{bc}+\gamma_bS_{ca}+\gamma_cS_{ab}-F_{abc}=0,
\qquad \gamma^{ab}S_{ab}=-\frac83T^{ab}\mathcal R_{ab}
```

Both equalities and the inversion above were checked in exact Clifford algebra for every independent spinor coefficient of general symbolic $`T_{ab}`$ and $`\Pi U`$.

To reduce the required contraction, use

```math
\gamma^{ecd}\mathcal R_{cd}=0,
\qquad
\varepsilon^{eabcd}\gamma_{ab}\mathcal R_{cd}
=2i\gamma^{ecd}\mathcal R_{cd}=0
```

Since the Hodge map is invertible, $`\gamma_{[ab}\mathcal R_{cd]}=0`$. Multiplication by $`T^{ab}T^{cd}`$ gives

```math
\begin{aligned}
0&=2A T^{cd}\mathcal R_{cd}
-4T^{ab}T^{cd}\gamma_d\gamma_a\mathcal R_{bc},\\
T^{ab}T^c{}_a\mathcal R_{bc}&=0,\\
T^{ab}S_{ab}
&=\left(-\frac83+12\frac12-3\right)A T^{cd}\mathcal R_{cd}
=\frac13A T^{cd}\mathcal R_{cd}
\end{aligned}
```

The second line uses the symmetry of $`T^{ab}T^c{}_a`$ in $`b,c`$.

The covariant curl of the $`\delta V|_{\phi,\psi}=-3i\bar\epsilon\phi/2+i\bar\epsilon A\psi`$ transformation of the $`V`$ connection gives, for the required curvature coefficients only,

```math
\delta\widehat R_{ab}(V)\big|_{R(S),T\mathcal R}
=-\frac{3i}{2}\bar\epsilon\widehat R_{ab}(S)
+i\bar\epsilon A\mathcal R_{ab}
```

Using $`L_{Wij}\supset(16/3)\widehat R_{abij}(V)T^{ab}`$ and $`\delta L_{Wij}=i\bar\epsilon_{(i}\varphi_{Wj)}`$,

```math
\begin{aligned}
\delta L_{Wij}\big|_{T^2\mathcal R}
&=\frac{16i}{3}\bar\epsilon_{(i}
\left[-\frac32\frac13+1\right]
A T^{cd}\mathcal R_{cd\,j)},\\
\boxed{\begin{aligned}\varphi_W^i\big|_{T^2\mathcal R}
&=\frac83\gamma_{ab}T^{ab}T^{cd}\widehat R_{cd}{}^i(Q).\end{aligned}}
\end{aligned}
```

Choosing $`16/3`$ leaves the residual $`-8i\bar\epsilon_{(i}\gamma_{ab}T^{ab}T^{cd}\widehat R_{cd\,j)}(Q)/3`$ in $`\delta L_W-i\bar\epsilon\varphi_W`$. This result verifies only that coefficient, not the complete local $`N_W,E_W`$ expressions.

<a id="3-density-the-pe-distinction-and-the-hatted-field-strength"></a>

### Density, the $`P`$–$`E`$ distinction and the hatted field strength

Directly from the root definitions

```math
\begin{aligned}
e^{-1}\epsilon^{\mu\nu\rho\sigma\lambda}
&=\varepsilon^{\mu\nu\rho\sigma\lambda},\\
-\frac1{12}e^{-1}C_\mu\epsilon^{\mu\nu\rho\sigma\lambda}\partial_\nu E_{\rho\sigma\lambda}
&=-\frac1{12}C_\mu\varepsilon^{\mu\nu\rho\sigma\lambda}\partial_\nu E_{\rho\sigma\lambda}.
\end{aligned}
```

An additional $`e^{-1}`$ on the right would violate equality. The ordinary-derivative expression here is the potential representation of $`C\cdot P`$; it must not be confused with the supercovariant definition of $`E^\mu`$:

```math
\begin{aligned}
P^a-E^a&=\frac i2\bar\psi_b\gamma^{ba}\varphi
+\frac14L_{ij}\bar\psi_b^i\gamma^{abc}\psi_c^j,\\
-4gC_a(P^a-E^a)
&=-2igC_a\bar\psi_b\gamma^{ba}\varphi
-gC_aL_{ij}\bar\psi_b^i\gamma^{abc}\psi_c^j.
\end{aligned}
```

The boundary term is also retained explicitly:

```math
\begin{aligned}
C_\mu P^\mu
&=C_\mu e^{-1}\partial_\nu(eE^{\mu\nu})\\
&=e^{-1}\partial_\nu(eC_\mu E^{\mu\nu})
-(\partial_\nu C_\mu)E^{\mu\nu}\\
&=e^{-1}\partial_\nu(eC_\mu E^{\mu\nu})
+\frac12G_{\mu\nu}E^{\mu\nu}.
\end{aligned}
```

For a general vector, the definition of $`\widehat F_{ab}=F_{ab}-\bar\psi_{[a}\gamma_{b]}\lambda+i\rho\bar\psi_{[a}\psi_{b]}/2`$ reconciles the BF representatives through:

```math
\begin{aligned}
\frac12\widehat F_{ab}E^{ab}
+\frac12E^{ab}\bar\psi_a\gamma_b\lambda
-\frac i4\rho E^{ab}\bar\psi_a\psi_b
&=\frac12F_{ab}E^{ab}
+\left(-\frac12+\frac12\right)E^{ab}\bar\psi_a\gamma_b\lambda\\
&\quad+\left(\frac i4-\frac i4\right)\rho E^{ab}\bar\psi_a\psi_b
=\frac12F_{ab}E^{ab}.
\end{aligned}
```

This equality verifies the joint transformation of all three terms, not merely the replacement $`\widehat F\mapsto F`$.

<a id="4-phase-of-the-mixed-linear-map"></a>

### Phase of the mixed linear map

Let the initial definition under examination be, as in the [mixed-map source](../common/details/superconformal_definitions.md),

```math
L^{\rm mix}_{ij}=\rho_1Y_{2ij}+\rho_2Y_{1ij}
-\frac i2\bar\lambda_{1(i}\lambda_{2j)}
```

The defining vector transformation is $`\delta\lambda_{Ai}|_{\mathcal D\rho}=-i(\mathord{\not{\mathcal D}}\rho_A)\epsilon_i/2`$. Applying the scalar-bilinear flip followed by the rank-one flip gives

```math
(\delta\bar\lambda_{1(i})\lambda_{2j)}\big|_{\mathcal D\rho}
=\bar\lambda_{2(j}\delta\lambda_{1i)}\big|_{\mathcal D\rho}
=-\frac i2\bar\epsilon_{(i}(\mathord{\not{\mathcal D}}\rho_1)\lambda_{2j)}
```

Therefore

```math
\begin{aligned}
\delta L^{\rm mix}_{ij}\big|_{\mathcal D\rho}
&=\left(-\frac i2\right)\left(-\frac i2\right)
\bar\epsilon_{(i}\big[(\mathord{\not{\mathcal D}}\rho_1)\lambda_{2j)}
+(\mathord{\not{\mathcal D}}\rho_2)\lambda_{1j)}\big]\\
&=-\frac14\bar\epsilon_{(i}\big[(\mathord{\not{\mathcal D}}\rho_1)\lambda_{2j)}
+(\mathord{\not{\mathcal D}}\rho_2)\lambda_{1j)}\big],\\
ic&=-\frac14\quad\Longrightarrow\quad
\boxed{\varphi^{\rm mix}_i\big|_{\mathcal D\rho}
=\frac i4\big[(\mathord{\not{\mathcal D}}\rho_1)\lambda_{2i}
+(\mathord{\not{\mathcal D}}\rho_2)\lambda_{1i}\big].}
\end{aligned}
```

Choosing $`c=1/4`$ leaves a transformation residual with coefficient $`-(1+i)/4`$. $`S`$-primarity also gives, for $`\delta_SY_{Aij}=d\bar\eta_{(i}\lambda_{Aj)}`$,

```math
\delta_SL^{\rm mix}_{ij}
=(d-i/2)\bar\eta_{(i}(\rho_1\lambda_{2j)}+\rho_2\lambda_{1j)})=0
\quad\Longrightarrow\quad d=i/2
```

Moreover, using $`\delta\lambda|_{\mathcal D\rho}=-i\mathord{\not{\mathcal D}}\rho\epsilon/2`$ and $`\delta\psi_\mu|_{\partial\epsilon}=\partial_\mu\epsilon`$,

```math
\big[\delta(\partial_\mu\lambda_i
+c_D\mathord{\not{\mathcal D}}\rho\,\psi_{\mu i})\big]_{\partial\epsilon}
=(-i/2+c_D)\mathord{\not{\mathcal D}}\rho\,\partial_\mu\epsilon_i,
\quad \boxed{c_D=i/2}.
```

This check excludes the real $`1/2`$ option in the derivative. These three coefficients alone cannot determine the full $`\delta Y`$ transformation or all components of the mixed multiplet.

<a id="5-log-h39-sign"></a>

### LOG: H3.9 sign

Only source indices are used here; conversion to the working frame uses $`\Gamma^a=i\gamma^a`$, $`\Sigma^{ab}=\gamma^{ab}/2`$, $`\varepsilon_{\mathrm G}^{abcde}=-\varepsilon^{abcde}`$. No numerical epsilon orientation is chosen. $`W`$ is the vector scalar; $`X^{ij}`$ is the vector triplet, whereas $`X_\alpha^i`$ is a distinct Weyl field.

The initial definition is [LOG Step 2, S2-01](../log/action/details/component_construction/results/gauged_full_fermionic_log/STEP_02_LOG_PRIMARY.md):

```math
H^{ij}=-\frac{3i}{40}\Delta^{ijkl}\nabla_{kl}\log W,
\qquad
\Delta^{ijkl}=-\frac1{96}\varepsilon^{\alpha\beta\gamma\delta}
\nabla_\alpha^{(i}\nabla_\beta^j\nabla_\gamma^k\nabla_\delta^{l)}.
```

$`+`$ and $`-`$ are merely two $`SU(2)`$ index labels. Let $`D_\alpha:=\nabla_\alpha^+`$ and $`B^{--}:=\lambda^{\alpha-}\lambda_\alpha^-`$. The same-$`+`$ anticommutator vanishes; antisymmetry over five spinor indices and the $`SU(2)`$ contraction give

```math
\Delta^{++kl}\nabla_{kl}
=(1+\tfrac12+\tfrac16)\Delta^{++++}\nabla^{--}
=\frac53\Delta^{++++}\nabla^{--}
```

Using $`\nabla_\alpha W=i\lambda_\alpha`$,

```math
H^{++}=-\frac12\Delta^{++++}(W^{-1}X^{--})
-\frac i8\Delta^{++++}(W^{-2}B^{--}).
```

The desired monomial comes from the derivative distributions $`2+2`$ and $`1+3`$. The first coefficient is $`(-1/2)(-1/96)\binom42(-2)=-1/16`$; the intermediate coefficient of the second is $`(-i/8)(-1/96)\binom41(-2i)=1/96`$. In $`\varepsilon^{\alpha\beta\gamma\delta}\lambda_\alpha^+D_\beta D_\gamma D_\delta B^{--}`$, when three derivatives act on the same gaugino, the factor $`(-2)\times3=-6`$ appears. Thus

```math
\begin{aligned}
[H^{++}]_{W^{-3}\lambda^2\nabla X}
=-\frac1{16W^3}\Big[
&\varepsilon^{\alpha\beta\gamma\delta}\lambda_\alpha^+\lambda_\beta^+
(D_\gamma D_\delta X^{--})_{\nabla X}\\
&+\lambda^{\alpha+}(D_\alpha D^{++}\lambda_\rho^-)_{\nabla X}\lambda^{\rho-}
\Big].
\end{aligned}
```

The relevant coefficients of the source vector constraints are differentiated directly:

```math
\begin{aligned}
D_\delta X^{--}&\supset2i(\Gamma^a)_\delta{}^\rho\nabla_a\lambda_\rho^-,
&D_\gamma\lambda_\rho^-&\supset-\varepsilon_{\gamma\rho}X^{+-},\\
(D_\gamma D_\delta X^{--})_{\nabla X}
&=2i(\Gamma^a)_{\gamma\delta}\nabla_aX^{+-},\\
D^{++}\lambda_\rho^-&\supset4i\nabla_\rho{}^\tau\lambda_\tau^+,
&D_\alpha\lambda_\tau^+&=-\varepsilon_{\alpha\tau}X^{++},\\
(D_\alpha D^{++}\lambda_\rho^-)_{\nabla X}
&=4i(\Gamma^a)_{\alpha\rho}\nabla_aX^{++}.
\end{aligned}
```

The remaining curvature and torsion terms of $`[D_\alpha,\nabla_a]`$ do not contain this independent $`\nabla X^{ij}`$ monomial; the commutator has not been set to zero. Using $`\varepsilon^{\alpha\beta\gamma\delta}(\Gamma^a)_{\gamma\delta}=-2(\Gamma^a)^{\alpha\beta}`$,

```math
\begin{aligned}
[H^{++}]_{W^{-3}\lambda^2\nabla X}
&=\frac{i}{4W^3}(\Gamma^a)^{\alpha\beta}
\big[\lambda_\alpha^+\lambda_\beta^+\nabla_aX^{+-}
-\lambda_\alpha^+\lambda_\beta^-\nabla_aX^{++}\big],\\
\boxed{\begin{aligned}[H^{ij}]_{W^{-3}\lambda^2\nabla X}
&=\frac{i}{4W^3}(\Gamma^a)^{\alpha\beta}
\lambda_\alpha^{(i}(\nabla_aX^{j)k})\lambda_{\beta k}.\end{aligned}}
\end{aligned}
```

The last line uses the source $`SU(2)`$ lowering rules $`\lambda_+=-\lambda^-`$, $`\lambda_-=\lambda^+`$. The difference from the printed $`-i/4`$ is the same monomial with coefficient $`+i/2`$. This calculation verifies only H3.9; it does not replace a check of all 58 terms.

<a id="6-log-jacobi-check-of-the-snabla_a-phases"></a>

### LOG: Jacobi check of the $`[S,\nabla_a]`$ phases

Write the disputed terms with an initially unknown $`a_X,a_W`$:

```math
[S_{\delta l},\nabla_a]\big|_K
=\left[\frac{a_X}{8}(\Gamma_a\Gamma^c)_\delta{}^\gamma X_{\gamma l}
-\frac{a_W}{4}W_a{}^c{}_{\delta l}\right]K_c.
```

The right-hand side of the $`S,\nabla_\alpha,\nabla_\beta`$ Jacobi identity in the source [C24 algebra record](../log/action/details/component_construction/results/gauged_full_fermionic_log/sources/reference_fragments/10_gold_source_equations_and_bridge.md) contains no $`K`$. On the left, since $`R(S)`$ is Grassmann odd,

```math
[S,-R(S)S']=-(SR(S))S'+R(S)\{S,S'\}.
```

With this sign, the $`K_c`$ coefficient is

```math
\mathscr J=-2i\varepsilon^{ij}(\Gamma^a)_{\alpha\beta}\mathcal V_{\delta l,a}{}^c
-S_{\delta l}R(K)_{\alpha\beta}^{ij,c}
+R(S)_{\alpha\beta}^{ij,\gamma k}\{S_{\delta l},S_{\gamma k}\}\big|_{K_c}
```

Here $`\mathcal V`$ is the bracket above. The source curvature coefficients under examination are

```math
\begin{aligned}
R(S)_{\alpha\beta}^{ij,\gamma k}
&=i\varepsilon^{ij}\left(\frac34\varepsilon_{\alpha\beta}X^{\gamma k}
+\delta_{[\alpha}^{\gamma}X_{\beta]}{}^k\right),\\
R(K)_{\alpha\beta}^{ij,c}
&=\varepsilon^{ij}\left[-\frac i2\varepsilon_{\alpha\beta}\nabla^bW_b{}^c
+\frac i2(\Gamma^a)_{\alpha\beta}\nabla^d\widetilde W_{da}{}^c
-\frac i{32}(\Gamma^c)_{\alpha\beta}Y\right]+R(K)|_{W^2}
\end{aligned}
```

Since $`SW=0`$, $`S(R(K)|_{W^2})=0`$. The Weyl-derivative definition is used as

```math
\nabla_\eta W_{bc}=W_{bc\eta}+(\Sigma_{bc})_\eta{}^\nu X_\nu
```

The required $`SY`$ coefficient can also be checked from its definition:

```math
X_\beta^j=\frac25\nabla^{\rho j}W_{\rho\beta},\quad
S_{\alpha i}X_\beta^j=\frac25(-2+10+2)\delta_i{}^jW_{\alpha\beta}
=4\delta_i{}^jW_{\alpha\beta}.
```

The three contributions here are, respectively, dilatation and the Lorentz generators acting on the two spinor indices of $`W`$. On $`Y=i\nabla^{\gamma k}X_{\gamma k}`$, the $`\{S,\nabla\}=2\varepsilon\mathbb D-4M+6\varepsilon J`$ and then $`-\nabla(SX)`$ contributions give

```math
S_{\alpha i}Y=i(-3+10-9+10)X_{\alpha i}=8iX_{\alpha i}
```

Explicit identities used in the Clifford/Fierz reduction:

```math
\begin{gathered}
\Gamma^b\Sigma_b{}^c=2\Gamma^c,\qquad
\Gamma^d\Gamma_{da}{}^c=-3\Gamma_a{}^c,\qquad
\Gamma^d\widetilde W_{da}{}^c=W_a{}^c,\\
4(\Gamma^c)_{\delta[\alpha}X_{\beta]}
=\varepsilon_{\alpha\beta}(\Gamma^cX)_\delta
-(\Gamma^a)_{\alpha\beta}(\Gamma_a\Gamma^cX)_\delta
-2(\Gamma^c)_{\alpha\beta}X_\delta.
\end{gathered}
```

The third identity is the two-form dual of the gamma-trace constraint of type $`\gamma^{ab}\mathcal R_{ab}=0`$; the last is the $`\Gamma=i\gamma`$ representation of the root Fierz relation. Temporarily suppressing the common factor $`\varepsilon^{ij}`$, the two curvature contributions are explicitly

```math
\begin{aligned}
-SR(K)={}&-\varepsilon_{\alpha\beta}(\Gamma^cX)_\delta
-\frac34(\Gamma^a)_{\alpha\beta}(\Gamma_a{}^cX)_\delta
-\frac14(\Gamma^c)_{\alpha\beta}X_\delta
+\frac12(\Gamma^a)_{\alpha\beta}W_a{}^c{}_{\delta l},\\
R(S)\{S,S\}|_K={}&\varepsilon_{\alpha\beta}(\Gamma^cX)_\delta
+\frac12(\Gamma^a)_{\alpha\beta}(\Gamma_a{}^cX)_\delta
+\frac12(\Gamma^c)_{\alpha\beta}X_\delta.
\end{aligned}
```

The suppressed $`l`$ index is the same for the $`X`$ objects. Taking the sum and using $`\Gamma_a\Gamma^c=\Gamma_a{}^c-\delta_a{}^c`$, now retaining all indices,

```math
\begin{aligned}
\mathscr J={}&-\frac i4(a_X-i)\varepsilon^{ij}(\Gamma^a)_{\alpha\beta}
(\Gamma_a\Gamma^c)_\delta{}^\gamma X_{\gamma l}\\
&+\frac i2(a_W-i)\varepsilon^{ij}(\Gamma^a)_{\alpha\beta}W_a{}^c{}_{\delta l}.
\end{aligned}
```

Coefficients of independent Weyl descendants must vanish separately:

```math
\boxed{a_X=i,\qquad a_W=i},\qquad
\boxed{[S_{\beta i},\nabla_a]\big|_K
=\left[\frac i8(\Gamma_a\Gamma^b)_\beta{}^\gamma X_{\gamma i}
-\frac i4W_a{}^b{}_{\beta i}\right]K_b.}
```

This check assigns no numerical values to fields and changes no other $`[S,\nabla_a]`$ coefficients. This Jacobi calculation does not automatically verify propagation of the phase change to every LOG $`N,E_a`$ component.

<a id="7-log-bosonic-coefficients-equality-between-source-polynomials"></a>

### LOG bosonic coefficients: equality between source polynomials

The objects checked here are the raw and reduced polynomials in the [bosonic source check](../log/action/details/component_construction/results/gauged_full_fermionic_log/notes/05_two_bosonic_corrections_source_audit.md). A complete derivation of the raw polynomial from six spinor derivatives is not assumed; the results below establish its rewriting and the discrepancy between the two records.

The first target is the image of the source polynomial

```math
\frac3{2048}Y^2+\frac{69}{1024}w^{ab}w_{ab}Y-\frac3{32}\Box Y
```

under the definition $`D=-3Y|/128`$. This $`Y`$ is not the vector triplet. Exact rational arithmetic:

```math
\begin{aligned}
Y|&=-\frac{128}{3}D,\\
\frac3{2048}\left(-\frac{128}{3}D\right)^2&=\frac83D^2,\\
\frac{69}{1024}w^2\left(-\frac{128}{3}D\right)&=-\frac{23}{8}w^2D,\\
-\frac3{32}\Box\left(-\frac{128}{3}D\right)&=4\Box D.
\end{aligned}
```

Thus the projection of this polynomial is $`\boxed{8D^2/3-23w^2D/8+4\Box D}`$, not the printed $`+368w^2D/3`$. In the source $`-WF_{\log}`$ BF term, the counterpart is $`+23Ww^2D/8`$. No additional copy is added to an action already containing this term.

The second target is the $`w^2`$ coefficients of two polynomials already written in the source's $`W=1`$ notation; this comparison imposes no new gauge. Temporary definitions:

```math
\begin{aligned}
J&:=R^{\mathrm S}_{abcd}w^{ab}w^{cd},&
K&:=R^{\mathrm S}_{ab}w^{ac}w^b{}_c,\\
\mathcal N&:=(\nabla_cw_{ab})(\nabla^cw^{ab}),&
P&:=(\nabla^cw^a{}_b)(\nabla^bw_{ac}),\quad
Q:=(\nabla^bw^a{}_b)(\nabla^cw_{ac}).
\end{aligned}
```

Here $`\nabla`$ is only the torsion-free metric connection for this bosonic coefficient; it does not replace $`\mathcal D`$ in the full action. The source curvature convention is fixed by

```math
[\nabla_a,\nabla_b]w_{cd}
=-R^{\mathrm S}_{ab c}{}^e w_{ed}-R^{\mathrm S}_{ab d}{}^e w_{ce},
\qquad R^{\mathrm S}_{ab}=g^{cd}R^{\mathrm S}_{acbd}
```

Contracting the Bianchi identity with two $`w`$ objects gives

```math
0=J-2R^{\mathrm S}_{acbd}w^{ab}w^{cd},\qquad
R^{\mathrm S}_{abcd}w^{ac}w^{bd}=\frac12J
```

Let the raw polynomial being compared be

```math
\begin{aligned}
\ell_{w,\rm raw}={}&\frac13J+\frac13R^{\mathrm S}_{abcd}w^{ac}w^{bd}
-K-\frac{27}{256}R^{\mathrm S}w^2
-\frac{39}{16}w^{ab}\nabla^2w_{ab}\\
&+\frac12w_{ac}\nabla^b\nabla^cw^a{}_b
-2w_{ac}\nabla^c\nabla^bw^a{}_b
-\frac{33}{16}\mathcal N-\frac94Q+\frac34P
\end{aligned}
```

Applying the Leibniz rule separately to three terms gives

```math
\begin{aligned}
-\frac{39}{16}w^{ab}\nabla^2w_{ab}
&=\frac{39}{16}\mathcal N-\frac{39}{16}\nabla_c(w^{ab}\nabla^cw_{ab}),\\
\frac12w_{ac}\nabla^b\nabla^cw^a{}_b
&=-\frac12P+\frac12\nabla^b(w_{ac}\nabla^cw^a{}_b),\\
-2w_{ac}\nabla^c\nabla^bw^a{}_b
&=2Q-2\nabla^c(w_{ac}\nabla^bw^a{}_b).
\end{aligned}
```

The first-derivative coefficients are $`39/16-33/16=3/8`$, $`-1/2+3/4=1/4`$, $`2-9/4=-1/4`$. The derivative-order difference is

```math
\begin{aligned}
P-Q={}&\nabla_c(w^a{}_b\nabla^bw_a{}^c)
-\nabla_b(w^{ab}\nabla^cw_{ac})
-w^a{}_b[\nabla^c,\nabla^b]w_{ac},\\
-w^a{}_b[\nabla^c,\nabla^b]w_{ac}
&=w^a{}_bR^{\mathrm S\,cb}{}_a{}^dw_{dc}
+w^a{}_bR^{\mathrm S\,cb}{}_c{}^dw_{ad}
=-\frac12J+K.
\end{aligned}
```

The first term in the last line follows from pair exchange and the Bianchi contraction above; the second is the defined Ricci contraction. Thus the $`J`$ coefficient is $`1/3+1/6-1/8=3/8`$, and the $`K`$ coefficient is $`-1+1/4=-3/4`$. Also using $`\mathcal N=\nabla_m(w^{ab}\nabla^mw_{ab})-w^{ab}\nabla^2w_{ab}`$, the **local** equality without boundary conditions is

```math
\boxed{
\begin{aligned}
\ell_{w,\rm raw}={}&\frac38R^{\mathrm S}_{abcd}w^{ab}w^{cd}
-\frac34R^{\mathrm S}_{ab}w^{ac}w^b{}_c
-\frac{27}{256}R^{\mathrm S}w^{ab}w_{ab}
-\frac38w^{ab}\nabla^2w_{ab}+\nabla_m\mathcal J^m,\\
\mathcal J^m={}&-\frac{33}{16}w^{ab}\nabla^mw_{ab}
+\frac34w_{ac}\nabla^cw^{am}
-\frac94w_a{}^m\nabla_bw^{ab}
\end{aligned}}
```

The difference from the record displaying $`J/4`$ is $`J/8`$ and the displayed divergence. By contrast, the other source contraction is

```math
\frac13R^{\mathrm S}_{abcd}F^{ab}F^{cd}
-\frac16R^{\mathrm S}_{acbd}F^{ab}F^{cd}
=\left(\frac13-\frac1{12}\right)R^{\mathrm S}_{abcd}F^{ab}F^{cd}
=\frac14R^{\mathrm S}_{abcd}F^{ab}F^{cd}
```

so the $`RFF`$ coefficient does not carry the same error.

The sign is also tracked in conversion to the working convention. Since the root lower-vector derivative satisfies $`[\nabla_a,\nabla_b]v_c=-R_{ab}{}^d{}_c v_d=+R_{ab c}{}^dv_d`$, $`R^{\mathrm S}_{abcd}=-R_{abcd}`$. Using $`w_{ab}=16T_{ab}/3`$, the image of the difference between the two polynomials is

```math
\frac18R^{\mathrm S}_{abcd}w^{ab}w^{cd}
=-\frac18\left(\frac{16}{3}\right)^2R_{abcd}T^{ab}T^{cd}
=\boxed{-\frac{32}{9}R_{abcd}T^{ab}T^{cd}}
```

This is not an independent SUSY proof that the raw polynomial is the correct action, and it has not been used as a term to add again to the effective LOG record.

<a id="8-composite-fields-dependent-connections-and-derivative-order"></a>

### Composite fields, dependent connections and derivative order

When the defining triplet constraint of the gauged map is

```math
2\sigma Y^{ij}-\frac i2\bar\psi^i\psi^j+gL^{ij}=0
```

the solution and back-substitution on the domain $`\sigma\ne0`$ are

```math
\begin{aligned}
Y^{ij}&=\frac{i}{4\sigma}\bar\psi^i\psi^j-\frac{g}{2\sigma}L^{ij},\\
2\sigma Y^{ij}-\frac i2\bar\psi^i\psi^j+gL^{ij}
&=\frac i2\bar\psi^i\psi^j-gL^{ij}-\frac i2\bar\psi^i\psi^j+gL^{ij}=0
\end{aligned}
```

This is not elimination of an auxiliary field from the target action; it solves the supplied defining constraint of the map. For $`B_\psi^{ij}:=\bar\psi^i\psi^j`$, the relevant product in the scalar map is

```math
\frac{Y^{ij}Y_{ij}}{4\sigma^2}
=-\frac{B_\psi^{ij}B_{\psi ij}}{64\sigma^4}
-\frac{ig}{16\sigma^4}L_{ij}B_\psi^{ij}
+\frac{g^2}{16\sigma^4}L^{ij}L_{ij}
```

For $`-8\sigma^2\chi^i+Y^{ij}\psi_j+g\varphi^i+\cdots=0`$ in the spinor constraint, solving only the relevant coefficients gives

```math
\chi^i\supset\frac{Y^{ij}\psi_j}{8\sigma^2}+\frac{g}{8\sigma^2}\varphi^i
=\frac{i}{32\sigma^3}(\bar\psi^i\psi^j)\psi_j
-\frac{g}{16\sigma^3}L^{ij}\psi_j+\frac{g}{8\sigma^2}\varphi^i
```

Since the scalar constraint also contains $`-4\sigma^2D+gN+\cdots=0`$, $`gN/(4\sigma^2)`$ is retained in $`D`$. These lines do not identify the complete $`D`$ difference with these terms alone: the $`g`$ dependence in $`\chi`$ and the full derivatives must also be carried through.

When evaluating the existing Poincaré representation, the $`\psi^i=0`$ condition does not set the covariant derivative constructed from the vector transformation to zero:

```math
\begin{aligned}
\mathcal D_\mu\psi^i
&\supset\frac14\gamma\!\cdot\!\widehat G\,\psi_\mu^i
+\frac i2\mathord{\not{\mathcal D}}\sigma\,\psi_\mu^i
-\sigma\gamma\!\cdot\!T\psi_\mu^i+Y^{ij}\psi_{\mu j}-\sigma\phi_\mu^i,\\
\left.\mathcal D_a\psi^i\right|_{\rm existing\ gauge}
&=\left(\frac14\widehat G_{bc}-T_{bc}\right)\gamma^{bc}\psi_a^i
-\frac g2L^{ij}\psi_{aj}-\phi_a^i.
\end{aligned}
```

For the same reason, the $`K`$ connection in the constant dilaton's second derivative $`\mathcal D_a\mathcal D_b\sigma`$ remains $`2f_{ab}`$. With fermions present, $`f_{ab}`$ cannot generally be assumed symmetric; the order $`\mathcal D_a\mathcal D_b`$ cannot be changed without a verified commutator.

For the root $`\widehat R'(M)`$ sign difference, define $`J_\mu{}^a:=\bar\psi_\mu\gamma^a\chi`$. The Ricci traces and result of converting $`-8`$ to the root $`+8`$ are

```math
\begin{aligned}
\Delta\widehat R'_{\mu\nu}{}^{ab}&=-16J_{[\mu}{}^{[a}e_{\nu]}{}^{b]},\\
\Delta R_a{}^c&=-12J_a{}^c-4\delta_a{}^cJ_b{}^b,
&\Delta R&=-32J_a{}^a,\\
\Delta f_a{}^c
&=-\frac16\Delta R_a{}^c+\frac1{48}\delta_a{}^c\Delta R
=2J_a{}^c,\\
\Delta\widehat R_{\mu\nu}{}^{ab}(M)
&=-16J_{[\mu}{}^{[a}e_{\nu]}{}^{b]}
+8(2J_{[\mu}{}^{[a})e_{\nu]}{}^{b]}=0
\end{aligned}
```

Changing only the explicit term's sign while keeping $`f`$ fixed violates this equality. As an independent check, the curl of $`\delta\omega|_\chi=-4e^{[a}\bar\epsilon\gamma^{b]}\chi`$ gives $`-8`$ in the $`\partial\epsilon`$ coefficient; the explicit $`c\bar\psi_{[\mu}e_{\nu]}{}^{[a}\gamma^{b]}\chi`$ completion gives $`c`$. $`-8+c=0`$ fixes the root sign $`c=8`$.

The Lorentz and dilatation derivatives are also separate coefficient checks:

```math
\begin{aligned}
\nabla_\mu T_{ab}
&=\partial_\mu T_{ab}-\omega_\mu{}^c{}_aT_{cb}-\omega_\mu{}^c{}_bT_{ac}
=\partial_\mu T_{ab}+2\omega_\mu{}^c{}_{[a}T_{b]c},\\
\left[\tfrac14\omega_\mu{}^{cd}\gamma_{cd},T_{ab}\gamma^{ab}\right]
&=2\gamma^{ab}\omega_\mu{}^c{}_{[a}T_{b]c},\\
\delta_\Lambda[(\partial_\mu-cb_\mu)\chi]
&\supset(w_\chi-c)(\partial_\mu\Lambda)\chi,
\qquad w_\chi=\tfrac32\quad\Longrightarrow\quad c=\tfrac32.
\end{aligned}
```

This excludes the opposite Lorentz sign in the $`T`$ derivative and the $`-7b\chi/2`$ option in $`\mathcal D\chi`$. The full $`\delta\widehat H`$ fermionic completion, whose scope is separately restricted in the root file, is not corrected or verified by weight counting alone.

<a id="9-fermionic-mixing-the-two-cross-terms-do-not-cancel"></a>

### Fermionic mixing: the two cross terms do not cancel

For the fermionic shift, let $`a,s,t`$ be symbolic coefficients:

```math
\psi_\mu^i=\Psi_\mu^i+s\delta^{ij}\gamma_\mu\varphi_j,
\qquad
\bar\psi_\mu^i=\bar\Psi_\mu^i+t\delta^{ij}\bar\varphi_j\gamma_\mu.
```

Since the root file does not specify the Hermitian-conjugation phase, no conjugacy relation among $`s,t`$ is initially imposed. The five-dimensional Clifford algebra gives

```math
\gamma_\mu\gamma^{\mu\nu}=4\gamma^\nu,\qquad
\gamma^{\mu\nu}\gamma_\nu=4\gamma^\mu,\qquad
\gamma_\mu\gamma^{\mu\nu}\gamma_\nu=20
```

With $`S_\varphi:=\delta_{ij}\bar\varphi^i\varphi^j`$, explicit multiplication gives

```math
\begin{aligned}
a\delta_{ij}\bar\psi_\mu^i\gamma^{\mu\nu}\psi_\nu^j
={}&a\delta_{ij}\bar\Psi_\mu^i\gamma^{\mu\nu}\Psi_\nu^j
+4at\bar\varphi_j\gamma^\nu\Psi_\nu^j
+4as\bar\Psi_\mu^i\gamma^\mu\varphi_i
+20astS_\varphi.
\end{aligned}
```

Keeping index positions, the rank-one flip is

```math
\bar\varphi_j\gamma^\mu\Psi_\mu^j
=\epsilon_{kj}\bar\varphi^k\gamma^\mu\Psi_\mu^j
=\epsilon_{kj}\bar\Psi_\mu^j\gamma^\mu\varphi^k
=\bar\Psi_\mu^j\gamma^\mu\varphi_j
```

so the total cross coefficient is $`4a(s+t)`$. In the linear Majorana-transpose representation explicitly used by the source, evaluating $`t=s`$ gives

```math
\boxed{
a\delta_{ij}\bar\psi_\mu^i\gamma^{\mu\nu}\psi_\nu^j
=a\delta_{ij}\bar\Psi_\mu^i\gamma^{\mu\nu}\Psi_\nu^j
+8as\bar\Psi_\mu^i\gamma^\mu\varphi_i
+20as^2\delta_{ij}\bar\varphi^i\varphi^j}
```

This algebraic identity fixes the cross coefficient; the full raw action determines the masses.

<a id="10-scope-available-for-subsequent-calculations"></a>

### Scope of the component comparisons

The verifications above concern the specified monomials, exact algebraic transformations and Jacobi component.

| Object | Usage status in this check |
|---|---|
| The $`N\varphi^2`$ block of $`Y_{Lij}`$ | The corrected form above was verified. This does not automatically verify other blocks. |
| The disputed $`T^2\widehat R(Q)`$ block of $`\varphi_W`$ | $`8/3`$ was verified. |
| LOG H3.9 and $`[S,\nabla_a]\vert _K`$ | The specified signs and phases were verified. |
| Raw LOG bosonic polynomial | Its projection and derivative reduction were verified. |

The displayed coefficient and representation discrepancies are resolved by the specific algebraic checks above. Their scope is the component blocks listed in the table.