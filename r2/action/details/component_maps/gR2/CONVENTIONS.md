# Conventions

<a id="1-dimension-indices-and-metric"></a>

## Dimension, indices, and metric

```math
D=5,\qquad
\eta_{ab}=\mathop{\mathrm{diag}}\nolimits(-,+,+,+,+).
```

World indices are $`(\mu,\nu,\ldots=0,\ldots,4)`$, tangent-space indices are $`(a,b,\ldots=0,\ldots,4)`$, and internal indices are $`(i,j=1,2)`$. Tangent indices are raised and lowered with $`(\eta_{ab})`$. The vielbein convention is

```math
g_{\mu\nu}=e_\mu{}^ae_\nu{}^b\eta_{ab}
```

as written.

```math
e=\det(e_\mu{}^a)=\sqrt{-g}.
```

The notation relating the action density and scalar Lagrangian is

```math
\mathscr L\equiv e^{-1}\mathcal L,
\qquad
S=\int d^5x\,\mathcal L
=\int d^5x\,e\,\mathscr L
```

This project uses tangent components. With $`e^{-1}\mathcal L`$, the bosonic
two-derivative scalar Lagrangian is called $`\mathscr L_{\mathrm{2-der}}^{(0)}`$, and the Einstein term
is $`LR`$. Relative to the alternative density normalization with
Einstein term $`LR/2`$, the global conversion is

```math
\left.\mathcal L_{\mathrm{2-der}}\right|_{g=0}
=2\mathcal L_{\mathrm{2-der}}^{\mathrm{lower}}
```

This factor does not represent two physical multiplets
or two independent actions.

```math
X_a=e_a{}^\mu X_\mu,
\qquad
X^a=e_\mu{}^aX^\mu,
\qquad
G_{ab}=e_a{}^\mu e_b{}^\nu G_{\mu\nu},
\qquad
V_a^{\prime\,ij}=e_a{}^\mu V_\mu^{\prime\,ij}.
```

The same pullback convention applies to $`C_a`$, $`V_a`$, and $`E^a`$.

The curvature convention is

```math
\begin{aligned}
R_{\mu\nu}{}^{ab}
&=2\partial_{[\mu}\omega_{\nu]}{}^{ab}
  +2\omega_{[\mu}{}^{ac}\omega_{\nu]c}{}^b,\\
R_{abcd}
&=e_a{}^\mu e_b{}^\nu R_{\mu\nu cd},\\
R_{bd}&=\eta^{ac}R_{abcd},\qquad
R=\eta^{bd}R_{bd}.
\end{aligned}
```

The equivalent convention for the torsion-free coordinate connection is

```math
R^\rho{}_{\sigma\mu\nu}
=2\partial_{[\mu}\Gamma^\rho_{\nu]\sigma}
 +2\Gamma^\rho_{[\mu|\lambda|}\Gamma^\lambda_{\nu]\sigma},
\qquad
R_{\mu\nu}=R^\rho{}_{\mu\rho\nu}
```

as specified.

The dependent second-order superconformal spin connection is

```math
\begin{aligned}
\omega_\mu{}^{ab}(e,\psi_\mu,b)
={}&2e^{\nu[a}\partial_{[\mu}e_{\nu]}{}^{b]}
-e^{\nu[a}e^{b]\rho}e_{\mu c}\partial_\nu e_\rho{}^c\\
&+2e_\mu{}^{[a}b^{b]}
+\frac12\bar\psi^{[a}\gamma^{b]}\psi_\mu
+\frac14\bar\psi^a\gamma_\mu\psi^b,
\qquad
\psi^a=e^{a\mu}\psi_\mu,qquad b^a=e^{a\mu}b_\mu .
\end{aligned}
```

In the selected $`b_\mu=0`$ gauge, the $`b`$ term vanishes. The fermion terms in the form

```math
-\frac12\bar\psi^{[b}\gamma^{a]}\psi_\mu
-\frac14\bar\psi^b\gamma_\mu\psi^a
```

This form is equivalent to the ordering above after antisymmetrization
and the NW–SE-contracted rank-one flip. The dilatino gauge $`\psi^i=0`$ does
not set the gravitino $`\psi_\mu^i`$ to zero; the connection reduces to torsion-free
Levi–Civita only under the bosonic truncation $`\psi_\mu^i=0`$.

<a id="3-antisymmetrization-and-forms"></a>

## (Anti)symmetrization and forms

(Anti)symmetrization has unit weight:

```math
X_{[ab]}=\frac12(X_{ab}-X_{ba}),\qquad
X_{(ab)}=\frac12(X_{ab}+X_{ba}).
```

The component convention for a general $`p`$-form is

```math
\phi_p
=\frac1{p!}\phi_{\mu_1\ldots\mu_p}
  dx^{\mu_1}\wedge\cdots\wedge dx^{\mu_p}.
```

The exterior derivative acts from the left. For a one-form,

```math
A=A_\mu dx^\mu,\qquad
dA=\partial_\nu A_\mu\,dx^\nu\wedge dx^\mu.
```

<a id="4-levicivita-orientation-and-duality"></a>

## Levi–Civita orientation and duality

The authoritative tangent-space orientation is

```math
\varepsilon^{01234}=+1,\qquad
\varepsilon_{01234}=-1.
```

Epsilon contraction

```math
\varepsilon_{a_1\ldots a_n b_1\ldots b_p}
\varepsilon^{a_1\ldots a_n c_1\ldots c_p}
=-n!p!\,
\delta_{[b_1}^{c_1}\cdots\delta_{b_p]}^{c_p}
```

as written. The coordinate epsilon symbol is denoted by $`\epsilon^{01234}=+1`$, and the contravariant Levi–Civita tensor by

```math
\varepsilon^{\mu\nu\rho\sigma\lambda}
=e^{-1}\epsilon^{\mu\nu\rho\sigma\lambda}
=e_a{}^\mu e_b{}^\nu e_c{}^\rho e_d{}^\sigma e_e{}^\lambda
 \varepsilon^{abcde}
```

as written. Equivalently, the coordinate symbol is

```math
\epsilon^{\mu\nu\rho\sigma\lambda}
=e\,e_a{}^\mu e_b{}^\nu e_c{}^\rho e_d{}^\sigma e_e{}^\lambda
 \varepsilon^{abcde}
```

The symbol $`\epsilon`$ and tensor $`\varepsilon`$ are not silently interchanged.

The tangent components of the three-form are

```math
H_{abc}
=e_a{}^\mu e_b{}^\nu e_c{}^\rho H_{\mu\nu\rho}
```

The $`H_{ab}`$ used here is the project-normalized two-form,
not the standard Hodge dual:

```math
\boxed{
H^{ab}=-\frac1{12}\varepsilon^{abcde}H_{cde},
\qquad
H_{ab}=-\frac1{12}\varepsilon_{abcde}H^{cde}.}
```

The standard Hodge dual of $`1/3!`$ has a separate symbol:

```math
\boxed{
\widetilde H_{ab}
\equiv(*H_3)_{ab}
=\frac1{3!}\varepsilon_{abcde}H^{cde}
=-2H_{ab}.}
```

Therefore,

```math
\widetilde H_{ab}\widetilde H^{ab}
=4H_{ab}H^{ab}.
```

With the same conventions, the norm relations are

```math
H_{ab}H^{ab}=-\frac1{12}H_{abc}H^{abc},
\qquad
\widetilde H_{ab}\widetilde H^{ab}
=-\frac13H_{abc}H^{abc}
```

Thus the coefficient $`+4H_{ab}H^{ab}`$ is unchanged in project notation;
the same term is $`+\widetilde H_{ab}\widetilde H^{ab}`$ in standard-dual notation.

In Lorentzian five dimensions, using $`*^2=-1`$, conversion from the
project-normalized two-form to the three-form is

```math
\boxed{
H^{abc}=\varepsilon^{abcde}H_{de},
\qquad
H_{abc}=\varepsilon_{abcde}H^{de}.}
```

The constrained vector $`E^a`$ is defined as the dual of the curl of the three-form potential $`E_{\mu\nu\rho}`$:

```math
E_{abc}
=e_a{}^\mu e_b{}^\nu e_c{}^\rho E_{\mu\nu\rho}.
```

At the exact source-supercovariant level,

```math
\boxed{
E^a
=-\frac1{12}e_\mu{}^a e^{-1}
 \epsilon^{\mu\nu\rho\sigma\lambda}
 \mathcal D_\nu E_{\rho\sigma\lambda},
\qquad
\mathcal D_aE^a=0.}
```

Here $`\mathcal D`$ denotes the source-supercovariant derivative and is not identified with the ordinary $`\partial`$, torsion-free $`\nabla`$, or residual-$`U(1)_R`$ derivative defined below. Under bosonic truncation,

```math
E^a
=-\frac1{12}e_\mu{}^a e^{-1}
 \epsilon^{\mu\nu\rho\sigma\lambda}
 \partial_\nu E_{\rho\sigma\lambda}
```

and, in tangent-space notation with $`\nabla_b`$ the torsion-free Levi–Civita derivative,

```math
\boxed{
E^a=-\frac1{12}\varepsilon^{abcde}\nabla_bE_{cde},
\qquad
E_a=-\frac1{12}\varepsilon_{abcde}\nabla^bE^{cde}
=\eta_{ab}E^b.}
```

With the four-form field strength

```math
\mathcal E_{\mu\nu\rho\sigma}
\equiv4\partial_{[\mu}E_{\nu\rho\sigma]},
\qquad
\mathcal E_{abcd}
=e_a{}^\mu e_b{}^\nu e_c{}^\rho e_d{}^\sigma
 \mathcal E_{\mu\nu\rho\sigma}
```

the same definition reads

```math
\boxed{
E^a=-\frac1{48}\varepsilon^{abcde}\mathcal E_{bcde},
\qquad
E_a=-\frac1{48}\varepsilon_{abcde}\mathcal E^{bcde}.}
```

This gives the bosonic identity $`\nabla_aE^a=0`$. The constrained vector denoted
$`P^a`$ in the alternative frame corresponds to $`E^a`$ here after the full
signed frame conversion below; $`P^a`$ and $`E^a`$ are not independent fields.

<a id="5-clifford-algebra"></a>

## Clifford algebra

```math
\{\gamma^a,\gamma^b\}=2\eta^{ab},\qquad
\gamma^{a_1\ldots a_r}
=\gamma^{[a_1}\cdots\gamma^{a_r]} .
```

For the odd-dimensional irrep $`+`$ specified for this analysis
and this project's orientation,

```math
\boxed{
\gamma^{a_1\ldots a_r}
=\frac{i}{(5-r)!}\varepsilon^{a_1\ldots a_5}
 \gamma_{a_5\ldots a_{r+1}}.}
```

In particular,

```math
\boxed{\gamma^{abcde}=+i\varepsilon^{abcde}\mathbf1.}
```

This permits choosing the independent Clifford basis as

```math
\{\mathbf1,\gamma^a,\gamma^{ab}\}
```

as written. No explicit gamma-matrix representation has been selected.

The dot and slash conventions are

```math
\boxed{
\gamma\!\cdot\!X
=\gamma^{a_1\ldots a_p}X_{a_1\ldots a_p}}
```

and

```math
\mathord{\not{X}}=\gamma^aX_a,\qquad
\mathord{\not{D}}=\gamma^aD_a.
```

The definition of $`\gamma\!\cdot\!X`$ contains no $`1/p!`$.

<a id="6-spinor-conventions"></a>

## Spinor conventions

The unconstrained dynamical fermions in the new gauge are $`\psi_\mu^i`$ and $`\varphi^i`$, both anticommuting symplectic–Majorana spinors. The dilatino $`\psi^i=0`$ is gauge-fixed and is not part of the dynamical fermion set. The collective notation is

```math
\Psi\equiv\left(\psi_\mu^i,\varphi^i\right)
```

and, for the retained bosonic fields,

```math
\Phi\equiv
\left(
e_\mu{}^a,C_\mu,B_{\mu\nu},L,E_{\mu\nu\rho},N,
V_\mu,V_\mu^{\prime\,ij}
\right)
```

as written. The gauge-fixed $`\sigma`$ and $`\psi^i`$ do not belong to the sets $`\Phi`$ and $`\Psi`$, respectively. The three-form potential $`E_{\mu\nu\rho}`$ is the equivalent potential representation of the constrained vector $`E^a`$ defined in Section 4, not a second independent field. Suppressed internal indices imply NW–SE contraction:

```math
\bar X\Gamma Y\equiv\bar X^i\Gamma Y_i.
```

The second residual-$`U(1)_R`$-invariant contraction is

```math
\bar X^i\Gamma Y^j\delta_{ij}
```

The NW–SE index-lowering tensor is denoted by $`\Omega_{ij}\equiv\epsilon_{ij}=-\epsilon_{ji}`$, with component sign

```math
\boxed{\epsilon_{12}=\epsilon^{12}=1}
```

fixed as shown.

The notation $`\epsilon_{ij}\equiv\Omega_{ij}`$ is also used equivalently to raise and lower SU(2) indices. For any spinor $`\Psi`$,

```math
\Psi^i=\epsilon^{ij}\Psi_j,
\qquad
\Psi_i=\Psi^j\epsilon_{ji}
=-\Psi^j\epsilon_{ij}.
```

With this choice,

```math
\epsilon_{ij}=-\epsilon_{ji},
\qquad
\epsilon^{ij}\epsilon_{kj}=\delta^i{}_k.
```

For symmetric $`L_{ij}=L_{ji}`$,

```math
L^{ij}=\epsilon^{ik}\epsilon^{j\ell}L_{k\ell},
\qquad
L_i{}^j=\epsilon^{jm}L_{im},
\qquad
L^i{}_j=\epsilon^{ik}L_{kj}.
```

Since $`L_{ij}=L\delta_{ij}/\sqrt2`$ on the selected gauge slice,

```math
\boxed{
\begin{aligned}
L^{ij}&=\frac{L}{\sqrt2}\delta^{ij},\\
L_i{}^j&=-\frac{L}{\sqrt2}\delta_{im}\epsilon^{mj},\\
L^i{}_j&=\frac{L}{\sqrt2}\epsilon^{ik}\delta_{kj}.
\end{aligned}}
```

Raising or lowering only one $`SU(2)`$ index leaves an epsilon; it does not produce a Kronecker delta.

Interchanging the positions of a contracted SU(2) index pair introduces a minus sign. For any two spinors $`\Psi,\Phi`$,

```math
\overline{\Psi^i}\,\gamma^{abc\ldots}\Phi_i
=-\overline{\Psi_i}\,\gamma^{abc\ldots}\Phi^i.
```

The same rule applies separately to each contracted index pair in expressions with multiple SU(2) indices. For example,

```math
\begin{aligned}
L^{ij}\,\overline{\Psi_i}\,\Gamma\Phi_j
&=-L^i{}_j\,\overline{\Psi_i}\,\Gamma\Phi^j\\
&=-L_i{}^j\,\overline{\Psi^i}\,\Gamma\Phi_j\\
&=L_{ij}\,\overline{\Psi^i}\,\Gamma\Phi^j.
\end{aligned}
```

In general, interchanging the positions of $`N`$ contracted SU(2) index pairs in this way produces the total sign factor $`(-1)^N`$.

The five-dimensional Fierz completeness relation used here is

```math
\psi_j\bar\lambda^i
=-\frac14(\bar\lambda^i\psi_j)
-\frac14(\bar\lambda^i\gamma^a\psi_j)\gamma_a
+\frac18(\bar\lambda^i\gamma^{ab}\psi_j)\gamma_{ab}
```

as written.

The flip rule for anticommuting symplectic–Majorana spinors is

```math
\bar\lambda^i\gamma_{(n)}\chi^j
=t_n\,\bar\chi^j\gamma_{(n)}\lambda^i
```

with signs

```math
t_0=t_1=t_4=t_5=+1,\qquad
t_2=t_3=-1.
```

The NW–SE-contracted flip has an additional minus sign from moving the index through epsilon:

```math
\boxed{
\bar\lambda^i\gamma_{(n)}\chi_i
=-t_n\,\bar\chi^i\gamma_{(n)}\lambda_i.}
```

The operational conjugate in calculations is the Majorana conjugate:

```math
\bar\lambda=\lambda^T C
```

as specified. Dirac-bar notation may be used only after its phase relative to the Majorana bar has been separately derived and fixed in the relevant explicit gamma representation. This project does not fix an independent Dirac-bar phase; the Majorana bar is not silently replaced by a Dirac bar during a calculation.

<a id="7-residual-internal-connection-and-fermion-derivatives"></a>

## Residual internal connection and fermion derivatives

The conformal gauge conditions and fields left free are theory data.
After the selected gauge choice, local $`SU(2)`$ is broken to $`U(1)_R`$.
The internal-connection convention is

```math
V_\mu^{ij}
=V_\mu^{\prime\,ij}+\frac12\delta^{ij}V_\mu,\qquad
V_\mu^{\prime\,ij}\delta_{ij}=0.
```

The full source-superconformal derivative $`\mathcal D_\mu`$ contains the full $`V_\mu{}^{ij}`$ connection and the other connections required by the field's source Weyl weights and charges. A derivative containing only the trace $`V_\mu`$ is residual-$`U(1)_R`$ shorthand, not the full $`\mathcal D_\mu`$; the missing $`V'_\mu{}^{ij}`$ contribution is written separately when required.

With $`\lambda^i`$ denoting any spinor doublet charged under residual $`U(1)_R`$, the gauge-fixed derivatives using the dependent connection are

```math
\begin{aligned}
D_\mu\psi_\nu^i
&=\left(\partial_\mu+\frac14\omega_\mu{}^{ab}(e,\psi,b)\gamma_{ab}\right)
  \psi_\nu^i
  -\frac12V_\mu\delta^{ij}\psi_{\nu j},\\
D'_\mu\lambda^i
&=\left(\partial_\mu+\frac14\omega_\mu{}^{ab}(e,\psi,b)\gamma_{ab}\right)
  \lambda^i
  +V_\mu^{\prime\,i}{}_j\lambda^j
  -\frac12V_\mu\delta^{ij}\lambda_j.
\end{aligned}
```

The torsion-free residual-$`U(1)_R`$-covariant derivative used in the bosonic truncation is

```math
\nabla_\mu^{(U(1))}\lambda^i
\equiv
\left(\partial_\mu+\frac14\omega_\mu{}^{ab}(e)\gamma_{ab}\right)
\lambda^i-\frac12V_\mu\delta^{ij}\lambda_j,
```

No exact equality is asserted because the dependent connection contains gravitino contorsion. Since the connection difference contains two fermions, fermion counting gives

```math
D_\mu\psi_\nu^i
=\nabla_\mu^{(U(1))}\psi_\nu^i+\mathcal O(\Psi^3),
\qquad
D'_\mu\lambda^i
=\nabla_\mu^{(U(1))}\lambda^i
 +V'_\mu{}^i{}_j\lambda^j+\mathcal O(\Psi^3).
```

The $`\mathcal O(\Psi^3)`$ terms vanish in the bosonic truncation. The second relation is used for the unconstrained linear-multiplet fermion $`\lambda^i=\varphi^i`$. No dynamical covariant derivative is defined for the dilatino $`\psi^i`$ set to zero by the gauge condition.

Ordinary, supercovariant, and torsionful objects remain distinct. In particular,

```math
\omega_{\pm\mu}{}^{ab}
\equiv\omega_\mu{}^{ab}(e,\psi,b)\pm H_\mu{}^{ab},
\qquad
H_\mu{}^{ab}\equiv e_\mu{}^cH_c{}^{ab},
```

are torsionful connections; $`H_\mu{}^{ab}`$ is the mixed component of the three-form $`H_{abc}`$. The quantities $`\widehat R`$, $`\widehat G`$, and $`\widehat H`$ denote hatted supercovariant completions. No independent $`\widehat\omega_\mu{}^{ab}`$ field is defined, and these objects are not identified with their ordinary counterparts merely because they share a base letter.

The sign conversion from the alternative frame to the project frame
acts throughout the multiplet as

```math
\boxed{
L_{ij}^{\mathrm{lower}}=-L_{ij},\qquad
\varphi_{\mathrm{lower}}^i=-\varphi^i,
\qquad
E_{\mathrm{lower}}^a=-E^a,
\qquad
N_{\mathrm{lower}}=-N,
\qquad
g_{\mathrm{lower}}=-g.}
```

This conversion is not applied piecemeal; in particular, simply replacing $`L=-1`$ with dynamical $`L`$ in a single formula from the old constant-$`L`$ gauge is invalid.

The normalization of the two Abelian gauge transformations is

```math
\delta_\lambda V_\mu=\partial_\mu\lambda,\qquad
\delta_\eta C_\mu=\partial_\mu\eta.
```

<a id="8-gauge-field-strength-normalizations"></a>

## Gauge field-strength normalizations

```math
\begin{aligned}
G_{\mu\nu}&=2\partial_{[\mu}C_{\nu]},\\
B_{\mu\nu\rho}&=3\partial_{[\mu}B_{\nu\rho]},\\
H_{\mu\nu\rho}
&=B_{\mu\nu\rho}
 +\frac32C_{[\mu}G_{\nu\rho]}
 +\frac12gE_{\mu\nu\rho}.
\end{aligned}
```

Thus, with $`g=0`$, the ungauged Dilaton–Weyl expression is

```math
H_{\mu\nu\rho}
=3\partial_{[\mu}B_{\nu\rho]}
 +\frac32C_{[\mu}G_{\nu\rho]}
```

Here $`B_{\mu\nu\rho}`$ denotes only the ordinary field strength of the potential $`B_{\mu\nu}`$, while $`H_{\mu\nu\rho}`$ denotes the three-form including Chern–Simons and gauging contributions.

The potential gauge transformations are

```math
\begin{aligned}
\delta E_{\mu\nu\rho}
&=3\partial_{[\mu}\Lambda_{\nu\rho]},\\
\delta B_{\mu\nu}
&=2\partial_{[\mu}\Lambda_{\nu]}
 -\frac12\eta G_{\mu\nu}
 -\frac12g\Lambda_{\mu\nu}.
\end{aligned}
```

Here $`\eta`$, $`\Lambda_\mu`$, and $`\Lambda_{\mu\nu}`$ are the gauge parameters of $`C_\mu`$, $`B_{\mu\nu}`$, and $`E_{\mu\nu\rho}`$, respectively.

Ungauged source-frame supercovariant field strengths

```math
\begin{aligned}
\widehat G_{\mu\nu}
&=G_{\mu\nu}
-\bar\psi_{[\mu}\gamma_{\nu]}\psi
+\frac{i}{2}\sigma\bar\psi_{[\mu}\psi_{\nu]},\\
\widehat H_{\mu\nu\rho}
&=H_{\mu\nu\rho}
-\frac34\sigma^2\bar\psi_{[\mu}\gamma_\nu\psi_{\rho]}
-\frac{3i}{2}\sigma
 \bar\psi_{[\mu}\gamma_{\nu\rho]}\psi.
\end{aligned}
```

Here the final spinor $`\psi^i`$ is the defining-vector dilatino, $`\psi_\mu^i`$ is the gravitino, and $`H_{\mu\nu\rho}`$ denotes the three-form $`g=0`$ defined above. These two formulas are valid only for the stated ungauged source frame; they are not identified with ordinary field strengths before fermion truncation and do not by themselves define the gauged target-gauge supercovariant completion.

<a id="9-weyl-weights-and-two-derivative-counting"></a>

## Weyl weights and two-derivative counting

Source superconformal Weyl weights are denoted by $`w_{\mathrm W}`$:

| Object | $`w_{\mathrm W}`$ |
|---|---:|
| $`e_\mu{}^a`$ | $`-1`$ |
| $`\psi_\mu^i`$ | $`-\frac12`$ |
| $`\sigma,T_{ab},\rho`$ | $`1`$ |
| $`\psi^i,\chi^i,\lambda_{\mathrm{src}}^i`$ | $`\frac32`$ |
| $`D_{\mathrm{aux}},Y^{ij},\widehat F_{ab}`$ | $`2`$ |
| $`L^{ij}`$ | $`3`$ |
| $`\varphi^i`$ | $`\frac72`$ |
| $`E_a,N`$ | $`4`$ |

Here $`\lambda_{\mathrm{src}}^i`$ is the specific fermion in the source multiplet; it is not identified with the generic dummy spinor $`\lambda^i`$ in Section 7. In particular, the source Weyl weight of the unconstrained linear-multiplet fermion $`\varphi^i`$ is $`7/2`$.

In particular, $`w_{\mathrm W}(\sigma)=1`$ before gauge fixing. These Weyl weights are not the derivative-counting degrees used after Poincaré gauge fixing.

The fermion-number expansion and transformation notation are defined by

```math
\mathscr L_{\mathrm{2-der}}
=\mathscr L_{\mathrm{2-der}}^{(0)}
+\mathscr L_{\mathrm{2-der}}^{(2)}
+\mathcal O(\Psi^4),
```

```math
\delta\Phi
=\delta^{(1)}\Phi+\mathcal O(\epsilon\Psi^3),
\qquad
\delta\Psi
=\delta^{(0)}\Psi+\mathcal O(\epsilon\Psi^2)
```

The superscript $`\mathscr L^{(n)}`$ counts dynamical fermions. Transformation superscripts also count dynamical fermions and exclude the Grassmann-odd parameter $`\epsilon^i`$.

The derivative-counting degree is denoted by $`\mathop{\mathrm{ord}}\nolimits_\partial`$:

```math
\mathop{\mathrm{ord}}\nolimits_\partial(L)=0,
\qquad
\mathop{\mathrm{ord}}\nolimits_\partial(\epsilon^i)=-\frac12,
\qquad
\mathop{\mathrm{ord}}\nolimits_\partial(\psi_\mu)
=\mathop{\mathrm{ord}}\nolimits_\partial(\varphi)=\frac12.
```

```math
\boxed{
\mathop{\mathrm{ord}}\nolimits_\partial(D_\mu)
=\mathop{\mathrm{ord}}\nolimits_\partial(G)
=\mathop{\mathrm{ord}}\nolimits_\partial(H)
=\mathop{\mathrm{ord}}\nolimits_\partial(E)
=\mathop{\mathrm{ord}}\nolimits_\partial(N)
=\mathop{\mathrm{ord}}\nolimits_\partial(V)
=\mathop{\mathrm{ord}}\nolimits_\partial(V')
=\mathop{\mathrm{ord}}\nolimits_\partial(g)=1.}
```

Moreover,

```math
\mathop{\mathrm{ord}}\nolimits_\partial(e_\mu{}^a)=0,
\qquad
\mathop{\mathrm{ord}}\nolimits_\partial(C_\mu)=0,
\qquad
\mathop{\mathrm{ord}}\nolimits_\partial(B_{\mu\nu})=0.
```

Thus a $`\Psi^2`$ monomial of derivative degree two contains one covariant derivative or one bosonic insertion of degree one. Since the unconstrained bosonic scalar of degree zero is $`L`$, unknown coefficients may remain general $`L`$-functions. The gauge-fixed $`\sigma=1`$ is not an independent argument of a coefficient function and has derivative-counting degree zero; this statement must not be confused with $`w_{\mathrm W}(\sigma)=1`$.

<a id="10-susy-commutator"></a>

## SUSY commutator

No independent project-wide SUSY commutator coefficient has been fixed. The coefficient $`\frac12\bar\epsilon_2\gamma^\mu\epsilon_1`$ is not used as closure input without being rederived from the relevant source and target-gauge transformation rules. At the time of this record, the full target-gauge transformations had not been supplied, so this normalization remained unspecified.

<a id="11-current-calculation-scope"></a>

## Current calculation scope

The following are scope rules for the project's current off-shell parent-action calculation, not mathematical conventions:

- The theory remains complete and off shell.
- No EOM are used.
- No auxiliary fields are eliminated.
- $`B_{\mu\nu}`$ is not dualized.
- No field redefinition is performed.
- No additional gauge choice, field truncation, or unspecified ansatz
  is applied beyond the selected conformal gauge.
- The free fields $`L`$ and $`\varphi^i`$ are neither fixed nor eliminated.
- Equalities are understood only modulo total derivatives, dummy-index
  relabeling, the spinor/Clifford identities recorded here, and identities
  following directly from stated field-strength definitions.

<a id="12-data-not-yet-supplied-for-the-new-gauge"></a>

## Source-frame and target-gauge distinction

- The ungauged source-frame definitions of $`\widehat G`$ and $`\widehat H`$ in Section 8 apply in their stated frame. The $`\sigma=1`$, $`\psi^i=0`$ target gauge uses its own gauge-preserving transformations and gauged supercovariant curvatures. Formulas specialized to $`L=-1`$, $`\varphi^i=0`$ have a different gauge domain and cannot be transferred by mechanical substitution.