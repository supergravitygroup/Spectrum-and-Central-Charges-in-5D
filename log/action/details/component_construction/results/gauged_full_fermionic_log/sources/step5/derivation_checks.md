## 5. Consistency Checks

### 5.1 Weights, index balance, parity and the truncation

The weights follow from the source definitions:

```math
w(H^{ij})=3,\qquad w(\nabla_\alpha^i)=\frac12,\qquad
w(\varphi_\alpha^i)=\frac72,\qquad w(\mathcal H^a)=4.
\tag{S5-C01}
```

Each retained term has one upper free Lorentz index $`a`$, no free spinor or doublet indices, and every dummy index paired once up and once down. Each has even parity and explicit degree zero or two. These tests run on the full derived polynomial and its index-raised display form. They also compare truncating after the full second derivative against retaining the first derivative through cubic degree and then differentiating. No boundary or on-shell equivalence is used.

For explicit examples of the weight check,

```math
w(W^{a}{}_{b}\nabla^bY)=1+1+2=4,\qquad
w(W^{-5}X^{ij}F_{bc}F_{de}\lambda\lambda)=-5+2+2+2+\frac32+\frac32=4.
\tag{S5-C02}
```

The second example checks the engineering of a possible retained field structure, not a claim that its uncontracted product alone is a vector. The actual contractions are all displayed in §7. No nonzero odd-degree term occurs in the vector endpoint. The count of written contributions is not a count of independent tensor structures: some reduce or cancel under further Clifford or tensor identities.

### 5.2 Independent eight-derivative check and the spinor/scalar link

The first comparison starts afresh with the original projector S23 (3.24), computes its six spinor derivatives, and then applies the **ordered** two derivatives and gamma trace of (S5-V02). It uses the original exterior-algebra projector implementation, not the new vector endpoint as an input. All eight gaugino components are independent Grassmann generators. The flat verification jets retain arbitrary constant $`F_{ab}`$, $`X^{ij}`$ and $`v_a=\partial_aW`$; other independent vector jets and the Weyl multiplet are zero. Only after eight differentiations are degrees zero and two selected.

Seven assignments (pure $`X`$, pure $`F`$, pure $`v`$, mixed $`F,X,v`$, and three integer probes) agree. A separate probe checks the index-raising operations used by the displayed expression. The largest reported residual is zero in this finite-matrix calculation. The report records the actual number of compared coefficients in each probe: [checks.json](../../../../../../../../references/source_evidence/log/results/gauged_full_fermionic_log/sources/step5/checks.json). These checks cover restricted jets, not arbitrary curved configurations.

The entire **uncontracted** spinor derivative is also compared with the actual previous scalar and new vector:

```math
\left[\nabla_\zeta^t\varphi_\eta^i\right]_{\le2}
=\left[-\frac i2\varepsilon^{ti}\varepsilon_{\zeta\eta}F_{\log W}
+\frac i2\varepsilon^{ti}(\Gamma^b)_{\zeta\eta}\mathcal H_{\log W\,b}
+i(\Gamma^b)_{\zeta\eta}\nabla_bH_{\log W}^{ti}\right]_{\le2}.
\tag{S5-C03}
```

Here $`[\ ]_{\le2}`$ only denotes selection of explicit fermion degree at the end; it is not a new physical field or an unevaluated operation in the final result. In the stated flat mixed probe, all $`4\times2\times4\times2=64`$ free-index components, comprising 1,856 pole/Grassmann coefficients, agree with zero residual. The first side is differentiated directly from our spinor; the second uses the separately stored scalar polynomial and vector polynomial. See [multiplet_checks.json](../../../../../../../../references/source_evidence/log/results/gauged_full_fermionic_log/sources/step5/multiplet_checks.json).

With the same constant jets, the ordinary derivative acts only on the remaining scalar powers. For each displayed term $`W^{-n}A^a`$ on this slice, it gives

```math
\partial_a(W^{-n}A^a)=-nW^{-n-1}v_aA^a,\qquad
\partial_a\mathcal H^a_{\log W}\big|_{\rm flat\ constant\ jets}=0
\quad\text{through degree two}.
\tag{S5-C04}
```

The coefficient of every independent Grassmann monomial and every scalar pole vanishes in the same eight probes. This verifies conservation on those jets; it is not substituted for the general superconformal constraint.

### 5.3 A curved source comparison, with the separate primary contributions

The first two terms in C24 supplement §2.2.3, [Components of curvature-squared invariants of minimal supergravity in five dimensions — PDF121](https://arxiv.org/abs/2311.00679), have the structures $`W^{a}{}_{b}\nabla^bY`$ and $`Y\nabla_bW^{ab}`$. We extract these field monomials **after** the full differentiation. All mixed curvatures in this extraction are substituted by the definitions in §3; terms with other field content are separated, not set to zero before a derivative.

Take a unit spatial two-form slot $`W_{12}=-W_{21}=1`$. For the first structure take $`(\nabla_2Y)=1`$; for the second take $`Y=1`$ and $`\nabla_2W_{12}=-\nabla_2W_{21}=1`$. The $`a=1`$ component of the selected tensor is then one. Substitution of the source Clifford matrices and explicit spinor/doublet metrics gives these separate contributions:

| Origin in our calculated primary | $`W^{a}{}_{b}\nabla^bY`$ | $`Y\nabla_bW^{ab}`$ |
|---|---:|---:|
| H0.1 | $`3/32`$ | $`0`$ |
| H0.2 | $`0`$ | $`51/256`$ |
| H1.1 | $`0`$ | $`-27/64`$ |
| H1.3 | $`3/16`$ | $`27/256`$ |
| H1.6 | $`0`$ | $`27/128`$ |
| H1.7 | $`-3/16`$ | $`0`$ |

The individual evaluated contractions behind this table are displayed immediately below. They preserve the original field expression on the left and show the matrix contraction on the right; a zero is an evaluated contraction, not a dropped source term. In these rows the vertical bar selects the stated field monomial and probe, and the remaining free vector is $`\delta^a{}_1`$.

<!-- WY_CONTRACTIONS -->

Adding the displayed coefficients gives

```math
\begin{aligned}
\frac3{32}+\frac3{16}-\frac3{16}&=\frac3{32},\qquad
\frac{51}{256}-\frac{27}{64}+\frac{27}{256}+\frac{27}{128}
=\frac{51-108+27+54}{256}=\frac3{32},\\
\mathcal H^a_{\log W}\big|_{W\nabla Y,\,Y\nabla W}
&=\frac3{32}W^{a}{}_{b}\nabla^bY+\frac3{32}Y\nabla_bW^{ab}.
\end{aligned}
\tag{S5-C05}
```

Both coefficients agree with the inspected source. The calculation is repeated on all ten antisymmetric two-form planes, including time-like planes; raising the two Lorentz indices supplies the required $`\eta^{aa}\eta^{bb}`$ signs. These twenty checks use a $`10^{-10}`$ absolute tolerance, with no fitting to the expected coefficient. Evidence: [wY_checks.json](../../../../../../../../references/source_evidence/log/results/gauged_full_fermionic_log/sources/step5/wY_checks.json). These two structures do not certify the other terms in the 29-page published vector.

### 5.4 The full component constraint and why an ordinary divergence is insufficient

For a certified primary linear multiplet, C24 (2.43) imposes the superspace constraint $`\nabla_a\mathcal H^a=0`$. Its component version is C24 (2.51), with the **full** projected derivative. Write $`D_a^{G,\mathrm{LUD}}`$ for the Lorentz/SU(2)/dilatation derivative used in C24 (2.53), not the full $`\nabla_a`$. The spinorial connections in C24 (2.16) act as

```math
\nabla_a\mathcal H_b
=D_a^{G,\mathrm{LUD}}\mathcal H_b
-\frac12\psi_a{}^{\alpha i}\nabla_{\alpha i}\mathcal H_b
-\frac12\phi_a{}^{\alpha i}S_{\alpha i}\mathcal H_b,
\tag{S5-C06}
```

where the $`K`$ term vanishes for a $`K`$-primary vector. Insert the generic source transformations C24 (2.41d), (2.44):

```math
\begin{aligned}
\nabla_\alpha^i\mathcal H_b
&=4(\Sigma_{bc})_\alpha{}^\beta\nabla^c\varphi_\beta^i
-\frac32(\Gamma_b)_\alpha{}^\beta W_{\beta\gamma}\varphi^{\gamma i}
-\frac12(\Gamma_b)_\gamma{}^\beta W_{\beta\alpha}\varphi^{\gamma i},\\
S_\alpha^i\mathcal H_b&=-8i(\Gamma_b)_\alpha{}^\beta\varphi_\beta^i.
\end{aligned}
\tag{S5-C07}
```

The connection coefficients are $`(-1/2)4=-2`$, $`(-1/2)(-3/2)=3/4`$, $`(-1/2)(-1/2)=1/4`$ and $`(-1/2)(-8i)=4i`$. Raising/lowering the spinor contractions in source order yields precisely C24 (2.53d), [Components of curvature-squared invariants of minimal supergravity in five dimensions — PDF23](https://arxiv.org/abs/2311.00679):

```math
\begin{aligned}
\nabla_a\mathcal H_b
={}&D_a^{G,\mathrm{LUD}}\mathcal H_b-2(\Sigma_{bc}\psi_{ai})_\alpha\nabla^c\varphi^{i\alpha}
+\frac34(\Gamma_b\psi_{ai})_\alpha W^{\alpha\beta}\varphi_\beta^i\\
&+\frac14\psi_{ai}^{\beta}W_{\alpha\beta}(\Gamma_b\varphi^i)^\alpha
+4i(\Gamma_b\phi_{ai})_\alpha\varphi^{i\alpha}.
\end{aligned}
\tag{S5-C08}
```

Contract the displayed indices with $`\eta^{ab}`$. The required component equation is therefore

```math
\begin{aligned}
0={}&D_a^{G,\mathrm{LUD}}\mathcal H^a-2(\Sigma^{a}{}_{c}\psi_{ai})_\alpha\nabla^c\varphi^{i\alpha}
+\frac34(\Gamma^a\psi_{ai})_\alpha W^{\alpha\beta}\varphi_\beta^i\\
&+\frac14\psi_{ai}^{\beta}W_{\alpha\beta}(\Gamma^a\varphi^i)^\alpha
+4i(\Gamma^a\phi_{ai})_\alpha\varphi^{i\alpha}.
\end{aligned}
\tag{S5-C09}
```

This is the source-frame expansion of the full constraint. The label $`\mathrm{LUD}`$ means Lorentz/SU(2)/dilatation connection content, not fermion order. The reduced derivative alone omits the explicitly displayed Q/S connections; the full projected $`\nabla_a`$ transports to the project's full $`\mathcal D_a`$. Thus $`\mathcal D_aE_{\log}^a=0`$ is precisely the active full-supercovariant constraint. Do not add the separate connection terms in (S5-C09) to that full operator a second time. The actual LOG constraint is now certified from full-primary linearity and the closed-four-form identity with the full R(Q) gamma trace, as detailed in the current certificate. The original flat check (S5-C04) remains a separate restricted test.

### 5.5 Transformations linking the four fields: what has and has not been checked

Besides (S5-V03), the remaining source relations are C24 (2.41a,c):

```math
\begin{aligned}
\nabla_\alpha^iH^{jk}&=2\varepsilon^{i(j}\varphi_\alpha^{k)},\\
\nabla_\alpha^iF&=-2\nabla_\alpha{}^\beta\varphi_\beta^i
-3W_{\alpha\beta}\varphi^{\beta i}-\frac32X_{\alpha j}H^{ij}.
\end{aligned}
\tag{S5-C10}
```

Here $`\nabla_\alpha{}^\beta=(\Gamma^a)_\alpha{}^\beta\nabla_a`$. Together with (S5-C07), these display the complete generic derivative chain connecting the triplet, spinor, scalar and vector. C24 (2.44) adds

```math
S_\alpha^i\varphi_\beta^j=-6\varepsilon_{\alpha\beta}H^{ij},\qquad
S_\alpha^iF=6i\varphi_\alpha^i,\qquad
K_a(\varphi,F,\mathcal H_b)=0.
\tag{S5-C11}
```

The explicit test performed in this step is (S5-C03) on the stated jets. The general curved forms of (S5-C07), (S5-C10), (S5-C11), the reality condition and their component Q/S transformations have **not** been independently checked on all 52,689 contributions. Source laws are recorded as the acceptance conditions, not relabeled as accomplished checks. The later full-primary and retained-component certificates close the relevant gates through the stated theorem and exact algebra checks.

There is also a fermion-order limitation: varying an omitted four-fermion term can produce a three-fermion term. Thus a vector displayed only through degree two can be used for a consistent Q-variation check through degree one; it cannot alone establish the full cubic-fermion transformation law. The higher-order remainder must be restored for that test.

### 5.6 The potential discrepancy, retained with its exact diagnostic

This issue concerns the later component/potential bridge, not the gamma trace (S5-V02). The detailed previous calculation is [note 07, §9](../../notes/07_step1_linear_bridge_independent_check.md). In the **project component frame only**, the locked current relation and potential definition are

```math
P^a=E^a+\frac i2\bar\psi_b\gamma^{ba}\varphi+\frac14\bar\psi_b^i\gamma^{abc}\psi_c^jL_{ij},\qquad
P^a=-\frac1{12}\epsilon_B^{abcde}\partial_bE_{cde}.
\tag{S5-C12}
```

At a local frame point, parameterize the potential variation by

```math
\delta E_{cde}=\alpha\bar\epsilon\gamma_{cde}\varphi
+\beta i\bar\psi_{[c}^{i}\gamma_{de]}\epsilon^jL_{ij}+3\partial_{[c}\Lambda_{de]}.
\tag{S5-C13}
```

Use the locked five-dimensional identities $`\epsilon_B^{abcde}\gamma_{cde}=6i\gamma^{ab}`$ and $`\epsilon_B^{abcde}\gamma_{de}=2i\gamma^{abc}`$, the fixed-upper-index odd-spinor flip $`\bar\zeta^i\gamma^{abc}\vartheta^j=-\bar\vartheta^j\gamma^{abc}\zeta^i`$, and $`\delta\psi_b|_{\partial\epsilon}=\partial_b\epsilon`$. The terms proportional to the derivative of the local parameter are

```math
\begin{aligned}
\delta P^a\big|_{\partial\epsilon}
&=-\frac{\alpha i}{2}(\partial_b\bar\epsilon)\gamma^{ab}\varphi
-\frac\beta6(\partial_b\bar\epsilon^i)\gamma^{abc}\psi_c^jL_{ij},\\
\delta\!\left(\frac i2\bar\psi_b\gamma^{ba}\varphi\right)\big|_{\partial\epsilon}
&=-\frac i2(\partial_b\bar\epsilon)\gamma^{ab}\varphi,\\
\delta\!\left(\frac14\bar\psi_b^i\gamma^{abc}\psi_c^jL_{ij}\right)\big|_{\partial\epsilon}
&=\frac14\left[(\partial_b\bar\epsilon^i)\gamma^{abc}\psi_c^j
- (\partial_c\bar\epsilon^j)\gamma^{abc}\psi_b^i\right]L_{ij}
=\frac12(\partial_b\bar\epsilon^i)\gamma^{abc}\psi_c^jL_{ij}.
\end{aligned}
\tag{S5-C14}
```

The last equality interchanges the dummy pairs $`b,c`$ and $`i,j`$ in the second summand, uses $`\gamma^{acb}=-\gamma^{abc}`$ and $`L_{ji}=L_{ij}`$. Subtract the last two rows from the first, as prescribed by (S5-C12):

```math
\delta E^a\big|_{\partial\epsilon}
=-\frac{i(\alpha-1)}2(\partial_b\bar\epsilon)\gamma^{ab}\varphi
-\frac{\beta+3}{6}(\partial_b\bar\epsilon^i)\gamma^{abc}\psi_c^jL_{ij}.
\tag{S5-C15}
```

Covariance fixes $`\alpha=1`$ and $`\beta=-3`$. These are the converted C24 (2.54) coefficients. Literal OP (2.24), $`\alpha=-1`$, $`\beta=1`$, fails this necessary test. The sign is not altered by the current two-fermion restriction: both diagnostic structures lie in its retained sector.

The separate literal C24 (2.50) formula converts to $`\mathcal H_G=h_G+Q_1-Q_2`$, whereas the required covariant vector is $`\mathcal H_G=h_G-Q_1-Q_2`$. Their difference is $`2Q_1`$ and the uncancelled principal-parameter variation is $`2\delta Q_1`$. The earlier plus-$`Q_2`$ conversion lowered the second spinor index on the wrong side; the indexed matrix is $`-MC`$. The [complete superform proof](../../../../../../../../references/source_evidence/log/derivations/form-interface.md) now derives the full potential/current relation and resolves FORM-01. The local-parameter test above remains a necessary diagnostic, rather than being promoted to that complete proof. Literal source transcriptions remain distinct from the derived repair.

## 6. Convention Dependence and Remaining Uncertainties

The explicit descent and checks have the following component scope:

- The expression is in Gold superspace, with source torsions/curvatures and full ordered vector derivatives. Neither bar projection nor conversion to the project component frame is applied to the endpoint.
- The expansion uses its displayed covariant basis. The curved source comparison evaluates the two $`W`$–$`Y`$ sectors against C24 supplement §2.2.3.
- Full-primary S/K/linearity and retained-order reality, component constraint and BF transformations are now certified independently. The proof uses the verified full primary and complete superform identities; the flat checks alone do not establish them.
- The full superform pullback now resolves FORM-01 and establishes the potential/current law; the principal test here is a separate diagnostic. Literal formulas and derived source repairs remain explicitly distinguished.
- The final $`+\text{high fermi term}`$ denotes explicit degree four and higher. It does not justify dropping the cubic spinor or quartic primary during differentiation, or using this truncation for a full cubic-fermion SUSY check.

The reusable verification scripts are [verify_log_step5_vector.py](../../../../../../../../references/source_evidence/log/results/gauged_full_fermionic_log/scripts/verify_log_step5_vector.py), [verify_log_step5_multiplet.py](../../../../../../../../references/source_evidence/log/results/gauged_full_fermionic_log/scripts/verify_log_step5_multiplet.py) and [verify_log_step5_wY.py](../../../../../../../../references/source_evidence/log/results/gauged_full_fermionic_log/scripts/verify_log_step5_wY.py). The source and result hashes, input coverage and final display locations are recorded in [sources/step5](../../../../EXTERNAL_REFERENCES.md#ref-addf133bd7cd).

