# Symbolic derivations for the action classification

This appendix checks the normalizations in the [main text](../action_family.md), coefficient decompositions of source expressions, and required algebraic convention conversions. The algebraic normalization checks are distinct from proofs of the underlying multiplet constructions and supersymmetry identities. The scope of this distinction is given in the [check record](../../references/component_records/02_action_family.md).

<a id="1-separating-couplings-as-coefficients"></a>

## Separating couplings as coefficients

Denote the source-density block with no explicit fermions by $`\mathcal U`$, its two-explicit-fermion block by $`\mathcal V`$, and the separate bosonic record by $`\mathcal B`$. For $`X\in\{\mathcal U,\mathcal V, \mathcal B\}`$, the source expressions are affine polynomials in the three couplings:

```math
X=X_2+\alpha X_W+\beta X_{\log}+\zeta X_R.
```

This identity was checked by separating every coupling monomial: there are no coefficients beyond the constant, $`\alpha`$, $`\beta`$, and $`\zeta`$ monomials. Formal coefficient extraction defines

```math
\begin{aligned}
X_2&=[\alpha^0\beta^0\zeta^0]X,\\
X_W&=[\alpha^1\beta^0\zeta^0]X,\\
X_{\log}&=[\alpha^0\beta^1\zeta^0]X,\\
X_R&=[\alpha^0\beta^0\zeta^1]X
\end{aligned}
```

This operation assigns no numerical values to couplings. For example, the source coefficient $`D^2`$ directly gives

```math
\begin{aligned}
\left(\frac{64}{3}\alpha+16\zeta\right)D^2
&=\alpha\left(\frac{64}{3}D^2\right)
 +\zeta\left(16D^2\right),\\
[\alpha]\left[\left(\frac{64}{3}\alpha+16\zeta\right)D^2\right]
&=\frac{64}{3}D^2,\\
[\zeta]\left[\left(\frac{64}{3}\alpha+16\zeta\right)D^2\right]
&=16D^2.
\end{aligned}
```

Each output block was decomposed again, and the exact rational coefficients of ordered products were compared with the source. The order of spinor, gamma, and derivative factors was unchanged. Derivative brackets were preserved; no integration by parts or boundary condition was used.

The bosonic form obtained from the source expression $`\mathcal U`$ was also compared with the independently recorded file $`\mathcal B`$. Hats become bosonic definitions, while $`\mathcal D`$ and $`\Box^c`$ become $`\mathscr D`$ and $`\Box_{\mathrm B}^c`$; objects such as $`T,D,f`$ are read using the [bosonic dictionary](../fields_and_derivatives.md). Agreement of these two records is not a SUSY verification of the underlying action.

<a id="2-selecting-curvature-coefficients"></a>

## Selecting curvature coefficients

Below, $`\supset`$ tracks only the coefficients of the specified curvature monomials. No field is set to zero, no background is selected, and no action truncation is performed. Here $`R_{abcd}`$ is the degree-zero torsionless curvature. The bosonic definition of the dependent connection gives

```math
\begin{aligned}
f_{ab}&=-\frac16R_{ab}+\frac1{48}\eta_{ab}R,\\
f_a{}^a&=\left(-\frac16+\frac5{48}\right)R=-\frac1{16}R,\\
2f_{ab}&=-\frac13R_{ab}+\frac1{24}\eta_{ab}R,\\
\Box_{\mathrm B}^c\sigma&=2f_a{}^a=-\frac18R,\\
D&\supset\frac12f_a{}^a=-\frac1{32}R.
\end{aligned}
```

The source scalar and triplet conformal boxes use the $`2w f_a{}^a X`$ connection term of a primary scalar with Weyl weight $`w`$. Here $`w(\sigma)=1`$ and $`w(L)=w(L^{ij})=3`$. Together with the $`6Lf_a{}^a`$ term in the box definition of the two-derivative construction, this fixes the curvature coefficients under consideration as

```math
\begin{aligned}
\Box_{\mathrm B}^c L&\supset6Lf_a{}^a=-\frac38LR,\\
\Box_{\mathrm B}^c L^{ij}&\supset6L^{ij}f_a{}^a=-\frac38L^{ij}R
\end{aligned}
```

The ratio of the connection coefficient to the weight is $`6/2=3/1`$; $`\Box^c\sigma=0`$ does not follow from the notation $`\sigma=1`$. These source operator definitions are not an independent proof of the full superconformal algebra.

### Two-derivative normalization

In the [bosonic two-derivative density](../two_derivative_action/bosonic.md), the two groups carrying the pure $`LR`$ coefficient are $`-8DL`$ and $`-2\Box_{\mathrm B}^c L`$. Therefore

```math
\begin{aligned}
\ell_2^{(0)}
&\supset-8L\left(-\frac{R}{32}\right)
-2\left(-\frac38LR\right)\\
&=\frac14LR+\frac34LR=LR.
\end{aligned}
```

### R-squared normalization

The three groups in the [bosonic R-squared file](../../r2/action/bosonic.md) contributing to this coefficient are

```math
\ell_R^{(0)}\supset
16D^2+\frac8L D\Box_{\mathrm B}^c L
+\frac1{L^2}(\Box_{\mathrm B}^c L_{ij})
                 (\Box_{\mathrm B}^c L^{ij})
```

Using $`L_{ij}L^{ij}=L^2`$ and the source domain $`L>0`$,

```math
\begin{aligned}
\ell_R^{(0)}
&\supset16\frac{R^2}{1024}
 +\frac8L\left(-\frac R{32}\right)\left(-\frac{3LR}{8}\right)
 +\frac1{L^2}\frac{9R^2}{64}L_{ij}L^{ij}\\
&=\left(\frac1{64}+\frac3{32}+\frac9{64}\right)R^2
=\frac14R^2.
\end{aligned}
```

Cancellation of $`L`$ does not extend the result to the $`L=0`$ branch. Other density terms also contain powers of $`L^{-1}`$.

### LOG normalization

In the [bosonic LOG file](../../log/action/bosonic.md), the relevant two groups are

```math
\ell_{\log}^{(0)}\supset
\frac56(\Box_{\mathrm B}^c\sigma)^2
-\frac32(\mathscr D_a\mathscr D_b\sigma)
          (\mathscr D^a\mathscr D^b\sigma)
```

so, using $`\mathscr D_a\mathscr D_b\sigma=2f_{ab}`$,

```math
\begin{aligned}
(2f_{ab})(2f^{ab})
&=\left(-\frac13R_{ab}+\frac1{24}\eta_{ab}R\right)
  \left(-\frac13R^{ab}+\frac1{24}\eta^{ab}R\right)\\
&=\frac19R_{ab}R^{ab}-\frac1{36}R^2+\frac5{576}R^2\\
&=\frac19R_{ab}R^{ab}-\frac{11}{576}R^2,\\
\ell_{\log}^{(0)}
&\supset\frac56\frac{R^2}{64}
-\frac32\left(\frac19R_{ab}R^{ab}-\frac{11}{576}R^2\right)\\
&=-\frac16R_{ab}R^{ab}
+\left(\frac5{384}+\frac{11}{384}\right)R^2\\
&=-\frac16R_{ab}R^{ab}+\frac1{24}R^2.
\end{aligned}
```

### Weyl-squared normalization

The relevant groups in the [bosonic Weyl-squared file](../../weyl2/action/bosonic.md) contain both $`C^2`$ and $`D^2`$:

```math
\begin{aligned}
\ell_W^{(0)}&\supset\frac18C_{abcd}C^{abcd}+\frac{64}{3}D^2\\
&\supset\frac18C_{abcd}C^{abcd}
+\frac{64}{3}\frac{R^2}{1024}
=\frac18C_{abcd}C^{abcd}+\frac1{48}R^2.
\end{aligned}
```

To check the five-dimensional Weyl decomposition by directly squaring it, temporarily define

```math
\begin{aligned}
A_{abcd}&:=\eta_{ac}R_{bd}-\eta_{bc}R_{ad}
             -\eta_{ad}R_{bc}+\eta_{bd}R_{ac},\\
U_{abcd}&:=\eta_{ac}\eta_{bd}-\eta_{ad}\eta_{bc},\\
C_{abcd}&=R_{abcd}-\frac13A_{abcd}+\frac R{12}U_{abcd}
\end{aligned}
```

The dot denotes complete contraction of all four indices. The Ricci definition and Riemann symmetries give

```math
\begin{aligned}
R_{abcd}A^{abcd}&=R_{ab}R^{ab}+R_{ab}R^{ab}
                         +R_{ab}R^{ab}+R_{ab}R^{ab}
=4R_{ab}R^{ab},\\
R_{abcd}U^{abcd}&=R-(-R)=2R,\\
U\cdot U&=25-2(5)+25=40.
\end{aligned}
```

In the notation $`A=P+Q+S+T`$, let $`P_{abcd}=\eta_{ac}R_{bd}`$, $`Q_{abcd}=-\eta_{bc}R_{ad}`$, $`S_{abcd}=-\eta_{ad}R_{bc}`$, and $`T_{abcd}=\eta_{bd}R_{ac}`$. The six cross-contractions give

```math
\begin{aligned}
P\cdot Q=P\cdot S=Q\cdot T=S\cdot T&=-R_{ab}R^{ab},\\
P\cdot T=Q\cdot S&=R^2,\\
P^2=Q^2=S^2=T^2&=5R_{ab}R^{ab}
\end{aligned}
```

and hence

```math
\begin{aligned}
A^2&=20R_{ab}R^{ab}
+2\left(-4R_{ab}R^{ab}+2R^2\right)
=12R_{ab}R^{ab}+4R^2,\\
A\cdot U&=4(5R-R)=16R,\\
C^2&=R_{abcd}R^{abcd}+\frac19A^2+\frac{R^2}{144}U^2
-\frac23R_{abcd}A^{abcd}+\frac R6R_{abcd}U^{abcd}
-\frac R{18}A\cdot U\\
&=R_{abcd}R^{abcd}
+\left(\frac{12}{9}-\frac83\right)R_{ab}R^{ab}
+\left(\frac49+\frac{40}{144}+\frac13-\frac{16}{18}\right)R^2\\
&=R_{abcd}R^{abcd}-\frac43R_{ab}R^{ab}+\frac16R^2.
\end{aligned}
```

In terms of the original curvatures, the Weyl-squared density gives

```math
\begin{aligned}
\ell_W^{(0)}
&\supset\frac18\left(R_{abcd}R^{abcd}
-\frac43R_{ab}R^{ab}+\frac16R^2\right)+\frac1{48}R^2\\
&=\frac18R_{abcd}R^{abcd}-\frac16R_{ab}R^{ab}+\frac1{24}R^2.
\end{aligned}
```

<a id="3-independence-and-gb-coefficient-matching"></a>

## Independence and GB coefficient matching

The coefficient matrix with columns $`(\ell_W,\ell_{\log},\ell_R)`$ and rows $`(R_{abcd}R^{abcd},R_{ab}R^{ab},R^2)`$ is

```math
M=\begin{pmatrix}
1/8&0&0\\
-1/6&-1/6&0\\
1/24&1/24&1/4
\end{pmatrix},
\qquad
\det M=\frac18\left(-\frac16\right)\frac14=-\frac1{192}\ne0.
```

This establishes linear independence at the level of the three specified curvature structures. It does not classify all possible supersymmetric invariants or compute a quotient by field redefinitions.

The general pure curvature-squared polynomial is

```math
\frac\alpha8R_{abcd}R^{abcd}
-\frac{\alpha+\beta}{6}R_{ab}R^{ab}
+\left(\frac{\alpha+\beta}{24}+\frac\zeta4\right)R^2
```

Matching it with $`c\mathcal G`$ and $`\mathcal G=R_{abcd}R^{abcd}-4R_{ab}R^{ab}+R^2`$ gives

```math
\begin{aligned}
c&=\frac\alpha8,\\
-\frac{\alpha+\beta}{6}=-4c
&\ \Longrightarrow\ \alpha+\beta=3\alpha
\ \Longrightarrow\ \beta=2\alpha,\\
\frac{\alpha+\beta}{24}+\frac\zeta4=c
&\ \Longrightarrow\ \frac{3\alpha}{24}+\frac\zeta4=\frac\alpha8
\ \Longrightarrow\ \zeta=0.
\end{aligned}
```

Direct substitution yields

```math
\frac\alpha8R_{abcd}R^{abcd}
-\frac{3\alpha}{6}R_{ab}R^{ab}
+\frac{3\alpha}{24}R^2
=\frac\alpha8\mathcal G
```

Since no division by $`\alpha`$ is made, $`\alpha=0`$ is included. Calling the free coupling of the GB family $`\lambda`$,

```math
(\alpha,\beta,\zeta)=(\lambda,2\lambda,0),
\qquad \ell_G=\ell_W+2\ell_{\log}.
```

Since the formal fermion projection is linear,

```math
\begin{aligned}
\Pi_q(\mathcal U_W+2\mathcal U_{\log}
             +\mathcal V_W+2\mathcal V_{\log})
&=\Pi_q(\mathcal U_W+\mathcal V_W)
 +2\Pi_q(\mathcal U_{\log}+\mathcal V_{\log})\\
&=\ell_W^{(q)}+2\ell_{\log}^{(q)},\qquad q=0,2.
\end{aligned}
```

The bosonic, core, and explicit two-fermion lists in the GB files were compared separately with this identity. The GB combination is not formed only from the $`C^2`$ or $`R^2`$ monomials.

<a id="4-clifford-rewritings-in-the-covariant-dictionary"></a>

## Clifford rewritings in the covariant dictionary

The source notation $`\gamma_\mu{}^{ab}`$ denotes the three-index antisymmetric Clifford element. For $`R'_{ab}(Q)=-R'_{ba}(Q)`$,

```math
\begin{aligned}
\gamma_\mu\gamma^{ab}
&=\gamma_\mu{}^{ab}+2e_\mu{}^{[a}\gamma^{b]},\\
\gamma_\mu{}^{ab}R'_{ab}(Q)
&=\gamma_\mu\gamma^{ab}R'_{ab}(Q)-2\gamma^aR'_{\mu a}(Q),\\
\frac i4\gamma^aR'_{\mu a}(Q)
-\frac i{24}\gamma_\mu{}^{ab}R'_{ab}(Q)
&=\left(\frac i4+\frac i{12}\right)\gamma^aR'_{\mu a}(Q)
-\frac i{24}\gamma_\mu\gamma^{ab}R'_{ab}(Q)\\
&=\frac i3\gamma^aR'_{\mu a}(Q)
-\frac i{24}\gamma_\mu\gamma^{ab}R'_{ab}(Q).
\end{aligned}
```

This is the algebraic equality between the source definition of $`\phi_\mu`$ and its form in the convention file. In addition,

```math
\gamma^{ab}\gamma_c
=\gamma_c{}^{ab}+\delta_c^b\gamma^a-\delta_c^a\gamma^b
```

using the identity

```math
2iT_{ab}\gamma^{ab}\gamma_{[\mu}\psi_{\nu]}
=2iT_{ab}\gamma_{[\mu}{}^{ab}\psi_{\nu]}
-4iT_{[\mu|b|}\gamma^b\psi_{\nu]}
```

the two $`T`$ terms in the source notation $`R'(Q)`$ combine into the single Clifford product of the common conventions.

Finally, using $`\gamma^a\gamma^{cd} =\gamma^{acd}+\eta^{ac}\gamma^d-\eta^{ad}\gamma^c`$,

```math
\begin{aligned}
\gamma^a\gamma^{cd}\gamma^b
={}&\gamma^{acdb}
 +\eta^{ab}\gamma^{cd}-\eta^{cb}\gamma^{ad}
 +\eta^{db}\gamma^{ac}\\
&+\eta^{ac}\gamma^{db}-\eta^{ad}\gamma^{cb}
 +\eta^{ac}\eta^{db}-\eta^{ad}\eta^{cb},\\
T_{cd}\gamma^a\gamma^{cd}\gamma^b
={}&T_{cd}\gamma^{abcd}+\eta^{ab}T_{cd}\gamma^{cd}
 +2T_c{}^b\gamma^{ac}+2T^a{}_d\gamma^{db}+2T^{ab}.
\end{aligned}
```

The intermediate rank-two gamma terms are symmetric under $`a,b`$. Antisymmetrization gives

```math
\gamma^{[a}(T_{cd}\gamma^{cd})\gamma^{b]}
=T_{cd}\gamma^{abcd}+2T^{ab}
```

This identity establishes equality of the source expression $`R'(M)`$, with its $`T`$ block, and the common-convention form. Since no spinors are interchanged, it requires no new adjoint or charge-conjugation convention.

<a id="5-expansion-check-for-bosonic-composites"></a>

## Expansion check for bosonic composites

From the common convention $`\varepsilon`$

```math
\varepsilon_{abcde}\varepsilon^{abfgh}H^{cde}H_{fgh}
=-2!3!\,\delta_{[c}^{f}\delta_d^g\delta_{e]}^h H^{cde}H_{fgh}
=-12H_{abc}H^{abc}.
```

Therefore, for $`T_{ab}=G_{ab}/8+\varepsilon_{abcde}H^{cde}/48`$,

```math
\begin{aligned}
T_{ab}T^{ab}
&=\frac1{64}G_{ab}G^{ab}
+\frac2{8\cdot48}\varepsilon_{abcde}G^{ab}H^{cde}
-\frac{12}{48^2}H_{abc}H^{abc}\\
&=\frac1{64}G_{ab}G^{ab}
+\frac1{192}\varepsilon_{abcde}G^{ab}H^{cde}
-\frac1{192}H_{abc}H^{abc},\\
G^{ab}T_{ab}
&=\frac18G_{ab}G^{ab}
+\frac1{48}\varepsilon_{abcde}G^{ab}H^{cde}.
\end{aligned}
```

Substitution into the source's bosonic definition of $`D`$ gives

```math
\begin{aligned}
D={}&-\frac R{32}-\frac1{16}G^2-\frac{26}{3}T^2+2G\cdot T
+\frac g4N+\frac{g^2}{16}L^2\\
={}&-\frac R{32}
+\left(-\frac1{16}-\frac{26}{192}+\frac14\right)G_{ab}G^{ab}\\
&+\left(-\frac{26}{576}+\frac1{24}\right)
\varepsilon_{abcde}G^{ab}H^{cde}
+\frac{26}{576}H_{abc}H^{abc}+\frac g4N+\frac{g^2}{16}L^2\\
={}&-\frac R{32}+\frac5{96}G_{ab}G^{ab}
-\frac1{288}\varepsilon_{abcde}G^{ab}H^{cde}
+\frac{13}{288}H_{abc}H^{abc}+\frac g4N+\frac{g^2}{16}L^2.
\end{aligned}
```

This check establishes algebraic equality of the two recorded forms of $`D`$; it does not rederive the composite's SUSY transformation.

<a id="6-scope-of-the-check"></a>

## Scope of the check

No values were assigned to free parameters in the calculations above. Curvature contractions were also checked while retaining all independent symbolic curvature components; Clifford identities were checked with exact arithmetic at the level of antisymmetric-basis coefficients.

This appendix documents normalization, curvature, and Clifford matching. Known invariant constructions are adopted through the [literature map](../../references/bibliography.md).
