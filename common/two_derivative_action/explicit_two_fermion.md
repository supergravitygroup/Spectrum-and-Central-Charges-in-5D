# Two-derivative building block: explicit two-fermion blocks

This file gives all blocks carrying **two explicit fermions**. The physical two-fermion density combines them with the implicit two-fermion contribution of the covariant core.

[Building-block action](invariant.md) · [Shared definitions](../fields_and_derivatives.md) · [Fermion order](../fermion_order.md) · [Check scope](../../references/component_records/02_action_family.md)

Equation provenance is provided in the [source record](../../references/component_records/02_action_family.md), and checked SUSY identities are listed in the [technical index](../action_family.md). These lists track the coefficients and fermion degree of the specified source action.

```math
\mathcal V_{2}=\sum_{r=1}^{33} \mathcal V_{2,r}.
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
<a id="v-029"></a>
<a id="v-030"></a>
<a id="v-031"></a>
<a id="v-032"></a>
<a id="v-033"></a>

```math
\begin{aligned}
\mathcal V_{2}={}&
% v-001: \mathcal V_{2,1}
-2 \bar\psi_{a}{}^{i} \gamma^{ab} \mathcal D_{b} (\varphi^{j}) L_{ij} i \frac{1}{L}
% v-002: \mathcal V_{2,2}
-\bar\psi_{a}{}^{i} \gamma^{ab} \psi_{b}{}^{j} L_{ij} i g
% v-003: \mathcal V_{2,3}
-\bar\psi_{a}{}^{i} \gamma^{ab} \psi_{b}{}^{j} L_{ij} i N \frac{1}{L}
\\
&{}
% v-004: \mathcal V_{2,4}
+2 \bar\psi_{a}{}^{i} \gamma^{ab} \varphi^{j} \frac{1}{L^{3}} L_{j}{}^{k} \mathcal D_{b} (L_{kl}) L_{i}{}^{l} i
% v-005: \mathcal V_{2,5}
-8 \bar\psi_{a}{}^{i} \gamma^{a} \chi_{i} L
% v-006: \mathcal V_{2,6}
-2 \bar\psi_{a}{}^{i} \gamma^{a} \varphi_{i} g
% v-007: \mathcal V_{2,7}
-\bar\psi_{a}{}^{i} \gamma^{a} \varphi_{i} N \frac{1}{L}
\\
&{}
% v-008: \mathcal V_{2,8}
-\bar\psi_{a}{}^{i} \gamma^{ba} \varphi_{i} \frac{1}{L} E_{b} i
% v-009: \mathcal V_{2,9}
+2 \bar\psi_{a}{}^{i} \gamma^{bc} \mathcal D_{c} (\varphi_{i}) i \frac{1}{L} E^{a}{}_{b}
% v-010: \mathcal V_{2,10}
-2 \bar\psi_{a}{}^{i} \gamma^{bc} \varphi^{j} L_{ij} \frac{1}{L} T_{de} \varepsilon^{a}{}_{bc}{}^{de} i
\\
&{}
% v-011: \mathcal V_{2,11}
+2 \bar\psi_{a}{}^{i} \gamma^{bc} \varphi^{j} L_{ij} i \frac{1}{L^{3}} E^{a}{}_{b} E_{c}
% v-012: \mathcal V_{2,12}
+2 \bar\psi_{a}{}^{i} \gamma^{bc} \varphi^{j} \frac{1}{L^{3}} L_{j}{}^{k} \mathcal D_{c} (L_{ik}) i E^{a}{}_{b}
% v-013: \mathcal V_{2,13}
-2 \bar\psi_{a}{}^{i} \gamma^{bc} \varphi_{i} \frac{1}{L} T_{de} \varepsilon_{bc}{}^{de}{}_{f} i E^{fa}
\\
&{}
% v-014: \mathcal V_{2,14}
-16 \bar\psi_{a}{}^{i} \gamma^{b} \chi^{j} \frac{1}{L} L_{ij} E^{a}{}_{b}
% v-015: \mathcal V_{2,15}
+8 \bar\psi_{a}{}^{i} \gamma^{b} \varphi^{j} L_{ij} \frac{1}{L} T^{a}{}_{b}
% v-016: \mathcal V_{2,16}
+2 \bar\psi_{a}{}^{i} \gamma^{b} \varphi^{j} L_{ij} N \frac{1}{L^{3}} E^{a}{}_{b}
\\
&{}
% v-017: \mathcal V_{2,17}
-8 \bar\psi_{a}{}^{i} \gamma^{b} \varphi_{i} \frac{1}{L} T_{bc} E^{ca}
% v-018: \mathcal V_{2,18}
-2 \bar\psi_{a}{}^{i} \mathcal D^{a} (\varphi^{j}) L_{ij} i \frac{1}{L}
% v-019: \mathcal V_{2,19}
+2 \bar\psi_{a}{}^{i} \mathcal D^{b} (\varphi_{i}) i \frac{1}{L} E^{a}{}_{b}
% v-020: \mathcal V_{2,20}
+N \frac{1}{L} \bar\psi_{a}{}^{i} \psi_{bi} i E^{ab}
\\
&{}
% v-021: \mathcal V_{2,21}
+2 \bar\psi_{a}{}^{i} \varphi^{j} \frac{1}{L^{3}} L_{j}{}^{k} \mathcal D_{b} (L_{ik}) i E^{ab}
% v-022: \mathcal V_{2,22}
+2 \bar\psi_{a}{}^{i} \varphi^{j} \frac{1}{L^{3}} L_{j}{}^{k} \mathcal D^{a} (L_{kl}) L_{i}{}^{l} i
% v-023: \mathcal V_{2,23}
-2 \bar\psi_{a}{}^{i} \varphi^{j} L_{ij} \frac{1}{L^{3}} E_{b} i E^{ba}
\\
&{}
% v-024: \mathcal V_{2,24}
+\bar\psi_{a}{}^{i} \varphi_{i} \frac{1}{L} E^{a} i
% v-025: \mathcal V_{2,25}
+32 \frac{1}{L} \bar\varphi^{i} \chi^{j} L_{ij} i
% v-026: \mathcal V_{2,26}
+4 \bar\varphi^{i} \gamma^{ab} \varphi_{i} \frac{1}{L} T_{ab} i
% v-027: \mathcal V_{2,27}
-4 \frac{1}{L^{2}} \bar\varphi^{i} \gamma^{a} \mathcal D^{b} (\varphi^{j}) L_{ij} \frac{1}{L} E_{ab}
\\
&{}
% v-028: \mathcal V_{2,28}
+2 \bar\varphi^{i} \gamma^{a} \mathcal D_{a} (\varphi_{i}) \frac{1}{L}
% v-029: \mathcal V_{2,29}
-6 \frac{1}{L^{2}} \bar\varphi^{i} \gamma^{a} \varphi^{j} L_{ij} \frac{1}{L^{2}} \mathcal D_{b} (L) E^{b}{}_{a}
% v-030: \mathcal V_{2,30}
+2 \frac{1}{L^{2}} \bar\varphi^{i} \gamma^{a} \varphi^{j} \frac{1}{L} L_{j}{}^{k} \mathcal D_{a} (L_{ik})
\\
&{}
% v-031: \mathcal V_{2,31}
-2 \frac{1}{L^{2}} \bar\varphi^{i} \gamma^{a} \varphi^{j} \frac{1}{L} \mathcal D_{b} (L_{ij}) E_{a}{}^{b}
% v-032: \mathcal V_{2,32}
-4 \bar\varphi^{i} \varphi^{j} L_{ij} i N \frac{1}{2 L^{3}}
% v-033: \mathcal V_{2,33}
+\bar\varphi^{i} \widehat R_{abi} (Q) i \frac{1}{L} E^{ab}
\end{aligned}
```
