# Verified AdS₅ branches and the background selected for the spectrum

<a id="1-selection-and-verification-scope"></a>

## Selection and verification scope

The total action and its domain remain

```math
S=S_{2\partial}+\alpha S_{\log},\qquad
\alpha\ne0,\qquad g\ne0,\qquad L\ne0
\tag{SB1}
```

Couplings and bosonic background fields are real. The selected spectral background is the Branch I root remaining finite in the two-derivative limit:

```math
\boxed{
L_*=\frac{2}{1+\sqrt{1-\alpha g^2/2}},\qquad
N_*=-\frac32gL_*^2,\qquad
\ell_*^{-2}=\frac12g^2L_*^2.
}
\tag{SB2}
```

The reality region of this branch is

```math
\boxed{\alpha g^2\le2,\qquad \alpha\ne0,\qquad g\ne0.}
\tag{SB3}
```

No additional sign restriction is imposed on $`\alpha`$. Selecting this branch does not invalidate other verified branches. The selected real Branch I background does not exist in the region $`\alpha g^2>2`$; Branch II candidates there remain separate with their own admissibility conditions.

**Scope:** the local background equations and preserved background SUSY under the supplied transformation rules were checked. The global prescription is **fixed sources and reflecting boundaries with zero symplectic flux on the universal cover of global AdS₅**. This prescription alone does not specify the asymptotic condition for each field. Global mode and norm statements require those additional boundary data.

The action is fixed by action.md, conventions by [CONVENTIONS.md](../../../common/details/source_conventions.md), field inventory by [indep_fields.md](independent_fields.md), general Euler equations by [eom.md](field_equations.md), and background-branch derivation by [logAdSBranches.md](logAdSBranches.md). This document performs no $`\alpha`$ expansion, auxiliary-field elimination in the general theory, or fluctuation-sector truncation.

<a id="2-background-class-and-back-substitution-into-all-field-equations"></a>

## Background class and back-substitution into all field equations

The superscript $`(0)`$ denotes the background. With $`k:=-\ell_{\mathrm{AdS}}^{-2}<0`$,

```math
\begin{gathered}
R_{\mu\nu\rho\sigma}^{(0)}
=k\bigl(g_{\mu\rho}^{(0)}g_{\nu\sigma}^{(0)}
-g_{\mu\sigma}^{(0)}g_{\nu\rho}^{(0)}\bigr),\\
R_{\mu\nu}^{(0)}=4k\,g_{\mu\nu}^{(0)},\qquad R^{(0)}=20k,\\
L^{(0)}=L_0\ne0,\qquad N^{(0)}=N_0,\qquad
\partial_\mu L_0=\partial_\mu N_0=0,\qquad
L_0^{ij}=\frac{L_0}{\sqrt2}\delta^{ij},\\
G^{(0)}=H_3^{(0)}=P^{(0)}=\mathcal F^{(0)ij}=0,\qquad
V_\mu^{\prime(0)ij}=0,\qquad
\psi_\mu^{(0)i}=\varphi^{(0)i}=0.
\end{gathered}
\tag{SB4}
```

These conditions are applied after variation. With the abbreviation $`L=L_0,\ N=N_0`$, the three independent scalar coefficients that must vanish are:

```math
\begin{aligned}
\mathcal E_N={}&-\frac{4N}{L}-2gL-4g
+\alpha\left(\frac{10gk}{3}-\frac{g^2N}{3}+\frac{2g^3L^2}{3}\right),\\
\mathcal E_L={}&20k+\frac{2N^2}{L^2}-2gN-\frac32g^2L^2+4g^2L\\
&+\alpha\left(-\frac{10g^2Lk}{3}+\frac{4g^3LN}{3}+\frac{5g^4L^3}{6}\right),\\
\mathfrak E={}&-6Lk+\frac{N^2}{L}+gLN+2gN+\frac14g^2L^3-g^2L^2\\
&+\alpha\left(-\frac{k^2}{3}-gNk+\frac{g^2L^2k}{2}
+\frac{g^2N^2}{12}-\frac{g^3NL^2}{3}-\frac{5g^4L^4}{48}\right).
\end{aligned}
\tag{SB5}
```

The metric and vielbein Euler expressions are related by

```math
\mathcal E_{\mu\nu}=\mathfrak E g_{\mu\nu},\qquad
\mathcal E_e{}^\rho{}_a=-2e_{\nu a}\mathcal E^{\rho\nu}
\tag{SB6}
```

No additional independent Euler equation is introduced for metric-dependent connections.

<a id="21-common-residual-identity-for-all-algebraic-candidates"></a>

### Common residual identity for all algebraic candidates

Temporary variables:

```math
q:=\alpha g^2,\qquad t:=qL,\qquad
u:=\frac{N}{gL^2}+\frac32.
\tag{SB7}
```

Branch polynomials:

```math
\begin{aligned}
\mathscr H(t,u)&:=2u^2+(t-12)u+10,\\
A_q(t,u)&:=
2t^2u^2+t(t-4)(t-6)u+3t^2-24t+24q,\\
B(t,u)&:=
4tu^3+(4t^2+32t)u^2\\
&\quad +(t^3+16t^2-356t+480)u-60t^2+360t-480.
\end{aligned}
\tag{SB8}
```

The quantity $`\mathscr H`$ is not the physical three-form $`H_3`$. Each candidate has field values

```math
L=\frac tq,\qquad
N=g\left(\frac tq\right)^2\left(u-\frac32\right),\qquad
k=-\frac{g^2}{20}\left(\frac tq\right)^2\mathscr H(t,u)
\tag{SB9}
```

Direct substitution into SB5, before using the equations, gives the residuals

```math
\boxed{\begin{aligned}
\mathcal E_N&=-\frac{gL}{6t}A_q(t,u),\\
\mathcal E_L&=\frac{g^2L^2}{6t}A_q(t,u),\\
\mathfrak E&=g^2L^3
\left[\frac{u-2}{12t}A_q(t,u)-\frac{u}{1200}B(t,u)\right].
\end{aligned}}
\tag{SB10}
```

Thus $`A_q=0,\ uB=0`$ satisfies the three original equations simultaneously. This identity applies to every candidate without free-parameter sampling.

<a id="22-branch-i"></a>

### Branch I

```math
u=0,\qquad
A_q(t,0)=3(t^2-8t+8q)=0
\quad\Longleftrightarrow\quad
qL^2-8L+8=0.
\tag{SB11}
```

Defining $`\mathscr R:=\alpha g^2L^2-8L+8`$ in the original variables,

```math
\begin{aligned}
&\left.
(\mathcal E_N,\mathcal E_L,\mathfrak E)
\right|_{N=-3gL^2/2,\ k=-g^2L^2/2}\\
&\hspace{2em}=
\mathscr R\left(-\frac g2,\frac{g^2L}{2},-\frac{g^2L^2}{2}\right)
=(0,0,0)
\qquad(\mathscr R=0).
\end{aligned}
\tag{SB12}
```

This check applies to both real roots of Branch I.

<a id="23-generic-and-special-parts-of-branch-ii"></a>

### Generic and special parts of Branch II

```math
\begin{aligned}
\mathscr D_q(t)&:=t(16q+34t^2+112t-192),\\
\mathscr C_q(t)&:=21t^4-102t^3-72t^2+192t
+8q(t^2+26t-24),\\
P_q(t)&:=
42t^8-78t^7+(1959+16q)t^6\\
&\quad+(-32424+3488q)t^5+(80640-9400q)t^4\\
&\quad+(-53760+59776q+1152q^2)t^3\\
&\quad+(-215040q+35136q^2)t^2
+(184320q-47616q^2)t+1536q^3.
\end{aligned}
\tag{SB13}
```

Verification identities:

```math
\begin{aligned}
t^2B(t,u)
&=(2tu+t^2+26t-24)A_q(t,u)
-3\bigl(\mathscr D_q(t)u+\mathscr C_q(t)\bigr),\\
\mathscr D_q(t)^2
A_q\left(t,-\frac{\mathscr C_q(t)}{\mathscr D_q(t)}\right)
&=4t^2P_q(t).
\end{aligned}
\tag{SB14}
```

On the $`\mathscr D_q\ne0`$ part,

```math
P_q(t)=0,\qquad
u=-\frac{\mathscr C_q(t)}{\mathscr D_q(t)},\qquad u\ne0
\quad\Longrightarrow\quad A_q=B=0
\quad\Longrightarrow\quad\text{SB10}=0.
\tag{SB15}
```

On the $`\mathscr D_q=0`$ part, using $`t\ne0`$,

```math
\begin{gathered}
q=12-7t-\frac{17}{8}t^2,\qquad
\mathscr C_q(t)=
4\bigl(t^4-150t^3-256t^2+1008t-576\bigr)=0,\\
\Delta(t):=t^4-20t^3+532t^2+1056t-1728,\\
u_\pm=\frac{-(t-4)(t-6)\pm\sqrt{\Delta(t)}}{4t}
\end{gathered}
\tag{SB16}
```

These two values are roots of $`A_q=0`$. Using $`\mathscr C_q=\mathscr D_q=A_q=0`$ in SB14,

```math
t^2B=0\quad\Longrightarrow\quad B=0
\quad\Longrightarrow\quad\text{SB10}=0.
\tag{SB17}
```

Both roots satisfying reality and AdS conditions are retained. No candidate is discarded because of a vanishing denominator.

<a id="24-vector-form-internal-connection-and-fermion-equations"></a>

### Vector, form, internal-connection, and fermion equations

General form Euler expressions:

```math
\begin{aligned}
\mathcal E_B^{\nu\rho}&=-\nabla_\mu Q^{\mu\nu\rho},\\
\mathcal E_C^\nu
&=J_C^\nu-\nabla_\mu\Pi^{\mu\nu}
+\frac12Q^{\nu\mu\rho}G_{\mu\rho}
-\frac12C_\mu\mathcal E_B^{\mu\nu},\\
\mathcal E_E^{\rho\sigma\lambda}
&=\frac g2Q^{\rho\sigma\lambda}
+\frac12\varepsilon^{\mu\nu\rho\sigma\lambda}\nabla_\nu W_\mu.
\end{aligned}
\tag{SB18}
```

Here $`\Pi,Q,W,J_C`$ are the form-variation responses of the general action. On SB4,

```math
\Pi=Q=M=J_C=0,\qquad
W=-2\sqrt2V-4gC,\qquad
dW=-2\sqrt2\,dV-4g\,dC=0.
\tag{SB19}
```

The quantity $`M`$ is the variation response of the internal-connection curvature. The common response for trace and traceless connection Euler expressions is

```math
\mathcal V^\nu_{ij}
=-\nabla_\mu^{(V)}M^{\mu\nu}_{ij}
+(4L-\alpha g^2L^2)V'{}^\nu_{ij}
-2\sqrt2P^\nu\delta_{ij}
=0
\tag{SB20}
```

where $`\nabla^{(V)}`$ denotes the bosonic Levi–Civita and internal-connection derivative. Thus

```math
\boxed{
\mathcal E_C=\mathcal E_{B_2}=\mathcal E_{E_3}
=\mathcal E_V=\mathcal E_{V'}=0.
}
\tag{SB21}
```

Denoting the fermions that vanish on the background by $`\Phi_F=(\psi_\mu^i,\varphi^i)`$,

```math
S=S_0+S_2+O(\Phi_F^4),\qquad
\frac{\delta S_2}{\delta\Phi_F}=O(\Phi_F),\qquad
\frac{\delta O(\Phi_F^4)}{\delta\Phi_F}=O(\Phi_F^3).
\tag{SB22}
```

Thus, after variation,

```math
\boxed{
\left.\mathcal E_{\psi_\mu^i}\right|_{\Phi_F=0}
=\left.\mathcal E_{\varphi^i}\right|_{\Phi_F=0}=0.
}
\tag{SB23}
```

This fermion-degree check includes implicit fermions in supercovariant objects and dependent connections. Fermionic fluctuations are not set to zero.

<a id="3-reality-regularity-and-special-parameter-points"></a>

## Reality, regularity, and special parameter points

The admissibility conditions on all branches are

```math
\boxed{
q\in\mathbb R\setminus\{0\},\qquad
t,u\in\mathbb R,\qquad t\ne0,\qquad
\mathscr H(t,u)>0.
}
\tag{SB24}
```

The special denominator branch additionally requires $`\Delta(t)\ge0`$. The general Branch II polynomial satisfies

```math
P_q(0)=1536q^3\ne0
\tag{SB25}
```

which excludes $`t=0`$. The quartic polynomial of the special branch also has a nonzero constant term.

For finite allowed couplings and admissible finite roots, $`L=t/q\ne0`$, $`N`$, and $`k`$ are finite. The geometric check is:

```math
R=20k,\qquad
R_{\mu\nu}R^{\mu\nu}=80k^2,\qquad
R_{\mu\nu\rho\sigma}R^{\mu\nu\rho\sigma}=40k^2.
\tag{SB26}
```

Neither a multiple root nor $`\mathscr D_q=0`$ alone is a geometric singularity. Negative roots of $`L`$ are not excluded from the initial field domain $`L\ne0`$ solely because of their sign.

<a id="31-regularity-of-the-selected-root"></a>

### Regularity of the selected root

Defining $`s:=\sqrt{1-\alpha g^2/2}\ge0`$,

```math
L_*=\frac2{1+s}>0,\qquad
N_*=-\frac{6g}{(1+s)^2},\qquad
\ell_*^{-2}=\frac{2g^2}{(1+s)^2}.
\tag{SB27}
```

Since $`1+s>0`$, this denominator never vanishes at finite allowed parameter values. The selected root follows from the original two Branch I roots as

```math
\begin{aligned}
L_{0,-}
&=\frac4{\alpha g^2}\left(1-\sqrt{1-\alpha g^2/2}\right)\\
&=\frac4{\alpha g^2}
\frac{1-(1-\alpha g^2/2)}{1+\sqrt{1-\alpha g^2/2}}
=\frac2{1+\sqrt{1-\alpha g^2/2}}
=L_*
\end{aligned}
\tag{SB28}
```

The selection criterion is

```math
\lim_{\alpha\to0}L_*=1
\tag{SB29}
```

This limit labels a branch after solving the total equations; the two-derivative solution was not used as initial input, and no $`\alpha`$ expansion was made. The condition $`L_*>0`$ on the selected branch follows from the solution; it is not a sign assumption imposed on all candidates beforehand.

<a id="32-algebraic-jacobian"></a>

### Algebraic Jacobian

Let the temporary variables be $`Y:=N/g,\ Z:=k/g^2`$ and the equation vector be

```math
\mathbf F:=
\left(\mathcal E_N/g,\ \mathcal E_L/g^2,\ \mathfrak E/g^2\right)
\tag{SB30}
```

Hold $`q=\alpha g^2`$ fixed when computing the Jacobian; rewrite using $`t=qL`$ only after differentiation. On Branch I:

```math
\left.\frac{\partial\mathbf F}{\partial(L,Y,Z)}\right|_{\mathrm I}
=
\begin{pmatrix}
\frac{4t}{3}-8&-\frac{12+t}{3L}&\frac{10t}{3L}\\
4-12L+\frac{13tL}{6}&\frac{4t}{3}-8&20-\frac{10t}{3}\\
-2L+\frac{tL^2}{12}&2-2L-\frac{tL}{12}&L(-6+\frac{7t}{3})
\end{pmatrix}.
\tag{SB31}
```

The branch equation $`qL^2-8L+8=0`$, with $`t=qL`$, gives

```math
(t-8)L+8=0\quad\Longrightarrow\quad L=\frac8{8-t}
\tag{SB32}
```

For finite $`L`$, $`t=8`$ is impossible. Substituting this relation into SB31,

```math
\boxed{
\det\frac{\partial\mathbf F}{\partial(L,Y,Z)}
=-\frac{8(t-4)^2(t-2)}{t-8}.
}
\tag{SB33}
```

Using $`t=4(1-s)`$ and $`q=t(8-t)/8`$ on the selected root gives the special points:

| $`\alpha g^2`$ | Property on the selected branch |
|---|---|
| $`3/2`$ | $`t=2`$: merger with Branch II; singular background Jacobian |
| $`2`$ | $`t=4`$: the two Branch I roots merge; singular background Jacobian |
| $`-30`$ | $`t=-12`$: the $`4/L+\alpha g^2/3`$ coefficient in the $`N`$ equation vanishes |

The condition in the final row follows directly from

```math
\frac4L+\frac{\alpha g^2}{3}
=\frac{12+t}{3L}=0
\quad\Longrightarrow\quad
t=-12,\qquad q=\frac{t(8-t)}8=-30
\tag{SB34}
```

These values are not free-parameter samples.

Background fields are finite at all three points. A singular Jacobian alone proves neither a physical zero mode, kinetic degeneracy, nor stability. These require the full fluctuation operator and boundary conditions. The tabulated points are not removed from the solution region.

<a id="4-preserved-background-susy"></a>

## Preserved background SUSY

Zero-fermion transformation inputs are [W01](component_construction/results/gauged_full_fermionic_log/sources/reference_fragments/01_shared_component_relations.md), the two-derivative source's [compensation rules (4.12)–(4.14)](05_gauged_two_derivative_full_fermionic_action_from_1608_map.md), and the linear-multiplet rule in the root [CONVENTIONS.md, §8](../../../common/details/source_conventions.md). The following check applies these rules on the background in common conventions.

<a id="41-linear-multiplet-fermion"></a>

### Linear-multiplet fermion

On the zero-flux, constant-scalar background, the gauge-preserving $`S`$ parameter and fermion transformation are:

```math
\eta^i=-\frac g2L_0^{ij}\epsilon_j,\qquad
\delta\varphi^i=\frac12N_0\epsilon^i+3L_0^{ij}\eta_j.
\tag{SB35}
```

The NW–SE lowering rule is:

```math
\eta_j=-\frac g2L_0^{k\ell}\epsilon_\ell\epsilon_{kj},
\qquad
\epsilon_\ell=\epsilon^m\epsilon_{m\ell}.
\tag{SB36}
```

For $`L_0^{ij}=L_0\delta^{ij}/\sqrt2`$, there is an exceptional family satisfying

```math
L_0^{ij}L_0^{k\ell}\epsilon_{m\ell}\epsilon_{kj}
=\frac{L_0^2}{2}\delta^{ij}\delta^{k\ell}
\epsilon_{m\ell}\epsilon_{kj}
=-\frac{L_0^2}{2}\delta^i{}_m.
\tag{SB37}
```

Therefore,

```math
\begin{aligned}
3L_0^{ij}\eta_j
&=-\frac{3g}{2}
L_0^{ij}L_0^{k\ell}\epsilon_{m\ell}\epsilon_{kj}\epsilon^m
=\frac{3gL_0^2}{4}\epsilon^i,\\
\boxed{\delta\varphi^i}
&\boxed{=
\left(\frac{N_0}{2}+\frac{3gL_0^2}{4}\right)\epsilon^i
=\frac{gL_0^2u}{2}\epsilon^i.}
\end{aligned}
\tag{SB38}
```

On Branch II, $`gL_0^2u\ne0`$, so $`\delta\varphi^i=0`$ is possible only with $`\epsilon^i=0`$. This branch preserves no SUSY; there is no spinor matrix generating a half-SUSY projection because the coefficient is proportional to the identity on spinor space.

On Branch I, $`u=0`$, so this transformation vanishes for every $`\epsilon^i`$.

<a id="42-gravitino-and-integrability"></a>

### Gravitino and integrability

Define the internal matrix by

```math
\mathsf J^i{}_j:=\delta^{ik}\epsilon_{jk},
\qquad
\mathsf J^2=-\mathbf1
\tag{SB39}
```

On $`T=0`$ and $`b_\mu=0`$, the gravitino transformation is

```math
\begin{aligned}
0=\delta\psi_\mu^i
&=\nabla_\mu\epsilon^i
-\frac12V_\mu\delta^{ij}\epsilon_j-i\gamma_\mu\eta^i,\\
0=\mathscr D_\mu\epsilon,\qquad
\mathscr D_\mu
&:=\nabla_\mu-\frac12V_\mu\mathsf J
+\frac{igL_0}{2\sqrt2}\gamma_\mu\mathsf J.
\end{aligned}
\tag{SB40}
```

Using $`dV=0`$, $`\partial_\mu L_0=0`$, $`\nabla_\mu\gamma_\nu=0`$, and $`\mathsf J^2=-\mathbf1`$,

```math
\begin{aligned}
[\mathscr D_\mu,\mathscr D_\nu]\epsilon
&=\left[
\frac14R_{\mu\nu}{}^{ab}\gamma_{ab}
+\left(\frac{igL_0}{2\sqrt2}\right)^2
\mathsf J^2[\gamma_\mu,\gamma_\nu]
\right]\epsilon\\
&=\left[
\frac k2+\left(-\frac{g^2L_0^2}{8}\right)(-1)\,2
\right]\gamma_{\mu\nu}\epsilon\\
&=\left(\frac k2+\frac{g^2L_0^2}{4}\right)
\gamma_{\mu\nu}\epsilon.
\end{aligned}
\tag{SB41}
```

On Branch I, $`k=-g^2L_0^2/2`$, so the $`\mathscr D`$ curvature vanishes. No algebraic projection remains on the eight real initial components of the symplectic–Majorana doublet:

```math
\boxed{\text{Branch I locally preserves eight real supersymmetries.}}
\tag{SB42}
```

SUSY transformations of bosonic fields contain at least one dynamical fermion and vanish on the background. The gauge-preserving traceless internal transformation and $`K`$ compensation also vanish on the zero-fermion background. Dependent-composite transformations follow from those of independent fields; no new Killing spinor equations are added for them.

On the selected universal cover, the flat internal connection has no holonomy obstruction, so these eight solutions extend to global background Killing spinors. This count does not establish SUSY closure of the full fluctuation boundary conditions or a new complete nonlinear SUSY verification of the combined action.

<a id="5-preserved-gauge-symmetries"></a>

## Preserved gauge symmetries

Local gauge redundancies of the theory are distinguished from the stabilizer of a particular background potential representative.

The general form transformations are

```math
\delta C=d\Lambda,\qquad
\delta B_2=d\Lambda_1-\frac12\Lambda G-\frac g2\Lambda_2,\qquad
\delta E_3=d\Lambda_2
\tag{SB43}
```

and, on the background with $`G=0`$ and $`\delta V=d\beta`$ for the residual internal connection,

```math
\delta C=d\Lambda,\qquad
\delta V=d\beta,\qquad
\delta B_2=d\Lambda_1-\frac g2\Lambda_2,\qquad
\delta E_3=d\Lambda_2.
\tag{SB44}
```

These transformations preserve the vanishing gauge-covariant field strengths. Parameters also leaving a fixed potential representative unchanged satisfy

```math
d\Lambda=d\beta=0,\qquad
d\Lambda_2=0,\qquad
d\Lambda_1=\frac g2\Lambda_2
\tag{SB45}
```

these conditions.

The residual internal symmetry of the orientation $`L_0^{ij}\ne0`$ is $`U(1)`$:

```math
\lambda^{ij}=\frac{\beta}{2}\delta^{ij}
\quad\Longrightarrow\quad
\delta_U L_0^{ij}
=-2\lambda^{(i}{}_kL_0^{j)k}=0.
\tag{SB46}
```

Here $`\lambda^{ij}`$ is an internal gauge parameter, unrelated to the action coupling $`\alpha`$.

Local Lorentz and diffeomorphism redundancies remain. The geometric stabilizer consists of

```math
\nabla_{(\mu}\xi_{\nu)}=0
\tag{SB47}
```

the fifteen AdS Killing vectors solving this equation. The Abelian gauge symmetry of $`C`$ and the form gauge hierarchy remain. This symmetry count does not determine which physical vector mixtures are massless.

<a id="6-global-ads₅-and-the-specified-boundary-prescription"></a>

## Global AdS₅ and the specified boundary prescription

Boundary prescription: **global AdS₅ with fixed sources and reflecting boundaries.**

<a id="61-global-geometry"></a>

### Global geometry

The metric on the universal cover of global AdS₅ is:

```math
\boxed{
ds^2=\frac1{\cos^2\rho}
\left[-dt^2+\ell_*^2
\left(d\rho^2+\sin^2\rho\,d\Omega_3^2\right)\right],
\quad
t\in\mathbb R,\quad 0\le\rho<\frac\pi2.
}
\tag{SB48}
```

Here $`t`$ is the global time coordinate, distinct from the temporary algebraic $`t=qL`$ of earlier sections. The radius $`\ell_*`$ retains its exact $`\alpha,g`$ dependence in SB2 and is not numerically fixed.

With $`a=1,\ldots,4`$ and $`n^an^a=1`$ in the embedding space, the metric is

```math
X^{-1}=\ell_*\sec\rho\cos(t/\ell_*),\qquad
X^0=\ell_*\sec\rho\sin(t/\ell_*),\qquad
X^a=\ell_*\tan\rho\,n^a
\tag{SB49}
```

follows from the parametrization:

```math
\begin{aligned}
-(X^{-1})^2-(X^0)^2+X^aX^a
&=-\ell_*^2\sec^2\rho+\ell_*^2\tan^2\rho
=-\ell_*^2,\\
-(dX^{-1})^2-(dX^0)^2+dX^adX^a
&=-\sec^2\rho\,dt^2
+\ell_*^2\sec^2\rho\,d\rho^2
+\ell_*^2\tan^2\rho\,d\Omega_3^2.
\end{aligned}
\tag{SB50}
```

The time coordinate is unwrapped on the universal cover; no periodic time identification is imposed. With $`z:=\cos\rho`$, the conformal boundary representative is

```math
\gamma^{(0)}
=\left.\lim_{z\to0}z^2g\right|_{\text{tangent to the boundary}}
=-dt^2+\ell_*^2d\Omega_3^2.
\tag{SB51}
```

This global completion includes no additional quotient or flat-connection holonomy. The spin structure is the smooth spin structure of the universal cover.

<a id="62-center-and-boundary-conditions"></a>

### Center and boundary conditions

1. **Regularity at the center:** at $`\rho=0`$, all bosonic tensors and fermions must be smooth in a smooth local frame. The spherical-coordinate singularity is not physical.
2. **Fixed sources:** fix the boundary metric and source components of every independent radial canonical pair. Fermionic sources vanish; fermionic responses and bulk fluctuations remain.
3. **Reflecting boundary:** the finite symplectic structure of the total theory must have zero flux through the boundary.

Denote independent sources by $`J^A`$ and conjugate responses by $`\Pi_A`$. The definition of $`\Pi_A`$ includes the common action factor $`(2\kappa_5^2)^{-1}`$. The required variational form and source condition are:

```math
\left.\delta S_{\mathrm{ren}}\right|_{\mathrm{EOM}=0}
=\int_{\partial M}\Pi_A\,\delta J^A,
\qquad
\boxed{\delta J^A=0.}
\tag{SB52}
```

For fermions, only source data in the appropriate canonical polarization are fixed; Dirichlet conditions are not imposed simultaneously on all spinor components. Additional radial canonical pairs introduced by higher derivatives cannot be omitted by retaining only the two-derivative sources. The field-specific canonical pairs $`J^A,\Pi_A`$ depend on the corresponding quadratic operators and boundary action.

Let $`\Phi`$ denote all independent fields, $`\delta_1,\delta_2`$ two even test variations, and $`\Theta_{\mathrm{ren}}`$ the total renormalized boundary-variation form. The symplectic current is:

```math
\omega_{\mathrm{ren}}
=\delta_1\Theta_{\mathrm{ren}}(\delta_2\Phi)
-\delta_2\Theta_{\mathrm{ren}}(\delta_1\Phi).
\tag{SB53}
```

On the background and linear equations,

```math
\begin{aligned}
d\omega_{\mathrm{ren}}&=0,\\
\Omega_{\Sigma_2}-\Omega_{\Sigma_1}
&=-\int_{\mathscr I_{12}}\omega_{\mathrm{ren}},\\
\left.\omega_{\mathrm{ren}}\right|_{\mathscr I}
&=\delta_1\Pi_A\,\delta_2J^A
-\delta_2\Pi_A\,\delta_1J^A=0
\qquad(\delta_1J^A=\delta_2J^A=0).
\end{aligned}
\tag{SB54}
```

Here $`\Omega_\Sigma:=\int_\Sigma\omega_{\mathrm{ren}}`$ is the symplectic pairing of the two variations, and $`\mathscr I_{12}`$ is the conformal boundary between two time slices. The quantity $`\Omega_\Sigma`$ must be finite. Positivity is not assumed.

SB52–SB54 are the variational conditions of the specified boundary prescription. They do not claim a completed explicit derivation of all boundary counterterms, canonical sources, or finite symplectic-current coefficients of this theory.

AdS boundary conditions do not follow from bulk equations alone; admissible conditions depend on the field operator. This distinction is studied by [Ishibashi–Wald, *Dynamics in Non-Globally-Hyperbolic Static Spacetimes III: Anti-de Sitter Spacetime*](https://arxiv.org/abs/hep-th/0402184). The role of boundary counterterms in the symplectic structure is shown by [Compère–Marolf, *Setting the boundary free in AdS/CFT*](https://arxiv.org/abs/0805.1902). The field-specific boundary coefficients depend on the LOG quadratic operators and the chosen boundary action.

<a id="7-completed-and-outstanding-scope"></a>

## Scope of the selected-background analysis

| Topic | Status |
|---|---|
| Back-substitution of all candidate branches into independent bosonic background equations | Verified symbolically by SB10–SB21 |
| Fermion Euler equations on the zero-fermion background | Satisfied by SB22–SB23 |
| Reality, field domain $`L\ne0`$, and geometric regularity | SB24–SB29; special branches retained |
| Known special algebraic parameter points | SB33–SB34; not discarded by division |
| Preserved background SUSY | Branch I: eight real supersymmetries; Branch II: none preserved |
| Gauge symmetries and background stabilizer | Distinguished by SB43–SB47 |
| Spectral branch | The root in SB2 with exact $`\alpha,g`$ dependence is selected |
| Global geometry and boundary choice | Universal cover of global AdS₅; fixed sources and zero symplectic flux |

[The general field-equation derivation](field_equations.md#verification-record) gives the bosonic-body equations and diagonal spinor operator. The AdS5 bilinear maps and checks are in [the quadratic action](../../ads5/quadratic_action.md), (Q31)–(Q40), (Q57). The boundary pairs in SB52 depend on the field operators and boundary action. Two-fermion action order is sufficient for the classical linear spectrum about a fermion-free background.

At repeated indicial roots, logarithmic modes cannot be discarded automatically. All bosonic and fermionic fluctuations remain; zero-flux background conditions are not imposed on fluctuations.

**Result:** the spectral background is the Branch I root in SB2. Its eight supersymmetries are verified. The fixed-source boundary prescription specifies the intended global domain; the local bulk spectrum does not establish all field-specific boundary data or a complete global boundary problem.
