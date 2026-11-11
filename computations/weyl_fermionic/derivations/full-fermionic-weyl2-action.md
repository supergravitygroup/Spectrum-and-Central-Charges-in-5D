# Full fermionic Weyl-squared density from the derived map

## 1. Problem and Target

Construct the full fermionic density associated with Özkan–Pang
Eq. (5.18), using the four-component map derived in this project.
The paper prints “$`+\text{fermions}`$” in that equation. The result below
is our explicit insertion of the calculated fermionic map, rather than
a claim that the paper prints these additional terms.

The construction follows the paper's sequence: vector–linear density
(3.1), Weyl composite linear multiplet (5.8), and defining-vector map
(5.16). The full $`E^a`$ to three-form bridge, already extracted as A02,
is from the companion local Özkan–Pang paper (3.1)–(3.2). It supplies
the explicit gravitino terms required to use our calculated $`E_W^a`$.

**A1.** Use the operational v5 conventions and the anchored working map
[FM01–FM04](../inputs/reference/notes/04_full_fermionic_weyl_linear_map.md), including
its adopted $`8/3`$ spinor coefficient. No source coefficient is adjusted
while constructing the density.

**A2.** Work off shell, with physical $`g=0`$, and on a patch $`\sigma\ne0`$.
There is no gauge fixing, equation of motion, background restriction,
auxiliary elimination or truncation of physical fermions.

**A3.** Retain the paper's supercovariant composite notation
$`T_{ab},\chi^i,D`$, whose complete definitions appear below. All four
linear-multiplet components are eliminated explicitly from the final
formula. This is a complete density in that notation, not a claim to
have expanded every hatted curvature into ordinary partial derivatives.

**A4.** Preserve the local representative of density (3.1)/A02.
No integration by parts is performed in the full fermionic result.
The bosonic coefficient comparison with (5.18) is separately identified
as a comparison with the paper's boundary-equivalent representative.

**A5.** This calculation inserts the anchored map algebraically. Independent
descendant laws, triplet matching and the S-law are outside this insertion's
scope. The superscript “map” on the final density records that scope;
this computation is not an independent proof of nonlinear invariance.

The final expression is one collected equation with related terms
sharing each line. No synthetic response fields or unnamed fermionic
remainders are introduced.

## 2. Convention Ledger

<!-- ASSERT_CONVENTION: natural_units=hbar=c=1, metric_signature=(-,+,+,+,+), source_lock=UNG-WEYL2-OP58-CONVENTIONS-v5 -->

Tangent indices $`a,b,c,\ldots`$ and $`m,n,p`$ run from $`0`$ to $`4`$;
$`i,j=1,2`$. The additional letters $`m,n,p`$ only keep the gravitino's
Lorentz indices distinct from dummy indices already inside the map.
$`\eta_{ab}=\mathop{\mathrm{diag}}\nolimits(-,+,+,+,+)`$,
$`\varepsilon^{01234}=+1`$, $`\varepsilon_{01234}=-1`$ and
$`\gamma^{01234}=i\mathbf1`$.

$`\gamma^{a_1\ldots a_n}=\gamma^{[a_1}\cdots\gamma^{a_n]}`$,
$`\{\gamma^a,\gamma^b\}=2\eta^{ab}`$, and antisymmetrization and
symmetrization have unit weight. Repeated antisymmetric pairs are full
ordered-index sums; there is no implicit $`1/2`$.

**$`\psi^i`$ is the dilatino; $`\psi_a^i=e_a{}^\mu\psi_\mu^i`$ is the
gravitino.** The dependent S connection is $`\phi_\mu^i`$, while
$`\varphi_W^i`$ denotes the composite linear-multiplet spinor only during
intermediate steps. They are distinct objects.

The Majorana bar is $`\bar\zeta^i=(\zeta^i)^T\mathsf C`$, linear in $`i`$.
All spinors are odd. Contracted bilinears obey
$`\bar u v=-\bar v u`$, $`\bar u\gamma_a v=-\bar v\gamma_a u`$ and
$`\bar u\gamma_{ab}v=+\bar v\gamma_{ab}u`$.
Products of two bilinears are even and commute. The calculation below
keeps the spinor order fixed and requires no Fierz re-pairing.

SU(2) lowering is $`X_i=X^j\varepsilon_{ji}`$ with
$`\varepsilon_{12}=\varepsilon^{12}=1`$; a suppressed contraction means
$`\bar u\Gamma v=\bar u^i\Gamma v_i`$.
$`T^2=T_{ab}T^{ab}`$ is the source's only scalar shorthand used below.
The curvatures, derivatives and Riemann sign are exactly G01–G03/R01–R03.
In particular $`[\nabla_\mu,\nabla_\nu]X^\rho =R^\rho{}_{\sigma\mu\nu}X^\sigma`$ and $`e=\det e_\mu{}^a>0`$.

This density has the native paper normalization
$`e^{-1}\mathcal L\supset\sigma\widehat C^2/8`$.
It introduces no new normalization of the later $`\lambda_{\rm Weyl}`$
and does not add the two-derivative action. Fourier, state normalization
and renormalization conventions are not used in this local construction.

## 3. Definitions and Required Identities

### 3.1. The full density and the three-form bridge

From OP (3.1), master A01, the complete vector–linear density is

```math
\begin{aligned}
e^{-1}\mathcal L_{VL}={}&Y^{ij}L_{ij}+i\bar\lambda\varphi-\frac12\bar\psi_m^i\gamma^m\lambda^jL_{ij}
-\frac1{12}\varepsilon^{\mu\nu\rho\sigma\lambda}A_\mu\partial_\nu E_{\rho\sigma\lambda}\\
&+\rho N+\frac\rho2\bar\psi_m\gamma^m\varphi+\frac{i\rho}{4}\bar\psi_m^i\gamma^{mn}\psi_n^jL_{ij}.
\end{aligned}\tag{WA01}
```

The ordinary three-form term is $`A_aP^a`$, where the existing source
quantity $`P^a`$ is given completely by A02:

```math
P^a=-\frac1{12}e_\mu{}^a\varepsilon^{\mu\nu\rho\sigma\lambda}\partial_\nu E_{\rho\sigma\lambda}
=E^a+\frac i2\bar\psi_b\gamma^{ba}\varphi+\frac14\bar\psi_b^i\gamma^{abc}\psi_c^jL_{ij}.
\tag{WA02}
```

Consequently replacing the three-form coupling by $`A_aE^a`$ alone would
omit two entire fermionic contributions. We insert the full right-hand
side of WA02 and do not introduce a potential for our computed $`E_W^a`$.
The source-literal potential-law conflict X10 is therefore not used.

The defining vector, OP (5.16)/V03, is

```math
\rho=\sigma,\qquad A_\mu=C_\mu,\qquad\lambda^i=\psi^i,
\qquad Y^{ij}=\frac{i}{4\sigma}\bar\psi^{(i}\psi^{j)}.
\tag{WA03}
```

No independent $`Y^{ij}`$ survives this identification.

### 3.2. Full Dilaton-Weyl composites and hatted curvatures

The following are definitions of the existing source fields in the final
action. They retain all fermions and make the dependence on the DW
fields explicit. They are not extra independent fields or auxiliary
field equations. Their source anchors are master H01, D01–D02, W04 and
R01–R03; those definitions are copied below without changing the lock.

**H01 (full definitions):**

```math
\begin{aligned}
G_{\mu\nu}&=2\partial_{[\mu}C_{\nu]},\qquad
H_{\mu\nu\rho}=3\partial_{[\mu}B_{\nu\rho]}+\tfrac32 C_{[\mu}G_{\nu\rho]},\\
\widehat G_{\mu\nu}&=G_{\mu\nu}-\bar\psi_{[\mu}\gamma_{\nu]}\psi
+\tfrac i2\sigma\bar\psi_{[\mu}\psi_{\nu]},\\
\widehat H_{\mu\nu\rho}&=H_{\mu\nu\rho}
-\tfrac34\sigma^2\bar\psi_{[\mu}\gamma_\nu\psi_{\rho]}
-\tfrac{3i}{2}\sigma\bar\psi_{[\mu}\gamma_{\nu\rho]}\psi,\\
\delta_\Lambda C_\mu&=\partial_\mu\Lambda,\qquad
\delta_\Lambda B_{\mu\nu}=2\partial_{[\mu}\Lambda_{\nu]}-\tfrac12\Lambda G_{\mu\nu}.
\end{aligned}\tag{AD01}
```

**D01 (full definitions):**

```math
\begin{aligned}
T_{ab}={}&\tfrac18\sigma^{-2}
\left(\sigma\widehat G_{ab}+\tfrac16\epsilon_{abcde}\widehat H^{cde}
+\tfrac i4\bar\psi\gamma_{ab}\psi\right),\\
\chi^i={}&\tfrac i8\sigma^{-1}\mathord{\not{\mathcal D}}\psi^i
+\tfrac i{16}\sigma^{-2}\mathord{\not{\mathcal D}}\sigma\psi^i
-\tfrac1{32}\sigma^{-2}\gamma\!\cdot\!\widehat G\psi^i
+\tfrac14\sigma^{-1}\gamma\!\cdot\!T\psi^i
+\tfrac i{32}\sigma^{-3}\psi_j\bar\psi^i\psi^j,\\
D={}&\tfrac14\sigma^{-1}\Box^c\sigma
+\tfrac18\sigma^{-2}(\mathcal D_a\sigma)(\mathcal D^a\sigma)
-\tfrac1{16}\sigma^{-2}\widehat G_{ab}\widehat G^{ab}
-\tfrac18\sigma^{-2}\bar\psi\mathord{\not{\mathcal D}}\psi\\
&-\tfrac1{64}\sigma^{-4}\bar\psi^i\psi^j\bar\psi_i\psi_j
-4i\sigma^{-1}\bar\psi\chi
+\left(-\tfrac{26}{3}T_{ab}+2\sigma^{-1}\widehat G_{ab}
+\tfrac i4\sigma^{-2}\bar\psi\gamma_{ab}\psi\right)T^{ab}.
\end{aligned}\tag{AD02}
```

**D02 (full definitions):**

```math
\Box^c\sigma=(\partial^a-2b^a+\omega_b{}^{ba})\mathcal D_a\sigma
-\tfrac i2\bar\psi_a\mathcal D^a\psi
-2\sigma\bar\psi_a\gamma^a\chi
+\tfrac12\bar\psi_a\gamma^a\gamma\!\cdot\!T\psi
+\tfrac12\bar\phi_a\gamma^a\psi+2f_a{}^a\sigma.
\tag{AD03}
```

**W04 (full definitions):**

```math
\begin{aligned}
\mathcal D_\mu\sigma&=(\partial_\mu-b_\mu)\sigma-\tfrac i2\bar\psi_\mu\psi,\\
\mathcal D_\mu\psi^i&=D_\mu^{(0)}\psi^i
+\tfrac14\gamma\!\cdot\!\widehat G\psi_\mu^i
+\tfrac i2\mathord{\not{\mathcal D}}\sigma\psi_\mu^i
+\tfrac i4\sigma^{-1}\psi_{\mu j}\bar\psi^i\psi^j
-\sigma\gamma\!\cdot\!T\psi_\mu^i-\sigma\phi_\mu^i,\\
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
\end{aligned}\tag{AD04}
```

**R01 (full definitions):**

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
\end{aligned}\tag{AD05}
```

**R02 (full definitions):**

```math
\begin{aligned}
V_{\mu\nu}{}^{ij}&=2\partial_{[\mu}V_{\nu]}{}^{ij}
-2V_{[\mu}{}^{k(i}V_{\nu]k}{}^{j)},\\
\widehat R_{\mu\nu}{}^{ij}(V)&=V_{\mu\nu}{}^{ij}
-3i\bar\phi_{[\mu}^{(i}\psi_{\nu]}^{j)}
-8\bar\psi_{[\mu}^{(i}\gamma_{\nu]}\chi^{j)}
-i\bar\psi_{[\mu}^{(i}\gamma\!\cdot\!T\psi_{\nu]}^{j)}.
\end{aligned}\tag{AD06}
```

**R03 (full definitions):**

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
\end{aligned}\tag{AD07}
```

Here $`\gamma\!\cdot\!T=\gamma^{ab}T_{ab}`$ and
$`\mathord{\not{\mathcal D}}=\gamma^a\mathcal D_a`$. In AD04,
$`D_\mu^{(0)}\zeta^i=(\partial_\mu-wb_\mu+\omega_\mu{}^{ab}\gamma_{ab}/4) \zeta^i-V_\mu{}^{ij}\zeta_j`$ with the field's actual weight.
$`R_{\mu\nu}{}^{ab}(\omega)=2\partial_{[\mu}\omega_{\nu]}{}^{ab} +2\omega_{[\mu}{}^{ac}\omega_{\nu]c}{}^b`$.
All remaining derivatives, including derivatives of products and
curvatures, are G01's full connection derivative, not a bosonic derivative.
The full derivative used here is explicitly

```math
\mathcal D_\mu\Phi=\partial_\mu\Phi-\delta_D(b_\mu)\Phi-\delta_M(\omega_\mu)\Phi-\delta_U(V_\mu)\Phi
-\delta_Q(\psi_\mu)\Phi-\delta_S(\phi_\mu)\Phi-\delta_K(f_\mu)\Phi,
\qquad\mathcal D_a=e_a{}^\mu\mathcal D_\mu.
\tag{AD08}
```

Here $`\Phi`$ means the field or tensor product being differentiated, not a
new field. The transformations in master W/R determine the connection
actions. In particular, a second derivative acts on the first derivative's
Lorentz index and its S/K transformation as well as on its field indices.

The use of AD02 is triangular: T is fixed first, then chi, then D;
AD03 and AD05–AD07 supply all dependent-connection terms.

For example, the terms $`-2\sigma\bar\psi_a\gamma^a\chi`$ and
$`2f_a{}^a\sigma`$ in $`\Box^c\sigma`$ are retained. Even on a later
$`\sigma=1`$, $`\psi^i=0`$ gauge slice, the full $`\mathcal D_a\psi^i`$ need
not vanish. We do not make that gauge restriction in this document.

### 3.3. Ordered gamma matrices and source fields

Products such as $`\gamma^m\gamma_{cd}`$,
$`\gamma^{nm}\gamma^{ab}\gamma^c`$ and $`\gamma^{mn}`$ have different
meanings. They are written explicitly in the result in their inherited
order. For reference, the identities that distinguish them are

```math
\gamma^a\gamma^{bc}=\gamma^{abc}+\eta^{ab}\gamma^c-\eta^{ac}\gamma^b,
\qquad \gamma_{abc}=-\frac i2\varepsilon_{abcde}\gamma^{de},
\qquad \gamma_{abcd}=i\varepsilon_{abcde}\gamma^e.
```

No Clifford rank is deleted in the present substitution. Keeping an
ordered matrix word is an exact representation of its full product,
including its scalar and lower-rank contractions. We do not assert a
new minimal gamma basis or interchange odd spinors to shorten the action.

## 4. Detailed Derivation

### 4.1. Insert the defining vector into every density term

<!-- ASSERT_CONVENTION: metric_signature=(-,+,+,+,+), source_lock=UNG-WEYL2-OP58-CONVENTIONS-v5 -->

Substitute WA02 and WA03 in WA01, and put the Weyl composite linear
multiplet in its four slots. The result before expanding the map is

```math
\begin{aligned}
e^{-1}\mathcal L_{\sigma C^2}^{\rm map}={}&\sigma N_W+C_aE_W^a+i\bar\psi\varphi_W
+\frac\sigma2\bar\psi_m\gamma^m\varphi_W
+\frac i2C_m\bar\psi_n\gamma^{nm}\varphi_W\\
&+\frac{i}{4\sigma}\bar\psi^{(i}\psi^{j)}L_{W\,ij}
-\frac12\bar\psi_m^i\gamma^m\psi^jL_{W\,ij}
+\frac{i\sigma}{4}\bar\psi_m^i\gamma^{mn}\psi_n^jL_{W\,ij}
+\frac14C_m\bar\psi_n^i\gamma^{mnp}\psi_p^jL_{W\,ij}.
\end{aligned}\tag{WA04}
```

This accounts for all terms of the density: two descendant couplings,
three spinor couplings, and four triplet couplings. In particular the
fifth and ninth terms arise from WA02, and the sixth uses the composite
Y of WA03. No term has been inferred from the bosonic action.

### 4.2. Lower the SU(2) indices before multiplying the map

FM01 gives

```math
L_{W\,ij}=\frac i4\overline{\widehat R}_{ab(i}(Q)\widehat R_{j)}{}^{ab}(Q)
+\frac{256i}{3}\bar\chi_{(i}\chi_{j)}
+\frac{16}{3}\widehat R_{ab\,ij}(V)T^{ab}.
\tag{WA05}
```

Both indices have been lowered with $`\varepsilon_{ki}\varepsilon_{lj}`$;
there is no extra sign or factor two. Since $`L_{W\,ij}=L_{W\,ji}`$,
$`\bar\psi^{(i}\psi^{j)}L_{W\,ij}=\bar\psi^i\psi^jL_{W\,ij}`$:
the two terms in the symmetrization agree after relabeling $`i,j`$.
The symmetrizations on the curvature and chi bilinears in WA05 are
retained throughout the multiplication.

The two SU(2)-curvature terms in the lowered spinor obey

```math
\begin{aligned}
(\varphi_W)_i\big|_{\widehat R(V)}
&=\varepsilon_{ki}\left[\frac12\widehat R^{ab\,k}{}_{\ell}(V)
 \widehat R_{ab}{}^\ell(Q)-\frac83\widehat R^{ab\,k}{}_{\ell}(V)\gamma_{ab}\chi^\ell\right]\\
&=\frac12\widehat R^{ab}{}_{ij}(V)\widehat R_{ab}{}^j(Q)
-\frac83\widehat R^{ab}{}_{ij}(V)\gamma_{ab}\chi^j.
\end{aligned}\tag{WA06}
```

Indeed $`\widehat R^{ab\,k}{}_{\ell}(V)=\widehat R^{ab\,kr}(V)\varepsilon_{r\ell}`$,
so $`\varepsilon_{ki}\widehat R^{ab\,kr}(V)\varepsilon_{rj} =\widehat R^{ab}{}_{ij}(V)`$. This fixes the actual SU(2) contractions
in all six curvature terms obtained from the three spinor couplings.

### 4.3. Multiply the scalar component by $`\sigma`$

<!-- ASSERT_CONVENTION: source_lock=UNG-WEYL2-OP58-CONVENTIONS-v5 -->

Insert all fifteen terms of FM04 in the first term of WA04. Since
$`\sigma`$ is even, it stays at the left of each product with no sign
change. In particular the four explicit fermionic coefficients become
$`3\sigma/4`$, $`-2i\sigma`$, $`-160i\sigma/3`$, and $`-256\sigma/3`$:

```math
\begin{aligned}
\sigma N_W={}&\frac{1}{8}\sigma \widehat C_{abcd}\widehat C^{abcd}+\frac{64}{3}\sigma D^2\\
 &+\frac{1024}{9}\sigma DT_{ab}T^{ab}-\frac{16}{3}\sigma \widehat C_{abcd}T^{ab}T^{cd}\\
 &-\frac{1}{3}\sigma \widehat R_{ab}{}^{ij}(V)\widehat R^{ab}{}_{ij}(V)-\frac{64}{3}\sigma (\mathcal D_aT_{bc})(\mathcal D^aT^{bc})\\
 &+\frac{64}{3}\sigma (\mathcal D_bT_{ac})(\mathcal D^aT^{bc})-\frac{128}{3}\sigma T_{ab}\mathcal D^b\mathcal D_cT^{ac}\\
 &-\frac{128}{3}\sigma \varepsilon_{abcde}T^{ab}T^{cd}\mathcal D_fT^{ef}+1024\sigma T_{ab}T^{bc}T_{cd}T^{da}\\
 &-\frac{2816}{27}\sigma (T_{ab}T^{ab})^2+\frac{3}{4}\sigma \overline{\widehat R_{ab}(Q)}\gamma^c\mathcal D_c\widehat R^{ab}(Q)\\
 &-2i\sigma T^{ab}\overline{\widehat R_{ca}(Q)}\widehat R^c{}_{b}(Q)-\frac{160i}{3}\sigma T^{ab}\overline{\widehat R_{ab}(Q)}\chi\\
 &-\frac{256}{3}\sigma \bar\chi\gamma^a\mathcal D_a\chi
\end{aligned}
\tag{WA07}
```

The ordered derivative in the eighth term remains
$`\mathcal D^b\mathcal D_cT^{ac}`$. No commutator or field equation has
been applied to it.

### 4.4. Multiply the vector component by $`C_a`$

In the second term of WA04 insert FM03. Contract its free index with
$`C_a`$. The factor $`C_a`$ stays outside every derivative, because this
operation is multiplication of the density, not integration by parts:

```math
\begin{aligned}
C_aE_W^a={}&\frac{1}{16}C_a\varepsilon^{abcde}\widehat C_{bcfg}\widehat C_{de}{}^{fg}-\frac{1}{12}C_a\varepsilon^{abcde}\widehat R(V)_{bc}{}^{ij}\widehat R(V)_{de\,ij}\\
 &+C_a\mathcal D_b\Big[4\widehat C^{ab}{}_{cd}T^{cd}-\frac{64}{3}DT^{ab}-\frac{128}{9}T^{ab}T_{cd}T^{cd}\\
 &\hspace{20mm}-\frac{512}{3}T^a{}_cT^{cd}T^b{}_d+8i\overline{\widehat R(Q)^{ab}}\chi-\frac{64i}{3}\bar\chi\gamma^{ab}\chi\Big]-32C_a\varepsilon^a{}_{bcde}\mathcal D^b\Big[\frac23T^{cf}\mathcal D_fT^{de}+T^c{}_f\mathcal D^dT^{ef}\Big]\\
 &-C_aT^{cd}\overline{\widehat R(Q)_{ec}}\gamma^a\widehat R(Q)^e{}_d+3C_aT_c{}^d\overline{\widehat R(Q)_e{}^a}\gamma^c\widehat R(Q)^e{}_d\\
 &+16C_aT^c{}_d\overline{\widehat R(Q)^a{}_c}\gamma^d\chi+\frac{16}{3}C_aT^{cd}\overline{\widehat R(Q)_{cd}}\gamma^a\chi\\
 &+\frac{i}{2}C_a\overline{\widehat R(Q)_{cd}}\mathcal D^a\widehat R(Q)^{cd}+\frac{3i}{2}C_a\overline{\widehat R(Q)_{cd}}\mathcal D^c\widehat R(Q)^{da}
\end{aligned}
\tag{WA08}
```

The differentiated fermion bilinears inside the bracket are included.
Their product rules, and those of every other product in this current,
are displayed in Section 4.7 below.

### 4.5. Calculate the three spinor couplings term by term

<!-- ASSERT_CONVENTION: source_lock=UNG-WEYL2-OP58-CONVENTIONS-v5 -->

The eleven FM02 terms occur in their original order. The following table
shows each numerical multiplication. In the middle column $`\sigma`$ is
written with the fields in WA10; in the last column $`C_m`$ is written with
the fields in WA11. Thus the numerical factors to multiply are
$`i`$, $`1/2`$, and $`i/2`$, respectively.

| FM02 term and coefficient | $`i`$ times the coefficient | $`1/2`$ times the coefficient | $`i/2`$ times the coefficient |
|---|---|---|---|
| 1: $`-1/8`$ | $`-i/8`$ | $`-1/16`$ | $`-i/16`$ |
| 2: $`-4i`$ | $`-4i^2=4`$ | $`-2i`$ | $`-2i^2=2`$ |
| 3: $`128/3`$ | $`128i/3`$ | $`64/3`$ | $`64i/3`$ |
| 4: $`8i`$ | $`8i^2=-8`$ | $`4i`$ | $`4i^2=-4`$ |
| 5: $`8i`$ | $`8i^2=-8`$ | $`4i`$ | $`4i^2=-4`$ |
| 6: $`-64i/3`$ | $`-64i^2/3=64/3`$ | $`-32i/3`$ | $`-32i^2/3=32/3`$ |
| 7: $`1024/9`$ | $`1024i/9`$ | $`512/9`$ | $`512i/9`$ |
| 8: $`128i/3`$ | $`128i^2/3=-128/3`$ | $`64i/3`$ | $`64i^2/3=-64/3`$ |
| 9: $`8/3`$ | $`8i/3`$ | $`4/3`$ | $`4i/3`$ |
| 10: $`1/2`$ | $`i/2`$ | $`1/4`$ | $`i/4`$ |
| 11: $`-8/3`$ | $`-8i/3`$ | $`-4/3`$ | $`-4i/3`$ |

In FM02 terms6 and7 the coefficients $`\mathcal D_aT_{bc}`$ and $`T^2`$
are Grassmann even. Moving them to the right of $`\chi`$ therefore gives
$`\gamma^{ab}\gamma^c(\mathcal D_aT_{bc})\chi =\gamma^{ab}\gamma^c\chi\mathcal D_aT_{bc}`$ and
$`T^2\chi=\chi T^2`$, with no sign change.

For the dilatino coupling, place $`\bar\psi`$ before each singlet spinor
term and use the lowered contractions WA06 for the last two terms:

```math
\begin{aligned}
i\bar\psi\varphi_W={}&-\frac{i}{8}\bar\psi\gamma_{cd}\widehat R_{ab}(Q)\widehat C^{abcd}+4\bar\psi\gamma_c\widehat R_{ab}(Q)\mathcal D^aT^{bc}\\
 &+\frac{128i}{3}\bar\psi\chi D-8\bar\psi\gamma_c\mathcal D^c\widehat R_{ab}(Q)T^{ab}\\
 &-8\bar\psi\gamma_a\mathcal D^c\widehat R_{bc}(Q)T^{ab}+\frac{64}{3}\bar\psi\gamma^{ab}\gamma^c\chi\mathcal D_aT_{bc}\\
 &+\frac{1024i}{9}\bar\psi\chi T^2-\frac{128}{3}\bar\psi\gamma_a\mathcal D_b\chi T^{ab}\\
 &+\frac{8i}{3}\bar\psi\gamma_{ab}\widehat R_{cd}(Q)T^{ab}T^{cd}+\frac{i}{2}\bar\psi^i\widehat R^{ab}{}_{ij}(V)\widehat R_{ab}{}^j(Q)\\
 &-\frac{8i}{3}\bar\psi^i\widehat R^{ab}{}_{ij}(V)\gamma_{ab}\chi^j
\end{aligned}
\tag{WA09}
```

For the fourth term of WA04, multiply each FM02 spinor from the left
by $`\bar\psi_m\gamma^m`$, using the middle coefficient column:

```math
\begin{aligned}
\frac\sigma2\bar\psi_m\gamma^m\varphi_W={}&-\frac{1}{16}\sigma\bar\psi_m\gamma^m\gamma_{cd}\widehat R_{ab}(Q)\widehat C^{abcd}-2i\sigma\bar\psi_m\gamma^m\gamma_c\widehat R_{ab}(Q)\mathcal D^aT^{bc}\\
 &+\frac{64}{3}\sigma\bar\psi_m\gamma^m\chi D+4i\sigma\bar\psi_m\gamma^m\gamma_c\mathcal D^c\widehat R_{ab}(Q)T^{ab}\\
 &+4i\sigma\bar\psi_m\gamma^m\gamma_a\mathcal D^c\widehat R_{bc}(Q)T^{ab}-\frac{32i}{3}\sigma\bar\psi_m\gamma^m\gamma^{ab}\gamma^c\chi\mathcal D_aT_{bc}\\
 &+\frac{512}{9}\sigma\bar\psi_m\gamma^m\chi T^2+\frac{64i}{3}\sigma\bar\psi_m\gamma^m\gamma_a\mathcal D_b\chi T^{ab}\\
 &+\frac{4}{3}\sigma\bar\psi_m\gamma^m\gamma_{ab}\widehat R_{cd}(Q)T^{ab}T^{cd}+\frac{1}{4}\sigma\bar\psi_m^i\gamma^m\widehat R^{ab}{}_{ij}(V)\widehat R_{ab}{}^j(Q)\\
 &-\frac{4}{3}\sigma\bar\psi_m^i\gamma^m\widehat R^{ab}{}_{ij}(V)\gamma_{ab}\chi^j
\end{aligned}
\tag{WA10}
```

For the fifth term of WA04, the bridge fixes the order $`\gamma^{nm}`$.
Multiply each FM02 term from the left by $`C_m\bar\psi_n\gamma^{nm}`$,
using the last coefficient column:

```math
\begin{aligned}
\frac i2C_m\bar\psi_n\gamma^{nm}\varphi_W={}&-\frac{i}{16}C_m\bar\psi_n\gamma^{nm}\gamma_{cd}\widehat R_{ab}(Q)\widehat C^{abcd}+2C_m\bar\psi_n\gamma^{nm}\gamma_c\widehat R_{ab}(Q)\mathcal D^aT^{bc}\\
 &+\frac{64i}{3}C_m\bar\psi_n\gamma^{nm}\chi D-4C_m\bar\psi_n\gamma^{nm}\gamma_c\mathcal D^c\widehat R_{ab}(Q)T^{ab}\\
 &-4C_m\bar\psi_n\gamma^{nm}\gamma_a\mathcal D^c\widehat R_{bc}(Q)T^{ab}+\frac{32}{3}C_m\bar\psi_n\gamma^{nm}\gamma^{ab}\gamma^c\chi\mathcal D_aT_{bc}\\
 &+\frac{512i}{9}C_m\bar\psi_n\gamma^{nm}\chi T^2-\frac{64}{3}C_m\bar\psi_n\gamma^{nm}\gamma_a\mathcal D_b\chi T^{ab}\\
 &+\frac{4i}{3}C_m\bar\psi_n\gamma^{nm}\gamma_{ab}\widehat R_{cd}(Q)T^{ab}T^{cd}+\frac{i}{4}C_m\bar\psi_n^i\gamma^{nm}\widehat R^{ab}{}_{ij}(V)\widehat R_{ab}{}^j(Q)\\
 &-\frac{4i}{3}C_m\bar\psi_n^i\gamma^{nm}\widehat R^{ab}{}_{ij}(V)\gamma_{ab}\chi^j
\end{aligned}
\tag{WA11}
```

This accounts for all thirty-three spinor products. No gamma matrix has
been moved past another matrix, and no odd spinor has been interchanged
with another odd spinor. Consequently the only new minus signs in these
three steps are the displayed $`i^2=-1`$ signs. Terms containing $`\chi`$
or $`\widehat R(Q)`$ keep their full definitions AD02 and AD05.

### 4.6. Calculate the four triplet couplings

The three coefficients in WA05 are $`i/4`$, $`256i/3`$, and $`16/3`$.
For the composite Y term the numerical products are

```math
\frac i4\frac i4=-\frac1{16},\qquad
\frac i4\frac{256i}{3}=-\frac{64}{3},\qquad
\frac i4\frac{16}{3}=\frac{4i}{3}.
```

Multiplying the three physical bilinears of WA05 by
$`\sigma^{-1}\bar\psi^i\psi^j`$ gives

```math
\begin{aligned}
\frac i{4\sigma}\bar\psi^{(i}\psi^{j)}L_{W\,ij}={}&-\frac{1}{16}\sigma^{-1}(\bar\psi^i\psi^j)\big(\overline{\widehat R}_{ab(i}(Q)\widehat R_{j)}{}^{ab}(Q)\big)-\frac{64}{3}\sigma^{-1}(\bar\psi^i\psi^j)\big(\bar\chi_{(i}\chi_{j)}\big)\\
 &+\frac{4i}{3}\sigma^{-1}(\bar\psi^i\psi^j)\big(\widehat R_{ab\,ij}(V)T^{ab}\big)
\end{aligned}
\tag{WA12}
```

For the gravitino–dilatino term, the products are
$`(-1/2)(i/4)=-i/8`$, $`(-1/2)(256i/3)=-128i/3`$, and
$`(-1/2)(16/3)=-8/3`$. Keeping the external spinors in density order gives

```math
\begin{aligned}
-\frac12\bar\psi_m^i\gamma^m\psi^jL_{W\,ij}={}&-\frac{i}{8}(\bar\psi_m^i\gamma^m\psi^j)\big(\overline{\widehat R}_{ab(i}(Q)\widehat R_{j)}{}^{ab}(Q)\big)-\frac{128i}{3}(\bar\psi_m^i\gamma^m\psi^j)\big(\bar\chi_{(i}\chi_{j)}\big)\\
 &-\frac{8}{3}(\bar\psi_m^i\gamma^m\psi^j)\big(\widehat R_{ab\,ij}(V)T^{ab}\big)
\end{aligned}
\tag{WA13}
```

For the two-gravitino term, multiply by $`i\sigma/4`$.
The three numerical products are again $`-1/16,-64/3,4i/3`$;
now the external bilinear is $`\bar\psi_m^i\gamma^{mn}\psi_n^j`$:

```math
\begin{aligned}
\frac{i\sigma}{4}\bar\psi_m^i\gamma^{mn}\psi_n^jL_{W\,ij}={}&-\frac{1}{16}\sigma(\bar\psi_m^i\gamma^{mn}\psi_n^j)\big(\overline{\widehat R}_{ab(i}(Q)\widehat R_{j)}{}^{ab}(Q)\big)-\frac{64}{3}\sigma(\bar\psi_m^i\gamma^{mn}\psi_n^j)\big(\bar\chi_{(i}\chi_{j)}\big)\\
 &+\frac{4i}{3}\sigma(\bar\psi_m^i\gamma^{mn}\psi_n^j)\big(\widehat R_{ab\,ij}(V)T^{ab}\big)
\end{aligned}
\tag{WA14}
```

For the remaining bridge term, multiply by $`C_m/4`$.
Here $`(1/4)(i/4)=i/16`$, $`(1/4)(256i/3)=64i/3`$, and
$`(1/4)(16/3)=4/3`$; there is no extra $`i`$ in its density prefactor:

```math
\begin{aligned}
\frac14C_m\bar\psi_n^i\gamma^{mnp}\psi_p^jL_{W\,ij}={}&\frac{i}{16}C_m(\bar\psi_n^i\gamma^{mnp}\psi_p^j)\big(\overline{\widehat R}_{ab(i}(Q)\widehat R_{j)}{}^{ab}(Q)\big)+\frac{64i}{3}C_m(\bar\psi_n^i\gamma^{mnp}\psi_p^j)\big(\bar\chi_{(i}\chi_{j)}\big)\\
 &+\frac{4}{3}C_m(\bar\psi_n^i\gamma^{mnp}\psi_p^j)\big(\widehat R_{ab\,ij}(V)T^{ab}\big)
\end{aligned}
\tag{WA15}
```

These are all twelve triplet products. In particular the source's
$`16Y_{ij}\widehat R_{ab}{}^{ij}(V)T^{ab}/3`$ becomes the last term
of WA12 after the defining-vector identification. Its fermionic value
must be retained even though Eq. (5.18) leaves it written with $`Y_{ij}`$.

### 4.7. Display the differentiated products retained in WA08

$`\mathcal D`$ is an even derivation. It therefore obeys an ordinary
plus-sign Leibniz rule even when both factors are odd. Metric compatibility
gives $`\mathcal D_bT^2=2T^{cd}\mathcal D_bT_{cd}`$. The six products
inside the first bracket of WA08 expand as follows:

```math
\begin{aligned}
4\mathcal D_b(\widehat C^{ab}{}_{cd}T^{cd})
&=4(\mathcal D_b\widehat C^{ab}{}_{cd})T^{cd}+4\widehat C^{ab}{}_{cd}\mathcal D_bT^{cd},\\
-\frac{64}{3}\mathcal D_b(DT^{ab})
&=-\frac{64}{3}(\mathcal D_bD)T^{ab}-\frac{64}{3}D\mathcal D_bT^{ab},\\
-\frac{128}{9}\mathcal D_b(T^{ab}T_{cd}T^{cd})
&=-\frac{128}{9}(\mathcal D_bT^{ab})T^2-\frac{256}{9}T^{ab}T^{cd}\mathcal D_bT_{cd},\\
-\frac{512}{3}\mathcal D_b(T^a{}_cT^{cd}T^b{}_d)
&=-\frac{512}{3}(\mathcal D_bT^a{}_c)T^{cd}T^b{}_d
-\frac{512}{3}T^a{}_c(\mathcal D_bT^{cd})T^b{}_d
-\frac{512}{3}T^a{}_cT^{cd}\mathcal D_bT^b{}_d,\\
8i\mathcal D_b(\overline{\widehat R(Q)^{ab}}\chi)
&=8i(\mathcal D_b\overline{\widehat R(Q)^{ab}})\chi
+8i\overline{\widehat R(Q)^{ab}}\mathcal D_b\chi,\\
-\frac{64i}{3}\mathcal D_b(\bar\chi\gamma^{ab}\chi)
&=-\frac{64i}{3}(\mathcal D_b\bar\chi)\gamma^{ab}\chi
-\frac{64i}{3}\bar\chi\gamma^{ab}\mathcal D_b\chi
=-\frac{128i}{3}\bar\chi\gamma^{ab}\mathcal D_b\chi.
\end{aligned}\tag{WA16}
```

Only in the last equality did we exchange odd spinors: the bivector
flip from C04 gives $`(\mathcal D_b\bar\chi)\gamma^{ab}\chi =+\bar\chi\gamma^{ab}\mathcal D_b\chi`$. Thus the two terms add.
For the epsilon-current bracket, the two product rules give four terms:

```math
\begin{aligned}
-32\varepsilon^a{}_{bcde}\mathcal D^b\!\left[
\frac23T^{cf}\mathcal D_fT^{de}+T^c{}_f\mathcal D^dT^{ef}\right]
={}&-\frac{64}{3}\varepsilon^a{}_{bcde}(\mathcal D^bT^{cf})\mathcal D_fT^{de}
-\frac{64}{3}\varepsilon^a{}_{bcde}T^{cf}\mathcal D^b\mathcal D_fT^{de}\\
&-32\varepsilon^a{}_{bcde}(\mathcal D^bT^c{}_f)\mathcal D^dT^{ef}
-32\varepsilon^a{}_{bcde}T^c{}_f\mathcal D^b\mathcal D^dT^{ef}.
\end{aligned}\tag{WA17}
```

Multiplying WA16 and WA17 by $`C_a`$ supplies every differentiated term
of WA08. The other eight terms of WA08 are already displayed separately.
The final expression retains the equivalent product-derivative form,
so that the current and its original derivative order remain readable.

## 5. Consistency Checks

### 5.1. Coverage, indices, parity and dimensions

| Term of WA04 | Fully multiplied expression | Contributions |
|---|---|---:|
| $`\sigma N_W`$ | WA07 | 15 |
| $`C_aE_W^a`$ | WA08; product rules WA16–WA17 | 24 after the displayed bilinear flip |
| $`i\bar\psi\varphi_W`$ | WA09 | 11 |
| $`\sigma\bar\psi_m\gamma^m\varphi_W/2`$ | WA10 | 11 |
| $`iC_m\bar\psi_n\gamma^{nm}\varphi_W/2`$ | WA11 | 11 |
| $`i\bar\psi^{(i}\psi^{j)}L_{W\,ij}/(4\sigma)`$ | WA12 | 3 |
| $`-\bar\psi_m^i\gamma^m\psi^jL_{W\,ij}/2`$ | WA13 | 3 |
| $`i\sigma\bar\psi_m^i\gamma^{mn}\psi_n^jL_{W\,ij}/4`$ | WA14 | 3 |
| $`C_m\bar\psi_n^i\gamma^{mnp}\psi_p^jL_{W\,ij}/4`$ | WA15 | 3 |

The count is $`15+24+33+12=84`$ with these product rules and the
C04 flip. It is a coverage count in this representation, not a count
of independent operators or of primitive DW-field monomials.

Every term in WA07 is a scalar, since its indices are already paired
in FM04. In WA08 the only free index of FM03 is paired with $`C_a`$.
In WA09–WA11 the lower spinor index is contracted with the upper barred
index, explicitly as WA06 when $`\widehat R(V)`$ occurs. In WA12–WA15
the two upper external indices contract the symmetric lower pair WA05.
The external $`m,n,p`$ indices appear exactly twice in every expression.
This checks the index structure without assuming that the fermionic
$`\widehat C`$ has every symmetry of an ordinary bosonic Weyl tensor.

The weights are

```math
w(\sigma)=w(C_a)=w(T)=1,\quad
w(\psi^i)=w(\chi)=w(\widehat R(Q))=\frac32,\quad
w(\psi_a)=\frac12,\quad
w(D)=w(\widehat C)=w(\widehat R(V))=2,
\quad w(\mathcal D_a)=1.
\tag{WA18}
```

Therefore $`w(L_W)=3`$, $`w(\varphi_W)=7/2`$ and
$`w(N_W)=w(E_W)=4`$. The nine density weights, in WA04 order, are

```math
1+4=5,\quad1+4=5,\quad\frac32+\frac72=5,\quad
1+\frac12+\frac72=5,\quad1+\frac12+\frac72=5,
\quad-1+3+3=5,\quad\frac12+\frac32+3=5,\quad
1+\frac12+\frac12+3=5,\quad1+\frac12+\frac12+3=5.
\tag{WA19}
```

With $`w(e)=-5`$, the density has the required conformal weight.
The same canonical dimensions hold before fixing the compensating scale.
No additional dimensionful coupling has been introduced.
All nine contributions are Grassmann even: the first two couple even
objects, the next three pair odd spinors, and the last four multiply an
even bilinear by an even triplet. Five dimensions introduces no Weyl
chirality projection. No quartic Grassmann product has been discarded.

### 5.2. Bosonic coefficients and the paper's boundary representative

Setting physical fermions to zero kills WA09–WA15 and the four bilinears
of WA07. The hats in the remaining terms reduce to their bosonic
covariants, and the Y term is zero because WA03 makes it a bilinear.
The eleven remaining WA07 coefficients are precisely the eleven
$`\sigma`$-weighted entries of OP (5.18). The first two WA08 coefficients,
$`1/16`$ and $`-1/12`$, give its gravitational and SU(2) Chern–Simons terms.

To explain the signs of the six displayed $`G_{ab}`$ terms in the paper,
consider its bosonic integration-by-parts step with a torsion-free
metric derivative. For an antisymmetric $`X^{ab}`$ the product rule is

```math
\begin{aligned}
eC_a\nabla_bX^{ab}=eC_\mu\nabla_\nu X^{\mu\nu}
&=\partial_\nu(eC_\mu X^{\mu\nu})-e(\nabla_\nu C_\mu)X^{\mu\nu}\\
&=\partial_\nu(eC_\mu X^{\mu\nu})
-\frac e2(\nabla_\nu C_\mu-\nabla_\mu C_\nu)X^{\mu\nu}
=\partial_\nu(eC_\mu X^{\mu\nu})+\frac e2G_{ab}X^{ab}.
\end{aligned}\tag{WA20}
```

Here $`X^{\mu\nu}=e_a{}^\mu e_b{}^\nu X^{ab}`$; $`\nabla`$ includes the corresponding frame connection.
The boundary term integrates to $`\int_{\partial M}d\Sigma_\nu C_\mu X^{\mu\nu}`$;
it is dropped only for vanishing boundary flux or compact support.
The paper's coefficient products are

```math
\begin{aligned}
\frac12G_{ab}(4C^{ab}{}_{cd}T^{cd})&=2C_{abcd}T^{cd}G^{ab},&
\frac12G_{ab}\left(-\frac{64}{3}DT^{ab}\right)&=-\frac{32}{3}DT_{ab}G^{ab},\\
\frac12G_{ab}\left(-\frac{128}{9}T^{ab}T^2\right)&=-\frac{64}{9}T_{ab}G^{ab}T^2,&
\frac12G_{ab}\left(-\frac{512}{3}T^a{}_cT^{cd}T^b{}_d\right)&=-\frac{256}{3}T_{ac}T^{cd}T_{bd}G^{ab},\\
\frac12G^{ab}\left(-\frac{64}{3}\varepsilon_{abcde}T^{cf}\mathcal D_fT^{de}\right)&=-\frac{32}{3}\varepsilon_{abcde}T^{cf}\mathcal D_fT^{de}G^{ab},&
\frac12G^{ab}\left(-32\varepsilon_{abcde}T^c{}_f\mathcal D^dT^{ef}\right)&=-16\varepsilon_{abcde}T^c{}_f\mathcal D^dT^{ef}G^{ab}.
\end{aligned}\tag{WA21}
```

Thus all nineteen explicitly bosonic coefficients are accounted for:
eleven from $`\sigma N_W`$, two Chern–Simons couplings, and six current
couplings. The source's remaining displayed $`Y`$ term is explicitly
completed in WA12. This is a coefficient comparison with (5.18).
WA20 is **not** being asserted for the full $`\mathcal D`$ with its S/K,
fermionic and dependent-connection actions. No all-order boundary
conversion is used in WA24; the final density keeps the original current.
A proof of equality to a fully component-expanded bosonic DW representative
must also track those connection terms.

As a normalization check on independent covariants, retaining only
$`\sigma`$, $`C_a`$ and the curvature leaves

```math
e^{-1}\mathcal L^{\rm map}\big|_{T=D=\widehat R(V)=\text{fermions}=0}
=\frac\sigma8 C_{abcd}C^{abcd}
+\frac1{16}\varepsilon^{abcde}C_aC_{bcfg}C_{de}{}^{fg}.
\tag{WA22}
```

This is a curvature-sector diagnostic, not a claimed DW solution; the
composite definitions need not admit arbitrary fields with these values.
All terms vanish when every map curvature, $`T`$, $`D`$ and fermion is zero.

### 5.3. Independent algebraic check and exact scope

The reusable checker is
[verify_weyl_action_substitution.py](../src/reference_checks/verify_weyl_action_substitution.py).
The [component-check guide](../README.md) gives the invocation and temporary-output scope.
It checks exact rational coefficients against the anchored map, unchanged
ordered tensor bodies for the two descendants, and every term of the
collected endpoint against WA07–WA15. A separate four-generator
Grassmann calculation compares the compact density and the distributed
spinor/triplet couplings, including nonzero fourth-degree coefficients.
All exact checks passed. The six Grassmann samples gave a maximum relative
residual $`8.54\times10^{-16}`$ (rounded upward), with nonzero quartic
coefficients included. This is an algebraic density test, not a test of
local supersymmetry.

The reality of the source density is the inherited starting assumption;
we retain its spinor order and the linear Majorana bar. We do not claim
an independent conjugation/IBP proof of the expanded expression. Likewise
the full local Q/S/K identities and the U(1) current conservation test
are outside this algebraic insertion's verification scope.

## 6. Final Result

Adding WA07–WA15 gives the following single density. Every composite
linear-multiplet slot and every defining-vector slot has been replaced.
Related terms share each row; the product derivatives are exactly those
expanded in WA16–WA17. $`T,\chi,D`$ and all hats mean the full definitions
AD01–AD08, not their bosonic restrictions.

```math
\fbox{$\displaystyle{
\begin{aligned}
e^{-1}\mathcal L_{\sigma C^2}^{\rm map}={}&\frac{1}{8}\sigma \widehat C_{abcd}\widehat C^{abcd}+\frac{64}{3}\sigma D^2\\
 &+\frac{1024}{9}\sigma DT_{ab}T^{ab}-\frac{16}{3}\sigma \widehat C_{abcd}T^{ab}T^{cd}\\
 &-\frac{1}{3}\sigma \widehat R_{ab}{}^{ij}(V)\widehat R^{ab}{}_{ij}(V)-\frac{64}{3}\sigma (\mathcal D_aT_{bc})(\mathcal D^aT^{bc})\\
 &+\frac{64}{3}\sigma (\mathcal D_bT_{ac})(\mathcal D^aT^{bc})-\frac{128}{3}\sigma T_{ab}\mathcal D^b\mathcal D_cT^{ac}\\
 &-\frac{128}{3}\sigma \varepsilon_{abcde}T^{ab}T^{cd}\mathcal D_fT^{ef}+1024\sigma T_{ab}T^{bc}T_{cd}T^{da}\\
 &-\frac{2816}{27}\sigma (T_{ab}T^{ab})^2+\frac{3}{4}\sigma \overline{\widehat R_{ab}(Q)}\gamma^c\mathcal D_c\widehat R^{ab}(Q)\\
 &-2i\sigma T^{ab}\overline{\widehat R_{ca}(Q)}\widehat R^c{}_{b}(Q)-\frac{160i}{3}\sigma T^{ab}\overline{\widehat R_{ab}(Q)}\chi\\
 &-\frac{256}{3}\sigma \bar\chi\gamma^a\mathcal D_a\chi\\
 &+\frac{1}{16}C_a\varepsilon^{abcde}\widehat C_{bcfg}\widehat C_{de}{}^{fg}-\frac{1}{12}C_a\varepsilon^{abcde}\widehat R(V)_{bc}{}^{ij}\widehat R(V)_{de\,ij}\\
 &+C_a\mathcal D_b\Big[4\widehat C^{ab}{}_{cd}T^{cd}-\frac{64}{3}DT^{ab}-\frac{128}{9}T^{ab}T_{cd}T^{cd}\\
 &\hspace{20mm}-\frac{512}{3}T^a{}_cT^{cd}T^b{}_d+8i\overline{\widehat R(Q)^{ab}}\chi-\frac{64i}{3}\bar\chi\gamma^{ab}\chi\Big]-32C_a\varepsilon^a{}_{bcde}\mathcal D^b\Big[\frac23T^{cf}\mathcal D_fT^{de}+T^c{}_f\mathcal D^dT^{ef}\Big]\\
 &-C_aT^{cd}\overline{\widehat R(Q)_{ec}}\gamma^a\widehat R(Q)^e{}_d+3C_aT_c{}^d\overline{\widehat R(Q)_e{}^a}\gamma^c\widehat R(Q)^e{}_d\\
 &+16C_aT^c{}_d\overline{\widehat R(Q)^a{}_c}\gamma^d\chi+\frac{16}{3}C_aT^{cd}\overline{\widehat R(Q)_{cd}}\gamma^a\chi\\
 &+\frac{i}{2}C_a\overline{\widehat R(Q)_{cd}}\mathcal D^a\widehat R(Q)^{cd}+\frac{3i}{2}C_a\overline{\widehat R(Q)_{cd}}\mathcal D^c\widehat R(Q)^{da}\\
 &-\frac{i}{8}\bar\psi\gamma_{cd}\widehat R_{ab}(Q)\widehat C^{abcd}+4\bar\psi\gamma_c\widehat R_{ab}(Q)\mathcal D^aT^{bc}\\
 &+\frac{128i}{3}\bar\psi\chi D-8\bar\psi\gamma_c\mathcal D^c\widehat R_{ab}(Q)T^{ab}\\
 &-8\bar\psi\gamma_a\mathcal D^c\widehat R_{bc}(Q)T^{ab}+\frac{64}{3}\bar\psi\gamma^{ab}\gamma^c\chi\mathcal D_aT_{bc}\\
 &+\frac{1024i}{9}\bar\psi\chi T^2-\frac{128}{3}\bar\psi\gamma_a\mathcal D_b\chi T^{ab}\\
 &+\frac{8i}{3}\bar\psi\gamma_{ab}\widehat R_{cd}(Q)T^{ab}T^{cd}+\frac{i}{2}\bar\psi^i\widehat R^{ab}{}_{ij}(V)\widehat R_{ab}{}^j(Q)\\
 &-\frac{8i}{3}\bar\psi^i\widehat R^{ab}{}_{ij}(V)\gamma_{ab}\chi^j\\
 &-\frac{1}{16}\sigma\bar\psi_m\gamma^m\gamma_{cd}\widehat R_{ab}(Q)\widehat C^{abcd}-2i\sigma\bar\psi_m\gamma^m\gamma_c\widehat R_{ab}(Q)\mathcal D^aT^{bc}\\
 &+\frac{64}{3}\sigma\bar\psi_m\gamma^m\chi D+4i\sigma\bar\psi_m\gamma^m\gamma_c\mathcal D^c\widehat R_{ab}(Q)T^{ab}\\
 &+4i\sigma\bar\psi_m\gamma^m\gamma_a\mathcal D^c\widehat R_{bc}(Q)T^{ab}-\frac{32i}{3}\sigma\bar\psi_m\gamma^m\gamma^{ab}\gamma^c\chi\mathcal D_aT_{bc}\\
 &+\frac{512}{9}\sigma\bar\psi_m\gamma^m\chi T^2+\frac{64i}{3}\sigma\bar\psi_m\gamma^m\gamma_a\mathcal D_b\chi T^{ab}\\
 &+\frac{4}{3}\sigma\bar\psi_m\gamma^m\gamma_{ab}\widehat R_{cd}(Q)T^{ab}T^{cd}+\frac{1}{4}\sigma\bar\psi_m^i\gamma^m\widehat R^{ab}{}_{ij}(V)\widehat R_{ab}{}^j(Q)\\
 &-\frac{4}{3}\sigma\bar\psi_m^i\gamma^m\widehat R^{ab}{}_{ij}(V)\gamma_{ab}\chi^j\\
 &-\frac{i}{16}C_m\bar\psi_n\gamma^{nm}\gamma_{cd}\widehat R_{ab}(Q)\widehat C^{abcd}+2C_m\bar\psi_n\gamma^{nm}\gamma_c\widehat R_{ab}(Q)\mathcal D^aT^{bc}\\
 &+\frac{64i}{3}C_m\bar\psi_n\gamma^{nm}\chi D-4C_m\bar\psi_n\gamma^{nm}\gamma_c\mathcal D^c\widehat R_{ab}(Q)T^{ab}\\
 &-4C_m\bar\psi_n\gamma^{nm}\gamma_a\mathcal D^c\widehat R_{bc}(Q)T^{ab}+\frac{32}{3}C_m\bar\psi_n\gamma^{nm}\gamma^{ab}\gamma^c\chi\mathcal D_aT_{bc}\\
 &+\frac{512i}{9}C_m\bar\psi_n\gamma^{nm}\chi T^2-\frac{64}{3}C_m\bar\psi_n\gamma^{nm}\gamma_a\mathcal D_b\chi T^{ab}\\
 &+\frac{4i}{3}C_m\bar\psi_n\gamma^{nm}\gamma_{ab}\widehat R_{cd}(Q)T^{ab}T^{cd}+\frac{i}{4}C_m\bar\psi_n^i\gamma^{nm}\widehat R^{ab}{}_{ij}(V)\widehat R_{ab}{}^j(Q)\\
 &-\frac{4i}{3}C_m\bar\psi_n^i\gamma^{nm}\widehat R^{ab}{}_{ij}(V)\gamma_{ab}\chi^j\\
 &-\frac{1}{16}\sigma^{-1}(\bar\psi^i\psi^j)\big(\overline{\widehat R}_{ab(i}(Q)\widehat R_{j)}{}^{ab}(Q)\big)-\frac{64}{3}\sigma^{-1}(\bar\psi^i\psi^j)\big(\bar\chi_{(i}\chi_{j)}\big)\\
 &+\frac{4i}{3}\sigma^{-1}(\bar\psi^i\psi^j)\big(\widehat R_{ab\,ij}(V)T^{ab}\big)\\
 &-\frac{i}{8}(\bar\psi_m^i\gamma^m\psi^j)\big(\overline{\widehat R}_{ab(i}(Q)\widehat R_{j)}{}^{ab}(Q)\big)-\frac{128i}{3}(\bar\psi_m^i\gamma^m\psi^j)\big(\bar\chi_{(i}\chi_{j)}\big)\\
 &-\frac{8}{3}(\bar\psi_m^i\gamma^m\psi^j)\big(\widehat R_{ab\,ij}(V)T^{ab}\big)\\
 &-\frac{1}{16}\sigma(\bar\psi_m^i\gamma^{mn}\psi_n^j)\big(\overline{\widehat R}_{ab(i}(Q)\widehat R_{j)}{}^{ab}(Q)\big)-\frac{64}{3}\sigma(\bar\psi_m^i\gamma^{mn}\psi_n^j)\big(\bar\chi_{(i}\chi_{j)}\big)\\
 &+\frac{4i}{3}\sigma(\bar\psi_m^i\gamma^{mn}\psi_n^j)\big(\widehat R_{ab\,ij}(V)T^{ab}\big)\\
 &+\frac{i}{16}C_m(\bar\psi_n^i\gamma^{mnp}\psi_p^j)\big(\overline{\widehat R}_{ab(i}(Q)\widehat R_{j)}{}^{ab}(Q)\big)+\frac{64i}{3}C_m(\bar\psi_n^i\gamma^{mnp}\psi_p^j)\big(\bar\chi_{(i}\chi_{j)}\big)\\
 &+\frac{4}{3}C_m(\bar\psi_n^i\gamma^{mnp}\psi_p^j)\big(\widehat R_{ab\,ij}(V)T^{ab}\big)
\end{aligned}}$}
\tag{WA24}
```

The corresponding source-normalized action is

```math
S_{\rm Weyl^2}^{\rm map}=\int d^5x\,\mathcal L_{\sigma C^2}^{\rm map}
=\int d^5x\,e\left(e^{-1}\mathcal L_{\sigma C^2}^{\rm map}\right).
\tag{WA25}
```

There is no unspecified “$`+\text{fermions}`$” contribution in WA24.
There are, however, unexpanded **defined** supercovariants and ordered
gamma products, just as in the map and in the paper's conformal method.
This is the full map-inserted density in that representation.

## 7. Convention Dependence and Remaining Uncertainties

The algebraic substitution is exact under A1–A5, at all retained physical
fermion orders; no perturbative error estimate applies. Its status is
conditional on the anchored map. It does not settle the adopted spinor's
$`8/3`$ versus the printed $`16/3`$ discrepancy beyond the
Q($`L`$) derivation recorded in M07–M08/X12.

The outstanding certification steps are the traceless SU(2) part of
Q($`\varphi_W`$), S($`\varphi_W`$), the independent $`E_W,N_W`$ laws and the
full constrained-vector divergence. In particular writing $`P^a`$ using
WA02 does not by itself prove the existence of a conserved three-form
current for an arbitrary candidate map. These checks are needed before
calling WA24 an independently verified nonlinear supersymmetric action.

The [current action](../../../weyl2/action/README.md) supplies the normalized
component expressions used by the [AdS5 spectrum](../../../weyl2/ads5/README.md).
The present result remains the gauge-unfixed density in defined
supercovariants; a full primitive-field expansion and an independent
nonlinear transformation proof are outside its scope.

Source trail: local Özkan–Pang Gauss–Bonnet completion paper (3.1), (5.8),
(5.16)–(5.18); local companion Özkan–Pang matter/invariants paper (3.1)–(3.2)
for the full current bridge; master A01–A02/V03/H01/D01–D02/W04/R01–R03/G01;
map FM01–FM04 and their [component derivations](README.md).
The cited OP and OPall sources are linked in the [bibliography](../../../references/bibliography.md);
the relevant density/current pages are OP pp.10,20 and OPall p.8.
