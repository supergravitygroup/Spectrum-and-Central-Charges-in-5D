# R-squared building block: covariant core

This file gives the **covariant core** without explicit spinors. Hatted objects and full derivatives contain implicit two-fermion contributions; this core is not identical to the bosonic density.

[Building-block action](invariant.md) · [Shared definitions](../../common/fields_and_derivatives.md) · [Fermion order](../../common/fermion_order.md) · [Check scope](../../references/component_records/02_action_family.md)

Equation provenance is provided in the [source record](../../references/component_records/02_action_family.md), and checked SUSY identities are listed in the [technical index](../../common/action_family.md). These lists track the coefficients and fermion degree of the specified source action.

```math
\mathcal U_{R}=\sum_{r=1}^{49} \mathcal U_{R,r}.
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
<a id="u-018"></a>
<a id="u-019"></a>
<a id="u-020"></a>
<a id="u-021"></a>

```math
\begin{aligned}
\sum_{r=1}^{21} \mathcal U_{R,r}={}&
% u-001: \mathcal U_{R,1}
\widehat G_{ab} L^{ij} \frac{1}{L^{3}} \mathcal D_{c} (L_{j}{}^{k}) \mathcal D_{d} (L_{ik}) \varepsilon^{abcd}{}_{e} [
-\frac{1}{2 L} E^{e} -\frac{\sqrt{2}}{4} V^{e}]
% u-002: \mathcal U_{R,2}
+\widehat G_{ab} L^{ij} \frac{1}{L} \widehat R_{cdij} (V) \varepsilon^{abcd}{}_{e} [
\\
&{}
-\frac{1}{2 L} E^{e} -\frac{\sqrt{2}}{4} V^{e}]
% u-003: \mathcal U_{R,3}
-\widehat G_{ab} L^{ij} N \frac{1}{L^{2}} \widehat R^{ab}{}_{ij} (V)
% u-004: \mathcal U_{R,4}
+\widehat G_{ab} L^{ij} N \frac{1}{L^{4}} \mathcal D^{a} (L_{ki}) \mathcal D^{b} (L^{k}{}_{j})
\\
&{}
% u-005: \mathcal U_{R,5}
+\widehat G_{ab} \frac{1}{L} \mathcal D_{c} (E_{d}) \varepsilon^{abcd}{}_{e} [
-\frac{1}{L} E^{e} -\frac{\sqrt{2}}{2} V^{e}]
% u-006: \mathcal U_{R,6}
+\widehat G_{ab} \sqrt{2} \frac{1}{L} V^{b} [-\frac{N}{L} \mathcal D^{a}(L)
+\mathcal D^{a}(N)]
\\
&{}
% u-007: \mathcal U_{R,7}
-\widehat G_{ab} \varepsilon^{ab}{}_{cde} \sqrt{2} \frac{1}{2 L^{2}} E^{c} V^{e} \mathcal D^{d} (L)
% u-008: \mathcal U_{R,8}
+16 \widehat G_{ab} N^{2} \frac{1}{L^{2}} T^{ab}
% u-009: \mathcal U_{R,9}
-2 \widehat G_{ab} N \frac{1}{L^{2}} \mathcal D^{a} (E^{b})
\\
&{}
% u-010: \mathcal U_{R,10}
-2 \widehat G_{ab} \frac{1}{L^{2}} E^{a} \mathcal D^{b} (N)
% u-011: \mathcal U_{R,11}
+2 \frac{1}{L} E_{a} \frac{1}{L} \mathcal D_{b} (L) \frac{1}{L} \mathcal D^{b} (L) [\frac{2}{L} E^{a}
+\sqrt{2} V^{a}]
% u-012: \mathcal U_{R,12}
+2 \frac{1}{L} E_{a} \frac{1}{L} \mathcal D_{b} (L) \frac{1}{L} \mathcal D^{a} (L) [
\\
&{}
-\frac{2}{L} E^{b} -\sqrt{2} V^{b}]
% u-013: \mathcal U_{R,13}
+2 \frac{1}{L} E_{a} \frac{1}{L} \mathcal D_{b} (L) \frac{1}{L} L^{ij} [\widehat R^{ab}{}_{ij}(V)
-\frac{5}{L^{2}} \mathcal D^{a}(L_{ki}) \mathcal D^{b}(L^{k}{}_{j})]
\\
&{}
% u-014: \mathcal U_{R,14}
+2 \frac{1}{L} E_{a} \frac{1}{L} \mathcal D_{b} (L) \frac{1}{L} \mathcal D^{a} (E^{b})
% u-015: \mathcal U_{R,15}
-4 \frac{1}{L} E_{a} \frac{1}{L} \mathcal D_{b} (L) \frac{1}{L} \mathcal D^{b} (E^{a})
% u-016: \mathcal U_{R,16}
-8 \frac{1}{L} E_{a} E^{a} D \frac{1}{L}
\\
&{}
% u-017: \mathcal U_{R,17}
+2 \frac{1}{L} E_{a} E^{a} N (g + \frac{N}{L^{2}}) \frac{1}{L}
% u-018: \mathcal U_{R,18}
-4 \frac{1}{L} E_{a} E^{a} \frac{1}{L^{2}} \Box^c (L)
% u-019: \mathcal U_{R,19}
+\frac{1}{L} E_{a} E^{a} \frac{1}{L^{3}} E^{b} E_{b}
\\
&{}
% u-020: \mathcal U_{R,20}
-16 \frac{1}{L} E_{a} E^{a} \frac{1}{3 L} T^{bc} T_{bc}
% u-021: \mathcal U_{R,21}
+\frac{1}{L} E_{a} E^{a} \frac{1}{L^{3}} \mathcal D^{b} (L^{ij}) \mathcal D_{b} (L_{ij})
\end{aligned}
```

<a id="u-022"></a>
<a id="u-023"></a>
<a id="u-024"></a>
<a id="u-025"></a>
<a id="u-026"></a>
<a id="u-027"></a>
<a id="u-028"></a>
<a id="u-029"></a>
<a id="u-030"></a>
<a id="u-031"></a>
<a id="u-032"></a>
<a id="u-033"></a>
<a id="u-034"></a>
<a id="u-035"></a>
<a id="u-036"></a>
<a id="u-037"></a>

```math
\begin{aligned}
\sum_{r=22}^{37} \mathcal U_{R,r}={}&
% u-022: \mathcal U_{R,22}
\frac{1}{L} E_{a} \frac{1}{L} [2 L^{ij}[\frac{1}{L^{2}} \mathcal D^{a}(L_{ik})[3 \Box^c(L^{k}{}_{j})
-\frac{1}{L^{2}} E_{b} L^{kl} \mathcal D^{b}(L_{jl})] -\mathcal D^{b}(\widehat R^{a}{}_{bij}(V))
\\
&{}
-\frac{1}{L^{2}} \mathcal D^{b}\mathcal D^{a}(L^{k}{}_{j}) \mathcal D_{b}(L_{ki})]
+\mathcal D^{a}\mathcal D_{b}(L)[\frac{2}{L} E^{b} +\sqrt{2} V^{b}]
\\
&{}
+\mathcal D_{b}(L^{ij})[-2 \widehat R^{ab}{}_{ij}(V) +\frac{1}{L^{2}} E^{b} \mathcal D^{a}(L_{ij})]
+2 \Box^c(E^{a}) +32 N \mathcal D^{b}(T^{a}{}_{b}) -2 N \mathcal D^{b}(\widehat G^{a}{}_{b})
\\
&{}
-2 \mathcal D^{b}\mathcal D^{a}(E_{b}) +32 T^{a}{}_{b} \mathcal D^{b}(N)
-\sqrt{2} V^{a} \Box^c(L) +\frac{2}{L} \mathcal D^{a}(L) \mathcal D^{b}(E_{b})]
\\
&{}
% u-023: \mathcal U_{R,23}
-4 \mathcal D_{a} (L_{ij}) \mathcal D^{a} (L^{ij}) D \frac{1}{L^{2}}
% u-024: \mathcal U_{R,24}
+\mathcal D_{a} (L_{ij}) \mathcal D^{a} (L^{ij}) N (g + \frac{N}{L^{2}}) \frac{1}{L} \frac{1}{L}
% u-025: \mathcal U_{R,25}
+\mathcal D_{a} (L_{ij}) \mathcal D^{a} (L^{ij}) \frac{1}{L^{3}} \Box^c (L)
\\
&{}
% u-026: \mathcal U_{R,26}
-8 \mathcal D_{a} (L_{ij}) \mathcal D^{a} (L^{ij}) \frac{1}{3 L^{2}} T^{bc} T_{bc}
% u-027: \mathcal U_{R,27}
-3 \mathcal D_{a} (L_{ij}) \mathcal D^{a} (L^{ij}) \frac{1}{4 L^{4}} \mathcal D^{b} (L^{kl}) \mathcal D_{b} (L_{kl})
\\
&{}
% u-028: \mathcal U_{R,28}
-16 \mathcal D_{a} (L_{ij}) \frac{1}{L^{3}} L^{jk} \mathcal D_{b} (L^{i}{}_{k}) N \frac{1}{L} T^{ab}
% u-029: \mathcal U_{R,29}
+3 \mathcal D_{a} (L_{ij}) \frac{1}{L^{3}} L^{jk} \mathcal D_{b} (L^{i}{}_{k}) \sqrt{2} \frac{1}{L} V^{b} \mathcal D^{a} (L)
\\
&{}
% u-030: \mathcal U_{R,30}
+\mathcal D_{a} (L_{ij}) \frac{1}{L^{3}} L^{jk} \sqrt{2} [V^{a} \Box^c(L^{i}{}_{k})
-V_{b} \mathcal D^{a}\mathcal D^{b}(L^{i}{}_{k})]
% u-031: \mathcal U_{R,31}
+\mathcal D_{a} (L_{ij}) \frac{1}{L^{3}} \mathcal D^{a} (L) [-2 \Box^c(L^{ij})
\\
&{}
+\frac{1}{L} \mathcal D^{b}(L^{ij}) \mathcal D_{b}(L)]
% u-032: \mathcal U_{R,32}
+\frac{64}{9} T_{ab} T_{cd} T^{ab} T^{cd}
% u-033: \mathcal U_{R,33}
+\frac{64}{3} T_{ab} T^{ab} D
% u-034: \mathcal U_{R,34}
-\frac{16}{3} T_{ab} T^{ab} N (g + \frac{27 N}{L^{2}})
\\
&{}
% u-035: \mathcal U_{R,35}
+16 T_{ab} T^{ab} \frac{1}{3 L} \Box^c (L)
% u-036: \mathcal U_{R,36}
+16 T_{ab} \sqrt{2} \frac{1}{L} V^{b} [\frac{N}{L} \mathcal D^{a}(L)
-\mathcal D^{a}(N)]
% u-037: \mathcal U_{R,37}
+32 T_{ab} N \frac{1}{L^{2}} \mathcal D^{a} (E^{b})
\end{aligned}
```

<a id="u-038"></a>
<a id="u-039"></a>
<a id="u-040"></a>
<a id="u-041"></a>
<a id="u-042"></a>
<a id="u-043"></a>
<a id="u-044"></a>
<a id="u-045"></a>
<a id="u-046"></a>
<a id="u-047"></a>
<a id="u-048"></a>
<a id="u-049"></a>

```math
\begin{aligned}
\sum_{r=38}^{49} \mathcal U_{R,r}={}&
% u-038: \mathcal U_{R,38}
16 T_{ab} N \frac{1}{L^{2}} L^{ij} \widehat R^{ab}{}_{ij} (V)
% u-039: \mathcal U_{R,39}
+\sqrt{2} \frac{1}{L} V_{a} [\frac{1}{L} \mathcal D_{b}(L)[\mathcal D^{a}(E^{b})
\\
&{}
-2 \mathcal D^{b}(E^{a}) -L^{ij} \widehat R^{ba}{}_{ij}(V)] +\Box^c(E^{a})
-16 N \mathcal D^{b}(T_{b}{}^{a}) +N \mathcal D^{b}(\widehat G_{b}{}^{a})
\\
&{}
-\mathcal D^{b}\mathcal D^{a}(E_{b}) -L^{ij} \mathcal D^{b}(\widehat R^{a}{}_{bij}(V))
+\frac{1}{L} \mathcal D^{a}(L) \mathcal D^{b}(E_{b}) -\mathcal D^{b}(L^{ij}) \widehat R^{a}{}_{bij}(V)]
\\
&{}
% u-040: \mathcal U_{R,40}
+4 \mathcal D_{a} (L) N^{2} \frac{1}{L^{4}} \mathcal D^{a} (L)
% u-041: \mathcal U_{R,41}
-4 \mathcal D_{a} (L) N \frac{1}{L^{3}} \mathcal D^{a} (N)
% u-042: \mathcal U_{R,42}
+16 D^{2}
% u-043: \mathcal U_{R,43}
-8 D N (g + \frac{3 N}{L^{2}})
\\
&{}
% u-044: \mathcal U_{R,44}
+N^{3} (2 g + \frac{N}{L^{2}}) \frac{1}{L^{2}}
% u-045: \mathcal U_{R,45}
+8 D \frac{1}{L} \Box^c (L)
% u-046: \mathcal U_{R,46}
-2 N (g + \frac{2 N}{L^{2}}) \frac{1}{L} \Box^c (L)
% u-047: \mathcal U_{R,47}
+2 N \frac{1}{L^{2}} \Box^c (N)
% u-048: \mathcal U_{R,48}
+4 N^{2} \frac{1}{L^{2}} f_{a}{}^{a}
\\
&{}
% u-049: \mathcal U_{R,49}
+\frac{1}{L^{2}} \Box^c (L^{ij}) \Box^c (L_{ij})
\end{aligned}
```
