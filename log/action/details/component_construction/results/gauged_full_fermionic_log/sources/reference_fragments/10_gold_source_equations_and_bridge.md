## Gold source equations and the Bergshoeff component-convention bridge

This reference gives the source equations and the published convention bridge.

<!-- ASSERT_CONVENTION: source_priority=local Sources PDFs before external literature, source_frame=Gold traceless Standard-Weyl superspace, conversion_target=Bergshoeff component frame only through explicit C24 Appendix C tables -->

This note preserves Gold source notation. A superscript `G` or `B` is added only in the bridge to distinguish the Gold and Bergshoeff frames. These superscripts are labels, not indices. At extraction start the inherited project `convention_lock` contained generic placeholders; the scoped existing project component locks are the comparison target, and this extraction does not replace them. Fourier transforms, state normalization, and quantum regularization do not enter this classical source extraction.

## Sources and scope

| ID | Local source | Version and page convention |
|---|---|---|
| S23 | [Gold et al., superspace paper](../../../../EXTERNAL_REFERENCES.md#ref-5eaee0fce8c8) | arXiv:2302.14295v2. `PDF n` means the one-based page in this local file; printed page is usually `n-1`. |
| C24 | [Gold et al., component paper and supplement](../../../../EXTERNAL_REFERENCES.md#ref-a8cbff0d3cc4) | Local combined PDF contains arXiv:2311.00679v1, subsequently published in JHEP 07 (2024) 221. Main printed page is `PDF-1`; supplement printed page is `PDF-99`. |

S23 calls the theory five-dimensional `N=1`; the project uses the older five-dimensional `N=2` nomenclature for the same eight-real-supercharge setting. This is a naming convention, not an extra supersymmetry doubling. The sources use the traceless Standard-Weyl superspace frame. The gauged Dilaton-Weyl substitution is a later operation, not part of S23 (3.24)–(3.27).

**Symbol collisions that must remain explicit.** `W` is the real vector-multiplet scalar superfield; `W_{ab}` or `W_{alpha beta}` is the super-Weyl tensor. `X^{ij}` is the vector triplet, whereas `X_alpha^i`, `X_{alpha beta}^{ij}`, and `Y` are super-Weyl descendants. The source scalar `Y` is not the Bergshoeff vector triplet `Y^{ij}`. `F` is the linear-multiplet scalar, while `F_{ab}` is a vector-multiplet field strength. `G^{ij}` is a generic linear primary and `H_log^{ij}` the composite LOG primary. The constrained linear-multiplet vector is written `mathcal H^a` below, as in the source; it is not the project Dilaton-Weyl three-form `widehat H_{abc}`. The source three-form potential `b_{mnp}` is also different from the dilatation connection `b_m`.

## S23 definitions needed before the LOG primary

All equations in this section are source equations without a Bergshoeff-frame substitution. Tangent indices are `a,b=0,...,4`; spinor indices `alpha,beta=1,...,4`; `i,j=1,2` are `SU(2)` indices. Round/square brackets have unit weight. Spinor ordering and index placement are part of the formula and must not be changed without the source spinor rules.

### Supergeometry and Weyl descendants [S23 (2.1)–(2.5), PDF7–8 / printed6–7]

```math
\begin{aligned}
\nabla_A&=E_A-\tfrac12\Omega_A{}^{ab}M_{ab}-\Phi_A{}^{ij}J_{ij}
-B_A\mathbb D-\mathfrak F_A{}^{\alpha i}S_{\alpha i}-\mathfrak F_A{}^aK_a,\\
[\nabla_A,\nabla_B\}&=-T_{AB}{}^C\nabla_C-\tfrac12R(M)_{AB}{}^{cd}M_{cd}
-R(J)_{AB}{}^{kl}J_{kl}-R(\mathbb D)_{AB}\mathbb D\\
&\quad-R(S)_{AB}{}^{\gamma k}S_{\gamma k}-R(K)_{AB}{}^cK_c,\\
W_{\alpha\beta}&=W_{\beta\alpha},\qquad K_AW_{\alpha\beta}=0,
\qquad\mathbb D W_{\alpha\beta}=W_{\alpha\beta},\\
\nabla_\gamma^kW_{\alpha\beta}
&=\nabla_{(\alpha}^kW_{\beta\gamma)}+\tfrac25\varepsilon_{\gamma(\alpha}\nabla^{\delta k}W_{\beta)\delta},\\
W_{\alpha\beta\gamma}{}^k&:=\nabla_{(\alpha}^kW_{\beta\gamma)},
\qquad X_\alpha{}^i:=\tfrac25\nabla^{\beta i}W_{\beta\alpha},\\
W_{\alpha\beta\gamma\delta}&:=\nabla_{(\alpha}^kW_{\beta\gamma\delta)k},
\quad X_{\alpha\beta}{}^{ij}:=\nabla_{(\alpha}^{(i}X_{\beta)}{}^{j)},
\quad Y:=i\nabla^{\gamma k}X_{\gamma k}.
\end{aligned}
```

The two-form/spinor conversion in S23 footnote4 (PDF8) is

```math
T_{ab}=(\Sigma_{ab})^{\alpha\beta}T_{\alpha\beta},
\qquad T_{\alpha\beta}=\tfrac12(\Sigma^{ab})_{\alpha\beta}T_{ab}.
```

This applies to `W`, `F`, and the corresponding two-form Weyl descendant. It does not identify the scalar `W` with any two-form.

### Generator and spinor-derivative algebra [C24 Appendix A, PDF81–82 / printed80–81]

S23 describes this same traceless frame but delegates the complete algebra to earlier sources. C24 collects it explicitly. The needed generator relations [C24 (A.1)] are

```math
\begin{gathered}
[M_{ab},M_{cd}]=2\eta_{c[a}M_{b]d}-2\eta_{d[a}M_{b]c},\qquad
[M_{ab},\nabla_c]=2\eta_{c[a}\nabla_{b]},\\
M_{\alpha\beta}=\tfrac12(\Sigma^{ab})_{\alpha\beta}M_{ab},\qquad
[M_{\alpha\beta},\nabla_\gamma^i]=\varepsilon_{\gamma(\alpha}\nabla_{\beta)}^i,\\
[J^{ij},J^{kl}]=\varepsilon^{k(i}J^{j)l}+\varepsilon^{l(i}J^{j)k},\qquad
[J^{ij},\nabla_\alpha^k]=\varepsilon^{k(i}\nabla_\alpha^{j)},\\
[\mathbb D,\nabla_a]=\nabla_a,\qquad
[\mathbb D,\nabla_\alpha^i]=\tfrac12\nabla_\alpha^i,\\
[M_{ab},K_c]=2\eta_{c[a}K_{b]},\qquad
[M_{\alpha\beta},S_\gamma^i]=\varepsilon_{\gamma(\alpha}S_{\beta)}^i,
\qquad[J^{ij},S_\alpha^k]=\varepsilon^{k(i}S_\alpha^{j)},\\
[\mathbb D,K_a]=-K_a,\qquad[\mathbb D,S_\alpha^i]=-\tfrac12S_\alpha^i,
\qquad\{S_\alpha^i,S_\beta^j\}=-2i\varepsilon^{ij}(\Gamma^c)_{\alpha\beta}K_c,\\
[K_a,\nabla_b]=2\eta_{ab}\mathbb D+2M_{ab},\qquad
[K_a,\nabla_\alpha^i]=i(\Gamma_a)_\alpha{}^\beta S_\beta^i,\\
\{S_{\alpha i},\nabla_\beta^j\}=2\varepsilon_{\alpha\beta}\delta_i{}^j\mathbb D
-4\delta_i{}^jM_{\alpha\beta}+6\varepsilon_{\alpha\beta}J_i{}^j,\\
[S_{\beta i},\nabla_a]=i(\Gamma_a)_\beta{}^\alpha\nabla_{\alpha i}
-\tfrac14W_a{}^b(\Gamma_b)_\beta{}^\alpha S_{\alpha i}
+\tfrac18(\Gamma_a\Gamma^b)_\beta{}^\gamma X_{\gamma i}K_b
-\tfrac14W_{ab\beta i}K^b.
\end{gathered}
```

**Derived source repair (2026-09-25).** The preceding display preserves literal C24 (A.1l). Its last two K coefficients fail the SDD super-Jacobi identity. With all other locked C24 relations unchanged, the identity requires

```math
[S_{\beta i},\nabla_a]_{\rm consistent}=i(\Gamma_a)_\beta{}^\alpha\nabla_{\alpha i}-\frac14W_a{}^b(\Gamma_b)_\beta{}^\alpha S_{\alpha i}+\frac{i}{8}(\Gamma_a\Gamma^b)_\beta{}^\gamma X_{\gamma i}K_b-\frac{i}{4}W_{ab\beta i}K^b.
\tag{G-C24-A1l-repair}
```

This is a project-derived correction, not a claim of a published erratum. The independent exact test exhausts 122,880 coefficient equations in the linear Weyl-descendant sector: the corrected coefficients pass and the printed coefficients fail. See [source-local Jacobi checks](../../../../../../../../references/source_evidence/log/results/gauged_full_fermionic_log/sources/certification_20260925/curved/jacobi-SDD-checks.json). It affects S acting on vector descendants, even when their elementary parent is K-primary. The scalar/vector reconstruction uses this corrected relation; it does not import the different frame-dependent $`WS`$ coefficient from the older source.

Write `T_{alpha beta}^{ij,c}` and `R_{alpha beta}^{ij,...}` for the slots with the two derivative labels `(alpha,i),(beta,j)`, not for an additional raising of the spinor labels. The full spinor anticommutator is

```math
\{\nabla_\alpha^i,\nabla_\beta^j\}
=-T_{\alpha\beta}^{ij,c}\nabla_c
-\tfrac12R(M)_{\alpha\beta}^{ij,cd}M_{cd}
-R(S)_{\alpha\beta}^{ij,\gamma k}S_{\gamma k}
-R(K)_{\alpha\beta}^{ij,c}K_c,
```

with the only nonzero coefficients [C24 (A.2a–d), PDF82 / printed81]

```math
\begin{aligned}
T_{\alpha\beta}^{ij,c}&=2i\varepsilon^{ij}(\Gamma^c)_{\alpha\beta},\\
R(M)_{\alpha\beta}^{ij,cd}&=2i\varepsilon^{ij}\varepsilon_{\alpha\beta}W^{cd}
+i\varepsilon^{ij}(\Gamma_b)_{\alpha\beta}\widetilde W^{bcd},\\
R(S)_{\alpha\beta}^{ij,\gamma k}&=\tfrac{3i}{4}\varepsilon^{ij}\varepsilon_{\alpha\beta}X^{\gamma k}
+i\varepsilon^{ij}\delta_{[\alpha}{}^\gamma X_{\beta]}{}^k,\\
R(K)_{\alpha\beta}^{ij,c}&=-\tfrac i2\varepsilon^{ij}\varepsilon_{\alpha\beta}\nabla^bW_b{}^c
+\tfrac i2\varepsilon^{ij}(\Gamma^a)_{\alpha\beta}\nabla^d\widetilde W_{da}{}^c
-\tfrac i{32}\varepsilon^{ij}(\Gamma^c)_{\alpha\beta}Y\\
&\quad+\tfrac i4\varepsilon^{ij}\varepsilon_{\alpha\beta}\widetilde W^{cde}W_{de}
+\tfrac i2\varepsilon^{ij}(\Gamma^a)_{\alpha\beta}
\left(W_{ad}W^{cd}-\tfrac3{16}W^{bd}W_{bd}\delta_a{}^c\right).
\end{aligned}
```

Here `widetilde W_{abc}=epsilon_{abcde}W^{de}/2` [C24 (2.19), PDF13 / printed12]. On the primary scalar `log W`, the Lorentz/S/K generators vanish, so the first anticommutator reduces to the torsion term. Once derivatives act, the descendants cease to be primary scalars and the curvature terms must be restored. The source-complete cache of C24 Appendix A also supplies the spinor–vector and vector–vector commutators (A.3)–(A.4), needed when reordering higher derivatives. The explicit towers below already give their required reduced action on the elementary superfields.

### Complete Weyl spinor-derivative tower [S23 (2.6a–f), PDF9 / printed8]

```math
\begin{aligned}
\nabla_\gamma^kW_{\alpha\beta}
&=W_{\alpha\beta\gamma}{}^k+\varepsilon_{\gamma(\alpha}X_{\beta)}{}^k,\qquad\text{(S23-2.6a)}\\
\nabla_\alpha^iX_\beta^j
&=X_{\alpha\beta}{}^{ij}+\tfrac i8\varepsilon^{ij}\varepsilon_{\alpha\beta}Y
-\tfrac{3i}{2}\varepsilon^{ij}(\Gamma^a)_\alpha{}^\rho\nabla_aW_{\beta\rho}
-2i\varepsilon^{ij}W_\alpha{}^\rho W_{\beta\rho}\\
&\quad+\tfrac i2\varepsilon^{ij}\varepsilon_{\alpha\beta}W^{\gamma\delta}W_{\gamma\delta}
-\tfrac i2\varepsilon^{ij}(\Gamma^a)_\beta{}^\rho\nabla_aW_{\alpha\rho},\qquad\text{(S23-2.6b)}\\
\nabla_\alpha^iW_{\beta\gamma\lambda}{}^j
&=-\tfrac12\varepsilon^{ij}\left(W_{\alpha\beta\gamma\lambda}
+3i(\Gamma^a)_{\alpha(\beta}\nabla_aW_{\gamma\lambda)}
+3i\varepsilon_{\alpha(\beta}(\Gamma^a)_\gamma{}^\tau\nabla_aW_{\lambda)\tau}\right)
-\tfrac32\varepsilon_{\alpha(\beta}X_{\gamma\lambda)}{}^{ij},\qquad\text{(S23-2.6c)}\\
\nabla_\alpha^iW_{\beta\gamma\lambda\rho}
&=-4i(\Gamma^a)_{\alpha(\beta}\nabla_aW_{\gamma\lambda\rho)}{}^i
-6iW_{\alpha(\beta\gamma}{}^iW_{\lambda\rho)}
+6iW_{\alpha(\beta}W_{\gamma\lambda\rho)}{}^i\\
&\quad+6i\varepsilon_{\alpha(\beta}\left(W_{\gamma\lambda}X_{\rho)}{}^i
-2(\Gamma^a)_\gamma{}^\tau\nabla_aW_{\lambda\rho)\tau}{}^i
-W_\gamma{}^\tau W_{\lambda\rho)\tau}{}^i\right),\qquad\text{(S23-2.6d)}\\
\nabla_\alpha^iX_{\beta\gamma}{}^{jk}
&=i\varepsilon^{i(j}\Big(-3W_{(\beta}{}^\lambda W_{\gamma)\alpha\lambda}{}^{k)}
-\varepsilon_{\alpha(\beta}W^{\rho\tau}W_{\gamma)\rho\tau}{}^{k)}
-W_{\alpha\lambda}W_{\beta\gamma}{}^{\lambda k)}-\tfrac32W_{\beta\gamma}X_\alpha{}^{k)}\\
&\qquad+\tfrac12W_{\alpha(\beta}X_{\gamma)}{}^{k)}
+\tfrac32\varepsilon_{\alpha(\beta}W_{\gamma)\lambda}X^{k)\lambda}
+2(\Gamma^a)_\alpha{}^\rho\nabla_aW_{\beta\gamma\rho}{}^{k)}\\
&\qquad+2(\Gamma^a)_{(\beta}{}^\rho\nabla_aW_{\gamma)\alpha\rho}{}^{k)}
-(\Gamma^a)_{\alpha(\beta}\nabla_aX_{\gamma)}{}^{k)}
+\varepsilon_{\alpha(\beta}(\Gamma^a)_{\gamma)\lambda}\nabla_aX^{k)\lambda}\Big),\qquad\text{(S23-2.6e)}\\
\nabla_\alpha^iY&=8(\Gamma^a)_\alpha{}^\beta\nabla_aX_\beta{}^i+8W_\alpha{}^\beta X_\beta{}^i.\qquad\text{(S23-2.6f)}
\end{aligned}
```

Nested round brackets in (2.6e) symmetrize the spinor and `SU(2)` index families separately; they do not include the intervening indices of the other family. Source S transformations and useful Bianchi identities [S23 (2.7)–(2.8), same page] are

```math
\begin{gathered}
\nabla_{(\alpha}{}^\gamma X_{\beta)\gamma}{}^{ij}
=-\tfrac12X^{\gamma(i}W_{\alpha\beta\gamma}{}^{j)},\qquad
\nabla_{(\alpha}{}^\lambda W_{\beta\gamma\tau)\lambda}
=3i\nabla_{(\alpha}{}^\lambda(W_{\beta\gamma}W_{\tau)\lambda}),\\
S_{\alpha i}W_{\beta\gamma\delta}{}^j=6\delta_i{}^j\varepsilon_{\alpha(\beta}W_{\gamma\delta)},
\quad S_{\alpha i}X_\beta{}^j=4\delta_i{}^jW_{\alpha\beta},\\
S_{\alpha i}W_{\beta\gamma\delta\rho}=24\varepsilon_{\alpha(\beta}W_{\gamma\delta\rho)i},
\quad S_{\alpha i}Y=8iX_{\alpha i},\\
S_{\alpha i}X_{\beta\gamma}{}^{jk}
=-4\delta_i{}^{(j}W_{\alpha\beta\gamma}{}^{k)}
+4\delta_i{}^{(j}\varepsilon_{\alpha(\beta}X_{\gamma)}{}^{k)}.
\end{gathered}
```

All these independent descendants are annihilated by `K_a`; their S transformations are generally nonzero.

### Vector multiplet and differential operators [S23 (2.11)–(2.17), PDF10–11 / printed9–10]

```math
\begin{gathered}
W^*=W,\quad K_AW=0,\quad\mathbb DW=W,\qquad
\nabla_\alpha^{(i}\nabla_\beta^{j)}W=\tfrac14\varepsilon_{\alpha\beta}\nabla^{\gamma(i}\nabla_\gamma^{j)}W,\\
\lambda_\alpha^i=-i\nabla_\alpha^iW,\qquad
X^{ij}=\tfrac i4\nabla^{\alpha(i}\nabla_\alpha^{j)}W
=-\tfrac14\nabla^{\alpha(i}\lambda_\alpha^{j)},\\
F_{\alpha\beta}=-\tfrac i4\nabla_{(\alpha}^k\nabla_{\beta)k}W-W_{\alpha\beta}W
=\tfrac14\nabla_{(\alpha}^k\lambda_{\beta)k}-W_{\alpha\beta}W,\\
\nabla_\alpha^i\lambda_\beta^j
=-2\varepsilon^{ij}(F_{\alpha\beta}+W_{\alpha\beta}W)
-\varepsilon_{\alpha\beta}X^{ij}-\varepsilon^{ij}\nabla_{\alpha\beta}W,\qquad\text{(S23-2.13a)}\\
\begin{aligned}
\nabla_\alpha^iF_{\beta\gamma}
&=-i\nabla_{\alpha(\beta}\lambda_{\gamma)}^i-i\varepsilon_{\alpha(\beta}\nabla_{\gamma)}{}^\delta\lambda_\delta^i
-\tfrac{3i}{2}W_{\beta\gamma}\lambda_\alpha^i-W_{\alpha\beta\gamma}{}^iW\\
&\quad+\tfrac i2W_{\alpha(\beta}\lambda_{\gamma)}^i
-\tfrac{3i}{2}\varepsilon_{\alpha(\beta}W_{\gamma)}{}^\delta\lambda_\delta^i,
\end{aligned}\qquad\text{(S23-2.13b)}\\
\nabla_\alpha^iX^{jk}
=2i\varepsilon^{i(j}\left(\nabla_\alpha{}^\beta\lambda_\beta^{k)}
-\tfrac12W_{\alpha\beta}\lambda^{\beta k)}+\tfrac{3i}{4}X_\alpha{}^{k)}W\right),\qquad\text{(S23-2.13c)}\\
\nabla_{(\alpha}{}^\gamma F_{\beta)\gamma}=\tfrac12\lambda^{\gamma k}W_{\alpha\beta\gamma k},\qquad\text{(S23-2.14)}\\
S_\alpha^i\lambda_\beta^j=-2i\varepsilon_{\alpha\beta}\varepsilon^{ij}W,
\quad S_\alpha^iF_{\beta\gamma}=4\varepsilon_{\alpha(\beta}\lambda_{\gamma)}^i,
\quad S_\alpha^iX^{jk}=-2\varepsilon^{i(j}\lambda_\alpha^{k)},\qquad\text{(S23-2.15)}\\
\nabla^{ij}:=\nabla^{\alpha(i}\nabla_\alpha^{j)},\qquad
\Delta^{ijkl}:=-\tfrac1{96}\varepsilon^{\alpha\beta\gamma\delta}
\nabla_\alpha^{(i}\nabla_\beta^j\nabla_\gamma^k\nabla_\delta^{l)}
=-\tfrac1{32}\nabla^{(ij}\nabla^{kl)}.
\end{gathered}
```

`K_a` annihilates the vector descendants. The real prepotential has weight `-2`, and `W=-(3i/40) nabla_{ij} Delta^{ijkl} V_{kl}` [S23 (2.16)]. In component expressions the source uses the same symbol for the superfield and its `theta=0` projection. `Box:=nabla^a nabla_a` is the superconformal covariant d'Alembertian, not a scalar Levi–Civita Laplacian.

## Generic linear multiplet [S23 (2.20)–(2.24), PDF11–12 / printed10–11]

```math
\nabla_\alpha^{(i}G^{jk)}=0,\qquad K_AG^{ij}=0,\qquad
\mathbb DG^{ij}=3G^{ij},\qquad (G^{ij})^*=\varepsilon_{ik}\varepsilon_{jl}G^{kl}.
```

The complete identities needed to differentiate a primary linear multiplet are

```math
\begin{aligned}
\nabla_\alpha^iG^{jk}&=2\varepsilon^{i(j}\varphi_\alpha^{k)},\\
\nabla_\alpha^i\varphi_\beta^j
&=-\tfrac i2\varepsilon^{ij}\varepsilon_{\alpha\beta}F
+\tfrac i2\varepsilon^{ij}\mathcal H_{\alpha\beta}+i\nabla_{\alpha\beta}G^{ij},\\
\nabla_\alpha^iF&=-2\nabla_\alpha{}^\beta\varphi_\beta^i
-3W_{\alpha\beta}\varphi^{\beta i}-\tfrac32X_{\alpha j}G^{ij},\\
\nabla_\alpha^i\mathcal H_a
&=4(\Sigma_{ab})_\alpha{}^\beta\nabla^b\varphi_\beta^i
-\tfrac32(\Gamma_a)_\alpha{}^\beta W_{\beta\gamma}\varphi^{\gamma i}
-\tfrac12(\Gamma_a)_\gamma{}^\beta W_{\beta\alpha}\varphi^{\gamma i}.
\end{aligned}
```

The descendants, conservation law, and S transformations are

```math
\begin{gathered}
\varphi_\alpha^i:=\tfrac13\nabla_{\alpha j}G^{ij},\qquad
F:=\tfrac i{12}\nabla^{\gamma i}\nabla_\gamma^jG_{ij}
=-\tfrac i4\nabla^{\gamma k}\varphi_{\gamma k},\\
\mathcal H_{abcd}:=\tfrac i{12}\varepsilon_{abcde}(\Gamma^e)^{\alpha\beta}
\nabla_\alpha^i\nabla_\beta^jG_{ij}=\varepsilon_{abcde}\mathcal H^e,\\
\mathcal H^a=-\tfrac1{4!}\varepsilon^{abcde}\mathcal H_{bcde},
\qquad\nabla_a\mathcal H^a=0,\\
K_a\varphi_\alpha^i=K_aF=K_a\mathcal H_b=0,\\
S_\alpha^i\varphi_\beta^j=-6\varepsilon_{\alpha\beta}G^{ij},
\quad S_\alpha^iF=6i\varphi_\alpha^i,
\quad S_\alpha^i\mathcal H_b=-8i(\Gamma_b)_\alpha{}^\beta\varphi_\beta^i.
\end{gathered}
```

## Complete LOG primary [S23 (3.24)–(3.25)]

The defining relation [S23 (3.24), PDF20 / printed19] is

```math
H_{\log W}^{ij}=-\frac{3i}{40}\Delta^{ijkl}\nabla_{kl}\log W
=\frac{3i}{1280}\nabla^{(ij}\nabla^{kl)}\nabla_{kl}\log W.
\tag{S23-3.24}
```

Work on a patch on which `W` is nonzero and a logarithm can be chosen. The six derivatives remove the irrelevant constant shift of the logarithm. The source's footnote5 explicitly records an overall minus sign relative to the older superspace reference [20]; do not import the latter's LOG action sign without conversion.

For readability only, define `P_n^{ij}` as the coefficient of `W^{-n}`. This grouping is project notation; the right-hand sides below reproduce all terms of S23 (3.25), PDF21–22 / printed20–21, without dropping fermions or integrating by parts:

```math
H_{\log W}^{ij}=\sum_{n=0}^{6}W^{-n}P_n^{ij}.
```

```math
P_0^{ij}=-\frac{3i}{8}W_{ab}X^{abij}+\frac{51i}{64}X^{\alpha i}X_\alpha^j.
\tag{S23-3.25-P0}
```

```math
\begin{aligned}
P_1^{ij}={}&\frac9{64}X^{ij}Y-\frac{3i}{8}F_{ab}X^{abij}-\frac12\Box X^{ij}
-\frac9{64}X^{ij}W^{ab}W_{ab}+\frac14W^{ab}W_{ab}{}^{\alpha(i}\lambda_\alpha^{j)}\\
&-\frac34(\Gamma^a)^{\alpha\beta}X_\alpha^{(i}\nabla_a\lambda_\beta^{j)}
+\frac34(\Gamma^a)^{\alpha\beta}\lambda_\alpha^{(i}\nabla_aX_\beta^{j)}.
\end{aligned}\tag{S23-3.25-P1}
```

```math
\begin{aligned}
P_2^{ij}={}&\frac12X^{ij}\Box W+\frac12(\nabla^aW)\nabla_aX^{ij}
+\frac14F^{ab}W_{ab}{}^{\alpha(i}\lambda_\alpha^{j)}
-\frac i2\lambda^{\alpha(j}\Box\lambda_\alpha^{i)}
-\frac i4(\nabla^a\lambda^{\alpha i})\nabla_a\lambda_\alpha^j\\
&-\frac{3i}{16}\varepsilon^{abcde}(\Sigma_{ab})^{\alpha\beta}W_{de}\lambda_\alpha^{(i}\nabla_c\lambda_\beta^{j)}
-\frac{3i}{8}(\Gamma^a)^{\alpha\beta}\lambda_\alpha^i\lambda_\beta^j\nabla^cW_{ac}\\
&+\frac{3i}{64}Y\lambda^{\alpha i}\lambda_\alpha^j
+\frac38(\Sigma_{ab})^{\alpha\beta}F^{ab}X_\alpha^{(i}\lambda_\beta^{j)}
+\frac{3i}{128}W^{ab}W_{ab}\lambda^{\alpha i}\lambda_\alpha^j\\
&+\frac{9i}{256}\varepsilon^{abcde}(\Gamma_a)^{\alpha\beta}W_{bc}W_{de}\lambda_\alpha^i\lambda_\beta^j
-\frac38X^{ij}X^{\alpha k}\lambda_{\alpha k}.
\end{aligned}\tag{S23-3.25-P2}
```

```math
\begin{aligned}
P_3^{ij}={}&\frac18X^{ij}F^{ab}F_{ab}-\frac18X^{ij}X^{kl}X_{kl}
-\frac14X^{ij}(\nabla^aW)\nabla_aW\\
&-\frac i8\varepsilon^{abcde}(\Sigma_{ab})^{\alpha\beta}F_{de}\lambda_\alpha^{(i}\nabla_c\lambda_\beta^{j)}
-\frac i4(\Gamma^a)^{\alpha\beta}F_{ab}\lambda_\alpha^{(i}\nabla^b\lambda_\beta^{j)}\\
&-\frac i4(\Gamma^a)^{\alpha\beta}\lambda_\alpha^i\lambda_\beta^j\nabla^cF_{ac}
+\frac i4(\Gamma^a)^{\alpha\beta}X^{ij}\lambda_\alpha^k\nabla_a\lambda_{\beta k}
+\frac i4(\Gamma^a)^{\alpha\beta}X^{k(i}\lambda_\alpha^{j)}\nabla_a\lambda_{\beta k}\\
&-\frac i4(\Gamma^a)^{\alpha\beta}\lambda_\alpha^{(i}(\nabla_aX^{j)l})\lambda_{\beta l}
+\frac i4\lambda^{\alpha i}\lambda_\alpha^j\Box W
+\frac{3i}{4}(\nabla^aW)\lambda^{\alpha(i}\nabla_a\lambda_\alpha^{j)}\\
&-\frac i2(\Sigma_{ab})^{\alpha\beta}(\nabla^aW)\lambda_\alpha^{(i}\nabla^b\lambda_\beta^{j)}
-\frac{3i}{16}(\Gamma^a)^{\alpha\beta}W_{ab}\lambda_\alpha^i\lambda_\beta^j\nabla^bW
+\frac{3i}{32}W_{ab}F^{ab}\lambda^{\alpha i}\lambda_\alpha^j\\
&+\frac{9i}{64}\varepsilon^{abcde}(\Gamma_a)^{\alpha\beta}W_{bc}F_{de}\lambda_\alpha^i\lambda_\beta^j
-\frac{3i}{32}(\Sigma_{ab})^{\alpha\beta}X^{ij}W^{ab}\lambda_\alpha^k\lambda_{\beta k}\\
&-\frac{3i}{8}X^{\alpha k}\lambda_\alpha^{(i}\lambda^{\beta j)}\lambda_{\beta k}
-\frac{3i}{8}X^{\alpha k}\lambda^{\beta i}\lambda_\beta^j\lambda_{\alpha k}.
\end{aligned}\tag{S23-3.25-P3}
```

```math
\begin{aligned}
P_4^{ij}={}&-\frac{3i}{16}\lambda^{\alpha i}\lambda_\alpha^j(\nabla^aW)\nabla_aW
-\frac{3i}{8}(\Gamma^a)^{\alpha\beta}X^{k(i}\lambda_\alpha^{j)}\lambda_{\beta k}\nabla_aW\\
&+\frac{3i}{8}(\Gamma^a)^{\alpha\beta}F_{ab}\lambda_\alpha^i\lambda_\beta^j\nabla^bW
+\frac{3i}{32}F^{ab}F_{ab}\lambda^{\alpha i}\lambda_\alpha^j
+\frac{3i}{64}\varepsilon^{abcde}(\Gamma_a)^{\alpha\beta}F_{bc}F_{de}\lambda_\alpha^i\lambda_\beta^j\\
&-\frac{3i}{16}(\Sigma_{ab})^{\alpha\beta}X^{ij}F^{ab}\lambda_\alpha^k\lambda_{\beta k}
-\frac{3i}{16}X^{ij}X^{kl}\lambda_k^\alpha\lambda_{\alpha l}
-\frac{3i}{32}X^{kl}X_{kl}\lambda^{\alpha i}\lambda_\alpha^j\\
&-\frac{15}{64}(\Gamma^a)^{\alpha\beta}\lambda_\alpha^i\lambda_\beta^j\lambda^{\gamma k}\nabla_a\lambda_{\gamma k}
-\frac9{32}(\Gamma^a)^{\alpha\beta}\lambda_\alpha^{(i}\lambda^{\rho j)}\lambda_\beta^k\nabla_a\lambda_{\rho k}\\
&-\frac{15}{32}(\Gamma^a)^{\alpha\beta}\lambda_\alpha^{(i}\lambda^{\rho j)}\lambda_\rho^k\nabla_a\lambda_{\beta k}
-\frac{15}{64}(\Gamma^a)^{\alpha\beta}\lambda^{\rho i}\lambda_\rho^j\lambda_\alpha^k\nabla_a\lambda_{\beta k}\\
&+\frac9{32}(\Sigma_{ab})^{\alpha\beta}W^{ab}\lambda_\alpha^{(i}\lambda^{\rho j)}\lambda_\beta^k\lambda_{\rho k}
+\frac9{64}(\Sigma_{ab})^{\alpha\beta}W^{ab}\lambda^{\rho i}\lambda_\rho^j\lambda_\alpha^k\lambda_{\beta k}.
\end{aligned}\tag{S23-3.25-P4}
```

```math
\begin{aligned}
P_5^{ij}={}&\frac38(\Gamma^a)^{\alpha\beta}\lambda_\alpha^{(i}\lambda^{\rho j)}\lambda_\beta^k\lambda_{\rho k}\nabla_aW
+\frac38(\Sigma_{ab})^{\alpha\beta}F^{ab}\lambda^{\rho i}\lambda_\rho^j\lambda_\alpha^k\lambda_{\beta k}
+\frac38X^{kl}\lambda^{\alpha i}\lambda_\alpha^j\lambda_k^\beta\lambda_{\beta l},\\
P_6^{ij}={}&\frac{3i}{32}\lambda^{\alpha i}\lambda_\alpha^j\lambda^{\beta k}\lambda_\beta^l\lambda_k^\gamma\lambda_{\gamma l}
+\frac{3i}{16}\lambda^{\alpha i}\lambda_\alpha^k\lambda^{\beta j}\lambda_\beta^l\lambda_k^\gamma\lambda_{\gamma l}.
\end{aligned}\tag{S23-3.25-P5-P6}
```

This is the full primary (including quartic and sextic fermions); it is not the fully expanded action. A useful transcription fingerprint is the term count by power: `(2,7,12,18,14,3,2)`, totaling 58 summands before any identities or integrations by parts. Gold 2025's shorter primary does not replace it for full fermionic work.

## LOG descendants and the full BF density

Source [S23 (3.26a–c), PDF22 / printed21]:

```math
\varphi_{\log W}^{\alpha i}=\frac13\nabla_j^\alpha H_{\log W}^{ij},
\qquad F_{\log W}=\frac i{12}\nabla_i^\alpha\nabla_{\alpha j}H_{\log W}^{ij},
\qquad\mathcal H_{\log W}^a=\frac i{12}(\Gamma^a)^{\alpha\beta}
\nabla_{\alpha i}\nabla_{\beta j}H_{\log W}^{ij}.
\tag{S23-3.26}
```

The general BF action [S23 (3.2a–b), PDF14 / printed13] is

```math
\begin{aligned}
S_{\rm BF}&=\int d^{5|8}z\,E\,\Omega W
=\int d^{5|8}z\,E\,G^{ij}V_{ij}\\
&=-\int d^5x\,e\Big[
v_a\mathcal H^a+WF+X_{ij}G^{ij}+2\lambda^{\alpha k}\varphi_{\alpha k}
-\psi_{ai}{}^\alpha(\Gamma^a)_\alpha{}^\beta\varphi_\beta{}^iW\\
&\hspace{37mm}-i\psi_{ai}{}^\alpha(\Gamma^a)_\alpha{}^\beta\lambda_{\beta j}G^{ij}
+i\psi_{ai}{}^\alpha(\Sigma^{ab})_\alpha{}^\beta\psi_{b\beta j}WG^{ij}\Big].
\end{aligned}\tag{S23-3.2}
```

Here `E=Ber(E_M{}^A)` is the superspace measure and `e` the component vielbein determinant. `U|:=U(x,theta)|_{theta=0}`. `v_m=V_m|` and `f_{mn}=2 partial_[m v_n]`. The component supercovariant strengths are [S23 (3.3)–(3.4), same page; C24 (2.37),(2.50), PDF18,22]

```math
\begin{aligned}
F_{ab}&=f_{ab}+i(\Gamma_{[a})_\alpha{}^\beta\psi_{b]k}{}^\alpha\lambda_\beta{}^k
+\tfrac i2W\psi_{[ak}{}^\gamma\psi_{b]\gamma}{}^k,
\qquad f_{ab}=e_a{}^me_b{}^nf_{mn},\\
\mathcal H^a&=h^a+2(\Sigma^{ab})_\alpha{}^\beta\psi_{bi}{}^\alpha\varphi_\beta{}^i
-\tfrac i2\varepsilon^{abcde}(\Sigma_{bc})_{\alpha\beta}\psi_{di}{}^\alpha\psi_{ej}{}^\beta G^{ij}.
\end{aligned}
```

The LOG action is the same density evaluated on the composite multiplet [S23 (3.27a–b), PDF22 / printed21; C24 (5.9a–b), PDF41 / printed40]:

```math
\begin{aligned}
S_{\log W}&=\int d^{5|8}z\,E\,V_{ij}H_{\log W}^{ij}\\
&=-\int d^5x\,e\Big[v_a\mathcal H_{\log W}^a+WF_{\log W}
+X_{ij}H_{\log W}^{ij}+2\lambda^k\varphi_{k\log W}\\
&\hspace{24mm}-\psi_{ai}\Gamma^a\varphi_{\log W}^iW
-i\psi_{ai}\Gamma^a\lambda_jH_{\log W}^{ij}
+i\psi_{ai}\Sigma^{ab}\psi_{bj}WH_{\log W}^{ij}\Big].
\end{aligned}\tag{S23-3.27;C24-5.9}
```

The implicit spinor contractions in the last display are fixed by the explicit general density above. The bracket has **seven summands**: `v H`, `W F`, `X G`, `2 lambda varphi`, and the three explicit gravitino terms. Neither the overall minus nor any explicit gravitino coupling may be discarded.

S23's text immediately after (3.27) defers the expanded descendants. Their full component support is C24 supplement §2.2.1 (`varphi`, PDF106–112 / printed7–13), §2.2.2 (`F`, PDF113–121 / printed14–22), §2.2.3 (`mathcal H^a`, PDF121–149 / printed22–50). The scalar and vector page ranges overlap on PDF121 at their subsection boundary. These are distinct from the bosonic-only supplement §3.1. The master source cache, rather than this compact equation list, carries the lengthy expanded descendants.

## Supplement notation and projections [C24 supplement §1, PDF103 / printed4]

The underlining and hatting conventions in (1.1a–b) mean weighted symmetrization and antisymmetrization, without exchanging the order of the Grassmann factors:

```math
\lambda_{\underline i}^{\alpha}\lambda_{\underline j}^{\beta}
:=\lambda_{(i}^{\alpha}\lambda_{j)}^{\beta}
=\tfrac12\lambda_i^\alpha\lambda_j^\beta+\tfrac12\lambda_j^\alpha\lambda_i^\beta,
\qquad
W_{c\hat a}W_{\hat b d}:=W_{c[a}W_{b]d}
=\tfrac12W_{ca}W_{bd}-\tfrac12W_{cb}W_{ad}.
```

The source projections (1.2a–b), and the immediately following curvature identification, are

```math
\chi_\alpha^i=\frac{3i}{32}X_\alpha^i|,
\qquad D=-\frac3{128}Y|,
\qquad\Phi_{ab}{}^{ij}=-\frac{3i}{4}X_{ab}{}^{ij}|.
\tag{C24-supp-1.2}
```

The last relation corresponds to `R(J)_{ab}^{ij}` in the superspace notation. Solving the first two gives `X_alpha^i|=-(32i/3)chi_alpha^i` and `Y|=-(128/3)D`. These inverse formulas follow algebraically; they are not new independent source equations. In the supplement, raw `R` and `f` use different typography from the main paper. Preserve the geometric and dependent-connection meanings, not only the visual glyphs. The supplement says its longer expressions can differ from the main text by algebra and sometimes integrations by parts; compare densities only with their boundary representatives recorded.

## Published Gold-to-Bergshoeff bridge [C24 Appendix C, Tables4–6]

The following uses the **Bergshoeff et al. column**. C24 also provides other convention systems; mixing a de Wit entry into this column is not permitted. Source: Tables4–5, PDF91 / printed90; Table6, PDF92 / printed91. The paragraph immediately before Table4 (PDF90 / printed89) explicitly explains the field-dependent S/K shifts and cancellation in the fully covariant vector derivative.

### Algebra and Weyl multiplet

```math
\begin{gathered}
\eta_G^{ab}=\eta_B^{ab},\qquad
\Gamma_G^a=i\gamma_B^a,\qquad
\Sigma_G^{ab}=\tfrac12\gamma_B^{ab},\qquad
\varepsilon_G^{abcde}=-\varepsilon_B^{abcde},\\
\psi_m^{Gi}=\psi_\mu^{Bi},\qquad
\mathcal V_m^{G,i}{}_j=-V_\mu^{B,i}{}_j,\qquad
\omega_m^{G,ab}=-\omega_\mu^{B,ab},\\
i\phi_m^{Gi}=-\phi_\mu^{Bi}+\tfrac13T_{ab}^B\gamma_B^{ab}\psi_\mu^{Bi},\\
\mathfrak f_m^{G,a}=-f_\mu^{B,a}+\tfrac13\psi_\mu^{Bi}\gamma_B^a\chi_i^B,\\
w_G^{ab}=\tfrac{16}{3}T_B^{ab},\qquad\chi_G^i=\chi_B^i,\qquad D_G=D_B.
\end{gathered}\tag{C24-Table4-fields}
```

`m` and `mu` are the same curved index under the naming conversion. The spinor contractions in the table are source contractions; a Majorana bar cannot be inserted or moved by typography alone. Here `w_ab=W_ab|`, using the two-form version of [C24 (2.15a), PDF12 / printed11].

The corresponding curvatures satisfy

```math
\begin{aligned}
R_G(Q)_{ab}{}^i&=\tfrac12R_B(Q)_{ab}{}^i,\\
R_G(M)_{ab}{}^{cd}&=-R_B(M)_{ab}{}^{cd},\\
R_G(J)_{ab}{}^i{}_j&=-R_B(V)_{ab}{}^i{}_j,\\
iR_G(S)_{ab}{}^i&=-\tfrac12R_B(S)_{ab}{}^i
+\tfrac16T_{cd}^B\gamma_B^{cd}R_B(Q)_{ab}{}^i,\\
R_G(K)_{ab}{}^c&=-R_B(K)_{ab}{}^c
+\tfrac13R_B(Q)_{ab}{}^i\gamma_B^c\chi_i^B.
\end{aligned}\tag{C24-Table4-curvatures}
```

The minus in `R(M)` is a frame-convention map. It does not license flipping a project metric Riemann tensor in isolation while keeping unchanged its connection/generator conventions.

### Supersymmetry parameters [C24 Table5]

A Gold `delta_Q(xi_G)+delta_S(eta_G)+delta_K(Lambda_G)` becomes a Bergshoeff transformation with

```math
\epsilon_B^i=2\xi_G^i,\qquad
\eta_B^{\prime i}=-2i\eta_G^i+\tfrac23T_{ab}^B\gamma_B^{ab}\xi_G^i,\qquad
\Lambda_K^{\prime Ba}=-\Lambda_K^{Ga}+\tfrac23\xi_G^i\gamma_B^a\chi_i^B.
\tag{C24-Table5}
```

Therefore the conversion of a Q rule includes induced S and K rules. Converting only the gamma matrices, the fields, or `epsilon=2xi` does not convert a complete transformation. The source states that these shifts cancel the corresponding gravitino terms in the S/K connections, leaving the same fully covariant vector derivative after generator-normalization conversion. This statement concerns the **whole derivative**, not a termwise equality of the named connections.

### Vector multiplet [C24 Table6]

```math
W_G=\sigma_B,\qquad\lambda_G^i=-\psi_B^i,\qquad X_G^{ij}=2Y_B^{ij}.
\tag{C24-Table6}
```

For a generic vector scalar called `rho` in the project, relabel `sigma_B` to `rho` only after identifying which vector is under discussion. The defining vector later has `rho=sigma` and `A=C`. Table6 itself does not list the vector potential or a full linear-multiplet normalization map.

## Conversion and homogeneity checks

These are direct algebraic checks, not a nonlinear action/SUSY validation.

1. **Clifford sign.** With the project Bergshoeff `\{\gamma_B^a,\gamma_B^b\}=2\eta^{ab}`, Table4 gives `\{\Gamma_G^a,\Gamma_G^b\}=-2\eta^{ab}`. For signature `(-++++)`, `(gamma_B^0)^2=-1` and `(Gamma_G^0)^2=+1`, while `(gamma_B^1)^2=+1` and `(Gamma_G^1)^2=-1`. Thus the shared metric does not mean the two Clifford anticommutators have the same sign. Also `Sigma_G^{ab}=-[Gamma_G^a,Gamma_G^b]/4=gamma_B^{ab}/2`, using `gamma^{ab}=gamma^{[a}gamma^{b]}`.
2. **Projection inverses.** Substituting `X|=-(32i/3)chi` into `chi=(3i/32)X|` gives `chi`, and substituting `Y|=-(128/3)D` into `D=-3Y|/128` gives `D`. Combining with Table4 gives `W_ab|=16 T_ab/3` and leaves `chi,D` unchanged between G and B.
3. **Primary weights.** `w(W)=w(W_ab)=1`, `w(lambda)=w(X_alpha)=w(W_abc-spinor)=3/2`, `w(X^{ij})=w(F_ab)=w(Y)=w(X_ab^{ij})=2`, `w(nabla_a)=1`, `w(nabla_alpha)=1/2`. Each displayed `P_n` has weight `3+n`, so `W^{-n}P_n` has weight3. For example `W^{-6}lambda^6` has `-6+6(3/2)=3`; `W^{-1}Box X^{ij}` has `-1+2+2=3`; `W_ab X^{abij}` has `1+2=3`. Six spinor derivatives in (3.24) have weight3; the inhomogeneous constant dilatation shift of `log W` is killed.
4. **BF weights.** The linear slots have `(w(G),w(varphi),w(F),w(mathcal H))=(3,7/2,4,4)`, and the tangent fields have `w(v_a)=1`, `w(psi_a)=1/2`. All seven BF terms have weight5: e.g. `W F=1+4`, `lambda varphi=3/2+7/2`, `psi psi W G=1/2+1/2+1+3`.
5. **BF normalization boundary.** `X_G G=2Y_B G` follows from Table6, but this alone does not determine `G` relative to the project's normalized `L^{ij}` or the overall Gold-to-project density conversion. A complete matching gate must compare scalar, triplet, form, spinor, and gravitino slots together, using their Q/S transformations and Table5. No equality between full component actions is inferred from a single bosonic slot.
6. **Orientation test.** Table4 maps every displayed upper five-index epsilon with a factor `-1`; two epsilon factors map with `+1`. It is not consistent to change epsilon in the CS term while leaving it unconverted in the corresponding Hodge dual.

## Source frames and conversion scope

- The full S23 primary is transcribed above. The compact descendant definitions are exact. The long descendants and higher component derivatives are available in the local source cache; the component derivations evaluate them in the stated source frame.
- S23 (3.27) and C24 (5.9b) are Standard-Weyl BF constructions. Their published local supersymmetry does not by itself prove a new, explicitly expanded, project-corrected gauged action.
- C24 Tables4–6 establish the published Gold/Bergshoeff bridge. They do not contain a full Gold linear-multiplet-to-project `L,varphi,E,N` normalization table. The branch derives that covariant normalization in LOG_CONVENTIONS.md. The [full superform interface](../../../../../../../../references/source_evidence/log/derivations/form-interface.md) completes the generic current/potential/BF comparison, preserving explicit derived repairs of the incompatible printed formulas. Checking the actual expanded LOG multiplet remains distinct from this generic conversion.
- Project-specific corrected fermionic curvature signs cannot be promoted to the printed C24 bridge. Compare them explicitly when substituting dependent connections.
- Gauging introduces its own deformed composite map; the Table4 Standard-Weyl bridge is not that gauged map. Gold2025's `f.t.` placeholders and lower-order primary are not full fermionic replacements.

## Extraction verification record

S23 PDF9–12, PDF14 and PDF21–22, and C24 PDF81–82, PDF91, PDF103 were rendered and visually inspected for coefficients, positions, symmetrizations, and projection factors. The complete primary was checked line by line against the source images, including its continuation onto PDF22. The source field frame is retained. Every formula block has a local source/equation/page cue; `P_n` grouping and the checks are explicitly identified as project organization or algebraic consequences.

Executed checks: **PASS** for the Weyl weight of all 58 primary summands, **PASS** for all 25 Clifford anticommutators in each frame, **PASS** for all 25 bivector conversions, **PASS** for both projection inverses. This verifies transcription-level homogeneity and convention conversions; it does not verify cancellations in the complete supersymmetry variation.

The following dependency-free Python is a reusable version of the executed checks. The monomial strings are ordered exactly as the displayed `P_n` terms. `w` is the scalar, `W` the Weyl two-form, `l` the gaugino, `x` the Weyl spinor, `u` the Weyl three-spinor descendant, `X` the vector triplet, `Z` the Weyl two-form triplet. The `d`/`box` prefixes count one/two vector derivatives.

```python
from fractions import Fraction as Q

weights = dict(w=1, W=1, l=Q(3,2), x=Q(3,2), u=Q(3,2),
               X=2, F=2, Y=2, Z=2, dw=2, dW=2, dl=Q(5,2),
               dx=Q(5,2), dX=3, dF=3, boxw=3, boxX=4, boxl=Q(7,2))
terms = {
    0: ['W Z', 'x x'],
    1: ['X Y', 'F Z', 'boxX', 'X W W', 'W u l', 'x dl', 'l dx'],
    2: ['X boxw', 'dw dX', 'F u l', 'l boxl', 'dl dl', 'W l dl',
        'l l dW', 'Y l l', 'F x l', 'W W l l', 'W W l l', 'X x l'],
    3: ['X F F', 'X X X', 'X dw dw', 'F l dl', 'F l dl', 'l l dF',
        'X l dl', 'X l dl', 'l dX l', 'l l boxw', 'dw l dl', 'dw l dl',
        'W l l dw', 'W F l l', 'W F l l', 'X W l l', 'x l l l', 'x l l l'],
    4: ['l l dw dw', 'X l l dw', 'F l l dw', 'F F l l', 'F F l l',
        'X F l l', 'X X l l', 'X X l l', 'l l l dl', 'l l l dl',
        'l l l dl', 'l l l dl', 'W l l l l', 'W l l l l'],
    5: ['l l l l dw', 'F l l l l', 'X l l l l'],
    6: ['l l l l l l', 'l l l l l l'],
}
assert tuple(map(len, terms.values())) == (2,7,12,18,14,3,2)
for n, group in terms.items():
    for k, term in enumerate(group, 1):
        assert sum(weights[f] for f in term.split()) - n == 3, (n,k,term)

I = ((1,0),(0,1))
s1, s2, s3 = ((0,1),(1,0)), ((0,-1j),(1j,0)), ((1,0),(0,-1))
def kron(A, B):
    return tuple(tuple(A[i//2][j//2]*B[i%2][j%2] for j in range(4)) for i in range(4))
def scale(c, A):
    return tuple(tuple(c*x for x in row) for row in A)
def add(A, B):
    return tuple(tuple(x+y for x,y in zip(ra,rb)) for ra,rb in zip(A,B))
def mm(A, B):
    return tuple(tuple(sum(A[i][k]*B[k][j] for k in range(4)) for j in range(4)) for i in range(4))
I4 = kron(I,I)
gamma = [scale(1j,kron(s3,s3)), kron(s1,I), kron(s2,I), kron(s3,s1), kron(s3,s2)]
Gamma = [scale(1j,g) for g in gamma]
for a in range(5):
    for b in range(5):
        eta = (-1 if a == 0 else 1) if a == b else 0
        assert add(mm(gamma[a],gamma[b]),mm(gamma[b],gamma[a])) == scale(2*eta,I4)
        assert add(mm(Gamma[a],Gamma[b]),mm(Gamma[b],Gamma[a])) == scale(-2*eta,I4)
        commG = add(mm(Gamma[a],Gamma[b]),scale(-1,mm(Gamma[b],Gamma[a])))
        commB = add(mm(gamma[a],gamma[b]),scale(-1,mm(gamma[b],gamma[a])))
        assert scale(-Q(1,4),commG) == scale(Q(1,4),commB)
assert Q(3,32)*1j*(-Q(32,3)*1j) == 1
assert -Q(3,128)*(-Q(128,3)) == 1
print('PASS: 58 primary weights; 2x25 Clifford checks; 25 bivectors; 2 inverses')
```
