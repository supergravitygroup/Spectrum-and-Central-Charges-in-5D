# Direct source audit of the two bosonic LOG coefficient claims

<!-- LOG_CURRENT_CERTIFICATION_20260925 -->

**Current scope:** [the 2026-09-25 certificate](../CERTIFICATION_LOG_TWO_FERMI_2026-09-25.md) verifies the full primary and the component action through two physical fermions. The source comparisons and restricted tests below retain their stated mathematical scope.

The calculation compares the two coefficient statements below.
The source is the unchanged local C24 arXiv:2311.00679v1 combined PDF.
This is a bosonic source-consistency check, not a new full-invariant certificate.

## Problem and Target

Check (i) the explicit scalar-descendant $`w^{ab}w_{ab}D`$ coefficient and
(ii) the coefficient of $`R^{\rm S}_{abcd}w^{ab}w^{cd}`$ in the degauged bosonic
action. Do not infer either coefficient from an AdS spectrum or fit it to G25.

The following original pages were inspected visually:

| Source location | Saved original page | Relevant content |
|---|---|---|
| C24 (4.8b), printed33 / PDF34 | [C24-p034](https://arxiv.org/abs/2311.00679) | Descendant first line prints $`+368w^2D/3`$ |
| Supplement (1.2b), printed4 / PDF103 | [C24-p103](https://arxiv.org/abs/2311.00679) | $`D=-3Y\vert/128`$ |
| Supplement §2.2.2, printed14 / PDF113 | [C24-p113](https://arxiv.org/abs/2311.00679) | Raw $`F_{\log}`$ starts with $`3Y^2/2048+69W^{ab}W_{ab}Y/1024`$ |
| C24 (2.21)–(2.24), printed13 / PDF14 | [C24-p014](https://arxiv.org/abs/2311.00679) | Degauged commutator and Ricci definitions |
| Supplement §3.1, printed51 / PDF150 | [C24-p150](https://arxiv.org/abs/2311.00679) | All raw pure-$`w`$ terms used in the curvature check |
| C24 (5.20), printed44 / PDF45 | [C24-p045](https://arxiv.org/abs/2311.00679) | Canonical action: $`+23w^2D/8`$ already present, but common $`1/4`$ for $`RFF`$ and $`Rww`$ |

PDF45 and PDF150 were added to the local audit cache because this check needed
the uncached canonical-action page and the continuation of supplement §3.1.
The main 159-page cache is unchanged. Image and source hashes are recorded in
[checks.json](../../../../../../../references/source_evidence/log/results/gauged_full_fermionic_log/sources/correction_audit/checks.json).

## Convention Ledger

- Five dimensions, mostly-plus metric, $`a,b,c,d=0,\ldots,4`$.
- Fermion number zero, exact off shell. No auxiliary equation, metric field
  equation, AdS background, or supersymmetric-vacuum condition is used.
- The scalar vector compensator is fixed to $`W=1`$ only for the degauged-action
  comparison, as in source (5.20) and supplement §3.1.
- Lower-case $`w_{ab}:=W_{ab}\vert`$ is the independent Standard-Weyl two-form.
  It is not the scalar $`W`$, not the graviphoton strength $`F_{ab}`$, and not
  the final Gold-frame $`T_{ab}`$. Other matter fields are set to zero only
  to isolate this polynomial sector, not by their equations of motion.
- $`D`$ is the auxiliary scalar; $`\mathcal D_a`$ is the degauged covariant
  derivative. At this bosonic stage it is torsion-free and metric-compatible
  on the R-symmetry-singlet $`w_{ab}`$. The Lorentz generator has its usual
  tensor action, with unit-strength antisymmetrization.
- C24 (2.21) gives

```math
[\mathcal D_a,\mathcal D_b]w_{cd}
=-R^{\rm S}_{ab c}{}^e w_{ed}-R^{\rm S}_{ab d}{}^e w_{ce},
\qquad R^{\rm S}_{ab}=g^{cd}R^{\rm S}_{acbd}.
```

- The Riemann tensor is antisymmetric in each pair, symmetric under pair
  exchange, and obeys $`R^{\rm S}_{abcd}+R^{\rm S}_{acdb}+R^{\rm S}_{adbc}=0`$.
- The scalar projection is $`D=-3Y\vert/128`$; the Standard-Weyl BF density
  has the overall minus sign in S23 (3.2), including $`-WF_{\log}`$.
- All boundary terms are retained below. Integrated-action equality uses
  vanishing normal flux of the displayed current. No boundary condition is
  needed for the exact local identity containing that divergence.
- Gamma, epsilon, and fermion-ordering rules do not enter this restricted
  tensor calculation. They are not being changed or independently checked here.

## Definitions and Required Identities

For compactness in the curvature calculation only, define the five contractions

```math
\begin{aligned}
J&=R^{\rm S}_{abcd}w^{ab}w^{cd},&
K&=R^{\rm S}_{ab}w^{ac}w^b{}_c,\\
\mathcal N&=(\mathcal D_cw_{ab})(\mathcal D^cw^{ab}),\\
P&=(\mathcal D^cw^a{}_b)(\mathcal D^bw_{ac}),&
Q&=(\mathcal D^bw^a{}_b)(\mathcal D^cw_{ac}).
\end{aligned}
```

The algebraic Bianchi identity contracted with $`w^{ab}w^{cd}`$ gives

```math
0=J-I_2-I_2,\qquad
I_2:=R^{\rm S}_{acbd}w^{ab}w^{cd}=\frac12J.
```

The second equality uses the antisymmetry of the last Riemann pair for the
second term, and $`c\leftrightarrow d`$ followed by $`w^{dc}=-w^{cd}`$ for the
third. Relabeling $`b\leftrightarrow c`$ shows that the raw contraction
$`R^{\rm S}_{abcd}w^{ac}w^{bd}`$ is precisely $`I_2`$.

## Detailed Derivation

### A. Scalar-descendant projection

The raw source supplies the terms

```math
F_{\log}\supset
\frac3{2048}Y^2+\frac{69}{1024}W^{ab}W_{ab}Y
-\frac3{32}\nabla^a\nabla_aY.
```

Solving the defining projection once gives $`Y\vert=-128D/3`$. Therefore

```math
\begin{aligned}
\frac{69}{1024}W^{ab}W_{ab}Y\Big|&=
\frac{69}{1024}\left(-\frac{128}{3}\right)w^{ab}w_{ab}D
=-\frac{23}{8}w^{ab}w_{ab}D,\\
\frac3{2048}Y^2\Big|&=
\frac3{2048}\left(-\frac{128}{3}\right)^2D^2=\frac83D^2,\\
-\frac3{32}\nabla^a\nabla_aY\Big|&=
\left(-\frac3{32}\right)\left(-\frac{128}{3}\right)
\Box D=4\Box D.
\end{aligned}
```

The last two coefficients agree with the same first line of C24 (4.8b);
the displayed $`+368w^2D/3`$ does not. Numerically,

```math
\left(-\frac{23}{8}\right)\left(-\frac{128}{3}\right)
=\frac{368}{3}.
```

Thus the discrepant number is exactly what a second Y-to-D substitution
would produce. This identifies a possible mechanism, not a verified account
of how the authors obtained their printed number.

At $`W=1`$, the BF term $`-WF_{\log}`$ reverses the sign:

```math
-F_{\log}\supset+\frac{23}{8}w^{ab}w_{ab}D.
```

**Important:** C24 (5.20) already contains
$`D(16w^{ab}F_{ab}-8F^{ab}F_{ab}+23w^{ab}w_{ab}+24X^{ij}X_{ij})/8`$.
Consequently this is a discrepancy in the earlier displayed descendant
(4.8b), not an instruction to add a further $`23w^2D/8`$ to (5.20) or G25 (11).

### B. Raw quadratic two-form sector

The original supplement PDF150 contains the following sector, with all its
second derivatives in their printed order:

```math
\begin{aligned}
\ell_{w,\mathrm{raw}}={}&
\frac13J+\frac13R^{\rm S}_{abcd}w^{ac}w^{bd}
-\frac23K-\frac13K-\frac{27}{256}R^{\rm S}w^{ab}w_{ab}\\
&-\frac{39}{16}w^{ab}\mathcal D_c\mathcal D^cw_{ab}
+\frac12(\mathcal D^b\mathcal D^cw^a{}_b)w_{ac}
-2(\mathcal D^c\mathcal D^bw^a{}_b)w_{ac}\\
&-\frac{33}{16}\mathcal N-\frac94Q+\frac34P.
\end{aligned}
```

The explicit curvature terms give
$`J/3+J/6-K=J/2-K`$. The three integrations by parts, keeping their currents,
are

```math
\begin{aligned}
-\frac{39}{16}w^{ab}\mathcal D_c\mathcal D^cw_{ab}
&=\frac{39}{16}\mathcal N
-\frac{39}{16}\mathcal D_c(w^{ab}\mathcal D^cw_{ab}),\\
\frac12(\mathcal D^b\mathcal D^cw^a{}_b)w_{ac}
&=-\frac12P+\frac12\mathcal D^b[(\mathcal D^cw^a{}_b)w_{ac}],\\
-2(\mathcal D^c\mathcal D^bw^a{}_b)w_{ac}
&=2Q-2\mathcal D^c[(\mathcal D^bw^a{}_b)w_{ac}].
\end{aligned}
```

Ignoring only those explicitly displayed divergences temporarily, the first
derivative terms collect as

```math
\left(\frac{39}{16}-\frac{33}{16}\right)\mathcal N
+\left(-\frac12+\frac34\right)P
+\left(2-\frac94\right)Q
=\frac38\mathcal N+\frac14(P-Q).
```

### C. Curvature commutator and the missing eighth

Apply the product rule twice without discarding its boundary terms:

```math
\begin{aligned}
P-Q={}&\mathcal D_c(w^a{}_b\mathcal D^bw_a{}^c)
-\mathcal D_b(w^{ab}\mathcal D^cw_{ac})\\
&-w^a{}_b[\mathcal D^c,\mathcal D^b]w_{ac}.
\end{aligned}
```

Inserting the tensor commutator from the convention ledger gives

```math
\begin{aligned}
-w^a{}_b[\mathcal D^c,\mathcal D^b]w_{ac}
&=w^a{}_bR^{\rm S\,cb}{}_{a}{}^d w_{dc}
+w^a{}_bR^{\rm S\,cb}{}_{c}{}^d w_{ad}\\
&=-\frac12J+K.
\end{aligned}
```

For the first contraction, pair symmetries and the contracted algebraic
Bianchi identity above give $`-J/2`$. For the second, contraction of the first
and third Riemann slots gives the declared Ricci tensor and hence $`K`$.
These two index contractions were also checked directly with generated
algebraic curvature tensors in both Lorentzian and Euclidean signatures;
the checker does not assume this reduced identity.

Consequently, modulo the stated currents,

```math
\begin{aligned}
\ell_{w,\mathrm{raw}}
&\simeq_{\partial}\frac12J-K-\frac{27}{256}R^{\rm S}w^2
+\frac38\mathcal N+\frac14\left(K-\frac12J\right)\\
&=\frac38J-\frac34K-\frac{27}{256}R^{\rm S}w^2
+\frac38\mathcal N.
\end{aligned}
```

The decisive coefficient is $`1/2-1/8=3/8`$. Finally,
$`\mathcal N=\mathcal D_m(w^{ab}\mathcal D^mw_{ab}) -w^{ab}\mathcal D^2w_{ab}`$ gives the exact local statement

```math
\begin{aligned}
\ell_{w,\mathrm{raw}}={}&
\frac38R^{\rm S}_{abcd}w^{ab}w^{cd}
-\frac34R^{\rm S}_{ab}w^{ac}w^b{}_c
-\frac{27}{256}R^{\rm S}w^{ab}w_{ab}
-\frac38w^{ab}\mathcal D^2w_{ab}
+\mathcal D_m\mathcal J^m,\\
\mathcal J^m={}&-\frac{33}{16}w^{ab}\mathcal D^mw_{ab}
+\frac34w_{ac}\mathcal D^cw^{am}
-\frac94w_a{}^m\mathcal D_bw^{ab}.
\end{aligned}
```

C24 (5.20) has the same Ricci, scalar-curvature and Laplacian coefficients
but $`J/4`$ in place of $`3J/8`$. Its difference from this raw-source reduction is
$`J/8`$ after accounting for the displayed current. This is a discrepancy
between two expressions in C24; the source-complete raw expression remains
an input, not something newly derived from six superspace derivatives here.

The independent $`RFF`$ contraction stays $`1/4`$:

```math
\frac13R^{\rm S}_{abcd}F^{ab}F^{cd}
-\frac16R^{\rm S}_{acbd}F^{ab}F^{cd}
=\left(\frac13-\frac1{12}\right)R^{\rm S}_{abcd}F^{ab}F^{cd}.
```

## Consistency Checks

[verify_two_bosonic_corrections.py](../../../../../../../references/source_evidence/log/results/gauged_full_fermionic_log/scripts/verify_two_bosonic_corrections.py)
and its [saved output](../../../../../../../references/source_evidence/log/results/gauged_full_fermionic_log/sources/correction_audit/checks.json) check:

1. Exact rational Y/D arithmetic, including the consistent neighboring
   $`8D^2/3`$ and $`4\Box D`$ coefficients, and the $`-1/18`$ Gold-frame map below.
2. Algebraic Riemann symmetries and first Bianchi identity, constructed from
   independent symmetric tensors; $`2R_{abcd}w^{ac}w^{bd}=J`$.
3. Antisymmetric two-form values and arbitrary first covariant derivatives.
   Second derivative data obey the source tensor commutator by construction.
4. Direct evaluation of the contracted commutator, rather than assuming
   $`P-Q\simeq_{\partial}K-J/2`$.
5. The pointwise identity
   $`\ell_{\rm raw}-\ell_{3/8}-\mathcal D_m\mathcal J^m=0`$
   in 24 exact-arithmetic tensor-jet cases across two metric signatures.
   Replacing $`3/8`$ by $`1/4`$ leaves exactly $`J/8`$, nonzero in the test cases.
6. All free indices are contracted. With $`[\mathcal D]=[w]=1`$ and
   $`[R]=[D]=[Y]=2`$, every compared density term has dimension four;
   $`\mathcal J^m`$ has dimension three.
7. In flat curvature the coefficient discrepancy vanishes; for $`w=0`$ both
   discrepancies vanish. Neither test licenses discarding the terms for
   generic off-shell fields. The algebraic source comparison uses no EOM.


## Final Result

The source-consistent explicit scalar projection is

```math
\boxed{F_{\log}\supset-\frac{23}{8}w^{ab}w_{ab}D.}
```

The raw supplement reduces, with the displayed boundary current, to

```math
\boxed{\ell_{\rm LOG}^{\rm S}\supset
\frac14R^{\rm S}_{abcd}F^{ab}F^{cd}
+\frac38R^{\rm S}_{abcd}w^{ab}w^{cd}.}
```

For the project bosonic bridge $`R^{\rm S}=-R^{\rm G}`$ and
$`w^{ab}=2(G^{ab}-2H^{ab})/3`$, the *change from the old $`1/4`$ ledger* is

```math
\delta\ell_{\rm LOG}
=\frac18R^{\rm S}_{abcd}w^{ab}w^{cd}
=-\frac1{18}R^{\rm G}_{abcd}
(G^{ab}-2H^{ab})(G^{cd}-2H^{cd}).
```

It is already included in the existing corrected result. It must not be
appended again to that result or treated as a separately established
additive correction to G25 (11).

## Convention Dependence and Scope

- **Certain arithmetic/source mismatch:** the printed descendant (4.8b)
  disagrees with the raw $`69Yw^2/1024`$ term and the defining projection.
  The later action (5.20) already uses the consistent $`+23w^2D/8`$ coefficient.
- **High confidence in the conditional curvature result:** using the raw
  supplement and source commutator, $`3/8`$ follows with explicit boundary
  accounting. Both the hand reduction and an independent tensor-jet check
  establish the mismatch with the printed $`1/4`$ representative.
- This source comparison takes the raw supplement as input. The separate
  [bosonic certificate](../sources/certification_20260925/bosonic/EXACT_BOSONIC_COMPARISON.md)
  reconstructs the sector from the calculated primary and descendants, with
  the boundary current explicit.
- The doubled-projection explanation for $`368/3`$ is an inference from its
  numerical value; no claim is made about the authors' actual workflow.
- No author-confirmed erratum is asserted. These are local source-consistency
  findings, distinct from the separately derived gauged $`E^a`$ omissions.

