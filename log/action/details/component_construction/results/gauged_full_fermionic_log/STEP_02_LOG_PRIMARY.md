---

<!-- LOG_FULL_SUPERCOVARIANT_DERIVATIVES_20260925 -->

**Derivative notation.** This is a Gold superspace calculation: its $`\nabla_A`$ remains the full source covariant derivative. Component projection at [Step 6](STEP_06_LOG_PROJECTED_MULTIPLET_AND_BOSONIC_ACTION.md) transports it to the full project $`\mathcal D_a`$, with $`\Box^c=\mathcal D^a\mathcal D_a`$, as in the fermionic Weyl-squared calculation. The [active gauged LOG result](../../../construction.md) retains that full derivative. No Lorentz/SU(2)-only replacement is intended here.
title: "Step 2 — calculation of the full LOG primary"
date: 2026-09-23
status: "Source-frame derivation; full-primary and retained-order component certification complete; see current certificate"
procedure: GAUGED-LOG-G25-S23-PROCEDURE-v1
source_frame: Gold traceless Standard-Weyl superspace
fermion_order: all orders; no construction truncation
---

# Step 2 — calculating the LOG primary

<!-- LOG_CURRENT_CERTIFICATION_20260925 -->

**Current scope:** [the 2026-09-25 certificate](CERTIFICATION_LOG_TWO_FERMI_2026-09-25.md) verifies the full primary and the component action through two physical fermions. The source comparisons and restricted tests below retain their stated mathematical scope.

## 1. Problem and Target

The target is the **complete local superfield**

```math
H_{\log W}^{ij}=-\frac{3i}{40}\Delta^{ijkl}\nabla_{kl}\log W
=\frac{3i}{1280}\nabla^{(ij}\nabla^{kl)}\nabla_{kl}\log W.
\tag{S2-01}
```

This is S23 (3.24), equivalently C24 (4.7). The derivation obtains its coefficients from the operator, compares them with S23 (3.25), projects to components, and checks the linear-multiplet conditions. The intermediate definitions are explained in the step 2 explanation. The operator derivation, component projection and linear-multiplet identities are separate checks.

This file records the complete coefficient reconstruction from the six-spinor definition: **all 58 written terms**, from $`W^0`$ through $`W^{-6}`$, now have displayed derivations. The two $`W^0`$ terms agree with the source. In total 57 terms agree with S23 (3.25); the $`W^{-3}`$ derivative-of-$`X^{ij}`$ coefficient is $`+i/4`$ from the defining operator, opposite to the printed $`-i/4`$, as derived and independently checked in (S2-79)–(S2-81). The final full expression (S2-193) includes this positive coefficient. The published comparison is preserved separately and unchanged. Full-primary defining-projector equality and curved S/K/linearity now pass. Project-frame projection, canonicalization, reality, current conservation and BF construction are certified through the retained order in [the current certificate](CERTIFICATION_LOG_TWO_FERMI_2026-09-25.md). The conservation and supersymmetry conclusions use verified multiplet premises and the complete superform proof; a separate brute-force variation of all expanded terms is not claimed.

The assumptions are:

1. **A1:** five-dimensional classical conformal supergravity, off shell, in the source's traceless Standard-Weyl frame.
2. **A2:** $`W>0`$ on the working patch; the inverse powers and real logarithm are locally defined.
3. **A3:** no construction gauge, auxiliary equation, background equation, field redefinition or fermion-order truncation is imposed.
4. **A4:** equalities are local equalities. No integration by parts is permitted to remove a primary term.
5. **A5:** explicitly identified flat/constant-field specializations below are verification probes only. They are not imposed on the full construction.

The [main reference](CONVENTIONS.md) and [LOG working conventions](LOG_CONVENTIONS.md) control the calculation. The independent compensating linear multiplet does not enter this step. The open step-1 current/form issue is retained for the later BF construction.

| Input | Located equations | Openable evidence |
|---|---|---|
| Covariant derivatives and torsion/curvature | S23 (2.1)–(2.2); C24 (A.1)–(A.4) | [S23 PDF7](https://arxiv.org/abs/2302.14295), [On curvature-squared invariants of minimal five-dimensional supergravity from superspace — PDF8](https://arxiv.org/abs/2302.14295); [C24 PDF81](https://arxiv.org/abs/2311.00679), [Components of curvature-squared invariants of minimal supergravity in five dimensions — PDF82](https://arxiv.org/abs/2311.00679), [Components of curvature-squared invariants of minimal supergravity in five dimensions — PDF83](https://arxiv.org/abs/2311.00679) |
| Vector definitions and derivative rules | S23 (2.11)–(2.15) = C24 (2.28)–(2.32) | [S23 PDF10](https://arxiv.org/abs/2302.14295), [On curvature-squared invariants of minimal five-dimensional supergravity from superspace — PDF11](https://arxiv.org/abs/2302.14295) |
| Weyl descendants | S23 (2.5)–(2.8), same numbering in C24 | [S23 PDF8](https://arxiv.org/abs/2302.14295), [On curvature-squared invariants of minimal five-dimensional supergravity from superspace — PDF9](https://arxiv.org/abs/2302.14295) |
| Projector | S23 (2.17) = C24 (2.34) | [S23 PDF11](https://arxiv.org/abs/2302.14295) |
| Definition and full comparison | S23 (3.24)–(3.25) | [On curvature-squared invariants of minimal five-dimensional supergravity from superspace — PDF20](https://arxiv.org/abs/2302.14295), [On curvature-squared invariants of minimal five-dimensional supergravity from superspace — PDF21](https://arxiv.org/abs/2302.14295), [On curvature-squared invariants of minimal five-dimensional supergravity from superspace — PDF22](https://arxiv.org/abs/2302.14295) |
| Later projection comparison | C24 (2.15)–(2.16), (4.8a) | [Components of curvature-squared invariants of minimal supergravity in five dimensions — PDF12](https://arxiv.org/abs/2311.00679), [Components of curvature-squared invariants of minimal supergravity in five dimensions — PDF32](https://arxiv.org/abs/2311.00679), [Components of curvature-squared invariants of minimal supergravity in five dimensions — PDF33](https://arxiv.org/abs/2311.00679), [Components of curvature-squared invariants of minimal supergravity in five dimensions — PDF34](https://arxiv.org/abs/2311.00679) |

The relevant derivative definitions are **C24 (2.29)–(2.30), equivalently S23 (2.12)–(2.13)**. S23 (2.29) instead describes the vector-bilinear composite linear multiplet.

## 2. Convention Ledger

<!-- ASSERT_CONVENTION: source_frame=Gold traceless Standard-Weyl superspace, metric_signature=(-,+,+,+,+), natural_units=hbar=c=1, scope=classical off-shell gauge-unfixed LOG primary, fermions=all degrees retained, regularization_scheme=Not applicable for initial classical analysis, renormalization_scheme=Not applicable for initial classical analysis -->

We use $`a,b=0,\ldots,4`$, $`\alpha,\beta=1,\ldots,4`$, and $`i,j=1,2`$. Parentheses and square brackets have unit weight. The metric is $`\eta_{ab}=\mathop{\mathrm{diag}}\nolimits(-,+,+,+,+)`$; Gold's matrices satisfy $`\{\Gamma^a,\Gamma^b\}=-2\eta^{ab}`$ and $`\Sigma^{ab}=-[\Gamma^a,\Gamma^b]/4`$. Gold's orientation has $`\varepsilon^{01234}=-1`$. We do not replace these matrices or epsilon by the component-frame ones mid-calculation.

The spinor metric is antisymmetric; $`\zeta^\alpha=\varepsilon^{\alpha\beta}\zeta_\beta`$. Source SU(2) lowering is $`\zeta_i=\varepsilon_{ij}\zeta^j`$, with $`\varepsilon^{12}=\varepsilon_{21}=1`$. This has the same numerical action as the component ledger's NW–SE convention; it does not justify identifying differently ordered written contractions. All spinors, spinor derivatives and SUSY parameters are Grassmann odd. Spinor derivatives act from the left; a parameter-contracted SUSY variation is even.

For the explicit flat matrix check, the second matrix slot is lowered as

```math
(\Gamma^a)_{\alpha\beta}=\varepsilon_{\beta\gamma}(\Gamma^a)_\alpha{}^\gamma,
\qquad
(\Sigma^{ab})_{\alpha\beta}=\varepsilon_{\beta\gamma}(\Sigma^{ab})_\alpha{}^\gamma.
\tag{S2-02}
```

These placements are fixed by the mixed and lowered matrices in Butter et al., Appendix A, (A.3)–(A.11), the formalism source cited as S23 reference [20]. Its $`C`$ denotes $`\varepsilon^{\alpha\beta}`$; the lower spinor metric is $`C^{-1}`$. This exact matrix-placement item was not explicitly fixed in the existing cached equations, so the [primary reference](https://arxiv.org/html/1410.8682) was consulted for this verification input only. The original S23/C24 curvature and derivative rules remain controlling. In particular, lowering that second matrix index on the wrong side gives a false sign mismatch in the mixed $`F\nabla W`$ probe.

All spacetime curvature signs are fixed by the covariant derivative algebra below, not by substituting a memorized Riemann convention. No Fourier transform, quantum-state normalization, action normalization or expansion in a curvature-squared coupling enters this local primary calculation. The later action coupling remains the one in the procedure lock.

| Symbol | Meaning | Weyl weight |
|---|---|---:|
| $`W`$ | Defining vector scalar superfield | 1 |
| $`W_{ab}`$, $`W_{\alpha\beta}`$ | Super-Weyl tensor, not the scalar $`W`$ | 1 |
| $`\lambda_\alpha^i`$ | Vector gaugino superfield | $`3/2`$ |
| $`X^{ij}`$, $`F_{ab}`$ | Vector auxiliary and field strength | 2 |
| $`X_\alpha^i`$, $`W_{\alpha\beta\gamma}{}^i`$ | Fermionic Weyl descendants | $`3/2`$ |
| $`X_{\alpha\beta}^{ij}`$, $`Y`$ | Bosonic Weyl descendants | 2 |
| $`\nabla_a`$, $`\nabla_\alpha^i`$ | Vector and spinor covariant derivatives | $`1`$, $`1/2`$ |

The $`Y`$ in this table is not the component vector auxiliary $`Y^{ij}`$; $`\mathbb D`$ is the dilatation generator, not the component Weyl auxiliary $`D`$.

## 3. Definitions and Required Identities

### 3.1 The derivative, with all connections retained

S23 (2.1)–(2.2) defines

```math
\begin{aligned}
\nabla_A&=E_A-\frac12\Omega_A{}^{ab}M_{ab}-\Phi_A{}^{ij}J_{ij}-B_A\mathbb D
-\mathfrak F_A{}^{\alpha i}S_{\alpha i}-\mathfrak F_A{}^aK_a,\\
[\nabla_A,\nabla_B\}&=-T_{AB}{}^C\nabla_C-\frac12R(M)_{AB}{}^{cd}M_{cd}
-R(J)_{AB}{}^{kl}J_{kl}-R(\mathbb D)_{AB}\mathbb D\\
&\quad-R(S)_{AB}{}^{\gamma k}S_{\gamma k}-R(K)_{AB}{}^cK_c.
\end{aligned}
\tag{S2-03}
```

The vector derivative in spinor notation and the d'Alembertian are

```math
\nabla_{\alpha\beta}:=(\Gamma^a)_{\alpha\beta}\nabla_a,
\qquad \Box:=\nabla^a\nabla_a.
\tag{S2-04}
```

Neither is a flat partial derivative. A bar projection is also not a replacement $`\nabla_a\mapsto\partial_a`$.

### 3.2 The vector multiplet and its three reduction rules

The source constraints and definitions, S23 (2.11)–(2.12), are

```math
\begin{gathered}
W^*=W,\qquad K_AW=0,\qquad\mathbb DW=W,\qquad
\nabla_\alpha^{(i}\nabla_\beta^{j)}W=\frac14\varepsilon_{\alpha\beta}\nabla^{ij}W,\\
\lambda_\alpha^i=-i\nabla_\alpha^iW,\qquad
X^{ij}=\frac i4\nabla^{ij}W=-\frac14\nabla^{\alpha(i}\lambda_\alpha^{j)},\\
F_{\alpha\beta}=-\frac i4\nabla_{(\alpha}^k\nabla_{\beta)k}W-W_{\alpha\beta}W
=\frac12(\Sigma^{ab})_{\alpha\beta}F_{ab}.
\end{gathered}
\tag{S2-05}
```

The complete first reductions are S23 (2.13a–c):

```math
\begin{aligned}
\nabla_\alpha^i\lambda_\beta^j
={}&-2\varepsilon^{ij}(F_{\alpha\beta}+W_{\alpha\beta}W)
-\varepsilon_{\alpha\beta}X^{ij}-\varepsilon^{ij}\nabla_{\alpha\beta}W,\\
\nabla_\alpha^iF_{\beta\gamma}
={}&-i\nabla_{\alpha(\beta}\lambda_{\gamma)}^i-i\varepsilon_{\alpha(\beta}\nabla_{\gamma)}{}^\delta\lambda_\delta^i
-\frac{3i}{2}W_{\beta\gamma}\lambda_\alpha^i-W_{\alpha\beta\gamma}{}^iW\\
&+\frac i2W_{\alpha(\beta}\lambda_{\gamma)}^i
-\frac{3i}{2}\varepsilon_{\alpha(\beta}W_{\gamma)}{}^\delta\lambda_\delta^i,\\
\nabla_\alpha^iX^{jk}
={}&2i\varepsilon^{i(j}\left(\nabla_\alpha{}^\beta\lambda_\beta^{k)}
-\frac12W_{\alpha\beta}\lambda^{\beta k)}+\frac{3i}{4}X_\alpha^{k)}W\right).
\end{aligned}
\tag{S2-06}
```

In the last line, $`X_\alpha^i`$ is a Weyl descendant. It cannot be discarded by choosing a value for the vector triplet $`X^{ij}`$.

### 3.3 Weyl fields generated by the calculation

S23 (2.5), together with the two-form/bispinor correspondence in footnote 4 on PDF8, gives

```math
\begin{gathered}
W_{\alpha\beta\gamma}{}^i=\nabla_{(\alpha}^iW_{\beta\gamma)},\quad
X_\alpha^i=\frac25\nabla^{\beta i}W_{\beta\alpha},\quad
W_{\alpha\beta\gamma\delta}=\nabla_{(\alpha}^kW_{\beta\gamma\delta)k},\\
X_{\alpha\beta}^{ij}=\nabla_{(\alpha}^{(i}X_{\beta)}^{j)},\quad
Y=i\nabla^{\gamma k}X_{\gamma k},\quad
T_{ab}=(\Sigma_{ab})^{\alpha\beta}T_{\alpha\beta}.
\end{gathered}
\tag{S2-07}
```

In the last relation, $`T_{ab}`$ denotes any antisymmetric two-form and $`T_{\alpha\beta}`$ its symmetric bispinor. The first Weyl identity used below is

```math
\nabla_\gamma^kW_{\alpha\beta}=W_{\alpha\beta\gamma}{}^k
+\varepsilon_{\gamma(\alpha}X_{\beta)}^k.
\tag{S2-08}
```

This is S23 (2.6a). The remaining five equations (2.6b–f), the Bianchi relations (2.7), and the generator actions (2.8) are explicitly stored together in [the master source fragment](sources/reference_fragments/10_gold_source_equations_and_bridge.md). They are the source inputs used in the completed coefficient reduction below; independent S/K and reality certification remain separate from that reduction.

### 3.4 Operator order and graded products

```math
\begin{gathered}
\nabla^{ij}=\nabla^{\alpha(i}\nabla_\alpha^{j)},\qquad
\Delta^{ijkl}=-\frac1{96}\varepsilon^{\alpha\beta\gamma\delta}
\nabla_\alpha^{(i}\nabla_\beta^j\nabla_\gamma^k\nabla_\delta^{l)}
=-\frac1{32}\nabla^{(ij}\nabla^{kl)},\\
\nabla_\alpha^i(AB)=(\nabla_\alpha^iA)B+(-1)^{|A|}A\nabla_\alpha^iB.
\end{gathered}
\tag{S2-09}
```

The first line is S23 (2.17). The second line fixes the odd left derivative. Rightmost operators act first. Since $`\mathbb DW=W`$,

```math
\mathbb D\log W=W^{-1}\mathbb DW=1,\qquad K_A\log W=0.
\tag{S2-10}
```

Thus the logarithm has an inhomogeneous dilatation shift. It is not a homogeneous weight-zero superfield.

## 4. Detailed Derivation

### 4.1 One and two derivatives of the logarithm

<!-- ASSERT_CONVENTION: source_frame=Gold traceless Standard-Weyl superspace, derivative_parity=odd left, scope=exact local superfield identities -->

First apply the chain rule and then (S2-05):

```math
\nabla_\alpha^i\log W=W^{-1}\nabla_\alpha^iW=iW^{-1}\lambda_\alpha^i,
\qquad
\nabla_\alpha^iW^{-n}=-nW^{-n-1}\nabla_\alpha^iW=-niW^{-n-1}\lambda_\alpha^i.
\tag{S2-11}
```

For the second derivative keep the original fermion order:

```math
\begin{aligned}
\nabla_\alpha^i\nabla_\beta^j\log W
&=i(\nabla_\alpha^iW^{-1})\lambda_\beta^j+iW^{-1}\nabla_\alpha^i\lambda_\beta^j\\
&=i(-i)W^{-2}\lambda_\alpha^i\lambda_\beta^j+iW^{-1}\nabla_\alpha^i\lambda_\beta^j\\
&=-2iW^{-1}\varepsilon^{ij}F_{\alpha\beta}-2i\varepsilon^{ij}W_{\alpha\beta}
-iW^{-1}\varepsilon_{\alpha\beta}X^{ij}-iW^{-1}\varepsilon^{ij}\nabla_{\alpha\beta}W
+W^{-2}\lambda_\alpha^i\lambda_\beta^j.
\end{aligned}
\tag{S2-12}
```

The second line uses $`i(-i)=+1`$; the third inserts every term of (S2-06)'s first line. In particular, $`W^{-1}(W_{\alpha\beta}W)=W_{\alpha\beta}`$. This is why some final terms have no inverse scalar factor.

Adding the expression with $`(\alpha,i)\leftrightarrow(\beta,j)`$ makes the $`F`$, Weyl and $`X^{ij}`$ terms cancel: $`F_{\beta\alpha}=F_{\alpha\beta}`$, $`W_{\beta\alpha}=W_{\alpha\beta}`$, and $`\varepsilon_{\beta\alpha}=-\varepsilon_{\alpha\beta}`$. The two odd-factor products cancel by $`\lambda_\beta^j\lambda_\alpha^i=-\lambda_\alpha^i\lambda_\beta^j`$. Since $`\nabla_{\beta\alpha}=-\nabla_{\alpha\beta}`$, the remaining term is

```math
\{\nabla_\alpha^i,\nabla_\beta^j\}\log W
=-2i\varepsilon^{ij}\nabla_{\alpha\beta}\log W.
\tag{S2-13}
```

This matches (S2-03) with C24 (A.2a) on the Lorentz-scalar $`S/K`$-primary logarithm. It does not justify dropping curvature generators when the same anticommutator acts on descendants.

### 4.2 Contract to the inner triplet seed

Use the contracted definition in (S2-05), keeping its source normalization:

```math
\begin{aligned}
\nabla^{ij}\log W
&=W^{-1}\nabla^{ij}W-W^{-2}(\nabla^{\alpha(i}W)(\nabla_\alpha^{j)}W)\\
&=-4iW^{-1}X^{ij}-i^2W^{-2}\lambda^{\alpha(i}\lambda_\alpha^{j)}\\
&=-4iW^{-1}X^{ij}+W^{-2}\lambda^{\alpha(i}\lambda_\alpha^{j)}.
\end{aligned}
\tag{S2-14}
```

The bilinear is symmetric without imposing an equation of motion. Indeed,

```math
\varepsilon^{\alpha\beta}\lambda_\beta^j\lambda_\alpha^i
=-\varepsilon^{\alpha\beta}\lambda_\alpha^i\lambda_\beta^j
=-\varepsilon^{\beta\alpha}\lambda_\beta^i\lambda_\alpha^j
=\varepsilon^{\alpha\beta}\lambda_\beta^i\lambda_\alpha^j.
\tag{S2-15}
```

The first equality exchanges odd factors, the second relabels dummy indices, and the third uses the antisymmetric spinor metric. Both terms of (S2-14) have weight one: $`-1+2=-2+2(3/2)=1`$.

### 4.3 The next spinor derivative, with the full source substitutions

Differentiate both seed terms before collecting any fields:

```math
\begin{aligned}
\nabla_\gamma^k\nabla^{ij}\log W
={}&-4i\left[-iW^{-2}\lambda_\gamma^kX^{ij}+W^{-1}\nabla_\gamma^kX^{ij}\right]
-2iW^{-3}\lambda_\gamma^k\lambda^{\alpha(i}\lambda_\alpha^{j)}\\
&+W^{-2}\left[(\nabla_\gamma^k\lambda^{\alpha(i})\lambda_\alpha^{j)}
-\lambda^{\alpha(i}\nabla_\gamma^k\lambda_\alpha^{j)}\right].
\end{aligned}
\tag{S2-16}
```

The minus sign inside the last bracket comes from differentiating the second odd factor. Inserting both relevant lines of (S2-06) now gives

```math
\begin{aligned}
\nabla_\gamma^k\nabla^{ij}\log W
={}&-4W^{-2}\lambda_\gamma^kX^{ij}
+8W^{-1}\varepsilon^{k(i}\nabla_\gamma{}^\beta\lambda_\beta^{j)}
-4W^{-1}\varepsilon^{k(i}W_{\gamma\beta}\lambda^{\beta j)}
+6i\varepsilon^{k(i}X_\gamma^{j)}\\
&-2iW^{-3}\lambda_\gamma^k\lambda^{\alpha(i}\lambda_\alpha^{j)}\\
&+W^{-2}\varepsilon^{\alpha\beta}
\left[-2\varepsilon^{k(i}(F_{\gamma\beta}+W_{\gamma\beta}W)
-\varepsilon_{\gamma\beta}X^{k(i}-\varepsilon^{k(i}\nabla_{\gamma\beta}W\right]\lambda_\alpha^{j)}\\
&+W^{-2}\lambda^{\alpha(i}
\left[2\varepsilon^{k j)}(F_{\gamma\alpha}+W_{\gamma\alpha}W)
+\varepsilon_{\gamma\alpha}X^{k j)}+\varepsilon^{k j)}\nabla_{\gamma\alpha}W\right].
\end{aligned}
\tag{S2-17}
```

Here $`(-4i)(-i)=-4`$, $`(-4i)(2i)=8`$, $`8(-1/2)=-4`$ and $`8(3i/4)=6i`$. The spinor metric in the third line raises precisely the original gaugino index. No odd factors were moved through one another in the substitution. All terms have weight $`3/2`$.

### 4.4 The first mixed commutator that must be retained

When a further spinor derivative reaches a vector derivative of $`W`$, its evaluation is

```math
\nabla_\alpha^i\nabla_bW
=\nabla_b\nabla_\alpha^iW+[\nabla_\alpha^i,\nabla_b]W.
\tag{S2-18}
```

C24 (A.3a,b) tabulates the opposite order, $`[\nabla_b,\nabla_\alpha^i]`$. On the primary scalar $`W`$, the Lorentz, SU(2), S and K generators annihilate $`W`$, while $`\mathbb DW=W`$. Therefore

```math
\begin{aligned}
[\nabla_b,\nabla_\alpha^i]W
&=-T_{b\alpha}{}^{i\gamma}{}_{k}\nabla_\gamma^kW-R(\mathbb D)_{b\alpha}{}^iW\\
&=-\frac i4\left[3(\Gamma_b)_\alpha{}^\beta W_\beta{}^\gamma
-W_\alpha{}^\beta(\Gamma_b)_\beta{}^\gamma\right]\lambda_\gamma^i
+\frac14(\Gamma_b)_\alpha{}^\gamma X_\gamma^iW,\\
\nabla_\alpha^i\nabla_bW
&=i\nabla_b\lambda_\alpha^i
+\frac i4\left[3(\Gamma_b)_\alpha{}^\beta W_\beta{}^\gamma
-W_\alpha{}^\beta(\Gamma_b)_\beta{}^\gamma\right]\lambda_\gamma^i
-\frac14(\Gamma_b)_\alpha{}^\gamma X_\gamma^iW.
\end{aligned}
\tag{S2-19}
```

The last equality reverses the mixed commutator in the preceding line. The Weyl-spinor term comes from the dilatation curvature; treating the logarithm as weight zero would erase its corresponding contribution. On $`\lambda`$, $`F`$ or $`X^{ij}`$, the generators omitted in this **scalar** calculation must instead be evaluated using their source representations and S laws.

### 4.5 The complete six-fermion sector

The only way to obtain six explicit gauginos from six derivatives is for each derivative to differentiate the scalar argument of the logarithm once. Its coefficient is

```math
\frac{d^6}{dW^6}\log W=(-1)^5\,5!\,W^{-6}=-120W^{-6},
\qquad (i\lambda)^6=i^6\lambda^6=-\lambda^6.
\tag{S2-20}
```

Substitution into the paired projector, without any derivative interchange, gives

```math
\left.H_{\log W}^{ij}\right|_{\lambda^6W^{-6}}
=\frac{3i}{1280}(-120)(-1)W^{-6}
\lambda^{\alpha(i}\lambda_\alpha^j\lambda^{\beta k}\lambda_\beta^{l)}
\lambda_k^\gamma\lambda_{\gamma l}.
\tag{S2-21}
```

Each contracted two-gaugino factor is even and symmetric in its SU(2) indices by (S2-15). Four-index unit symmetrization therefore has three distinct pairings. Interchanging the even pairs introduces no Grassmann sign:

```math
\begin{aligned}
\lambda^{\alpha(i}\lambda_\alpha^j\lambda^{\beta k}\lambda_\beta^{l)}
\lambda_k^\gamma\lambda_{\gamma l}
=\frac13\Big(&\lambda^{\alpha i}\lambda_\alpha^j\lambda^{\beta k}\lambda_\beta^l\lambda_k^\gamma\lambda_{\gamma l}
+\lambda^{\alpha i}\lambda_\alpha^k\lambda^{\beta j}\lambda_\beta^l\lambda_k^\gamma\lambda_{\gamma l}\\
&+\lambda^{\alpha i}\lambda_\alpha^l\lambda^{\beta j}\lambda_\beta^k\lambda_k^\gamma\lambda_{\gamma l}\Big).
\end{aligned}
\tag{S2-22}
```

Rename $`k\leftrightarrow l`$ in the last term and use symmetry of the final even bilinear. The last two terms become equal. Since $`3\cdot120/(1280\cdot3)=3/32`$, the entire sector is

```math
\left.H_{\log W}^{ij}\right|_{\lambda^6W^{-6}}
=W^{-6}\left(
\frac{3i}{32}\lambda^{\alpha i}\lambda_\alpha^j\lambda^{\beta k}\lambda_\beta^l\lambda_k^\gamma\lambda_{\gamma l}
+\frac{3i}{16}\lambda^{\alpha i}\lambda_\alpha^k\lambda^{\beta j}\lambda_\beta^l\lambda_k^\gamma\lambda_{\gamma l}
\right).
\tag{S2-23}
```

Both coefficients and both contractions agree with S23 (3.25). No Fierz rearrangement, integration by parts or fermion truncation enters this derivation.

### 4.6 Reducing the four outer derivatives without discarding curvature

Choose a basis in the two-dimensional SU(2) index space and write $`+=1`$, $`-=2`$, so $`\varepsilon^{+-}=1`$. These labels contract SU(2) indices; they are **not** a gauge choice on a physical field. Write $`\nabla_\alpha^+=\nabla_\alpha^1`$, $`X^{++}=X^{11}`$, $`X^{+-}=X^{12}`$, and $`X^{--}=X^{22}`$. A formula for $`H^{++}`$ in every such basis determines the symmetric tensor $`H^{ij}`$.

Every coefficient in the spinor anticommutator in section 3.1 is proportional to $`\varepsilon^{ij}`$. Hence

```math
\{\nabla_\alpha^+,\nabla_\beta^+\}=0,
\qquad \nabla_{\alpha_1}^+\nabla_{\alpha_2}^+\nabla_{\alpha_3}^+\nabla_{\alpha_4}^+\nabla_{\alpha_5}^+=0.
\tag{S2-28}
```

The second identity is antisymmetry over five indices taking four values. It is an operator identity, including on descendants; no scalar-only commutator has been used. Its SU(2)-polarized form is $`\Delta^{(ijkl}\nabla_\alpha^{m)}=0`$. The components with four plus indices and one minus index, and with three plus and two minus indices, give

```math
\begin{aligned}
\Delta^{++++}\nabla_\alpha^-+4\Delta^{+++-}\nabla_\alpha^+&=0,\\
2\Delta^{+++-}\nabla_\alpha^-+3\Delta^{++--}\nabla_\alpha^+&=0.
\end{aligned}
\tag{S2-29}
```

Contract the first identity on the right with a second minus derivative, and the second with a plus derivative. Since $`\nabla^{ij}=\nabla^{ji}`$, the results are

```math
\Delta^{+++-}\nabla^{+-}=-\frac14\Delta^{++++}\nabla^{--},
\qquad \Delta^{++--}\nabla^{++}=\frac16\Delta^{++++}\nabla^{--}.
\tag{S2-30}
```

SU(2) lowering gives $`\nabla_{++}=\nabla^{--}`$, $`\nabla_{+-}=-\nabla^{+-}`$ and $`\nabla_{--}=\nabla^{++}`$. Thus

```math
\begin{aligned}
\Delta^{++kl}\nabla_{kl}
&=\Delta^{++++}\nabla^{--}-2\Delta^{+++-}\nabla^{+-}+\Delta^{++--}\nabla^{++}\\
&=\left(1+\frac12+\frac16\right)\Delta^{++++}\nabla^{--}
=\frac53\Delta^{++++}\nabla^{--},\\
H^{++}&=-\frac i8\Delta^{++++}\nabla^{--}\log W
=-\frac12\Delta^{++++}(W^{-1}X^{--})-\frac i8\Delta^{++++}(W^{-2}\lambda^{\alpha-}\lambda_\alpha^-).
\end{aligned}
\tag{S2-31}
```

This rewrites exactly the original six-derivative operator. It still applies the two inner derivatives first and the four outer derivatives afterwards. The same representation is the formalism identity in Butter et al. (2015), (7.5), (14.27); the factor $`5/3`$ has been derived here from the source projector, so no older action-sign convention is imported.

The vector rules now imply

```math
\begin{aligned}
\nabla_\alpha^+W&=i\lambda_\alpha^+,&
\nabla_\alpha^+\lambda_\beta^+&=-\varepsilon_{\alpha\beta}X^{++},&
\nabla_\alpha^+X^{++}&=0,\\
\nabla_\alpha^+\nabla_\beta^+W&=-i\varepsilon_{\alpha\beta}X^{++},&
\nabla_\gamma^+\nabla_\alpha^+\nabla_\beta^+W&=0.
\end{aligned}
\tag{S2-32}
```

These last identities hold in the curved theory. They do **not** assert that mixed-plus/minus third derivatives vanish.

For the following displayed contractions only, let $`B^{rs}=\lambda^{\alpha r}\lambda_\alpha^s`$, for $`r,s\in\{+,-\}`$. This is the ordinary even gaugino bilinear; section 4.2 already proved $`B^{rs}=B^{sr}`$. The left product rule gives, with the two terms displayed separately,

```math
\begin{aligned}
\nabla_\alpha^+B^{++}
&=(\nabla_\alpha^+\lambda^{\beta+})\lambda_\beta^+
-\lambda^{\beta+}\nabla_\alpha^+\lambda_\beta^+\\
&=\delta_\alpha{}^\beta X^{++}\lambda_\beta^+
+\lambda^{\beta+}\varepsilon_{\alpha\beta}X^{++}=2X^{++}\lambda_\alpha^+,\\
\nabla^{++}B^{++}&=2X^{++}\nabla^{\alpha+}\lambda_\alpha^+=-8(X^{++})^2,\\
\nabla^{++}f(W)&=-4if'(W)X^{++}-f''(W)B^{++}.
\end{aligned}
\tag{S2-33}
```

For even $`A,C`$, $`\nabla^{++}(AC)=(\nabla^{++}A)C+A\nabla^{++}C+2(\nabla^{\alpha+}A)\nabla_\alpha^+C`$. Applying this rule twice, retaining the canceling cross terms, gives

```math
\begin{aligned}
(\nabla^{++})^2f
&=-4i[-4if''X^{++}-f'''B^{++}]X^{++}\\
&\quad-\big[(-4if'''X^{++}-f''''B^{++})B^{++}-8f''(X^{++})^2+4if'''X^{++}B^{++}\big]\\
&=-8f''(X^{++})^2+4if'''X^{++}B^{++}+f''''(B^{++})^2,\\
\Delta^{++++}f(W)
&=\frac14f''(X^{++})^2-\frac i8f'''X^{++}B^{++}-\frac1{32}f''''(B^{++})^2.
\end{aligned}
\tag{S2-34}
```

In particular, every coefficient in the two inverse-power derivatives is now explicit:

```math
\begin{aligned}
\Delta^{++++}W^{-1}&=\frac{(X^{++})^2}{2W^3}+\frac{3iX^{++}B^{++}}{4W^4}-\frac{3(B^{++})^2}{4W^5},\\
\Delta^{++++}W^{-2}&=\frac{3(X^{++})^2}{2W^4}+\frac{3iX^{++}B^{++}}{W^5}-\frac{15(B^{++})^2}{4W^6}.
\end{aligned}
\tag{S2-35}
```

The products in (S2-31) also require derivatives acting on $`X^{--}`$ and $`B^{--}`$. For even $`A,C`$, the complete four-derivative product is

```math
\begin{aligned}
\Delta^{++++}(AC)={}&(\Delta^{++++}A)C+A\Delta^{++++}C\\
&-\frac1{24}\varepsilon^{\alpha\beta\gamma\delta}(\nabla_\alpha^+\nabla_\beta^+\nabla_\gamma^+A)\nabla_\delta^+C
-\frac1{16}\varepsilon^{\alpha\beta\gamma\delta}(\nabla_\alpha^+\nabla_\beta^+A)\nabla_\gamma^+\nabla_\delta^+C\\
&-\frac1{24}\varepsilon^{\alpha\beta\gamma\delta}(\nabla_\alpha^+A)\nabla_\beta^+\nabla_\gamma^+\nabla_\delta^+C.
\end{aligned}
\tag{S2-36}
```

The factors are $`4/96`$, $`6/96`$, $`4/96`$. For example, the six choices of the two derivative positions acting on $`A`$ have shuffle signs $`+,-,+,+,-,+`$; the same signs arise when their indices are moved into the first two slots of $`\varepsilon^{\alpha\beta\gamma\delta}`$. Their products are all $`+1`$, yielding $`6/96`$. This explains why all three displayed cross terms have the projector's minus sign.

### 4.7 All three terms at order $`W^{-5}`$

Only three contributions in (S2-31), (S2-35), (S2-36) can have this pole: the $`W^{-5}`$ term of $`\Delta W^{-1}`$ times $`X^{--}`$; the $`W^{-5}`$ term of $`\Delta W^{-2}`$ times $`B^{--}`$; and the part with three derivatives of $`W^{-2}`$ and one derivative of $`B^{--}`$. The latter uses

```math
\left.\nabla_\alpha^+\nabla_\beta^+\nabla_\gamma^+W^{-2}\right|_{W^{-5}}
=(-24W^{-5})i^3\lambda_\alpha^+\lambda_\beta^+\lambda_\gamma^+
=24iW^{-5}\lambda_\alpha^+\lambda_\beta^+\lambda_\gamma^+.
\tag{S2-37}
```

Here and below a restriction to a pole is a coefficient extraction, not a field restriction. The vector rule and the odd product rule give

```math
\begin{aligned}
\nabla_\delta^+B^{--}
&=\varepsilon^{\rho\sigma}(\nabla_\delta^+\lambda_\sigma^-)\lambda_\rho^-
-\lambda^{\rho-}\nabla_\delta^+\lambda_\rho^-\\
&=-2(\nabla_\delta^+\lambda_\rho^-)\lambda^{\rho-}\\
&=4(F_{\delta\rho}+W_{\delta\rho}W)\lambda^{\rho-}
+2X^{+-}\lambda_\delta^-+2\nabla_{\delta\rho}W\lambda^{\rho-}.
\end{aligned}
\tag{S2-38}
```

For clarity, the symplectic identity used in contracting three equal-SU gauginos is displayed with those actual spinors:

```math
\begin{aligned}
\lambda_\alpha^+\lambda_\beta^+\lambda_\gamma^+
&=\frac12B^{++}(\varepsilon_{\alpha\beta}\lambda_\gamma^+-\varepsilon_{\alpha\gamma}\lambda_\beta^++\varepsilon_{\beta\gamma}\lambda_\alpha^+),\\
\varepsilon^{\alpha\beta\gamma\delta}\lambda_\alpha^+\lambda_\beta^+\lambda_\gamma^+
&=3B^{++}\lambda^{\delta+}.
\end{aligned}
\tag{S2-39}
```

One can establish the first line without a gamma-matrix convention: both sides are alternating three-spinors in a four-dimensional symplectic space. In a Darboux basis with $`\varepsilon_{12}=\varepsilon_{34}=1`$, $`B^{++}=2(\lambda_1^+\lambda_2^++\lambda_3^+\lambda_4^+)`$. The independent components $`123,124,134,234`$ on the right are respectively $`\lambda_1^+\lambda_2^+\lambda_3^+`$, $`\lambda_1^+\lambda_2^+\lambda_4^+`$, $`\lambda_1^+\lambda_3^+\lambda_4^+`$, $`\lambda_2^+\lambda_3^+\lambda_4^+`$. Repeated-index components vanish on both sides. The second line follows by inserting $`\varepsilon^{\alpha\beta\gamma\delta}=\varepsilon^{\alpha\beta}\varepsilon^{\gamma\delta}-\varepsilon^{\alpha\gamma}\varepsilon^{\beta\delta}+\varepsilon^{\alpha\delta}\varepsilon^{\beta\gamma}`$; all three terms give $`B^{++}\lambda^{\delta+}`$.

Using (S2-39) in the three specified contributions gives

```math
\begin{aligned}
\left.H^{++}\right|_{W^{-5}}
={}&\frac{3}{8W^5}X^{--}(B^{++})^2+\frac{3}{8W^5}X^{++}B^{++}B^{--}\\
&-\frac{1}{8W^5}\varepsilon^{\alpha\beta\gamma\delta}\lambda_\alpha^+\lambda_\beta^+\lambda_\gamma^+
[4F_{\delta\rho}\lambda^{\rho-}+2X^{+-}\lambda_\delta^-+2\nabla_{\delta\rho}W\lambda^{\rho-}]\\
={}&\frac{3B^{++}}{8W^5}[X^{--}B^{++}+X^{++}B^{--}-2X^{+-}B^{+-}]\\
&-\frac{3B^{++}}{2W^5}F_{\delta\rho}\lambda^{\delta+}\lambda^{\rho-}
-\frac{3B^{++}}{4W^5}(\Gamma^a)^{\alpha\beta}\lambda_\alpha^+\lambda_\beta^-\nabla_aW.
\end{aligned}
\tag{S2-40}
```

The coefficient of the second line before its bracket is $`(-i/8)(-1/24)(24i)=-1/8`$. The $`W_{\delta\rho}W`$ part of (S2-38) contributes at $`W^{-4}`$ and is retained for that subsequent sector.

The auxiliary bracket is exactly $`X^{kl}B_{kl}`$ because $`B_{++}=B^{--}`$, $`B_{+-}=-B^{+-}`$, $`B_{--}=B^{++}`$. For the symmetric bispinor $`F_{\alpha\beta}`$, the SU(2) contraction and the one odd interchange give

```math
\begin{aligned}
F^{\alpha\beta}\lambda_\alpha^k\lambda_{\beta k}
&=F^{\alpha\beta}[-\lambda_\alpha^+\lambda_\beta^-+\lambda_\alpha^-\lambda_\beta^+]\\
&=-2F^{\alpha\beta}\lambda_\alpha^+\lambda_\beta^-
=-2F_{\delta\rho}\lambda^{\delta+}\lambda^{\rho-},\\
-\frac32B^{++}F_{\delta\rho}\lambda^{\delta+}\lambda^{\rho-}
&=\frac34B^{++}F^{\alpha\beta}\lambda_\alpha^k\lambda_{\beta k}
=\frac38B^{++}(\Sigma_{ab})^{\alpha\beta}F^{ab}\lambda_\alpha^k\lambda_{\beta k}.
\end{aligned}
\tag{S2-41}
```

For the vector term, expand the SU(2) contraction first. Applying (S2-39) to the three plus gauginos in the first term gives

```math
\begin{aligned}
&(\Gamma^a)^{\alpha\beta}\lambda_\alpha^+\lambda^{\rho+}\lambda_\beta^k\lambda_{\rho k}\\
&\quad=(\Gamma^a)^{\alpha\beta}\lambda_\alpha^+\lambda_\beta^+\lambda^{\rho+}\lambda_\rho^-
-B^{++}(\Gamma^a)^{\alpha\beta}\lambda_\alpha^+\lambda_\beta^-\\
&\quad=\frac12B^{++}(\Gamma^a)^{\alpha\beta}\varepsilon^{\rho\sigma}
(\varepsilon_{\alpha\beta}\lambda_\sigma^+-\varepsilon_{\alpha\sigma}\lambda_\beta^++\varepsilon_{\beta\sigma}\lambda_\alpha^+)\lambda_\rho^-
-B^{++}(\Gamma^a)^{\alpha\beta}\lambda_\alpha^+\lambda_\beta^-\\
&\quad=\frac12B^{++}(\Gamma^a)^{\alpha\beta}
(\lambda_\beta^+\lambda_\alpha^--\lambda_\alpha^+\lambda_\beta^-)
-B^{++}(\Gamma^a)^{\alpha\beta}\lambda_\alpha^+\lambda_\beta^-\\
&\quad=-2B^{++}(\Gamma^a)^{\alpha\beta}\lambda_\alpha^+\lambda_\beta^-.
\end{aligned}
\tag{S2-42}
```

The third-to-fourth line uses gamma tracelessness and $`\varepsilon^{\rho\sigma}\varepsilon_{\alpha\sigma}=-\delta_\alpha{}^\rho`$. The last line only relabels $`\alpha,\beta`$ and uses the antisymmetry of $`(\Gamma^a)^{\alpha\beta}`$.

Since the chosen SU(2) basis was arbitrary, the resulting symmetric-tensor identity, now without the bilinear abbreviation, is

```math
\begin{aligned}
\left.H^{ij}\right|_{W^{-5}}=\frac{3}{8W^5}\Big[&
(\Gamma^a)^{\alpha\beta}\lambda_\alpha^{(i}\lambda^{\rho j)}\lambda_\beta^k\lambda_{\rho k}\nabla_aW
+(\Sigma_{ab})^{\alpha\beta}F^{ab}\lambda^{\rho i}\lambda_\rho^j\lambda_\alpha^k\lambda_{\beta k}
+X^{kl}\lambda^{\alpha i}\lambda_\alpha^j\lambda_k^\beta\lambda_{\beta l}\Big].
\end{aligned}
\tag{S2-43}
```

Thus all three $`W^{-5}`$ terms follow from the defining operator, including their coefficients, contractions and signs. No flat specialization was required.

### 4.8 The third vector derivative, including the mixed curvature term

The $`W^{-4}`$ coefficient also needs $`\nabla_\gamma^+\nabla_\delta^+\lambda_\rho^-`$. Start with the first vector rule and differentiate every factor:

```math
\begin{aligned}
\nabla_\gamma^+\nabla_\delta^+\lambda_\rho^-
={}&-2\nabla_\gamma^+F_{\delta\rho}-2(\nabla_\gamma^+W_{\delta\rho})W-2iW_{\delta\rho}\lambda_\gamma^+
-\varepsilon_{\delta\rho}\nabla_\gamma^+X^{+-}
-(\Gamma^a)_{\delta\rho}\nabla_\gamma^+\nabla_aW.
\end{aligned}
\tag{S2-44}
```

The four derivative substitutions, before collecting them, are

```math
\begin{aligned}
-2\nabla_\gamma^+F_{\delta\rho}
={}&i\nabla_{\gamma\delta}\lambda_\rho^++i\nabla_{\gamma\rho}\lambda_\delta^+
+i\varepsilon_{\gamma\delta}\nabla_\rho{}^\tau\lambda_\tau^+
+i\varepsilon_{\gamma\rho}\nabla_\delta{}^\tau\lambda_\tau^+
+3iW_{\delta\rho}\lambda_\gamma^++2W_{\gamma\delta\rho}{}^+W\\
&-\frac i2(W_{\gamma\delta}\lambda_\rho^++W_{\gamma\rho}\lambda_\delta^+)
+\frac{3i}{2}(\varepsilon_{\gamma\delta}W_\rho{}^\tau+\varepsilon_{\gamma\rho}W_\delta{}^\tau)\lambda_\tau^+,\\
-2(\nabla_\gamma^+W_{\delta\rho})W
={}&-2W_{\gamma\delta\rho}{}^+W-(\varepsilon_{\gamma\delta}X_\rho^++\varepsilon_{\gamma\rho}X_\delta^+)W,\\
-\varepsilon_{\delta\rho}\nabla_\gamma^+X^{+-}
={}&-i\varepsilon_{\delta\rho}\nabla_\gamma{}^\tau\lambda_\tau^+
+\frac i2\varepsilon_{\delta\rho}W_{\gamma\tau}\lambda^{\tau+}
+\frac34\varepsilon_{\delta\rho}X_\gamma^+W,\\
-(\Gamma^a)_{\delta\rho}\nabla_\gamma^+\nabla_aW
={}&-i\nabla_{\delta\rho}\lambda_\gamma^+
-\frac i4(\Gamma^a)_{\delta\rho}(3\Gamma_aW-W\Gamma_a)_\gamma{}^\tau\lambda_\tau^+
+\frac14(\Gamma^a)_{\delta\rho}(\Gamma_a)_\gamma{}^\tau X_\tau^+W.
\end{aligned}
\tag{S2-45}
```

Only in the matrix products in the last line, $`W`$ denotes the Weyl matrix $`W_\alpha{}^\beta`$; it is not the scalar multiplying $`X_\tau^+`$. In particular $`W_\alpha{}^\beta\lambda_\beta=-W_{\alpha\beta}\lambda^\beta`$. This minus sign follows from raising the second matrix slot with the antisymmetric spinor metric.

The Clifford contraction needed to remove those matrix products is

```math
\begin{aligned}
(\Gamma^a)_{\delta\rho}(\Gamma_a)_{\gamma\sigma}
&=\varepsilon_{\delta\rho}\varepsilon_{\gamma\sigma}-2\varepsilon_{\delta\gamma}\varepsilon_{\rho\sigma}+2\varepsilon_{\delta\sigma}\varepsilon_{\rho\gamma},\\
(\Gamma^a)_{\delta\rho}(\Gamma_a)_\gamma{}^\tau
&=-\varepsilon_{\delta\rho}\delta_\gamma{}^\tau+2\varepsilon_{\delta\gamma}\delta_\rho{}^\tau-2\varepsilon_{\rho\gamma}\delta_\delta{}^\tau.
\end{aligned}
\tag{S2-46}
```

The first identity is the Gold Clifford completeness relation, also written in Butter et al., Appendix A, (A.26a). The second raises its last index using (S2-02). For example, the entire $`WX_\alpha^+`$ coefficient in (S2-45) becomes

```math
\begin{aligned}
&W[-\varepsilon_{\gamma\delta}X_\rho^+-\varepsilon_{\gamma\rho}X_\delta^++\tfrac34\varepsilon_{\delta\rho}X_\gamma^+
+\tfrac14(-\varepsilon_{\delta\rho}X_\gamma^++2\varepsilon_{\delta\gamma}X_\rho^+-2\varepsilon_{\rho\gamma}X_\delta^+)]\\
&\quad=W[-\tfrac32\varepsilon_{\gamma\delta}X_\rho^+-\tfrac12\varepsilon_{\gamma\rho}X_\delta^++\tfrac12\varepsilon_{\delta\rho}X_\gamma^+].
\end{aligned}
\tag{S2-47}
```

For the terms containing the Weyl two-form and a gaugino, the two matrix contractions in (S2-45) give

```math
\begin{aligned}
&(\Gamma^a)_{\delta\rho}(\Gamma_aW)_\gamma{}^\tau\lambda_\tau^+
=\varepsilon_{\delta\rho}W_{\gamma\tau}\lambda^{\tau+}
-2\varepsilon_{\delta\gamma}W_{\rho\tau}\lambda^{\tau+}
+2\varepsilon_{\rho\gamma}W_{\delta\tau}\lambda^{\tau+},\\
&(\Gamma^a)_{\delta\rho}(W\Gamma_a)_\gamma{}^\tau\lambda_\tau^+
=\varepsilon_{\delta\rho}W_{\gamma\tau}\lambda^{\tau+}
+2W_{\gamma\delta}\lambda_\rho^+-2W_{\gamma\rho}\lambda_\delta^+.
\end{aligned}
\tag{S2-48}
```

The coefficients of $`\varepsilon_{\delta\rho}W_{\gamma\tau}\lambda^{\tau+}`$ are $`1/2-3/4+1/4=0`$; those of $`\varepsilon_{\gamma\rho}W_{\delta\tau}\lambda^{\tau+}`$ are $`-3/2+3/2=0`$; those of $`\varepsilon_{\gamma\delta}W_{\rho\tau}\lambda^{\tau+}`$ sum to $`-3`$. The $`W_{\gamma\delta}\lambda_\rho^+`$ terms cancel and the $`W_{\gamma\rho}\lambda_\delta^+`$ terms sum to $`-1`$. The $`W_{\gamma\delta\rho}{}^+W`$ terms cancel between the first two lines of (S2-45). Thus the fully reduced third vector derivative is

```math
\begin{aligned}
\nabla_\gamma^+\nabla_\delta^+\lambda_\rho^-
={}&i[\nabla_{\gamma\delta}\lambda_\rho^++\nabla_{\gamma\rho}\lambda_\delta^+
+\varepsilon_{\gamma\delta}\nabla_\rho{}^\tau\lambda_\tau^+
+\varepsilon_{\gamma\rho}\nabla_\delta{}^\tau\lambda_\tau^+
-\varepsilon_{\delta\rho}\nabla_\gamma{}^\tau\lambda_\tau^+
-\nabla_{\delta\rho}\lambda_\gamma^+]\\
&+i[W_{\delta\rho}\lambda_\gamma^+-W_{\gamma\rho}\lambda_\delta^+-3\varepsilon_{\gamma\delta}W_{\rho\tau}\lambda^{\tau+}]\\
&+W[-\tfrac32\varepsilon_{\gamma\delta}X_\rho^+-\tfrac12\varepsilon_{\gamma\rho}X_\delta^++\tfrac12\varepsilon_{\delta\rho}X_\gamma^+].
\end{aligned}
\tag{S2-49}
```

Every line is antisymmetric in $`\gamma,\delta`$, as required by (S2-28). It has weight $`5/2`$. The last two lines would not follow by replacing the mixed commutator with zero.

### 4.9 Contributions to the full $`W^{-4}`$ coefficient

The six contributions at this pole are obtained directly from (S2-31) and the three product-rule terms in (S2-36):

```math
\begin{aligned}
W^4\left.H^{++}\right|_{W^{-4}}
={}&-\frac{3i}{8}X^{++}X^{--}B^{++}-\frac{3i}{16}(X^{++})^2B^{--}\\
&-\frac34B^{++}\lambda^{\rho+}\nabla_\rho{}^\tau\lambda_\tau^-
+\frac38B^{++}W_{\rho\tau}\lambda^{\rho+}\lambda^{\tau-}\\
&+\frac{3i}{16}X^{++}\lambda^{\delta+}
[4F_{\delta\rho}\lambda^{\rho-}+2X^{+-}\lambda_\delta^-+2\nabla_{\delta\rho}W\lambda^{\rho-}]\\
&-\frac{3i}{64}\varepsilon^{\alpha\beta\gamma\delta}\lambda_\alpha^+\lambda_\beta^+
\left.\nabla_\gamma^+\nabla_\delta^+B^{--}\right|_{W^0}
-\frac32B^{++}W_{\delta\rho}\lambda^{\delta+}\lambda^{\rho-}.
\end{aligned}
\tag{S2-50}
```

In this equation $`|_{W^0}`$ on a numerator retains its terms with no explicit scalar $`W`$ factor; $`\nabla_aW`$ is retained. The last term is precisely the $`W_{\delta\rho}W`$ contribution deferred after (S2-40). This notation extracts a Laurent coefficient, with the ordinary fields and their covariant derivatives held as independent jets.

To evaluate the remaining bilinear derivative, differentiate (S2-38) in its uncollected form. The two terms and their signs are

```math
\begin{aligned}
\nabla_\gamma^+\nabla_\delta^+B^{--}
&=-2(\nabla_\gamma^+\nabla_\delta^+\lambda_\rho^-)\lambda^{\rho-}
-2(\nabla_\delta^+\lambda_\rho^-)\varepsilon^{\rho\sigma}\nabla_\gamma^+\lambda_\sigma^-.
\end{aligned}
\tag{S2-51}
```

The first factor $`\nabla_\delta^+\lambda_\rho^-`$ is even, so the second term has no additional odd-product sign. In the first term substitute all of (S2-49); its last line has one explicit scalar $`W`$ and contributes at $`W^{-3}`$. In the second term substitute $`-2F_{\alpha\beta}-\varepsilon_{\alpha\beta}X^{+-}-\nabla_{\alpha\beta}W`$ for the coefficient at the present pole.

#### 4.9.1 The eight terms with two gauginos

The bispinor product needed in the second term of (S2-51) is

```math
\begin{aligned}
&[2F_{\gamma\rho}+\varepsilon_{\gamma\rho}X^{+-}+\nabla_{\gamma\rho}W]
\varepsilon^{\rho\sigma}
[2F_{\delta\sigma}+\varepsilon_{\delta\sigma}X^{+-}+\nabla_{\delta\sigma}W]\\
&\quad=4F_{\gamma\rho}\varepsilon^{\rho\sigma}F_{\sigma\delta}
-\nabla_{\gamma\rho}W\varepsilon^{\rho\sigma}\nabla_{\sigma\delta}W
+2(F_{\gamma\rho}\varepsilon^{\rho\sigma}\nabla_{\sigma\delta}W
-\nabla_{\gamma\rho}W\varepsilon^{\rho\sigma}F_{\sigma\delta})\\
&\qquad-2X^{+-}\nabla_{\gamma\delta}W-(X^{+-})^2\varepsilon_{\gamma\delta}\\
&\quad=\left[-\frac12F^{ab}F_{ab}+\nabla^aW\nabla_aW-(X^{+-})^2\right]\varepsilon_{\gamma\delta}\\
&\qquad+\left[2F_{ab}\nabla^bW-2X^{+-}\nabla_aW
+\frac14\varepsilon_a{}^{bcde}F_{bc}F_{de}\right](\Gamma^a)_{\gamma\delta}.
\end{aligned}
\tag{S2-52}
```

The nine distributed products in the first line give the four groups in the second and third lines: the two $`FX^{+-}`$ terms cancel; the two $`X^{+-}\nabla W`$ terms add; $`FF`$, $`\nabla W\nabla W`$, and $`(X^{+-})^2`$ each remain. The final equality uses the following three explicit Clifford products, with the same $`F_{ab}`$ and $`\nabla_aW`$:

```math
\begin{aligned}
\left(\frac12F_{ab}\Sigma^{ab}\right)^2
&=-\frac18F^{ab}F_{ab}\mathbf1-\frac1{16}\varepsilon^{abcde}F_{ab}F_{cd}\Gamma_e,\\
(\Gamma^a\nabla_aW)^2&=-\nabla^aW\nabla_aW\mathbf1,\\
\left[\Gamma^a\nabla_aW,\frac12F_{bc}\Sigma^{bc}\right]
&=\frac12\nabla_aW F_{bc}(\eta^{ab}\Gamma^c-\eta^{ac}\Gamma^b)
=-F_{ab}\nabla^bW\Gamma^a.
\end{aligned}
\tag{S2-53}
```

For the first line define only the conventional antisymmetric gamma $`\Gamma^{ab}=\Gamma^{[a}\Gamma^{b]}=-2\Sigma^{ab}`$. Expanding the two commutators gives

```math
\begin{aligned}
\Gamma^{ab}\Gamma^{cd}
&=\Gamma^{abcd}-\eta^{bc}\Gamma^{ad}+\eta^{ac}\Gamma^{bd}+\eta^{bd}\Gamma^{ac}-\eta^{ad}\Gamma^{bc}
+(\eta^{ad}\eta^{bc}-\eta^{ac}\eta^{bd})\mathbf1,\\
F_{ab}F_{cd}(\eta^{ad}\eta^{bc}-\eta^{ac}\eta^{bd})&=-F_{ab}F^{ab}-F_{ab}F^{ab}=-2F^{ab}F_{ab},\\
F_{ab}F_{cd}(-\eta^{bc}\Gamma^{ad}+\eta^{ac}\Gamma^{bd}+\eta^{bd}\Gamma^{ac}-\eta^{ad}\Gamma^{bc})&=0,\\
\frac1{16}F_{ab}F_{cd}\Gamma^{abcd}&=-\frac1{16}\varepsilon^{abcde}F_{ab}F_{cd}\Gamma_e.
\end{aligned}
\tag{S2-53a}
```

Each rank-two contraction in the third line is an antisymmetric gamma contracted with a symmetric tensor quadratic in $`F`$, and therefore vanishes separately. The last line uses $`\Gamma^{abcd}=-\varepsilon^{abcde}\Gamma_e`$ with the locked Gold orientation. Combining the scalar and rank-four lines and using $`(F_{ab}\Sigma^{ab}/2)^2=F_{ab}F_{cd}\Gamma^{ab}\Gamma^{cd}/16`$ proves the first line of (S2-53). The explicit frozen Clifford matrices check every two-form basis element and every pairwise polarization of this identity. The second line follows directly from the Clifford anticommutator because $`\nabla_aW\nabla_bW`$ is symmetric. The third uses the displayed commutator and then relabels $`b,c`$.

The spinor contraction in (S2-50) is reduced by expanding its three epsilon pairings:

```math
\begin{aligned}
\varepsilon^{\alpha\beta\gamma\delta}\lambda_\alpha^+\lambda_\beta^+
&=-B^{++}\varepsilon^{\gamma\delta}-2\lambda^{\gamma+}\lambda^{\delta+},\\
\varepsilon^{\alpha\beta\gamma\delta}\lambda_\alpha^+\lambda_\beta^+\varepsilon_{\gamma\delta}&=2B^{++},\qquad
\varepsilon^{\alpha\beta\gamma\delta}\lambda_\alpha^+\lambda_\beta^+(\Gamma^a)_{\gamma\delta}
=-2(\Gamma^a)^{\gamma\delta}\lambda_\gamma^+\lambda_\delta^+.
\end{aligned}
\tag{S2-54}
```

Consequently the second term of (S2-51), including its coefficient in (S2-50), supplies

```math
\begin{aligned}
&\left[\frac{3i}{32}F^{ab}F_{ab}-\frac{3i}{16}\nabla^aW\nabla_aW+\frac{3i}{16}(X^{+-})^2\right]B^{++}\\
&\quad+\frac{3i}{8}(\Gamma^a)^{\alpha\beta}F_{ab}\lambda_\alpha^+\lambda_\beta^+\nabla^bW
-\frac{3i}{8}X^{+-}(\Gamma^a)^{\alpha\beta}\lambda_\alpha^+\lambda_\beta^+\nabla_aW
+\frac{3i}{64}\varepsilon^{abcde}(\Gamma_a)^{\alpha\beta}F_{bc}F_{de}\lambda_\alpha^+\lambda_\beta^+.
\end{aligned}
\tag{S2-55}
```

The remaining two-gaugino terms are the first and third lines of (S2-50). Their $`X^2`$, $`XF`$ and $`X\nabla W`$ contractions collect as follows:

```math
\begin{aligned}
&-\frac{3i}{8}X^{++}X^{--}B^{++}-\frac{3i}{16}(X^{++})^2B^{--}
+\frac{3i}{8}X^{++}X^{+-}B^{+-}+\frac{3i}{16}(X^{+-})^2B^{++}\\
&\quad=-\frac{3i}{16}X^{++}X^{kl}B_{kl}-\frac{3i}{32}X^{kl}X_{kl}B^{++},\\
&\frac{3i}{4}X^{++}F_{\alpha\beta}\lambda^{\alpha+}\lambda^{\beta-}
=-\frac{3i}{16}X^{++}(\Sigma_{ab})^{\alpha\beta}F^{ab}\lambda_\alpha^k\lambda_{\beta k},\\
&\frac{3i}{8}(\Gamma^a)^{\alpha\beta}[X^{++}\lambda_\alpha^+\lambda_\beta^--X^{+-}\lambda_\alpha^+\lambda_\beta^+]\nabla_aW
=-\frac{3i}{8}(\Gamma^a)^{\alpha\beta}X^{k+}\lambda_\alpha^+\lambda_{\beta k}\nabla_aW.
\end{aligned}
\tag{S2-56}
```

In the first line use $`X^{kl}X_{kl}=2X^{++}X^{--}-2(X^{+-})^2`$ and $`X^{kl}B_{kl}=X^{++}B^{--}+X^{--}B^{++}-2X^{+-}B^{+-}`$. The second equality is the same symmetric-bispinor contraction explicitly evaluated in (S2-41); the last equality merely writes out the two values of $`k`$. These equations give all eight non-derivative-bilinear terms in the $`W^{-4}`$ sector.

#### 4.9.2 Four gauginos with one covariant derivative

Substitute the first line of (S2-49) into the first term of (S2-51). Its common coefficient in (S2-50) is $`(3i/32)i=-3/32`$. The six contractions before multiplying by this coefficient are recorded below. Each equation includes the actual fermion order. For compactness within each equation the common $`(\Gamma^a)^{\mu\nu}`$ is factored out, but the field products remain explicit:

```math
\begin{aligned}
&\varepsilon^{\alpha\beta\gamma\delta}\lambda_\alpha^+\lambda_\beta^+(\nabla_{\gamma\delta}\lambda_\rho^+)\lambda^{\rho-}
=2(\Gamma^a)^{\mu\nu}\lambda_\mu^+\lambda_\nu^+\lambda^{\rho-}\nabla_a\lambda_\rho^+,\\
&\varepsilon^{\alpha\beta\gamma\delta}\lambda_\alpha^+\lambda_\beta^+(\nabla_{\gamma\rho}\lambda_\delta^+)\lambda^{\rho-}
=(\Gamma^a)^{\mu\nu}\left[\frac12\lambda_\mu^+\lambda_\nu^+\lambda^{\rho-}\nabla_a\lambda_\rho^+
+\lambda_\mu^+\lambda^{\rho+}\lambda_\nu^-\nabla_a\lambda_\rho^+
+\lambda_\mu^+\lambda^{\rho+}\lambda_\rho^-\nabla_a\lambda_\nu^+
-\frac12B^{++}\lambda_\mu^-\nabla_a\lambda_\nu^+\right],\\
&\varepsilon^{\alpha\beta\gamma\delta}\lambda_\alpha^+\lambda_\beta^+\varepsilon_{\gamma\delta}(\nabla_\rho{}^\tau\lambda_\tau^+)\lambda^{\rho-}
=2(\Gamma^a)^{\mu\nu}B^{++}\lambda_\mu^-\nabla_a\lambda_\nu^+,\\
&\varepsilon^{\alpha\beta\gamma\delta}\lambda_\alpha^+\lambda_\beta^+\varepsilon_{\gamma\rho}(\nabla_\delta{}^\tau\lambda_\tau^+)\lambda^{\rho-}
=(\Gamma^a)^{\mu\nu}\left[-\frac12\lambda_\mu^+\lambda_\nu^+\lambda^{\rho-}\nabla_a\lambda_\rho^+
+\lambda_\mu^+\lambda^{\rho+}\lambda_\nu^-\nabla_a\lambda_\rho^+
+\lambda_\mu^+\lambda^{\rho+}\lambda_\rho^-\nabla_a\lambda_\nu^+
+\frac12B^{++}\lambda_\mu^-\nabla_a\lambda_\nu^+\right].
\end{aligned}
\tag{S2-57}
```

The fifth contraction, with $`-\varepsilon_{\delta\rho}\nabla_\gamma{}^\tau\lambda_\tau^+`$, equals the fourth after $`\gamma\leftrightarrow\delta`$; its explicit minus is canceled by the epsilon sign. The sixth, with $`-\nabla_{\delta\rho}\lambda_\gamma^+`$, equals the second by the same relabeling. To obtain each line, first insert (S2-54), then raise the contracted spinor index and move the odd $`\nabla\lambda`$ past $`\lambda^-`$ once. The only rearrangement needed between the four resulting products is the polarized three-spinor identity:

```math
\begin{aligned}
0=(\Gamma^a)^{\mu\nu}\big[&\lambda_\mu^+\lambda_\nu^+\lambda^{\rho-}\nabla_a\lambda_\rho^+
-2\lambda_\mu^+\lambda^{\rho+}\lambda_\nu^-\nabla_a\lambda_\rho^+
+2\lambda_\mu^+\lambda^{\rho+}\lambda_\rho^-\nabla_a\lambda_\nu^+
+B^{++}\lambda_\mu^-\nabla_a\lambda_\nu^+\big].
\end{aligned}
\tag{S2-58}
```

For its derivation replace $`\lambda^+`$ in the first line of (S2-39) by $`\lambda^++t\lambda^-`$ and equate the coefficient of the commuting variable $`t`$. The left side is $`\lambda_\alpha^+\lambda_\beta^+\lambda_\gamma^-+\lambda_\alpha^+\lambda_\beta^-\lambda_\gamma^++\lambda_\alpha^-\lambda_\beta^+\lambda_\gamma^+`$. The right side is $`\frac12B^{++}(\varepsilon_{\alpha\beta}\lambda_\gamma^--\varepsilon_{\alpha\gamma}\lambda_\beta^-+\varepsilon_{\beta\gamma}\lambda_\alpha^-)+B^{+-}(\varepsilon_{\alpha\beta}\lambda_\gamma^+-\varepsilon_{\alpha\gamma}\lambda_\beta^++\varepsilon_{\beta\gamma}\lambda_\alpha^+)`$. Contracting with the traceless antisymmetric gamma and $`\nabla_a\lambda^+`$ gives exactly (S2-58).

Adding the first, twice the second, the third, and twice the fourth lines of (S2-57) gives coefficients $`2,4,4,2`$ of the four products in that order. Multiplication by $`-3/32`$ gives $`-3/16,-3/8,-3/8,-3/16`$. Add $`-3/64`$ times the explicitly zero combination (S2-58). The coefficients become $`-15/64,-9/32,-15/32,-15/64`$. Finally include the second line of (S2-50), whose derivative term is $`+3B^{++}(\Gamma^a)^{\mu\nu}\lambda_\mu^+\nabla_a\lambda_\nu^-/4`$. Restoring the SU(2) contractions gives

```math
\begin{aligned}
&-\frac{15}{64}(\Gamma^a)^{\alpha\beta}\lambda_\alpha^+\lambda_\beta^+\lambda^{\gamma k}\nabla_a\lambda_{\gamma k}
-\frac9{32}(\Gamma^a)^{\alpha\beta}\lambda_\alpha^+\lambda^{\rho+}\lambda_\beta^k\nabla_a\lambda_{\rho k}\\
&\quad-\frac{15}{32}(\Gamma^a)^{\alpha\beta}\lambda_\alpha^+\lambda^{\rho+}\lambda_\rho^k\nabla_a\lambda_{\beta k}
-\frac{15}{64}(\Gamma^a)^{\alpha\beta}B^{++}\lambda_\alpha^k\nabla_a\lambda_{\beta k}.
\end{aligned}
\tag{S2-59}
```

One can check the restored $`\nabla\lambda^-`$ coefficient without an omitted rearrangement: expanding $`k=+,-`$ in (S2-59), the three-plus identity (S2-39) gives coefficients $`-15/64,+18/64,+30/64,+15/64`$ times $`B^{++}(\Gamma^a)^{\mu\nu}\lambda_\mu^+\nabla_a\lambda_\nu^-`$. Their sum is $`48/64=3/4`$, exactly the term in (S2-50).

#### 4.9.3 The two Weyl-tensor quartic terms

Inserting the second line of (S2-49) into (S2-51) gives zero at this pole, by the following explicit cancellation:

```math
\begin{aligned}
&\varepsilon^{\alpha\beta\gamma\delta}\lambda_\alpha^+\lambda_\beta^+
[W_{\delta\rho}\lambda_\gamma^+-W_{\gamma\rho}\lambda_\delta^+-3\varepsilon_{\gamma\delta}W_{\rho\tau}\lambda^{\tau+}]\lambda^{\rho-}\\
&\quad=6B^{++}W_{\delta\rho}\lambda^{\delta+}\lambda^{\rho-}
-6B^{++}W_{\rho\tau}\lambda^{\tau+}\lambda^{\rho-}=0.
\end{aligned}
\tag{S2-60}
```

The first equality uses (S2-39) on the first two terms and (S2-54) on the last. The final equality relabels the two indices of the symmetric Weyl bispinor. The two remaining Weyl contributions in (S2-50) therefore sum to

```math
\begin{aligned}
\left(\frac38-\frac32\right)B^{++}W_{\rho\tau}\lambda^{\rho+}\lambda^{\tau-}
&=\frac9{16}B^{++}W^{\alpha\beta}\lambda_\alpha^k\lambda_{\beta k}
=\frac9{32}(\Sigma_{ab})^{\alpha\beta}W^{ab}B^{++}\lambda_\alpha^k\lambda_{\beta k}.
\end{aligned}
\tag{S2-61}
```

To compare with the source's two written terms, apply the same actual spinor rearrangement as (S2-42), now to the symmetric $`\Sigma^{ab}`$ instead of the antisymmetric $`\Gamma^a`$. Its first three-plus contraction vanishes because $`\Sigma^{\alpha\beta}(\lambda_\beta^+\lambda_\alpha^--\lambda_\alpha^+\lambda_\beta^-)=0`$. Its second contraction gives

```math
\begin{aligned}
(\Sigma_{ab})^{\alpha\beta}\lambda_\alpha^+\lambda^{\rho+}\lambda_\beta^k\lambda_{\rho k}
&=-B^{++}(\Sigma_{ab})^{\alpha\beta}\lambda_\alpha^+\lambda_\beta^-
=\frac12B^{++}(\Sigma_{ab})^{\alpha\beta}\lambda_\alpha^k\lambda_{\beta k},\\
\frac9{32}B^{++}(\Sigma_{ab})^{\alpha\beta}W^{ab}\lambda_\alpha^k\lambda_{\beta k}
&=\frac9{32}(\Sigma_{ab})^{\alpha\beta}W^{ab}\lambda_\alpha^+\lambda^{\rho+}\lambda_\beta^k\lambda_{\rho k}
+\frac9{64}(\Sigma_{ab})^{\alpha\beta}W^{ab}B^{++}\lambda_\alpha^k\lambda_{\beta k}.
\end{aligned}
\tag{S2-62}
```

Equations (S2-55)–(S2-62) evaluate **all fourteen** $`W^{-4}`$ summands. Restoring the arbitrary symmetric indices and writing out the bilinear, their collected result is

```math
\begin{aligned}
\left.H^{ij}\right|_{W^{-4}}=\frac1{W^4}\Big[&-\frac{3i}{16}\lambda^{\alpha i}\lambda_\alpha^j\nabla^aW\nabla_aW
-\frac{3i}{8}(\Gamma^a)^{\alpha\beta}X^{k(i}\lambda_\alpha^{j)}\lambda_{\beta k}\nabla_aW
+\frac{3i}{8}(\Gamma^a)^{\alpha\beta}F_{ab}\lambda_\alpha^i\lambda_\beta^j\nabla^bW\\
&+\frac{3i}{32}F^{ab}F_{ab}\lambda^{\alpha i}\lambda_\alpha^j
+\frac{3i}{64}\varepsilon^{abcde}(\Gamma_a)^{\alpha\beta}F_{bc}F_{de}\lambda_\alpha^i\lambda_\beta^j
-\frac{3i}{16}(\Sigma_{ab})^{\alpha\beta}X^{ij}F^{ab}\lambda_\alpha^k\lambda_{\beta k}\\
&-\frac{3i}{16}X^{ij}X^{kl}\lambda_k^\alpha\lambda_{\alpha l}
-\frac{3i}{32}X^{kl}X_{kl}\lambda^{\alpha i}\lambda_\alpha^j
-\frac{15}{64}(\Gamma^a)^{\alpha\beta}\lambda_\alpha^i\lambda_\beta^j\lambda^{\gamma k}\nabla_a\lambda_{\gamma k}\\
&-\frac9{32}(\Gamma^a)^{\alpha\beta}\lambda_\alpha^{(i}\lambda^{\rho j)}\lambda_\beta^k\nabla_a\lambda_{\rho k}
-\frac{15}{32}(\Gamma^a)^{\alpha\beta}\lambda_\alpha^{(i}\lambda^{\rho j)}\lambda_\rho^k\nabla_a\lambda_{\beta k}\\
&-\frac{15}{64}(\Gamma^a)^{\alpha\beta}\lambda^{\rho i}\lambda_\rho^j\lambda_\alpha^k\nabla_a\lambda_{\beta k}
+\frac9{32}(\Sigma_{ab})^{\alpha\beta}W^{ab}\lambda_\alpha^{(i}\lambda^{\rho j)}\lambda_\beta^k\lambda_{\rho k}
+\frac9{64}(\Sigma_{ab})^{\alpha\beta}W^{ab}\lambda^{\rho i}\lambda_\rho^j\lambda_\alpha^k\lambda_{\beta k}\Big].
\end{aligned}
\tag{S2-63}
```

### 4.10 Complete extraction of the $`W^{-3}`$ coefficient

This continuation retains the assumptions in section 1. It uses S23 (2.13a–c), (2.6a–b), the projector (2.17), and C24 (A.3), without imposing a component gauge or a field equation. All eighteen structures will be obtained below. **One coefficient disagrees with the printed S23 (3.25): the derivative-of-$`X^{ij}`$ term has coefficient $`+i/4`$ in the defining-operator calculation, whereas the paper prints $`-i/4`$.** Equations (S2-79)–(S2-81) exhibit the discrepancy and an independent check. The published expression at the end of this file is preserved verbatim as a benchmark.

For readability in this continuation only, $`D_\alpha=\nabla_\alpha^+`$ and $`D^{++}=\nabla^{++}`$. $`B^{rs}=\lambda^{\alpha r}\lambda_\alpha^s`$ retains its definition in section 4.6. A subscript $`0`$ or $`1`$ on a differentiated expression below selects its coefficient of **explicit scalar** $`W^0`$ or $`W^1`$, respectively, after using the source derivative rules. It never sets $`W=0`$, never removes $`W_{\alpha\beta}`$, and never treats $`\nabla_aW`$ as zero. This selection is just the collection of the rational expression by its scalar denominator.

First, the derivatives of an ordinary even function are

```math
\begin{aligned}
D_\alpha f&=if'\lambda_\alpha^+,\\
D_\alpha D_\beta f&=-f''\lambda_\alpha^+\lambda_\beta^+-if'\varepsilon_{\alpha\beta}X^{++},\\
D_\alpha D_\beta D_\gamma f
&=-if'''\lambda_\alpha^+\lambda_\beta^+\lambda_\gamma^+
+f''X^{++}(\varepsilon_{\alpha\beta}\lambda_\gamma^+-\varepsilon_{\alpha\gamma}\lambda_\beta^++\varepsilon_{\beta\gamma}\lambda_\alpha^+),\\
\varepsilon^{\alpha\beta\gamma\delta}D_\alpha D_\beta D_\gamma f
&=-3if'''B^{++}\lambda^{\delta+}+6f''X^{++}\lambda^{\delta+}.
\end{aligned}
\tag{S2-64}
```

The second line uses $`D_\alpha\lambda_\beta^+=-\varepsilon_{\alpha\beta}X^{++}`$. In the third line, differentiating the second gaugino gives a minus sign from crossing the first odd gaugino. The last line inserts (S2-39) and contracts the three spinor metrics; the three identical contributions give the factors $`3`$ and $`6`$.

Insert (S2-64) and (S2-35) into the two products in (S2-31), using the three cross terms in (S2-36). The full coefficient multiplying $`W^{-3}`$ in $`H^{++}`$ is

```math
\begin{aligned}
\left.H^{++}\right|_{W^{-3}}=W^{-3}\Big\{&-\frac14(X^{++})^2X^{--}
+\frac i2X^{++}\lambda^{\alpha+}\big(\nabla_\alpha{}^\beta\lambda_\beta^--\tfrac12W_{\alpha\beta}\lambda^{\beta-}\big)
-\frac1{16}\varepsilon^{\alpha\beta\gamma\delta}\lambda_\alpha^+\lambda_\beta^+(D_\gamma D_\delta X^{--})_0\\
&-\frac{9i}{16}B^{++}\lambda^{\alpha+}X_\alpha^-
+\frac{3i}{4}X^{++}\lambda^{\alpha+}W_{\alpha\beta}\lambda^{\beta-}
-\frac1{64}X^{++}\varepsilon^{\alpha\beta\gamma\delta}\varepsilon_{\alpha\beta}(D_\gamma D_\delta B^{--})_0\\
&-\frac{3i}{64}\varepsilon^{\alpha\beta\gamma\delta}\lambda_\alpha^+\lambda_\beta^+(D_\gamma D_\delta B^{--})_1
-\frac1{16}\lambda^{\alpha+}(D_\alpha D^{++}\lambda_\rho^-)_0\lambda^{\rho-}\\
&+\frac1{16}\varepsilon^{\alpha\beta\gamma\delta}\lambda_\alpha^+(D_\beta D_\gamma\lambda_\rho^-)_0\varepsilon^{\rho\sigma}
(-2F_{\delta\sigma}-\varepsilon_{\delta\sigma}X^{+-}-\nabla_{\delta\sigma}W)\Big\}.
\end{aligned}
\tag{S2-65}
```

Here is the origin of every coefficient in that expression. From the first product, $`-\tfrac12(\Delta W^{-1})X^{--}`$ gives $`-1/4`$; its $`3+1`$ cross term gives $`(1/48)(6)(2)(2i)=i/2`$ and $`(1/48)(18i)(-3/2)=-9i/16`$; its $`2+2`$ cross term gives $`(1/32)(-2)=-1/16`$. From the second product, its $`3+1`$ term containing $`W_{\alpha\beta}W`$ gives $`(i/192)(6)(6)(4)=3i/4`$; its $`2+2`$ term gives $`(i/128)(2i)=-1/64`$ and $`(i/128)(-6)=-3i/64`$. Finally, its $`1+3`$ term has $`(i/192)(-2i)=1/96`$. The last two terms of (S2-65) follow from

```math
\begin{aligned}
D_\delta B^{--}&=-2(D_\delta\lambda_\rho^-)\lambda^{\rho-},\\
D_\gamma D_\delta B^{--}
&=-2(D_\gamma D_\delta\lambda_\rho^-)\lambda^{\rho-}
-2(D_\delta\lambda_\rho^-)\varepsilon^{\rho\sigma}(D_\gamma\lambda_\sigma^-),\\
\varepsilon^{\alpha\beta\gamma\delta}\lambda_\alpha^+D_\beta D_\gamma D_\delta B^{--}
&=-2\varepsilon^{\alpha\beta\gamma\delta}\lambda_\alpha^+(D_\beta D_\gamma D_\delta\lambda_\rho^-)\lambda^{\rho-}
+6\varepsilon^{\alpha\beta\gamma\delta}\lambda_\alpha^+(D_\beta D_\gamma\lambda_\rho^-)\varepsilon^{\rho\sigma}D_\delta\lambda_\sigma^-,\\
\varepsilon^{\alpha\beta\gamma\delta}\lambda_\alpha^+D_\beta D_\gamma D_\delta\lambda_\rho^-&=3\lambda^{\alpha+}D_\alpha D^{++}\lambda_\rho^-.
\end{aligned}
\tag{S2-66}
```

For the second line, $`D_\delta\lambda`$ is even, so its product with the last gaugino differentiates with a plus sign. At the next derivative, $`D_\gamma D_\delta\lambda`$ is odd, so the derivative on the last gaugino changes sign. The three placements of the single derivative become equal after antisymmetrization, giving $`+6`$. To obtain the last line, expand $`\varepsilon^{\alpha\beta\gamma\delta}=\varepsilon^{\alpha\beta}\varepsilon^{\gamma\delta}-\varepsilon^{\alpha\gamma}\varepsilon^{\beta\delta}+\varepsilon^{\alpha\delta}\varepsilon^{\beta\gamma}`$ and use $`D^{++}=-\varepsilon^{\gamma\delta}D_\gamma D_\delta`$; reordering three odd derivatives gives $`-3D^{\alpha+}D^{++}\lambda_\rho^-`$ before multiplication by $`\lambda_\alpha^+`$. Then $`\lambda_\alpha^+D^{\alpha+}=-\lambda^{\alpha+}D_\alpha`$ gives the displayed plus sign. Multiplying by $`1/96`$ gives the two coefficients $`-1/16`$ and $`+1/16`$ in (S2-65).

No further product can have this pole: $`W^{-1}\Delta X^{--}`$ starts at $`W^{-1}`$, $`W^{-2}\Delta B^{--}`$ starts at $`W^{-2}`$, and all source descendants of the vector multiplet are polynomial in its fields. There are no hidden inverse powers in these descendants. The explicit-$`W`$ contributions retained in the fourth, fifth and seventh terms of (S2-65) are essential.

### 4.11 Mixed commutators on the gaugino and the required fourth derivative

For $`[D_\alpha,\nabla_a]`$, reverse the order tabulated in C24 (A.3). Thus the torsion and curvature actions have **plus** signs. The required coefficients are

```math
\begin{aligned}
T_{a\alpha}{}^\gamma&=\tfrac14(3\Gamma_aW-W\Gamma_a)_\alpha{}^\gamma,\qquad
R(\mathbb D)_{a\alpha}{}^+=-\tfrac14(\Gamma_a)_\alpha{}^\tau X_\tau^+,\\
R(J)_{a\alpha}{}^{+,kl}&=-\tfrac34(\Gamma_a)_\alpha{}^\tau\varepsilon^{+(k}X_\tau^{l)},\\
R(M)_{a\alpha}{}^{+,cd}&=-(\Gamma_a)_\alpha{}^\tau W^{cd}{}_{\tau}^+
-\tfrac14\varepsilon_a{}^{cdef}W_{ef\alpha}^+
+\tfrac12\delta_a{}^{[c}(\Gamma^{d]})_\alpha{}^\tau X_\tau^+ .
\end{aligned}
\tag{S2-67}
```

The matrix $`W`$ in the first line means $`W_\alpha{}^\beta=-W_{\alpha\gamma}\varepsilon^{\gamma\beta}`$, never the vector scalar. On a lower spinor, $`M_{cd}\lambda_\rho=(\Sigma_{cd})_\rho{}^\tau\lambda_\tau`$; $`\mathbb D\lambda=3\lambda/2`$; $`J^{kl}\lambda^j=\varepsilon^{j(k}\lambda^{l)}`$. The $`K`$ action vanishes. The S action is S23 (2.15), $`S_{\tau k}\lambda_\rho^j=-2i\varepsilon_{\tau\rho}\delta_k{}^jW`$.

The Clifford contraction used to evaluate these generator actions is (S2-46), equivalently

```math
\sum_a(\Gamma^a)_\beta{}^\rho(\Gamma_a)_\alpha{}^\tau
=\delta_\beta{}^\rho\delta_\alpha{}^\tau
-2\varepsilon_{\alpha\beta}\varepsilon^{\rho\tau}
-2\delta_\alpha{}^\rho\delta_\beta{}^\tau.
\tag{S2-68}
```

For example, its contraction with $`X_\tau^+\lambda_\rho^-`$ is
$`X_\alpha^+\lambda_\beta^--2\varepsilon_{\alpha\beta}X^{\rho+}\lambda_\rho^--2X_\beta^+\lambda_\alpha^-`$. Inserting (S2-67), converting $`W_{ab\alpha}=(\Sigma_{ab})^{\rho\sigma}W_{\rho\sigma\alpha}`$ and using the symmetry of the three-spinor gives the separate Lorentz and dilatation/SU(2) actions

```math
\begin{aligned}
&\tfrac12(\Gamma^a)_\beta{}^\rho R(M)_{a\alpha}{}^{+,cd}(\Sigma_{cd})_\rho{}^\tau\lambda_\tau^j
=\tfrac12W_{\alpha\beta\tau}^+\lambda^{\tau j}
-\varepsilon_{\alpha\beta}X^{\tau+}\lambda_\tau^j
+\tfrac12X_\alpha^+\lambda_\beta^j-X_\beta^+\lambda_\alpha^j,\\
&\left.(\Gamma^a)_\beta{}^\rho\{R(\mathbb D)\mathbb D+R(J)J\}\lambda_\rho^+\right.=0,\\
&\left.(\Gamma^a)_\beta{}^\rho\{R(\mathbb D)\mathbb D+R(J)J\}\lambda_\rho^-\right.
=-\tfrac34X_\alpha^+\lambda_\beta^-+\tfrac32\varepsilon_{\alpha\beta}X^{\tau+}\lambda_\tau^-+\tfrac32X_\beta^+\lambda_\alpha^-\\
&\hspace{32mm}+\tfrac34X_\alpha^-\lambda_\beta^+-\tfrac32\varepsilon_{\alpha\beta}X^{\tau-}\lambda_\tau^+-\tfrac32X_\beta^-\lambda_\alpha^+.
\end{aligned}
\tag{S2-69}
```

In the second line the coefficients are $`(-1/4)(3/2)+3/8=0`$. In the last two lines, before the Clifford contraction, the coefficients multiplying $`(\Gamma_a)_\alpha{}^\tau X_\tau^+\lambda_\rho^-`$ and $`(\Gamma_a)_\alpha{}^\tau X_\tau^-\lambda_\rho^+`$ are $`-3/4`$ and $`+3/4`$. Applying (S2-68) gives all six displayed terms, with no interchange of the two odd fields.

For the first line, the two $`W_{ab\alpha}`$ pieces of (S2-67) reduce to $`W_{\alpha\beta\tau}^+\lambda^{\tau j}/2`$; the $`X`$ piece reduces to the other three terms. A direct form of the matrix identities, with the spinor multiplying on the right left visible, is

```math
\begin{aligned}
&\tfrac12(\Gamma^a)_\beta{}^\rho\Big[-(\Gamma_a)_\alpha{}^\kappa(\Sigma^{cd})^{\mu\nu}W_{\mu\nu\kappa}^+
-\tfrac14\varepsilon_a{}^{cdef}(\Sigma_{ef})^{\mu\nu}W_{\mu\nu\alpha}^+\Big](\Sigma_{cd})_\rho{}^\tau\lambda_\tau^j
=\tfrac12W_{\alpha\beta\tau}^+\lambda^{\tau j},\\
&\tfrac14(\Gamma^a)_\beta{}^\rho\delta_a{}^{[c}(\Gamma^{d]})_\alpha{}^\kappa X_\kappa^+(\Sigma_{cd})_\rho{}^\tau\lambda_\tau^j
=-\varepsilon_{\alpha\beta}X^{\tau+}\lambda_\tau^j+\tfrac12X_\alpha^+\lambda_\beta^j-X_\beta^+\lambda_\alpha^j.
\end{aligned}
\tag{S2-70}
```

These are applications of $`\Sigma^{ab}=-[\Gamma^a,\Gamma^b]/4`$, (S2-68), and the four-gamma duality used in (S2-53). The independent verifier checks the identities on all twenty symmetric components of $`W_{\alpha\beta\gamma}`$ and all four components of $`X_\alpha`$, rather than assuming a gamma-trace condition on an arbitrary spinor.

For $`\lambda^+`$, the ordinary derivative, torsion, Lorentz and S terms are now

```math
\begin{aligned}
D_\alpha\nabla_\rho{}^\beta\lambda_\beta^+
={}&\nabla_{\alpha\rho}X^{++}+\tfrac12W_{\alpha\rho}X^{++}-\tfrac{3i}{4}WX_{\alpha\rho}^{++}
+\tfrac12W_{\alpha\rho\tau}^+\lambda^{\tau+}\\
&-\varepsilon_{\alpha\rho}X^{\tau+}\lambda_\tau^+
+\tfrac12X_\alpha^+\lambda_\rho^+-X_\rho^+\lambda_\alpha^+.
\end{aligned}
\tag{S2-71}
```

The ordinary term follows from $`-(\Gamma^a)_\rho{}^\beta\varepsilon_{\alpha\beta}\nabla_aX^{++}=(\Gamma^a)_{\alpha\rho}\nabla_aX^{++}`$. The torsion contraction is
$`-(\Gamma^a)_\rho{}^\beta(3\Gamma_aW-W\Gamma_a)_\alpha{}^\gamma\varepsilon_{\gamma\beta}/4=W_{\alpha\rho}/2`$.
For S, the same-SU part of C24 (A.3e) is $`X_{cd}^{++}(\Sigma^{cd}\Gamma_a-2\Gamma_a\Sigma^{cd})/16`$; multiplication by $`-2iW\varepsilon_{\gamma\beta}`$ and contraction with $`(\Gamma^a)_\rho{}^\beta`$ gives $`-3iWX_{\alpha\rho}^{++}/4`$. All remaining terms of that curvature carry $`\varepsilon^{++}=0`$.

Trace (S2-49) first; then differentiate the traced result. This requires no interchange of vector derivatives:

```math
\begin{aligned}
D^{++}\lambda_\rho^-&=4i\nabla_\rho{}^\tau\lambda_\tau^+-10iW_{\rho\tau}\lambda^{\tau+}-7WX_\rho^+,\\
4iD_\alpha(\nabla_\rho{}^\tau\lambda_\tau^+)
&=4i\nabla_{\alpha\rho}X^{++}+2iW_{\alpha\rho}X^{++}+3WX_{\alpha\rho}^{++}
+2iW_{\alpha\rho\tau}^+\lambda^{\tau+}-4i\varepsilon_{\alpha\rho}X^{\tau+}\lambda_\tau^+
+2iX_\alpha^+\lambda_\rho^+-4iX_\rho^+\lambda_\alpha^+,\\
-10iD_\alpha(W_{\rho\tau}\lambda^{\tau+})
&=-10iW_{\alpha\rho\tau}^+\lambda^{\tau+}+5i\varepsilon_{\alpha\rho}X^{\tau+}\lambda_\tau^+
-5iX_\rho^+\lambda_\alpha^+-10iW_{\alpha\rho}X^{++},\\
-7D_\alpha(WX_\rho^+)&=+7iX_\rho^+\lambda_\alpha^+-7WX_{\alpha\rho}^{++},\\
D_\alpha D^{++}\lambda_\rho^-
&=4i\nabla_{\alpha\rho}X^{++}-8iW_{\alpha\rho}X^{++}-4WX_{\alpha\rho}^{++}
-8iW_{\alpha\rho\tau}^+\lambda^{\tau+}
+i\varepsilon_{\alpha\rho}X^{\tau+}\lambda_\tau^++2iX_\alpha^+\lambda_\rho^+-2iX_\rho^+\lambda_\alpha^+.
\end{aligned}
\tag{S2-72}
```

The third line uses S23 (2.6a) and $`D_\alpha\lambda^{\tau+}=\delta_\alpha{}^\tau X^{++}`$. In the fourth line, $`\lambda_\alpha^+X_\rho^+=-X_\rho^+\lambda_\alpha^+`$ gives the displayed plus sign. This supplies the eighth term of (S2-65), including its Weyl-spinor contributions.

### 4.12 The two derivatives of $`X^{--}`$, with every source term retained at this pole

Differentiate S23 (2.13c) directly:

```math
\begin{aligned}
D_\beta X^{--}&=2i\nabla_\beta{}^\rho\lambda_\rho^--iW_{\beta\rho}\lambda^{\rho-}-\tfrac32WX_\beta^-,\\
(D_\alpha D_\beta X^{--})_0
={}&2i(\Gamma^a)_\beta{}^\rho\nabla_a(-2F_{\alpha\rho}-\varepsilon_{\alpha\rho}X^{+-}-\nabla_{\alpha\rho}W)
-4i(\Gamma^a)_\beta{}^\rho W_{\alpha\rho}\nabla_aW\\
&+\tfrac i2(\Gamma^a)_\beta{}^\rho(3\Gamma_aW-W\Gamma_a)_\alpha{}^\gamma
(-2F_{\gamma\rho}-\varepsilon_{\gamma\rho}X^{+-}-\nabla_{\gamma\rho}W)\\
&+2i\Big[\tfrac12W_{\alpha\beta\tau}^+\lambda^{\tau-}
+\tfrac12\varepsilon_{\alpha\beta}X^{\tau+}\lambda_\tau^--\tfrac14X_\alpha^+\lambda_\beta^-+\tfrac12X_\beta^+\lambda_\alpha^-\\
&\hspace{14mm}+\tfrac34X_\alpha^-\lambda_\beta^+-\tfrac32\varepsilon_{\alpha\beta}X^{\tau-}\lambda_\tau^+-\tfrac32X_\beta^-\lambda_\alpha^+\Big]\\
&-i\big(W_{\alpha\beta\rho}^++\tfrac12\varepsilon_{\alpha\beta}X_\rho^++\tfrac12\varepsilon_{\alpha\rho}X_\beta^+\big)\lambda^{\rho-}
-iW_{\beta\rho}\varepsilon^{\rho\sigma}(-2F_{\alpha\sigma}-\varepsilon_{\alpha\sigma}X^{+-}-\nabla_{\alpha\sigma}W)
+\tfrac{3i}{2}X_\beta^-\lambda_\alpha^+.
\end{aligned}
\tag{S2-73}
```

The first line after the equality differentiates the vector rule inside the ordinary vector derivative. In particular, differentiating $`-2W_{\alpha\rho}W`$ retains $`-2W_{\alpha\rho}\nabla_aW`$ at this pole; $`(\nabla_aW_{\alpha\rho})W`$ belongs to the next pole. The second line is torsion; the bracket is the sum of the Lorentz and dilatation/SU(2) actions in (S2-69). The last line differentiates the explicit Weyl tensor and the last two factors of $`D_\beta X^{--}`$. All S-curvature actions on $`\lambda^-`$ have an explicit scalar $`W`$ and therefore belong to lower poles. Their exclusion from (S2-73) is pole collection, not a claim that these actions vanish.

The $`W_{\alpha\beta\rho}^+\lambda^{\rho-}`$ coefficients are $`2i(1/2)-i=0`$. The remaining Weyl-spinor part, written with the Weyl spinor first, is

```math
\begin{aligned}
(D_\alpha D_\beta X^{--})_{X_\gamma\lambda}
={}&\tfrac{3i}{2}\varepsilon_{\alpha\beta}X^{\rho+}\lambda_\rho^-
-\tfrac i2X_\alpha^+\lambda_\beta^-+\tfrac i2X_\beta^+\lambda_\alpha^-\\
&+\tfrac{3i}{2}X_\alpha^-\lambda_\beta^+-\tfrac{3i}{2}X_\beta^-\lambda_\alpha^+
-3i\varepsilon_{\alpha\beta}X^{\rho-}\lambda_\rho^+.
\end{aligned}
\tag{S2-74}
```

For instance, the first coefficient is $`i+i/2=3i/2`$, since $`X_\rho^+\lambda^{\rho-}=-X^{\rho+}\lambda_\rho^-`$. The $`X_\beta^+\lambda_\alpha^-`$ coefficient is $`i-i/2=i/2`$, and the $`X_\beta^-\lambda_\alpha^+`$ coefficient is $`-3i+3i/2=-3i/2`$. Equation (S2-74) is antisymmetric in $`\alpha,\beta`$, as required by $`\{D_\alpha,D_\beta\}=0`$.

### 4.13 Bosonic terms and the three derivatives of bosonic fields

The scalar part of the sixth term of (S2-65) is obtained by substituting the second term in the second line of (S2-66). Its full contraction is

```math
\begin{aligned}
&\frac{X^{++}}{32}\varepsilon^{\alpha\beta\gamma\delta}\varepsilon_{\alpha\beta}
(-2F_{\delta\rho}-\varepsilon_{\delta\rho}X^{+-}-\nabla_{\delta\rho}W)\varepsilon^{\rho\sigma}
(-2F_{\gamma\sigma}-\varepsilon_{\gamma\sigma}X^{+-}-\nabla_{\gamma\sigma}W)\\
&\quad=\frac18X^{++}F^{ab}F_{ab}+\frac14X^{++}(X^{+-})^2-\frac14X^{++}(\nabla^aW)\nabla_aW.
\end{aligned}
\tag{S2-75}
```

To see each coefficient, use $`\varepsilon^{\alpha\beta\gamma\delta}\varepsilon_{\alpha\beta}=-2\varepsilon^{\gamma\delta}`$. The remaining quadratic contraction, before the factor $`X^{++}/32`$, has diagonal contributions $`4F^{ab}F_{ab}`$, $`8(X^{+-})^2`$, and $`-8(\nabla W)^2`$. Its three mixed contributions vanish: $`\mathop{\mathrm{tr}}\nolimits\Sigma^{ab}=0`$, $`\mathop{\mathrm{tr}}\nolimits\Gamma^a=0`$, and $`\mathop{\mathrm{tr}}\nolimits(\Sigma^{ab}\Gamma^c)=0`$. These traces follow by taking the trace of the Clifford algebra; the diagonal factors follow from the two squares (S2-53). Add the first term of (S2-65) and use
$`X^{kl}X_{kl}=2X^{++}X^{--}-2(X^{+-})^2`$:

```math
-\tfrac14(X^{++})^2X^{--}+\tfrac14X^{++}(X^{+-})^2
=-\tfrac18X^{++}X^{kl}X_{kl}.
\tag{S2-76}
```

Next contract the first derivative line in (S2-73) against the third term of (S2-65). The identity

```math
\varepsilon^{\alpha\beta\gamma\delta}\lambda_\alpha^+\lambda_\beta^+
=-B^{++}\varepsilon^{\gamma\delta}-2\lambda^{\gamma+}\lambda^{\delta+}
\tag{S2-77}
```

is (S2-52), obtained by expanding the three metric products in the four-index epsilon. Its application to the $`\nabla F`$ and ordered Hessian terms gives, with their original coefficients,

```math
\begin{aligned}
&\frac i4\varepsilon^{\alpha\beta\gamma\delta}\lambda_\alpha^+\lambda_\beta^+(\Gamma^a)_\delta{}^\rho\nabla_aF_{\gamma\rho}
=-\frac i4(\Gamma^a)^{\alpha\beta}\lambda_\alpha^+\lambda_\beta^+\nabla^cF_{ac},\\
&\frac i8\varepsilon^{\alpha\beta\gamma\delta}\lambda_\alpha^+\lambda_\beta^+(\Gamma^a)_\delta{}^\rho(\Gamma^b)_{\gamma\rho}\nabla_a\nabla_bW
=\frac i4B^{++}\Box W.
\end{aligned}
\tag{S2-78}
```

For the first line, insert $`F_{\gamma\rho}=\tfrac12(\Sigma^{bc})_{\gamma\rho}F_{bc}`$ and expand $`\Gamma^a\Sigma^{bc}`$ into its three-gamma and metric pieces. The three-gamma piece has symmetric raised spinor indices and hence contracts to zero with $`\lambda_\alpha^+\lambda_\beta^+`$; the two metric pieces give $`-\nabla^cF_{ac}`$. For the second line, $`\Gamma^a\Gamma^b=-\eta^{ab}\mathbf1-2\Sigma^{ab}`$ leaves only the metric trace: the $`\Sigma^{ab}`$ piece again has symmetric spinor indices. Thus no commutation of $`\nabla_a,\nabla_b`$ is made. In particular, the torsion commutator in C24 (A.4) is not silently set to zero. The symmetric spinor part of $`\nabla_\alpha{}^\rho F_{\beta\rho}`$, fixed by S23 (2.14), drops out of this contraction for the same reason. The Bianchi identity is respected, but does not add a term to this pole.

The derivative-of-auxiliary term must be kept separately because of the source discrepancy. Its two origins are

```math
\begin{aligned}
(D_\gamma D_\delta X^{--})_{\nabla X}
&=-2i(\Gamma^a)_\delta{}^\rho\varepsilon_{\gamma\rho}\nabla_aX^{+-}
=2i(\Gamma^a)_{\gamma\delta}\nabla_aX^{+-},\\
-\tfrac1{16}\varepsilon^{\alpha\beta\gamma\delta}\lambda_\alpha^+\lambda_\beta^+(D_\gamma D_\delta X^{--})_{\nabla X}
&=+\tfrac i4(\Gamma^a)^{\alpha\beta}\lambda_\alpha^+\lambda_\beta^+\nabla_aX^{+-},\\
-\tfrac1{16}\lambda^{\alpha+}(D_\alpha D^{++}\lambda_\rho^-)_{\nabla X}\lambda^{\rho-}
&=-\tfrac i4\lambda^{\alpha+}(\Gamma^a)_{\alpha\rho}\lambda^{\rho-}\nabla_aX^{++}
=-\tfrac i4(\Gamma^a)^{\alpha\beta}\lambda_\alpha^+\lambda_\beta^-\nabla_aX^{++},\\
\text{sum}&=+\tfrac i4(\Gamma^a)^{\alpha\beta}\lambda_\alpha^+(\nabla_aX^{+l})\lambda_{\beta l}.
\end{aligned}
\tag{S2-79}
```

The second line uses $`\varepsilon^{\alpha\beta\gamma\delta}(\Gamma^a)_{\gamma\delta}=-2(\Gamma^a)^{\alpha\beta}`$. The last line uses **both** $`\lambda_{\beta+}=-\lambda_\beta^-`$ and $`\lambda_{\beta-}=\lambda_\beta^+`$. No odd fields cross in moving $`\nabla_aX`$, which is even. Therefore SU(2) covariance gives

```math
\left.H^{ij}\right|_{W^{-3}\nabla X}
=+\frac{i}{4W^3}(\Gamma^a)^{\alpha\beta}\lambda_\alpha^{(i}(\nabla_aX^{j)l})\lambda_{\beta l}.
\tag{S2-80}
```

This differs in sign from S23 (3.25), PDF21 / printed20. A flat local jet makes the discrepancy explicit. At a point take the Weyl multiplet, $`F`$, $`X`$, $`\nabla W`$, $`\nabla\lambda`$ and the Hessian of $`W`$ to vanish, retain $`\nabla_0X^{+-}=q`$, and retain two independent Grassmann components $`\lambda_1^+=\vartheta_1`$, $`\lambda_2^+=\vartheta_2`$. In the locked matrix representation $`(\Gamma^0)^{12}=-1`$, $`(\Gamma^0)^{21}=1`$, so

```math
(\Gamma^0)^{\alpha\beta}\lambda_\alpha^+\lambda_\beta^+=-2\vartheta_1\vartheta_2,
\qquad
\left.H^{++}\right|_{\text{definition}}=-\frac{iq}{2W^3}\vartheta_1\vartheta_2,
\qquad
\left.H^{++}\right|_{\text{printed (3.25)}}=+\frac{iq}{2W^3}\vartheta_1\vartheta_2.
\tag{S2-81}
```

These are coefficient probes in the complexified Grassmann algebra; they do not impose a nonzero classical value on an odd field. The symplectic-Majorana real form does not identify the two distinct polynomials. A separate calculation applies the **original six derivatives** of (S2-01), with its four-index SU(2) symmetrization, to the flat vector rules. It verifies all fifteen $`\nabla_aX^{ij}`$ components and agrees with (S2-79), without using (S2-72), (S2-73), or their contracted coefficients. See [the independent calculation](../../../../../../references/source_evidence/log/results/gauged_full_fermionic_log/scripts/verify_log_step2_w3_flat_gradient_x.py) and [its exact report](../../../../../../references/source_evidence/log/results/gauged_full_fermionic_log/sources/step2/w3_flat_gradient_x_checks.json). There is no integration by parts or on-shell equivalence that can repair this local sign comparison.

### 4.14 All gaugino-derivative contractions

The derivative part of (S2-49) has six summands. They enter the last term of (S2-65) with the original order $`\lambda_\alpha^+\nabla\lambda^+`$; no Grassmann interchange is implicit. The following lines give **each** contraction with $`F`$. They use (S2-68), $`F_{\alpha\beta}=\Sigma^{ab}_{\alpha\beta}F_{ab}/2`$, and the Clifford product $`\Gamma^a\Gamma^b=-\eta^{ab}-2\Sigma^{ab}`$, with its three-gamma duality. In particular, the four-index epsilon is expanded before the two-form conversion.

```math
\begin{aligned}
&-\tfrac i8\varepsilon^{\alpha\beta\gamma\delta}\lambda_\alpha^+(\nabla_{\beta\gamma}\lambda_\rho^+)F_\delta{}^\rho
=-\tfrac i{16}\varepsilon^{abcde}(\Sigma_{ab})^{\alpha\beta}F_{de}\lambda_\alpha^+\nabla_c\lambda_\beta^+
-\tfrac i8(\Gamma^a)^{\alpha\beta}F_{ab}\lambda_\alpha^+\nabla^b\lambda_\beta^+,\\
&-\tfrac i8\varepsilon^{\alpha\beta\gamma\delta}\lambda_\alpha^+(\nabla_{\beta\rho}\lambda_\gamma^+)F_\delta{}^\rho
=-\tfrac i8(\Gamma^a)^{\alpha\beta}F_{ab}\lambda_\alpha^+\nabla^b\lambda_\beta^+,\\
&-\tfrac i8\varepsilon^{\alpha\beta\gamma\delta}\lambda_\alpha^+\varepsilon_{\beta\gamma}(\nabla_\rho{}^\tau\lambda_\tau^+)F_\delta{}^\rho
=-\tfrac i{16}\varepsilon^{abcde}(\Sigma_{ab})^{\alpha\beta}F_{de}\lambda_\alpha^+\nabla_c\lambda_\beta^+
+\tfrac i8(\Gamma^a)^{\alpha\beta}F_{ab}\lambda_\alpha^+\nabla^b\lambda_\beta^+,\\
&-\tfrac i8\varepsilon^{\alpha\beta\gamma\delta}\lambda_\alpha^+\varepsilon_{\beta\rho}(\nabla_\gamma{}^\tau\lambda_\tau^+)F_\delta{}^\rho=0,
\qquad
+\tfrac i8\varepsilon^{\alpha\beta\gamma\delta}\lambda_\alpha^+\varepsilon_{\gamma\rho}(\nabla_\beta{}^\tau\lambda_\tau^+)F_\delta{}^\rho=0,\\
&+\tfrac i8\varepsilon^{\alpha\beta\gamma\delta}\lambda_\alpha^+(\nabla_{\gamma\rho}\lambda_\beta^+)F_\delta{}^\rho
=-\tfrac i8(\Gamma^a)^{\alpha\beta}F_{ab}\lambda_\alpha^+\nabla^b\lambda_\beta^+.
\end{aligned}
\tag{S2-82}
```

In the fourth line, $`\varepsilon_{\beta\rho}F_\delta{}^\rho=F_{\delta\beta}`$ and $`\varepsilon_{\gamma\rho}F_\delta{}^\rho=F_{\delta\gamma}`$ are symmetric in two antisymmetrized epsilon slots. That proves both zeroes. The epsilon/two-form coefficients add to $`-1/16-1/16=-1/8`$; the vector coefficients add to $`-1/8-1/8+1/8-1/8=-1/4`$.

For the scalar gradient the same six substitutions are

```math
\begin{aligned}
&-\tfrac i{16}\varepsilon^{\alpha\beta\gamma\delta}\lambda_\alpha^+(\nabla_{\beta\gamma}\lambda_\rho^+)\nabla_\delta{}^\rho W
=\tfrac i8(\nabla^aW)\lambda^{\alpha+}\nabla_a\lambda_\alpha^+
+\tfrac i4(\Sigma_{ab})^{\alpha\beta}(\nabla^aW)\lambda_\alpha^+\nabla^b\lambda_\beta^+,\\
&-\tfrac i{16}\varepsilon^{\alpha\beta\gamma\delta}\lambda_\alpha^+(\nabla_{\beta\rho}\lambda_\gamma^+)\nabla_\delta{}^\rho W
=\tfrac i8(\nabla^aW)\lambda^{\alpha+}\nabla_a\lambda_\alpha^+,\\
&-\tfrac i{16}\varepsilon^{\alpha\beta\gamma\delta}\lambda_\alpha^+\varepsilon_{\beta\gamma}(\nabla_\rho{}^\tau\lambda_\tau^+)\nabla_\delta{}^\rho W
=\tfrac i8(\nabla^aW)\lambda^{\alpha+}\nabla_a\lambda_\alpha^+
-\tfrac i4(\Sigma_{ab})^{\alpha\beta}(\nabla^aW)\lambda_\alpha^+\nabla^b\lambda_\beta^+,\\
&-\tfrac i{16}\varepsilon^{\alpha\beta\gamma\delta}\lambda_\alpha^+\varepsilon_{\beta\rho}(\nabla_\gamma{}^\tau\lambda_\tau^+)\nabla_\delta{}^\rho W
=\tfrac i8(\nabla^aW)\lambda^{\alpha+}\nabla_a\lambda_\alpha^+
-\tfrac i4(\Sigma_{ab})^{\alpha\beta}(\nabla^aW)\lambda_\alpha^+\nabla^b\lambda_\beta^+,\\
&+\tfrac i{16}\varepsilon^{\alpha\beta\gamma\delta}\lambda_\alpha^+\varepsilon_{\gamma\rho}(\nabla_\beta{}^\tau\lambda_\tau^+)\nabla_\delta{}^\rho W
=\tfrac i8(\nabla^aW)\lambda^{\alpha+}\nabla_a\lambda_\alpha^+
-\tfrac i4(\Sigma_{ab})^{\alpha\beta}(\nabla^aW)\lambda_\alpha^+\nabla^b\lambda_\beta^+,\\
&+\tfrac i{16}\varepsilon^{\alpha\beta\gamma\delta}\lambda_\alpha^+(\nabla_{\gamma\rho}\lambda_\beta^+)\nabla_\delta{}^\rho W
=\tfrac i8(\nabla^aW)\lambda^{\alpha+}\nabla_a\lambda_\alpha^+.
\end{aligned}
\tag{S2-83}
```

The scalar coefficients add to $`6/8=3/4`$; the two-form coefficients add to $`1/4-1/4-1/4-1/4=-1/2`$. Raising both vector indices in the latter term is essential: $`(\Sigma_{ab})\nabla^aW\nabla^b\lambda=(\Sigma^{ab})\nabla_aW\nabla_b\lambda`$. There is no extra metric sign on just one factor.

For the $`X^{+-}`$ insertion in the last term of (S2-65), the same six rows have coefficients $`(-1,+1,-1,+1,+1,+1)i/8`$ multiplying $`(\Gamma^a)^{\alpha\beta}X^{+-}\lambda_\alpha^+\nabla_a\lambda_\beta^+`$. Here the insertion is $`-\varepsilon_{\delta\sigma}X^{+-}`$ and $`\varepsilon^{\rho\sigma}\varepsilon_{\delta\sigma}=-\delta_\delta{}^\rho`$; applying the three terms of the four-index epsilon gives the six stated signs. Their sum is $`i/4`$. The other two origins, already in the second and sixth terms of (S2-65), are

```math
\begin{aligned}
\tfrac i2X^{++}\lambda^{\alpha+}\nabla_\alpha{}^\beta\lambda_\beta^-
&=-\tfrac i2(\Gamma^a)^{\alpha\beta}X^{++}\lambda_\alpha^+\nabla_a\lambda_\beta^-,\\
\tfrac1{32}X^{++}\varepsilon^{\alpha\beta\gamma\delta}\varepsilon_{\alpha\beta}(D_\gamma D_\delta\lambda_\rho^-)_{\nabla\lambda}\lambda^{\rho-}
&=+\tfrac i4(\Gamma^a)^{\alpha\beta}X^{++}\lambda_\alpha^-\nabla_a\lambda_\beta^+,\\
\text{sum of all three origins}
&=\tfrac i4(\Gamma^a)^{\alpha\beta}X^{++}\lambda_\alpha^k\nabla_a\lambda_{\beta k}
+\tfrac i4(\Gamma^a)^{\alpha\beta}X^{k+}\lambda_\alpha^+\nabla_a\lambda_{\beta k}.
\end{aligned}
\tag{S2-84}
```

The second line follows from the trace $`\varepsilon^{\gamma\delta}(D_\gamma D_\delta\lambda_\rho^-)_{\nabla\lambda}=-4i\nabla_\rho{}^\tau\lambda_\tau^+`$ and moving that odd derivative past $`\lambda^{\rho-}`$. Expanding the final line with $`\lambda_+=-\lambda^-`$ reproduces the three coefficients $`-i/2,+i/4,+i/4`$ individually.
### 4.15 Weyl-two-form terms: the mixed products and their coefficients

The Clifford identities required here follow by polarizing (S2-53). For clarity the matrices in the following two equations are written out, rather than denoting them by new fields:

```math
\begin{aligned}
\left\{\tfrac12W_{ab}\Sigma^{ab},\tfrac12F_{cd}\Sigma^{cd}\right\}
&=-\tfrac14W_{ab}F^{ab}\mathbf1-\tfrac18\varepsilon^{abcde}W_{bc}F_{de}\Gamma_a,\\
\left[\Gamma^a\nabla_aW,\tfrac12W_{bc}\Sigma^{bc}\right]
&=-W_{ab}\nabla^bW\Gamma^a,\\
\Gamma^a\Sigma^{bc}&=-\tfrac12\varepsilon^{abcde}\Sigma_{de}
+\tfrac12\eta^{ab}\Gamma^c-\tfrac12\eta^{ac}\Gamma^b.
\end{aligned}
\tag{S2-85}
```

The first identity is the coefficient linear in each of $`W_{ab},F_{ab}`$ in the square of $`(W_{ab}+F_{ab})\Sigma^{ab}/2`$. The second is the Clifford commutator; the third uses $`\Gamma^{abc}=\varepsilon^{abcde}\Sigma_{de}`$. These equations, together with (S2-77), reduce the following actual contractions from (S2-73):

```math
\begin{aligned}
&\frac i{16}\varepsilon^{\alpha\beta\gamma\delta}\lambda_\alpha^+\lambda_\beta^+(\Gamma^a)_\delta{}^\rho(3\Gamma_aW-W\Gamma_a)_\gamma{}^\tau F_{\tau\rho}
=-\frac{7i}{32}W_{ab}F^{ab}B^{++}
+\frac{5i}{64}\varepsilon^{abcde}(\Gamma_a)^{\alpha\beta}W_{bc}F_{de}\lambda_\alpha^+\lambda_\beta^+,\\
&-\frac i8\varepsilon^{\alpha\beta\gamma\delta}\lambda_\alpha^+\lambda_\beta^+W_{\delta\rho}\varepsilon^{\rho\sigma}F_{\gamma\sigma}
=-\frac i{32}W_{ab}F^{ab}B^{++}
-\frac i{64}\varepsilon^{abcde}(\Gamma_a)^{\alpha\beta}W_{bc}F_{de}\lambda_\alpha^+\lambda_\beta^+,\\
&\frac i4\varepsilon^{\alpha\beta\gamma\delta}\lambda_\alpha^+\lambda_\beta^+(\Gamma^a)_\delta{}^\rho W_{\gamma\rho}\nabla_aW
=-\frac i4(\Gamma^a)^{\alpha\beta}W_{ab}\lambda_\alpha^+\lambda_\beta^+\nabla^bW,\\
&\frac i{32}\varepsilon^{\alpha\beta\gamma\delta}\lambda_\alpha^+\lambda_\beta^+(\Gamma^a)_\delta{}^\rho(3\Gamma_aW-W\Gamma_a)_\gamma{}^\tau\nabla_{\tau\rho}W
=-\frac{3i}{16}(\Gamma^a)^{\alpha\beta}W_{ab}\lambda_\alpha^+\lambda_\beta^+\nabla^bW,\\
&-\frac i{16}\varepsilon^{\alpha\beta\gamma\delta}\lambda_\alpha^+\lambda_\beta^+W_{\delta\rho}\varepsilon^{\rho\sigma}\nabla_{\gamma\sigma}W
=-\frac i{16}(\Gamma^a)^{\alpha\beta}W_{ab}\lambda_\alpha^+\lambda_\beta^+\nabla^bW.
\end{aligned}
\tag{S2-86}
```

For an explicit way to track the $`3\Gamma_aW-W\Gamma_a`$ reduction in the first and fourth lines, insert (S2-68) before contracting the last field:

```math
\begin{aligned}
&(\Gamma^a)_\delta{}^\rho(3\Gamma_aW-W\Gamma_a)_\gamma{}^\tau\\
&\quad=2\delta_\delta{}^\rho W_\gamma{}^\tau
-6\varepsilon_{\gamma\delta}\varepsilon^{\rho\kappa}W_\kappa{}^\tau
-6\delta_\gamma{}^\rho W_\delta{}^\tau
+2W_\gamma{}^\kappa\varepsilon_{\kappa\delta}\varepsilon^{\rho\tau}
+2W_\gamma{}^\rho\delta_\delta{}^\tau.
\end{aligned}
\tag{S2-87}
```

This has five contributions with coefficients $`(2,-6,-6,2,2)`$, obtained as $`(3-1,-6,-6,+2,+2)`$ from the two products. Insert $`W_\alpha{}^\beta=-W_{\alpha\rho}\varepsilon^{\rho\beta}`$, contract against $`F_{\tau\rho}`$ or $`\nabla_{\tau\rho}W`$, and apply (S2-77). The symmetric spinor products reduce by the anticommutator in (S2-85), and the antisymmetric products by its commutator. The first two lines of (S2-86) therefore contribute $`(-7-1)i/32=-i/4`$ to $`W\cdot F\,B^{++}`$ and $`(5-1)i/64=i/16`$ to the epsilon contraction. The last three contribute $`(-4-3-1)i/16=-i/2`$ to the $`W_{ab}\nabla^bW`$ contraction. Terms with $`W_{\alpha\beta}X^{+-}`$ have a symmetric free spinor pair contracted with $`\lambda^+\lambda^+`$ and vanish.

The scalar part of $`(D_\gamma D_\delta B^{--})_1`$ in the seventh term of (S2-65) comes from one $`-2W_{\alpha\beta}W`$ insertion in each possible factor of $`D\lambda`$. Its two needed contractions are

```math
\begin{aligned}
&\frac{3i}{8}\varepsilon^{\alpha\beta\gamma\delta}\lambda_\alpha^+\lambda_\beta^+
\big(W_{\delta\rho}\varepsilon^{\rho\sigma}F_{\gamma\sigma}+F_{\delta\rho}\varepsilon^{\rho\sigma}W_{\gamma\sigma}\big)
=\frac{3i}{16}W_{ab}F^{ab}B^{++}
+\frac{3i}{32}\varepsilon^{abcde}(\Gamma_a)^{\alpha\beta}W_{bc}F_{de}\lambda_\alpha^+\lambda_\beta^+,\\
&\frac{3i}{16}\varepsilon^{\alpha\beta\gamma\delta}\lambda_\alpha^+\lambda_\beta^+
\big(W_{\delta\rho}\varepsilon^{\rho\sigma}\nabla_{\gamma\sigma}W+\nabla_{\delta\rho}W\varepsilon^{\rho\sigma}W_{\gamma\sigma}\big)
=\frac{3i}{8}(\Gamma^a)^{\alpha\beta}W_{ab}\lambda_\alpha^+\lambda_\beta^+\nabla^bW.
\end{aligned}
\tag{S2-88}
```

Both are the sum of the two placements already present in (S2-66); there is no extra factor from exchanging the two even field strengths. Inserting (S2-77) into their left sides gives the sum of a spinor trace and two ordered matrix products. The trace and anticommutator in (S2-85) give the coefficients $`3/16`$ and $`3/32`$ in the first line. The commutator gives $`3/8`$ in the second. The auxiliary insertion again reduces to the vanishing symmetric $`W_{\alpha\beta}\lambda^{\alpha+}\lambda^{\beta+}`$.

There remain the three Weyl-two-form pieces of (S2-49) in the last term of (S2-65). Their $`F`$ contractions, separately, are

```math
\begin{aligned}
&-\tfrac i8\varepsilon^{\alpha\beta\gamma\delta}\lambda_\alpha^+W_{\gamma\rho}\lambda_\beta^+F_\delta{}^\rho
=\tfrac i{32}W_{ab}F^{ab}B^{++}+\tfrac i{64}\varepsilon^{abcde}(\Gamma_a)^{\alpha\beta}W_{bc}F_{de}\lambda_\alpha^+\lambda_\beta^+,\\
&+\tfrac i8\varepsilon^{\alpha\beta\gamma\delta}\lambda_\alpha^+W_{\beta\rho}\lambda_\gamma^+F_\delta{}^\rho
=\tfrac i{32}W_{ab}F^{ab}B^{++}+\tfrac i{64}\varepsilon^{abcde}(\Gamma_a)^{\alpha\beta}W_{bc}F_{de}\lambda_\alpha^+\lambda_\beta^+,\\
&+\tfrac{3i}{8}\varepsilon^{\alpha\beta\gamma\delta}\lambda_\alpha^+\varepsilon_{\beta\gamma}W_{\rho\tau}\lambda^{\tau+}F_\delta{}^\rho
=\tfrac{3i}{32}W_{ab}F^{ab}B^{++}-\tfrac{3i}{64}\varepsilon^{abcde}(\Gamma_a)^{\alpha\beta}W_{bc}F_{de}\lambda_\alpha^+\lambda_\beta^+.
\end{aligned}
\tag{S2-89}
```

For their scalar-gradient counterparts, replace $`-2F_\delta{}^\rho`$ by $`-\nabla_\delta{}^\rho W`$ in the original last term of (S2-65). The explicit contractions are

```math
\begin{aligned}
&-\tfrac i{16}\varepsilon^{\alpha\beta\gamma\delta}\lambda_\alpha^+W_{\gamma\rho}\lambda_\beta^+\nabla_\delta{}^\rho W
=\tfrac i{16}(\Gamma^a)^{\alpha\beta}W_{ab}\lambda_\alpha^+\lambda_\beta^+\nabla^bW,\\
&+\tfrac i{16}\varepsilon^{\alpha\beta\gamma\delta}\lambda_\alpha^+W_{\beta\rho}\lambda_\gamma^+\nabla_\delta{}^\rho W
=\tfrac i{16}(\Gamma^a)^{\alpha\beta}W_{ab}\lambda_\alpha^+\lambda_\beta^+\nabla^bW,\\
&+\tfrac{3i}{16}\varepsilon^{\alpha\beta\gamma\delta}\lambda_\alpha^+\varepsilon_{\beta\gamma}W_{\rho\tau}\lambda^{\tau+}\nabla_\delta{}^\rho W
=-\tfrac{3i}{16}(\Gamma^a)^{\alpha\beta}W_{ab}\lambda_\alpha^+\lambda_\beta^+\nabla^bW.
\end{aligned}
\tag{S2-90}
```

These three rows add to $`5i/32,-i/64,-i/16`$ for the scalar $`W\cdot F`$, epsilon, and $`W\nabla W`$ contractions, respectively. Combining all three origins (S2-86), (S2-88), (S2-89)–(S2-90) gives the final coefficients

```math
-\tfrac14+\tfrac3{16}+\tfrac5{32}=\tfrac3{32},\qquad
\tfrac1{16}+\tfrac3{32}-\tfrac1{64}=\tfrac9{64},\qquad
-\tfrac12+\tfrac38-\tfrac1{16}=-\tfrac3{16}.
\tag{S2-91}
```

The remaining Weyl-two-form term contains $`X^{++}`$. The spinor conversion, including its SU(2) sign, is

```math
\begin{aligned}
\lambda^{\alpha+}W_{\alpha\beta}\lambda^{\beta-}
&=\tfrac12(\Sigma^{ab})^{\alpha\beta}W_{ab}\lambda_\alpha^+\lambda_\beta^-
=-\tfrac14(\Sigma_{ab})^{\alpha\beta}W^{ab}\lambda_\alpha^k\lambda_{\beta k},\\
\lambda_\alpha^k\lambda_{\beta k}
&=-\lambda_\alpha^+\lambda_\beta^-+\lambda_\alpha^-\lambda_\beta^+.
\end{aligned}
\tag{S2-92}
```

In the symmetric $`\Sigma`$ contraction, exchanging the two odd fields in the second term of the last line gives a second $`-\lambda^+\lambda^-`$ term. The four origins in (S2-65), in their order, have coefficients $`-i/4`$, $`+3i/4`$, $`-5i/8`$, $`+i/2`$ multiplying $`X^{++}\lambda^{\alpha+}W_{\alpha\beta}\lambda^{\beta-}`$. The third coefficient comes from tracing (S2-49): $`\varepsilon^{\gamma\delta}(D_\gamma D_\delta\lambda_\rho^-)_{W\lambda}=10iW_{\rho\tau}\lambda^{\tau+}`$, together with (S2-66). The fourth comes from the $`-8iW_{\alpha\rho}X^{++}`$ term in (S2-72). Thus

```math
\left(\tfrac1{16}-\tfrac3{16}+\tfrac5{32}-\tfrac18\right)i
(\Sigma_{ab})^{\alpha\beta}X^{++}W^{ab}\lambda_\alpha^k\lambda_{\beta k}
=-\tfrac{3i}{32}(\Sigma_{ab})^{\alpha\beta}X^{++}W^{ab}\lambda_\alpha^k\lambda_{\beta k}.
\tag{S2-93}
```

### 4.16 Weyl-spinor times three-gaugino terms, including the fermion rearrangements

All Weyl spinors and all gauginos are odd. We put the Weyl spinor first. Applying (S2-77) to the actual spinors, and using $`X_\gamma\lambda^{\gamma+}=-X^{\gamma}\lambda_\gamma^+`$, gives

```math
\begin{aligned}
\varepsilon^{\alpha\beta\gamma\delta}\lambda_\alpha^+\lambda_\beta^+X_\gamma^+\lambda_\delta^-
&=B^{++}X^{\rho+}\lambda_\rho^-+2X^{\alpha+}\lambda_\alpha^+\lambda^{\beta+}\lambda_\beta^-,\\
\varepsilon^{\alpha\beta\gamma\delta}\lambda_\alpha^+\lambda_\beta^+X_\gamma^-\lambda_\delta^+
&=B^{++}X^{\rho-}\lambda_\rho^++2X^{\alpha-}\lambda_\alpha^+B^{++}
=3B^{++}X^{\rho-}\lambda_\rho^+,\\
B^{++}\lambda^{\alpha+}X_\alpha^-&=B^{++}X^{\alpha-}\lambda_\alpha^+.
\end{aligned}
\tag{S2-94}
```

In the first two lines, moving $`X`$ through two gauginos gives $`(-1)^2=+1`$; raising its contracted index gives the remaining minus sign needed in applying (S2-77). In the last line the odd interchange and the antisymmetric raising metric each give a minus sign, whose product is plus. No four-spinor identity with unspecified pairings is being invoked.

For the third term of (S2-65), insert all six terms of (S2-74). The three groups, before collection, are

```math
\begin{aligned}
&-\tfrac1{16}\varepsilon^{\alpha\beta\gamma\delta}\lambda_\alpha^+\lambda_\beta^+
\big(\tfrac{3i}{2}\varepsilon_{\gamma\delta}X^{\rho+}\lambda_\rho^--3i\varepsilon_{\gamma\delta}X^{\rho-}\lambda_\rho^+\big)
=-\tfrac{3i}{16}B^{++}X^{\rho+}\lambda_\rho^-+\tfrac{3i}{8}B^{++}X^{\rho-}\lambda_\rho^+,\\
&-\tfrac1{16}\varepsilon^{\alpha\beta\gamma\delta}\lambda_\alpha^+\lambda_\beta^+
\big(-\tfrac i2X_\gamma^+\lambda_\delta^-+\tfrac i2X_\delta^+\lambda_\gamma^-\big)
=\tfrac i{16}B^{++}X^{\rho+}\lambda_\rho^-+\tfrac i8X^{\alpha+}\lambda_\alpha^+\lambda^{\beta+}\lambda_\beta^-,\\
&-\tfrac1{16}\varepsilon^{\alpha\beta\gamma\delta}\lambda_\alpha^+\lambda_\beta^+
\big(\tfrac{3i}{2}X_\gamma^-\lambda_\delta^+-\tfrac{3i}{2}X_\delta^-\lambda_\gamma^+\big)
=-\tfrac{9i}{16}B^{++}X^{\rho-}\lambda_\rho^+,\\
\text{sum}&=\tfrac i8X^{\alpha+}\lambda_\alpha^+\lambda^{\beta+}\lambda_\beta^-
-\tfrac i8B^{++}X^{\rho+}\lambda_\rho^--\tfrac{3i}{16}B^{++}X^{\rho-}\lambda_\rho^+.
\end{aligned}
\tag{S2-95}
```

The fourth term of (S2-65) is already reduced by the last line of (S2-94): it contributes $`-9iB^{++}X^{\alpha-}\lambda_\alpha^+/16`$.

For the seventh term of (S2-65), insert the explicit-$`W`$ part of (S2-49) into (S2-66). Its full fermionic coefficient is

```math
\begin{aligned}
(D_\gamma D_\delta B^{--})_{1,\mathrm{fermionic}}
&=-2\big(-\tfrac32\varepsilon_{\gamma\delta}X_\rho^+-\tfrac12\varepsilon_{\gamma\rho}X_\delta^++\tfrac12\varepsilon_{\delta\rho}X_\gamma^+\big)\lambda^{\rho-}\\
&=-3\varepsilon_{\gamma\delta}X^{\rho+}\lambda_\rho^-+X_\delta^+\lambda_\gamma^--X_\gamma^+\lambda_\delta^-,\\
-\tfrac{3i}{64}\varepsilon^{\alpha\beta\gamma\delta}\lambda_\alpha^+\lambda_\beta^+(D_\gamma D_\delta B^{--})_{1,\mathrm{fermionic}}
&=\tfrac{9i}{32}B^{++}X^{\rho+}\lambda_\rho^-+\tfrac{3i}{32}\big(B^{++}X^{\rho+}\lambda_\rho^-+2X^{\alpha+}\lambda_\alpha^+\lambda^{\beta+}\lambda_\beta^-\big)\\
&=\tfrac{3i}{8}B^{++}X^{\rho+}\lambda_\rho^-+\tfrac{3i}{16}X^{\alpha+}\lambda_\alpha^+\lambda^{\beta+}\lambda_\beta^-.
\end{aligned}
\tag{S2-96}
```

For the eighth term, use the last three terms of (S2-72). Its three separate contributions are

```math
\begin{aligned}
-\tfrac i{16}\lambda^{\alpha+}\varepsilon_{\alpha\rho}X^{\tau+}\lambda_\tau^+\lambda^{\rho-}
&=-\tfrac i{16}X^{\alpha+}\lambda_\alpha^+\lambda^{\beta+}\lambda_\beta^-,\\
-\tfrac i8\lambda^{\alpha+}X_\alpha^+\lambda_\rho^+\lambda^{\rho-}
&=\tfrac i8X^{\alpha+}\lambda_\alpha^+\lambda^{\beta+}\lambda_\beta^-,\\
+\tfrac i8\lambda^{\alpha+}X_\rho^+\lambda_\alpha^+\lambda^{\rho-}
&=\tfrac i8B^{++}X^{\rho+}\lambda_\rho^- .
\end{aligned}
\tag{S2-97}
```

In the first line $`\lambda^{\alpha+}\varepsilon_{\alpha\rho}=-\lambda_\rho^+`$; moving $`X`$ past that gaugino gives a second minus sign, and then moving the other plus gaugino and raising its paired index gives the displayed coefficient. In the second line $`\lambda^{\alpha+}X_\alpha^+=X^{\alpha+}\lambda_\alpha^+`$ and $`\lambda_\rho^+\lambda^{\rho-}=-B^{+-}`$. In the third line moving $`X_\rho^+`$ past the first gaugino and using $`X_\rho^+\lambda^{\rho-}=-X^{\rho+}\lambda_\rho^-`$ gives two minus signs. The sum is $`iX^{\alpha+}\lambda_\alpha^+\lambda^{\beta+}\lambda_\beta^-/16+iB^{++}X^{\rho+}\lambda_\rho^-/8`$.

Finally, adding (S2-95), the fourth term of (S2-65), (S2-96), and (S2-97) gives

```math
\begin{aligned}
&\left(\tfrac18+\tfrac3{16}+\tfrac1{16}\right)iX^{\alpha+}\lambda_\alpha^+\lambda^{\beta+}\lambda_\beta^-
+\left(-\tfrac18+\tfrac38+\tfrac18\right)iB^{++}X^{\rho+}\lambda_\rho^-
+\left(-\tfrac3{16}-\tfrac9{16}\right)iB^{++}X^{\rho-}\lambda_\rho^+\\
&\quad=\tfrac{3i}{8}X^{\alpha+}\lambda_\alpha^+\lambda^{\beta+}\lambda_\beta^-
+\tfrac{3i}{8}B^{++}X^{\rho+}\lambda_\rho^--\tfrac{3i}{4}B^{++}X^{\rho-}\lambda_\rho^+\\
&\quad=-\tfrac{3i}{8}X^{\alpha k}\lambda_\alpha^+\lambda^{\beta+}\lambda_{\beta k}
-\tfrac{3i}{8}X^{\alpha k}B^{++}\lambda_{\alpha k}.
\end{aligned}
\tag{S2-98}
```

The final equality expands $`k=+,-`$ with the fixed SU(2) lowering rule. The two $`X^{\alpha-}\lambda_\alpha^+B^{++}`$ terms combine to $`-3i/4`$. The other Weyl fermion, $`W_{\alpha\beta\gamma}^+`$, canceled in (S2-73); its remaining appearance from (S2-72) is proportional to
$`W_{\alpha\rho\tau}^+\lambda^{\alpha+}\lambda^{\tau+}\lambda^{\rho-}=0`$, since $`\alpha,\tau`$ are symmetric in the Weyl tensor and antisymmetric in the two plus gauginos. This accounts for every Weyl-fermion contribution at this pole.

### 4.17 Collected eighteen-term $`W^{-3}`$ result

All equations through (S2-98) are local identities. Restore $`ij`$ by polarization of the two external plus indices; the plus direction was arbitrary and no SU(2) gauge was fixed. The independently derived result is

```math
\boxed{\begin{aligned}
\left.H_{\log W}^{ij}\right|_{W^{-3}}=W^{-3}\Big\{&\frac18X^{ij}F^{ab}F_{ab}-\frac18X^{ij}X^{kl}X_{kl}-\frac14X^{ij}(\nabla^aW)\nabla_aW\\
&-\frac i8\varepsilon^{abcde}(\Sigma_{ab})^{\alpha\beta}F_{de}\lambda_\alpha^{(i}\nabla_c\lambda_\beta^{j)}
-\frac i4(\Gamma^a)^{\alpha\beta}F_{ab}\lambda_\alpha^{(i}\nabla^b\lambda_\beta^{j)}
-\frac i4(\Gamma^a)^{\alpha\beta}\lambda_\alpha^i\lambda_\beta^j\nabla^cF_{ac}\\
&+\frac i4(\Gamma^a)^{\alpha\beta}X^{ij}\lambda_\alpha^k\nabla_a\lambda_{\beta k}
+\frac i4(\Gamma^a)^{\alpha\beta}X^{k(i}\lambda_\alpha^{j)}\nabla_a\lambda_{\beta k}
+\frac i4(\Gamma^a)^{\alpha\beta}\lambda_\alpha^{(i}(\nabla_aX^{j)l})\lambda_{\beta l}\\
&+\frac i4\lambda^{\alpha i}\lambda_\alpha^j\Box W
+\frac{3i}{4}(\nabla^aW)\lambda^{\alpha(i}\nabla_a\lambda_\alpha^{j)}
-\frac i2(\Sigma_{ab})^{\alpha\beta}(\nabla^aW)\lambda_\alpha^{(i}\nabla^b\lambda_\beta^{j)}\\
&-\frac{3i}{16}(\Gamma^a)^{\alpha\beta}W_{ab}\lambda_\alpha^i\lambda_\beta^j\nabla^bW
+\frac{3i}{32}W_{ab}F^{ab}\lambda^{\alpha i}\lambda_\alpha^j
+\frac{9i}{64}\varepsilon^{abcde}(\Gamma_a)^{\alpha\beta}W_{bc}F_{de}\lambda_\alpha^i\lambda_\beta^j\\
&-\frac{3i}{32}(\Sigma_{ab})^{\alpha\beta}X^{ij}W^{ab}\lambda_\alpha^k\lambda_{\beta k}
-\frac{3i}{8}X^{\alpha k}\lambda_\alpha^{(i}\lambda^{\beta j)}\lambda_{\beta k}
-\frac{3i}{8}X^{\alpha k}\lambda^{\beta i}\lambda_\beta^j\lambda_{\alpha k}\Big\}.
\end{aligned}}
\tag{S2-99}
```

The positive derivative-of-$`X`$ term is intentional and definition-derived; it must not be silently replaced by the negative printed term. Seventeen terms agree with S23 (3.25), and (S2-79)–(S2-81) isolate the one discrepancy. The result includes its bosonic, two-fermion and four-fermion terms; no gravitino or other connection hidden in $`\nabla_a`$ has been set to zero.

### 4.18 Selecting every contribution to the $`W^{-2}`$ coefficient

We continue from the **operator definition**, using S23 (3.24), (2.13a–c), (2.6a–c,e), and C24 (A.1), (A.3). S23 (3.25) is used only for comparison after collection. The $`W^{-2}`$ coefficient has twelve surviving terms. Unlike the $`W^{-3}`$ gradient-$`X`$ term, these twelve terms agree with the printed expression.

Keep $`D_\alpha=\nabla_\alpha^+`$, $`D^{++}=-\varepsilon^{\alpha\beta}D_\alpha D_\beta`$, $`B^{rs}=\lambda^{\alpha r}\lambda_\alpha^s`$, and the explicit-scalar-$`W`$ coefficient notation introduced in section 4.10. In particular, the subscript $`1`$ below is a coefficient of scalar $`W`$, not an instruction to set the super-Weyl tensor to zero. The starting expression is (S2-31),

```math
H^{++}=-\tfrac12\Delta(W^{-1}X^{--})-\tfrac i8\Delta(W^{-2}B^{--}),\qquad
\Delta=-\tfrac1{32}D^{++}D^{++}.
\tag{S2-100}
```

Insert $`f'=-W^{-2}`$, $`f''=2W^{-3}`$ for the first product, and $`g'=-2W^{-3}`$, $`g''=6W^{-4}`$ for the second, into the graded product rule (S2-36). Before doing any Clifford reductions, the coefficient of $`W^{-2}`$ is the sum of the following twelve contributions, in their displayed order:

```math
\begin{aligned}
\left.H^{++}\right|_{W^{-2}}=W^{-2}\Big\{&
-\tfrac38X^{++}\lambda^{\alpha+}X_\alpha^-
-\tfrac1{16}\varepsilon^{\alpha\beta\gamma\delta}\lambda_\alpha^+\lambda_\beta^+(D_\gamma D_\delta X^{--})_1
+\tfrac i{16}X^{++}(D^{++}X^{--})_0
-\tfrac i{16}\lambda^{\alpha+}(D_\alpha D^{++}X^{--})_0\\
&-\tfrac1{64}X^{++}\varepsilon^{\alpha\beta\gamma\delta}\varepsilon_{\alpha\beta}(D_\gamma D_\delta B^{--})_1
-\tfrac{3i}{64}\varepsilon^{\alpha\beta\gamma\delta}\lambda_\alpha^+\lambda_\beta^+(D_\gamma D_\delta B^{--})_2
+\tfrac14\lambda^{\alpha+}X_{\alpha\rho}^{++}\lambda^{\rho-}\\
&-\tfrac18\varepsilon^{\alpha\beta\gamma\delta}\lambda_\alpha^+(D_\beta D_\gamma\lambda_\rho^-)_0\varepsilon^{\rho\sigma}W_{\delta\sigma}
+\tfrac1{16}\varepsilon^{\alpha\beta\gamma\delta}\lambda_\alpha^+(D_\beta D_\gamma\lambda_\rho^-)_1\varepsilon^{\rho\sigma}
(-2F_{\delta\sigma}-\varepsilon_{\delta\sigma}X^{+-}-\nabla_{\delta\sigma}W)\\
&+\tfrac i4(\Delta\lambda_\rho^-)_0\lambda^{\rho-}
+\tfrac i{32}\varepsilon^{\delta\alpha}(D_\alpha D^{++}\lambda_\rho^-)_0\varepsilon^{\rho\sigma}
(-2F_{\delta\sigma}-\varepsilon_{\delta\sigma}X^{+-}-\nabla_{\delta\sigma}W)\\
&-\tfrac i{128}\varepsilon^{\alpha\beta\gamma\delta}(D_\alpha D_\beta\lambda_\rho^-)_0\varepsilon^{\rho\sigma}(D_\gamma D_\delta\lambda_\sigma^-)_0\Big\}.
\end{aligned}
\tag{S2-101}
```

Here $`X_{\alpha\rho}^{++}`$ is the **Weyl descendant**, whereas $`X^{++}`$ is the vector auxiliary. The first four terms come from the first product in (S2-100). The $`3+1`$ distribution gives $`(1/48)(6)(2)(-3/2)=-3/8`$. The two pieces of the $`2+2`$ distribution give $`-1/16`$ and, after $`\varepsilon^{\alpha\beta\gamma\delta}\varepsilon_{\alpha\beta}=-2\varepsilon^{\gamma\delta}`$, $`+i/16`$. The $`1+3`$ distribution gives $`-i/16`$. The next five terms come from the second product's $`2+2`$ and $`1+3`$ distributions. Its last three terms are $`-i\Delta B^{--}/8`$, expanded below. Neither $`W^{-1}\Delta X^{--}`$ nor $`(\Delta W^{-1})X^{--}`$ supplies this pole: the former starts at $`W^{-1}`$, and the latter has poles at least three. This accounts for every placement of the four remaining spinor derivatives.

### 4.19 The full trace $`D^{++}X^{--}`$ and the explicit-$`W`$ part of $`D_\alpha D_\beta X^{--}`$

The terms previously excluded from (S2-73) because they carried an explicit scalar $`W`$ are now required. Starting from its first line gives

```math
\begin{aligned}
(D_\alpha D_\beta X^{--})_1={}&
-4i(\Gamma^a)_\beta{}^\rho\nabla_aW_{\alpha\rho}
-4i(\Gamma^a)_\beta{}^\rho T_{a\alpha}{}^\gamma W_{\gamma\rho}
+4(\Gamma^a)_\beta{}^\rho R(S)_{a\alpha}^{+,\gamma-}\varepsilon_{\gamma\rho}\\
&+2iW_{\beta\rho}\varepsilon^{\rho\sigma}W_{\alpha\sigma}
-\tfrac32D_\alpha X_\beta^- .
\end{aligned}
\tag{S2-102}
```

The five origins are, respectively: differentiating $`W_{\alpha\rho}W`$ inside $`\nabla_aD_\alpha\lambda_\rho^-`$; the mixed torsion acting on the $`-2W_{\gamma\rho}W`$ part of $`D_\gamma\lambda_\rho^-`$; the S action $`S_{\gamma-}\lambda_\rho^-=-2i\varepsilon_{\gamma\rho}W`$ multiplied by $`2i`$; differentiating the gaugino in $`-iW_{\beta\rho}\lambda^{\rho-}`$; and differentiating $`X_\beta^-`$ in $`-3WX_\beta^-/2`$. Thus the coefficient $`+4`$ of the S curvature is $`2i(-2i)`$, not a convention choice.

For clarity, the two source substitutions used in this equation are written out here. S23 (2.6b) gives

```math
\begin{aligned}
D_\alpha X_\beta^-={}&X_{\alpha\beta}^{+-}+\tfrac i8\varepsilon_{\alpha\beta}Y
-\tfrac{3i}{2}(\Gamma^a)_\alpha{}^\rho\nabla_aW_{\beta\rho}
-2iW_\alpha{}^\rho W_{\beta\rho}
+\tfrac i2\varepsilon_{\alpha\beta}W^{\gamma\delta}W_{\gamma\delta}
-\tfrac i2(\Gamma^a)_\beta{}^\rho\nabla_aW_{\alpha\rho}.
\end{aligned}
\tag{S2-103}
```

With $`\widetilde W_{abc}=\varepsilon_{abcde}W^{de}/2`$, C24 (A.3e), at $`i=+,j=-`$, is

```math
\begin{aligned}
R(S)_{b\alpha}^{+,\gamma-}={}&\tfrac1{16}X_{cd}^{+-}(\Sigma^{cd}\Gamma_b-2\Gamma_b\Sigma^{cd})_\alpha{}^\gamma
-\tfrac{3i}{8}\nabla_{[b}W_{cd]}(\Sigma^{cd})_\alpha{}^\gamma
-\tfrac i8\nabla^dW_{dc}(\Sigma^c{}_b)_\alpha{}^\gamma\\
&+\tfrac{3i}{16}\nabla^dW_{db}\delta_\alpha{}^\gamma
-\tfrac i8\nabla^c\widetilde W_{cbd}(\Gamma^d)_\alpha{}^\gamma
+\tfrac i{16}\widetilde W^{cde}W_{de}(\Sigma_{cb})_\alpha{}^\gamma
-\tfrac{3i}{32}\widetilde W_{bde}W^{de}\delta_\alpha{}^\gamma\\
&+\tfrac i4W_{bd}W^{cd}(\Gamma_c)_\alpha{}^\gamma
-\tfrac{3i}{64}W^{cd}W_{cd}(\Gamma_b)_\alpha{}^\gamma.
\end{aligned}
\tag{S2-104}
```

The antisymmetrization in $`\nabla_{[b}W_{cd]}`$ has unit weight: it equals $`(\nabla_bW_{cd}+\nabla_cW_{db}+\nabla_dW_{bc})/3`$. For $`R(S)^{+,\gamma+}`$ only the first term survives, with $`X_{cd}^{++}`$ replacing $`X_{cd}^{+-}`$. No curvature in (S2-104) is replaced by a field equation.

We can reduce (S2-102) using the complete antisymmetric spinor basis $`\varepsilon_{\alpha\beta},(\Gamma^a)_{\alpha\beta}`$. Its normalization and extraction formula are

```math
\begin{gathered}
\varepsilon^{\alpha\beta}\varepsilon_{\alpha\beta}=-4,\qquad
(\Gamma^a)^{\alpha\beta}(\Gamma^b)_{\alpha\beta}=-4\eta^{ab},\qquad
\varepsilon^{\alpha\beta}(\Gamma^a)_{\alpha\beta}=0,\\
A_{[\alpha\beta]}=-\tfrac14\varepsilon_{\alpha\beta}\varepsilon^{\rho\sigma}A_{\rho\sigma}
-\tfrac14(\Gamma_a)_{\alpha\beta}(\Gamma^a)^{\rho\sigma}A_{\rho\sigma}.
\end{gathered}
\tag{S2-105}
```

Insert $`W_{\alpha\beta}=W_{ab}(\Sigma^{ab})_{\alpha\beta}/2`$, $`T_a=(3\Gamma_aW-W\Gamma_a)/4`$, (S2-103) and (S2-104). Expand each $`\Gamma\Sigma`$ using (S2-85). The coefficients of the four possible antisymmetric structures are as follows; the first column identifies the actual term of (S2-102), not a new composite field.

| Term in (S2-102) | $`i\varepsilon_{\alpha\beta}Y`$ | $`i\varepsilon_{\alpha\beta}W^{ab}W_{ab}`$ | $`i(\Gamma^a)_{\alpha\beta}\nabla^cW_{ac}`$ | $`i\varepsilon^{abcde}(\Gamma_a)_{\alpha\beta}W_{bc}W_{de}`$ |
|---|---:|---:|---:|---:|
| $`-4i\Gamma^a\nabla_aW`$ | $`0`$ | $`0`$ | $`-2`$ | $`0`$ |
| $`-4i\Gamma^aT_aW`$ | $`0`$ | $`7/4`$ | $`0`$ | $`5/8`$ |
| $`4\Gamma^aR(S)_a\varepsilon`$ | $`0`$ | $`-1/16`$ | $`-1/4`$ | $`-1/16`$ |
| $`2iW\varepsilon^{-1}W`$ | $`0`$ | $`1/4`$ | $`0`$ | $`-1/8`$ |
| $`-3D_\alpha X_\beta^-/2`$ | $`-3/16`$ | $`0`$ | $`-3/4`$ | $`-3/16`$ |

For example, the $`Y`$ coefficient is $`(-3/2)(i/8)=-3i/16`$. The scalar Weyl-square coefficient is $`7/4-1/16+1/4=31/16`$; the divergence coefficient is $`-2-1/4-3/4=-3`$; the epsilon coefficient is $`5/8-1/16-1/8-3/16=1/4`$. The symmetric $`X_{\alpha\beta}^{+-}`$ terms cancel between the S-curvature term ($`+3X_{\alpha\beta}^{+-}/2`$) and the last term ($`-3X_{\alpha\beta}^{+-}/2`$). The symmetric curl pieces cancel upon inserting the two derivative terms and dual derivative in (S2-104). Equivalently their coefficients in $`A_{(\alpha\beta)}`$ sum to zero before (S2-105) is used. This leaves

```math
(D_\alpha D_\beta X^{--})_1
=-\tfrac{3i}{16}\varepsilon_{\alpha\beta}Y+\tfrac{31i}{16}\varepsilon_{\alpha\beta}W^{ab}W_{ab}
-3i(\Gamma^a)_{\alpha\beta}\nabla^cW_{ac}
+\tfrac i4\varepsilon^{abcde}(\Gamma_a)_{\alpha\beta}W_{bc}W_{de}.
\tag{S2-106}
```

To obtain the full trace, contract (S2-73) and (S2-74) with $`-\varepsilon^{\alpha\beta}`$. The ordinary derivative gives $`-8i\Box W`$; its $`\nabla F`$ and $`\nabla X`$ traces vanish because $`\mathop{\mathrm{tr}}\nolimits(\Gamma^a\Sigma^{bc})=\mathop{\mathrm{tr}}\nolimits\Gamma^a=0`$. The torsion and explicit $`W D\lambda`$ terms give $`7iW_{ab}F^{ab}+iW_{ab}F^{ab}=8iW_{ab}F^{ab}`$. In (S2-74) the $`X^{\alpha+}\lambda_\alpha^-`$ coefficients are $`6i-i=5i`$, and the $`X^{\alpha-}\lambda_\alpha^+`$ coefficients are $`-12i+3i=-9i`$. Finally (S2-106) has trace $`-3iY/4+31iW^{ab}W_{ab}/4`$. Consequently

```math
\begin{aligned}
D^{++}X^{--}={}&-8i\Box W+8iW_{ab}F^{ab}
+5iX^{\alpha+}\lambda_\alpha^--9iX^{\alpha-}\lambda_\alpha^+
+W\big(-\tfrac{3i}{4}Y+\tfrac{31i}{4}W^{ab}W_{ab}\big).
\end{aligned}
\tag{S2-107}
```

Its weight is three: $`[D^{++}X]=1+2=3`$, and each term on the right has that weight. The large coefficient $`31/4`$ is an intermediate coefficient, not the final Weyl-square coefficient in $`H`$.

### 4.20 Differentiating the trace: the connections in $`D_\alpha\Box W`$

The derivative in (S2-107) is fully superconformal. On the scalar $`W`$, the mixed commutator gives

```math
D_\alpha\nabla_aW=i\nabla_a\lambda_\alpha^++iT_{a\alpha}{}^\beta\lambda_\beta^+
-\tfrac14(\Gamma_a)_\alpha{}^\beta X_\beta^+W,
\qquad
D_\alpha\Box W=\nabla^a(D_\alpha\nabla_aW)+[D_\alpha,\nabla^a]\nabla_aW.
\tag{S2-108}
```

The second commutator acts on a vector descendant of weight two, rather than on a primary scalar of weight one. We need

```math
\mathbb D(\nabla_aW)=2\nabla_aW,\qquad
S_{\gamma k}\nabla_aW=-(\Gamma_a)_\gamma{}^\delta\lambda_{\delta k},\qquad
K_c\nabla_aW=2\eta_{ca}W.
\tag{S2-109}
```

The S equality follows from C24 (A.1l): $`i(\Gamma_a)_\gamma{}^\delta\nabla_{\delta k}W=i^2(\Gamma_a)_\gamma{}^\delta\lambda_{\delta k}`$. The Lorentz trace in the second commutator contributes $`+(\Gamma^a)_\alpha{}^\beta X_\beta^+\nabla_aW`$; the gamma-trace of the symmetric three-spinor $`W_{\alpha\beta\gamma}^+`$ is zero, since the gamma matrix with two lowered spinor indices is antisymmetric. The dilatation action contributes $`-(\Gamma^a)_\alpha{}^\beta X_\beta^+\nabla_aW/2`$. Differentiating the last term of the first equality in (S2-108) contributes another $`-(\Gamma^a)_\alpha{}^\beta X_\beta^+\nabla_aW/4`$. Thus the net coefficient is $`1-1/2-1/4=1/4`$.

The two torsion contributions to $`\nabla\lambda`$ add. The derivative of the torsion and the second torsion action remain separately visible. Terms proportional to $`K_c\nabla_aW`$ or $`W\nabla X`$ contain an explicit scalar $`W`$ and belong to the next pole, not to the coefficient selected here. Therefore

```math
\begin{aligned}
(D_\alpha\Box W)_0={}&i\Box\lambda_\alpha^++2iT^a{}_\alpha{}^\beta\nabla_a\lambda_\beta^+
+i(\nabla^aT_a)_\alpha{}^\beta\lambda_\beta^+
+i(T^aT_a)_\alpha{}^\beta\lambda_\beta^+\\
&+\tfrac14(\Gamma^a)_\alpha{}^\beta X_\beta^+\nabla_aW
-R(S)^a{}_\alpha{}^{+,\gamma k}(\Gamma_a)_\gamma{}^\delta\lambda_{\delta k}.
\end{aligned}
\tag{S2-110}
```

Here is the contraction of each nontrivial connection contribution with the leading gaugino, using (S2-85), (S2-104), and $`\lambda_+=-\lambda^-`$, $`\lambda_-=\lambda^+`$:

```math
\begin{aligned}
2i\lambda^{\alpha+}T^a{}_\alpha{}^\beta\nabla_a\lambda_\beta^+
&=\tfrac i4\varepsilon^{abcde}(\Sigma_{ab})^{\alpha\beta}W_{de}\lambda_\alpha^+\nabla_c\lambda_\beta^+
+i(\Gamma^a)^{\alpha\beta}W_{ab}\lambda_\alpha^+\nabla^b\lambda_\beta^+,\\
i\lambda^{\alpha+}(\nabla^aT_a)_\alpha{}^\beta\lambda_\beta^+
&=\tfrac i2(\Gamma^a)^{\alpha\beta}\lambda_\alpha^+\lambda_\beta^+\nabla^cW_{ac},\\
i\lambda^{\alpha+}(T^aT_a)_\alpha{}^\beta\lambda_\beta^+
&=-\tfrac{5i}{32}W^{ab}W_{ab}B^{++}
-\tfrac i{64}\varepsilon^{abcde}(\Gamma_a)^{\alpha\beta}W_{bc}W_{de}\lambda_\alpha^+\lambda_\beta^+,\\
-\lambda^{\alpha+}R(S)^a{}_\alpha{}^{+,\gamma k}(\Gamma_a)_\gamma{}^\delta\lambda_{\delta k}
&=\tfrac i{16}(\Gamma^a)^{\alpha\beta}\lambda_\alpha^+\lambda_\beta^+\nabla^cW_{ac}
+\tfrac i{64}W^{ab}W_{ab}B^{++}
+\tfrac i{64}\varepsilon^{abcde}(\Gamma_a)^{\alpha\beta}W_{bc}W_{de}\lambda_\alpha^+\lambda_\beta^+\\
&\quad+\tfrac38X_{\alpha\beta}^{++}\lambda^{\alpha+}\lambda^{\beta-},\\
\tfrac14\lambda^{\alpha+}(\Gamma^a)_\alpha{}^\beta X_\beta^+\nabla_aW
&=-\tfrac14(\Gamma^a)^{\alpha\beta}(\nabla_aW)X_\alpha^+\lambda_\beta^+.
\end{aligned}
\tag{S2-111}
```

In the last line moving the odd $`X`$ past the leading odd $`\lambda`$ gives the minus sign. In the S-curvature line, the $`X^{+-}_{\alpha\beta}`$ contraction contains two identical plus gauginos and vanishes because $`X^{+-}_{\alpha\beta}`$ is symmetric. The $`X^{++}_{\alpha\beta}`$ term instead pairs a plus and a minus gaugino and must be kept. For the torsion-square line, expand $`(3\Gamma^aW-W\Gamma^a)(3\Gamma_aW-W\Gamma_a)/16`$ before applying (S2-105). This gives $`-5W^{ab}W_{ab}/32`$ in the scalar pairing and $`-\varepsilon^{abcde}W_{bc}W_{de}/64`$ in the gamma pairing. The two epsilon terms in the third and fourth lines cancel, while $`1/2+1/16=9/16`$ and $`-5/32+1/64=-9/64`$. Thus

```math
\begin{aligned}
\lambda^{\alpha+}(D_\alpha\Box W)_0={}&i\lambda^{\alpha+}\Box\lambda_\alpha^+
+\tfrac i4\varepsilon^{abcde}(\Sigma_{ab})^{\alpha\beta}W_{de}\lambda_\alpha^+\nabla_c\lambda_\beta^+
+i(\Gamma^a)^{\alpha\beta}W_{ab}\lambda_\alpha^+\nabla^b\lambda_\beta^+\\
&+\tfrac{9i}{16}(\Gamma^a)^{\alpha\beta}\lambda_\alpha^+\lambda_\beta^+\nabla^cW_{ac}
-\tfrac{9i}{64}W^{ab}W_{ab}B^{++}
+\tfrac38X_{\alpha\beta}^{++}\lambda^{\alpha+}\lambda^{\beta-}
-\tfrac14(\Gamma^a)^{\alpha\beta}(\nabla_aW)X_\alpha^+\lambda_\beta^+.
\end{aligned}
\tag{S2-112}
```

Next differentiate the field-strength contraction. Converting both two-forms to symmetric spinors gives $`W_{ab}F^{ab}=2W^{\beta\gamma}F_{\beta\gamma}`$. Its product rule reads

```math
\begin{aligned}
(D_\alpha(W_{ab}F^{ab}))_0={}&
2F^{\beta\gamma}\big(W_{\alpha\beta\gamma}^++\varepsilon_{\alpha(\beta}X_{\gamma)}^+\big)\\
&+2W^{\beta\gamma}\Big[-\tfrac i2\big(\nabla_{\alpha\beta}\lambda_\gamma^++\nabla_{\alpha\gamma}\lambda_\beta^+
+\varepsilon_{\alpha\beta}\nabla_\gamma{}^\rho\lambda_\rho^++\varepsilon_{\alpha\gamma}\nabla_\beta{}^\rho\lambda_\rho^+\big)
-\tfrac{3i}{2}W_{\beta\gamma}\lambda_\alpha^+\\
&\hspace{17mm}+\tfrac i4\big(W_{\alpha\beta}\lambda_\gamma^++W_{\alpha\gamma}\lambda_\beta^+\big)
-\tfrac{3i}{4}\big(\varepsilon_{\alpha\beta}W_\gamma{}^\rho\lambda_\rho^++\varepsilon_{\alpha\gamma}W_\beta{}^\rho\lambda_\rho^+\big)\Big].
\end{aligned}
\tag{S2-113}
```

This is S23 (2.6a) and (2.13b) with only the explicit-$`W`$ coefficient selected. The first line gives the $`F W_{ab}{}^{\alpha+}\lambda_\alpha^+`$ and $`\Sigma F X\lambda`$ contractions. In the second part, the four $`\nabla\lambda`$ placements reduce by $`\Gamma\Sigma`$; their epsilon pieces cancel and their vector pieces add to $`2i\Gamma^aW_{ab}\lambda\nabla^b\lambda`$. The remaining three Weyl-two-form placements reduce by the square and anticommutator in (S2-53), (S2-85). With the Weyl spinor ordered first, the resulting identity is

```math
\begin{aligned}
\lambda^{\alpha+}(D_\alpha(W_{ab}F^{ab}))_0={}&
2i(\Gamma^a)^{\alpha\beta}W_{ab}\lambda_\alpha^+\nabla^b\lambda_\beta^+
-iW^{ab}W_{ab}B^{++}
-\tfrac i4\varepsilon^{abcde}(\Gamma_a)^{\alpha\beta}W_{bc}W_{de}\lambda_\alpha^+\lambda_\beta^+\\
&+(\Sigma_{ab})^{\alpha\beta}F^{ab}X_\alpha^+\lambda_\beta^+
+F^{ab}W_{ab}^{\alpha+}\lambda_\alpha^+.
\end{aligned}
\tag{S2-114}
```

For the two Weyl-spinor products in (S2-107), the graded rule is $`D(X\lambda)=(DX)\lambda-X(D\lambda)`$. Using $`D_\alpha X_\beta^+=X_{\alpha\beta}^{++}`$, (S2-103), and the vector rule gives

```math
\begin{aligned}
\lambda^{\alpha+}D_\alpha(X^{\rho+}\lambda_\rho^-)
={}&-X_{\alpha\beta}^{++}\lambda^{\alpha+}\lambda^{\beta-}
-(\Sigma_{ab})^{\alpha\beta}F^{ab}X_\alpha^+\lambda_\beta^+
+X^{+-}X^{\alpha+}\lambda_\alpha^+
+(\Gamma^a)^{\alpha\beta}(\nabla_aW)X_\alpha^+\lambda_\beta^+,\\
\lambda^{\alpha+}(D_\alpha X^{\rho-})\lambda_\rho^+
={}&-\tfrac i8YB^{++}
-\tfrac i2(\Gamma^a)^{\alpha\beta}\lambda_\alpha^+\lambda_\beta^+\nabla^cW_{ac}
-\tfrac i8\varepsilon^{abcde}(\Gamma_a)^{\alpha\beta}W_{bc}W_{de}\lambda_\alpha^+\lambda_\beta^+,\\
\lambda^{\alpha+}D_\alpha(X^{\rho-}\lambda_\rho^+)
={}&\lambda^{\alpha+}(D_\alpha X^{\rho-})\lambda_\rho^+
+X^{++}X^{\alpha-}\lambda_\alpha^+.
\end{aligned}
\tag{S2-115}
```

The first term in the first line has a minus sign because $`\varepsilon^{\rho\sigma}\lambda_\rho^-=-\lambda^{\sigma-}`$. The second line retains only the antisymmetric spinor part of $`D_\alpha X_\beta^-`$; its $`X_{\alpha\beta}^{+-}`$ term contracts to zero. Its scalar $`W^{ab}W_{ab}`$ contributions cancel within (S2-103), so no such term is omitted there.

Finally differentiate (S2-107). Even the last, explicitly-$`W`$ part contributes to the selected coefficient because $`D_\alpha W=i\lambda_\alpha^+`$. Multiplying by the prefactor in the fourth term of (S2-101) gives the useful fully specified intermediate equality

```math
\begin{aligned}
-\tfrac i{16}\lambda^{\alpha+}(D_\alpha D^{++}X^{--})_0={}&
-\tfrac12\lambda^{\alpha+}(D_\alpha\Box W)_0
+\tfrac12\lambda^{\alpha+}(D_\alpha(W_{ab}F^{ab}))_0\\
&+\tfrac5{16}\lambda^{\alpha+}D_\alpha(X^{\rho+}\lambda_\rho^-)
-\tfrac9{16}\lambda^{\alpha+}D_\alpha(X^{\rho-}\lambda_\rho^+)
-\tfrac{3i}{64}YB^{++}+\tfrac{31i}{64}W^{ab}W_{ab}B^{++}.
\end{aligned}
\tag{S2-116}
```

Equations (S2-112), (S2-114) and (S2-115) evaluate every derivative on its right-hand side. For example its divergence coefficient is $`-9i/32+9i/32=0`$; its scalar Weyl-square coefficient is $`9i/128-i/2+31i/64=7i/128`$; and its Weyl-tensor-descendant coefficient is $`-3/16-5/16=-1/2`$.

### 4.21 Four derivatives of the gaugino, and then of its bilinear

The fourth derivative is also required in (S2-101). Start with the **full** previously derived (S2-72):

```math
\begin{aligned}
D_\alpha D^{++}\lambda_\rho^-={}&4i\nabla_{\alpha\rho}X^{++}-8iW_{\alpha\rho}X^{++}-4WX_{\alpha\rho}^{++}
-8iW_{\alpha\rho\tau}^+\lambda^{\tau+}
+i\varepsilon_{\alpha\rho}X^{\tau+}\lambda_\tau^+
+2iX_\alpha^+\lambda_\rho^+-2iX_\rho^+\lambda_\alpha^+.
\end{aligned}
\tag{S2-117}
```

Here $`D_\beta\nabla_aX^{++}`$ is obtained by applying the mixed commutator to $`X^{++}`$, for which $`D_\beta X^{++}=0`$. Its dilatation coefficient is $`-2/4=-1/2`$ and its SU(2) coefficient is $`+3/4`$, giving $`+1/4`$. Its S action is $`S_{\gamma+}X^{++}=-2\lambda_\gamma^+`$. Hence

```math
\begin{gathered}
D_\beta\nabla_aX^{++}=\tfrac14(\Gamma_a)_\beta{}^\tau X_\tau^+X^{++}
-2R(S)_{a\beta}^{+,\tau+}\lambda_\tau^+,\qquad
D_\beta X_{\alpha\rho}^{++}=0,\\
D_\beta W_{\alpha\rho\tau}^+=-\tfrac12\big(\varepsilon_{\beta\alpha}X_{\rho\tau}^{++}
+\varepsilon_{\beta\rho}X_{\alpha\tau}^{++}+\varepsilon_{\beta\tau}X_{\alpha\rho}^{++}\big),\qquad
D_\beta\lambda^{\tau+}=-\delta_\beta{}^\tau X^{++}.
\end{gathered}
\tag{S2-118}
```

The second and third identities are S23 (2.6e,c) at all plus SU(2) indices. The terms $`-8iW_{\alpha\rho\beta}^+X^{++}`$ from differentiating the second term of (S2-117) and $`+8iW_{\alpha\rho\beta}^+X^{++}`$ from differentiating its fourth term cancel. After that cancellation, differentiate the seven terms of (S2-117) in order:

```math
\begin{aligned}
D_\beta(4i\nabla_{\alpha\rho}X^{++})={}&i(\Gamma^a)_{\alpha\rho}(\Gamma_a)_\beta{}^\tau X_\tau^+X^{++}
-8i(\Gamma^a)_{\alpha\rho}R(S)_{a\beta}^{+,\tau+}\lambda_\tau^+,\\
D_\beta(-8iW_{\alpha\rho}X^{++})\big|_{X_\gamma}={}&-4i(\varepsilon_{\beta\alpha}X_\rho^++\varepsilon_{\beta\rho}X_\alpha^+)X^{++},\\
D_\beta(-4WX_{\alpha\rho}^{++})={}&-4i\lambda_\beta^+X_{\alpha\rho}^{++},\\
D_\beta(-8iW_{\alpha\rho\tau}^+\lambda^{\tau+})\big|_{X_{\gamma\delta}}={}&
4i(\varepsilon_{\beta\alpha}X_{\rho\tau}^{++}+\varepsilon_{\beta\rho}X_{\alpha\tau}^{++}+\varepsilon_{\beta\tau}X_{\alpha\rho}^{++})\lambda^{\tau+},\\
D_\beta(i\varepsilon_{\alpha\rho}X^{\tau+}\lambda_\tau^+)={}&i\varepsilon_{\alpha\rho}(-X_{\beta\sigma}^{++}\lambda^{\sigma+}+X_\beta^+X^{++}),\\
D_\beta(2iX_\alpha^+\lambda_\rho^+)={}&2iX_{\beta\alpha}^{++}\lambda_\rho^++2i\varepsilon_{\beta\rho}X_\alpha^+X^{++},\\
D_\beta(-2iX_\rho^+\lambda_\alpha^+)={}&-2iX_{\beta\rho}^{++}\lambda_\alpha^+-2i\varepsilon_{\beta\alpha}X_\rho^+X^{++}.
\end{aligned}
\tag{S2-119}
```

The restriction labels in two lines only remove the mutually canceled three-spinor terms just displayed. Contract each line with $`-\varepsilon^{\beta\alpha}`$ to obtain $`D^{++}D^{++}\lambda_\rho^-`$. The individual coefficients are

| Differentiated term of (S2-117) | $`iX_\rho^+X^{++}`$ | $`iX_{\rho\tau}^{++}\lambda^{\tau+}`$ |
|---|---:|---:|
| $`4i\nabla_{\alpha\rho}X^{++}`$ | $`-5`$ | $`9`$ |
| $`-8iW_{\alpha\rho}X^{++}`$ | $`-20`$ | $`0`$ |
| $`-4WX_{\alpha\rho}^{++}`$ | $`0`$ | $`-4`$ |
| $`-8iW_{\alpha\rho\tau}^+\lambda^{\tau+}`$ | $`0`$ | $`24`$ |
| $`i\varepsilon_{\alpha\rho}X^{\tau+}\lambda_\tau^+`$ | $`-1`$ | $`1`$ |
| $`2iX_\alpha^+\lambda_\rho^+`$ | $`2`$ | $`0`$ |
| $`-2iX_\rho^+\lambda_\alpha^+`$ | $`-8`$ | $`2`$ |
| Sum | $`-32`$ | $`32`$ |

The first row uses $`\Gamma^a\Gamma_a=-5\mathbf1`$ and the first term of (S2-104); its curvature contraction is $`-\varepsilon^{\beta\alpha}[-8i(\Gamma^a)_{\alpha\rho}R(S)_{a\beta}^{+,\tau+}\lambda_\tau^+]=9iX_{\rho\tau}^{++}\lambda^{\tau+}`$. The remaining rows use just $`\varepsilon^{\alpha\beta}\varepsilon_{\alpha\beta}=-4`$ and index raising. Multiplication by $`-1/32`$ therefore gives

```math
\Delta\lambda_\rho^-=iX_\rho^+X^{++}-iX_{\rho\tau}^{++}\lambda^{\tau+}.
\tag{S2-120}
```

Now apply four derivatives to $`B^{--}=\lambda^{\rho-}\lambda_\rho^-`$. Equation (S2-66) has already supplied its first three derivatives. Differentiating once more before contracting the four derivative indices gives multiplicities $`-2,+8,-6`$ for the $`4+0`$, $`3+1`$, and $`2+2`$ distributions. In detail, the first term of $`D^3B`$ supplies $`-2D^4\lambda\lambda`$ and $`-2D^3\lambda D\lambda`$. The second supplies three placements; after antisymmetrizing the four indices its $`D^3\lambda D\lambda`$ terms add to the first product to give $`+8`$, while the odd parity of $`D^2\lambda`$ gives $`-6D^2\lambda D^2\lambda`$. Multiplication by $`-1/96`$ and $`\varepsilon D^3=3D D^{++}`$ yields

```math
\begin{aligned}
\Delta B^{--}={}&-2(\Delta\lambda_\rho^-)\lambda^{\rho-}
-\tfrac14\varepsilon^{\delta\alpha}(D_\alpha D^{++}\lambda_\rho^-)\varepsilon^{\rho\sigma}D_\delta\lambda_\sigma^-
+\tfrac1{16}\varepsilon^{\alpha\beta\gamma\delta}(D_\alpha D_\beta\lambda_\rho^-)\varepsilon^{\rho\sigma}(D_\gamma D_\delta\lambda_\sigma^-).
\end{aligned}
\tag{S2-121}
```

This explicitly proves the last three coefficients in (S2-101): $`(-i/8)(-2)=i/4`$, $`(-i/8)(-1/4)=i/32`$, and $`(-i/8)(1/16)=-i/128`$.

### 4.22 Reducing the twelve contributions without hiding any remainder

We now evaluate (S2-101) in its displayed order. All formulas in this subsection are **contributions to the numerator**; the common $`W^{-2}`$ is restored in the final result. First, the leading term is already reduced because $`\lambda^{\alpha+}X_\alpha^-=X^{\alpha-}\lambda_\alpha^+`$: odd interchange and the antisymmetric raising metric give two minus signs. Thus it is $`-3X^{++}X^{\alpha-}\lambda_\alpha^+/8`$.

For the second term, insert (S2-106) and contract the two leading gauginos using (S2-77). The scalar spinor metric gives $`\varepsilon^{\alpha\beta\gamma\delta}\lambda_\alpha^+\lambda_\beta^+\varepsilon_{\gamma\delta}=2B^{++}`$; the gamma matrix is traceless, leaving the second term in (S2-77). Hence

```math
\begin{aligned}
-\tfrac1{16}\varepsilon^{\alpha\beta\gamma\delta}\lambda_\alpha^+\lambda_\beta^+(D_\gamma D_\delta X^{--})_1
={}&\tfrac{3i}{128}YB^{++}-\tfrac{31i}{128}W^{ab}W_{ab}B^{++}
-\tfrac{3i}{8}(\Gamma^a)^{\alpha\beta}\lambda_\alpha^+\lambda_\beta^+\nabla^cW_{ac}\\
&+\tfrac i{32}\varepsilon^{abcde}(\Gamma_a)^{\alpha\beta}W_{bc}W_{de}\lambda_\alpha^+\lambda_\beta^+.
\end{aligned}
\tag{S2-122}
```

For the third term, multiplication of the four scalar-$`W^0`$ terms in (S2-107) by $`iX^{++}/16`$ gives

```math
\begin{aligned}
\tfrac i{16}X^{++}(D^{++}X^{--})_0
={}&\tfrac12X^{++}\Box W-\tfrac12X^{++}W_{ab}F^{ab}
-\tfrac5{16}X^{++}X^{\alpha+}\lambda_\alpha^-
+\tfrac9{16}X^{++}X^{\alpha-}\lambda_\alpha^+.
\end{aligned}
\tag{S2-123}
```

The fourth term is obtained by substituting the three explicit identities into (S2-116). Keeping even the terms that will cancel later gives

```math
\begin{aligned}
-\tfrac i{16}\lambda^{\alpha+}(D_\alpha D^{++}X^{--})_0={}&
-\tfrac i2\lambda^{\alpha+}\Box\lambda_\alpha^+
-\tfrac i8\varepsilon^{abcde}(\Sigma_{ab})^{\alpha\beta}W_{de}\lambda_\alpha^+\nabla_c\lambda_\beta^+
+\tfrac i2(\Gamma^a)^{\alpha\beta}W_{ab}\lambda_\alpha^+\nabla^b\lambda_\beta^+\\
&+\tfrac{3i}{128}YB^{++}+\tfrac{7i}{128}W^{ab}W_{ab}B^{++}
-\tfrac{7i}{128}\varepsilon^{abcde}(\Gamma_a)^{\alpha\beta}W_{bc}W_{de}\lambda_\alpha^+\lambda_\beta^+\\
&+\tfrac3{16}(\Sigma_{ab})^{\alpha\beta}F^{ab}X_\alpha^+\lambda_\beta^+
-\tfrac9{16}X^{++}X^{\alpha-}\lambda_\alpha^+
+\tfrac5{16}X^{+-}X^{\alpha+}\lambda_\alpha^+\\
&+\tfrac7{16}(\Gamma^a)^{\alpha\beta}(\nabla_aW)X_\alpha^+\lambda_\beta^+
+\tfrac12F^{ab}W_{ab}^{\alpha+}\lambda_\alpha^+
-\tfrac12X_{\alpha\beta}^{++}\lambda^{\alpha+}\lambda^{\beta-}.
\end{aligned}
\tag{S2-124}
```

For instance, the $`\Sigma F X\lambda`$ coefficient is $`1/2-5/16=3/16`$; the $`(\nabla W)X\lambda`$ coefficient is $`1/8+5/16=7/16`$; and the epsilon Weyl-square coefficient is $`-1/8+9/128=-7/128`$. These checks retain the fermion order used in (S2-115).

For the fifth and sixth terms, differentiate the bilinear by (S2-66), retaining respectively one and two explicit powers of scalar $`W`$:

```math
\begin{aligned}
(D_\gamma D_\delta B^{--})_1={}&
-2\big(-\tfrac32\varepsilon_{\gamma\delta}X_\rho^+-\tfrac12\varepsilon_{\gamma\rho}X_\delta^++\tfrac12\varepsilon_{\delta\rho}X_\gamma^+\big)\lambda^{\rho-}\\
&+4W_{\delta\rho}\varepsilon^{\rho\sigma}(-2F_{\gamma\sigma}-\varepsilon_{\gamma\sigma}X^{+-}-\nabla_{\gamma\sigma}W)
+4(-2F_{\delta\rho}-\varepsilon_{\delta\rho}X^{+-}-\nabla_{\delta\rho}W)\varepsilon^{\rho\sigma}W_{\gamma\sigma},\\
(D_\gamma D_\delta B^{--})_2={}&-8W_{\delta\rho}\varepsilon^{\rho\sigma}W_{\gamma\sigma}.
\end{aligned}
\tag{S2-125}
```

The first line is (S2-49)'s explicit-$`W`$ coefficient multiplied by $`-2\lambda^{\rho-}`$; the next two products count both placements of $`-2W_{\alpha\beta}W`$ in $`D\lambda`$. In the fifth term's trace the $`X^{+-}`$ and $`\nabla W`$ products vanish by $`\mathop{\mathrm{tr}}\nolimits\Sigma=\mathop{\mathrm{tr}}\nolimits(\Gamma\Sigma)=0`$. The two $`F`$ placements add to $`X^{++}W\cdot F/4`$. For its fermionic part, tracing $`(D_\gamma D_\delta\lambda_\rho^-)_1`$ gives $`7X_\rho^+`$, equivalently $`(D^{++}\lambda_\rho^-)_1=-7X_\rho^+`$, so the coefficient is $`7/16`$. For the sixth term use the Weyl-square specialization of (S2-88), including the identical two-form placements. The complete results are

```math
\begin{aligned}
-\tfrac1{64}X^{++}\varepsilon^{\alpha\beta\gamma\delta}\varepsilon_{\alpha\beta}(D_\gamma D_\delta B^{--})_1
&=\tfrac14X^{++}W_{ab}F^{ab}+\tfrac7{16}X^{++}X^{\alpha+}\lambda_\alpha^-,\\
-\tfrac{3i}{64}\varepsilon^{\alpha\beta\gamma\delta}\lambda_\alpha^+\lambda_\beta^+(D_\gamma D_\delta B^{--})_2
&=\tfrac{3i}{32}W^{ab}W_{ab}B^{++}
+\tfrac{3i}{64}\varepsilon^{abcde}(\Gamma_a)^{\alpha\beta}W_{bc}W_{de}\lambda_\alpha^+\lambda_\beta^+.
\end{aligned}
\tag{S2-126}
```

The seventh term, $`X_{\alpha\beta}^{++}\lambda^{\alpha+}\lambda^{\beta-}/4`$, is already explicit. It came from $`(D_\alpha D^{++}\lambda_\rho^-)_1=-4X_{\alpha\rho}^{++}`$ in the three-derivative bilinear and has not been dropped by falsely imposing a gamma trace.

For the eighth term, insert separately the six $`\nabla\lambda`$ terms and the three $`W\lambda`$ terms in (S2-49). Its derivative part is exactly (S2-82) with the two-form there replaced by $`W_{ab}`$. Its algebraic part is (S2-89) with $`F_{ab}=W_{ab}`$. Those earlier identities included their original prefactors, which equal the present $`-1/8`$. Their sums give

```math
\begin{aligned}
-\tfrac18\varepsilon^{\alpha\beta\gamma\delta}\lambda_\alpha^+(D_\beta D_\gamma\lambda_\rho^-)_0\varepsilon^{\rho\sigma}W_{\delta\sigma}
={}&-\tfrac i8\varepsilon^{abcde}(\Sigma_{ab})^{\alpha\beta}W_{de}\lambda_\alpha^+\nabla_c\lambda_\beta^+
-\tfrac i4(\Gamma^a)^{\alpha\beta}W_{ab}\lambda_\alpha^+\nabla^b\lambda_\beta^+\\
&+\tfrac{5i}{32}W^{ab}W_{ab}B^{++}
-\tfrac i{64}\varepsilon^{abcde}(\Gamma_a)^{\alpha\beta}W_{bc}W_{de}\lambda_\alpha^+\lambda_\beta^+.
\end{aligned}
\tag{S2-127}
```

For the ninth term there are only three insertions from (S2-49): $`-3\varepsilon_{\beta\gamma}X_\rho^+/2`$, $`-\varepsilon_{\beta\rho}X_\gamma^+/2`$, and $`+\varepsilon_{\gamma\rho}X_\beta^+/2`$. Insert each into the displayed contraction in (S2-101), expand the four-index epsilon into its three metric products, and move the odd Weyl spinor left. Contracting in turn with $`-2F`$, $`-\varepsilon X^{+-}`$ and $`-\nabla W`$ yields the following three results:

```math
\begin{aligned}
&\tfrac1{16}\varepsilon^{\alpha\beta\gamma\delta}\lambda_\alpha^+
\big(-\tfrac32\varepsilon_{\beta\gamma}X_\rho^+-\tfrac12\varepsilon_{\beta\rho}X_\gamma^++\tfrac12\varepsilon_{\gamma\rho}X_\beta^+\big)
\varepsilon^{\rho\sigma}(-2F_{\delta\sigma}-\varepsilon_{\delta\sigma}X^{+-}-\nabla_{\delta\sigma}W)\\
&\qquad=\tfrac3{16}(\Sigma_{ab})^{\alpha\beta}F^{ab}X_\alpha^+\lambda_\beta^+
-\tfrac1{16}X^{+-}X^{\alpha+}\lambda_\alpha^+
-\tfrac5{16}(\Gamma^a)^{\alpha\beta}(\nabla_aW)X_\alpha^+\lambda_\beta^+.
\end{aligned}
\tag{S2-128}
```

The three insertions in (S2-128) can also be audited individually. Each entry includes the common prefactor $`1/16`$ and the indicated factor $`-2F`$, $`-\varepsilon X^{+-}`$ or $`-\nabla W`$:

| Inserted term of $`(D_\beta D_\gamma\lambda_\rho^-)_1`$ | $`(\Sigma_{ab})^{\alpha\beta}F^{ab}X_\alpha^+\lambda_\beta^+`$ | $`X^{+-}X^{\alpha+}\lambda_\alpha^+`$ | $`(\Gamma^a)^{\alpha\beta}(\nabla_aW)X_\alpha^+\lambda_\beta^+`$ |
|---|---:|---:|---:|
| $`-3\varepsilon_{\beta\gamma}X_\rho^+/2`$ | $`3/16`$ | $`-3/16`$ | $`-3/16`$ |
| $`-\varepsilon_{\beta\rho}X_\gamma^+/2`$ | $`0`$ | $`1/16`$ | $`-1/16`$ |
| $`+\varepsilon_{\gamma\rho}X_\beta^+/2`$ | $`0`$ | $`1/16`$ | $`-1/16`$ |
| Sum | $`3/16`$ | $`-1/16`$ | $`-5/16`$ |

The zeros in the first column contract a symmetric $`F_{\alpha\beta}`$ with the remaining antisymmetric spinor metric. The two $`1/16`$ entries in the middle column use the scalar metric trace, while the corresponding gradient entries change sign because $`(\Gamma^a)_{\alpha\beta}`$ is antisymmetric. No fermion field is commuted without the odd sign already included in the table.

The tenth term follows directly from (S2-120):

```math
\begin{aligned}
\tfrac i4(\Delta\lambda_\rho^-)_0\lambda^{\rho-}
&=-\tfrac14X^{++}X_\rho^+\lambda^{\rho-}
+\tfrac14X_{\rho\tau}^{++}\lambda^{\tau+}\lambda^{\rho-}\\
&=\tfrac14X^{++}X^{\alpha+}\lambda_\alpha^-
+\tfrac14X_{\alpha\beta}^{++}\lambda^{\alpha+}\lambda^{\beta-}.
\end{aligned}
\tag{S2-129}
```

The first sign change uses $`X_\rho^+\lambda^{\rho-}=-X^{\rho+}\lambda_\rho^-`$, without interchanging the two odd fields. The second term uses the symmetry of $`X_{\rho\tau}^{++}`$.

For the eleventh term use all six scalar-$`W^0`$ terms in (S2-117). The derivative part $`4i\nabla_{\alpha\rho}X^{++}`$ contracts only with $`-\nabla_{\delta\sigma}W`$; its $`F`$ and auxiliary traces are zero. It gives $`\nabla^aW\nabla_aX^{++}/2`$. The $`-8iW_{\alpha\rho}X^{++}`$ term contracts only with $`-2F`$ and gives $`X^{++}W\cdot F/4`$. In the three-spinor term, the scalar and gradient traces vanish by full spinor symmetry, leaving $`-F^{ab}W_{ab}^{\alpha+}\lambda_\alpha^+/4`$. The last three terms contribute $`-X^{+-}X^{\alpha+}\lambda_\alpha^+/4-(\Gamma^a)^{\alpha\beta}\nabla_aW X_\alpha^+\lambda_\beta^+/8`$; their $`F X\lambda`$ pieces cancel. Thus

```math
\begin{aligned}
&\tfrac i{32}\varepsilon^{\delta\alpha}(D_\alpha D^{++}\lambda_\rho^-)_0\varepsilon^{\rho\sigma}
(-2F_{\delta\sigma}-\varepsilon_{\delta\sigma}X^{+-}-\nabla_{\delta\sigma}W)\\
&\qquad=\tfrac12(\nabla^aW)\nabla_aX^{++}+\tfrac14X^{++}W_{ab}F^{ab}
-\tfrac14F^{ab}W_{ab}^{\alpha+}\lambda_\alpha^+
-\tfrac14X^{+-}X^{\alpha+}\lambda_\alpha^+
-\tfrac18(\Gamma^a)^{\alpha\beta}(\nabla_aW)X_\alpha^+\lambda_\beta^+.
\end{aligned}
\tag{S2-130}
```

The three Weyl-spinor products just used in (S2-130) have the following separate contractions, including the $`i/32`$ prefactor:

| Inserted term of $`(D_\alpha D^{++}\lambda_\rho^-)_0`$ | $`(\Sigma_{ab})^{\alpha\beta}F^{ab}X_\alpha^+\lambda_\beta^+`$ | $`X^{+-}X^{\alpha+}\lambda_\alpha^+`$ | $`(\Gamma^a)^{\alpha\beta}(\nabla_aW)X_\alpha^+\lambda_\beta^+`$ |
|---|---:|---:|---:|
| $`i\varepsilon_{\alpha\rho}X^{\tau+}\lambda_\tau^+`$ | $`0`$ | $`-1/8`$ | $`0`$ |
| $`2iX_\alpha^+\lambda_\rho^+`$ | $`-1/16`$ | $`-1/16`$ | $`-1/16`$ |
| $`-2iX_\rho^+\lambda_\alpha^+`$ | $`1/16`$ | $`-1/16`$ | $`-1/16`$ |
| Sum | $`0`$ | $`-1/4`$ | $`-1/8`$ |

In the first row the $`F`$ and gradient traces are zero; the scalar trace contributes four, multiplying $`(i/32)i=-1/32`$ to give $`-1/8`$. In the last two rows the symmetry of the field-strength spinor makes the $`F`$ coefficients opposite, while the antisymmetric scalar and gamma pairings make the other coefficients equal. This accounts for every Weyl-spinor term in (S2-130).

For completeness, the twelfth term requires the product of two third vector derivatives, not just a repeated scalar derivative. Insert (S2-49) in both factors. There are a $`\nabla\lambda\nabla\lambda`$ part, two cross placements $`\nabla\lambda\,W\lambda`$, and a $`W\lambda W\lambda`$ part. The following table keeps the first factor's six derivative terms separate, while the second factor is the full derivative part of (S2-49). Every entry includes the prefactor $`-i\varepsilon^{\alpha\beta\gamma\delta}\varepsilon^{\rho\sigma}/128`$ of the twelfth term. The last two columns include **both** cross placements; they are equal after interchanging two odd descendants and the antisymmetric $`\varepsilon^{\rho\sigma}`$, giving a net plus sign.

| First derivative term in $`(D_\alpha D_\beta\lambda_\rho^-)_0`$ | $`i(\nabla^a\lambda^{\tau+})\nabla_a\lambda_\tau^+`$ | $`i(\Sigma^{ab})^{\tau\upsilon}(\nabla_a\lambda_\tau^+)\nabla_b\lambda_\upsilon^+`$ | $`i\varepsilon^{abcde}(\Sigma_{ab})^{\tau\upsilon}W_{de}\lambda_\tau^+\nabla_c\lambda_\upsilon^+`$ | $`i(\Gamma^a)^{\tau\upsilon}W_{ab}\lambda_\tau^+\nabla^b\lambda_\upsilon^+`$ |
|---|---:|---:|---:|---:|
| $`i\nabla_{\alpha\beta}\lambda_\rho^+`$ | $`-1/16`$ | $`-1/8`$ | $`-1/64`$ | $`-1/32`$ |
| $`i\nabla_{\alpha\rho}\lambda_\beta^+`$ | $`-3/32`$ | $`1/16`$ | $`-3/128`$ | $`1/64`$ |
| $`i\varepsilon_{\alpha\beta}\nabla_\rho{}^\tau\lambda_\tau^+`$ | $`1/16`$ | $`-1/8`$ | $`5/64`$ | $`-5/32`$ |
| $`i\varepsilon_{\alpha\rho}\nabla_\beta{}^\tau\lambda_\tau^+`$ | $`-1/32`$ | $`1/16`$ | $`3/128`$ | $`-3/64`$ |
| $`-i\varepsilon_{\beta\rho}\nabla_\alpha{}^\tau\lambda_\tau^+`$ | $`-1/32`$ | $`1/16`$ | $`3/128`$ | $`-3/64`$ |
| $`-i\nabla_{\beta\rho}\lambda_\alpha^+`$ | $`-3/32`$ | $`1/16`$ | $`-3/128`$ | $`1/64`$ |
| Sum | $`-1/4`$ | $`0`$ | $`1/16`$ | $`-1/4`$ |

These contractions use the complete three-product expansion of the four-spinor epsilon, (S2-68), and $`\Gamma^a\Gamma^b=-\eta^{ab}\mathbf1-2\Sigma^{ab}`$. Thus the second column is a genuine cancellation of a two-derivative contraction; it has not been removed by integrating by parts or commuting vector derivatives.

The three algebraic terms of the first factor, paired with the full algebraic second factor, give

| First algebraic term | $`iW^{ab}W_{ab}B^{++}`$ | $`i\varepsilon^{abcde}(\Gamma_a)^{\tau\upsilon}W_{bc}W_{de}\lambda_\tau^+\lambda_\upsilon^+`$ |
|---|---:|---:|
| $`iW_{\beta\rho}\lambda_\alpha^+`$ | $`5/512`$ | $`-1/1024`$ |
| $`-iW_{\alpha\rho}\lambda_\beta^+`$ | $`5/512`$ | $`-1/1024`$ |
| $`-3i\varepsilon_{\alpha\beta}W_{\rho\tau}\lambda^{\tau+}`$ | $`-15/256`$ | $`15/512`$ |
| Sum | $`-5/128`$ | $`7/256`$ |

For these columns insert $`W_{\alpha\beta}=\Sigma^{ab}_{\alpha\beta}W_{ab}/2`$ twice, so that the common two-form conversion is $`1/4`$; the spinor scalar and gamma projections are (S2-105). Including these $`1/2`$ factors is necessary to obtain the displayed denominators. Adding all three types of products gives the fully reduced twelfth contribution:

```math
\begin{aligned}
&-\tfrac i{128}\varepsilon^{\alpha\beta\gamma\delta}(D_\alpha D_\beta\lambda_\rho^-)_0\varepsilon^{\rho\sigma}(D_\gamma D_\delta\lambda_\sigma^-)_0\\
&\qquad=-\tfrac i4(\nabla^a\lambda^{\alpha+})\nabla_a\lambda_\alpha^+
+\tfrac i{16}\varepsilon^{abcde}(\Sigma_{ab})^{\alpha\beta}W_{de}\lambda_\alpha^+\nabla_c\lambda_\beta^+
-\tfrac i4(\Gamma^a)^{\alpha\beta}W_{ab}\lambda_\alpha^+\nabla^b\lambda_\beta^+\\
&\qquad\quad-\tfrac{5i}{128}W^{ab}W_{ab}B^{++}
+\tfrac{7i}{256}\varepsilon^{abcde}(\Gamma_a)^{\alpha\beta}W_{bc}W_{de}\lambda_\alpha^+\lambda_\beta^+.
\end{aligned}
\tag{S2-131}
```

### 4.23 Collecting the coefficient and restoring the symmetric SU(2) indices

Every contribution in (S2-101) is now evaluated. Before combining the surviving terms, explicitly check the structures that disappear:

```math
\begin{aligned}
X^{++}W_{ab}F^{ab}:&\quad-\tfrac12+\tfrac14+\tfrac14=0,\qquad
X_{\alpha\beta}^{++}\lambda^{\alpha+}\lambda^{\beta-}:\quad-\tfrac12+\tfrac14+\tfrac14=0,\\
X^{+-}X^{\alpha+}\lambda_\alpha^+:&\quad\tfrac5{16}-\tfrac1{16}-\tfrac14=0,\qquad
(\Gamma^a)^{\alpha\beta}(\nabla_aW)X_\alpha^+\lambda_\beta^+:\quad\tfrac7{16}-\tfrac5{16}-\tfrac18=0,\\
i(\Gamma^a)^{\alpha\beta}W_{ab}\lambda_\alpha^+\nabla^b\lambda_\beta^+:&\quad\tfrac12-\tfrac14-\tfrac14=0.
\end{aligned}
\tag{S2-132}
```

The twelve surviving coefficients can now be followed by ordinary rational addition:

| Surviving numerator in the $`++`$ component | Contributions | Total |
|---|---|---:|
| $`X^{++}\Box W`$ | $`1/2`$ from (S2-123) | $`1/2`$ |
| $`(\nabla^aW)\nabla_aX^{++}`$ | $`1/2`$ from (S2-130) | $`1/2`$ |
| $`F^{ab}W_{ab}^{\alpha+}\lambda_\alpha^+`$ | $`1/2-1/4`$ | $`1/4`$ |
| $`i\lambda^{\alpha+}\Box\lambda_\alpha^+`$ | $`-1/2`$ from (S2-124) | $`-1/2`$ |
| $`i(\nabla^a\lambda^{\alpha+})\nabla_a\lambda_\alpha^+`$ | $`-1/4`$ from (S2-131) | $`-1/4`$ |
| $`i\varepsilon^{abcde}(\Sigma_{ab})^{\alpha\beta}W_{de}\lambda_\alpha^+\nabla_c\lambda_\beta^+`$ | $`-1/8-1/8+1/16`$ | $`-3/16`$ |
| $`i(\Gamma^a)^{\alpha\beta}\lambda_\alpha^+\lambda_\beta^+\nabla^cW_{ac}`$ | $`-3/8`$ from (S2-122) | $`-3/8`$ |
| $`iYB^{++}`$ | $`3/128+3/128`$ | $`3/64`$ |
| $`(\Sigma_{ab})^{\alpha\beta}F^{ab}X_\alpha^+\lambda_\beta^+`$ | $`3/16+3/16`$ | $`3/8`$ |
| $`iW^{ab}W_{ab}B^{++}`$ | $`(-31+7+12+20-5)/128`$ | $`3/128`$ |
| $`i\varepsilon^{abcde}(\Gamma_a)^{\alpha\beta}W_{bc}W_{de}\lambda_\alpha^+\lambda_\beta^+`$ | $`(8-14+12-4+7)/256`$ | $`9/256`$ |
| $`X^{++}X^{\alpha k}\lambda_{\alpha k}`$ | SU(2) collection below | $`-3/8`$ |

For the last row the two separate components have coefficients

```math
\begin{aligned}
X^{++}X^{\alpha+}\lambda_\alpha^-:&\quad-\tfrac5{16}+\tfrac7{16}+\tfrac14=\tfrac38,\qquad
X^{++}X^{\alpha-}\lambda_\alpha^+:\quad-\tfrac38+\tfrac9{16}-\tfrac9{16}=-\tfrac38,\\
\tfrac38X^{++}(X^{\alpha+}\lambda_\alpha^--X^{\alpha-}\lambda_\alpha^+)
&=-\tfrac38X^{++}X^{\alpha k}\lambda_{\alpha k}.
\end{aligned}
\tag{S2-133}
```

The last equality uses the fixed lowering convention, rather than a fermion interchange: $`X^{\alpha k}\lambda_{\alpha k}=-X^{\alpha+}\lambda_\alpha^-+X^{\alpha-}\lambda_\alpha^+`$. All other plus indices restore uniquely to a symmetric external pair $`ij`$, because the calculation was made with an arbitrary constant isotwistor $`u_i^+`$, as in section 4.6. The resulting full $`W^{-2}`$ expression is collected under **Final Result**, (S2-134).

### 4.24 Selecting the complete $`W^{-1}`$ coefficient

<!-- ASSERT_CONVENTION: source_frame=Gold traceless Standard-Weyl superspace, metric_signature=(-,+,+,+,+), natural_units=hbar=c=1, scope=classical off-shell gauge-unfixed LOG primary, fermions=all degrees retained -->

This continuation derives the seven $`W^{-1}`$ terms. The starting point is still S23 (3.24), in the equivalent projected form (S2-100). We use S23 (2.6a–f), (2.13a–c), (2.15), and C24 (A.1), (A.3a–f); the last line of (A.3f) continues onto the next source page. No field equation, gauge, integration by parts, or fermion truncation is used. The new calculation needs the K curvature because a vector derivative of a primary is not itself primary.

The notation $`D_\alpha`$, $`D^{++}`$, $`\Delta`$, $`B^{--}`$ and the explicit-scalar-$`W`$ coefficient subscripts retain their earlier meanings. In particular, $`\Delta`$ here contains four plus spinor derivatives. The terms at the required pole are

```math
\begin{aligned}
\left.H^{++}\right|_{W^{-1}}=W^{-1}\Big\{&
-\tfrac12(\Delta X^{--})_0
+\tfrac i{16}X^{++}(D^{++}X^{--})_1
-\tfrac i{16}\lambda^{\alpha+}(D_\alpha D^{++}X^{--})_1\\
&-\tfrac1{64}X^{++}\varepsilon^{\alpha\beta\gamma\delta}\varepsilon_{\alpha\beta}(D_\gamma D_\delta B^{--})_2
-\tfrac18\varepsilon^{\alpha\beta\gamma\delta}\lambda_\alpha^+(D_\beta D_\gamma\lambda_\rho^-)_1\varepsilon^{\rho\sigma}W_{\delta\sigma}
-\tfrac i8(\Delta B^{--})_1\Big\}.
\end{aligned}
\tag{S2-135}
```

This exhausts the product rule. The $`W^{-1}\Delta X^{--}`$ term enters for the first time. In the first product of (S2-100), the $`2+2`$ and $`1+3`$ distributions have denominator $`W^2`$ and a descendant linear in scalar $`W`$, giving the second and third terms above. The first product's $`3+1`$ distribution has denominator at least $`W^3`$ and at most one explicit scalar $`W`$, so cannot enter. In the second product, the $`2+2`$ and $`1+3`$ distributions have denominator $`W^3`$ and descendants quadratic in scalar $`W`$. The $`0+4`$ distribution gives the last term. The remaining placements have poles at least two. This is collection of an exact rational expression, not an expansion in a small field.

Inserting (S2-107), (S2-117), (S2-120), (S2-121), and (S2-125) resolves that last term into two parts and gives a convenient seven-contribution expression:

```math
\begin{aligned}
\left.H^{++}\right|_{W^{-1}}=W^{-1}\Big\{&
-\tfrac12(\Delta X^{--})_0+\tfrac3{64}X^{++}Y-\tfrac{31}{64}X^{++}W^{ab}W_{ab}
-\tfrac i{16}\lambda^{\alpha+}(D_\alpha D^{++}X^{--})_1+\tfrac18X^{++}W^{ab}W_{ab}\\
&-\tfrac18\varepsilon^{\alpha\beta\gamma\delta}\lambda_\alpha^+(D_\beta D_\gamma\lambda_\rho^-)_1\varepsilon^{\rho\sigma}W_{\delta\sigma}\\
&+\tfrac i{32}\varepsilon^{\delta\alpha}\varepsilon^{\rho\sigma}\Big[-4X_{\alpha\rho}^{++}(-2F_{\delta\sigma}-\varepsilon_{\delta\sigma}X^{+-}-\nabla_{\delta\sigma}W)
-2(D_\alpha D^{++}\lambda_\rho^-)_0W_{\delta\sigma}\Big]\\
&-\tfrac i{128}\varepsilon^{\alpha\beta\gamma\delta}\varepsilon^{\rho\sigma}\Big[(D_\alpha D_\beta\lambda_\rho^-)_0(D_\gamma D_\delta\lambda_\sigma^-)_1
+(D_\alpha D_\beta\lambda_\rho^-)_1(D_\gamma D_\delta\lambda_\sigma^-)_0\Big]\Big\}.
\end{aligned}
\tag{S2-136}
```

The two factors in each product on the last line are odd; their written order is retained. There is no contribution from $`\Delta\lambda^-`$ at explicit scalar degree one, because (S2-120) has no scalar $`W`$. All seven contributions in (S2-136) are reduced below.

### 4.25 The K-curvature trace and $`(D_\alpha\Box W)_1`$

The term omitted from (S2-110) at explicit scalar degree one is

```math
(D_\alpha\Box W)_1=-\tfrac14(\Gamma^a)_\alpha{}^\beta\nabla_aX_\beta^+
-\tfrac14(T^a\Gamma_a)_\alpha{}^\beta X_\beta^+
+2R(K)_{a\alpha}^{+,a}.
\tag{S2-137}
```

The first term differentiates $`-W\Gamma_aX^+/4`$ in (S2-108); the second is the torsion acting on the same expression. The third is the K action $`K_c\nabla_aW=2\eta_{ca}W`$. Thus K curvature must be included even though $`K_cW=0`$.

For use in the untraced commutator below, the full K curvature from C24 (A.3f), including its continuation on PDF page 83, is

```math
\begin{aligned}
R(K)_{b\alpha}^{+,c}={}&\tfrac16(\Gamma^c)_\alpha{}^\beta\nabla^dW_{db\beta}^+
+\tfrac1{12}(\Gamma_b)_\alpha{}^\beta\nabla^dW_d{}^c{}_\beta^+
+\tfrac16\nabla_\alpha{}^\beta W_b{}^c{}_\beta^+
-\tfrac1{24}\varepsilon_b{}^{cdef}\nabla_dW_{ef\alpha}^+\\
&+\tfrac18(\Gamma^c)_\alpha{}^\beta\nabla_bX_\beta^+
+\tfrac1{64}W^{de}(3\Gamma_b\Sigma_{de}\Gamma^c-\Sigma_{de}\Gamma_b\Gamma^c)_\alpha{}^\beta X_\beta^+
-\tfrac1{48}\widetilde W_{bde}(\Gamma^c)_\alpha{}^\beta W^{de}{}_{\beta}^+\\
&+\tfrac18\delta_b{}^cW^{de}W_{de\alpha}^+
+\tfrac1{12}(\Sigma_b{}^c)_\alpha{}^\beta W_{de\beta}^+W^{de}
-\tfrac1{12}W^{de}(\Sigma_{de})_\alpha{}^\beta W_b{}^c{}_\beta^+\\
&+\tfrac{13}{48}W_{bd}W^{dc}{}_{\alpha}^+
+\tfrac{11}{48}W_{bd\alpha}^+W^{dc}
-\tfrac{13}{96}(\Gamma_b)_\alpha{}^\beta W_{de\beta}^+\widetilde W^{dec}.
\end{aligned}
\tag{S2-137a}
```

The dual is $`\widetilde W_{abc}=\varepsilon_{abcde}W^{de}/2`$. No field equation is used in this curvature definition.

Contract the vector indices $`c=b`$ in C24 (A.3f). The first two derivative terms give $`\Gamma^b\nabla^dW_{db\alpha}^+/4`$. The $`\nabla_\alpha{}^\beta W_b{}^b{}_\beta`$ term is zero because the two vector indices of $`W_{ab\alpha}`$ are antisymmetric. The epsilon trace and $`\Sigma_b{}^b`$ trace are zero for the same stated index reason. The remaining terms, before simplification, are

```math
\begin{aligned}
R(K)_{b\alpha}^{+,b}={}&\tfrac14(\Gamma^b)_\alpha{}^\beta\nabla^dW_{db\beta}^+
+\tfrac18(\Gamma^b)_\alpha{}^\beta\nabla_bX_\beta^+
+\tfrac1{64}W^{de}(3\Gamma_b\Sigma_{de}\Gamma^b-\Sigma_{de}\Gamma_b\Gamma^b)_\alpha{}^\beta X_\beta^+\\
&+\big(\tfrac58-\tfrac{13}{48}-\tfrac{11}{48}\big)W^{de}W_{de\alpha}^+
-\big(\tfrac1{48}+\tfrac{13}{96}\big)\widetilde W_{bde}(\Gamma^b)_\alpha{}^\beta W^{de}{}_{\beta}^+.
\end{aligned}
\tag{S2-138}
```

Here the $`5/8`$ is the trace of $`\delta_b{}^c/8`$ in five dimensions; the $`13/48`$ and $`11/48`$ terms acquire minus signs from $`W^{db}=-W^{bd}`$. The two dual terms add because moving $`b`$ through the two indices $`d,e`$ has even permutation parity. The identities needed for the remaining reduction are

```math
\begin{gathered}
\Gamma_b\Gamma^b=-5\mathbf1,\qquad \Gamma_b\Sigma_{de}\Gamma^b=-\Sigma_{de},\qquad
(\Gamma^b)_\alpha{}^\beta W_{db\beta}^+=0,\\
\widetilde W_{bde}(\Gamma^b)_\alpha{}^\beta W^{de}{}_{\beta}^+=W^{de}W_{de\alpha}^+,
\qquad T^a\Gamma_a=\tfrac12W_\alpha{}^\beta.
\end{gathered}
\tag{S2-139}
```

The last equality is a matrix equality with the free spinor indices on the right understood: expand $`T^a\Gamma_a=(3\Gamma^aW\Gamma_a-W\Gamma^a\Gamma_a)/4`$, use $`\Gamma^aW\Gamma_a=-W`$, and obtain $`(-3+5)W/4=W/2`$. In the gamma-trace identity substitute $`W_{db\beta}=(\Sigma_{db})^{\rho\sigma}W_{\rho\sigma\beta}`$; the gamma product reduces by (S2-85) and its totally symmetric three-spinor part vanishes. The dual identity follows by inserting $`\widetilde W_{bde}=\varepsilon_{bdefg}W^{fg}/2`$ and applying that same gamma-trace identity to $`\Gamma^b\Sigma^{de}`$. It has coefficient one with Gold's orientation; no component-frame epsilon is substituted.

Consequently the third term of (S2-138) is $`W^{de}(\Sigma_{de})_\alpha{}^\beta X_\beta^+/32`$. Its two three-spinor coefficients combine as $`1/8-5/32=-1/32`$. We obtain

```math
\begin{aligned}
R(K)_{b\alpha}^{+,b}&=\tfrac18(\Gamma^a)_\alpha{}^\beta\nabla_aX_\beta^+
+\tfrac1{32}W^{ab}(\Sigma_{ab})_\alpha{}^\beta X_\beta^+-\tfrac1{32}W^{ab}W_{ab\alpha}^+,\\
(D_\alpha\Box W)_1&=(-\tfrac14+\tfrac14)(\Gamma^a)_\alpha{}^\beta\nabla_aX_\beta^+
+(-\tfrac1{16}+\tfrac1{16})W^{ab}(\Sigma_{ab})_\alpha{}^\beta X_\beta^+
-\tfrac1{16}W^{ab}W_{ab\alpha}^+\\
&=-\tfrac1{16}W^{ab}W_{ab\alpha}^+.
\end{aligned}
\tag{S2-140}
```

This is a local superfield identity. Its weight is $`5/2`$ after removing the explicit scalar $`W`$: the right side has $`1+3/2=5/2`$.

Differentiate (S2-107) and retain explicit scalar degree one. The other ingredients are obtained directly from S23 (2.13b), (2.6a,f):

```math
\begin{aligned}
(D_\alpha(W_{ab}F^{ab}))_1&=-W^{ab}W_{ab\alpha}^+,\\
(D_\alpha(X^{\rho+}\lambda_\rho^-))_1&=2X^{\rho+}W_{\alpha\rho}=-2W_\alpha{}^\rho X_\rho^+,\\
D_\alpha(W^{ab}W_{ab})&=2W^{ab}W_{ab\alpha}^++4W_\alpha{}^\beta X_\beta^+,\\
D_\alpha Y&=8(\Gamma^a)_\alpha{}^\beta\nabla_aX_\beta^++8W_\alpha{}^\beta X_\beta^+.
\end{aligned}
\tag{S2-141}
```

For the first line only $`D_\alpha F_{\beta\gamma}\supset-W_{\alpha\beta\gamma}^+W`$ supplies a scalar $`W`$. For the second line the minus sign in $`D(X\lambda)=(DX)\lambda-XD\lambda`$ cancels the minus sign in $`D\lambda\supset-2W_{\alpha\rho}W`$. Its displayed index-raising step uses $`W_\alpha{}^\rho=-W_{\alpha\sigma}\varepsilon^{\sigma\rho}`$. The third line follows from $`W^{ab}W_{ab}=2W^{\beta\gamma}W_{\beta\gamma}`$ and (2.6a), including the two equal even-factor placements.

The five differentiated terms of (S2-107) therefore give

```math
\begin{aligned}
(D_\alpha D^{++}X^{--})_1={}&
\big(\tfrac i2-8i+\tfrac{31i}{2}\big)W^{ab}W_{ab\alpha}^+
+(-10i-6i+31i)W_\alpha{}^\beta X_\beta^+
-6i(\Gamma^a)_\alpha{}^\beta\nabla_aX_\beta^+\\
={}&8iW^{ab}W_{ab\alpha}^++15iW_\alpha{}^\beta X_\beta^+
-6i(\Gamma^a)_\alpha{}^\beta\nabla_aX_\beta^+.
\end{aligned}
\tag{S2-142}
```

### 4.26 Deriving $`(\Delta X^{--})_0`$: product rule and Weyl-spinor derivatives

We compute this descendant from (S2-107), rather than solving for it from the published primary. Acting with $`-D^{++}/32`$ gives exactly five contributions:

```math
\begin{aligned}
(\Delta X^{--})_0={}&\tfrac i4(D^{++}\Box W)_0-\tfrac i4(D^{++}(W_{ab}F^{ab}))_0
-\tfrac{5i}{32}(D^{++}(X^{\alpha+}\lambda_\alpha^-))_0
+\tfrac{9i}{32}(D^{++}(X^{\alpha-}\lambda_\alpha^+))_0\\
&-\tfrac1{32}\big[D^{++}\{W(-\tfrac{3i}{4}Y+\tfrac{31i}{4}W^{ab}W_{ab})\}\big]_0.
\end{aligned}
\tag{S2-143}
```

The second-derivative product rules, with $`D^{++}=-\varepsilon^{\alpha\beta}D_\alpha D_\beta`$, are

```math
\begin{aligned}
D^{++}(AB)&=(D^{++}A)B+A(D^{++}B)-2\varepsilon^{\alpha\beta}(D_\alpha A)(D_\beta B),&& |A|=|B|=0,\\
D^{++}(\xi\zeta)&=(D^{++}\xi)\zeta+\xi(D^{++}\zeta)+2\varepsilon^{\alpha\beta}(D_\alpha\xi)(D_\beta\zeta),&& |\xi|=|\zeta|=1.
\end{aligned}
\tag{S2-144}
```

For the first equality the two single-derivative factors are odd and their order is fixed; the antisymmetric spinor metric makes the two cross placements equal. For the second, differentiate $`D_\beta(\xi\zeta)=(D_\beta\xi)\zeta-\xi D_\beta\zeta`$ once more. The cross terms have the opposite sign, since $`D_\beta\xi`$ is even. This explains the relative sign between the two lines.

The needed Weyl-spinor trace follows from S23 (2.6b). Differentiating each of its six terms gives the following explicit equation before contraction:

```math
\begin{aligned}
D_\alpha D_\beta X_\rho^-={}&D_\alpha X_{\beta\rho}^{+-}+\tfrac i8\varepsilon_{\beta\rho}D_\alpha Y
-\tfrac{3i}{2}(\Gamma^a)_\beta{}^\tau D_\alpha\nabla_aW_{\rho\tau}
-\tfrac i2(\Gamma^a)_\rho{}^\tau D_\alpha\nabla_aW_{\beta\tau}\\
&-2i(D_\alpha W_\beta{}^\tau)W_{\rho\tau}-2iW_\beta{}^\tau D_\alpha W_{\rho\tau}
+\tfrac i4\varepsilon_{\beta\rho}D_\alpha(W^{ab}W_{ab}).
\end{aligned}
\tag{S2-145}
```

The source substitutions here are (S2-141), (S2-103), and

```math
\begin{aligned}
D_\alpha\nabla_aW_{\rho\tau}={}&\nabla_a\big(W_{\alpha\rho\tau}^++\varepsilon_{\alpha(\rho}X_{\tau)}^+\big)
+T_{a\alpha}{}^\gamma\big(W_{\gamma\rho\tau}^++\varepsilon_{\gamma(\rho}X_{\tau)}^+\big)\\
&+\tfrac12R(M)_{a\alpha}^{+,bc}\big[(\Sigma_{bc})_\rho{}^\gamma W_{\gamma\tau}+(\Sigma_{bc})_\tau{}^\gamma W_{\rho\gamma}\big]
-\tfrac14(\Gamma_a)_\alpha{}^\gamma X_\gamma^+W_{\rho\tau}.
\end{aligned}
\tag{S2-146}
```

The S and K actions on $`W_{\rho\tau}`$ vanish because it is primary; the last term is its weight-one dilatation action. To remove ambiguity in the symmetrizations of S23 (2.6e), its required $`+,+-`$ component is

```math
\begin{aligned}
D_\alpha X_{\beta\gamma}^{+-}=\tfrac i2\Big[&
-\tfrac32(W_\beta{}^\rho W_{\gamma\alpha\rho}^++W_\gamma{}^\rho W_{\beta\alpha\rho}^+)
-\tfrac12(\varepsilon_{\alpha\beta}W^{\rho\tau}W_{\gamma\rho\tau}^++\varepsilon_{\alpha\gamma}W^{\rho\tau}W_{\beta\rho\tau}^+)
-W_{\alpha\rho}W_{\beta\gamma}{}^{\rho+}\\
&-\tfrac32W_{\beta\gamma}X_\alpha^++\tfrac14(W_{\alpha\beta}X_\gamma^++W_{\alpha\gamma}X_\beta^+)
+\tfrac34(\varepsilon_{\alpha\beta}W_{\gamma\rho}+\varepsilon_{\alpha\gamma}W_{\beta\rho})X^{\rho+}\\
&+2(\Gamma^a)_\alpha{}^\rho\nabla_aW_{\beta\gamma\rho}^+
+(\Gamma^a)_\beta{}^\rho\nabla_aW_{\gamma\alpha\rho}^++(\Gamma^a)_\gamma{}^\rho\nabla_aW_{\beta\alpha\rho}^+\\
&-\tfrac12(\Gamma^a)_{\alpha\beta}\nabla_aX_\gamma^+-\tfrac12(\Gamma^a)_{\alpha\gamma}\nabla_aX_\beta^+
+\tfrac12\varepsilon_{\alpha\beta}(\Gamma^a)_{\gamma\rho}\nabla_aX^{\rho+}
+\tfrac12\varepsilon_{\alpha\gamma}(\Gamma^a)_{\beta\rho}\nabla_aX^{\rho+}\Big].
\end{aligned}
\tag{S2-147}
```

The overall $`1/2`$ comes from $`\varepsilon^{+(+}A^{-)}=A^+/2`$. The further halves inside the brackets symmetrize the two spinor indices and must be retained separately. For example, contracting the four $`\nabla X`$ terms on the last line with $`-\varepsilon^{\alpha\beta}`$ gives coefficients $`0,+i/4,-i,-i/4`$, whose sum is $`-i`$, multiplying $`(\Gamma^a)_\rho{}^\tau\nabla_aX_\tau^+`$. In (S2-145) the $`Y`$ term contributes another $`-i`$, and the two $`\nabla W`$ terms contribute $`-3i/4`$ and $`-5i/4`$. Their sum is $`-4i`$. The algebraic terms reduce with (S2-68), (S2-85), and (S2-139); the three-spinor contractions cancel, leaving the same coefficient for $`W_\rho{}^\tau X_\tau^+`$. The table below displays the remaining algebraic coefficients.

The algebraic part of the trace can be followed without leaving an implicit cancellation. Here are all seven terms of (S2-145), after multiplication by $`-\varepsilon^{\alpha\beta}`$. The derivative column also records the four contributions just discussed. Indices $`\rho`$ are free in every column.

| Differentiated term in (S2-145) | $`i(\Gamma^a)_\rho{}^\tau\nabla_aX_\tau^+`$ | $`iW_\rho{}^\tau X_\tau^+`$ | $`iW^{ab}W_{ab\rho}^+`$ |
|---|---:|---:|---:|
| $`D_\alpha X_{\beta\rho}^{+-}`$ | $`-1`$ | $`-1`$ | $`0`$ |
| $`i\varepsilon_{\beta\rho}D_\alpha Y/8`$ | $`-1`$ | $`-1`$ | $`0`$ |
| $`-3i(\Gamma^a)_\beta{}^\tau D_\alpha\nabla_aW_{\rho\tau}/2`$ | $`-3/4`$ | $`-21/4`$ | $`-3/4`$ |
| $`-i(\Gamma^a)_\rho{}^\tau D_\alpha\nabla_aW_{\beta\tau}/2`$ | $`-5/4`$ | $`1/4`$ | $`1/4`$ |
| $`-2i(D_\alpha W_\beta{}^\tau)W_{\rho\tau}`$ | $`0`$ | $`5`$ | $`0`$ |
| $`-2iW_\beta{}^\tau D_\alpha W_{\rho\tau}`$ | $`0`$ | $`-1`$ | $`1`$ |
| $`i\varepsilon_{\beta\rho}D_\alpha(W^{ab}W_{ab})/4`$ | $`0`$ | $`-1`$ | $`-1/2`$ |
| Sum | $`-4`$ | $`-4`$ | $`0`$ |

For example the last row of contributions inserts $`2W^{ab}W_{ab\alpha}^++4W_\alpha{}^\tau X_\tau^+`$, then uses $`\varepsilon^{\alpha\beta}\varepsilon_{\beta\rho}=\delta^\alpha_\rho`$. It gives precisely $`-iW^{ab}W_{ab\rho}^+/2-iW_\rho{}^\tau X_\tau^+`$. The total three-spinor coefficient is $`-3/4+1/4+1-1/2=0`$; the matrix–Weyl-spinor coefficient is $`-1-1-21/4+1/4+5-1-1=-4`$.

Thus the complete trace and the related all-plus traces are

```math
D^{++}X_\rho^-=-4i(\Gamma^a)_\rho{}^\tau\nabla_aX_\tau^+-4iW_\rho{}^\tau X_\tau^+
=-\tfrac i2D_\rho Y,\qquad D^{++}X_\rho^+=0,\qquad D^{++}\lambda_\rho^+=0.
\tag{S2-148}
```

For the first vanishing trace, $`D_\alpha X_\rho^+=X_{\alpha\rho}^{++}`$ and $`D_\beta X_{\alpha\rho}^{++}=0`$ by (2.6e); for the second vanishing trace, $`D_\alpha\lambda_\rho^+=-\varepsilon_{\alpha\rho}X^{++}`$ and $`D_\beta X^{++}=0`$. These are exact derivative identities, not auxiliary equations.

Insert (S2-148), (S2-72), and $`D_\alpha\lambda_\beta^-|_0=-2F_{\alpha\beta}-\varepsilon_{\alpha\beta}X^{+-}-\nabla_{\alpha\beta}W`$ into the odd product rule. Both Weyl-spinor products in (S2-143) are then fully reduced:

```math
\begin{aligned}
(D^{++}(X^{\alpha+}\lambda_\alpha^-))_0={}&
X^{\alpha+}(4i\nabla_\alpha{}^\beta\lambda_\beta^+-10iW_{\alpha\beta}\lambda^{\beta+})
+2\varepsilon^{\rho\sigma}\varepsilon^{\alpha\beta}X_{\rho\beta}^{++}(-2F_{\sigma\alpha}-\varepsilon_{\sigma\alpha}X^{+-}-\nabla_{\sigma\alpha}W)\\
={}&-4i(\Gamma^a)^{\alpha\beta}X_\alpha^+\nabla_a\lambda_\beta^+
-5i(\Sigma_{ab})^{\alpha\beta}W^{ab}X_\alpha^+\lambda_\beta^++2F_{ab}X^{ab++},\\
(D^{++}(X^{\alpha-}\lambda_\alpha^+))_0={}&
\varepsilon^{\alpha\rho}[-4i(\Gamma^a)_\rho{}^\beta\nabla_aX_\beta^+-4iW_\rho{}^\beta X_\beta^+]\lambda_\alpha^+
-2X^{++}\varepsilon^{\rho\sigma}\varepsilon^{\alpha\beta}(D_\rho X_\beta^-)\varepsilon_{\sigma\alpha}\\
={}&4i(\Gamma^a)^{\alpha\beta}\lambda_\alpha^+\nabla_aX_\beta^+
-2i(\Sigma_{ab})^{\alpha\beta}W^{ab}X_\alpha^+\lambda_\beta^++iYX^{++}.
\end{aligned}
\tag{S2-149}
```

The symmetric spinor $`X_{\rho\beta}^{++}`$ annihilates the auxiliary and gradient contractions in the first cross term. Its field-strength contraction is $`2F_{ab}X^{ab++}`$, using $`F_{\alpha\beta}=\Sigma^{ab}_{\alpha\beta}F_{ab}/2`$ and the same relation for $`X_{\alpha\beta}^{++}`$. In the second cross term only the $`i\varepsilon_{\rho\beta}Y/8`$ part of (S2-103) contributes to the spinor trace; the Weyl-square trace cancels inside that equation. The sign of $`\lambda\nabla X`$ changes when the two odd fields are reordered; both that sign and the antisymmetric spinor raising metric have been included.

For the last product in (S2-143), use $`D^{++}W=-4iX^{++}`$ and (S2-141). Its term with an undifferentiated scalar $`W`$ has explicit degree one and is outside this coefficient. The other two terms give

```math
\begin{aligned}
&\big[D^{++}\{W(-\tfrac{3i}{4}Y+\tfrac{31i}{4}W^{ab}W_{ab})\}\big]_0\\
&=(-4iX^{++})(-\tfrac{3i}{4}Y+\tfrac{31i}{4}W^{ab}W_{ab})
-2i\varepsilon^{\alpha\beta}\lambda_\alpha^+
\big[-6i(\Gamma^a)_\beta{}^\rho\nabla_aX_\rho^++25iW_\beta{}^\rho X_\rho^++\tfrac{31i}{2}W^{ab}W_{ab\beta}^+\big]\\
&=-3YX^{++}+31W^{ab}W_{ab}X^{++}
-12(\Gamma^a)^{\alpha\beta}\lambda_\alpha^+\nabla_aX_\beta^+
-25(\Sigma_{ab})^{\alpha\beta}W^{ab}X_\alpha^+\lambda_\beta^+
-31W^{ab}W_{ab}^{\alpha+}\lambda_\alpha^+.
\end{aligned}
\tag{S2-150}
```

### 4.27 The second derivative of $`W_{ab}F^{ab}`$

The two-form conversion is $`W_{ab}F^{ab}=2W^{\rho\sigma}F_{\rho\sigma}`$. The even product rule gives three, and only three, contributions:

```math
\begin{aligned}
(D^{++}(W_{ab}F^{ab}))_0={}&2(D^{++}W^{\rho\sigma})F_{\rho\sigma}
+2W^{\rho\sigma}(D^{++}F_{\rho\sigma})_0
-4\varepsilon^{\alpha\beta}(D_\alpha W^{\rho\sigma})(D_\beta F_{\rho\sigma})_0.
\end{aligned}
\tag{S2-151}
```

For the first contribution, S23 (2.6a,c) gives

```math
\begin{aligned}
D_\alpha D_\beta W_{\rho\sigma}
&=-\tfrac12\big(\varepsilon_{\alpha\rho}X_{\sigma\beta}^{++}+\varepsilon_{\alpha\sigma}X_{\rho\beta}^{++}+\varepsilon_{\alpha\beta}X_{\rho\sigma}^{++}\big)
+\tfrac12\big(\varepsilon_{\beta\rho}X_{\alpha\sigma}^{++}+\varepsilon_{\beta\sigma}X_{\alpha\rho}^{++}\big),\\
D^{++}W_{\rho\sigma}&=-4X_{\rho\sigma}^{++},\qquad
2(D^{++}W^{\rho\sigma})F_{\rho\sigma}=-8X^{\rho\sigma++}F_{\rho\sigma}=-4F_{ab}X^{ab++}.
\end{aligned}
\tag{S2-152}
```

The three terms in the first parentheses come from $`D_\alpha W_{\beta\rho\sigma}^+`$; the other two differentiate $`\varepsilon_{\beta(\rho}X_{\sigma)}^+`$. All five must be traced before imposing the two-form conversion.

For the second contribution, differentiating S23 (2.13b) explicitly gives

```math
\begin{aligned}
(D_\alpha D_\beta F_{\rho\sigma})_0={}&
-\tfrac i2\Big[(\Gamma^a)_{\beta\rho}(D_\alpha\nabla_a\lambda_\sigma^+)_0
+(\Gamma^a)_{\beta\sigma}(D_\alpha\nabla_a\lambda_\rho^+)_0
+\varepsilon_{\beta\rho}(\Gamma^a)_\sigma{}^\tau(D_\alpha\nabla_a\lambda_\tau^+)_0
+\varepsilon_{\beta\sigma}(\Gamma^a)_\rho{}^\tau(D_\alpha\nabla_a\lambda_\tau^+)_0\Big]\\
&-\tfrac{3i}{2}\big[(D_\alpha W_{\rho\sigma})\lambda_\beta^+-W_{\rho\sigma}\varepsilon_{\alpha\beta}X^{++}\big]
+\tfrac i4\big[(D_\alpha W_{\beta\rho})\lambda_\sigma^+-W_{\beta\rho}\varepsilon_{\alpha\sigma}X^{++}\big]
+\tfrac i4\big[(D_\alpha W_{\beta\sigma})\lambda_\rho^+-W_{\beta\sigma}\varepsilon_{\alpha\rho}X^{++}\big]\\
&-\tfrac{3i}{4}\varepsilon_{\beta\rho}\big[(D_\alpha W_\sigma{}^\tau)\lambda_\tau^+-W_\sigma{}^\tau\varepsilon_{\alpha\tau}X^{++}\big]
-\tfrac{3i}{4}\varepsilon_{\beta\sigma}\big[(D_\alpha W_\rho{}^\tau)\lambda_\tau^+-W_\rho{}^\tau\varepsilon_{\alpha\tau}X^{++}\big]
+iW_{\beta\rho\sigma}^+\lambda_\alpha^+.
\end{aligned}
\tag{S2-153}
```

The last term is essential: differentiating $`-W_{\beta\rho\sigma}^+W`$ gives $`-(D_\alpha W_{\beta\rho\sigma}^+)W+W_{\beta\rho\sigma}^+D_\alpha W`$. The second product is $`+iW_{\beta\rho\sigma}^+\lambda_\alpha^+`$ and has explicit scalar degree zero. The first product has degree one. This is a Grassmann-product sign, not a convention choice.

For the four differentiated vector derivatives in the first line, the needed degree-zero rule is

```math
(D_\alpha\nabla_a\lambda_\rho^+)_0
=-\varepsilon_{\alpha\rho}\nabla_aX^{++}
-T_{a\alpha}{}^\tau\varepsilon_{\tau\rho}X^{++}
+\tfrac12R(M)_{a\alpha}^{+,bc}(\Sigma_{bc})_\rho{}^\tau\lambda_\tau^+.
\tag{S2-154}
```

It follows from $`\nabla_a(D_\alpha\lambda_\rho^+)+[D_\alpha,\nabla_a]\lambda_\rho^+`$. The dilatation and SU(2) actions cancel on $`\lambda^+`$ in this particular plus projection. The S action is proportional to scalar $`W`$ and is outside (S2-154). K annihilates this first spinor descendant. The Lorentz curvature is (S2-67); its three-spinor and Weyl-spinor parts are both retained.

Inserting (S2-153)–(S2-154), $`D_\alpha W_{\rho\sigma}=W_{\alpha\rho\sigma}^++\varepsilon_{\alpha(\rho}X_{\sigma)}^+`$, and the first derivative of $`F`$ in (S2-06) into (S2-151), the individual contractions are:

| Contribution in (S2-151) | $`F_{ab}X^{ab++}`$ | $`iW^{ab}W_{ab}X^{++}`$ | $`iW^{ab}W_{ab}^{\alpha+}\lambda_\alpha^+`$ | $`i(\Sigma_{ab})^{\alpha\beta}W^{ab}X_\alpha^+\lambda_\beta^+`$ | $`i(\Gamma^a)^{\alpha\beta}X_\alpha^+\nabla_a\lambda_\beta^+`$ |
|---|---:|---:|---:|---:|---:|
| $`2(D^{++}W^{\rho\sigma})F_{\rho\sigma}`$ | $`-4`$ | $`0`$ | $`0`$ | $`0`$ | $`0`$ |
| $`2W^{\rho\sigma}(D^{++}F_{\rho\sigma})_0`$ | $`0`$ | $`8`$ | $`-6`$ | $`-2`$ | $`0`$ |
| $`-4\varepsilon^{\alpha\beta}(D_\alpha W^{\rho\sigma})(D_\beta F_{\rho\sigma})_0`$ | $`0`$ | $`0`$ | $`-2`$ | $`4`$ | $`8`$ |
| Sum | $`-4`$ | $`8`$ | $`-8`$ | $`2`$ | $`8`$ |

Here each entry includes the coefficient in the first column. The contractions use (S2-68), (S2-85), and the $`\Sigma`$ normalization in (S2-05); there is no derivative interchange. The possible $`W\nabla X^{++}`$ contribution from (S2-154) is zero since $`W^{\rho\sigma}(\Gamma^a)_{\rho\sigma}=0`$. Gamma traces of $`W_{\alpha\rho\sigma}^+`$ vanish by (S2-139). Thus the five-column sum is the complete answer:

```math
\begin{aligned}
(D^{++}(W_{ab}F^{ab}))_0={}&-4F_{ab}X^{ab++}+8iW^{ab}W_{ab}X^{++}
-8iW^{ab}W_{ab}^{\alpha+}\lambda_\alpha^+
+2i(\Sigma_{ab})^{\alpha\beta}W^{ab}X_\alpha^+\lambda_\beta^+
+8i(\Gamma^a)^{\alpha\beta}X_\alpha^+\nabla_a\lambda_\beta^+.
\end{aligned}
\tag{S2-155}
```

### 4.28 The second derivative of $`\Box W`$: retaining S and K actions

The uncontracted $`(D_\beta\Box W)_0`$ must be differentiated, not its contraction with a leading gaugino in (S2-112). That contraction would lose the symmetric Weyl descendant. Expand the three connection terms in (S2-110) before multiplying by a gaugino. The required matrix identities are

```math
\begin{aligned}
i(\nabla^aT_a)_\beta{}^\rho
&=-\tfrac i2(\Gamma^a)_\beta{}^\rho\nabla^cW_{ac}
-\tfrac{i}{8}\varepsilon^{abcde}(\Sigma_{ab})_\beta{}^\rho\nabla_cW_{de},\\
i(T^aT_a)_\beta{}^\rho
&=-\tfrac{5i}{32}W^{ab}W_{ab}\delta_\beta{}^\rho
+\tfrac i{64}\varepsilon^{abcde}(\Gamma_a)_\beta{}^\rho W_{bc}W_{de},\\
-R(S)^a{}_\beta{}^{+,\gamma k}(\Gamma_a)_\gamma{}^\rho\lambda_{\rho k}
&=-\tfrac38X_{\beta\rho}^{+-}\lambda^{\rho+}+\tfrac38X_{\beta\rho}^{++}\lambda^{\rho-}
+\tfrac i{64}W^{ab}W_{ab}\lambda_\beta^+
-\tfrac i{64}\varepsilon^{abcde}(\Gamma_a)_\beta{}^\rho W_{bc}W_{de}\lambda_\rho^+\\
&\quad-\tfrac i{16}(\Gamma^a)_\beta{}^\rho(\nabla^cW_{ac})\lambda_\rho^+
-\tfrac{i}{16}\varepsilon^{abcde}(\Sigma_{ab})_\beta{}^\rho(\nabla_cW_{de})\lambda_\rho^+.
\end{aligned}
\tag{S2-156}
```

In the first line insert $`T_a=(3\Gamma_aW-W\Gamma_a)/4`$, then $`W_\alpha{}^\beta=W^{ab}(\Sigma_{ab})_\alpha{}^\beta/2`$, and apply the two ordered $`\Gamma\Sigma`$ products in (S2-85). Their divergence coefficients add to $`-1/2`$, and their three-gamma dual coefficients to $`-1/8`$. In the second line multiply out the four ordered products in $`16T^aT_a=9\Gamma^aW\Gamma_aW-3\Gamma^aWW\Gamma_a-3W\Gamma^a\Gamma_aW+W\Gamma^aW\Gamma_a`$. The scalar and four-gamma parts reduce by (S2-53), giving $`-5/32`$ and $`+1/64`$. In the last equality substitute all terms of C24 (A.3e), also displayed in (S2-104). The $`X^{ij}_{ab}`$ part has coefficient $`3/8`$ after $`\Gamma\Sigma\Gamma=-\Sigma`$; SU(2) lowering makes its $`+-`$ and $`++`$ contributions opposite. The two derivative two-form structures remain separate. Adding these three equalities cancels the two epsilon–$`W^2`$ terms and gives

```math
\begin{aligned}
(D_\beta\Box W)_0={}&i\Box\lambda_\beta^++2iT^a{}_\beta{}^\rho\nabla_a\lambda_\rho^+
-\tfrac38X_{\beta\rho}^{+-}\lambda^{\rho+}+\tfrac38X_{\beta\rho}^{++}\lambda^{\rho-}
-\tfrac{9i}{64}W^{ab}W_{ab}\lambda_\beta^+\\
&-\tfrac{9i}{16}(\Gamma^a)_\beta{}^\rho(\nabla^cW_{ac})\lambda_\rho^+
-\tfrac{3i}{16}\varepsilon^{abcde}(\Sigma_{ab})_\beta{}^\rho(\nabla_cW_{de})\lambda_\rho^+
+\tfrac14(\Gamma^a)_\beta{}^\rho X_\rho^+\nabla_aW.
\end{aligned}
\tag{S2-157}
```

Every term has weight $`7/2`$. This is the full coefficient, including the symmetric $`X_{\beta\rho}^{+-}`$ term which vanished in (S2-111). Also, the derivative index in the epsilon term is lower: it is $`\nabla_cW_{de}`$, not $`\nabla^cW_{de}`$.

The first term in (S2-157) requires the commutator on a spinor and then on a vector-spinor:

```math
\begin{aligned}
D_\alpha\Box\lambda_\beta^+
&=\Box(D_\alpha\lambda_\beta^+)
+\nabla^a([D_\alpha,\nabla_a]\lambda_\beta^+)
+[D_\alpha,\nabla^a]\nabla_a\lambda_\beta^+,\\
([D_\alpha,\nabla_a]\lambda_\beta^+)_0
&=-T_{a\alpha}{}^\tau\varepsilon_{\tau\beta}X^{++}
+\tfrac12R(M)_{a\alpha}^{+,bc}(\Sigma_{bc})_\beta{}^\tau\lambda_\tau^+,\\
([D_\alpha,\nabla_a]\lambda_\beta^+)_1
&=-2iR(S)_{a\alpha}^{+,\gamma+}\varepsilon_{\gamma\beta}.
\end{aligned}
\tag{S2-158}
```

The first line is an exact ordered identity, not $`D_\alpha\Box=\Box D_\alpha`$. The degree-one term in the last line contributes at degree zero after $`\nabla^a`$ acts on the scalar $`W`$. It produces $`-2iR(S)_{a\alpha}^{+,\gamma+}\varepsilon_{\gamma\beta}\nabla^aW`$. Dropping it would spoil the gradient cancellation.

On the vector-spinor in the last commutator, the generator actions from C24 (A.1) and S23 (2.15) are

```math
\begin{aligned}
\mathbb D\nabla_a\lambda_\beta^+&=\tfrac52\nabla_a\lambda_\beta^+,\qquad
K_c\nabla_a\lambda_\beta^+=3\eta_{ca}\lambda_\beta^++2(\Sigma_{ca})_\beta{}^\tau\lambda_\tau^+,\\
(S_{\gamma k}\nabla_a\lambda_\beta^+)_0
&=i(\Gamma_a)_\gamma{}^\tau(\nabla_{\tau k}\lambda_\beta^+)_0-2i\delta_k^+\varepsilon_{\gamma\beta}\nabla_aW,\\
(\nabla_{\tau+}\lambda_\beta^+)_0
&=-2F_{\tau\beta}+\varepsilon_{\tau\beta}X^{+-}-\nabla_{\tau\beta}W,
\qquad(\nabla_{\tau-}\lambda_\beta^+)_0=-\varepsilon_{\tau\beta}X^{++}.
\end{aligned}
\tag{S2-159}
```

For K, insert $`[K_c,\nabla_a]=2\eta_{ca}\mathbb D+2M_{ca}`$ and $`M_{ca}\lambda_\beta=(\Sigma_{ca})_\beta{}^\tau\lambda_\tau`$; the primary spinor has weight $`3/2`$. For S, commute it past $`\nabla_a`$ and differentiate $`S_{\gamma k}\lambda_\beta^+=-2i\delta_k^+\varepsilon_{\gamma\beta}W`$. For the lowered SU(2) derivatives use $`\nabla_{\tau+}=-\nabla_\tau^-`$ and $`\nabla_{\tau-}=\nabla_\tau^+`$, followed by (S2-06).

Inserting these actions into (S2-158), the complete untraced expression is

```math
\begin{aligned}
(D_\alpha\Box\lambda_\beta^+)_0={}&-\varepsilon_{\alpha\beta}\Box X^{++}
-(\nabla^aT_a)_\alpha{}^\tau\varepsilon_{\tau\beta}X^{++}
-2T^a{}_\alpha{}^\tau\varepsilon_{\tau\beta}\nabla_aX^{++}
-T^a{}_\alpha{}^\tau T_{a\tau}{}^\rho\varepsilon_{\rho\beta}X^{++}\\
&+\tfrac12T^a{}_\alpha{}^\tau R(M)_{a\tau}^{+,cd}(\Sigma_{cd})_\beta{}^\rho\lambda_\rho^+
+\tfrac12(\nabla^aR(M)_{a\alpha}^{+,cd})(\Sigma_{cd})_\beta{}^\rho\lambda_\rho^+
+R(M)_{a\alpha}^{+,cd}(\Sigma_{cd})_\beta{}^\rho\nabla^a\lambda_\rho^+\\
&+\tfrac34(\Gamma^a)_\alpha{}^\tau X_\tau^+\nabla_a\lambda_\beta^+
-2iR(S)_{a\alpha}^{+,\gamma+}\varepsilon_{\gamma\beta}\nabla^aW\\
&+iR(S)^{a}{}_{\alpha}{}^{+,\gamma+}(\Gamma_a)_\gamma{}^\tau
(-2F_{\tau\beta}+\varepsilon_{\tau\beta}X^{+-}-\nabla_{\tau\beta}W)
-2iR(S)^{a}{}_{\alpha}{}^{+,\gamma+}\varepsilon_{\gamma\beta}\nabla_aW\\
&-iR(S)^{a}{}_{\alpha}{}^{+,\gamma-}(\Gamma_a)_\gamma{}^\tau\varepsilon_{\tau\beta}X^{++}
+R(K)^{a}{}_{\alpha}{}^{+,c}\big[3\eta_{ca}\lambda_\beta^++2(\Sigma_{ca})_\beta{}^\tau\lambda_\tau^+\big].
\end{aligned}
\tag{S2-160}
```

The two displayed $`R(S)\nabla W`$ terms have different origins: one is the differentiated degree-one commutator, and the other is the second term in the S action in (S2-159). The coefficient $`3/4`$ on the third line is the vector Lorentz trace $`+1`$ plus the additional dilatation weight contribution $`-1/4`$. The scalar/spinor Lorentz curvature and the full K curvature remain visible, so none is silently replaced by a scalar commutator.

For the other seven terms in (S2-157), the ordinary graded product rule is sufficient once the single-derivative rules are inserted. For example, the last term gives

```math
\begin{aligned}
D_\alpha\big[\tfrac14(\Gamma^a)_\beta{}^\rho X_\rho^+\nabla_aW\big]_0
={}&\tfrac14(\Gamma^a)_\beta{}^\rho X_{\alpha\rho}^{++}\nabla_aW
-\tfrac i4(\Gamma^a)_\beta{}^\rho X_\rho^+\big(\nabla_a\lambda_\alpha^++T_{a\alpha}{}^\tau\lambda_\tau^+\big),\\
D_\alpha\big[-\tfrac38X_{\beta\rho}^{+-}\lambda^{\rho+}\big]_0
={}&-\tfrac38(D_\alpha X_{\beta\rho}^{+-})\lambda^{\rho+}
+\tfrac38X_{\beta\rho}^{+-}\varepsilon^{\rho\tau}\varepsilon_{\alpha\tau}X^{++},\\
D_\alpha\big[\tfrac38X_{\beta\rho}^{++}\lambda^{\rho-}\big]_0
={}&\tfrac38X_{\beta\rho}^{++}\varepsilon^{\rho\tau}
(-2F_{\alpha\tau}-\varepsilon_{\alpha\tau}X^{+-}-\nabla_{\alpha\tau}W),\\
D_\alpha(2iT^a{}_\beta{}^\rho\nabla_a\lambda_\rho^+)_0
={}&2i(D_\alpha T^a{}_\beta{}^\rho)\nabla_a\lambda_\rho^+
+2iT^a{}_\beta{}^\rho(D_\alpha\nabla_a\lambda_\rho^+)_0,\\
D_\alpha T_a&=\tfrac14[3\Gamma_a(D_\alpha W)-(D_\alpha W)\Gamma_a].
\end{aligned}
\tag{S2-161}
```

Only in the last line, as in the existing definition of $`T_a`$, $`W`$ without spinor indices denotes the **matrix** $`W_\rho{}^\sigma`$, not the scalar superfield. The derivative is $`(D_\alpha W)_\rho{}^\sigma=-(W_{\alpha\rho\tau}^++\varepsilon_{\alpha(\rho}X_{\tau)}^+)\varepsilon^{\tau\sigma}`$. In the first line, the minus sign is the odd $`X_\rho^+`$ sign. In the third line $`D_\alpha X_{\beta\rho}^{++}=0`$. For the three remaining even coefficient matrices multiplying $`\lambda_\beta^+`$ or $`\lambda_\rho^+`$ in (S2-157), differentiate $`W^{ab}W_{ab}`$ with (S2-141) and $`\nabla_aW_{bc}`$ with (S2-146), then add the coefficient times $`D_\alpha\lambda_\rho^+=-\varepsilon_{\alpha\rho}X^{++}`$. Explicitly,

```math
\begin{aligned}
D_\alpha(W^{ab}W_{ab}\lambda_\beta^+)_0
&=(D_\alpha(W^{ab}W_{ab}))\lambda_\beta^+-W^{ab}W_{ab}\varepsilon_{\alpha\beta}X^{++},\\
D_\alpha((\nabla^cW_{ac})\lambda_\rho^+)_0
&=(D_\alpha\nabla^cW_{ac})\lambda_\rho^+-(\nabla^cW_{ac})\varepsilon_{\alpha\rho}X^{++},\\
D_\alpha((\nabla_cW_{de})\lambda_\rho^+)_0
&=(D_\alpha\nabla_cW_{de})\lambda_\rho^+-(\nabla_cW_{de})\varepsilon_{\alpha\rho}X^{++}.
\end{aligned}
\tag{S2-162}
```

Finally the coefficient selector and spinor derivative do not commute: $`D_\beta\Box W=(D_\beta\Box W)_0+W(D_\beta\Box W)_1`$. Hence the complete trace is

```math
(D^{++}\Box W)_0=-\varepsilon^{\alpha\beta}\Big[D_\alpha(D_\beta\Box W)_0
-\tfrac i{16}\lambda_\alpha^+W^{ab}W_{ab\beta}^+\Big].
\tag{S2-163}
```

The second term is $`D_\alpha W=i\lambda_\alpha^+`$ multiplying (S2-140); it must not be lost after selecting a coefficient.

The following tables carry out the trace of every term in (S2-163). Each row includes $`-\varepsilon^{\alpha\beta}D_\alpha`$, the original coefficient in (S2-157), and any Grassmann interchange required to put $`X_\rho^+`$ first or the differentiated Weyl spinor second. Row 9 is the second term of (S2-163), already differentiated. All source curvatures in (S2-160) are substituted before the Clifford contractions (S2-68), (S2-85), and (S2-139).

| Term being differentiated | $`i\Box X^{++}`$ | $`F_{ab}X^{ab++}`$ | $`iW^{ab}W_{ab}X^{++}`$ |
|---|---:|---:|---:|
| $`i\Box\lambda_\beta^+`$ | $`-4`$ | $`-3/8`$ | $`9/16`$ |
| $`2iT^a{}_\beta{}^\rho\nabla_a\lambda_\rho^+`$ | $`0`$ | $`0`$ | $`11/4`$ |
| $`-3X_{\beta\rho}^{+-}\lambda^{\rho+}/8`$ | $`0`$ | $`0`$ | $`0`$ |
| $`3X_{\beta\rho}^{++}\lambda^{\rho-}/8`$ | $`0`$ | $`-3/8`$ | $`0`$ |
| $`-9iW^{ab}W_{ab}\lambda_\beta^+/64`$ | $`0`$ | $`0`$ | $`9/16`$ |
| $`-9i(\Gamma^a)_\beta{}^\rho(\nabla^cW_{ac})\lambda_\rho^+/16`$ | $`0`$ | $`0`$ | $`0`$ |
| $`-3i\varepsilon^{abcde}(\Sigma_{ab})_\beta{}^\rho(\nabla_cW_{de})\lambda_\rho^+/16`$ | $`0`$ | $`0`$ | $`0`$ |
| $`(\Gamma^a)_\beta{}^\rho X_\rho^+\nabla_aW/4`$ | $`0`$ | $`0`$ | $`0`$ |
| $`-i\lambda_\alpha^+W^{ab}W_{ab\beta}^+/16`$ from (S2-163) | $`0`$ | $`0`$ | $`0`$ |
| Sum | $`-4`$ | $`-3/4`$ | $`31/8`$ |

| Same row, in the same order | $`i(\Gamma^a)^{\alpha\beta}X_\alpha^+\nabla_a\lambda_\beta^+`$ | $`i(\Gamma^a)^{\alpha\beta}\lambda_\alpha^+\nabla_aX_\beta^+`$ | $`iW^{ab}W_{ab}^{\alpha+}\lambda_\alpha^+`$ | $`i(\Sigma_{ab})^{\alpha\beta}W^{ab}X_\alpha^+\lambda_\beta^+`$ |
|---|---:|---:|---:|---:|
| 1: $`\Box\lambda`$ | $`1/4`$ | $`-3/8`$ | $`-27/32`$ | $`3/32`$ |
| 2: $`T\nabla\lambda`$ | $`1/2`$ | $`0`$ | $`-7/2`$ | $`-1/2`$ |
| 3: $`X^{+-}_{\beta\rho}\lambda^{\rho+}`$ | $`0`$ | $`3/8`$ | $`0`$ | $`-3/16`$ |
| 4: $`X^{++}_{\beta\rho}\lambda^{\rho-}`$ | $`0`$ | $`0`$ | $`0`$ | $`0`$ |
| 5: $`W^{ab}W_{ab}\lambda`$ | $`0`$ | $`0`$ | $`-9/32`$ | $`-9/32`$ |
| 6: divergence of $`W_{ab}`$ | $`0`$ | $`9/8`$ | $`9/16`$ | $`9/8`$ |
| 7: curl of $`W_{ab}`$ | $`0`$ | $`-9/8`$ | $`0`$ | $`9/16`$ |
| 8: $`X_\rho^+\nabla_aW`$ | $`-1/4`$ | $`0`$ | $`0`$ | $`7/16`$ |
| 9: differentiated explicit scalar $`W`$ | $`0`$ | $`0`$ | $`-1/16`$ | $`0`$ |
| Sum | $`1/2`$ | $`0`$ | $`-33/8`$ | $`5/4`$ |

For example, row 4 is $`-(3/8)\varepsilon^{\alpha\beta}X_{\beta\rho}^{++}\varepsilon^{\rho\tau}(-2F_{\alpha\tau}-\varepsilon_{\alpha\tau}X^{+-}-\nabla_{\alpha\tau}W)`$. The last two contractions vanish because the remaining symmetric $`X_{\beta\rho}^{++}`$ pairs with an antisymmetric spinor metric or gamma matrix; the first is $`-3F_{ab}X^{ab++}/8`$. Row 5 gives $`(-9i/64)(-1)(-1)(-4)=+9i/16`$: the two minus signs are the overall trace and $`D_\alpha\lambda_\beta^+=-\varepsilon_{\alpha\beta}X^{++}`$, while $`\varepsilon^{\alpha\beta}\varepsilon_{\alpha\beta}=-4`$. Its other two entries insert $`D_\alpha W^2=2W^{ab}W_{ab\alpha}^++4W_\alpha{}^\rho X_\rho^+`$ and raise the remaining spinor index. Row 9 moves $`\lambda_\alpha^+`$ past the odd $`W_{ab\beta}^+`$, then raises $`\beta`$; the result is $`-iW^{ab}W_{ab}^{\alpha+}\lambda_\alpha^+/16`$.

In particular the $`\lambda\nabla X`$ terms cancel as $`-3/8+3/8+9/8-9/8=0`$. The Weyl three-spinor coefficient is $`(-27-112-9+18-2)/32=-33/8`$. The $`\Sigma WX\lambda`$ coefficient is $`(3-16-6-9+36+18+14)/32=5/4`$. Adding all rows gives

```math
\begin{aligned}
(D^{++}\Box W)_0={}&-4i\Box X^{++}-\tfrac34F_{ab}X^{ab++}+\tfrac{31i}{8}W^{ab}W_{ab}X^{++}
-\tfrac{33i}{8}W^{ab}W_{ab}^{\alpha+}\lambda_\alpha^+\\
&+\tfrac{5i}{4}(\Sigma_{ab})^{\alpha\beta}W^{ab}X_\alpha^+\lambda_\beta^+
+\tfrac i2(\Gamma^a)^{\alpha\beta}X_\alpha^+\nabla_a\lambda_\beta^+.
\end{aligned}
\tag{S2-164}
```

This has weight four, as required by $`[D^{++}\Box W]=1+2+1`$. The derivative of $`W`$ and the derivative of $`X^{++}`$ that occur inside (S2-160) cancel in the spinor trace; no field equation sets them to zero.

### 4.29 Collecting the new descendant $`(\Delta X^{--})_0`$

Now substitute (S2-149), (S2-150), (S2-155), and (S2-164) into the five actual terms of (S2-143). The following table includes each prefactor in (S2-143); consequently the columns can be added without any further projector factor.

| Term of (S2-143) | $`\Box X^{++}`$ | $`YX^{++}`$ | $`W^{ab}W_{ab}X^{++}`$ | $`iF_{ab}X^{ab++}`$ |
|---|---:|---:|---:|---:|
| $`i(D^{++}\Box W)_0/4`$ | $`1`$ | $`0`$ | $`-31/32`$ | $`-3/16`$ |
| $`-i(D^{++}(W_{ab}F^{ab}))_0/4`$ | $`0`$ | $`0`$ | $`2`$ | $`1`$ |
| $`-5i(D^{++}(X^{\alpha+}\lambda_\alpha^-))_0/32`$ | $`0`$ | $`0`$ | $`0`$ | $`-5/16`$ |
| $`9i(D^{++}(X^{\alpha-}\lambda_\alpha^+))_0/32`$ | $`0`$ | $`-9/32`$ | $`0`$ | $`0`$ |
| Last product in (S2-143) | $`0`$ | $`3/32`$ | $`-31/32`$ | $`0`$ |
| Sum | $`1`$ | $`-3/16`$ | $`1/16`$ | $`1/2`$ |
| Same five terms | $`W^{ab}W_{ab}^{\alpha+}\lambda_\alpha^+`$ | $`(\Sigma_{ab})^{\alpha\beta}W^{ab}X_\alpha^+\lambda_\beta^+`$ | $`(\Gamma^a)^{\alpha\beta}X_\alpha^+\nabla_a\lambda_\beta^+`$ | $`(\Gamma^a)^{\alpha\beta}\lambda_\alpha^+\nabla_aX_\beta^+`$ |
|---|---:|---:|---:|---:|
| $`i(D^{++}\Box W)_0/4`$ | $`33/32`$ | $`-5/16`$ | $`-1/8`$ | $`0`$ |
| $`-i(D^{++}(W_{ab}F^{ab}))_0/4`$ | $`-2`$ | $`1/2`$ | $`2`$ | $`0`$ |
| $`-5i(D^{++}(X^{\alpha+}\lambda_\alpha^-))_0/32`$ | $`0`$ | $`-25/32`$ | $`-5/8`$ | $`0`$ |
| $`9i(D^{++}(X^{\alpha-}\lambda_\alpha^+))_0/32`$ | $`0`$ | $`9/16`$ | $`0`$ | $`-9/8`$ |
| Last product in (S2-143) | $`31/32`$ | $`25/32`$ | $`0`$ | $`3/8`$ |
| Sum | $`0`$ | $`3/4`$ | $`5/4`$ | $`-3/4`$ |

The $`W W_{ab}^{\alpha+}\lambda_\alpha^+`$ contraction cancels already in this descendant: $`(33-64+31)/32=0`$. The other coefficients follow, for example, from $`(-31+64-31)/32=1/16`$ and $`(-5+8-25/2+9+25/2)/16=3/4`$. Thus

```math
\begin{aligned}
(\Delta X^{--})_0={}&\Box X^{++}-\tfrac3{16}YX^{++}+\tfrac1{16}W^{ab}W_{ab}X^{++}
+\tfrac i2F_{ab}X^{ab++}\\
&+\tfrac54(\Gamma^a)^{\alpha\beta}X_\alpha^+\nabla_a\lambda_\beta^+
-\tfrac34(\Gamma^a)^{\alpha\beta}\lambda_\alpha^+\nabla_aX_\beta^+
+\tfrac34(\Sigma_{ab})^{\alpha\beta}W^{ab}X_\alpha^+\lambda_\beta^+.
\end{aligned}
\tag{S2-165}
```

All seven terms here have weight four and two external plus indices. This is a descendant identity derived from (S2-107); no coefficient of the published $`H^{ij}`$ was used to obtain it.

### 4.30 Reducing the remaining six contributions to $`H^{++}|_{W^{-1}}`$

The second and fourth contributions in (S2-136) are already reduced, namely $`3YX^{++}/64-31W^{ab}W_{ab}X^{++}/64`$ and $`W^{ab}W_{ab}X^{++}/8`$. For the third, insert (S2-142) with its original spinor order:

```math
\begin{aligned}
-\tfrac i{16}\lambda^{\alpha+}(D_\alpha D^{++}X^{--})_1
={}&-\tfrac i{16}\lambda^{\alpha+}\big[8iW^{ab}W_{ab\alpha}^++15iW_\alpha{}^\beta X_\beta^+-6i(\Gamma^a)_\alpha{}^\beta\nabla_aX_\beta^+\big]\\
={}&\tfrac12W^{ab}W_{ab}^{\alpha+}\lambda_\alpha^+
+\tfrac{15}{32}(\Sigma_{ab})^{\alpha\beta}W^{ab}X_\alpha^+\lambda_\beta^+
+\tfrac38(\Gamma^a)^{\alpha\beta}\lambda_\alpha^+\nabla_aX_\beta^+.
\end{aligned}
\tag{S2-166}
```

The raising/reordering identities used on these three terms are $`\lambda^{\alpha+}W_{ab\alpha}^+=W_{ab}^{\alpha+}\lambda_\alpha^+`$, $`\lambda^{\alpha+}W_\alpha{}^\beta X_\beta^+=(\Sigma_{ab})^{\alpha\beta}W^{ab}X_\alpha^+\lambda_\beta^+/2`$, and $`\lambda^{\alpha+}(\Gamma^a)_\alpha{}^\beta\nabla_aX_\beta^+=-(\Gamma^a)^{\alpha\beta}\lambda_\alpha^+\nabla_aX_\beta^+`$. Each uses the fixed antisymmetric spinor metric. The first two also interchange two odd factors.

For the fifth contribution, (S2-128) applies directly with $`F_{ab}`$ there replaced by $`W_{ab}`$: the prefactor $`1/16`$ times $`-2F_{\delta\sigma}`$ is precisely the present $`-W_{\delta\sigma}/8`$. Inserting its three terms individually gives

```math
\begin{aligned}
&-\tfrac18\varepsilon^{\alpha\beta\gamma\delta}\lambda_\alpha^+
\big[-\tfrac32\varepsilon_{\beta\gamma}X_\rho^+-\tfrac12\varepsilon_{\beta\rho}X_\gamma^++\tfrac12\varepsilon_{\gamma\rho}X_\beta^+\big]\varepsilon^{\rho\sigma}W_{\delta\sigma}\\
&\qquad=\big(\tfrac3{16}+0+0\big)(\Sigma_{ab})^{\alpha\beta}W^{ab}X_\alpha^+\lambda_\beta^+
=\tfrac3{16}(\Sigma_{ab})^{\alpha\beta}W^{ab}X_\alpha^+\lambda_\beta^+.
\end{aligned}
\tag{S2-167}
```

The sixth contribution contains two products. The first pairs $`-4X_{\alpha\rho}^{++}`$ only with $`-2F_{\delta\sigma}`$: its scalar and gradient traces vanish. It gives $`-iF_{ab}X^{ab++}/8`$. In the second product insert every degree-zero term of (S2-117). The $`4i\nabla_{\alpha\rho}X^{++}`$ term has zero trace with $`W_{\delta\sigma}`$. The $`-8iW_{\alpha\rho}X^{++}`$ term gives $`W^{ab}W_{ab}X^{++}/4`$. The three-spinor term $`-8iW_{\alpha\rho\tau}^+\lambda^{\tau+}`$ gives $`-W^{ab}W_{ab}^{\alpha+}\lambda_\alpha^+/4`$. The remaining three Weyl-spinor terms have coefficients $`0,-1/16,+1/16`$ multiplying $`(\Sigma_{ab})^{\alpha\beta}W^{ab}X_\alpha^+\lambda_\beta^+`$, and cancel. Therefore its complete reduction is

```math
\begin{aligned}
&\tfrac i{32}\varepsilon^{\delta\alpha}\varepsilon^{\rho\sigma}
\Big[-4X_{\alpha\rho}^{++}(-2F_{\delta\sigma}-\varepsilon_{\delta\sigma}X^{+-}-\nabla_{\delta\sigma}W)
-2(D_\alpha D^{++}\lambda_\rho^-)_0W_{\delta\sigma}\Big]\\
&\qquad=-\tfrac i8F_{ab}X^{ab++}+\tfrac14W^{ab}W_{ab}X^{++}
-\tfrac14W^{ab}W_{ab}^{\alpha+}\lambda_\alpha^+.
\end{aligned}
\tag{S2-168}
```

For the seventh contribution, use both placements of the scalar-degree-one part of (S2-49). They are equal: exchanging the triples $`(\alpha,\beta,\rho)`$ and $`(\gamma,\delta,\sigma)`$ gives an even permutation in the four-index epsilon, a minus sign in $`\varepsilon^{\rho\sigma}`$, and a minus sign from exchanging the two odd descendants. Consequently

```math
\begin{aligned}
&-\tfrac i{128}\varepsilon^{\alpha\beta\gamma\delta}\varepsilon^{\rho\sigma}
\Big[(D_\alpha D_\beta\lambda_\rho^-)_0(D_\gamma D_\delta\lambda_\sigma^-)_1
+(D_\alpha D_\beta\lambda_\rho^-)_1(D_\gamma D_\delta\lambda_\sigma^-)_0\Big]\\
&=-\tfrac i{64}\varepsilon^{\alpha\beta\gamma\delta}\varepsilon^{\rho\sigma}
(D_\alpha D_\beta\lambda_\rho^-)_0
\big[-\tfrac32\varepsilon_{\gamma\delta}X_\sigma^+-\tfrac12\varepsilon_{\gamma\sigma}X_\delta^++\tfrac12\varepsilon_{\delta\sigma}X_\gamma^+\big].
\end{aligned}
\tag{S2-169}
```

The six derivative terms and three algebraic terms of the first factor give the following nine separate contractions. The table includes the $`-i/64`$ and the three terms in the second factor; the Weyl spinor has been moved to the left, with its odd interchange sign.

| Term inserted from $`(D_\alpha D_\beta\lambda_\rho^-)_0`$ | $`(\Gamma^a)^{\mu\nu}X_\mu^+\nabla_a\lambda_\nu^+`$ | $`(\Sigma_{ab})^{\mu\nu}W^{ab}X_\mu^+\lambda_\nu^+`$ |
|---|---:|---:|
| $`i\nabla_{\alpha\beta}\lambda_\rho^+`$ | $`-1/32`$ | $`0`$ |
| $`i\nabla_{\alpha\rho}\lambda_\beta^+`$ | $`5/64`$ | $`0`$ |
| $`i\varepsilon_{\alpha\beta}\nabla_\rho{}^\tau\lambda_\tau^+`$ | $`-7/32`$ | $`0`$ |
| $`i\varepsilon_{\alpha\rho}\nabla_\beta{}^\tau\lambda_\tau^+`$ | $`-1/64`$ | $`0`$ |
| $`-i\varepsilon_{\beta\rho}\nabla_\alpha{}^\tau\lambda_\tau^+`$ | $`-1/64`$ | $`0`$ |
| $`-i\nabla_{\beta\rho}\lambda_\alpha^+`$ | $`5/64`$ | $`0`$ |
| $`iW_{\beta\rho}\lambda_\alpha^+`$ | $`0`$ | $`3/128`$ |
| $`-iW_{\alpha\rho}\lambda_\beta^+`$ | $`0`$ | $`3/128`$ |
| $`-3i\varepsilon_{\alpha\beta}W_{\rho\tau}\lambda^{\tau+}`$ | $`0`$ | $`-21/64`$ |
| Sum | $`-1/8`$ | $`-9/32`$ |

For these entries expand $`\varepsilon^{\alpha\beta\gamma\delta}=\varepsilon^{\alpha\beta}\varepsilon^{\gamma\delta}-\varepsilon^{\alpha\gamma}\varepsilon^{\beta\delta}+\varepsilon^{\alpha\delta}\varepsilon^{\beta\gamma}`$ before contracting; only one gamma or one $`\Sigma`$ is left. Thus this table uses spinor-metric contractions, not a new Fierz ansatz. The two sums are $`(-2+5-14-1-1+5)/64=-1/8`$ and $`(3+3-42)/128=-9/32`$. This completes the last contribution:

```math
\text{last line of (S2-136)}
=-\tfrac18(\Gamma^a)^{\alpha\beta}X_\alpha^+\nabla_a\lambda_\beta^+
-\tfrac9{32}(\Sigma_{ab})^{\alpha\beta}W^{ab}X_\alpha^+\lambda_\beta^+.
\tag{S2-170}
```

### 4.31 Final coefficient addition and restoration of $`ij`$

Every term in (S2-136) has now been reduced. The unwanted $`\Sigma WX\lambda`$ contraction cancels as

```math
-\tfrac12\big(\tfrac34\big)+\tfrac{15}{32}+\tfrac3{16}-\tfrac9{32}
=\tfrac{-12+15+6-9}{32}=0.
\tag{S2-171}
```

Its four origins are (S2-165), (S2-166), (S2-167), and (S2-170), respectively. No local fermion bilinear was discarded. The seven surviving numerators have the following coefficients, already including $`-1/2`$ multiplying (S2-165):

| Numerator of the $`W^{-1}`$ sector, with $`W^{-1}`$ factored out | Contributions in (S2-136) | Sum |
|---|---|---:|
| $`YX^{++}`$ | $`3/32+3/64`$ | $`9/64`$ |
| $`iF_{ab}X^{ab++}`$ | $`-1/4-1/8`$ | $`-3/8`$ |
| $`\Box X^{++}`$ | $`-1/2`$ | $`-1/2`$ |
| $`W^{ab}W_{ab}X^{++}`$ | $`-1/32-31/64+1/8+1/4`$ | $`-9/64`$ |
| $`W^{ab}W_{ab}^{\alpha+}\lambda_\alpha^+`$ | $`1/2-1/4`$ | $`1/4`$ |
| $`(\Gamma^a)^{\alpha\beta}X_\alpha^+\nabla_a\lambda_\beta^+`$ | $`-5/8-1/8`$ | $`-3/4`$ |
| $`(\Gamma^a)^{\alpha\beta}\lambda_\alpha^+\nabla_aX_\beta^+`$ | $`3/8+3/8`$ | $`3/4`$ |

The plus projection was made with arbitrary constant $`u_i^+`$. Each row is quadratic in that isotwistor. Equality for arbitrary $`u_i^+`$ therefore gives equality of the symmetric rank-two SU(2) tensors: $`X^{++}\mapsto X^{ij}`$ and $`A^+B^+\mapsto A^{(i}B^{j)}`$. It introduces no extra factor because the normalized symmetrization is already selected by $`u_i^+u_j^+`$. The complete seven-term result is (S2-172) under **Final Result**.

### 4.32 Selecting the two remaining $`W^0`$ contributions

<!-- ASSERT_CONVENTION: source_frame=Gold traceless Standard-Weyl superspace, metric_signature=(-,+,+,+,+), natural_units=hbar=c=1, scope=classical off-shell gauge-unfixed LOG primary, fermions=all degrees retained -->

This last denominator sector completes the coefficient reconstruction from S23 (3.24). The assumptions A1–A4 and the spinor order of section 2 remain in force. We use the source Weyl identities S23 (2.6), the generator action (2.8a), the vector rules (2.13), (2.15), and C24 (A.1l), (A.3). The new source-sensitive point is the $`W_a{}^b\Gamma_b S`$ term of (A.1l), whose action first contributes to the scalar-degree-one calculation below. Its exact source image is [C24 PDF82](https://arxiv.org/abs/2311.00679). The comparison target is the first line of [S23 (3.25), PDF21](https://arxiv.org/abs/2302.14295).

The subscript $`n`$ still means the coefficient of **explicit scalar** $`W^n`$, with the super-Weyl two-form $`W_{ab}`$ kept distinct. In (S2-100), any derivative on $`W^{-1}`$ produces a denominator at least $`W^{-2}`$; the corresponding differentiated $`X^{--}`$ contains at most one scalar $`W`$. A derivative on $`W^{-2}`$ produces a denominator at least $`W^{-3}`$, while the differentiated bilinear contains at most two scalar factors. Those distributed products therefore have a strictly negative power of $`W`$. Only the undistributed four derivatives can give $`W^0`$:

```math
\left.H^{++}\right|_{W^0}
=-\tfrac12(\Delta X^{--})_1-\tfrac i8(\Delta B^{--})_2,
\qquad B^{--}=\lambda^{\alpha-}\lambda_\alpha^-.
\tag{S2-173}
```

For the first term, take the degree-one coefficient of (S2-143):

```math
\begin{aligned}
(\Delta X^{--})_1={}&\tfrac i4(D^{++}\Box W)_1-\tfrac i4(D^{++}(W_{ab}F^{ab}))_1
-\tfrac{5i}{32}(D^{++}(X^{\alpha+}\lambda_\alpha^-))_1
+\tfrac{9i}{32}(D^{++}(X^{\alpha-}\lambda_\alpha^+))_1\\
&-\tfrac1{32}D^{++}\big(-\tfrac{3i}{4}Y+\tfrac{31i}{4}W^{ab}W_{ab}\big).
\end{aligned}
\tag{S2-174}
```

The last line has no scalar $`W`$: it is the coefficient of $`W`$ in the derivative of $`W(-3iY/4+31iW^{ab}W_{ab}/4)`$. Its other product-rule placements have degree zero and were already included in (S2-150). Every term of (S2-174) has weight three after stripping one scalar $`W`$ from the weight-four descendant.

### 4.33 Weyl traces and the two odd products

The all-plus specializations of S23 (2.6a–c,e) and (2.13a), together with (S2-72), are

```math
\begin{aligned}
D_\alpha W_{\rho\sigma}&=W_{\alpha\rho\sigma}^++\tfrac12\varepsilon_{\alpha\rho}X_\sigma^++\tfrac12\varepsilon_{\alpha\sigma}X_\rho^+,
& D_\alpha X_\rho^+&=X_{\alpha\rho}^{++},\\
D_\alpha W_{\beta\rho\sigma}^+&=-\tfrac12(\varepsilon_{\alpha\beta}X_{\rho\sigma}^{++}+\varepsilon_{\alpha\rho}X_{\beta\sigma}^{++}+\varepsilon_{\alpha\sigma}X_{\beta\rho}^{++}),
& D_\alpha X_{\rho\sigma}^{++}&=0,\\
(D_\alpha\lambda_\rho^-)_1&=-2W_{\alpha\rho},
& (D^{++}\lambda_\rho^-)_1&=-7X_\rho^+.
\end{aligned}
\tag{S2-175}
```

The factor $`1/2`$ in the three-spinor derivative is $`3/2`$ times its normalized three-index symmetrization. The coefficient $`-7`$ in the last line is the contraction of the three degree-one terms in (S2-49); their uncontracted form remains visible in (S2-187) below.

We first evaluate $`D^{++}Y`$. The mixed commutator on the Weyl spinor is

```math
\begin{aligned}
D_\alpha\nabla_aX_\rho^+={}&\nabla_aX_{\alpha\rho}^{++}+T_{a\alpha}{}^\tau X_{\tau\rho}^{++}
+\tfrac12R(M)_{a\alpha}^{+,bc}(\Sigma_{bc})_\rho{}^\tau X_\tau^+
+4R(S)_{a\alpha}^{+,\tau+}W_{\tau\rho},\\
R(S)_{a\alpha}^{+,\tau+}&=\tfrac1{16}X_{bc}^{++}(\Sigma^{bc}\Gamma_a-2\Gamma_a\Sigma^{bc})_\alpha{}^\tau.
\end{aligned}
\tag{S2-176}
```

The Weyl spinor has weight $`3/2`$ and the same external plus index as the gaugino, so its dilatation and SU(2) terms cancel in this projected mixed commutator. The S term is different: S23 (2.8a) gives $`S_{\tau k}X_\rho^+=4\delta_k^+W_{\tau\rho}`$, with no $`i`$. K annihilates $`X_\rho^+`$. In the second line all terms proportional to $`\varepsilon^{++}`$ in C24 (A.3e) vanish, leaving the displayed two-form descendant.

Differentiate S23 (2.6f), $`D_\beta Y=8(\Gamma^a)_\beta{}^\rho\nabla_aX_\rho^++8W_\beta{}^\rho X_\rho^+`$, then trace:

```math
\begin{aligned}
D^{++}Y={}&-8\varepsilon^{\alpha\beta}(\Gamma^a)_\beta{}^\rho
\Big[\nabla_aX_{\alpha\rho}^{++}+T_{a\alpha}{}^\tau X_{\tau\rho}^{++}
+\tfrac12R(M)_{a\alpha}^{+,bc}(\Sigma_{bc})_\rho{}^\tau X_\tau^+
+4R(S)_{a\alpha}^{+,\tau+}W_{\tau\rho}\Big]\\
&-8\varepsilon^{\alpha\beta}(D_\alpha W_\beta{}^\rho)X_\rho^+
-8\varepsilon^{\alpha\beta}W_\beta{}^\rho X_{\alpha\rho}^{++}\\
={}&(-14+18-4)W_{ab}X^{ab++}+(-20+20)X^{\alpha+}X_\alpha^+=0.
\end{aligned}
\tag{S2-177}
```

Here are the contractions that give the last line, including the common $`-8\varepsilon^{\alpha\beta}`$:

| Actual term being traced | $`W_{ab}X^{ab++}`$ | $`X^{\alpha+}X_\alpha^+`$ |
|---|---:|---:|
| $`(\Gamma^a)_\beta{}^\rho\nabla_aX_{\alpha\rho}^{++}`$ | $`0`$ | $`0`$ |
| $`(\Gamma^a)_\beta{}^\rho T_{a\alpha}{}^\tau X_{\tau\rho}^{++}`$ | $`-14`$ | $`0`$ |
| $`(\Gamma^a)_\beta{}^\rho R(M)_{a\alpha}^{+,bc}(\Sigma_{bc})_\rho{}^\tau X_\tau^+/2`$ | $`0`$ | $`-20`$ |
| $`4(\Gamma^a)_\beta{}^\rho R(S)_{a\alpha}^{+,\tau+}W_{\tau\rho}`$ | $`18`$ | $`0`$ |
| $`(D_\alpha W_\beta{}^\rho)X_\rho^+`$ | $`0`$ | $`20`$ |
| $`W_\beta{}^\rho X_{\alpha\rho}^{++}`$ | $`-4`$ | $`0`$ |

For the first row, raising the $`\beta`$ slot leaves a gamma matrix antisymmetric in $`\alpha,\rho`$, whereas $`X_{\alpha\rho}^{++}`$ is symmetric; thus its contraction is exactly zero even before applying any Bianchi identity to $`\nabla_aX_{\alpha\rho}^{++}`$. For rows 2 and 4 insert $`T_a=(3\Gamma_aW-W\Gamma_a)/4`$ and the second line of (S2-176), then use $`\Gamma^a\Gamma_a=-5`$ and $`\Gamma^a\Sigma^{bc}\Gamma_a=-\Sigma^{bc}`$. Each remaining pair of symmetric bispinors converts by $`2W^{\alpha\beta}X_{\alpha\beta}^{++}=W_{ab}X^{ab++}`$. In row 3 insert all three parts of $`R(M)`$ in (S2-67). The two three-spinor parts vanish by $`\Gamma^aW_{ab}^+=0`$; the Weyl-spinor part leaves $`-20X^{\alpha+}X_\alpha^+`$. In row 5 use $`D_\alpha W_\beta{}^\rho=-(D_\alpha W_{\beta\tau})\varepsilon^{\tau\rho}`$ and (S2-175); the three-spinor trace vanishes and the two metric terms give $`20X^{\alpha+}X_\alpha^+`$. These are cancellations of actual curvature contributions, not an assumption that $`Y`$ is constant.

For the two largest bosonic entries, the intermediate matrix contractions are especially useful. Define the mixed Weyl descendant by $`X_\alpha{}^{\beta++}=-X_{\alpha\rho}^{++}\varepsilon^{\rho\beta}`$, consistently with the mixed super-Weyl matrix. Then

```math
\begin{aligned}
W_\alpha{}^\beta X_\beta{}^{\alpha++}&=-\tfrac12W_{ab}X^{ab++},\\
(\Gamma^a)_\beta{}^\rho T_{a\rho}{}^\tau
&=\tfrac14[3\Gamma^a\Gamma_aW-\Gamma^aW\Gamma_a]_\beta{}^\tau
=\tfrac14(-15+1)W_\beta{}^\tau=-\tfrac72W_\beta{}^\tau,\\
(\Gamma^a)_\beta{}^\rho R(S)_{a\rho}^{+,\tau+}
&=\tfrac1{16}X_{bc}^{++}[\Gamma^a\Sigma^{bc}\Gamma_a-2\Gamma^a\Gamma_a\Sigma^{bc}]_\beta{}^\tau
=\tfrac9{16}X_{bc}^{++}(\Sigma^{bc})_\beta{}^\tau
=\tfrac98X_\beta{}^{\tau++}.
\end{aligned}
\tag{S2-177a}
```

The first equality follows by inserting both two-form/bispinor definitions and the $`\Sigma`$ trace in (S2-85). Thus row 2 has coefficient $`(-8)(-7/2)(-1/2)=-14`$ and row 4 has $`(-32)(9/8)(-1/2)=18`$. These explicit contractions fix the relative sign of torsion and S curvature.

Next use $`W^{ab}W_{ab}=2W^{\rho\sigma}W_{\rho\sigma}`$. Keeping the differentiated odd factors in their written order gives

```math
\begin{aligned}
D^{++}(W^{ab}W_{ab})
&=-4\varepsilon^{\alpha\beta}(D_\alpha W^{\rho\sigma})(D_\beta W_{\rho\sigma})
-4\varepsilon^{\alpha\beta}W^{\rho\sigma}D_\alpha D_\beta W_{\rho\sigma}\\
&=4W^{\alpha\beta\gamma+}W_{\alpha\beta\gamma}^+
+(4+1+1+4)X^{\alpha+}X_\alpha^+-8W_{ab}X^{ab++}.
\end{aligned}
\tag{S2-178}
```

All three spinor indices in $`W^{\alpha\beta\gamma+}`$ are raised with the same antisymmetric spinor metric. In the first product, the two three-spinors give the coefficient $`4`$: $`\varepsilon^{\alpha\beta}\varepsilon^{\rho\mu}\varepsilon^{\sigma\nu}W_{\alpha\mu\nu}^+W_{\beta\rho\sigma}^+=-W^{\alpha\beta\gamma+}W_{\alpha\beta\gamma}^+`$, with the sign from the raised first index. Each mixed three-spinor–$`X`$ term traces two symmetric three-spinor slots against an antisymmetric metric and is zero. The four products of the two half-weight metric terms in (S2-175) have coefficients $`4,1,1,4`$, in the order $`(\varepsilon_{\alpha\mu}X_\nu,\varepsilon_{\alpha\nu}X_\mu)`$ against $`(\varepsilon_{\beta\rho}X_\sigma,\varepsilon_{\beta\sigma}X_\rho)`$. Their common factor $`-4(1/2)(1/2)=-1`$ has already been included. Finally (S2-152) gives $`4W^{\rho\sigma}D^{++}W_{\rho\sigma}=-16W^{\rho\sigma}X_{\rho\sigma}^{++}=-8W_{ab}X^{ab++}`$.

For the first odd product in (S2-174), use the odd rule (S2-144), $`D^{++}X_\rho^+=0`$, and the last line of (S2-175):

```math
\begin{aligned}
(D^{++}(X^{\rho+}\lambda_\rho^-))_1
&=-7X^{\rho+}X_\rho^+
+2\varepsilon^{\alpha\beta}\varepsilon^{\rho\sigma}X_{\alpha\sigma}^{++}(-2W_{\beta\rho})
=2W_{ab}X^{ab++}-7X^{\rho+}X_\rho^+,\\
(D^{++}(X^{\rho-}\lambda_\rho^+))_1&=0,\\
\big[D^{++}\{W(-\tfrac{3i}{4}Y+\tfrac{31i}{4}W^{ab}W_{ab})\}\big]_1
&=-62iW_{ab}X^{ab++}+\tfrac{155i}{2}X^{\alpha+}X_\alpha^+
+31iW^{\alpha\beta\gamma+}W_{\alpha\beta\gamma}^+.
\end{aligned}
\tag{S2-179}
```

The first cross term is $`-4\varepsilon^{\alpha\beta}\varepsilon^{\rho\sigma}X_{\alpha\sigma}^{++}W_{\beta\rho}=4X^{\rho\sigma++}W_{\rho\sigma}`$, giving the coefficient $`2`$ after two-form conversion. The second product is zero at degree one because neither $`D\lambda^+`$, $`D^{++}\lambda^+`$, nor any derivative of the Weyl spinor carries a scalar $`W`$. The last equality inserts (S2-177)–(S2-178), multiplying by $`31i/4`$; it does not set any Weyl field to zero.

### 4.34 The last connection contribution: $`(D^{++}\Box W)_1`$

In this coefficient the full S action on a vector derivative of $`\lambda^+`$ is needed. In addition to the part in (S2-159), the Jacobi-consistent repair of C24 (A.1l) gives the relation below. The factors of $`i`$ in its K terms are derived in [the curved audit](../../../../../../references/source_evidence/log/derivations/curved.md), (CC-03)–(CC-11); the literal source is preserved separately in the master:

```math
\begin{aligned}
[S_{\gamma k},\nabla_a]
&=i(\Gamma_a)_\gamma{}^\tau\nabla_{\tau k}
-\tfrac14W_a{}^b(\Gamma_b)_\gamma{}^\tau S_{\tau k}
+\tfrac i8(\Gamma_a\Gamma^b)_\gamma{}^\tau X_{\tau k}K_b
-\tfrac i4W_{ab\gamma k}K^b,\\
(S_{\gamma k}\nabla_a\lambda_\beta^+)_1
&=\delta_k^+\big[-2i(\Gamma_a)_\gamma{}^\tau W_{\tau\beta}
+\tfrac i2W_a{}^b(\Gamma_b)_\gamma{}^\tau\varepsilon_{\tau\beta}\big].
\end{aligned}
\tag{S2-180}
```

The first term substitutes $`(\nabla_{\tau+}\lambda_\beta^+)_1=-2W_{\tau\beta}`$. The second substitutes $`S_{\tau k}\lambda_\beta^+=-2i\delta_k^+\varepsilon_{\tau\beta}W`$ into $`-W_a{}^b\Gamma_b S/4`$, producing $`+i/2`$. Both K terms annihilate $`\lambda^+`$. The separate $`\nabla_a(S\lambda^+)`$ is proportional to $`\nabla_aW`$, so has explicit scalar degree zero, already handled at the previous pole. Thus no term in this generator action has been suppressed merely because the original scalar was primary.

Insert (S2-180) into the ordered two-commutator identity (S2-158):

```math
\begin{aligned}
(D_\alpha\Box\lambda_\beta^+)_1={}&-2i(\nabla^aR(S)_{a\alpha}^{+,\gamma+})\varepsilon_{\gamma\beta}
-2iT^a{}_\alpha{}^\tau R(S)_{a\tau}^{+,\gamma+}\varepsilon_{\gamma\beta}\\
&-2iR(S)^a{}_{\alpha}{}^{+,\gamma+}(\Gamma_a)_\gamma{}^\tau W_{\tau\beta}
+\tfrac i2R(S)^a{}_{\alpha}{}^{+,\gamma+}W_a{}^b(\Gamma_b)_\gamma{}^\tau\varepsilon_{\tau\beta}.
\end{aligned}
\tag{S2-181}
```

Its first term differentiates the degree-one commutator; its second is torsion acting on that commutator; its last two are the two S actions just derived. Lorentz curvature, the additional dilatation weight, and the K action in (S2-160) contain no scalar $`W`$ at this stage. The four contributions to $`-i\varepsilon^{\alpha\beta}(D_\alpha\Box\lambda_\beta^+)_1`$ have coefficients $`0,9/16,-3/8,-3/8`$ multiplying $`W_{ab}X^{ab++}`$. Their sum is $`-3/16`$.

For the zero, contract the first term's spinor indices: the remaining $`\nabla^a\mathop{\mathrm{tr}}\nolimits R(S)_a^{++}`$ is zero because the second line of (S2-176) contains traces of $`\Sigma^{bc}\Gamma_a`$ and $`\Gamma_a\Sigma^{bc}`$, both zero. The other three numbers follow by substituting that same line and the definition of $`T_a`$ before using (S2-85). The last number explicitly measures the $`W_a{}^b\Gamma_bS`$ contribution; it cannot be omitted.

Now differentiate the complete degree-zero expression (S2-157), and add the derivative of its degree-one coefficient (S2-140). The scalar coefficient selector must again be applied after differentiation:

```math
\begin{aligned}
(D^{++}\Box W)_1=-\varepsilon^{\alpha\beta}\Big[&
i(D_\alpha\Box\lambda_\beta^+)_1
+2iT^a{}_\beta{}^\rho(D_\alpha\nabla_a\lambda_\rho^+)_1
-\tfrac34X_{\beta\rho}^{++}\varepsilon^{\rho\tau}W_{\alpha\tau}\\
&+\tfrac1{16}(\Gamma^a)_\beta{}^\rho X_\rho^+(\Gamma_a)_\alpha{}^\tau X_\tau^+
-\tfrac1{16}D_\alpha(W^{ab}W_{ab\beta}^+)\Big],\qquad
(D_\alpha\nabla_a\lambda_\rho^+)_1=-2iR(S)_{a\alpha}^{+,\tau+}\varepsilon_{\tau\rho}.
\end{aligned}
\tag{S2-182}
```

The third term differentiates the plus/minus gaugino in $`3X_{\beta\rho}^{++}\lambda^{\rho-}/8`$. The fourth comes from the odd-product minus sign in $`D_\alpha(X_\rho^+\nabla_aW)`$ multiplied by $`(D_\alpha\nabla_aW)_1=- (\Gamma_a)_\alpha{}^\tau X_\tau^+/4`$. All the other terms of (S2-157) contain only $`\lambda^+`$ and its scalar-independent spinor derivative, and therefore contribute zero to this coefficient.

The five displayed terms reduce separately as follows. Every entry includes the overall $`-\varepsilon^{\alpha\beta}`$ in (S2-182).

| Term in the brackets of (S2-182) | $`W_{ab}X^{ab++}`$ | $`X^{\alpha+}X_\alpha^+`$ | $`W^{\alpha\beta\gamma+}W_{\alpha\beta\gamma}^+`$ |
|---|---:|---:|---:|
| $`i(D_\alpha\Box\lambda_\beta^+)_1`$ | $`-3/16`$ | $`0`$ | $`0`$ |
| $`2iT^a{}_\beta{}^\rho(D_\alpha\nabla_a\lambda_\rho^+)_1`$ | $`15/8`$ | $`0`$ | $`0`$ |
| $`-3X_{\beta\rho}^{++}\varepsilon^{\rho\tau}W_{\alpha\tau}/4`$ | $`-3/8`$ | $`0`$ | $`0`$ |
| $`(\Gamma^a)_\beta{}^\rho X_\rho^+(\Gamma_a)_\alpha{}^\tau X_\tau^+/16`$ | $`0`$ | $`5/16`$ | $`0`$ |
| $`-D_\alpha(W^{ab}W_{ab\beta}^+)/16`$ | $`3/16`$ | $`0`$ | $`-1/8`$ |
| Sum | $`3/2`$ | $`5/16`$ | $`-1/8`$ |

Row 2 substitutes $`-2iR(S)\varepsilon`$ and $`T_a`$, giving the scalar Clifford trace $`15/8`$. Row 3 is the same symmetric-bispinor contraction as in (S2-179), with its distinct prefactor. For row 4, the identity $`\varepsilon^{\alpha\beta}(\Gamma^a)_\beta{}^\rho(\Gamma_a)_\alpha{}^\tau=5\varepsilon^{\rho\tau}`$ gives $`-5\varepsilon^{\rho\tau}X_\rho^+X_\tau^+/16=5X^{\alpha+}X_\alpha^+/16`$. This last sign raises the first spinor index; it does not replace an odd bilinear by a commuting one. In row 5 expand $`D_\alpha(W^{ab}W_{ab\beta}^+)=(D_\alpha W^{ab})W_{ab\beta}^++W^{ab}D_\alpha W_{ab\beta}^+`$. The first product converts to the three-spinor square with coefficient $`-1/8`$; its $`XW_3`$ trace vanishes. The second inserts the three metric terms of (S2-175), giving $`3W_{ab}X^{ab++}/16`$. Thus

```math
(D^{++}\Box W)_1=\tfrac32W_{ab}X^{ab++}+\tfrac5{16}X^{\alpha+}X_\alpha^+
-\tfrac18W^{\alpha\beta\gamma+}W_{\alpha\beta\gamma}^+.
\tag{S2-183}
```

Each term has weight three, as required after removing one scalar $`W`$ from $`D^{++}\Box W`$.

### 4.35 The degree-one derivative of $`W_{ab}F^{ab}`$

Take the degree-one part of the three-product expression (S2-151). The term $`(D^{++}W^{\rho\sigma})F_{\rho\sigma}`$ has no scalar $`W`$. The remaining two products give

```math
\begin{aligned}
(D^{++}(W_{ab}F^{ab}))_1
={}&-2\varepsilon^{\alpha\beta}W^{\rho\sigma}(D_\alpha D_\beta F_{\rho\sigma})_1
+4\varepsilon^{\alpha\beta}(D_\alpha W^{\rho\sigma})W_{\beta\rho\sigma}^+,\\
(D_\alpha D_\beta F_{\rho\sigma})_1
={}&-\tfrac i2\Big[(\Gamma^a)_{\beta\rho}(D_\alpha\nabla_a\lambda_\sigma^+)_1
+(\Gamma^a)_{\beta\sigma}(D_\alpha\nabla_a\lambda_\rho^+)_1\\
&\qquad+\varepsilon_{\beta\rho}(\Gamma^a)_\sigma{}^\tau(D_\alpha\nabla_a\lambda_\tau^+)_1
+\varepsilon_{\beta\sigma}(\Gamma^a)_\rho{}^\tau(D_\alpha\nabla_a\lambda_\tau^+)_1\Big]
-D_\alpha W_{\beta\rho\sigma}^+.
\end{aligned}
\tag{S2-184}
```

The positive cross term in the first line comes from the negative $`(D_\beta F_{\rho\sigma})_1=-W_{\beta\rho\sigma}^+`$ times the negative even-product coefficient $`-4`$. In the second line, the derivative of $`-W_{\beta\rho\sigma}^+W`$ contributes $`-D_\alpha W_{\beta\rho\sigma}^+`$ to degree one; its other odd-product term had degree zero and was retained in (S2-153).

Substitute the final rule of (S2-182) into the four vector-derivative terms. After contraction with $`-2\varepsilon^{\alpha\beta}W^{\rho\sigma}`$ they give $`3W_{ab}X^{ab++}`$. The last term of (S2-184), using (S2-175), gives another $`3W_{ab}X^{ab++}`$. The cross product contributes $`-4W^{\alpha\beta\gamma+}W_{\alpha\beta\gamma}^+`$: its Weyl-spinor pieces trace two symmetric slots of $`W_{\beta\rho\sigma}^+`$ with an antisymmetric metric and vanish. In full,

```math
\begin{aligned}
-2\varepsilon^{\alpha\beta}W^{\rho\sigma}(D_\alpha D_\beta F_{\rho\sigma})_1
&=(3+3)W_{ab}X^{ab++},\\
4\varepsilon^{\alpha\beta}(D_\alpha W^{\rho\sigma})W_{\beta\rho\sigma}^+
&=-4W^{\alpha\beta\gamma+}W_{\alpha\beta\gamma}^+,\\
(D^{++}(W_{ab}F^{ab}))_1
&=6W_{ab}X^{ab++}-4W^{\alpha\beta\gamma+}W_{\alpha\beta\gamma}^+.
\end{aligned}
\tag{S2-185}
```

The three-spinor sign is the same raised-index contraction that produced $`+4`$ in (S2-178), with the opposite overall coefficient. No three-spinor field has been set to zero.

### 4.36 Completing $`(\Delta X^{--})_1`$

All five contributions in (S2-174) are now known. The following table includes their prefactors, so the entries can be added directly:

| Contribution to $`(\Delta X^{--})_1`$ | $`iW_{ab}X^{ab++}`$ | $`iX^{\alpha+}X_\alpha^+`$ | $`iW^{\alpha\beta\gamma+}W_{\alpha\beta\gamma}^+`$ |
|---|---:|---:|---:|
| $`i(D^{++}\Box W)_1/4`$ | $`3/8`$ | $`5/64`$ | $`-1/32`$ |
| $`-i(D^{++}(W_{ab}F^{ab}))_1/4`$ | $`-3/2`$ | $`0`$ | $`1`$ |
| $`-5i(D^{++}(X^{\alpha+}\lambda_\alpha^-))_1/32`$ | $`-5/16`$ | $`35/32`$ | $`0`$ |
| $`9i(D^{++}(X^{\alpha-}\lambda_\alpha^+))_1/32`$ | $`0`$ | $`0`$ | $`0`$ |
| Last line of (S2-174) | $`31/16`$ | $`-155/64`$ | $`-31/32`$ |
| Sum | $`1/2`$ | $`-5/4`$ | $`0`$ |

The three-spinor square cancels as $`(-1+32-31)/32=0`$. The other two sums are $`(6-24-5+31)/16=1/2`$ and $`(5+70-155)/64=-5/4`$. Therefore

```math
(\Delta X^{--})_1=\tfrac i2W_{ab}X^{ab++}-\tfrac{5i}{4}X^{\alpha+}X_\alpha^+.
\tag{S2-186}
```

This cancellation is essential to obtaining the source field content of the zero-pole sector. It occurs before adding the gaugino-bilinear descendant, so it is separately checkable.

### 4.37 Completing $`(\Delta B^{--})_2`$ with the odd order visible

In (S2-121), $`\Delta\lambda_\rho^-`$ has no scalar $`W`$, so its first term has degree zero. The other two products have a degree-two part obtained by multiplying their degree-one coefficients. By (S2-117) and (S2-49),

```math
\begin{aligned}
(\Delta B^{--})_2={}&-\tfrac14\varepsilon^{\delta\alpha}(-4X_{\alpha\rho}^{++})\varepsilon^{\rho\sigma}(-2W_{\delta\sigma})\\
&+\tfrac1{16}\varepsilon^{\alpha\beta\gamma\delta}\varepsilon^{\rho\sigma}
\big[-\tfrac32\varepsilon_{\alpha\beta}X_\rho^+-\tfrac12\varepsilon_{\alpha\rho}X_\beta^++\tfrac12\varepsilon_{\beta\rho}X_\alpha^+\big]
\big[-\tfrac32\varepsilon_{\gamma\delta}X_\sigma^+-\tfrac12\varepsilon_{\gamma\sigma}X_\delta^++\tfrac12\varepsilon_{\delta\sigma}X_\gamma^+\big].
\end{aligned}
\tag{S2-187}
```

The first line is a product of even descendants. Its factors $`(-1/4)(-4)(-2)=-2`$ multiply a spinor contraction equal to $`-W_{ab}X^{ab++}/2`$, leaving $`+W_{ab}X^{ab++}`$. The second line is a product of odd descendants, in precisely the order inherited from the four derivatives. Expand its nine products before collecting them. In this table each entry is the coefficient of $`X^{\tau+}X_\tau^+`$, including $`\varepsilon^{\alpha\beta\gamma\delta}\varepsilon^{\rho\sigma}/16`$:

| First odd factor / second odd factor | $`-3\varepsilon_{\gamma\delta}X_\sigma^+/2`$ | $`-\varepsilon_{\gamma\sigma}X_\delta^+/2`$ | $`+\varepsilon_{\delta\sigma}X_\gamma^+/2`$ |
|---|---:|---:|---:|
| $`-3\varepsilon_{\alpha\beta}X_\rho^+/2`$ | $`-9/8`$ | $`-3/32`$ | $`-3/32`$ |
| $`-\varepsilon_{\alpha\rho}X_\beta^+/2`$ | $`-3/32`$ | $`1/32`$ | $`1/32`$ |
| $`+\varepsilon_{\beta\rho}X_\alpha^+/2`$ | $`-3/32`$ | $`1/32`$ | $`1/32`$ |

For example the upper-left entry is

```math
\begin{aligned}
\tfrac9{64}\varepsilon^{\alpha\beta\gamma\delta}\varepsilon_{\alpha\beta}\varepsilon_{\gamma\delta}
\varepsilon^{\rho\sigma}X_\rho^+X_\sigma^+
&=\tfrac9{64}(8)\big(-X^{\rho+}X_\rho^+\big)
=-\tfrac98X^{\rho+}X_\rho^+,\\
\varepsilon^{\alpha\beta\gamma\delta}
&=\varepsilon^{\alpha\beta}\varepsilon^{\gamma\delta}
-\varepsilon^{\alpha\gamma}\varepsilon^{\beta\delta}
+\varepsilon^{\alpha\delta}\varepsilon^{\beta\gamma}.
\end{aligned}
\tag{S2-188}
```

For every other entry insert the three products on the last line and contract the displayed metrics, without exchanging the order of the two $`X`$ fields. The four off-diagonal $`-3/32`$ terms come from one $`-3/2`$ factor and one half-weight factor; the four $`+1/32`$ terms come from the lower-right block. Raising the first index gives the same $`\varepsilon^{\rho\sigma}X_\rho^+X_\sigma^+=-X^{\rho+}X_\rho^+`$ sign. The sum is $`(-36-12+4)/32=-11/8`$, so

```math
(\Delta B^{--})_2=W_{ab}X^{ab++}-\tfrac{11}{8}X^{\alpha+}X_\alpha^+.
\tag{S2-189}
```

### 4.38 Adding the last sector and collecting all denominator powers

Insert (S2-186) and (S2-189) into (S2-173), keeping their distinct prefactors:

```math
\begin{aligned}
\left.H^{++}\right|_{W^0}
&=-\tfrac12\big[\tfrac i2W_{ab}X^{ab++}-\tfrac{5i}{4}X^{\alpha+}X_\alpha^+\big]
-\tfrac i8\big[W_{ab}X^{ab++}-\tfrac{11}{8}X^{\alpha+}X_\alpha^+\big]\\
&=-i\big(\tfrac14+\tfrac18\big)W_{ab}X^{ab++}
+i\big(\tfrac58+\tfrac{11}{64}\big)X^{\alpha+}X_\alpha^+.
\end{aligned}
\tag{S2-190}
```

The two coefficients are $`-3i/8`$ and $`51i/64`$. Restoring the arbitrary isotwistor gives the symmetric tensor in (S2-192) under **Final Result**. For the fermion bilinear, $`X^{\alpha i}X_\alpha^j=X^{\alpha j}X_\alpha^i`$: exchanging the odd fields gives one minus sign and exchanging the indices of the antisymmetric spinor metric gives the other. No extra factor accompanies the restoration.

All denominator sectors have now been reduced. The sum has $`(2,7,12,18,14,3,2)`$ written terms at $`W^0,W^{-1},\ldots,W^{-6}`$, for 58 in total. Section 6 collects the complete expression in the source fields. It retains the independently derived **positive** $`W^{-3}`$ gradient-$`X`$ coefficient from (S2-79)–(S2-81); the separate published benchmark retains its printed negative coefficient. The component projection and retained-order checks are recorded in the subsequent construction stages.

## 5. Consistency Checks

### 5.1 Weight and parity

Let the ordered six-spinor operator in (S2-01) be written out with its six factors. C24 (A.1e) gives a contribution $`1/2`$ from commuting $`\mathbb D`$ past each factor. The operator acting on the inhomogeneous shift gives zero:

```math
\mathbb D H_{\log W}^{ij}
=6\left(\frac12\right)H_{\log W}^{ij}
+\frac{3i}{1280}\nabla^{(ij}\nabla^{kl)}\nabla_{kl}(1)
=3H_{\log W}^{ij}.
\tag{S2-24}
```

Thus the **definition** has weight three. Independently, the term ledger checks the weight of each of the 58 source summands. For example, $`W^{-1}\Box X^{ij}`$ has weight $`-1+2+2=3`$, $`W_{ab}X^{abij}`$ has $`1+2=3`$, and the sextic sector has $`-6+6(3/2)=3`$. The seed and sextic calculations display their free $`ij`$ symmetry and even parity. The newly derived $`W^{-4}`$ coefficient has weight three: its two-gaugino numerators have weight $`3+4=7`$, and its $`\lambda^3\nabla\lambda`$ and $`W_{ab}\lambda^4`$ numerators both have weight seven. Multiplication by $`W^{-4}`$ gives three. The complete source polynomial's reality, primarity and linearity have not been independently certified by these checks.

### 5.2 Flat constant-field check of the operator

For this probe only, set the Weyl multiplet and its descendants to zero and take $`F_{ab}`$, $`X^{ij}`$, $`\nabla_aW`$ and $`\lambda_\alpha^i`$ spacetime constant. The vector rules then give

```math
\nabla_\alpha^iW=i\lambda_\alpha^i,\qquad
\nabla_\alpha^i\lambda_\beta^j=-2\varepsilon^{ij}F_{\alpha\beta}
-\varepsilon_{\alpha\beta}X^{ij}-\varepsilon^{ij}(\Gamma^a)_{\alpha\beta}\nabla_aW,
\qquad \nabla_\gamma^k\nabla_\alpha^i\lambda_\beta^j=0.
\tag{S2-25}
```

The last equality follows from S23 (2.13b,c), $`\nabla_a\lambda=0`$, and the flat mixed commutator; it is restricted to this probe. Representing the eight gaugino components by eight exterior-algebra generators preserves every odd interchange. Directly applying the six operators and symmetrizing their SU(2) labels then checks the surviving terms against the source. The reproducible implementation and exact scope are in [the verification script](../../../../../../references/source_evidence/log/results/gauged_full_fermionic_log/scripts/verify_log_step2.py) and [its report](../../../../../../references/source_evidence/log/results/gauged_full_fermionic_log/sources/step2/checks.json). This is an independent algebraic check on a restricted field configuration, not a derivation of the general curved expression.

There is one additional useful scope distinction. The $`W^{-5}`$ sector comes only from the fifth ordinary derivative of the logarithm: four first spinor derivatives of $`W`$ and one second derivative. Its second derivative supplies $`F_{ab}`$, $`X^{ij}`$ or $`\nabla_aW`$; the $`W_{\alpha\beta}W`$ piece instead lowers the pole to $`W^{-4}`$. Thus the general $`W^{-5}`$ coefficients can be tested without higher jets. The verifier separately checks all ten independent components of $`F_{ab}`$, all three of $`X^{ij}`$, all five of $`\nabla_aW`$, and every four-generator Grassmann monomial. This exhausts this sector's coefficient test. The independent hand contractions for this entire sector are now supplied in section 4.7; the coefficient test checks that derivation.

Retained source implementations: [verify_log_step2.py](../../../../../../references/source_evidence/log/results/gauged_full_fermionic_log/scripts/verify_log_step2.py). Their source-relative dependencies and execution limits are described in the [component evidence guide](../../../../../../references/source_evidence/README.md).

The arithmetic keeps Gaussian integer sums until the projector normalization, then compares after clearing that denominator; it does not test commuting numerical spinors. Thirteen constant-field probes pass, and the separate eighteen-component $`W^{-5}`$ basis test passes. These counts and their limited scope are recorded in the JSON report.

For the still more restricted bosonic, constant-$`X`$ probe, only the $`X^3`$ term survives. The six-derivative chain rule has fifteen pairings of three second derivatives. Each second derivative is $`-i\varepsilon_{\alpha\beta}X^{ij}`$, so the common coefficient is

```math
\frac{3i}{1280}\frac{2}{W^3}(-i)^3=-\frac3{640W^3}.
\tag{S2-26}
```

The following table displays all contractions. Positions 1–6 refer to the six derivatives in (S2-01), in their original order. The SU(2) column is the coefficient of $`X^{ij}X^{kl}X_{kl}`$ after the four-index symmetrization; the spinor column includes the three raising metrics from the three derivative pairs. For example, the first row has three traces of four, and its SU(2) factor is $`\frac13(1+\frac12+\frac12)=\frac23`$.

| Pairing | Graded shuffle sign | Spinor contraction | SU(2) factor | Product |
|---|---:|---:|---:|---:|
| $`(12)(34)(56)`$ | $`+1`$ | $`64`$ | $`2/3`$ | $`128/3`$ |
| $`(12)(35)(46)`$ | $`-1`$ | $`16`$ | $`-1/6`$ | $`8/3`$ |
| $`(12)(36)(45)`$ | $`+1`$ | $`-16`$ | $`-1/6`$ | $`8/3`$ |
| $`(13)(24)(56)`$ | $`-1`$ | $`16`$ | $`2/3`$ | $`-32/3`$ |
| $`(13)(25)(46)`$ | $`+1`$ | $`4`$ | $`-1/6`$ | $`-2/3`$ |
| $`(13)(26)(45)`$ | $`-1`$ | $`-4`$ | $`-1/6`$ | $`-2/3`$ |
| $`(14)(23)(56)`$ | $`+1`$ | $`-16`$ | $`2/3`$ | $`-32/3`$ |
| $`(14)(25)(36)`$ | $`-1`$ | $`-4`$ | $`-1/6`$ | $`-2/3`$ |
| $`(14)(26)(35)`$ | $`+1`$ | $`4`$ | $`-1/6`$ | $`-2/3`$ |
| $`(15)(23)(46)`$ | $`-1`$ | $`-4`$ | $`-1/6`$ | $`-2/3`$ |
| $`(15)(24)(36)`$ | $`+1`$ | $`4`$ | $`-1/6`$ | $`-2/3`$ |
| $`(15)(26)(34)`$ | $`-1`$ | $`16`$ | $`-1/6`$ | $`8/3`$ |
| $`(16)(23)(45)`$ | $`+1`$ | $`4`$ | $`-1/6`$ | $`-2/3`$ |
| $`(16)(24)(35)`$ | $`-1`$ | $`-4`$ | $`-1/6`$ | $`-2/3`$ |
| $`(16)(25)(34)`$ | $`+1`$ | $`-16`$ | $`-1/6`$ | $`8/3`$ |

There are four $`8/3`$ rows, two $`-32/3`$ rows and eight $`-2/3`$ rows. Hence

```math
\frac{128+4(8)-2(32)-8(2)}3=\frac{80}3,\qquad
-\frac3{640W^3}\frac{80}3X^{ij}X^{kl}X_{kl}
=-\frac1{8W^3}X^{ij}X^{kl}X_{kl}.
\tag{S2-27}
```

This reproduces that source coefficient from the defining operator on the stated probe. If the **entire** flat vector superfield is constant, its spinor descendants and vector field strength vanish, so $`\nabla_{kl}\log W=0`$ and $`H^{ij}=0`$. Merely taking its lowest scalar component constant would not imply this stronger condition.

### 5.3 Independent checks of the newly displayed reductions

[verify_log_step2_projected.py](../../../../../../references/source_evidence/log/results/gauged_full_fermionic_log/scripts/verify_log_step2_projected.py) evaluates the $`W^{-4}`$ coefficient from (S2-50)–(S2-51), using the derived third vector derivative (S2-49). It checks it against the fourteen source terms **after** that operator-based evaluation. Its [report](../../../../../../references/source_evidence/log/results/gauged_full_fermionic_log/sources/step2/projected_checks.json) distinguishes this completed coefficient check from the later, independently certified full primary.

The verification includes all 171 diagonal and pairwise-polarized choices of the eighteen even jets $`F_{ab}`$, $`X^{ij}`$ and $`\nabla_aW`$, all forty independent odd $`\nabla_a\lambda_\alpha^i`$ generators, and the ten Weyl two-form basis elements. It checks the actual six contractions in (S2-57), the zero identity (S2-58), and the unreduced-to-reduced calculation (S2-45)–(S2-49). Equality uses exact Gaussian dyadic coefficients; no coefficients are fitted to the source polynomial. These tests support the displayed $`W^{-4}`$ hand calculations. The subsequent $`W^{-1}`$ calculation and its checks are recorded separately below.

### 5.4 Independent checks of the completed $`W^{-3}`$ sector

[verify_log_step2_w3.py](../../../../../../references/source_evidence/log/results/gauged_full_fermionic_log/scripts/verify_log_step2_w3.py) evaluates (S2-65) using the displayed descendant reductions. It retains eight gauginos, forty derivative-gaugino components, eight Weyl-spinor components, and forty symmetric three-spinor Weyl components as independent Grassmann generators. It checks all 1,140 degree-three even-jet simplex probes, all eighteen even-field insertions against the forty derivative-gaugino generators, 180 mixed Weyl-two-form probes, fifty uncontracted field-strength derivatives, twenty-five ordered Hessian components, and fifteen auxiliary-gradient components. Thus the checks neither assume a commuting Hessian nor erase a field-strength curl. The complete exterior polynomials in the two Weyl-fermion channels are also checked. All comparisons use exact Gaussian dyadic arithmetic with `==`, not fitted coefficients.

The [individual-contraction checks](../../../../../../references/source_evidence/log/results/gauged_full_fermionic_log/sources/step2/w3_contraction_checks.json) also verify all six rows of (S2-82) and (S2-83), the six auxiliary insertions in (S2-84), the actual odd pairings (S2-94), (S2-97), and all 125 Clifford products in (S2-85). The [W^-3 report](../../../../../../references/source_evidence/log/results/gauged_full_fermionic_log/sources/step2/w3_checks.json) records a PASS for the **definition-derived** coefficient and the one disagreement with the printed expression. The [separate six-derivative calculation](../../../../../../references/source_evidence/log/results/gauged_full_fermionic_log/scripts/verify_log_step2_w3_flat_gradient_x.py) checks all fifteen auxiliary-gradient components directly from (S2-01); ten have nonzero contributions to the selected $`++`$ component and all ten fail the printed sign. Its [report](../../../../../../references/source_evidence/log/results/gauged_full_fermionic_log/sources/step2/w3_flat_gradient_x_checks.json) preserves this distinction.

Each numerator in (S2-99) has weight six: $`X F^2`$ has $`2+2+2`$, $`F\lambda\nabla\lambda`$ has $`2+3/2+1+3/2`$, $`\lambda^2\nabla X`$ has $`3+1+2`$, $`W_{ab}F^{ab}\lambda^2`$ has $`1+2+3`$, and $`X_\alpha\lambda^3`$ has $`3/2+9/2`$. Multiplication by $`W^{-3}`$ gives weight three. Every term is even, has exactly two external symmetric SU(2) indices, and has no unpaired spinor or vector index. Scalar flat constant-superfield limits vanish as before. No reality or primarity claim for a *single denominator sector* is inferred: those transformations mix sectors through the descendants.

### 5.5 Checks of the complete $`W^{-2}`$ sector

[verify_log_step2_w2.py](../../../../../../references/source_evidence/log/results/gauged_full_fermionic_log/scripts/verify_log_step2_w2.py) constructs the twelve unreduced contributions of (S2-101) from the source descendant rules, and compares their sum with the twelve terms in (S2-134). The two sides are separately encoded; no coefficients are fitted. Its [report](../../../../../../references/source_evidence/log/results/gauged_full_fermionic_log/sources/step2/w2_checks.json) records **399 exact comparisons**: 25 ordered Hessian components, 75 scalar-gradient/auxiliary-gradient combinations, 55 Weyl-two-form quadratic polarizations, 30 Weyl-two-form/odd-field probes, 20 field-strength/Weyl-fermion probes, all 50 uncontracted $`\nabla_aW_{bc}`$ components, 30 Weyl-tensor-descendant probes, 100 $`X^{++}W\cdot F`$ cancellation probes, three vector-auxiliary/Weyl-spinor probes, five scalar-gradient/Weyl-spinor cancellation probes, the $`Y`$ channel, four isolated odd-field channels, and one simultaneous nonzero-field probe. The same inputs check the **uncontracted** equality (S2-106), including its symmetric-part cancellation.

Eight gauginos, forty derivative-gaugino components, eight Weyl-spinor components, forty symmetric Weyl three-spinor components and eight $`\Box\lambda`$ components are independent exterior-algebra generators. Thus a comparison checks every Grassmann monomial present in the specified input, not a numerical value assigned to an anticommuting field. Exact Gaussian dyadic coefficients are compared with equality, without a tolerance. The seven traced rows of (S2-119) are also checked for all four free spinor components and all ten independent Weyl-tensor components, giving **308 row checks**.

The [separate contraction verifier](../../../../../../references/source_evidence/log/results/gauged_full_fermionic_log/scripts/verify_log_step2_w2_contractions.py) checks the tables in sections 4.19 and 4.22, including the individual terms before cancellations. Its [report](../../../../../../references/source_evidence/log/results/gauged_full_fermionic_log/sources/step2/w2_contraction_checks.json) records the exact scope. The retained source implementations are:

Retained source implementations: [verify_log_step2_w2.py](../../../../../../references/source_evidence/log/results/gauged_full_fermionic_log/scripts/verify_log_step2_w2.py), [verify_log_step2_w2_contractions.py](../../../../../../references/source_evidence/log/results/gauged_full_fermionic_log/scripts/verify_log_step2_w2_contractions.py). Their source-relative dependencies and execution limits are described in the [component evidence guide](../../../../../../references/source_evidence/README.md).

The weight check uses $`[W]=[W_{ab}]=1`$, $`[\lambda]=[X_\alpha]=[W_{ab}{}^\alpha]=3/2`$, $`[X^{ij}]=[F_{ab}]=[Y]=2`$ and $`[\nabla_a]=1`$. The numerator weights are respectively $`2+3`$, $`2+3`$, $`2+3/2+3/2`$, $`3/2+2+3/2`$, $`5/2+5/2`$, $`1+3/2+5/2`$, $`3+2`$, $`2+3`$, $`2+3/2+3/2`$, $`2+3`$, $`2+3`$, and $`2+3/2+3/2`$: **all are five**. The common $`W^{-2}`$ gives weight three. Each term is Grassmann even, has a symmetric external $`ij`$ pair, and contracts every Lorentz and spinor index. For example $`\lambda^{\alpha i}\lambda_\alpha^j`$ is symmetric in $`i,j`$ because the odd interchange and antisymmetric spinor metric both give a minus sign; the same reasoning applies to the contracted derivative-gaugino bilinear.

Setting the explicit fermion fields to zero gives the bosonic coefficient directly:

```math
\left.H^{ij}\right|_{W^{-2},\mathrm{bosonic}}
=\frac1{2W^2}\big[X^{ij}\Box W+(\nabla^aW)\nabla_aX^{ij}\big].
```

It comes from (S2-123) and (S2-130); the potentially surviving $`X^{ij}W\cdot F`$ terms cancel by (S2-132). In flat superspace with the entire Weyl multiplet zero, the remaining coefficient is

```math
\left.H^{ij}\right|_{W^{-2},\mathrm{flat}}
=\frac1{W^2}\big[\tfrac12X^{ij}\Box W+\tfrac12(\partial^aW)\partial_aX^{ij}
-\tfrac i2\lambda^{\alpha(j}\Box\lambda_\alpha^{i)}-\tfrac i4(\partial^a\lambda^{\alpha i})\partial_a\lambda_\alpha^j\big].
```

This vanishes for spacetime-constant flat component fields, including constant $`F`$ and $`X`$. It does not require those fields to vanish. No integration by parts relates the two gaugino terms in this local-superfield calculation. No equations of motion or component gauge have been used. The full-primary S/K tests and retained-component reality checks are now certified independently; see the current certificate. Linearity is proved from the full projector in (S2-191); a denominator sector by itself is not asserted to form a linear multiplet.

### 5.6 Checks of the complete $`W^{-1}`$ calculation

The source-rule calculation is reproducible in [verify_log_step2_w1.py](../../../../../../references/source_evidence/log/results/gauged_full_fermionic_log/scripts/verify_log_step2_w1.py). It forms $`D^{++}\Box W`$, $`D^{++}(W\cdot F)`$, both Weyl-spinor products, and the five contributions to $`\Delta X^{--}`$ before evaluating the seven contributions in (S2-136). Its separate comparison function supplies the seven printed S23 terms only after this evaluation. The [coefficient report](../../../../../../references/source_evidence/log/results/gauged_full_fermionic_log/sources/step2/w1_checks.json) records **241 passing probes**, testing both the primary coefficient and (S2-165).

The probes include all ten Weyl two-form basis elements, all 55 diagonal and pairwise polarizations of the Weyl-square term, all 100 $`F_{ab}X_{cd}^{++}`$ basis pairings, all 50 uncontracted $`\nabla_aW_{bc}`$ basis elements, all five scalar gradients and all fifteen auxiliary gradients. Fermions and their first derivatives are independent exterior-algebra generators, rather than commuting numerical spinors. The remaining probes separately test $`\Box X`$, $`YX`$, the odd sector with vanishing even fields, and a combined nonzero configuration. The derivative probes explicitly test the absence of residual $`\nabla W_{ab}`$, $`\nabla W`$, and $`\nabla X^{ij}`$ structures in this pole.

The [individual-contraction verifier](../../../../../../references/source_evidence/log/results/gauged_full_fermionic_log/scripts/verify_log_step2_w1_contractions.py) checks the fixed rational entries in the displayed tables against their unreduced contractions. Its [report](../../../../../../references/source_evidence/log/results/gauged_full_fermionic_log/sources/step2/w1_contraction_checks.json) records **1,195 passing row and matrix identities**: 135 rows for $`D^{++}\Box W`$, 75 for $`\Delta X^{--}`$, 105 for the primary contributions, 45 for $`D^{++}(W\cdot F)`$, 615 for the derivative-product/Weyl-spinor/K-trace calculations, and 220 matrix identities. Coefficients are not fitted in these verifiers. The source K curvature is multiplied by 96 before contraction to clear its thirds; the remaining denominator is divided only after exact cancellation of the factors of three. The final polynomial comparisons use exact Gaussian dyadic coefficients.

Retained source implementations: [verify_log_step2_w1.py](../../../../../../references/source_evidence/log/results/gauged_full_fermionic_log/scripts/verify_log_step2_w1.py), [verify_log_step2_w1_contractions.py](../../../../../../references/source_evidence/log/results/gauged_full_fermionic_log/scripts/verify_log_step2_w1_contractions.py). Their source-relative dependencies and execution limits are described in the [component evidence guide](../../../../../../references/source_evidence/README.md).

The seven numerator weights are, in final-result order, $`2+2`$, $`2+2`$, $`2+2`$, $`2+1+1`$, $`1+3/2+3/2`$, $`3/2+1+3/2`$, and $`3/2+1+3/2`$: **all are four**. The common $`W^{-1}`$ leaves weight three. All terms are Grassmann even. All Lorentz and spinor indices are contracted; the external $`ij`$ pair is symmetric because the arbitrary-isotwistor reconstruction selects exactly its symmetric part. $`X^{abij}`$ is the two-form Weyl descendant defined in (S2-07), whereas $`X^{ij}`$ is the vector auxiliary. These must not be identified.

Setting the explicit fermion fields to zero in (S2-172) gives

```math
\left.H^{ij}\right|_{W^{-1},\mathrm{bosonic}}
=W^{-1}\big[\tfrac9{64}YX^{ij}-\tfrac{3i}{8}F_{ab}X^{abij}-\tfrac12\Box X^{ij}-\tfrac9{64}W^{ab}W_{ab}X^{ij}\big].
```

These four coefficients are the first four rows of the addition table in section 4.31. For the flat-superspace limit set the entire Weyl multiplet and its descendants to zero, while keeping the vector multiplet arbitrary. Then

```math
\left.H^{ij}\right|_{W^{-1},\mathrm{flat}}=-\frac1{2W}\partial^a\partial_aX^{ij}.
```

It follows independently from $`(D^{++}\Box W)_0=-4i\Box X^{++}`$: (S2-143) gives $`(\Delta X^{--})_0=\Box X^{++}`$, and the coefficient $`-1/2`$ in (S2-136) gives this flat result. Spacetime-constant flat vector fields therefore give zero at this pole, without requiring constant $`F`$ or $`X`$ to vanish. No integration by parts, auxiliary equation, truncation in fermion order, or gauged substitution enters these identities. Full-primary S/K and retained-component reality are now checked in the independent certificate; those conditions mix denominator sectors and are not proved by this pole calculation alone. Linearity is proved from the full projector in (S2-191).

### 5.7 Checks of the $`W^0`$ sector and the completed coefficient reconstruction

[verify_log_step2_w0.py](../../../../../../references/source_evidence/log/results/gauged_full_fermionic_log/scripts/verify_log_step2_w0.py) evaluates the raw source derivatives in (S2-174) and (S2-187), before comparing the collected answer with the two printed coefficients. Its [report](../../../../../../references/source_evidence/log/results/gauged_full_fermionic_log/sources/step2/w0_checks.json) records **152 passing probes**, including all 100 two-form pairings $`W_{ab}X_{cd}^{++}`$ and all 50 uncontracted first derivatives $`\nabla_aX_{bc}^{++}`$. The latter verify their cancellation without assuming a restricted background. The Weyl spinor and all twenty independent components of the symmetric Weyl three-spinor remain independent exterior generators in each probe. The fixed intermediate tables pass 3,192 row checks; the extra $`\Box\lambda`$ and $`WF`$ subdivisions pass 912 checks, and all nine entries of the odd-product table pass separately. These checks use the displayed source rules and exact polynomial equality; they do not solve for coefficients by fitting the source result.

Retained source implementations: [verify_log_step2_w0.py](../../../../../../references/source_evidence/log/results/gauged_full_fermionic_log/scripts/verify_log_step2_w0.py). Their source-relative dependencies and execution limits are described in the [component evidence guide](../../../../../../references/source_evidence/README.md).

The two final terms have weight $`1+2=3`$ and $`3/2+3/2=3`$. Their external $`ij`$ indices are symmetric; all Lorentz and spinor indices are paired. The zero-pole fermion bilinear is Grassmann even, and its SU(2) symmetry was proved below (S2-190). The intermediate three-spinor square has the same weight but cancels with coefficients $`-1/32+1-31/32=0`$. No derivative, field equation or boundary term was used to discard it.

The zero-pole bosonic restriction is $`-3iW_{ab}X^{abij}/8`$, obtained by setting explicit fermion fields to zero in (S2-192). It agrees with the first bosonic term of S23 (3.25). If the entire Weyl multiplet vanishes, the zero-pole coefficient vanishes; this is also immediate from the two source-driven descendants (S2-186), (S2-189), each of which then vanishes. This flat-Weyl limit is a check on the sector, not an imposed condition on the general calculation.

There is now also a short exact proof of the linear constraint **from the reconstructed projector representation**. C24 (A.2a–d) makes every spinor anticommutator coefficient proportional to $`\varepsilon^{ij}`$. Thus, for arbitrary constant $`u_i^+`$,

```math
\begin{aligned}
\{D_\alpha,D_\beta\}&=u_i^+u_j^+\{\nabla_\alpha^i,\nabla_\beta^j\}=0,\\
D_\eta\Delta
&=-\tfrac1{96}\varepsilon^{\alpha\beta\gamma\delta}
D_\eta D_\alpha D_\beta D_\gamma D_\delta=0,\\
D_\eta H^{++}
&=-\tfrac12(D_\eta\Delta)(W^{-1}X^{--})
-\tfrac i8(D_\eta\Delta)(W^{-2}B^{--})=0,\\
0=u_i^+u_j^+u_k^+\nabla_\eta^iH^{jk}\quad\text{for every }u^+\quad
&\Longrightarrow\quad\nabla_\eta^{(i}H^{jk)}=0.
\end{aligned}
\tag{S2-191}
```

The second line contains five anticommuting derivatives but only four spinor labels. Every ordered word therefore has a repeated derivative; commuting the repetition next to itself gives $`D_\alpha^2=0`$. The verifier checks this repeated-index condition in all 96 words before summation. No anticommutator has been approximated by its flat-space part. This proof uses the exact equivalence of the collected polynomial to (S2-31), established by the pole calculations; it is not an additional term-by-term differentiation of the full 58-term polynomial. That distinction matters when judging the independence of the verification.

The full coefficient ledger is [primary_derived_term_ledger.json](../../../../../../references/source_evidence/log/results/gauged_full_fermionic_log/sources/step2/primary_derived_term_ledger.json). Each of its 58 terms points to its hand derivation. [verify_log_step2_collection.py](../../../../../../references/source_evidence/log/results/gauged_full_fermionic_log/scripts/verify_log_step2_collection.py) checks that every derived term appears in the final full expression and that the sole change from the separate literal source ledger is the previously established sign of H3.9. Its [report](../../../../../../references/source_evidence/log/results/gauged_full_fermionic_log/sources/step2/collection_checks.json) checks collection and provenance, not new physics identities. The weight and parity checks apply to all 58 terms; changing that one sign does not alter either property.

### 5.8 Checks still required

Full-primary defining-projector equality and curved S/K/linearity now pass. Project-frame projection, canonicalization, reality, current conservation and BF construction are certified through the retained order in [the current certificate](CERTIFICATION_LOG_TWO_FERMI_2026-09-25.md). The conservation and supersymmetry conclusions use verified multiplet premises and the complete superform proof; a separate brute-force variation of all expanded terms is not claimed. No boundary term was discarded, auxiliary field eliminated, or gauged/gauge-fixed equation used.

## 6. Final Result

### 6.1 Complete, independently derived $`W^0`$ result

Under A1–A4, (S2-173)–(S2-190) give the two remaining terms together:

```math
\boxed{\left.H_{\log W}^{ij}\right|_{W^0}=-\frac{3i}{8}W_{ab}X^{abij}+\frac{51i}{64}X^{\alpha i}X_\alpha^j.}
\tag{S2-192}
```

Both agree with S23 (3.25). The coefficient $`51/64=5/8+11/64`$ receives contributions from **both** descendants in (S2-173). The two-form coefficient is $`-3/8=-1/4-1/8`$. This is a local off-shell superfield equality in the source frame, with no gauge or fermion-order restriction.

### 6.2 Complete, independently derived $`W^{-1}`$ result

Under A1–A4, (S2-135)–(S2-171) give all seven terms, with their symmetric SU(2) indices restored:

```math
\boxed{\begin{aligned}
\left.H_{\log W}^{ij}\right|_{W^{-1}}=W^{-1}\Big\{&\tfrac9{64}X^{ij}Y-\tfrac{3i}{8}F_{ab}X^{abij}-\tfrac12\Box X^{ij}\\
&-\tfrac9{64}X^{ij}W^{ab}W_{ab}+\tfrac14W^{ab}W_{ab}^{\alpha(i}\lambda_\alpha^{j)}\\
&-\tfrac34(\Gamma^a)^{\alpha\beta}X_\alpha^{(i}\nabla_a\lambda_\beta^{j)}+\tfrac34(\Gamma^a)^{\alpha\beta}\lambda_\alpha^{(i}\nabla_aX_\beta^{j)}\Big\}.
\end{aligned}}
\tag{S2-172}
```

This is an exact local coefficient of the off-shell, gauge-unfixed LOG primary in the locked Gold superspace conventions. It agrees with all seven $`W^{-1}`$ terms of S23 (3.25). The three explicit fermion bilinears are included; the covariant derivatives also retain their fermionic connections. The two different derivative bilinears remain separately visible because no integration by parts is allowed in a local multiplet component. This equation is the superspace coefficient, before bar projection and the later gauged substitutions.

### 6.3 Complete, independently derived $`W^{-2}`$ result

Under A1–A4, restoring the symmetric $`ij`$ indices in (S2-122)–(S2-133) gives all twelve terms:

```math
\boxed{\begin{aligned}
\left.H_{\log W}^{ij}\right|_{W^{-2}}=W^{-2}\Big\{&
\tfrac12X^{ij}\Box W+\tfrac12(\nabla^aW)\nabla_aX^{ij}+\tfrac14F^{ab}W_{ab}^{\alpha(i}\lambda_\alpha^{j)}\\
&-\tfrac i2\lambda^{\alpha(j}\Box\lambda_\alpha^{i)}-\tfrac i4(\nabla^a\lambda^{\alpha i})\nabla_a\lambda_\alpha^j
-\tfrac{3i}{16}\varepsilon^{abcde}(\Sigma_{ab})^{\alpha\beta}W_{de}\lambda_\alpha^{(i}\nabla_c\lambda_\beta^{j)}\\
&-\tfrac{3i}{8}(\Gamma^a)^{\alpha\beta}\lambda_\alpha^i\lambda_\beta^j\nabla^cW_{ac}
+\tfrac{3i}{64}Y\lambda^{\alpha i}\lambda_\alpha^j
+\tfrac38(\Sigma_{ab})^{\alpha\beta}F^{ab}X_\alpha^{(i}\lambda_\beta^{j)}\\
&+\tfrac{3i}{128}W^{ab}W_{ab}\lambda^{\alpha i}\lambda_\alpha^j
+\tfrac{9i}{256}\varepsilon^{abcde}(\Gamma_a)^{\alpha\beta}W_{bc}W_{de}\lambda_\alpha^i\lambda_\beta^j
-\tfrac38X^{ij}X^{\alpha k}\lambda_{\alpha k}\Big\}.
\end{aligned}}
\tag{S2-134}
```

This is a local off-shell identity in the locked Gold superspace conventions. Every term, including the two bosonic terms, comes from the operator calculation above. The result agrees term by term with the $`W^{-2}`$ sector of S23 (3.25). The derivatives retain their full superconformal connections. Neither the bar projection nor a gauged substitution is included in this equality.

### 6.4 Unchanged published comparison

The pole endpoints are (S2-192), (S2-172), (S2-134), (S2-99), (S2-63), (S2-43), and (S2-23), in increasing denominator order. Their full sum is (S2-193) below. The source expression here is retained to make the one audited sign difference inspectable.

For a complete visible comparison, the following is **the full published S23 (3.25)** in the original source fields. It has $`(2,7,12,18,14,3,2)`$ summands at powers $`W^0,\ldots,W^{-6}`$, respectively. No terms are hidden in named coefficient polynomials, and each displayed row groups several terms. Its exact term ledger is [primary_term_ledger.json](../../../../../../references/source_evidence/log/results/gauged_full_fermionic_log/sources/step2/primary_term_ledger.json).

<!-- FULL_PRIMARY_BENCHMARK_BEGIN -->
```math
\begin{aligned}
H_{\log W}^{ij}={}&-\frac{3i}{8}W_{ab}X^{abij}+\frac{51i}{64}X^{\alpha i}X_\alpha^j\\
&+W^{-1}\Bigl\{\frac9{64}X^{ij}Y-\frac{3i}{8}F_{ab}X^{abij}-\frac12\Box X^{ij}\\
&\qquad -\frac9{64}X^{ij}W^{ab}W_{ab}+\frac14W^{ab}W_{ab}^{\alpha(i}\lambda_\alpha^{j)}\\
&\qquad -\frac34(\Gamma^a)^{\alpha\beta}X_\alpha^{(i}\nabla_a\lambda_\beta^{j)}+\frac34(\Gamma^a)^{\alpha\beta}\lambda_\alpha^{(i}\nabla_aX_\beta^{j)}\Bigr\}\\
&+W^{-2}\Bigl\{\frac12X^{ij}\Box W+\frac12(\nabla^aW)\nabla_aX^{ij}+\frac14F^{ab}W_{ab}^{\alpha(i}\lambda_\alpha^{j)}\\
&\qquad -\frac i2\lambda^{\alpha(j}\Box\lambda_\alpha^{i)}-\frac i4(\nabla^a\lambda^{\alpha i})\nabla_a\lambda_\alpha^j-\frac{3i}{16}\varepsilon^{abcde}(\Sigma_{ab})^{\alpha\beta}W_{de}\lambda_\alpha^{(i}\nabla_c\lambda_\beta^{j)}\\
&\qquad -\frac{3i}{8}(\Gamma^a)^{\alpha\beta}\lambda_\alpha^i\lambda_\beta^j\nabla^cW_{ac}+\frac{3i}{64}Y\lambda^{\alpha i}\lambda_\alpha^j+\frac38(\Sigma_{ab})^{\alpha\beta}F^{ab}X_\alpha^{(i}\lambda_\beta^{j)}\\
&\qquad +\frac{3i}{128}W^{ab}W_{ab}\lambda^{\alpha i}\lambda_\alpha^j+\frac{9i}{256}\varepsilon^{abcde}(\Gamma_a)^{\alpha\beta}W_{bc}W_{de}\lambda_\alpha^i\lambda_\beta^j-\frac38X^{ij}X^{\alpha k}\lambda_{\alpha k}\Bigr\}\\
&+W^{-3}\Bigl\{\frac18X^{ij}F^{ab}F_{ab}-\frac18X^{ij}X^{kl}X_{kl}-\frac14X^{ij}(\nabla^aW)\nabla_aW\\
&\qquad -\frac i8\varepsilon^{abcde}(\Sigma_{ab})^{\alpha\beta}F_{de}\lambda_\alpha^{(i}\nabla_c\lambda_\beta^{j)}-\frac i4(\Gamma^a)^{\alpha\beta}F_{ab}\lambda_\alpha^{(i}\nabla^b\lambda_\beta^{j)}\\
&\qquad -\frac i4(\Gamma^a)^{\alpha\beta}\lambda_\alpha^i\lambda_\beta^j\nabla^cF_{ac}+\frac i4(\Gamma^a)^{\alpha\beta}X^{ij}\lambda_\alpha^k\nabla_a\lambda_{\beta k}\\
&\qquad +\frac i4(\Gamma^a)^{\alpha\beta}X^{k(i}\lambda_\alpha^{j)}\nabla_a\lambda_{\beta k}-\frac i4(\Gamma^a)^{\alpha\beta}\lambda_\alpha^{(i}(\nabla_aX^{j)l})\lambda_{\beta l}+\frac i4\lambda^{\alpha i}\lambda_\alpha^j\Box W\\
&\qquad +\frac{3i}{4}(\nabla^aW)\lambda^{\alpha(i}\nabla_a\lambda_\alpha^{j)}-\frac i2(\Sigma_{ab})^{\alpha\beta}(\nabla^aW)\lambda_\alpha^{(i}\nabla^b\lambda_\beta^{j)}\\
&\qquad -\frac{3i}{16}(\Gamma^a)^{\alpha\beta}W_{ab}\lambda_\alpha^i\lambda_\beta^j\nabla^bW+\frac{3i}{32}W_{ab}F^{ab}\lambda^{\alpha i}\lambda_\alpha^j\\
&\qquad +\frac{9i}{64}\varepsilon^{abcde}(\Gamma_a)^{\alpha\beta}W_{bc}F_{de}\lambda_\alpha^i\lambda_\beta^j-\frac{3i}{32}(\Sigma_{ab})^{\alpha\beta}X^{ij}W^{ab}\lambda_\alpha^k\lambda_{\beta k}\\
&\qquad -\frac{3i}{8}X^{\alpha k}\lambda_\alpha^{(i}\lambda^{\beta j)}\lambda_{\beta k}-\frac{3i}{8}X^{\alpha k}\lambda^{\beta i}\lambda_\beta^j\lambda_{\alpha k}\Bigr\}\\
&+W^{-4}\Bigl\{-\frac{3i}{16}\lambda^{\alpha i}\lambda_\alpha^j(\nabla^aW)\nabla_aW-\frac{3i}{8}(\Gamma^a)^{\alpha\beta}X^{k(i}\lambda_\alpha^{j)}\lambda_{\beta k}\nabla_aW\\
&\qquad +\frac{3i}{8}(\Gamma^a)^{\alpha\beta}F_{ab}\lambda_\alpha^i\lambda_\beta^j\nabla^bW+\frac{3i}{32}F^{ab}F_{ab}\lambda^{\alpha i}\lambda_\alpha^j\\
&\qquad +\frac{3i}{64}\varepsilon^{abcde}(\Gamma_a)^{\alpha\beta}F_{bc}F_{de}\lambda_\alpha^i\lambda_\beta^j-\frac{3i}{16}(\Sigma_{ab})^{\alpha\beta}X^{ij}F^{ab}\lambda_\alpha^k\lambda_{\beta k}\\
&\qquad -\frac{3i}{16}X^{ij}X^{kl}\lambda_k^\alpha\lambda_{\alpha l}-\frac{3i}{32}X^{kl}X_{kl}\lambda^{\alpha i}\lambda_\alpha^j-\frac{15}{64}(\Gamma^a)^{\alpha\beta}\lambda_\alpha^i\lambda_\beta^j\lambda^{\gamma k}\nabla_a\lambda_{\gamma k}\\
&\qquad -\frac9{32}(\Gamma^a)^{\alpha\beta}\lambda_\alpha^{(i}\lambda^{\rho j)}\lambda_\beta^k\nabla_a\lambda_{\rho k}-\frac{15}{32}(\Gamma^a)^{\alpha\beta}\lambda_\alpha^{(i}\lambda^{\rho j)}\lambda_\rho^k\nabla_a\lambda_{\beta k}\\
&\qquad -\frac{15}{64}(\Gamma^a)^{\alpha\beta}\lambda^{\rho i}\lambda_\rho^j\lambda_\alpha^k\nabla_a\lambda_{\beta k}+\frac9{32}(\Sigma_{ab})^{\alpha\beta}W^{ab}\lambda_\alpha^{(i}\lambda^{\rho j)}\lambda_\beta^k\lambda_{\rho k}\\
&\qquad +\frac9{64}(\Sigma_{ab})^{\alpha\beta}W^{ab}\lambda^{\rho i}\lambda_\rho^j\lambda_\alpha^k\lambda_{\beta k}\Bigr\}\\
&+W^{-5}\Bigl\{\frac38(\Gamma^a)^{\alpha\beta}\lambda_\alpha^{(i}\lambda^{\rho j)}\lambda_\beta^k\lambda_{\rho k}\nabla_aW+\frac38(\Sigma_{ab})^{\alpha\beta}F^{ab}\lambda^{\rho i}\lambda_\rho^j\lambda_\alpha^k\lambda_{\beta k}\\
&\qquad +\frac38X^{kl}\lambda^{\alpha i}\lambda_\alpha^j\lambda_k^\beta\lambda_{\beta l}\Bigr\}\\
&+W^{-6}\Bigl\{\frac{3i}{32}\lambda^{\alpha i}\lambda_\alpha^j\lambda^{\beta k}\lambda_\beta^l\lambda_k^\gamma\lambda_{\gamma l}+\frac{3i}{16}\lambda^{\alpha i}\lambda_\alpha^k\lambda^{\beta j}\lambda_\beta^l\lambda_k^\gamma\lambda_{\gamma l}\Bigr\}.
\end{aligned}
\tag{S2-BENCHMARK}
```
<!-- FULL_PRIMARY_BENCHMARK_END -->

## 7. Convention Dependence and Remaining Uncertainties

The source comparison and the definition-derived result retain Gold's fields, epsilon, spinor order and full superconformal $`\Box`$. The final derived expression (S2-193) contains all 58 terms, including all explicit fermion degrees; its unexpanded covariant derivatives retain fermionic connection terms. It differs from the unchanged printed comparison by the audited $`W^{-3}`$ gradient-$`X`$ sign only. Neither expression is yet the gauged invariant action.

The coefficient reconstruction is complete. The subsequent Step 6 construction performs the bar projection with C24 (2.15)–(2.16), including all projected connections, and comparison with C24 (4.8a). The full-primary S/K checks and retained-component reality/projection checks are now recorded in the current certificate. The existing bridge gives $`L_{\log}^{ij}=-2H_{\log W}^{ij}|`$ in the component ledger's normalization; no projection or gauged substitution has been used to bypass a superspace coefficient calculation here.

The gradient-$`X`$ discrepancy remains distinct from the earlier scalar-descendant discrepancy, curvature-sector correction, and step-1 BF current/form conflict. Each retains its documented scope. Completing the 58 coefficients and proving linearity from the projector do not close those separate source-reconciliation or nonlinear-invariant gates.

## 8. Complete collected result: all 58 terms

The sum of the seven derived sectors is the following complete superspace polynomial. Every source field is displayed, with several summands on each row and no hidden coefficient function. **The $`W^{-3}`$ gradient-$`X`$ term carries $`+i/4`$**, as independently derived in (S2-79)–(S2-81). The equality below records the coefficient reconstruction from (S2-01); it is not a claim that the subsequent component action or its nonlinear supersymmetry has been verified.

The formula has Weyl weight three and a symmetric external $`ij`$ pair. Its linear constraint follows from (S2-191). The symbols and all derivative connections retain their definitions in sections 2–3. It is valid locally for $`W>0`$, off shell, with all fermion degrees retained and with no integrations by parts. The factor $`W^{-n}`$ labels an exact denominator sector, not a perturbation series or fermion truncation. Section 7 gives the component projection and its checks.

<!-- FULL_PRIMARY_DERIVED_BEGIN -->
```math
\boxed{\begin{aligned}
H_{\log W}^{ij}={}&-\frac{3i}{8}W_{ab}X^{abij}+\frac{51i}{64}X^{\alpha i}X_\alpha^j\\
&+W^{-1}\Bigl\{\frac9{64}X^{ij}Y-\frac{3i}{8}F_{ab}X^{abij}-\frac12\Box X^{ij}\\
&\qquad -\frac9{64}X^{ij}W^{ab}W_{ab}+\frac14W^{ab}W_{ab}^{\alpha(i}\lambda_\alpha^{j)}\\
&\qquad -\frac34(\Gamma^a)^{\alpha\beta}X_\alpha^{(i}\nabla_a\lambda_\beta^{j)}+\frac34(\Gamma^a)^{\alpha\beta}\lambda_\alpha^{(i}\nabla_aX_\beta^{j)}\Bigr\}\\
&+W^{-2}\Bigl\{\frac12X^{ij}\Box W+\frac12(\nabla^aW)\nabla_aX^{ij}+\frac14F^{ab}W_{ab}^{\alpha(i}\lambda_\alpha^{j)}\\
&\qquad -\frac i2\lambda^{\alpha(j}\Box\lambda_\alpha^{i)}-\frac i4(\nabla^a\lambda^{\alpha i})\nabla_a\lambda_\alpha^j-\frac{3i}{16}\varepsilon^{abcde}(\Sigma_{ab})^{\alpha\beta}W_{de}\lambda_\alpha^{(i}\nabla_c\lambda_\beta^{j)}\\
&\qquad -\frac{3i}{8}(\Gamma^a)^{\alpha\beta}\lambda_\alpha^i\lambda_\beta^j\nabla^cW_{ac}+\frac{3i}{64}Y\lambda^{\alpha i}\lambda_\alpha^j+\frac38(\Sigma_{ab})^{\alpha\beta}F^{ab}X_\alpha^{(i}\lambda_\beta^{j)}\\
&\qquad +\frac{3i}{128}W^{ab}W_{ab}\lambda^{\alpha i}\lambda_\alpha^j+\frac{9i}{256}\varepsilon^{abcde}(\Gamma_a)^{\alpha\beta}W_{bc}W_{de}\lambda_\alpha^i\lambda_\beta^j-\frac38X^{ij}X^{\alpha k}\lambda_{\alpha k}\Bigr\}\\
&+W^{-3}\Bigl\{\frac18X^{ij}F^{ab}F_{ab}-\frac18X^{ij}X^{kl}X_{kl}-\frac14X^{ij}(\nabla^aW)\nabla_aW\\
&\qquad -\frac i8\varepsilon^{abcde}(\Sigma_{ab})^{\alpha\beta}F_{de}\lambda_\alpha^{(i}\nabla_c\lambda_\beta^{j)}-\frac i4(\Gamma^a)^{\alpha\beta}F_{ab}\lambda_\alpha^{(i}\nabla^b\lambda_\beta^{j)}\\
&\qquad -\frac i4(\Gamma^a)^{\alpha\beta}\lambda_\alpha^i\lambda_\beta^j\nabla^cF_{ac}+\frac i4(\Gamma^a)^{\alpha\beta}X^{ij}\lambda_\alpha^k\nabla_a\lambda_{\beta k}\\
&\qquad +\frac i4(\Gamma^a)^{\alpha\beta}X^{k(i}\lambda_\alpha^{j)}\nabla_a\lambda_{\beta k}+\frac i4(\Gamma^a)^{\alpha\beta}\lambda_\alpha^{(i}(\nabla_aX^{j)l})\lambda_{\beta l}+\frac i4\lambda^{\alpha i}\lambda_\alpha^j\Box W\\
&\qquad +\frac{3i}{4}(\nabla^aW)\lambda^{\alpha(i}\nabla_a\lambda_\alpha^{j)}-\frac i2(\Sigma_{ab})^{\alpha\beta}(\nabla^aW)\lambda_\alpha^{(i}\nabla^b\lambda_\beta^{j)}\\
&\qquad -\frac{3i}{16}(\Gamma^a)^{\alpha\beta}W_{ab}\lambda_\alpha^i\lambda_\beta^j\nabla^bW+\frac{3i}{32}W_{ab}F^{ab}\lambda^{\alpha i}\lambda_\alpha^j\\
&\qquad +\frac{9i}{64}\varepsilon^{abcde}(\Gamma_a)^{\alpha\beta}W_{bc}F_{de}\lambda_\alpha^i\lambda_\beta^j-\frac{3i}{32}(\Sigma_{ab})^{\alpha\beta}X^{ij}W^{ab}\lambda_\alpha^k\lambda_{\beta k}\\
&\qquad -\frac{3i}{8}X^{\alpha k}\lambda_\alpha^{(i}\lambda^{\beta j)}\lambda_{\beta k}-\frac{3i}{8}X^{\alpha k}\lambda^{\beta i}\lambda_\beta^j\lambda_{\alpha k}\Bigr\}\\
&+W^{-4}\Bigl\{-\frac{3i}{16}\lambda^{\alpha i}\lambda_\alpha^j(\nabla^aW)\nabla_aW-\frac{3i}{8}(\Gamma^a)^{\alpha\beta}X^{k(i}\lambda_\alpha^{j)}\lambda_{\beta k}\nabla_aW\\
&\qquad +\frac{3i}{8}(\Gamma^a)^{\alpha\beta}F_{ab}\lambda_\alpha^i\lambda_\beta^j\nabla^bW+\frac{3i}{32}F^{ab}F_{ab}\lambda^{\alpha i}\lambda_\alpha^j\\
&\qquad +\frac{3i}{64}\varepsilon^{abcde}(\Gamma_a)^{\alpha\beta}F_{bc}F_{de}\lambda_\alpha^i\lambda_\beta^j-\frac{3i}{16}(\Sigma_{ab})^{\alpha\beta}X^{ij}F^{ab}\lambda_\alpha^k\lambda_{\beta k}\\
&\qquad -\frac{3i}{16}X^{ij}X^{kl}\lambda_k^\alpha\lambda_{\alpha l}-\frac{3i}{32}X^{kl}X_{kl}\lambda^{\alpha i}\lambda_\alpha^j-\frac{15}{64}(\Gamma^a)^{\alpha\beta}\lambda_\alpha^i\lambda_\beta^j\lambda^{\gamma k}\nabla_a\lambda_{\gamma k}\\
&\qquad -\frac9{32}(\Gamma^a)^{\alpha\beta}\lambda_\alpha^{(i}\lambda^{\rho j)}\lambda_\beta^k\nabla_a\lambda_{\rho k}-\frac{15}{32}(\Gamma^a)^{\alpha\beta}\lambda_\alpha^{(i}\lambda^{\rho j)}\lambda_\rho^k\nabla_a\lambda_{\beta k}\\
&\qquad -\frac{15}{64}(\Gamma^a)^{\alpha\beta}\lambda^{\rho i}\lambda_\rho^j\lambda_\alpha^k\nabla_a\lambda_{\beta k}+\frac9{32}(\Sigma_{ab})^{\alpha\beta}W^{ab}\lambda_\alpha^{(i}\lambda^{\rho j)}\lambda_\beta^k\lambda_{\rho k}\\
&\qquad +\frac9{64}(\Sigma_{ab})^{\alpha\beta}W^{ab}\lambda^{\rho i}\lambda_\rho^j\lambda_\alpha^k\lambda_{\beta k}\Bigr\}\\
&+W^{-5}\Bigl\{\frac38(\Gamma^a)^{\alpha\beta}\lambda_\alpha^{(i}\lambda^{\rho j)}\lambda_\beta^k\lambda_{\rho k}\nabla_aW+\frac38(\Sigma_{ab})^{\alpha\beta}F^{ab}\lambda^{\rho i}\lambda_\rho^j\lambda_\alpha^k\lambda_{\beta k}\\
&\qquad +\frac38X^{kl}\lambda^{\alpha i}\lambda_\alpha^j\lambda_k^\beta\lambda_{\beta l}\Bigr\}\\
&+W^{-6}\Bigl\{\frac{3i}{32}\lambda^{\alpha i}\lambda_\alpha^j\lambda^{\beta k}\lambda_\beta^l\lambda_k^\gamma\lambda_{\gamma l}+\frac{3i}{16}\lambda^{\alpha i}\lambda_\alpha^k\lambda^{\beta j}\lambda_\beta^l\lambda_k^\gamma\lambda_{\gamma l}\Bigr\}.
\end{aligned}}
\tag{S2-193}
```
<!-- FULL_PRIMARY_DERIVED_END -->
