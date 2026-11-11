# Weyl-squared building block: covariant core

This file gives the **covariant core** without explicit spinors. Hatted objects and full derivatives contain implicit two-fermion contributions; this core is not identical to the bosonic density.

[Building-block action](invariant.md) · [Shared definitions](../../common/fields_and_derivatives.md) · [Fermion order](../../common/fermion_order.md) · [Check scope](../../references/component_records/02_action_family.md)

Equation provenance is provided in the [source record](../../references/component_records/02_action_family.md), and checked SUSY identities are listed in the [technical index](../../common/action_family.md). These lists track the coefficients and fermion degree of the specified source action.

```math
\mathcal U_{W}=\sum_{r=1}^{17} \mathcal U_{W,r}.
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
<a id="u-012"></a>
<a id="u-013"></a>
<a id="u-014"></a>
<a id="u-015"></a>
<a id="u-016"></a>
<a id="u-017"></a>

```math
\begin{aligned}
\mathcal U_{W}={}&
% u-001: \mathcal U_{W,1}
\frac{4}{9} C_{a} T_{bc} [64 T^{a}{}_{d}[-6 \mathcal D^{b}(T^{dc})
-\mathcal D^{d}(T^{bc})] +24 \varepsilon^{ac}{}_{def}[-2 \mathcal D^{d}\mathcal D^{b}(T^{ef})
\\
&{}
+3 \mathcal D^{d}\mathcal D^{e}(T^{bf})] +9 \mathcal D^{d}(\widehat C^{a}{}_{d}{}^{bc})
+384 T^{ab} \mathcal D^{d}(T^{c}{}_{d}) -32 T^{bc} \mathcal D^{d}(T^{a}{}_{d})
-384 T^{b}{}_{d} \mathcal D^{d}(T^{ac})]
\\
&{}
% u-002: \mathcal U_{W,2}
+\frac{4}{3} C_{a} \mathcal D_{b} (T_{cd}) [8 \varepsilon^{abd}{}_{ef}[2 \mathcal D^{c}(T^{ef})
-3 \mathcal D^{e}(T^{cf})] +3 \widehat C^{abcd}]
% u-003: \mathcal U_{W,3}
+\frac{1}{16} C_{a} \varepsilon^{a}{}_{bcde} \widehat C^{bc}{}_{fg} \widehat C^{defg}
\\
&{}
% u-004: \mathcal U_{W,4}
-\frac{1}{12} C_{a} \varepsilon^{a}{}_{bcde} \widehat R^{bc}{}_{ij} (V) \widehat R^{deij} (V)
% u-005: \mathcal U_{W,5}
-\frac{64}{3} C_{a} D \mathcal D^{b} (T^{a}{}_{b})
% u-006: \mathcal U_{W,6}
-\frac{64}{3} C_{a} T^{a}{}_{b} \mathcal D^{b} (D)
% u-007: \mathcal U_{W,7}
-\frac{16}{3} T_{ab} T_{cd} \widehat C^{abcd}
\\
&{}
% u-008: \mathcal U_{W,8}
-\frac{2816}{27} T_{ab} T_{cd} T^{ab} T^{cd}
% u-009: \mathcal U_{W,9}
+1024 T_{ab} T_{cd} T^{ac} T^{bd}
% u-010: \mathcal U_{W,10}
+\frac{128}{3} T_{ab} T_{cd} \mathcal D^{e} (T_{ef}) \varepsilon^{abcdf}
% u-011: \mathcal U_{W,11}
+\frac{1024}{9} T_{ab} T^{ab} D
\\
&{}
% u-012: \mathcal U_{W,12}
+\frac{128}{3} T_{ab} \mathcal D^{a} \mathcal D^{c} (T^{b}{}_{c})
% u-013: \mathcal U_{W,13}
-\frac{8}{3} T_{ab} g L^{ij} \widehat R^{ab}{}_{ij} (V)
% u-014: \mathcal U_{W,14}
+\frac{64}{3} \mathcal D_{a} (T_{bc}) [-\mathcal D^{a}(T^{bc}) +\mathcal D^{b}(T^{ac})]
% u-015: \mathcal U_{W,15}
+\frac{64}{3} D^{2}
\\
&{}
% u-016: \mathcal U_{W,16}
+\frac{1}{8} \widehat C^{abcd} \widehat C_{abcd}
% u-017: \mathcal U_{W,17}
-\frac{1}{3} \widehat R^{abij} (V) \widehat R_{abij} (V)
\end{aligned}
```
