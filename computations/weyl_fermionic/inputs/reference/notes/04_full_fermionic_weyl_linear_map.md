# Full fermionic Weyl-to-linear map

This is the consolidated working reference for
$`(L_W^{ij},\varphi_W^i,E_W^a,N_W)`$ in the ungauged five-dimensional
construction. It collects the findings of the
[fermionic-map calculation notebook](../../../derivations/fermionic-map.md)
into four explicit formulas. Use this file when inserting or varying the
map, together with the definitions in
[the convention reference](../../../derivations/component_conventions.md).

**Scope.** The map is written in gauge-unfixed Standard-Weyl covariants,
with all physical fermion orders retained in the full curvatures and
covariant derivatives. There is no “plus fermions” remainder. The scalar
and vector descendants are extracted from the complete singlet Q-variation.
The [ungauged density](../../../derivations/full-fermionic-weyl2-action.md),
[gauged construction](../../../../../weyl2/action/details/construction.md)
and [AdS5 reduction](../../../../../weyl2/ads5/README.md) use this map.
The component checks below establish their stated algebraic identities;
independent full descendant transformation laws and nonlinear multiplet
closure are outside those checks.

**Provenance.** The selected construction starts from local Özkan–Pang
Eq. (5.8), with conventions and source-interface repairs recorded in
master C01–C07/G01–G04/W01–W04/R01–R07 and X01–X12. The working spinor is
M08, derived from Q($`L`$). The printed
M02 coefficient $`16/3`$ is retained as a source record; the working
coefficient is **$`8/3`$**. No other field or coupling rescaling accompanies
that choice.

## 1. Conventions and definitions used by every component

<!-- ASSERT_CONVENTION: natural_units=hbar=c=1, metric_signature=(-,+,+,+,+), source_lock=UNG-WEYL2-OP58-CONVENTIONS-v5 -->

- $`a,b,\ldots=0,\ldots,4`$ are tangent indices;
  $`i,j=1,2`$ are SU(2) doublet indices.
- $`\eta_{ab}=\mathop{\mathrm{diag}}\nolimits(-,+,+,+,+)`$,
  $`\varepsilon^{01234}=+1`$, $`\varepsilon_{01234}=-1`$.
  The five-index epsilon is the volume tensor.
- $`\{\gamma^a,\gamma^b\}=2\eta^{ab}`$,
  $`\gamma^{a_1\ldots a_n}=\gamma^{[a_1}\cdots\gamma^{a_n]}`$ and
  $`\gamma^{01234}=i\mathbf1`$. Brackets and parentheses have unit weight.
  Repeated antisymmetric pairs are summed over all ordered values.
- $`T_{ab}=-T_{ba}`$, $`\chi^i`$ and $`D`$ are the Standard-Weyl auxiliary
  tensor, spinor and scalar. Here $`D`$ denotes the scalar field; derivatives
  are always written $`\mathcal D_a`$. The only scalar shorthand is
  $`T^2:=T_{ab}T^{ab}`$.
- $`\widehat R_{ab}{}^i(Q)`$ is the full constrained gravitino curvature
  (master R01); $`\widehat R_{ab}{}^{ij}(V)`$ is the full SU(2) curvature
  (R02); $`\widehat C_{abcd}`$ is the full Lorentz/Weyl curvature of R03.
  In particular, $`\widehat C`$ is not replaced by the ordinary bosonic
  Weyl tensor inside these formulas.
- The dependent connections $`\omega_\mu{}^{ab},\phi_\mu^i,f_\mu{}^a`$
  are fixed by G03/R01/R03, including
  $`\gamma^a\widehat R_{ab}(Q)=0`$. These are conventional constraints,
  not field equations.
- $`\bar\zeta^{,i}=(\zeta^i)^T\mathsf C`$ is the C03 Majorana bar,
  linear in $`i`$. All spinors are Grassmann odd. A suppressed SU(2)
  contraction means $`\bar u\Gamma v=\bar u^i\Gamma v_i`$.
  Thus contracted scalar and vector bilinears have a minus under
  interchange of odd spinors, while contracted bivector bilinears have
  a plus.
- $`X_i=X^j\varepsilon_{ji}`$ and $`X^i=\varepsilon^{ij}X_j`$, with
  $`\varepsilon_{12}=\varepsilon^{12}=1`$. In particular,
  $`L_{W,ij}=L_W^{kl}\varepsilon_{ki}\varepsilon_{lj}`$ and
  $`E_{W,a}=\eta_{ab}E_W^b`$.

Every $`\mathcal D`$ is the full superconformal derivative of G01:

```math
\mathcal D_\mu\Phi=\partial_\mu\Phi
-\delta_D(b_\mu)\Phi-\delta_M(\omega_\mu)\Phi
-\delta_U(V_\mu)\Phi-\delta_Q(\psi_\mu)\Phi
-\delta_S(\phi_\mu)\Phi-\delta_K(f_\mu)\Phi,
\qquad \mathcal D_a=e_a{}^\mu\mathcal D_\mu.
```

It acts on products by the covariant product rule. A second derivative
acts on the full first derivative, including its S/K transformation.
Keep the displayed derivative order. The product derivatives in the
vector component below are retained local terms, not discarded boundary
terms. Setting a physical field to zero does not automatically set its
full covariant derivative to zero.

| Object | Weyl weight | SU(2) representation / parity |
|---|---:|---|
| $`L_W^{ij}`$ | $`3`$ | symmetric triplet, even |
| $`\varphi_W^i`$ | $`7/2`$ | doublet, odd |
| $`E_W^a`$ | $`4`$ | singlet vector, even |
| $`N_W`$ | $`4`$ | singlet scalar, even |

The subscript $`W`$ labels the Weyl **composite** linear multiplet. It must
not be identified with the independent compensator
$`(L_c^{ij},\varphi_c^i,E_{ca},N_c)`$.

## 2. Scalar triplet

**Anchor:** master M01; notebook Parts I–II. Its S-invariance and
Q-variation were calculated before extracting the descendants.

```math
\boxed{
\begin{aligned}
L_W^{ij}={}&\frac{i}{4}\overline{\widehat R}_{ab}{}^{(i}(Q)
                       \widehat R^{j)ab}(Q)
+\frac{256i}{3}\bar\chi^{(i}\chi^{j)}
+\frac{16}{3}\widehat R_{ab}{}^{ij}(V)T^{ab}.
\end{aligned}}
\tag{FM01}
```

## 3. Adopted composite spinor

**Anchor:** master M08; notebook Q63, with its full Q-variation in
Parts III–VIII. All eleven terms are retained.

```math
\boxed{
\begin{aligned}
\varphi_W^i={}&
-\frac18\gamma_{cd}\widehat R_{ab}{}^i(Q)\widehat C^{abcd}
-4i\gamma_c\widehat R_{ab}{}^i(Q)\mathcal D^aT^{bc}
+\frac{128}{3}\chi^iD
\\
&+8i\gamma_c\mathcal D^c\widehat R_{ab}{}^i(Q)T^{ab}
+8i\gamma_a\mathcal D^c\widehat R_{bc}{}^i(Q)T^{ab}
-\frac{64i}{3}\gamma^{ab}\gamma^c\mathcal D_aT_{bc}\chi^i
\\
&+\frac{1024}{9}T^2\chi^i
+\frac{128i}{3}\gamma_a\mathcal D_b\chi^i T^{ab}
+\frac{8}{3}\gamma_{ab}\widehat R_{cd}{}^i(Q)T^{ab}T^{cd}
\\
&+\frac12\widehat R^{ab\,i}{}_{j}(V)\widehat R_{ab}{}^j(Q)
-\frac83\widehat R^{ab\,i}{}_{j}(V)\gamma_{ab}\chi^j.
\end{aligned}}
\tag{FM02}
```

The third term on the third line has coefficient $`8/3`$. The displayed
$`\gamma^{ab}\gamma^c`$ elsewhere is the ordered matrix product of M08;
it is not a single rank-three gamma.

## 4. Vector component, with the fermionic completion explicit

**Anchor:** master M14c–M14d; notebook Part VIII, VC42–VC44.
The conversion from the coefficient of $`\gamma_a\epsilon^i`$ is

```math
-\frac i2E_W^a=t^a
\quad\Longrightarrow\quad E_W^a=2it^a.
```

Multiplying every term of VC42 by $`2i`$ gives

```math
\boxed{
\begin{aligned}
E_W^a={}&\frac1{16}\varepsilon^{abcde}
 \widehat C_{bcfg}\widehat C_{de}{}^{fg}
-\frac1{12}\varepsilon^{abcde}
 \widehat R(V)_{bc}{}^{ij}\widehat R(V)_{de\,ij}\\
&+\mathcal D_b\Big[
 4\widehat C^{ab}{}_{cd}T^{cd}
 -\frac{64}{3}DT^{ab}
 -\frac{128}{9}T^{ab}T_{cd}T^{cd}
 -\frac{512}{3}T^a{}_cT^{cd}T^b{}_d\\
&\hspace{24mm}
 +8i\overline{\widehat R(Q)^{ab}}\chi
 -\frac{64i}{3}\bar\chi\gamma^{ab}\chi\Big]\\
&-32\varepsilon^a{}_{bcde}\mathcal D^b\Big[
 \frac23T^{cf}\mathcal D_fT^{de}
 +T^c{}_f\mathcal D^dT^{ef}\Big]\\
&-T^{cd}\overline{\widehat R(Q)_{ec}}
 \gamma^a\widehat R(Q)^e{}_d
+3T_c{}^d\overline{\widehat R(Q)_e{}^a}
 \gamma^c\widehat R(Q)^e{}_d\\
&+16T^c{}_d\overline{\widehat R(Q)^a{}_c}\gamma^d\chi
+\frac{16}{3}T^{cd}\overline{\widehat R(Q)_{cd}}\gamma^a\chi\\
&+\frac i2\overline{\widehat R(Q)_{cd}}\mathcal D^a\widehat R(Q)^{cd}
+\frac{3i}{2}\overline{\widehat R(Q)_{cd}}\mathcal D^c\widehat R(Q)^{da}.
\end{aligned}}
\tag{FM03}
```

This is the vector component itself, rather than the intermediate
coefficient $`t^a`$. In particular, the final two terms carry $`i/2`$ and
$`3i/2`$, and the $`T\overline{R(Q)}R(Q)`$ terms carry $`-1`$ and $`+3`$.
The product derivatives include the full differentiated fermion terms
shown in VC38; none have been omitted.

## 5. Scalar component, with the fermionic completion explicit

**Anchor:** master M13c and M14d; notebook Part VII, SC32–SC33.
The scalar-singlet coefficient fixes $`N_W/2=p`$, hence $`N_W=2p`$:

```math
\boxed{
\begin{aligned}
N_W={}&\frac18\widehat C_{abcd}\widehat C^{abcd}
+\frac{64}{3}D^2+\frac{1024}{9}D\,T_{ab}T^{ab}
-\frac{16}{3}\widehat C_{abcd}T^{ab}T^{cd}
-\frac13\widehat R_{ab}{}^{ij}(V)\widehat R^{ab}{}_{ij}(V)\\
&-\frac{64}{3}(\mathcal D_aT_{bc})(\mathcal D^aT^{bc})
+\frac{64}{3}(\mathcal D_bT_{ac})(\mathcal D^aT^{bc})
-\frac{128}{3}T_{ab}\mathcal D^b\mathcal D_cT^{ac}\\
&-\frac{128}{3}\varepsilon_{abcde}T^{ab}T^{cd}\mathcal D_fT^{ef}
+1024T_{ab}T^{bc}T_{cd}T^{da}
-\frac{2816}{27}(T_{ab}T^{ab})^2\\
&+\frac34\overline{\widehat R_{ab}(Q)}\gamma^c\mathcal D_c\widehat R^{ab}(Q)
-2iT^{ab}\overline{\widehat R_{ca}(Q)}\widehat R^c{}_{b}(Q)\\
&-\frac{160i}{3}T^{ab}\overline{\widehat R_{ab}(Q)}\chi
-\frac{256}{3}\bar\chi\gamma^a\mathcal D_a\chi.
\end{aligned}}
\tag{FM04}
```

The last two lines display all four explicit fermion bilinears of this
canonical scalar expression. Hidden fermions in the other lines remain
included through the full covariants. The order
$`\mathcal D^b\mathcal D_cT^{ac}`$ is fixed by the commutator calculation
SC09–SC16; it must not be reversed without the complete M12b correction.

## 6. What the calculated variations establish

The completed derivations give

```math
\begin{aligned}
\delta_S L_W^{ij}&=0,\\
\delta_Q L_W^{ij}&=i\bar\epsilon^{(i}\varphi_W^{j)},\\
\left.\delta_Q\varphi_W^i\right|_{\mathrm{SU(2)\ singlet}}
&=\left(\frac12N_W-\frac i2\gamma_aE_W^a\right)\epsilon^i,
\qquad k^{ab}=0.
\end{aligned}
\tag{FM05}
```

These are established relative to the v5 operational laws and
conventional identities. They do not set the traceless SU(2) part of
$`\delta_Q\varphi_W^i`$ to zero. For full matching, master L01 requires

```math
\begin{aligned}
\delta\varphi_W^i={}&
-\frac i2\gamma^a\mathcal D_aL_W^{ij}\epsilon_j
-\frac i2\gamma^aE_{W\,a}\epsilon^i
+\frac12N_W\epsilon^i
-\gamma^{ab}T_{ab}L_W^{ij}\epsilon_j
+3L_W^{ij}\eta_j.
\end{aligned}
\tag{FM06}
```

FM06 is the **target law** of the linear multiplet. The listed component
checks establish the singlet terms and FM05's scalar-triplet laws.
The independent descendant laws are

```math
\begin{aligned}
\delta E_{W\,a}={}&-\frac i2\bar\epsilon\gamma_{ab}\mathcal D^b\varphi_W
-2\bar\epsilon\gamma^b\varphi_W T_{ba}
-2\bar\eta\gamma_a\varphi_W,\\
\delta N_W={}&\frac12\bar\epsilon\gamma^a\mathcal D_a\varphi_W
+\frac{3i}{2}\bar\epsilon\gamma^{ab}T_{ab}\varphi_W
+4i\bar\epsilon^i\chi^jL_{W\,ij}
+\frac{3i}{2}\bar\eta\varphi_W,\\
\mathcal D^aE_{W\,a}={}&0.
\end{aligned}
\tag{FM07}
```

FM07 records the L01/L03 requirements, **not newly proved identities**.
In particular the last line uses the full L02 derivative, including its
fermion and connection terms; an ordinary divergence test is insufficient.

## 7. Verification scope

| Finding | Provenance | Status |
|---|---|---|
| $`\delta_SL_W=0`$ | M06; notebook Part I | Derived and algebraically checked |
| Q($`L_W`$) gives FM02 with $`8/3`$ | M07–M08; Part II Q63 | Derived in the stated source calculation |
| Full termwise Q($`\varphi_W`$), with singlet Fierz extraction | M09–M11; Parts III–V | Calculated without a fermion truncation |
| Singlet bivector cancels | M12; Part VI | Proved and independently checked |
| $`N_W=2p`$, all 15 canonical scalar terms | M13; Part VII | Derived singlet slot; bosonic part matches all 11 M04 terms |
| $`E_W=2it`$, all 34 starting vector terms accounted for | M14; Part VIII | Derived singlet slot; bosonic part matches all 8 M03 structures |
| FM01–FM04 transcription and E/N normalization in this file | [Map-anchor checker](../../../src/reference_checks/verify_full_fermionic_map_anchor.py) via the component-check suite | Exact coefficient and tensor-body comparison with M01/M08/M13/M14 |
| Traceless SU(2) Q($`\varphi_W`$) and S($`\varphi_W`$) | FM06 | Outside the listed component checks |
| Independent Q/S laws of $`E_W,N_W`$ and full divergence | FM07 | Outside the listed component checks |
| Gauged density and AdS5 spectrum | [Gauged construction](../../../../../weyl2/action/details/construction.md), [AdS5 reduction](../../../../../weyl2/ads5/README.md) | Separate calculations using this map |

The [component-check suite](../../../checks/reference_suite.py) runs the
[S-invariance](../../../src/reference_checks/verify_weyl_map_s_invariance.py),
[triplet Q-variation](../../../src/reference_checks/verify_weyl_map_q_variation.py),
[bivector cancellation](../../../src/reference_checks/verify_weyl_bivector_cancellation.py),
[scalar collection](../../../src/reference_checks/verify_weyl_scalar_canonicalization.py)
and [vector collection](../../../src/reference_checks/verify_weyl_vector_canonicalization.py)
checks. The [package guide](../../../README.md) gives the command and output scope.
The map's weights are $`(3,7/2,4,4)`$; the scalar and vector components have
the reality assignments checked in SC28–SC29 and VC40. None of these
checks uses an equation of motion or discards a total derivative.
