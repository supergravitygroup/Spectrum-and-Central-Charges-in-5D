# First two transformations of the Weyl-squared multiplet

## Equations checked

The results of this appendix, with physical fermion degrees displayed, are

```math
\begin{aligned}
[\delta_Q L_W^{ij}]_1&=i\bar\epsilon^{(i}[\varphi_W^{j)}]_1,
&[\delta_S L_W^{ij}]_1&=0,\\
[\delta_Q\varphi_W^i]_0
&=-\frac i2\gamma^a\mathcal D_aL_W^{ij(0)}\epsilon_j
 -\frac i2\gamma^aE_{Wa}^{(0)}\epsilon^i
 +\frac12N_W^{(0)}\epsilon^i
 -\gamma^{ab}T_{ab}L_W^{ij(0)}\epsilon_j,
&[\delta_S\varphi_W^i]_0&=3L_W^{ij(0)}\eta_j
\end{aligned}
```

The quantities $`L_W`$, $`\varphi_W`$, $`N_W`$, and $`E_W`$ are components of the [source Weyl map](details/linear_multiplet.md). This calculation uses Standard-Weyl covariants; their gauged composite forms are defined in the [shared dictionary](../../common/fields_and_derivatives.md). No new field elimination or background choice is made.

This appendix checks the four graded equations above. Applying the [general-density SUSY identity](../../common/details/vector_linear_density.md) to a particular action additionally requires matching all composite components of that action to the required transformation coefficients.

<a id="1-curvature-projection-and-derivative-rules"></a>

## Curvature projection and derivative rules

Throughout this calculation, introduce the temporary abbreviations

```math
Q_{ab}^i:=\widehat R_{ab}^i(Q),\quad
\mathsf T:=\gamma^{ab}T_{ab},\quad
U_{ab}^{ij}:=\widehat R_{ab}^{ij}(V),\quad
C_{abcd}:=\widehat R_{abcd}(M)
```

The tensor $`Q_{ab}`$ is antisymmetric and satisfies $`\gamma^aQ_{ab}=0`$. For an arbitrary antisymmetric spinor tensor $`X_{ab}`$, define

```math
\begin{aligned}
\Phi_a[X]&:=\frac i3\gamma^bX_{ab}
 -\frac i{24}\gamma_a\gamma^{bc}X_{bc},\\
(\mathcal PX)_{ab}&:=X_{ab}-i\gamma_a\Phi_b[X]+i\gamma_b\Phi_a[X]
\end{aligned}
```

The Clifford contractions in the [connection derivation](../../common/details/composite_fields.md) directly yield

```math
\gamma^a(\mathcal PX)_{ab}=0,qquad
\mathcal P Q=Q,qquad \mathcal P^2=\mathcal P
```

Thus $`Q=\mathcal PX`$ used in the check covers all gamma-traceless spinor curvatures; no particular curvature is selected.

Direct variation of the gravitino definition gives the primed part of the zero-fermion $`Q`$ variation:

```math
\begin{aligned}
\mathcal A_{ab}{}^i{}_j\epsilon^j
:=[\delta_Q R'_{ab}{}^i(Q)]_0
={}&\frac14R_{ab cd}(\omega)\gamma^{cd}\epsilon^i
 +U_{ab}{}^i{}_j\epsilon^j\\
&+i\big[(\nabla_a\mathsf T)\gamma_b
       -(\nabla_b\mathsf T)\gamma_a\big]\epsilon^i\\
&-\mathsf T(\gamma_a\mathsf T\gamma_b
            -\gamma_b\mathsf T\gamma_a)\epsilon^i
\end{aligned}
```

For example, the $`\nabla\epsilon`$ terms cancel through

```math
i\mathsf T(\gamma_b\nabla_a\epsilon-\gamma_a\nabla_b\epsilon)
+i\mathsf T(\gamma_a\nabla_b\epsilon-\gamma_b\nabla_a\epsilon)=0
```

Here $`\nabla`$ is the derivative with bosonic connections.

```math
[\delta_Q\phi_a]_0=\Phi_a[\mathcal A]\epsilon,qquad
[\delta_QQ_{ab}]_0=(\mathcal P\mathcal A)_{ab}\epsilon.
```

The same operation in the $`S`$ variation gives

```math
\begin{aligned}
[\delta_S R'_{ab}(Q)]_0
&=-i\gamma_b\nabla_a\eta+i\gamma_a\nabla_b\eta
 +2\mathsf T\gamma_{ab}\eta,\\
[\delta_S\phi_a]_0
&=\nabla_a\eta+\Phi_a[2\mathsf T\gamma_{cd}]\eta,\\
[\delta_SQ_{ab}]_0&=\mathcal P(2\mathsf T\gamma_{ab})\eta\\
&=\left(-8T_{ab}+\frac{16}{3}T_{[a}{}^c\gamma_{b]c}
 +\frac43\gamma_{abcd}T^{cd}\right)\eta
\end{aligned}
```

The action of $`\mathcal P`$ on $`\mathsf T\gamma_{[a}\mathsf T\gamma_{b]}`$ vanishes. Hence no separate $`T^2\epsilon`$ block appears in the variation of the curvature $`Q`$.

Expanding the $`Q`$ variation gives the $`C`$, $`U`$, and $`\nabla T`$ coefficients in [covariant-rule equation R05](../../log/action/details/covariant_rules.md). This matching uses the bosonic Weyl decomposition of $`C`$, while leaving the Ricci curvature free.

For the curvature $`S`$ used here,

```math
\begin{aligned}
R_{ab}(S)={}&-i\mathord{\not{\mathcal D}}Q_{ab}
 -i\gamma_{[a}\mathcal D^cQ_{b]c}
 -\frac83\gamma_{ab}T^{cd}Q_{cd}\\
&+12\gamma_dT^{cd}\gamma_{[a}Q_{b]c}
 -3\mathsf TQ_{ab}-8T^c{}_{[a}Q_{b]c}
\end{aligned}
```

the differential identity checked is

```math
\mathcal D_aQ_{bc}+\mathcal D_bQ_{ca}+\mathcal D_cQ_{ab}
=-i\mathsf T(\gamma_aQ_{bc}+\gamma_bQ_{ca}+\gamma_cQ_{ab})
+i(\gamma_aR_{bc}(S)+\gamma_bR_{ca}(S)+\gamma_cR_{ab}(S))
```

Substituting the explicit expression verifies this equality separately for the $`\mathcal DQ`$ and $`TQ`$ coefficients. Writing $`Q=\mathcal PX`$, the check covers every $`\mathcal D_mX_{ab}`$ and $`T_{cd}X_{ab}`$ coefficient.

<a id="2-triplet-variation"></a>

## Triplet variation

The starting equation is

```math
L_{Wij}=\frac i4\bar Q_{ab(i}Q^{ab}{}_{j)}
 +\frac{256i}{3}\bar\chi_{(i}\chi_{j)}
 +\frac{16}{3}U_{abij}T^{ab}
```

so the open-index scalar flip gives

```math
\begin{aligned}
\delta L_{Wij}
={}&\frac i2\overline{\delta Q}_{ab(i}Q^{ab}{}_{j)}
 +\frac{512i}{3}\overline{\delta\chi}_{(i}\chi_{j)}\\
&+\frac{16}{3}\left[(\delta U_{abij})T^{ab}
 +U_{abij}\delta T^{ab}\right].
\end{aligned}
```

Substitute $`\delta Q=\mathcal P\mathcal A\epsilon`$, the $`R(S)`$ from §1, and

```math
\begin{aligned}
\delta_Q\chi^i={}&\left(\frac14D
 +\frac i8\gamma^{ab}\gamma^c\mathcal D_cT_{ab}
 -\frac i8\gamma^a\mathcal D^bT_{ab}
 -\frac14\gamma^{abcd}T_{ab}T_{cd}+\frac16T^2\right)\epsilon^i
 -\frac1{64}\gamma^{ab}U_{ab}^{ij}\epsilon_j,\\
\delta_Q U_{ab}^{ij}={}&-\frac{3i}{2}\bar\epsilon^{(i}R_{ab}^{j)}(S)
 -8\bar\epsilon^{(i}\gamma_{[a}\mathcal D_{b]}\chi^{j)}
 +i\bar\epsilon^{(i}\mathsf TQ_{ab}^{j)}
 +8i\bar\epsilon^{(i}\gamma_{[a}\mathsf T\gamma_{b]}\chi^{j)},\\
\delta_QT_{ab}={}&\frac i2\bar\epsilon\gamma_{ab}\chi
 -\frac{3i}{32}\bar\epsilon Q_{ab}
\end{aligned}
```

The flip reverses gamma-product order. The resulting spinor coefficient is:

```math
\begin{aligned}
\varphi_W^i={}&-\frac18\gamma_{cd}C^{abcd}Q_{ab}^i
 -4i\gamma_c(\mathcal D^aT^{bc})Q_{ab}^i
 +\frac{128}{3}D\chi^i\\
&+8iT^{ab}\gamma_c\mathcal D^cQ_{ab}^i
 +8iT^{ab}\gamma_a\mathcal D^cQ_{bc}^i
 -\frac{64i}{3}\gamma^{ab}\gamma^c(\mathcal D_aT_{bc})\chi^i\\
&+\frac{1024}{9}T^2\chi^i
 +\frac{128i}{3}T^{ab}\gamma_a\mathcal D_b\chi^i
 +\frac83\mathsf T T^{cd}Q_{cd}^i\\
&+\frac12U^{ab\,i}{}_jQ_{ab}^j
 -\frac83U^{ab\,i}{}_j\gamma_{ab}\chi^j.
\end{aligned}
```

Some intermediate reductions fixing the coefficients are:

```math
\begin{aligned}
\frac i2\overline{\left(\frac14 C_{ab cd}\gamma^{cd}\epsilon\right)}Q^{ab}
&=-\frac i8\bar\epsilon\gamma_{cd}C^{abcd}Q_{ab},\\
\frac{512i}{3}\overline{\left(\frac14D\epsilon\right)}\chi
&=i\bar\epsilon\frac{128}{3}D\chi,\\
T^{ab}\gamma_a\mathsf T\gamma_b
&=\gamma^{abcd}T_{ab}T_{cd}+2T^2,\\
\left.\frac1i\delta L_W\right|_{T^2\chi}
&=\bar\epsilon\left[-\frac{128}{3}\gamma^{abcd}T_{ab}T_{cd}
 +\frac{256}{9}T^2
 +\frac{128}{3}\left(\gamma^{abcd}T_{ab}T_{cd}+2T^2\right)\right]\chi\\
&=\frac{1024}{9}T^2\bar\epsilon\chi.
\end{aligned}
```

For gamma-traceless $`Q`$, additional contractions give

```math
\begin{aligned}
\left(\gamma^{abcd}-\gamma^{ab}\gamma^{cd}
 -\frac12\gamma^{cd}\gamma^{ab}\right)Q_{ab}&=6Q^{cd},\\
T^{ab}T^{cd}\gamma_d\gamma_aQ_{bc}&=\frac12\mathsf T T^{ab}Q_{ab},\\
T^{ab}T^c{}_aQ_{bc}&=0,\\
T^{ab}R_{ab}(S)\big|_{TQ}&=\frac13\mathsf T T^{cd}Q_{cd}
\end{aligned}
```

Substituting the preceding two lines into $`R(S)`$ of §1 gives the coefficient $`-8/3+6-3=1/3`$ in the last line. Therefore

```math
\left.\varphi_W\right|_{T^2Q}
=\frac{16}{3}\left[-\frac32\left(\frac13\mathsf T T^{cd}Q_{cd}\right)
 +\mathsf T T^{cd}Q_{cd}\right]
=\frac83\mathsf T T^{cd}Q_{cd}.
```

The alternative $`16/3`$ leaves the residual $`-8i\bar\epsilon_{(i}\mathsf T T^{ab}Q_{abj)}/3`$ in the same transformation.

For the three independent $`SU(2)`$ triplet components, every Clifford coefficient in $`[\delta_Q L_W-i\bar\epsilon\varphi_W]_1`$ and $`[\delta_S L_W]_1`$ vanishes. This check does not set any of the structures $`C,U,D,T,\mathcal DT,Q,\mathcal DQ,\chi,\mathcal D\chi`$ to zero.

<a id="3-expanding-derivatives-in-the-spinor-variation"></a>

## Expanding derivatives in the spinor variation

Let $`M_\chi`$ and $`N_\chi`$ be the coefficients of $`[\delta_Q\chi]_0=M_\chi\epsilon`$ and $`[\delta_S\chi]_0=N_\chi\eta`$, respectively; $`N_\chi=\mathsf T/4`$. Similarly,

```math
M_{Q,bc}:=(\mathcal P\mathcal A)_{bc},\qquad
N_{Q,bc}:=\mathcal P(2\mathsf T\gamma_{bc}),\qquad
\Phi_{Q,a}:=\Phi_a[\mathcal A],\qquad
\Phi_{S,a}:=\Phi_a[2\mathsf T\gamma_{bc}].
```

Since the one-fermion covariant derivative is $`\mathcal D_aX=\nabla_aX-M_X\psi_a-N_X\phi_a`$, variation and the product rule give

```math
\begin{aligned}
[\delta_Q(\mathcal D_aX)]_0
&=\left(\nabla_aM_X-iM_X\mathsf T\gamma_a-N_X\Phi_{Q,a}\right)\epsilon,\\
[\delta_S(\mathcal D_aX)]_0
&=\left(\nabla_aN_X+iM_X\gamma_a-N_X\Phi_{S,a}\right)\eta
\end{aligned}
```

The same formula applies to $`X=\chi,Q_{bc}`$. For example, $`\nabla_a(M_X\epsilon)-M_X\nabla_a\epsilon=(\nabla_aM_X)\epsilon`$, and $`\nabla_a\eta`$ cancels with $`-N_X\delta\phi_a`$. This does not replace the derivative by an ordinary derivative; it explicitly includes variations of the subtracted $`Q`$ and $`S`$ connections.

Make the following substitutions in the eleven terms of the spinor in §2:

```math
\begin{array}{c|c|c}
X & \delta_QX|_0 & \delta_SX|_0\\ \hline
Q_{ab}&M_{Q,ab}\epsilon&N_{Q,ab}\eta\\
\chi&M_\chi\epsilon&(\mathsf T/4)\eta\\
\mathcal D_aQ_{bc}&
(\nabla_aM_{Q,bc}-iM_{Q,bc}\mathsf T\gamma_a-N_{Q,bc}\Phi_{Q,a})\epsilon&
(\nabla_aN_{Q,bc}+iM_{Q,bc}\gamma_a-N_{Q,bc}\Phi_{S,a})\eta\\
\mathcal D_a\chi&
(\nabla_aM_\chi-iM_\chi\mathsf T\gamma_a-\mathsf T\Phi_{Q,a}/4)\epsilon&
(\nabla_a\mathsf T/4+iM_\chi\gamma_a-\mathsf T\Phi_{S,a}/4)\eta
\end{array}
```

Coefficient variations do not contribute at this degree: $`[\delta B]_1[X]_1`$ contains two physical fermions and is not a coefficient of $`[\delta\varphi_W]_0`$.

The differential operations retain second derivatives using these two identities:

```math
\begin{aligned}
\nabla_a\nabla_bT_{cd}
&=\nabla_{(a}\nabla_{b)}T_{cd}
 +\frac12\left(R_{ab c}{}^eT_{ed}+R_{ab d}{}^eT_{ce}\right),\\
[\mathcal D_b\mathcal D_cT_{de}]_0
&=\nabla_b\nabla_cT_{de}-f_b{}^m(K_m\nabla_cT_{de}),\\
K_m\nabla_cT_{de}
&=-2\eta_{mc}T_{de}-2\eta_{cd}T_{em}
 +2\eta_{md}T_{ec}+2\eta_{ce}T_{dm}-2\eta_{me}T_{dc},\\
f_{ab}&=-\frac16R_{ab}+\frac1{48}\eta_{ab}R.
\end{aligned}
```

The $`K_m\nabla T`$ line substitutes $`\delta_Kb_a=2\Lambda_{Ka}`$ and $`\delta_K\omega_a{}^{bc}=-4\Lambda_K^{[b}\delta_a^{c]}`$ into the definition of $`\mathcal D T`$. The $`fT`$ contribution is therefore not lost inside the second derivative.

<a id="4-extracting-the-bosonic-scalar-and-vector"></a>

## Extracting the bosonic scalar and vector

Let $`\mathcal M_W\epsilon:=[\delta_Q\varphi_W]_0`$ be defined by the explicit substitution table above. Denoting the gamma-scalar coefficient by $`\mathop{\mathrm{sc}}\nolimits`$, scalar extraction is

```math
N_W^{(0)}=\sum_{i=1}^2\mathop{\mathrm{sc}}\nolimits(\mathcal M_W{}^i{}_i)
```

The trace $`SU(2)`$ removes the two terms containing $`L_W^{ij}\epsilon_j`$. Rank-five gamma terms are not separated from the scalar: apply $`\gamma^{01234}=i\varepsilon^{01234}\mathbf1`$. The gamma-vector coefficient of the same sum is $`-iE_{Wa}^{(0)}\gamma^a`$. These two projections give:

```math
\begin{aligned}
N_W^{(0)}={}&\frac18C_{abcd}C^{abcd}
 +\frac{64}{3}D^2+\frac{1024}{9}T^2D
 -\frac{16}{3}C_{abcd}T^{ab}T^{cd}
 -\frac13U_{ab}^{ij}U^{ab}_{ij}\\
&-\frac{64}{3}\mathcal D_aT_{bc}\mathcal D^aT^{bc}
 +\frac{64}{3}\mathcal D_bT_{ac}\mathcal D^aT^{bc}
 -\frac{128}{3}T_{ab}\mathcal D^b\mathcal D_cT^{ac}\\
&-\frac{128}{3}\varepsilon_{abcde}T^{ab}T^{cd}\mathcal D_fT^{ef}
 +1024T_{ab}T^{bc}T_{cd}T^{da}
 -\frac{2816}{27}(T^2)^2,
\end{aligned}
```

```math
\begin{aligned}
E_{Wa}^{(0)}={}&\frac1{16}\varepsilon_{abcde}C^{bcfg}C^{de}{}_{fg}
 -\frac1{12}\varepsilon_{abcde}U^{bcij}U^{de}{}_{ij}\\
&+\mathcal D^b\left(4C_{abcd}T^{cd}-\frac{64}{3}DT_{ab}
 -\frac{128}{9}T_{ab}T^2-\frac{512}{3}T_{ac}T^{cd}T_{bd}\right)\\
&-32\varepsilon_{abcde}\mathcal D^b\left(
 \frac23T^{cf}\mathcal D_fT^{de}+T^c{}_f\mathcal D^dT^{ef}\right).
\end{aligned}
```

In both identities, take the zero-fermion coefficient of the right-hand side; $`\mathcal D\mathcal DT`$ is the conformal second derivative expanded above. Examples of scalar contractions directly fixing the normalizations are

```math
\begin{aligned}
\left.\mathcal M_W\right|_{D^2}
&=\frac{128}{3}D\left(\frac14D\right)\mathbf1
=\frac{32}{3}D^2\mathbf1=\frac12\left(\frac{64}{3}D^2\right)\mathbf1,\\
\left.\mathcal M_W\right|_{C^2}
&=-\frac1{32}C^{ab cd}C_{ab ef}\gamma_{cd}\gamma^{ef},\\
\mathop{\mathrm{sc}}\nolimits(\gamma_{cd}\gamma^{ef})
&=-\delta_c{}^e\delta_d{}^f+\delta_c{}^f\delta_d{}^e,\\
\left.\mathop{\mathrm{sc}}\nolimits(\mathcal M_W)\right|_{C^2}
&=\frac1{16}C_{abcd}C^{abcd}
=\frac12\left(\frac18C_{abcd}C^{abcd}\right)
\end{aligned}
```

The quantities $`T^4`$ and $`(T^2)^2`$ remain independent.

Back-substitution is not restricted to comparing these two traces:

```math
\mathcal R_Q{}^i{}_j\epsilon^j:=[\delta_Q\varphi_W^i]_0
 +\frac i2\gamma^a\mathcal D_aL_W^{ij(0)}\epsilon_j
 +\frac i2\gamma^aE_{Wa}^{(0)}\epsilon^i
 -\frac12N_W^{(0)}\epsilon^i
 +\mathsf T L_W^{ij(0)}\epsilon_j
```

**All** scalar, vector, and rank-two gamma coefficients of the residual are tested. Rank-three, four, and five gamma terms are converted to this basis using the root duality convention; $`\varepsilon^{01234}`$ remains symbolic, and $`(\varepsilon^{01234})^2=1`$ follows from epsilon contraction. No orientation branch is chosen.

Under the algebraic Weyl symmetries, $`\nabla_{[a}U_{bc]}=0`$, the $`[\nabla_a,\nabla_b]T`$ above, and the differential Riemann Bianchi identity $`\nabla_{[a}R_{bc]de}=0`$,

```math
\boxed{\mathcal R_Q{}^i{}_j=0.}
```

An independent $`S`$ check using the last column of the same substitution table gives

```math
\boxed{[\delta_S\varphi_W^i]_0-3L_W^{ij(0)}\eta_j=0}
```

Only algebraic Weyl symmetries are needed in this check.

<a id="5-tensor-space-covered-by-the-symbolic-coefficient-check"></a>

## Tensor space covered by the symbolic coefficient check

The ten components of the free $`T_{ab}`$, general triplets $`SU(2)`$, $`D`$, first derivatives, and symmetric second derivatives remain symbolic. The Riemann tensor is constructed by projecting the 55 symbolic entries of a symmetric two-form-pair matrix onto the algebraic Bianchi identity. Subtracting Ricci traces gives the Weyl tensor; no curvature value is assigned.

For the differential Bianchi identity, introduce an auxiliary fully symbolic tensor $`H_{ab,cde}=H_{(ab),(cde)}`$ and write

```math
\nabla_mR_{abcd}
=\frac12\left(H_{cb,adm}+H_{ad,bcm}-H_{bd,acm}-H_{ac,bdm}\right)
```

This is a linear parametrization of the specified index symmetries, not a field or coordinate choice. Exact rational elimination of the fixed index-coefficient matrices in five dimensions gives

```math
\dim(\text{pair-symmetric }\nabla R)=275,qquad
\mathop{\mathrm{rank}}\nolimits(\text{Bianchi conditions})=100,qquad
\mathop{\mathrm{rank}}\nolimits(H\mapsto\nabla R)=175
```

The product of the constraint and parametrization matrices also vanishes. Since $`175+100=275`$, the parametrization spans the entire Bianchi kernel. These ranks are exact rational ranks of fixed index projectors, not sampled ranks of a matrix depending on free physical parameters. With this parametrization, every coefficient of $`\mathcal R_Q`$ vanishes.

Result: the recorded $`L_W`$, $`\varphi_W`$, $`N_W^{(0)}`$, and $`E_W^{(0)}`$ obey the four transformation identities stated at the beginning of this appendix at the specified fermion degrees.
