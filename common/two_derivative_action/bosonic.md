# Two-derivative building block: bosonic density

This file gives every block of the **bosonic projection** of the source density. Derivatives here are bosonic superconformal derivatives; dependent connections are retained in second and higher derivatives.

[Building-block action](invariant.md) · [Shared definitions](../fields_and_derivatives.md) · [Fermion order](../fermion_order.md) · [Check scope](../../references/component_records/02_action_family.md)

Equation provenance is provided in the [source record](../../references/component_records/02_action_family.md), and checked SUSY identities are listed in the [technical index](../action_family.md). These lists track the coefficients and fermion degree of the specified source action.

```math
\mathcal B_{2}=\sum_{r=1}^{11} \mathcal B_{2,r}.
```

Within each aligned sum, the indexed terms follow their original order; each term link points to the group containing that term.

<a id="b-001"></a>
<a id="b-002"></a>
<a id="b-003"></a>
<a id="b-004"></a>
<a id="b-005"></a>
<a id="b-006"></a>
<a id="b-007"></a>
<a id="b-008"></a>
<a id="b-009"></a>
<a id="b-010"></a>
<a id="b-011"></a>

```math
\begin{aligned}
\mathcal B_{2}={}&
% b-001: \mathcal B_{2,1}
-4 \frac{1}{L} E_{a} \frac{1}{L} \mathscr D_{b} (L) E^{ab}
% b-002: \mathcal B_{2,2}
+2 \frac{1}{L} E_{a} E^{a}
% b-003: \mathcal B_{2,3}
+\mathscr D_{a} (L_{ij}) \mathscr D^{a} (L^{ij}) \frac{1}{L}
% b-004: \mathcal B_{2,4}
+2 \mathscr D_{a} (L_{ij}) \frac{1}{L^{3}} L^{jk} \mathscr D_{b} (L^{i}{}_{k}) E^{ab}
\\
&{}
% b-005: \mathcal B_{2,5}
-\frac{16}{3} T_{ab} T^{ab} L
% b-006: \mathcal B_{2,6}
+2 E_{ab} [-g G^{ab} -\frac{2}{L} \mathscr D^{a}(E^{b}) -\frac{1}{L} L^{ij} R^{ab}{}_{ij}(V)]
% b-007: \mathcal B_{2,7}
-8 D L
% b-008: \mathcal B_{2,8}
+2 L^{2} g^{2}
% b-009: \mathcal B_{2,9}
-4 N g
\\
&{}
% b-010: \mathcal B_{2,10}
-2 N^{2} \frac{1}{L}
% b-011: \mathcal B_{2,11}
-2 \Box_{\mathrm B}^{c} (L)
\end{aligned}
```
