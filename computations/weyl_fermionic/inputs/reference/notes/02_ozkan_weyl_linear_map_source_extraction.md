# Özkan–Pang Weyl-to-linear map: source extraction and completion target

**Date:** 2026-09-17  
**Source-selection lock:** `UNG-WEYL2-OP58-CONVENTIONS-v5`  
**Status:** Source extraction only. No missing fermionic term has been derived.

## 1. Problem and Target

The construction uses the map in Özkan–Pang, *Supersymmetric Completion of
Gauss-Bonnet Combination in Five Dimensions*, local corrected
arXiv:1301.6622v4. In the current Weyl² context, the relevant map is **§5.1,
Eq. (5.8), printed/PDF page 18**: Weyl-multiplet fields and curvatures
realize a composite linear multiplet

```math
\{T_{ab},\chi^i,D,\widehat R_{ab}{}^i(Q),
\widehat R_{ab}{}^{ij}(V),\widehat C_{abcd};\text{connections}\}
\longmapsto (L^{ij},\varphi^i,E_a,N).
\tag{1}
```

The source realizes $`T,\chi,D`$ through the ungauged Dilaton-Weyl composites
of (2.9)–(2.10). The symbols in (1) are a convenient intermediate description;
they are not a declaration of additional independent fields.

This is the Weyl **composite** linear multiplet, distinct from the original
linear compensator. We keep the paper's component names in the extraction.
Eq. (5.16) is the separate defining-vector identification used later; it is
not the partially displayed Weyl-to-linear map being completed here.

The selected procedure is: extract (5.8), derive its omitted fermionic pieces
from source Q/S transformations, verify the completed multiplet, and only
then insert it in the vector–linear density. The operational inputs and source-derived repairs are centralized in
[CONVENTIONS.md](../../../derivations/component_conventions.md), especially M01–M05 and X01–X11.
The later two-derivative + lambda_Weyl Weyl² spectrum objective is unchanged.

**Current boundary:** no gauge fixing, field equations, auxiliary elimination,
field redefinition, integration by parts, action construction or spectrum.
All displayed fermions are retained. Omitted fermions are explicitly unknown,
not zero. This note transcribes and classifies; it does not derive the map.

## 2. Convention Ledger

**Operational update:** the following records the original transcription.
For calculation use master C01–C07 and X01–X11, which distinguish fixed-index
from contracted bilinear flips and repair source errors. No source-derived
correction is silently inserted into the map transcription below.

Use the paper's own notation and Appendix A, PDF pp.28–29:

- $`D=5`$, $`\eta_{ab}=\mathrm{diag}(-,+,+,+,+)`$; tangent indices
  $`a,b,\ldots=0,\ldots,4`$, $`SU(2)`$ indices $`i,j=1,2`$.
- $`A^i=\varepsilon^{ij}A_j`$, $`A_i=A^j\varepsilon_{ji}`$,
  $`\varepsilon_{12}=\varepsilon^{12}=1`$; weighted brackets.
- $`\gamma^{a_1\cdots a_n}=\gamma^{[a_1}\cdots\gamma^{a_n]}`$;
  $`\{\gamma^a,\gamma^b\}=2\eta^{ab}`$; source duality
  $`\gamma^{abcde}=i\epsilon^{abcde}`$.
- Suppressed spinor indices mean NW–SE contraction; source bilinear flip
  signs are $`t_0=t_1=1`$, $`t_2=t_3=-1`$. No bilinear is reordered here.
- Fermions and Q/S parameters are Grassmann odd. Use the source symplectic
  Majorana convention; no Dirac-bar replacement or complex conjugation of
  scalar coefficients is introduced.
- $`\mathcal D`$ denotes the paper's full superconformal covariant derivative,
  not a Levi-Civita derivative. Hats and unhatted quantities are preserved
  as printed in (5.8). No curvature sign conversion is made.
- The Riemann convention is inherited from the source curvature definitions
  (2.5)–(2.7); no curvature commutator is evaluated in this extraction.
- No boundary conditions or fermionic functional-derivative convention are
  needed for transcription. They must be specified when performing the
  corresponding later operations. No action normalization is changed here.

## 3. Definitions and Required Identities

The shorthand in (5.9), printed/PDF p.19, is

```math
T^2=T_{ab}T^{ab},\qquad
T^4=T_{ab}T^{bc}T_{cd}T^{da},\qquad
(T^2)^2=(T_{ab}T^{ab})^2.
\tag{2}
```

$`\gamma\cdot T=\gamma^{ab}T_{ab}`$ and
$`\mathord{\not{\mathcal D}}=\gamma^a\mathcal D_a`$.
$`\widehat R(Q)`$ is the gravitino curvature, (2.6), PDF p.6;
$`\widehat R(V)`$ is the supercovariant R-symmetry curvature, (2.7), PDF p.7.
$`\widehat C`$ denotes the superconformal Lorentz curvature as explained
between (5.4) and (5.5), PDF p.17. The unhatted R-symmetry field strength is

```math
V_{\mu\nu}{}^{ij}
=2\partial_{[\mu}V_{\nu]}{}^{ij}
-2V_{[\mu}{}^{k(i}V_{\nu]k}{}^{j)}
\qquad\text{[source (5.13), PDF p.19].}
\tag{3}
```

The map below deliberately retains the source's unhatted $`C,V`$ in its
bosonic $`E_a,N`$ displays. Adding hats alone is not a derivation of their
fermionic completion. All implicit connection definitions must be expanded
consistently in the component calculation.

## 4. Detailed Source Extraction

### 4.1 The scalar triplet

```math
\begin{aligned}
L^{ij}={}&\frac{i}{4}\overline{\widehat R}_{ab}{}^{(i}(Q)
                       \widehat R^{j)ab}(Q)
+\frac{256i}{3}\bar\chi^{(i}\chi^{j)}
+\frac{16}{3}\widehat R_{ab}{}^{ij}(V)T^{ab}.
\end{aligned}
\tag{4; source 5.8-L}
```

The first two terms are explicit fermion bilinears. The third also has
implicit fermions through $`\widehat R(V)`$ and, after the Dilaton-Weyl map,
through $`T`$. Thus (5.8) is not wholly bosonic.

### 4.2 The spinor

```math
\begin{aligned}
\varphi^i={}&
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
+\frac{16}{3}\gamma_{ab}\widehat R_{cd}{}^i(Q)T^{ab}T^{cd}
\\
&+\frac12\widehat R^{ab\,i}{}_{j}(V)\widehat R_{ab}{}^j(Q)
-\frac83\widehat R^{ab\,i}{}_{j}(V)\gamma_{ab}\chi^j.
\end{aligned}
\tag{5; source 5.8-phi}
```

The source prints this fermionic component without a separate remainder
marker. It remains supercovariant: apparent linearity in the explicit
fermionic factors does not imply linearity in independent physical fermions.
The [component variation](../../../derivations/fermionic-map.md) checks the
working map. This source transcription alone does not establish all-order
closure.

### 4.3 The constrained vector, with its printed omission

```math
\begin{aligned}
E_a={}&\frac1{16}\epsilon_{abcde}C^{bcfg}C^{de}{}_{fg}
-\frac1{12}\epsilon_{abcde}V^{bc}{}_{ij}V^{de\,ij}
\\
&+\mathcal D^b\left(
4C_{abcd}T^{cd}-\frac{64}{3}DT_{ab}
-\frac{128}{9}T_{ab}T^2-\frac{512}{3}T_{ac}T^{cd}T_{bd}
\right)
\\
&-32\epsilon_{abcde}\mathcal D^b\left(
\frac23T^{cf}\mathcal D_fT^{de}
+T^c{}_{f}\mathcal D^dT^{ef}\right)
+\text{fermions}.
\end{aligned}
\tag{6; source 5.8-E}
```

The terminal “fermions” is present in the source. It is an unknown
completion, not a term set to zero or an independently specified functional.

### 4.4 The scalar, with its printed omission

```math
\begin{aligned}
N={}&\frac18C^{abcd}C_{abcd}
+\frac{64}{3}D^2+\frac{1024}{9}T^2D
-\frac{16}{3}C_{abcd}T^{ab}T^{cd}
-\frac13V_{ab}{}^{ij}V^{ab}{}_{ij}
\\
&-\frac{64}{3}\mathcal D_aT_{bc}\mathcal D^aT^{bc}
+\frac{64}{3}\mathcal D_bT_{ac}\mathcal D^aT^{bc}
-\frac{128}{3}T_{ab}\mathcal D^b\mathcal D_cT^{ac}
\\
&-\frac{128}{3}\epsilon_{abcde}T^{ab}T^{cd}\mathcal D_fT^{ef}
+1024T^4-\frac{2816}{27}(T^2)^2
+\text{fermions}.
\end{aligned}
\tag{7; source 5.8-N}
```

The two explicit missing-completion locations are therefore (6) and (7).
They are not a reason to discard the already printed fermions in (4)–(5).

### 4.5 The transformation equations that will determine the completion

Source (2.18), printed/PDF p.9, gives

```math
\delta L^{ij}=i\bar\epsilon^{(i}\varphi^{j)},
\tag{8}
```

```math
\begin{aligned}
\delta\varphi^i={}&
-\frac{i}{2}\mathord{\not{\mathcal D}}L^{ij}\epsilon_j
-\frac{i}{2}\gamma^aE_a\epsilon^i
+\frac12N\epsilon^i
-\gamma\cdot T\,L^{ij}\epsilon_j
+3L^{ij}\eta_j,
\end{aligned}
\tag{9}
```

```math
\delta E_a=-\frac{i}{2}\bar\epsilon\gamma_{ab}\mathcal D^b\varphi
-2\bar\epsilon\gamma^b\varphi\,T_{ba}
-2\bar\eta\gamma_a\varphi,
\tag{10}
```

```math
\delta N=\frac12\bar\epsilon\mathord{\not{\mathcal D}}\varphi
+\frac{3i}{2}\bar\epsilon\gamma\cdot T\,\varphi
+4i\bar\epsilon^i\chi^jL_{ij}
+\frac{3i}{2}\bar\eta\varphi.
\tag{11}
```

The constrained-vector identity is

```math
\mathcal D^aE_a=0\qquad\text{[source (2.20), PDF p.9].}
\tag{12}
```

We will vary (4) using the Weyl transformations and compare with (8) to
check/recover (5). Next we will vary (5), retaining variations of all hatted
curvatures, dependent connections and covariant derivatives, and match (9).
The scalar and gamma-vector structures determine the candidate $`N`$ and
$`E_a`$ once the other displayed terms and the $`SU(2)`$ structures have been
separated. Fierz reduction and the full source identities must precede a
claim that the matching is complete or unique. Finally (10)–(12) give
independent consistency conditions on those candidates.

This is the planned calculation, not a variation performed in this note.
Source p.19 explicitly says that Q/S transformations of supercovariant
curvatures from its reference [26] were used to obtain (5.8); the corresponding
5D Weyl-multiplet source is already local in this project.

## 5. Consistency Checks

**Visual transcription:** source PDF pp.18 and 9 were rendered and inspected.
The extraction retains 3 additive terms in L, 11 in varphi, and the source's
explicit remainder markers in E and N. No sign or coefficient repair is
asserted in this extraction.

**Indices and parity:** each L term has two symmetric free $`SU(2)`$ indices
and even Grassmann parity; each varphi term has one free spinor doublet
index and odd parity. In E all Lorentz indices except a are contracted;
N is a Lorentz and $`SU(2)`$ scalar. $`\gamma^{ab}\gamma^c`$ is retained as a
product, not changed into $`\gamma^{abc}`$. Derivative ordering
$`\mathcal D^b\mathcal D_cT^{ac}`$ is preserved.

**Conformal weights:** these are Weyl weights before scale fixing, not
canonically normalized Poincare mass dimensions. The source transformations and W Table3 give $`w(T)=1`$, $`w(\chi)=3/2`$; the transformation (2.11)
gives $`w(D)=2`$. Tangent curvatures have
$`w(\widehat R(Q))=3/2`$, $`w(C)=w(R(V))=2`$, and
$`w(\mathcal D_a)=1`$. Consequently:

- L: $`3/2+3/2=3`$, $`3/2+3/2=3`$, $`2+1=3`$.
- varphi: $`3/2+2=7/2`$; $`3/2+1+1=7/2`$;
  $`3/2+2=7/2`$; derivative-curvature times T has
  $`1+3/2+1=7/2`$; $`T^2\chi`$ and $`R(V)\chi`$ both have $`7/2`$.
- E: $`C^2,V^2`$ have weight 4;
  $`\mathcal D(CT),\mathcal D(DT),\mathcal D(T^3)`$ have $`1+3=4`$;
  $`\mathcal D(T\mathcal DT)`$ has $`1+1+1+1=4`$.
- N: $`C^2,D^2,T^2D,CTT,V^2,(\mathcal DT)^2, T\mathcal D\mathcal DT,T^2\mathcal DT,T^4`$ all have weight 4.

These match the linear-multiplet weights in Appendix B, PDF p.29:
$`(3,7/2,4,4)`$ for $`(L,\varphi,E,N)`$.

**Bosonic restriction:** with all fermions zero,
$`\widehat R(Q)=\chi=0`$, so

```math
L^{ij}\big|_{\mathrm{bos}}=\frac{16}{3}V_{ab}{}^{ij}T^{ab},
\qquad\varphi^i\big|_{\mathrm{bos}}=0.
\tag{13}
```

In E,N take the bosonic restrictions of all retained composites and
derivatives as well; simply deleting the words “fermions” is not an
independent-field expansion. As a narrower algebraic check, when additionally
$`T=D=V=0`$, the displayed bosonic expressions reduce to
$`L=\varphi=0`$, $`E_a=\epsilon_{abcde}C^{bcfg}C^{de}{}_{fg}/16`$ and
$`N=C^2/8`$. This is a restriction of the intermediate polynomial, not a
claimed arbitrary Dilaton-Weyl background or vacuum solution.

**Extraction scope:** transcription alone does not establish direct Q/S
variation matching, Fierz reduction, the full supercovariant divergence
identity or reality of the completed map. The
[component derivations](../../../derivations/README.md) give the calculated map
and the scope of its algebraic checks.

## 6. Final Result

```math
\boxed{\text{Use Özkan–Pang (5.8): retain printed }L^{ij},\varphi^i;
\ \text{derive the omitted fermions in }E_a,N\text{ through (2.18).}}
\tag{14}
```

The L/varphi transformation checks and singlet E/N extraction are given in
[the component derivation](../../../derivations/fermionic-map.md);
the box states that construction prescription, not an all-order completeness claim.

## 7. Convention Dependence and Remaining Uncertainties

No external convention conversion is inserted into this extraction. Native OP source
expressions are preserved; the [working conventions](../../../derivations/component_conventions.md)
identify the source-to-component corrections. Hats, explicit fermions and implicit
fermions inside supercovariant objects must be tracked separately.

The source does not print explicit remainder markers on L or varphi, but
does on E and N. This establishes what is displayed; it does not prove
the full nonlinear correctness of every printed slot. The linked component
derivation supplies the variation and singlet extraction, with its stated
limitations on independent multiplet laws.

The ungauged map (2.9)–(2.10), the defining-vector map (5.16), later BF
insertion, Poincare gauge fixing, action normalization and spectrum remain
separate stages. No new completion, action, background or mass is delivered
in the present extraction.

## Q-variation status, 2026-09-17

The original formulas above remain literal source records. Notebook Part II
now derives Q(L) and finds phi_Q=phi_printed-(8/3)(gamma.T)(T.R(Q)).
Ten of the eleven printed coefficients match; the T²R(Q) coefficient is8/3
from the locked laws rather than the printed16/3. See master M07/X12 and
the notebook Q54–Q64. This comparison is a FAIL for literal M02 matching,
not a completed verification of the linear multiplet.

## Working-spinor adoption — 2026-09-18
