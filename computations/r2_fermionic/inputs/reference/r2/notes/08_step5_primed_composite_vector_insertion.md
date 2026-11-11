# Step 5: insert the complete primed composite vector

**Date:** 2026-09-10. **Working derivation:** `R2-PRIMED-COMPOSITE-INSERTION-v1`.
**Parent:** [corrected Step 4](06_step4_Gold_unprimed_vector_and_gauge.md), Eq. (47), `R2-GOLD4-UNPRIMED-SUBSTITUTION-v2`.
**Input map:** `OZKAN1608-SINGLE-LINEAR-TO-VECTOR-MAP-v2`.

## 1. Problem and Target

Apply the earlier complete linear-to-vector map to every primed vector argument of the Step 4 density. The input is the **same original unprimed** $`(L_{ij},\varphi_i,E_a,N)`$ used in Gold's defining-vector map. This is Step 5 of [the confirmed framework](00_action_construction_framework.md). No mixed coefficient is applied again, and no vector components are identified with one another.

The calculation is off shell. It retains every explicit fermion term of the locked map, including the cubic spinor and quartic triplet terms, and retains all implicit supercovariant completions. No auxiliary equation, integration by parts, dualization, bosonic restriction, or quadratic-fermion approximation is used in the action insertion. Diagnostic limits are labelled separately.

Gold (7), $`\sigma=1`$, $`b_\mu=0`$, $`\psi^i=0`$, is inherited from Step 4. The original linear fermion $`\varphi_i`$ and the gravitino $`\psi_\mu{}^i`$ survive. Section 4.5 examines the additional aligned-triplet gauge locally for the potential; the unrestricted triplet map is preserved before that examination.

The common $`T_{ab},\chi^i,D`$ and every dependent connection remain **gauged Coomans background slots**. The [Step 6 calculation](10_step6_gauged_action_through_two_fermions.md) expands these slots through two physical fermions. It does not determine source-omitted higher orders. Keeping those slots in exact source notation here is not an instruction to use their bosonic parts.

## 2. Convention Ledger

<!-- ASSERT_CONVENTION: metric_signature=mostly_plus (-++++); natural_units=hbar=c=1; gauge_slice=R2-GOLD7-GAUGE-v1; spinor_bar=NW-SE-transpose; fermion_order=full_source_map; background=gauged_Coomans -->

| Item | Convention used in this calculation |
|---|---|
| Geometry | $`d=5`$, $`\eta_{ab}=(-,+,+,+,+)`$; $`a,b,c=0,\ldots,4`$ and $`\mu,\nu=0,\ldots,4`$. Curvature and torsion are the parent Coomans/Özkan conventions; the project $`R'(M)\vert_\chi`$ correction is retained. |
| Clifford algebra | $`\{\gamma_a,\gamma_b\}=2\eta_{ab}`$; antisymmetrized products and symmetrization have unit weight; $`\gamma^{abcde}=i\varepsilon^{abcde}`$. Gamma-dot includes no extra factorial. |
| Orientation | $`\varepsilon^{01234}=+1`$, $`\varepsilon_{01234}=-1`$ in an oriented orthonormal frame. |
| $`SU(2)`$ | $`i,j,k,l,m,n=1,2`$; $`X^i=\varepsilon^{ij}X_j`$, $`X_i=X^j\varepsilon_{ji}`$, $`\varepsilon_{12}=\varepsilon^{12}=1`$. |
| Spinors | Grassmann-odd symplectic Majorana. Operational bar $`\bar\zeta^i=(\zeta^i)^TC`$, $`C^T=-C`$. The source bar operation does not complex-conjugate scalar $`i`$. No fermionic functional derivative is taken. |
| Transposes | $`(\gamma^a)^TC=C\gamma^a`$, $`(\gamma^{ab})^TC=-C\gamma^{ab}`$. Fixed-index bilinear flips have $`t_0=t_1=+1`$, $`t_2=t_3=-1`$; a contracted NW–SE pair supplies its additional index sign. |
| Derivatives | Full source superconformal derivatives, even as operators; their product rule introduces no Grassmann sign without reordering. Keep spin connection, contorsion, $`SU(2)`$, $`S`$ and $`K`$ connections. |
| Couplings | Inherit the unit BF density and dimensionless conformal $`g`$. The later physical $`\lambda_{R^2}`$ has mass dimension $`-2`$ after normalization; no normalization is fitted here. |
| Domain | $`L=(L_{ij}L^{ij})^{1/2}>0`$ on the composite-map patch. The singular locus $`L=0`$ is excluded. |

Fixing a compensator does not assign dimension zero to every descendant term. All weights below are checked before the compensator powers are set to one.

## 3. Definitions and Required Identities

The [immutable earlier-map anchor](../../../../../two_derivative_fermionic/inputs/reference/results/gauged_two_derivative_fermionic_action/03_single_linear_multiplet_linear_map_anchor.md) fixes its [full derivation](../../../../../two_derivative_fermionic/inputs/reference/results/gauged_two_derivative_fermionic_action/02_single_linear_multiplet_mapping_construction.md): scalar Sec. 7.9; spinor Secs. 8.7/8.11; **full** triplet Sec. 9.7; strength Eqs. (10.11),(10.15). The final summary's bosonic triplet is not a replacement for Sec. 9.7. The [source lock](../../../../../../common/README.md) and audit qualifications are inherited.

The supporting derivative definitions are Coomans (2.16)–(2.17) and corrected Özkan–Pang (2.19), (2.20), (3.6), anchored in the [two-derivative source/action record](../../../../../../common/two_derivative_action/details/construction.md), Secs. 3.2–3.4 and 4.7. Only its source definitions are reused; its quadratic action is not used as the full map.

```math
\begin{aligned}
L^2&=L_{ij}L^{ij},\qquad \mathcal F_{11}=L^{-1},\\
2L\mathcal D_aL&=(\mathcal D_aL_{ij})L^{ij}+L_{ij}\mathcal D_aL^{ij}
=2L^{ij}\mathcal D_aL_{ij},\\
\mathcal D_aL&=L^{-1}L^{ij}\mathcal D_aL_{ij},\qquad
\mathcal D_aL^{-p}=-pL^{-p-1}\mathcal D_aL.
\end{aligned}
\tag{1}
```

The two terms in the differentiated norm are equal after raising both triplet indices with the two epsilon tensors and relabelling the contracted pair. The multiplet label $`11`$ on $`\mathcal F`$ belongs only to the earlier single-linear map; it does not replace the mixed vector labels $`B,C=1,2`$.

```math
\begin{aligned}
\mathcal D_a(XY)&=(\mathcal D_aX)Y+X\mathcal D_aY,\\
\overline{c\,\gamma^{a_1\cdots a_p}\zeta}
&=c\,\bar\zeta\,C^{-1}(\gamma^{a_1\cdots a_p})^TC,
\qquad |c|=0,\\
\lambda'{}^i&=\varepsilon^{ir}\lambda'_r,\qquad
\bar\lambda'{}^i=\varepsilon^{ir}\bar\lambda'_r,\qquad
Y'^{ij}=\varepsilon^{ir}\varepsilon^{js}Y'_{rs}.
\end{aligned}
\tag{2}
```

In the bar identity $`c`$ may be an even spinor bilinear. It commutes past a single spinor with sign $`(-1)^{2\cdot1}=+1`$. Gamma transpose reverses the rank-two matrix sign; scalar $`i`$ keeps its source coefficient. Epsilon tensors are displayed until the free indices have been raised.

## 4. Detailed Derivation

### 4.1 Relabel only the output of the earlier map

<!-- ASSERT_CONVENTION: metric_signature=mostly_plus (-++++); natural_units=hbar=c=1; gauge_slice=R2-GOLD7-GAUGE-v1; spinor_bar=NW-SE-transpose; fermion_order=full_source_map; background=gauged_Coomans -->

```math
\rho'=\left[\begin{aligned}
&2L^{-1}N\\
&+iL^{-3}L_{ij}\bar\varphi^i\varphi^j
\end{aligned}\right]
\tag{3}
```

The earlier scalar has two terms. Relabelling its vector output adds the prime to the left-hand side only. Its input $`N,L_{ij},\varphi_i`$ is unchanged. Neither term contains the gauge-fixed defining gaugino $`\psi^i`$.

```math
\lambda'_i=\left[\begin{aligned}
&-2iL^{-1}\not{\mathcal D}\varphi_i\\
&+16L^{-1}L_{ij}\chi^j\\
&+4L^{-1}\gamma\!\cdot\!T\varphi_i\\
&-2NL^{-3}L_{ij}\varphi^j\\
&+2iL^{-3}(\not{\mathcal D}L_{ij})L^{jk}\varphi_k\\
&-2iL^{-3}\not E L_{ij}\varphi^j\\
&+2iL^{-3}\varphi^j\bar\varphi_i\varphi_j\\
&-6iL^{-5}\varphi^j\bar\varphi_k\varphi_lL^{kl}L_{ij}
\end{aligned}\right]
\tag{4}
```

The first six terms have one explicit fermion; the last two have three. The derivative of $`\varphi_i`$ has its own connection and gravitino completion, so the explicit-degree count is not a truncation. The two cubic coefficients remain $`+2iL^{-3}`$ and $`-6iL^{-5}`$.

```math
Y'_{ij}=\left[\begin{aligned}
&L^{-1}\square^c L_{ij}\\
&-L^{-3}L^{km}\mathcal D_aL_{k(i}\mathcal D^aL_{j)m}\\
&-L^{-3}L_{ij}N^2\\
&-L^{-3}L_{ij}E_aE^a\\
&+2L^{-3}E_aL_{k(i}\mathcal D^aL_{j)}{}^k\\
&+\frac83L^{-1}L_{ij}T^2\\
&+4L^{-1}L_{ij}D\\
&+iNL^{-3}\bar\varphi_{(i}\varphi_{j)}\\
&-3iNL^{-5}L_{ij}L^{kl}\bar\varphi_k\varphi_l\\
&+3L^{-5}L_{ij}L^{kl}\bar\varphi_k\not E\varphi_l\\
&-L^{-3}\bar\varphi_{(i}\not E\varphi_{j)}\\
&-16iL^{-1}\bar\chi_{(i}\varphi_{j)}\\
&+16iL^{-3}L_{ij}L_{kl}\bar\chi^k\varphi^l\\
&+2L^{-3}L_{k(i}\bar\varphi^k\not{\mathcal D}\varphi_{j)}\\
&-3L^{-5}L_{k(i}L^{lm}\bar\varphi^k(\not{\mathcal D}L_{j)l})\varphi_m\\
&+\frac12L^{-3}\bar\varphi^l(\not{\mathcal D}L_{l(i})\varphi_{j)}\\
&+\frac12L^{-3}\bar\varphi^m(\not{\mathcal D}L_{ij})\varphi_m\\
&+2iL^{-3}L_{ij}\bar\varphi\gamma\!\cdot\!T\varphi\\
&+\frac{15}{2}L^{-7}L_{ij}(L^{kl}\bar\varphi_k\varphi_l)^2\\
&-3L^{-5}(L^{kl}\bar\varphi_k\varphi_l)\bar\varphi_{(i}\varphi_{j)}\\
&-\frac32L^{-5}L_{ij}(\bar\varphi_m\varphi_n)(\bar\varphi^m\varphi^n)
\end{aligned}\right]
\tag{5}
```

This is the sum of seven terms with no explicit spinor, eleven explicit bilinear terms, and three explicit quartic terms. Their order is the source order. In particular the quartic coefficients are $`15/2,-3,-3/2`$; no Fierz conversion to the different 2013 triplet is assumed.

```math
\widehat F'_{\mu\nu}=\left[\begin{aligned}
&4\mathcal D_{[\mu}(L^{-1}E_{\nu]})\\
&+2L^{-1}\widehat R_{\mu\nu}^{ij}(V)L_{ij}\\
&-2L^{-3}L_k{}^l\mathcal D_{[\mu}L^{kp}\mathcal D_{\nu]}L_{lp}\\
&-2\mathcal D_{[\mu}(L^{-3}L_{ij}\bar\varphi^i\gamma_{\nu]}\varphi^j)\\
&-iL^{-1}\bar\varphi^i\widehat R_{\mu\nu i}(Q)
\end{aligned}\right]
\tag{6}
```

The map supplies a **hatted field strength**. Its last term contains the gravitino curvature and remains when the defining gaugino vanishes. The last two terms also show why the strength cannot be integrated as a purely bosonic curl.

### 4.2 Bar and epsilon operations before insertion

<!-- ASSERT_CONVENTION: metric_signature=mostly_plus (-++++); natural_units=hbar=c=1; gauge_slice=R2-GOLD7-GAUGE-v1; spinor_bar=NW-SE-transpose; fermion_order=full_source_map; background=gauged_Coomans -->

```math
\begin{aligned}
\overline{-2iL^{-1}\gamma^a\mathcal D_a\varphi_i}
&=-2iL^{-1}(\mathcal D_a\bar\varphi_i)\gamma^a,\\
\overline{4L^{-1}\gamma^{ab}T_{ab}\varphi_i}
&=-4L^{-1}\bar\varphi_i\gamma^{ab}T_{ab},\\
\overline{2iL^{-3}\varphi^j(\bar\varphi_i\varphi_j)}
&=2iL^{-3}(\bar\varphi_i\varphi_j)\bar\varphi^j
=2iL^{-3}\bar\varphi^j(\bar\varphi_i\varphi_j).
\end{aligned}
\tag{7}
```

The three lines apply, respectively, the rank-one transpose, rank-two transpose, and passage of an even bilinear through one odd spinor. The remaining terms use the rank-zero or rank-one rule without changing their scalar coefficient.

```math
\bar\lambda'_i=\left[\begin{aligned}
&-2iL^{-1}(\mathcal D_a\bar\varphi_i)\gamma^a\\
&+16L^{-1}L_{ij}\bar\chi^j\\
&-4L^{-1}\bar\varphi_i\gamma\!\cdot\!T\\
&-2NL^{-3}L_{ij}\bar\varphi^j\\
&+2iL^{-3}L^{jk}\bar\varphi_k(\not{\mathcal D}L_{ij})\\
&-2iL^{-3}L_{ij}\bar\varphi^j\not E\\
&+2iL^{-3}\bar\varphi^j(\bar\varphi_i\varphi_j)\\
&-6iL^{-5}\bar\varphi^j(\bar\varphi_k\varphi_l)L^{kl}L_{ij}
\end{aligned}\right]
\tag{8}
```

```math
\begin{aligned}
\bar\lambda'{}^i\not{\mathcal D}\lambda'_i
&=\varepsilon^{ir}\bar\lambda'_r\gamma^a\mathcal D_a\lambda'_i,\\
\bar\lambda'{}^iL_{ij}\lambda'{}^j
&=\varepsilon^{ir}\varepsilon^{js}\bar\lambda'_rL_{ij}\lambda'_s,\\
Y'^{ij}Y'_{ij}&=\varepsilon^{ir}\varepsilon^{js}Y'_{rs}Y'_{ij},\\
L^{rj}\varepsilon_{ri}\psi_{\mu j}&=-L_{ij}\psi_\mu{}^j.
\end{aligned}
\tag{9}
```

The last identity is obtained by substituting $`L^{rj}=\varepsilon^{rp}\varepsilon^{jq}L_{pq}`$ and $`\psi_{\mu j}=\psi_\mu{}^k\varepsilon_{kj}`$: $`\varepsilon^{rp}\varepsilon_{ri}=\delta^p_i`$ whereas $`\varepsilon^{jq}\varepsilon_{kj}=-\delta^q_k`$. This is the sign needed below. No delta replaces a single epsilon.

### 4.3 Differentiate the complete map

<!-- ASSERT_CONVENTION: metric_signature=mostly_plus (-++++); natural_units=hbar=c=1; gauge_slice=R2-GOLD7-GAUGE-v1; spinor_bar=NW-SE-transpose; fermion_order=full_source_map; background=gauged_Coomans -->

```math
\begin{aligned}
\mathcal D_a(2L^{-1}N)&=2L^{-1}\mathcal D_aN-2NL^{-2}\mathcal D_aL,\\
\mathcal D_a(iL^{-3}L_{ij}\bar\varphi^i\varphi^j)
&=-3iL^{-4}(\mathcal D_aL)L_{ij}\bar\varphi^i\varphi^j\\
&\quad+iL^{-3}(\mathcal D_aL_{ij})\bar\varphi^i\varphi^j\\
&\quad+iL^{-3}L_{ij}(\mathcal D_a\bar\varphi^i)\varphi^j
+iL^{-3}L_{ij}\bar\varphi^i\mathcal D_a\varphi^j.
\end{aligned}
\tag{10}
```

```math
\mathcal D_a\rho'=\left[\begin{aligned}
&2L^{-1}\mathcal D_aN\\
&-2NL^{-2}\mathcal D_aL\\
&+iL^{-3}(\mathcal D_aL_{ij})\bar\varphi^i\varphi^j\\
&+iL^{-3}L_{ij}(\mathcal D_a\bar\varphi^i)\varphi^j\\
&+iL^{-3}L_{ij}\bar\varphi^i\mathcal D_a\varphi^j\\
&-3iL^{-4}(\mathcal D_aL)L_{ij}\bar\varphi^i\varphi^j
\end{aligned}\right]
\tag{11}
```

Every factor of the scalar has been differentiated exactly once. The last two bilinear terms retain their order. The covariant product expression is read with the full parent derivative definitions, not with $`\mathcal D_a\rho'=\partial_a\rho'`$; the independently specified vector derivative is displayed below as the operational definition in the action.

```math
\begin{aligned}\mathcal D_a(-2iL^{-1}\not{\mathcal D}\varphi_i)
={}&2iL^{-2}(\mathcal D_aL)\not{\mathcal D}\varphi_i\\
&-2iL^{-1}\gamma^b\mathcal D_a\mathcal D_b\varphi_i\end{aligned}
\tag{12}
```

This is the product rule for gaugino term 1. The derivative order remains $`\mathcal D_a\mathcal D_b`$; no commutator or curvature term has been discarded.

```math
\begin{aligned}\mathcal D_a(16L^{-1}L_{ij}\chi^j)
={}&-16L^{-2}(\mathcal D_aL)L_{ij}\chi^j\\
&+16L^{-1}(\mathcal D_aL_{ij})\chi^j+16L^{-1}L_{ij}\mathcal D_a\chi^j\end{aligned}
\tag{13}
```

This is the product rule for gaugino term 2. All undifferentiated factors remain in their original order.

```math
\begin{aligned}\mathcal D_a(4L^{-1}\gamma\!\cdot\!T\varphi_i)
={}&-4L^{-2}(\mathcal D_aL)\gamma\!\cdot\!T\varphi_i\\
&+4L^{-1}\gamma^{bc}(\mathcal D_aT_{bc})\varphi_i\\
&+4L^{-1}\gamma\!\cdot\!T\mathcal D_a\varphi_i\end{aligned}
\tag{14}
```

This is the product rule for gaugino term 3. All undifferentiated factors remain in their original order.

```math
\begin{aligned}\mathcal D_a(-2NL^{-3}L_{ij}\varphi^j)
={}&-2L^{-3}(\mathcal D_aN)L_{ij}\varphi^j\\
&+6NL^{-4}(\mathcal D_aL)L_{ij}\varphi^j\\
&-2NL^{-3}(\mathcal D_aL_{ij})\varphi^j-2NL^{-3}L_{ij}\mathcal D_a\varphi^j\end{aligned}
\tag{15}
```

This is the product rule for gaugino term 4. All undifferentiated factors remain in their original order.

```math
\begin{aligned}\mathcal D_a\{2iL^{-3}(\not{\mathcal D}L_{ij})L^{jk}\varphi_k\}
={}&-6iL^{-4}(\mathcal D_aL)(\not{\mathcal D}L_{ij})L^{jk}\varphi_k\\
&+2iL^{-3}\gamma^b(\mathcal D_a\mathcal D_bL_{ij})L^{jk}\varphi_k\\
&+2iL^{-3}(\not{\mathcal D}L_{ij})(\mathcal D_aL^{jk})\varphi_k\\
&+2iL^{-3}(\not{\mathcal D}L_{ij})L^{jk}\mathcal D_a\varphi_k\end{aligned}
\tag{16}
```

This is the product rule for gaugino term 5. The derivative order remains $`\mathcal D_a\mathcal D_b`$; no commutator or curvature term has been discarded.

```math
\begin{aligned}\mathcal D_a(-2iL^{-3}\not E L_{ij}\varphi^j)
={}&6iL^{-4}(\mathcal D_aL)\not E L_{ij}\varphi^j\\
&-2iL^{-3}\gamma^b(\mathcal D_aE_b)L_{ij}\varphi^j\\
&-2iL^{-3}\not E(\mathcal D_aL_{ij})\varphi^j\\
&-2iL^{-3}\not E L_{ij}\mathcal D_a\varphi^j\end{aligned}
\tag{17}
```

This is the product rule for gaugino term 6. All undifferentiated factors remain in their original order.

```math
\begin{aligned}\mathcal D_a\{2iL^{-3}\varphi^j\bar\varphi_i\varphi_j\}
={}&-6iL^{-4}(\mathcal D_aL)\varphi^j\bar\varphi_i\varphi_j\\
&+2iL^{-3}(\mathcal D_a\varphi^j)\bar\varphi_i\varphi_j\\
&+2iL^{-3}\varphi^j(\mathcal D_a\bar\varphi_i)\varphi_j\\
&+2iL^{-3}\varphi^j\bar\varphi_i\mathcal D_a\varphi_j\end{aligned}
\tag{18}
```

This is the product rule for gaugino term 7. All undifferentiated factors remain in their original order.

```math
\begin{aligned}\mathcal D_a\{-6iL^{-5}\varphi^j\bar\varphi_k\varphi_lL^{kl}L_{ij}\}
={}&30iL^{-6}(\mathcal D_aL)\varphi^j\bar\varphi_k\varphi_lL^{kl}L_{ij}\\
&-6iL^{-5}(\mathcal D_a\varphi^j)\bar\varphi_k\varphi_lL^{kl}L_{ij}\\
&-6iL^{-5}\varphi^j(\mathcal D_a\bar\varphi_k)\varphi_lL^{kl}L_{ij}\\
&-6iL^{-5}\varphi^j\bar\varphi_k(\mathcal D_a\varphi_l)L^{kl}L_{ij}\\
&-6iL^{-5}\varphi^j\bar\varphi_k\varphi_l(\mathcal D_aL^{kl})L_{ij}\\
&-6iL^{-5}\varphi^j\bar\varphi_k\varphi_lL^{kl}\mathcal D_aL_{ij}\end{aligned}
\tag{19}
```

This is the product rule for gaugino term 8. All undifferentiated factors remain in their original order.

```math
\begin{aligned}
4\mathcal D_{[\mu}(L^{-1}E_{\nu]})
&=4L^{-1}\mathcal D_{[\mu}E_{\nu]}-4L^{-2}(\mathcal D_{[\mu}L)E_{\nu]},\\
-2\mathcal D_{[\mu}(L^{-3}L_{ij}\bar\varphi^i\gamma_{\nu]}\varphi^j)
&=6L^{-4}(\mathcal D_{[\mu}L)L_{ij}\bar\varphi^i\gamma_{\nu]}\varphi^j\\
&\quad-2L^{-3}(\mathcal D_{[\mu}L_{ij})\bar\varphi^i\gamma_{\nu]}\varphi^j\\
&\quad-2L^{-3}L_{ij}(\mathcal D_{[\mu}\bar\varphi^i)\gamma_{\nu]}\varphi^j
-2L^{-3}L_{ij}\bar\varphi^i\gamma_{[\nu}\mathcal D_{\mu]}\varphi^j.
\end{aligned}
\tag{20}
```

```math
\widehat F'_{\mu\nu}=\left[\begin{aligned}
&4L^{-1}\mathcal D_{[\mu}E_{\nu]}\\
&-4L^{-2}(\mathcal D_{[\mu}L)E_{\nu]}\\
&+2L^{-1}\widehat R_{\mu\nu}^{ij}(V)L_{ij}\\
&-2L^{-3}L_k{}^l\mathcal D_{[\mu}L^{kp}\mathcal D_{\nu]}L_{lp}\\
&+6L^{-4}(\mathcal D_{[\mu}L)L_{ij}\bar\varphi^i\gamma_{\nu]}\varphi^j\\
&-2L^{-3}(\mathcal D_{[\mu}L_{ij})\bar\varphi^i\gamma_{\nu]}\varphi^j\\
&-2L^{-3}L_{ij}(\mathcal D_{[\mu}\bar\varphi^i)\gamma_{\nu]}\varphi^j\\
&-2L^{-3}L_{ij}\bar\varphi^i\gamma_{[\nu}\mathcal D_{\mu]}\varphi^j\\
&-iL^{-1}\bar\varphi^i\widehat R_{\mu\nu i}(Q)
\end{aligned}\right]
\tag{21}
```

The derivative of $`L^{-3}`$ multiplies $`-2`$ by $`-3`$, giving $`+6`$. The last bilinear derivative is $`\bar\varphi^i(\gamma_ u\mathcal D_\mu-\gamma_\mu\mathcal D_ u)\varphi^j/2`$; the displayed $`[ u\,\mu]`$ order preserves that sign. Gamma compatibility has removed only $`\mathcal D_\mu\gamma_ u`$, not a spinor derivative.

### 4.4 Restrict the parent derivatives, retaining their connections

<!-- ASSERT_CONVENTION: metric_signature=mostly_plus (-++++); natural_units=hbar=c=1; gauge_slice=R2-GOLD7-GAUGE-v1; spinor_bar=NW-SE-transpose; fermion_order=full_source_map; background=gauged_Coomans -->

```math
\begin{aligned}
\mathcal D_\mu L_{ij}&=\partial_\mu L_{ij}+2V_{\mu(i}{}^kL_{j)k}
-i\bar\psi_{\mu(i}\varphi_{j)},\\
\mathcal D_\mu\varphi_i
&=(\partial_\mu+\tfrac14\omega_\mu{}^{ab}\gamma_{ab})\varphi_i
-V_{\mu i}{}^j\varphi_j\\
&\quad-\tfrac i2\gamma^a(\mathcal D_aL_{ij})\psi_\mu{}^j
+\tfrac i2\not E\psi_{\mu i}-\tfrac12N\psi_{\mu i}\\
&\quad-L_{ij}\gamma\!\cdot\!T\psi_\mu{}^j+3L_{ij}\phi_\mu{}^j.
\end{aligned}
\tag{22}
```

This is the older locked derivative convention, including the $`-i/2`$ lower-index triplet derivative term. The defining-gaugino gauge sets none of the terms in these two lines to zero. The dependent $`S`$ connection is $`\phi_\mu{}^i`$, distinct from the original linear fermion $`\varphi_i`$.

```math
\begin{aligned}
\mathcal D_\mu\rho'&=\partial_\mu\rho'-\tfrac i2\bar\psi_\mu{}^i\lambda'_i,\\
\mathcal D_\mu\lambda'_i
&=(\partial_\mu+\tfrac14\omega_\mu{}^{ab}\gamma_{ab})\lambda'_i
-V_{\mu i}{}^j\lambda'_j
+\tfrac14\gamma\!\cdot\!\widehat F'\psi_{\mu i}\\
&\quad+\tfrac i2(\not{\mathcal D}\rho')\psi_{\mu i}
-Y'_{ij}\psi_\mu{}^j-\rho'\gamma\!\cdot\!T\psi_{\mu i}-\rho'\phi_{\mu i},\\
\Box_c\rho'&=(\partial^a+\omega_b{}^{ba})\mathcal D_a\rho'
-\tfrac i2\bar\psi_a{}^i\mathcal D^a\lambda'_i
-2\rho'\bar\psi_a{}^i\gamma^a\chi_i\\
&\quad+\tfrac12\bar\psi_a{}^i\gamma^a\gamma\!\cdot\!T\lambda'_i
+\tfrac12\bar\phi_a{}^i\gamma^a\lambda'_i+2f_a{}^a\rho'.
\end{aligned}
\tag{23}
```

These equations, followed by literal replacement of each argument by Section 4.1, specify the differentiated composite in the density. The $`-Y'_{ij}\psi_\mu{}^j`$ sign follows from the explicit epsilon calculation. The $`2f_a{}^a\rho'`$ term is a conformal-box contribution, so even a constant scalar cannot justify discarding it. The derivative product rules above expand the covariant composite expressions; they do not independently certify their entire local transformation law.

### 4.5 Derive the local primed potential on the aligned triplet patch

<!-- ASSERT_CONVENTION: metric_signature=mostly_plus (-++++); natural_units=hbar=c=1; gauge_slice=R2-GOLD7-GAUGE-v1; spinor_bar=NW-SE-transpose; fermion_order=full_source_map; background=gauged_Coomans -->
An ordinary BF potential is required by Step 4. The hatted strength alone does not permit omitting its gravitino completions. Use the stated gauge locally, **after** preserving the unrestricted map above:

```math
\begin{aligned}
L_{ij}&=\frac{L}{\sqrt2}\delta_{ij},\qquad L>0,\\
V_\mu{}^{ij}&=V'_\mu{}^{ij}+\frac12\delta^{ij}V_\mu,
\qquad \delta_{ij}V'_\mu{}^{ij}=0,\qquad V_\mu=\delta_{ij}V_\mu{}^{ij},\\
\mathcal D_\mu L_{ij}
&=\frac{\delta_{ij}}{\sqrt2}\partial_\mu L
+\sqrt2L V'_{\mu(i}{}^k\delta_{j)k}
-i\bar\psi_{\mu(i}\varphi_{j)}.
\end{aligned}
\tag{24}
```

The first two lines are Gold (25),(27), PDF/printed p. 14, visually inspected for this step. $`V_\mu`$ and $`V'_\mu{}^{ij}`$ are the source trace and traceless connection; their primes do not label another matter multiplet. The connection in the third line is not zero even at constant $`L`$. $`\delta_{ij}`$ is the fixed gauge direction and is not a new covariantly constant $`SU(2)`$ tensor.

The ordinary orientation term of Özkan (3.16) is different from the supercovariant orientation term. Its alignment reduction is

```math
\begin{aligned}
L_k{}^l\partial_{[\mu}L^{kp}\partial_{\nu]}L_{lp}
&=\frac12L_k{}^l\delta^{kp}\delta_{lp}
 (\partial_{[\mu}L)(\partial_{\nu]}L)=0,\\
4\partial_{[\mu}\big(L^{-1}E_{\nu]}+L^{-1}V_{\nu]}{}^{ij}L_{ij}\big)
&=2\partial_{[\mu}\big(2L^{-1}E_{\nu]}+\sqrt2V_{\nu]}\big).
\end{aligned}
\tag{25}
```

The first zero follows already from the antisymmetrized product of the same even gradient, not from setting $`\mathcal D L_{ij}=0`$. It fixes the bosonic potential. The explicit differentiated fermion bilinear in the full strength fixes its bilinear-potential term. The $`\partial\psi_\mu`$ part of $`-iL^{-1}\bar\varphi\widehat R(Q)`$ fixes a second fermionic term. This produces the candidate to be checked:

```math
A'_\mu\ \stackrel{\rm candidate}{=}\
2L^{-1}E_\mu+\sqrt2V_\mu
-L^{-3}L_{ij}\bar\varphi^i\gamma_\mu\varphi^j
-iL^{-1}\bar\varphi^i\psi_{\mu i}.
\tag{26}
```

Expand its ordinary curl before comparing it with the supercovariant map. In a locally inertial frame at the evaluation point, $`\partial_\mu\gamma_\nu=0`$, while the gravitino contorsion is retained in the covariant side:
```math
\begin{aligned}
2\partial_{[\mu}A'_{\nu]}\big|_{\rm candidate}
={}&4L^{-1}\partial_{[\mu}E_{\nu]}
-4L^{-2}(\partial_{[\mu}L)E_{\nu]}
+2\sqrt2\partial_{[\mu}V_{\nu]}\\
&+6L^{-4}(\partial_{[\mu}L)L_{ij}\bar\varphi^i\gamma_{\nu]}\varphi^j
-2L^{-3}(\partial_{[\mu}L_{ij})\bar\varphi^i\gamma_{\nu]}\varphi^j\\
&-2L^{-3}L_{ij}(\partial_{[\mu}\bar\varphi^i)\gamma_{\nu]}\varphi^j
-2L^{-3}L_{ij}\bar\varphi^i\gamma_{[\nu}\partial_{\mu]}\varphi^j\\
&+2iL^{-2}(\partial_{[\mu}L)\bar\varphi^i\psi_{\nu]i}
-2iL^{-1}(\partial_{[\mu}\bar\varphi^i)\psi_{\nu]i}
-2iL^{-1}\bar\varphi^i\partial_{[\mu}\psi_{\nu]i}.
\end{aligned}
\tag{27}
```

The two first-gradient terms from the bilinear coefficient are kept separately: they come from $`L^{-3}`$ and $`L_{ij}`$. The complete comparison, rather than setting a hatted strength equal to an ordinary curl, is

```math
\widehat F'_{\mu\nu}
+\bar\psi_{[\mu}{}^i\gamma_{\nu]}\lambda'_i
-\frac i2\rho'\bar\psi_{[\mu}{}^i\psi_{\nu]i}
-2\partial_{[\mu}A'_{\nu]}\big|_{\rm candidate}\ \stackrel{?}{=}\ 0.
\tag{28}
```

For the covariant side, use the following complete parent definitions. At the evaluation point $`E_\nu=e_\nu{}^aE_a`$ with $`e_\nu{}^a=\delta_\nu{}^a`$, so the explicitly displayed $`\omega E`$ term below is the tangent-vector Lorentz term. Away from the point the corresponding vielbeins and ordinary Christoffel conversion are restored; $`\partial_\mu E_\nu+\omega_{\mu\nu}{}^bE_b`$ is not a replacement for a general world-vector covariant derivative.
```math
\begin{aligned}
\mathcal D_\mu L^{ij}
&=\partial_\mu L^{ij}+2V_\mu{}^{(i}{}_kL^{j)k}
-i\bar\psi_\mu{}^{(i}\varphi^{j)},\\
\mathcal D_\mu\varphi^i
&=\partial_\mu\varphi^i+\frac14\omega_\mu{}^{ab}\gamma_{ab}\varphi^i
-V_\mu{}^{ij}\varphi_j
+\frac i2\gamma^a\mathcal D_aL^{ij}\psi_{\mu j}
+\frac i2\not E\psi_\mu{}^i\\
&\quad-\frac12N\psi_\mu{}^i
+\gamma\!\cdot\!T L^{ij}\psi_{\mu j}-3L^{ij}\phi_{\mu j},\\
\mathcal D_\mu E_\nu
&=\partial_\mu E_\nu+\omega_{\mu\nu}{}^bE_b
+\frac i2\bar\psi_\mu\gamma_{\nu b}\mathcal D^b\varphi
+2\bar\psi_\mu\gamma^b\varphi T_{b\nu}
+2\bar\phi_\mu\gamma_\nu\varphi .
\end{aligned}
\tag{29}
```

```math
\begin{aligned}
\widehat R_{\mu\nu}{}^i(Q)
&=2\partial_{[\mu}\psi_{\nu]}{}^i
+\frac12\omega_{[\mu}{}^{ab}\gamma_{ab}\psi_{\nu]}{}^i
-2V_{[\mu}{}^{ij}\psi_{\nu]j}\\
&\quad+2i\gamma\!\cdot\!T\gamma_{[\mu}\psi_{\nu]}{}^i
-2i\gamma_{[\mu}\phi_{\nu]}{}^i,\\
\widehat R_{\mu\nu}{}^{ij}(V)
&=2\partial_{[\mu}V_{\nu]}{}^{ij}
-2V_{[\mu}{}^{k(i}V_{\nu]k}{}^{j)}
-3i\bar\phi_{[\mu}{}^{(i}\psi_{\nu]}{}^{j)}\\
&\quad-8\bar\psi_{[\mu}{}^{(i}\gamma_{\nu]}\chi^{j)}
-i\bar\psi_{[\mu}{}^{(i}\gamma\!\cdot\!T\psi_{\nu]}{}^{j)}.
\end{aligned}
\tag{30}
```

```math
\omega_\mu{}^{ab}\big|_{\partial e=b=0}
=\frac12\bar\psi^{[a}\gamma^{b]}\psi_\mu
+\frac14\bar\psi^a\gamma_\mu\psi^b.
\tag{31}
```

This is the fermionic contorsion at the chosen point. The original linear fermion is kept in all source derivatives. The lower-spinor derivative in Section 4.4 is the epsilon lowering of the upper-spinor rule just displayed.
#### Explicit cancellation of the background and derivative terms

The following cancellations use arbitrary full $`T,\chi,\phi_\mu`$. Consequently their algebra does not assume a truncation of the gauged expressions that will later occupy those slots.

For $`\chi`$, only the displayed $`\widehat R(V)`$ term and the $`16L^{-1}L_{ij}\chi^j`$ part of $`\lambda'_i`$ contribute:

```math
\begin{aligned}
2L^{-1}L_{ij}\widehat R_{\mu\nu}{}^{ij}(V)\big|_\chi
&=-16L^{-1}L_{ij}\bar\psi_{[\mu}{}^i\gamma_{\nu]}\chi^j,\\
\bar\psi_{[\mu}\gamma_{\nu]}\lambda'\big|_{\lambda'\supset\chi}
&=+16L^{-1}L_{ij}\bar\psi_{[\mu}{}^i\gamma_{\nu]}\chi^j.
\end{aligned}
\tag{32}
```

Their sum is zero without a Fierz rearrangement.

The terms linear in $`\phi_\mu`$ and $`\varphi`$ have coefficients $`8,-6,-2`$ from the explicit S term of $`\mathcal D E`$, the bilinear curl, and $`\bar\varphi\widehat R(Q)`$ respectively:

```math
\begin{aligned}
4L^{-1}\mathcal D_{[\mu}E_{\nu]}\big|_{\phi\varphi}
&=8L^{-1}\bar\phi_{[\mu}\gamma_{\nu]}\varphi,\\
-2\mathcal D_{[\mu}(L^{-3}L_{ij}\bar\varphi^i\gamma_{\nu]}\varphi^j)
 \big|_{\phi\varphi}
&=-6L^{-1}\bar\phi_{[\mu}\gamma_{\nu]}\varphi,\\
-iL^{-1}\bar\varphi\widehat R_{\mu\nu}(Q)\big|_{\phi\varphi}
&=-2L^{-1}\bar\phi_{[\mu}\gamma_{\nu]}\varphi.
\end{aligned}
\tag{33}
```

For the middle line insert $`\mathcal D_\mu\varphi^i|_\phi=-3L^{ij}\phi_{\mu j}`$ into both differentiated spinors and use $`L_{ij}L^{jk}=L^2\delta_i{}^k/2`$. Each differentiated spinor gives $`+3\bar\phi_\mu\gamma_\nu\varphi/(2L)`$ before the overall curl coefficient $`-2`$. For the last line use the contracted rank-one flip followed by the antisymmetry in $`\mu,\nu`$. Therefore $`(8-6-2)L^{-1}\bar\phi_{[\mu}\gamma_{\nu]}\varphi=0`$.

The remaining $`\phi\psi L`$ terms cancel by one Clifford product and the fixed-index scalar flip:

```math
\begin{aligned}
&6iL^{-1}L_{ij}\bar\psi_{[\mu}{}^i
 (\gamma_{\nu]a}-\gamma_{\nu]}\gamma_a)\phi^{aj}
-6iL^{-1}L_{ij}\bar\phi_{[\mu}{}^i\psi_{\nu]}{}^j\\
&=-6iL^{-1}L_{ij}\bar\psi_{[\mu}{}^i\phi_{\nu]}{}^j
-6iL^{-1}L_{ij}\bar\phi_{[\mu}{}^i\psi_{\nu]}{}^j=0.
\end{aligned}
\tag{34}
```

The first coefficient comes from $`\mathcal D E`$ through $`\mathcal D\varphi|_\phi`$, the second from $`\lambda'|_{\mathcal D\varphi,\phi}`$, and the last from $`\widehat R(V)|_\phi`$. In the last equality $`L_{ij}`$ is symmetric and $`\bar\psi_\mu{}^i\phi_\nu{}^j=\bar\phi_\nu{}^j\psi_\mu{}^i`$, followed by exchanging the antisymmetric world pair. Thus a dependent $`\phi_\mu`$ can be substituted afterwards without changing the identity.

For the $`T\psi\varphi`$ terms, the direct $`T`$ term of $`\mathcal D E`$ contributes $`8L^{-1}\bar\psi_{[\mu}\gamma^b\varphi T_{b\nu]}`$. The bilinear curl contributes $`-2L^{-1}\bar\psi_{[\mu}\gamma\!\cdot\!T\gamma_{\nu]}\varphi`$, the Q curvature contributes $`-2L^{-1}\bar\psi_{[\mu}\gamma_{\nu]}\gamma\!\cdot\!T\varphi`$, and the explicit $`4L^{-1}\gamma\!\cdot\!T\varphi`$ in $`\lambda'`$ contributes $`+4`$ times the latter matrix structure. Hence

```math
\begin{aligned}
&8L^{-1}\bar\psi_{[\mu}\gamma^b\varphi T_{b\nu]}
+2L^{-1}\bar\psi_{[\mu}
 [\gamma_{\nu]},\gamma\!\cdot\!T]\varphi\\
&=8L^{-1}\bar\psi_{[\mu}\gamma^b\varphi T_{b\nu]}
+8L^{-1}\bar\psi_{[\mu}\gamma^b\varphi T_{\nu]b}=0,
\end{aligned}
\tag{35}
```

where $`[\gamma_\nu,\gamma^{ab}]T_{ab}=4T_{\nu b}\gamma^b`$ follows by two Clifford anticommutations and $`T_{ab}=-T_{ba}`$. The other $`T`$ terms use $`\mathcal D\varphi|_T`$ inside $`\mathcal D E`$ and $`\lambda'`$:

```math
\begin{aligned}
&2iL^{-1}L_{ij}\bar\psi_{[\mu}{}^i
 (\gamma_{\nu]}\gamma^a-\gamma_{\nu]}{}^a)
 \gamma\!\cdot\!T\psi_a{}^j
-2iL^{-1}L_{ij}\bar\psi_{[\mu}{}^i\gamma\!\cdot\!T\psi_{\nu]}{}^j\\
&=2iL^{-1}L_{ij}\bar\psi_{[\mu}{}^i\gamma\!\cdot\!T\psi_{\nu]}{}^j
-2iL^{-1}L_{ij}\bar\psi_{[\mu}{}^i\gamma\!\cdot\!T\psi_{\nu]}{}^j=0.
\end{aligned}
\tag{36}
```

The last term is exactly $`2L^{-1}L_{ij}\widehat R(V)^{ij}|_T`$.

The ordinary $`\partial\varphi`$ terms coming from $`\mathcal D E`$ and $`\lambda'`$ combine as

```math
\begin{aligned}
2iL^{-1}\bar\psi_{[\mu}
 (\gamma_{\nu]}{}^a-\gamma_{\nu]}\gamma^a)
 \partial_a\varphi
&=-2iL^{-1}\bar\psi_{[\mu}\partial_{\nu]}\varphi\\
&=-2iL^{-1}(\partial_{[\mu}\bar\varphi)\psi_{\nu]}.
\end{aligned}
\tag{37}
```

The first equality is $`\gamma_\nu\gamma^a=\gamma_\nu{}^a+\delta_\nu{}^a`$; the second uses the contracted rank-zero flip and antisymmetrizes the world indices. The displayed ordinary $`\partial\varphi`$ identity is the $`\partial\varphi`$ part of $`2\partial_{[\mu}(-iL^{-1}\bar\varphi\psi_{\nu]})`$. All other ordinary $`\partial\varphi`$ factors are precisely the derivative of the candidate's explicit bilinear. The independent ordinary $`\partial\psi`$ term is

```math
-iL^{-1}\bar\varphi\widehat R_{\mu\nu}(Q)\big|_{\partial\psi}
=-2iL^{-1}\bar\varphi\partial_{[\mu}\psi_{\nu]},
\tag{38}
```

which is its other product-rule term. No other independent $`\partial\psi`$ term remains after the displayed $`\chi`$, $`\phi_\mu`$ and $`T`$ cancellations cancel the S connection.

The $`N\psi\varphi`$ part of the differentiated bilinear is $`+2NL^{-3}L_{ij}\bar\psi_{[\mu}{}^i\gamma_{\nu]}\varphi^j`$; the explicit $`-2NL^{-3}L_{ij}\varphi^j`$ term of $`\lambda'_i`$ cancels it. The remaining $`N\psi\psi`$ terms are

```math
\begin{aligned}
iNL^{-1}\bar\psi_{[\mu}
(\gamma_{\nu]}\gamma^a-\gamma_{\nu]}{}^a)\psi_a
-iNL^{-1}\bar\psi_{[\mu}\psi_{\nu]}
=0.
\end{aligned}
\tag{39}
```

The final coefficient comes from the $`2N/L`$ part of $`\rho'`$ in the ordinary-strength completion. These identities explain directly why the potential contains no explicit $`N,T,\chi`$, or $`\phi_\mu`$.

#### Quartic terms, Clifford completeness and the remaining coefficient tensor

The exact quartic coefficient test now assigns an independent generator to **each** of the 40 gravitino and eight $`\varphi`$ components. It therefore includes $`\psi^3\varphi`$ as well as $`\psi^2\varphi^2`$ and $`\psi\varphi^3`$; these terms cannot vanish merely from too few generators. The universal $`\phi,T,\chi`$ dependence cancels in the displayed $`\chi`$, $`\phi_\mu`$ and $`T`$ cancellations, so those slots can be zero in this separate quartic coefficient test without discarding their gauged completions.

For readability the following projection notation denotes fermion order of an existing field or derivative, not a new field. The full expressions used to generate the quartic blocks are

```math
\begin{aligned}
(\mathcal D_\mu L_{ij})_{(2)}
&=-i\bar\psi_{\mu(i}\varphi_{j)},\\
(\mathcal D_\mu\varphi_i)_{(3)}
&=\frac14\omega_\mu{}^{ab}|_{(2)}\gamma_{ab}\varphi_i
-\frac12\gamma^a\bar\psi_{a(i}\varphi_{j)}\psi_\mu{}^j,\\
\lambda'_i|_{(3)}
&=-2i\gamma^a(\mathcal D_a\varphi_i)_{(3)}
+2\gamma^a\bar\psi_{a(i}\varphi_{j)}L^{jk}\varphi_k\\
&\quad+2i\varphi^j\bar\varphi_i\varphi_j
-6i\varphi^j\bar\varphi_k\varphi_lL^{kl}L_{ij},\\
\rho'|_{(2)}&=iL_{ij}\bar\varphi^i\varphi^j.
\end{aligned}
\tag{40}
```

The quartic-projection equation above is stated at $`L=1`$ for the exact coefficient test. Its first line enters both the upper and lower triplets by the two explicit epsilon matrices. The coefficient $`-1/2`$ in the second line is $`(-i/2)(-i)`$; the coefficient $`+2`$ in the third line is $`(2i)(-i)`$. No Grassmann factors have been moved in these products.

The six nonzero quartic source blocks, before addition, are

```math
\begin{aligned}
&2i\bar\psi_{[\mu}\gamma_{\nu]a}
 (\mathcal D^a\varphi)_{(3)},\\
&-2L_k{}^l(\mathcal D_{[\mu}L^{kp})_{(2)}
 (\mathcal D_{\nu]}L_{lp})_{(2)},\\
&-2\big[(\mathcal D_{[\mu}L_{ij})_{(2)}
-3L_{ij}L^{kl}(\mathcal D_{[\mu}L_{kl})_{(2)}\big]
 \bar\varphi^i\gamma_{\nu]}\varphi^j\\
&\qquad-2L_{ij}\big[
 \overline{(\mathcal D_{[\mu}\varphi^i)_{(3)}}\gamma_{\nu]}\varphi^j
+\bar\varphi^i\gamma_{[\nu}(\mathcal D_{\mu]}\varphi^j)_{(3)}\big],\\
&-\frac i2\bar\varphi\omega_{[\mu}{}^{ab}|_{(2)}\gamma_{ab}\psi_{\nu]},\\
&\bar\psi_{[\mu}\gamma_{\nu]}\lambda'|_{(3)},\\
&+\frac12L_{ij}\bar\varphi^i\varphi^j\bar\psi_{[\mu}\psi_{\nu]}.
\end{aligned}
\tag{41}
```

In the third block each $`[\mu,\nu]`$ acts on the whole differentiated-bilinear expression, as in the differentiated field-strength formula in Section 4.3. These blocks retain all connection terms from the contorsion formula above, not only the explicit cubic terms of $`\lambda'`$. They are the exact polynomial inputs behind the reported coefficient counts.

The applicable Fierz basis and its normalization can be obtained without a remembered coefficient. Orthogonality gives

```math
\begin{aligned}
\mathop{\mathrm{tr}}\nolimits1&=4,&
\mathop{\mathrm{tr}}\nolimits(\gamma^a\gamma^b)&=4\eta^{ab},\\
\mathop{\mathrm{tr}}\nolimits(\gamma^{ab}\gamma^{cd})
&=4(\eta^{ad}\eta^{bc}-\eta^{ac}\eta^{bd}),\\
M&=\frac14\mathop{\mathrm{tr}}\nolimits M
+\frac14\gamma_a\mathop{\mathrm{tr}}\nolimits(\gamma^aM)
-\frac18\gamma_{ab}\mathop{\mathrm{tr}}\nolimits(\gamma^{ab}M).
\end{aligned}
\tag{42}
```

For $`M=\zeta\bar\xi`$, a trace moves one odd component past another, so each trace is minus the corresponding $`\bar\xi\Gamma\zeta`$. Therefore

```math
\zeta\bar\xi
=-\frac14(\bar\xi\zeta)1
-\frac14(\bar\xi\gamma^a\zeta)\gamma_a
+\frac18(\bar\xi\gamma^{ab}\zeta)\gamma_{ab}.
\tag{43}
```

The $`1/8`$ has both the trace sign and the antisymmetric rank-two normalization from the trace-completeness equation above. Equation the Fierz equation above agrees with the inspected Özkan–Pang (2013) Appendix A, Eq. (A.5). The program verifies the trace-completeness equation above for all 16 matrix units, so this completeness identity is checked on the full $`4\times4`$ matrix space. The coefficient implementation does not assume a Fierz cancellation: it evaluates both sides of the full curl directly in the complete Clifford representation and exterior algebra, preserving every component coefficient.

The independent zero/two-fermion test uses **336 independent odd generators**: 40 gravitino components, eight $`\varphi`$ components, 40 ordinary $`\partial\varphi`$ components, 200 ordinary $`\partial\psi`$ components, 40 S-connection components, and eight $`\chi`$ components. Every component of $`E,N,T,V,\partial L,\partial E,\partial V`$ is an independent commuting symbol. Projecting this second calculation to degrees zero and two is a coefficient separation only; the exhaustive degree-four calculation above is separate. No higher fermion order can enter the potential-curl identity before replacing the universal Weyl slots, and those full slot contributions have the analytic cancellations the displayed $`\chi`$, $`\phi_\mu`$ and $`T`$ cancellations.

For component $`(1,2)`$ the exhaustive quartic blocks contain respectively $`3056,104,792,1728,4568,32`$ nonzero exterior coefficients before addition; their sum has none. The exhaustive zero/two calculation produces 73 nonzero coefficients on each side of the ordinary/hatted-strength comparison, equal as symbolic polynomials. These are complete coefficient tests at the stated point, not evaluations at chosen spinor values. The report records the separate all-component run as well.

#### Explicit $`E`$, $`V`$, and scalar-gradient collections

For the $`E\psi\psi`$ terms, $`\mathcal D\varphi|_E=i\not E\psi/2`$ enters $`\mathcal D E`$ and $`\lambda'`$ with opposite antisymmetric-gamma terms. Their sum is

```math
L^{-1}\bar\psi_{[\mu}
(\gamma_{\nu]}\gamma^a-\gamma_{\nu]}{}^a)\not E\psi_a
=L^{-1}\bar\psi_{[\mu}\not E\psi_{\nu]}.
\tag{44}
```

The spin-connection part of the constrained-vector curl cancels this. With $`\partial e=0`$, insert the contorsion above, expand its first antisymmetrization, and use the contracted rank-one flip to obtain

```math
\begin{aligned}
4\omega_{[\mu\nu]}{}^a
&=2(\eta_{\nu\nu}\omega_\mu{}^{\nu a}
-\eta_{\mu\mu}\omega_\nu{}^{\mu a})
=-\bar\psi_{[\mu}\gamma^a\psi_{\nu]},\\
4L^{-1}\omega_{[\mu\nu]}{}^aE_a
&=-L^{-1}\bar\psi_{[\mu}\not E\psi_{\nu]}.
\end{aligned}
\tag{45}
```

There is no sum on the diagonal metric labels in the first line. It is the conventional torsion relation in this local frame. The cancellation (44)+(45) explains why discarding contorsion is an invalid simplification.

For the $`E\psi\varphi`$ terms, $`\mathcal D_\mu L|_{\psi\varphi}=-iL^{-1}L_{ij}\bar\psi_\mu{}^i\varphi^j`$ gives $`+4iL^{-3}L_{ij}\bar\psi_{[\mu}{}^i\varphi^jE_{\nu]}`$ from $`4\mathcal D_{[\mu}(L^{-1}E_{\nu]})`$. The differentiated bilinear and the explicit $`-2iL^{-3}L_{ij}\not E\varphi^j`$ in $`\lambda'_i`$ give

```math
\begin{aligned}
&-2iL^{-3}L_{ij}\bar\psi_{[\mu}{}^i
(\not E\gamma_{\nu]}+\gamma_{\nu]}\not E)\varphi^j\\
&=-4iL^{-3}L_{ij}\bar\psi_{[\mu}{}^i\varphi^jE_{\nu]}.
\end{aligned}
\tag{46}
```

Thus all nondifferentiated $`E`$ contributions cancel. The surviving $`\partial E`$ and ordinary $`\partial L\,E`$ terms are exactly $`4\partial_{[\mu}(L^{-1}E_{\nu]})`$, already in the proposed potential.

For the connection algebra, write $`[V_\mu{}^{ij}]`$ for the symmetric matrix of the existing connection components (while $`V_\mu`$ without indices remains its scalar trace) and use $`\varepsilon=\left(\begin{smallmatrix}0&1\\-1&0\end{smallmatrix}\right)`$. Within square matrix brackets, $`i,j`$ label matrix entries rather than Einstein sums; the indices outside the brackets label the resulting component. Triplet alignment gives

```math
\begin{aligned}
(\mathcal D_\mu L^{ij})_V
&=\frac L{\sqrt2}([V_\mu{}^{ij}]\varepsilon-\varepsilon [V_\mu{}^{ij}])^{ij},\\
(\mathcal D_\mu L_{ij})_V
&=\frac L{\sqrt2}(\varepsilon [V_\mu{}^{ij}]-[V_\mu{}^{ij}]\varepsilon)_{ij},\\
L^{ij}(\mathcal D_\mu L_{ij})_V&=0,\\
\widehat R_{\mu\nu}(V)\big|_{V^2}
&=[V_\mu{}^{ij}]\varepsilon [V_\nu{}^{ij}]-[V_\nu{}^{ij}]\varepsilon [V_\mu{}^{ij}].
\end{aligned}
\tag{47}
```

The scalar equation is the trace of a commutator. For arbitrary symmetric matrices $`[V_\mu{}^{ij}]=\left(\begin{smallmatrix}a&b\\b&c\end{smallmatrix}\right)`$ and $`[V_\nu{}^{ij}]=\left(\begin{smallmatrix}d&e\\e&f\end{smallmatrix}\right)`$, multiplying the four $`2\times2`$ matrices gives

```math
\mathop{\mathrm{tr}}\nolimits\{\varepsilon[[\varepsilon,[V_\mu{}^{ij}]],[\varepsilon,[V_\nu{}^{ij}]]]\}
=4\mathop{\mathrm{tr}}\nolimits\{\varepsilon[[V_\mu{}^{ij}],[V_\nu{}^{ij}]]\}.
\tag{48}
```

Indeed $`\mathop{\mathrm{tr}}\nolimits(\varepsilon[[V_\mu{}^{ij}],[V_\nu{}^{ij}]])=-2[ae+bf-bd-ce]`$, and the left side is $`-8[ae+bf-bd-ce]`$. The $`V^2`$ term from the SU(2) curvature is $`-\sqrt2\mathop{\mathrm{tr}}\nolimits(\varepsilon[[V_\mu{}^{ij}],[V_\nu{}^{ij}]])`$. Substitution of (47) into the orientation term gives the left side of (48) divided by $`2\sqrt2`$, hence $`+\sqrt2\mathop{\mathrm{tr}}\nolimits(\varepsilon[[V_\mu{}^{ij}],[V_\nu{}^{ij}]])`$. Their sum is zero. The remaining ordinary curvature is $`2\sqrt2\partial_{[\mu}V_{\nu]}`$.

The pure SU(2) connections in the differentiated bilinear cancel because all its SU(2) indices are contracted:

```math
\begin{aligned}
0={}&(\mathcal D_\mu L_{ij})_V\bar\varphi^i\gamma_\nu\varphi^j\\
&+L_{ij}\big[
 (\mathcal D_\mu\bar\varphi^i)_V\gamma_\nu\varphi^j
+\bar\varphi^i\gamma_\nu(\mathcal D_\mu\varphi^j)_V
\big].
\end{aligned}
\tag{49}
```

Here the subscript $`V`$ in the spinor terms means only the direct SU(2) connection, excluding the $`\mathcal D L\,\psi`$ term. Substituting $`(\mathcal D\varphi^i)_V=-V^{ij}\varphi_j`$ and its lower/upper-index conjugate gives the negative of the first line twice with its $`1/2`$ symmetrization, proving (49). The remaining direct $`V\varphi`$ terms from $`\mathcal D E`$ and $`\lambda'`$ are $`-2iL^{-1}\bar\psi_{[\mu}{}^iV_{\nu]ij}\varphi^j`$. The Q curvature supplies $`-2iL^{-1}\bar\varphi^i V_{[\mu ij}\psi_{\nu]}{}^j=+2iL^{-1}\bar\psi_{[\mu}{}^iV_{\nu]ij}\varphi^j`$, by its symmetric SU(2) indices, the fixed-index scalar flip, and exchanging the antisymmetric world pair. Their sum is zero.

It remains to collect the $`\mathcal D L\,\psi`$ terms and the explicit $`\mathcal D L\,\varphi`$ term of $`\lambda'`$. This handles the ordinary scalar gradient and the transverse SU(2) connection together. Use the following purely algebraic identity for two arbitrary symmetric triplets:

```math
L_{ik}X^{kj}+X_{ik}L^{kj}
=\delta_i{}^j L_{kl}X^{kl}.
\tag{50}
```

For $`[L_{ij}]=\left(\begin{smallmatrix}a&b\\b&c\end{smallmatrix}\right)`$ and $`X=\left(\begin{smallmatrix}d&e\\e&f\end{smallmatrix}\right)`$, raising both indices replaces each matrix by its adjugate. Their two products sum to $`(af+cd-2be)1`$, which equals the displayed contraction. The letter $`X`$ in (50) is an arbitrary matrix used to prove this identity, not an added physical field.

From the bilinear curl and the explicit $`\mathcal D L\,\varphi`$ term of $`\lambda'`$, the anticommutator $`\gamma^a\gamma_\nu+\gamma_\nu\gamma^a=2\delta_\nu{}^a`$ gives

```math
4iL^{-3}\bar\psi_{[\mu}{}^i
 (\mathcal D_{\nu]}L_{ij})_{\rm bos}L^{jk}\varphi_k.
\tag{51}
```

Now insert $`\mathcal D L|_{(2)}=-i\bar\psi_{(i}\varphi_{j)}`$ into either factor of the orientation term, retaining the other factor at bosonic order. Raise the triplet indices with the two epsilon matrices, apply (50), and the two ordered cross terms become

```math
\begin{aligned}
&2iL^{-3}L_k{}^l\big[
 (\mathcal D_{[\mu}L^{kp})_{\rm bos}\bar\psi_{\nu](l}\varphi_{p)}
+\bar\psi_{[\mu}{}^{(k}\varphi^{p)}
 (\mathcal D_{\nu]}L_{lp})_{\rm bos}\big]\\
&=-4iL^{-3}\bar\psi_{[\mu}{}^i
 (\mathcal D_{\nu]}L_{ij})_{\rm bos}L^{jk}\varphi_k
+2iL^{-3}\bar\psi_{[\mu}\varphi\,
 L^{ij}(\mathcal D_{\nu]}L_{ij})_{\rm bos}.
\end{aligned}
\tag{52}
```

This identity also has a separate exact exterior-coefficient check with an arbitrary symmetric $`X_{ij}=(\mathcal D_\nu L_{ij})_{\rm bos}`$ and independent components of one gravitino and $`\varphi`$; its residual has zero coefficients. In (51)+(52) the first terms cancel. Equation (47) removes the connection from the trace, and $`L^{ij}\partial_\nu L_{ij}=L\partial_\nu L`$, leaving

```math
2iL^{-2}\bar\psi_{[\mu}\varphi\,\partial_{\nu]}L
=2iL^{-2}(\partial_{[\mu}L)\bar\varphi\psi_{\nu]}.
\tag{53}
```

This is precisely the derivative of $`L^{-1}`$ in $`2\partial_{[\mu}(-iL^{-1}\bar\varphi\psi_{\nu]})`$; the two other product-rule terms are the two displayed ordinary spinor-derivative identities. The $`\psi\psi\mathcal D L|_{\rm bos}`$ terms left by the same Clifford anticommutation are proportional to $`\bar\psi_{[\mu}{}^i\gamma^a\psi_{\nu]}{}^j(\mathcal D_aL_{ij})_{\rm bos}`$. They vanish because the triplet is symmetric in $`i,j`$, while the fixed-index rank-one flip makes its spinor bilinear symmetric in the combined exchange $`(\mu,i)\leftrightarrow(\nu,j)`$. The explicit world antisymmetrization therefore gives zero.

Finally, on an aligned triplet $`\partial_\mu(L^{-3}L_{ij})=-2L^{-4}L_{ij}\partial_\mu L`$. The ordinary derivative of this coefficient is already retained on both sides of the bilinear curl. This accounts for every scalar-gradient source: the $`L^{-1}E`$ curl, the explicit bilinear curl, and the fermion–gravitino term (53).

The displayed potential-curl derivation records exact exterior-coefficient comparisons: each independent odd component is a separate exterior generator, and the tensor comparisons retain every coefficient. The two quartic negative controls record a nonzero residual when contorsion or the scalar gravitino completion is omitted. These statements describe the coefficient checks recorded in this derivation; a separate potential-curl executable or report is not included. The [current component runner](../../../../checks/run_component_checks.py) checks the subsequent supercovariant insertion and collection with the scope stated in [its guide](../../../../README.md).

To extend the complete coefficient result from $`L=1`$ to arbitrary $`L>0`$, rescale the **original linear multiplet** by one constant positive $`t`$, while holding the universal Weyl slots fixed:

```math
\begin{aligned}
(L_{ij},\varphi_i,E_a,N)&\longrightarrow t(L_{ij},\varphi_i,E_a,N),
\qquad L\longrightarrow tL,\\
L^{-1}N&\longrightarrow t^{-1}t L^{-1}N=L^{-1}N,\\
L^{-3}L_{ij}\bar\varphi^i\varphi^j
&\longrightarrow t^{-3+1+2}L^{-3}L_{ij}\bar\varphi^i\varphi^j,\\
L^{-5}\varphi^j\bar\varphi_k\varphi_l L^{kl}L_{ij}
&\longrightarrow t^{-5+3+2}\varphi^j\bar\varphi_k\varphi_l L^{kl}L_{ij},\\
\partial_\mu(tX)&=t\partial_\mu X,\qquad
\mathcal D_\mu(tX)=t\mathcal D_\mu X,\qquad \partial_\mu t=0.
\end{aligned}
\tag{54}
```

Every term of $`\rho',\lambda',\widehat F'`$ and the candidate $`A'`$ has degree zero under this common input rescaling. The source linear derivatives respect it term by term. At any point where $`L=L_0>0`$, choose $`t=1/L_0`$. This sets the value of $`L`$ at that point to one while leaving its first jets arbitrary; it is a constant rescaling, so no missing $`\partial t`$ terms are introduced. Therefore the exact $`L=1`$ coefficient identity holds at every $`L>0`$.

Both curls in the difference are ordinary two-forms once the hatted-strength completion has been included. All Lorentz frame and world indices are contracted consistently; checking the identity in a locally inertial vielbein frame at each point therefore suffices. The full contorsion was retained, so the frame choice has not removed the fermionic spin connection. Alignment leaves the source residual $`U(1)`$ connection; changing its local representative adds an ordinary gauge gradient to $`A'`$. The statement is local on the aligned $`SU(2)`$ patch. No claim that a single potential covers a nontrivial global bundle is required by this local action construction.

The homogeneity argument was applied to the universal map before substituting Coomans. The exact identity cancels its full arbitrary $`T,\chi,\phi_\mu`$ dependence; replacing them afterwards by their common gauged expressions preserves it even though those expressions can themselves depend on $`L`$. Thus the required local potential, with its gauge-gradient freedom, is

```math
\boxed{\begin{aligned}
A'_\mu&=2L^{-1}E_\mu+\sqrt2V_\mu
-L^{-3}L_{ij}\bar\varphi^i\gamma_\mu\varphi^j
-iL^{-1}\bar\varphi^i\psi_{\mu i},\\
2\partial_{[\mu}A'_{\nu]}
&=\widehat F'_{\mu\nu}+\bar\psi_{[\mu}{}^i\gamma_{\nu]}\lambda'_i
-\frac i2\rho'\bar\psi_{[\mu}{}^i\psi_{\nu]i},\\
A'_a&=e_a{}^\mu A'_\mu,\qquad
A'_\mu\sim A'_\mu+\partial_\mu\alpha.
\end{aligned}}
\tag{55}
```

The equality is an exact local component identity in the stated source conventions and gauge, with the source map's existing qualifications. It was not obtained by a BF integration by parts. Choosing the displayed representative keeps the Step 4 density as written. If a different representative is used, its change is the explicitly constrained BF gauge boundary term; the old mixed $`E'^a`$ is not identified with the original $`E^a`$.

For the residual-gradient check, the **new mixed** linear multiplet has the ordinary conserved density $`eP'^\mu`$ from Step 1/Step 3. Hence

```math
\delta_\alpha(e^{-1}\mathcal L_{VL})
=P'^\mu\partial_\mu\alpha
=e^{-1}\partial_\mu(e\alpha P'^\mu)
-\alpha e^{-1}\partial_\mu(eP'^\mu)
=e^{-1}\partial_\mu(e\alpha P'^\mu).
\tag{56}
```

This displays the boundary term; it is not discarded anywhere in the 42-group insertion. $`P'^\mu`$ in this boundary identity is the already-defined mixed BF conserved vector, not a new independent field and not the original linear constrained vector.

The simplest algebraic alignment reductions, which are useful for subsequent collection, are

```math
\begin{aligned}
\rho'&=2L^{-1}N+\frac{i}{\sqrt2}L^{-2}\delta_{ij}\bar\varphi^i\varphi^j,\\
A'_a&=2L^{-1}E_a+\sqrt2V_a
-\frac1{\sqrt2}L^{-2}\delta_{ij}\bar\varphi^i\gamma_a\varphi^j
-iL^{-1}\bar\varphi^i\psi_{ai}.
\end{aligned}
\tag{57}
```

The triplet and its covariant derivatives in Section 4.7 remain in the original source index notation subject to the displayed alignment condition. This keeps the $`V'`$ and gravitino terms visible rather than replacing $`\mathcal D L_{ij}`$ by a bare scalar gradient. There is no alignment of the fermion $`\varphi_i`$ and no new fermion gauge.

### 4.6 The scalar box after substitution

<!-- ASSERT_CONVENTION: metric_signature=mostly_plus (-++++); natural_units=hbar=c=1; gauge_slice=R2-GOLD7-GAUGE-v1; spinor_bar=NW-SE-transpose; fermion_order=full_source_map; background=gauged_Coomans -->

The parent vector derivative defines the derivative of the composite scalar by the following equality. This line is also the explicit prescription for every differentiated scalar bracket in Section 4.7. Partial derivatives act on every factor inside their displayed brackets.
```math
\mathcal D_\mu\rho'=\partial_\mu\left[\begin{aligned}
&2L^{-1}N\\
&+iL^{-3}L_{i_{1}j_{1}}\bar\varphi^{i_{1}}\varphi^{j_{1}}
\end{aligned}\right]-\frac i2\bar\psi_\mu{}^i\left[\begin{aligned}
&-2iL^{-1}\not{\mathcal D}\varphi_{i}\\
&+16L^{-1}L_{ij_{2}}\chi^{j_{2}}\\
&+4L^{-1}\gamma\!\cdot\!T\varphi_{i}\\
&-2NL^{-3}L_{ij_{2}}\varphi^{j_{2}}\\
&+2iL^{-3}(\not{\mathcal D}L_{ij_{2}})L^{j_{2}k_{2}}\varphi_{k_{2}}\\
&-2iL^{-3}\not E L_{ij_{2}}\varphi^{j_{2}}\\
&+2iL^{-3}\varphi^{j_{2}}\bar\varphi_{i}\varphi_{j_{2}}\\
&-6iL^{-5}\varphi^{j_{2}}\bar\varphi_{k_{2}}\varphi_{l_{2}}L^{k_{2}l_{2}}L_{ij_{2}}
\end{aligned}\right]
\tag{58}
```

For the gaugino, substituting into the complete lower-index derivative gives seven terms. The triplet contribution keeps the minus sign derived in Section 4.2. This is the operational prescription for every differentiated spinor bracket below.
```math
\left.\mathcal D_\mu\lambda'_i\right|_{\text{summand 1}}=(\partial_\mu+\tfrac14\omega_\mu{}^{ab}\gamma_{ab})\left[\begin{aligned}
&-2iL^{-1}\not{\mathcal D}\varphi_{i}\\
&+16L^{-1}L_{ij_{1}}\chi^{j_{1}}\\
&+4L^{-1}\gamma\!\cdot\!T\varphi_{i}\\
&-2NL^{-3}L_{ij_{1}}\varphi^{j_{1}}\\
&+2iL^{-3}(\not{\mathcal D}L_{ij_{1}})L^{j_{1}k_{1}}\varphi_{k_{1}}\\
&-2iL^{-3}\not E L_{ij_{1}}\varphi^{j_{1}}\\
&+2iL^{-3}\varphi^{j_{1}}\bar\varphi_{i}\varphi_{j_{1}}\\
&-6iL^{-5}\varphi^{j_{1}}\bar\varphi_{k_{1}}\varphi_{l_{1}}L^{k_{1}l_{1}}L_{ij_{1}}
\end{aligned}\right]
\tag{59}
```

```math
\left.\mathcal D_\mu\lambda'_i\right|_{\text{summand 2}}=-V_{\mu i}{}^j\left[\begin{aligned}
&-2iL^{-1}\not{\mathcal D}\varphi_{j}\\
&+16L^{-1}L_{jj_{2}}\chi^{j_{2}}\\
&+4L^{-1}\gamma\!\cdot\!T\varphi_{j}\\
&-2NL^{-3}L_{jj_{2}}\varphi^{j_{2}}\\
&+2iL^{-3}(\not{\mathcal D}L_{jj_{2}})L^{j_{2}k_{2}}\varphi_{k_{2}}\\
&-2iL^{-3}\not E L_{jj_{2}}\varphi^{j_{2}}\\
&+2iL^{-3}\varphi^{j_{2}}\bar\varphi_{j}\varphi_{j_{2}}\\
&-6iL^{-5}\varphi^{j_{2}}\bar\varphi_{k_{2}}\varphi_{l_{2}}L^{k_{2}l_{2}}L_{jj_{2}}
\end{aligned}\right]
\tag{60}
```

```math
\left.\mathcal D_\mu\lambda'_i\right|_{\text{summand 3}}=+\tfrac14\gamma^{ab}e_{a}{}^{\mu_{3}}e_{b}{}^{\nu_{3}}\left[\begin{aligned}
&4L^{-1}\mathcal D_{[\mu_{3}}E_{\nu_{3}]}\\
&-4L^{-2}(\mathcal D_{[\mu_{3}}L)E_{\nu_{3}]}\\
&+2L^{-1}\widehat R_{\mu_{3}\nu_{3}}^{i_{4}j_{4}}(V)L_{i_{4}j_{4}}\\
&-2L^{-3}L_{k_{4}}{}^{l_{4}}\mathcal D_{[\mu_{3}}L^{k_{4}p_{4}}\mathcal D_{\nu_{3}]}L_{l_{4}p_{4}}\\
&+6L^{-4}(\mathcal D_{[\mu_{3}}L)L_{i_{4}j_{4}}\bar\varphi^{i_{4}}\gamma_{\nu_{3}]}\varphi^{j_{4}}\\
&-2L^{-3}(\mathcal D_{[\mu_{3}}L_{i_{4}j_{4}})\bar\varphi^{i_{4}}\gamma_{\nu_{3}]}\varphi^{j_{4}}\\
&-2L^{-3}L_{i_{4}j_{4}}(\mathcal D_{[\mu_{3}}\bar\varphi^{i_{4}})\gamma_{\nu_{3}]}\varphi^{j_{4}}\\
&-2L^{-3}L_{i_{4}j_{4}}\bar\varphi^{i_{4}}\gamma_{[\nu_{3}}\mathcal D_{\mu_{3}]}\varphi^{j_{4}}\\
&-iL^{-1}\bar\varphi^{i_{4}}\widehat R_{\mu_{3}\nu_{3} i_{4}}(Q)
\end{aligned}\right]\psi_{\mu i}
\tag{61}
```

```math
\left.\mathcal D_\mu\lambda'_i\right|_{\text{summand 4}}=+\tfrac i2\gamma^a\mathcal D_a\left[\begin{aligned}
&2L^{-1}N\\
&+iL^{-3}L_{i_{5}j_{5}}\bar\varphi^{i_{5}}\varphi^{j_{5}}
\end{aligned}\right]\psi_{\mu i}
\tag{62}
```

```math
\left.\mathcal D_\mu\lambda'_i\right|_{\text{summand 5}}=-\left[\begin{aligned}
&L^{-1}\square^{c} L_{ij}\\
&-L^{-3}L^{k_{6}m_{6}}\mathcal D_{c_{6}}L_{k_{6}(i}\mathcal D^{c_{6}}L_{j)m_{6}}\\
&-L^{-3}L_{ij}N^{2}\\
&-L^{-3}L_{ij}E_{c_{6}}E^{c_{6}}\\
&+2L^{-3}E_{c_{6}}L_{k_{6}(i}\mathcal D^{c_{6}}L_{j)}{}^{k_{6}}\\
&+\frac83L^{-1}L_{ij}T^{2}\\
&+4L^{-1}L_{ij}D\\
&+iNL^{-3}\bar\varphi_{(i}\varphi_{j)}\\
&-3iNL^{-5}L_{ij}L^{k_{6}l_{6}}\bar\varphi_{k_{6}}\varphi_{l_{6}}\\
&+3L^{-5}L_{ij}L^{k_{6}l_{6}}\bar\varphi_{k_{6}}\not E\varphi_{l_{6}}\\
&-L^{-3}\bar\varphi_{(i}\not E\varphi_{j)}\\
&-16iL^{-1}\bar\chi_{(i}\varphi_{j)}\\
&+16iL^{-3}L_{ij}L_{k_{6}l_{6}}\bar\chi^{k_{6}}\varphi^{l_{6}}\\
&+2L^{-3}L_{k_{6}(i}\bar\varphi^{k_{6}}\not{\mathcal D}\varphi_{j)}\\
&-3L^{-5}L_{k_{6}(i}L^{l_{6}m_{6}}\bar\varphi^{k_{6}}(\not{\mathcal D}L_{j)l_{6}})\varphi_{m_{6}}\\
&+\frac12L^{-3}\bar\varphi^{l_{6}}(\not{\mathcal D}L_{l_{6}(i})\varphi_{j)}\\
&+\frac12L^{-3}\bar\varphi^{m_{6}}(\not{\mathcal D}L_{ij})\varphi_{m_{6}}\\
&+2iL^{-3}L_{ij}\bar\varphi\gamma\!\cdot\!T\varphi\\
&+\frac{15}{2}L^{-7}L_{ij}(L^{k_{6}l_{6}}\bar\varphi_{k_{6}}\varphi_{l_{6}})^{2}\\
&-3L^{-5}(L^{k_{6}l_{6}}\bar\varphi_{k_{6}}\varphi_{l_{6}})\bar\varphi_{(i}\varphi_{j)}\\
&-\frac32L^{-5}L_{ij}(\bar\varphi_{m_{6}}\varphi_{n_{6}})(\bar\varphi^{m_{6}}\varphi^{n_{6}})
\end{aligned}\right]\psi_\mu{}^j
\tag{63}
```

```math
\left.\mathcal D_\mu\lambda'_i\right|_{\text{summand 6}}=-\left[\begin{aligned}
&2L^{-1}N\\
&+iL^{-3}L_{i_{7}j_{7}}\bar\varphi^{i_{7}}\varphi^{j_{7}}
\end{aligned}\right]\gamma\!\cdot\!T\psi_{\mu i}
\tag{64}
```

```math
\left.\mathcal D_\mu\lambda'_i\right|_{\text{summand 7}}=-\left[\begin{aligned}
&2L^{-1}N\\
&+iL^{-3}L_{i_{8}j_{8}}\bar\varphi^{i_{8}}\varphi^{j_{8}}
\end{aligned}\right]\phi_{\mu i}
\tag{65}
```

The sum of the seven displayed summands is $`\mathcal D_\mu\lambda'_i`$. These labels partition a displayed equation; they do not define seven fields. In the next line, $`\mathcal D^a`$ on the full spinor bracket means precisely that sum with a raised tangent derivative index. The scalar-derivative bracket uses the preceding two-term definition. Thus the nested expression has no unspecified primed input.
```math
\Box_c\rho'=\left[\begin{aligned}
&(\partial^a+\omega_b{}^{ba})\mathcal D_a\left[\begin{aligned}
&2L^{-1}N\\
&+iL^{-3}L_{i_{1}j_{1}}\bar\varphi^{i_{1}}\varphi^{j_{1}}
\end{aligned}\right]\\
&-\tfrac i2\bar\psi_a{}^i\mathcal D^a\left[\begin{aligned}
&-2iL^{-1}\not{\mathcal D}\varphi_{i}\\
&+16L^{-1}L_{ij_{2}}\chi^{j_{2}}\\
&+4L^{-1}\gamma\!\cdot\!T\varphi_{i}\\
&-2NL^{-3}L_{ij_{2}}\varphi^{j_{2}}\\
&+2iL^{-3}(\not{\mathcal D}L_{ij_{2}})L^{j_{2}k_{2}}\varphi_{k_{2}}\\
&-2iL^{-3}\not E L_{ij_{2}}\varphi^{j_{2}}\\
&+2iL^{-3}\varphi^{j_{2}}\bar\varphi_{i}\varphi_{j_{2}}\\
&-6iL^{-5}\varphi^{j_{2}}\bar\varphi_{k_{2}}\varphi_{l_{2}}L^{k_{2}l_{2}}L_{ij_{2}}
\end{aligned}\right]\\
&-2\left[\begin{aligned}
&2L^{-1}N\\
&+iL^{-3}L_{i_{3}j_{3}}\bar\varphi^{i_{3}}\varphi^{j_{3}}
\end{aligned}\right]\bar\psi_a{}^i\gamma^a\chi_i\\
&+\tfrac12\bar\psi_a{}^i\gamma^a\gamma\!\cdot\!T\left[\begin{aligned}
&-2iL^{-1}\not{\mathcal D}\varphi_{i}\\
&+16L^{-1}L_{ij_{4}}\chi^{j_{4}}\\
&+4L^{-1}\gamma\!\cdot\!T\varphi_{i}\\
&-2NL^{-3}L_{ij_{4}}\varphi^{j_{4}}\\
&+2iL^{-3}(\not{\mathcal D}L_{ij_{4}})L^{j_{4}k_{4}}\varphi_{k_{4}}\\
&-2iL^{-3}\not E L_{ij_{4}}\varphi^{j_{4}}\\
&+2iL^{-3}\varphi^{j_{4}}\bar\varphi_{i}\varphi_{j_{4}}\\
&-6iL^{-5}\varphi^{j_{4}}\bar\varphi_{k_{4}}\varphi_{l_{4}}L^{k_{4}l_{4}}L_{ij_{4}}
\end{aligned}\right]\\
&+\tfrac12\bar\phi_a{}^i\gamma^a\left[\begin{aligned}
&-2iL^{-1}\not{\mathcal D}\varphi_{i}\\
&+16L^{-1}L_{ij_{5}}\chi^{j_{5}}\\
&+4L^{-1}\gamma\!\cdot\!T\varphi_{i}\\
&-2NL^{-3}L_{ij_{5}}\varphi^{j_{5}}\\
&+2iL^{-3}(\not{\mathcal D}L_{ij_{5}})L^{j_{5}k_{5}}\varphi_{k_{5}}\\
&-2iL^{-3}\not E L_{ij_{5}}\varphi^{j_{5}}\\
&+2iL^{-3}\varphi^{j_{5}}\bar\varphi_{i}\varphi_{j_{5}}\\
&-6iL^{-5}\varphi^{j_{5}}\bar\varphi_{k_{5}}\varphi_{l_{5}}L^{k_{5}l_{5}}L_{ij_{5}}
\end{aligned}\right]\\
&+2f_a{}^a\left[\begin{aligned}
&2L^{-1}N\\
&+iL^{-3}L_{i_{6}j_{6}}\bar\varphi^{i_{6}}\varphi^{j_{6}}
\end{aligned}\right]
\end{aligned}\right]
\tag{66}
```

The $`2f_a{}^a`$ contribution remains distinct from the separate $`(\rho')^2f_a{}^a`$ already present in the parent density. In the parent term $`\rho'\Box_c\rho'/2`$ it contributes another $`(\rho')^2f_a{}^a`$; it is not dropped or counted twice. Keeping the box unintegrated preserves the exact BF boundary representative.
### 4.7 Insert into every term of Step 4 Eq. (47)

<!-- ASSERT_CONVENTION: metric_signature=mostly_plus (-++++); natural_units=hbar=c=1; gauge_slice=R2-GOLD7-GAUGE-v1; spinor_bar=NW-SE-transpose; fermion_order=full_source_map; background=gauged_Coomans -->

The following is the density written as **42 additive groups**, in exactly the order of Step 4 Eq. (47). Five retained four-term gravitino brackets account for its 57 distributed rows. Each displayed arrow is literal substitution, not an equation of motion or an omitted operation. The final density is the sum of the 42 right-hand sides. The group numbers are equation labels, not new fields.

Every replacement bracket below is printed in full. Internal dummy indices are renamed separately for each occurrence ($`i_1,k_2,c_3,\ldots`$) before multiplication; all still run over their original $`SU(2)`$ or tangent ranges. Thus multiplying two triplet brackets never identifies their internal contraction indices. The factors retain spinor and gamma order. No new physical field names are introduced.

The derivatives on the right are the full source operators defined in Section 4.4, acting on the displayed composite argument. Section 4.3 gives all first product derivatives. Section 4.6 spells out the conformal-box replacement, including its $`S`$ and $`K`$ pieces. In particular, $`\Box_c`$ on a displayed scalar bracket never means an ordinary scalar Laplacian. The $`A'_a`$ replacements use the local potential of Section 4.5, on the stated aligned-triplet patch.

#### Additive group 1

<!-- BEGIN STEP5 GROUP 01 -->

```math
\begin{gathered}Y'^{ij}Y'_{ij}\\\longmapsto\\\begin{aligned}
&\varepsilon^{ir_{1}}\varepsilon^{js_{1}}\left[\begin{aligned}
&L^{-1}\square^{c} L_{r_{1}s_{1}}\\
&-L^{-3}L^{k_{2}m_{2}}\mathcal D_{c_{2}}L_{k_{2}(r_{1}}\mathcal D^{c_{2}}L_{s_{1})m_{2}}\\
&-L^{-3}L_{r_{1}s_{1}}N^{2}\\
&-L^{-3}L_{r_{1}s_{1}}E_{c_{2}}E^{c_{2}}\\
&+2L^{-3}E_{c_{2}}L_{k_{2}(r_{1}}\mathcal D^{c_{2}}L_{s_{1})}{}^{k_{2}}\\
&+\frac83L^{-1}L_{r_{1}s_{1}}T^{2}\\
&+4L^{-1}L_{r_{1}s_{1}}D\\
&+iNL^{-3}\bar\varphi_{(r_{1}}\varphi_{s_{1})}\\
&-3iNL^{-5}L_{r_{1}s_{1}}L^{k_{2}l_{2}}\bar\varphi_{k_{2}}\varphi_{l_{2}}\\
&+3L^{-5}L_{r_{1}s_{1}}L^{k_{2}l_{2}}\bar\varphi_{k_{2}}\not E\varphi_{l_{2}}\\
&-L^{-3}\bar\varphi_{(r_{1}}\not E\varphi_{s_{1})}\\
&-16iL^{-1}\bar\chi_{(r_{1}}\varphi_{s_{1})}\\
&+16iL^{-3}L_{r_{1}s_{1}}L_{k_{2}l_{2}}\bar\chi^{k_{2}}\varphi^{l_{2}}\\
&+2L^{-3}L_{k_{2}(r_{1}}\bar\varphi^{k_{2}}\not{\mathcal D}\varphi_{s_{1})}\\
&-3L^{-5}L_{k_{2}(r_{1}}L^{l_{2}m_{2}}\bar\varphi^{k_{2}}(\not{\mathcal D}L_{s_{1})l_{2}})\varphi_{m_{2}}\\
&+\frac12L^{-3}\bar\varphi^{l_{2}}(\not{\mathcal D}L_{l_{2}(r_{1}})\varphi_{s_{1})}\\
&+\frac12L^{-3}\bar\varphi^{m_{2}}(\not{\mathcal D}L_{r_{1}s_{1}})\varphi_{m_{2}}\\
&+2iL^{-3}L_{r_{1}s_{1}}\bar\varphi\gamma\!\cdot\!T\varphi\\
&+\frac{15}{2}L^{-7}L_{r_{1}s_{1}}(L^{k_{2}l_{2}}\bar\varphi_{k_{2}}\varphi_{l_{2}})^{2}\\
&-3L^{-5}(L^{k_{2}l_{2}}\bar\varphi_{k_{2}}\varphi_{l_{2}})\bar\varphi_{(r_{1}}\varphi_{s_{1})}\\
&-\frac32L^{-5}L_{r_{1}s_{1}}(\bar\varphi_{m_{2}}\varphi_{n_{2}})(\bar\varphi^{m_{2}}\varphi^{n_{2}})
\end{aligned}\right]\\
&{}\times \left[\begin{aligned}
&L^{-1}\square^{c} L_{ij}\\
&-L^{-3}L^{k_{3}m_{3}}\mathcal D_{c_{3}}L_{k_{3}(i}\mathcal D^{c_{3}}L_{j)m_{3}}\\
&-L^{-3}L_{ij}N^{2}\\
&-L^{-3}L_{ij}E_{c_{3}}E^{c_{3}}\\
&+2L^{-3}E_{c_{3}}L_{k_{3}(i}\mathcal D^{c_{3}}L_{j)}{}^{k_{3}}\\
&+\frac83L^{-1}L_{ij}T^{2}\\
&+4L^{-1}L_{ij}D\\
&+iNL^{-3}\bar\varphi_{(i}\varphi_{j)}\\
&-3iNL^{-5}L_{ij}L^{k_{3}l_{3}}\bar\varphi_{k_{3}}\varphi_{l_{3}}\\
&+3L^{-5}L_{ij}L^{k_{3}l_{3}}\bar\varphi_{k_{3}}\not E\varphi_{l_{3}}\\
&-L^{-3}\bar\varphi_{(i}\not E\varphi_{j)}\\
&-16iL^{-1}\bar\chi_{(i}\varphi_{j)}\\
&+16iL^{-3}L_{ij}L_{k_{3}l_{3}}\bar\chi^{k_{3}}\varphi^{l_{3}}\\
&+2L^{-3}L_{k_{3}(i}\bar\varphi^{k_{3}}\not{\mathcal D}\varphi_{j)}\\
&-3L^{-5}L_{k_{3}(i}L^{l_{3}m_{3}}\bar\varphi^{k_{3}}(\not{\mathcal D}L_{j)l_{3}})\varphi_{m_{3}}\\
&+\frac12L^{-3}\bar\varphi^{l_{3}}(\not{\mathcal D}L_{l_{3}(i})\varphi_{j)}\\
&+\frac12L^{-3}\bar\varphi^{m_{3}}(\not{\mathcal D}L_{ij})\varphi_{m_{3}}\\
&+2iL^{-3}L_{ij}\bar\varphi\gamma\!\cdot\!T\varphi\\
&+\frac{15}{2}L^{-7}L_{ij}(L^{k_{3}l_{3}}\bar\varphi_{k_{3}}\varphi_{l_{3}})^{2}\\
&-3L^{-5}(L^{k_{3}l_{3}}\bar\varphi_{k_{3}}\varphi_{l_{3}})\bar\varphi_{(i}\varphi_{j)}\\
&-\frac32L^{-5}L_{ij}(\bar\varphi_{m_{3}}\varphi_{n_{3}})(\bar\varphi^{m_{3}}\varphi^{n_{3}})
\end{aligned}\right]
\end{aligned}\end{gathered}
\tag{67}
```

<!-- END STEP5 GROUP 01 -->

#### Additive group 2

<!-- BEGIN STEP5 GROUP 02 -->

```math
\begin{gathered}-g\rho'Y'^{ij}L_{ij}\\\longmapsto\\\begin{aligned}
&-g\left[\begin{aligned}
&2L^{-1}N\\
&+iL^{-3}L_{i_{1}j_{1}}\bar\varphi^{i_{1}}\varphi^{j_{1}}
\end{aligned}\right]\\
&{}\times \varepsilon^{ir_{2}}\varepsilon^{js_{2}}\left[\begin{aligned}
&L^{-1}\square^{c} L_{r_{2}s_{2}}\\
&-L^{-3}L^{k_{3}m_{3}}\mathcal D_{c_{3}}L_{k_{3}(r_{2}}\mathcal D^{c_{3}}L_{s_{2})m_{3}}\\
&-L^{-3}L_{r_{2}s_{2}}N^{2}\\
&-L^{-3}L_{r_{2}s_{2}}E_{c_{3}}E^{c_{3}}\\
&+2L^{-3}E_{c_{3}}L_{k_{3}(r_{2}}\mathcal D^{c_{3}}L_{s_{2})}{}^{k_{3}}\\
&+\frac83L^{-1}L_{r_{2}s_{2}}T^{2}\\
&+4L^{-1}L_{r_{2}s_{2}}D\\
&+iNL^{-3}\bar\varphi_{(r_{2}}\varphi_{s_{2})}\\
&-3iNL^{-5}L_{r_{2}s_{2}}L^{k_{3}l_{3}}\bar\varphi_{k_{3}}\varphi_{l_{3}}\\
&+3L^{-5}L_{r_{2}s_{2}}L^{k_{3}l_{3}}\bar\varphi_{k_{3}}\not E\varphi_{l_{3}}\\
&-L^{-3}\bar\varphi_{(r_{2}}\not E\varphi_{s_{2})}\\
&-16iL^{-1}\bar\chi_{(r_{2}}\varphi_{s_{2})}\\
&+16iL^{-3}L_{r_{2}s_{2}}L_{k_{3}l_{3}}\bar\chi^{k_{3}}\varphi^{l_{3}}\\
&+2L^{-3}L_{k_{3}(r_{2}}\bar\varphi^{k_{3}}\not{\mathcal D}\varphi_{s_{2})}\\
&-3L^{-5}L_{k_{3}(r_{2}}L^{l_{3}m_{3}}\bar\varphi^{k_{3}}(\not{\mathcal D}L_{s_{2})l_{3}})\varphi_{m_{3}}\\
&+\frac12L^{-3}\bar\varphi^{l_{3}}(\not{\mathcal D}L_{l_{3}(r_{2}})\varphi_{s_{2})}\\
&+\frac12L^{-3}\bar\varphi^{m_{3}}(\not{\mathcal D}L_{r_{2}s_{2}})\varphi_{m_{3}}\\
&+2iL^{-3}L_{r_{2}s_{2}}\bar\varphi\gamma\!\cdot\!T\varphi\\
&+\frac{15}{2}L^{-7}L_{r_{2}s_{2}}(L^{k_{3}l_{3}}\bar\varphi_{k_{3}}\varphi_{l_{3}})^{2}\\
&-3L^{-5}(L^{k_{3}l_{3}}\bar\varphi_{k_{3}}\varphi_{l_{3}})\bar\varphi_{(r_{2}}\varphi_{s_{2})}\\
&-\frac32L^{-5}L_{r_{2}s_{2}}(\bar\varphi_{m_{3}}\varphi_{n_{3}})(\bar\varphi^{m_{3}}\varphi^{n_{3}})
\end{aligned}\right]\\
&{}\times L_{ij}
\end{aligned}\end{gathered}
\tag{68}
```

<!-- END STEP5 GROUP 02 -->

#### Additive group 3

<!-- BEGIN STEP5 GROUP 03 -->

```math
\begin{gathered}-\frac12\bar\lambda'{}^i\not{\mathcal D}\lambda'_i\\\longmapsto\\\begin{aligned}
&-\frac12\varepsilon^{ir_{1}}\left[\begin{aligned}
&-2iL^{-1}(\mathcal D_{c_{2}}\bar\varphi_{r_{1}})\gamma^{c_{2}}\\
&+16L^{-1}L_{r_{1}j_{2}}\bar\chi^{j_{2}}\\
&-4L^{-1}\bar\varphi_{r_{1}}\gamma\!\cdot\!T\\
&-2NL^{-3}L_{r_{1}j_{2}}\bar\varphi^{j_{2}}\\
&+2iL^{-3}L^{j_{2}k_{2}}\bar\varphi_{k_{2}}(\not{\mathcal D}L_{r_{1}j_{2}})\\
&-2iL^{-3}L_{r_{1}j_{2}}\bar\varphi^{j_{2}}\not E\\
&+2iL^{-3}\bar\varphi^{j_{2}}(\bar\varphi_{r_{1}}\varphi_{j_{2}})\\
&-6iL^{-5}\bar\varphi^{j_{2}}(\bar\varphi_{k_{2}}\varphi_{l_{2}})L^{k_{2}l_{2}}L_{r_{1}j_{2}}
\end{aligned}\right]\\
&{}\times \not{\mathcal D}\left[\begin{aligned}
&-2iL^{-1}\not{\mathcal D}\varphi_{i}\\
&+16L^{-1}L_{ij_{3}}\chi^{j_{3}}\\
&+4L^{-1}\gamma\!\cdot\!T\varphi_{i}\\
&-2NL^{-3}L_{ij_{3}}\varphi^{j_{3}}\\
&+2iL^{-3}(\not{\mathcal D}L_{ij_{3}})L^{j_{3}k_{3}}\varphi_{k_{3}}\\
&-2iL^{-3}\not E L_{ij_{3}}\varphi^{j_{3}}\\
&+2iL^{-3}\varphi^{j_{3}}\bar\varphi_{i}\varphi_{j_{3}}\\
&-6iL^{-5}\varphi^{j_{3}}\bar\varphi_{k_{3}}\varphi_{l_{3}}L^{k_{3}l_{3}}L_{ij_{3}}
\end{aligned}\right]
\end{aligned}\end{gathered}
\tag{69}
```

<!-- END STEP5 GROUP 03 -->

#### Additive group 4

<!-- BEGIN STEP5 GROUP 04 -->

```math
\begin{gathered}+i\bar\lambda'{}^i\gamma\!\cdot\!T\lambda'_i\\\longmapsto\\\begin{aligned}
&+i\varepsilon^{ir_{1}}\left[\begin{aligned}
&-2iL^{-1}(\mathcal D_{c_{2}}\bar\varphi_{r_{1}})\gamma^{c_{2}}\\
&+16L^{-1}L_{r_{1}j_{2}}\bar\chi^{j_{2}}\\
&-4L^{-1}\bar\varphi_{r_{1}}\gamma\!\cdot\!T\\
&-2NL^{-3}L_{r_{1}j_{2}}\bar\varphi^{j_{2}}\\
&+2iL^{-3}L^{j_{2}k_{2}}\bar\varphi_{k_{2}}(\not{\mathcal D}L_{r_{1}j_{2}})\\
&-2iL^{-3}L_{r_{1}j_{2}}\bar\varphi^{j_{2}}\not E\\
&+2iL^{-3}\bar\varphi^{j_{2}}(\bar\varphi_{r_{1}}\varphi_{j_{2}})\\
&-6iL^{-5}\bar\varphi^{j_{2}}(\bar\varphi_{k_{2}}\varphi_{l_{2}})L^{k_{2}l_{2}}L_{r_{1}j_{2}}
\end{aligned}\right]\\
&{}\times \gamma\!\cdot\!T\left[\begin{aligned}
&-2iL^{-1}\not{\mathcal D}\varphi_{i}\\
&+16L^{-1}L_{ij_{3}}\chi^{j_{3}}\\
&+4L^{-1}\gamma\!\cdot\!T\varphi_{i}\\
&-2NL^{-3}L_{ij_{3}}\varphi^{j_{3}}\\
&+2iL^{-3}(\not{\mathcal D}L_{ij_{3}})L^{j_{3}k_{3}}\varphi_{k_{3}}\\
&-2iL^{-3}\not E L_{ij_{3}}\varphi^{j_{3}}\\
&+2iL^{-3}\varphi^{j_{3}}\bar\varphi_{i}\varphi_{j_{3}}\\
&-6iL^{-5}\varphi^{j_{3}}\bar\varphi_{k_{3}}\varphi_{l_{3}}L^{k_{3}l_{3}}L_{ij_{3}}
\end{aligned}\right]
\end{aligned}\end{gathered}
\tag{70}
```

<!-- END STEP5 GROUP 04 -->

#### Additive group 5

<!-- BEGIN STEP5 GROUP 05 -->

```math
\begin{gathered}-8i\rho'\bar\lambda'{}^i\chi_i\\\longmapsto\\\begin{aligned}
&-8i\left[\begin{aligned}
&2L^{-1}N\\
&+iL^{-3}L_{i_{1}j_{1}}\bar\varphi^{i_{1}}\varphi^{j_{1}}
\end{aligned}\right]\\
&{}\times \varepsilon^{ir_{2}}\left[\begin{aligned}
&-2iL^{-1}(\mathcal D_{c_{3}}\bar\varphi_{r_{2}})\gamma^{c_{3}}\\
&+16L^{-1}L_{r_{2}j_{3}}\bar\chi^{j_{3}}\\
&-4L^{-1}\bar\varphi_{r_{2}}\gamma\!\cdot\!T\\
&-2NL^{-3}L_{r_{2}j_{3}}\bar\varphi^{j_{3}}\\
&+2iL^{-3}L^{j_{3}k_{3}}\bar\varphi_{k_{3}}(\not{\mathcal D}L_{r_{2}j_{3}})\\
&-2iL^{-3}L_{r_{2}j_{3}}\bar\varphi^{j_{3}}\not E\\
&+2iL^{-3}\bar\varphi^{j_{3}}(\bar\varphi_{r_{2}}\varphi_{j_{3}})\\
&-6iL^{-5}\bar\varphi^{j_{3}}(\bar\varphi_{k_{3}}\varphi_{l_{3}})L^{k_{3}l_{3}}L_{r_{2}j_{3}}
\end{aligned}\right]\\
&{}\times \chi_i
\end{aligned}\end{gathered}
\tag{71}
```

<!-- END STEP5 GROUP 05 -->

#### Additive group 6

<!-- BEGIN STEP5 GROUP 06 -->

```math
\begin{gathered}-\frac i8\bar\lambda'{}^i\gamma\!\cdot\!\widehat G\lambda'_i\\\longmapsto\\\begin{aligned}
&-\frac i8\varepsilon^{ir_{1}}\left[\begin{aligned}
&-2iL^{-1}(\mathcal D_{c_{2}}\bar\varphi_{r_{1}})\gamma^{c_{2}}\\
&+16L^{-1}L_{r_{1}j_{2}}\bar\chi^{j_{2}}\\
&-4L^{-1}\bar\varphi_{r_{1}}\gamma\!\cdot\!T\\
&-2NL^{-3}L_{r_{1}j_{2}}\bar\varphi^{j_{2}}\\
&+2iL^{-3}L^{j_{2}k_{2}}\bar\varphi_{k_{2}}(\not{\mathcal D}L_{r_{1}j_{2}})\\
&-2iL^{-3}L_{r_{1}j_{2}}\bar\varphi^{j_{2}}\not E\\
&+2iL^{-3}\bar\varphi^{j_{2}}(\bar\varphi_{r_{1}}\varphi_{j_{2}})\\
&-6iL^{-5}\bar\varphi^{j_{2}}(\bar\varphi_{k_{2}}\varphi_{l_{2}})L^{k_{2}l_{2}}L_{r_{1}j_{2}}
\end{aligned}\right]\\
&{}\times \gamma\!\cdot\!\widehat G\left[\begin{aligned}
&-2iL^{-1}\not{\mathcal D}\varphi_{i}\\
&+16L^{-1}L_{ij_{3}}\chi^{j_{3}}\\
&+4L^{-1}\gamma\!\cdot\!T\varphi_{i}\\
&-2NL^{-3}L_{ij_{3}}\varphi^{j_{3}}\\
&+2iL^{-3}(\not{\mathcal D}L_{ij_{3}})L^{j_{3}k_{3}}\varphi_{k_{3}}\\
&-2iL^{-3}\not E L_{ij_{3}}\varphi^{j_{3}}\\
&+2iL^{-3}\varphi^{j_{3}}\bar\varphi_{i}\varphi_{j_{3}}\\
&-6iL^{-5}\varphi^{j_{3}}\bar\varphi_{k_{3}}\varphi_{l_{3}}L^{k_{3}l_{3}}L_{ij_{3}}
\end{aligned}\right]
\end{aligned}\end{gathered}
\tag{72}
```

<!-- END STEP5 GROUP 06 -->

#### Additive group 7

<!-- BEGIN STEP5 GROUP 07 -->

```math
\begin{gathered}+\frac{ig}4\bar\lambda'{}^iL_{ij}\lambda'{}^j\\\longmapsto\\\begin{aligned}
&+\frac{ig}4\varepsilon^{ir_{1}}\left[\begin{aligned}
&-2iL^{-1}(\mathcal D_{c_{2}}\bar\varphi_{r_{1}})\gamma^{c_{2}}\\
&+16L^{-1}L_{r_{1}j_{2}}\bar\chi^{j_{2}}\\
&-4L^{-1}\bar\varphi_{r_{1}}\gamma\!\cdot\!T\\
&-2NL^{-3}L_{r_{1}j_{2}}\bar\varphi^{j_{2}}\\
&+2iL^{-3}L^{j_{2}k_{2}}\bar\varphi_{k_{2}}(\not{\mathcal D}L_{r_{1}j_{2}})\\
&-2iL^{-3}L_{r_{1}j_{2}}\bar\varphi^{j_{2}}\not E\\
&+2iL^{-3}\bar\varphi^{j_{2}}(\bar\varphi_{r_{1}}\varphi_{j_{2}})\\
&-6iL^{-5}\bar\varphi^{j_{2}}(\bar\varphi_{k_{2}}\varphi_{l_{2}})L^{k_{2}l_{2}}L_{r_{1}j_{2}}
\end{aligned}\right]\\
&{}\times L_{ij}\varepsilon^{jr_{3}}\left[\begin{aligned}
&-2iL^{-1}\not{\mathcal D}\varphi_{r_{3}}\\
&+16L^{-1}L_{r_{3}j_{4}}\chi^{j_{4}}\\
&+4L^{-1}\gamma\!\cdot\!T\varphi_{r_{3}}\\
&-2NL^{-3}L_{r_{3}j_{4}}\varphi^{j_{4}}\\
&+2iL^{-3}(\not{\mathcal D}L_{r_{3}j_{4}})L^{j_{4}k_{4}}\varphi_{k_{4}}\\
&-2iL^{-3}\not E L_{r_{3}j_{4}}\varphi^{j_{4}}\\
&+2iL^{-3}\varphi^{j_{4}}\bar\varphi_{r_{3}}\varphi_{j_{4}}\\
&-6iL^{-5}\varphi^{j_{4}}\bar\varphi_{k_{4}}\varphi_{l_{4}}L^{k_{4}l_{4}}L_{r_{3}j_{4}}
\end{aligned}\right]
\end{aligned}\end{gathered}
\tag{73}
```

<!-- END STEP5 GROUP 07 -->

#### Additive group 8

<!-- BEGIN STEP5 GROUP 08 -->

```math
\begin{gathered}+\frac g4\rho'\bar\psi_a{}^i\gamma^a\lambda'{}^jL_{ij}\\\longmapsto\\\begin{aligned}
&+\frac g4\left[\begin{aligned}
&2L^{-1}N\\
&+iL^{-3}L_{i_{1}j_{1}}\bar\varphi^{i_{1}}\varphi^{j_{1}}
\end{aligned}\right]\\
&{}\times \bar\psi_a{}^i\gamma^a\varepsilon^{jr_{2}}\left[\begin{aligned}
&-2iL^{-1}\not{\mathcal D}\varphi_{r_{2}}\\
&+16L^{-1}L_{r_{2}j_{3}}\chi^{j_{3}}\\
&+4L^{-1}\gamma\!\cdot\!T\varphi_{r_{2}}\\
&-2NL^{-3}L_{r_{2}j_{3}}\varphi^{j_{3}}\\
&+2iL^{-3}(\not{\mathcal D}L_{r_{2}j_{3}})L^{j_{3}k_{3}}\varphi_{k_{3}}\\
&-2iL^{-3}\not E L_{r_{2}j_{3}}\varphi^{j_{3}}\\
&+2iL^{-3}\varphi^{j_{3}}\bar\varphi_{r_{2}}\varphi_{j_{3}}\\
&-6iL^{-5}\varphi^{j_{3}}\bar\varphi_{k_{3}}\varphi_{l_{3}}L^{k_{3}l_{3}}L_{r_{2}j_{3}}
\end{aligned}\right]\\
&{}\times L_{ij}
\end{aligned}\end{gathered}
\tag{74}
```

<!-- END STEP5 GROUP 08 -->

#### Additive group 9

<!-- BEGIN STEP5 GROUP 09 -->

```math
\begin{gathered}-\frac12\bar\psi_a{}^i\gamma^a\lambda'{}^jY'_{ij}\\\longmapsto\\\begin{aligned}
&-\frac12\bar\psi_a{}^i\gamma^a\varepsilon^{jr_{1}}\left[\begin{aligned}
&-2iL^{-1}\not{\mathcal D}\varphi_{r_{1}}\\
&+16L^{-1}L_{r_{1}j_{2}}\chi^{j_{2}}\\
&+4L^{-1}\gamma\!\cdot\!T\varphi_{r_{1}}\\
&-2NL^{-3}L_{r_{1}j_{2}}\varphi^{j_{2}}\\
&+2iL^{-3}(\not{\mathcal D}L_{r_{1}j_{2}})L^{j_{2}k_{2}}\varphi_{k_{2}}\\
&-2iL^{-3}\not E L_{r_{1}j_{2}}\varphi^{j_{2}}\\
&+2iL^{-3}\varphi^{j_{2}}\bar\varphi_{r_{1}}\varphi_{j_{2}}\\
&-6iL^{-5}\varphi^{j_{2}}\bar\varphi_{k_{2}}\varphi_{l_{2}}L^{k_{2}l_{2}}L_{r_{1}j_{2}}
\end{aligned}\right]\\
&{}\times \left[\begin{aligned}
&L^{-1}\square^{c} L_{ij}\\
&-L^{-3}L^{k_{3}m_{3}}\mathcal D_{c_{3}}L_{k_{3}(i}\mathcal D^{c_{3}}L_{j)m_{3}}\\
&-L^{-3}L_{ij}N^{2}\\
&-L^{-3}L_{ij}E_{c_{3}}E^{c_{3}}\\
&+2L^{-3}E_{c_{3}}L_{k_{3}(i}\mathcal D^{c_{3}}L_{j)}{}^{k_{3}}\\
&+\frac83L^{-1}L_{ij}T^{2}\\
&+4L^{-1}L_{ij}D\\
&+iNL^{-3}\bar\varphi_{(i}\varphi_{j)}\\
&-3iNL^{-5}L_{ij}L^{k_{3}l_{3}}\bar\varphi_{k_{3}}\varphi_{l_{3}}\\
&+3L^{-5}L_{ij}L^{k_{3}l_{3}}\bar\varphi_{k_{3}}\not E\varphi_{l_{3}}\\
&-L^{-3}\bar\varphi_{(i}\not E\varphi_{j)}\\
&-16iL^{-1}\bar\chi_{(i}\varphi_{j)}\\
&+16iL^{-3}L_{ij}L_{k_{3}l_{3}}\bar\chi^{k_{3}}\varphi^{l_{3}}\\
&+2L^{-3}L_{k_{3}(i}\bar\varphi^{k_{3}}\not{\mathcal D}\varphi_{j)}\\
&-3L^{-5}L_{k_{3}(i}L^{l_{3}m_{3}}\bar\varphi^{k_{3}}(\not{\mathcal D}L_{j)l_{3}})\varphi_{m_{3}}\\
&+\frac12L^{-3}\bar\varphi^{l_{3}}(\not{\mathcal D}L_{l_{3}(i})\varphi_{j)}\\
&+\frac12L^{-3}\bar\varphi^{m_{3}}(\not{\mathcal D}L_{ij})\varphi_{m_{3}}\\
&+2iL^{-3}L_{ij}\bar\varphi\gamma\!\cdot\!T\varphi\\
&+\frac{15}{2}L^{-7}L_{ij}(L^{k_{3}l_{3}}\bar\varphi_{k_{3}}\varphi_{l_{3}})^{2}\\
&-3L^{-5}(L^{k_{3}l_{3}}\bar\varphi_{k_{3}}\varphi_{l_{3}})\bar\varphi_{(i}\varphi_{j)}\\
&-\frac32L^{-5}L_{ij}(\bar\varphi_{m_{3}}\varphi_{n_{3}})(\bar\varphi^{m_{3}}\varphi^{n_{3}})
\end{aligned}\right]
\end{aligned}\end{gathered}
\tag{75}
```

<!-- END STEP5 GROUP 09 -->

#### Additive group 10

<!-- BEGIN STEP5 GROUP 10 -->

```math
\begin{gathered}-\frac{3\rho'}4\bar\lambda'{}^i\gamma^a [\frac14\gamma\!\cdot\!\widehat G\psi_{ai} -\gamma\!\cdot\!T\psi_{ai}+\frac g2L_{ij}\psi_a{}^j-\phi_{ai}]\\\longmapsto\\\begin{aligned}
&-\frac34\left[\begin{aligned}
&2L^{-1}N\\
&+iL^{-3}L_{i_{1}j_{1}}\bar\varphi^{i_{1}}\varphi^{j_{1}}
\end{aligned}\right]\\
&{}\times \varepsilon^{ir_{2}}\left[\begin{aligned}
&-2iL^{-1}(\mathcal D_{c_{3}}\bar\varphi_{r_{2}})\gamma^{c_{3}}\\
&+16L^{-1}L_{r_{2}j_{3}}\bar\chi^{j_{3}}\\
&-4L^{-1}\bar\varphi_{r_{2}}\gamma\!\cdot\!T\\
&-2NL^{-3}L_{r_{2}j_{3}}\bar\varphi^{j_{3}}\\
&+2iL^{-3}L^{j_{3}k_{3}}\bar\varphi_{k_{3}}(\not{\mathcal D}L_{r_{2}j_{3}})\\
&-2iL^{-3}L_{r_{2}j_{3}}\bar\varphi^{j_{3}}\not E\\
&+2iL^{-3}\bar\varphi^{j_{3}}(\bar\varphi_{r_{2}}\varphi_{j_{3}})\\
&-6iL^{-5}\bar\varphi^{j_{3}}(\bar\varphi_{k_{3}}\varphi_{l_{3}})L^{k_{3}l_{3}}L_{r_{2}j_{3}}
\end{aligned}\right]\\
&{}\times \gamma^a [\frac14\gamma\!\cdot\!\widehat G\psi_{ai} -\gamma\!\cdot\!T\psi_{ai}+\frac g2L_{ij}\psi_a{}^j-\phi_{ai}]
\end{aligned}\end{gathered}
\tag{76}
```

<!-- END STEP5 GROUP 10 -->

#### Additive group 11

<!-- BEGIN STEP5 GROUP 11 -->

```math
\begin{gathered}-\frac12A'_a(\mathcal D_b\rho')\widehat G^{ab}\\\longmapsto\\\begin{aligned}
&-\frac12\left[\begin{aligned}
&2L^{-1}E_{a}\\
&+\sqrt2V_{a}\\
&-L^{-3}L_{i_{1}j_{1}}\bar\varphi^{i_{1}}\gamma_{a}\varphi^{j_{1}}\\
&-iL^{-1}\bar\varphi^{i_{1}}\psi_{ai_{1}}
\end{aligned}\right]\\
&{}\times (\mathcal D_b\left[\begin{aligned}
&2L^{-1}N\\
&+iL^{-3}L_{i_{2}j_{2}}\bar\varphi^{i_{2}}\varphi^{j_{2}}
\end{aligned}\right])\\
&{}\times \widehat G^{ab}
\end{aligned}\end{gathered}
\tag{77}
```

<!-- END STEP5 GROUP 11 -->

#### Additive group 12

<!-- BEGIN STEP5 GROUP 12 -->

```math
\begin{gathered}-\frac12A'_a\rho'\mathcal D_b\widehat G^{ab}\\\longmapsto\\\begin{aligned}
&-\frac12\left[\begin{aligned}
&2L^{-1}E_{a}\\
&+\sqrt2V_{a}\\
&-L^{-3}L_{i_{1}j_{1}}\bar\varphi^{i_{1}}\gamma_{a}\varphi^{j_{1}}\\
&-iL^{-1}\bar\varphi^{i_{1}}\psi_{ai_{1}}
\end{aligned}\right]\\
&{}\times \left[\begin{aligned}
&2L^{-1}N\\
&+iL^{-3}L_{i_{2}j_{2}}\bar\varphi^{i_{2}}\varphi^{j_{2}}
\end{aligned}\right]\\
&{}\times \mathcal D_b\widehat G^{ab}
\end{aligned}\end{gathered}
\tag{78}
```

<!-- END STEP5 GROUP 12 -->

#### Additive group 13

<!-- BEGIN STEP5 GROUP 13 -->

```math
\begin{gathered}-\frac12A'_a\mathcal D_b\widehat F'^{ab}\\\longmapsto\\\begin{aligned}
&-\frac12\left[\begin{aligned}
&2L^{-1}E_{a}\\
&+\sqrt2V_{a}\\
&-L^{-3}L_{i_{1}j_{1}}\bar\varphi^{i_{1}}\gamma_{a}\varphi^{j_{1}}\\
&-iL^{-1}\bar\varphi^{i_{1}}\psi_{ai_{1}}
\end{aligned}\right]\\
&{}\times \mathcal D_b\left(e^{a\mu_{2}}e^{b\nu_{2}}\left[\begin{aligned}
&4L^{-1}\mathcal D_{[\mu_{2}}E_{\nu_{2}]}\\
&-4L^{-2}(\mathcal D_{[\mu_{2}}L)E_{\nu_{2}]}\\
&+2L^{-1}\widehat R_{\mu_{2}\nu_{2}}^{i_{3}j_{3}}(V)L_{i_{3}j_{3}}\\
&-2L^{-3}L_{k_{3}}{}^{l_{3}}\mathcal D_{[\mu_{2}}L^{k_{3}p_{3}}\mathcal D_{\nu_{2}]}L_{l_{3}p_{3}}\\
&+6L^{-4}(\mathcal D_{[\mu_{2}}L)L_{i_{3}j_{3}}\bar\varphi^{i_{3}}\gamma_{\nu_{2}]}\varphi^{j_{3}}\\
&-2L^{-3}(\mathcal D_{[\mu_{2}}L_{i_{3}j_{3}})\bar\varphi^{i_{3}}\gamma_{\nu_{2}]}\varphi^{j_{3}}\\
&-2L^{-3}L_{i_{3}j_{3}}(\mathcal D_{[\mu_{2}}\bar\varphi^{i_{3}})\gamma_{\nu_{2}]}\varphi^{j_{3}}\\
&-2L^{-3}L_{i_{3}j_{3}}\bar\varphi^{i_{3}}\gamma_{[\nu_{2}}\mathcal D_{\mu_{2}]}\varphi^{j_{3}}\\
&-iL^{-1}\bar\varphi^{i_{3}}\widehat R_{\mu_{2}\nu_{2} i_{3}}(Q)
\end{aligned}\right]\right)
\end{aligned}\end{gathered}
\tag{79}
```

<!-- END STEP5 GROUP 13 -->

#### Additive group 14

<!-- BEGIN STEP5 GROUP 14 -->

```math
\begin{gathered}+8A'_a(\mathcal D_b\rho')T^{ab}\\\longmapsto\\\begin{aligned}
&+8\left[\begin{aligned}
&2L^{-1}E_{a}\\
&+\sqrt2V_{a}\\
&-L^{-3}L_{i_{1}j_{1}}\bar\varphi^{i_{1}}\gamma_{a}\varphi^{j_{1}}\\
&-iL^{-1}\bar\varphi^{i_{1}}\psi_{ai_{1}}
\end{aligned}\right]\\
&{}\times (\mathcal D_b\left[\begin{aligned}
&2L^{-1}N\\
&+iL^{-3}L_{i_{2}j_{2}}\bar\varphi^{i_{2}}\varphi^{j_{2}}
\end{aligned}\right])\\
&{}\times T^{ab}
\end{aligned}\end{gathered}
\tag{80}
```

<!-- END STEP5 GROUP 14 -->

#### Additive group 15

<!-- BEGIN STEP5 GROUP 15 -->

```math
\begin{gathered}+8A'_a\rho'\mathcal D_bT^{ab}\\\longmapsto\\\begin{aligned}
&+8\left[\begin{aligned}
&2L^{-1}E_{a}\\
&+\sqrt2V_{a}\\
&-L^{-3}L_{i_{1}j_{1}}\bar\varphi^{i_{1}}\gamma_{a}\varphi^{j_{1}}\\
&-iL^{-1}\bar\varphi^{i_{1}}\psi_{ai_{1}}
\end{aligned}\right]\\
&{}\times \left[\begin{aligned}
&2L^{-1}N\\
&+iL^{-3}L_{i_{2}j_{2}}\bar\varphi^{i_{2}}\varphi^{j_{2}}
\end{aligned}\right]\\
&{}\times \mathcal D_bT^{ab}
\end{aligned}\end{gathered}
\tag{81}
```

<!-- END STEP5 GROUP 15 -->

#### Additive group 16

<!-- BEGIN STEP5 GROUP 16 -->

```math
\begin{gathered}-\frac18A'_a\varepsilon^{abcde}\widehat F'_{bc}\widehat G_{de}\\\longmapsto\\\begin{aligned}
&-\frac18\left[\begin{aligned}
&2L^{-1}E_{a}\\
&+\sqrt2V_{a}\\
&-L^{-3}L_{i_{1}j_{1}}\bar\varphi^{i_{1}}\gamma_{a}\varphi^{j_{1}}\\
&-iL^{-1}\bar\varphi^{i_{1}}\psi_{ai_{1}}
\end{aligned}\right]\\
&{}\times \varepsilon^{abcde}e_{b}{}^{\mu_{2}}e_{c}{}^{\nu_{2}}\left[\begin{aligned}
&4L^{-1}\mathcal D_{[\mu_{2}}E_{\nu_{2}]}\\
&-4L^{-2}(\mathcal D_{[\mu_{2}}L)E_{\nu_{2}]}\\
&+2L^{-1}\widehat R_{\mu_{2}\nu_{2}}^{i_{3}j_{3}}(V)L_{i_{3}j_{3}}\\
&-2L^{-3}L_{k_{3}}{}^{l_{3}}\mathcal D_{[\mu_{2}}L^{k_{3}p_{3}}\mathcal D_{\nu_{2}]}L_{l_{3}p_{3}}\\
&+6L^{-4}(\mathcal D_{[\mu_{2}}L)L_{i_{3}j_{3}}\bar\varphi^{i_{3}}\gamma_{\nu_{2}]}\varphi^{j_{3}}\\
&-2L^{-3}(\mathcal D_{[\mu_{2}}L_{i_{3}j_{3}})\bar\varphi^{i_{3}}\gamma_{\nu_{2}]}\varphi^{j_{3}}\\
&-2L^{-3}L_{i_{3}j_{3}}(\mathcal D_{[\mu_{2}}\bar\varphi^{i_{3}})\gamma_{\nu_{2}]}\varphi^{j_{3}}\\
&-2L^{-3}L_{i_{3}j_{3}}\bar\varphi^{i_{3}}\gamma_{[\nu_{2}}\mathcal D_{\mu_{2}]}\varphi^{j_{3}}\\
&-iL^{-1}\bar\varphi^{i_{3}}\widehat R_{\mu_{2}\nu_{2} i_{3}}(Q)
\end{aligned}\right]\\
&{}\times \widehat G_{de}
\end{aligned}\end{gathered}
\tag{82}
```

<!-- END STEP5 GROUP 16 -->

#### Additive group 17

<!-- BEGIN STEP5 GROUP 17 -->

```math
\begin{gathered}-\frac i4A'_a\bar\lambda'{}^i\gamma^{ab} [\frac14\gamma\!\cdot\!\widehat G\psi_{bi} -\gamma\!\cdot\!T\psi_{bi}+\frac g2L_{ij}\psi_b{}^j-\phi_{bi}]\\\longmapsto\\\begin{aligned}
&-\frac i4\left[\begin{aligned}
&2L^{-1}E_{a}\\
&+\sqrt2V_{a}\\
&-L^{-3}L_{i_{1}j_{1}}\bar\varphi^{i_{1}}\gamma_{a}\varphi^{j_{1}}\\
&-iL^{-1}\bar\varphi^{i_{1}}\psi_{ai_{1}}
\end{aligned}\right]\\
&{}\times \varepsilon^{ir_{2}}\left[\begin{aligned}
&-2iL^{-1}(\mathcal D_{c_{3}}\bar\varphi_{r_{2}})\gamma^{c_{3}}\\
&+16L^{-1}L_{r_{2}j_{3}}\bar\chi^{j_{3}}\\
&-4L^{-1}\bar\varphi_{r_{2}}\gamma\!\cdot\!T\\
&-2NL^{-3}L_{r_{2}j_{3}}\bar\varphi^{j_{3}}\\
&+2iL^{-3}L^{j_{3}k_{3}}\bar\varphi_{k_{3}}(\not{\mathcal D}L_{r_{2}j_{3}})\\
&-2iL^{-3}L_{r_{2}j_{3}}\bar\varphi^{j_{3}}\not E\\
&+2iL^{-3}\bar\varphi^{j_{3}}(\bar\varphi_{r_{2}}\varphi_{j_{3}})\\
&-6iL^{-5}\bar\varphi^{j_{3}}(\bar\varphi_{k_{3}}\varphi_{l_{3}})L^{k_{3}l_{3}}L_{r_{2}j_{3}}
\end{aligned}\right]\\
&{}\times \gamma^{ab} [\frac14\gamma\!\cdot\!\widehat G\psi_{bi} -\gamma\!\cdot\!T\psi_{bi}+\frac g2L_{ij}\psi_b{}^j-\phi_{bi}]
\end{aligned}\end{gathered}
\tag{83}
```

<!-- END STEP5 GROUP 17 -->

#### Additive group 18

<!-- BEGIN STEP5 GROUP 18 -->

```math
\begin{gathered}-\frac14A'_a\rho'\bar\psi_b{}^i\gamma^{ba}\gamma^c [\frac14\gamma\!\cdot\!\widehat G\psi_{ci} -\gamma\!\cdot\!T\psi_{ci}+\frac g2L_{ij}\psi_c{}^j-\phi_{ci}]\\\longmapsto\\\begin{aligned}
&-\frac14\left[\begin{aligned}
&2L^{-1}E_{a}\\
&+\sqrt2V_{a}\\
&-L^{-3}L_{i_{1}j_{1}}\bar\varphi^{i_{1}}\gamma_{a}\varphi^{j_{1}}\\
&-iL^{-1}\bar\varphi^{i_{1}}\psi_{ai_{1}}
\end{aligned}\right]\\
&{}\times \left[\begin{aligned}
&2L^{-1}N\\
&+iL^{-3}L_{i_{2}j_{2}}\bar\varphi^{i_{2}}\varphi^{j_{2}}
\end{aligned}\right]\\
&{}\times \bar\psi_b{}^i\gamma^{ba}\gamma^c [\frac14\gamma\!\cdot\!\widehat G\psi_{ci} -\gamma\!\cdot\!T\psi_{ci}+\frac g2L_{ij}\psi_c{}^j-\phi_{ci}]
\end{aligned}\end{gathered}
\tag{84}
```

<!-- END STEP5 GROUP 18 -->

#### Additive group 19

<!-- BEGIN STEP5 GROUP 19 -->

```math
\begin{gathered}-\frac14A'_a\bar\psi_b{}^i\gamma^{ba}\not{\mathcal D}\lambda'_i\\\longmapsto\\\begin{aligned}
&-\frac14\left[\begin{aligned}
&2L^{-1}E_{a}\\
&+\sqrt2V_{a}\\
&-L^{-3}L_{i_{1}j_{1}}\bar\varphi^{i_{1}}\gamma_{a}\varphi^{j_{1}}\\
&-iL^{-1}\bar\varphi^{i_{1}}\psi_{ai_{1}}
\end{aligned}\right]\\
&{}\times \bar\psi_b{}^i\gamma^{ba}\not{\mathcal D}\left[\begin{aligned}
&-2iL^{-1}\not{\mathcal D}\varphi_{i}\\
&+16L^{-1}L_{ij_{2}}\chi^{j_{2}}\\
&+4L^{-1}\gamma\!\cdot\!T\varphi_{i}\\
&-2NL^{-3}L_{ij_{2}}\varphi^{j_{2}}\\
&+2iL^{-3}(\not{\mathcal D}L_{ij_{2}})L^{j_{2}k_{2}}\varphi_{k_{2}}\\
&-2iL^{-3}\not E L_{ij_{2}}\varphi^{j_{2}}\\
&+2iL^{-3}\varphi^{j_{2}}\bar\varphi_{i}\varphi_{j_{2}}\\
&-6iL^{-5}\varphi^{j_{2}}\bar\varphi_{k_{2}}\varphi_{l_{2}}L^{k_{2}l_{2}}L_{ij_{2}}
\end{aligned}\right]
\end{aligned}\end{gathered}
\tag{85}
```

<!-- END STEP5 GROUP 19 -->

#### Additive group 20

<!-- BEGIN STEP5 GROUP 20 -->

```math
\begin{gathered}+\frac i2A'_a\bar\psi_b{}^i\gamma^{ba}\gamma\!\cdot\!T\lambda'_i\\\longmapsto\\\begin{aligned}
&+\frac i2\left[\begin{aligned}
&2L^{-1}E_{a}\\
&+\sqrt2V_{a}\\
&-L^{-3}L_{i_{1}j_{1}}\bar\varphi^{i_{1}}\gamma_{a}\varphi^{j_{1}}\\
&-iL^{-1}\bar\varphi^{i_{1}}\psi_{ai_{1}}
\end{aligned}\right]\\
&{}\times \bar\psi_b{}^i\gamma^{ba}\gamma\!\cdot\!T\left[\begin{aligned}
&-2iL^{-1}\not{\mathcal D}\varphi_{i}\\
&+16L^{-1}L_{ij_{2}}\chi^{j_{2}}\\
&+4L^{-1}\gamma\!\cdot\!T\varphi_{i}\\
&-2NL^{-3}L_{ij_{2}}\varphi^{j_{2}}\\
&+2iL^{-3}(\not{\mathcal D}L_{ij_{2}})L^{j_{2}k_{2}}\varphi_{k_{2}}\\
&-2iL^{-3}\not E L_{ij_{2}}\varphi^{j_{2}}\\
&+2iL^{-3}\varphi^{j_{2}}\bar\varphi_{i}\varphi_{j_{2}}\\
&-6iL^{-5}\varphi^{j_{2}}\bar\varphi_{k_{2}}\varphi_{l_{2}}L^{k_{2}l_{2}}L_{ij_{2}}
\end{aligned}\right]
\end{aligned}\end{gathered}
\tag{86}
```

<!-- END STEP5 GROUP 20 -->

#### Additive group 21

<!-- BEGIN STEP5 GROUP 21 -->

```math
\begin{gathered}-4iA'_a\rho'\bar\psi_b{}^i\gamma^{ba}\chi_i\\\longmapsto\\\begin{aligned}
&-4i\left[\begin{aligned}
&2L^{-1}E_{a}\\
&+\sqrt2V_{a}\\
&-L^{-3}L_{i_{1}j_{1}}\bar\varphi^{i_{1}}\gamma_{a}\varphi^{j_{1}}\\
&-iL^{-1}\bar\varphi^{i_{1}}\psi_{ai_{1}}
\end{aligned}\right]\\
&{}\times \left[\begin{aligned}
&2L^{-1}N\\
&+iL^{-3}L_{i_{2}j_{2}}\bar\varphi^{i_{2}}\varphi^{j_{2}}
\end{aligned}\right]\\
&{}\times \bar\psi_b{}^i\gamma^{ba}\chi_i
\end{aligned}\end{gathered}
\tag{87}
```

<!-- END STEP5 GROUP 21 -->

#### Additive group 22

<!-- BEGIN STEP5 GROUP 22 -->

```math
\begin{gathered}-\frac i{16}A'_a\bar\psi_b{}^i\gamma^{ba}\gamma\!\cdot\!\widehat G\lambda'_i\\\longmapsto\\\begin{aligned}
&-\frac i{16}\left[\begin{aligned}
&2L^{-1}E_{a}\\
&+\sqrt2V_{a}\\
&-L^{-3}L_{i_{1}j_{1}}\bar\varphi^{i_{1}}\gamma_{a}\varphi^{j_{1}}\\
&-iL^{-1}\bar\varphi^{i_{1}}\psi_{ai_{1}}
\end{aligned}\right]\\
&{}\times \bar\psi_b{}^i\gamma^{ba}\gamma\!\cdot\!\widehat G\left[\begin{aligned}
&-2iL^{-1}\not{\mathcal D}\varphi_{i}\\
&+16L^{-1}L_{ij_{2}}\chi^{j_{2}}\\
&+4L^{-1}\gamma\!\cdot\!T\varphi_{i}\\
&-2NL^{-3}L_{ij_{2}}\varphi^{j_{2}}\\
&+2iL^{-3}(\not{\mathcal D}L_{ij_{2}})L^{j_{2}k_{2}}\varphi_{k_{2}}\\
&-2iL^{-3}\not E L_{ij_{2}}\varphi^{j_{2}}\\
&+2iL^{-3}\varphi^{j_{2}}\bar\varphi_{i}\varphi_{j_{2}}\\
&-6iL^{-5}\varphi^{j_{2}}\bar\varphi_{k_{2}}\varphi_{l_{2}}L^{k_{2}l_{2}}L_{ij_{2}}
\end{aligned}\right]
\end{aligned}\end{gathered}
\tag{88}
```

<!-- END STEP5 GROUP 22 -->

#### Additive group 23

<!-- BEGIN STEP5 GROUP 23 -->

```math
\begin{gathered}+\frac{ig}8A'_a\bar\psi_b{}^i\gamma^{ba}L_{ij}\lambda'{}^j\\\longmapsto\\\begin{aligned}
&+\frac{ig}8\left[\begin{aligned}
&2L^{-1}E_{a}\\
&+\sqrt2V_{a}\\
&-L^{-3}L_{i_{1}j_{1}}\bar\varphi^{i_{1}}\gamma_{a}\varphi^{j_{1}}\\
&-iL^{-1}\bar\varphi^{i_{1}}\psi_{ai_{1}}
\end{aligned}\right]\\
&{}\times \bar\psi_b{}^i\gamma^{ba}L_{ij}\varepsilon^{jr_{2}}\left[\begin{aligned}
&-2iL^{-1}\not{\mathcal D}\varphi_{r_{2}}\\
&+16L^{-1}L_{r_{2}j_{3}}\chi^{j_{3}}\\
&+4L^{-1}\gamma\!\cdot\!T\varphi_{r_{2}}\\
&-2NL^{-3}L_{r_{2}j_{3}}\varphi^{j_{3}}\\
&+2iL^{-3}(\not{\mathcal D}L_{r_{2}j_{3}})L^{j_{3}k_{3}}\varphi_{k_{3}}\\
&-2iL^{-3}\not E L_{r_{2}j_{3}}\varphi^{j_{3}}\\
&+2iL^{-3}\varphi^{j_{3}}\bar\varphi_{r_{2}}\varphi_{j_{3}}\\
&-6iL^{-5}\varphi^{j_{3}}\bar\varphi_{k_{3}}\varphi_{l_{3}}L^{k_{3}l_{3}}L_{r_{2}j_{3}}
\end{aligned}\right]
\end{aligned}\end{gathered}
\tag{89}
```

<!-- END STEP5 GROUP 23 -->

#### Additive group 24

<!-- BEGIN STEP5 GROUP 24 -->

```math
\begin{gathered}-\frac g8A'_a\rho'\bar\psi_b{}^i\gamma^{abc}\psi_c{}^jL_{ij}\\\longmapsto\\\begin{aligned}
&-\frac g8\left[\begin{aligned}
&2L^{-1}E_{a}\\
&+\sqrt2V_{a}\\
&-L^{-3}L_{i_{1}j_{1}}\bar\varphi^{i_{1}}\gamma_{a}\varphi^{j_{1}}\\
&-iL^{-1}\bar\varphi^{i_{1}}\psi_{ai_{1}}
\end{aligned}\right]\\
&{}\times \left[\begin{aligned}
&2L^{-1}N\\
&+iL^{-3}L_{i_{2}j_{2}}\bar\varphi^{i_{2}}\varphi^{j_{2}}
\end{aligned}\right]\\
&{}\times \bar\psi_b{}^i\gamma^{abc}\psi_c{}^jL_{ij}
\end{aligned}\end{gathered}
\tag{90}
```

<!-- END STEP5 GROUP 24 -->

#### Additive group 25

<!-- BEGIN STEP5 GROUP 25 -->

```math
\begin{gathered}+\frac14A'_a\bar\psi_b{}^i\gamma^{abc}\psi_c{}^jY'_{ij}\\\longmapsto\\\begin{aligned}
&+\frac14\left[\begin{aligned}
&2L^{-1}E_{a}\\
&+\sqrt2V_{a}\\
&-L^{-3}L_{i_{1}j_{1}}\bar\varphi^{i_{1}}\gamma_{a}\varphi^{j_{1}}\\
&-iL^{-1}\bar\varphi^{i_{1}}\psi_{ai_{1}}
\end{aligned}\right]\\
&{}\times \bar\psi_b{}^i\gamma^{abc}\psi_c{}^j\left[\begin{aligned}
&L^{-1}\square^{c} L_{ij}\\
&-L^{-3}L^{k_{2}m_{2}}\mathcal D_{c_{2}}L_{k_{2}(i}\mathcal D^{c_{2}}L_{j)m_{2}}\\
&-L^{-3}L_{ij}N^{2}\\
&-L^{-3}L_{ij}E_{c_{2}}E^{c_{2}}\\
&+2L^{-3}E_{c_{2}}L_{k_{2}(i}\mathcal D^{c_{2}}L_{j)}{}^{k_{2}}\\
&+\frac83L^{-1}L_{ij}T^{2}\\
&+4L^{-1}L_{ij}D\\
&+iNL^{-3}\bar\varphi_{(i}\varphi_{j)}\\
&-3iNL^{-5}L_{ij}L^{k_{2}l_{2}}\bar\varphi_{k_{2}}\varphi_{l_{2}}\\
&+3L^{-5}L_{ij}L^{k_{2}l_{2}}\bar\varphi_{k_{2}}\not E\varphi_{l_{2}}\\
&-L^{-3}\bar\varphi_{(i}\not E\varphi_{j)}\\
&-16iL^{-1}\bar\chi_{(i}\varphi_{j)}\\
&+16iL^{-3}L_{ij}L_{k_{2}l_{2}}\bar\chi^{k_{2}}\varphi^{l_{2}}\\
&+2L^{-3}L_{k_{2}(i}\bar\varphi^{k_{2}}\not{\mathcal D}\varphi_{j)}\\
&-3L^{-5}L_{k_{2}(i}L^{l_{2}m_{2}}\bar\varphi^{k_{2}}(\not{\mathcal D}L_{j)l_{2}})\varphi_{m_{2}}\\
&+\frac12L^{-3}\bar\varphi^{l_{2}}(\not{\mathcal D}L_{l_{2}(i})\varphi_{j)}\\
&+\frac12L^{-3}\bar\varphi^{m_{2}}(\not{\mathcal D}L_{ij})\varphi_{m_{2}}\\
&+2iL^{-3}L_{ij}\bar\varphi\gamma\!\cdot\!T\varphi\\
&+\frac{15}{2}L^{-7}L_{ij}(L^{k_{2}l_{2}}\bar\varphi_{k_{2}}\varphi_{l_{2}})^{2}\\
&-3L^{-5}(L^{k_{2}l_{2}}\bar\varphi_{k_{2}}\varphi_{l_{2}})\bar\varphi_{(i}\varphi_{j)}\\
&-\frac32L^{-5}L_{ij}(\bar\varphi_{m_{2}}\varphi_{n_{2}})(\bar\varphi^{m_{2}}\varphi^{n_{2}})
\end{aligned}\right]
\end{aligned}\end{gathered}
\tag{91}
```

<!-- END STEP5 GROUP 25 -->

#### Additive group 26

<!-- BEGIN STEP5 GROUP 26 -->

```math
\begin{gathered}+\frac12\rho'\Box_c\rho'\\\longmapsto\\\begin{aligned}
&+\frac12\left[\begin{aligned}
&2L^{-1}N\\
&+iL^{-3}L_{i_{1}j_{1}}\bar\varphi^{i_{1}}\varphi^{j_{1}}
\end{aligned}\right]\\
&{}\times \Box_c\left[\begin{aligned}
&2L^{-1}N\\
&+iL^{-3}L_{i_{2}j_{2}}\bar\varphi^{i_{2}}\varphi^{j_{2}}
\end{aligned}\right]
\end{aligned}\end{gathered}
\tag{92}
```

<!-- END STEP5 GROUP 26 -->

#### Additive group 27

<!-- BEGIN STEP5 GROUP 27 -->

```math
\begin{gathered}+(\rho')^2 f_a{}^a\\\longmapsto\\\begin{aligned}
&+(\left[\begin{aligned}
&2L^{-1}N\\
&+iL^{-3}L_{i_{1}j_{1}}\bar\varphi^{i_{1}}\varphi^{j_{1}}
\end{aligned}\right])^2\\
&{}\times f_a{}^a
\end{aligned}\end{gathered}
\tag{93}
```

<!-- END STEP5 GROUP 27 -->

#### Additive group 28

<!-- BEGIN STEP5 GROUP 28 -->

```math
\begin{gathered}-\frac14\rho'\widehat F'_{ab}\widehat G^{ab}\\\longmapsto\\\begin{aligned}
&-\frac14\left[\begin{aligned}
&2L^{-1}N\\
&+iL^{-3}L_{i_{1}j_{1}}\bar\varphi^{i_{1}}\varphi^{j_{1}}
\end{aligned}\right]\\
&{}\times e_{a}{}^{\mu_{2}}e_{b}{}^{\nu_{2}}\left[\begin{aligned}
&4L^{-1}\mathcal D_{[\mu_{2}}E_{\nu_{2}]}\\
&-4L^{-2}(\mathcal D_{[\mu_{2}}L)E_{\nu_{2}]}\\
&+2L^{-1}\widehat R_{\mu_{2}\nu_{2}}^{i_{3}j_{3}}(V)L_{i_{3}j_{3}}\\
&-2L^{-3}L_{k_{3}}{}^{l_{3}}\mathcal D_{[\mu_{2}}L^{k_{3}p_{3}}\mathcal D_{\nu_{2}]}L_{l_{3}p_{3}}\\
&+6L^{-4}(\mathcal D_{[\mu_{2}}L)L_{i_{3}j_{3}}\bar\varphi^{i_{3}}\gamma_{\nu_{2}]}\varphi^{j_{3}}\\
&-2L^{-3}(\mathcal D_{[\mu_{2}}L_{i_{3}j_{3}})\bar\varphi^{i_{3}}\gamma_{\nu_{2}]}\varphi^{j_{3}}\\
&-2L^{-3}L_{i_{3}j_{3}}(\mathcal D_{[\mu_{2}}\bar\varphi^{i_{3}})\gamma_{\nu_{2}]}\varphi^{j_{3}}\\
&-2L^{-3}L_{i_{3}j_{3}}\bar\varphi^{i_{3}}\gamma_{[\nu_{2}}\mathcal D_{\mu_{2}]}\varphi^{j_{3}}\\
&-iL^{-1}\bar\varphi^{i_{3}}\widehat R_{\mu_{2}\nu_{2} i_{3}}(Q)
\end{aligned}\right]\\
&{}\times \widehat G^{ab}
\end{aligned}\end{gathered}
\tag{94}
```

<!-- END STEP5 GROUP 28 -->

#### Additive group 29

<!-- BEGIN STEP5 GROUP 29 -->

```math
\begin{gathered}+4(\rho')^2\widehat G_{ab}T^{ab}\\\longmapsto\\\begin{aligned}
&+4(\left[\begin{aligned}
&2L^{-1}N\\
&+iL^{-3}L_{i_{1}j_{1}}\bar\varphi^{i_{1}}\varphi^{j_{1}}
\end{aligned}\right])^2\\
&{}\times \widehat G_{ab}T^{ab}
\end{aligned}\end{gathered}
\tag{95}
```

<!-- END STEP5 GROUP 29 -->

#### Additive group 30

<!-- BEGIN STEP5 GROUP 30 -->

```math
\begin{gathered}+4\rho'\widehat F'_{ab}T^{ab}\\\longmapsto\\\begin{aligned}
&+4\left[\begin{aligned}
&2L^{-1}N\\
&+iL^{-3}L_{i_{1}j_{1}}\bar\varphi^{i_{1}}\varphi^{j_{1}}
\end{aligned}\right]\\
&{}\times e_{a}{}^{\mu_{2}}e_{b}{}^{\nu_{2}}\left[\begin{aligned}
&4L^{-1}\mathcal D_{[\mu_{2}}E_{\nu_{2}]}\\
&-4L^{-2}(\mathcal D_{[\mu_{2}}L)E_{\nu_{2}]}\\
&+2L^{-1}\widehat R_{\mu_{2}\nu_{2}}^{i_{3}j_{3}}(V)L_{i_{3}j_{3}}\\
&-2L^{-3}L_{k_{3}}{}^{l_{3}}\mathcal D_{[\mu_{2}}L^{k_{3}p_{3}}\mathcal D_{\nu_{2}]}L_{l_{3}p_{3}}\\
&+6L^{-4}(\mathcal D_{[\mu_{2}}L)L_{i_{3}j_{3}}\bar\varphi^{i_{3}}\gamma_{\nu_{2}]}\varphi^{j_{3}}\\
&-2L^{-3}(\mathcal D_{[\mu_{2}}L_{i_{3}j_{3}})\bar\varphi^{i_{3}}\gamma_{\nu_{2}]}\varphi^{j_{3}}\\
&-2L^{-3}L_{i_{3}j_{3}}(\mathcal D_{[\mu_{2}}\bar\varphi^{i_{3}})\gamma_{\nu_{2}]}\varphi^{j_{3}}\\
&-2L^{-3}L_{i_{3}j_{3}}\bar\varphi^{i_{3}}\gamma_{[\nu_{2}}\mathcal D_{\mu_{2}]}\varphi^{j_{3}}\\
&-iL^{-1}\bar\varphi^{i_{3}}\widehat R_{\mu_{2}\nu_{2} i_{3}}(Q)
\end{aligned}\right]\\
&{}\times T^{ab}
\end{aligned}\end{gathered}
\tag{96}
```

<!-- END STEP5 GROUP 30 -->

#### Additive group 31

<!-- BEGIN STEP5 GROUP 31 -->

```math
\begin{gathered}-4(\rho')^2D\\\longmapsto\\\begin{aligned}
&-4(\left[\begin{aligned}
&2L^{-1}N\\
&+iL^{-3}L_{i_{1}j_{1}}\bar\varphi^{i_{1}}\varphi^{j_{1}}
\end{aligned}\right])^2\\
&{}\times D
\end{aligned}\end{gathered}
\tag{97}
```

<!-- END STEP5 GROUP 31 -->

#### Additive group 32

<!-- BEGIN STEP5 GROUP 32 -->

```math
\begin{gathered}-\frac{104}{3}(\rho')^2T^2\\\longmapsto\\\begin{aligned}
&-\frac{104}{3}(\left[\begin{aligned}
&2L^{-1}N\\
&+iL^{-3}L_{i_{1}j_{1}}\bar\varphi^{i_{1}}\varphi^{j_{1}}
\end{aligned}\right])^2\\
&{}\times T^2
\end{aligned}\end{gathered}
\tag{98}
```

<!-- END STEP5 GROUP 32 -->

#### Additive group 33

<!-- BEGIN STEP5 GROUP 33 -->

```math
\begin{gathered}+8i\rho'\bar\chi\lambda'\\\longmapsto\\\begin{aligned}
&+8i\left[\begin{aligned}
&2L^{-1}N\\
&+iL^{-3}L_{i_{1}j_{1}}\bar\varphi^{i_{1}}\varphi^{j_{1}}
\end{aligned}\right]\\
&{}\times \bar\chi^i\left[\begin{aligned}
&-2iL^{-1}\not{\mathcal D}\varphi_{i}\\
&+16L^{-1}L_{ij_{2}}\chi^{j_{2}}\\
&+4L^{-1}\gamma\!\cdot\!T\varphi_{i}\\
&-2NL^{-3}L_{ij_{2}}\varphi^{j_{2}}\\
&+2iL^{-3}(\not{\mathcal D}L_{ij_{2}})L^{j_{2}k_{2}}\varphi_{k_{2}}\\
&-2iL^{-3}\not E L_{ij_{2}}\varphi^{j_{2}}\\
&+2iL^{-3}\varphi^{j_{2}}\bar\varphi_{i}\varphi_{j_{2}}\\
&-6iL^{-5}\varphi^{j_{2}}\bar\varphi_{k_{2}}\varphi_{l_{2}}L^{k_{2}l_{2}}L_{ij_{2}}
\end{aligned}\right]
\end{aligned}\end{gathered}
\tag{99}
```

<!-- END STEP5 GROUP 33 -->

#### Additive group 34

<!-- BEGIN STEP5 GROUP 34 -->

```math
\begin{gathered}-5(\rho')^2\bar\psi_a{}^i\gamma^a\chi_i\\\longmapsto\\\begin{aligned}
&-5(\left[\begin{aligned}
&2L^{-1}N\\
&+iL^{-3}L_{i_{1}j_{1}}\bar\varphi^{i_{1}}\varphi^{j_{1}}
\end{aligned}\right])^2\\
&{}\times \bar\psi_a{}^i\gamma^a\chi_i
\end{aligned}\end{gathered}
\tag{100}
```

<!-- END STEP5 GROUP 34 -->

#### Additive group 35

<!-- BEGIN STEP5 GROUP 35 -->

```math
\begin{gathered}+\frac i4\rho'\bar\psi_a{}^i\gamma^a\not{\mathcal D}\lambda'_i\\\longmapsto\\\begin{aligned}
&+\frac i4\left[\begin{aligned}
&2L^{-1}N\\
&+iL^{-3}L_{i_{1}j_{1}}\bar\varphi^{i_{1}}\varphi^{j_{1}}
\end{aligned}\right]\\
&{}\times \bar\psi_a{}^i\gamma^a\not{\mathcal D}\left[\begin{aligned}
&-2iL^{-1}\not{\mathcal D}\varphi_{i}\\
&+16L^{-1}L_{ij_{2}}\chi^{j_{2}}\\
&+4L^{-1}\gamma\!\cdot\!T\varphi_{i}\\
&-2NL^{-3}L_{ij_{2}}\varphi^{j_{2}}\\
&+2iL^{-3}(\not{\mathcal D}L_{ij_{2}})L^{j_{2}k_{2}}\varphi_{k_{2}}\\
&-2iL^{-3}\not E L_{ij_{2}}\varphi^{j_{2}}\\
&+2iL^{-3}\varphi^{j_{2}}\bar\varphi_{i}\varphi_{j_{2}}\\
&-6iL^{-5}\varphi^{j_{2}}\bar\varphi_{k_{2}}\varphi_{l_{2}}L^{k_{2}l_{2}}L_{ij_{2}}
\end{aligned}\right]
\end{aligned}\end{gathered}
\tag{101}
```

<!-- END STEP5 GROUP 35 -->

#### Additive group 36

<!-- BEGIN STEP5 GROUP 36 -->

```math
\begin{gathered}+\frac12\rho'\bar\psi_a{}^i\gamma^a\gamma\!\cdot\!T\lambda'_i\\\longmapsto\\\begin{aligned}
&+\frac12\left[\begin{aligned}
&2L^{-1}N\\
&+iL^{-3}L_{i_{1}j_{1}}\bar\varphi^{i_{1}}\varphi^{j_{1}}
\end{aligned}\right]\\
&{}\times \bar\psi_a{}^i\gamma^a\gamma\!\cdot\!T\left[\begin{aligned}
&-2iL^{-1}\not{\mathcal D}\varphi_{i}\\
&+16L^{-1}L_{ij_{2}}\chi^{j_{2}}\\
&+4L^{-1}\gamma\!\cdot\!T\varphi_{i}\\
&-2NL^{-3}L_{ij_{2}}\varphi^{j_{2}}\\
&+2iL^{-3}(\not{\mathcal D}L_{ij_{2}})L^{j_{2}k_{2}}\varphi_{k_{2}}\\
&-2iL^{-3}\not E L_{ij_{2}}\varphi^{j_{2}}\\
&+2iL^{-3}\varphi^{j_{2}}\bar\varphi_{i}\varphi_{j_{2}}\\
&-6iL^{-5}\varphi^{j_{2}}\bar\varphi_{k_{2}}\varphi_{l_{2}}L^{k_{2}l_{2}}L_{ij_{2}}
\end{aligned}\right]
\end{aligned}\end{gathered}
\tag{102}
```

<!-- END STEP5 GROUP 36 -->

#### Additive group 37

<!-- BEGIN STEP5 GROUP 37 -->

```math
\begin{gathered}-\frac1{16}\rho'\bar\psi_a{}^i\gamma^a\gamma\!\cdot\!\widehat G\lambda'_i\\\longmapsto\\\begin{aligned}
&-\frac1{16}\left[\begin{aligned}
&2L^{-1}N\\
&+iL^{-3}L_{i_{1}j_{1}}\bar\varphi^{i_{1}}\varphi^{j_{1}}
\end{aligned}\right]\\
&{}\times \bar\psi_a{}^i\gamma^a\gamma\!\cdot\!\widehat G\left[\begin{aligned}
&-2iL^{-1}\not{\mathcal D}\varphi_{i}\\
&+16L^{-1}L_{ij_{2}}\chi^{j_{2}}\\
&+4L^{-1}\gamma\!\cdot\!T\varphi_{i}\\
&-2NL^{-3}L_{ij_{2}}\varphi^{j_{2}}\\
&+2iL^{-3}(\not{\mathcal D}L_{ij_{2}})L^{j_{2}k_{2}}\varphi_{k_{2}}\\
&-2iL^{-3}\not E L_{ij_{2}}\varphi^{j_{2}}\\
&+2iL^{-3}\varphi^{j_{2}}\bar\varphi_{i}\varphi_{j_{2}}\\
&-6iL^{-5}\varphi^{j_{2}}\bar\varphi_{k_{2}}\varphi_{l_{2}}L^{k_{2}l_{2}}L_{ij_{2}}
\end{aligned}\right]
\end{aligned}\end{gathered}
\tag{103}
```

<!-- END STEP5 GROUP 37 -->

#### Additive group 38

<!-- BEGIN STEP5 GROUP 38 -->

```math
\begin{gathered}+\frac g8\rho'\bar\psi_a{}^i\gamma^aL_{ij}\lambda'{}^j\\\longmapsto\\\begin{aligned}
&+\frac g8\left[\begin{aligned}
&2L^{-1}N\\
&+iL^{-3}L_{i_{1}j_{1}}\bar\varphi^{i_{1}}\varphi^{j_{1}}
\end{aligned}\right]\\
&{}\times \bar\psi_a{}^i\gamma^aL_{ij}\varepsilon^{jr_{2}}\left[\begin{aligned}
&-2iL^{-1}\not{\mathcal D}\varphi_{r_{2}}\\
&+16L^{-1}L_{r_{2}j_{3}}\chi^{j_{3}}\\
&+4L^{-1}\gamma\!\cdot\!T\varphi_{r_{2}}\\
&-2NL^{-3}L_{r_{2}j_{3}}\varphi^{j_{3}}\\
&+2iL^{-3}(\not{\mathcal D}L_{r_{2}j_{3}})L^{j_{3}k_{3}}\varphi_{k_{3}}\\
&-2iL^{-3}\not E L_{r_{2}j_{3}}\varphi^{j_{3}}\\
&+2iL^{-3}\varphi^{j_{3}}\bar\varphi_{r_{2}}\varphi_{j_{3}}\\
&-6iL^{-5}\varphi^{j_{3}}\bar\varphi_{k_{3}}\varphi_{l_{3}}L^{k_{3}l_{3}}L_{r_{2}j_{3}}
\end{aligned}\right]
\end{aligned}\end{gathered}
\tag{104}
```

<!-- END STEP5 GROUP 38 -->

#### Additive group 39

<!-- BEGIN STEP5 GROUP 39 -->

```math
\begin{gathered}+\frac i4(\rho')^2\bar\psi_a{}^i\gamma^a\gamma^b [\frac14\gamma\!\cdot\!\widehat G\psi_{bi} -\gamma\!\cdot\!T\psi_{bi}+\frac g2L_{ij}\psi_b{}^j-\phi_{bi}]\\\longmapsto\\\begin{aligned}
&+\frac i4(\left[\begin{aligned}
&2L^{-1}N\\
&+iL^{-3}L_{i_{1}j_{1}}\bar\varphi^{i_{1}}\varphi^{j_{1}}
\end{aligned}\right])^2\\
&{}\times \bar\psi_a{}^i\gamma^a\gamma^b [\frac14\gamma\!\cdot\!\widehat G\psi_{bi} -\gamma\!\cdot\!T\psi_{bi}+\frac g2L_{ij}\psi_b{}^j-\phi_{bi}]
\end{aligned}\end{gathered}
\tag{105}
```

<!-- END STEP5 GROUP 39 -->

#### Additive group 40

<!-- BEGIN STEP5 GROUP 40 -->

```math
\begin{gathered}-\frac i4(\rho')^2\bar\psi_a{}^i [\frac14\gamma\!\cdot\!\widehat G\psi^a_i -\gamma\!\cdot\!T\psi^a_i+\frac g2L_{ij}\psi^{aj}-\phi^a_i]\\\longmapsto\\\begin{aligned}
&-\frac i4(\left[\begin{aligned}
&2L^{-1}N\\
&+iL^{-3}L_{i_{1}j_{1}}\bar\varphi^{i_{1}}\varphi^{j_{1}}
\end{aligned}\right])^2\\
&{}\times \bar\psi_a{}^i [\frac14\gamma\!\cdot\!\widehat G\psi^a_i -\gamma\!\cdot\!T\psi^a_i+\frac g2L_{ij}\psi^{aj}-\phi^a_i]
\end{aligned}\end{gathered}
\tag{106}
```

<!-- END STEP5 GROUP 40 -->

#### Additive group 41

<!-- BEGIN STEP5 GROUP 41 -->

```math
\begin{gathered}-\frac{ig}8(\rho')^2\bar\psi_a{}^i\gamma^{ab}\psi_b{}^jL_{ij}\\\longmapsto\\\begin{aligned}
&-\frac{ig}8(\left[\begin{aligned}
&2L^{-1}N\\
&+iL^{-3}L_{i_{1}j_{1}}\bar\varphi^{i_{1}}\varphi^{j_{1}}
\end{aligned}\right])^2\\
&{}\times \bar\psi_a{}^i\gamma^{ab}\psi_b{}^jL_{ij}
\end{aligned}\end{gathered}
\tag{107}
```

<!-- END STEP5 GROUP 41 -->

#### Additive group 42

<!-- BEGIN STEP5 GROUP 42 -->

```math
\begin{gathered}+\frac i4\rho'\bar\psi_a{}^i\gamma^{ab}\psi_b{}^jY'_{ij}\\\longmapsto\\\begin{aligned}
&+\frac i4\left[\begin{aligned}
&2L^{-1}N\\
&+iL^{-3}L_{i_{1}j_{1}}\bar\varphi^{i_{1}}\varphi^{j_{1}}
\end{aligned}\right]\\
&{}\times \bar\psi_a{}^i\gamma^{ab}\psi_b{}^j\left[\begin{aligned}
&L^{-1}\square^{c} L_{ij}\\
&-L^{-3}L^{k_{2}m_{2}}\mathcal D_{c_{2}}L_{k_{2}(i}\mathcal D^{c_{2}}L_{j)m_{2}}\\
&-L^{-3}L_{ij}N^{2}\\
&-L^{-3}L_{ij}E_{c_{2}}E^{c_{2}}\\
&+2L^{-3}E_{c_{2}}L_{k_{2}(i}\mathcal D^{c_{2}}L_{j)}{}^{k_{2}}\\
&+\frac83L^{-1}L_{ij}T^{2}\\
&+4L^{-1}L_{ij}D\\
&+iNL^{-3}\bar\varphi_{(i}\varphi_{j)}\\
&-3iNL^{-5}L_{ij}L^{k_{2}l_{2}}\bar\varphi_{k_{2}}\varphi_{l_{2}}\\
&+3L^{-5}L_{ij}L^{k_{2}l_{2}}\bar\varphi_{k_{2}}\not E\varphi_{l_{2}}\\
&-L^{-3}\bar\varphi_{(i}\not E\varphi_{j)}\\
&-16iL^{-1}\bar\chi_{(i}\varphi_{j)}\\
&+16iL^{-3}L_{ij}L_{k_{2}l_{2}}\bar\chi^{k_{2}}\varphi^{l_{2}}\\
&+2L^{-3}L_{k_{2}(i}\bar\varphi^{k_{2}}\not{\mathcal D}\varphi_{j)}\\
&-3L^{-5}L_{k_{2}(i}L^{l_{2}m_{2}}\bar\varphi^{k_{2}}(\not{\mathcal D}L_{j)l_{2}})\varphi_{m_{2}}\\
&+\frac12L^{-3}\bar\varphi^{l_{2}}(\not{\mathcal D}L_{l_{2}(i})\varphi_{j)}\\
&+\frac12L^{-3}\bar\varphi^{m_{2}}(\not{\mathcal D}L_{ij})\varphi_{m_{2}}\\
&+2iL^{-3}L_{ij}\bar\varphi\gamma\!\cdot\!T\varphi\\
&+\frac{15}{2}L^{-7}L_{ij}(L^{k_{2}l_{2}}\bar\varphi_{k_{2}}\varphi_{l_{2}})^{2}\\
&-3L^{-5}(L^{k_{2}l_{2}}\bar\varphi_{k_{2}}\varphi_{l_{2}})\bar\varphi_{(i}\varphi_{j)}\\
&-\frac32L^{-5}L_{ij}(\bar\varphi_{m_{2}}\varphi_{n_{2}})(\bar\varphi^{m_{2}}\varphi^{n_{2}})
\end{aligned}\right]
\end{aligned}\end{gathered}
\tag{108}
```

<!-- END STEP5 GROUP 42 -->

## 5. Consistency Checks

The displayed substitution contains the exact scalar, all eight gaugino terms, all 21 triplet terms and the complete field strength, organized as 76 replacement brackets and 42 source groups. The [component-check runner](../../../../checks/run_component_checks.py) uses this map in the retained supercovariant insertion and compares the regenerated raw and collected tensor records with the current expected action data. Its mathematical scope is stated in the [package guide](../../../../README.md).

### Weyl weights and fermion parity

| Quantity | Weight | Explicit fermion degrees of the anchored formula |
|---|---:|---|
| $`L,L_{ij}`$ | $`3`$ | $`0`$ |
| $`\varphi_i`$ | $`7/2`$ | $`1`$ |
| $`E_a,N`$ | $`4`$ | $`0`$ |
| $`T,\chi,D`$ | $`1,3/2,2`$ | full gauged slots retained |
| $`\rho'`$ | $`1`$ | $`0,2`$ |
| $`\lambda'_i`$ | $`3/2`$ | $`1,3`$ |
| $`Y'_{ij}`$ | $`2`$ | $`0,2,4`$ |
| $`A'_a,\widehat F'_{ab}`$ | $`1,2`$ | implicit source completions retained |

The component weights in the table give the following termwise checks:
```math
\begin{aligned}
w(L^{-3}L_{ij}\bar\varphi^i\varphi^j)&=-9+3+7=1,\\
w(L^{-5}\varphi^j\bar\varphi_k\varphi_lL^{kl}L_{ij})
&=-15+\frac{21}{2}+6=\frac32,\\
w(L^{-7}L_{ij}(L^{kl}\bar\varphi_k\varphi_l)^2)
&=-21+3+2(3+7)=2,\\
w(L^{-1}\bar\varphi\widehat R_{ab}(Q))&=-3+\frac72+\frac32=2,\\
w(L^{-1}\bar\varphi\psi_a)&=-3+\frac72+\frac12=1.
\end{aligned}
\tag{109}
```
Thus every replacement has the weight and parity of the primed vector component that it replaces. The inherited pre-gauge BF rows consequently retain weight five. On the gauge slice compensator powers differ among terms and must be restored before comparing individual terms: $`Y'^2`$ inherited a factor $`\sigma`$, whereas $`-g\rho'Y'^{ij}L_{ij}`$ inherited $`\sigma^{-1}`$. Assigning them equal weights after setting $`\sigma=1`$ would be an incorrect dimension test.

The complete source triplet has seven explicit degree-zero terms, eleven bilinears and three quartics. Its square therefore contains ordered blocks with degrees $`0,2,4,6,8`$. Writing two complete brackets multiplies every term of one by every term of the other; it includes all $`21\times21=441`$ ordered products. The multiplicities are
```math
\begin{aligned}
(7+11z^2+3z^4)^2
&=49+154z^2+163z^4+66z^6+9z^8,\\
49+154+163+66+9&=441,\\
(6z+2z^3)^2&=36z^2+24z^4+4z^6.
\end{aligned}
\tag{110}
```
Here $`z`$ is only a formal fermion-degree counter, not a field. The last polynomial counts the $`8\times8`$ products of two complete gaugino slots. It does not commute their spinors or assert that these formal terms are independent after Fierz identities. No higher block has been deleted. Implicit fermions in the covariant derivatives and gauged slots remain in addition to these explicit-degree counts.

### Bosonic and ungauged coefficient checks

As a check of the substitution coefficients, hold the universal background slots fixed and formally set gravitini, $`\varphi`$, $`E,T,\chi,D,f,V`$ and ordinary jets to zero, while keeping $`L>0,N`$ and the explicit $`g`$ symbolic. This is a coefficient test in the universal source algebra, **not** a solution of the gauged Coomans composites or an auxiliary-field elimination. The surviving map and density are
```math
\begin{aligned}
\rho'&=\frac{2N}{L},&Y'_{ij}&=-\frac{N^2}{\sqrt2L^2}\delta_{ij},&
\lambda'_i&=\widehat F'_{ab}=A'_a=0,\\
Y'^{ij}Y'_{ij}
&=\frac{N^4}{2L^4}\delta^{ij}\delta_{ij}=\frac{N^4}{L^4},\\
-g\rho'Y'^{ij}L_{ij}
&=-g\frac{2N}{L}\left(-\frac{N^2}{2L}\delta^{ij}\delta_{ij}\right)
=\frac{2gN^3}{L^2},\\
e^{-1}\mathcal L_{VL}\big|_{\rm coefficient\ test}
&=\frac{N^4}{L^4}+\frac{2gN^3}{L^2}
\ \xrightarrow{g\to0}\ \frac{N^4}{L^4}.
\end{aligned}
\tag{111}
```
The exact epsilon-matrix calculation and symbolic scalar test in the verifier reproduce these two coefficients independently of the 42-group output. In a true bosonic or ungauged **action** comparison the full Coomans slots must also be specialized; that later normalization/completion comparison is not claimed here.

### Covariance, indices, boundaries and scope

Every replacement preserves its free index slots; all internal contraction indices are freshly renamed before products. The independent alpha-renaming checks preserve repeated-index incidence and upper/lower positions. The full potential identity was tested for all ten spacetime pairs with exact zero/two/quartic exterior coefficients, then extended to $`L>0`$ by the constant-input homogeneity argument. No ordinary-field derivative has been set to zero merely by Gold (7) or triplet alignment.

No integration by parts or field equation was used in the density. The sole displayed boundary relation is the check of the residual potential gauge freedom. All source bar phases and contorsion are retained. Full nonlinear action reality, full local supersymmetry and source-normalization matching remain distinct Step 6 obligations; the coefficient checks do not assert those results.

## 6. Final Result

Step 5 gives the complete **local composite substitution** of the earlier full vector map into the corrected Step 4 density. Its fully displayed endpoint is the sum of the 42 right-hand sides in Section 4.7:
```math
\boxed{
\left.e^{-1}\mathcal L_{VL}\right|_{\substack{\sigma=1,\ b_\mu=0,\ \psi^i=0\\ L_{ij}=\delta_{ij}L/\sqrt2}}
=\sum_{r=1}^{42}\big[\text{right-hand side of additive group }r\big].
}
\tag{112}
```
The sum refers to the explicitly written formulas, not to unnamed composite fields. There are no residual primed vector components in those right-hand sides. Their only fields are the original unprimed linear multiplet, the gauged background fields and source connections/curvatures. The scalar box and spinor derivative use the complete unprimed-argument definitions in Section 4.6. The local $`A'_\mu`$ replacement includes both fermionic terms and satisfies the full ordinary/hatted-strength bridge.

This result is locked as **R2-PRIMED-COMPOSITE-INSERTION-v1**. It completes the requested map insertion; it does not promote the action to the completed, normalized full gauged $`R^2`$ invariant before Step 6.

## 7. Convention Dependence and Remaining Uncertainties

- The endpoint is an off-shell equality on Gold (7) and the additionally authorized **local** Gold (25) alignment. The general-triplet map and earlier gauge-unfixed parent are preserved. Outside this local alignment patch, a varying triplet direction contributes the source orientation term and the displayed potential cannot be used unchanged.
- The same original unprimed $`(L_{ij},\varphi_i,E_a,N)`$ enters both vector maps. The gauge-fixed defining gaugino is $`\psi^i`$; the retained $`\psi_\mu{}^i`$ is the gravitino. No new fermion, component identification or effective-vector sum was introduced.
- Every explicit term of the earlier source map is retained, including cubic and quartic terms. Full gauged $`T,\chi,D`$ slots remain implicit everywhere, including covariant derivatives and dependent connections. Coomans' source-omitted higher-fermion completion is not set to zero and must be resolved in Step 6.
- The map is singular at $`L=0`$. Neither the local potential proof nor the action insertion extends through that locus without a different composite chart.
- Gold bosonic normalization, full common gauged expansion, full action reality/supersymmetry, auxiliary-field dynamics and spectrum are not performed in Step 5. No auxiliary equation or on-shell representative is used to simplify this result.
