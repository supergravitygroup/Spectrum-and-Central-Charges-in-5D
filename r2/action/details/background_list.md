# AdS₅ and product backgrounds with constant flux

<a id="1-action-scope-and-independent-fields"></a>

## Action, scope, and independent fields

The action agrees with action.md, and conventions with [CONVENTIONS.md](../../../common/details/source_conventions.md). Below, write

```math
\alpha:=\lambda_{R^2},\qquad g\ne0
```

The source coefficients $`-2,-4g`$ of the two-derivative density and coefficient $`\alpha`$ of the $`R^2`$ density are unchanged. The first source's field-strength representative (5.10) is retained.

The class consists of **local direct-product geometries** with constant scalars and covariantly constant fluxes in the current gauge. The internal connection is restricted to the $`\mathcal D_\mu L_{ij}=0`$, $`V_\mu^{\prime\,ij}=0`$ branch; the curvature of the remaining Abelian $`V_\mu`$ connection remains free. Internal-connection branches with $`\mathcal D L\ne0`$, warp factors, and position-dependent scalar profiles are outside this class.

The independent fields are retained as

```math
e_\mu{}^a,\ C_\mu,\ B_{\mu\nu},\ L,\ N,\ E_{\mu\nu\rho},\
V_\mu,\ V_\mu^{\prime\,ij},\ \psi_\mu{}^i,\ \varphi^i
```

These fields are retained. The quantities $`E_a,T_{ab},D,\chi^i,\omega,\phi,f`$ are not independent variation variables. The calculation below gives **background values of all independent field equations** within this class; it does not claim a derivation of the general fermionic field equations or the full spectrum.

<a id="2-substitution-of-bosonic-composites"></a>

## Substitution of bosonic composites

The fermionic background vanishes. First retaining bosonic dependencies, write

```math
\begin{gathered}
G=dC,\qquad H=dB+\frac12C\wedge G+\frac g2E_3,
\qquad dH=\frac12G\wedge G+\frac g2dE_3,\\
E^a=-\frac1{48}\varepsilon^{abcde}(dE_3)_{bcde},\qquad
Q_{ab}:=\frac16\varepsilon_{abcde}H^{cde},\qquad
T_{ab}=\frac18(G_{ab}+Q_{ab})
\end{gathered}
\tag{1}
```

The symbol $`Q`$ abbreviates only the algebraic dual of $`H`$. The Lorentz-signature sign is explicitly fixed by

```math
\begin{aligned}
Q_{ab}Q^{ab}
&=\frac1{36}\varepsilon_{abcde}\varepsilon^{abfgh}
 H^{cde}H_{fgh}
=-\frac{2!3!}{36}H^{cde}H_{cde}
=-\frac13H^2,\\
H^{abc}&=-\frac12\varepsilon^{abcde}Q_{de}
\end{aligned}
\tag{2}
```

No numerical epsilon orientation is selected.

At zero fermions, the dependent connections and $`D`$ are:

```math
\begin{aligned}
\omega&=\omega(e),&\quad \phi_\mu{}^i&=\chi^i=0,\\
f_\mu{}^a&=-\frac16R_\mu{}^a+\frac1{48}e_\mu{}^aR,
& f_a{}^a&=-\frac R{16},\\
D&=-\frac R{32}-\frac1{16}G^2-\frac{26}{3}T^2
 +2G\cdot T+\frac g4N+\frac{g^2}{16}L^2.
\end{aligned}
\tag{3}
```

On $`V'=0`$, the relations are $`L_{ij}=n_{ij}L`$, $`n_{ij}:=\delta_{ij}/\sqrt2`$, $`n^{ij}n_{ij}=1`$, and $`\mathcal D n_{ij}=0`$. Before taking $`L`$ constant, for $`\Box:=\nabla_\mu\nabla^\mu`$,

```math
\begin{aligned}
\Box_cL_{ij}&=n_{ij}(\Box L+6f_a{}^aL),\\
-L^{-3}L^{km}\mathcal D_aL_{k(i}\mathcal D^aL_{j)m}
&=-\frac{n_{ij}}{2L^2}(\partial L)^2,\\
2L^{-3}E_aL_{k(i}\mathcal D^aL_{j)}{}^k&=0.
\end{aligned}
\tag{4}
```

The second equality uses $`L^{km}\mathcal D L_{ki}\mathcal D L_{jm} =L n_{ij}(\partial L)^2/2`$; in the third, the symmetrized internal matrix vanishes by antisymmetry. Thus the bosonic components of the composite vector are

```math
\begin{gathered}
r:=\rho'=\frac{2N}{L},\qquad
a_\mu:=A'_\mu=\frac2L E_\mu+\sqrt2V_\mu,\qquad
F:=F'=da,\qquad Y'_{ij}=n_{ij}y,\\
y=\frac{\Box L}{L}-\frac{(\partial L)^2}{2L^2}
 +6f_a{}^a+4D+\frac83T^2-\frac{N^2+E^2}{L^2}
\end{gathered}
\tag{5}
```

The curvature and flux coefficient check is:

```math
\begin{aligned}
6f_a{}^a+4D+\frac83T^2
&=8f_a{}^a-\frac14G^2-32T^2+8G\cdot T
 +gN+\frac{g^2L^2}{4}\\
&=-\frac R2-\frac14G^2-\frac12(G+Q)^2
 +G\cdot(G+Q)+gN+\frac{g^2L^2}{4}\\
&=-\frac R2+\frac14G^2-\frac12Q^2+gN+\frac{g^2L^2}{4}\\
&=-\frac R2+\frac14G^2+\frac16H^2+gN+\frac{g^2L^2}{4}.
\end{aligned}
\tag{6}
```

For the subsequent algebra, define

```math
z:=y-gN
=-\frac R2+\frac{\Box L}{L}-\frac{(\partial L)^2}{2L^2}
 -\frac{N^2+E^2}{L^2}+\frac14G^2+\frac16H^2+\frac{g^2L^2}{4}
\tag{7}
```

The quantities $`r,a,F,y,z`$ are not new independent fields.

<a id="21-bosonic-density-used-for-variation"></a>

### Bosonic density used for variation

The bosonic source expression of the first sector is

```math
I_2^{F}=-2\left(Ly+rN+\frac12F_{\mu\nu}E^{\mu\nu}\right)
 -4g\left(\frac12G_{\mu\nu}E^{\mu\nu}+N-\frac g2L^2\right).
\tag{8}
```

Using $`E^{\mu\nu}=-\varepsilon^{\mu\nu\rho\sigma\lambda}E_{\rho\sigma\lambda}/12`$
and $`E^\mu=e^{-1}\partial_\nu(eE^{\mu\nu})`$,

```math
\begin{aligned}
a_\mu E^\mu
&=\frac12F_{\mu\nu}E^{\mu\nu}
 -\frac1{12}\nabla_\nu
  \bigl[\varepsilon^{\mu\nu\rho\sigma\lambda}a_\mu E_{\rho\sigma\lambda}\bigr],\\
I_2^{F}&=I_2+\nabla_\nu J_2^\nu,\\
J_2^\nu&=-2\nabla^\nu L
 -\frac16\varepsilon^{\mu\nu\rho\sigma\lambda}
  (a_\mu+2gC_\mu)E_{\rho\sigma\lambda},\\
I_2&=LR+\frac{(\partial L)^2}{L}-\frac L2G^2-\frac L3H^2
 -\frac2L(N^2+E^2)-2\sqrt2V_\mu E^\mu-4gC_\mu E^\mu\\
&\hspace{1em}-2gLN-4gN-\frac{g^2}{2}L^3+2g^2L^2.
\end{aligned}
\tag{9}
```

For example, adding $`+2E^2/L`$ from $`-2Ly`$ and $`-4E^2/L`$ from $`-2a\cdot E`$ gives the coefficient $`-2E^2/L`$ of $`E^2`$. This boundary term is not removed from the action; $`I_2`$ is usable only for compactly supported bulk variations.

After substituting composites, the zero-fermion terms of the second source (R2) fall into the following groups:

```math
\begin{aligned}
I_4^{\rm source}={}&y^2-grLy
 -\frac12a_a\nabla_b\bigl[F^{ab}+r(G^{ab}-16T^{ab})\bigr]
 -\frac18\varepsilon^{abcde}a_aF_{bc}G_{de}\\
&+\frac12r\Box_c r+r^2f_a{}^a
 -\frac14rF\cdot(G-16T)
 +4r^2G\cdot T-4r^2D-\frac{104}{3}r^2T^2.
\end{aligned}
\tag{10}
```

The $`Y'^2`$ part of this grouping can be checked by direct expansion. Within this check, let $`b:=\Box L+6f_a{}^aL`$ and $`U:=4D+8T^2/3-(E^2+N^2)/L^2+(\partial L)^2/(2L^2)`$:

```math
\begin{aligned}
&\frac{b^2}{L^2}-\frac{2b(\partial L)^2}{L^3}
 +\frac{2Ub}{L}+\frac{[(\partial L)^2]^2}{L^4}
 -\frac{2U(\partial L)^2}{L^2}+U^2\\
&\hspace{2em}=\left[\frac bL-\frac{(\partial L)^2}{L^2}+U\right]^2=y^2.
\end{aligned}
\tag{11}
```

The remaining bosonic groups are the $`-grLy`$, $`a\nabla[\cdots]`$, $`\varepsilon aFG`$, $`r\Box_c r/2`$, $`r^2f`$, $`-rF(G-16T)/4`$, $`4r^2GT`$, $`-4r^2D`$, and $`-104r^2T^2/3`$ terms, respectively. This regroups the expanded action of the second source; it does not replace it with a different $`R^2`$ action.

With the definition $`M^{ab}:=F^{ab}+r(G^{ab}-16T^{ab})`$, the required operations are

```math
\begin{aligned}
-\frac12a_a\nabla_bM^{ab}
&=-\frac14F_{ab}M^{ab}-\frac12\nabla_b(a_aM^{ab}),\\
\frac12r\Box_c r+r^2f_a{}^a
&=-\frac12(\partial r)^2+2r^2f_a{}^a
 +\frac12\nabla_a(r\nabla^ar),\\
2f_a{}^a+4G\cdot T-4D-\frac{104}{3}T^2
&=\frac14G^2-4G\cdot T-gN-\frac{g^2L^2}{4},\\
y^2-grLy&=(y-gN)^2-g^2N^2,\\
-\frac14F^2-\frac r2F\cdot(G-16T)
 +r^2\left(\frac14G^2-4G\cdot T\right)
&=-\frac14(F-rG)^2+r\left(F-\frac r2G\right)\cdot Q
\end{aligned}
\tag{12}
```

The result is:

```math
\begin{aligned}
I_4^{\rm source}&=I_4+\nabla_bJ_4^b,
&J_4^b&=-\frac12a_aM^{ab}+\frac12r\nabla^br,\\
I_4&=z^2-2g^2N^2-\frac{4gN^3}{L^2}
 -\frac12(\partial r)^2-\frac14(F-rG)^2\\
&\quad+r\left(F-\frac r2G\right)\cdot Q
 -\frac18\varepsilon^{abcde}a_aF_{bc}G_{de}.
\end{aligned}
\tag{13}
```

Thus, on this bosonic branch and with the specified boundary representative,

```math
S_{\rm bos}=
\int_M d^5x\,e(I_2+\alpha I_4)
+\int_{\partial M}d\Sigma_b\,e(J_2^b+\alpha J_4^b).
\tag{14}
```

<a id="3-product-ansatz-and-all-background-equations"></a>

## Product ansatz and all background equations

Let the factors have dimensions $`2,3`$ and sectional curvatures $`k_2,k_3`$:

```math
\begin{gathered}
R_{ijkl}^{(2)}=k_2(g_{ik}g_{jl}-g_{il}g_{jk}),\qquad
R_{mnpq}^{(3)}=k_3(g_{mp}g_{nq}-g_{mq}g_{np}),\\
R_{ij}=k_2g_{ij},\qquad R_{mn}=2k_3g_{mn},\qquad
R=2k_2+6k_3.
\end{gathered}
\tag{15}
```

Only in these geometric formulas, $`i,j`$ is a two-dimensional coordinate index; it is not contracted with internal $`SU(2)`$ indices.

Let $`\Omega_2`$ be the volume form of the two-dimensional factor. The signature and dual three-form are defined by

```math
\begin{gathered}
s:=\tfrac12(\Omega_2)_{ab}(\Omega_2)^{ab}
=\begin{cases}
+1,&\Sigma_3\text{ Lorentzian},\ \Sigma_2\text{ Riemannian},\\
-1,&\Sigma_2\text{ Lorentzian},\ \Sigma_3\text{ Riemannian},
\end{cases}\\
(\Omega_3)^{abc}:=-\frac12\varepsilon^{abcde}(\Omega_2)_{de},
\qquad \Omega_3^2=-6s
\end{gathered}
\tag{16}
```

Since full isotropy permits no invariant one-form or four-form, take $`E_a=0`$ and $`dE_3=0`$; the potential $`E_3`$ need not itself vanish. The background profiles are

```math
\begin{gathered}
L=L_0>0,\quad N=N_0,\quad
\psi_\mu{}^i=\varphi^i=0,\quad V_\mu^{\prime\,ij}=0,\\
G=q\Omega_2,\qquad H=p\Omega_3,\qquad
Q=p\Omega_2,\qquad F'=\sqrt2dV=u\Omega_2,\qquad
\nabla\Omega_2=\nabla\Omega_3=0
\end{gathered}
\tag{17}
```

Here $`q,p,u`$ are real constants. The algebra writes $`L,N`$ for $`L_0,N_0`$. In particular,

```math
\begin{gathered}
G^2=2sq^2,\qquad H^2=-6sp^2,\qquad
G\cdot Q=2sqp,\qquad F'\cdot Q=2sup,\\
G\wedge G=F'\wedge G=F'\wedge F'=0,\qquad dH=0
\end{gathered}
\tag{18}
```

The geometries $`\Sigma_3\times\Sigma_2`$ and $`\Sigma_2\times\Sigma_3`$ agree only by reordering the factors; the physical distinction is which factor is Lorentzian and which factors carry the fluxes. The flux $`G`$ fills the two-dimensional factor, and $`H`$ the three-dimensional one.

Define the three algebraic background abbreviations by

```math
\begin{aligned}
z&=-\frac R2-\frac{N^2}{L^2}
 +s\left(\frac{q^2}{2}-p^2\right)+\frac{g^2L^2}{4},\\
w&:=u-\frac{2N}{L}q,\qquad \mathcal A:=L-\alpha z,\\
\mathscr F&:=LR+sL(2p^2-q^2)-\frac{2N^2}{L}-2gLN-4gN
 -\frac{g^2L^3}{2}+2g^2L^2\\
&\quad+\alpha\left[z^2-2g^2N^2-\frac{4gN^3}{L^2}
 -\frac s2w^2\right]
\end{aligned}
\tag{19}
```

Here $`\mathscr F`$ is the algebraic density contributing to metric variation. Metric-independent epsilon terms are excluded from $`\mathscr F`$.

<a id="31-variations-of-n-and-l"></a>

### Variations of $`N`$ and $`L`$

Variation is taken first in (9), (13). First variations of derivative terms vanish on the constant background. For example,

```math
\begin{aligned}
\delta\!\int e\,\alpha z^2\big|_{\delta(\Box L)}
&=\int e\,\frac{2\alpha z}{L}\Box\delta L
=\int e\,\delta L\Box\left(\frac{2\alpha z}{L}\right)=0,\\
\delta\!\int e\,\frac{(\partial L)^2}{L}&=0,
\qquad \delta\!\int e\,(\partial r)^2=0
\end{aligned}
\tag{20}
```

because $`z,L,r`$ is constant on the background. This does not delete $`\Box L`$ from the action before variation.

The epsilon-containing $`r(F-rG/2)\cdot Q`$ term is retained in the scalar variation:

```math
\mathscr L_{\rm alg}
=\mathscr F+\alpha s(2rup-r^2qp),\qquad r=\frac{2N}{L}.
\tag{21}
```

First check with the invertible variables $`(L,N)\leftrightarrow(L,r)`$:

```math
\begin{aligned}
\mathcal E_r={}&-L(r+gL+2g)
 +\alpha\left[-rz-g^2L^2r-\frac32gLr^2+s(q+2p)w\right],\\
\mathcal E_{L|r}={}&R+s(2p^2-q^2)-\frac{r^2}{2}
 -2gr(L+1)-\frac32g^2L^2+4g^2L\\
&+\alpha\left[g^2Lz-g^2Lr^2-\frac g2r^3\right].
\end{aligned}
\tag{22}
```

These results use $`\partial_rz=-r/2`$, $`\partial_Lz|_r=g^2L/2`$, $`\partial_rw=-q`$, and $`\partial_r[s(2rup-r^2qp)]=2spw`$. Returning to the original independent variables:

```math
\delta r=\frac2L\delta N-\frac rL\delta L,
\qquad \mathcal E_N=\frac2L\mathcal E_r,
\qquad \mathcal E_L=\mathcal E_{L|r}-\frac rL\mathcal E_r.
\tag{23}
```

Thus the **original $`N,L`$ equations** are

```math
\boxed{\begin{aligned}
0=\mathcal E_N={}&-\frac{4N}{L}-2gL-4g\\
&+\alpha\left[-\frac{4Nz}{L^2}-4g^2N-\frac{12gN^2}{L^2}
 +\frac{2s}{L}(q+2p)w\right],\\[2pt]
0=\mathcal E_L={}&R+s(2p^2-q^2)+\frac{2N^2}{L^2}-2gN
 -\frac32g^2L^2+4g^2L\\
&+\alpha\left[\left(g^2L+\frac{4N^2}{L^3}\right)z
 +\frac{8gN^3}{L^3}-\frac{2sN}{L^2}(q+2p)w\right]
\end{aligned}}
\tag{24}
```

The field $`N`$ has not been assumed auxiliary and eliminated beforehand.

<a id="32-vielbeinmetric-variation"></a>

### Vielbein/metric variation

Keeping the independent coordinate-component forms fixed, use

```math
\begin{gathered}
\delta e=-\frac e2g_{\mu\nu}\delta g^{\mu\nu},\qquad
\delta G^2=2G_{\mu\rho}G_\nu{}^\rho\delta g^{\mu\nu},\qquad
\delta H^2=3H_{\mu\rho\sigma}H_\nu{}^{\rho\sigma}\delta g^{\mu\nu},\\
\frac{\partial(I_2+\alpha I_4)}{\partial R}=L-\alpha z=\mathcal A,\qquad
\frac{\partial(I_2+\alpha I_4)}{\partial G^2}\Big|_{F-rG}
=-\frac{\mathcal A}{2},\qquad
\frac{\partial(I_2+\alpha I_4)}{\partial H^2}
=-\frac{\mathcal A}{3}
\end{gathered}
\tag{25}
```

In the epsilon term, $`e\varepsilon^{\mu\nu\rho\sigma\lambda}`$ is metric-independent. The metric variation of the composite $`a_\mu`$ also vanishes on $`E_a=0=dE_3`$. With the definition $`W_{\mu\nu}:=F'_{\mu\nu}-rG_{\mu\nu}`$, on the background,

```math
\begin{aligned}
\mathcal E_{\mu\nu}\big|_0={}&
\mathcal A R_{\mu\nu}-\frac12g_{\mu\nu}\mathscr F
 +(g_{\mu\nu}\Box-\nabla_\mu\nabla_\nu)\mathcal A\\
&-\mathcal A G_{\mu\rho}G_\nu{}^\rho
 -\mathcal A H_{\mu\rho\sigma}H_\nu{}^{\rho\sigma}
 -\frac\alpha2W_{\mu\rho}W_\nu{}^\rho,\\
\nabla_\mu\mathcal A&=0,\qquad
G_{i\rho}G_j{}^\rho=sq^2g_{ij},\qquad
W_{i\rho}W_j{}^\rho=sw^2g_{ij},\\
H_{m\rho\sigma}H_n{}^{\rho\sigma}&=-2sp^2g_{mn}.
\end{aligned}
\tag{26}
```

Here the $`(g\Box-\nabla\nabla)\mathcal A`$ term is the $`\delta R`$ contribution of the dependent Levi–Civita connection; it vanishes on the constant background. The two metric equations are

```math
\boxed{\begin{aligned}
0=\mathcal E_{(2)}&=\mathcal A k_2-\frac12\mathscr F
 -s\mathcal A q^2-\frac{\alpha s}{2}w^2,\\
0=\mathcal E_{(3)}&=2\mathcal A k_3-\frac12\mathscr F
 +2s\mathcal A p^2
\end{aligned}}
\tag{27}
```

Mixed blocks vanish. These equations are retained without dividing by $`\mathcal A`$, to preserve the possibility $`\mathcal A=0`$.

For an independent metric-sign check, scale the two blocks separately with coordinate forms fixed:

```math
\begin{gathered}
g_{(2)}\mapsto e^{2x}g_{(2)},\quad
g_{(3)}\mapsto e^{2y}g_{(3)},\quad e\mapsto e^{2x+3y}e,\\
k_2\mapsto e^{-2x}k_2,\quad k_3\mapsto e^{-2y}k_3,
\quad(q,u)\mapsto e^{-2x}(q,u),\quad p\mapsto e^{-3y}p,\\
e^{2x+3y}\left[2r(e^{-2x}u)(e^{-3y}p)
 -r^2(e^{-2x}q)(e^{-3y}p)\right]=2rup-r^2qp.
\end{gathered}
```

The last line states invariance of the epsilon density. Derivatives of (19) and (21) with respect to these scales are

```math
\begin{aligned}
\left.e^{-1}\partial_x(e\mathscr L_{\rm alg})\right|_{x=y=0}
&=2\mathscr F-4\mathcal A k_2+4s\mathcal A q^2+2\alpha s w^2
=-4\mathcal E_{(2)},\\
\left.e^{-1}\partial_y(e\mathscr L_{\rm alg})\right|_{x=y=0}
&=3\mathscr F-12\mathcal A k_3-12s\mathcal A p^2
=-6\mathcal E_{(3)}
\end{aligned}
```

In particular, tangent-frame flux amplitudes $`p,q,u`$ are not held fixed during variation; the independent coordinate form components are fixed.

<a id="33-equation-of-the-independent-three-form"></a>

### Equation of the independent three-form

The background $`E_a=0`$ does not remove the independent $`E_3`$ variation. In particular, retain

```math
\delta H_{abc}\big|_{\delta E_3}=\frac g2\delta E_{abc},\qquad
\delta E^a=-\frac1{48}\varepsilon^{abcde}(d\delta E_3)_{bcde}
\tag{28}
```

as written. The field-strength-representative BF term and $`H`$ dependencies give

```math
\begin{aligned}
\frac1e\delta S\big|_{\delta E_{cde},0}
=\bigg[&\frac1{12}\varepsilon^{abcde}(F'_{ab}+2gG_{ab})
 +\frac g3(\alpha z-L)H^{cde}\\
&+\frac{\alpha gr}{12}\varepsilon^{abcde}
 \left(F'_{ab}-\frac r2G_{ab}\right)\bigg]\delta E_{cde}.
\end{aligned}
\tag{29}
```

Using $`\varepsilon_{mncde}\varepsilon^{abcde}=-12\delta_{[m}^a\delta_{n]}^b`$
and $`\varepsilon_{mncde}H^{cde}=6Q_{mn}`$,

```math
\begin{aligned}
0&=(1+\alpha gr)F'
 +g\left(2-\frac{\alpha r^2}{2}\right)G+2g\mathcal A Q,\\
\mathcal E_{E_3}
&=\left(1+\frac{2\alpha gN}{L}\right)u
 +g\left(2-\frac{2\alpha N^2}{L^2}\right)q
 +2g\mathcal A p=0.
\end{aligned}
\tag{30}
```

Thus setting the $`V`$ flux to zero at the outset would impose an additional constraint changing the allowed $`H,G`$ backgrounds.

<a id="34-check-of-the-other-independent-field-equations"></a>

### Check of the other independent field equations

To check derivative contributions including the $`E_3`$ dependence of the composite $`a`$, define $`P:=rF'-r^2G/2`$. At constant $`r`$ and parallel fluxes, the Maxwell and dual-form parts of the $`a`$ variation are

```math
\delta_a S_4\big|_0
=\int e\left[-\frac12W^{ab}+rQ^{ab}\right]
 2\nabla_a\delta a_b
\ \Longrightarrow\
\nabla_a(W^{ab}-2rQ^{ab})=0.
\tag{31}
```

The Chern–Simons contribution is proportional to $`\varepsilon^{abcde}F'_{bc}G_{de}`$ and vanishes by (18). The two-derivative $`V`$ current is proportional to $`E^a`$ and vanishes. Thus additional $`E_3`$ derivative contributions through $`\delta a=2\delta E/L`$ also vanish; (30) includes all $`E_3`$ contributions on this background.

In the $`B`$ variation

```math
\begin{aligned}
\frac{\partial(I_2+\alpha I_4)}{\partial H_{abc}}\Big|_0
&=-\frac{2\mathcal A}{3}H^{abc}
 +\frac\alpha6\varepsilon^{deabc}P_{de},\\
\delta H_{abc}\big|_{\delta B}&=3\nabla_{[a}\delta B_{bc]},\\
\mathcal E_B^{bc}\big|_0
&=-3\nabla_a\left[-\frac{2\mathcal A}{3}H^{abc}
 +\frac\alpha6\varepsilon^{deabc}P_{de}\right]=0.
\end{aligned}
\tag{32}
```

The $`C`$ variation retains $`\delta G=d\delta C`$ and $`\delta H=(\delta C\wedge G+C\wedge d\delta C)/2`$ together. Derivative currents are parallel. Directly in the sources,

```math
H^{abc}G_{bc}=0,\qquad
\varepsilon^{deabc}P_{de}G_{bc}=0,\qquad
F'\wedge F'=F'\wedge G=G\wedge G=0
\tag{33}
```

because $`H`$ and $`G`$ fill different factors, while $`P,G,F'`$ are two-forms on the same two-dimensional factor. Thus $`\mathcal E_C|_0=0`$.

Along $`V'`$, $`\delta(\mathcal D L_{ij})`$ is orthogonal to constant $`n_{ij}`$. Since $`Y'_{ij}=n_{ij}y`$,

```math
\begin{gathered}
n^{ij}\delta_{V'}(\mathcal D_aL_{ij})=0,\qquad
n^{ij}\delta_{V'}(\Box_cL_{ij})=0,\\
\delta_{V'}(Y'^{ij}Y'_{ij})=2y\,n^{ij}\delta_{V'}Y'_{ij}=0,\qquad
\delta_{V'}(L^{ij}Y'_{ij})=L\,n^{ij}\delta_{V'}Y'_{ij}=0.
\end{gathered}
\tag{34}
```

The variation of $`F'`$ in this direction also vanishes: in the Abelian projection, $`\delta R(V')`$ is orthogonal; remaining $`V'`$ contributions start with $`V'^2`$ or $`(\mathcal D L)^2`$. The first variation of the $`E\mathcal D L`$ term vanishes on $`E=\mathcal D L=0`$. Thus $`\mathcal E_{V'}|_0=0`$; this equation was not discarded when imposing the ansatz.

The action is Grassmann-even. For $`\Theta=(\psi_\mu{}^i,\varphi^i)`$, every fermionic monomial contains at least two odd fields:

```math
S=S_{\rm bos}+S_{(2)}[\Theta]+O(\Theta^4),\qquad
\left.\frac{\delta^L S}{\delta\Theta}\right|_{\Theta=0}=0,
\qquad
\left.\delta_{\rm bos}S_{(2)}\right|_{\Theta=0}=0.
\tag{35}
```

These equalities require no conversion of Grassmann variables to commuting variables. Contributions of dependent fermionic connections vanish by the same degree counting. Thus the full local solution criterion in this class comprises **the five algebraic equations (24), (27), (30)**, $`L>0`$, real fluxes, and the geometric conditions (15)–(18).

<a id="4-verified-ads₅-branch"></a>

## Verified AdS₅ branch

For maximal symmetry,

```math
R_{abcd}=\kappa(\eta_{ac}\eta_{bd}-\eta_{ad}\eta_{bc}),\qquad
R_{ab}=4\kappa\eta_{ab},\qquad R=20\kappa.
\tag{36}
```

The quantity $`G,H,dE_3,dV`$ preserving full five-dimensional isotropy vanishes. Let the proposed constant field values be

```math
\boxed{\begin{gathered}
L=L_0>0,\qquad N=-\frac32gL_0^2,\qquad
\kappa=-\frac12g^2L_0^2,\\
G=H=dE_3=dV=0,\qquad E_a=0,\qquad V_\mu^{\prime\,ij}=0,\\
\psi_\mu{}^i=\varphi^i=0
\end{gathered}}
\tag{37}
```

Substitute these into (19) without yet assuming they solve the equations:

```math
\begin{aligned}
z_0&=-\frac{-10g^2L_0^2}{2}
 -\frac{(9/4)g^2L_0^4}{L_0^2}+\frac14g^2L_0^2
=3g^2L_0^2,\\
\mathcal A_0&=L_0-3\alpha g^2L_0^2,\\
\mathscr F_0&=2g^2L_0^2(9\alpha g^2L_0^2-6L_0+4).
\end{aligned}
\tag{38}
```

With the definition $`\mathcal C(L):=3\alpha g^2L^2-4L+4`$, all residuals of the original scalar and metric equations are

```math
\begin{aligned}
\mathcal E_N\big|_{(37)}&=-g\,\mathcal C(L_0),\\
\mathcal E_L\big|_{(37)}&=g^2L_0\,\mathcal C(L_0),\\
\mathcal E_{ab}\big|_{(37)}
&=\left(4\kappa\mathcal A_0-\frac12\mathscr F_0\right)\eta_{ab}
=-g^2L_0^2\mathcal C(L_0)\eta_{ab}
\end{aligned}
\tag{39}
```

The form and fermion equations vanish. Thus

```math
\boxed{3\lambda_{R^2}g^2L_0^2-4L_0+4=0,
\qquad \ell_{\mathrm{AdS}_5}^2=\frac{2}{g^2L_0^2}}
\tag{40}
```

under this condition, (37) is a bosonic solution of the supplied action, not merely a candidate.

Check of the dependent composites:

```math
\begin{aligned}
T_{ab}&=0,\qquad
f_\mu{}^a=-\frac\kappa4e_\mu{}^a
=\frac{g^2L_0^2}{8}e_\mu{}^a,\qquad
f_a{}^a=\frac58g^2L_0^2,\\
D_0&=-\frac{R_0}{32}+\frac g4N_0+\frac{g^2L_0^2}{16}
=\left(\frac5{16}-\frac6{16}+\frac1{16}\right)g^2L_0^2=0,\\
\Box_cL_{ij}\big|_0&=6f_a{}^aL_{ij}
=\frac{15}{4}g^2L_0^2L_{ij},\\
\rho'_0&=-3gL_0,\qquad
Y'_{ij}\big|_0=\frac{\delta_{ij}}{\sqrt2}\frac32g^2L_0^2,
\qquad F'_0=\lambda'_0=0.
\end{aligned}
\tag{41}
```

The condition $`D_0=0`$ follows as a result; it was not imposed initially.

<a id="41-coefficient-condition"></a>

### Coefficient condition

For $`t:=\lambda_{R^2}g^2`$, the roots of (40) are

```math
L_- =\frac{2}{1+\sqrt{1-3t}},\qquad
L_+ =\frac{2}{1-\sqrt{1-3t}}
\tag{42}
```

while $`t=0`$ is evaluated separately:

| Coefficient | Positive $`L_0`$ values on this branch are |
|---|---|
| $`t<0`$ | Only $`L_-`$ |
| $`t=0`$ | $`L_0=1`$ |
| $`0<t<1/3`$ | $`L_-`$ and $`L_+`$ |
| $`t=1/3`$ | Coincident root $`L_0=2`$ |
| $`t>1/3`$ | No real root on this branch |

This table concerns branch (37); it is not a nonexistence theorem for other scalar branches. For example, the degenerate branch below supplies additional solutions of the same action. On (40), $`\mathcal A_0=4-3L_0`$; the conditions $`\mathcal A_0=0`$ and $`\mathcal A_0<0`$ are not removed from the solution equations. The table classifies solutions of the background equations on this branch.

<a id="5-explicit-product-solution-branch-carrying-both-fluxes"></a>

## Explicit product-solution branch carrying both fluxes

For the same $`L_0`$ satisfying (40), take $`p\in\mathbb R`$:

```math
\boxed{\begin{gathered}
N_0=-\frac32gL_0^2,\qquad
H=p\Omega_3,\qquad G=2p\Omega_2,\qquad
\sqrt2dV=-6gL_0p\Omega_2,\\
k_2=-2g^2L_0^2+4sp^2,\qquad
k_3=-g^2L_0^2-sp^2,\\
L=L_0>0,\quad V'=0,\quad E_a=dE_3=0,\quad
\psi_\mu{}^i=\varphi^i=0.
\end{gathered}}
\tag{43}
```

The relation $`q=2p`$ is a property of this explicit branch, not a requirement added to the general field equations.

Direct substitution:

```math
\begin{aligned}
R_0&=2k_2+6k_3=-10g^2L_0^2+2sp^2,\\
w_0&=-6gL_0p-(-3gL_0)(2p)=0,\\
z_0&=5g^2L_0^2-sp^2-\frac94g^2L_0^2
 +s(2p^2-p^2)+\frac14g^2L_0^2=3g^2L_0^2,\\
\mathscr F_0+4\mathcal A_0g^2L_0^2
&=2g^2L_0^2(3\alpha g^2L_0^2-4L_0+4)
=2g^2L_0^2\mathcal C(L_0).
\end{aligned}
\tag{44}
```

The five independent algebraic residuals are:

```math
\boxed{\begin{aligned}
\mathcal E_N&=-g\mathcal C(L_0),&
\mathcal E_L&=g^2L_0\mathcal C(L_0),\\
\mathcal E_{(2)}&=-g^2L_0^2\mathcal C(L_0),&
\mathcal E_{(3)}&=-g^2L_0^2\mathcal C(L_0),\\
\mathcal E_{E_3}&=gp\mathcal C(L_0).
\end{aligned}}
\tag{45}
```

For example, cancellation in the three-form equation, retaining every coefficient, is

```math
\begin{aligned}
\mathcal E_{E_3}
&=(1-3\alpha g^2L_0)(-6gL_0p)
 +g\left(2-\frac92\alpha g^2L_0^2\right)(2p)
 +2g(L_0-3\alpha g^2L_0^2)p\\
&=gp\left[-6L_0+18\alpha g^2L_0^2+4
 -9\alpha g^2L_0^2+2L_0-6\alpha g^2L_0^2\right]\\
&=gp\mathcal C(L_0).
\end{aligned}
\tag{46}
```

On this branch, the dependent $`T,D`$ is also

```math
\begin{aligned}
T_{ab}\big|_0&=\frac{3p}{8}(\Omega_2)_{ab},\\
D\big|_0
&=-\frac{R_0}{32}
 +\frac{s(5q^2-2qp-13p^2)}{48}
 +\frac g4N_0+\frac{g^2L_0^2}{16}\Bigg|_{q=2p}\\
&=\frac5{16}g^2L_0^2-\frac{s p^2}{16}
 +\frac{s p^2}{16}-\frac38g^2L_0^2+\frac1{16}g^2L_0^2=0.
\end{aligned}
\tag{47}
```

<a id="51-lorentzian-sigma_3-magnetic-g-electric-h"></a>

### Lorentzian $`\Sigma_3`$: magnetic $`G`$, electric $`H`$

For $`s=+1`$, there is an exceptional family satisfying

```math
k_3=-(g^2L_0^2+p^2)<0,\qquad
k_2=4p^2-2g^2L_0^2.
\tag{48}
```

| Flux interval | Verified geometry |
|---|---|
| $`0<p^2<g^2L_0^2/2`$ | $`\mathrm{AdS}_3\times H^2`$ |
| $`p^2=g^2L_0^2/2`$ | $`\mathrm{AdS}_3\times\mathbb R^2`$ |
| $`p^2>g^2L_0^2/2`$ | $`\mathrm{AdS}_3\times S^2`$ |

$`\ell_{\mathrm{AdS}_3}^{-2}=g^2L_0^2+p^2`$;
the curved two-dimensional factor has radius $`|4p^2-2g^2L_0^2|^{-1/2}`$.

<a id="52-lorentzian-sigma_2-electric-g-magnetic-h"></a>

### Lorentzian $`\Sigma_2`$: electric $`G`$, magnetic $`H`$

For $`s=-1`$, there is an exceptional family satisfying

```math
k_2=-(2g^2L_0^2+4p^2)<0,\qquad
k_3=p^2-g^2L_0^2.
\tag{49}
```

| Flux interval | Verified geometry |
|---|---|
| $`0<p^2<g^2L_0^2`$ | $`\mathrm{AdS}_2\times H^3`$ |
| $`p^2=g^2L_0^2`$ | $`\mathrm{AdS}_2\times\mathbb R^3`$ |
| $`p^2>g^2L_0^2`$ | $`\mathrm{AdS}_2\times S^3`$ |

$`\ell_{\mathrm{AdS}_2}^{-2}=2g^2L_0^2+4p^2`$;
the curved three-dimensional factor has radius $`|p^2-g^2L_0^2|^{-1/2}`$.

In the limit $`p=0`$, (43) is a fluxless Einstein **product** geometry. Its mixed Riemann components vanish, so it differs from the maximally symmetric AdS₅ in (37), despite having the same Ricci tensor.

<a id="6-broader-degenerate-branch-for-lambda_r2g214"></a>

## Broader degenerate branch for $`\lambda_{R^2}g^2=1/4`$

Solving (27) by dividing by $`\mathcal A`$ would lose this branch. Take the following values without imposing (40):

```math
\boxed{\begin{gathered}
\lambda_{R^2}g^2=\frac14,\qquad L=L_0>0,\qquad N_0=-2gL_0,\\
G=q\Omega_2,\qquad H=p\Omega_3,\qquad
\sqrt2dV=-4gq\Omega_2,\\
2k_2+6k_3+s(2p^2-q^2)
=g^2\left(\frac{L_0^2}{2}-8L_0-8\right).
\end{gathered}}
\tag{50}
```

Other background fields are as in (17). Here $`L_0`$ is free, with no constraint $`q=2p`$. The definitions give

```math
r_0=-4g,\qquad w_0=0,\qquad z_0=4g^2L_0,
\qquad \mathcal A_0=L_0-\frac{4g^2L_0}{4g^2}=0.
\tag{51}
```

For the check, write $`X:=R+s(2p^2-q^2) =g^2(L_0^2/2-8L_0-8)`$. The density is

```math
\begin{aligned}
\mathscr F_0
={}&\underbrace{L_0X
 -8g^2L_0+4g^2L_0^2+8g^2L_0
 -\frac12g^2L_0^3+2g^2L_0^2}_{-2g^2L_0^2-8g^2L_0}\\
&+\underbrace{\frac1{4g^2}
 \left(16g^4L_0^2-8g^4L_0^2+32g^4L_0\right)}
 _{2g^2L_0^2+8g^2L_0}=0.
\end{aligned}
\tag{52}
```

The scalar equations, in the form (22), are

```math
\begin{aligned}
\mathcal E_r\big|_0
&=-gL_0(L_0-2)
 +\frac1{4g^2}\left(16g^3L_0+4g^3L_0^2-24g^3L_0\right)=0,\\
\mathcal E_{L|r}\big|_0
&=g^2(-L_0^2+4L_0-8)
 +\frac1{4g^2}\left(4g^4L_0^2-16g^4L_0+32g^4\right)=0.
\end{aligned}
\tag{53}
```

Equation (23) gives the original $`\mathcal E_N=\mathcal E_L=0`$ result. In the three-form equation,

```math
1+\alpha gr_0=1-1=0,\qquad
2-\frac{\alpha r_0^2}{2}=2-2=0,\qquad \mathcal A_0=0;
\tag{54}
```

and the metric equations have $`\mathcal A_0=\mathscr F_0=w_0=0`$. All background equations hold.

<a id="61-geometric-possibilities-on-this-branch"></a>

### Geometric possibilities on this branch

For either signature and a supplied $`k_2,k_3,L_0>0`$, (50) can be solved as follows:

```math
q^2=2p^2+s\left[2k_2+6k_3
 -g^2\left(\frac{L_0^2}{2}-8L_0-8\right)\right].
\tag{55}
```

For sufficiently large $`p^2`$, both $`p^2>0`$ and $`q^2>0`$ hold. Thus **at this special coefficient**, with both fluxes present,

```math
\begin{gathered}
\{\mathrm{AdS}_3,\mathbb R^{1,2},\mathrm{dS}_3\}
\times\{H^2,\mathbb R^2,S^2\},\\
\{\mathrm{AdS}_2,\mathbb R^{1,1},\mathrm{dS}_2\}
\times\{H^3,\mathbb R^3,S^3\}
\end{gathered}
\tag{56}
```

local solutions exist for every listed geometric type. This prevents inferring a general exclusion of dS or flat Lorentzian factors at arbitrary coefficients. The AdS restriction in (48)–(49) belongs only to branch (43).

If only $`H`$ or only $`G`$ is required, (50) imposes, respectively,

```math
\begin{aligned}
G=0:&\quad 2s p^2=g^2\left(\frac{L_0^2}{2}-8L_0-8\right)-R,\quad p^2>0,\\
H=0:&\quad s q^2=R-g^2\left(\frac{L_0^2}{2}-8L_0-8\right),\quad q^2>0
\end{aligned}
\tag{57}
```

these conditions. Single-flux and two-flux branches therefore remain distinct.

<a id="62-additional-maximally-symmetric-branch-at-the-same-special-coefficient"></a>

### Additional maximally symmetric branch at the same special coefficient

With zero fluxes and $`R=20\kappa`$, (50)–(54) similarly give

```math
N_0=-2gL_0,\qquad
\kappa=\frac{g^2}{40}(L_0^2-16L_0-16)
\tag{58}
```

as stated. Since $`L_0^2-16L_0-16=(L_0-8)^2-80`$,

```math
\begin{cases}
0<L_0<8+4\sqrt5:&\mathrm{AdS}_5,\quad
\ell^2=\dfrac{40}{g^2(16+16L_0-L_0^2)},\\
L_0=8+4\sqrt5:&\mathbb R^{1,4},\\
L_0>8+4\sqrt5:&\mathrm{dS}_5.
\end{cases}
\tag{59}
```

Since $`\mathcal A_0=0`$, this branch must be marked degenerate. This means neither absence of a solution nor removal of fermionic fluctuations. Spectral procedures assuming a standard nonzero Einstein coefficient do not apply.

<a id="7-independent-coefficient-check-in-the-two-derivative-limit"></a>

## Independent coefficient check in the two-derivative limit

Set $`\alpha=0`$ only as a limit check. The analysis of the total theory does not set $`\alpha`$ to zero. In this limit, for $`X:=R+s(2p^2-q^2)`$, the general equations (24), (27), and (30) become

```math
\begin{aligned}
\mathcal E_r=0&\ \Longrightarrow\ r=-g(L+2),\\
\mathcal E_{L|r}=0&\ \Longrightarrow\ X=-g^2(8L+2),\\
\mathscr F&=LX+4g^2L^2+2g^2L=-4g^2L^2,\\
k_2&=-2g^2L+sq^2,\qquad k_3=-g^2L-sp^2,\\
X&=-10g^2L+s(q^2-4p^2)
\end{aligned}
\tag{60}
```

Equating the two expressions for $`X`$, in the original fields,

```math
\boxed{\begin{gathered}
L_0=1+\frac{s(q^2-4p^2)}{2g^2}>0,\qquad
N_0=-\frac g2L_0(L_0+2),\qquad
\sqrt2dV=(-2gq-2gL_0p)\Omega_2,\\
k_2=-2g^2+4sp^2,\qquad
k_3=-g^2-\frac s2q^2+sp^2
\end{gathered}}
\tag{61}
```

The choice $`q=2p`$, with $`L_0=1`$, gives the limit of (43). This check also shows that (43) does not classify every flux branch. For arbitrary $`\lambda_{R^2}`$ and arbitrary flux ratio, the admissibility criterion is (24), (27), (30); the explicit solution tables list branches directly verified in these equations.

<a id="8-local-realization-and-fluctuations"></a>

## Local realization and fluctuations

On a coordinate patch, choose a one-form $`\mathcal U_2`$ satisfying $`d\mathcal U_2=\Omega_2`$. Then, in the local representative

```math
C=q\mathcal U_2,\qquad V=\frac u{\sqrt2}\mathcal U_2,
\qquad B=0,\qquad E_3=\frac2g p\Omega_3
\tag{62}
```

one has

```math
C\wedge G=0,\qquad
dB+\frac12C\wedge G+\frac g2E_3=p\Omega_3,\qquad
dE_3=0\ \Longrightarrow\ E_a=0
\tag{63}
```

Although $`\mathcal U_2`$ is a one-form, its subscript denotes only the two-dimensional factor on which it is defined. This representative shows that $`E_3\ne0`$ and $`E_a=0`$ can coexist; it adds no gauge condition to the action. Global quotients, flux quantization, and bundle transitions require additional global data; the existence results here are local.

**All independent fluctuations are retained** on these backgrounds:

```math
\begin{gathered}
e=e^{(0)}+\delta e,\quad C=C^{(0)}+\delta C,\quad
B=B^{(0)}+\delta B,\quad L=L_0+\delta L,\quad N=N_0+\delta N,\\
E_3=E_3^{(0)}+\delta E_3,\quad V=V^{(0)}+\delta V,\quad
V'=\delta V',\quad \psi_\mu{}^i=\delta\psi_\mu{}^i,\quad
\varphi^i=\delta\varphi^i.
\end{gathered}
\tag{64}
```

In particular, $`\delta\psi_\mu{}^i`$, $`\delta\varphi^i`$, $`\delta V'`$, and $`\delta E_3`$ are not set to zero. Fluctuations are not restricted to the homogeneous product ansatz of the background. The quantities $`\delta E_a,\delta T,\delta D`$ and dependent connections are computed by varying their definitions; for example, $`D_0=0`$ does not imply $`\delta D=0`$. These solution conditions are not interpreted as BPS, stability, or spectral results.
