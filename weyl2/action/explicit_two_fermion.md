# Weyl-squared building block: explicit two-fermion blocks

This file gives all blocks carrying **two explicit fermions**. The physical two-fermion density combines them with the implicit two-fermion contribution of the covariant core.

[Building-block action](invariant.md) · [Shared definitions](../../common/fields_and_derivatives.md) · [Fermion order](../../common/fermion_order.md) · [Check scope](../../references/component_records/02_action_family.md)

Equation provenance is provided in the [source record](../../references/component_records/02_action_family.md), and checked SUSY identities are listed in the [technical index](../../common/action_family.md). These lists track the coefficients and fermion degree of the specified source action.

```math
\mathcal V_{W}=\sum_{r=1}^{62} \mathcal V_{W,r}.
```

Within each aligned sum, the indexed terms follow their original order; each term link points to the group containing that term.

<a id="v-001"></a>
<a id="v-002"></a>
<a id="v-003"></a>
<a id="v-004"></a>
<a id="v-005"></a>
<a id="v-006"></a>
<a id="v-007"></a>
<a id="v-008"></a>
<a id="v-009"></a>
<a id="v-010"></a>
<a id="v-011"></a>
<a id="v-012"></a>
<a id="v-013"></a>
<a id="v-014"></a>
<a id="v-015"></a>
<a id="v-016"></a>
<a id="v-017"></a>
<a id="v-018"></a>
<a id="v-019"></a>
<a id="v-020"></a>
<a id="v-021"></a>
<a id="v-022"></a>
<a id="v-023"></a>
<a id="v-024"></a>
<a id="v-025"></a>
<a id="v-026"></a>
<a id="v-027"></a>
<a id="v-028"></a>

```math
\begin{aligned}
\sum_{r=1}^{28} \mathcal V_{W,r}={}&
% v-001: \mathcal V_{W,1}
-\frac{128}{3} i g L_{ij} \bar\chi^{i} \chi^{j}
% v-002: \mathcal V_{W,2}
-\frac{128}{3} i C_{a} \bar\chi^{i} \gamma^{ab} \mathcal D_{b} (\chi_{i})
% v-003: \mathcal V_{W,3}
-\frac{256}{3} \bar\chi^{i} \gamma^{a} \mathcal D_{a} (\chi_{i})
% v-004: \mathcal V_{W,4}
+\frac{16}{3} \bar\chi^{i} \gamma^{a} \widehat R_{bci} (Q) [3 C^{b} T_{a}{}^{c}
\\
&{}
-C_{a} T^{bc}]
% v-005: \mathcal V_{W,5}
-8 i C^{b} \bar\chi^{i} \mathcal D^{a} (\widehat R_{bai}(Q))
% v-006: \mathcal V_{W,6}
+\frac{160}{3} i T^{ab} \bar\chi^{i} \widehat R_{abi} (Q)
% v-007: \mathcal V_{W,7}
-\frac{8}{3} \bar\psi_{a}{}^{i} \chi^{j} i C_{b} \widehat R^{ba}{}_{ij} (V)
\\
&{}
% v-008: \mathcal V_{W,8}
+\frac{32}{3} \bar\psi_{a}{}^{i} \chi_{i} [-i \mathcal D^{b}(T_{b}{}^{a})
+i C_{b} \mathcal D^{c}(T_{de}) \varepsilon^{b}{}_{c}{}^{dea}]
% v-009: \mathcal V_{W,9}
-\frac{8}{3} \bar\psi_{a}{}^{i} \gamma^{ab} \chi^{j} i C_{c} \widehat R^{c}{}_{bij} (V)
\\
&{}
% v-010: \mathcal V_{W,10}
+4 \bar\psi_{a}{}^{i} \gamma^{ab} \mathcal D_{b} (\widehat R_{cdi}(Q)) i T^{cd}
% v-011: \mathcal V_{W,11}
+\frac{4}{3} \bar\psi_{a}{}^{i} \gamma^{ab} \psi_{b}{}^{j} \widehat R_{cdij} (V) i T^{cd}
% v-012: \mathcal V_{W,12}
+\frac{64}{3} \bar\psi_{a}{}^{i} \gamma^{a} \chi_{i} D
\\
&{}
% v-013: \mathcal V_{W,13}
-\frac{32}{3} \bar\psi_{a}{}^{i} \gamma^{a} \chi_{i} C_{b} \mathcal D^{c} (T^{b}{}_{c})
% v-014: \mathcal V_{W,14}
+\frac{512}{9} \bar\psi_{a}{}^{i} \gamma^{a} \chi_{i} T^{bc} T_{bc}
% v-015: \mathcal V_{W,15}
-\frac{64}{3} C_{c} T^{c}{}_{b} \bar\psi_{a}{}^{i} \gamma^{a} \mathcal D^{b} (\chi_{i})
\\
&{}
% v-016: \mathcal V_{W,16}
-4 C_{d} \bar\psi_{a}{}^{i} \gamma^{a} \mathcal D^{b} (\widehat R_{cbi}(Q)) T^{dc}
% v-017: \mathcal V_{W,17}
-4 \bar\psi_{a}{}^{i} \gamma^{a} \mathcal D^{b} (\widehat R_{cdi}(Q)) C_{b} T^{cd}
% v-018: \mathcal V_{W,18}
-2 \bar\psi_{a}{}^{i} \gamma^{a} \widehat R_{bci} (Q) C_{d} \mathcal D^{b} (T^{dc})
\\
&{}
% v-019: \mathcal V_{W,19}
+\frac{1}{4} \bar\psi_{a}{}^{i} \gamma^{a} \widehat R_{bc}{}^{j} (Q) \widehat R^{bc}{}_{ij} (V)
% v-020: \mathcal V_{W,20}
+\bar\psi_{a}{}^{i} \gamma^{ba} \chi_{i} C_{b} [-\frac{64 i D}{3} -\frac{512 i}{9} T^{cd} T_{cd}]
% v-021: \mathcal V_{W,21}
+\frac{32}{3} \bar\psi_{a}{}^{i} \gamma^{ba} \chi_{i} i \mathcal D^{c} (T_{cb})
\\
&{}
% v-022: \mathcal V_{W,22}
-\frac{64}{3} i T_{bc} \bar\psi_{a}{}^{i} \gamma^{ba} \mathcal D^{c} (\chi_{i})
% v-023: \mathcal V_{W,23}
-4 \bar\psi_{a}{}^{i} \gamma^{ba} \mathcal D^{c} (\widehat R_{dci}(Q)) i T_{b}{}^{d}
% v-024: \mathcal V_{W,24}
+\frac{1}{8} \bar\psi_{a}{}^{i} \gamma^{ba} \widehat R_{cdi} (Q) C_{e} i \widehat C^{cde}{}_{b}
\\
&{}
% v-025: \mathcal V_{W,25}
-\frac{8}{3} \bar\psi_{a}{}^{i} \gamma^{ba} \widehat R_{cdi} (Q) C_{e} i T^{cd} T^{e}{}_{b}
% v-026: \mathcal V_{W,26}
-2 \bar\psi_{a}{}^{i} \gamma^{ba} \widehat R_{cdi} (Q) i \mathcal D^{c} (T_{b}{}^{d})
\\
&{}
% v-027: \mathcal V_{W,27}
-\frac{1}{4} \bar\psi_{a}{}^{i} \gamma^{ba} \widehat R_{cd}{}^{j} (Q) C_{b} i \widehat R^{cd}{}_{ij} (V)
% v-028: \mathcal V_{W,28}
+\frac{2}{3} \bar\psi_{a}{}^{i} \gamma^{bc} \chi^{j} [4 i C_{b} \widehat R^{a}{}_{cij}(V)
+i \varepsilon^{a}{}_{bcde} \widehat R^{de}{}_{ij}(V)]
\end{aligned}
```

<a id="v-029"></a>
<a id="v-030"></a>
<a id="v-031"></a>
<a id="v-032"></a>
<a id="v-033"></a>
<a id="v-034"></a>
<a id="v-035"></a>
<a id="v-036"></a>
<a id="v-037"></a>
<a id="v-038"></a>
<a id="v-039"></a>
<a id="v-040"></a>
<a id="v-041"></a>
<a id="v-042"></a>
<a id="v-043"></a>
<a id="v-044"></a>
<a id="v-045"></a>

```math
\begin{aligned}
\sum_{r=29}^{45} \mathcal V_{W,r}={}&
% v-029: \mathcal V_{W,29}
\frac{16}{3} \bar\psi_{a}{}^{i} \gamma^{bc} \chi_{i} [C_{d}[\varepsilon_{bc}{}^{d}{}_{ef}[i \mathcal D^{a}(T^{ef})
+2 i \mathcal D^{e}(T^{fa})] +\varepsilon^{a}{}_{bcef}[-i \mathcal D^{d}(T^{ef})
\\
&{}
+2 i \mathcal D^{e}(T^{df})] -i \mathcal D^{e}(T_{ef}) \varepsilon^{dfa}{}_{bc}]
+2[-i \mathcal D^{a}(T_{bc}) +2 i \mathcal D_{b}(T^{a}{}_{c})]]
\\
&{}
% v-030: \mathcal V_{W,30}
+\frac{32}{3} i C_{e} T_{fd} \varepsilon^{efa}{}_{bc} \bar\psi_{a}{}^{i} \gamma^{bc} \mathcal D^{d} (\chi_{i})
% v-031: \mathcal V_{W,31}
+2 \bar\psi_{a}{}^{i} \gamma^{bc} \mathcal D^{d} (\widehat R_{edi}(Q)) C_{f} \varepsilon^{a}{}_{bc}{}^{f}{}_{g} i T^{ge}
\\
&{}
% v-032: \mathcal V_{W,32}
-2 \bar\psi_{a}{}^{i} \gamma^{bc} \mathcal D^{d} (\widehat R_{efi}(Q)) C_{g} \varepsilon^{a}{}_{bcd}{}^{g} i T^{ef}
% v-033: \mathcal V_{W,33}
-\frac{2}{3} \bar\psi_{a}{}^{i} \gamma^{bc} \psi_{d}{}^{j} C_{e} \widehat R_{fgij} (V) \varepsilon^{a}{}_{bc}{}^{de} i T^{fg}
\\
&{}
% v-034: \mathcal V_{W,34}
+\frac{1}{8} \bar\psi_{a}{}^{i} \gamma^{bc} \widehat R_{dei} (Q) C_{b} i \widehat C^{dea}{}_{c}
% v-035: \mathcal V_{W,35}
-\frac{8}{3} \bar\psi_{a}{}^{i} \gamma^{bc} \widehat R_{dei} (Q) C_{b} i T^{a}{}_{c} T^{de}
\\
&{}
% v-036: \mathcal V_{W,36}
+\bar\psi_{a}{}^{i} \gamma^{bc} \widehat R_{dei} (Q) C_{f} \varepsilon^{a}{}_{bc}{}^{f}{}_{g} i \mathcal D^{d} (T^{ge})
% v-037: \mathcal V_{W,37}
+\frac{1}{32} \bar\psi_{a}{}^{i} \gamma^{bc} \widehat R_{dei} (Q) \varepsilon^{a}{}_{bcfg} i \widehat C^{defg}
\\
&{}
% v-038: \mathcal V_{W,38}
-\frac{2}{3} \bar\psi_{a}{}^{i} \gamma^{bc} \widehat R_{dei} (Q) \varepsilon^{a}{}_{bcfg} i T^{de} T^{fg}
% v-039: \mathcal V_{W,39}
+\frac{4}{3} \bar\psi_{a}{}^{i} \gamma^{b} \chi^{j} [-2 \widehat R^{a}{}_{bij}(V)
-C_{c} \varepsilon^{ca}{}_{bde} \widehat R^{de}{}_{ij}(V)]
\\
&{}
% v-040: \mathcal V_{W,40}
+\frac{32}{3} \bar\psi_{a}{}^{i} \gamma^{b} \chi_{i} [2 C_{c}[-\mathcal D^{a}(T^{c}{}_{b})
+\mathcal D^{c}(T^{a}{}_{b}) +\mathcal D_{b}(T^{ca})] -C_{b} \mathcal D^{c}(T_{c}{}^{a})
-\mathcal D^{c}(T_{de}) \varepsilon_{c}{}^{dea}{}_{b}]
\\
&{}
% v-041: \mathcal V_{W,41}
+4 \bar\psi_{a}{}^{i} \gamma^{b} \mathcal D^{a} (\widehat R_{cdi}(Q)) C_{b} T^{cd}
% v-042: \mathcal V_{W,42}
+\frac{64}{3} C_{b} T^{a}{}_{c} \bar\psi_{a}{}^{i} \gamma^{b} \mathcal D^{c} (\chi_{i})
% v-043: \mathcal V_{W,43}
+4 \bar\psi_{a}{}^{i} \gamma^{b} \mathcal D^{c} (\widehat R_{dci}(Q)) C_{b} T^{ad}
\\
&{}
% v-044: \mathcal V_{W,44}
-\frac{1}{16} \bar\psi_{a}{}^{i} \gamma^{b} \widehat R_{cdi} (Q) C_{e} \varepsilon^{a}{}_{b}{}^{e}{}_{fg} \widehat C^{cdfg}
% v-045: \mathcal V_{W,45}
+\frac{4}{3} \bar\psi_{a}{}^{i} \gamma^{b} \widehat R_{cdi} (Q) C_{e} \varepsilon^{a}{}_{b}{}^{e}{}_{fg} T^{cd} T^{fg}
\end{aligned}
```

<a id="v-046"></a>
<a id="v-047"></a>
<a id="v-048"></a>
<a id="v-049"></a>
<a id="v-050"></a>
<a id="v-051"></a>
<a id="v-052"></a>
<a id="v-053"></a>
<a id="v-054"></a>
<a id="v-055"></a>
<a id="v-056"></a>
<a id="v-057"></a>
<a id="v-058"></a>
<a id="v-059"></a>
<a id="v-060"></a>
<a id="v-061"></a>
<a id="v-062"></a>

```math
\begin{aligned}
\sum_{r=46}^{62} \mathcal V_{W,r}={}&
% v-046: \mathcal V_{W,46}
2 \bar\psi_{a}{}^{i} \gamma^{b} \widehat R_{cdi} (Q) C_{b} \mathcal D^{c} (T^{ad})
% v-047: \mathcal V_{W,47}
-\frac{1}{8} \bar\psi_{a}{}^{i} \gamma^{b} \widehat R_{cdi} (Q) \widehat C^{cda}{}_{b}
% v-048: \mathcal V_{W,48}
+\frac{8}{3} \bar\psi_{a}{}^{i} \gamma^{b} \widehat R_{cdi} (Q) T^{a}{}_{b} T^{cd}
\\
&{}
% v-049: \mathcal V_{W,49}
+4 \bar\psi_{a}{}^{i} \mathcal D^{a} (\widehat R_{bci}(Q)) i T^{bc}
% v-050: \mathcal V_{W,50}
+\frac{64}{3} i T^{a}{}_{b} \bar\psi_{a}{}^{i} \mathcal D^{b} (\chi_{i})
% v-051: \mathcal V_{W,51}
+4 \bar\psi_{a}{}^{i} \mathcal D^{b} (\widehat R_{cbi}(Q)) i T^{ac}
\\
&{}
% v-052: \mathcal V_{W,52}
-\frac{1}{8} \bar\psi_{a}{}^{i} \widehat R_{bci} (Q) C_{d} i \widehat C^{bcda}
% v-053: \mathcal V_{W,53}
+\frac{8}{3} \bar\psi_{a}{}^{i} \widehat R_{bci} (Q) C_{d} i T^{bc} T^{da}
% v-054: \mathcal V_{W,54}
+2 \bar\psi_{a}{}^{i} \widehat R_{bci} (Q) i \mathcal D^{b} (T^{ac})
\\
&{}
% v-055: \mathcal V_{W,55}
-8 i C^{b} \overline{\mathcal D^{a}(\chi^{i})} \widehat R_{bai} (Q)
% v-056: \mathcal V_{W,56}
+\frac{3}{4} \overline{\widehat R_{ab}{}^{i}(Q)} \gamma^{c} \mathcal D_{c} (\widehat R^{ab}{}_{i}(Q))
% v-057: \mathcal V_{W,57}
-\overline{\widehat R_{ab}{}^{i}(Q)} \gamma^{c} \widehat R_{d}{}^{b}{}_{i} (Q) C_{c} T^{ad}
\\
&{}
% v-058: \mathcal V_{W,58}
+3 \overline{\widehat R_{ab}{}^{i}(Q)} \gamma^{c} \widehat R_{d}{}^{b}{}_{i} (Q) C^{a} T_{c}{}^{d}
% v-059: \mathcal V_{W,59}
-\frac{3}{2} i C^{c} \overline{\widehat R_{ab}{}^{i}(Q)} \mathcal D^{a} (\widehat R_{c}{}^{b}{}_{i}(Q))
% v-060: \mathcal V_{W,60}
+\frac{1}{2} i C_{c} \overline{\widehat R_{ab}{}^{i}(Q)} \mathcal D^{c} (\widehat R^{ab}{}_{i}(Q))
\\
&{}
% v-061: \mathcal V_{W,61}
-\frac{1}{8} i g L_{ij} \overline{\widehat R_{ab}{}^{i}(Q)} \widehat R^{abj} (Q)
% v-062: \mathcal V_{W,62}
-2 \overline{\widehat R_{ab}{}^{i}(Q)} \widehat R_{c}{}^{b}{}_{i} (Q) i T^{ac}
\end{aligned}
```
