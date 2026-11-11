

The equations and reported residuals below belong to the cited construction. Finite component tests and formal symbolic identities retain their distinct scopes; the former do not establish an unrestricted symbolic identity.

# LOG form, potential and BF interface certification

**Result.** The component current and compact BF action already used in the active calculation are the pullbacks of the source superforms. The generic form/potential interface can be closed, conditional on using a genuine linear multiplet. The full potential law follows, including its undifferentiated-parameter terms; this conclusion is stronger than the earlier principal-$`\partial\epsilon`$ test. The earlier local note made a separate spinor-index-lowering error: literal C24 (2.50) differs from the required current by **$`2Q_1`$ only**, not $`2(Q_1+Q_2)`$. C24 (3.2b) must use the **ordinary** four-form dual in its vector coupling, as its cited original derivation explicitly does. These corrections change the source-interface explanation and its test, not the active $`P=E+Q_1+Q_2`$ density.

This bounded report does not independently prove that all expanded LOG component polynomials satisfy the linear constraint. That input belongs to the parallel curved-multiplet verification. The closed-superform argument below certifies the generic BF assembly once that input has been established.

Contents: 1. Inputs and conventions; 2. Spinor-index calculation; 3. Complete four-form pullback; 4. Full potential law; 5. Closed BF form and component action; 6. Gauged compact action; 7. Checks, exact scope and repair ledger.

## 1. Problem and target

The old FORM-01 gate concerned three potentially inconsistent objects: the covariant vector $`\mathcal H_G^a`$, the ordinary curl current $`h_G^a`$, and the current which multiplies $`v_{Ga}`$ in the action. None may be identified merely because their bosonic limits coincide. We reconstruct them using the differential form from which the linear multiplet follows.

Source equations used here are: C24 **(2.12)–(2.16), (2.41)–(2.42), (2.50)–(2.54), (3.2)**, especially [C24 (2.50)](https://arxiv.org/abs/2311.00679) and [C24 (2.54)](https://arxiv.org/abs/2311.00679). The source does not reproduce the lower components of the superfour-form or the five-form pullback; it explicitly refers to its ref. 30. The bibliography identifies that reference as Butter, Kuzenko, Novak and Tartaglino-Mazzucchelli, *Conformal supergravity in five dimensions: New approach and applications*, JHEP 02 (2015) 111, [arXiv:1410.8682v2, §§8.1–8.2](https://arxiv.org/html/1410.8682v2). That exact missing input justified consulting this external primary source. The HTML, selected equation TeX, checks and source hashes are cached under [sources/certification_20260925/form/](../../../../log/action/details/component_construction/EXTERNAL_REFERENCES.md#ref-f79ee9495bf2).

The scoped locks are `GAUGED-LOG-CONVENTIONS-v1` and `GAUGED-LOG-STEP1-v1`. We use $`a=0,\ldots,4`$, $`\alpha=1,\ldots,4`$, $`i=1,2`$, mostly-plus $`\eta`$, unit-weight brackets, linear Majorana bar $`\bar u=u^T C`$, and odd spinors and supersymmetry parameters. This is a classical, local, off-shell calculation; there is no Fourier transform, background assumption, field equation or auxiliary-field elimination. The independent linear multiplet is initially arbitrary. Higher fermions of the composite LOG multiplet can be truncated only after applying this interface.

The complete slots needed here are

```math
G_G^{ij}=-\frac12L^{ij},\qquad \varphi_G^i=\frac i2\varphi^i,\qquad F_G=-N,\qquad \mathcal H_G^a=E^a;\qquad W_G=\rho,\quad v_G=-A,\quad\lambda_G=-\lambda,\quad X_G^{ij}=2Y^{ij}.
\tag{FI01}
```

The first line is the previously derived covariant Q/S bridge, not a new fit to the current. The remaining conventions are

```math
\Gamma_G^a=i\gamma^a,\qquad \Sigma_G^{ab}=\frac12\gamma^{ab},\qquad \epsilon_G^{abcde}=-\epsilon_B^{abcde},\qquad \epsilon_B^{01234}=1,\qquad \epsilon_B=2\xi_G,\qquad \psi_{Ga}=\psi_a.
\tag{FI02}
```

In the parameter identity the unsubscripted $`\epsilon_B`$ is a spinor parameter; $`\epsilon_B^{abcde}`$ is the orientation tensor. We keep them distinct by their indices. Source versus project SU(2) metric signs compensate their opposite-side lowering conventions, so arrays for an already lowered doublet agree; nevertheless $`\bar u_i Mv^i=-\bar u^i Mv_i`$. The spinor metric in this calibrated basis is $`\varepsilon^{\alpha\beta}=-C`$, $`\varepsilon_{\alpha\beta}=C`$, with $`C^2=-1`$. The matrices $`\Gamma_\alpha{}^\beta`$ and $`\Sigma_\alpha{}^\beta`$ act on lower spinor columns.

## 2. The index-lowering calculation which fixes the local audit error

The source convention, already correctly used by Step 2 (S2-02) and Step 6 (S6-02), is

```math
M_{\alpha\beta}=\varepsilon_{\beta\gamma}M_\alpha{}^\gamma.
\tag{FI03}
```

The summed $`\gamma`$ is the column index of $`M`$ but the column index of $`\varepsilon`$ too. Thus this is multiplication by the **transpose** of the lower metric:

```math
M_{\downarrow\downarrow}=MC^T=-MC,\qquad U:=\varepsilon^{\uparrow\uparrow}=-C,\qquad U^T=C.
\tag{FI04}
```

For two independent lower spinor columns $`u,v`$, keeping their order unchanged gives

```math
u^\alpha M_\alpha{}^\beta v_\beta=u^T U^T Mv=\bar uMv,\qquad u^\alpha M_{\alpha\beta}v^\beta=u^TU^T(-MC)Uv=-\bar uMv.
\tag{FI05}
```

The second result uses $`(-MC)(-C)=MC^2=-M`$. No Grassmann interchange was used to obtain its minus. Equivalently, the full kernel is $`U^T(-MC)U=-CM`$.

Old note 07 (LB42) used $`MC`$ instead of $`MC^T`$. Its algebraic identity $`U^T(MC)U=CM`$ is true for that matrix, but that matrix is **not** $`\Sigma_{\alpha\beta}`$ under (FI03). Its claimed application to C24 (2.50) is therefore false. This is the specific local error, rather than a change to the source or to the Step 2–6 tensor conventions.

For later use define the component bilinears

```math
Q_1^a:=\frac i2\bar\psi_b\gamma^{ba}\varphi,\qquad Q_2^a:=\frac14\bar\psi_b^i\gamma^{abc}\psi_c^jL_{ij}.
\tag{FI06}
```

The two raw Gold contractions convert separately:

```math
2(\Sigma_G^{ab})_\alpha{}^\beta\psi_{bi}^{\alpha}\varphi_{G\beta}^{i}=\frac i2\bar\psi_{bi}\gamma^{ab}\varphi^i=-\frac i2\bar\psi_b^i\gamma^{ab}\varphi_i=Q_1^a,
\tag{FI07}
```

and

```math
\frac i2\epsilon_G^{abcde}(\Sigma_{Gbc})_{\alpha\beta}\psi_{di}^{\alpha}\psi_{ej}^{\beta}G_G^{ij}=-\frac i8\epsilon_B^{abcde}\bar\psi_d^i\gamma_{bc}\psi_e^jL_{ij}=Q_2^a.
\tag{FI08}
```

The first coefficient in (FI08) is $`(i/2)(-1)(-1/2)(-1/2)=-i/8`$: orientation, generator/raised-spinor kernel, and triplet respectively. Both lowered SU(2) indices are converted together with the upper triplet, producing $`L_{ij}`$ without an additional sign. The last equality uses $`\epsilon_B^{abcde}\gamma_{bc}=2i\gamma^{ade}`$.

## 3. The entire four-form pullback

Write $`\Phi_4=d\mathcal B_3`$. Source (8.3) uses the reversed basis order

```math
\Phi_4=\frac1{4!}E^D\wedge E^C\wedge E^B\wedge E^A\Phi_{ABCD},\qquad E^a\Vert=e^a,\qquad E_i^\alpha\Vert=\frac12\psi_i^\alpha.
\tag{FI09}
```

The second projection is C24 (2.12)–(2.13); $`\Vert`$ means the pullback to $`\theta=d\theta=0`$. Source (8.6a–c) gives all nonzero components:

```math
\Phi_{ab\,\alpha^i\beta^j}=8i(\Sigma_{ab})_{\alpha\beta}G_G^{ij},\qquad \Phi_{abc\,\alpha}^{i}=-2\epsilon_{Gabcde}(\Sigma^{de})_\alpha{}^\beta\varphi_{G\beta}^{i},\qquad \Phi_{abcd}=\epsilon_{Gabcde}\mathcal H_G^e,
\tag{FI10}
```

while components with three or four spinor legs vanish. These formulas contain no truncation in the independent linear multiplet fields.

Here is the combinatorial sign, rather than an assumed bosonic pullback. For a $`p`$-form term with $`k`$ fermionic legs, there are $`\binom pk`$ placements. The $`k`$ factors $`E_i^\alpha\Vert`$ give $`2^{-k}`$. Moving the fermionic tensor slots to the right, together with moving their world indices to the front of the antisymmetrization, gives $`(-1)^{k(p-k)}`$. The reversed vielbein product reverses the order of the $`k`$ odd gravitino coefficients; returning them to ascending world-index order gives $`(-1)^{k(k-1)/2}`$. Thus

```math
c_{p,k}=2^{-k}\binom pk(-1)^{k(p-k)+k(k-1)/2}.
\tag{FI11}
```

For $`p=5`$, this yields $`(1,5/2,-5/2,-5/4,5/16,1/32)`$, exactly the independently printed source (8.27). For $`p=4`$, the first three coefficients are $`(1,-2,-3/2)`$. The remaining two multiply vanishing components in (FI10). Consequently the ordinary four-form components are exactly

```math
h_{abcd}=\Phi_{abcd}|-2\psi_{[a i}^{\alpha}\Phi_{bcd]\,\alpha}^{i}|-\frac32\psi_{[a i}^{\alpha}\psi_{b j}^{\beta}\Phi_{cd]\,\alpha^i\beta^j}|=4\partial_{[a}b_{G bcd]},
\tag{FI12}
```

with inverse vielbeins understood in the last expression if the chosen frame is not coordinate. A completely unambiguous curved-coordinate version is $`h_{mnpq}=4\partial_{[m}b_{Gnpq]}`$ followed by conversion of all four indices to tangent indices.

Now use the ordinary dual

```math
h_G^a=-\frac1{24}\epsilon_G^{abcde}h_{bcde}.
\tag{FI13}
```

The top component gives $`\mathcal H_G^a`$ because $`\epsilon_G^{abcde}\epsilon_{Gbcdef}=-24\delta^a_f`$. The single-gravitino term in (FI12) is $`+4\psi_{[b}\epsilon_{Gcde]fg}\Sigma^{fg}\varphi_G`$. After contraction its coefficient is

```math
-\frac4{24}\epsilon_G^{abcde}\epsilon_{Gcdefg}\psi_{bi}\Sigma^{fg}\varphi_G^i=-\frac16(-6)(\delta^a_f\delta^b_g-\delta^a_g\delta^b_f)\psi_{bi}\Sigma^{fg}\varphi_G^i=2\psi_{bi}\Sigma^{ab}\varphi_G^i.
\tag{FI14}
```

The two-gravitino term is $`-(3/2)8i\psi_{[b i}^{\alpha}\psi_{c j}^{\beta}(\Sigma_{de]})_{\alpha\beta}G^{ij}`$. Its dual gives $`+i\epsilon_G^{abcde}(\Sigma_{bc})_{\alpha\beta}\psi_{di}^{\alpha}\psi_{ej}^{\beta}G^{ij}/2`$. Therefore

```math
h_G^a=\mathcal H_G^a+2(\Sigma_G^{ab})_\alpha{}^\beta\psi_{bi}^{\alpha}\varphi_{G\beta}^{i}+\frac i2\epsilon_G^{abcde}(\Sigma_{Gbc})_{\alpha\beta}\psi_{di}^{\alpha}\psi_{ej}^{\beta}G_G^{ij}=E^a+Q_1^a+Q_2^a.
\tag{FI15}
```

The corresponding local potential normalization, fixed already by the bosonic top slot, is

```math
b_{Gmnp}=-\frac12E_{mnp},\qquad P^a:=h_G^a=-\frac1{12}\epsilon_B^{abcde}e_b{}^m e_c{}^n e_d{}^p e_e{}^q\partial_m E_{npq},\qquad E^a=P^a-Q_1^a-Q_2^a.
\tag{FI16}
```

This normalization is now a full superform identification, locally modulo a closed three-form and the two-form gauge parameter, rather than only a bosonic guess.

The source (8.5) Bianchi identity is $`d\Phi_4=0`$. Its tangent-component consequence is source (8.9): $`\nabla^a\mathcal H_{Ga}+5iX^{\gamma k}\varphi_{G\gamma k}=\widehat\nabla^a\mathcal H_{Ga}=0`$. The hat here is the source **traceless superspace frame**, whose vector connection differs from the original frame; it is not a removal of fermion terms. C24 uses this traceless frame and prints its covariant constraint as $`\nabla^a\mathcal H_{Ga}=0`$. Transporting the full derivative gives the project constraint $`\mathcal D^aE_a=0`$. Independently, the ordinary pullback has

```math
\partial_m(eP^m)=0,
\tag{FI17}
```

because its divergence is proportional to the symmetric $`\partial_m\partial_n`$ contracted with the antisymmetric coordinate epsilon. Equations (FI17) and $`\mathcal D\cdot E=0`$ are two descriptions of this Bianchi identity; they are not permission to replace $`P`$ by $`E`$ in an ordinary Abelian coupling.

**Literal-source discrepancy.** Solving (FI15) for $`\mathcal H_G`$ requires minus signs in front of both raw Gold bilinears. C24 (2.50) instead prints plus in front of the single-gravitino bilinear and minus in front of the double-gravitino bilinear. Its exact conversion is

```math
\mathcal H_G^{a}\big|_{\mathrm{C24\ literal}}=h_G^a+Q_1^a-Q_2^a,\qquad \mathcal H_G^a\big|_{\mathrm{superform}}=h_G^a-Q_1^a-Q_2^a,\qquad \Delta_{\mathrm{literal-required}}\mathcal H_G^a=2Q_1^a.
\tag{FI18}
```

Thus only the first source completion sign is inconsistent with this form reconstruction. The old local plus-$`Q_2`$ conversion was the separate error diagnosed in §2. The raw printed formula must remain preserved as a source record; (FI18) is a derived correction under the fixed dictionary, not a claim that a published erratum exists.

## 4. Derivation of the full potential law

For a superform potential the covariant local supersymmetry variation, including a redefinition of its gauge parameter, is the contraction with its field strength:

```math
\delta_\xi\mathcal B_3=i_\xi\Phi_4+d\Lambda_2.
\tag{FI19}
```

This is the Cartan identity $`\mathcal L_\xi\mathcal B_3=i_\xi d\mathcal B_3+d(i_\xi\mathcal B_3)`$, with the latter term absorbed in $`d\Lambda_2`$. In source component ordering $`(i_\xi\Phi)_{ABC}=\xi^D\Phi_{DABC}`$. When taking the pullback the parameter stays to the right of the reversed vielbein coefficients until the Grassmann signs have been taken. For no gravitino, moving the first spinor slot through three vector slots gives a minus. For one gravitino there are three positions. In position $`r=0,1,2`$, moving the two fermion slots past vectors gives $`(-1)^{2+(2-r)}`$, and the world antisymmetrization gives $`(-1)^r`$; their product is plus in every case. Each vielbein supplies $`1/2`$. Thus

```math
\delta b_{Gabc}=-\xi_i^\alpha\Phi_{abc\,\alpha}^i|+\frac32\psi_{[a i}^{\alpha}\xi_j^\beta\Phi_{bc]\,\alpha^i\beta^j}|+3\partial_{[a}\Lambda_{bc]}.
\tag{FI20}
```

There are no further gravitino terms: the requisite three-spinor components of $`\Phi`$ vanish. Inserting (FI10) gives

```math
\delta b_{Gabc}=2\epsilon_{Gabcde}\xi_i^\alpha(\Sigma^{de})_\alpha{}^\beta\varphi_{G\beta}^i+12i\psi_{[a i}^{\alpha}\xi_j^\beta(\Sigma_{bc]})_{\alpha\beta}G_G^{ij}+3\partial_{[a}\Lambda_{bc]}.
\tag{FI21}
```

In the second term, $`\Sigma_{\alpha\beta}\xi^\beta=(-MC)(-C)\xi_\downarrow=-M\xi_\downarrow`$. Converting both SU(2) indices together with $`G^{ij}`$ then gives

```math
\delta b_{Gmnp}=2\epsilon_{Gabcde}e_m^ae_n^be_p^c(\xi_i\Sigma^{de}\varphi_G^i)-12i(\psi_{[m}^{i}\Sigma_{np]}\xi^j)G_{Gij}+3\partial_{[m}\Lambda_{np]}.
\tag{FI22}
```

This reproduces **both terms of literal C24 (2.54)** with their exact coefficients and index order. It is the full local potential transformation modulo its form gauge symmetry, not only a determination of the coefficients of $`\partial\xi`$.

For transparency the first project coefficient follows from

```math
2\epsilon_G\xi_i\Sigma_G\varphi_G^i=-\frac i4\epsilon_B\bar\epsilon_{Bi}\gamma_2\varphi^i=\frac i4\epsilon_B\bar\epsilon_B\gamma_2\varphi=-\frac12\bar\epsilon_B\gamma_3\varphi.
\tag{FI23}
```

The last step uses $`\epsilon_{Babcde}\gamma^{de}=2i\gamma_{abc}`$. The second coefficient is $`(-12i)(1/2)(1/2)(-1/2)=3i/2`$. Dividing both by $`b_G/E_3=-1/2`$ yields

```math
\boxed{\delta E_{mnp}=\bar\epsilon_B\gamma_{mnp}\varphi-3i\bar\psi_{[m}^{i}\gamma_{np]}\epsilon_B^jL_{ij}+3\partial_{[m}\Lambda^{(B)}_{np]}.}
\tag{FI24}
```

This also explains the earlier independent cancellation of the principal parameter derivatives in $`E=P-Q_1-Q_2`$. Literal OP (2.24) has coefficients $`(-1,+1)`$ and is incompatible with (FI24) under the already fixed covariant slot/current map. Their ratios are not a common potential rescaling. Its discrepancy remains a quarantined literal source formula; the complete superform construction now supports the operational $`(+1,-3)`$ law.

The geometry proves more than a principal test: $`d\Phi=0`$ implies $`\delta\Phi=\mathcal L_\xi\Phi`$ with all curvature and connection terms included. Commutators of superdiffeomorphisms close by the graded Lie bracket; choosing the covariant representative (FI19) changes closure only by a form-gauge transformation. No component equation of motion is used. On a gauge-fixed realization, the compensating superconformal transformation is composed with this same identity; it does not change the form definition or require expanding every curvature.

## 5. Closed BF form, normalization and all seven component slots

Let the defining vector one-form be $`V`$, with $`F_2=dV`$, and let $`\Sigma_G`$ be the source curvature-induced five-form. Source **(8.19), (8.22), (8.25)** gives

```math
d\Sigma_G=F_2\wedge\Phi_4,\qquad \mathfrak J=V\wedge\Phi_4-\Sigma_G,\qquad d\mathfrak J=F_2\wedge\Phi_4-V\wedge d\Phi_4-d\Sigma_G=0.
\tag{FI25}
```

The overall sign here is the literal (8.25). The opposite sign also defines a closed form but reverses the action normalization; it is not silently substituted. The action is $`S=\int_{M^5}i^*\mathfrak J`$. Source (8.12) gives

```math
\delta_\xi S=\int i^*(\mathcal L_\xi\mathfrak J)=\int i^*\big(i_\xi d\mathfrak J+d(i_\xi\mathfrak J)\big)=\int d\big(i^*i_\xi\mathfrak J\big).
\tag{FI26}
```

For the Abelian transformation $`\delta V=d\alpha`$,

```math
\delta_\alpha\mathfrak J=d\alpha\wedge\Phi_4=d(\alpha\Phi_4),
\tag{FI27}
```

and the linear potential gauge transformation leaves $`\Phi_4`$ unchanged. The covariant superforms are superconformal, as required by source (8.14)–(8.15); their induced action is invariant up to these boundary terms. This establishes the generic off-shell BF invariant without expanding its many composite terms. It assumes the defining vector constraints and the actual linear-multiplet constraint, not just a collection of fields named $`L,\varphi,N,E`$.

We also reproduce the nonform density rather than relying only on closedness. The nonzero source (8.22) entries are

```math
\Sigma_{abc\,\alpha^i\beta^j}=-4i\epsilon_{Gabcde}(\Sigma^{de})_{\alpha\beta}\rho G_G^{ij},\qquad \Sigma_{abcd\,\alpha}^{i}=2\epsilon_{Gabcde}(\Gamma^e)_\alpha{}^\beta(\rho\varphi_{G\beta}^i+i\lambda_{G\beta j}G_G^{ji}),\qquad \Sigma_{abcde}=-\epsilon_{Gabcde}(\rho F_G+X_G^{ij}G_{Gij}+2\lambda_G^{\alpha k}\varphi_{G\alpha k}).
\tag{FI28}
```

Let the final parenthesis be $`S_0`$, and let $`Z^i:=\rho\varphi_G^i+i\lambda_{Gj}G_G^{ji}`$. Using (FI11) for $`p=5`$, the top term contributes $`S_0`$. The one-gravitino coefficient is $`(5/2)2/5!=1/24`$, and $`\epsilon_G^{abcde}\epsilon_{Gbcdef}=-24\delta^a_f`$, so it contributes $`-\psi_{ai}\Gamma^a Z^i`$. For the two-gravitino term the coefficient is $`(-5/2)(-4i)/5!=i/12`$; contracting two epsilons yields $`-6(\delta^a_f\delta^b_g-\delta^a_g\delta^b_f)`$, hence $`-i\psi_{ai}^\alpha\psi_{bj}^\beta(\Sigma^{ab})_{\alpha\beta}\rho G_G^{ij}`$. The raised-spinor identity (FI05) converts that last contraction to **plus** $`i\psi_{ai}\Sigma^{ab}\psi_{bj}\rho G_G^{ij}`$. Therefore

```math
\frac1{5!}\epsilon_G^{abcde}(\Sigma_G\Vert)_{abcde}=S_0-\psi_{ai}\Gamma^a\varphi_G^i\rho-i\psi_{ai}\Gamma^a\lambda_{Gj}G_G^{ij}+i\psi_{ai}\Sigma^{ab}\psi_{bj}\rho G_G^{ij}.
\tag{FI29}
```

The $`V\wedge\Phi_4`$ term contains the **ordinary pullback** $`h_{mnpq}`$, not just its purely tangent superfield component. By (FI13) its scalar density is $`-v_{Ga}h_G^a`$. Subtracting (FI29), as required in (FI25), gives source **(8.28)**:

```math
e^{-1}\mathcal L_G=-v_{Ga}h_G^a-\rho F_G-X_G^{ij}G_{Gij}-2\lambda_G^{\alpha k}\varphi_{G\alpha k}+\psi_{ai}\Gamma^a\varphi_G^i\rho+i\psi_{ai}\Gamma^a\lambda_{Gj}G_G^{ij}-i\psi_{ai}\Sigma^{ab}\psi_{bj}\rho G_G^{ij}.
\tag{FI30}
```

Source **(8.29)** explicitly identifies the ordinary four-form in this term as $`h_{mnpq}=4\partial_{[m}b_{Gnpq]}`$; source **(8.30)** integrates it by parts. Therefore the use of a calligraphic covariant $`\mathcal H`$ in C24/S23 (3.2b), while retaining the other six coefficients, is a source symbol/interface error. It can be repaired either by writing $`h_G`$ there, or by explicitly adding its $`h_G-\mathcal H_G`$ completion. It is not an identically conserved improvement which may be omitted: $`\partial(eE)`$ is generally nonzero while $`\partial(eP)=0`$.

Each coefficient in (FI30) can now be checked without any expansion of the composite linear multiplet:

| Source contribution | Conversion factors, including the displayed action sign | Project contribution |
|---|---|---|
| $`-v_Gh_G`$ | $`-(-1)(1)`$ | $`A_aP^a`$ |
| $`-X_GG_G`$ | $`-(2)(-1/2)`$ | $`Y^{ij}L_{ij}`$ |
| $`-\rho F_G`$ | $`-(-1)`$ | $`\rho N`$ |
| $`-2\lambda_G\varphi_G`$ | $`-2(-1)(i/2)`$ | $`i\bar\lambda\varphi`$ |
| $`+\rho\psi_i\Gamma\varphi_G^i`$ | $`(i)(i/2)(-1)`$, last minus from SU(2) | $`\rho\bar\psi_a\gamma^a\varphi/2`$ |
| $`+i\psi_i\Gamma\lambda_{Gj}G_G^{ij}`$ | $`i(i)(-1)(-1/2)`$ | $`-\bar\psi_a^i\gamma^a\lambda^jL_{ij}/2`$ |
| $`-i\rho\psi_i\Sigma\psi_jG_G^{ij}`$ | $`-i(1/2)(-1/2)`$ | $`i\rho\bar\psi_a^i\gamma^{ab}\psi_b^jL_{ij}/4`$ |

The resulting exact generic density is

```math
\boxed{\ell_{VL}=Y^{ij}L_{ij}+i\bar\lambda\varphi-\frac12\bar\psi_a^i\gamma^a\lambda^jL_{ij}+A_aP^a+\rho\left(N+\frac12\bar\psi_a\gamma^a\varphi+\frac i4\bar\psi_a^i\gamma^{ab}\psi_b^jL_{ij}\right),\qquad P^a=E^a+\frac i2\bar\psi_b\gamma^{ba}\varphi+\frac14\bar\psi_b^i\gamma^{abc}\psi_c^jL_{ij}.}
\tag{FI31}
```

The ordinary form representative is $`A\cdot P\simeq_\partial-\epsilon_B^{abcde}F_{Bab}E_{cde}/24`$, using $`F_B=dA`$ and the divergence current $`J^b=-\epsilon_B^{abcde}A_aE_{cde}/12`$. In curved coordinates $`e\epsilon^{mnpqr}`$ is the constant coordinate symbol. This is the only integration by parts used for the density comparison. The local component equalities (FI15) and (FI24) do not use integration by parts.

## 6. Gauged realization and the retained compact LOG action

Replace the generic four slots in (FI31) by the derived LOG multiplet, and implement the already locked gauged dilaton-Weyl realization on all slots and their full covariant descendants. This means substituting the complete gauged composites for $`Y,T,\chi,D`$, using the conventional dependent connections, then evaluating the compensator gauges **after** each derivative. The current and superform identities are covariant identities and survive this transport. This report does not reopen the detailed component-composite derivation or simplify $`\mathcal D`$ to a bosonic derivative.

The relevant outer-vector gauges are $`\rho=\sigma=1`$, $`\lambda=\psi^i=0`$, $`A=C`$, and $`Y^{ij}=-gL_c^{ij}/2`$. The vanishing gaugino value does not set its covariant descendants inside LOG to zero. Write $`(0),(1),(2)`$ for total fermion degree, with implicit dependence of supercovariants counted when needed. Then the retained current and action are

```math
\boxed{P_{\log}^{a(\le2)}=E_{\log}^{a(0)}+E_{\log}^{a(2)}+\frac i2\bar\psi_b\gamma^{ba}\varphi_{\log}^{(1)}+\frac14\bar\psi_b^i\gamma^{abc}\psi_c^jL_{\log ij}^{(0)},}
\tag{FI32}
```

```math
\boxed{\ell_{\log}^{\rm gauged}=N_{\log}^{(0)}+N_{\log}^{(2)}-\frac g2L_c^{ij}\big(L_{\log ij}^{(0)}+L_{\log ij}^{(2)}\big)+C_a\big(E_{\log}^{a(0)}+E_{\log}^{a(2)}\big)+\frac12\bar\psi_a\gamma^a\varphi_{\log}^{(1)}+\frac i2 C_a\bar\psi_b\gamma^{ba}\varphi_{\log}^{(1)}+\frac i4\bar\psi_a^i\gamma^{ab}\psi_b^jL_{\log ij}^{(0)}+\frac14 C_a\bar\psi_b^i\gamma^{abc}\psi_c^jL_{\log ij}^{(0)}+\text{high fermi terms}.}
\tag{FI33}
```

The five-form proof is an exact statement for an exact linear multiplet. Its retained-order consequence cancels the variation through one physical fermion (one supersymmetry parameter is not counted as a physical fermion), while the omitted four-fermion action begins contributing to variations with three physical fermions. The higher terms are inherited from the exact construction; it does not assert that an arbitrarily truncated action is exactly invariant at every higher fermion order. No second set of projection factors multiplies the LOG slots in (FI33). The active Step 7 (SC7-51)–(SC7-52) has precisely these current and density coefficients and needs **no formula correction from FORM-01**.

In the bosonic limit $`Q_1=Q_2=0`$, the density reduces to $`N_{\log}^{(0)}-gL_c^{ij}L_{\log ij}^{(0)}/2+C_aE_{\log}^{a(0)}`$. Thus this interface correction neither changes the earlier bosonic action nor constrains a vacuum. In the ungauged limit the explicit $`gL_cL_{\log}`$ term disappears and the same form construction remains valid.

## 7. Exact checks, limits and repair ledger

Retained source implementations: [verify_log_form_interface.py](../results/gauged_full_fermionic_log/scripts/verify_log_form_interface.py). Their source-relative dependencies and execution limits are described in the [component evidence guide](../../README.md).

The [coefficient verifier](../results/gauged_full_fermionic_log/scripts/verify_log_form_interface.py) constructs an explicit exact Gaussian-rational Clifford representation independently of the production routines. It verifies all ten independent two-form generators with the correctly lowered second spinor index; all 48 choices of fermionic legs for the four-/five-form pullbacks; all five current components as Grassmann polynomials; all ten independent potential components for all three symmetric triplet basis tensors; all seven BF coefficients; and Weyl weights. It deliberately checks that the old $`+MC`$ kernel is the opposite of the required kernel. The [checks JSON](../results/gauged_full_fermionic_log/sources/certification_20260925/form/checks.json) contains hashes and scope. All listed checks pass. This is exact coefficient arithmetic, not numerical sampling.

The conformal weights are $`w(L,\varphi,N,E)=(3,7/2,4,4)`$, $`w(\rho,\lambda,Y,A_a)=(1,3/2,2,1)`$, $`w(\psi_a)=1/2`$ and $`w(\epsilon)=-1/2`$. The current completions both have weight four and every density term has weight five. The potential has world-index weight zero; inserting the three inverse-weight vielbeins or two in $`\gamma_{mn}`$ verifies every term in (FI24). These are **pre-gauge Weyl weights**, not gauge-fixed engineering dimensions.

No field equation, special curvature, constant compensator derivative or vanishing gravitino was imposed. The local potential comparison assumes a contractible patch; global flux/cohomology sectors and boundary counterterms are not fixed by it. Reality of the full substituted LOG polynomials is a separate check; this report establishes the exact spinor phases and order for their interface, not reality by assertion.

