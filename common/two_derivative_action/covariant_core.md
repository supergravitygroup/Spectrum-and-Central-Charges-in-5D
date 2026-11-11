# Two-derivative building block: covariant core

This file gives the **covariant core** without explicit spinors. Hatted objects and full derivatives contain implicit two-fermion contributions; this core is not identical to the bosonic density.

[Building-block action](invariant.md) · [Shared definitions](../fields_and_derivatives.md) · [Fermion order](../fermion_order.md) · [Check scope](../../references/component_records/02_action_family.md)

Equation provenance is provided in the [source record](../../references/component_records/02_action_family.md), and checked SUSY identities are listed in the [technical index](../action_family.md). These lists track the coefficients and fermion degree of the specified source action.

```math
\mathcal U_{2}=\sum_{r=1}^{11} \mathcal U_{2,r}.
```

Within each aligned sum, the indexed terms follow their original order; each term link points to the group containing that term.

<a id="u-001"></a>
<a id="u-002"></a>
<a id="u-003"></a>
<a id="u-004"></a>
<a id="u-005"></a>
<a id="u-006"></a>
<a id="u-007"></a>
<a id="u-008"></a>
<a id="u-009"></a>
<a id="u-010"></a>
<a id="u-011"></a>

```math
\begin{aligned}
\mathcal U_{2}={}&
% u-001: \mathcal U_{2,1}
-4 \frac{1}{L} E_{a} \frac{1}{L} \mathcal D_{b} (L) E^{ab}
% u-002: \mathcal U_{2,2}
+2 \frac{1}{L} E_{a} E^{a}
% u-003: \mathcal U_{2,3}
+\mathcal D_{a} (L_{ij}) \mathcal D^{a} (L^{ij}) \frac{1}{L}
% u-004: \mathcal U_{2,4}
+2 \mathcal D_{a} (L_{ij}) \frac{1}{L^{3}} L^{jk} \mathcal D_{b} (L^{i}{}_{k}) E^{ab}
\\
&{}
% u-005: \mathcal U_{2,5}
-\frac{16}{3} T_{ab} T^{ab} L
% u-006: \mathcal U_{2,6}
+2 E_{ab} [-g G^{ab} -\frac{2}{L} \mathcal D^{a}(E^{b}) -\frac{1}{L} L^{ij} \widehat R^{ab}{}_{ij}(V)]
% u-007: \mathcal U_{2,7}
-8 D L
% u-008: \mathcal U_{2,8}
+2 L^{2} g^{2}
% u-009: \mathcal U_{2,9}
-4 N g
\\
&{}
% u-010: \mathcal U_{2,10}
-2 N^{2} \frac{1}{L}
% u-011: \mathcal U_{2,11}
-2 \Box^c (L)
\end{aligned}
```
