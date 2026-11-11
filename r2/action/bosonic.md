# R-squared building block: bosonic density

This file gives every block of the **bosonic projection** of the source density. Derivatives here are bosonic superconformal derivatives; dependent connections are retained in second and higher derivatives.

[Building-block action](invariant.md) · [Shared definitions](../../common/fields_and_derivatives.md) · [Fermion order](../../common/fermion_order.md) · [Check scope](../../references/component_records/02_action_family.md)

Equation provenance is provided in the [source record](../../references/component_records/02_action_family.md), and checked SUSY identities are listed in the [technical index](../../common/action_family.md). These lists track the coefficients and fermion degree of the specified source action.

```math
\mathcal B_{R}=\sum_{r=1}^{49} \mathcal B_{R,r}.
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
<a id="b-012"></a>
<a id="b-013"></a>
<a id="b-014"></a>
<a id="b-015"></a>
<a id="b-016"></a>
<a id="b-017"></a>
<a id="b-018"></a>
<a id="b-019"></a>
<a id="b-020"></a>
<a id="b-021"></a>

```math
\begin{aligned}
\sum_{r=1}^{21} \mathcal B_{R,r}={}&
% b-001: \mathcal B_{R,1}
G_{ab} L^{ij} \frac{1}{L^{3}} \mathscr D_{c} (L_{j}{}^{k}) \mathscr D_{d} (L_{ik}) \varepsilon^{abcd}{}_{e} [
-\frac{1}{2 L} E^{e} -\frac{\sqrt{2}}{4} V^{e}]
% b-002: \mathcal B_{R,2}
+G_{ab} L^{ij} \frac{1}{L} R_{cdij} (V) \varepsilon^{abcd}{}_{e} [-\frac{1}{2 L} E^{e}
\\
&{}
-\frac{\sqrt{2}}{4} V^{e}]
% b-003: \mathcal B_{R,3}
-G_{ab} L^{ij} N \frac{1}{L^{2}} R^{ab}{}_{ij} (V)
% b-004: \mathcal B_{R,4}
+G_{ab} L^{ij} N \frac{1}{L^{4}} \mathscr D^{a} (L_{ki}) \mathscr D^{b} (L^{k}{}_{j})
\\
&{}
% b-005: \mathcal B_{R,5}
+G_{ab} \frac{1}{L} \mathscr D_{c} (E_{d}) \varepsilon^{abcd}{}_{e} [
-\frac{1}{L} E^{e} -\frac{\sqrt{2}}{2} V^{e}]
% b-006: \mathcal B_{R,6}
+G_{ab} \sqrt{2} \frac{1}{L} V^{b} [-\frac{N}{L} \mathscr D^{a}(L)
+\mathscr D^{a}(N)]
\\
&{}
% b-007: \mathcal B_{R,7}
-G_{ab} \varepsilon^{ab}{}_{cde} \sqrt{2} \frac{1}{2 L^{2}} E^{c} V^{e} \mathscr D^{d} (L)
% b-008: \mathcal B_{R,8}
+16 G_{ab} N^{2} \frac{1}{L^{2}} T^{ab}
% b-009: \mathcal B_{R,9}
-2 G_{ab} N \frac{1}{L^{2}} \mathscr D^{a} (E^{b})
\\
&{}
% b-010: \mathcal B_{R,10}
-2 G_{ab} \frac{1}{L^{2}} E^{a} \mathscr D^{b} (N)
% b-011: \mathcal B_{R,11}
+2 \frac{1}{L} E_{a} \frac{1}{L} \mathscr D_{b} (L) \frac{1}{L} \mathscr D^{b} (L) [\frac{2}{L} E^{a}
+\sqrt{2} V^{a}]
% b-012: \mathcal B_{R,12}
+2 \frac{1}{L} E_{a} \frac{1}{L} \mathscr D_{b} (L) \frac{1}{L} \mathscr D^{a} (L) [
\\
&{}
-\frac{2}{L} E^{b} -\sqrt{2} V^{b}]
% b-013: \mathcal B_{R,13}
+2 \frac{1}{L} E_{a} \frac{1}{L} \mathscr D_{b} (L) \frac{1}{L} L^{ij} [R^{ab}{}_{ij}(V)
-\frac{5}{L^{2}} \mathscr D^{a}(L_{ki}) \mathscr D^{b}(L^{k}{}_{j})]
\\
&{}
% b-014: \mathcal B_{R,14}
+2 \frac{1}{L} E_{a} \frac{1}{L} \mathscr D_{b} (L) \frac{1}{L} \mathscr D^{a} (E^{b})
% b-015: \mathcal B_{R,15}
-4 \frac{1}{L} E_{a} \frac{1}{L} \mathscr D_{b} (L) \frac{1}{L} \mathscr D^{b} (E^{a})
% b-016: \mathcal B_{R,16}
-8 \frac{1}{L} E_{a} E^{a} D \frac{1}{L}
\\
&{}
% b-017: \mathcal B_{R,17}
+2 \frac{1}{L} E_{a} E^{a} N (g + \frac{N}{L^{2}}) \frac{1}{L}
% b-018: \mathcal B_{R,18}
-4 \frac{1}{L} E_{a} E^{a} \frac{1}{L^{2}} \Box_{\mathrm B}^{c} (L)
% b-019: \mathcal B_{R,19}
+\frac{1}{L} E_{a} E^{a} \frac{1}{L^{3}} E^{b} E_{b}
\\
&{}
% b-020: \mathcal B_{R,20}
-16 \frac{1}{L} E_{a} E^{a} \frac{1}{3 L} T^{bc} T_{bc}
% b-021: \mathcal B_{R,21}
+\frac{1}{L} E_{a} E^{a} \frac{1}{L^{3}} \mathscr D^{b} (L^{ij}) \mathscr D_{b} (L_{ij})
\end{aligned}
```

<a id="b-022"></a>
<a id="b-023"></a>
<a id="b-024"></a>
<a id="b-025"></a>
<a id="b-026"></a>
<a id="b-027"></a>
<a id="b-028"></a>
<a id="b-029"></a>
<a id="b-030"></a>
<a id="b-031"></a>
<a id="b-032"></a>
<a id="b-033"></a>
<a id="b-034"></a>
<a id="b-035"></a>
<a id="b-036"></a>
<a id="b-037"></a>

```math
\begin{aligned}
\sum_{r=22}^{37} \mathcal B_{R,r}={}&
% b-022: \mathcal B_{R,22}
\frac{1}{L} E_{a} \frac{1}{L} [2 L^{ij}[\frac{1}{L^{2}} \mathscr D^{a}(L_{ik})[3 \Box_{\mathrm B}^{c}(L^{k}{}_{j})
-\frac{1}{L^{2}} E_{b} L^{kl} \mathscr D^{b}(L_{jl})] -\mathscr D^{b}(R^{a}{}_{bij}(V))
\\
&{}
-\frac{1}{L^{2}} \mathscr D^{b}\mathscr D^{a}(L^{k}{}_{j}) \mathscr D_{b}(L_{ki})]
+\mathscr D^{a}\mathscr D_{b}(L)[\frac{2}{L} E^{b} +\sqrt{2} V^{b}]
\\
&{}
+\mathscr D_{b}(L^{ij})[-2 R^{ab}{}_{ij}(V) +\frac{1}{L^{2}} E^{b} \mathscr D^{a}(L_{ij})]
+2 \Box_{\mathrm B}^{c}(E^{a}) +32 N \mathscr D^{b}(T^{a}{}_{b}) -2 N \mathscr D^{b}(G^{a}{}_{b})
\\
&{}
-2 \mathscr D^{b}\mathscr D^{a}(E_{b}) +32 T^{a}{}_{b} \mathscr D^{b}(N)
-\sqrt{2} V^{a} \Box_{\mathrm B}^{c}(L) +\frac{2}{L} \mathscr D^{a}(L) \mathscr D^{b}(E_{b})]
\\
&{}
% b-023: \mathcal B_{R,23}
-4 \mathscr D_{a} (L_{ij}) \mathscr D^{a} (L^{ij}) D \frac{1}{L^{2}}
% b-024: \mathcal B_{R,24}
+\mathscr D_{a} (L_{ij}) \mathscr D^{a} (L^{ij}) N (g + \frac{N}{L^{2}}) \frac{1}{L} \frac{1}{L}
% b-025: \mathcal B_{R,25}
+\mathscr D_{a} (L_{ij}) \mathscr D^{a} (L^{ij}) \frac{1}{L^{3}} \Box_{\mathrm B}^{c} (L)
\\
&{}
% b-026: \mathcal B_{R,26}
-8 \mathscr D_{a} (L_{ij}) \mathscr D^{a} (L^{ij}) \frac{1}{3 L^{2}} T^{bc} T_{bc}
% b-027: \mathcal B_{R,27}
-3 \mathscr D_{a} (L_{ij}) \mathscr D^{a} (L^{ij}) \frac{1}{4 L^{4}} \mathscr D^{b} (L^{kl}) \mathscr D_{b} (L_{kl})
\\
&{}
% b-028: \mathcal B_{R,28}
-16 \mathscr D_{a} (L_{ij}) \frac{1}{L^{3}} L^{jk} \mathscr D_{b} (L^{i}{}_{k}) N \frac{1}{L} T^{ab}
% b-029: \mathcal B_{R,29}
+3 \mathscr D_{a} (L_{ij}) \frac{1}{L^{3}} L^{jk} \mathscr D_{b} (L^{i}{}_{k}) \sqrt{2} \frac{1}{L} V^{b} \mathscr D^{a} (L)
\\
&{}
% b-030: \mathcal B_{R,30}
+\mathscr D_{a} (L_{ij}) \frac{1}{L^{3}} L^{jk} \sqrt{2} [V^{a} \Box_{\mathrm B}^{c}(L^{i}{}_{k})
-V_{b} \mathscr D^{a}\mathscr D^{b}(L^{i}{}_{k})]
% b-031: \mathcal B_{R,31}
+\mathscr D_{a} (L_{ij}) \frac{1}{L^{3}} \mathscr D^{a} (L) [-2 \Box_{\mathrm B}^{c}(L^{ij})
\\
&{}
+\frac{1}{L} \mathscr D^{b}(L^{ij}) \mathscr D_{b}(L)]
% b-032: \mathcal B_{R,32}
+\frac{64}{9} T_{ab} T_{cd} T^{ab} T^{cd}
% b-033: \mathcal B_{R,33}
+\frac{64}{3} T_{ab} T^{ab} D
% b-034: \mathcal B_{R,34}
-\frac{16}{3} T_{ab} T^{ab} N (g + \frac{27 N}{L^{2}})
\\
&{}
% b-035: \mathcal B_{R,35}
+16 T_{ab} T^{ab} \frac{1}{3 L} \Box_{\mathrm B}^{c} (L)
% b-036: \mathcal B_{R,36}
+16 T_{ab} \sqrt{2} \frac{1}{L} V^{b} [\frac{N}{L} \mathscr D^{a}(L)
-\mathscr D^{a}(N)]
% b-037: \mathcal B_{R,37}
+32 T_{ab} N \frac{1}{L^{2}} \mathscr D^{a} (E^{b})
\end{aligned}
```

<a id="b-038"></a>
<a id="b-039"></a>
<a id="b-040"></a>
<a id="b-041"></a>
<a id="b-042"></a>
<a id="b-043"></a>
<a id="b-044"></a>
<a id="b-045"></a>
<a id="b-046"></a>
<a id="b-047"></a>
<a id="b-048"></a>
<a id="b-049"></a>

```math
\begin{aligned}
\sum_{r=38}^{49} \mathcal B_{R,r}={}&
% b-038: \mathcal B_{R,38}
16 T_{ab} N \frac{1}{L^{2}} L^{ij} R^{ab}{}_{ij} (V)
% b-039: \mathcal B_{R,39}
+\sqrt{2} \frac{1}{L} V_{a} [\frac{1}{L} \mathscr D_{b}(L)[\mathscr D^{a}(E^{b})
\\
&{}
-2 \mathscr D^{b}(E^{a}) -L^{ij} R^{ba}{}_{ij}(V)] +\Box_{\mathrm B}^{c}(E^{a})
-16 N \mathscr D^{b}(T_{b}{}^{a}) +N \mathscr D^{b}(G_{b}{}^{a}) -\mathscr D^{b}\mathscr D^{a}(E_{b})
\\
&{}
-L^{ij} \mathscr D^{b}(R^{a}{}_{bij}(V)) +\frac{1}{L} \mathscr D^{a}(L) \mathscr D^{b}(E_{b})
-\mathscr D^{b}(L^{ij}) R^{a}{}_{bij}(V)]
% b-040: \mathcal B_{R,40}
+4 \mathscr D_{a} (L) N^{2} \frac{1}{L^{4}} \mathscr D^{a} (L)
\\
&{}
% b-041: \mathcal B_{R,41}
-4 \mathscr D_{a} (L) N \frac{1}{L^{3}} \mathscr D^{a} (N)
% b-042: \mathcal B_{R,42}
+16 D^{2}
% b-043: \mathcal B_{R,43}
-8 D N (g + \frac{3 N}{L^{2}})
% b-044: \mathcal B_{R,44}
+N^{3} (2 g + \frac{N}{L^{2}}) \frac{1}{L^{2}}
% b-045: \mathcal B_{R,45}
+8 D \frac{1}{L} \Box_{\mathrm B}^{c} (L)
\\
&{}
% b-046: \mathcal B_{R,46}
-2 N (g + \frac{2 N}{L^{2}}) \frac{1}{L} \Box_{\mathrm B}^{c} (L)
% b-047: \mathcal B_{R,47}
+2 N \frac{1}{L^{2}} \Box_{\mathrm B}^{c} (N)
% b-048: \mathcal B_{R,48}
+4 N^{2} \frac{1}{L^{2}} f_{a}{}^{a}
% b-049: \mathcal B_{R,49}
+\frac{1}{L^{2}} \Box_{\mathrm B}^{c} (L^{ij}) \Box_{\mathrm B}^{c} (L_{ij})
\end{aligned}
```
