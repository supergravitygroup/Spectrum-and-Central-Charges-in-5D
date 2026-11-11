# Action family and theory classification

The action family consists of a common two-derivative density and three four-derivative building blocks. Retaining source normalizations, define

```math
S_{\le2}(\alpha,\beta,\zeta)
=\frac1{2\kappa_5^2}\int d^5x\,e\,
\bigl(\ell_{2,\le2}
 +\alpha\ell_{W,\le2}
 +\beta\ell_{\log,\le2}
 +\zeta\ell_{R,\le2}\bigr)
```

The symbols $`\ell_W`$, $`\ell_{\log}`$, and $`\ell_R`$ denote the Weyl-squared, LOG, and $`R^2`$ building blocks, respectively. The subscript $`\le2`$ retains physical fermion degrees zero and two, including all implicit fermions. No coupling expansion is made.

This section classifies the action records and their algebraic normalization relations. Established invariant constructions are adopted with citations; the paper concerns spectra of the selected theories. The component identities and their fermion degree are specified in the [identity record](../references/component_records/02_action_family.md).

The spectrum studies include the [four AdS5 studies](../README.md). The generic combination below is an action basis, not an additional spectrum study. The two-derivative theory is a reference limit.

The Gauss–Bonnet on AdS₅ study uses the normalization and component inputs as documented in [its action record](../gauss_bonnet/ads5/action_inputs.md). Its coupling label is not silently equated with the common-basis coupling below.

<a id="1-building-blocks-and-source-normalizations"></a>

## Building blocks and source normalizations

With $`\ell_A^{(0)}`$ the bosonic part and $`\ell_A^{(2)}`$ the physical two-fermion part,

```math
\ell_{A,\le2}=\ell_A^{(0)}+\ell_A^{(2)},
\qquad A\in\{2,W,\log,R\}.
```

The coefficients of pure-curvature monomials are

| Building block | Pure-curvature contribution | Complete recorded expressions |
|---|---|---|
| Two derivatives | $`LR`$ | [Two-derivative building block](two_derivative_action/invariant.md) |
| Weyl squared | $`\frac18R_{abcd}R^{abcd}-\frac16R_{ab}R^{ab}+\frac1{24}R^2`$ | [Weyl squared](../weyl2/action/invariant.md) |
| LOG | $`-\frac16R_{ab}R^{ab}+\frac1{24}R^2`$ | [LOG](../log/action/invariant.md) |
| $`R^2`$ | $`\frac14R^2`$ | [$`R^2`$](../r2/action/invariant.md) |

This table decomposes the recorded densities by the specified monomials; it is not an action obtained by setting other fields to zero. In particular, Weyl-squared names the relevant completion, not merely the $`C_{abcd}C^{abcd}`$ term. The algebraic derivation of the normalizations is given in the [corresponding appendix](details/action_normalizations.md).

<a id="2-theory-families"></a>

## Theory families

Each theory includes the common two-derivative building block:

| Family | Density at physical fermion degree $`\le2`$ | Coupling condition | Bosonic and fermionic content |
|---|---|---|---|
| Two-derivative reference | $`\ell_2`$ | $`\alpha=\beta=\zeta=0`$ | [Reference theory](two_derivative_action/README.md) |
| Two derivatives + $`R^2`$ | $`\ell_2+\zeta\ell_R`$ | $`\alpha=\beta=0`$ | [$`R^2`$ theory](../r2/action/README.md) |
| Two derivatives + Weyl-squared | $`\ell_2+\alpha\ell_W`$ | $`\beta=\zeta=0`$ | [Weyl-squared theory](../weyl2/action/README.md) |
| Two derivatives + LOG | $`\ell_2+\beta\ell_{\log}`$ | $`\alpha=\zeta=0`$ | [LOG theory](../log/action/README.md) |
| Generic combination | $`\ell_2+\alpha\ell_W+\beta\ell_{\log}+\zeta\ell_R`$ | Three free couplings | [Generic theory](generic_action.md) |
| Two derivatives + GB | $`\ell_2+\lambda\ell_G`$ | $`(\alpha,\beta,\zeta)=(\lambda,2\lambda,0)`$ | [GB theory](../gauss_bonnet/action/common_basis.md) |

The zero conditions in the table define the named theories. The remaining couplings are arbitrary. Pairwise combinations occur on the subfamilies $`\zeta=0`$, $`\beta=0`$, and $`\alpha=0`$, all contained in the generic expression.

<a id="3-gaussbonnet-combination"></a>

## Gauss–Bonnet combination

Define the Gauss–Bonnet curvature polynomial by

```math
\mathcal G:=R_{abcd}R^{abcd}-4R_{ab}R^{ab}+R^2
```

The pure curvature-squared part of the generic density is

```math
\frac\alpha8R_{abcd}R^{abcd}
-\frac{\alpha+\beta}{6}R_{ab}R^{ab}
+\left(\frac{\alpha+\beta}{24}+\frac\zeta4\right)R^2
```

so matching coefficients with $`\alpha\mathcal G/8`$ gives

```math
\begin{aligned}
-\frac{\alpha+\beta}{6}&=-\frac\alpha2
&&\Longrightarrow\quad\beta=2\alpha,\\
\frac{\alpha+\beta}{24}+\frac\zeta4&=\frac\alpha8
&&\Longrightarrow\quad\zeta=0
\end{aligned}
```

Since no division by $`\alpha`$ is made, $`\alpha=0`$, which includes the common two-derivative point, is retained.

In the source normalization,

```math
\ell_G:=\ell_W+2\ell_{\log},
\qquad
\ell_G\supset\frac18\mathcal G,
\qquad
S_{\mathrm{GB},\le2}
=\frac1{2\kappa_5^2}\int d^5x\,e\,
\bigl(\ell_{2,\le2}+\lambda\ell_{G,\le2}\bigr).
```

The quantity $`\lambda`$ is the free coupling of this subfamily. GB is a linear combination of the three building blocks, not a fourth independent four-derivative invariant. The same combination has been applied to every bosonic and fermionic term, rather than only to the pure-curvature table while leaving other field coefficients generic.

Coefficient matching alone gives no conclusion about all field equations, ghost content, or independent SUSY invariance.

<a id="4-field-content-and-representation"></a>

## Field content and representation

The independent fields in the sources' existing Poincaré representation are

```math
\begin{aligned}
\Phi_{\mathrm B}&=
\{e_\mu{}^a,C_\mu,B_{\mu\nu},E_{\mu\nu\rho},L,N,V_\mu,V_\mu^{\prime ij}\},\\
\Phi_{\mathrm F}&=\{\psi_\mu^i,\varphi^i\}.
\end{aligned}
```

Composites and dependent connections are not counted as new independent fields. The gauge conditions, source-local branch $`L>0`$, condition $`g\ne0`$, and all covariant definitions are stated in the [shared dictionary](fields_and_derivatives.md). These formulae define the action before selecting a background.

<a id="5-reading-the-technical-files"></a>

## Reading the technical files

For each building block, separate files contain the bosonic density, covariant core, and two-explicit-fermion blocks. The physical two-fermion definition includes implicit contributions. The common two-derivative action is therefore used through links to the same explicit formulas instead of being duplicated in every theory file.

The [action index](action_family.md) provides access to every theory and building-block file. Composite-field degree expansions, the general density's SUSY boundary current, and graded checks of composite-multiplet transformations appear there as separate appendices.
