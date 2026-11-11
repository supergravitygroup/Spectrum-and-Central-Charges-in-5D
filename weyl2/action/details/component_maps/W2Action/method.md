# Construction method for the Log-invariant action

The LOG-invariant construction below follows the two cited papers. The method builds a composite linear multiplet from the logarithm of a compensating vector superfield, calculates its upper components, and inserts them into the known BF action principle. Construction in the Standard Weyl formulation and conversion to gauged Dilaton–Weyl variables are separate stages.

This note presents the cited source formulas and the algebraic deductions explaining their construction method.

[CONVENTIONS.md](../Weyl2Action/CONVENTIONS.md) remains the project's working convention file. It organizes the Özkan–Pang (5.8) calculation and several corrected working definitions. The formulas below are explained in each paper's own notation and are not treated as converted to project conventions. In particular, the gauged Dilaton–Weyl map is not identified with the existing ungauged map. The described gauge conditions and bosonic expressions are stages of the authors' published calculation; no new gauge or truncation is imposed on the project theory.

<a id="1-roles-of-the-two-sources-and-equation-locations"></a>

## Roles of the two sources and equation locations

**[S]** [Published component construction](../../../../../references/bibliography.md): G. Gold, J. Hutomo, S. Khandelwal, and G. Tartaglino-Mazzucchelli, *Components of curvature-squared invariants of minimal supergravity in five dimensions*, JHEP 07 (2024) 221. The source file is the 67-page published version.

**[T]** [Curvature-squared supergravity and holography](../../../../../references/bibliography.md): G. Gold, P.-J. Hu, J. Hutomo, S. Khandelwal, M. Ozkan, Y. Pang, and G. Tartaglino-Mazzucchelli, *On five-dimensional curvature squared supergravity and holography*, 2024 MATRIX Annals, Part I, printed pp. 457–481. The source file is the 25-page book-chapter version.

| Role in the calculation | Source location | Printed page / PDF page |
|---|---|---|
| Weyl multiplet and derivative rules | [S] §2.1, especially (2.6)–(2.9), (2.15)–(2.26) | 5-11 / 6-12 |
| Vector multiplet and spinor derivatives | [S] (2.27)-(2.38) | 11-13 / 12-14 |
| Linear multiplet and component projections | [S] (2.39)-(2.52) | 14-16 / 15-17 |
| General BF action principle | [S] (3.2); [T] (3) | 17 / 18; 461 / 5 |
| Log definition and full lowest component | [S] (4.7), (4.8a) | 24-25 / 25-26 |
| Bosonic expressions for the upper Log components | [S] (4.8b)-(4.8d) | 25-27 / 26-28 |
| Expanding connections and reorganizing the vector component | [S] (4.9)-(4.14) | 27-28 / 28-29 |
| Standard Weyl construction of the Log action | [S] (5.9)-(5.20) | 31-34 / 32-35 |
| Full superconformal derivative algebra | [S] Appendix A | 56-58 / 57-59 |
| Dictionary of fields, connections, and transformation parameters | [S] Appendix B, Tables 4–7 | 58-59 / 59-60 |
| Gauged Dilaton–Weyl map | [T] (1)-(4) | 460-462 / 4-6 |
| Gauge conditions and target Log density | [T] (7), (9)-(11) | 462-465 / 6-9 |

Equation numbers refer to these published versions. The [arXiv record](https://arxiv.org/abs/2311.00679) of [S] lists a preprint with 99 main-text pages and a 228-page supplementary file; its page and equation numbers must not be assumed to match the published file. The [arXiv record](https://arxiv.org/abs/2504.10856) of [T] links it to the book chapter above.

[S] cites its reference [30] for the geometric Log definition and [31] for the earlier lowest-component calculation. The physical formulas below come directly from [S] and [T]. Their bibliographies are not used to assume new transformation rules.

<a id="2-how-is-the-log-multiplet-selected"></a>

## How is the Log multiplet selected?

In [S] (2.27), $`W`$ is the real primary Abelian vector-multiplet field-strength superfield of weight one. Let $`\mathbb D`$ denote the dilatation generator and $`S_\alpha^i`$, $`K_a`$ the special superconformal generators. The source conditions are

```math
\mathbb DW=W,\qquad S_\alpha^iW=K_aW=0,
```

```math
\nabla_\alpha^{(i}\nabla_\beta^{j)}W
=\frac14\varepsilon_{\alpha\beta}
\nabla^{\gamma(i}\nabla_\gamma^{j)}W
```

On a local patch where $`W`$ is nonzero and its logarithm is defined,

```math
\begin{aligned}
\mathbb D\log W&=W^{-1}\mathbb DW=1,\\
S_\alpha^i\log W&=W^{-1}S_\alpha^iW=0,\\
K_a\log W&=W^{-1}K_aW=0.
\end{aligned}
```

Thus $`\log W`$ cannot be treated as a homogeneous weight-zero superfield: its dilatation transformation is inhomogeneous.

[S] (2.45) supplies an operator producing a linear multiplet from a weight-zero primary prepotential $`\Omega`$:

```math
G^{ij}=-\frac{3i}{40}\Delta^{ijkl}\nabla_{kl}\Omega,
\qquad
\Delta^{ijkl}:=-\frac1{32}\nabla^{(ij}\nabla^{kl)},
\qquad
\nabla^{ij}:=\nabla^{\alpha(i}\nabla_\alpha^{j)}.
```

The Log construction is a special application of the same operator to $`\log W`$. [S] (4.7) and [T] (9):

```math
\boxed{
\begin{aligned}
H_{\mathrm{Log}}^{ij}
&=-\frac{3i}{40}\Delta^{ijkl}\nabla_{kl}\log W\\
&=-\frac{3i}{40}\left(-\frac1{32}\right)
\nabla^{(ij}\nabla^{kl)}\nabla_{kl}\log W\\
&=\frac{3i}{1280}
\nabla^{(ij}\nabla^{kl)}\nabla_{kl}\log W.
\end{aligned}}
```

This contains six ordered spinor derivatives. Parentheses symmetrize the four $`SU(2)`$ indices; they do not permit exchanging derivatives without commutators.

The structural result used by the paper is that this special composite satisfies

```math
\nabla_\alpha^{(i}H_{\mathrm{Log}}^{jk)}=0,
\qquad S_\alpha^kH_{\mathrm{Log}}^{ij}=K_aH_{\mathrm{Log}}^{ij}=0,
\qquad \mathbb D H_{\mathrm{Log}}^{ij}=3H_{\mathrm{Log}}^{ij}
```

these conditions. To explain its weight, temporarily write $`\mathcal O^{ij}:=\nabla^{(ij}\nabla^{kl)}\nabla_{kl}`$; [S] (A.1e) gives

```math
\begin{aligned}
[\mathbb D,\mathcal O^{ij}]&=6\left(\frac12\right)\mathcal O^{ij}=3\mathcal O^{ij},\\
\mathbb D\big(\mathcal O^{ij}\log W\big)
&=[\mathbb D,\mathcal O^{ij}]\log W
 +\mathcal O^{ij}\mathbb D\log W\\
&=3\mathcal O^{ij}\log W+\mathcal O^{ij}1
=3\mathcal O^{ij}\log W,\\
\mathbb D H_{\mathrm{Log}}^{ij}&=3H_{\mathrm{Log}}^{ij}.
\end{aligned}
```

This weight calculation alone proves neither $`S`$-primarity nor linearity. Reproving these requires commuting generators through the operator using the full algebra in [S] Appendix A. Equation (4.7) of [S] takes the construction with these properties as input; the main text does not display all intermediate algebra of the six derivatives.

On printed p. 24, footnote 9 of [S] states that its Log definition differs from the earlier geometric source by an **overall minus sign**. Recalculation must fix the $`+3i/1280`$ normalization above.

<a id="3-which-inputs-determine-the-six-derivatives"></a>

## Which inputs determine the six derivatives?

The method does not infer a bosonic ansatz from the $`R_{ab}R^{ab}`$ term. It starts from the full superfield definition, with the following independent derivative data:

| Input | Use | Source |
|---|---|---|
| Vector superfields $`W,\lambda_\alpha^i,X^{ij},F_{\alpha\beta}`$ | Expand successive derivatives of $`\log W`$ | [S] (2.28)-(2.31) |
| Super-Weyl tensor $`W_{\alpha\beta}`$ and its descendants | Expand derivatives of Weyl fields generated by vector-multiplet derivatives | [S] (2.5)-(2.9) |
| Full $`\{\nabla_\alpha^i,\nabla_\beta^j\}`$, $`[\nabla_a,\nabla_\alpha^i]`$, $`[\nabla_a,\nabla_b]`$ | Retain torsion and curvatures when reordering derivatives | [S] (2.2), Appendix A |
| Actions of $`S,K,\mathbb D`$, Lorentz, and $`SU(2)`$ generators | Apply commutator generators to fields | [S] (2.8), (2.31), (A.1) |
| Clifford and spinor-index rules | Express equivalent tensor structures in a common basis | Conventions of [S]; an additional dictionary is required for project conversion |

The scalar $`W`$ and the two-spinor-index $`W_{\alpha\beta}`$ are distinct superfields. $`W_{ab}`$ is the two-form representation of the latter, not the vector field strength $`F_{ab}`$. $`D`$ is the auxiliary scalar of the Weyl multiplet, whereas $`\mathbb D`$ is a generator. Equation (2.15) of [S] contains $`\chi_\alpha^i=\frac{3i}{32}X_\alpha^i|`$ and $`D=-\frac3{128}Y|`$; their $`X_\alpha^i,Y`$ are Weyl descendants, distinct from the vector auxiliary field $`X^{ij}`$.

### Explicit example of the first two derivatives

[S] (2.28a) defines $`\lambda_\alpha^i:=-i\nabla_\alpha^iW`$. Thus

```math
\begin{aligned}
\nabla_\alpha^i\log W
&=W^{-1}\nabla_\alpha^iW=iW^{-1}\lambda_\alpha^i,\\
\nabla_\beta^j\nabla_\alpha^i\log W
&=i(\nabla_\beta^jW^{-1})\lambda_\alpha^i
+iW^{-1}\nabla_\beta^j\lambda_\alpha^i\\
&=i(-iW^{-2}\lambda_\beta^j)\lambda_\alpha^i
+iW^{-1}\nabla_\beta^j\lambda_\alpha^i\\
&=W^{-2}\lambda_\beta^j\lambda_\alpha^i
+iW^{-1}\nabla_\beta^j\lambda_\alpha^i.
\end{aligned}
```

Substitute [S] (2.29a) into the second term with the same index order:

```math
\nabla_\beta^j\lambda_\alpha^i
=-2\varepsilon^{ji}(F_{\beta\alpha}+W_{\beta\alpha}W)
-\varepsilon_{\beta\alpha}X^{ji}
-\varepsilon^{ji}\nabla_{\beta\alpha}W,
```

```math
\begin{aligned}
\nabla_\beta^j\nabla_\alpha^i\log W
={}&W^{-2}\lambda_\beta^j\lambda_\alpha^i
-2iW^{-1}\varepsilon^{ji}F_{\beta\alpha}
-2i\varepsilon^{ji}W_{\beta\alpha}\\
&-iW^{-1}\varepsilon_{\beta\alpha}X^{ji}
-iW^{-1}\varepsilon^{ji}\nabla_{\beta\alpha}W.
\end{aligned}
```

Here $`\nabla_{\alpha\beta}:=(\Gamma^a)_{\alpha\beta}\nabla_a`$ is the source spinor–vector notation. Subsequent derivatives act on $`W^{-n}`$, $`\lambda`$, $`F`$, $`X`$, $`W_{\alpha\beta}`$, and each differentiated field. Rules (2.29b)–(2.29c) and (2.6) of [S] continue the chain.

For one Grassmann-odd derivative $`\nabla_A`$ and a field of Grassmann parity $`|U|`$,

```math
\nabla_A(UV)=(\nabla_AU)V+(-1)^{|U|}U\nabla_AV.
```

When encountering a differentiated field, use

```math
\nabla_A\nabla_aU
=\nabla_a\nabla_AU+[\nabla_A,\nabla_a]U
```

Exchanging two odd derivatives gives

```math
\nabla_A\nabla_BU
=-\nabla_B\nabla_AU+\{\nabla_A,\nabla_B\}U.
```

The final terms cannot be replaced by flat-superspace algebra; the source's Weyl-field-dependent torsion and curvatures are required. Written fermion order is retained.

Section 4.2 of [S] states that Cadabra assisted this long expansion. The software repeatedly applies the supplied derivative rules; it does not choose the supersymmetry rules or action. Retaining each derivative stage separately permits comparison of the sixth-derivative result with [S] (4.8a).

[S] (4.8a) gives the full lowest component, including four- and six-fermion terms. [T] (10) presents the same structure with higher fermion degrees omitted. They must not be compared as two complete formulas of identical scope.

<a id="4-upper-components-six-seven-and-eight-derivatives-in-total"></a>

## Upper components: six, seven, and eight derivatives in total

The vertical bar $`|`$ denotes the $`\theta=0`$ projection; it does not set fermion fields to zero. Applying [S] (2.41) to the Log composite gives:

```math
\begin{aligned}
\text{lowest component:}\quad&H_{\mathrm{Log}}^{ij}|,\\
\varphi_{\alpha,\mathrm{Log}}^i
&=\frac13\nabla_{\alpha j}H_{\mathrm{Log}}^{ij}|,\\
F_{\mathrm{Log}}
&=\frac{i}{12}\nabla_i^\alpha\nabla_{\alpha j}H_{\mathrm{Log}}^{ij}|,\\
\mathcal H^a_{\mathrm{Log}}
&=\frac{i}{12}(\Gamma^a)^{\alpha\beta}
\nabla_{\alpha i}\nabla_{\beta j}H_{\mathrm{Log}}^{ij}|.
\end{aligned}
```

These require six, seven, eight, and eight spinor derivatives, respectively. As in [S], component formulas use the same symbol $`H_{\mathrm{Log}}^{ij}`$ for $`H_{\mathrm{Log}}^{ij}|`$. $`F_{\mathrm{Log}}`$ is a scalar, not the two-form $`F_{ab}`$. $`\mathcal H^a_{\mathrm{Log}}`$ is not the Dilaton–Weyl three-form $`H_{abc}`$.

The same calculation can also be organized using the definition

```math
Q_\alpha^i(U|):=(\nabla_\alpha^iU)|
```

in [S] (2.16), by successively applying the full component $`Q`$ transformations. This route must retain connection transformations and the source definition of $`Q`$; transformations of elementary fields alone are insufficient.

**Discarding all fermions of a lower component before deriving the bosonic upper component is incorrect.** For odd fields $`U,V`$ and odd derivatives $`\nabla_A,\nabla_B`$,

```math
\begin{aligned}
\nabla_A(UV)&=(\nabla_AU)V-U\nabla_AV,\\
\nabla_B\nabla_A(UV)
&=(\nabla_B\nabla_AU)V+(\nabla_AU)(\nabla_BV)\\
&\quad-(\nabla_BU)(\nabla_AV)+U\nabla_B\nabla_AV.
\end{aligned}
```

In the middle two products, each odd field receives one derivative, so fermion-free contributions can occur. The two-fermion terms in [T] (10) are therefore required for bosonic upper components. Terms with four or more fermions cannot become fermion-free with the two spinor derivatives remaining at this stage, explaining their omission in [T]. Recalculating the full action requires retaining them too.

[S] (4.8b) gives bosonic $`F_{\mathrm{Log}}`$, while (4.8c)–(4.8d) give bosonic $`\mathcal H^a_{\mathrm{Log}}`$. Printed p. 25 refers to the **supplementary file** for upper components with full fermionic content. The cited 67-page main text does not contain that supplement or an embedded attachment. Those long expressions are therefore not treated as inspected or verified here. They can be reproduced from the full definition, but comparison with the full published result also requires the supplement.

<a id="5-bf-action-and-reorganization-of-the-upper-vector-component"></a>

## BF action and reorganization of the upper vector component

[S] (5.9a) gives the superspace action of the construction:

```math
S_{\mathrm{Log}}=\int d^{5|8}z\,E\,V_{ij}H_{\mathrm{Log}}^{ij}.
```

Here $`E`$ is the supervielbein Berezinian and $`V_{ij}`$ the Mezincescu prepotential of the vector multiplet; the component $`SU(2)`$ connection is not $`V_\mu^{ij}`$. Inserting the primary linear composite into the BF action principle provides the superconformal action construction.

Its full component form in [S] (5.9b) is

```math
\begin{aligned}
S_{\mathrm{Log}}=-\int d^5x\,e\Big[&
v_a\mathcal H^a_{\mathrm{Log}}+WF_{\mathrm{Log}}
+X_{ij}H^{ij}_{\mathrm{Log}}+2\lambda^k\varphi_{k,\mathrm{Log}}\\
&-\psi_{ai}\Gamma^a\varphi^i_{\mathrm{Log}}W
-i\psi_{ai}\Gamma^a\lambda_jH^{ij}_{\mathrm{Log}}
+i\psi_{ai}\Sigma^{ab}\psi_{bj}WH^{ij}_{\mathrm{Log}}\Big]
\end{aligned}
```

Here $`e=\det e_\mu{}^a`$, $`v_a,W,\lambda^i,X^{ij}`$ are vector-multiplet fields, $`\psi_{ai}`$ is the gravitino, and $`\Gamma^a,\Sigma^{ab}`$ are the source Clifford matrices. Spinor contractions retain source order.

[S] uses $`S=\int d^5x\,e\,\mathcal L`$ for the scalar Lagrangian. [T] writes the density as $`\mathcal L`$ and its scalar as $`e^{-1}\mathcal L`$. Matching letters across these notations does not justify inserting or removing a determinant factor.

In the source's bosonic presentation, [S] (5.10):

```math
\mathcal L_{\mathrm{Log}}
=-v_a\mathcal H^a_{\mathrm{Log}}-WF_{\mathrm{Log}}-X_{ij}H^{ij}_{\mathrm{Log}}.
```

Thus calculating only the upper scalar component does not calculate the action; all three contributions are needed.

### From the raw vector component to integration by parts

On printed p. 26, [S] states that the initial bosonic expression for $`\mathcal H^a_{\mathrm{Log}}`$ has **261 terms**. Simplification uses vector-derivative commutators, Weyl-tensor symmetries, and Bianchi identities. The source's resulting bosonic expression (4.8c) is

```math
\mathcal H^a_{\mathrm{Log}}
=\frac1{12}\varepsilon^{abcde}\Phi_{bc}^{ij}\Phi_{deij}
-\frac38(\nabla_bC^{abcd})W_{cd}
-\frac38W^{-1}(\nabla_bC^{abcd})F_{cd}
+\nabla_b\widetilde H^{ab}_{\mathrm{Log}}
```

Here $`\Phi_{ab}^{ij}`$ is the source $`SU(2)`$ curvature, $`C_{abcd}`$ the Weyl tensor, and $`\widetilde H^{ab}_{\mathrm{Log}}=-\widetilde H^{ba}_{\mathrm{Log}}`$ the composite in (4.8d). This final formula presents only the source bosonic component in this paragraph.

The source emphasizes that $`\widetilde H^{ab}_{\mathrm{Log}}`$ is not $`K`$-invariant. Antisymmetry alone does not make the full conformal double divergence vanish. The bosonic identity in [S] (4.12) is

```math
\begin{aligned}
\nabla_a\nabla_b\widetilde H^{ab}_{\mathrm{Log}}
&=-\frac12R(K)_{ab}{}^cK_c\widetilde H^{ab}_{\mathrm{Log}}\\
&=\frac38\nabla^bC_{abcd}
\big(\nabla^aW^{cd}+W^{-1}\nabla^aF^{cd}
-W^{-2}F^{cd}\nabla^aW\big)
\end{aligned}
```

Here $`R(K)`$ is the special conformal curvature. Together with other terms, this contribution enters the $`\nabla_a\mathcal H^a_{\mathrm{Log}}=0`$ check and cannot be discarded by itself.

Expanding outer derivatives and using Riemann Bianchi identities, [S] (4.10) rewrites this as

```math
\mathcal H^a_{\mathrm{Log}}
=\frac1{12}\varepsilon^{abcde}\Phi_{bc}^{ij}\Phi_{deij}
+\mathcal D_b\big(\widetilde H^{ab}_{\mathrm{Log}}
+\widehat H^{ab}_{\mathrm{Log}}\big)
```

Here $`\mathcal D_a`$ is the source derivative with Lorentz, dilatation, and $`SU(2)`$ connections, distinct from the full $`\nabla_a`$. The additional antisymmetric composite is

```math
\widehat H^{ab}_{\mathrm{Log}}
=\frac5{16}RW^{ab}+R^{c[a}W^{b]}{}_c
+\frac5{16}RW^{-1}F^{ab}+W^{-1}R^{c[a}F^{b]}{}_c
```

It carries curvature contributions generated by expanding connections. $`\widetilde H^{ab}_{\mathrm{Log}}`$ in (4.10b) may still contain unexpanded derivatives; an outer $`\mathcal D_b`$ derivative alone does not mean that the full expansion is complete.

The integration-by-parts sign can be tracked explicitly in the source's bosonic $`b_\mu=0`$ notation. Temporarily writing $`B^{ab}:=\widetilde H^{ab}_{\mathrm{Log}}+\widehat H^{ab}_{\mathrm{Log}}=-B^{ba}`$ and $`F_{ab}=2\mathcal D_{[a}v_{b]}`$ gives

```math
\begin{aligned}
-e\,v_a\mathcal D_bB^{ab}
&=e(\mathcal D_bv_a)B^{ab}
-\partial_\mu\big(e\,e_b{}^\mu v_aB^{ab}\big)\\
&=\frac e2(\mathcal D_bv_a-\mathcal D_av_b)B^{ab}
-\partial_\mu\big(e\,e_b{}^\mu v_aB^{ab}\big)\\
&=-\frac e2F_{ab}
\big(\widetilde H^{ab}_{\mathrm{Log}}+\widehat H^{ab}_{\mathrm{Log}}\big)
-\partial_\mu\!\left[e\,e_b{}^\mu v_a
\big(\widetilde H^{ab}_{\mathrm{Log}}+\widehat H^{ab}_{\mathrm{Log}}\big)\right].
\end{aligned}
```

Up to this boundary density, [S] (5.11) writes

```math
\mathcal L_{\mathrm{Log}}
=-\frac1{12}v_a\varepsilon^{abcde}\Phi_{bc}^{ij}\Phi_{deij}
-\frac12F_{ab}\big(\widetilde H^{ab}_{\mathrm{Log}}+\widehat H^{ab}_{\mathrm{Log}}\big)
-WF_{\mathrm{Log}}-X_{ij}H^{ij}_{\mathrm{Log}}
```

The vector component therefore produces both the Chern–Simons term and other bosonic interactions. The boundary density is recorded explicitly here; no boundary condition making it vanish is assumed.

<a id="6-why-does-ricci-squared-arise-from-higher-derivatives"></a>

## Why does Ricci squared arise from higher derivatives?

[S] (2.16) defines the full component vector derivative as

```math
\nabla_a=e_a{}^m\left(
\mathcal D_m-\frac12\psi_m{}^\alpha_i\nabla_\alpha^i|
-\frac12\phi_m{}^{\alpha i}S_{\alpha i}-f_m{}^bK_b
\right)
```

Here $`\phi_m`$ is the dependent $`S`$ connection and $`f_m{}^b`$ the dependent $`K`$ connection. The paper calls explicit evaluation of their action on fields and derivatives **degauging**. This does not eliminate auxiliary fields through EOM.

Despite $`K_aW=0`$, the first derivative is not $`K`$-primary. Applying [S] (A.1i) to the scalar $`W`$ gives

```math
\begin{aligned}
K_c(\nabla_bW)
&=[K_c,\nabla_b]W+\nabla_b(K_cW)\\
&=(2\eta_{cb}\mathbb D+2M_{cb})W
=2\eta_{cb}W.
\end{aligned}
```

The $`-f_a{}^cK_c`$-connection contribution to the second derivative is therefore

```math
-f_a{}^cK_c(\nabla_bW)=-2f_{ab}W
```

The bosonic equality [S] (4.9a) is exactly

```math
\nabla_a\nabla_bW=\mathcal D_a\mathcal D_bW-2f_{ab}W
```

The full expression also has fermionic contributions.

Similarly, at bosonic order, [S] (4.9e) gives for $`\Box:=\nabla^a\nabla_a`$,

```math
\begin{aligned}
\Box\Box W={}&
\mathcal D_a\mathcal D^a\mathcal D_b\mathcal D^bW
-2\mathcal D_a\mathcal D^a(f_b{}^bW)
+4f_{ab}\mathcal D^a\mathcal D^bW\\
&+2(\mathcal D^af_{ab})\mathcal D^bW
-6f_a{}^a\mathcal D_b\mathcal D^bW
-4f_{ab}f^{ab}W+12f_a{}^af_b{}^bW
\end{aligned}
```

The bosonic part of the dependent connection in [S] (2.23c) is

```math
f_{ab}=-\frac16R_{ab}+\frac1{48}\eta_{ab}R
```

so $`f_{ab}f^{ab}`$ and $`(f_a{}^a)^2`$ generate Ricci-squared terms.

### Explicit origin of the curvature coefficient in the source result

The short calculation below shows how pure-curvature monomials arise in the bosonic $`W|=1`$, $`b_\mu=0`$ presentation of [S]. Other fields are not set to zero; only the derivative chain contributing to these monomials is tracked.

The relevant terms in [S] (5.12b) are

```math
\mathcal L_{\mathrm{Log}}^{\mathrm{cov}}
\supset\Box\Box W
-W^{-1}(\Box W)^2
-\frac12W^{-1}(\nabla_a\nabla_bW)(\nabla^a\nabla^bW)
```

In this source gauge, when $`\mathcal D_aW=0`$,

```math
\nabla_a\nabla_bW=-2f_{ab},\qquad
\Box W=-2f_a{}^a,
```

```math
\Box\Box W=-2\mathcal D_a\mathcal D^a(f_b{}^b)
-4f_{ab}f^{ab}+12(f_a{}^a)^2.
```

Substitution shows why retaining $`\Box\Box W`$ alone is insufficient:

```math
\begin{aligned}
&\Box\Box W-W^{-1}(\Box W)^2
-\frac12W^{-1}(\nabla_a\nabla_bW)(\nabla^a\nabla^bW)\\
&\quad=-2\mathcal D_a\mathcal D^a(f_b{}^b)
-4f_{ab}f^{ab}+12(f_a{}^a)^2
-4(f_a{}^a)^2-2f_{ab}f^{ab}\\
&\quad=-2\mathcal D_a\mathcal D^a(f_b{}^b)
-6f_{ab}f^{ab}+8(f_a{}^a)^2.
\end{aligned}
```

Using $`\eta_{ab}\eta^{ab}=5`$ in five dimensions,

```math
\begin{aligned}
f_a{}^a
&=\left(-\frac16+\frac5{48}\right)R=-\frac1{16}R,\\
f_{ab}f^{ab}
&=\frac1{36}R_{ab}R^{ab}
-\frac1{144}R^2+\frac5{2304}R^2\\
&=\frac1{36}R_{ab}R^{ab}-\frac{11}{2304}R^2,\\
-6f_{ab}f^{ab}+8(f_a{}^a)^2
&=-\frac16R_{ab}R^{ab}
+\left(\frac{66}{2304}+\frac8{256}\right)R^2\\
&=-\frac16R_{ab}R^{ab}+\frac{23}{384}R^2.
\end{aligned}
```

Returning to the original derivative expression in the same source gauge and bosonic presentation,

```math
\boxed{
\begin{aligned}
&\Box\Box W-W^{-1}(\Box W)^2
-\frac12W^{-1}(\nabla_a\nabla_bW)(\nabla^a\nabla^bW)\\
&\qquad=\frac18\mathcal D_a\mathcal D^aR
-\frac16R_{ab}R^{ab}+\frac{23}{384}R^2.
\end{aligned}}
```

For this $`\frac18\mathcal D^2R`$, the density is

```math
\frac e8\mathcal D_a\mathcal D^aR
=\frac18\partial_\mu\big(e\,g^{\mu\nu}\partial_\nu R\big)
```

This displays the $`-1/6`$ and $`23/384`$ coefficients in the source's integrated-by-parts expression (5.20). The limited calculation does not verify all of (5.20).

**Setting $`W|=1`$ is not setting the superfield to $`W\equiv1`$ at the outset.** The latter would incorrectly remove every derivative of $`\log W`$. In the former, $`\nabla_a\nabla_bW=-2f_{ab}`$ remains. This is the physical reason for expanding higher derivatives before gauge fixing.

### Conformal divergence versus an actual boundary term

In [S] (5.12)–(5.18), the action is arranged as $`\mathcal L_{\mathrm{Log}}^{\mathrm{cov}}+\mathcal L'_{\mathrm{Log}}`$. $`\mathcal L'_{\mathrm{Log}}`$ denotes explicit curvature terms from $`\widehat H^{ab}_{\mathrm{Log}}`$. The source represents them using a composite vector $`X^a`$, distinct from the auxiliary field $`X^{ij}`$, as

```math
\mathcal L'_{\mathrm{Log}}
=\nabla_aX^a-\mathcal D_aX^a
=-f_{ab}K^bX^a
```

This again uses the source's bosonic notation. Thus $`\nabla_aX^a`$ is generally not merely a boundary term.

The ten-coefficient ansatz in (5.15) belongs to this **rewriting step**. Curvature matching in (5.16) and the condition $`K^a\mathcal L_{\mathrm{Log}}=0`$ give five independent equations; $`X^a`$ is not unique. Equation (5.17) is the chosen representative. This freedom does not mean that the authors guessed the physical action coefficients at the outset.

The local equality is

```math
\mathcal L_{\mathrm{Log}}
=\mathcal L_{\mathrm{Log}}^{\mathrm{cov}}
+\nabla_aX^a-\mathcal D_aX^a
```

The final $`\mathcal D_aX^a`$ can be removed only while recording its boundary density in the action. Dropping a total derivative from a composite-multiplet component would be a different operation.

<a id="7-convention-conversion-from-s-to-t"></a>

## Convention conversion from [S] to [T]

The overall minus sign in the full BF formula of [S] and the notation

```math
e^{-1}\mathcal L_{\mathrm{BF}}
=A_aE^a+\rho N+Y_{ij}L^{ij}+\text{fermionic terms}
```

of [T] (3) must not be directly mixed. Overall normalizations of the composite multiplet and action must be tracked together with field conversions.

The Bergshoeff column in Appendix B of [S] shows that the conversion is more than renaming. The identifications below transcribe that source table; they are not a new dictionary verified against all corrected project rules:

| Notation of [S] | Bergshoeff notation in Appendix B |
|---|---|
| $`W`$ | $`\sigma`$ |
| $`\lambda^i`$ | $`-\psi^i`$ |
| $`X^{ij}`$ | $`2Y^{ij}`$ |
| $`v_m`$ | $`-A_\mu`$ |
| $`W_{ab}`$ | $`\frac{16}{3}T_{ab}`$ |
| $`\Gamma^a`$ | $`i\gamma^a`$ |
| $`\varepsilon^{abcde}`$ | $`-\varepsilon^{abcde}`$ |
| $`\omega_m{}^{ab}`$ | $`-\omega_\mu{}^{ab}`$ |
| General linear multiplet $`G^{ij}`$ | $`\frac12L^{ij}`$ |
| General linear multiplet $`F`$ | $`N`$ |
| General linear multiplet $`\mathcal H^a`$ | $`-E^a`$ |

Table 5 also gives field-dependent changes in the $`Q,S,K`$ parameters. Table 4 includes conversions of the dependent $`S,K`$ connections. Thus merely setting $`W_{ab}\to16T_{ab}/3`$ does not perform a full fermionic convention conversion. The $`L_{\mathrm{Log}}^{ij}\to H_{\mathrm{Log}}^{ij}`$ notation in [T] (9) must not replace this dictionary either.

In particular, distinguish the scalar compensator $`W`$, Weyl two-form $`W_{ab}`$, Log linear multiplet $`H_{\mathrm{Log}}^{ij}`$, and independent linear multiplet $`L^{ij}`$ in the Dilaton–Weyl formulation.

<a id="8-gauged-dilatonweyl-map-and-target-action"></a>

## Gauged Dilaton–Weyl map and target action

The procedure described in [T] §2.3.3 first inserts the Standard Weyl Log composite into the BF principle, then applies maps (1) and (4). In [T] notation, the bosonic vector identification is

```math
\rho\mapsto\sigma,\qquad A_\mu\mapsto C_\mu,
\qquad Y^{ij}\mapsto-\frac g2\sigma^{-1}L^{ij}
```

and the bosonic map for the Weyl auxiliary fields is

```math
T_{ab}\mapsto\frac18\sigma^{-1}G_{ab}
+\frac1{48}\sigma^{-2}\varepsilon_{abcde}H^{cde},
```

```math
\begin{aligned}
D\mapsto{}&\frac14\sigma^{-1}\nabla^a\nabla_a\sigma
+\frac18\sigma^{-2}(\nabla^a\sigma)\nabla_a\sigma
-\frac1{32}R-\frac1{16}\sigma^{-2}G_{ab}G^{ab}\\
&-\left(\frac{26}{3}T^{ab}-2\sigma^{-1}G^{ab}\right)T_{ab}
+\frac g4\sigma^{-2}N+\frac{g^2}{16}\sigma^{-4}L^{ij}L_{ij}
\end{aligned}
```

The $`T_{ab}`$ on the right is also expanded using its own map. Here $`\nabla_a`$ is the derivative in [T] (2) with Lorentz, dilatation, and $`SU(2)`$ connections; the shared symbol does not identify it with the full superconformal $`\nabla_a`$ of [S].

The source definition of the three-form is

```math
G_{\mu\nu}=2\partial_{[\mu}C_{\nu]},\qquad
H_{\mu\nu\rho}=3\partial_{[\mu}B_{\nu\rho]}
+\frac32C_{[\mu}G_{\nu\rho]}+\frac g2E_{\mu\nu\rho}
```

Gauging enters both this final term and the $`D,Y^{ij}`$ maps. All are carried through together. The $`L^{ij},N,E_{\mu\nu\rho}`$ here are not components of the Log composite.

The $`Y`$ identification in [T] (4) also contains $`\frac{i}{4}\sigma^{-1}\bar\psi^i\psi^j`$ and writes $`\lambda^i\mapsto\psi^i`$. Equation (1) of [T] explicitly suppresses other fermionic contributions. Thus the displayed bosonic map alone cannot convert the full fermionic action; the full map is an additional required input.

Section 2.2 of [T] explains the origin of this Weyl-multiplet representation through coupled vector- and linear-multiplet equations; §2.3.1 states that the resulting map constructs off-shell models. Writing the Log action in this representation is not equivalent to solving the new four-derivative action's auxiliary-field EOM and passing on shell.

In presenting their results, the authors use [T] (7),

```math
\sigma=1,\qquad b_\mu=0,\qquad\psi^i=0
```

Here $`\psi^i`$ is the compensator fermion/dilatino, not the gravitino $`\psi_\mu^i`$. Presenting the bosonic result also separates fermionic terms. Fields such as $`N,L^{ij},V_\mu^{ij}`$ remain in (11).

The final expression in [T] uses

```math
H^{ab}:=-\frac1{12}\varepsilon^{abcde}H_{cde},\qquad
H^2_{ab}:=H_a{}^cH_{bc},\qquad
G^2_{ab}:=G_a{}^cG_{bc}
```

This coefficient for $`H^{ab}`$ must be retained, rather than silently replaced by the standard $`1/3!`$ Hodge dual.

In their respective representations and normalizations, the pure-curvature coefficients in the two sources are

```math
\begin{aligned}
\text{[S] (5.20):}\quad
\mathcal L_{\mathrm{Log}}
&\supset-\frac16R_{ab}R^{ab}+\frac{23}{384}R^2,\\
\text{[T] (11):}\quad
 e^{-1}\mathcal L_{\mathrm{Log}}
&\supset-\frac16R_{ab}R^{ab}+\frac1{24}R^2
\end{aligned}
```

The difference between these two $`R^2`$ coefficients alone does not prove an error: [S] (5.20) also contains $`-\frac12RD-\frac83D^2`$, and the $`D`$ map of [T] contains curvature. Direct comparison requires the complete convention conversion and these substitutions. The comparison here concerns the displayed curvature coefficients and their stated convention dependence.

<a id="9-which-intermediate-results-should-track-a-recalculation"></a>

## Source formulas and their roles

| Order | Component expression or identity | Source |
|---|---|---|
| 1 | Field definitions, full derivative algebra, and Log normalization in one convention | [S] §2, Appendix A, (4.7) |
| 2 | Six ordered derivatives of $`\log W`$; full $`H_{\mathrm{Log}}^{ij}`$ with Grassmann order retained | [S] (4.8a) |
| 3 | Each of $`\varphi_{\mathrm{Log}},F_{\mathrm{Log}},\mathcal H^a_{\mathrm{Log}}`$ separately | [S] (2.41), (4.8); supplementary file for full fermionic content |
| 4 | Linearity, primarity, and vector divergence | [S] (2.39), (2.42), (4.12)-(4.14) |
| 5 | Separate contributions of each BF product and the combined density | [S] (5.9)-(5.12) |
| 6 | Connection contributions to every higher derivative; boundary densities from integration by parts | [S] (4.9), (5.13)-(5.20) |
| 7 | Full field, connection, and parameter conversion, including action normalization | [S] Appendix B, Tables 4–7 |
| 8 | Application of the gauged Dilaton–Weyl map to each term | [T] (1)-(4) |
| 9 | Difference expression in the same gauge and derivative basis as the published presentation | [T] (7), (11) |

The table locates the component expressions, identities and convention conversions in the cited sources. The off-shell presentation includes fermions, auxiliary fields and connections; the bosonic source-gauge expressions are their specified restrictions.

The defining linear-multiplet conditions are:

```math
\nabla_\alpha^{(i}H_{\mathrm{Log}}^{jk)}=0,
\qquad S_\alpha^kH_{\mathrm{Log}}^{ij}=K_aH_{\mathrm{Log}}^{ij}=0,
\qquad\nabla_a\mathcal H^a_{\mathrm{Log}}=0.
```

On printed p. 28, [S] reports checking the vector divergence at bosonic order and $`K`$-invariance of all descendants including fermions. These are the authors' reported checks, not independent verifications repeated here. Upper components are generally not annihilated by $`S`$; they have their own $`S`$ transformations in [S] (2.43). Lowest-component primarity must not be imposed unchanged on every descendant.

From Tables 1–2 of [S], the weights must be

```math
w(H_{\mathrm{Log}})=3,\quad
w(\varphi_{\mathrm{Log}})=\frac72,\quad
w(F_{\mathrm{Log}})=w(\mathcal H^a_{\mathrm{Log}})=4
```

Since BF contains $`w(v_a)=w(W)=1`$, $`w(X^{ij})=2`$, and $`w(e)=-5`$,

```math
\begin{aligned}
w(ev_a\mathcal H^a_{\mathrm{Log}})&=-5+1+4=0,\\
w(eWF_{\mathrm{Log}})&=-5+1+4=0,\\
w(eX_{ij}H^{ij}_{\mathrm{Log}})&=-5+2+3=0.
\end{aligned}
```

These checks detect incorrect weights or missing compensator powers; they do not prove individual coefficients.

The method must track Grassmann derivative signs, bosonic upper-component contributions from two-fermion lower components, $`K`$-connection terms, BF normalization, actual boundary densities, and the $`g`$ dependence of the gauged map. These distinctions locate discrepancies in the multiplet calculation, action substitution, or representation conversion. Subsequent on-shell eliminations and holographic calculations in the papers do not replace this off-shell construction.
