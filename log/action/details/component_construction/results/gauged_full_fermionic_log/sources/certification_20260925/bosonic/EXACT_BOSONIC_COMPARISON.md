# Exact bosonic LOG comparison: displayed equations

<!-- ASSERT_CONVENTION: metric_signature=mostly-plus -->

This is the readable equation companion to [the certification report](../../../../../../../../../references/source_evidence/log/derivations/bosonic.md). It is generated from the actual saved polynomials and the independently transcribed comparison target. All terms are zero-fermion terms. Here only, $`\nabla_a`$ denotes the ordinary torsion-free bosonic Lorentz/SU(2) derivative obtained after evaluating the full covariant derivatives on the target gauge slice. It is **not** a new definition of the full $`\mathcal D_a`$ used in the active multiplet documents.

The independent linear-compensator fields are $`L_c^{ij},N_c,E_c^a`$. Its $`SU(2)`$ gauge orientation is understood; $`\nabla L_c`$ still contains the $`SU(2)`$ connection. The conventional bosonic dependent field is $`f_{ab}=-R_{ab}/6+\eta_{ab}R/48`$ and $`f^a{}_a=-R/16`$. $`R(M)_{abcd}`$ is the traceless bosonic Weyl curvature in this convention. In particular $`f_{ab}=f_{ba}`$ is used **only** on the zero-fermion body.

## Actual triplet and scalar before the dilaton-Weyl substitutions

These expressions were freshly rebuilt from the original calculated full-covariant component polynomials, retaining the bosonic contributions of the connection terms before gauge fixing. Their terms were not obtained by differentiating the comparison action.

```math
\begin{aligned}
L_{\log}^{ij}|_0={}&\frac{16}{3}V{}^{abij}T{}_{ab}-12DgL_c{}^{ij}-V{}^{abij}G{}_{ab} \\
&-g\big(\nabla^2 L_c{}^{ij}\big)-2gL_c{}^{ij}f{}^{a}{}_{a}-8gL_c{}^{ij}T^2 \\
&+\frac{1}{4}gL_c{}^{ij}G^2-\frac{1}{4}g^3L_c{}^{ij}L_c{}^{kl}L_c{}_{kl}
\end{aligned}\tag{BC-01}
```

```math
\begin{aligned}
N_{\log}|_0={}&\frac{1}{6}V{}^{abij}V{}_{abij}-\frac{88}{9}R(M){}^{abcd}T{}_{ab}T{}_{cd}-\frac{80}{9}R(M){}^{abcd}T{}_{ac}T{}_{bd} \\
&+\frac{10720}{27}(T^2)^{2}-\frac{256}{3}T{}^{ab}T{}^{cd}\big(\nabla^{e}T{}_{e}{}^{f}\big)\epsilon{}_{abcdf}+\frac{736}{9}DT^2 \\
&+\frac{3}{2}\big(\nabla^{a}R(M){}_{a}{}^{bcd}\big)T{}^{ef}\epsilon{}_{bcdef}+\big(\nabla^{a}R(M){}^{bcde}\big)T{}_{b}{}^{f}\epsilon{}_{acdef}+\big(\nabla^{a}R(M){}^{bcde}\big)T{}_{a}{}^{f}\epsilon{}_{bcdef} \\
&+\frac{512}{9}T{}^{ab}\big(\nabla_{a}\nabla^{c}T{}_{bc}\big)-\frac{512}{9}f{}^{ab}T{}_{a}{}^{c}T{}_{bc}-\frac{208}{3}T{}^{ab}\big(\nabla^2 T{}_{ab}\big) \\
&-\frac{944}{9}f{}^{a}{}_{a}T^2-\frac{128}{9}T{}^{ab}\big(\nabla^{c}\nabla_{a}T{}_{bc}\big)-\frac{8}{3}D^{2} \\
&+\frac{64}{3}\big(\nabla^{a}T{}^{bc}\big)\big(\nabla_{b}T{}_{ac}\big)-\frac{176}{3}\big(\nabla^{a}T{}^{bc}\big)\big(\nabla_{a}T{}_{bc}\big)+64\big(\nabla^{a}T{}_{a}{}^{b}\big)\big(\nabla^{c}T{}_{bc}\big) \\
&-3Dg^2L_c{}^{ij}L_c{}_{ij}-8Df{}^{a}{}_{a}-\frac{1}{2}gL_c{}^{ij}V{}^{ab}{}_{ij}G{}_{ab} \\
&+\frac{7}{6}R(M){}^{abcd}G{}_{ab}T{}_{cd}+\frac{1}{3}R(M){}^{abcd}G{}_{ac}T{}_{bd}+\frac{563}{36}G{}^{ab}T{}^{cd}\big(\nabla_{a}T{}^{ef}\big)\epsilon{}_{bcdef} \\
&-\frac{139}{18}G{}^{ab}T{}_{a}{}^{c}\big(\nabla^{d}T{}^{ef}\big)\epsilon{}_{bcdef}+\frac{38}{3}G{}^{ab}T{}^{cd}\big(\nabla^{e}T{}_{a}{}^{f}\big)\epsilon{}_{bcdef}-\frac{361}{36}G{}^{ab}T{}^{cd}\big(\nabla^{e}T{}_{e}{}^{f}\big)\epsilon{}_{abcdf} \\
&+\frac{89}{18}G{}^{ab}T{}^{cd}\big(\nabla^{e}T{}_{c}{}^{f}\big)\epsilon{}_{abdef}-\frac{25}{2}G{}^{ab}T{}^{cd}\big(\nabla_{c}T{}^{ef}\big)\epsilon{}_{abdef}-\frac{9}{32}\big(\nabla^{a}R(M){}_{a}{}^{bcd}\big)G{}^{ef}\epsilon{}_{bcdef} \\
&-\frac{3}{16}\big(\nabla^{a}R(M){}^{bcde}\big)G{}_{b}{}^{f}\epsilon{}_{acdef}-\frac{3}{16}\big(\nabla^{a}R(M){}^{bcde}\big)G{}_{a}{}^{f}\epsilon{}_{bcdef}+\frac{16}{3}G{}^{ab}\big(\nabla_{a}\nabla^{c}T{}_{bc}\big) \\
&+\frac{16}{3}f{}^{ab}G{}_{a}{}^{c}T{}_{bc}+8G{}^{ab}\big(\nabla^2 T{}_{ab}\big)+\frac{16}{3}f{}^{a}{}_{a}G{}^{bc}T{}_{bc} \\
&+\frac{8}{3}G{}^{ab}\big(\nabla^{c}\nabla_{a}T{}_{bc}\big)-\frac{1}{2}g^2L_c{}^{ij}\big(\nabla^2 L_c{}_{ij}\big)-\frac{1}{2}g^2L_c{}^{ij}L_c{}_{ij}f{}^{a}{}_{a} \\
&+2\big(\nabla^2 f{}^{b}{}_{b}\big)-6f{}^{ab}f{}_{ab}+8f{}^{a}{}_{a}f{}^{b}{}_{b} \\
&+6\big(\nabla^{a}G{}^{bc}\big)\big(\nabla_{a}T{}_{bc}\big)+\frac{8}{3}\big(\nabla^2 G{}^{bc}\big)T{}_{bc}-8\big(\nabla^{a}G{}_{a}{}^{b}\big)\big(\nabla^{c}T{}_{bc}\big) \\
&+4\big(\nabla^{a}G{}^{bc}\big)\big(\nabla_{b}T{}_{ac}\big)+\frac{32}{3}\big(\nabla^{a}\nabla^{b}G{}_{b}{}^{c}\big)T{}_{ac}+16\big(\nabla^{a}G{}_{a}{}^{b}\big)T{}^{cd}T{}^{ef}\epsilon{}_{bcdef} \\
&-4\big(\nabla^2 D\big)-2g^2L_c{}^{ij}L_c{}_{ij}T^2-\frac{1}{4}g^2\big(\nabla^{a}L_c{}^{ij}\big)\big(\nabla_{a}L_c{}_{ij}\big) \\
&+\frac{1}{8}R(M){}^{abcd}G{}_{ab}G{}_{cd}+\frac{1}{4}R(M){}^{abcd}G{}_{ac}G{}_{bd}+\frac{50}{3}G^2T^2 \\
&-64G{}^{ab}G{}_{a}{}^{c}T{}_{b}{}^{d}T{}_{cd}+2G{}^{ab}G{}^{cd}\big(\nabla^{e}T{}_{e}{}^{f}\big)\epsilon{}_{abcdf}+\frac{1}{2}G{}^{ab}\big(\nabla^2 G{}_{ab}\big) \\
&+\frac{3}{2}f{}^{a}{}_{a}G^2+\frac{25}{12}G{}^{ab}\big(\nabla_{a}G{}^{cd}\big)T{}^{ef}\epsilon{}_{bcdef}-\frac{17}{6}G{}^{ab}\big(\nabla^{c}G{}^{de}\big)T{}_{a}{}^{f}\epsilon{}_{bcdef} \\
&-\frac{7}{3}G{}^{ab}\big(\nabla^{c}G{}_{a}{}^{d}\big)T{}^{ef}\epsilon{}_{bcdef}+\frac{35}{12}G{}^{ab}\big(\nabla^{c}G{}_{c}{}^{d}\big)T{}^{ef}\epsilon{}_{abdef}+\frac{11}{6}G{}^{ab}\big(\nabla^{c}G{}^{de}\big)T{}_{d}{}^{f}\epsilon{}_{abcef} \\
&+2G{}^{ab}\big(\nabla^{c}G{}^{de}\big)T{}_{c}{}^{f}\epsilon{}_{abdef}+\frac{1}{4}\big(\nabla^{a}G{}^{bc}\big)\big(\nabla_{a}G{}_{bc}\big)+\frac{3}{16}g^2L_c{}^{ij}L_c{}_{ij}G^2 \\
&-4G{}^{ab}T{}_{ab}G^2+DG^2-\frac{5}{32}g^4L_c{}^{ij}L_c{}_{ij}L_c{}^{kl}L_c{}_{kl} \\
&-\frac{1}{8}G{}^{ab}G{}^{cd}\big(\nabla^{e}G{}_{e}{}^{f}\big)\epsilon{}_{abcdf}-2f{}^{ab}G{}_{a}{}^{c}G{}_{bc}+8G{}^{ab}G{}_{a}{}^{c}G{}_{b}{}^{d}T{}_{cd} \\
&+\frac{3}{32}(G^2)^{2}-\frac{3}{8}G{}^{ab}G{}_{a}{}^{c}G{}_{b}{}^{d}G{}_{cd}+\frac{1}{8}g^4L_c{}^{ij}L_c{}_{i}{}^{k}L_c{}_{j}{}^{l}L_c{}_{kl}
\end{aligned}\tag{BC-02}
```

## Complete vector in divergence form

The 177-term actual vector equals the following local expression, with no integration by parts:

```math
E_{\log}^{a}|_0=\nabla_b Q^{ab}-\frac1{12}\epsilon^{abcde}V_{bc}^{ij}V_{de\,ij},\qquad Q^{ab}=-Q^{ba}.\tag{BC-03}
```

The potential is C24 (4.8d), (4.10c) after the field bridge and bosonic gauge evaluation. All 34 canonical terms are displayed below; its divergence was compared directly to the calculated vector. The equality uses the explicit pointwise identities in the report and the 116-row transcript below.

```math
\begin{aligned}
Q^{ab}={}&-\frac{64}{3}DT{}^{ab}+64T{}^{cd}\big(\nabla^{e}T{}_{e}{}^{f}\big)\epsilon{}^{ab}{}_{cdf}+\frac{64}{3}T{}^{cd}\big(\nabla_{c}T{}^{ef}\big)\epsilon{}^{ab}{}_{def} \\
&-\frac{128}{9}T{}^{ab}T^2-\frac{2048}{3}T{}^{ac}T{}^{bd}T{}_{cd}+8R(M){}^{abcd}T{}_{cd} \\
&+8\big(\nabla^2 T{}^{ab}\big)+64f{}^{c}{}_{c}T{}^{ab}-4DG{}^{ab} \\
&-4G{}^{cd}\big(\nabla_{c}T{}^{ef}\big)\epsilon{}^{ab}{}_{def}-8G{}^{cd}\big(\nabla^{e}T{}_{e}{}^{f}\big)\epsilon{}^{ab}{}_{cdf}-8\big(\nabla^{c}G{}_{c}{}^{d}\big)T{}^{ef}\epsilon{}^{ab}{}_{def} \\
&-4\big(\nabla^{c}G{}^{de}\big)T{}_{c}{}^{f}\epsilon{}^{ab}{}_{def}-\big(\nabla^2 G{}^{ab}\big)-6f{}^{c}{}_{c}G{}^{ab} \\
&-\frac{200}{3}G{}^{ab}T^2-128G{}^{bc}T{}^{ad}T{}_{cd}+128G{}^{ac}T{}^{bd}T{}_{cd} \\
&+gL_c{}^{ij}V{}^{ab}{}_{ij}-R(M){}^{abcd}G{}_{cd}+\frac{1}{4}G{}^{cd}\big(\nabla_{c}G{}^{ef}\big)\epsilon{}^{ab}{}_{def} \\
&+\frac{1}{2}G{}^{cd}\big(\nabla^{e}G{}_{e}{}^{f}\big)\epsilon{}^{ab}{}_{cdf}+4f{}^{bc}G{}^{a}{}_{c}-4f{}^{ac}G{}^{b}{}_{c} \\
&+8G{}^{bc}G{}_{c}{}^{d}T{}^{a}{}_{d}-8G{}^{ac}G{}_{c}{}^{d}T{}^{b}{}_{d}+4T{}^{ab}G^2 \\
&-8G{}^{ac}G{}^{bd}T{}_{cd}+8G{}^{ab}G{}^{cd}T{}_{cd}-\frac{1}{4}G{}^{ab}G^2 \\
&+G{}^{ac}G{}^{bd}G{}_{cd}-\frac{1}{4}g^2L_c{}^{ij}L_c{}_{ij}G{}^{ab}+16f{}^{ac}T{}^{b}{}_{c} \\
&-16f{}^{bc}T{}^{a}{}_{c}
\end{aligned}\tag{BC-04}
```

## Boundary currents and the actual BF density

Since $`G_{ab}=2\nabla_{[a}C_{b]}`$, antisymmetry gives

```math
C_a\nabla_bQ^{ab}=\nabla_b(C_aQ^{ab})+\frac12G_{ab}Q^{ab}.\tag{BC-05}
```

Define the intermediate non-CS density only for the comparison,

```math
\ell_{\mathrm{calc},0}=N_{\log}|_0-\frac g2L_c^{ij}L_{\log\,ij}|_0+\frac12G_{ab}Q^{ab}.
\tag{BC-06}
```

The equality to the corrected Standard-Weyl source ledger is local after adding the following displayed current: $`\ell_{\mathrm{calc},0}-\ell_{\mathrm{standard}}=\nabla_aJ_{\mathrm{standard}}^a`$. No boundary term is silently discarded.

```math
\begin{aligned}
J_{\mathrm{standard}}^a={}&\frac{32}{3}G{}^{ab}T{}^{cd}T{}^{ef}\epsilon{}_{bcdef}-\frac{40}{3}G{}^{bc}\big(\nabla_{b}T{}^{a}{}_{c}\big)+\frac{8}{3}G{}^{ab}\big(\nabla^{c}T{}_{bc}\big) \\
&+\frac{64}{3}T{}^{bc}\big(\nabla_{b}T{}^{a}{}_{c}\big)+64T{}^{ab}\big(\nabla^{c}T{}_{bc}\big)-\frac{176}{3}T{}^{bc}\big(\nabla^{a}T{}_{bc}\big) \\
&+12G{}^{bc}\big(\nabla^{a}T{}_{bc}\big)+2\big(\nabla^{a}f{}^{b}{}_{b}\big)+\frac{8}{3}\big(\nabla^{a}G{}^{bc}\big)T{}_{bc} \\
&+\frac{32}{3}\big(\nabla^{b}G{}_{b}{}^{c}\big)T{}^{a}{}_{c}-4\big(\nabla^{a}D\big)
\end{aligned}\tag{BC-07}
```

The gauged dilaton-Weyl replacements are

```math
T_{ab}=\frac18(G_{ab}-2H_{ab}),\qquad D=\frac12f^a{}_a+\frac5{96}G^2+\frac1{24}G\!\cdot\!H-\frac{13}{24}H^2+\frac g4N_c+\frac{g^2}{16}L_c^{ij}L_{c\,ij}.
\tag{BC-08}
```

The replacement in every derivative uses the ordinary covariant product rule and preserves its order. The second boundary relation is $`\ell_{\mathrm{standard}}|_{\mathrm{gauged}}-\ell_{\mathrm{CORR05,non-CS}}=\nabla_aJ_{\mathrm{gauged}}^a`$, with

```math
\begin{aligned}
J_{\mathrm{gauged}}^a={}&\frac{4}{3}H{}^{bc}\big(\nabla_{b}H{}^{a}{}_{c}\big)-\frac{1}{3}H{}^{bc}\big(\nabla^{a}G{}_{bc}\big)-\frac{4}{3}H{}^{ab}\big(\nabla^{c}G{}_{bc}\big) \\
&+\frac{1}{4}G{}^{bc}\big(\nabla^{a}G{}_{bc}\big)-\frac{1}{6}G{}^{ab}\big(\nabla^{c}G{}_{bc}\big)+\frac{4}{3}H{}^{ab}\big(\nabla^{c}H{}_{bc}\big) \\
&+\frac{1}{3}\big(\nabla^{a}H{}^{bc}\big)G{}_{bc}-\frac{2}{3}H{}^{bc}\big(\nabla^{a}H{}_{bc}\big)-2\big(\nabla^{b}H{}_{b}{}^{c}\big)G{}^{a}{}_{c}
\end{aligned}\tag{BC-09}
```

Their sum after the substitution, $`J^a=J_{\mathrm{standard}}^a|_{\mathrm{gauged}}+J_{\mathrm{gauged}}^a`$, is fully collected:

```math
\begin{aligned}
J^a={}&\frac{1}{6}G{}^{ab}G{}^{cd}G{}^{ef}\epsilon{}_{bcdef}-\frac{2}{3}H{}^{bc}G{}^{ad}G{}^{ef}\epsilon{}_{bcdef}+\frac{2}{3}H{}^{bc}H{}^{de}G{}^{af}\epsilon{}_{bcdef} \\
&-\frac{4}{3}G{}^{bc}\big(\nabla_{b}G{}^{a}{}_{c}\big)+\frac{8}{3}\big(\nabla^{b}H{}^{ac}\big)G{}_{bc}+\frac{2}{3}\big(\nabla^{b}H{}_{b}{}^{c}\big)G{}^{a}{}_{c} \\
&-\frac{2}{3}H{}^{bc}\big(\nabla_{b}G{}^{a}{}_{c}\big)+\frac{8}{3}H{}^{bc}\big(\nabla_{b}H{}^{a}{}_{c}\big)-\frac{2}{3}H{}^{ab}\big(\nabla^{c}G{}_{bc}\big) \\
&+\frac{16}{3}H{}^{ab}\big(\nabla^{c}H{}_{bc}\big)+\frac{3}{4}G{}^{bc}\big(\nabla^{a}G{}_{bc}\big)-\big(\nabla^{a}H{}^{bc}\big)G{}_{bc} \\
&+\frac{2}{3}H{}^{bc}\big(\nabla^{a}G{}_{bc}\big)-g\big(\nabla^{a}N_c\big)-\frac{1}{2}g^2L_c{}^{ij}\big(\nabla^{a}L_c{}_{ij}\big) \\
&-\frac{1}{6}G{}^{ab}\big(\nabla^{c}G{}_{bc}\big)
\end{aligned}\tag{BC-10}
```

Thus the final local density relation is

```math
\boxed{\ell_{\mathrm{BF}}^{(0)}=\ell_{\mathrm{LOG-CORR05}}+\nabla_b\!\left(C_aQ^{ab}|_{\mathrm{gauged}}+J^b\right).}\tag{BC-11}
```

This equality retains the independent $`E_c`$ terms. Its gauged three-form identity is $`\nabla_bH^{ab}=-\epsilon^{abcde}G_{bc}G_{de}/16+gE_c^a/2`$. It is a Bianchi identity, not an equation used to eliminate $`E_c`$.

## Complete corrected target

The following is the existing LOG-CORR05 expression, reproduced to make the comparison target explicit. In this display $`L,N,E`$ denote $`L_c,N_c,E_c`$; $`V_{ab}^{ij}`$ is the $`SU(2)`$ curvature. It includes the common Chern-Simons term already fixed by (BC-03).

```math
\begin{aligned} \ell_{\rm LOG}^{\rm def,bos}\simeq_{\partial}{}& -\frac1{12}\epsilon^{abcde}C_aV_{bc}^{ij}V_{de\,ij} +\frac16V_{ab}^{ij}V^{ab}_{ij} +\frac g6V_{ab}^{ij}L_{ij}G^{ab} +\frac{2g}{3}V_{ab}^{ij}L_{ij}H^{ab} \\
 &-\frac16R_{ab}R^{ab}+\frac1{24}R^2 +\frac16R_{ab}G^{ac}G^b{}_c -\frac43R_{ab}G^{ac}H^b{}_c \\
 &+R\left(\frac g6N-\frac{g^2}{12}L^{ij}L_{ij} +\frac13G_{ab}H^{ab}-\frac13H_{ab}H^{ab}\right) \\
 &-\frac{g^2}{6}N^2+\frac{2g^3}{3}N L^{ij}L_{ij} +\frac{5g^4}{24}(L^{ij}L_{ij})^2 \\
 &+gN\left(-\frac13G_{ab}G^{ab}-\frac23G_{ab}H^{ab} +2H_{ab}H^{ab}\right) \\
 &+g^2L^{ij}L_{ij}\left(\frac1{24}G_{ab}G^{ab} -\frac16G_{ab}H^{ab}-H_{ab}H^{ab}\right) \\
 &-\frac1{48}(G_{ab}G^{ab})^2 -\frac13(G_{ab}G^{ab})(G_{cd}H^{cd}) +\frac23(G_{ab}G^{ab})(H_{cd}H^{cd}) \\
 &+\frac43(G_{ab}H^{ab})^2 -\frac43(G_{ab}H^{ab})(H_{cd}H^{cd}) -2(H_{ab}H^{ab})^2 \\
 &-\frac1{24}G_{ab}G^{bc}G_{cd}G^{da} +G_{ab}G^{bc}G_{cd}H^{da} -\frac43G_{ab}G^{bc}H_{cd}H^{da} \\
 &-\frac83G_{ab}H^{bc}G_{cd}H^{da} +\frac{16}{3}G_{ab}H^{bc}H_{cd}H^{da} \\
 &-\frac16(\nabla_bG^{ab})(\nabla^cG_{ac}) +\frac23(\nabla_aH_{bc}) \left(\nabla^aH^{bc}+\nabla^bH^{ca}+\nabla^cH^{ab}\right) \\
 &-\frac{g^2}{4}(\nabla_aL^{ij})(\nabla^aL_{ij}) \\
 &+\frac1{48}(\nabla^bG_{ab})\epsilon^{acdef}G_{cd}G_{ef} +\frac13(\nabla^bG_{ab})\epsilon^{acdef}H_{cd}H_{ef} \\
 &-\frac16(\nabla^bG_{ab})\epsilon^{acdef}H_{cd}G_{ef} \\
 &+\frac1{12}(\epsilon^{abcde}G_{bc}G_{de}) (\epsilon_{a}{}^{fghi}H_{fg}H_{hi}) \\
 &+\frac g3E_a\nabla_bG^{ab} -\frac g{24}E_a\epsilon^{abcde}G_{bc}G_{de} -\frac{2g}{3}E_a\epsilon^{abcde}H_{bc}H_{de} +\frac{g^2}{3}E_aE^a. \end{aligned} \tag{LOG-CORR05}
```

## Exact pointwise identity transcripts

Every displayed row below is multiplied by its exact coefficient from the elimination certificate. Summing the vector rows reproduces $`E_{\log}^{a}|_0-\nabla_bQ^{ab}+\epsilon^{abcde}V_{bc}^{ij}V_{de\,ij}/12`$. Summing the final-density rows reproduces $`\ell_{\mathrm{calc},0}|_{\mathrm{gauged}}-\ell_{\mathrm{CORR05,non-CS}}-\nabla_aJ^a`$. Every row is zero by its named identity; neither transcript uses integration by parts. The product-rule boundary currents have already been removed explicitly.

### Vector local equality

Identity 1: `Schouten`; this is the actual weighted relation used in the comparison.

```math
\begin{aligned}
0={}&-\frac{263}{96}R(M){}^{abcd}G{}^{ef}T{}_{b}{}^{g}\epsilon{}_{cdefg}+\frac{263}{48}R(M){}^{bcde}G{}_{b}{}^{f}T{}_{c}{}^{g}\epsilon{}^{a}{}_{defg}-\frac{263}{96}R(M){}^{bcde}G{}^{fg}T{}_{bc}\epsilon{}^{a}{}_{defg}
\end{aligned}\tag{VE-1}
```

Identity 2: `Schouten`; this is the actual weighted relation used in the comparison.

```math
\begin{aligned}
0={}&-\frac{65}{96}R(M){}^{abcd}G{}^{ef}T{}_{b}{}^{g}\epsilon{}_{cdefg}-\frac{65}{96}R(M){}^{abcd}G{}_{b}{}^{e}T{}^{fg}\epsilon{}_{cdefg}
\end{aligned}\tag{VE-2}
```

Identity 3: `Schouten`; this is the actual weighted relation used in the comparison.

```math
\begin{aligned}
0={}&\frac{3}{16}R(M){}^{abcd}G{}^{ef}T{}_{b}{}^{g}\epsilon{}_{cdefg}-\frac{3}{8}R(M){}^{abcd}G{}^{ef}T{}_{c}{}^{g}\epsilon{}_{bdefg}-\frac{3}{8}R(M){}^{abcd}G{}^{ef}T{}_{e}{}^{g}\epsilon{}_{bcdfg}
\end{aligned}\tag{VE-3}
```

Identity 4: `algebraic_Bianchi`; this is the actual weighted relation used in the comparison.

```math
\begin{aligned}
0={}&\frac{3}{2}R(M){}^{abcd}G{}^{ef}T{}_{b}{}^{g}\epsilon{}_{cdefg}-3R(M){}^{abcd}G{}^{ef}T{}_{c}{}^{g}\epsilon{}_{bdefg}
\end{aligned}\tag{VE-4}
```

Identity 5: `Schouten`; this is the actual weighted relation used in the comparison.

```math
\begin{aligned}
0={}&\frac{263}{48}R(M){}^{abcd}G{}^{ef}T{}_{c}{}^{g}\epsilon{}_{bdefg}-\frac{263}{24}R(M){}^{bcde}G{}_{b}{}^{f}T{}_{d}{}^{g}\epsilon{}^{a}{}_{cefg}+\frac{263}{48}R(M){}^{bcde}G{}^{fg}T{}_{bd}\epsilon{}^{a}{}_{cefg}
\end{aligned}\tag{VE-5}
```

Identity 6: `Schouten`; this is the actual weighted relation used in the comparison.

```math
\begin{aligned}
0={}&\frac{83}{48}R(M){}^{abcd}G{}^{ef}T{}_{c}{}^{g}\epsilon{}_{bdefg}+\frac{83}{48}R(M){}^{abcd}G{}_{c}{}^{e}T{}^{fg}\epsilon{}_{bdefg}
\end{aligned}\tag{VE-6}
```

Identity 7: `Schouten`; this is the actual weighted relation used in the comparison.

```math
\begin{aligned}
0={}&\frac{7}{8}R(M){}^{abcd}G{}^{ef}T{}_{e}{}^{g}\epsilon{}_{bcdfg}-\frac{7}{8}R(M){}^{bcde}G{}_{b}{}^{f}T{}_{f}{}^{g}\epsilon{}^{a}{}_{cdeg}+\frac{7}{8}R(M){}^{bcde}G{}^{fg}T{}_{bf}\epsilon{}^{a}{}_{cdeg}
\end{aligned}\tag{VE-7}
```

Identity 8: `Schouten`; this is the actual weighted relation used in the comparison.

```math
\begin{aligned}
0={}&-\frac{41}{96}R(M){}^{abcd}G{}_{b}{}^{e}T{}^{fg}\epsilon{}_{cdefg}-\frac{41}{96}R(M){}^{bcde}G{}_{bc}T{}^{fg}\epsilon{}^{a}{}_{defg}+\frac{41}{48}R(M){}^{bcde}G{}_{b}{}^{f}T{}_{c}{}^{g}\epsilon{}^{a}{}_{defg}
\end{aligned}\tag{VE-8}
```

Identity 9: `Schouten`; this is the actual weighted relation used in the comparison.

```math
\begin{aligned}
0={}&-\frac{13}{12}R(M){}^{abcd}G{}_{c}{}^{e}T{}^{fg}\epsilon{}_{bdefg}-\frac{13}{12}R(M){}^{bcde}G{}_{bd}T{}^{fg}\epsilon{}^{a}{}_{cefg}+\frac{13}{6}R(M){}^{bcde}G{}_{b}{}^{f}T{}_{d}{}^{g}\epsilon{}^{a}{}_{cefg}
\end{aligned}\tag{VE-9}
```

Identity 10: `algebraic_Bianchi`; this is the actual weighted relation used in the comparison.

```math
\begin{aligned}
0={}&R(M){}^{abcd}\big(\nabla_{b}G{}_{cd}\big)-2R(M){}^{abcd}\big(\nabla_{c}G{}_{bd}\big)
\end{aligned}\tag{VE-10}
```

Identity 11: `algebraic_Bianchi`; this is the actual weighted relation used in the comparison.

```math
\begin{aligned}
0={}&-8R(M){}^{abcd}\big(\nabla_{b}T{}_{cd}\big)+16R(M){}^{abcd}\big(\nabla_{c}T{}_{bd}\big)
\end{aligned}\tag{VE-11}
```

Identity 12: `algebraic_Bianchi`; this is the actual weighted relation used in the comparison.

```math
\begin{aligned}
0={}&-\frac{5}{4}\big(\nabla^{b}R(M){}^{ac}{}_{b}{}^{d}\big)G{}_{cd}+\frac{5}{8}\big(\nabla^{b}R(M){}^{a}{}_{b}{}^{cd}\big)G{}_{cd}
\end{aligned}\tag{VE-12}
```

Identity 13: `dR=0`; this is the actual weighted relation used in the comparison.

```math
\begin{aligned}
0={}&-\frac{1}{2}\big(\nabla^{b}R(M){}^{ac}{}_{b}{}^{d}\big)G{}_{cd}+\big(\nabla^{b}f{}_{b}{}^{c}\big)G{}^{a}{}_{c}+2\big(\nabla^{b}f{}^{ac}\big)G{}_{bc} \\
&-\big(\nabla^{b}f{}^{c}{}_{c}\big)G{}^{a}{}_{b}
\end{aligned}\tag{VE-13}
```

Identity 14: `algebraic_Bianchi`; this is the actual weighted relation used in the comparison.

```math
\begin{aligned}
0={}&12\big(\nabla^{b}R(M){}^{ac}{}_{b}{}^{d}\big)T{}_{cd}-6\big(\nabla^{b}R(M){}^{a}{}_{b}{}^{cd}\big)T{}_{cd}
\end{aligned}\tag{VE-14}
```

Identity 15: `Schouten`; this is the actual weighted relation used in the comparison.

```math
\begin{aligned}
0={}&\frac{5}{8}R(M){}^{bcde}G{}^{af}G{}_{b}{}^{g}\epsilon{}_{cdefg}-\frac{5}{16}R(M){}^{bcde}G{}^{a}{}_{b}G{}^{fg}\epsilon{}_{cdefg}
\end{aligned}\tag{VE-15}
```

Identity 16: `Schouten`; this is the actual weighted relation used in the comparison.

```math
\begin{aligned}
0={}&-\frac{9}{32}R(M){}^{bcde}G{}^{af}G{}_{b}{}^{g}\epsilon{}_{cdefg}-\frac{9}{32}R(M){}^{bcde}G{}_{b}{}^{f}G{}_{c}{}^{g}\epsilon{}^{a}{}_{defg}+\frac{9}{16}R(M){}^{bcde}G{}_{b}{}^{f}G{}_{d}{}^{g}\epsilon{}^{a}{}_{cefg} \\
&+\frac{9}{32}R(M){}^{bcde}G{}_{b}{}^{f}G{}_{f}{}^{g}\epsilon{}^{a}{}_{cdeg}
\end{aligned}\tag{VE-16}
```

Identity 17: `algebraic_Bianchi`; this is the actual weighted relation used in the comparison.

```math
\begin{aligned}
0={}&-\frac{1}{4}R(M){}^{bcde}G{}^{af}G{}_{b}{}^{g}\epsilon{}_{cdefg}
\end{aligned}\tag{VE-17}
```

Identity 18: `Schouten`; this is the actual weighted relation used in the comparison.

```math
\begin{aligned}
0={}&-\frac{143}{24}R(M){}^{bcde}G{}^{af}T{}_{b}{}^{g}\epsilon{}_{cdefg}+\frac{143}{48}R(M){}^{bcde}G{}^{a}{}_{b}T{}^{fg}\epsilon{}_{cdefg}
\end{aligned}\tag{VE-18}
```

Identity 19: `Schouten`; this is the actual weighted relation used in the comparison.

```math
\begin{aligned}
0={}&-\frac{187}{24}R(M){}^{bcde}G{}^{af}T{}_{b}{}^{g}\epsilon{}_{cdefg}-\frac{187}{24}R(M){}^{bcde}G{}_{b}{}^{f}T{}_{c}{}^{g}\epsilon{}^{a}{}_{defg}+\frac{187}{12}R(M){}^{bcde}G{}_{b}{}^{f}T{}_{d}{}^{g}\epsilon{}^{a}{}_{cefg} \\
&+\frac{187}{24}R(M){}^{bcde}G{}^{fg}T{}_{bf}\epsilon{}^{a}{}_{cdeg}
\end{aligned}\tag{VE-19}
```

Identity 20: `Schouten`; this is the actual weighted relation used in the comparison.

```math
\begin{aligned}
0={}&\frac{23}{24}R(M){}^{bcde}G{}^{af}T{}_{b}{}^{g}\epsilon{}_{cdefg}+\frac{23}{96}R(M){}^{bcde}G{}^{af}T{}_{f}{}^{g}\epsilon{}_{bcdeg}
\end{aligned}\tag{VE-20}
```

Identity 21: `algebraic_Bianchi`; this is the actual weighted relation used in the comparison.

```math
\begin{aligned}
0={}&8R(M){}^{bcde}G{}^{af}T{}_{b}{}^{g}\epsilon{}_{cdefg}
\end{aligned}\tag{VE-21}
```

Identity 22: `Schouten`; this is the actual weighted relation used in the comparison.

```math
\begin{aligned}
0={}&-\frac{5}{96}R(M){}^{bcde}G{}^{af}T{}_{f}{}^{g}\epsilon{}_{bcdeg}+\frac{5}{24}R(M){}^{bcde}G{}_{b}{}^{f}T{}_{f}{}^{g}\epsilon{}^{a}{}_{cdeg}-\frac{5}{96}R(M){}^{bcde}G{}^{fg}T{}_{fg}\epsilon{}^{a}{}_{bcde}
\end{aligned}\tag{VE-22}
```

Identity 23: `Schouten`; this is the actual weighted relation used in the comparison.

```math
\begin{aligned}
0={}&\frac{17}{64}R(M){}^{bcde}G{}^{a}{}_{b}G{}^{fg}\epsilon{}_{cdefg}+\frac{17}{64}R(M){}^{bcde}G{}_{bc}G{}^{fg}\epsilon{}^{a}{}_{defg}-\frac{17}{32}R(M){}^{bcde}G{}_{bd}G{}^{fg}\epsilon{}^{a}{}_{cefg} \\
&-\frac{17}{32}R(M){}^{bcde}G{}_{b}{}^{f}G{}_{f}{}^{g}\epsilon{}^{a}{}_{cdeg}
\end{aligned}\tag{VE-23}
```

Identity 24: `algebraic_Bianchi`; this is the actual weighted relation used in the comparison.

```math
\begin{aligned}
0={}&\frac{1}{32}R(M){}^{bcde}\epsilon{}^{a}{}_{bcde}G^2
\end{aligned}\tag{VE-24}
```

Identity 25: `Schouten`; this is the actual weighted relation used in the comparison.

```math
\begin{aligned}
0={}&-\frac{11}{32}R(M){}^{bcde}G{}^{fg}T{}^{a}{}_{b}\epsilon{}_{cdefg}-\frac{11}{16}R(M){}^{bcde}G{}_{b}{}^{f}T{}^{ag}\epsilon{}_{cdefg}
\end{aligned}\tag{VE-25}
```

Identity 26: `Schouten`; this is the actual weighted relation used in the comparison.

```math
\begin{aligned}
0={}&\frac{155}{48}R(M){}^{bcde}G{}^{fg}T{}^{a}{}_{b}\epsilon{}_{cdefg}+\frac{155}{48}R(M){}^{bcde}G{}^{fg}T{}_{bc}\epsilon{}^{a}{}_{defg}-\frac{155}{24}R(M){}^{bcde}G{}^{fg}T{}_{bd}\epsilon{}^{a}{}_{cefg} \\
&-\frac{155}{24}R(M){}^{bcde}G{}^{fg}T{}_{bf}\epsilon{}^{a}{}_{cdeg}
\end{aligned}\tag{VE-26}
```

Identity 27: `Schouten`; this is the actual weighted relation used in the comparison.

```math
\begin{aligned}
0={}&-\frac{1}{8}R(M){}^{bcde}G{}^{fg}T{}^{a}{}_{b}\epsilon{}_{cdefg}-\frac{1}{16}R(M){}^{bcde}G{}^{fg}T{}^{a}{}_{f}\epsilon{}_{bcdeg}
\end{aligned}\tag{VE-27}
```

Identity 28: `algebraic_Bianchi`; this is the actual weighted relation used in the comparison.

```math
\begin{aligned}
0={}&-\frac{11}{12}R(M){}^{bcde}G{}^{fg}T{}_{bc}\epsilon{}^{a}{}_{defg}+\frac{11}{6}R(M){}^{bcde}G{}^{fg}T{}_{bd}\epsilon{}^{a}{}_{cefg}
\end{aligned}\tag{VE-28}
```

Identity 29: `Schouten`; this is the actual weighted relation used in the comparison.

```math
\begin{aligned}
0={}&\frac{13}{32}R(M){}^{bcde}G{}_{b}{}^{f}G{}_{c}{}^{g}\epsilon{}^{a}{}_{defg}-\frac{13}{64}R(M){}^{abcd}G{}_{b}{}^{e}G{}^{fg}\epsilon{}_{cdefg}-\frac{13}{64}R(M){}^{bcde}G{}_{bc}G{}^{fg}\epsilon{}^{a}{}_{defg}
\end{aligned}\tag{VE-29}
```

Identity 30: `Schouten`; this is the actual weighted relation used in the comparison.

```math
\begin{aligned}
0={}&\frac{52}{3}R(M){}^{bcde}T{}^{af}T{}_{b}{}^{g}\epsilon{}_{cdefg}-\frac{26}{3}R(M){}^{bcde}T{}^{a}{}_{b}T{}^{fg}\epsilon{}_{cdefg}
\end{aligned}\tag{VE-30}
```

Identity 31: `Schouten`; this is the actual weighted relation used in the comparison.

```math
\begin{aligned}
0={}&23R(M){}^{bcde}T{}^{af}T{}_{b}{}^{g}\epsilon{}_{cdefg}+23R(M){}^{bcde}T{}_{b}{}^{f}T{}_{c}{}^{g}\epsilon{}^{a}{}_{defg}-46R(M){}^{bcde}T{}_{b}{}^{f}T{}_{d}{}^{g}\epsilon{}^{a}{}_{cefg} \\
&-23R(M){}^{bcde}T{}_{b}{}^{f}T{}_{f}{}^{g}\epsilon{}^{a}{}_{cdeg}
\end{aligned}\tag{VE-31}
```

Identity 32: `Schouten`; this is the actual weighted relation used in the comparison.

```math
\begin{aligned}
0={}&6R(M){}^{bcde}T{}^{af}T{}_{b}{}^{g}\epsilon{}_{cdefg}+\frac{3}{2}R(M){}^{bcde}T{}^{af}T{}_{f}{}^{g}\epsilon{}_{bcdeg}
\end{aligned}\tag{VE-32}
```

Identity 33: `algebraic_Bianchi`; this is the actual weighted relation used in the comparison.

```math
\begin{aligned}
0={}&-\frac{80}{3}R(M){}^{bcde}T{}^{af}T{}_{b}{}^{g}\epsilon{}_{cdefg}
\end{aligned}\tag{VE-33}
```

Identity 34: `Schouten`; this is the actual weighted relation used in the comparison.

```math
\begin{aligned}
0={}&-\frac{13}{6}R(M){}^{bcde}T{}^{af}T{}_{f}{}^{g}\epsilon{}_{bcdeg}+\frac{26}{3}R(M){}^{bcde}T{}_{b}{}^{f}T{}_{f}{}^{g}\epsilon{}^{a}{}_{cdeg}-\frac{13}{6}R(M){}^{bcde}\epsilon{}^{a}{}_{bcde}T^2
\end{aligned}\tag{VE-34}
```

Identity 35: `Schouten`; this is the actual weighted relation used in the comparison.

```math
\begin{aligned}
0={}&-\frac{119}{18}R(M){}^{bcde}T{}^{a}{}_{b}T{}^{fg}\epsilon{}_{cdefg}-\frac{119}{18}R(M){}^{bcde}T{}_{bc}T{}^{fg}\epsilon{}^{a}{}_{defg}+\frac{119}{9}R(M){}^{bcde}T{}_{bd}T{}^{fg}\epsilon{}^{a}{}_{cefg} \\
&+\frac{119}{9}R(M){}^{bcde}T{}_{b}{}^{f}T{}_{f}{}^{g}\epsilon{}^{a}{}_{cdeg}
\end{aligned}\tag{VE-35}
```

Identity 36: `algebraic_Bianchi`; this is the actual weighted relation used in the comparison.

```math
\begin{aligned}
0={}&\frac{14}{9}R(M){}^{bcde}\epsilon{}^{a}{}_{bcde}T^2
\end{aligned}\tag{VE-36}
```

Identity 37: `Schouten`; this is the actual weighted relation used in the comparison.

```math
\begin{aligned}
0={}&-\frac{169}{9}R(M){}^{bcde}T{}_{b}{}^{f}T{}_{c}{}^{g}\epsilon{}^{a}{}_{defg}+\frac{169}{18}R(M){}^{abcd}T{}_{b}{}^{e}T{}^{fg}\epsilon{}_{cdefg}+\frac{169}{18}R(M){}^{bcde}T{}_{bc}T{}^{fg}\epsilon{}^{a}{}_{defg}
\end{aligned}\tag{VE-37}
```

Identity 38: `Schouten`; this is the actual weighted relation used in the comparison.

```math
\begin{aligned}
0={}&\frac{200}{9}R(M){}^{bcde}T{}_{b}{}^{f}T{}_{d}{}^{g}\epsilon{}^{a}{}_{cefg}-\frac{100}{9}R(M){}^{abcd}T{}_{c}{}^{e}T{}^{fg}\epsilon{}_{bdefg}-\frac{100}{9}R(M){}^{bcde}T{}_{bd}T{}^{fg}\epsilon{}^{a}{}_{cefg}
\end{aligned}\tag{VE-38}
```

Identity 39: `Schouten`; this is the actual weighted relation used in the comparison.

```math
\begin{aligned}
0={}&\frac{1}{4}f{}^{ab}G{}^{cd}G{}^{ef}\epsilon{}_{bcdef}-\frac{1}{4}f{}^{b}{}_{b}G{}^{cd}G{}^{ef}\epsilon{}^{a}{}_{cdef}+f{}^{bc}G{}_{b}{}^{d}G{}^{ef}\epsilon{}^{a}{}_{cdef}
\end{aligned}\tag{VE-39}
```

Identity 40: `Schouten`; this is the actual weighted relation used in the comparison.

```math
\begin{aligned}
0={}&\frac{37}{2}f{}^{ab}G{}^{cd}T{}^{ef}\epsilon{}_{bcdef}-\frac{37}{2}f{}^{b}{}_{b}G{}^{cd}T{}^{ef}\epsilon{}^{a}{}_{cdef}+37f{}^{bc}G{}_{b}{}^{d}T{}^{ef}\epsilon{}^{a}{}_{cdef} \\
&+37f{}^{bc}G{}^{de}T{}_{b}{}^{f}\epsilon{}^{a}{}_{cdef}
\end{aligned}\tag{VE-40}
```

Identity 41: `Schouten`; this is the actual weighted relation used in the comparison.

```math
\begin{aligned}
0={}&-\frac{352}{9}f{}^{ab}T{}^{cd}T{}^{ef}\epsilon{}_{bcdef}+\frac{352}{9}f{}^{b}{}_{b}T{}^{cd}T{}^{ef}\epsilon{}^{a}{}_{cdef}-\frac{1408}{9}f{}^{bc}T{}_{b}{}^{d}T{}^{ef}\epsilon{}^{a}{}_{cdef}
\end{aligned}\tag{VE-41}
```

Identity 42: `contracted_Ricci_Bianchi`; this is the actual weighted relation used in the comparison.

```math
\begin{aligned}
0={}&\frac{80}{3}\big(\nabla^{b}f{}_{b}{}^{c}\big)T{}^{a}{}_{c}-\frac{80}{3}\big(\nabla^{b}f{}^{c}{}_{c}\big)T{}^{a}{}_{b}
\end{aligned}\tag{VE-42}
```

Identity 43: `dF=0`; this is the actual weighted relation used in the comparison.

```math
\begin{aligned}
0={}&-\frac{20}{3}G{}^{ab}\big(\nabla_{b}G{}^{cd}\big)T{}_{cd}+\frac{40}{3}G{}^{ab}\big(\nabla^{c}G{}_{b}{}^{d}\big)T{}_{cd}
\end{aligned}\tag{VE-43}
```

Identity 44: `Schouten`; this is the actual weighted relation used in the comparison.

```math
\begin{aligned}
0={}&\frac{1}{12}G{}^{ab}G{}^{cd}G{}^{ef}T{}_{b}{}^{g}\epsilon{}_{cdefg}-\frac{1}{3}G{}^{bc}G{}_{b}{}^{d}G{}^{ef}T{}_{c}{}^{g}\epsilon{}^{a}{}_{defg}+\frac{1}{12}G{}^{bc}G{}^{de}G{}^{fg}T{}_{bc}\epsilon{}^{a}{}_{defg}
\end{aligned}\tag{VE-44}
```

Identity 45: `Schouten`; this is the actual weighted relation used in the comparison.

```math
\begin{aligned}
0={}&-\frac{95}{48}G{}^{ab}G{}^{cd}G{}^{ef}T{}_{b}{}^{g}\epsilon{}_{cdefg}-\frac{95}{24}G{}^{ab}G{}_{b}{}^{c}G{}^{de}T{}^{fg}\epsilon{}_{cdefg}
\end{aligned}\tag{VE-45}
```

Identity 46: `Schouten`; this is the actual weighted relation used in the comparison.

```math
\begin{aligned}
0={}&\frac{25}{16}G{}^{ab}G{}^{cd}G{}^{ef}T{}_{b}{}^{g}\epsilon{}_{cdefg}-\frac{25}{4}G{}^{ab}G{}^{cd}G{}^{ef}T{}_{c}{}^{g}\epsilon{}_{bdefg}
\end{aligned}\tag{VE-46}
```

Identity 47: `Schouten`; this is the actual weighted relation used in the comparison.

```math
\begin{aligned}
0={}&-\frac{1}{4}G{}^{ab}G{}^{cd}G{}^{ef}T{}_{c}{}^{g}\epsilon{}_{bdefg}+\frac{1}{4}G{}^{bc}G{}_{b}{}^{d}G{}^{ef}T{}_{c}{}^{g}\epsilon{}^{a}{}_{defg}-\frac{1}{4}G{}^{bc}G{}^{de}G{}^{fg}T{}_{bd}\epsilon{}^{a}{}_{cefg}
\end{aligned}\tag{VE-47}
```

Identity 48: `dF=0`; this is the actual weighted relation used in the comparison.

```math
\begin{aligned}
0={}&-G{}^{ab}G{}^{cd}\big(\nabla_{c}G{}_{bd}\big)+\frac{1}{2}G{}^{ab}G{}^{cd}\big(\nabla_{b}G{}_{cd}\big)
\end{aligned}\tag{VE-48}
```

Identity 49: `Schouten`; this is the actual weighted relation used in the comparison.

```math
\begin{aligned}
0={}&\frac{3}{16}G{}^{ab}G{}_{b}{}^{c}G{}^{de}G{}^{fg}\epsilon{}_{cdefg}
\end{aligned}\tag{VE-49}
```

Identity 50: `Schouten`; this is the actual weighted relation used in the comparison.

```math
\begin{aligned}
0={}&-\frac{1}{2}G{}^{ab}G{}_{b}{}^{c}G{}^{de}T{}^{fg}\epsilon{}_{cdefg}-\frac{1}{2}G{}^{bc}T{}^{de}\epsilon{}^{a}{}_{bcde}G^2+G{}^{bc}G{}_{b}{}^{d}G{}_{c}{}^{e}T{}^{fg}\epsilon{}^{a}{}_{defg} \\
&+G{}^{bc}G{}_{b}{}^{d}G{}^{ef}T{}_{c}{}^{g}\epsilon{}^{a}{}_{defg}
\end{aligned}\tag{VE-50}
```

Identity 51: `Schouten`; this is the actual weighted relation used in the comparison.

```math
\begin{aligned}
0={}&-\frac{19}{12}G{}^{ab}G{}_{b}{}^{c}T{}^{de}T{}^{fg}\epsilon{}_{cdefg}-\frac{19}{12}T{}^{bc}T{}^{de}\epsilon{}^{a}{}_{bcde}G^2+\frac{19}{3}G{}^{bc}G{}_{b}{}^{d}T{}_{c}{}^{e}T{}^{fg}\epsilon{}^{a}{}_{defg}
\end{aligned}\tag{VE-51}
```

Identity 52: `Schouten`; this is the actual weighted relation used in the comparison.

```math
\begin{aligned}
0={}&-\frac{5}{4}G{}^{ab}G{}_{b}{}^{c}T{}^{de}T{}^{fg}\epsilon{}_{cdefg}-\frac{5}{2}G{}^{ab}G{}^{cd}T{}_{b}{}^{e}T{}^{fg}\epsilon{}_{cdefg}
\end{aligned}\tag{VE-52}
```

Identity 53: `Schouten`; this is the actual weighted relation used in the comparison.

```math
\begin{aligned}
0={}&-\frac{1}{3}G{}^{ab}G{}_{b}{}^{c}T{}^{de}T{}^{fg}\epsilon{}_{cdefg}-\frac{4}{3}G{}^{ab}G{}^{cd}T{}_{c}{}^{e}T{}^{fg}\epsilon{}_{bdefg}
\end{aligned}\tag{VE-53}
```

Identity 54: `Schouten`; this is the actual weighted relation used in the comparison.

```math
\begin{aligned}
0={}&\frac{67}{12}G{}^{ab}\big(\nabla^{c}\nabla^{d}T{}^{ef}\big)\epsilon{}_{bcdef}+\frac{67}{12}G{}^{bc}\big(\nabla_{b}\nabla^{d}T{}^{ef}\big)\epsilon{}^{a}{}_{cdef}-\frac{67}{12}G{}^{bc}\big(\nabla^{d}\nabla_{b}T{}^{ef}\big)\epsilon{}^{a}{}_{cdef} \\
&+\frac{67}{6}G{}^{bc}\big(\nabla^{d}\nabla^{e}T{}_{b}{}^{f}\big)\epsilon{}^{a}{}_{cdef}
\end{aligned}\tag{VE-54}
```

Identity 55: `covariant_commutator`; this is the actual weighted relation used in the comparison.

```math
\begin{aligned}
0={}&-\frac{8}{3}G{}^{ab}\big(\nabla^{c}\nabla^{d}T{}^{ef}\big)\epsilon{}_{bcdef}+\frac{8}{3}R(M){}^{bcde}G{}^{af}T{}_{b}{}^{g}\epsilon{}_{cdefg}
\end{aligned}\tag{VE-55}
```

Identity 56: `Schouten`; this is the actual weighted relation used in the comparison.

```math
\begin{aligned}
0={}&\frac{446}{27}G{}^{ab}T{}_{b}{}^{c}T{}^{de}T{}^{fg}\epsilon{}_{cdefg}+\frac{446}{27}G{}^{bc}T{}_{bc}T{}^{de}T{}^{fg}\epsilon{}^{a}{}_{defg}-\frac{1784}{27}G{}^{bc}T{}_{b}{}^{d}T{}_{c}{}^{e}T{}^{fg}\epsilon{}^{a}{}_{defg}
\end{aligned}\tag{VE-56}
```

Identity 57: `Schouten`; this is the actual weighted relation used in the comparison.

```math
\begin{aligned}
0={}&-\frac{2672}{27}G{}^{ab}T{}_{b}{}^{c}T{}^{de}T{}^{fg}\epsilon{}_{cdefg}
\end{aligned}\tag{VE-57}
```

Identity 58: `Schouten`; this is the actual weighted relation used in the comparison.

```math
\begin{aligned}
0={}&-\frac{49}{6}\big(\nabla^{b}G{}^{ac}\big)\big(\nabla^{d}T{}^{ef}\big)\epsilon{}_{bcdef}+\frac{49}{6}\big(\nabla^{b}G{}_{b}{}^{c}\big)\big(\nabla^{d}T{}^{ef}\big)\epsilon{}^{a}{}_{cdef}+\frac{49}{6}\big(\nabla^{b}G{}^{cd}\big)\big(\nabla_{c}T{}^{ef}\big)\epsilon{}^{a}{}_{bdef} \\
&-\frac{49}{3}\big(\nabla^{b}G{}^{cd}\big)\big(\nabla^{e}T{}_{c}{}^{f}\big)\epsilon{}^{a}{}_{bdef}
\end{aligned}\tag{VE-58}
```

Identity 59: `dF=0`; this is the actual weighted relation used in the comparison.

```math
\begin{aligned}
0={}&15\big(\nabla^{b}G{}^{ac}\big)\big(\nabla^{d}T{}^{ef}\big)\epsilon{}_{bcdef}-\frac{15}{2}\big(\nabla^{a}G{}^{bc}\big)\big(\nabla^{d}T{}^{ef}\big)\epsilon{}_{bcdef}
\end{aligned}\tag{VE-59}
```

Identity 60: `Schouten`; this is the actual weighted relation used in the comparison.

```math
\begin{aligned}
0={}&-\frac{4}{3}\big(\nabla^{b}\nabla^{c}G{}^{ad}\big)T{}^{ef}\epsilon{}_{bcdef}+\frac{4}{3}\big(\nabla^{b}\nabla^{c}G{}_{b}{}^{d}\big)T{}^{ef}\epsilon{}^{a}{}_{cdef}-\frac{4}{3}\big(\nabla^{b}\nabla^{c}G{}_{c}{}^{d}\big)T{}^{ef}\epsilon{}^{a}{}_{bdef} \\
&-\frac{8}{3}\big(\nabla^{b}\nabla^{c}G{}^{de}\big)T{}_{d}{}^{f}\epsilon{}^{a}{}_{bcef}
\end{aligned}\tag{VE-60}
```

Identity 61: `dF=0`; this is the actual weighted relation used in the comparison.

```math
\begin{aligned}
0={}&\frac{16}{3}\big(\nabla^{b}\nabla^{c}G{}^{ad}\big)T{}^{ef}\epsilon{}_{bcdef}-\frac{8}{3}\big(\nabla^{b}\nabla^{a}G{}^{cd}\big)T{}^{ef}\epsilon{}_{bcdef}
\end{aligned}\tag{VE-61}
```

Identity 62: `covariant_commutator`; this is the actual weighted relation used in the comparison.

```math
\begin{aligned}
0={}&-\frac{16}{3}\big(\nabla^{b}\nabla^{c}G{}^{ad}\big)T{}^{ef}\epsilon{}_{bcdef}+\frac{8}{3}R(M){}^{abcd}G{}_{b}{}^{e}T{}^{fg}\epsilon{}_{cdefg}-\frac{32}{3}f{}^{ab}G{}^{cd}T{}^{ef}\epsilon{}_{bcdef} \\
&-\frac{32}{3}f{}^{bc}G{}_{b}{}^{d}T{}^{ef}\epsilon{}^{a}{}_{cdef}-\frac{8}{3}R(M){}^{bcde}G{}^{a}{}_{b}T{}^{fg}\epsilon{}_{cdefg}
\end{aligned}\tag{VE-62}
```

Identity 63: `covariant_commutator`; this is the actual weighted relation used in the comparison.

```math
\begin{aligned}
0={}&\big(\nabla^{b}\nabla^2 G{}^{a}{}_{b}\big)-\big(\nabla^{b}\nabla^{c}\nabla_{b}G{}^{a}{}_{c}\big)-2f{}^{bc}\big(\nabla_{b}G{}^{a}{}_{c}\big) \\
&+R(M){}^{abcd}\big(\nabla_{c}G{}_{bd}\big)-2f{}^{ab}\big(\nabla^{c}G{}_{bc}\big)
\end{aligned}\tag{VE-63}
```

Identity 64: `covariant_commutator`; this is the actual weighted relation used in the comparison.

```math
\begin{aligned}
0={}&-\big(\nabla^2 \nabla^{c}G{}^{a}{}_{c}\big)+\big(\nabla^{b}\nabla^{c}\nabla_{b}G{}^{a}{}_{c}\big)+\big(\nabla^{b}R(M){}^{ac}{}_{b}{}^{d}\big)G{}_{cd} \\
&+R(M){}^{abcd}\big(\nabla_{c}G{}_{bd}\big)+2\big(\nabla^{b}f{}^{ac}\big)G{}_{bc}-2f{}^{ab}\big(\nabla^{c}G{}_{bc}\big) \\
&+4\big(\nabla^{b}f{}_{b}{}^{c}\big)G{}^{a}{}_{c}+4f{}^{bc}\big(\nabla_{b}G{}^{a}{}_{c}\big)+2\big(\nabla^{b}f{}^{c}{}_{c}\big)G{}^{a}{}_{b} \\
&+2f{}^{b}{}_{b}\big(\nabla^{c}G{}^{a}{}_{c}\big)
\end{aligned}\tag{VE-64}
```

Identity 65: `Schouten`; this is the actual weighted relation used in the comparison.

```math
\begin{aligned}
0={}&\frac{19}{3}\big(\nabla^{a}G{}^{bc}\big)\big(\nabla^{d}T{}^{ef}\big)\epsilon{}_{bcdef}-\frac{38}{3}\big(\nabla^{b}G{}_{b}{}^{c}\big)\big(\nabla^{d}T{}^{ef}\big)\epsilon{}^{a}{}_{cdef}-\frac{19}{3}\big(\nabla^{b}G{}^{cd}\big)\big(\nabla_{b}T{}^{ef}\big)\epsilon{}^{a}{}_{cdef} \\
&+\frac{38}{3}\big(\nabla^{b}G{}^{cd}\big)\big(\nabla^{e}T{}_{b}{}^{f}\big)\epsilon{}^{a}{}_{cdef}
\end{aligned}\tag{VE-65}
```

Identity 66: `dF=0`; this is the actual weighted relation used in the comparison.

```math
\begin{aligned}
0={}&\frac{8}{3}G{}^{bc}\big(\nabla_{b}G{}^{ad}\big)T{}_{cd}-\frac{8}{3}G{}^{bc}\big(\nabla^{a}G{}_{b}{}^{d}\big)T{}_{cd}-\frac{8}{3}G{}^{bc}\big(\nabla^{d}G{}^{a}{}_{b}\big)T{}_{cd}
\end{aligned}\tag{VE-66}
```

Identity 67: `Schouten`; this is the actual weighted relation used in the comparison.

```math
\begin{aligned}
0={}&-\frac{7}{4}G{}^{bc}G{}^{de}G{}^{fg}T{}^{a}{}_{b}\epsilon{}_{cdefg}
\end{aligned}\tag{VE-67}
```

Identity 68: `Schouten`; this is the actual weighted relation used in the comparison.

```math
\begin{aligned}
0={}&-\frac{65}{72}G{}^{bc}G{}^{de}T{}^{af}T{}_{f}{}^{g}\epsilon{}_{bcdeg}+\frac{65}{18}G{}^{bc}G{}^{de}T{}_{b}{}^{f}T{}_{f}{}^{g}\epsilon{}^{a}{}_{cdeg}-\frac{65}{72}G{}^{bc}G{}^{de}\epsilon{}^{a}{}_{bcde}T^2
\end{aligned}\tag{VE-68}
```

Identity 69: `Schouten`; this is the actual weighted relation used in the comparison.

```math
\begin{aligned}
0={}&-\frac{65}{72}G{}^{bc}G{}^{de}T{}^{af}T{}_{f}{}^{g}\epsilon{}_{bcdeg}-\frac{65}{18}G{}^{bc}G{}^{de}T{}^{af}T{}_{b}{}^{g}\epsilon{}_{cdefg}
\end{aligned}\tag{VE-69}
```

Identity 70: `Schouten`; this is the actual weighted relation used in the comparison.

```math
\begin{aligned}
0={}&-5G{}^{bc}G{}^{de}T{}_{b}{}^{f}T{}_{c}{}^{g}\epsilon{}^{a}{}_{defg}+\frac{5}{2}G{}^{ab}G{}^{cd}T{}_{b}{}^{e}T{}^{fg}\epsilon{}_{cdefg}-5G{}^{bc}G{}_{b}{}^{d}T{}_{c}{}^{e}T{}^{fg}\epsilon{}^{a}{}_{defg} \\
&+\frac{5}{2}G{}^{bc}G{}^{de}T{}_{bc}T{}^{fg}\epsilon{}^{a}{}_{defg}
\end{aligned}\tag{VE-70}
```

Identity 71: `Schouten`; this is the actual weighted relation used in the comparison.

```math
\begin{aligned}
0={}&\frac{65}{18}G{}^{bc}G{}^{de}T{}_{b}{}^{f}T{}_{c}{}^{g}\epsilon{}^{a}{}_{defg}+\frac{65}{18}G{}^{bc}G{}^{de}T{}^{af}T{}_{b}{}^{g}\epsilon{}_{cdefg}-\frac{65}{9}G{}^{bc}G{}^{de}T{}_{b}{}^{f}T{}_{d}{}^{g}\epsilon{}^{a}{}_{cefg} \\
&-\frac{65}{18}G{}^{bc}G{}^{de}T{}_{b}{}^{f}T{}_{f}{}^{g}\epsilon{}^{a}{}_{cdeg}
\end{aligned}\tag{VE-71}
```

Identity 72: `Schouten`; this is the actual weighted relation used in the comparison.

```math
\begin{aligned}
0={}&-\frac{8}{3}G{}^{bc}G{}^{de}T{}_{b}{}^{f}T{}_{d}{}^{g}\epsilon{}^{a}{}_{cefg}+\frac{4}{3}G{}^{ab}G{}^{cd}T{}_{c}{}^{e}T{}^{fg}\epsilon{}_{bdefg}-\frac{4}{3}G{}^{bc}G{}_{b}{}^{d}T{}_{c}{}^{e}T{}^{fg}\epsilon{}^{a}{}_{defg} \\
&+\frac{4}{3}G{}^{bc}G{}^{de}T{}_{bd}T{}^{fg}\epsilon{}^{a}{}_{cefg}
\end{aligned}\tag{VE-72}
```

Identity 73: `Schouten`; this is the actual weighted relation used in the comparison.

```math
\begin{aligned}
0={}&-\frac{1}{4}G{}^{bc}\big(\nabla^{d}\nabla_{b}G{}^{ef}\big)\epsilon{}^{a}{}_{cdef}+\frac{1}{4}G{}^{ab}\big(\nabla^{c}\nabla^{d}G{}^{ef}\big)\epsilon{}_{bcdef}+\frac{1}{4}G{}^{bc}\big(\nabla_{b}\nabla^{d}G{}^{ef}\big)\epsilon{}^{a}{}_{cdef} \\
&+\frac{1}{2}G{}^{bc}\big(\nabla^{d}\nabla^{e}G{}_{b}{}^{f}\big)\epsilon{}^{a}{}_{cdef}
\end{aligned}\tag{VE-73}
```

Identity 74: `dF=0`; this is the actual weighted relation used in the comparison.

```math
\begin{aligned}
0={}&\frac{1}{4}G{}^{bc}\big(\nabla^{d}\nabla_{b}G{}^{ef}\big)\epsilon{}^{a}{}_{cdef}-\frac{1}{2}G{}^{bc}\big(\nabla^{d}\nabla^{e}G{}_{b}{}^{f}\big)\epsilon{}^{a}{}_{cdef}
\end{aligned}\tag{VE-74}
```

Identity 75: `covariant_commutator`; this is the actual weighted relation used in the comparison.

```math
\begin{aligned}
0={}&\frac{1}{4}G{}^{bc}\big(\nabla^{d}\nabla_{b}G{}^{ef}\big)\epsilon{}^{a}{}_{cdef}-\frac{1}{4}G{}^{bc}\big(\nabla_{b}\nabla^{d}G{}^{ef}\big)\epsilon{}^{a}{}_{cdef}-\frac{1}{2}R(M){}^{bcde}G{}_{b}{}^{f}G{}_{d}{}^{g}\epsilon{}^{a}{}_{cefg} \\
&-2f{}^{bc}G{}_{b}{}^{d}G{}^{ef}\epsilon{}^{a}{}_{cdef}
\end{aligned}\tag{VE-75}
```

Identity 76: `dF=0`; this is the actual weighted relation used in the comparison.

```math
\begin{aligned}
0={}&\frac{1}{4}G{}^{bc}\big(\nabla^2 G{}^{ef}\big)\epsilon{}^{a}{}_{bcef}-\frac{1}{2}G{}^{bc}\big(\nabla^{d}\nabla^{e}G{}_{d}{}^{f}\big)\epsilon{}^{a}{}_{bcef}
\end{aligned}\tag{VE-76}
```

Identity 77: `dF=0`; this is the actual weighted relation used in the comparison.

```math
\begin{aligned}
0={}&-\frac{16}{3}G{}^{bc}\big(\nabla^{d}G{}_{bc}\big)T{}^{a}{}_{d}-\frac{32}{3}G{}^{bc}\big(\nabla_{b}G{}_{c}{}^{d}\big)T{}^{a}{}_{d}
\end{aligned}\tag{VE-77}
```

Identity 78: `covariant_commutator`; this is the actual weighted relation used in the comparison.

```math
\begin{aligned}
0={}&-\frac{1}{2}G{}^{bc}\big(\nabla^{d}\nabla^{e}G{}_{e}{}^{f}\big)\epsilon{}^{a}{}_{bcdf}+\frac{1}{2}G{}^{bc}\big(\nabla^{d}\nabla^{e}G{}_{d}{}^{f}\big)\epsilon{}^{a}{}_{bcef}+f{}^{bc}G{}_{b}{}^{d}G{}^{ef}\epsilon{}^{a}{}_{cdef} \\
&+f{}^{b}{}_{b}G{}^{cd}G{}^{ef}\epsilon{}^{a}{}_{cdef}+\frac{1}{2}R(M){}^{bcde}G{}_{bd}G{}^{fg}\epsilon{}^{a}{}_{cefg}
\end{aligned}\tag{VE-78}
```

Identity 79: `Schouten`; this is the actual weighted relation used in the comparison.

```math
\begin{aligned}
0={}&\frac{6856}{9}G{}^{bc}T{}^{ad}T{}_{b}{}^{e}T{}^{fg}\epsilon{}_{cdefg}-\frac{1714}{9}G{}^{bc}T{}^{a}{}_{b}T{}^{de}T{}^{fg}\epsilon{}_{cdefg}
\end{aligned}\tag{VE-79}
```

Identity 80: `Schouten`; this is the actual weighted relation used in the comparison.

```math
\begin{aligned}
0={}&-\frac{1921}{27}G{}^{bc}T{}^{ad}T{}_{b}{}^{e}T{}^{fg}\epsilon{}_{cdefg}-\frac{1921}{27}G{}^{bc}T{}_{b}{}^{d}T{}_{c}{}^{e}T{}^{fg}\epsilon{}^{a}{}_{defg}+\frac{1921}{27}G{}^{bc}T{}_{b}{}^{d}T{}_{d}{}^{e}T{}^{fg}\epsilon{}^{a}{}_{cefg}
\end{aligned}\tag{VE-80}
```

Identity 81: `Schouten`; this is the actual weighted relation used in the comparison.

```math
\begin{aligned}
0={}&-\frac{2663}{27}G{}^{bc}T{}^{ad}T{}_{b}{}^{e}T{}^{fg}\epsilon{}_{cdefg}-\frac{2663}{54}G{}^{bc}T{}^{ad}T{}_{d}{}^{e}T{}^{fg}\epsilon{}_{bcefg}
\end{aligned}\tag{VE-81}
```

Identity 82: `Schouten`; this is the actual weighted relation used in the comparison.

```math
\begin{aligned}
0={}&-\frac{392}{27}G{}^{bc}T{}^{ad}T{}_{d}{}^{e}T{}^{fg}\epsilon{}_{bcefg}+\frac{784}{27}G{}^{bc}T{}_{b}{}^{d}T{}_{d}{}^{e}T{}^{fg}\epsilon{}^{a}{}_{cefg}-\frac{392}{27}G{}^{bc}T{}^{de}\epsilon{}^{a}{}_{bcde}T^2 \\
&+\frac{784}{27}G{}^{bc}T{}^{de}T{}_{d}{}^{f}T{}_{e}{}^{g}\epsilon{}^{a}{}_{bcfg}
\end{aligned}\tag{VE-82}
```

Identity 83: `Schouten`; this is the actual weighted relation used in the comparison.

```math
\begin{aligned}
0={}&\frac{22}{3}G{}^{bc}\big(\nabla^{d}\nabla^{e}T{}^{af}\big)\epsilon{}_{bcdef}-\frac{44}{3}G{}^{bc}\big(\nabla^{d}\nabla^{e}T{}_{b}{}^{f}\big)\epsilon{}^{a}{}_{cdef}-\frac{22}{3}G{}^{bc}\big(\nabla^{d}\nabla^{e}T{}_{d}{}^{f}\big)\epsilon{}^{a}{}_{bcef} \\
&+\frac{22}{3}G{}^{bc}\big(\nabla^{d}\nabla^{e}T{}_{e}{}^{f}\big)\epsilon{}^{a}{}_{bcdf}
\end{aligned}\tag{VE-83}
```

Identity 84: `covariant_commutator`; this is the actual weighted relation used in the comparison.

```math
\begin{aligned}
0={}&-\frac{10}{3}G{}^{bc}\big(\nabla^{d}\nabla^{e}T{}^{af}\big)\epsilon{}_{bcdef}+\frac{5}{3}R(M){}^{abcd}G{}^{ef}T{}_{b}{}^{g}\epsilon{}_{cdefg}-\frac{20}{3}f{}^{ab}G{}^{cd}T{}^{ef}\epsilon{}_{bcdef} \\
&-\frac{20}{3}f{}^{bc}G{}^{de}T{}_{b}{}^{f}\epsilon{}^{a}{}_{cdef}-\frac{5}{3}R(M){}^{bcde}G{}^{fg}T{}^{a}{}_{b}\epsilon{}_{cdefg}
\end{aligned}\tag{VE-84}
```

Identity 85: `Schouten`; this is the actual weighted relation used in the comparison.

```math
\begin{aligned}
0={}&\frac{7}{4}G{}^{bc}\big(\nabla^{a}\nabla^{d}T{}^{ef}\big)\epsilon{}_{bcdef}-\frac{7}{2}G{}^{bc}\big(\nabla_{b}\nabla^{d}T{}^{ef}\big)\epsilon{}^{a}{}_{cdef}-\frac{7}{4}G{}^{bc}\big(\nabla^2 T{}^{ef}\big)\epsilon{}^{a}{}_{bcef} \\
&+\frac{7}{2}G{}^{bc}\big(\nabla^{d}\nabla^{e}T{}_{d}{}^{f}\big)\epsilon{}^{a}{}_{bcef}
\end{aligned}\tag{VE-85}
```

Identity 86: `covariant_commutator`; this is the actual weighted relation used in the comparison.

```math
\begin{aligned}
0={}&-G{}^{bc}\big(\nabla^{a}\nabla^{d}T{}^{ef}\big)\epsilon{}_{bcdef}+G{}^{bc}\big(\nabla^{d}\nabla^{a}T{}^{ef}\big)\epsilon{}_{bcdef}-2R(M){}^{abcd}G{}^{ef}T{}_{c}{}^{g}\epsilon{}_{bdefg} \\
&+4f{}^{ab}G{}^{cd}T{}^{ef}\epsilon{}_{bcdef}+4f{}^{bc}G{}^{de}T{}_{b}{}^{f}\epsilon{}^{a}{}_{cdef}
\end{aligned}\tag{VE-86}
```

Identity 87: `covariant_commutator`; this is the actual weighted relation used in the comparison.

```math
\begin{aligned}
0={}&\frac{10}{3}G{}^{bc}\big(\nabla^{d}\nabla_{b}T{}^{ef}\big)\epsilon{}^{a}{}_{cdef}-\frac{10}{3}G{}^{bc}\big(\nabla_{b}\nabla^{d}T{}^{ef}\big)\epsilon{}^{a}{}_{cdef}-\frac{20}{3}R(M){}^{bcde}G{}_{b}{}^{f}T{}_{d}{}^{g}\epsilon{}^{a}{}_{cefg} \\
&-\frac{40}{3}f{}^{bc}G{}_{b}{}^{d}T{}^{ef}\epsilon{}^{a}{}_{cdef}-\frac{40}{3}f{}^{bc}G{}^{de}T{}_{b}{}^{f}\epsilon{}^{a}{}_{cdef}
\end{aligned}\tag{VE-87}
```

Identity 88: `Schouten`; this is the actual weighted relation used in the comparison.

```math
\begin{aligned}
0={}&-\frac{4}{3}\big(\nabla^{a}\nabla^{b}G{}^{cd}\big)T{}^{ef}\epsilon{}_{bcdef}+\frac{4}{3}\big(\nabla^2 G{}^{cd}\big)T{}^{ef}\epsilon{}^{a}{}_{cdef}-\frac{8}{3}\big(\nabla^{b}\nabla^{c}G{}_{b}{}^{d}\big)T{}^{ef}\epsilon{}^{a}{}_{cdef} \\
&-\frac{8}{3}\big(\nabla^{b}\nabla^{c}G{}^{de}\big)T{}_{b}{}^{f}\epsilon{}^{a}{}_{cdef}
\end{aligned}\tag{VE-88}
```

Identity 89: `dF=0`; this is the actual weighted relation used in the comparison.

```math
\begin{aligned}
0={}&\frac{2}{3}\big(\nabla^{a}\nabla^{b}G{}^{cd}\big)T{}^{ef}\epsilon{}_{bcdef}
\end{aligned}\tag{VE-89}
```

Identity 90: `Schouten`; this is the actual weighted relation used in the comparison.

```math
\begin{aligned}
0={}&3\big(\nabla^{b}\nabla^{a}G{}^{cd}\big)T{}^{ef}\epsilon{}_{bcdef}-3\big(\nabla^2 G{}^{cd}\big)T{}^{ef}\epsilon{}^{a}{}_{cdef}+6\big(\nabla^{b}\nabla^{c}G{}_{c}{}^{d}\big)T{}^{ef}\epsilon{}^{a}{}_{bdef} \\
&+6\big(\nabla^{b}\nabla^{c}G{}^{de}\big)T{}_{c}{}^{f}\epsilon{}^{a}{}_{bdef}
\end{aligned}\tag{VE-90}
```

Identity 91: `dF=0`; this is the actual weighted relation used in the comparison.

```math
\begin{aligned}
0={}&-\frac{2}{3}\big(\nabla^2 G{}^{cd}\big)T{}^{ef}\epsilon{}^{a}{}_{cdef}+\frac{4}{3}\big(\nabla^{b}\nabla^{c}G{}_{b}{}^{d}\big)T{}^{ef}\epsilon{}^{a}{}_{cdef}
\end{aligned}\tag{VE-91}
```

Identity 92: `dF=0`; this is the actual weighted relation used in the comparison.

```math
\begin{aligned}
0={}&\frac{1}{8}\big(\nabla^{b}G{}^{cd}\big)\big(\nabla_{b}G{}^{ef}\big)\epsilon{}^{a}{}_{cdef}-\frac{1}{4}\big(\nabla^{b}G{}^{cd}\big)\big(\nabla_{c}G{}^{ef}\big)\epsilon{}^{a}{}_{bdef}
\end{aligned}\tag{VE-92}
```

Identity 93: `Schouten`; this is the actual weighted relation used in the comparison.

```math
\begin{aligned}
0={}&5\big(\nabla^{b}G{}^{cd}\big)\big(\nabla^{e}T{}^{af}\big)\epsilon{}_{bcdef}-5\big(\nabla^{b}G{}^{cd}\big)\big(\nabla^{e}T{}_{b}{}^{f}\big)\epsilon{}^{a}{}_{cdef}+10\big(\nabla^{b}G{}^{cd}\big)\big(\nabla^{e}T{}_{c}{}^{f}\big)\epsilon{}^{a}{}_{bdef} \\
&+5\big(\nabla^{b}G{}^{cd}\big)\big(\nabla^{e}T{}_{e}{}^{f}\big)\epsilon{}^{a}{}_{bcdf}
\end{aligned}\tag{VE-93}
```

Identity 94: `dF=0`; this is the actual weighted relation used in the comparison.

```math
\begin{aligned}
0={}&-9\big(\nabla^{b}G{}^{cd}\big)\big(\nabla^{e}T{}^{af}\big)\epsilon{}_{bcdef}
\end{aligned}\tag{VE-94}
```

Identity 95: `dF=0`; this is the actual weighted relation used in the comparison.

```math
\begin{aligned}
0={}&\frac{32}{3}\big(\nabla^{b}G{}^{cd}\big)T{}^{a}{}_{b}T{}_{cd}-\frac{64}{3}\big(\nabla^{b}G{}^{cd}\big)T{}^{a}{}_{c}T{}_{bd}
\end{aligned}\tag{VE-95}
```

Identity 96: `dF=0`; this is the actual weighted relation used in the comparison.

```math
\begin{aligned}
0={}&\frac{5}{2}\big(\nabla^{b}G{}^{cd}\big)\big(\nabla_{b}T{}^{ef}\big)\epsilon{}^{a}{}_{cdef}-5\big(\nabla^{b}G{}^{cd}\big)\big(\nabla_{c}T{}^{ef}\big)\epsilon{}^{a}{}_{bdef}
\end{aligned}\tag{VE-96}
```

Identity 97: `Schouten`; this is the actual weighted relation used in the comparison.

```math
\begin{aligned}
0={}&-\big(\nabla^{b}\nabla^{c}G{}^{de}\big)T{}^{af}\epsilon{}_{bcdef}+\big(\nabla^{b}\nabla^{c}G{}^{de}\big)T{}_{b}{}^{f}\epsilon{}^{a}{}_{cdef}-\big(\nabla^{b}\nabla^{c}G{}^{de}\big)T{}_{c}{}^{f}\epsilon{}^{a}{}_{bdef} \\
&+2\big(\nabla^{b}\nabla^{c}G{}^{de}\big)T{}_{d}{}^{f}\epsilon{}^{a}{}_{bcef}
\end{aligned}\tag{VE-97}
```

Identity 98: `covariant_commutator`; this is the actual weighted relation used in the comparison.

```math
\begin{aligned}
0={}&\frac{4}{3}\big(\nabla^{b}\nabla^{c}G{}^{de}\big)T{}_{b}{}^{f}\epsilon{}^{a}{}_{cdef}-\frac{4}{3}\big(\nabla^{b}\nabla^{c}G{}^{de}\big)T{}_{c}{}^{f}\epsilon{}^{a}{}_{bdef}-\frac{8}{3}R(M){}^{bcde}G{}_{b}{}^{f}T{}_{d}{}^{g}\epsilon{}^{a}{}_{cefg} \\
&-\frac{16}{3}f{}^{bc}G{}^{de}T{}_{b}{}^{f}\epsilon{}^{a}{}_{cdef}-\frac{16}{3}f{}^{bc}G{}_{b}{}^{d}T{}^{ef}\epsilon{}^{a}{}_{cdef}
\end{aligned}\tag{VE-98}
```

Identity 99: `dF=0`; this is the actual weighted relation used in the comparison.

```math
\begin{aligned}
0={}&\frac{1}{2}\big(\nabla^{b}G{}_{b}{}^{c}\big)\big(\nabla^{d}G{}^{ef}\big)\epsilon{}^{a}{}_{cdef}
\end{aligned}\tag{VE-99}
```

Identity 100: `Schouten`; this is the actual weighted relation used in the comparison.

```math
\begin{aligned}
0={}&-\frac{242}{9}T{}^{ab}\big(\nabla^{c}\nabla^{d}T{}^{ef}\big)\epsilon{}_{bcdef}-\frac{242}{9}T{}^{bc}\big(\nabla_{b}\nabla^{d}T{}^{ef}\big)\epsilon{}^{a}{}_{cdef}+\frac{242}{9}T{}^{bc}\big(\nabla^{d}\nabla_{b}T{}^{ef}\big)\epsilon{}^{a}{}_{cdef} \\
&-\frac{484}{9}T{}^{bc}\big(\nabla^{d}\nabla^{e}T{}_{b}{}^{f}\big)\epsilon{}^{a}{}_{cdef}
\end{aligned}\tag{VE-100}
```

Identity 101: `covariant_commutator`; this is the actual weighted relation used in the comparison.

```math
\begin{aligned}
0={}&\frac{44}{3}T{}^{ab}\big(\nabla^{c}\nabla^{d}T{}^{ef}\big)\epsilon{}_{bcdef}-\frac{44}{3}R(M){}^{bcde}T{}^{af}T{}_{b}{}^{g}\epsilon{}_{cdefg}
\end{aligned}\tag{VE-101}
```

Identity 102: `Schouten`; this is the actual weighted relation used in the comparison.

```math
\begin{aligned}
0={}&\frac{20320}{81}T{}^{ab}T{}_{b}{}^{c}T{}^{de}T{}^{fg}\epsilon{}_{cdefg}+\frac{20320}{81}T{}^{bc}T{}^{de}\epsilon{}^{a}{}_{bcde}T^2-\frac{81280}{81}T{}^{bc}T{}_{b}{}^{d}T{}_{c}{}^{e}T{}^{fg}\epsilon{}^{a}{}_{defg}
\end{aligned}\tag{VE-102}
```

Identity 103: `Schouten`; this is the actual weighted relation used in the comparison.

```math
\begin{aligned}
0={}&\frac{29560}{27}T{}^{ab}T{}_{b}{}^{c}T{}^{de}T{}^{fg}\epsilon{}_{cdefg}
\end{aligned}\tag{VE-103}
```

Identity 104: `Schouten`; this is the actual weighted relation used in the comparison.

```math
\begin{aligned}
0={}&-\frac{431}{24}\big(\nabla^{b}T{}^{ac}\big)\big(\nabla^{d}T{}^{ef}\big)\epsilon{}_{bcdef}+\frac{431}{24}\big(\nabla^{b}T{}_{b}{}^{c}\big)\big(\nabla^{d}T{}^{ef}\big)\epsilon{}^{a}{}_{cdef}+\frac{431}{24}\big(\nabla^{b}T{}^{cd}\big)\big(\nabla_{c}T{}^{ef}\big)\epsilon{}^{a}{}_{bdef} \\
&-\frac{431}{12}\big(\nabla^{b}T{}^{cd}\big)\big(\nabla^{e}T{}_{c}{}^{f}\big)\epsilon{}^{a}{}_{bdef}
\end{aligned}\tag{VE-104}
```

Identity 105: `covariant_commutator`; this is the actual weighted relation used in the comparison.

```math
\begin{aligned}
0={}&-8\big(\nabla^{b}\nabla^2 T{}^{a}{}_{b}\big)+8\big(\nabla^{b}\nabla^{c}\nabla_{b}T{}^{a}{}_{c}\big)+16f{}^{bc}\big(\nabla_{b}T{}^{a}{}_{c}\big) \\
&-8R(M){}^{abcd}\big(\nabla_{c}T{}_{bd}\big)+16f{}^{ab}\big(\nabla^{c}T{}_{bc}\big)
\end{aligned}\tag{VE-105}
```

Identity 106: `covariant_commutator`; this is the actual weighted relation used in the comparison.

```math
\begin{aligned}
0={}&8\big(\nabla^2 \nabla^{c}T{}^{a}{}_{c}\big)-8\big(\nabla^{b}\nabla^{c}\nabla_{b}T{}^{a}{}_{c}\big)-8\big(\nabla^{b}R(M){}^{ac}{}_{b}{}^{d}\big)T{}_{cd} \\
&-8R(M){}^{abcd}\big(\nabla_{c}T{}_{bd}\big)-16\big(\nabla^{b}f{}^{ac}\big)T{}_{bc}+16f{}^{ab}\big(\nabla^{c}T{}_{bc}\big) \\
&-32\big(\nabla^{b}f{}_{b}{}^{c}\big)T{}^{a}{}_{c}-32f{}^{bc}\big(\nabla_{b}T{}^{a}{}_{c}\big)-16\big(\nabla^{b}f{}^{c}{}_{c}\big)T{}^{a}{}_{b} \\
&-16f{}^{b}{}_{b}\big(\nabla^{c}T{}^{a}{}_{c}\big)
\end{aligned}\tag{VE-106}
```

Identity 107: `Schouten`; this is the actual weighted relation used in the comparison.

```math
\begin{aligned}
0={}&-\frac{191}{24}\big(\nabla^{a}T{}^{bc}\big)\big(\nabla^{d}T{}^{ef}\big)\epsilon{}_{bcdef}+\frac{191}{12}\big(\nabla^{b}T{}_{b}{}^{c}\big)\big(\nabla^{d}T{}^{ef}\big)\epsilon{}^{a}{}_{cdef}+\frac{191}{24}\big(\nabla^{b}T{}^{cd}\big)\big(\nabla_{b}T{}^{ef}\big)\epsilon{}^{a}{}_{cdef} \\
&-\frac{191}{12}\big(\nabla^{b}T{}^{cd}\big)\big(\nabla_{c}T{}^{ef}\big)\epsilon{}^{a}{}_{bdef}
\end{aligned}\tag{VE-107}
```

Identity 108: `Schouten`; this is the actual weighted relation used in the comparison.

```math
\begin{aligned}
0={}&-\frac{308}{9}T{}^{bc}\big(\nabla^{d}\nabla^{e}T{}^{af}\big)\epsilon{}_{bcdef}+\frac{616}{9}T{}^{bc}\big(\nabla^{d}\nabla^{e}T{}_{b}{}^{f}\big)\epsilon{}^{a}{}_{cdef}+\frac{308}{9}T{}^{bc}\big(\nabla^{d}\nabla^{e}T{}_{d}{}^{f}\big)\epsilon{}^{a}{}_{bcef} \\
&-\frac{308}{9}T{}^{bc}\big(\nabla^{d}\nabla^{e}T{}_{e}{}^{f}\big)\epsilon{}^{a}{}_{bcdf}
\end{aligned}\tag{VE-108}
```

Identity 109: `covariant_commutator`; this is the actual weighted relation used in the comparison.

```math
\begin{aligned}
0={}&\frac{164}{9}T{}^{bc}\big(\nabla^{d}\nabla^{e}T{}^{af}\big)\epsilon{}_{bcdef}-\frac{82}{9}R(M){}^{abcd}T{}_{b}{}^{e}T{}^{fg}\epsilon{}_{cdefg}+\frac{328}{9}f{}^{ab}T{}^{cd}T{}^{ef}\epsilon{}_{bcdef} \\
&+\frac{328}{9}f{}^{bc}T{}_{b}{}^{d}T{}^{ef}\epsilon{}^{a}{}_{cdef}+\frac{82}{9}R(M){}^{bcde}T{}^{a}{}_{b}T{}^{fg}\epsilon{}_{cdefg}
\end{aligned}\tag{VE-109}
```

Identity 110: `Schouten`; this is the actual weighted relation used in the comparison.

```math
\begin{aligned}
0={}&-\frac{22}{3}T{}^{bc}\big(\nabla^{a}\nabla^{d}T{}^{ef}\big)\epsilon{}_{bcdef}+\frac{44}{3}T{}^{bc}\big(\nabla_{b}\nabla^{d}T{}^{ef}\big)\epsilon{}^{a}{}_{cdef}+\frac{22}{3}T{}^{bc}\big(\nabla^2 T{}^{ef}\big)\epsilon{}^{a}{}_{bcef} \\
&-\frac{44}{3}T{}^{bc}\big(\nabla^{d}\nabla^{e}T{}_{d}{}^{f}\big)\epsilon{}^{a}{}_{bcef}
\end{aligned}\tag{VE-110}
```

Identity 111: `covariant_commutator`; this is the actual weighted relation used in the comparison.

```math
\begin{aligned}
0={}&\frac{50}{9}T{}^{bc}\big(\nabla^{a}\nabla^{d}T{}^{ef}\big)\epsilon{}_{bcdef}-\frac{50}{9}T{}^{bc}\big(\nabla^{d}\nabla^{a}T{}^{ef}\big)\epsilon{}_{bcdef}+\frac{100}{9}R(M){}^{abcd}T{}_{c}{}^{e}T{}^{fg}\epsilon{}_{bdefg} \\
&-\frac{200}{9}f{}^{ab}T{}^{cd}T{}^{ef}\epsilon{}_{bcdef}-\frac{200}{9}f{}^{bc}T{}_{b}{}^{d}T{}^{ef}\epsilon{}^{a}{}_{cdef}
\end{aligned}\tag{VE-111}
```

Identity 112: `covariant_commutator`; this is the actual weighted relation used in the comparison.

```math
\begin{aligned}
0={}&-\frac{160}{9}T{}^{bc}\big(\nabla^{d}\nabla_{b}T{}^{ef}\big)\epsilon{}^{a}{}_{cdef}+\frac{160}{9}T{}^{bc}\big(\nabla_{b}\nabla^{d}T{}^{ef}\big)\epsilon{}^{a}{}_{cdef}+\frac{320}{9}R(M){}^{bcde}T{}_{b}{}^{f}T{}_{d}{}^{g}\epsilon{}^{a}{}_{cefg} \\
&+\frac{1280}{9}f{}^{bc}T{}_{b}{}^{d}T{}^{ef}\epsilon{}^{a}{}_{cdef}
\end{aligned}\tag{VE-112}
```

Identity 113: `Schouten`; this is the actual weighted relation used in the comparison.

```math
\begin{aligned}
0={}&\frac{13}{64}R(M){}^{abcd}G{}_{b}{}^{e}G{}^{fg}\epsilon{}_{cdefg}
\end{aligned}\tag{VE-113}
```

Identity 114: `Schouten`; this is the actual weighted relation used in the comparison.

```math
\begin{aligned}
0={}&-\frac{5}{18}R(M){}^{abcd}T{}_{b}{}^{e}T{}^{fg}\epsilon{}_{cdefg}
\end{aligned}\tag{VE-114}
```

Identity 115: `contracted_Ricci_Bianchi`; this is the actual weighted relation used in the comparison.

```math
\begin{aligned}
0={}&-5\big(\nabla^{b}f{}_{b}{}^{c}\big)G{}^{a}{}_{c}+5\big(\nabla^{b}f{}^{c}{}_{c}\big)G{}^{a}{}_{b}
\end{aligned}\tag{VE-115}
```

Identity 116: `dF=0`; this is the actual weighted relation used in the comparison.

```math
\begin{aligned}
0={}&-\frac{1}{4}G{}^{ab}\big(\nabla^{c}\nabla^{d}G{}^{ef}\big)\epsilon{}_{bcdef}
\end{aligned}\tag{VE-116}
```

### Full gauged density with boundary current removed

Identity 1: `Schouten`; this is the actual weighted relation used in the comparison.

```math
\begin{aligned}
0={}&-\frac{89}{576}H{}^{ab}\big(\nabla_{a}H{}^{cd}\big)G{}^{ef}\epsilon{}_{bcdef}+\frac{89}{288}H{}^{ab}\big(\nabla^{c}H{}_{a}{}^{d}\big)G{}^{ef}\epsilon{}_{bcdef}+\frac{89}{288}H{}^{ab}\big(\nabla^{c}H{}^{de}\big)G{}_{a}{}^{f}\epsilon{}_{bcdef}
\end{aligned}\tag{BF-1}
```

Identity 2: `Schouten`; this is the actual weighted relation used in the comparison.

```math
\begin{aligned}
0={}&\frac{23}{576}H{}^{ab}\big(\nabla_{a}H{}^{cd}\big)G{}^{ef}\epsilon{}_{bcdef}+\frac{23}{576}H{}^{ab}\big(\nabla^{c}H{}_{c}{}^{d}\big)G{}^{ef}\epsilon{}_{abdef}+\frac{23}{576}H{}^{ab}\big(\nabla^{c}H{}^{de}\big)G{}_{c}{}^{f}\epsilon{}_{abdef}
\end{aligned}\tag{BF-2}
```

Identity 3: `gauged_H_Bianchi`; this is the actual weighted relation used in the comparison.

```math
\begin{aligned}
0={}&\frac{4}{3}H{}^{ab}H{}^{cd}\big(\nabla^{e}H{}_{e}{}^{f}\big)\epsilon{}_{abcdf}+\frac{2}{3}H{}^{ab}H{}^{cd}G{}_{ab}G{}_{cd}-\frac{4}{3}H{}^{ab}H{}^{cd}G{}_{ac}G{}_{bd} \\
&+\frac{2}{3}gH{}^{ab}H{}^{cd}E_c{}^{e}\epsilon{}_{abcde}
\end{aligned}\tag{BF-3}
```

Identity 4: `algebraic_Bianchi`; this is the actual weighted relation used in the comparison.

```math
\begin{aligned}
0={}&-\frac{11}{18}H{}^{ab}H{}^{cd}R(M){}_{abcd}+\frac{11}{9}H{}^{ab}H{}^{cd}R(M){}_{acbd}
\end{aligned}\tag{BF-4}
```

Identity 5: `Schouten`; this is the actual weighted relation used in the comparison.

```math
\begin{aligned}
0={}&-\frac{19}{24}H{}^{ab}\big(\nabla^{c}H{}^{de}\big)G{}_{a}{}^{f}\epsilon{}_{bcdef}-\frac{19}{48}H{}^{ab}\big(\nabla^{c}H{}^{de}\big)G{}_{c}{}^{f}\epsilon{}_{abdef}+\frac{19}{24}H{}^{ab}\big(\nabla^{c}H{}^{de}\big)G{}_{d}{}^{f}\epsilon{}_{abcef}
\end{aligned}\tag{BF-5}
```

Identity 6: `covariant_commutator`; this is the actual weighted relation used in the comparison.

```math
\begin{aligned}
0={}&\frac{16}{9}H{}^{ab}\big(\nabla^{c}\nabla_{a}H{}_{bc}\big)-\frac{16}{9}H{}^{ab}\big(\nabla_{a}\nabla^{c}H{}_{bc}\big)-\frac{16}{9}H{}^{ab}H{}^{cd}R(M){}_{acbd} \\
&-\frac{32}{9}H{}^{ab}H{}_{a}{}^{c}f{}_{bc}-\frac{32}{9}H{}^{ab}H{}_{ab}f{}^{c}{}_{c}
\end{aligned}\tag{BF-6}
```

Identity 7: `Schouten`; this is the actual weighted relation used in the comparison.

```math
\begin{aligned}
0={}&\frac{1}{16}H{}^{ab}\big(\nabla_{a}R(M){}^{cdef}\big)\epsilon{}_{bcdef}-\frac{1}{4}H{}^{ab}\big(\nabla^{c}R(M){}_{a}{}^{def}\big)\epsilon{}_{bcdef}
\end{aligned}\tag{BF-7}
```

Identity 8: `Schouten`; this is the actual weighted relation used in the comparison.

```math
\begin{aligned}
0={}&-\frac{3}{16}H{}^{ab}\big(\nabla_{a}R(M){}^{cdef}\big)\epsilon{}_{bcdef}-\frac{3}{8}H{}^{ab}\big(\nabla^{c}R(M){}_{c}{}^{def}\big)\epsilon{}_{abdef}
\end{aligned}\tag{BF-8}
```

Identity 9: `algebraic_Bianchi`; this is the actual weighted relation used in the comparison.

```math
\begin{aligned}
0={}&-\frac{1}{8}H{}^{ab}\big(\nabla_{a}R(M){}^{cdef}\big)\epsilon{}_{bcdef}
\end{aligned}\tag{BF-9}
```

Identity 10: `algebraic_Bianchi`; this is the actual weighted relation used in the comparison.

```math
\begin{aligned}
0={}&\frac{49}{36}H{}^{ab}R(M){}_{a}{}^{c}{}_{b}{}^{d}G{}_{cd}-\frac{49}{72}H{}^{ab}R(M){}_{ab}{}^{cd}G{}_{cd}
\end{aligned}\tag{BF-10}
```

Identity 11: `Schouten`; this is the actual weighted relation used in the comparison.

```math
\begin{aligned}
0={}&\frac{161}{1152}H{}^{ab}G{}^{cd}\big(\nabla_{a}G{}^{ef}\big)\epsilon{}_{bcdef}+\frac{161}{576}H{}^{ab}G{}_{a}{}^{c}\big(\nabla^{d}G{}^{ef}\big)\epsilon{}_{bcdef}-\frac{161}{576}H{}^{ab}G{}^{cd}\big(\nabla^{e}G{}_{a}{}^{f}\big)\epsilon{}_{bcdef}
\end{aligned}\tag{BF-11}
```

Identity 12: `Schouten`; this is the actual weighted relation used in the comparison.

```math
\begin{aligned}
0={}&-\frac{287}{1152}H{}^{ab}G{}^{cd}\big(\nabla_{a}G{}^{ef}\big)\epsilon{}_{bcdef}-\frac{287}{1152}H{}^{ab}G{}^{cd}\big(\nabla_{c}G{}^{ef}\big)\epsilon{}_{abdef}-\frac{287}{1152}H{}^{ab}G{}^{cd}\big(\nabla^{e}G{}_{e}{}^{f}\big)\epsilon{}_{abcdf}
\end{aligned}\tag{BF-12}
```

Identity 13: `dF=0`; this is the actual weighted relation used in the comparison.

```math
\begin{aligned}
0={}&\frac{1}{6}H{}^{ab}G{}^{cd}\big(\nabla_{a}G{}^{ef}\big)\epsilon{}_{bcdef}-\frac{1}{3}H{}^{ab}G{}^{cd}\big(\nabla^{e}G{}_{a}{}^{f}\big)\epsilon{}_{bcdef}
\end{aligned}\tag{BF-13}
```

Identity 14: `Schouten`; this is the actual weighted relation used in the comparison.

```math
\begin{aligned}
0={}&-\frac{3}{32}H{}^{ab}G{}^{cd}\big(\nabla_{c}G{}^{ef}\big)\epsilon{}_{abdef}+\frac{3}{16}H{}^{ab}G{}_{a}{}^{c}\big(\nabla^{d}G{}^{ef}\big)\epsilon{}_{bcdef}+\frac{3}{16}H{}^{ab}G{}^{cd}\big(\nabla^{e}G{}_{c}{}^{f}\big)\epsilon{}_{abdef}
\end{aligned}\tag{BF-14}
```

Identity 15: `dF=0`; this is the actual weighted relation used in the comparison.

```math
\begin{aligned}
0={}&\frac{2}{3}H{}^{ab}\big(\nabla^2 G{}_{ab}\big)+\frac{4}{3}H{}^{ab}\big(\nabla^{c}\nabla_{a}G{}_{bc}\big)
\end{aligned}\tag{BF-15}
```

Identity 16: `covariant_commutator`; this is the actual weighted relation used in the comparison.

```math
\begin{aligned}
0={}&-\frac{14}{9}H{}^{ab}\big(\nabla^{c}\nabla_{a}G{}_{bc}\big)+\frac{14}{9}H{}^{ab}\big(\nabla_{a}\nabla^{c}G{}_{bc}\big)+\frac{14}{9}H{}^{ab}R(M){}_{a}{}^{c}{}_{b}{}^{d}G{}_{cd} \\
&-\frac{28}{9}H{}^{ab}f{}_{a}{}^{c}G{}_{bc}+\frac{28}{9}H{}^{ab}f{}^{c}{}_{c}G{}_{ab}
\end{aligned}\tag{BF-16}
```

Identity 17: `Schouten`; this is the actual weighted relation used in the comparison.

```math
\begin{aligned}
0={}&\frac{265}{576}\big(\nabla^{a}H{}^{bc}\big)G{}_{a}{}^{d}G{}^{ef}\epsilon{}_{bcdef}+\frac{265}{1152}\big(\nabla^{a}H{}_{a}{}^{b}\big)G{}^{cd}G{}^{ef}\epsilon{}_{bcdef}
\end{aligned}\tag{BF-17}
```

Identity 18: `Schouten`; this is the actual weighted relation used in the comparison.

```math
\begin{aligned}
0={}&\frac{317}{1152}\big(\nabla^{a}H{}^{bc}\big)G{}_{a}{}^{d}G{}^{ef}\epsilon{}_{bcdef}-\frac{317}{576}\big(\nabla^{a}H{}^{bc}\big)G{}_{b}{}^{d}G{}^{ef}\epsilon{}_{acdef}
\end{aligned}\tag{BF-18}
```

Identity 19: `dF=0`; this is the actual weighted relation used in the comparison.

```math
\begin{aligned}
0={}&-\frac{13}{3}\big(\nabla^{a}H{}^{bc}\big)\big(\nabla_{b}G{}_{ac}\big)+\frac{13}{6}\big(\nabla^{a}H{}^{bc}\big)\big(\nabla_{a}G{}_{bc}\big)
\end{aligned}\tag{BF-19}
```

Identity 20: `gauged_H_Bianchi`; this is the actual weighted relation used in the comparison.

```math
\begin{aligned}
0={}&-\frac{4}{3}\big(\nabla^{a}H{}_{a}{}^{b}\big)\big(\nabla^{c}H{}_{bc}\big)-\frac{1}{12}\big(\nabla^{a}H{}_{a}{}^{b}\big)G{}^{cd}G{}^{ef}\epsilon{}_{bcdef}+\frac{2}{3}g\big(\nabla^{a}H{}_{a}{}^{b}\big)E_c{}_{b}
\end{aligned}\tag{BF-20}
```

Identity 21: `gauged_H_Bianchi`; this is the actual weighted relation used in the comparison.

```math
\begin{aligned}
0={}&-\frac{2}{3}\big(\nabla^{a}H{}_{a}{}^{b}\big)\big(\nabla^{c}G{}_{bc}\big)-\frac{1}{24}G{}^{ab}G{}^{cd}\big(\nabla^{e}G{}_{e}{}^{f}\big)\epsilon{}_{abcdf}-\frac{1}{3}gE_c{}^{a}\big(\nabla^{b}G{}_{ab}\big)
\end{aligned}\tag{BF-21}
```

Identity 22: `covariant_commutator`; this is the actual weighted relation used in the comparison.

```math
\begin{aligned}
0={}&-\frac{22}{9}\big(\nabla^{a}\nabla^{b}H{}_{a}{}^{c}\big)G{}_{bc}+\frac{22}{9}\big(\nabla^{a}\nabla^{b}H{}_{b}{}^{c}\big)G{}_{ac}-\frac{44}{9}H{}^{ab}f{}^{c}{}_{c}G{}_{ab} \\
&+\frac{44}{9}H{}^{ab}f{}_{a}{}^{c}G{}_{bc}-\frac{22}{9}H{}^{ab}R(M){}_{a}{}^{c}{}_{b}{}^{d}G{}_{cd}
\end{aligned}\tag{BF-22}
```

Identity 23: `algebraic_Bianchi`; this is the actual weighted relation used in the comparison.

```math
\begin{aligned}
0={}&\frac{17}{144}R(M){}^{abcd}G{}_{ab}G{}_{cd}-\frac{17}{72}R(M){}^{abcd}G{}_{ac}G{}_{bd}
\end{aligned}\tag{BF-23}
```

Identity 24: `Schouten`; this is the actual weighted relation used in the comparison.

```math
\begin{aligned}
0={}&-\frac{3}{64}\big(\nabla^{a}R(M){}^{bcde}\big)G{}_{a}{}^{f}\epsilon{}_{bcdef}-\frac{3}{32}\big(\nabla^{a}R(M){}_{a}{}^{bcd}\big)G{}^{ef}\epsilon{}_{bcdef}
\end{aligned}\tag{BF-24}
```

Identity 25: `Schouten`; this is the actual weighted relation used in the comparison.

```math
\begin{aligned}
0={}&\frac{1}{64}\big(\nabla^{a}R(M){}^{bcde}\big)G{}_{a}{}^{f}\epsilon{}_{bcdef}-\frac{1}{16}\big(\nabla^{a}R(M){}^{bcde}\big)G{}_{b}{}^{f}\epsilon{}_{acdef}
\end{aligned}\tag{BF-25}
```

Identity 26: `algebraic_Bianchi`; this is the actual weighted relation used in the comparison.

```math
\begin{aligned}
0={}&-\frac{1}{32}\big(\nabla^{a}R(M){}^{bcde}\big)G{}_{a}{}^{f}\epsilon{}_{bcdef}
\end{aligned}\tag{BF-26}
```

Identity 27: `SU2_triplet_quartic`; this is the actual weighted relation used in the comparison.

```math
\begin{aligned}
0={}&\frac{1}{8}g^4L_c{}^{ij}L_c{}_{i}{}^{k}L_c{}_{j}{}^{l}L_c{}_{kl}-\frac{1}{16}g^4L_c{}^{ij}L_c{}_{ij}L_c{}^{kl}L_c{}_{kl}
\end{aligned}\tag{BF-27}
```

Identity 28: `Schouten`; this is the actual weighted relation used in the comparison.

```math
\begin{aligned}
0={}&-\frac{245}{2304}G{}^{ab}G{}^{cd}\big(\nabla_{a}G{}^{ef}\big)\epsilon{}_{bcdef}+\frac{245}{1152}G{}^{ab}G{}^{cd}\big(\nabla^{e}G{}_{a}{}^{f}\big)\epsilon{}_{bcdef}
\end{aligned}\tag{BF-28}
```

Identity 29: `Schouten`; this is the actual weighted relation used in the comparison.

```math
\begin{aligned}
0={}&\frac{143}{1152}G{}^{ab}G{}^{cd}\big(\nabla_{a}G{}^{ef}\big)\epsilon{}_{bcdef}+\frac{143}{2304}G{}^{ab}G{}^{cd}\big(\nabla^{e}G{}_{e}{}^{f}\big)\epsilon{}_{abcdf}
\end{aligned}\tag{BF-29}
```

Identity 30: `dF=0`; this is the actual weighted relation used in the comparison.

```math
\begin{aligned}
0={}&-\frac{5}{12}G{}^{ab}\big(\nabla^2 G{}_{ab}\big)-\frac{5}{6}G{}^{ab}\big(\nabla^{c}\nabla_{a}G{}_{bc}\big)
\end{aligned}\tag{BF-30}
```

Identity 31: `covariant_commutator`; this is the actual weighted relation used in the comparison.

```math
\begin{aligned}
0={}&-\frac{7}{18}G{}^{ab}\big(\nabla^{c}\nabla_{a}G{}_{bc}\big)+\frac{7}{18}G{}^{ab}\big(\nabla_{a}\nabla^{c}G{}_{bc}\big)+\frac{7}{18}R(M){}^{abcd}G{}_{ac}G{}_{bd} \\
&+\frac{7}{9}f{}^{ab}G{}_{a}{}^{c}G{}_{bc}+\frac{7}{9}f{}^{a}{}_{a}G^2
\end{aligned}\tag{BF-31}
```

Identity 32: `dF=0`; this is the actual weighted relation used in the comparison.

```math
\begin{aligned}
0={}&\frac{13}{6}\big(\nabla^{a}G{}^{bc}\big)\big(\nabla_{b}G{}_{ac}\big)-\frac{13}{12}\big(\nabla^{a}G{}^{bc}\big)\big(\nabla_{a}G{}_{bc}\big)
\end{aligned}\tag{BF-32}
```

Identity 33: `gauged_H_Bianchi`; this is the actual weighted relation used in the comparison.

```math
\begin{aligned}
0={}&-\frac{2}{3}g\big(\nabla^{a}H{}_{a}{}^{b}\big)E_c{}_{b}+\frac{1}{24}gE_c{}^{a}G{}^{bc}G{}^{de}\epsilon{}_{abcde}-\frac{1}{3}g^2E_c{}^{a}E_c{}_{a}
\end{aligned}\tag{BF-33}
```
