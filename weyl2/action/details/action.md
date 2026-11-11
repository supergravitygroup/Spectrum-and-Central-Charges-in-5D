# Total action: common conventions and fixed coefficients

This file fixes the total action **through two-fermion order**
in the common gauge specified for this analysis:

```math
\sigma=1,\qquad \psi^i=0,\qquad b_\mu=0,\qquad
L_{ij}=\frac{L}{\sqrt2}\delta_{ij},\qquad
V_\mu^{ij}=V_\mu^{\prime\,ij}+\frac12\delta^{ij}V_\mu,\qquad
\delta_{ij}V_\mu^{\prime\,ij}=0 .
\tag{P}
```

The two-derivative sector is **(5.10)** of the first file. The Weyl-squared
sector is the projection of **(GA24)** of the second file to the same gauge
and fermion order. Intrasector coefficients of both files are retained;
the entire Weyl-squared sector is multiplied by the generic nonzero
constant $`\alpha`$. $`\alpha`$ is not a perturbative parameter. No additional
truncation is made in bosons, $`g`$, $`\alpha`$, or derivatives; no auxiliary-field
equation of motion is used.

This file fixes the conversion of the two supplied action expressions to
common conventions and their sum. It does not claim a complete independent
SUSY certification of the source maps. Inclusion of fermions inside hatted
objects in the two-fermion calculation is defined in §8 by an exact
coefficient-selection operation.

<a id="1-common-fields-and-normalization"></a>

## Common fields and normalization

Sources:

- [Two-derivative action](../../../common/two_derivative_action/details/construction.md):
  (5.10); component definitions in (3.1)–(3.14), (4.5),
  (4.9), and (4.27)–(4.37).
- [Weyl-squared action](construction.md):
  (GA01)–(GA03), (GC03)–(GC24), and (GA24).
- [Project conventions](../../../common/details/source_conventions.md): common metric, index, spinor,
  curvature, and supercovariant-derivative definitions.

The compensator role label in the second file is removed:

```math
(L_c^{ij},\varphi_c^i,E_c^a,N_c,E_{c\,\mu\nu\rho})
\longmapsto
(L^{ij},\varphi^i,E^a,N,E_{\mu\nu\rho}).
\tag{A1}
```

This identification changes neither coefficients nor signs. The $`W`$ label
of the Weyl-composite linear multiplet is retained: $`(L_W^{ij},\varphi_W^i,E_W^a,N_W)`$ differs from
the compensator. $`\psi^i`$ is the dilatino, $`\psi_\mu^i`$ the gravitino,
$`\varphi^i`$ the compensator fermion, and $`\phi_\mu^i`$ the dependent $`S`$ connection.

```math
\begin{gathered}
e=\det(e_\mu{}^a)=\sqrt{-g},\qquad
g_{\mu\nu}=e_\mu{}^ae_\nu{}^b\eta_{ab},\qquad
\eta_{ab}=\mathop{\mathrm{diag}}\nolimits(-,+,+,+,+),\\
L^{ij}L_{ij}=\frac{L^2}{2}\delta^{ij}\delta_{ij}=L^2,\qquad L\ne0,\qquad
g\in\mathbb R,\quad \partial_\mu g=0,\quad g\ne0,\qquad
\alpha\ne0,\quad \partial_\mu\alpha=0.
\end{gathered}
\tag{A2}
```

$`L`$ is the same scalar field as in source (5.10); the map involving $`L^{-1}`$
is used on the $`L\ne0`$ patch. Pregauge expressions for $`\sigma^{-1}`$ are evaluated
with $`\sigma=1`$ after their derivatives are calculated. Neither $`L`$, $`g`$,
nor any fermion is rescaled. $`\alpha`$ is the independent relative coefficient
of the Weyl-squared action; it is not absorbed into the sectors' own
normalizations. No Newton-constant factor or overall factor of two is added:

```math
\mathcal L_{\rm total}^{(\le2)}
=\mathcal L_{2\partial}^{(\le2)}
+\alpha\,\Pi_{\le2}\!\left[
 \left.\mathcal L_{\sigma C^2,g}^{\rm map}\right|_{\rm P}\right].
\tag{A3}
```

Equivalent action definition:

```math
\boxed{
S_{\rm total}^{(\le2)}
=S_{2\text{-der}}^{(\le2)}
+\alpha S_{\mathrm{Weyl}^2}^{(\le2)},
\qquad \alpha\ne0,\quad \partial_\mu\alpha=0 .
}
\tag{A3S}
```

No smallness assumption or series expansion is made in $`\alpha`$.
By definition, the $`\alpha`$ dependence of this sum is exact; the
fermion-order projection is independent of $`\alpha`$.

<a id="2-spinors-epsilon-and-index-conversions"></a>

## Spinors, epsilon, and index conversions

```math
\begin{gathered}
X_{[ab]}=\tfrac12(X_{ab}-X_{ba}),\qquad
\{\gamma^a,\gamma^b\}=2\eta^{ab},\qquad
\gamma^{a_1\cdots a_p}=\gamma^{[a_1}\cdots\gamma^{a_p]},\\
\gamma\!\cdot T=\gamma^{ab}T_{ab},\qquad
\mathord{\not{\mathcal D}}=\gamma^a\mathcal D_a,\qquad
\mathord{\not{E}}=\gamma^aE_a,\\
\epsilon_{12}=\epsilon^{12}=1,\qquad
X^i=\epsilon^{ij}X_j,\qquad X_i=X^j\epsilon_{ji},\\
L^{ij}=\epsilon^{ik}\epsilon^{j\ell}L_{k\ell},\qquad
L_i{}^j=\epsilon^{jk}L_{ik},\qquad
L^i{}_j=\epsilon^{ik}L_{kj},\qquad
\bar X\Gamma Y=\bar X^i\Gamma Y_i .
\end{gathered}
\tag{A4}
```

Antisymmetric index contractions are full sums without $`1/p!`$.
The NW–SE contraction sign is explicitly

```math
\begin{aligned}
\bar X^i\gamma_{(n)}Y_i
&=\epsilon_{ji}\bar X^i\gamma_{(n)}Y^j
=t_n\epsilon_{ji}\bar Y^j\gamma_{(n)}X^i\\
&=-t_n\bar Y^j\gamma_{(n)}X_j,\\
(t_0,t_1,t_2,t_3,t_4,t_5)&=(+1,+1,-1,-1,+1,+1)
\end{aligned}
\tag{A5}
```

The spinor ordering of both files is consistent with this rule.
The linear Majorana bar in the sources can be used consistently with
the project's open-index flip rule. For an arbitrary test spinor $`Z`$
and even scalar $`c`$,

```math
\begin{aligned}
\overline{cX}^{\,i}Z^j
&=\bar Z^j(cX^i)=c\,\bar X^iZ^j,\\
\overline{\gamma_{(n)}X}^{\,i}Z^j
&=\bar Z^j\gamma_{(n)}X^i
=t_n\bar X^i\gamma_{(n)}Z^j.
\end{aligned}
\tag{A6}
```

Thus $`i`$ under the bar is not antilinearly conjugated to $`-i`$;
the bar of a rank-two gamma matrix carries a minus sign. This operation
neither selects a Dirac-bar phase nor proves reality of the action.

Since the project conventions do not fix orientation numerically,
the Weyl-squared file's notation $`\varepsilon^{01234}=+1`$ is replaced throughout by
the same symbolic epsilon and its associated Clifford orientation:

```math
\begin{gathered}
\gamma^{abcde}=i\varepsilon^{abcde}\mathbf1,\qquad
\varepsilon_{a_1\cdots a_n b_1\cdots b_p}
\varepsilon^{a_1\cdots a_n c_1\cdots c_p}
=-n!p!\,\delta_{[b_1}^{c_1}\cdots\delta_{b_p]}^{c_p},
\quad n+p=5,\\
\varepsilon^{\mu\nu\rho\sigma\lambda}
=e_a{}^\mu e_b{}^\nu e_c{}^\rho e_d{}^\sigma e_f{}^\lambda
 \varepsilon^{abcdf},\qquad
\epsilon^{\mu\nu\rho\sigma\lambda}
=e\,\varepsilon^{\mu\nu\rho\sigma\lambda}.
\end{gathered}
\tag{A7}
```

This is not a field transformation reversing only the epsilon sign.
Coefficients of action terms with tangent epsilon remain unchanged.
The two-index SU(2) symbols $`\varepsilon^{ij}`$ and $`\varepsilon_{ij}`$ in the sources are written
as $`\epsilon^{ij}`$ and $`\epsilon_{ij}`$, respectively, in this file; only the symbols differ.

<a id="3-forms-density-correction-and-boundary-representative"></a>

## Forms, density correction, and boundary representative

With the definitions $`C=C_\mu dx^\mu`$, $`B=B_{\mu\nu}dx^\mu\wedge dx^\nu/2`$, and
$`E_3=E_{\mu\nu\rho}dx^\mu\wedge dx^\nu\wedge dx^\rho/3!`$,

```math
\begin{aligned}
G&=dC,&
H&=dB+\tfrac12 C\wedge G+\tfrac g2E_3,\\
G_{\mu\nu}&=2\partial_{[\mu}C_{\nu]},&
H_{\mu\nu\rho}
&=3\partial_{[\mu}B_{\nu\rho]}
+\tfrac32C_{[\mu}G_{\nu\rho]}+\tfrac g2E_{\mu\nu\rho},\\
dH&=\tfrac12G\wedge G+\tfrac g2dE_3,&
\partial_{[\mu}H_{\nu\rho\sigma]}
&=\tfrac34G_{[\mu\nu}G_{\rho\sigma]}
+\tfrac g2\partial_{[\mu}E_{\nu\rho\sigma]} .
\end{aligned}
\tag{A8}
```

Here $`(C\wedge G)_{\mu\nu\rho}=3C_{[\mu}G_{\nu\rho]}`$,
$`(G\wedge G)_{\mu\nu\rho\sigma}=6G_{[\mu\nu}G_{\rho\sigma]}`$,
$`(dH)_{\mu\nu\rho\sigma}=4\partial_{[\mu}H_{\nu\rho\sigma]}`$
so all numerical factors are fixed. Gauge check:

```math
\begin{aligned}
\delta C&=d\Lambda,\qquad \delta E_3=d\Lambda_2,\qquad
\delta B=d\Lambda_1-\tfrac12\Lambda G-\tfrac g2\Lambda_2,\\
\delta H
&=-\tfrac12d\Lambda\wedge G-\tfrac12\Lambda\,dG
-\tfrac g2d\Lambda_2+\tfrac12d\Lambda\wedge G
+\tfrac g2d\Lambda_2=0,\qquad dG=d^2C=0.
\end{aligned}
\tag{A9}
```

In (3.5), (3.6), (3.8), and (3.10) of the first file, using the same letter
for the epsilon tensor and density symbol makes determinant factors
ambiguous. The common **tensor** notation is:

```math
\begin{gathered}
E^{\mu\nu}:=-\frac1{12}\varepsilon^{\mu\nu\rho\sigma\lambda}
E_{\rho\sigma\lambda},\qquad
E_{\rho\sigma\lambda}
=\varepsilon_{\rho\sigma\lambda\mu\nu}E^{\mu\nu},\\
E^\mu=-\frac1{12}\varepsilon^{\mu\nu\rho\sigma\lambda}
\mathcal D_\nu E_{\rho\sigma\lambda},\qquad
P^\mu=-\frac1{12}\varepsilon^{\mu\nu\rho\sigma\lambda}
\partial_\nu E_{\rho\sigma\lambda}
=e^{-1}\partial_\nu(eE^{\mu\nu}),\\
P^a=E^a+\frac i2\bar\psi_b\gamma^{ba}\varphi
+\frac14\bar\psi_b^i\gamma^{abc}\psi_c^jL_{ij}.
\end{gathered}
\tag{A10}
```

$`E^{\mu\nu}`$ is not a new independent field; it is the dual representative of
$`E_3`$. No dual field named $`H_{ab}`$ is defined. Direct substitution
of the inverse dualization gives

```math
\begin{aligned}
\varepsilon_{\alpha\beta\gamma\mu\nu}E^{\mu\nu}
&=-\frac1{12}
\varepsilon_{\alpha\beta\gamma\mu\nu}
\varepsilon^{\mu\nu\rho\sigma\lambda}E_{\rho\sigma\lambda}\\
&=-\frac1{12}(-2!\,3!)\,
\delta_{[\alpha}^{\rho}\delta_\beta^\sigma
\delta_{\gamma]}^\lambda E_{\rho\sigma\lambda}
=E_{\alpha\beta\gamma}.
\end{aligned}
\tag{A11}
```

With the density symbol, $`e^{-1}`$ precedes upper epsilon and $`e`$
precedes lower epsilon. The two notations are not mixed. The coordinate
expression of the bridge is also

```math
\begin{aligned}
E^\mu
&=e^{-1}\partial_\nu(eE^{\mu\nu})
+\frac i2\bar\psi_\nu\gamma^{\mu\nu}\varphi
-\frac14\bar\psi_\nu^i\gamma^{\mu\nu\rho}\psi_\rho^jL_{ij}\\
&=e^{-1}\partial_\nu(eE^{\mu\nu})
+\frac i2\bar\psi_\nu\gamma^{\mu\nu}\varphi
+\frac14\bar\psi_\rho^i\gamma^{\mu\nu\rho}\psi_\nu^jL_{ij}.
\end{aligned}
\tag{A12}
```

Thus the bare $`\partial_\nu E^{\mu\nu}`$ in source (3.8) must be read as
$`e^{-1}\partial_\nu(eE^{\mu\nu})`$ when $`E^{\mu\nu}`$ is retained as a tensor.
$`E^a`$ is not identified with $`P^a`$, nor is $`\mathcal D E_3`$ replaced by $`\partial E_3`$.

For the ordinary field strength $`F_{\mu\nu}=2\partial_{[\mu}A_{\nu]}`$ of an arbitrary vector argument,

```math
\begin{aligned}
eA_\mu P^\mu
&=A_\mu\partial_\nu(eE^{\mu\nu})\\
&=\partial_\nu(eA_\mu E^{\mu\nu})
-e(\partial_\nu A_\mu)E^{\mu\nu}\\
&=\frac e2F_{\mu\nu}E^{\mu\nu}
+\partial_\nu(eA_\mu E^{\mu\nu})\\
&=\frac e2F_{\mu\nu}E^{\mu\nu}
-\frac1{12}\partial_\nu
 (\epsilon^{\mu\nu\rho\sigma\lambda}A_\mu E_{\rho\sigma\lambda}).
\end{aligned}
\tag{A13}
```

This file fixes the **field-strength representative** of source (3.2)/(5.10)
for the two-derivative sector and the **potential representative** of (GA24)
for the Weyl-squared sector. Each is defined below as a local density.
If the two-derivative sector is also converted to the potential
representative of source (3.1), the exact change in the total is

```math
\begin{aligned}
S_{\rm pot}-S_{\rm total}
&=-2\int_{\partial M}d\Sigma_\nu\,
 e(A_{{\rm linear}\,\mu}+2gC_\mu)E^{\mu\nu}\\
&=\frac16\int_{\partial M}d\Sigma_\nu\,
 \epsilon^{\mu\nu\rho\sigma\lambda}
 (A_{{\rm linear}\,\mu}+2gC_\mu)E_{\rho\sigma\lambda}.
\end{aligned}
\tag{A14}
```

Here $`A_{\rm linear}`$ is the local potential of the source composite vector;
it is not separately needed in the field-strength action below.
(A14) is the difference between the full representatives.
For the two-fermion actions, the same gauge and $`\Pi_{\le2}`$ are applied to both sides:

```math
S_{\rm pot}^{(\le2)}-S_{\rm total}^{(\le2)}
=-2\int_{\partial M}d\Sigma_\nu\,e\,
\Pi_{\le2}\!\left[
(A_{{\rm linear}\,\mu}+2gC_\mu)E^{\mu\nu}
\right]_{\rm P}.
\tag{A14q}
```

This difference is not set to zero; no boundary condition has been assumed.
Since the Weyl-squared contribution is the same $`\alpha S_{\mathrm{Weyl}^2}`$ in both
representatives, the difference in (A14)–(A14q) comes solely from the
two-derivative sector and carries no factor $`\alpha`$.

The notation $`-4gC_aE^a`$ in (5.11) of the first file cannot replace $`-4gC_aP^a`$
in the presence of fermions. The omitted difference is explicitly

```math
-4gC_a(P^a-E^a)
=-2igC_a\bar\psi_b\gamma^{ba}\varphi
-gC_a\bar\psi_b^i\gamma^{abc}\psi_c^jL_{ij}.
\tag{A15}
```

Thus (5.11) is not used as an input to the combined action.
The two-derivative sector retains the ordinary $`F E/2`$ expression in (A13);
the Weyl-squared sector retains both $`P_W-E_W`$ bridge terms in (GA24).

<a id="4-pregauge-definitions-of-common-composites"></a>

## Pregauge definitions of common composites

Except for removing the compensator label, the source coefficients in
the formulas below are unchanged. These define the common composite fields
of the supplied functional. Derivatives are calculated using these
definitions, followed by (P) and the $`\Pi_{\le2}`$ of §8.
$`T,\chi,D,Y`$ are not separate copies in the two sectors. Giving pregauge
formulas here does not retain the dilatino or dilatation gauge field
in the action.

```math
\begin{aligned}
G_{\mu\nu}&=2\partial_{[\mu}C_{\nu]},\qquad
\widehat G_{\mu\nu}=G_{\mu\nu}-\bar\psi_{[\mu}\gamma_{\nu]}\psi
+\frac i2\sigma\bar\psi_{[\mu}\psi_{\nu]},\\
\widehat H_{\mu\nu\rho}&=3\partial_{[\mu}B_{\nu\rho]}
+\frac32 C_{[\mu}G_{\nu\rho]}+\frac g2E_{\mu\nu\rho}
-\frac34\sigma^2\bar\psi_{[\mu}\gamma_\nu\psi_{\rho]}
-\frac{3i}{2}\sigma\bar\psi_{[\mu}\gamma_{\nu\rho]}\psi,\\
\delta C_\mu&=\partial_\mu\Lambda,\qquad
\delta E_{\mu\nu\rho}=3\partial_{[\mu}\Lambda_{\nu\rho]},\qquad
\delta B_{\mu\nu}=2\partial_{[\mu}\Lambda_{\nu]}
-\frac12\Lambda G_{\mu\nu}-\frac g2\Lambda_{\mu\nu}.
\end{aligned}\tag{B-GC03}
```

```math
2\sigma Y^{ij}-\frac i2\bar\psi^i\psi^j+gL^{ij}=0
\quad\Longrightarrow\quad
Y^{ij}=\frac{i}{4\sigma}\bar\psi^{(i}\psi^{j)}
-\frac{g}{2\sigma}L^{ij}.
\tag{B-GA03}
```

```math
T_{ab}=\frac1{8\sigma^2}\left(\sigma\widehat G_{ab}
+\frac16\varepsilon_{abcde}\widehat H^{cde}
+\frac i4\bar\psi\gamma_{ab}\psi\right),
\qquad
T_{ab}\big|_{\text{explicit }gE}=\frac g{96\sigma^2}
\varepsilon_{abcde}E{}^{cde}.
\tag{B-GC12}
```

```math
\begin{aligned}
\chi^i={}&\frac i{8\sigma}\mathord{\not{\mathcal D}}\psi^i
+\frac i{16\sigma^2}\mathord{\not{\mathcal D}}\sigma\psi^i
-\frac1{32\sigma^2}\gamma\!\cdot\!\widehat G\psi^i
+\frac1{4\sigma}\gamma\!\cdot\!T\psi^i
+\frac i{32\sigma^3}\psi_j\bar\psi^i\psi^j\\
&-\frac g{16\sigma^3}L^{ij}\psi_j
+\frac g{8\sigma^2}\varphi^i.
\end{aligned}\tag{B-GC08}
```

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
+\frac g{4\sigma^2}N
-\frac{ig}{16\sigma^4}L_{ij}\bar\psi^i\psi^j
+\frac{g^2}{16\sigma^4}L^{ij}L_{ij}.
\end{aligned}\tag{B-GC11}
```

```math
\begin{aligned}
\mathcal D_\mu\sigma&=(\partial_\mu-b_\mu)\sigma-\frac i2\bar\psi_\mu\psi,\\
\mathcal D_\mu\psi^i&=\left(\partial_\mu-\frac32b_\mu
+\frac14\omega_\mu{}^{ab}\gamma_{ab}\right)\psi^i-V_\mu{}^{ij}\psi_j
+\frac14\gamma\!\cdot\!\widehat G\psi_\mu^i
+\frac i2\mathord{\not{\mathcal D}}\sigma\psi_\mu^i\\
&\quad+\frac i{4\sigma}\psi_{\mu j}\bar\psi^i\psi^j
-\frac g{2\sigma}L^{ij}\psi_{\mu j}
-\sigma\gamma\!\cdot\!T\psi_\mu^i-\sigma\phi_\mu^i.
\end{aligned}\tag{B-GC14}
```

```math
\Box^c\sigma=(\partial^a-2b^a+\omega_b{}^{ba})\mathcal D_a\sigma
-\tfrac i2\bar\psi_a\mathcal D^a\psi
-2\sigma\bar\psi_a\gamma^a\chi
+\tfrac12\bar\psi_a\gamma^a\gamma\!\cdot\!T\psi
+\tfrac12\bar\phi_a\gamma^a\psi+2f_a{}^a\sigma.
\tag{B-GC16}
```

Algebraic check of (GA03) with the same normalization, and check of
the two $`Y`$ products in $`D`$:

```math
\begin{aligned}
2\sigma Y^{ij}
&=\frac i2\bar\psi^{(i}\psi^{j)}-gL^{ij},\\
Y^{ij}Y_{ij}
&=\left(\frac i{4\sigma}\bar\psi^i\psi^j-\frac g{2\sigma}L^{ij}\right)
  \left(\frac i{4\sigma}\bar\psi_i\psi_j-\frac g{2\sigma}L_{ij}\right)\\
&=-\frac1{16\sigma^2}(\bar\psi^i\psi^j)(\bar\psi_i\psi_j)
-\frac{ig}{4\sigma^2}L_{ij}\bar\psi^i\psi^j
+\frac{g^2}{4\sigma^2}L^{ij}L_{ij},\\
\frac1{4\sigma^2}Y^{ij}Y_{ij}
&=-\frac1{64\sigma^4}(\bar\psi^i\psi^j)(\bar\psi_i\psi_j)
-\frac{ig}{16\sigma^4}L_{ij}\bar\psi^i\psi^j
+\frac{g^2}{16\sigma^4}L^{ij}L_{ij}.
\end{aligned}
\tag{B1}
```

Reduction with two epsilon tensors gives the same sign for both mixed terms:
$`L^{ij}\bar\psi_i\psi_j=L_{ij}\bar\psi^i\psi^j`$.
Exchanging even bilinears introduces no Grassmann sign.

<a id="5-common-connections-curvatures-and-derivatives"></a>

## Common connections, curvatures, and derivatives

Ordinary Lorentz curvature and supercovariant Lorentz curvature are distinct:

```math
\begin{gathered}
R_{\mu\nu}{}^{ab}(\omega)
=2\partial_{[\mu}\omega_{\nu]}{}^{ab}
+2\omega_{[\mu}{}^{ac}\omega_{\nu]c}{}^b,\\
R_{abcd}(\omega)=e_a{}^\mu e_b{}^\nu R_{\mu\nu cd}(\omega),
\qquad R_{bd}(\omega)=\eta^{ac}R_{abcd}(\omega).
\end{gathered}
\tag{C1}
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
\end{aligned}\tag{C-GC18}
```

```math
\begin{aligned}
V_{\mu\nu}{}^{ij}&=2\partial_{[\mu}V_{\nu]}{}^{ij}
-2V_{[\mu}{}^{k(i}V_{\nu]k}{}^{j)},\\
\widehat R_{\mu\nu}{}^{ij}(V)&=V_{\mu\nu}{}^{ij}
-3i\bar\phi_{[\mu}^{(i}\psi_{\nu]}^{j)}
-8\bar\psi_{[\mu}^{(i}\gamma_{\nu]}\chi^{j)}
-i\bar\psi_{[\mu}^{(i}\gamma\!\cdot\!T\psi_{\nu]}^{j)}.
\end{aligned}\tag{C-GC19}
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
\end{aligned}\tag{C-GC20}
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
\end{aligned}\tag{C-GC17}
```

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
\end{aligned}\tag{C-GC22}
```

```math
\begin{aligned}
\mathcal D_\mu L^{ij}&=(\partial_\mu-3b_\mu)L^{ij}
+2V_\mu{}^{(i}{}_kL^{j)k}-i\bar\psi_\mu^{(i}\varphi^{j)},\\
\mathcal D_\mu\varphi^i&=\left(\partial_\mu-\frac72b_\mu
+\frac14\omega_\mu{}^{ab}\gamma_{ab}\right)\varphi^i-V_\mu{}^{ij}\varphi_j
+\frac i2\mathord{\not{\mathcal D}}L^{ij}\psi_{\mu j}
+\frac i2\gamma^aE_a\psi_\mu^i\\
&\quad-\frac12N\psi_\mu^i+\gamma\!\cdot\!T L^{ij}\psi_{\mu j}
-3L^{ij}\phi_{\mu j}.
\end{aligned}\tag{C-GC24}
```

```math
\mathcal D_\mu\Phi=\partial_\mu\Phi
-\delta_D(b_\mu)\Phi-\delta_M(\omega_\mu)\Phi
-\delta_U(V_\mu)\Phi-\delta_Q(\psi_\mu)\Phi
-\delta_S(\phi_\mu)\Phi-\delta_K(f_\mu)\Phi,\qquad
\mathcal D_a=e_a{}^\mu\mathcal D_\mu.
\tag{C-GC21}
```

$`\Box^c\sigma`$ in (B-GC16) is the same operator as $`\square^C\sigma`$ in the two-derivative
file. The differences among $`\Box^c`$, $`\square^c`$, and $`\square^C`$ are purely notational.
On the weight-three triplet, $`\square^cL_{ij}`$ is $`\mathcal D^a\mathcal D_aL_{ij}`$; (C-GC21) also acts on
the tangent index of the first derivative and on the $`S,K`$ transformations.
$`\mathcal D^b\mathcal D_cT^{ac}`$ is retained in the same order. These operators are not replaced
by an ordinary Laplace operator.

The $`E_a`$ and $`N`$ derivatives of the compensator are determined by
inserting the transformations of CONVENTIONS.md §8 into (C-GC21). For example,

```math
\begin{aligned}
\mathcal D_\mu E_a
&=(\partial_\mu-4b_\mu)E_a+\omega_{\mu ab}E^b
-\left[-\frac i2\bar\psi_\mu\gamma_{ab}\mathcal D^b\varphi
-2\bar\psi_\mu\gamma^b\varphi T_{ba}
-2\bar\phi_\mu\gamma_a\varphi\right]\\
&=(\partial_\mu-4b_\mu)E_a+\omega_{\mu ab}E^b
+\frac i2\bar\psi_\mu\gamma_{ab}\mathcal D^b\varphi
+2\bar\psi_\mu\gamma^b\varphi T_{ba}
+2\bar\phi_\mu\gamma_a\varphi,\\
\mathcal D_\mu N
&=(\partial_\mu-4b_\mu)N
-\frac12\bar\psi_\mu\mathord{\not{\mathcal D}}\varphi
-\frac{3i}{2}\bar\psi_\mu\gamma\!\cdot T\varphi
-4i\bar\psi_\mu^i\chi^jL_{ij}
-\frac{3i}{2}\bar\phi_\mu\varphi .
\end{aligned}
\tag{C2}
```

The $`SU(2)`$ connection of a doublet is $`-V_\mu^{ij}X_j`$. Lowering indices,
for example in the compensator derivative terms, gives

```math
\begin{aligned}
L^{rj}\epsilon_{ri}X_j
&=\epsilon^{rk}\epsilon^{j\ell}L_{k\ell}
 \epsilon_{ri}X^s\epsilon_{sj}
=-L_{is}X^s,\\
\frac i2\mathord{\not{\mathcal D}}L^{rj}\psi_{\mu j}\epsilon_{ri}
&=-\frac i2\mathord{\not{\mathcal D}}L_{ij}\psi_\mu^j,\\
-3L^{rj}\phi_{\mu j}\epsilon_{ri}
&=+3L_{ij}\phi_\mu^j.
\end{aligned}
\tag{C3}
```

These signs agree with (4.30) of the first file. The Lorentz-connection
sign in $`\mathcal D_\mu T_{ab}`$ is also

```math
\begin{aligned}
\nabla_\mu T_{ab}
&=\partial_\mu T_{ab}
-\omega_\mu{}^c{}_aT_{cb}-\omega_\mu{}^c{}_bT_{ac}\\
&=\partial_\mu T_{ab}
+\omega_\mu{}^c{}_aT_{bc}-\omega_\mu{}^c{}_bT_{ac}
=\partial_\mu T_{ab}+2\omega_\mu{}^c{}_{[a}T_{b]c}
\end{aligned}
\tag{C4}
```

Both files use this plus sign. The weight of $`\chi`$ is $`3/2`$:
$`w(\sigma^{-1}\mathord{\not{\mathcal D}}\psi)=-1+1+3/2=3/2`$ and
$`w(g\sigma^{-2}\varphi)=-2+7/2=3/2`$.
Hence $`-3b_\mu/2`$ is retained in $`\mathcal D_\mu\chi`$.

In both sources, the explicit $`\chi`$ term of $`\widehat R'(M)`$ is $`+8\bar\psi_{[\mu}e_{\nu]}{}^{[a}\gamma^{b]}\chi`$.
Since $`f`$ is calculated from the same primed curvature,

```math
\begin{aligned}
f_a{}^a&=\left(-\frac16+\frac5{48}\right)\mathcal R
=-\frac1{16}\mathcal R,\\
\widehat R_{ab}{}^{cb}(M)
&=\mathcal R_a{}^c+6f_a{}^c+2\delta_a{}^cf_b{}^b\\
&=\mathcal R_a{}^c-\mathcal R_a{}^c
+\frac18\delta_a{}^c\mathcal R-\frac18\delta_a{}^c\mathcal R=0 .
\end{aligned}
\tag{C5}
```

This trace calculation remains valid in the presence of fermions;
$`\mathcal R`$ is not replaced by the ordinary $`R(\omega)`$. For completeness,
the conversion from the old $`-8`$ sign is also fixed.
With temporary $`J_\mu{}^a:=\bar\psi_\mu\gamma^a\chi`$,

```math
\begin{aligned}
\Delta\widehat R'_{\mu\nu}{}^{ab}
&=-16J_{[\mu}{}^{[a}e_{\nu]}{}^{b]},&
\Delta\mathcal R_a{}^c
&=-12J_a{}^c-4\delta_a{}^cJ_b{}^b,\\
\Delta\mathcal R&=-32J_a{}^a,&
\Delta f_a{}^c
&=-\frac16\Delta\mathcal R_a{}^c
+\frac1{48}\delta_a{}^c\Delta\mathcal R=2J_a{}^c,\\
\Delta\widehat R_{\mu\nu}{}^{ab}
&=-16J_{[\mu}{}^{[a}e_{\nu]}{}^{b]}
+8(2J_{[\mu}{}^{[a})e_{\nu]}{}^{b]}=0 .
\end{aligned}
\tag{C6}
```

In the original variables, $`\Delta f_\mu{}^a=2\bar\psi_\mu\gamma^a\chi`$.
The two current sources already use the same plus sign, so no additional
$`\Delta f`$ term is inserted in their combination.

<a id="6-component-definitions-of-the-two-derivative-source-action"></a>

## Component definitions of the two-derivative source action

The following four formulas are (4.33), (4.34), (4.36), and (4.37)
of the first file. They define only the components of source (5.10)
and make order selection explicit. The last two cubic terms of $`\lambda`$
and last three quartic terms of $`Y`$ do not contribute to the action
under $`\Pi_{\le2}`$. All $`\mathcal D,T,\chi,D,\widehat R`$ objects are evaluated with the common gauged
definitions in §§4–5, followed by (P).

```math
\boxed{
\rho_{\mathrm{linear}}
=2L^{-1}N
+iL^{-3}L_{ij}\bar\varphi^i\varphi^j.
}
\tag{D-4.33}
```

```math
\boxed{
\begin{aligned}
\lambda_{\mathrm{linear}\,i}
={}&-2iL^{-1}\not{\mathcal D}\varphi_i
+L^{-1}\left(
16L_{ij}\chi^j
+4\gamma\mathbin{\cdot}T\,\varphi_i
\right)\\
&-2NL^{-3}L_{ij}\varphi^j\\
&+2iL^{-3}\left(
\not{\mathcal D}L_{ij}L^{jk}\varphi_k
-\not E\,L_{ij}\varphi^j
\right)\\
&+2iL^{-3}\varphi^j\bar\varphi_i\varphi_j\\
&-6iL^{-5}\varphi^j\bar\varphi_k\varphi_l
L^{kl}L_{ij}.
\end{aligned}
}
\tag{D-4.34}
```

```math
\boxed{
\begin{aligned}
Y_{\mathrm{linear}\,ij}
={}&L^{-1}\square^cL_{ij}
-L^{-3}L^{km}
\mathcal D_aL_{k(i}\mathcal D^aL_{j)m}\\
&-L^{-3}L_{ij}N^2
-L^{-3}L_{ij}E_aE^a\\
&+2L^{-3}E_aL_{k(i}\mathcal D^aL_{j)}{}^k\\
&+\frac83L^{-1}L_{ij}T^2
+4L^{-1}L_{ij}D\\
&+iNL^{-3}\bar\varphi_{(i}\varphi_{j)}
-3iNL^{-5}L_{ij}L^{kl}
\bar\varphi_k\varphi_l\\
&+3L^{-5}L_{ij}L^{kl}
\bar\varphi_k\not E\varphi_l
-L^{-3}\bar\varphi_{(i}\not E\varphi_{j)}\\
&-16iL^{-1}\bar\chi_{(i}\varphi_{j)}
+16iL^{-3}L_{ij}L_{kl}
\bar\chi^k\varphi^l\\
&+2L^{-3}L_{k(i}\bar\varphi^k
\not{\mathcal D}\varphi_{j)}\\
&-3L^{-5}L_{k(i}L^{lm}\bar\varphi^k
\not{\mathcal D}L_{j)l}\varphi_m\\
&+\frac12L^{-3}\bar\varphi^l
\not{\mathcal D}L_{l(i}\varphi_{j)}\\
&+\frac12L^{-3}\bar\varphi^m
\not{\mathcal D}L_{ij}\varphi_m\\
&+2iL^{-3}L_{ij}
\bar\varphi\gamma\mathbin{\cdot}T\varphi\\
&+\frac{15}{2}L^{-7}L_{ij}
\left(L^{kl}\bar\varphi_k\varphi_l\right)^2\\
&-3L^{-5}
\left(L^{kl}\bar\varphi_k\varphi_l\right)
\bar\varphi_{(i}\varphi_{j)}\\
&-\frac32L^{-5}L_{ij}
\left(\bar\varphi_m\varphi_n\right)
\left(\bar\varphi^m\varphi^n\right).
\end{aligned}
}
\tag{D-4.36}
```

```math
\boxed{
\begin{aligned}
\widehat F_{\mathrm{linear}\,\mu\nu}
={}&4\mathcal D_{[\mu}\left(L^{-1}E_{\nu]}\right)
+2L^{-1}\widehat R_{\mu\nu}{}^{ij}(V)L_{ij}\\
&-2L^{-3}L_k{}^\ell
\mathcal D_{[\mu}L^{kp}
\mathcal D_{\nu]}L_{\ell p}\\
&-2\mathcal D_{[\mu}\left(
L^{-3}L_{ij}\bar\varphi^i\gamma_{\nu]}\varphi^j
\right)\\
&-iL^{-1}\bar\varphi^i
\widehat R_{\mu\nu i}(Q).
\end{aligned}
}
\tag{D-4.37}
```

$`\lambda_{\rm linear}{}^i=\epsilon^{ij}\lambda_{{\rm linear}\,j}`$.
The bar acts on this entire spinor. The composite ordinary field strength is:

```math
F_{{\rm linear}\,\mu\nu}
:=\widehat F_{{\rm linear}\,\mu\nu}
+\bar\psi_{[\mu}^i\gamma_{\nu]}\lambda_{{\rm linear}\,i}
-\frac i2\rho_{\rm linear}\bar\psi_{[\mu}^i\psi_{\nu]i}.
\tag{D1}
```

In the last term, the fermion bilinear in $`\rho_{\rm linear}`$ multiplied by two
gravitini has four fermions; $`\Pi_{\le2}`$ in §9 removes it.
The pregauge components of the effective vector are:

```math
\begin{aligned}
\rho_{\rm eff}&=\rho_{\rm linear}+2g\sigma,\\
\lambda_{{\rm eff}\,i}&=\lambda_{{\rm linear}\,i}+2g\psi_i,\\
Y_{{\rm eff}\,ij}
&=Y_{{\rm linear}\,ij}
+\frac{ig}{2\sigma}\bar\psi_i\psi_j-\frac{g^2}{\sigma}L_{ij},\\
\widehat F_{{\rm eff}\,\mu\nu}
&=\widehat F_{{\rm linear}\,\mu\nu}+2g\widehat G_{\mu\nu}.
\end{aligned}
\tag{D2}
```

For the ordinary field strength, without restricting to the bosonic limit:

```math
\begin{aligned}
F_{{\rm eff}\,\mu\nu}
={}&\widehat F_{{\rm linear}\,\mu\nu}
+2g\left(G_{\mu\nu}-\bar\psi_{[\mu}\gamma_{\nu]}\psi
+\frac i2\sigma\bar\psi_{[\mu}\psi_{\nu]}\right)\\
&+\bar\psi_{[\mu}\gamma_{\nu]}(\lambda_{\rm linear}+2g\psi)
-\frac i2(\rho_{\rm linear}+2g\sigma)
 \bar\psi_{[\mu}\psi_{\nu]}\\
={}&F_{{\rm linear}\,\mu\nu}+2gG_{\mu\nu}.
\end{aligned}
\tag{D3}
```

$`-2g\bar\psi\gamma\psi`$ cancels $`+2g\bar\psi\gamma\psi`$, and $`+ig\sigma\bar\psi\psi`$ cancels $`-ig\sigma\bar\psi\psi`$, separately;
(D3) is an exact fermionic algebraic equality.

<a id="7-weyl-squared-action-in-the-common-gauge"></a>

## Weyl-squared action in the common gauge

$`\mathscr W_{\rm P}`$ denotes the explicit expression below. It follows by applying (P)
to (GA24) and removing monomials with at least four explicit fermions.
Higher fermion orders inside hatted objects are additionally removed
by $`\Pi_{\le2}`$ in §8:

```math
\begin{aligned}
\left.e^{-1}\mathcal L_{\sigma C^2,g}^{\rm map}\right|_{\rm P}
&=\mathscr W_{\rm P}+\mathcal O_{\ge4},\\
e^{-1}\mathcal L_{W^2}^{(\le2)}
&:=\Pi_{\le2}\mathscr W_{\rm P}.
\end{aligned}
\tag{W0}
```

Here $`\mathcal O_{\ge4}`$ counts fermions only.
The explicitly removed terms are accounted for as follows:
$`\psi^i=0`$ sets all dilatino factors to zero;
$`\bar\psi_\mu\psi_\nu\overline{\widehat R(Q)}\widehat R(Q)`$
and $`\bar\psi_\mu\psi_\nu\bar\chi\chi`$ have four fermions.
In contrast, $`L^{ij}\overline{\widehat R(Q)}\widehat R(Q)`$,
$`L^{ij}\bar\chi\chi`$, and
$`\bar\psi_\mu\psi_\nu\widehat R(V)T`$ are retained.
The last three gauging factors directly become

```math
-\frac g2\frac L{\sqrt2}\left(\frac i4,\frac{256i}{3},\frac{16}{3}\right)
=\left(-\frac{igL}{8\sqrt2},-\frac{128igL}{3\sqrt2},
-\frac{8gL}{3\sqrt2}\right)
\tag{W-coeff}
```

Here $`T^2=T_{ab}T^{ab}`$,
$`T^4=T_{ab}T^{bc}T_{cd}T^{da}`$, and
$`(T^2)^2=(T_{ab}T^{ab})^2`$ are distinct.

```math
\begin{aligned}
\mathscr W_{\rm P}={}&
\frac{1}{8} \widehat C_{abcd}\widehat C^{abcd}+\frac{64}{3} D^2\\
 &+\frac{1024}{9} DT_{ab}T^{ab}-\frac{16}{3} \widehat C_{abcd}T^{ab}T^{cd}\\
 &-\frac{1}{3} \widehat R_{ab}{}^{ij}(V)\widehat R^{ab}{}_{ij}(V)-\frac{64}{3} (\mathcal D_aT_{bc})(\mathcal D^aT^{bc})\\
 &+\frac{64}{3} (\mathcal D_bT_{ac})(\mathcal D^aT^{bc})-\frac{128}{3} T_{ab}\mathcal D^b\mathcal D_cT^{ac}\\
 &-\frac{128}{3} \varepsilon_{abcde}T^{ab}T^{cd}\mathcal D_fT^{ef}+1024 T_{ab}T^{bc}T_{cd}T^{da}\\
 &-\frac{2816}{27} (T_{ab}T^{ab})^2+\frac{3}{4} \overline{\widehat R_{ab}(Q)}\gamma^c\mathcal D_c\widehat R^{ab}(Q)\\
 &-2i T^{ab}\overline{\widehat R_{ca}(Q)}\widehat R^c{}_{b}(Q)-\frac{160i}{3} T^{ab}\overline{\widehat R_{ab}(Q)}\chi\\
 &-\frac{256}{3} \bar\chi\gamma^a\mathcal D_a\chi
\\
&+\frac{1}{16}C_a\varepsilon^{abcde}\widehat C_{bcfg}\widehat C_{de}{}^{fg}-\frac{1}{12}C_a\varepsilon^{abcde}\widehat R(V)_{bc}{}^{ij}\widehat R(V)_{de\,ij}\\
 &+C_a\mathcal D_b\Big[4\widehat C^{ab}{}_{cd}T^{cd}-\frac{64}{3}DT^{ab}-\frac{128}{9}T^{ab}T_{cd}T^{cd}\\
 &\hspace{20mm}-\frac{512}{3}T^a{}_cT^{cd}T^b{}_d+8i\overline{\widehat R(Q)^{ab}}\chi-\frac{64i}{3}\bar\chi\gamma^{ab}\chi\Big]-32C_a\varepsilon^a{}_{bcde}\mathcal D^b\Big[\frac23T^{cf}\mathcal D_fT^{de}+T^c{}_f\mathcal D^dT^{ef}\Big]\\
 &-C_aT^{cd}\overline{\widehat R(Q)_{ec}}\gamma^a\widehat R(Q)^e{}_d+3C_aT_c{}^d\overline{\widehat R(Q)_e{}^a}\gamma^c\widehat R(Q)^e{}_d\\
 &+16C_aT^c{}_d\overline{\widehat R(Q)^a{}_c}\gamma^d\chi+\frac{16}{3}C_aT^{cd}\overline{\widehat R(Q)_{cd}}\gamma^a\chi\\
 &+\frac{i}{2}C_a\overline{\widehat R(Q)_{cd}}\mathcal D^a\widehat R(Q)^{cd}+\frac{3i}{2}C_a\overline{\widehat R(Q)_{cd}}\mathcal D^c\widehat R(Q)^{da}
\\
&-\frac{1}{16}\bar\psi_m\gamma^m\gamma_{cd}\widehat R_{ab}(Q)\widehat C^{abcd}-2i\bar\psi_m\gamma^m\gamma_c\widehat R_{ab}(Q)\mathcal D^aT^{bc}\\
 &+\frac{64}{3}\bar\psi_m\gamma^m\chi D+4i\bar\psi_m\gamma^m\gamma_c\mathcal D^c\widehat R_{ab}(Q)T^{ab}\\
 &+4i\bar\psi_m\gamma^m\gamma_a\mathcal D^c\widehat R_{bc}(Q)T^{ab}-\frac{32i}{3}\bar\psi_m\gamma^m\gamma^{ab}\gamma^c\chi\mathcal D_aT_{bc}\\
 &+\frac{512}{9}\bar\psi_m\gamma^m\chi T^2+\frac{64i}{3}\bar\psi_m\gamma^m\gamma_a\mathcal D_b\chi T^{ab}\\
 &+\frac{4}{3}\bar\psi_m\gamma^m\gamma_{ab}\widehat R_{cd}(Q)T^{ab}T^{cd}+\frac{1}{4}\bar\psi_m^i\gamma^m\widehat R^{ab}{}_{ij}(V)\widehat R_{ab}{}^j(Q)\\
 &-\frac{4}{3}\bar\psi_m^i\gamma^m\widehat R^{ab}{}_{ij}(V)\gamma_{ab}\chi^j
\\
&-\frac{i}{16}C_m\bar\psi_n\gamma^{nm}\gamma_{cd}\widehat R_{ab}(Q)\widehat C^{abcd}+2C_m\bar\psi_n\gamma^{nm}\gamma_c\widehat R_{ab}(Q)\mathcal D^aT^{bc}\\
 &+\frac{64i}{3}C_m\bar\psi_n\gamma^{nm}\chi D-4C_m\bar\psi_n\gamma^{nm}\gamma_c\mathcal D^c\widehat R_{ab}(Q)T^{ab}\\
 &-4C_m\bar\psi_n\gamma^{nm}\gamma_a\mathcal D^c\widehat R_{bc}(Q)T^{ab}+\frac{32}{3}C_m\bar\psi_n\gamma^{nm}\gamma^{ab}\gamma^c\chi\mathcal D_aT_{bc}\\
 &+\frac{512i}{9}C_m\bar\psi_n\gamma^{nm}\chi T^2-\frac{64}{3}C_m\bar\psi_n\gamma^{nm}\gamma_a\mathcal D_b\chi T^{ab}\\
 &+\frac{4i}{3}C_m\bar\psi_n\gamma^{nm}\gamma_{ab}\widehat R_{cd}(Q)T^{ab}T^{cd}+\frac{i}{4}C_m\bar\psi_n^i\gamma^{nm}\widehat R^{ab}{}_{ij}(V)\widehat R_{ab}{}^j(Q)\\
 &-\frac{4i}{3}C_m\bar\psi_n^i\gamma^{nm}\widehat R^{ab}{}_{ij}(V)\gamma_{ab}\chi^j
\\
&-\frac{igL}{8\sqrt2}\delta^{ij}
 \overline{\widehat R}_{ab(i}(Q)\widehat R_{j)}{}^{ab}(Q)
-\frac{128igL}{3\sqrt2}\delta^{ij}\bar\chi_{(i}\chi_{j)}
-\frac{8gL}{3\sqrt2}\delta^{ij}\widehat R_{ab\,ij}(V)T^{ab}\\
&+\frac{4i}{3}
 (\bar\psi_m^i\gamma^{mn}\psi_n^j)
 \widehat R_{ab\,ij}(V)T^{ab}
+\frac43 C_m(\bar\psi_n^i\gamma^{mnp}\psi_p^j)
 \widehat R_{ab\,ij}(V)T^{ab}.

\end{aligned}
\tag{W1}
```

All objects are evaluated at (P). Because its hatted composites are
untruncated, (W1) alone may also contain higher-fermion monomials;
**the contribution entering the total action is $`\alpha\,\Pi_{\le2}\mathscr W_{\rm P}`$**.
(W0)–(W1) define the source normalization of this contribution
before multiplication by $`\alpha`$.

The first two coefficients and their ratio are:

```math
\frac18\widehat C_{abcd}\widehat C^{abcd}
+\frac{64}{3}D^2,\qquad
\frac{64/3}{1/8}=\frac{512}{3}.
\tag{W2}
```

$`512/3`$ is only the relative coefficient; it does not replace $`64/3`$.
The two-derivative sector's factor $`-2`$ is not applied to (W1).
$`\alpha`$ multiplies all terms in (W1) uniformly; for example, the first
two Weyl-sector coefficients in the total density are $`\alpha/8`$ and $`64\alpha/3`$.
For $`\alpha\ne0`$, their ratio remains $`512/3`$.

<a id="8-exact-two-fermion-selection-including-hatted-objects"></a>

## Exact two-fermion selection including hatted objects

The independent fields are $`e_\mu{}^a,C_\mu,B_{\mu\nu},L,N,E_{\mu\nu\rho}, V_\mu,V_\mu^{\prime\,ij},\psi_\mu^i,\varphi^i`$.
$`E_a`$ is defined from $`E_3`$ by the supercovariant bridge in §3;
it is not counted as a second independent field.

Let $`t`$ be an even, dimensionless fermion-counting variable only.
After evaluating the full derivative/composite definitions and applying (P),
replace the independent fermions by $`(\psi_\mu,\varphi)\mapsto(t\psi_\mu,t\varphi)`$.
For each $`X`$,

```math
X_{[n]}:=\left.\frac1{n!}\frac{d^n}{dt^n}X(t)\right|_{t=0},
\qquad
\Pi_{\le2}X:=X_{[0]}+X_{[1]}+X_{[2]}.
\tag{V0}
```

Since the action is Grassmann-even, the odd-order density vanishes.
This definition is the exact fermion-order projection used here,
not an approximate numerical expansion. At the end, $`t`$ is $`1`$
and is not a physical coupling. $`\alpha`$ is constant independently of $`t`$. Thus

```math
\begin{aligned}
(\alpha X)_{[n]}
&=\left.\frac1{n!}\frac{d^n}{dt^n}
 [\alpha X(t)]\right|_{t=0}
=\alpha X_{[n]},\\
\Pi_{\le2}(\alpha X)&=\alpha\,\Pi_{\le2}X .
\end{aligned}
\tag{V0a}
```

No order in $`\alpha`$ is selected during the two-fermion projection;
$`\alpha`$ is retained unchanged as a generic constant.

Dependent objects are recalculated from their definitions; $`E_a,T,D,\omega`$
are not treated as entirely zeroth order merely because their names
denote bosonic fields. The first required components are directly

```math
\begin{aligned}
E^a_{[0]}&=P^a
=-\frac1{12}e_\mu{}^a\varepsilon^{\mu\nu\rho\sigma\lambda}
  \partial_\nu E_{\rho\sigma\lambda},\\
E^a_{[2]}&=-\frac i2\bar\psi_b\gamma^{ba}\varphi
-\frac{L}{4\sqrt2}\delta_{ij}
 \bar\psi_b^i\gamma^{abc}\psi_c^j,\\
\widehat G_{[0]\,\mu\nu}&=G_{\mu\nu},&
\widehat G_{[2]\,\mu\nu}&=\frac i2\bar\psi_{[\mu}\psi_{\nu]},\\
\widehat H_{[0]\,\mu\nu\rho}&=H_{\mu\nu\rho},&
\widehat H_{[2]\,\mu\nu\rho}
&=-\frac34\bar\psi_{[\mu}\gamma_\nu\psi_{\rho]},\\
T_{[0]\,ab}&=\frac18\left(G_{ab}
+\frac16\varepsilon_{abcde}H^{cde}\right),&
T_{[2]\,ab}&=\frac18\left(\widehat G_{[2]\,ab}
+\frac16\varepsilon_{abcde}\widehat H_{[2]}^{cde}\right),\\
\omega_{[0]\,\mu}{}^{ab}
&=2e^{\nu[a}\partial_{[\mu}e_{\nu]}{}^{b]}
-e^{\nu[a}e^{b]\rho}e_{\mu c}\partial_\nu e_\rho{}^c,&
\omega_{[2]\,\mu}{}^{ab}
&=\frac12\bar\psi^{[a}\gamma^{b]}\psi_\mu
+\frac14\bar\psi^a\gamma_\mu\psi^b .
\end{aligned}
\tag{V1}
```

For $`\widehat R'(Q)_{[1]}`$, substitute $`\omega_{[0]},T_{[0]},b_\mu=0`$ in (C-GC18); the linear $`\phi`$ formula
in the same equation determines $`\phi_{\mu[1]}`$, and its last line determines
$`\widehat R(Q)_{[1]}`$. Then

```math
\begin{aligned}
(\mathcal D_\mu\psi^i)_{[1]}\big|_{\rm P}
&=\left(\frac14\gamma^{ab}G_{ab}
-\gamma^{ab}T_{[0]\,ab}\right)\psi_\mu^i
-\phi_{\mu[1]}^i-\frac{gL}{2\sqrt2}\delta^{ij}\psi_{\mu j},\\
\chi^i_{[1]}
&=\frac i8\gamma^\mu(\mathcal D_\mu\psi^i)_{[1]}\big|_{\rm P}
+\frac g8\varphi^i,\\
\widehat R_{\mu\nu}^{ij}(V)_{[0]}&=V_{\mu\nu}^{ij},\\
\widehat R_{\mu\nu}^{ij}(V)_{[2]}
&=-3i\bar\phi_{[\mu[1]}^{(i}\psi_{\nu]}^{j)}
-8\bar\psi_{[\mu}^{(i}\gamma_{\nu]}\chi_{[1]}^{j)}
-i\bar\psi_{[\mu}^{(i}\gamma^{ab}T_{[0]\,ab}\psi_{\nu]}^{j)} .
\end{aligned}
\tag{V2}
```

$`f_{[0]},f_{[2]},\widehat C_{[0]},\widehat C_{[2]}`$ is determined by the same coefficient selection in (C-GC20).
In this calculation, the second-order connection contribution to
the ordinary curvature is

```math
\begin{aligned}
R_{\mu\nu}{}^{ab}(\omega)_{[2]}
={}&2\partial_{[\mu}\omega_{\nu][2]}{}^{ab}
+2\omega_{[\mu[0]}{}^{ac}\omega_{\nu][2]c}{}^b
+2\omega_{[\mu[2]}{}^{ac}\omega_{\nu][0]c}{}^b .
\end{aligned}
\tag{V3a}
```

$`\omega_{[2]}\omega_{[2]}`$ has four fermions.
With $`\mathcal R_{[n]}`$ the same primed Ricci contraction,
$`f_{\mu[n]}{}^a=-\mathcal R_{\mu[n]}{}^a/6+ e_\mu{}^a\mathcal R_{[n]}/48`$, $`n=0,2`$.

The full box definition for the constant dilaton is evaluated first:

```math
\begin{aligned}
\Box^c\sigma\big|_{\rm P}
&=-\frac i2\bar\psi_a\mathcal D^a\psi\big|_{\rm P}
-2\bar\psi_a\gamma^a\chi+2f_a{}^a,\\
D_{[0]}
&=\frac12f_{a[0]}{}^a-\frac1{16}G_{ab}G^{ab}
-\frac{26}{3}T_{[0]\,ab}T_{[0]}^{ab}
+2G_{ab}T_{[0]}^{ab}+\frac g4N+\frac{g^2}{16}L^2,\\
D_{[2]}
&=\frac12f_{a[2]}{}^a
-\frac18G^{ab}\widehat G_{[2]\,ab}
-\frac{52}{3}T_{[0]}^{ab}T_{[2]\,ab}
+2G^{ab}T_{[2]\,ab}+2\widehat G_{[2]}^{ab}T_{[0]\,ab}\\
&\quad-\frac i8\bar\psi_a(\mathcal D^a\psi)_{[1]}\big|_{\rm P}
-\frac12\bar\psi_a\gamma^a\chi_{[1]} .
\end{aligned}
\tag{V4}
```

For example, $`-(26/3)(1/8)^2=-13/96`$ and $`(-1/2)(g/8)=-g/16`$ reproduce the coefficients of source (4.24).
$`\psi^i|_{\rm P}=0`$ does not imply $`\mathcal D_\mu\psi^i|_{\rm P}=0`$.

The gauge-fixed derivatives required in the two-derivative action also follow
from source (4.27), (4.28), (4.30), and (4.32), consistently with (C-GC24)
and the common NW–SE conventions:

```math
\boxed{
\begin{aligned}
\mathcal D_\mu L_{ij}\big|_{\mathrm P}
={}&\frac1{\sqrt2}\delta_{ij}\partial_\mu L
-\sqrt2L\,V'_{\mu(i}{}^k\delta_{j)k}\\
&-i\bar\psi_{\mu(i}\varphi_{j)}.
\end{aligned}
}
\tag{V-4.27}
```

The minus sign in the connection term is fixed by lowering the indices
of (C-GC24):

```math
\begin{aligned}
\epsilon_{ki}\epsilon_{\ell j}
 \left(2V_\mu{}^{(k}{}_mL^{\ell)m}\right)
&=-2V_{\mu(i}{}^kL_{j)k},\\
\mathcal D_\mu L_{ij}
&=(\partial_\mu-3b_\mu)L_{ij}
 -2V_{\mu(i}{}^kL_{j)k}
 -i\bar\psi_{\mu(i}\varphi_{j)},\\
-2V_{\mu(i}{}^kL_{j)k}\big|_{\mathrm P}
&=-\sqrt2L\,V'_{\mu(i}{}^k\delta_{j)k}.
\end{aligned}
\tag{V-4.27a}
```

The plus sign in the earlier lower-index expression was corrected here
and in (4.27), (6.1) of the two-derivative source file.
The upper-index connection sign in (C-GC24) remains positive.

```math
\boxed{
\begin{aligned}
\mathcal D_\mu L^{ij}\big|_{\mathrm P}
&=\epsilon^{ik}\epsilon^{j\ell}
\mathcal D_\mu L_{k\ell}\big|_{\mathrm P},\\
\mathcal D_\mu L_j{}^k\big|_{\mathrm P}
&=\epsilon^{k\ell}
\mathcal D_\mu L_{j\ell}\big|_{\mathrm P}.
\end{aligned}
}
\tag{V-4.28}
```

```math
\boxed{
\begin{aligned}
\mathcal D_\mu\varphi_i\big|_{\mathrm P}
={}&\left(
\partial_\mu+\frac14\omega_\mu{}^{ab}\gamma_{ab}
\right)\varphi_i
-V_{\mu i}{}^j\varphi_j\\
&-\frac{i}{2}\gamma^a
\left(
\mathcal D_aL_{ij}\big|_{\mathrm P}
\right)\psi_\mu{}^j
+\frac{i}{2}\gamma^aE_a\psi_{\mu i}
-\frac12N\psi_{\mu i}\\
&-\frac{L}{8\sqrt2}\delta_{ij}\gamma^{ab}
\left(
\widehat G_{ab}
+\frac16\varepsilon_{abcde}\widehat H^{cde}
\right)\psi_\mu{}^j\\
&+\frac{3L}{\sqrt2}\delta_{ij}\phi_\mu{}^j.
\end{aligned}
}
\tag{V-4.30}
```

```math
\boxed{
\begin{aligned}
L_{ij}\square^CL^{ij}\big|_{\mathrm P}
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
\tag{V-4.32}
```

This correction is applied throughout the map using the same (V-4.27)
definition. The correction is not restricted to the final bosonic action
while leaving fermionic derivatives unchanged. To display its propagation,
define $`K_{\mu ij}:=V'_{\mu(i}{}^k\delta_{j)k}`$ and
$`\Delta:=\text{corrected expression}-\text{previous expression}`$:

```math
\begin{aligned}
\Delta(\mathcal D_\mu L_{ij})&=-2\sqrt2L\,K_{\mu ij},\\
\Delta(\mathcal D_\mu\varphi_i)
&=-\frac i2\gamma^a\Delta(\mathcal D_aL_{ij})\psi_\mu{}^j
=i\sqrt2L\,\gamma^aK_{aij}\psi_\mu{}^j,\\
\Delta\lambda_{{\rm linear}\,i}
&=-2iL^{-1}\gamma^\mu\Delta(\mathcal D_\mu\varphi_i)
 +2iL^{-3}\gamma^a\Delta(\mathcal D_aL_{ij})L^{jk}\varphi_k\\
&=2\sqrt2\gamma^\mu\gamma^aK_{aij}\psi_\mu{}^j
 -\frac{4i}{L}\gamma^aK_{aij}\delta^{jk}\varphi_k .
\end{aligned}
\tag{V-4.32a}
```

The derivatives in $`Y_{\rm linear}`$, $`F_{\rm linear}`$, and (V-4.32) are also calculated from
(V-4.27)–(V-4.28). Thus the coefficients of (D-4.34), (D-4.36), (D-4.37),
and (S4) remain unchanged; the values of their composite derivatives
are corrected. The sign of the explicit
$`+\sqrt2L\,\delta_{ij}V_a{}^i{}_k\mathcal D^aL^{jk}`$
term in (V-4.32) itself is unchanged.

These expressions also use the same $`\chi,D,\omega,\phi,f`$ definitions of §§4–5.
The first-order coefficient of $`\mathcal D_\mu\chi`$ or $`\mathcal D_\mu\widehat R(Q)`$ is not merely
the bosonic spinor connection: the gravitino and $`S`$-connection terms
of (C-GC17)/(C-GC22) are retained at first order too.

The projector acts on all products exactly as

```math
(X_1\cdots X_k)_{[n]}
=\sum_{n_1+\cdots+n_k=n}
 (X_1)_{[n_1]}\cdots(X_k)_{[n_k]}
\tag{V5}
```

without changing source order. For example,

```math
\begin{aligned}
\Pi_{\le2}(\widehat C_{abcd}\widehat C^{abcd})
&=\widehat C_{[0]\,abcd}\widehat C_{[0]}^{abcd}
+2\widehat C_{[0]\,abcd}\widehat C_{[2]}^{abcd},\\
\Pi_{\le2}(D^2)&=D_{[0]}^2+2D_{[0]}D_{[2]},\\
\Pi_{\le2}(DT_{ab}T^{ab})
&=D_{[0]}T_{[0]\,ab}T_{[0]}^{ab}
+D_{[2]}T_{[0]\,ab}T_{[0]}^{ab}
+2D_{[0]}T_{[0]\,ab}T_{[2]}^{ab},\\
\Pi_{\le2}\!\left[
(\mathcal D_aT_{bc})(\mathcal D^aT^{bc})\right]
&=(\mathcal D_aT_{bc})_{[0]}(\mathcal D^aT^{bc})_{[0]}
+2(\mathcal D_aT_{bc})_{[0]}(\mathcal D^aT^{bc})_{[2]},\\
\Pi_{\le2}\!\left[T_{ab}\mathcal D^b\mathcal D_cT^{ac}\right]
&=T_{[0]\,ab}(\mathcal D^b\mathcal D_cT^{ac})_{[0]}
+T_{[2]\,ab}(\mathcal D^b\mathcal D_cT^{ac})_{[0]}
+T_{[0]\,ab}(\mathcal D^b\mathcal D_cT^{ac})_{[2]},\\
\Pi_{\le2}\!\left[
\overline{\widehat R_{ab}(Q)}
\gamma^c\mathcal D_c\widehat R^{ab}(Q)\right]
&=\overline{\widehat R_{ab}(Q)_{[1]}}\,
 \gamma^c(\mathcal D_c\widehat R^{ab}(Q))_{[1]} .
\end{aligned}
\tag{V6}
```

(V0), the full definitions, and (V5) specify a finite, unambiguous procedure
for every monomial; they do not permit fourth and higher fermion orders
inside hatted expressions to remain in the action.

The numerical coefficients in the product of the Weyl-squared map with
the linear density can also be checked separately. Temporarily denote
the source-ordered coefficient lists of the map spinor and triplet
by $`r`$ and $`q`$, respectively:

```math
\begin{aligned}
r&=\left(-\frac18,-4i,\frac{128}{3},8i,8i,-\frac{64i}{3},
\frac{1024}{9},\frac{128i}{3},\frac83,\frac12,-\frac83\right),\\
ir&=\left(-\frac i8,4,\frac{128i}{3},-8,-8,\frac{64}{3},
\frac{1024i}{9},-\frac{128}{3},\frac{8i}{3},\frac i2,-\frac{8i}{3}\right),\\
\frac r2&=\left(-\frac1{16},-2i,\frac{64}{3},4i,4i,-\frac{32i}{3},
\frac{512}{9},\frac{64i}{3},\frac43,\frac14,-\frac43\right),\\
\frac{ir}{2}&=\left(-\frac i{16},2,\frac{64i}{3},-4,-4,\frac{32}{3},
\frac{512i}{9},-\frac{64}{3},\frac{4i}{3},\frac i4,-\frac{4i}{3}\right),\\
q&=\left(\frac i4,\frac{256i}{3},\frac{16}{3}\right),\\
\frac i4q&=\left(-\frac1{16},-\frac{64}{3},\frac{4i}{3}\right),&
-\frac12q&=\left(-\frac i8,-\frac{128i}{3},-\frac83\right),\\
\frac14q&=\left(\frac i{16},\frac{64i}{3},\frac43\right),&
-\frac g{2\sigma}q
&=\left(-\frac{ig}{8\sigma},-\frac{128ig}{3\sigma},
-\frac{8g}{3\sigma}\right).
\end{aligned}
\tag{V3}
```

These are the spinor/triplet factors in (GA09)–(GA15) and (W1), respectively;
gamma order and odd-spinor order are unchanged. In the common gauge,
dilatino factors vanish; terms containing two gravitini and two $`\chi`$
or two $`\widehat R(Q)`$ are removed by $`\Pi_{\le2}`$. Thus 52 groups shown in (W1) remain
from the 73 term groups of source (GA24). This check verifies coefficient
multiplication from map data to density, not the map's SUSY transformation.

<a id="9-the-single-fixed-total-action"></a>

## The single fixed total action

In (5.10) of the two-derivative file, the first large bracket multiplied
by $`-2`$ is the linear map of §6 evaluated at (P). The last bracket
is the $`2gV_{\rm defining}`$ contribution of the same effective vector.
Checking this directly in components gives

```math
\begin{aligned}
\rho_{\rm eff}\big|_{\rm P}&=\rho_{\rm linear}\big|_{\rm P}+2g,\\
\lambda_{{\rm eff}\,i}\big|_{\rm P}
&=\lambda_{{\rm linear}\,i}\big|_{\rm P},\\
Y_{{\rm eff}\,ij}\big|_{\rm P}
&=Y_{{\rm linear}\,ij}\big|_{\rm P}-g^2L_{ij},\\
F_{{\rm eff}\,\mu\nu}\big|_{\rm P}
&=F_{{\rm linear}\,\mu\nu}\big|_{\rm P}+2gG_{\mu\nu},\\
-2(-g^2L^{ij}L_{ij})&=+2g^2L^2,\\
-2(2g)\left[N+\frac12\bar\psi_a\gamma^a\varphi
+\frac{iL}{4\sqrt2}\delta_{ij}
 \bar\psi_a^i\gamma^{ab}\psi_b^j\right]
&=-4g\left[N+\frac12\bar\psi_a\gamma^a\varphi
+\frac{iL}{4\sqrt2}\delta_{ij}
 \bar\psi_a^i\gamma^{ab}\psi_b^j\right],\\
-2\left(\frac12\,2gG_{\mu\nu}E^{\mu\nu}\right)
&=-2gG_{\mu\nu}E^{\mu\nu}.
\end{aligned}
\tag{S1}
```

These are all coefficients in the last bracket of (5.10).
The same equality can be read as $`-4g[-gL^2/2]=+2g^2L^2`$; no additional
cosmological invariant is inserted.

For example, the scalar map component is

```math
\rho_{{\rm linear}[0]}=\frac{2N}{L},\qquad
\rho_{{\rm linear}[2]}
=\frac{i}{\sqrt2L^2}\delta_{ij}\bar\varphi^i\varphi^j
\tag{S2}
```

so the exact two-fermion selection of this block is

```math
\begin{aligned}
\Pi_{\le2}\Bigg[
\rho_{\rm linear}\left(
N+\frac12\bar\psi_a\gamma^a\varphi
+\frac{iL}{4\sqrt2}\delta_{ij}
 \bar\psi_a^i\gamma^{ab}\psi_b^j\right)\Bigg]
={}&\frac{2N^2}{L}
+\frac{iN}{\sqrt2L^2}\delta_{ij}\bar\varphi^i\varphi^j\\
&+\frac NL\bar\psi_a\gamma^a\varphi
+\frac{iN}{2\sqrt2}\delta_{ij}
 \bar\psi_a^i\gamma^{ab}\psi_b^j .
\end{aligned}
\tag{S3}
```

In the following expression, $`\rho_{\rm linear},\lambda_{\rm linear},Y_{\rm linear}, F_{\rm linear}`$ denote their values **at (P)**.
The map in §6 and derivatives in §8 define them explicitly;
$`Y_{\rm linear}^{ij}=\epsilon^{ik}\epsilon^{j\ell} Y_{{\rm linear}\,k\ell}`$.

```math
\boxed{
\begin{aligned}
S_{\rm total}^{(\le2)}
={}&\int_M d^5x\,e\,\Pi_{\le2}\Bigg[
-2\Bigg\{
\frac{L}{\sqrt2}\delta^{ij}Y_{{\rm linear}\,ij}
+i\bar\lambda_{\rm linear}^{\,i}\varphi_i
-\frac{L}{2\sqrt2}\delta_{ij}
 \bar\psi_a^i\gamma^a\lambda_{\rm linear}^{\,j}
+\frac12F_{{\rm linear}\,\mu\nu}E^{\mu\nu}\\
&\hspace{20mm}
+\rho_{\rm linear}\left(
N+\frac12\bar\psi_a\gamma^a\varphi
+\frac{iL}{4\sqrt2}\delta_{ij}
 \bar\psi_a^i\gamma^{ab}\psi_b^j
\right)
\Bigg\}\\
&-4g\Bigg\{
\frac12G_{\mu\nu}E^{\mu\nu}
+N-\frac g2L^2
+\frac12\bar\psi_a\gamma^a\varphi
+\frac{iL}{4\sqrt2}\delta_{ij}
 \bar\psi_a^i\gamma^{ab}\psi_b^j
\Bigg\}
+\alpha\,\underbrace{\mathscr W_{\rm P}}_{\text{(W1)}}
\Bigg].
\end{aligned}}
\tag{S4}
```

In this equality, $`\Pi_{\le2}`$ is the exact coefficient-selection operator
defined in (V0). The $`\mathcal O(\text{four fermions})`$ expression in source (5.10) is explicitly
fixed by this operator; no unknown remainder is added to the action.

(S4) is the sum
$`S_{2\text{-der}}^{(\le2)}+\alpha S_{\mathrm{Weyl}^2}^{(\le2)}`$
in the common gauge. It is exact in bosons, $`g`$, and the generic
constant $`\alpha\ne0`$, and extends through second order in fermions.
Auxiliary fields are retained off shell. No perturbative expansion
in $`\alpha`$ is made. The source intrasector normalizations and
the boundary representative in (A13)–(A14) are preserved.
