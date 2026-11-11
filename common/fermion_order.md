# Physical fermion order and the bosonic decomposition

This file defines the common grading for all building blocks in the [action index](action_family.md). The fundamental physical fermions are $`\psi_\mu^i,\varphi^i`$. Fermion degrees of dependent objects are counted in these fields. The distinction between $`\psi^i`$ and $`\psi_\mu^i`$, and the construction of derivatives before gauge fixing, are maintained in the [shared dictionary](fields_and_derivatives.md).

<a id="1-definition-of-the-projection"></a>

## Definition of the projection

Let $`\tau`$ be a formal Grassmann-even variable used only to track fermion degree. Each fundamental physical fermion and its barred counterpart carries one factor of $`\tau`$; every dependent object is evaluated from its definition under the same operation. Bosonic fields and couplings remain symbolic.

```math
\Pi_q F:=[\tau^q]F[\tau],
\qquad
\Pi_{\le2}F:=\Pi_0F+\Pi_1F+\Pi_2F.
```

The notation $`[\tau^q]`$ denotes formal coefficient extraction. The variable $`\tau`$ is not a physical parameter and is assigned no numerical sample value. Only the contributions $`q=0,2`$ remain in an even density.

Keeping product order fixed,

```math
\begin{aligned}
\Pi_0(XY)&=(\Pi_0X)(\Pi_0Y),\\
\Pi_2(XY)&=(\Pi_0X)(\Pi_2Y)
 +(\Pi_1X)(\Pi_1Y)+(\Pi_2X)(\Pi_0Y)
\end{aligned}
```

These identities follow directly by adding powers of $`\tau`$ in the product $`X[\tau]Y[\tau]`$; no Grassmann-odd factors are interchanged. In particular, for even $`X`$,

```math
\Pi_2(X^2)=X^{(0)}X^{(2)}+X^{(2)}X^{(0)}.
```

For tensor-valued objects, contraction order is preserved as well.

<a id="2-three-distinct-blocks"></a>

## Three distinct blocks

For each building block, let $`\mathcal U_A`$ denote the covariant core with no explicit fermions and $`\mathcal V_A`$ the terms with two explicit fermions. Hatted fields and supercovariant derivatives mean that $`\Pi_2\mathcal U_A`$ is generally nonzero.

```math
\begin{aligned}
\mathcal B_A&:=\Pi_0\mathcal U_A,
&\Pi_0\mathcal V_A&=0,\\
\ell_A^{(0)}&=\mathcal B_A,
&\ell_A^{(2)}&=\Pi_2\mathcal U_A+\Pi_2\mathcal V_A,\\
\Pi_{\le2}(\mathcal U_A+\mathcal V_A)
&=\mathcal B_A+\ell_A^{(2)}.
\end{aligned}
```

Therefore,

```math
\ell_A^{(2)}
=\Pi_{\le2}(\mathcal U_A+\mathcal V_A-\mathcal B_A).
```

The three separate formula lists in the action files supply every term in this identity. The physical two-fermion density cannot be replaced by $`\mathcal V_A`$ alone.

<a id="3-an-explicit-example-of-implicit-fermions"></a>

## An explicit example of implicit fermions

Decomposing the source definitions by physical fermion order gives

```math
\begin{aligned}
\widehat G_{\mu\nu}^{(0)}&=G_{\mu\nu},
&\widehat G_{\mu\nu}^{(2)}&=\frac i2\bar\psi_{[\mu}\psi_{\nu]},\\
\widehat H_{\mu\nu\rho}^{(0)}&=H_{\mu\nu\rho},
&\widehat H_{\mu\nu\rho}^{(2)}&=-\frac34\bar\psi_{[\mu}\gamma_\nu\psi_{\rho]}.
\end{aligned}
```

Therefore, retaining the metric and vielbein as independent bosonic fields,

```math
\begin{aligned}
\Pi_2(\widehat G_{ab}\widehat G^{ab})
&=G_{ab}\widehat G^{ab(2)}+\widehat G_{ab}^{(2)}G^{ab}\\
&=2G^{ab}\left(\frac i2\bar\psi_{[a}\psi_{b]}\right)
=iG^{ab}\bar\psi_a\psi_b,\\
\Pi_2(\widehat H_{abc}\widehat H^{abc})
&=2H^{abc}\left(-\frac34\bar\psi_{[a}\gamma_b\psi_{c]}\right)\\
&=-\frac32H^{abc}\bar\psi_a\gamma_b\psi_c.
\end{aligned}
```

In the last identities, complete contraction with an antisymmetric tensor expands unit-weight antisymmetrization. These examples do not choose parameter or field values; they are the exact degree-two coefficients of the corresponding monomials.

The same operation for the composite $`T`$ gives

```math
T_{ab}^{(q)}
=\frac18\widehat G_{ab}^{(q)}
 +\frac1{48}\varepsilon_{abcde}\widehat H^{cde(q)},
\qquad q=0,2
```

The degree-two part of the dependent spin connection remains

```math
\omega_\mu{}^{ab(2)}
=\frac12\bar\psi^{[a}\gamma^{b]}\psi_\mu
 +\frac14\bar\psi^a\gamma_\mu\psi^b
```

Replacing $`\omega`$ directly by the torsionless connection would lose this contribution.

<a id="4-derivatives-and-scope-of-completeness"></a>

## Derivatives and scope of completeness

The coefficient $`\Pi_q(\mathcal D_aX)`$ is selected after establishing the full supercovariant derivative on the relevant field or derivative descendant. In general, this does not mean replacing $`\mathcal D_a`$ by a Lorentz derivative alone. Derivatives are not reordered, and total derivatives are not discarded.

Action components are given in compact supercovariant form. Constructing the Hessian requires expanding the relevant fermion degrees of these objects together; the [quadratic field definitions and coefficient index](fluctuation_method.md) identify the local sources for this operation. Established multiplet and derivative constructions are listed in the [source map](../references/bibliography.md). Specific matches between local action versions and spectrum Hessians are tracked in the [correction record](../references/source_distinctions.md).

## Degree in the SUSY check

The condition for the two-fermion action is the one-fermion variation of the two-fermion action:

```math
[\delta\mathcal L]_1=\delta_{+1}\mathcal L^{(0)}+\delta_{-1}\mathcal L^{(2)}.
```

The [general vector–linear density calculation](details/vector_linear_density.md) derives the explicit boundary current of this sum, including the three-form contribution and dependent connections. The SUSY parameter is not counted as a physical fermion in the grading.
