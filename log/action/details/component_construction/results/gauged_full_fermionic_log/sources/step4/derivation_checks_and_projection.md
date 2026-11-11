## 5. Two explicit coefficient calculations

### 5.1 Highest, eight-gaugino term

Only the two $`W^{-6}\lambda^6`$ inputs can produce $`W^{-8}\lambda^8`$. All terms from differentiating a numerator have a lower explicit inverse power. Consequently the first term of (S4-09), with $`n=6`$, gives the entire highest sector:

```math
\begin{aligned}
F_{\log W}\big|_{W^{-8}}
={}&-\frac{21}{64}W^{-8}\varepsilon^{\eta\zeta}\varepsilon_{ti}\varepsilon_{jr}
\lambda_\zeta^t\lambda_\eta^r\lambda^{\alpha i}\lambda_\alpha^j
\lambda^{\beta k}\lambda_\beta^l\lambda_k^\gamma\lambda_{\gamma l}\\
&-\frac{21}{32}W^{-8}\varepsilon^{\eta\zeta}\varepsilon_{ti}\varepsilon_{jr}
\lambda_\zeta^t\lambda_\eta^r\lambda^{\alpha i}\lambda_\alpha^k
\lambda^{\beta j}\lambda_\beta^l\lambda_k^\gamma\lambda_{\gamma l}.
\end{aligned}
\tag{S4-20}
```

The coefficients, including the scalar trace, are

```math
\left(-\frac i{12}\right)(-6\cdot7)\left(\frac{3i}{32}\right)=-\frac{21}{64},\qquad
\left(-\frac i{12}\right)(-6\cdot7)\left(\frac{3i}{16}\right)=-\frac{21}{32}.
\tag{S4-21}
```

The new gaugino $`\lambda_\zeta^t`$ is leftmost because the second derivative acts from the left. No permutation of it through the other seven factors is implicit. Contracting the displayed epsilons with eight independent exterior generators in the order $`(\lambda_1^1,\lambda_1^2,\lambda_2^1,\lambda_2^2,\lambda_3^1,\lambda_3^2,\lambda_4^1,\lambda_4^2)`$ gives $`315W^{-8}\lambda_1^1\lambda_1^2\lambda_2^1\lambda_2^2\lambda_3^1\lambda_3^2\lambda_4^1\lambda_4^2`$. This component-basis contraction is an additional sign check, not a replacement of the covariant formula.

### 5.2 Reconstructing the disputed $`W^{ab}W_{ab}Y`$ coefficient

This sector is extracted **after both spinor derivatives**, from the primary-derived calculation. Setting fermions to zero before differentiation would remove some of its nonzero contributions. We select derivative-free monomials with one $`Y`$ and two Weyl two-forms, retaining contributions from the torsion and S-curvature definitions. This is coefficient extraction in the local expression, not an assertion that all the chosen jets form a supergravity solution.

A Lorentz scalar with these fields is proportional to $`W^{ab}W_{ab}Y`$: two antisymmetric two-forms exhaust four indices, so a five-index epsilon cannot give an additional scalar without another vector. Therefore its coefficient can be calculated exactly on $`W_{12}=t`$, $`W_{21}=-t`$, $`Y=y`$:

```math
W^{ab}W_{ab}Y=2t^2y.
\tag{S4-22}
```

For an explicit contraction, the following matrices realize the locked Clifford algebra. They are a calculation basis, not a new convention:

```math
\begin{aligned}
\varepsilon_{\alpha\beta}&=\begin{pmatrix}0&1&0&0\\-1&0&0&0\\0&0&0&-1\\0&0&1&0\end{pmatrix},\qquad
\varepsilon^{\alpha\beta}=-\varepsilon_{\alpha\beta},\qquad
\varepsilon^{ij}=\begin{pmatrix}0&1\\-1&0\end{pmatrix},\quad \varepsilon_{ij}=-\varepsilon^{ij},\\
\Gamma^0&=\mathop{\mathrm{diag}}\nolimits(1,1,-1,-1),\qquad
\Gamma^1=\begin{pmatrix}0&0&0&i\\0&0&i&0\\0&i&0&0\\i&0&0&0\end{pmatrix},\qquad
\Gamma^2=\begin{pmatrix}0&0&0&1\\0&0&-1&0\\0&1&0&0\\-1&0&0&0\end{pmatrix},\\
\Gamma^3&=\begin{pmatrix}0&0&i&0\\0&0&0&-i\\i&0&0&0\\0&-i&0&0\end{pmatrix},\qquad
\Gamma^4=\begin{pmatrix}0&0&1&0\\0&0&0&1\\-1&0&0&0\\0&-1&0&0\end{pmatrix}.
\end{aligned}
\tag{S4-23}
```

Here the displayed gamma matrices have one lower and one upper spinor index. The all-lower matrices are $`\Gamma^a_{\alpha\beta}=-(\Gamma^a)_\alpha{}^\gamma\varepsilon_{\gamma\beta}`$, and the same rule applies to $`\Sigma^{ab}`$. For example,

```math
\begin{aligned}
\Sigma^{12}&=-\tfrac12\Gamma^1\Gamma^2
=\tfrac i2\mathop{\mathrm{diag}}\nolimits(1,-1,1,-1),\\
W_{\alpha\beta}&=t(\Sigma^{12})_{\alpha\beta}
=\frac{it}{2}\begin{pmatrix}0&-1&0&0\\-1&0&0&0\\0&0&0&1\\0&0&1&0\end{pmatrix},\\
W^{\alpha\beta}W_{\alpha\beta}&=t^2,qquad
\mathop{\mathrm{tr}}\nolimits(W_\alpha{}^\beta W_\beta{}^\gamma)=-t^2,qquad
\varepsilon^{\alpha\beta}\varepsilon_{\beta\alpha}=4.
\end{aligned}
\tag{S4-24}
```

The next rows display **every surviving candidate contraction** from this sector, including those whose matrix contraction is zero. Each left-hand side already includes its coefficient and the scalar trace (S4-02). On the right the matrices of (S4-23)–(S4-24) have been inserted, each repeated spinor index summed from 1 to 4 and each SU(2) index from 1 to 2. This exposes the numerical contractions underlying the seven nonzero primary contributions.

<!-- W2Y_CONTRACTIONS_INSERT -->

Collect the nonzero contributions and restore $`2t^2y=W^{ab}W_{ab}Y`$:

| Calculated primary input | Contribution to $`F_{\log W}`$ |
|---|---|
| H0.1: $`-3iW_{ab}X^{abij}/8`$ | $`+(96/1024)W^{ab}W_{ab}Y`$ |
| H1.1: $`9W^{-1}X^{ij}Y/64`$ | $`-(279/1024)W^{ab}W_{ab}Y`$ |
| H1.3: $`-W^{-1}\Box X^{ij}/2`$ | $`+(93/1024)W^{ab}W_{ab}Y`$ |
| H1.4: $`-9W^{-1}X^{ij}W^{ab}W_{ab}/64`$ | $`-(27/1024)W^{ab}W_{ab}Y`$ |
| H1.6: $`-3W^{-1}(\Gamma^a)^{\alpha\beta}X_\alpha^{(i}\nabla_a\lambda_\beta^{j)}/4`$ | $`+(162/1024)W^{ab}W_{ab}Y`$ |
| H1.7: $`+3W^{-1}(\Gamma^a)^{\alpha\beta}\lambda_\alpha^{(i}\nabla_aX_\beta^{j)}/4`$ | $`-(24/1024)W^{ab}W_{ab}Y`$ |
| H2.8: $`+3iW^{-2}Y\lambda^{\alpha i}\lambda_\alpha^j/64`$ | $`+(48/1024)W^{ab}W_{ab}Y`$ |

Thus the coefficient derived from our primary and spinor is

```math
F_{\log W}\supset\frac{96-279+93-27+162-24+48}{1024}W^{ab}W_{ab}Y
=\frac{69}{1024}W^{ab}W_{ab}Y.
\tag{S4-25}
```

The independent contraction checks repeat this evaluation for all ten single two-form slots, including time-like slots, and three mixed integer two-forms. They also give $`3Y^2/2048`$. The report is [w2Y_checks.json](../../../../../../../../references/source_evidence/log/results/gauged_full_fermionic_log/sources/step4/w2Y_checks.json), with every individual contraction retained. The raw source comparison is C24 supplement §2.2.2, [Components of curvature-squared invariants of minimal supergravity in five dimensions — PDF113](https://arxiv.org/abs/2311.00679); it agrees with $`69/1024`$. The source value was not an input to the derivative calculation.

## 6. Common superfield stage and later projection

The primary, spinor and scalar are kept at the same superspace point $`z=(x,\theta)`$:

```math
H_{\log W}^{ij}(z),\qquad \varphi_{\log W\,\alpha}^i(z),\qquad
F_{\log W}(z)=-\frac{i}{4}\nabla^{\alpha i}\varphi_{\log W\,\alpha i}(z).
\tag{S4-SF-01}
```

No $`\theta=0`$ bar projection is taken anywhere in the active scalar calculation or in §8. In particular, $`X_\alpha^i`$ and $`Y`$ remain the Weyl superfield descendants; they are not replaced by component $`\chi_\alpha^i`$ or $`D`$. The Weyl two-form remains $`W_{ab}`$ and the triplet Weyl descendant remains $`X_{ab}^{ij}`$. The scalar vector superfield $`W`$ is still distinct from $`W_{ab}`$.

The tensors $`\mathcal T`$ and $`\mathcal R`$ retain exactly their superspace definitions in §3.2. The covariant derivative is the source superspace operator of S23 (2.1):

```math
\nabla_A=E_A-\frac12\Omega_A{}^{ab}M_{ab}-\Phi_A{}^{ij}J_{ij}-B_A\mathbb D
-\mathfrak F_A{}^{\alpha i}S_{\alpha i}-\mathfrak F_A{}^aK_a,
\qquad \Box=\nabla^a\nabla_a.
\tag{S4-SF-02}
```

This preserves the common source notation needed to compare the three descendants with S23 (3.24)–(3.26) and the raw descendant expressions in C24 supplement §2.2. The already checked scalar sectors remain

```math
F_{\log W}(z)\supset\frac{69}{1024}W^{ab}W_{ab}Y+\frac{3}{2048}Y^2.
\tag{S4-SF-03}
```

Component projection and the Gold-to-project convention conversion are performed explicitly in the [Step 6 component projection](../../STEP_06_LOG_PROJECTED_MULTIPLET_AND_BOSONIC_ACTION.md). They are separate operations, neither of which is applied here. The **complete earlier once-projected result** is retained separately in [STEP_04_LOG_SCALAR_PROJECTED_REFERENCE.md](../../STEP_04_LOG_SCALAR_PROJECTED_REFERENCE.md), with the projection rules and all terms written out. The component-coefficient audit remains in [note 05](../../notes/05_two_bosonic_corrections_source_audit.md). The former component-projection displays S4-29–S4-31 are replaced here by the superfield-stage declarations; their projection content is preserved as S4-P-01–S4-P-06 in that companion file.

## 7. Checks and precise certification boundary

The weights are $`w(H)=3`$, $`w(\varphi)=7/2`$, $`w(F)=4`$ and $`w(\nabla_\alpha^i)=1/2`$. Every term in the expanded scalar has weight four, even Grassmann parity, no free index, and each dummy index occurs once up and once down. These are checked on all written terms in the unprojected superfield expression. For example, $`w(W^{-8}\lambda^8)=-8+8(3/2)=4`$ and $`w(W^{ab}W_{ab}Y)=1+1+2=4`$. No boundary term was discarded.

The independent flat comparison starts again from the **original** projector in S23 (3.24), evaluates six derivatives to form $`H`$, then the two derivatives and epsilon contractions in (S4-02). With constant $`F_{ab}`$, $`X^{ij}`$ and $`\nabla_aW`$, all eight gaugino components are independent exterior generators. The candidate and this original eight-derivative calculation agree in seven probes: pure $`X`$, pure $`F`$, pure scalar gradient, a mixed case, and three independent mixed integer assignments. An additional probe checks the index-raising simplification used for printing. See [checks.json](../../../../../../../../references/source_evidence/log/results/gauged_full_fermionic_log/sources/step4/checks.json).

A useful numerical normalization slice is $`F_{ab}=0`$, $`\nabla_aW=0`$, $`X^{ij}=\begin{pmatrix}2&3\\3&5\end{pmatrix}`$ and zero gaugini after differentiation. It has $`X^{ij}X_{ij}=2`$ and gives $`F_{\log W}=3W^{-4}/8=3W^{-4}(X^{ij}X_{ij})^2/32`$. With all fields and derivatives except a constant scalar $`W`$ zero, every term vanishes. Both statements refer to flat verification jets, not to a truncation of the full result.

The separate curved algebraic check derives $`69W^2Y/1024`$ and $`3Y^2/2048`$ in the same superfield frame; projection is deferred. These checks do **not** prove the full nonlinear component transformations, symplectic reality of the reconstructed expression, or equality to every term of the nine-page reduced C24 supplement. The later certificate establishes full-primary S/K/linearity, retained-component projection/reality and the BF theorem. Literal all-fermion source-basis equality remains outside that scope. In particular, the generic relations $`K_aF=0`$ and $`S_\alpha^iF=6i\varphi_\alpha^i`$ from C24 (2.44) are target checks whose primary premises are now certified; their justification is the general linear-multiplet identity and verified polynomial reconstruction, not a separate brute-force scalar variation.

[derivation_coverage.json](../../../../../../../../references/source_evidence/log/results/gauged_full_fermionic_log/sources/step4/derivation_coverage.json) records the 58 inputs, product terms, evaluated scalar terms, source hashes, and final expression hash. [endpoint_term_locations.json](../../../../../../../../references/source_evidence/log/results/gauged_full_fermionic_log/sources/step4/endpoint_term_locations.json) maps every written scalar term to its originating primary input and final display segment.
