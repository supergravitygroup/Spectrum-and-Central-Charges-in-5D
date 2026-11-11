# LOG building block: covariant core

This file gives the **covariant core** without explicit spinors. Hatted objects and full derivatives contain implicit two-fermion contributions; this core is not identical to the bosonic density.

[Building-block action](invariant.md) · [Shared definitions](../../common/fields_and_derivatives.md) · [Fermion order](../../common/fermion_order.md) · [Check scope](../../references/component_records/02_action_family.md)

Equation provenance is provided in the [source record](../../references/component_records/02_action_family.md), and checked SUSY identities are listed in the [technical index](../../common/action_family.md). These lists track the coefficients and fermion degree of the specified source action.

```math
\mathcal U_{\log}=\sum_{r=1}^{40} \mathcal U_{\log,r}.
```

Within each aligned sum, the indexed terms follow their original order; each term link points to the group containing that term.

<a id="u-001"></a>

```math
\begin{aligned}
\mathcal U_{\log,1}={}&
% u-001: \mathcal U_{\log,1}
C_{a} \widehat H_{bcd} [\frac{1}{248832} \widehat H_{efg}[\varepsilon^{defg}{}_{h}[27648 \mathcal D^{h}(\widehat H^{abc})
+7632 \widehat C^{abch} +504 \widehat C^{ahbc} -6480 \widehat C^{bhac}
\\
&{}
-6408 \widehat G^{ab} \widehat G^{ch} +19823 \widehat G^{ah} \widehat G^{bc}]
+5 \varepsilon^{efg}{}_{hm}[2725 \widehat H^{abc} \widehat H^{dhm}
\\
&{}
-2032 \widehat H^{abh} \widehat H^{cdm} -1247 \widehat H^{ahm} \widehat H^{bcd}]
+1152 \varepsilon^{bcdef}[7 \mathcal D^{a}\mathcal D^{g}(\sigma) -37 \mathcal D^{g}\mathcal D^{a}(\sigma)]
\\
&{}
-4752 \varepsilon^{ahefg} \widehat C^{b}{}_{h}{}^{cd} +23027 \varepsilon^{cdefg} \widehat G^{a}{}_{h} \widehat G^{hb}]
+\frac{1}{497664} \widehat G_{ef}[\widehat H^{a}{}_{gh}[-8770 \varepsilon^{efbcd} \widehat G^{gh}
\\
&{}
-92108 \varepsilon^{fhbcd} \widehat G^{eg} +23027 \varepsilon^{ghbcd} \widehat G^{ef}]
+4385 \widehat G_{gh}[3 \varepsilon^{efghd} \widehat H^{abc} +4 \varepsilon^{fhbcd} \widehat H^{aeg}]
\\
&{}
+2[13824 \varepsilon^{bcdf}{}_{g}[-\mathcal D^{a}(\widehat G^{eg})
-4 \mathcal D^{e}(\widehat G^{ag})] +6912 \varepsilon^{abcd}{}_{g}[4 \mathcal D^{e}(\widehat G^{fg})
\\
&{}
-\mathcal D^{g}(\widehat G^{ef})] -41472 \mathcal D^{g}(\widehat G^{a}{}_{g}) \varepsilon^{efbcd}
-13824 \mathcal D^{g}(\widehat G^{e}{}_{g}) \varepsilon^{afbcd} +26677 \widehat H^{aef} \widehat H^{bcd}]]
\\
&{}
+\frac{1}{576} \widehat G^{a}{}_{e}[32 \varepsilon^{bcd}{}_{fg}[-5 \mathcal D^{e}(\widehat G^{fg})
+3 \mathcal D^{f}(\widehat G^{eg})] -192 \mathcal D^{b}(\widehat H^{ecd})
\\
&{}
+64 \mathcal D^{e}(\widehat H^{bcd}) +53 \widehat C^{bced} -5 \widehat C^{ebcd}
+160 \mathcal D^{f}(\widehat G_{fg}) \varepsilon^{egbcd}] +\frac{1}{82944} \widehat H^{a}{}_{ef}[192 \varepsilon^{bcd}{}_{gh}[
\\
&{}
-18 \widehat C^{egfh} -11 \widehat C^{ghef}] +11520 \Box^c(\sigma) \varepsilon^{efbcd}
-26677 \widehat G^{bc} \widehat H^{efd} -53354 \widehat G^{eb} \widehat H^{fcd}]
\\
&{}
+\frac{1}{18} \mathcal D_{e}(\widehat H_{fgh})[-2 \varepsilon^{adfgh} \widehat H^{bce}
+\varepsilon^{aefgh} \widehat H^{bcd} -2 \varepsilon^{defgh} \widehat H^{abc}]
\\
&{}
+\frac{1}{576} \widehat G^{d}{}_{e}[-165 \widehat C^{abec} +133 \widehat C^{aebc}
-21 \widehat C^{bcae} -485 \widehat C^{ebac}] +\frac{1}{20736} \widehat G^{b}{}_{e}[27648 \mathcal D^{c}(\widehat H^{aed})
\\
&{}
-6912 \mathcal D^{e}(\widehat H^{acd}) +26677 \widehat H^{ac}{}_{f} \widehat H^{efd}]
+\frac{1}{1152} \widehat C_{efgh}[5 \varepsilon^{aefgh} \widehat H^{bcd}
\\
&{}
+6 \varepsilon^{efghd} \widehat H^{abc}] +\frac{1}{576} \widehat H^{cd}{}_{e}[
-192 \mathcal D^{e}(\widehat G^{ab}) +5 \varepsilon^{afghe} \widehat C^{b}{}_{fgh}]
+\frac{1}{6} \widehat H^{ad}{}_{e}[-10 \mathcal D^{b}(\widehat G^{ec})
\\
&{}
+\mathcal D^{e}(\widehat G^{bc})] +\frac{1}{6} \widehat G^{bc}[\mathcal D^{a}\mathcal D^{d}(\sigma)
+3 \mathcal D^{d}\mathcal D^{a}(\sigma)] +\frac{1}{9} \widehat G^{ab}[5 \mathcal D^{c}\mathcal D^{d}(\sigma)
\\
&{}
-3 \mathcal D^{e}(\widehat H^{cd}{}_{e})] +\varepsilon^{abcd}{}_{e}[\frac{2}{9} \Box^c\mathcal D^{e}(\sigma)
+\frac{L g^{2}}{18} \mathcal D^{e}(L) +\frac{g}{9} \mathcal D^{e}(N)
\\
&{}
-\frac{1}{9} \mathcal D^{e}\Box^c(\sigma) -\frac{55}{864} \mathcal D^{f}\mathcal D^{g}(\widehat H_{fg}{}^{e})]
+\frac{1}{864}[\varepsilon^{bcd}{}_{ef}[25 \mathcal D^{e}\mathcal D^{g}(\widehat H^{a}{}_{g}{}^{f})
\\
&{}
+72 \mathcal D^{g}(\widehat C^{ae}{}_{g}{}^{f}) +36 \mathcal D^{g}(\widehat C^{a}{}_{g}{}^{ef})
-55 \mathcal D^{g}\mathcal D^{e}(\widehat H^{a}{}_{g}{}^{f})] +\varepsilon^{cd}{}_{efg}[8 \mathcal D^{a}\mathcal D^{b}(\widehat H^{efg})
\\
&{}
+25 \mathcal D^{b}\mathcal D^{a}(\widehat H^{efg})] +3[3 \varepsilon^{ad}{}_{efg}[8 \mathcal D^{b}\mathcal D^{c}(\widehat H^{efg})
-11 \mathcal D^{e}\mathcal D^{f}(\widehat H^{bcg})] +16[-4 \mathcal D^{a}\mathcal D^{b}(\widehat G^{cd})
\\
&{}
+10 \mathcal D^{b}\mathcal D^{a}(\widehat G^{cd}) -2 \mathcal D^{b}\mathcal D^{c}(\widehat G^{ad})
+\mathcal D^{e}(\widehat G^{a}{}_{e}) \widehat H^{bcd} +6 \mathcal D^{e}(\widehat G_{e}{}^{b}) \widehat H^{acd}]]]]
\end{aligned}
```

<a id="u-002"></a>

```math
\begin{aligned}
\mathcal U_{\log,2}={}&
% u-002: \mathcal U_{\log,2}
\frac{1}{82944} C_{a} \widehat G_{bc} [\widehat G_{de}[\widehat G_{fg}[
-4408 \varepsilon^{acefg} \widehat G^{bd} +1102 \varepsilon^{adefg} \widehat G^{bc}
\\
&{}
-86015 \varepsilon^{cdefg} \widehat G^{ab}] +72[112 \varepsilon^{bcde}{}_{f}[\mathcal D^{a}\mathcal D^{f}(\sigma)
-4 \mathcal D^{f}\mathcal D^{a}(\sigma)] +\varepsilon^{ade}{}_{fg}[
\\
&{}
-\widehat C^{bcfg} -31 \widehat C^{bfcg}] +2[\varepsilon^{ace}{}_{fg}[5 \widehat C^{bdfg}
-41 \widehat C^{bfdg}] +168 \Box^c(\sigma) \varepsilon^{abcde}]]]
\\
&{}
+36[\widehat G^{a}{}_{d}[2 \varepsilon^{cd}{}_{efg}[-320 \mathcal D^{b}(\widehat H^{efg})
+9 \widehat C^{befg}] +3[\varepsilon^{bc}{}_{efg}[-128 \mathcal D^{d}(\widehat H^{efg})
\\
&{}
+25 \widehat C^{defg}] +896[2 \mathcal D^{b}(\widehat G^{dc}) -\mathcal D^{d}(\widehat G^{bc})]]]
+2 \widehat H^{a}{}_{de}[384 \mathcal D^{b}(\widehat H^{cde}) -19 \widehat C^{bcde}
\\
&{}
-16 \widehat C^{bdce} +59 \widehat C^{debc}] +128 \mathcal D_{d}(\widehat H_{efg})[
-\varepsilon^{acefg} \widehat G^{bd} +\varepsilon^{adefg} \widehat G^{bc}
\\
&{}
+\varepsilon^{cdefg} \widehat G^{ab}] +256 \widehat H^{ab}{}_{d}[4 \mathcal D^{c}\mathcal D^{d}(\sigma)
-7 \mathcal D^{d}\mathcal D^{c}(\sigma) +12 \mathcal D^{e}(\widehat H^{cd}{}_{e})]
\\
&{}
+\widehat C_{defg}[35 \varepsilon^{adefg} \widehat G^{bc} +12 \varepsilon^{defgc} \widehat G^{ab}]
+4[2 \varepsilon^{bc}{}_{def}[-5 \mathcal D^{a}\mathcal D^{d}(\widehat G^{ef})
\\
&{}
+23 \mathcal D^{d}\mathcal D^{a}(\widehat G^{ef}) +24 \mathcal D^{d}\mathcal D^{e}(\widehat G^{af})]
+8 \varepsilon^{ac}{}_{def}[-2 \mathcal D^{b}\mathcal D^{d}(\widehat G^{ef})
\\
&{}
+5 \mathcal D^{d}\mathcal D^{b}(\widehat G^{ef}) -9 \mathcal D^{d}\mathcal D^{e}(\widehat G^{bf})]
+4 \varepsilon^{abc}{}_{de}[-21 \Box^c(\widehat G^{de}) -5 \mathcal D^{d}\mathcal D^{f}(\widehat G_{f}{}^{e})
\\
&{}
-25 \mathcal D^{f}\mathcal D^{d}(\widehat G_{f}{}^{e})] -32 \mathcal D^{a}\mathcal D^{d}(\widehat H^{bc}{}_{d})
+160 \mathcal D^{b}\mathcal D^{d}(\widehat H^{ac}{}_{d}) -144 \mathcal D^{d}(\widehat C^{ab}{}_{d}{}^{c})
\\
&{}
-72 \mathcal D^{d}(\widehat C^{a}{}_{d}{}^{bc}) +32 \mathcal D^{d}\mathcal D^{a}(\widehat H^{bc}{}_{d})
-352 \mathcal D^{d}\mathcal D^{b}(\widehat H^{ac}{}_{d}) -384 \Box^c(\sigma) \widehat H^{abc}
\\
&{}
+384 \mathcal D^{d}(\widehat G^{ac}) \widehat G^{b}{}_{d} -96 \mathcal D^{d}(\widehat G^{a}{}_{d}) \widehat G^{bc}
-384 \mathcal D^{d}(\widehat G^{c}{}_{d}) \widehat G^{ab} -43 \varepsilon^{adefg} \widehat C^{b}{}_{def} \widehat G^{c}{}_{g}]]]
\end{aligned}
```

<a id="u-003"></a>
<a id="u-004"></a>
<a id="u-005"></a>
<a id="u-006"></a>

```math
\begin{aligned}
\sum_{r=3}^{6} \mathcal U_{\log,r}={}&
% u-003: \mathcal U_{\log,3}
C_{a} \mathcal D_{b} (\widehat H_{cde}) [\frac{1}{4608} \varepsilon^{cde}{}_{fg}[191 \mathcal D^{a}(\widehat H^{bfg})
-191 \mathcal D^{b}(\widehat H^{afg}) -561 \mathcal D^{f}(\widehat H^{abg})]
\\
&{}
+\frac{1}{1536} \varepsilon^{bcde}{}_{f}[-64 \mathcal D^{a}\mathcal D^{f}(\sigma)
+320 \mathcal D^{f}\mathcal D^{a}(\sigma) +241 \mathcal D^{g}(\widehat H^{a}{}_{g}{}^{f})]
\\
&{}
+\frac{1}{4608} \varepsilon^{acde}{}_{f}[1920 \mathcal D^{b}\mathcal D^{f}(\sigma)
-384 \mathcal D^{f}\mathcal D^{b}(\sigma) -431 \mathcal D^{g}(\widehat H_{g}{}^{bf})]
\\
&{}
+\varepsilon^{abcde}[-\frac{g (L^{2} g + 4 N)}{36} -\frac{5}{18} \Box^c(\sigma)]
+\frac{431}{1536} \mathcal D^{f}(\widehat H^{cd}{}_{g}) \varepsilon^{abe}{}_{f}{}^{g}]
% u-004: \mathcal U_{\log,4}
+\frac{1}{1536} C_{a} \mathcal D_{b} (\widehat G_{cd}) [\varepsilon^{bcd}{}_{ef}[
\\
&{}
-415 \mathcal D^{a}(\widehat G^{ef}) +113 \mathcal D^{e}(\widehat G^{af})]
+\varepsilon^{abd}{}_{ef}[1105 \mathcal D^{c}(\widehat G^{ef}) -2078 \mathcal D^{e}(\widehat G^{cf})]
\\
&{}
+1728 \mathcal D^{a}(\widehat H^{bcd}) -704 \mathcal D^{b}(\widehat H^{acd})
+2432 \mathcal D^{c}(\widehat H^{abd}) -353 \mathcal D^{b}(\widehat G_{ef}) \varepsilon^{aefcd}
\\
&{}
+525 \mathcal D^{e}(\widehat G_{ef}) \varepsilon^{afbcd}]
% u-005: \mathcal U_{\log,5}
+\frac{1}{864} C_{a} \widehat H^{a}{}_{bc} [2 \varepsilon^{c}{}_{defg}[67 \mathcal D^{b}\mathcal D^{d}(\widehat H^{efg})
\\
&{}
+44 \mathcal D^{d}\mathcal D^{b}(\widehat H^{efg})] +3[96 \Box^c(\widehat G^{bc})
-32 \mathcal D^{b}\mathcal D^{d}(\widehat G_{d}{}^{c}) -160 \mathcal D^{d}\mathcal D^{b}(\widehat G_{d}{}^{c})
\\
&{}
-11 \Box^c(\widehat H_{efg}) \varepsilon^{bcefg}]]
% u-006: \mathcal U_{\log,6}
+\frac{1}{12} C_{a} \mathcal D_{b} \mathcal D_{c} (\sigma) [6 \mathcal D^{a}(\widehat G^{bc})
+6 \mathcal D^{b}(\widehat G^{ac}) +6 \mathcal D^{c}(\widehat G^{ab})
\\
&{}
+\mathcal D^{a}(\widehat H_{def}) \varepsilon^{defbc}]
\end{aligned}
```

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
\sum_{r=7}^{17} \mathcal U_{\log,r}={}&
% u-007: \mathcal U_{\log,7}
C_{a} \widehat G^{a}{}_{b} [\frac{2}{3} \Box^c\mathcal D^{b}(\sigma)
-\frac{4 L g^{2}}{3} \mathcal D^{b}(L) -\frac{5 g}{3} \mathcal D^{b}(N)
-\frac{1}{3} \mathcal D^{b}\Box^c(\sigma) -\frac{1}{18} \mathcal D^{c}\mathcal D^{d}(\widehat H^{b}{}_{cd})
\\
&{}
+\frac{7}{144} \mathcal D^{c}\mathcal D^{d}(\widehat G_{ef}) \varepsilon^{b}{}_{cd}{}^{ef}]
% u-008: \mathcal U_{\log,8}
+\frac{1}{12} C_{a} \mathcal D_{b} (\widehat G^{b}{}_{c}) [3 \mathcal D^{a}\mathcal D^{c}(\sigma)
-15 \mathcal D^{c}\mathcal D^{a}(\sigma) +4 \mathcal D^{d}(\widehat H^{ac}{}_{d})]
\\
&{}
% u-009: \mathcal U_{\log,9}
+\frac{1}{12} C_{a} \mathcal D_{b} (\widehat H_{cd}{}^{b}) [7 \mathcal D^{a}(\widehat G^{cd})
-18 \mathcal D^{c}(\widehat G^{ad})]
% u-010: \mathcal U_{\log,10}
+C_{a} \mathcal D_{b} (\widehat G^{ab}) [-\frac{g (2 L^{2} g + 5 N)}{3}
-\frac{2}{3} \Box^c(\sigma)]
\\
&{}
% u-011: \mathcal U_{\log,11}
+\frac{1}{6} C_{a} \varepsilon^{a}{}_{bcde} \Box^c \mathcal D^{b} (\widehat H^{cde})
% u-012: \mathcal U_{\log,12}
-\frac{1}{12} C_{a} \varepsilon^{a}{}_{bcde} \widehat R^{bc}{}_{ij} (V) \widehat R^{deij} (V)
% u-013: \mathcal U_{\log,13}
+C_{a} g L^{ij} \mathcal D^{b} (\widehat R^{a}{}_{bij}(V))
\\
&{}
% u-014: \mathcal U_{\log,14}
+C_{a} g \mathcal D^{b} (L^{ij}) \widehat R^{a}{}_{bij} (V)
% u-015: \mathcal U_{\log,15}
+\widehat G_{ab} \widehat H_{cde} [\frac{1}{12} \widehat G_{fg}[-2 \varepsilon^{bgcde} \widehat G^{af}
\\
&{}
+\varepsilon^{fgcde} \widehat G^{ab}] +\frac{1}{3456} \varepsilon^{cde}{}_{fg}[225 \mathcal D^{f}(\widehat H^{abg})
-136 \widehat C^{afbg} -92 \widehat C^{fgab}] +\frac{7}{27} \varepsilon^{acde}{}_{f}[
\\
&{}
-\mathcal D^{b}\mathcal D^{f}(\sigma) +\mathcal D^{f}\mathcal D^{b}(\sigma)]
+\varepsilon^{abcde}[\frac{g (L^{2} g + 4 N)}{36} +\frac{1}{9} \Box^c(\sigma)]
+\frac{1}{6912}[-278 \mathcal D^{f}(\widehat H^{a}{}_{fg}) \varepsilon^{bcdeg}
\\
&{}
-267 \mathcal D^{f}(\widehat H^{cd}{}_{g}) \varepsilon^{abe}{}_{f}{}^{g}
-192 \widehat G^{ab} \widehat H^{cde} +1152 \widehat G^{ac} \widehat H^{bde}
-2304 \widehat G^{cd} \widehat H^{abe}]]
\\
&{}
% u-016: \mathcal U_{\log,16}
-\frac{1}{3} \widehat G_{ab} L^{ij} g \widehat R^{ab}{}_{ij} (V)
% u-017: \mathcal U_{\log,17}
+\frac{1}{144} \widehat G_{ab} \widehat G_{cd} [-96 \mathcal D^{a}(\widehat H^{bcd})
\\
&{}
+17 \widehat C^{abcd} +22 \widehat C^{acbd} +12 \mathcal D^{e}(\widehat G_{ef}) \varepsilon^{abcdf}
+9 \widehat G^{ab} \widehat G^{cd} -54 \widehat G^{ac} \widehat G^{bd}]
\end{aligned}
```

<a id="u-018"></a>
<a id="u-019"></a>
<a id="u-020"></a>
<a id="u-021"></a>
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

```math
\begin{aligned}
\sum_{r=18}^{31} \mathcal U_{\log,r}={}&
% u-018: \mathcal U_{\log,18}
\frac{1}{6912} \widehat G_{ab} \mathcal D_{c} (\widehat H_{def}) [456 \varepsilon^{bgdef} \widehat H^{ac}{}_{g}
-1129 \varepsilon^{gcdef} \widehat H^{ab}{}_{g}]
% u-019: \mathcal U_{\log,19}
+\frac{1}{3} \widehat G_{ab} \widehat H^{b}{}_{cd} [-2 \mathcal D^{a}(\widehat G^{cd})
\\
&{}
+\mathcal D^{c}(\widehat G^{ad})]
% u-020: \mathcal U_{\log,20}
+\frac{1}{432} \widehat G_{ab} \varepsilon^{b}{}_{cdef} [-27 \mathcal D^{a}(\widehat C^{cdef})
+112 \mathcal D^{a}\mathcal D^{c}(\widehat H^{def}) -27 \mathcal D^{c}(\widehat C^{adef})
\\
&{}
+8 \mathcal D^{c}\mathcal D^{a}(\widehat H^{def})]
% u-021: \mathcal U_{\log,21}
-\frac{3}{32} \widehat G_{ab} \varepsilon^{ab}{}_{cde} \mathcal D^{f} (\widehat C_{f}{}^{cde})
% u-022: \mathcal U_{\log,22}
+\frac{1}{3} \widehat G_{ab} \Box^c (\widehat G^{ab})
% u-023: \mathcal U_{\log,23}
+\frac{2}{9} \widehat G_{ab} \mathcal D^{a} \mathcal D^{c} (\widehat G^{b}{}_{c})
\\
&{}
% u-024: \mathcal U_{\log,24}
+\frac{1}{9} \widehat G_{ab} \mathcal D^{c} \mathcal D^{a} (\widehat G^{b}{}_{c})
% u-025: \mathcal U_{\log,25}
+\frac{1}{8} \widehat G_{ab} g (3 L^{2} g + 4 N) \widehat G^{ab}
% u-026: \mathcal U_{\log,26}
-\frac{1}{3} \widehat G_{ab} \mathcal D^{c} (\widehat G_{cd}) \widehat H^{abd}
% u-027: \mathcal U_{\log,27}
-\frac{4}{3} \widehat G_{ab} \mathcal D^{c} \mathcal D^{b} (\sigma) \widehat G^{a}{}_{c}
\\
&{}
% u-028: \mathcal U_{\log,28}
+\frac{563}{6912} \widehat G_{ab} \mathcal D^{b} (\widehat H_{cde}) \varepsilon^{fgcde} \widehat H^{a}{}_{fg}
% u-029: \mathcal U_{\log,29}
+\widehat H_{abc} [\widehat H^{abc}[\frac{g (L^{2} g - 2 N)}{12} +\frac{1}{9} \Box^c(\sigma)
\\
&{}
-\frac{1}{72} \widehat H^{def} \widehat H_{def}] +\frac{1}{72} \widehat H^{c}{}_{de}[11 \widehat C^{abde}
+10 \widehat C^{adbe}] +\varepsilon^{abc}{}_{de}[-\frac{1}{9} \Box^c(\widehat G^{de})
\\
&{}
+\frac{2}{27} \mathcal D^{d}\mathcal D^{f}(\widehat G_{f}{}^{e}) +\frac{1}{27} \mathcal D^{f}\mathcal D^{d}(\widehat G_{f}{}^{e})
-\frac{g}{18} L^{ij} \widehat R^{de}{}_{ij}(V)] +\frac{1}{36}[4 \Box^c(\widehat H^{abc})
\\
&{}
+4 \mathcal D^{a}\mathcal D^{d}(\widehat H^{bc}{}_{d}) +9 \mathcal D^{d}(\widehat C^{ab}{}_{d}{}^{c})
-16 \mathcal D^{d}\mathcal D^{a}(\widehat H^{bc}{}_{d}) +24 \mathcal D^{d}(\widehat H^{ebc}) \widehat H^{a}{}_{de}
\\
&{}
-12 \mathcal D^{d}\mathcal D^{c}(\sigma) \widehat H^{ab}{}_{d} -\mathcal D^{d}(\widehat G_{d}{}^{a}) \varepsilon^{bcefg} \widehat H_{efg}]]
% u-030: \mathcal U_{\log,30}
-\frac{1}{4} \mathcal D_{a} (L_{ij}) \mathcal D^{a} (L^{ij}) g^{2}
% u-031: \mathcal U_{\log,31}
+\frac{1}{72} \mathcal D_{a} (\widehat H_{bcd}) [\varepsilon^{bcd}{}_{ef}[
\\
&{}
-11 \mathcal D^{a}(\widehat G^{ef}) +14 \mathcal D^{e}(\widehat G^{af})]
+4[\mathcal D^{a}(\widehat H^{bcd}) -9 \mathcal D^{b}(\widehat H^{acd})
+3 \mathcal D^{e}(\widehat G_{ef}) \varepsilon^{fabcd}]]
\end{aligned}
```

<a id="u-032"></a>
<a id="u-033"></a>
<a id="u-034"></a>
<a id="u-035"></a>
<a id="u-036"></a>
<a id="u-037"></a>
<a id="u-038"></a>
<a id="u-039"></a>
<a id="u-040"></a>

```math
\begin{aligned}
\sum_{r=32}^{40} \mathcal U_{\log,r}={}&
% u-032: \mathcal U_{\log,32}
\frac{3}{4} \mathcal D_{a} \mathcal D_{b} (\sigma) [-2 \mathcal D^{a}\mathcal D^{b}(\sigma)
+2 \mathcal D^{c}(\widehat H_{c}{}^{ab}) -\mathcal D^{c}(\widehat G_{de}) \varepsilon_{c}{}^{deab}]
\\
&{}
% u-033: \mathcal U_{\log,33}
+\Box^c (\sigma) [\frac{g (13 L^{2} g + 16 N)}{6} +\frac{5}{6} \Box^c(\sigma)]
% u-034: \mathcal U_{\log,34}
+\frac{1}{6} \mathcal D_{a} (\widehat G_{bc}) [-2 \mathcal D^{a}(\widehat G^{bc})
+5 \mathcal D^{b}(\widehat G^{ac})]
\\
&{}
% u-035: \mathcal U_{\log,35}
-\frac{1}{2} \mathcal D_{a} (L) g^{2} \mathcal D^{a} (L)
% u-036: \mathcal U_{\log,36}
+\frac{1}{24} g^{2} (5 L^{4} g^{2} + 16 L^{2} N g - 4 N^{2})
% u-037: \mathcal U_{\log,37}
-\frac{1}{2} L g^{2} \Box^c (L)
% u-038: \mathcal U_{\log,38}
-g \Box^c (N)
\\
&{}
% u-039: \mathcal U_{\log,39}
+\frac{1}{6} \mathcal D^{a} (\widehat H_{abc}) \mathcal D^{d} (\widehat H^{bc}{}_{d})
% u-040: \mathcal U_{\log,40}
+\frac{1}{6} \widehat R^{abij} (V) \widehat R_{abij} (V)
\end{aligned}
```
