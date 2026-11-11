# Total action in common conventions

<a id="1-fixed-inputs-and-scope"></a>

## Fixed inputs and scope

The action in this file is the sum of the following two **supplied component expressions**:

| Sector | Input | Expression used | Retained normalization |
|---|---|---|---|
| Two derivatives | [05_gauged_two_derivative_full_fermionic_action_from_1608_map.md](../../../common/two_derivative_action/details/construction.md) | (5.10); spinor inside the bar from (5.5) | $`-2`$ in the linear-map block, $`-4g`$ in the defining-vector block |
| $`R^2`$ | [BF_to_R2_canonical_action_through_two_fermions.md](construction.md) | (R2) | Unit BF density and overall $`\lambda_{R^2}`$ |
| Common conventions | [CONVENTIONS.md](../../../common/details/source_conventions.md) | §§3–9, 11 | Metric, NW–SE, curvature, derivative, and form definitions |

Original input-version SHA-256 hashes:

| File | SHA-256 |
|---|---|
| 05_gauged_two_derivative_full_fermionic_action_from_1608_map.md | `6a05742d1c2bb798fcb10b973fa6045165f4ff77a302f02f42b23c3a20b7d2fe` |
| BF_to_R2_canonical_action_through_two_fermions.md | `2b1a66ddadb24ec68e3062d186d9fb46f21a049087622310b70d171b3a009dea` |
| CONVENTIONS.md | `dddcde58009227f6ef0ca131f3d10c80fb98372775b4988bd6798be1791d10f3` |

The two-derivative hash identifies the [frozen 2016 source](../../../common/two_derivative_action/details/construction.md). The linked common construction also includes the lower-triplet correction (4.27a); the assembled action below already specifies that corrected derivative in (A.19). The [input correspondence](../../../references/fermionic_input_correspondence.md#lower-triplet-derivative) identifies the lower-triplet derivative used by these actions.

The common field space on which both actions are already defined is:

```math
\sigma=1,\qquad \psi^i=0,\qquad b_\mu=0,\qquad
L_{ij}=\frac{L}{\sqrt2}\delta_{ij},\qquad
L=\sqrt{L_{ij}L^{ij}}>0,\qquad g\ne0.
\tag{A.1}
```

Here $`\psi^i`$ is the defining dilatino, $`\psi_\mu{}^i`$ the gravitino, $`\varphi^i`$ the original linear-multiplet fermion, and $`\phi_\mu{}^i`$ the dependent $`S`$ connection. These four objects are distinct. The independent target fields remain

```math
e_\mu{}^a,\quad\psi_\mu{}^i,\quad C_\mu,\quad B_{\mu\nu},\quad
L,\quad\varphi^i,\quad E_{\mu\nu\rho},\quad N,\quad
V_\mu,\quad V_\mu^{\prime\,ij}
\tag{A.2}
```

Here $`E_a`$ is a component of the full supercovariant three-form definition below. No field equation is used for $`N,E_3,V,V'`$. This is the existing source gauge slice; the assembly introduces no new gauge condition or auxiliary-field elimination.

In the final action, $`\{\cdots\}_{\leq2}`$ selects physical fermion degrees zero and two of the **entire** expression, including fermions inside compact supercovariant objects. Bosonic dependence is not truncated. Since both inputs have this accuracy, the fixed object is $`S_{\mathrm{total}}^{\leq2}`$; the two files do not supply an action at all fermion orders. Arbitrarily chosen four-fermion completions of compact objects are excluded from this definition.

<a id="2-common-index-spinor-and-density-operations"></a>

## Common index, spinor, and density operations

```math
\begin{gathered}
\eta_{ab}=\mathop{\mathrm{diag}}\nolimits(-,+,+,+,+),\qquad
a,b,\mu,\nu=0,\ldots,4,\qquad i,j=1,2,\\
g_{\mu\nu}=e_\mu{}^ae_\nu{}^b\eta_{ab},\qquad
e=\det(e_\mu{}^a)=\sqrt{-g},\qquad X_a=e_a{}^\mu X_\mu,\\
X_{[ab]}=\frac12(X_{ab}-X_{ba}),\qquad
X_{(ij)}=\frac12(X_{ij}+X_{ji}),\\
\{\gamma^a,\gamma^b\}=2\eta^{ab},\qquad
\gamma^{a_1\cdots a_p}=\gamma^{[a_1}\cdots\gamma^{a_p]},\\
\gamma\!\cdot\!T=\gamma^{ab}T_{ab},\qquad
\not E=\gamma^aE_a,\qquad
\not{\mathcal D}=\gamma^a\mathcal D_a,\qquad T^2=T_{ab}T^{ab}.
\end{gathered}
\tag{A.3}
```

Dot contractions contain no additional $`1/p!`$. Denote the $`SU(2)`$ epsilon by $`\epsilon_{ij}`$, and the spacetime epsilon tensor by $`\varepsilon`$:

```math
\begin{gathered}
\epsilon_{12}=\epsilon^{12}=1,\qquad
X^i=\epsilon^{ij}X_j,\qquad X_i=X^j\epsilon_{ji},\\
L^{ij}=\epsilon^{ik}\epsilon^{j\ell}L_{k\ell},\qquad
L_i{}^j=\epsilon^{jk}L_{ik},\qquad
L^i{}_j=\epsilon^{ik}L_{kj},\\
\bar X\Gamma Y=\bar X^i\Gamma Y_i
=-\bar X_i\Gamma Y^i.
\end{gathered}
\tag{A.4}
```

Writing the source $`\varepsilon`$ symbols with two $`SU(2)`$ indices as $`\epsilon`$ changes notation only. The sign between the explicit-index and contracted flips follows directly from

```math
\begin{aligned}
\bar X^i\gamma_{(n)}Y^j&=t_n\bar Y^j\gamma_{(n)}X^i,
&t_0=t_1=t_4=t_5&=+1,\quad t_2=t_3=-1,\\
\bar X^i\gamma_{(n)}Y_i
&=\epsilon_{ji}\bar X^i\gamma_{(n)}Y^j
=t_n\epsilon_{ji}\bar Y^j\gamma_{(n)}X^i
=-t_n\bar Y^j\gamma_{(n)}X_j
\end{aligned}
\tag{A.5}
```

Both sources use a Majorana transpose-bar linear in coefficients. The file `CONVENTIONS.md` selects neither an explicit $`C`$ matrix nor a Dirac-bar phase; the sources' shared **operational** bar rule supplies the definition without choosing a matrix representation:

```math
\begin{aligned}
\overline{cX^i}&=c\bar X^i,\qquad
\overline{\gamma^{a_1\cdots a_n}X^i}
=t_n\bar X^i\gamma^{a_1\cdots a_n},\\
\overline{\gamma^a\gamma^{bc}X^i}
&=-\bar X^i\gamma^{bc}\gamma^a,\\
\overline{-2iL^{-1}\gamma^a\mathcal D_a\varphi_i}
&=-2iL^{-1}(\mathcal D_a\bar\varphi_i)\gamma^a,\\
\overline{4L^{-1}\gamma^{ab}T_{ab}\varphi_i}
&=-4L^{-1}\bar\varphi_i\gamma^{ab}T_{ab}.
\end{aligned}
\tag{A.6}
```

Here $`c`$ is an even scalar coefficient; in particular, $`i\mapsto-i`$ is not performed. Consistency with the flip is checked by writing $`C^T=-C`$ and $`\gamma_{(n)}^TC=t_nC\gamma_{(n)}`$:

```math
Y^TC\gamma_{(n)}X
=-X^T(C\gamma_{(n)})^TY
=X^T\gamma_{(n)}^TCY
=t_nX^TC\gamma_{(n)}Y.
\tag{A.7}
```

The first equality is Grassmann interchange. This algebraic check requires no choice of $`C`$ matrix.

Distinction between epsilon tensor and density symbol:

```math
\begin{gathered}
\varepsilon^{\mu\nu\rho\sigma\lambda}
=e_a{}^\mu e_b{}^\nu e_c{}^\rho e_d{}^\sigma e_f{}^\lambda
\varepsilon^{abcdf},\qquad
\epsilon^{\mu\nu\rho\sigma\lambda}
=e\,\varepsilon^{\mu\nu\rho\sigma\lambda},\\
\varepsilon_{a_1\cdots a_n b_1\cdots b_p}
\varepsilon^{a_1\cdots a_n c_1\cdots c_p}
=-n!p!\,\delta_{[b_1}^{c_1}\cdots\delta_{b_p]}^{c_p},\quad n+p=5,\\
\gamma^{abcde}=i\varepsilon^{abcde}\mathbf1,\qquad
\gamma^{a_1\cdots a_r}
=\frac{i}{(5-r)!}\varepsilon^{a_1\cdots a_5}
\gamma_{a_5\cdots a_{r+1}}.
\end{gathered}
\tag{A.8}
```

Instead of the numerical $`\varepsilon^{01234}=+1`$ choice in $`R^2`$, epsilon and gamma duality are kept symbolic together according to `CONVENTIONS.md`. No individual epsilon term is sign-flipped in isolation; no new numerical orientation or field rescaling is used.

<a id="3-common-forms-and-required-corrections"></a>

## Common forms and required corrections

```math
\begin{aligned}
G_{\mu\nu}&=2\partial_{[\mu}C_{\nu]},\\
H_{\mu\nu\rho}
&=3\partial_{[\mu}B_{\nu\rho]}+\frac32C_{[\mu}G_{\nu\rho]}
+\frac g2E_{\mu\nu\rho},\\
\widehat G_{\mu\nu}
&=G_{\mu\nu}+\frac i2\bar\psi_{[\mu}{}^i\psi_{\nu]i},\\
\widehat H_{\mu\nu\rho}
&=H_{\mu\nu\rho}-\frac34\bar\psi_{[\mu}{}^i\gamma_\nu\psi_{\rho]i}.
\end{aligned}
\tag{A.9}
```

The field $`H`$ is a three-form; $`H_\mu{}^{ab}=e^{a\nu}e^{b\rho}H_{\mu\nu\rho}`$ is not a two-form dual. With standard $`1/p!`$ component notation, the form relations are $`G=dC`$ and $`H=dB+\frac12C\wedge G+\frac g2E_3`$:

```math
\begin{aligned}
(C\wedge G)_{\mu\nu\rho}&=3C_{[\mu}G_{\nu\rho]},\\
\delta C&=d\Lambda,\qquad
\delta E_3=d\Lambda_2,\qquad
\delta B=d\Lambda_1-\frac12\Lambda G-\frac g2\Lambda_2,\\
\delta H
&=-\frac12d\Lambda\wedge G-\frac12\Lambda\,dG
-\frac g2d\Lambda_2+\frac12d\Lambda\wedge G+\frac g2d\Lambda_2=0,
\qquad dG=d^2C=0.
\end{aligned}
\tag{A.10}
```

Lines (3.5)–(3.10) of the first file use the same epsilon letter alternately for a tensor and a density symbol. In the total action, $`E^{\mu\nu}`$ is a **tensor**, and the consistent form of all these lines is

```math
\begin{aligned}
E^{\mu\nu}&=-\frac1{12}\varepsilon^{\mu\nu\rho\sigma\lambda}
E_{\rho\sigma\lambda},&
E_{\mu\nu\rho}&=\varepsilon_{\mu\nu\rho\sigma\lambda}E^{\sigma\lambda},\\
E^\mu&=-\frac1{12}\varepsilon^{\mu\nu\rho\sigma\lambda}
\mathcal D_\nu E_{\rho\sigma\lambda},&
E_\mu&=g_{\mu\nu}E^\nu,\\
E^a+\frac i2\bar\psi_b{}^i\gamma^{ba}\varphi_i
+\frac14\bar\psi_b{}^i\gamma^{abc}\psi_c{}^jL_{ij}
&=-\frac1{12}e_\mu{}^a\varepsilon^{\mu\nu\rho\sigma\lambda}
\partial_\nu E_{\rho\sigma\lambda}.&&
\end{aligned}
\tag{A.11}
```

This is the source three-form representation of the same linear-multiplet constraint $`\mathcal D_aE^a=0`$; neither $`E^{\mu\nu}`$ nor $`E_3`$ adds a new independent field.

Independent check of the inverse of the first equality:

```math
-\frac1{12}\varepsilon^{\mu\nu\rho\sigma\lambda}
\varepsilon_{\rho\sigma\lambda\alpha\beta}E^{\alpha\beta}
=\frac{3!2!}{12}\delta_{[\alpha}^{\mu}\delta_{\beta]}^{\nu}
E^{\alpha\beta}=E^{\mu\nu}.
\tag{A.12}
```

If the density symbol is chosen, write $`e^{-1}\epsilon^{\mu\nu\rho\sigma\lambda}`$ for every upper coordinate epsilon in (A.11). For the lower symbol use $`\varepsilon_{\mu\nu\rho\sigma\lambda} =e\epsilon_{\mu\nu\rho\sigma\lambda}`$; symbol indices are not raised with the metric as tensor indices are. Thus $`e`$ in (3.6) of the first source is correct only when the lower epsilon is a **symbol**.

The bare $`\partial_\nu E^{\mu\nu}`$ in (3.8) of the first source must be read, for tensor $`E^{\mu\nu}`$, as the following determinant-containing expression:

```math
\begin{aligned}
P^\mu&:=E^\mu+\frac i2\bar\psi_\nu{}^i\gamma^{\nu\mu}\varphi_i
+\frac14\bar\psi_\nu{}^i\gamma^{\mu\nu\rho}\psi_\rho{}^jL_{ij},\\
\frac1e\partial_\nu(eE^{\mu\nu})
&=-\frac1{12e}\partial_\nu
\bigl(e\varepsilon^{\mu\nu\rho\sigma\lambda}E_{\rho\sigma\lambda}\bigr)
=-\frac1{12}\varepsilon^{\mu\nu\rho\sigma\lambda}
\partial_\nu E_{\rho\sigma\lambda}=P^\mu,\\
E^\mu
&=\frac1e\partial_\nu(eE^{\mu\nu})
+\frac i2\bar\psi_\nu{}^i\gamma^{\mu\nu}\varphi_i
+\frac14\bar\psi_\rho{}^i\gamma^{\mu\nu\rho}\psi_\nu{}^jL_{ij}.
\end{aligned}
\tag{A.13}
```

Here $`P^\mu`$ is only a temporary abbreviation in this conversion. The density identity $`\partial_\nu(e\varepsilon^{\mu\nu\rho\sigma\lambda})=0`$ is used; $`\mathcal D E_3`$ and $`\partial E_3`$ are not identified. This full form conversion agrees with (B.7) of the second file.

<a id="4-common-connections-curvatures-and-covariant-derivatives"></a>

## Common connections, curvatures, and covariant derivatives

```math
\begin{aligned}
\omega_\mu{}^{ab}
={}&2e^{\nu[a}\partial_{[\mu}e_{\nu]}{}^{b]}
-e^{\nu[a}e^{b]\rho}e_{\mu c}\partial_\nu e_\rho{}^c
+\frac12\bar\psi^{[a}\gamma^{b]}\psi_\mu
+\frac14\bar\psi^a\gamma_\mu\psi^b,\\
V_\mu^{ij}&=V_\mu^{\prime\,ij}+\frac12\delta^{ij}V_\mu,
\qquad\delta_{ij}V_\mu^{\prime\,ij}=0,\\
\widehat R'_{\mu\nu}{}^i(Q)
={}&2\partial_{[\mu}\psi_{\nu]}{}^i
+\frac12\omega_{[\mu}{}^{ab}\gamma_{ab}\psi_{\nu]}{}^i
-2V_{[\mu}^{ij}\psi_{\nu]j}
+2i\gamma\!\cdot\!T\gamma_{[\mu}\psi_{\nu]}{}^i,\\
\phi_\mu{}^i
={}&\frac i3\gamma^a\widehat R'_{\mu a}{}^i(Q)
-\frac i{24}\gamma_\mu\gamma^{ab}\widehat R'_{ab}{}^i(Q),\\
\widehat R_{\mu\nu}{}^i(Q)
={}&\widehat R'_{\mu\nu}{}^i(Q)-2i\gamma_{[\mu}\phi_{\nu]}{}^i,\\
\widehat R_{\mu\nu}{}^{ij}(V)
={}&2\partial_{[\mu}V_{\nu]}^{ij}
-2V_{[\mu}^{k(i}V_{\nu]k}{}^{j)}
-3i\bar\phi_{[\mu}^{(i}\psi_{\nu]}^{j)}
-8\bar\psi_{[\mu}^{(i}\gamma_{\nu]}\chi^{j)}
-i\bar\psi_{[\mu}^{(i}\gamma\!\cdot\!T\psi_{\nu]}^{j)}.
\end{aligned}
\tag{A.14}
```

Here $`\psi^a=e^{a\mu}\psi_\mu`$; (A.14) uses only the already fixed $`b_\mu=0`$. Gravitino contorsion is retained. The prime in $`V'`$ denotes the traceless connection, while that in $`\widehat R'(Q)`$ denotes removal of the $`\phi`$ contribution; neither is the composite-vector prime.

```math
\begin{aligned}
R_{\mu\nu}{}^{ab}(\omega)
&=2\partial_{[\mu}\omega_{\nu]}{}^{ab}
+2\omega_{[\mu}{}^{ac}\omega_{\nu]c}{}^b,\\
\widehat R'_{\mu\nu}{}^{ab}(M)
&=R_{\mu\nu}{}^{ab}(\omega)
+i\bar\phi_{[\mu}\gamma^{ab}\psi_{\nu]}
+i\bar\psi_{[\mu}\gamma^{[a}\gamma\!\cdot\!T\gamma^{b]}\psi_{\nu]}\\
&\quad+\bar\psi_{[\mu}\gamma^{[a}\widehat R_{\nu]}{}^{b]}(Q)
+\frac12\bar\psi_{[\mu}\gamma_{\nu]}\widehat R^{ab}(Q)
+8\bar\psi_{[\mu}e_{\nu]}{}^{[a}\gamma^{b]}\chi,\\
\mathcal R_\mu{}^a
&:=\widehat R'_{\mu\nu}{}^{ab}(M)e_b{}^\nu,
\qquad \mathcal R:=e_a{}^\mu\mathcal R_\mu{}^a,\\
f_\mu{}^a&=-\frac16\mathcal R_\mu{}^a+\frac1{48}e_\mu{}^a\mathcal R,
\qquad
\widehat R_{\mu\nu}{}^{ab}(M)
=\widehat R'_{\mu\nu}{}^{ab}(M)+8f_{[\mu}{}^{[a}e_{\nu]}{}^{b]}.
\end{aligned}
\tag{A.15}
```

Here $`\mathcal R`$ is defined notation preventing confusion with ordinary $`R(\omega)`$, not a new field. Ordinary contractions are $`R_{bd}(\omega)=\eta^{ac}R_{abcd}(\omega)`$ and $`R(\omega)=\eta^{bd}R_{bd}(\omega)`$. Comparison with the $`R^\rho{}_{\sigma\mu\nu}`$ convention of the second source also tracks Ricci index order for the common connection. In this calculation, $`R^{\rm aff}_{\mu\nu}:=R^\rho{}_{\mu\rho\nu}`$ denotes the affine Ricci contraction of the second source:

```math
\begin{aligned}
R^\rho{}_{\sigma\mu\nu}
&=e_a{}^\rho e_{\sigma b}R_{\mu\nu}{}^{ab}(\omega),\\
e_b{}^\mu e_d{}^\nu R^\rho{}_{\mu\rho\nu}
&=\eta^{ac}R_{adcb}(\omega)=R_{db}(\omega),\\
R^{\rm aff}_{bd}&=R_{db}(\omega),\qquad
\eta^{bd}R^{\rm aff}_{bd}
=\eta^{bd}R_{db}(\omega)=R(\omega)
\end{aligned}
\tag{A.16}
```

as checked here. Ricci symmetry is not assumed with torsion: converting the affine contraction to the project contraction interchanges the Ricci indices. The scalar requires no $`R\mapsto-R`$ conversion. The total action does not separately use affine Ricci; $`f`$ is always computed from (A.15). The supercovariant $`\mathcal R`$ in (A.15) is not replaced by an ordinary scalar when fermions are present.

Both inputs use the sign $`+8`$. Its effect on the trace and $`f`$ is:

```math
\begin{aligned}
\mathcal R\big|_{\bar\psi\chi}
&=8\frac{1-5-5+1}{4}\bar\psi_a\gamma^a\chi
=-16\bar\psi_a\gamma^a\chi,\\
f_a{}^a&=\left(-\frac16+\frac5{48}\right)\mathcal R
=-\frac1{16}\mathcal R,
\qquad f_a{}^a\big|_{\bar\psi\chi}=+\bar\psi_a\gamma^a\chi,\\
\widehat R_{ab}{}^{cb}(M)
&=\mathcal R_a{}^c+6f_a{}^c+2\delta_a{}^cf_b{}^b\\
&=\mathcal R_a{}^c-\mathcal R_a{}^c
+\left(\frac18-\frac18\right)\delta_a{}^c\mathcal R=0.
\end{aligned}
\tag{A.17}
```

A separate source monomial $`i\bar\psi_{[\mu}\gamma^{ab}\psi_{\nu]}`$ vanishes by (A.5):
$`\bar\psi_\mu\gamma^{ab}\psi_\nu=-t_2\bar\psi_\nu\gamma^{ab}\psi_\mu =\bar\psi_\nu\gamma^{ab}\psi_\mu`$.

All $`\mathcal D`$ denote full source supercovariant derivatives. The connection part is

```math
\left(\partial_\mu-wb_\mu+\frac14\omega_\mu{}^{ab}\gamma_{ab}\right)X^i
-V_\mu^{ij}X_j
\tag{A.18}
```

and is not the full derivative by itself. The definitions are $`w(\chi)=3/2`$, $`w(\varphi)=7/2`$, $`w(L_{ij})=3`$, $`w(\rho')=1`$. The common working definitions are:

```math
\begin{aligned}
\mathcal D_\mu L_{ij}\big|_{\rm P}
&=\frac{\delta_{ij}}{\sqrt2}\partial_\mu L
-\sqrt2L V'_{\mu(i}{}^k\delta_{j)k}
-i\bar\psi_{\mu(i}\varphi_{j)},\\
\mathcal D_\mu\varphi_i\big|_{\rm P}
&=\left(\partial_\mu+\frac14\omega_\mu{}^{ab}\gamma_{ab}\right)\varphi_i
-V_{\mu i}{}^j\varphi_j
-\frac i2\gamma^a\mathcal D_aL_{ij}\,\psi_\mu{}^j\\
&\quad+\frac i2\not E\psi_{\mu i}-\frac12N\psi_{\mu i}
-L_{ij}\gamma\!\cdot\!T\psi_\mu{}^j+3L_{ij}\phi_\mu{}^j,\\
\mathcal D_\mu T_{ab}\big|_{\rm P}
&=\partial_\mu T_{ab}+2\omega_\mu{}^c{}_{[a}T_{b]c}
-\frac i2\bar\psi_\mu\gamma_{ab}\chi
+\frac{3i}{32}\bar\psi_\mu\widehat R_{ab}(Q).
\end{aligned}
\tag{A.19}
```

The connection action on a lower Lorentz index fixes the sign of the $`T`$ derivative:

```math
\begin{aligned}
\partial_\mu T_{ab}-\omega_\mu{}^c{}_aT_{cb}
-\omega_\mu{}^c{}_bT_{ac}
&=\partial_\mu T_{ab}+\omega_\mu{}^c{}_aT_{bc}
-\omega_\mu{}^c{}_bT_{ac}\\
&=\partial_\mu T_{ab}+2\omega_\mu{}^c{}_{[a}T_{b]c}.
\end{aligned}
\tag{A.20}
```

A derivative with the opposite sign in the same index order would require the difference $`+4\omega_\mu{}^c{}_{[a}T_{b]c}`$. Since the supplied actions leave $`\mathcal D T`$ compact, (A.19) specifies its definition here; no overall sign is applied to coefficients.

The first source's $`\square^C,\square^c`$ and the second source's $`\Box_c`$ are written as $`\Box_c`$ in the total action. The argument's multiplet representation is retained. The weight-three triplet box acting on $`L_{ij}`$ and weight-one vector-scalar box acting on $`\rho'`$ are not the same ordinary scalar Laplacian. In particular, the contraction explicitly given in the first source is:

```math
\boxed{
\begin{aligned}
L_{ij}\Box_cL^{ij}\big|_{\mathrm P}
={}&\frac{L}{\sqrt2}\delta_{ij}
(\partial^a+\omega_b{}^{ba})
\mathcal D_aL^{ij}\big|_{\mathrm P}\\
&+\sqrt2L\,\delta_{ij}V_a{}^i{}_k
\mathcal D^aL^{jk}\big|_{\mathrm P}
+6L^2f_a{}^a\\
&-\frac{iL}{\sqrt2}\delta_{ij}
\bar\psi^{ai}\mathcal D_a\varphi^j\big|_{\mathrm P}
-6L^2\bar\psi_a{}^i\gamma^a\chi_i\big|_{\mathrm P}\\
&-\frac{L}{8\sqrt2}\delta_{ij}
\bar\varphi^i\gamma^{bc}
\left(
\widehat G_{bc}
+\frac16\varepsilon_{bcdef}\widehat H^{def}
\right)\gamma^a\psi_a{}^j\\
&+\frac{L}{\sqrt2}\delta_{ij}
\bar\varphi^i\gamma^a\phi_a{}^j.
\end{aligned}
}
\tag{K.L}
```

For a vector multiplet, substituting its components for $`(\rho,\lambda,Y,\widehat F)`$, use

```math
\begin{aligned}
\widehat F_{\mu\nu}&=2\partial_{[\mu}A_{\nu]}-\bar\psi_{[\mu}\gamma_{\nu]}\lambda
+\frac i2\rho\bar\psi_{[\mu}\psi_{\nu]},\\
\mathcal D_\mu\rho&=(\partial_\mu-b_\mu)\rho-\frac i2\bar\psi_\mu\lambda,\\
\mathcal D_\mu\lambda^i&=(\partial_\mu-\tfrac32b_\mu)\lambda^i
+\frac14\omega_\mu{}^{ab}\gamma_{ab}\lambda^i-V_\mu{}^{ij}\lambda_j
+\frac14\gamma\!\cdot\!\widehat F\psi_\mu^i\\
&\quad+\frac i2(\not{\mathcal D}\rho)\psi_\mu^i+Y^{ij}\psi_{\mu j}
-\rho\gamma\!\cdot\!T\psi_\mu^i-\rho\phi_\mu^i,\\
\Box_c\rho&=(\partial^a-2b^a+\omega_b{}^{ba})\mathcal D_a\rho
-\frac i2\bar\psi_a\mathcal D^a\lambda-2\rho\bar\psi_a\gamma^a\chi\\
&\quad+\frac12\bar\psi_a\gamma^a\gamma\!\cdot\!T\lambda
+\frac12\bar\phi_a\gamma^a\lambda+2f_a{}^a\rho.
\end{aligned}
\tag{K.V}
```

This definition contains $`Y'`$ and $`\lambda'`$ for $`\rho'`$; the defining vector's values $`Y=-gL/2`$, $`\psi^i=0`$ are not imposed on the primed multiplet. Other compact derivatives retain the same supercovariant representation meaning. This file does not derive a new independent derivative or SUSY system expanding every compact source derivative into ordinary components.

<a id="5-matching-gauged-composites"></a>

## Matching gauged composites

For the reversed three-form index order in (D.1) of the second source, $`\widehat H^{edc}=-\widehat H^{cde}`$, so

```math
\begin{aligned}
-\frac16\varepsilon_{abcde}\widehat H^{edc}
&=\frac16\varepsilon_{abcde}\widehat H^{cde}
=8T_{ab}-\widehat G_{ab},\\
T_{ab}&=\frac18\left(\widehat G_{ab}
+\frac16\varepsilon_{abcde}\widehat H^{cde}\right).
\end{aligned}
\tag{A.21}
```

This agrees with (4.18) of the first source; no extra factor of two or six is needed in the $`H`$ normalization.

The **derivative** of the fixed dilatino is obtained by applying the vector derivative definition before restricting to the gauge slice:

```math
\begin{aligned}
\mathcal D_\mu\psi^i\big|_{\rm P}
&=\left(\frac14\gamma\!\cdot\!\widehat G-\gamma\!\cdot\!T\right)
\psi_\mu{}^i-\frac g2L^{ij}\psi_{\mu j}-\phi_\mu{}^i,\\
L^{kj}\psi_{\mu j}\epsilon_{ki}
&=\epsilon^{km}\epsilon^{jn}L_{mn}\psi_\mu{}^\ell
\epsilon_{\ell j}\epsilon_{ki}=-L_{ij}\psi_\mu{}^j,\\
\mathcal D_\mu\psi_i\big|_{\rm P}
&=\left(\frac14\gamma\!\cdot\!\widehat G-\gamma\!\cdot\!T\right)
\psi_{\mu i}+\frac g2L_{ij}\psi_\mu{}^j-\phi_{\mu i},\\
\mathcal D_\mu\sigma\big|_{\rm P}&=0,\\
\Box_c\sigma\big|_{\rm P}
&=2f_a{}^a-\frac i2\bar\psi_a{}^i\mathcal D^a\psi_i\big|_{\rm P}
-2\bar\psi_a{}^i\gamma^a\chi_i.
\end{aligned}
\tag{A.22}
```

The composites common to both sources, at the degrees required by the action, are:

```math
\begin{aligned}
\chi^i\big|_{\rm P}
&=\frac i8\gamma^a\mathcal D_a\psi^i\big|_{\rm P}
+\frac g8\varphi^i+O(\mathrm{fermion}^3),\\
D\big|_{\rm P}
&=\frac12f_a{}^a-\frac1{16}\widehat G_{ab}\widehat G^{ab}
-\frac{26}{3}T_{ab}T^{ab}+2\widehat G^{ab}T_{ab}
+\frac g4N+\frac{g^2}{16}L^2\\
&\quad-\frac i8\bar\psi_a{}^i\mathcal D^a\psi_i\big|_{\rm P}
-\frac12\bar\psi_a{}^i\gamma^a\chi_i
+O(\mathrm{fermion}^4).
\end{aligned}
\tag{A.23}
```

Matching the ordinary $`G`$ expression of the second source to the first:

```math
\begin{aligned}
\widehat G_{ab}\widehat G^{ab}
&=\left(G_{ab}+\frac i2\bar\psi_{[a}\psi_{b]}\right)
\left(G^{ab}+\frac i2\bar\psi^{[a}\psi^{b]}\right)\\
&=G_{ab}G^{ab}+iG^{ab}\bar\psi_a\psi_b
+O(\mathrm{fermion}^4),\\
-\frac1{16}G^2-\frac i{16}G^{ab}\bar\psi_a\psi_b
&=-\frac1{16}\widehat G^2+O(\mathrm{fermion}^4).
\end{aligned}
\tag{A.24}
```

Substituting (A.21) and (A.22) into (A.23) gives the coefficients of (4.24) separately as

```math
\begin{aligned}
-\frac{26}{3}T^2
&=-\frac{26}{3\cdot64}
\left(\widehat G_{ab}+\frac16\varepsilon_{abcde}\widehat H^{cde}\right)
\left(\widehat G^{ab}+\frac16\varepsilon^{abfgh}\widehat H_{fgh}\right)\\
&=-\frac{13}{96}
\left(\widehat G_{ab}+\frac16\varepsilon_{abcde}\widehat H^{cde}\right)
\left(\widehat G^{ab}+\frac16\varepsilon^{abfgh}\widehat H_{fgh}\right),\\
2\widehat G^{ab}T_{ab}
&=\frac14\widehat G^{ab}
\left(\widehat G_{ab}+\frac16\varepsilon_{abcde}\widehat H^{cde}\right),\\
-\frac12\bar\psi_a\gamma^a\chi
&=-\frac i{16}\bar\psi_a\gamma^a\gamma^\mu
\mathcal D_\mu\psi\big|_{\rm P}
-\frac g{16}\bar\psi_a\gamma^a\varphi+O(\mathrm{fermion}^4),\\
\frac14Y^{ij}Y_{ij}\big|_{\rm P}
&=\frac14\left(-\frac g2\right)^2L^{ij}L_{ij}
=\frac{g^2}{16}L^2
\end{aligned}
\tag{A.25}
```

Thus the same $`T,\chi,D,f`$ are used in both sectors; they are not counted as a second independent Weyl multiplet.

<a id="6-common-linear-map-and-normalization-check"></a>

## Common linear map and normalization check

Matching the vector labels of the sources:

```math
\begin{aligned}
(\rho',\lambda'_i,Y'_{ij},\widehat F'_{\mu\nu})_{R^2}
&=(\rho_{\rm linear},\lambda_{{\rm linear}\,i},
Y_{{\rm linear}\,ij},\widehat F_{{\rm linear}\,\mu\nu})_{2\partial},\\
(\rho,\lambda^i,Y^{ij},A_\mu,\widehat F_{\mu\nu})_{R^2}
&=(\sigma,\psi^i,Y^{ij},C_\mu,\widehat G_{\mu\nu}),\\
\rho_{\rm eff}&=\rho'+2g,\qquad
\lambda_{{\rm eff}\,i}=\lambda'_i,\qquad
Y_{{\rm eff}\,ij}=Y'_{ij}-g^2L_{ij}.
\end{aligned}
\tag{A.26}
```

Thus the primed vector of the $`R^2`$ source is the **linear composite** of the two-derivative source, not its effective vector with $`2g`$ added. The $`Y`$ in the second equality belongs to the defining vector; the replacement $`Y'=-gL/2`$ is not made.

The common map of both sources, preserving source order, is:

```math
\rho'=\left[\begin{aligned}
&2L^{-1}N\\
&+iL^{-3}L_{ij}\bar\varphi^i\varphi^j
\end{aligned}\right]
\tag{M.1}
```

```math
\lambda'_i=\left[\begin{aligned}
&-2iL^{-1}\not{\mathcal D}\varphi_i\\
&+16L^{-1}L_{ij}\chi^j\\
&+4L^{-1}\gamma\!\cdot\!T\varphi_i\\
&-2NL^{-3}L_{ij}\varphi^j\\
&+2iL^{-3}(\not{\mathcal D}L_{ij})L^{jk}\varphi_k\\
&-2iL^{-3}\not E L_{ij}\varphi^j
\end{aligned}\right]+O_{\rm explicit}(\mathrm{fermion}^3)
\tag{M.2}
```

```math
Y'_{ij}=\left[\begin{aligned}
&L^{-1}\Box_c L_{ij}\\
&-L^{-3}L^{km}\mathcal D_aL_{k(i}\mathcal D^aL_{j)m}\\
&-L^{-3}L_{ij}N^2\\
&-L^{-3}L_{ij}E_aE^a\\
&+2L^{-3}E_aL_{k(i}\mathcal D^aL_{j)}{}^k\\
&+\frac83L^{-1}L_{ij}T^2\\
&+4L^{-1}L_{ij}D\\
&+iNL^{-3}\bar\varphi_{(i}\varphi_{j)}\\
&-3iNL^{-5}L_{ij}L^{kl}\bar\varphi_k\varphi_l\\
&+3L^{-5}L_{ij}L^{kl}\bar\varphi_k\not E\varphi_l\\
&-L^{-3}\bar\varphi_{(i}\not E\varphi_{j)}\\
&-16iL^{-1}\bar\chi_{(i}\varphi_{j)}\\
&+16iL^{-3}L_{ij}L_{kl}\bar\chi^k\varphi^l\\
&+2L^{-3}L_{k(i}\bar\varphi^k\not{\mathcal D}\varphi_{j)}\\
&-3L^{-5}L_{k(i}L^{lm}\bar\varphi^k(\not{\mathcal D}L_{j)l})\varphi_m\\
&+\frac12L^{-3}\bar\varphi^l(\not{\mathcal D}L_{l(i})\varphi_{j)}\\
&+\frac12L^{-3}\bar\varphi^m(\not{\mathcal D}L_{ij})\varphi_m\\
&+2iL^{-3}L_{ij}\bar\varphi\gamma\!\cdot\!T\varphi
\end{aligned}\right]+O_{\rm explicit}(\mathrm{fermion}^4)
\tag{M.3}
```

```math
\widehat F'_{\mu\nu}=\left[\begin{aligned}
&4\mathcal D_{[\mu}(L^{-1}E_{\nu]})\\
&+2L^{-1}\widehat R_{\mu\nu}^{ij}(V)L_{ij}\\
&-2L^{-3}L_k{}^l\mathcal D_{[\mu}L^{kp}\mathcal D_{\nu]}L_{lp}\\
&-2\mathcal D_{[\mu}(L^{-3}L_{ij}\bar\varphi^i\gamma_{\nu]}\varphi^j)\\
&-iL^{-1}\bar\varphi^i\widehat R_{\mu\nu i}(Q)
\end{aligned}\right]
\tag{M.4}
```

The ordered coefficients of these four equalities agree between (4.33)–(4.37) of the first file and (SC1)–(SC4) of the second:

```math
\begin{aligned}
\rho':&\quad (2,i),\\
\lambda'_i:&\quad(-2i,16,4,-2,2i,-2i),\\
Y'_{ij}:&\quad
(1,-1,-1,-1,2,\tfrac83,4,i,-3i,3,-1,-16i,16i,2,-3,\tfrac12,\tfrac12,2i),\\
\widehat F':&\quad(4,2,-2,-2,-i).
\end{aligned}
\tag{A.27}
```

These number lists specify the monomial ordering above, not new independent parameters. Gauge evaluation of the coefficients can be followed directly, for example, through

```math
\begin{aligned}
iL^{-3}L_{ij}\bar\varphi^i\varphi^j
&=\frac{i}{\sqrt2L^2}\delta_{ij}\bar\varphi^i\varphi^j,\\
16L^{-1}L_{ij}\chi^j
&=8\sqrt2\delta_{ij}
\left(\frac i8\gamma^\mu\mathcal D_\mu\psi^j+\frac g8\varphi^j\right)+O(\mathrm{fermion}^3)\\
&=i\sqrt2\delta_{ij}\gamma^\mu\mathcal D_\mu\psi^j
+\sqrt2g\delta_{ij}\varphi^j+O(\mathrm{fermion}^3),\\
-3iNL^{-5}L_{ij}L^{kl}
&=-\frac{3iN}{2L^3}\delta_{ij}\delta^{kl},\\
16iL^{-3}L_{ij}L_{kl}&=\frac{8i}{L}\delta_{ij}\delta_{kl},\\
-3L^{-5}L_{k(i}L^{lm}&=-\frac{3}{2L^3}\delta_{k(i}\delta^{lm},\\
L_k{}^\ell&=\epsilon^{\ell m}\frac{L}{\sqrt2}\delta_{km}
=-\frac{L}{\sqrt2}\delta_{km}\epsilon^{m\ell},\\
-2L^{-3}L_k{}^\ell
&=\frac{\sqrt2}{L^2}\delta_{km}\epsilon^{m\ell}
\end{aligned}
\tag{A.28}
```

For $`\mathcal D L_{ij}`$, this substitution means (A.19); applying $`\mathcal D L_{ij}=\delta_{ij}\partial L/\sqrt2`$ is incorrect.

The triplet-derivative identity used in the second file's assembly follows the same NW–SE definition. For temporary symmetric $`2\times2`$ matrices $`S=(L_{ij})`$, $`P=(\mathcal D_aL_{ij})`$,

```math
\begin{gathered}
S=\begin{pmatrix}u&v\\v&w\end{pmatrix},\qquad
P=\begin{pmatrix}p&q\\q&r\end{pmatrix},\qquad
\mathop{\mathrm{adj}}\nolimits S=\begin{pmatrix}w&-v\\-v&u\end{pmatrix},\\
2L\mathcal D_aL=(\mathcal D_aL_{ij})L^{ij}+L_{ij}\mathcal D_aL^{ij}
=2L^{ij}\mathcal D_aL_{ij},\\
P\mathop{\mathrm{adj}}\nolimits S P
=\begin{pmatrix}
wp^2-2vpq+uq^2 & wpq-v(pr+q^2)+uqr\\
wpq-v(pr+q^2)+uqr & wq^2-2vqr+ur^2
\end{pmatrix}\\
=\mathop{\mathrm{tr}}\nolimits(\mathop{\mathrm{adj}}\nolimits S P)P-\det(P)S,\\
L^2=2\det S,\qquad
\mathop{\mathrm{tr}}\nolimits(\mathop{\mathrm{adj}}\nolimits S P)=L\mathcal D_aL,
\qquad 2\det P=\mathcal D_aL_{ij}\mathcal D_aL^{ij}
\quad\text{(fixed $a$ in these last two expressions)},\\
-L^{-3}L^{km}\mathcal D_aL_{k(i}\mathcal D^aL_{j)m}
=-L^{-2}(\mathcal D_aL)\mathcal D^aL_{ij}
+\frac{L_{ij}}{2L^3}\mathcal D_aL_{kl}\mathcal D^aL^{kl}.
\end{gathered}
\tag{A.29}
```

The Lorentz index in the final line is contracted with the metric. This shows that the different appearance of derivative squares in $`R^2`$ does not represent a field redefinition.

The independent normalization check selects only the coefficient of the relevant monomial, without imposing background conditions on fields:

```math
\begin{aligned}
f_a{}^a\big|_R&=-\frac{R}{16},\qquad
D\big|_R=\frac12\left(-\frac R{16}\right)=-\frac R{32},\\
\Box_cL_{ij}\big|_R&=6\left(-\frac R{16}\right)L_{ij}
=-\frac{3R}{8}L_{ij},\\
Y'_{ij}\big|_R
&=\frac1L\left(-\frac{3R}{8}L_{ij}\right)
+\frac4L L_{ij}\left(-\frac R{32}\right)
=-\frac R{2L}L_{ij},\\
\left(-2Y'^{ij}L_{ij}\right)\big|_R
&=-2\left(-\frac R{2L}\right)L^{ij}L_{ij}=LR,\\
\left(Y'^{ij}Y'_{ij}\right)\big|_{R^2}
&=\frac{R^2}{4L^2}L^{ij}L_{ij}=\frac14R^2.
\end{aligned}
\tag{A.30}
```

Thus the $`LR`$ and $`\lambda_{R^2}R^2/4`$ normalizations are preserved in the total action. No factor $`-2`$, $`2`$, or $`4`$ multiplies the $`R^2`$ sector. The parameter $`\lambda_{R^2}`$ is the same free coefficient as in the second file; no numerical value is fixed. No new $`\kappa`$ or common action prefactor is introduced.

The post-gauge engineering dimensions of the sources also give

```math
[L]=0,\quad [N]=[E_a]=[g]=[T]=[\widehat G]=1,\quad
[\psi_a]=[\varphi]=\tfrac12,\quad [Y']=2,
```

```math
[-2Y'^{ij}L_{ij}]=2,\qquad [Y'^{ij}Y'_{ij}]=4,\qquad
[\lambda_{R^2}]=-2,\qquad
[\lambda_{R^2}Y'^{ij}Y'_{ij}]=2.
\tag{A.30b}
```

These are not the pre-gauge Weyl weights of (A.18); for example, $`[L]=0`$ and $`w(L)=3`$ are not interchangeable.

<a id="7-explicit-distinction-between-boundary-representatives"></a>

## Explicit distinction between boundary representatives

the total action retains **the field-strength representative (5.10) itself** from the first file. The boundary difference computed in (A.32) is neither added to the total action nor assumed zero. The second sector's (R2) expression retains its own local BF representative unchanged. The boundary representative of the sum below is thus fixed; no unconditional equality of potential and field-strength representatives is asserted.

In this paragraph, $`A_\mu`$ is any even vector potential inserted into the density; $`F_{\mu\nu}=2\partial_{[\mu}A_{\nu]}`$. Using (A.11),

```math
\begin{aligned}
e\left(-\frac1{12}\varepsilon^{\mu\nu\rho\sigma\lambda}
A_\mu\partial_\nu E_{\rho\sigma\lambda}\right)
&=A_\mu\partial_\nu(eE^{\mu\nu})\\
&=\partial_\nu(eA_\mu E^{\mu\nu})
-e(\partial_\nu A_\mu)E^{\mu\nu}\\
&=\frac e2F_{\mu\nu}E^{\mu\nu}
-\frac1{12}\partial_\nu
\left(e\varepsilon^{\mu\nu\rho\sigma\lambda}
A_\mu E_{\rho\sigma\lambda}\right).
\end{aligned}
\tag{A.31}
```

Substituting the first sector's factor $`-2`$ and $`A_{{\rm eff}\,\mu}=A'_\mu+2gC_\mu`$ yields

```math
S_{2\partial}^{\rm pot}-S_{2\partial}^{F}
=\frac16\int_{\partial M}d\Sigma_\nu\,
e\varepsilon^{\mu\nu\rho\sigma\lambda}
(A'_\mu+2gC_\mu)E_{\rho\sigma\lambda}.
\tag{A.32}
```

The local composite potential in this equality is (SC5) of the second input:

```math
A'_\mu=\frac2L E_\mu+\sqrt2V_\mu
-\frac1{L^3}L_{ij}\bar\varphi^i\gamma_\mu\varphi^j
-\frac iL\bar\varphi^i\psi_{\mu i}.
\tag{A.33}
```

The sign and gauging cancellation when removing the field-strength hat are also checked by

```math
\begin{aligned}
F_{{\rm eff}\,\mu\nu}
&=\widehat F'_{\mu\nu}+2g\widehat G_{\mu\nu}
+\bar\psi_{[\mu}\gamma_{\nu]}\lambda'
-\frac i2(\rho'+2g)\bar\psi_{[\mu}\psi_{\nu]}\\
&=\widehat F'_{\mu\nu}+\bar\psi_{[\mu}\gamma_{\nu]}\lambda'
-\frac i2\rho'\bar\psi_{[\mu}\psi_{\nu]}
+2gG_{\mu\nu}
+(ig-ig)\bar\psi_{[\mu}\psi_{\nu]}\\
&=F'_{\mu\nu}+2gG_{\mu\nu}
\end{aligned}
\tag{A.34}
```

Thus the field strength multiplying $`E^{\mu\nu}`$ in the first sector is ordinary; $`\widehat F'`$ and $`\widehat G`$ inside $`R^2`$ retain their hatted definitions.

**Fermionic omission in line (5.11) of the first source:** (A.13) shows that $`C_aE^a`$ is not exactly equal to the potential BF coupling:

```math
\begin{aligned}
-4gC_aP^a
&=-4gC_aE^a
-2igC_a\bar\psi_b{}^i\gamma^{ba}\varphi_i
-gC_a\bar\psi_b{}^i\gamma^{abc}\psi_c{}^jL_{ij}.
\end{aligned}
\tag{A.35}
```

The expression with $`-4gC_aE^a`$ in (5.11) lacks the last two terms, so that line does not replace the full two-fermion action. The expression (5.10) used here is consistent with this conversion in the $`F_{\mu\nu}E^{\mu\nu}`$ representative. Action coefficients remain unchanged; (A.31) and (A.35) replace the incorrect alternative notation.

<a id="8-single-total-action"></a>

## Single total action

In the single integral below, the first two blocks are (5.10) of the first input, with the spinor inside the bar explicitly substituted from (5.5). The next block is the **entire 365-term (R2) integrand** of the second input, multiplied only by $`\lambda_{R^2}`$. No new mixed invariant is constructed between the inputs. The common definitions above are part of this integral.

```math
S_{\mathrm{total}}^{\leq2}:=\int_M d^5x\,e\,
\left\{\begin{aligned}
-2\Bigg\{&
\frac{L}{\sqrt2}\delta^{ij}
\Bigg[
L^{-1}\Box_c\left(
\frac{L}{\sqrt2}\delta_{ij}
\right)\\
&-\frac1{\sqrt2}L^{-2}\delta^{km}
\mathcal D_aL_{k(i}\big|_{\mathrm P}
\mathcal D^aL_{j)m}\big|_{\mathrm P}\\
&-\frac1{\sqrt2}L^{-2}\delta_{ij}N^2
-\frac1{\sqrt2}L^{-2}\delta_{ij}E_aE^a\\
&+\sqrt2L^{-2}E_a\delta_{k(i}
\mathcal D^aL_{j)}{}^k\big|_{\mathrm P}\\
&+\frac1{24\sqrt2}\delta_{ij}
\left(
\widehat G_{ab}
+\frac16\varepsilon_{abcde}\widehat H^{cde}
\right)
\left(
\widehat G^{ab}
+\frac16\varepsilon^{abfgh}\widehat H_{fgh}
\right)\\
&+2\sqrt2\delta_{ij}D\big|_{\mathrm P}\\
&+iNL^{-3}\bar\varphi_{(i}\varphi_{j)}
-\frac{3i}{2}NL^{-3}\delta_{ij}\delta^{kl}
\bar\varphi_k\varphi_l\\
&+\frac32L^{-3}\delta_{ij}\delta^{kl}
\bar\varphi_k\not E\varphi_l
-L^{-3}\bar\varphi_{(i}\not E\varphi_{j)}\\
&-16iL^{-1}\bar\chi_{(i}\big|_{\mathrm P}\varphi_{j)}
+8iL^{-1}\delta_{ij}\delta_{kl}
\bar\chi^k\big|_{\mathrm P}\varphi^l\\
&+\sqrt2L^{-2}\delta_{k(i}\bar\varphi^k
\not{\mathcal D}\varphi_{j)}\big|_{\mathrm P}\\
&-\frac32L^{-3}\delta_{k(i}\delta^{lm}
\bar\varphi^k
\not{\mathcal D}L_{j)l}\big|_{\mathrm P}\varphi_m\\
&+\frac12L^{-3}\bar\varphi^l
\not{\mathcal D}L_{l(i}\big|_{\mathrm P}\varphi_{j)}\\
&+\frac12L^{-3}\bar\varphi^m
\not{\mathcal D}L_{ij}\big|_{\mathrm P}\varphi_m\\
&+\frac{i}{4\sqrt2}L^{-2}\delta_{ij}
\bar\varphi\gamma^{ab}
\left(
\widehat G_{ab}
+\frac16\varepsilon_{abcde}\widehat H^{cde}
\right)\varphi
\Bigg]\\[2pt]
&+i\left[
\overline{\left(
\begin{aligned}
\epsilon^{ir}\Bigg\{&
-2iL^{-1}\gamma^\mu
\mathcal D_\mu\varphi_r\big|_{\mathrm P}\\
&+i\sqrt2\delta_{rs}\gamma^\mu
\Bigg[
\Bigg(
\frac14\gamma^{ab}\widehat G_{ab}
-\frac18\gamma^{ab}\left(
\widehat G_{ab}
+\frac16\varepsilon_{abcde}\widehat H^{cde}
\right)
\Bigg)\psi_\mu{}^s\\
&\hspace{8em}
-\phi_\mu{}^s
-\frac{gL}{2\sqrt2}\delta^{sk}\psi_{\mu k}
\Bigg]\\
&+\frac1{2L}\gamma^{ab}
\left(
\widehat G_{ab}
+\frac16\varepsilon_{abcde}\widehat H^{cde}
\right)\varphi_r\\
&-\sqrt2NL^{-2}\delta_{rs}\varphi^s\\
&+2iL^{-3}\left[
\left(\not{\mathcal D}L_{rs}\big|_{\mathrm P}\right)
\frac{L}{\sqrt2}\delta^{st}\varphi_t
-\frac{L}{\sqrt2}\delta_{rs}\not E\,\varphi^s
\right]\\
&+\sqrt2g\delta_{rs}\varphi^s
\Bigg\}
\end{aligned}
\right)}\varphi_i
\right]\\[2pt]
&-\frac{L}{2\sqrt2}\delta_{ij}
\bar\psi_a{}^i\gamma^a\epsilon^{jr}
\Bigg[
-2iL^{-1}\gamma^\mu
\mathcal D_\mu\varphi_r\big|_{\mathrm P}\\
&\quad+i\sqrt2\delta_{rs}\gamma^\mu
\Bigg\{
\Bigg[
\frac14\gamma^{bc}\widehat G_{bc}
-\frac18\gamma^{bc}\left(
\widehat G_{bc}
+\frac16\varepsilon_{bcdef}\widehat H^{def}
\right)
\Bigg]\psi_\mu{}^s\\
&\qquad\qquad
-\phi_\mu{}^s
-\frac{gL}{2\sqrt2}\delta^{sk}\psi_{\mu k}
\Bigg\}\\
&\quad+\frac1{2L}\gamma^{bc}
\left(
\widehat G_{bc}
+\frac16\varepsilon_{bcdef}\widehat H^{def}
\right)\varphi_r\\
&\quad-\sqrt2NL^{-2}\delta_{rs}\varphi^s\\
&\quad+2iL^{-3}\Bigg[
\left(\not{\mathcal D}L_{rs}\big|_{\mathrm P}\right)
\frac{L}{\sqrt2}\delta^{st}\varphi_t\\
&\qquad\qquad
-\frac{L}{\sqrt2}\delta_{rs}\not E\,\varphi^s
\Bigg]
+\sqrt2g\delta_{rs}\varphi^s
\Bigg]\\[2pt]
&+\frac12E^{\mu\nu}\Bigg[
4\mathcal D_{[\mu}\left(L^{-1}E_{\nu]}\right)
+\sqrt2\delta_{ij}\widehat R_{\mu\nu}{}^{ij}(V)\\
&\quad+\sqrt2L^{-2}\delta_{km}\epsilon^{m\ell}
\mathcal D_{[\mu}L^{kp}\big|_{\mathrm P}
\mathcal D_{\nu]}L_{\ell p}\big|_{\mathrm P}\\
&\quad-\sqrt2\mathcal D_{[\mu}\left(
L^{-2}\delta_{ij}
\bar\varphi^i\gamma_{\nu]}\varphi^j
\right)
-iL^{-1}\bar\varphi^i\widehat R_{\mu\nu i}(Q)\\
&\quad+\bar\psi_{[\mu}{}^i\gamma_{\nu]}
\Bigg\{
-2iL^{-1}\gamma^\rho
\mathcal D_\rho\varphi_i\big|_{\mathrm P}\\
&\qquad+i\sqrt2\delta_{ij}\gamma^\rho
\Bigg[
\Bigg(
\frac14\gamma^{ab}\widehat G_{ab}
-\frac18\gamma^{ab}\left(
\widehat G_{ab}
+\frac16\varepsilon_{abcde}\widehat H^{cde}
\right)
\Bigg)\psi_\rho{}^j\\
&\hspace{13em}
-\phi_\rho{}^j
-\frac{gL}{2\sqrt2}\delta^{jk}\psi_{\rho k}
\Bigg]\\
&\qquad+\frac1{2L}\gamma^{ab}
\left(
\widehat G_{ab}
+\frac16\varepsilon_{abcde}\widehat H^{cde}
\right)\varphi_i\\
&\qquad-\sqrt2NL^{-2}\delta_{ij}\varphi^j\\
&\qquad+2iL^{-3}\Bigg[
\left(\not{\mathcal D}L_{ij}\big|_{\mathrm P}\right)
\frac{L}{\sqrt2}\delta^{jk}\varphi_k\\
&\hspace{12em}
-\frac{L}{\sqrt2}\delta_{ij}\not E\,\varphi^j
\Bigg]
+\sqrt2g\delta_{ij}\varphi^j
\Bigg\}\\
&\quad-iL^{-1}N
\bar\psi_{[\mu}{}^i\psi_{\nu]i}
\Bigg]\\[2pt]
&+\left(
2L^{-1}N
+\frac{i}{\sqrt2}L^{-2}\delta_{ij}
\bar\varphi^i\varphi^j
\right)\\
&\quad\times\left(
N+\frac12\bar\psi_a{}^i\gamma^a\varphi_i
+\frac{iL}{4\sqrt2}\delta_{ij}
\bar\psi_a{}^i\gamma^{ab}\psi_b{}^j
\right)
\Bigg\}\\[2pt]
&-4g\Bigg\{
\frac12G_{\mu\nu}E^{\mu\nu}
+N-\frac g2L^2\\
&\qquad+\frac12\bar\psi_a{}^i\gamma^a\varphi_i
+\frac{iL}{4\sqrt2}\delta_{ij}
\bar\psi_a{}^i\gamma^{ab}\psi_b{}^j
\Bigg\}
\\[4pt]
&+\lambda_{R^2}\Bigg\{\begin{aligned}[t]
&\frac{1}{L^{2}} \Box_c\!\left(L_{ij}\right) \Box_c\!\left(L^{ij}\right) - \frac{2}{L^{3}} \Box_c\!\left(L_{ij}\right) \mathcal D_{a}\!\left(L\right) \mathcal D^{a}\!\left(L^{ij}\right) +\frac{2}{L^{2}} \left(4 D +\frac{8}{3} T_{ab} T^{ab} - \frac{1}{L^{2}} E_{a} E^{a} - \frac{N^{2}}{L^{2}} +\frac{1}{2 L^{2}} \mathcal D_{a}\!\left(L_{kl}\right) \mathcal D^{a}\!\left(L^{kl}\right)\right) L_{ij} \Box_c\!\left(L^{ij}\right) +\frac{2}{L^{4}} \Box_c\!\left(L^{ij}\right) \left(\bar\varphi_{(i} \left(i N - \gamma^{b} E_{b}\right) \varphi_{j)}\right)\\
&+\frac{6}{L^{6}} L_{i}{}^{j} L_{kl} \Box_c\!\left(L^{kl}\right) \bar\varphi^{i} \left(i N - \gamma^{a} E_{a}\right) \varphi_{j} +\frac{4}{L^{4}} E_{a} \left(L_{k(i} \mathcal D^{a}\!\left(L_{j)}{}^{k}\right)\right) \Box_c\!\left(L^{ij}\right) +\frac{6}{L^{6}} \left(L_{m(k} \mathcal D_{a}\!\left(L_{l)}{}^{m}\right)\right) L_{i}{}^{j} \Box_c\!\left(L^{kl}\right) \bar\varphi^{i} \gamma^{a} \varphi_{j} - \frac{32 i}{L^{2}} \Box_c\!\left(L^{ij}\right) \left(\bar\chi_{(i} \varphi_{j)}\right)\\
&- \frac{32 i}{L^{4}} L_{i}{}^{j} L_{kl} \Box_c\!\left(L^{kl}\right) \bar\chi^{i} \varphi_{j} +\frac{4}{L^{4}} \Box_c\!\left(L^{ij}\right) \left(L_{k(i} \bar\varphi^{k} \gamma^{a} \mathcal D_{a}\!\left(\varphi_{j)}\right)\right) - \frac{2}{L^{4}} \Box_c\!\left(L^{ij}\right) \left(\bar\varphi^{k} \gamma^{a} \mathcal D_{a}\!\left(L_{k(i}\right) \varphi_{j)}\right) +\frac{4 i}{L^{4}} L_{jk} \Box_c\!\left(L^{jk}\right) T_{ab} \bar\varphi^{i} \gamma^{ab} \varphi_{i}\\
&+\frac{1}{L^{4}} \mathcal D_{a}\!\left(L\right) \mathcal D_{b}\!\left(L\right) \mathcal D^{a}\!\left(L_{ij}\right) \mathcal D^{b}\!\left(L^{ij}\right) - \frac{2}{L^{3}} \left(4 D +\frac{8}{3} T_{bc} T^{bc} - \frac{1}{L^{2}} E_{b} E^{b} - \frac{N^{2}}{L^{2}} +\frac{1}{2 L^{2}} \mathcal D_{b}\!\left(L_{kl}\right) \mathcal D^{b}\!\left(L^{kl}\right)\right) L_{ij} \mathcal D_{a}\!\left(L\right) \mathcal D^{a}\!\left(L^{ij}\right) - \frac{2}{L^{5}} \mathcal D_{a}\!\left(L\right) \mathcal D^{a}\!\left(L^{ij}\right) \left(\bar\varphi_{(i} \left(i N - \gamma^{c} E_{c}\right) \varphi_{j)}\right) - \frac{6}{L^{7}} L_{i}{}^{j} L_{kl} \mathcal D_{a}\!\left(L\right) \mathcal D^{a}\!\left(L^{kl}\right) \bar\varphi^{i} \left(i N - \gamma^{b} E_{b}\right) \varphi_{j}\\
&- \frac{4}{L^{5}} E_{a} \left(L_{k(i} \mathcal D^{a}\!\left(L_{j)}{}^{k}\right)\right) \mathcal D_{b}\!\left(L\right) \mathcal D^{b}\!\left(L^{ij}\right) - \frac{6}{L^{7}} \left(L_{m(k} \mathcal D_{a}\!\left(L_{l)}{}^{m}\right)\right) L_{i}{}^{j} \mathcal D_{b}\!\left(L\right) \mathcal D^{b}\!\left(L^{kl}\right) \bar\varphi^{i} \gamma^{a} \varphi_{j} +\frac{32 i}{L^{3}} \mathcal D_{a}\!\left(L\right) \mathcal D^{a}\!\left(L^{ij}\right) \left(\bar\chi_{(i} \varphi_{j)}\right) +\frac{32 i}{L^{5}} L_{i}{}^{j} L_{kl} \mathcal D_{a}\!\left(L\right) \mathcal D^{a}\!\left(L^{kl}\right) \bar\chi^{i} \varphi_{j}\\
&- \frac{4}{L^{5}} \mathcal D_{a}\!\left(L\right) \mathcal D^{a}\!\left(L^{ij}\right) \left(L_{k(i} \bar\varphi^{k} \gamma^{b} \mathcal D_{b}\!\left(\varphi_{j)}\right)\right) +\frac{2}{L^{5}} \mathcal D_{a}\!\left(L\right) \mathcal D^{a}\!\left(L^{ij}\right) \left(\bar\varphi^{k} \gamma^{b} \mathcal D_{b}\!\left(L_{k(i}\right) \varphi_{j)}\right) - \frac{4 i}{L^{5}} L_{jk} \mathcal D_{c}\!\left(L\right) \mathcal D^{c}\!\left(L^{jk}\right) T_{ab} \bar\varphi^{i} \gamma^{ab} \varphi_{i} +\left(4 D +\frac{8}{3} T_{ab} T^{ab} - \frac{1}{L^{2}} E_{a} E^{a} - \frac{N^{2}}{L^{2}} +\frac{1}{2 L^{2}} \mathcal D_{a}\!\left(L_{ij}\right) \mathcal D^{a}\!\left(L^{ij}\right)\right) \left(4 D +\frac{8}{3} T_{cd} T^{cd} - \frac{1}{L^{2}} E_{c} E^{c} - \frac{N^{2}}{L^{2}} +\frac{1}{2 L^{2}} \mathcal D_{c}\!\left(L_{kl}\right) \mathcal D^{c}\!\left(L^{kl}\right)\right)\\
&+\frac{2}{L^{4}} \left(4 D +\frac{8}{3} T_{ab} T^{ab} - \frac{1}{L^{2}} E_{a} E^{a} - \frac{N^{2}}{L^{2}} +\frac{1}{2 L^{2}} \mathcal D_{a}\!\left(L_{kl}\right) \mathcal D^{a}\!\left(L^{kl}\right)\right) L^{ij} \left(\bar\varphi_{(i} \left(i N - \gamma^{d} E_{d}\right) \varphi_{j)}\right) +\frac{6}{L^{4}} \left(4 D +\frac{8}{3} T_{ab} T^{ab} - \frac{1}{L^{2}} E_{a} E^{a} - \frac{N^{2}}{L^{2}} +\frac{1}{2 L^{2}} \mathcal D_{a}\!\left(L_{kl}\right) \mathcal D^{a}\!\left(L^{kl}\right)\right) L_{i}{}^{j} \bar\varphi^{i} \left(i N - \gamma^{c} E_{c}\right) \varphi_{j} +\frac{4}{L^{4}} E_{a} \left(4 D +\frac{8}{3} T_{bc} T^{bc} - \frac{1}{L^{2}} E_{b} E^{b} - \frac{N^{2}}{L^{2}} +\frac{1}{2 L^{2}} \mathcal D_{b}\!\left(L_{kl}\right) \mathcal D^{b}\!\left(L^{kl}\right)\right) \left(L_{m(i} \mathcal D^{a}\!\left(L_{j)}{}^{m}\right)\right) L^{ij} +\frac{6}{L^{6}} \left(4 D +\frac{8}{3} T_{bc} T^{bc} - \frac{1}{L^{2}} E_{b} E^{b} - \frac{N^{2}}{L^{2}} +\frac{1}{2 L^{2}} \mathcal D_{b}\!\left(L_{mn}\right) \mathcal D^{b}\!\left(L^{mn}\right)\right) \left(L_{o(k} \mathcal D_{a}\!\left(L_{l)}{}^{o}\right)\right) L_{i}{}^{j} L^{kl} \bar\varphi^{i} \gamma^{a} \varphi_{j}\\
&- \frac{32 i}{L^{2}} \left(4 D +\frac{8}{3} T_{ab} T^{ab} - \frac{1}{L^{2}} E_{a} E^{a} - \frac{N^{2}}{L^{2}} +\frac{1}{2 L^{2}} \mathcal D_{a}\!\left(L_{kl}\right) \mathcal D^{a}\!\left(L^{kl}\right)\right) L^{ij} \left(\bar\chi_{(i} \varphi_{j)}\right) - \frac{32 i}{L^{2}} \left(4 D +\frac{8}{3} T_{ab} T^{ab} - \frac{1}{L^{2}} E_{a} E^{a} - \frac{N^{2}}{L^{2}} +\frac{1}{2 L^{2}} \mathcal D_{a}\!\left(L_{kl}\right) \mathcal D^{a}\!\left(L^{kl}\right)\right) L_{i}{}^{j} \bar\chi^{i} \varphi_{j} +\frac{4}{L^{4}} \left(4 D +\frac{8}{3} T_{ab} T^{ab} - \frac{1}{L^{2}} E_{a} E^{a} - \frac{N^{2}}{L^{2}} +\frac{1}{2 L^{2}} \mathcal D_{a}\!\left(L_{kl}\right) \mathcal D^{a}\!\left(L^{kl}\right)\right) L^{ij} \left(L_{m(i} \bar\varphi^{m} \gamma^{c} \mathcal D_{c}\!\left(\varphi_{j)}\right)\right) - \frac{2}{L^{4}} \left(4 D +\frac{8}{3} T_{ab} T^{ab} - \frac{1}{L^{2}} E_{a} E^{a} - \frac{N^{2}}{L^{2}} +\frac{1}{2 L^{2}} \mathcal D_{a}\!\left(L_{kl}\right) \mathcal D^{a}\!\left(L^{kl}\right)\right) L^{ij} \left(\bar\varphi^{m} \gamma^{c} \mathcal D_{c}\!\left(L_{m(i}\right) \varphi_{j)}\right)\\
&+\frac{4 i}{L^{2}} \left(4 D +\frac{8}{3} T_{cd} T^{cd} - \frac{1}{L^{2}} E_{c} E^{c} - \frac{N^{2}}{L^{2}} +\frac{1}{2 L^{2}} \mathcal D_{c}\!\left(L_{jk}\right) \mathcal D^{c}\!\left(L^{jk}\right)\right) T_{ab} \bar\varphi^{i} \gamma^{ab} \varphi_{i} +\frac{4}{L^{6}} E_{a} \left(L_{k}{}^{(i} \mathcal D^{a}\!\left(L^{j)k}\right)\right) \left(\bar\varphi_{(i} \left(i N - \gamma^{c} E_{c}\right) \varphi_{j)}\right) +\frac{12}{L^{8}} E_{a} \left(L_{m(k} \mathcal D^{a}\!\left(L_{l)}{}^{m}\right)\right) L_{i}{}^{j} L^{kl} \bar\varphi^{i} \left(i N - \gamma^{b} E_{b}\right) \varphi_{j} +\frac{4}{L^{6}} E_{a} E_{b} \left(L_{k(i} \mathcal D^{a}\!\left(L_{j)}{}^{k}\right)\right) \left(L_{l}{}^{(i} \mathcal D^{b}\!\left(L^{j)l}\right)\right)\\
&+\frac{6}{L^{8}} E_{b} \left(L_{m(k} \mathcal D^{b}\!\left(L_{l)}{}^{m}\right)\right) \left(L_{n}{}^{(k} \mathcal D_{a}\!\left(L^{l)n}\right)\right) L_{i}{}^{j} \bar\varphi^{i} \gamma^{a} \varphi_{j} - \frac{64 i}{L^{4}} E_{a} \left(L_{k}{}^{(i} \mathcal D^{a}\!\left(L^{j)k}\right)\right) \left(\bar\chi_{(i} \varphi_{j)}\right) - \frac{64 i}{L^{6}} E_{a} \left(L_{m(k} \mathcal D^{a}\!\left(L_{l)}{}^{m}\right)\right) L_{i}{}^{j} L^{kl} \bar\chi^{i} \varphi_{j} +\frac{8}{L^{6}} E_{a} \left(L_{k}{}^{(i} \mathcal D^{a}\!\left(L^{j)k}\right)\right) \left(L_{l(i} \bar\varphi^{l} \gamma^{b} \mathcal D_{b}\!\left(\varphi_{j)}\right)\right)\\
&- \frac{4}{L^{6}} E_{a} \left(L_{k}{}^{(i} \mathcal D^{a}\!\left(L^{j)k}\right)\right) \left(\bar\varphi^{l} \gamma^{b} \mathcal D_{b}\!\left(L_{l(i}\right) \varphi_{j)}\right) +\frac{8 i}{L^{6}} E_{c} \left(L_{l(j} \mathcal D^{c}\!\left(L_{k)}{}^{l}\right)\right) L^{jk} T_{ab} \bar\varphi^{i} \gamma^{ab} \varphi_{i} +\frac{6}{L^{8}} E_{b} \left(L_{m(k} \mathcal D_{a}\!\left(L_{l)}{}^{m}\right)\right) \left(L_{n}{}^{(k} \mathcal D^{b}\!\left(L^{l)n}\right)\right) L_{i}{}^{j} \bar\varphi^{i} \gamma^{a} \varphi_{j} - \frac{2 N g}{L^{2}} L_{ij} \Box_c\!\left(L^{ij}\right)\\
&+\frac{2 N g}{L^{3}} L_{ij} \mathcal D_{a}\!\left(L\right) \mathcal D^{a}\!\left(L^{ij}\right) - 2 N g \left(4 D +\frac{8}{3} T_{ab} T^{ab} - \frac{1}{L^{2}} E_{a} E^{a} - \frac{N^{2}}{L^{2}} +\frac{1}{2 L^{2}} \mathcal D_{a}\!\left(L_{ij}\right) \mathcal D^{a}\!\left(L^{ij}\right)\right) - \frac{2 N g}{L^{4}} L^{ij} \left(\bar\varphi_{(i} \left(i N - \gamma^{b} E_{b}\right) \varphi_{j)}\right) - \frac{6 N g}{L^{4}} L_{i}{}^{j} \bar\varphi^{i} \left(i N - \gamma^{a} E_{a}\right) \varphi_{j}\\
&- \frac{4 N g}{L^{4}} E_{a} \left(L_{k(i} \mathcal D^{a}\!\left(L_{j)}{}^{k}\right)\right) L^{ij} - \frac{6 N g}{L^{6}} \left(L_{m(k} \mathcal D_{a}\!\left(L_{l)}{}^{m}\right)\right) L_{i}{}^{j} L^{kl} \bar\varphi^{i} \gamma^{a} \varphi_{j} +\frac{32 i N g}{L^{2}} L^{ij} \left(\bar\chi_{(i} \varphi_{j)}\right) +\frac{32 i N g}{L^{2}} L_{i}{}^{j} \bar\chi^{i} \varphi_{j}\\
&- \frac{4 N g}{L^{4}} L^{ij} \left(L_{k(i} \bar\varphi^{k} \gamma^{a} \mathcal D_{a}\!\left(\varphi_{j)}\right)\right) +\frac{2 N g}{L^{4}} L^{ij} \left(\bar\varphi^{k} \gamma^{a} \mathcal D_{a}\!\left(L_{k(i}\right) \varphi_{j)}\right) - \frac{4 i N g}{L^{2}} T_{ab} \bar\varphi^{i} \gamma^{ab} \varphi_{i} +\frac{i g}{L^{4}} L_{i}{}^{j} L_{kl} \Box_c\!\left(L^{kl}\right) \bar\varphi^{i} \varphi_{j}\\
&- \frac{i g}{L^{5}} L_{i}{}^{j} L_{kl} \mathcal D_{a}\!\left(L\right) \mathcal D^{a}\!\left(L^{kl}\right) \bar\varphi^{i} \varphi_{j} +\frac{i g}{L^{2}} \left(4 D +\frac{8}{3} T_{ab} T^{ab} - \frac{1}{L^{2}} E_{a} E^{a} - \frac{N^{2}}{L^{2}} +\frac{1}{2 L^{2}} \mathcal D_{a}\!\left(L_{kl}\right) \mathcal D^{a}\!\left(L^{kl}\right)\right) L_{i}{}^{j} \bar\varphi^{i} \varphi_{j} +\frac{2 i g}{L^{6}} E_{a} \left(L_{m(k} \mathcal D^{a}\!\left(L_{l)}{}^{m}\right)\right) L_{i}{}^{j} L^{kl} \bar\varphi^{i} \varphi_{j} - \frac{2}{L} \mathcal D_{a}\!\left(\bar\varphi_{i}\right) \gamma^{a} \gamma^{b} \mathcal D_{b}\!\left(\frac{1}{L} \gamma^{c} \mathcal D_{c}\!\left(\varphi^{i}\right)\right)\\
&- \frac{16 i}{L} \mathcal D_{a}\!\left(\bar\varphi_{i}\right) \gamma^{a} \gamma^{b} \mathcal D_{b}\!\left(\frac{1}{L} L^{i}{}_{j} \chi^{j}\right) - \frac{4 i}{L} \mathcal D_{a}\!\left(\bar\varphi_{i}\right) \gamma^{a} \gamma^{b} \mathcal D_{b}\!\left(\frac{1}{L} \gamma^{cd} T_{cd} \varphi^{i}\right) +\frac{2 i}{L} \mathcal D_{a}\!\left(\bar\varphi_{i}\right) \gamma^{a} \gamma^{b} \mathcal D_{b}\!\left(\frac{1}{L^{3}} L^{i}{}_{j} \left(i \gamma^{c} E_{c} +N\right) \varphi^{j}\right) +\frac{2}{L} \mathcal D_{a}\!\left(\bar\varphi_{i}\right) \gamma^{a} \gamma^{b} \mathcal D_{b}\!\left(\frac{1}{L^{3}} \gamma^{c} \mathcal D_{c}\!\left(L^{i}{}_{j}\right) L^{jk} \varphi_{k}\right)\\
&+\frac{16 i}{L} L_{i}{}^{j} \bar\chi^{i} \gamma^{a} \mathcal D_{a}\!\left(\frac{1}{L} \gamma^{b} \mathcal D_{b}\!\left(\varphi_{j}\right)\right) - \frac{128}{L} L_{i}{}^{j} \bar\chi^{i} \gamma^{a} \mathcal D_{a}\!\left(\frac{1}{L} L_{jk} \chi^{k}\right) - \frac{32}{L} L_{i}{}^{j} \bar\chi^{i} \gamma^{a} \mathcal D_{a}\!\left(\frac{1}{L} \gamma^{bc} T_{bc} \varphi_{j}\right) +\frac{16}{L} L_{i}{}^{j} \bar\chi^{i} \gamma^{a} \mathcal D_{a}\!\left(\frac{1}{L^{3}} L_{jk} \left(i \gamma^{b} E_{b} +N\right) \varphi^{k}\right)\\
&- \frac{16 i}{L} L_{i}{}^{j} \bar\chi^{i} \gamma^{a} \mathcal D_{a}\!\left(\frac{1}{L^{3}} \gamma^{b} \mathcal D_{b}\!\left(L_{jk}\right) L^{kl} \varphi_{l}\right) - \frac{4 i}{L} T_{ab} \bar\varphi^{i} \gamma^{ab} \gamma^{c} \mathcal D_{c}\!\left(\frac{1}{L} \gamma^{d} \mathcal D_{d}\!\left(\varphi_{i}\right)\right) +\frac{32}{L} T_{ab} \bar\varphi^{i} \gamma^{ab} \gamma^{c} \mathcal D_{c}\!\left(\frac{1}{L} L_{ij} \chi^{j}\right) +\frac{8}{L} T_{ab} \bar\varphi^{i} \gamma^{ab} \gamma^{c} \mathcal D_{c}\!\left(\frac{1}{L} \gamma^{de} T_{de} \varphi_{i}\right)\\
&- \frac{4}{L} T_{ab} \bar\varphi^{i} \gamma^{ab} \gamma^{c} \mathcal D_{c}\!\left(\frac{1}{L^{3}} L_{ij} \left(i \gamma^{d} E_{d} +N\right) \varphi^{j}\right) +\frac{4 i}{L} T_{ab} \bar\varphi^{i} \gamma^{ab} \gamma^{c} \mathcal D_{c}\!\left(\frac{1}{L^{3}} \gamma^{d} \mathcal D_{d}\!\left(L_{ij}\right) L^{jk} \varphi_{k}\right) - \frac{2 i}{L^{3}} L_{i}{}^{j} \bar\varphi^{i} \left(i E_{b} \gamma^{b} +N\right) \gamma^{a} \mathcal D_{a}\!\left(\frac{1}{L} \gamma^{c} \mathcal D_{c}\!\left(\varphi_{j}\right)\right) +\frac{16}{L^{3}} L_{i}{}^{j} \bar\varphi^{i} \left(i E_{b} \gamma^{b} +N\right) \gamma^{a} \mathcal D_{a}\!\left(\frac{1}{L} L_{jk} \chi^{k}\right)\\
&+\frac{4}{L^{3}} L_{i}{}^{j} \bar\varphi^{i} \left(i E_{b} \gamma^{b} +N\right) \gamma^{a} \mathcal D_{a}\!\left(\frac{1}{L} \gamma^{cd} T_{cd} \varphi_{j}\right) - \frac{2}{L^{3}} L_{i}{}^{j} \bar\varphi^{i} \left(i E_{b} \gamma^{b} +N\right) \gamma^{a} \mathcal D_{a}\!\left(\frac{1}{L^{3}} L_{jk} \left(i \gamma^{c} E_{c} +N\right) \varphi^{k}\right) +\frac{2 i}{L^{3}} L_{i}{}^{j} \bar\varphi^{i} \left(i E_{b} \gamma^{b} +N\right) \gamma^{a} \mathcal D_{a}\!\left(\frac{1}{L^{3}} \gamma^{c} \mathcal D_{c}\!\left(L_{jk}\right) L^{kl} \varphi_{l}\right) - \frac{2}{L^{3}} L_{ik} \mathcal D_{a}\!\left(L^{jk}\right) \bar\varphi^{i} \gamma^{a} \gamma^{b} \mathcal D_{b}\!\left(\frac{1}{L} \gamma^{c} \mathcal D_{c}\!\left(\varphi_{j}\right)\right)\\
&- \frac{16 i}{L^{3}} L_{ik} \mathcal D_{a}\!\left(L^{jk}\right) \bar\varphi^{i} \gamma^{a} \gamma^{b} \mathcal D_{b}\!\left(\frac{1}{L} L_{jl} \chi^{l}\right) - \frac{4 i}{L^{3}} L_{ik} \mathcal D_{a}\!\left(L^{jk}\right) \bar\varphi^{i} \gamma^{a} \gamma^{b} \mathcal D_{b}\!\left(\frac{1}{L} \gamma^{cd} T_{cd} \varphi_{j}\right) +\frac{2 i}{L^{3}} L_{ik} \mathcal D_{a}\!\left(L^{jk}\right) \bar\varphi^{i} \gamma^{a} \gamma^{b} \mathcal D_{b}\!\left(\frac{1}{L^{3}} L_{jl} \left(i \gamma^{c} E_{c} +N\right) \varphi^{l}\right) +\frac{2}{L^{3}} L_{ik} \mathcal D_{a}\!\left(L^{jk}\right) \bar\varphi^{i} \gamma^{a} \gamma^{b} \mathcal D_{b}\!\left(\frac{1}{L^{3}} \gamma^{c} \mathcal D_{c}\!\left(L_{jl}\right) L^{lm} \varphi_{m}\right)\\
&+\frac{4 i}{L^{2}} T_{bc} \mathcal D_{a}\!\left(\bar\varphi_{i}\right) \gamma^{a} \gamma^{bc} \gamma^{d} \mathcal D_{d}\!\left(\varphi^{i}\right) +\frac{32}{L^{2}} L^{ij} T_{bc} \mathcal D_{a}\!\left(\bar\varphi_{i}\right) \gamma^{a} \gamma^{bc} \chi_{j} - \frac{8}{L^{2}} T_{bc} T_{de} \mathcal D_{a}\!\left(\bar\varphi_{i}\right) \gamma^{a} \gamma^{bc} \gamma^{de} \varphi^{i} - \frac{4}{L^{4}} L^{ij} T_{bc} \mathcal D_{a}\!\left(\bar\varphi_{i}\right) \gamma^{a} \gamma^{bc} \left(i \gamma^{d} E_{d} +N\right) \varphi_{j}\\
&+\frac{4 i}{L^{4}} L^{j}{}_{k} \mathcal D_{d}\!\left(L^{ik}\right) T_{bc} \mathcal D_{a}\!\left(\bar\varphi_{i}\right) \gamma^{a} \gamma^{bc} \gamma^{d} \varphi_{j} +\frac{32}{L^{2}} L_{i}{}^{j} T_{ab} \bar\chi^{i} \gamma^{ab} \gamma^{c} \mathcal D_{c}\!\left(\varphi_{j}\right) +128 i T_{ab} \bar\chi^{i} \gamma^{ab} \chi_{i} +\frac{64 i}{L^{2}} L_{i}{}^{j} T_{ab} T_{cd} \bar\chi^{i} \gamma^{ab} \gamma^{cd} \varphi_{j}\\
&- \frac{16 i}{L^{2}} T_{ab} \bar\chi^{i} \gamma^{ab} \left(i \gamma^{c} E_{c} +N\right) \varphi_{i} - \frac{32}{L^{4}} L_{ik} L^{j}{}_{l} \mathcal D_{c}\!\left(L^{kl}\right) T_{ab} \bar\chi^{i} \gamma^{ab} \gamma^{c} \varphi_{j} - \frac{8}{L^{2}} T_{ab} T_{cd} \bar\varphi^{i} \gamma^{ab} \gamma^{cd} \gamma^{e} \mathcal D_{e}\!\left(\varphi_{i}\right) +\frac{64 i}{L^{2}} L_{i}{}^{j} T_{ab} T_{cd} \bar\varphi^{i} \gamma^{ab} \gamma^{cd} \chi_{j}\\
&- \frac{16 i}{L^{2}} T_{ab} T_{cd} T_{ef} \bar\varphi^{i} \gamma^{ab} \gamma^{cd} \gamma^{ef} \varphi_{i} - \frac{8 i}{L^{4}} L_{i}{}^{j} T_{ab} T_{cd} \bar\varphi^{i} \gamma^{ab} \gamma^{cd} \left(i \gamma^{e} E_{e} +N\right) \varphi_{j} - \frac{8}{L^{4}} L^{j}{}_{k} \mathcal D_{e}\!\left(L_{i}{}^{k}\right) T_{ab} T_{cd} \bar\varphi^{i} \gamma^{ab} \gamma^{cd} \gamma^{e} \varphi_{j} - \frac{4}{L^{4}} L_{i}{}^{j} T_{ab} \bar\varphi^{i} \left(i E_{d} \gamma^{d} +N\right) \gamma^{ab} \gamma^{c} \mathcal D_{c}\!\left(\varphi_{j}\right)\\
&- \frac{16 i}{L^{2}} T_{ab} \bar\varphi^{i} \left(i E_{c} \gamma^{c} +N\right) \gamma^{ab} \chi_{i} - \frac{8 i}{L^{4}} L_{i}{}^{j} T_{ab} T_{cd} \bar\varphi^{i} \left(i E_{e} \gamma^{e} +N\right) \gamma^{ab} \gamma^{cd} \varphi_{j} +\frac{2 i}{L^{4}} T_{ab} \bar\varphi^{i} \left(i E_{c} \gamma^{c} +N\right) \gamma^{ab} \left(i \gamma^{d} E_{d} +N\right) \varphi_{i} +\frac{4}{L^{6}} L_{ik} L^{j}{}_{l} \mathcal D_{c}\!\left(L^{kl}\right) T_{ab} \bar\varphi^{i} \left(i E_{d} \gamma^{d} +N\right) \gamma^{ab} \gamma^{c} \varphi_{j}\\
&+\frac{4 i}{L^{4}} L_{ik} \mathcal D_{a}\!\left(L^{jk}\right) T_{bc} \bar\varphi^{i} \gamma^{a} \gamma^{bc} \gamma^{d} \mathcal D_{d}\!\left(\varphi_{j}\right) +\frac{32}{L^{4}} L_{ik} L^{j}{}_{l} \mathcal D_{a}\!\left(L^{lk}\right) T_{bc} \bar\varphi^{i} \gamma^{a} \gamma^{bc} \chi_{j} - \frac{8}{L^{4}} L_{ik} \mathcal D_{a}\!\left(L^{jk}\right) T_{bc} T_{de} \bar\varphi^{i} \gamma^{a} \gamma^{bc} \gamma^{de} \varphi_{j} - \frac{4}{L^{6}} L_{ik} L^{j}{}_{l} \mathcal D_{a}\!\left(L^{lk}\right) T_{bc} \bar\varphi^{i} \gamma^{a} \gamma^{bc} \left(i \gamma^{d} E_{d} +N\right) \varphi_{j}\\
&- \frac{4 i}{L^{6}} L_{ik} L^{j}{}_{l} \mathcal D_{a}\!\left(L_{m}{}^{k}\right) \mathcal D_{d}\!\left(L^{ml}\right) T_{bc} \bar\varphi^{i} \gamma^{a} \gamma^{bc} \gamma^{d} \varphi_{j} +\frac{4 \left(L^{2} g + 16 N\right)}{L^{2}} \mathcal D_{a}\!\left(\bar\varphi_{i}\right) \gamma^{a} \chi^{i} - \frac{32 i \left(L^{2} g + 16 N\right)}{L^{2}} L_{i}{}^{j} \bar\chi^{i} \chi_{j} +\frac{8 i \left(L^{2} g + 16 N\right)}{L^{2}} T_{ab} \bar\varphi^{i} \gamma^{ab} \chi_{i}\\
&+\frac{4 i \left(L^{2} g + 16 N\right)}{L^{4}} L_{i}{}^{j} \bar\varphi^{i} \left(i E_{a} \gamma^{a} +N\right) \chi_{j} +\frac{4 \left(L^{2} g + 16 N\right)}{L^{4}} L_{ik} \mathcal D_{a}\!\left(L^{jk}\right) \bar\varphi^{i} \gamma^{a} \chi_{j} - \frac{i}{2 L^{2}} \widehat G_{bc} \mathcal D_{a}\!\left(\bar\varphi_{i}\right) \gamma^{a} \gamma^{bc} \gamma^{d} \mathcal D_{d}\!\left(\varphi^{i}\right) - \frac{4}{L^{2}} \widehat G_{bc} L^{ij} \mathcal D_{a}\!\left(\bar\varphi_{i}\right) \gamma^{a} \gamma^{bc} \chi_{j}\\
&+\frac{1}{L^{2}} \widehat G_{bc} T_{de} \mathcal D_{a}\!\left(\bar\varphi_{i}\right) \gamma^{a} \gamma^{bc} \gamma^{de} \varphi^{i} +\frac{1}{2 L^{4}} \widehat G_{bc} L^{ij} \mathcal D_{a}\!\left(\bar\varphi_{i}\right) \gamma^{a} \gamma^{bc} \left(i \gamma^{d} E_{d} +N\right) \varphi_{j} - \frac{i}{2 L^{4}} \widehat G_{bc} L^{j}{}_{k} \mathcal D_{d}\!\left(L^{ik}\right) \mathcal D_{a}\!\left(\bar\varphi_{i}\right) \gamma^{a} \gamma^{bc} \gamma^{d} \varphi_{j} - \frac{4}{L^{2}} \widehat G_{ab} L_{i}{}^{j} \bar\chi^{i} \gamma^{ab} \gamma^{c} \mathcal D_{c}\!\left(\varphi_{j}\right)\\
&- 16 i \widehat G_{ab} \bar\chi^{i} \gamma^{ab} \chi_{i} - \frac{8 i}{L^{2}} \widehat G_{ab} L_{i}{}^{j} T_{cd} \bar\chi^{i} \gamma^{ab} \gamma^{cd} \varphi_{j} +\frac{2 i}{L^{2}} \widehat G_{ab} \bar\chi^{i} \gamma^{ab} \left(i \gamma^{c} E_{c} +N\right) \varphi_{i} +\frac{4}{L^{4}} \widehat G_{ab} L_{ik} L^{j}{}_{l} \mathcal D_{c}\!\left(L^{kl}\right) \bar\chi^{i} \gamma^{ab} \gamma^{c} \varphi_{j}\\
&+\frac{1}{L^{2}} \widehat G_{cd} T_{ab} \bar\varphi^{i} \gamma^{ab} \gamma^{cd} \gamma^{e} \mathcal D_{e}\!\left(\varphi_{i}\right) - \frac{8 i}{L^{2}} \widehat G_{cd} L_{i}{}^{j} T_{ab} \bar\varphi^{i} \gamma^{ab} \gamma^{cd} \chi_{j} +\frac{2 i}{L^{2}} \widehat G_{cd} T_{ab} T_{ef} \bar\varphi^{i} \gamma^{ab} \gamma^{cd} \gamma^{ef} \varphi_{i} +\frac{i}{L^{4}} \widehat G_{cd} L_{i}{}^{j} T_{ab} \bar\varphi^{i} \gamma^{ab} \gamma^{cd} \left(i \gamma^{e} E_{e} +N\right) \varphi_{j}\\
&+\frac{1}{L^{4}} \widehat G_{cd} L^{j}{}_{k} \mathcal D_{e}\!\left(L_{i}{}^{k}\right) T_{ab} \bar\varphi^{i} \gamma^{ab} \gamma^{cd} \gamma^{e} \varphi_{j} +\frac{1}{2 L^{4}} \widehat G_{ab} L_{i}{}^{j} \bar\varphi^{i} \left(i E_{d} \gamma^{d} +N\right) \gamma^{ab} \gamma^{c} \mathcal D_{c}\!\left(\varphi_{j}\right) +\frac{2 i}{L^{2}} \widehat G_{ab} \bar\varphi^{i} \left(i E_{c} \gamma^{c} +N\right) \gamma^{ab} \chi_{i} +\frac{i}{L^{4}} \widehat G_{ab} L_{i}{}^{j} T_{cd} \bar\varphi^{i} \left(i E_{e} \gamma^{e} +N\right) \gamma^{ab} \gamma^{cd} \varphi_{j}\\
&- \frac{i}{4 L^{4}} \widehat G_{ab} \bar\varphi^{i} \left(i E_{c} \gamma^{c} +N\right) \gamma^{ab} \left(i \gamma^{d} E_{d} +N\right) \varphi_{i} - \frac{1}{2 L^{6}} \widehat G_{ab} L_{ik} L^{j}{}_{l} \mathcal D_{c}\!\left(L^{kl}\right) \bar\varphi^{i} \left(i E_{d} \gamma^{d} +N\right) \gamma^{ab} \gamma^{c} \varphi_{j} - \frac{i}{2 L^{4}} \widehat G_{bc} L_{ik} \mathcal D_{a}\!\left(L^{jk}\right) \bar\varphi^{i} \gamma^{a} \gamma^{bc} \gamma^{d} \mathcal D_{d}\!\left(\varphi_{j}\right) - \frac{4}{L^{4}} \widehat G_{bc} L_{ik} L^{j}{}_{l} \mathcal D_{a}\!\left(L^{lk}\right) \bar\varphi^{i} \gamma^{a} \gamma^{bc} \chi_{j}\\
&+\frac{1}{L^{4}} \widehat G_{bc} L_{ik} \mathcal D_{a}\!\left(L^{jk}\right) T_{de} \bar\varphi^{i} \gamma^{a} \gamma^{bc} \gamma^{de} \varphi_{j} +\frac{1}{2 L^{6}} \widehat G_{bc} L_{ik} L^{j}{}_{l} \mathcal D_{a}\!\left(L^{lk}\right) \bar\varphi^{i} \gamma^{a} \gamma^{bc} \left(i \gamma^{d} E_{d} +N\right) \varphi_{j} +\frac{i}{2 L^{6}} \widehat G_{bc} L_{ik} L^{j}{}_{l} \mathcal D_{a}\!\left(L_{m}{}^{k}\right) \mathcal D_{d}\!\left(L^{ml}\right) \bar\varphi^{i} \gamma^{a} \gamma^{bc} \gamma^{d} \varphi_{j} - \frac{i g}{L^{2}} L^{ij} \mathcal D_{a}\!\left(\bar\varphi_{i}\right) \gamma^{a} \gamma^{b} \mathcal D_{b}\!\left(\varphi_{j}\right)\\
&+\frac{2 g}{L^{2}} L^{ij} T_{bc} \mathcal D_{a}\!\left(\bar\varphi_{i}\right) \gamma^{a} \gamma^{bc} \varphi_{j} - \frac{g}{2 L^{2}} \mathcal D_{a}\!\left(\bar\varphi_{i}\right) \gamma^{a} \left(i \gamma^{b} E_{b} +N\right) \varphi^{i} +\frac{i g}{L^{4}} L^{i}{}_{k} L^{j}{}_{l} \mathcal D_{b}\!\left(L^{kl}\right) \mathcal D_{a}\!\left(\bar\varphi_{i}\right) \gamma^{a} \gamma^{b} \varphi_{j} +4 g \bar\chi^{i} \gamma^{a} \mathcal D_{a}\!\left(\varphi_{i}\right)\\
&+8 i g T_{ab} \bar\chi^{i} \gamma^{ab} \varphi_{i} +\frac{4 i g}{L^{2}} L_{i}{}^{j} \bar\chi^{i} \left(i \gamma^{a} E_{a} +N\right) \varphi_{j} +\frac{4 g}{L^{2}} L^{j}{}_{k} \mathcal D_{a}\!\left(L_{i}{}^{k}\right) \bar\chi^{i} \gamma^{a} \varphi_{j} +\frac{2 g}{L^{2}} L_{i}{}^{j} T_{ab} \bar\varphi^{i} \gamma^{ab} \gamma^{c} \mathcal D_{c}\!\left(\varphi_{j}\right)\\
&+\frac{4 i g}{L^{2}} L_{i}{}^{j} T_{ab} T_{cd} \bar\varphi^{i} \gamma^{ab} \gamma^{cd} \varphi_{j} - \frac{i g}{L^{2}} T_{ab} \bar\varphi^{i} \gamma^{ab} \left(i \gamma^{c} E_{c} +N\right) \varphi_{i} - \frac{2 g}{L^{4}} L_{ik} L^{j}{}_{l} \mathcal D_{c}\!\left(L^{kl}\right) T_{ab} \bar\varphi^{i} \gamma^{ab} \gamma^{c} \varphi_{j} - \frac{g}{2 L^{2}} \bar\varphi^{i} \left(i E_{b} \gamma^{b} +N\right) \gamma^{a} \mathcal D_{a}\!\left(\varphi_{i}\right)\\
&- \frac{i g}{L^{2}} T_{ab} \bar\varphi^{i} \left(i E_{c} \gamma^{c} +N\right) \gamma^{ab} \varphi_{i} - \frac{i g}{2 L^{4}} L_{i}{}^{j} \bar\varphi^{i} \left(i E_{a} \gamma^{a} +N\right) \left(i \gamma^{b} E_{b} +N\right) \varphi_{j} - \frac{g}{2 L^{4}} L^{j}{}_{k} \mathcal D_{a}\!\left(L_{i}{}^{k}\right) \bar\varphi^{i} \left(i E_{b} \gamma^{b} +N\right) \gamma^{a} \varphi_{j} - \frac{i g}{L^{4}} L_{ik} L^{j}{}_{l} \mathcal D_{a}\!\left(L^{lk}\right) \bar\varphi^{i} \gamma^{a} \gamma^{b} \mathcal D_{b}\!\left(\varphi_{j}\right)\\
&+\frac{2 g}{L^{4}} L_{ik} L^{j}{}_{l} \mathcal D_{a}\!\left(L^{lk}\right) T_{bc} \bar\varphi^{i} \gamma^{a} \gamma^{bc} \varphi_{j} - \frac{g}{2 L^{4}} L_{ik} \mathcal D_{a}\!\left(L^{jk}\right) \bar\varphi^{i} \gamma^{a} \left(i \gamma^{b} E_{b} +N\right) \varphi_{j} +\frac{i g}{L^{6}} L_{ik} L^{j}{}_{l} L_{mn} \mathcal D_{a}\!\left(L^{mk}\right) \mathcal D_{b}\!\left(L^{nl}\right) \bar\varphi^{i} \gamma^{a} \gamma^{b} \varphi_{j} +\frac{3 i N g}{2 L^{2}} L_{i}{}^{j} \bar\psi_{a}{}^{i} \gamma^{a} \gamma^{b} \mathcal D_{b}\!\left(\varphi_{j}\right)\\
&- \frac{2 N \left(3 L^{2} g + 10 N\right)}{L^{2}} \bar\psi_{a}{}^{i} \gamma^{a} \chi_{i} - \frac{3 N g}{L^{2}} L_{i}{}^{j} T_{bc} \bar\psi_{a}{}^{i} \gamma^{a} \gamma^{bc} \varphi_{j} +\frac{3 N g}{4 L^{2}} \bar\psi_{a}{}^{i} \gamma^{a} \left(i \gamma^{b} E_{b} +N\right) \varphi_{i} - \frac{3 i N g}{2 L^{4}} L_{ik} L^{j}{}_{l} \mathcal D_{b}\!\left(L^{kl}\right) \bar\psi_{a}{}^{i} \gamma^{a} \gamma^{b} \varphi_{j}\\
&- \frac{i}{L^{2}} \Box_c\!\left(L_{i}{}^{j}\right) \bar\psi_{a}{}^{i} \gamma^{a} \gamma^{b} \mathcal D_{b}\!\left(\varphi_{j}\right) +\frac{i}{L^{3}} \mathcal D_{c}\!\left(L\right) \mathcal D^{c}\!\left(L_{i}{}^{j}\right) \bar\psi_{a}{}^{i} \gamma^{a} \gamma^{b} \mathcal D_{b}\!\left(\varphi_{j}\right) - \frac{i}{L^{2}} \left(4 D +\frac{8}{3} T_{cd} T^{cd} - \frac{1}{L^{2}} E_{c} E^{c} - \frac{N^{2}}{L^{2}} +\frac{1}{2 L^{2}} \mathcal D_{c}\!\left(L_{kl}\right) \mathcal D^{c}\!\left(L^{kl}\right)\right) L_{i}{}^{j} \bar\psi_{a}{}^{i} \gamma^{a} \gamma^{b} \mathcal D_{b}\!\left(\varphi_{j}\right) - \frac{2 i}{L^{4}} E_{c} \epsilon^{jk}\left(L_{l(i} \mathcal D^{c}\!\left(L_{k)}{}^{l}\right)\right) \bar\psi_{a}{}^{i} \gamma^{a} \gamma^{b} \mathcal D_{b}\!\left(\varphi_{j}\right)\\
&- \frac{8}{L^{2}} L^{j}{}_{k} \Box_c\!\left(L_{i}{}^{k}\right) \bar\psi_{a}{}^{i} \gamma^{a} \chi_{j} +\frac{8}{L^{3}} L^{j}{}_{k} \mathcal D_{b}\!\left(L\right) \mathcal D^{b}\!\left(L_{i}{}^{k}\right) \bar\psi_{a}{}^{i} \gamma^{a} \chi_{j} +4 \left(4 D +\frac{8}{3} T_{bc} T^{bc} - \frac{1}{L^{2}} E_{b} E^{b} - \frac{N^{2}}{L^{2}} +\frac{1}{2 L^{2}} \mathcal D_{b}\!\left(L_{jk}\right) \mathcal D^{b}\!\left(L^{jk}\right)\right) \bar\psi_{a}{}^{i} \gamma^{a} \chi_{i} +\frac{16}{L^{4}} E_{b} \left(L_{l(i} \mathcal D^{b}\!\left(L_{k)}{}^{l}\right)\right) L^{jk} \bar\psi_{a}{}^{i} \gamma^{a} \chi_{j}\\
&+\frac{2}{L^{2}} \Box_c\!\left(L_{i}{}^{j}\right) T_{bc} \bar\psi_{a}{}^{i} \gamma^{a} \gamma^{bc} \varphi_{j} - \frac{2}{L^{3}} \mathcal D_{d}\!\left(L\right) \mathcal D^{d}\!\left(L_{i}{}^{j}\right) T_{bc} \bar\psi_{a}{}^{i} \gamma^{a} \gamma^{bc} \varphi_{j} +\frac{2}{L^{2}} \left(4 D +\frac{8}{3} T_{de} T^{de} - \frac{1}{L^{2}} E_{d} E^{d} - \frac{N^{2}}{L^{2}} +\frac{1}{2 L^{2}} \mathcal D_{d}\!\left(L_{kl}\right) \mathcal D^{d}\!\left(L^{kl}\right)\right) L_{i}{}^{j} T_{bc} \bar\psi_{a}{}^{i} \gamma^{a} \gamma^{bc} \varphi_{j} +\frac{4}{L^{4}} E_{d} \epsilon^{jk}\left(L_{l(i} \mathcal D^{d}\!\left(L_{k)}{}^{l}\right)\right) T_{bc} \bar\psi_{a}{}^{i} \gamma^{a} \gamma^{bc} \varphi_{j}\\
&+\frac{1}{L^{4}} L^{j}{}_{k} \Box_c\!\left(L_{i}{}^{k}\right) \bar\psi_{a}{}^{i} \gamma^{a} \left(i \gamma^{b} E_{b} +N\right) \varphi_{j} - \frac{1}{L^{5}} L^{j}{}_{k} \mathcal D_{b}\!\left(L\right) \mathcal D^{b}\!\left(L_{i}{}^{k}\right) \bar\psi_{a}{}^{i} \gamma^{a} \left(i \gamma^{c} E_{c} +N\right) \varphi_{j} - \frac{1}{2 L^{2}} \left(4 D +\frac{8}{3} T_{bc} T^{bc} - \frac{1}{L^{2}} E_{b} E^{b} - \frac{N^{2}}{L^{2}} +\frac{1}{2 L^{2}} \mathcal D_{b}\!\left(L_{jk}\right) \mathcal D^{b}\!\left(L^{jk}\right)\right) \bar\psi_{a}{}^{i} \gamma^{a} \left(i \gamma^{d} E_{d} +N\right) \varphi_{i} - \frac{2}{L^{6}} E_{b} \left(L_{l(i} \mathcal D^{b}\!\left(L_{k)}{}^{l}\right)\right) L^{jk} \bar\psi_{a}{}^{i} \gamma^{a} \left(i \gamma^{c} E_{c} +N\right) \varphi_{j}\\
&+\frac{i}{L^{4}} L^{j}{}_{k} \Box_c\!\left(L_{il}\right) \mathcal D_{b}\!\left(L^{lk}\right) \bar\psi_{a}{}^{i} \gamma^{a} \gamma^{b} \varphi_{j} +\frac{i}{L^{5}} L^{j}{}_{k} \mathcal D_{c}\!\left(L\right) \mathcal D_{b}\!\left(L_{l}{}^{k}\right) \mathcal D^{c}\!\left(L_{i}{}^{l}\right) \bar\psi_{a}{}^{i} \gamma^{a} \gamma^{b} \varphi_{j} +\frac{i}{L^{4}} \left(4 D +\frac{8}{3} T_{cd} T^{cd} - \frac{1}{L^{2}} E_{c} E^{c} - \frac{N^{2}}{L^{2}} +\frac{1}{2 L^{2}} \mathcal D_{c}\!\left(L_{mn}\right) \mathcal D^{c}\!\left(L^{mn}\right)\right) L_{ik} L^{j}{}_{l} \mathcal D_{b}\!\left(L^{kl}\right) \bar\psi_{a}{}^{i} \gamma^{a} \gamma^{b} \varphi_{j} +\frac{2 i}{L^{6}} E_{c} \left(L_{m(i} \mathcal D^{c}\!\left(L_{k)}{}^{m}\right)\right) L^{j}{}_{l} \mathcal D_{b}\!\left(L^{kl}\right) \bar\psi_{a}{}^{i} \gamma^{a} \gamma^{b} \varphi_{j}\\
&- \frac{3 i N}{4 L^{2}} \widehat G_{cd} \mathcal D_{a}\!\left(\bar\varphi_{i}\right) \gamma^{a} \gamma^{b} \gamma^{cd} \psi_{b}{}^{i} - \frac{6 N}{L^{2}} \widehat G_{bc} L_{i}{}^{j} \bar\chi^{i} \gamma^{a} \gamma^{bc} \psi_{aj} +\frac{3 N}{2 L^{2}} \widehat G_{de} T_{ab} \bar\varphi^{i} \gamma^{ab} \gamma^{c} \gamma^{de} \psi_{ci} +\frac{3 N}{4 L^{4}} \widehat G_{bc} L_{i}{}^{j} \bar\varphi^{i} \left(i E_{d} \gamma^{d} +N\right) \gamma^{a} \gamma^{bc} \psi_{aj}\\
&- \frac{3 i N}{4 L^{4}} \widehat G_{cd} L_{ik} \mathcal D_{a}\!\left(L^{jk}\right) \bar\varphi^{i} \gamma^{a} \gamma^{b} \gamma^{cd} \psi_{bj} +\frac{3 i N}{L^{2}} T_{cd} \mathcal D_{a}\!\left(\bar\varphi_{i}\right) \gamma^{a} \gamma^{b} \gamma^{cd} \psi_{b}{}^{i} +\frac{24 N}{L^{2}} L_{i}{}^{j} T_{bc} \bar\chi^{i} \gamma^{a} \gamma^{bc} \psi_{aj} - \frac{6 N}{L^{2}} T_{ab} T_{de} \bar\varphi^{i} \gamma^{ab} \gamma^{c} \gamma^{de} \psi_{ci}\\
&- \frac{3 N}{L^{4}} L_{i}{}^{j} T_{bc} \bar\varphi^{i} \left(i E_{d} \gamma^{d} +N\right) \gamma^{a} \gamma^{bc} \psi_{aj} +\frac{3 i N}{L^{4}} L_{ik} \mathcal D_{a}\!\left(L^{jk}\right) T_{cd} \bar\varphi^{i} \gamma^{a} \gamma^{b} \gamma^{cd} \psi_{bj} +\frac{3 i N g}{2 L^{2}} L^{ij} \mathcal D_{a}\!\left(\bar\varphi_{i}\right) \gamma^{a} \gamma^{b} \psi_{bj} - 6 N g \bar\chi^{i} \gamma^{a} \psi_{ai}\\
&- \frac{3 N g}{L^{2}} L_{i}{}^{j} T_{ab} \bar\varphi^{i} \gamma^{ab} \gamma^{c} \psi_{cj} +\frac{3 N g}{4 L^{2}} \bar\varphi^{i} \left(i E_{b} \gamma^{b} +N\right) \gamma^{a} \psi_{ai} +\frac{3 i N g}{2 L^{4}} L_{ik} L^{j}{}_{l} \mathcal D_{a}\!\left(L^{lk}\right) \bar\varphi^{i} \gamma^{a} \gamma^{b} \psi_{bj} +\frac{3 i N}{L^{2}} \mathcal D_{a}\!\left(\bar\varphi_{i}\right) \gamma^{a} \gamma^{b} \phi_{b}{}^{i}\\
&+\frac{24 N}{L^{2}} L_{i}{}^{j} \bar\chi^{i} \gamma^{a} \phi_{aj} - \frac{6 N}{L^{2}} T_{ab} \bar\varphi^{i} \gamma^{ab} \gamma^{c} \phi_{ci} - \frac{3 N}{L^{4}} L_{i}{}^{j} \bar\varphi^{i} \left(i E_{b} \gamma^{b} +N\right) \gamma^{a} \phi_{aj} +\frac{3 i N}{L^{4}} L_{ik} \mathcal D_{a}\!\left(L^{jk}\right) \bar\varphi^{i} \gamma^{a} \gamma^{b} \phi_{bj}\\
&- \frac{1}{L} E_{a} \mathcal D_{b}\!\left(\left(4 \left(\mathcal D^{[a}\!\left(\frac{1}{L} E^{b]}\right)\right) +\frac{2}{L} L_{ij} \widehat R(V)^{abij} - \frac{2}{L^{3}} L_{i}{}^{j} \left(\mathcal D^{[a}\!\left(L^{ik}\right) \mathcal D^{b]}\!\left(L_{jk}\right)\right) +\frac{2 N}{L} \left(\widehat G^{ab} -16 T^{ab}\right)\right)\right) - \frac{1}{L} E^{b} \mathcal D_{a}\!\left(\left(-2 \eta^{ac}\left(\mathcal D_{[b}\!\left(\frac{1}{L^{3}} L_{mn} \bar\varphi^{m} \gamma_{c]} \varphi^{n}\right)\right) - \frac{i}{L} \bar\varphi^{i} \widehat R(Q)_{b}{}^{a}{}_{i} +\frac{i}{L^{3}} L_{ij} \bar\varphi^{i} \varphi^{j} \left(\widehat G_{b}{}^{a} -16 T_{b}{}^{a}\right)\right)\right) - \frac{\sqrt{2}}{2} \mathcal D_{a}\!\left(\left(4 \eta^{ac}\left(\mathcal D_{[b}\!\left(\frac{1}{L} E_{c]}\right)\right) +\frac{2}{L} L_{ij} \widehat R(V)_{b}{}^{aij} - \frac{2}{L^{3}} L_{i}{}^{j} \eta^{ad}\left(\mathcal D_{[b}\!\left(L^{ik}\right) \mathcal D_{d]}\!\left(L_{jk}\right)\right) +\frac{2 N}{L} \left(\widehat G_{b}{}^{a} -16 T_{b}{}^{a}\right)\right)\right) V^{b} - \frac{\sqrt{2}}{2} V^{b} \mathcal D_{a}\!\left(\left(-2 \eta^{ac}\left(\mathcal D_{[b}\!\left(\frac{1}{L^{3}} L_{mn} \bar\varphi^{m} \gamma_{c]} \varphi^{n}\right)\right) - \frac{i}{L} \bar\varphi^{i} \widehat R(Q)_{b}{}^{a}{}_{i} +\frac{i}{L^{3}} L_{ij} \bar\varphi^{i} \varphi^{j} \left(\widehat G_{b}{}^{a} -16 T_{b}{}^{a}\right)\right)\right)\\
&- \frac{1}{2 L^{3}} L_{i}{}^{j} \mathcal D_{b}\!\left(\left(4 \eta^{bc}\left(\mathcal D_{[a}\!\left(\frac{1}{L} E_{c]}\right)\right) +\frac{2}{L} L_{kl} \widehat R(V)_{a}{}^{bkl} - \frac{2}{L^{3}} L_{k}{}^{l} \eta^{bd}\left(\mathcal D_{[a}\!\left(L^{km}\right) \mathcal D_{d]}\!\left(L_{lm}\right)\right) +\frac{2 N}{L} \left(\widehat G_{a}{}^{b} -16 T_{a}{}^{b}\right)\right)\right) \bar\varphi^{i} \gamma^{a} \varphi_{j} +\frac{i}{2 L} \mathcal D_{b}\!\left(\left(4 \left(\mathcal D^{[a}\!\left(\frac{1}{L} E^{b]}\right)\right) +\frac{2}{L} L_{jk} \widehat R(V)^{abjk} - \frac{2}{L^{3}} L_{j}{}^{k} \left(\mathcal D^{[a}\!\left(L^{jl}\right) \mathcal D^{b]}\!\left(L_{kl}\right)\right) +\frac{2 N}{L} \left(\widehat G^{ab} -16 T^{ab}\right)\right)\right) \bar\varphi^{i} \psi_{ai} - \frac{1}{L} E_{a} \widehat G_{bc} \left(\mathcal D_{[d}\!\left(\frac{1}{L} E_{e]}\right)\right) \varepsilon^{abcde} - \frac{1}{2 L^{2}} E_{a} \widehat G_{bc} L_{ij} \widehat R(V)_{de}{}^{ij} \varepsilon^{abcde}\\
&- \frac{1}{2 L^{4}} E_{a} \widehat G_{bc} \left(\mathcal D_{[d}\!\left(L_{i}{}^{k}\right) \mathcal D_{e]}\!\left(L_{jk}\right)\right) L^{ij} \varepsilon^{abcde} +\frac{1}{2 L} E_{c} \widehat G_{de} \varepsilon^{abcde} \left(\mathcal D_{[a}\!\left(\frac{1}{L^{3}} L_{kl} \bar\varphi^{k} \gamma_{b]} \varphi^{l}\right)\right) +\frac{i}{4 L^{2}} E_{c} \widehat G_{de} \varepsilon^{abcde} \bar\varphi^{i} \widehat R(Q)_{abi} - \frac{\sqrt{2}}{2} \widehat G_{ab} \left(\mathcal D_{[c}\!\left(\frac{1}{L} E_{d]}\right)\right) V_{e} \varepsilon^{abcde}\\
&- \frac{\sqrt{2}}{4 L} \widehat G_{ab} L_{ij} \widehat R(V)_{cd}{}^{ij} V_{e} \varepsilon^{abcde} - \frac{\sqrt{2}}{4 L^{3}} \widehat G_{ab} \left(\mathcal D_{[c}\!\left(L_{i}{}^{k}\right) \mathcal D_{d]}\!\left(L_{jk}\right)\right) L^{ij} V_{e} \varepsilon^{abcde} +\frac{\sqrt{2}}{4} \widehat G_{cd} V_{e} \varepsilon^{abcde} \left(\mathcal D_{[a}\!\left(\frac{1}{L^{3}} L_{kl} \bar\varphi^{k} \gamma_{b]} \varphi^{l}\right)\right) +\frac{\sqrt{2} i}{8 L} \widehat G_{cd} V_{e} \varepsilon^{abcde} \bar\varphi^{i} \widehat R(Q)_{abi}\\
&- \frac{1}{2 L^{3}} \widehat G_{bc} \left(\mathcal D_{[d}\!\left(\frac{1}{L} E_{e]}\right)\right) L_{i}{}^{j} \varepsilon_{a}{}^{bcde} \bar\varphi^{i} \gamma^{a} \varphi_{j} - \frac{1}{4 L^{4}} \widehat G_{bc} L_{i}{}^{j} L_{kl} \widehat R(V)_{de}{}^{kl} \varepsilon_{a}{}^{bcde} \bar\varphi^{i} \gamma^{a} \varphi_{j} - \frac{1}{4 L^{6}} \widehat G_{bc} \left(\mathcal D_{[d}\!\left(L_{k}{}^{m}\right) \mathcal D_{e]}\!\left(L_{lm}\right)\right) L_{i}{}^{j} L^{kl} \varepsilon_{a}{}^{bcde} \bar\varphi^{i} \gamma^{a} \varphi_{j} +\frac{i}{2 L} \widehat G_{bc} \left(\mathcal D_{[d}\!\left(\frac{1}{L} E_{e]}\right)\right) \varepsilon^{abcde} \bar\varphi^{i} \psi_{ai}\\
&+\frac{i}{4 L^{2}} \widehat G_{bc} L_{jk} \widehat R(V)_{de}{}^{jk} \varepsilon^{abcde} \bar\varphi^{i} \psi_{ai} +\frac{i}{4 L^{4}} \widehat G_{bc} \left(\mathcal D_{[d}\!\left(L_{j}{}^{l}\right) \mathcal D_{e]}\!\left(L_{kl}\right)\right) L^{jk} \varepsilon^{abcde} \bar\varphi^{i} \psi_{ai} +\frac{1}{4 L^{2}} E_{b} \widehat G_{de} \mathcal D_{a}\!\left(\bar\varphi_{i}\right) \gamma^{a} \gamma^{bc} \gamma^{de} \psi_{c}{}^{i} - \frac{2 i}{L^{2}} E_{a} \widehat G_{cd} L_{i}{}^{j} \bar\chi^{i} \gamma^{ab} \gamma^{cd} \psi_{bj}\\
&+\frac{i}{2 L^{2}} E_{c} \widehat G_{ef} T_{ab} \bar\varphi^{i} \gamma^{ab} \gamma^{cd} \gamma^{ef} \psi_{di} +\frac{i}{4 L^{4}} E_{a} \widehat G_{cd} L_{i}{}^{j} \bar\varphi^{i} \left(i E_{e} \gamma^{e} +N\right) \gamma^{ab} \gamma^{cd} \psi_{bj} +\frac{1}{4 L^{4}} E_{b} \widehat G_{de} L_{ik} \mathcal D_{a}\!\left(L^{jk}\right) \bar\varphi^{i} \gamma^{a} \gamma^{bc} \gamma^{de} \psi_{cj} +\frac{\sqrt{2}}{8 L} \widehat G_{de} V_{b} \mathcal D_{a}\!\left(\bar\varphi_{i}\right) \gamma^{a} \gamma^{bc} \gamma^{de} \psi_{c}{}^{i}\\
&- \frac{\sqrt{2} i}{L} \widehat G_{cd} L_{i}{}^{j} V_{a} \bar\chi^{i} \gamma^{ab} \gamma^{cd} \psi_{bj} +\frac{\sqrt{2} i}{4 L} \widehat G_{ef} T_{ab} V_{c} \bar\varphi^{i} \gamma^{ab} \gamma^{cd} \gamma^{ef} \psi_{di} +\frac{\sqrt{2} i}{8 L^{3}} \widehat G_{cd} L_{i}{}^{j} V_{a} \bar\varphi^{i} \left(i E_{e} \gamma^{e} +N\right) \gamma^{ab} \gamma^{cd} \psi_{bj} +\frac{\sqrt{2}}{8 L^{3}} \widehat G_{de} L_{ik} \mathcal D_{a}\!\left(L^{jk}\right) V_{b} \bar\varphi^{i} \gamma^{a} \gamma^{bc} \gamma^{de} \psi_{cj}\\
&- \frac{1}{L^{2}} E_{b} T_{de} \mathcal D_{a}\!\left(\bar\varphi_{i}\right) \gamma^{a} \gamma^{bc} \gamma^{de} \psi_{c}{}^{i} +\frac{8 i}{L^{2}} E_{a} L_{i}{}^{j} T_{cd} \bar\chi^{i} \gamma^{ab} \gamma^{cd} \psi_{bj} - \frac{2 i}{L^{2}} E_{c} T_{ab} T_{ef} \bar\varphi^{i} \gamma^{ab} \gamma^{cd} \gamma^{ef} \psi_{di} - \frac{i}{L^{4}} E_{a} L_{i}{}^{j} T_{cd} \bar\varphi^{i} \left(i E_{e} \gamma^{e} +N\right) \gamma^{ab} \gamma^{cd} \psi_{bj}\\
&- \frac{1}{L^{4}} E_{b} L_{ik} \mathcal D_{a}\!\left(L^{jk}\right) T_{de} \bar\varphi^{i} \gamma^{a} \gamma^{bc} \gamma^{de} \psi_{cj} - \frac{\sqrt{2}}{2 L} T_{de} V_{b} \mathcal D_{a}\!\left(\bar\varphi_{i}\right) \gamma^{a} \gamma^{bc} \gamma^{de} \psi_{c}{}^{i} +\frac{4 \sqrt{2} i}{L} L_{i}{}^{j} T_{cd} V_{a} \bar\chi^{i} \gamma^{ab} \gamma^{cd} \psi_{bj} - \frac{\sqrt{2} i}{L} T_{ab} T_{ef} V_{c} \bar\varphi^{i} \gamma^{ab} \gamma^{cd} \gamma^{ef} \psi_{di}\\
&- \frac{\sqrt{2} i}{2 L^{3}} L_{i}{}^{j} T_{cd} V_{a} \bar\varphi^{i} \left(i E_{e} \gamma^{e} +N\right) \gamma^{ab} \gamma^{cd} \psi_{bj} - \frac{\sqrt{2}}{2 L^{3}} L_{ik} \mathcal D_{a}\!\left(L^{jk}\right) T_{de} V_{b} \bar\varphi^{i} \gamma^{a} \gamma^{bc} \gamma^{de} \psi_{cj} - \frac{g}{2 L^{2}} E_{b} L^{ij} \mathcal D_{a}\!\left(\bar\varphi_{i}\right) \gamma^{a} \gamma^{bc} \psi_{cj} - 2 i g E_{a} \bar\chi^{i} \gamma^{ab} \psi_{bi}\\
&- \frac{i g}{L^{2}} E_{c} L_{i}{}^{j} T_{ab} \bar\varphi^{i} \gamma^{ab} \gamma^{cd} \psi_{dj} +\frac{i g}{4 L^{2}} E_{a} \bar\varphi^{i} \left(i E_{c} \gamma^{c} +N\right) \gamma^{ab} \psi_{bi} - \frac{g}{2 L^{4}} E_{b} L_{ik} L^{j}{}_{l} \mathcal D_{a}\!\left(L^{lk}\right) \bar\varphi^{i} \gamma^{a} \gamma^{bc} \psi_{cj} - \frac{\sqrt{2} g}{4 L} L^{ij} V_{b} \mathcal D_{a}\!\left(\bar\varphi_{i}\right) \gamma^{a} \gamma^{bc} \psi_{cj}\\
&- \sqrt{2} i L g V_{a} \bar\chi^{i} \gamma^{ab} \psi_{bi} - \frac{\sqrt{2} i g}{2 L} L_{i}{}^{j} T_{ab} V_{c} \bar\varphi^{i} \gamma^{ab} \gamma^{cd} \psi_{dj} +\frac{\sqrt{2} i g}{8 L} V_{a} \bar\varphi^{i} \left(i E_{c} \gamma^{c} +N\right) \gamma^{ab} \psi_{bi} - \frac{\sqrt{2} g}{4 L^{3}} L_{ik} L^{j}{}_{l} \mathcal D_{a}\!\left(L^{lk}\right) V_{b} \bar\varphi^{i} \gamma^{a} \gamma^{bc} \psi_{cj}\\
&- \frac{1}{L^{2}} E_{b} \mathcal D_{a}\!\left(\bar\varphi_{i}\right) \gamma^{a} \gamma^{bc} \phi_{c}{}^{i} +\frac{8 i}{L^{2}} E_{a} L_{i}{}^{j} \bar\chi^{i} \gamma^{ab} \phi_{bj} - \frac{2 i}{L^{2}} E_{c} T_{ab} \bar\varphi^{i} \gamma^{ab} \gamma^{cd} \phi_{di} - \frac{i}{L^{4}} E_{a} L_{i}{}^{j} \bar\varphi^{i} \left(i E_{c} \gamma^{c} +N\right) \gamma^{ab} \phi_{bj}\\
&- \frac{1}{L^{4}} E_{b} L_{ik} \mathcal D_{a}\!\left(L^{jk}\right) \bar\varphi^{i} \gamma^{a} \gamma^{bc} \phi_{cj} - \frac{\sqrt{2}}{2 L} V_{b} \mathcal D_{a}\!\left(\bar\varphi_{i}\right) \gamma^{a} \gamma^{bc} \phi_{c}{}^{i} +\frac{4 \sqrt{2} i}{L} L_{i}{}^{j} V_{a} \bar\chi^{i} \gamma^{ab} \phi_{bj} - \frac{\sqrt{2} i}{L} T_{ab} V_{c} \bar\varphi^{i} \gamma^{ab} \gamma^{cd} \phi_{di}\\
&- \frac{\sqrt{2} i}{2 L^{3}} L_{i}{}^{j} V_{a} \bar\varphi^{i} \left(i E_{c} \gamma^{c} +N\right) \gamma^{ab} \phi_{bj} - \frac{\sqrt{2}}{2 L^{3}} L_{ik} \mathcal D_{a}\!\left(L^{jk}\right) V_{b} \bar\varphi^{i} \gamma^{a} \gamma^{bc} \phi_{cj} - \frac{N}{4 L^{2}} E_{b} \widehat G_{de} \bar\psi_{a}{}^{i} \gamma^{ab} \gamma^{c} \gamma^{de} \psi_{ci} - \frac{\sqrt{2} N}{8 L} \widehat G_{de} V_{b} \bar\psi_{a}{}^{i} \gamma^{ab} \gamma^{c} \gamma^{de} \psi_{ci}\\
&+\frac{N}{L^{2}} E_{b} T_{de} \bar\psi_{a}{}^{i} \gamma^{ab} \gamma^{c} \gamma^{de} \psi_{ci} +\frac{\sqrt{2} N}{2 L} T_{de} V_{b} \bar\psi_{a}{}^{i} \gamma^{ab} \gamma^{c} \gamma^{de} \psi_{ci} +\frac{N g}{2 L^{2}} E_{b} L_{i}{}^{j} \bar\psi_{a}{}^{i} \gamma^{ab} \gamma^{c} \psi_{cj} +\frac{\sqrt{2} N g}{4 L} L_{i}{}^{j} V_{b} \bar\psi_{a}{}^{i} \gamma^{ab} \gamma^{c} \psi_{cj}\\
&+\frac{N}{L^{2}} E_{b} \bar\psi_{a}{}^{i} \gamma^{ab} \gamma^{c} \phi_{ci} +\frac{\sqrt{2} N}{2 L} V_{b} \bar\psi_{a}{}^{i} \gamma^{ab} \gamma^{c} \phi_{ci} +\frac{i}{L} E_{b} \bar\psi_{a}{}^{i} \gamma^{ab} \gamma^{c} \mathcal D_{c}\!\left(\frac{1}{L} \gamma^{d} \mathcal D_{d}\!\left(\varphi_{i}\right)\right) - \frac{8}{L} E_{b} \bar\psi_{a}{}^{i} \gamma^{ab} \gamma^{c} \mathcal D_{c}\!\left(\frac{1}{L} L_{ij} \chi^{j}\right)\\
&- \frac{2}{L} E_{b} \bar\psi_{a}{}^{i} \gamma^{ab} \gamma^{c} \mathcal D_{c}\!\left(\frac{1}{L} \gamma^{de} T_{de} \varphi_{i}\right) +\frac{1}{L} E_{b} \bar\psi_{a}{}^{i} \gamma^{ab} \gamma^{c} \mathcal D_{c}\!\left(\frac{1}{L^{3}} L_{ij} \left(i \gamma^{d} E_{d} +N\right) \varphi^{j}\right) - \frac{i}{L} E_{b} \bar\psi_{a}{}^{i} \gamma^{ab} \gamma^{c} \mathcal D_{c}\!\left(\frac{1}{L^{3}} \gamma^{d} \mathcal D_{d}\!\left(L_{ij}\right) L^{jk} \varphi_{k}\right) +\frac{\sqrt{2} i}{2} V_{b} \bar\psi_{a}{}^{i} \gamma^{ab} \gamma^{c} \mathcal D_{c}\!\left(\frac{1}{L} \gamma^{d} \mathcal D_{d}\!\left(\varphi_{i}\right)\right)\\
&- 4 \sqrt{2} V_{b} \bar\psi_{a}{}^{i} \gamma^{ab} \gamma^{c} \mathcal D_{c}\!\left(\frac{1}{L} L_{ij} \chi^{j}\right) - \sqrt{2} V_{b} \bar\psi_{a}{}^{i} \gamma^{ab} \gamma^{c} \mathcal D_{c}\!\left(\frac{1}{L} \gamma^{de} T_{de} \varphi_{i}\right) +\frac{\sqrt{2}}{2} V_{b} \bar\psi_{a}{}^{i} \gamma^{ab} \gamma^{c} \mathcal D_{c}\!\left(\frac{1}{L^{3}} L_{ij} \left(i \gamma^{d} E_{d} +N\right) \varphi^{j}\right) - \frac{\sqrt{2} i}{2} V_{b} \bar\psi_{a}{}^{i} \gamma^{ab} \gamma^{c} \mathcal D_{c}\!\left(\frac{1}{L^{3}} \gamma^{d} \mathcal D_{d}\!\left(L_{ij}\right) L^{jk} \varphi_{k}\right)\\
&+\frac{2}{L^{2}} E_{b} T_{cd} \bar\psi_{a}{}^{i} \gamma^{ab} \gamma^{cd} \gamma^{e} \mathcal D_{e}\!\left(\varphi_{i}\right) - \frac{16 i}{L^{2}} E_{b} L_{i}{}^{j} T_{cd} \bar\psi_{a}{}^{i} \gamma^{ab} \gamma^{cd} \chi_{j} +\frac{4 i}{L^{2}} E_{b} T_{cd} T_{ef} \bar\psi_{a}{}^{i} \gamma^{ab} \gamma^{cd} \gamma^{ef} \varphi_{i} +\frac{2 i}{L^{4}} E_{b} L_{i}{}^{j} T_{cd} \bar\psi_{a}{}^{i} \gamma^{ab} \gamma^{cd} \left(i \gamma^{e} E_{e} +N\right) \varphi_{j}\\
&+\frac{2}{L^{4}} E_{b} L^{j}{}_{k} \mathcal D_{e}\!\left(L_{i}{}^{k}\right) T_{cd} \bar\psi_{a}{}^{i} \gamma^{ab} \gamma^{cd} \gamma^{e} \varphi_{j} +\frac{\sqrt{2}}{L} T_{cd} V_{b} \bar\psi_{a}{}^{i} \gamma^{ab} \gamma^{cd} \gamma^{e} \mathcal D_{e}\!\left(\varphi_{i}\right) - \frac{8 \sqrt{2} i}{L} L_{i}{}^{j} T_{cd} V_{b} \bar\psi_{a}{}^{i} \gamma^{ab} \gamma^{cd} \chi_{j} +\frac{2 \sqrt{2} i}{L} T_{cd} T_{ef} V_{b} \bar\psi_{a}{}^{i} \gamma^{ab} \gamma^{cd} \gamma^{ef} \varphi_{i}\\
&+\frac{\sqrt{2} i}{L^{3}} L_{i}{}^{j} T_{cd} V_{b} \bar\psi_{a}{}^{i} \gamma^{ab} \gamma^{cd} \left(i \gamma^{e} E_{e} +N\right) \varphi_{j} +\frac{\sqrt{2}}{L^{3}} L^{j}{}_{k} \mathcal D_{e}\!\left(L_{i}{}^{k}\right) T_{cd} V_{b} \bar\psi_{a}{}^{i} \gamma^{ab} \gamma^{cd} \gamma^{e} \varphi_{j} - \frac{2 i \left(L^{2} g + 8 N\right)}{L^{2}} E_{b} \bar\psi_{a}{}^{i} \gamma^{ab} \chi_{i} - \frac{\sqrt{2} i \left(L^{2} g + 8 N\right)}{L} V_{b} \bar\psi_{a}{}^{i} \gamma^{ab} \chi_{i}\\
&- \frac{1}{4 L^{2}} E_{b} \widehat G_{cd} \bar\psi_{a}{}^{i} \gamma^{ab} \gamma^{cd} \gamma^{e} \mathcal D_{e}\!\left(\varphi_{i}\right) +\frac{2 i}{L^{2}} E_{b} \widehat G_{cd} L_{i}{}^{j} \bar\psi_{a}{}^{i} \gamma^{ab} \gamma^{cd} \chi_{j} - \frac{i}{2 L^{2}} E_{b} \widehat G_{cd} T_{ef} \bar\psi_{a}{}^{i} \gamma^{ab} \gamma^{cd} \gamma^{ef} \varphi_{i} - \frac{i}{4 L^{4}} E_{b} \widehat G_{cd} L_{i}{}^{j} \bar\psi_{a}{}^{i} \gamma^{ab} \gamma^{cd} \left(i \gamma^{e} E_{e} +N\right) \varphi_{j}\\
&- \frac{1}{4 L^{4}} E_{b} \widehat G_{cd} L^{j}{}_{k} \mathcal D_{e}\!\left(L_{i}{}^{k}\right) \bar\psi_{a}{}^{i} \gamma^{ab} \gamma^{cd} \gamma^{e} \varphi_{j} - \frac{\sqrt{2}}{8 L} \widehat G_{cd} V_{b} \bar\psi_{a}{}^{i} \gamma^{ab} \gamma^{cd} \gamma^{e} \mathcal D_{e}\!\left(\varphi_{i}\right) +\frac{\sqrt{2} i}{L} \widehat G_{cd} L_{i}{}^{j} V_{b} \bar\psi_{a}{}^{i} \gamma^{ab} \gamma^{cd} \chi_{j} - \frac{\sqrt{2} i}{4 L} \widehat G_{cd} T_{ef} V_{b} \bar\psi_{a}{}^{i} \gamma^{ab} \gamma^{cd} \gamma^{ef} \varphi_{i}\\
&- \frac{\sqrt{2} i}{8 L^{3}} \widehat G_{cd} L_{i}{}^{j} V_{b} \bar\psi_{a}{}^{i} \gamma^{ab} \gamma^{cd} \left(i \gamma^{e} E_{e} +N\right) \varphi_{j} - \frac{\sqrt{2}}{8 L^{3}} \widehat G_{cd} L^{j}{}_{k} \mathcal D_{e}\!\left(L_{i}{}^{k}\right) V_{b} \bar\psi_{a}{}^{i} \gamma^{ab} \gamma^{cd} \gamma^{e} \varphi_{j} - \frac{g}{2 L^{2}} E_{b} L_{i}{}^{j} \bar\psi_{a}{}^{i} \gamma^{ab} \gamma^{c} \mathcal D_{c}\!\left(\varphi_{j}\right) - \frac{i g}{L^{2}} E_{b} L_{i}{}^{j} T_{cd} \bar\psi_{a}{}^{i} \gamma^{ab} \gamma^{cd} \varphi_{j}\\
&+\frac{i g}{4 L^{2}} E_{b} \bar\psi_{a}{}^{i} \gamma^{ab} \left(i \gamma^{c} E_{c} +N\right) \varphi_{i} +\frac{g}{2 L^{4}} E_{b} L_{ik} L^{j}{}_{l} \mathcal D_{c}\!\left(L^{kl}\right) \bar\psi_{a}{}^{i} \gamma^{ab} \gamma^{c} \varphi_{j} - \frac{\sqrt{2} g}{4 L} L_{i}{}^{j} V_{b} \bar\psi_{a}{}^{i} \gamma^{ab} \gamma^{c} \mathcal D_{c}\!\left(\varphi_{j}\right) - \frac{\sqrt{2} i g}{2 L} L_{i}{}^{j} T_{cd} V_{b} \bar\psi_{a}{}^{i} \gamma^{ab} \gamma^{cd} \varphi_{j}\\
&+\frac{\sqrt{2} i g}{8 L} V_{b} \bar\psi_{a}{}^{i} \gamma^{ab} \left(i \gamma^{c} E_{c} +N\right) \varphi_{i} +\frac{\sqrt{2} g}{4 L^{3}} L_{ik} L^{j}{}_{l} \mathcal D_{c}\!\left(L^{kl}\right) V_{b} \bar\psi_{a}{}^{i} \gamma^{ab} \gamma^{c} \varphi_{j} - \frac{N g}{2 L^{2}} E_{b} L_{i}{}^{j} \bar\psi_{a}{}^{i} \gamma^{abc} \psi_{cj} - \frac{\sqrt{2} N g}{4 L} L_{i}{}^{j} V_{b} \bar\psi_{a}{}^{i} \gamma^{abc} \psi_{cj}\\
&+\frac{1}{2 L^{2}} E_{b} \Box_c\!\left(L_{i}{}^{j}\right) \bar\psi_{a}{}^{i} \gamma^{abc} \psi_{cj} - \frac{1}{2 L^{3}} E_{b} \mathcal D_{d}\!\left(L\right) \mathcal D^{d}\!\left(L_{i}{}^{j}\right) \bar\psi_{a}{}^{i} \gamma^{abc} \psi_{cj} +\frac{1}{2 L^{2}} E_{b} \left(4 D +\frac{8}{3} T_{de} T^{de} - \frac{1}{L^{2}} E_{d} E^{d} - \frac{N^{2}}{L^{2}} +\frac{1}{2 L^{2}} \mathcal D_{d}\!\left(L_{kl}\right) \mathcal D^{d}\!\left(L^{kl}\right)\right) L_{i}{}^{j} \bar\psi_{a}{}^{i} \gamma^{abc} \psi_{cj} +\frac{1}{L^{4}} E_{b} E_{d} \epsilon^{jk}\left(L_{l(i} \mathcal D^{d}\!\left(L_{k)}{}^{l}\right)\right) \bar\psi_{a}{}^{i} \gamma^{abc} \psi_{cj}\\
&+\frac{\sqrt{2}}{4 L} \Box_c\!\left(L_{i}{}^{j}\right) V_{b} \bar\psi_{a}{}^{i} \gamma^{abc} \psi_{cj} - \frac{\sqrt{2}}{4 L^{2}} \mathcal D_{d}\!\left(L\right) \mathcal D^{d}\!\left(L_{i}{}^{j}\right) V_{b} \bar\psi_{a}{}^{i} \gamma^{abc} \psi_{cj} +\frac{\sqrt{2}}{4 L} \left(4 D +\frac{8}{3} T_{de} T^{de} - \frac{1}{L^{2}} E_{d} E^{d} - \frac{N^{2}}{L^{2}} +\frac{1}{2 L^{2}} \mathcal D_{d}\!\left(L_{kl}\right) \mathcal D^{d}\!\left(L^{kl}\right)\right) L_{i}{}^{j} V_{b} \bar\psi_{a}{}^{i} \gamma^{abc} \psi_{cj} +\frac{\sqrt{2}}{2 L^{3}} E_{d} \epsilon^{jk}\left(L_{l(i} \mathcal D^{d}\!\left(L_{k)}{}^{l}\right)\right) V_{b} \bar\psi_{a}{}^{i} \gamma^{abc} \psi_{cj}\\
&+\frac{2 N}{L} \Box_c\!\left(\frac{N}{L}\right) +\frac{i N}{L} \Box_c\!\left(\frac{1}{L^{3}} L_{ij} \bar\varphi^{i} \varphi^{j}\right) - \frac{i}{L^{3}} L_{i}{}^{j} \Box_c\!\left(\frac{N}{L}\right) \bar\varphi^{i} \varphi_{j} +\frac{4 N^{2}}{L^{2}} f_{a}{}^{a}\\
&- \frac{4 i N}{L^{4}} L_{i}{}^{j} f_{a}{}^{a} \bar\varphi^{i} \varphi_{j} - \frac{2 N}{L} \left(\widehat G_{ab} -16 T_{ab}\right) \left(\mathcal D^{[a}\!\left(\frac{1}{L} E^{b]}\right)\right) - \frac{N}{L^{2}} \left(\widehat G_{ab} -16 T_{ab}\right) L_{ij} \widehat R(V)^{abij} - \frac{N}{L^{4}} \left(\widehat G_{ab} -16 T_{ab}\right) \left(\mathcal D^{[a}\!\left(L_{i}{}^{k}\right) \mathcal D^{b]}\!\left(L_{jk}\right)\right) L^{ij}\\
&+\frac{N}{L} \left(\widehat G^{ab} -16 T^{ab}\right) \left(\mathcal D_{[a}\!\left(\frac{1}{L^{3}} L_{kl} \bar\varphi^{k} \gamma_{b]} \varphi^{l}\right)\right) +\frac{i N}{2 L^{2}} \left(\widehat G^{ab} -16 T^{ab}\right) \bar\varphi^{i} \widehat R(Q)_{abi} +\frac{i}{L^{3}} \left(\widehat G_{ab} -16 T_{ab}\right) \left(\mathcal D^{[a}\!\left(\frac{1}{L} E^{b]}\right)\right) L_{i}{}^{j} \bar\varphi^{i} \varphi_{j} +\frac{i}{2 L^{4}} \left(\widehat G_{ab} -16 T_{ab}\right) L_{i}{}^{j} L_{kl} \widehat R(V)^{abkl} \bar\varphi^{i} \varphi_{j}\\
&+\frac{i}{2 L^{6}} \left(\widehat G_{ab} -16 T_{ab}\right) \left(\mathcal D^{[a}\!\left(L_{k}{}^{m}\right) \mathcal D^{b]}\!\left(L_{lm}\right)\right) L_{i}{}^{j} L^{kl} \bar\varphi^{i} \varphi_{j} +\frac{16 N^{2}}{L^{2}} \widehat G_{ab} T^{ab} - \frac{16 i N}{L^{4}} \widehat G_{ab} L_{i}{}^{j} T^{ab} \bar\varphi^{i} \varphi_{j} - \frac{16 N^{2}}{L^{2}} D\\
&+\frac{16 i N}{L^{4}} D L_{i}{}^{j} \bar\varphi^{i} \varphi_{j} - \frac{416 N^{2}}{3 L^{2}} T_{ab} T^{ab} +\frac{416 i N}{3 L^{4}} L_{i}{}^{j} T_{ab} T^{ab} \bar\varphi^{i} \varphi_{j} +\frac{N}{L} \bar\psi_{a}{}^{i} \gamma^{a} \gamma^{b} \mathcal D_{b}\!\left(\frac{1}{L} \gamma^{c} \mathcal D_{c}\!\left(\varphi_{i}\right)\right)\\
&+\frac{8 i N}{L} \bar\psi_{a}{}^{i} \gamma^{a} \gamma^{b} \mathcal D_{b}\!\left(\frac{1}{L} L_{ij} \chi^{j}\right) +\frac{2 i N}{L} \bar\psi_{a}{}^{i} \gamma^{a} \gamma^{b} \mathcal D_{b}\!\left(\frac{1}{L} \gamma^{cd} T_{cd} \varphi_{i}\right) - \frac{i N}{L} \bar\psi_{a}{}^{i} \gamma^{a} \gamma^{b} \mathcal D_{b}\!\left(\frac{1}{L^{3}} L_{ij} \left(i \gamma^{c} E_{c} +N\right) \varphi^{j}\right) - \frac{N}{L} \bar\psi_{a}{}^{i} \gamma^{a} \gamma^{b} \mathcal D_{b}\!\left(\frac{1}{L^{3}} \gamma^{c} \mathcal D_{c}\!\left(L_{ij}\right) L^{jk} \varphi_{k}\right)\\
&- \frac{2 i N}{L^{2}} T_{bc} \bar\psi_{a}{}^{i} \gamma^{a} \gamma^{bc} \gamma^{d} \mathcal D_{d}\!\left(\varphi_{i}\right) - \frac{16 N}{L^{2}} L_{i}{}^{j} T_{bc} \bar\psi_{a}{}^{i} \gamma^{a} \gamma^{bc} \chi_{j} +\frac{4 N}{L^{2}} T_{bc} T_{de} \bar\psi_{a}{}^{i} \gamma^{a} \gamma^{bc} \gamma^{de} \varphi_{i} +\frac{2 N}{L^{4}} L_{i}{}^{j} T_{bc} \bar\psi_{a}{}^{i} \gamma^{a} \gamma^{bc} \left(i \gamma^{d} E_{d} +N\right) \varphi_{j}\\
&- \frac{2 i N}{L^{4}} L^{j}{}_{k} \mathcal D_{d}\!\left(L_{i}{}^{k}\right) T_{bc} \bar\psi_{a}{}^{i} \gamma^{a} \gamma^{bc} \gamma^{d} \varphi_{j} +\frac{i N}{4 L^{2}} \widehat G_{bc} \bar\psi_{a}{}^{i} \gamma^{a} \gamma^{bc} \gamma^{d} \mathcal D_{d}\!\left(\varphi_{i}\right) +\frac{2 N}{L^{2}} \widehat G_{bc} L_{i}{}^{j} \bar\psi_{a}{}^{i} \gamma^{a} \gamma^{bc} \chi_{j} - \frac{N}{2 L^{2}} \widehat G_{bc} T_{de} \bar\psi_{a}{}^{i} \gamma^{a} \gamma^{bc} \gamma^{de} \varphi_{i}\\
&- \frac{N}{4 L^{4}} \widehat G_{bc} L_{i}{}^{j} \bar\psi_{a}{}^{i} \gamma^{a} \gamma^{bc} \left(i \gamma^{d} E_{d} +N\right) \varphi_{j} +\frac{i N}{4 L^{4}} \widehat G_{bc} L^{j}{}_{k} \mathcal D_{d}\!\left(L_{i}{}^{k}\right) \bar\psi_{a}{}^{i} \gamma^{a} \gamma^{bc} \gamma^{d} \varphi_{j} +\frac{i N^{2}}{4 L^{2}} \widehat G_{cd} \bar\psi_{a}{}^{i} \gamma^{ab} \gamma^{cd} \psi_{bi} - \frac{i N^{2}}{L^{2}} T_{cd} \bar\psi_{a}{}^{i} \gamma^{ab} \gamma^{cd} \psi_{bi}\\
&- \frac{i N^{2}}{L^{2}} \bar\psi_{a}{}^{i} \gamma^{ab} \phi_{bi} - \frac{i N}{2 L^{2}} \Box_c\!\left(L_{i}{}^{j}\right) \bar\psi_{a}{}^{i} \gamma^{ab} \psi_{bj} +\frac{i N}{2 L^{3}} \mathcal D_{c}\!\left(L\right) \mathcal D^{c}\!\left(L_{i}{}^{j}\right) \bar\psi_{a}{}^{i} \gamma^{ab} \psi_{bj} - \frac{i N}{2 L^{2}} \left(4 D +\frac{8}{3} T_{cd} T^{cd} - \frac{1}{L^{2}} E_{c} E^{c} - \frac{N^{2}}{L^{2}} +\frac{1}{2 L^{2}} \mathcal D_{c}\!\left(L_{kl}\right) \mathcal D^{c}\!\left(L^{kl}\right)\right) L_{i}{}^{j} \bar\psi_{a}{}^{i} \gamma^{ab} \psi_{bj}\\
&- \frac{i N}{L^{4}} E_{c} \epsilon^{jk}\left(L_{l(i} \mathcal D^{c}\!\left(L_{k)}{}^{l}\right)\right) \bar\psi_{a}{}^{i} \gamma^{ab} \psi_{bj}
\end{aligned}\Bigg\}
\end{aligned}\right\}_{\leq2}.
\tag{S}
```

The sum is the off-shell action on the common source gauge slice, exact in bosons and through quadratic fermions. This equality is not a new proof of SUSY invariance or reality of the source actions.
