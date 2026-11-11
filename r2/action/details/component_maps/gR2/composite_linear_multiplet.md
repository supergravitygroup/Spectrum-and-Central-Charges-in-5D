Source superconformal definitions of $`\mathcal D\rho_A`$, $`\mathcal D\lambda_A^i`$, $`\Box^c\rho_A`$, $`\widehat F_A`$,
and dependent connections are in
[superconformal_definitions.md](../../../../../common/details/superconformal_definitions.md).
Section 2.2 of that record explicitly gives the fermion derivative with
a lower SU(2) index. All $`\mathcal D`$ and $`\Box^c`$ operators use its corrected
definitions. In particular, the plus-sign Lorentz connection in Section 4.4
applies to $`\mathcal D_bT^{ab}`$. Section 6.4 derives the correction of the source
$`\delta Y`$ coefficients and the need for coefficient $`i/4`$ in the $`(\mathord{\not{\mathcal D}}\rho)\lambda`$
term below; the coefficient $`i/2`$ of the $`\rho\mathord{\not{\mathcal D}}\lambda`$ term is retained.

```math
\boxed{
L_{1ij}
=\rho_1Y_{2ij}+\rho_2Y_{1ij}
-\frac{i}{2}\bar\lambda_{1(i}\lambda_{2j)}.
}
```

```math
\boxed{
\begin{aligned}
\varphi_{1i}
={}&\frac{i}{2}\left(
\rho_1\mathord{\not{\mathcal D}}\lambda_{2i}
+\rho_2\mathord{\not{\mathcal D}}\lambda_{1i}
\right)
+\gamma\!\cdot\!T\left(
\rho_1\lambda_{2i}+\rho_2\lambda_{1i}
\right)
-8\rho_1\rho_2\chi_i\\
&-\frac18\left(
\gamma\!\cdot\!\widehat F_1\lambda_{2i}
+\gamma\!\cdot\!\widehat F_2\lambda_{1i}
\right)
+\frac{i}{4}\left[
(\mathord{\not{\mathcal D}}\rho_1)\lambda_{2i}
+(\mathord{\not{\mathcal D}}\rho_2)\lambda_{1i}
\right]\\
&-\frac12\left(
Y_{1ij}\lambda_2^j+Y_{2ij}\lambda_1^j
\right).
\end{aligned}
}
```

```math
\boxed{
\begin{aligned}
E_1^a
={}&\mathcal D_b\left[
-\frac12\left(
\rho_1\widehat F_2^{ab}+\rho_2\widehat F_1^{ab}
\right)
+8\rho_1\rho_2T^{ab}
-\frac{i}{4}\bar\lambda_1\gamma^{ab}\lambda_2
\right]\\
&-\frac18\varepsilon^{abcde}
\widehat F_{1bc}\widehat F_{2de}.
\end{aligned}
}
```

```math
\boxed{
\begin{aligned}
N_1
={}&\frac12\left(
\rho_1\Box^c\rho_2+\rho_2\Box^c\rho_1
\right)
+\frac12\mathcal D_a\rho_1\mathcal D^a\rho_2
-\frac14\widehat F_{1ab}\widehat F_2^{ab}
+Y_{1ij}Y_2^{ij}\\
&+4\left(
\rho_1\widehat F_{2ab}+\rho_2\widehat F_{1ab}
\right)T^{ab}
-4\rho_1\rho_2\left(D+\frac{26}{3}T^2\right)\\
&-\frac14\left(
\bar\lambda_1\mathord{\not{\mathcal D}}\lambda_2
+\bar\lambda_2\mathord{\not{\mathcal D}}\lambda_1
\right)
+i\bar\lambda_1\gamma\!\cdot\!T\,\lambda_2\\
&+8i\left(
\rho_1\bar\chi\lambda_2+\rho_2\bar\chi\lambda_1
\right).
\end{aligned}
}
```

<a id="e_1ab-potential"></a>

# $`E_1^{ab}`$ potential

Multiplet labels $`A=1,2`$ always appear first in the subscript group.
Potentials of the two input vector multiplets are written $`A_{A\mu}`$,
and field strengths $`F_{A\mu\nu}=2\partial_{[\mu}A_{A\nu]}`$. The input vector labeled $`1`$ is the
same vector multiplet denoted $`\rho_1`$, $`\lambda_{1i}`$, $`Y_{1ij}`$, and $`A_{1\mu}`$ in the BF file.
Earlier upper or lower label placement does not distinguish another multiplet.

<a id="1-relation-determining-the-potential"></a>

### Relation determining the potential

Using local `multiplets.pdf` (3.3)–(3.6), (3.12)–(3.13), and project epsilon normalization,

```math
\begin{aligned}
E_1^{ab}&=-\frac1{12}\varepsilon^{abcde}E_{1cde},\qquad
E_{1abc}=\varepsilon_{abcde}E_1^{de},\\
E_1^{\mu\nu}&=e_a{}^\mu e_b{}^\nu E_1^{ab},\\
P_1^a
&=e_\mu{}^a e^{-1}\partial_\nu(eE_1^{\mu\nu})\\
&=E_1^a+\frac i2\bar\psi_b^i\gamma^{ba}\varphi_{1i}
+\frac14\bar\psi_b^i\gamma^{abc}\psi_c^jL_{1ij}.
\end{aligned}
```

Let the two temporary abbreviations used in the calculation be

```math
\begin{aligned}
Q_1^{ab}
&\equiv-\frac12(\rho_1\widehat F_2^{ab}+\rho_2\widehat F_1^{ab})
+8\rho_1\rho_2T^{ab}-\frac i4\bar\lambda_1\gamma^{ab}\lambda_2,\\
U^i&\equiv\rho_1\lambda_2^i+\rho_2\lambda_1^i
\end{aligned}
```

The composite vector component above is

```math
E_1^a=\mathcal D_bQ_1^{ab}
-\frac18\varepsilon^{abcde}\widehat F_{1bc}\widehat F_{2de}
```

Since $`\mathcal D`$ is supercovariant, the identity $`E_1^{ab}=Q_1^{ab}`$ does not follow.
The ordinary divergence of the potential must reproduce $`P_1^a`$.

<a id="2-coefficients-of-gravitino-contributions"></a>

### Coefficients of gravitino contributions

In source (3.5), the two-index potential has no independent $`S`$
transformation. The required transformations from (3.8), (A.3), and (3.9) are

```math
\begin{aligned}
\delta_S\rho_A&=0,\qquad
\delta_S\lambda_A^i=\rho_A\eta^i,\qquad
\delta_S\psi_a^i=-i\gamma_a\eta^i,\\
\delta_ST_{ab}&=0,\qquad \delta_SA_{A\mu}=0,\qquad
\delta_S\widehat F_{Aab}=i\bar\eta\gamma_{ab}\lambda_A.
\end{aligned}
```

Substituting $`\widehat F_{Aab} =F_{Aab}-\bar\psi_{[a}\gamma_{b]}\lambda_A +\frac i2\rho_A\bar\psi_{[a}\psi_{b]}`$ into the final equality gives

```math
\begin{aligned}
\delta_S\widehat F_{Aab}
&=i\bar\eta\gamma_{[a}\gamma_{b]}\lambda_A
-\rho_A\bar\psi_{[a}\gamma_{b]}\eta\\
&\quad+\frac12\rho_A\left(
\bar\eta\gamma_{[a}\psi_{b]}
+\bar\psi_{[a}\gamma_{b]}\eta\right)\\
&=i\bar\eta\gamma_{ab}\lambda_A
-\rho_A\bar\psi_{[a}\gamma_{b]}\eta
+\rho_A\bar\psi_{[a}\gamma_{b]}\eta
=i\bar\eta\gamma_{ab}\lambda_A.
\end{aligned}
```

This uses Majorana conjugation and the NW–SE rank-one flip.
The NW–SE rank-two flip gives $`\bar\lambda_1\gamma^{ab}\lambda_2 =\bar\lambda_2\gamma^{ab}\lambda_1`$. Thus

```math
\begin{aligned}
\delta_SQ_1^{ab}
&=-\frac i2\bar\eta\gamma^{ab}
(\rho_1\lambda_2+\rho_2\lambda_1)
-\frac i4\bar\eta\gamma^{ab}
(\rho_1\lambda_2+\rho_2\lambda_1)\\
&=-\frac{3i}{4}\bar\eta\gamma^{ab}U.
\end{aligned}
```

To cancel this variation, let $`h`$ be the coefficient of the gravitino
term and $`k`$ that of its induced two-gravitino term. In five dimensions,

```math
\gamma_c\gamma^{abc}=3\gamma^{ab},\qquad
\gamma_c\gamma^{abcd}=2\gamma^{abd},\qquad
\gamma^{abcd}\gamma_d=2\gamma^{abc}
```

and, using $`\delta_SU=2\rho_1\rho_2\eta`$,

```math
\begin{aligned}
\delta_S(\bar\psi_c\gamma^{abc}U)
&=-i\bar\eta\gamma_c\gamma^{abc}U
+2\rho_1\rho_2\bar\psi_c\gamma^{abc}\eta\\
&=-3i\bar\eta\gamma^{ab}U
+2\rho_1\rho_2\bar\psi_c\gamma^{abc}\eta,\\
\delta_S(\rho_1\rho_2\bar\psi_c\gamma^{abcd}\psi_d)
&=-i\rho_1\rho_2\left(
\bar\eta\gamma_c\gamma^{abcd}\psi_d
+\bar\psi_c\gamma^{abcd}\gamma_d\eta\right)\\
&=-2i\rho_1\rho_2\left(
\bar\eta\gamma^{abd}\psi_d+\bar\psi_c\gamma^{abc}\eta\right)\\
&=-4i\rho_1\rho_2\bar\psi_c\gamma^{abc}\eta.
\end{aligned}
```

The final line uses the NW–SE rank-three flip, $`-t_3=+1`$.
Coefficients of the two independent structures vanish separately:

```math
\begin{aligned}
-\frac{3i}{4}-3ih=0&\quad\Longrightarrow\quad h=-\frac14,\\
2h-4ik=0
\quad\Longrightarrow\quad-\frac12-4ik=0
&\quad\Longrightarrow\quad k=\frac i8.
\end{aligned}
```

The temporary two-index expression including gravitino contributions is therefore

```math
J_1^{ab}\equiv Q_1^{ab}
-\frac14\bar\psi_c\gamma^{abc}U
+\frac i8\rho_1\rho_2\bar\psi_c\gamma^{abcd}\psi_d
```

This does not solve for auxiliary fields; it determines fermionic
contributions to the same composite potential.

<a id="3-comparison-of-ordinary-and-supercovariant-divergence"></a>

### Comparison of ordinary and supercovariant divergence

For any antisymmetric tangent tensor $`X^{ab}`$, temporarily denote
the ordinary density divergence by

```math
\mathfrak d_bX^{ab}\equiv
e_\mu{}^a e^{-1}\partial_\nu
\left(e\,e_c{}^\mu e_d{}^\nu X^{cd}\right)
```

This operator is not $`\mathcal D_b`$. Using the source's dependent $`R(P)=0`$
connection definition, for $`Q_1^{ab}`$ of weight $`3`$, its relation
to the covariant derivative $`D^{(0)}`$ with $`Q,S`$ connections removed is

```math
D_b^{(0)}Q_1^{ab}
=\mathfrak d_bQ_1^{ab}
-\frac14\bar\psi_b\gamma^a\psi_c\,Q_1^{bc}
+\frac12\bar\psi_b\gamma^b\psi_c\,Q_1^{ac}
```

Here $`D^{(0)}`$ retains Lorentz, dilatation, and any internal connections.
The $`b_\mu`$ contributions cancel in this divergence because $`w(Q_1)=5-2=3`$;
the condition $`b_\mu=0`$ has not been imposed.

The $`Q,S`$ connections in the supercovariant derivative are added
by subtracting the $`\epsilon\to\psi_b`$ and $`\eta\to\phi_b`$ substitutions in $`\delta_QQ_1^{ab}`$
and $`\delta_SQ_1^{ab}`$, respectively:

```math
\begin{aligned}
\mathcal D_bQ_1^{ab}
={}&D_b^{(0)}Q_1^{ab}
-\left.\delta_QQ_1^{ab}\right|_{\epsilon\to\psi_b}
-\left.\delta_SQ_1^{ab}\right|_{\eta\to\phi_b},\\
-\left.\delta_SQ_1^{ab}\right|_{\eta\to\phi_b}
={}&+\frac{3i}{4}\bar\phi_b\gamma^{ab}U.
\end{aligned}
```

The field-strength transformation used in the calculation, after
inserting corrected (3.8) and (A.3) into (3.9), is

```math
\delta_Q\widehat F_{Aab}
=-\bar\epsilon\gamma_{[a}\mathcal D_{b]}\lambda_A
-\frac i2\rho_A\bar\epsilon\widehat R_{ab}(Q)
+i\bar\epsilon\gamma_{[a}(\gamma\!\cdot\!T)\gamma_{b]}\lambda_A
```

This transformation uses the same version of the $`\mathcal D\rho_A`$, $`\mathcal D\lambda_A`$,
$`\mathcal D T`$, and dependent $`\phi_b`$ definitions. The ordinary Leibniz
expansions of the two gravitino corrections are

```math
\begin{aligned}
\mathfrak d_b\left(-\frac14\bar\psi_c\gamma^{abc}U\right)
&=-\frac14\nabla_b\bar\psi_c\,\gamma^{abc}U
-\frac14\bar\psi_c\gamma^{abc}\nabla_bU,\\
\mathfrak d_b\left(\frac i8\rho_1\rho_2
\bar\psi_c\gamma^{abcd}\psi_d\right)
&=\frac i8\partial_b(\rho_1\rho_2)
\bar\psi_c\gamma^{abcd}\psi_d\\
&\quad+\frac i8\rho_1\rho_2\left[
(\nabla_b\bar\psi_c)\gamma^{abcd}\psi_d
+\bar\psi_c\gamma^{abcd}\nabla_b\psi_d\right],\\
\partial_b(\rho_1\rho_2)
&=\rho_1\partial_b\rho_2+\rho_2\partial_b\rho_1,\\
\nabla_bU
&=(\partial_b\rho_1)\lambda_2+\rho_1\nabla_b\lambda_2
+(\partial_b\rho_2)\lambda_1+\rho_2\nabla_b\lambda_1.
\end{aligned}
```

Here $`\nabla`$ is only the ordinary Levi–Civita/spin derivative; contorsion
contributions remain in the $`D^{(0)}-\mathfrak d`$ difference above and in supercovariant
derivatives. Internal indices in these equalities use NW–SE contractions.

Comparison of these expansions with the composite $`L_{1ij},\varphi_{1i}`$ gives
the exact divergence relation:

```math
\boxed{
\begin{aligned}
\mathfrak d_bJ_1^{ab}
={}&\mathcal D_bQ_1^{ab}
+\frac i2\bar\psi_b^i\gamma^{ba}\varphi_{1i}
+\frac14\bar\psi_b^i\gamma^{abc}\psi_c^jL_{1ij}\\
&-\frac18\varepsilon^{abcde}\left(
\widehat F_{1bc}\widehat F_{2de}-F_{1bc}F_{2de}\right).
\end{aligned}}
```

In particular, the derivative contribution in the dependent $`S`$
connection is

```math
\bar\phi_b\gamma^{ab}
=\frac i6\overline{\widehat R'_{cd}(Q)}\gamma^{acd},\qquad
\frac{3i}{4}\bar\phi_b\gamma^{ab}U
=-\frac18\overline{\widehat R'_{cd}(Q)}\gamma^{acd}U
```

The $`2\partial_{[c}\psi_{d]}`$ part inside $`\widehat R'_{cd}(Q)`$ produces $`-\frac14(\partial_c\bar\psi_d)\gamma^{acd}U`$.
This is the gravitino derivative of the first Leibniz expansion.
Matter-fermion derivatives enter its second term through $`\gamma^{ab}\gamma^c=\gamma^{abc}+2\gamma^{[a}\eta^{b]c}`$.
The $`Y`$ and $`\chi`$ contributions match the explicit coefficients
in $`\varphi_{1i}`$ and $`L_{1ij}`$, respectively. The identity used for
four-fermion terms is

```math
\lambda_j\bar\lambda^i
=-\frac14(\bar\lambda^i\lambda_j)
-\frac14(\bar\lambda^i\gamma^c\lambda_j)\gamma_c
+\frac18(\bar\lambda^i\gamma^{cd}\lambda_j)\gamma_{cd}
```

together with its bilinear version for different input fermions.
The field-strength difference also includes four-fermion contributions.
Explicitly, defining $`\Delta_{Aab}\equiv\widehat F_{Aab}-F_{Aab} =-\bar\psi_{[a}\gamma_{b]}\lambda_A +\frac i2\rho_A\bar\psi_{[a}\psi_{b]}`$ gives

```math
\widehat F_{1bc}\widehat F_{2de}-F_{1bc}F_{2de}
=F_{1bc}\Delta_{2de}+\Delta_{1bc}F_{2de}
+\Delta_{1bc}\Delta_{2de}.
```

The final product is retained; this is not a two-fermion truncation.
Thus the $`P_1^a`$ relation above reduces to

```math
\begin{aligned}
P_1^a
&=\mathcal D_bQ_1^{ab}
-\frac18\varepsilon^{abcde}\widehat F_{1bc}\widehat F_{2de}
+\frac i2\bar\psi_b^i\gamma^{ba}\varphi_{1i}
+\frac14\bar\psi_b^i\gamma^{abc}\psi_c^jL_{1ij}\\
&=\mathfrak d_bJ_1^{ab}
+\frac18\varepsilon^{abcde}
(\widehat F_{1bc}\widehat F_{2de}-F_{1bc}F_{2de})
-\frac18\varepsilon^{abcde}\widehat F_{1bc}\widehat F_{2de}\\
&=\mathfrak d_bJ_1^{ab}
-\frac18\varepsilon^{abcde}F_{1bc}F_{2de}
\end{aligned}
```

Hatted field strengths become ordinary ones after including
the gravitino contributions.

<a id="4-integration-of-the-chernsimons-term"></a>

### Integration of the Chern–Simons term

For ordinary field strengths, $`\partial_{[\nu}F_{A\sigma\lambda]}=0`$.
Using this identity and $`F_{A\nu\rho}=2\partial_{[\nu}A_{A\rho]}`$,

```math
\begin{aligned}
&e^{-1}\partial_\nu\left[
\epsilon^{\mu\nu\rho\sigma\lambda}
(A_{1\rho}F_{2\sigma\lambda}+A_{2\rho}F_{1\sigma\lambda})
\right]\\
&\quad=e^{-1}\epsilon^{\mu\nu\rho\sigma\lambda}\left[
(\partial_\nu A_{1\rho})F_{2\sigma\lambda}
+(\partial_\nu A_{2\rho})F_{1\sigma\lambda}
+A_{1\rho}\partial_\nu F_{2\sigma\lambda}
+A_{2\rho}\partial_\nu F_{1\sigma\lambda}
\right]\\
&\quad=\frac12e^{-1}\epsilon^{\mu\nu\rho\sigma\lambda}
(F_{1\nu\rho}F_{2\sigma\lambda}
+F_{2\nu\rho}F_{1\sigma\lambda})\\
&\quad=e^{-1}\epsilon^{\mu\nu\rho\sigma\lambda}
F_{1\nu\rho}F_{2\sigma\lambda}.
\end{aligned}
```

In the final line, exchanging the two antisymmetric index pairs has
a plus sign. The Chern–Simons contribution and its divergence are therefore

```math
\begin{aligned}
K_1^{ab}&\equiv-\frac18\varepsilon^{abcde}
(A_{1c}F_{2de}+A_{2c}F_{1de}),\\
\mathfrak d_bK_1^{ab}
&=-\frac18\varepsilon^{abcde}F_{1bc}F_{2de}
\end{aligned}
```

Thus $`P_1^a=\mathfrak d_b(J_1^{ab}+K_1^{ab})`$ holds.

<a id="5-result-and-direct-back-substitution"></a>

### Result and direct back-substitution

Removing temporary abbreviations, the local composite-potential
representative used in this calculation is

```math
\boxed{
\begin{aligned}
E_1^{ab}
={}&-\frac12\left(
\rho_1\widehat F_2^{ab}+\rho_2\widehat F_1^{ab}\right)
+8\rho_1\rho_2T^{ab}
-\frac i4\bar\lambda_1\gamma^{ab}\lambda_2\\
&-\frac14\bar\psi_c\gamma^{abc}
\left(\rho_1\lambda_2+\rho_2\lambda_1\right)
+\frac i8\rho_1\rho_2\bar\psi_c\gamma^{abcd}\psi_d\\
&-\frac18\varepsilon^{abcde}
\left(A_{1c}F_{2de}+A_{2c}F_{1de}\right).
\end{aligned}}
```

Its reproduction of the component is explicitly

```math
\begin{aligned}
&e_\mu{}^a e^{-1}\partial_\nu(eE_1^{\mu\nu})
-\frac i2\bar\psi_b^i\gamma^{ba}\varphi_{1i}
-\frac14\bar\psi_b^i\gamma^{abc}\psi_c^jL_{1ij}\\
&\quad=\mathcal D_b\left[
-\frac12(\rho_1\widehat F_2^{ab}+\rho_2\widehat F_1^{ab})
+8\rho_1\rho_2T^{ab}-\frac i4\bar\lambda_1\gamma^{ab}\lambda_2
\right]
-\frac18\varepsilon^{abcde}\widehat F_{1bc}\widehat F_{2de}
=E_1^a
\end{aligned}
```

The two-index object used in the BF file is this $`E_1^{ab}`$;
the BF density retains its own $`\widehat F_{1ab}E_1^{ab}`$ notation.
