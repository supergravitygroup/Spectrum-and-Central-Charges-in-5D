# Özkan 1608 anchor for the $`\mathcal F_{AB}(L)`$ constraints and local composite

> **Status:** source anchor only  
> **Lock:** `OZKAN1608-FAB-LOCAL-COMPOSITE-SOURCE-v2`  
> **Mapping status:** constructed separately under `OZKAN1608-SINGLE-LINEAR-TO-VECTOR-MAP-v2`  
> **Action status:** constructed separately in file 05; this remains a source-only anchor

This document gives arXiv:1608.00349 a deliberately narrow role. It is used
only for

1. the constraints on the general function $`\mathcal F_{AB}(L)`$; and
2. the complete local-supergravity linear-to-vector composite in Eq. (3.14).

The vector--linear density, conformal d'Alembertians, supercovariant
derivatives, curvatures, and dependent connections continue to be taken from
the older project source anchors. No mapping component is evaluated in this
source-anchor document. The downstream calculation does not alter this
lock's source-only certification boundary.

## 1. Canonical local source

| Item | Value |
| --- | --- |
| Author | Mehmet Özkan |
| Title | *Off-Shell N = 2 Linear Multiplets in Five Dimensions* |
| arXiv | `1608.00349v2 [hep-th]`, 26 November 2016 |
| Source PDF | [Özkan (2016)](../../../../../../references/bibliography.md#Ozkan2016); the fingerprint below identifies the inspected source, which is not bundled |
| PDF pages | 22 |
| File size | 242991 bytes |
| SHA-256 | `a750540743e89e5a128b3939b8df9de18aa9df5c44c3096e735d7b20102ba0a2` |
| Official URL | <https://arxiv.org/abs/1608.00349> |

## 2. Exact allowed-use ledger for arXiv:1608.00349

“PDF page” is the one-based page number in the local PDF viewer. “Printed
page” is the page number printed in the article.

| Allowed purpose | Equation | Local page |
| --- | --- | --- |
| Lowest component used to initiate the composite construction | Eq. (2.5) | PDF p. 5, printed p. 4 |
| Definitions of derivatives of $`\mathcal F_{AB}`$ | Eq. (2.6) | PDF p. 5, printed p. 4 |
| Dilatation-weight condition | Eq. (2.7) | PDF p. 5, printed p. 4 |
| S-supersymmetry constraints | Eq. (2.8) | PDF p. 5, printed p. 4 |
| Q-descendant used in constructing the composite | Eq. (2.9) | PDF p. 5, printed p. 4 |
| Higher-derivative epsilon-trace condition | Eq. (2.10) | PDF p. 5, printed p. 4 |
| Collected four constraints on $`\mathcal F_{AB}(L)`$ | Eq. (2.11) | PDF pp. 5–6, printed pp. 4–5 |
| Complete local composite $`(\rho_A,\lambda_{iA},Y_{ijA},\widehat F_{\mu\nu A})`$ | Eq. (3.14) | PDF p. 9, printed p. 8 |

Equation (2.12), the rigid composite, is not an active formula anchor for the
supergravity mapping. It may later be used only as a rigid-limit check of the
local Eq. (3.14).

## 3. The $`\mathcal F_{AB}(L)`$ source contract

The downstream derivation begins with the definitions in Eq. (2.6) and verifies
all four conditions collected in Eq. (2.11):

- Weyl weight $`-3`$;
- the stated symmetry of the first derivative in multiplet labels;
- the contraction condition with $`L^C_{ij}`$;
- the epsilon-trace condition on the second derivative.

The single-linear-multiplet statement below Eq. (2.8),

```math
\mathcal F_{AB}=\delta_{AB}L^{-1},
\qquad
L^2=L_{ij}L^{ij},
```

is specialized in the downstream single-multiplet calculation. Neither this
function nor any of its derivatives is evaluated in the present document.

## 4. The local composite source contract

Equation (3.14) is the sole 2016 anchor for the local-supergravity composite
vector

```math
(\rho_A,\lambda_{iA},Y_{ijA},\widehat F_{\mu\nu A}).
```

The downstream derivation transcribes Eq. (3.14) term by term and interprets
its density, derivatives, d'Alembertian, curvatures, and dependent connections
using the older anchors listed below. Those supporting objects must not be
re-sourced to the 2016 paper merely because they are also printed there. The
completed result is anchored by `OZKAN1608-SINGLE-LINEAR-TO-VECTOR-MAP-v2`.

## 5. Older anchors retained for all supporting structures

The active older source lock is

`OZKAN-GB13-DW-PSI0-v2`,

with canonical ledger

`results/two_derivative_fermionic_action/03_ozkan_gb_psi_gauge_source_anchor.md`.

### 5.1 Vector--linear density and boundary representative

Use corrected Özkan--Pang arXiv:1301.6622v4:

- Eq. (3.1), printed p. 10: complete vector--linear density;
- Eq. (3.2), printed p. 10: boundary-equivalent field-strength
  representative.

### 5.2 Conformal d'Alembertians

Use corrected Özkan--Pang arXiv:1301.6622v4:

- Eq. (2.10), printed p. 7: $`\square^C\sigma`$ and the dependent
  $`f_\mu{}^a`$ relation;
- Eq. (3.6), printed p. 11: the conformal d'Alembertian of the linear
  multiplet entering the linear-to-vector composite.

### 5.3 Standard- and Dilaton-Weyl derivatives and field strengths

Use corrected Özkan--Pang arXiv:1301.6622v4:

- Eqs. (2.1)–(2.4), printed pp. 5–6: Dilaton-Weyl transformations,
  derivatives, and supercovariant field strengths;
- Eqs. (2.14)–(2.16), printed p. 8: vector-multiplet derivatives and field
  strength;
- Eqs. (2.18)–(2.22), printed pp. 8–9: linear-multiplet transformations,
  derivatives, constraint, and form representative.

For gauging-dependent deformations, use Coomans–Özkan arXiv:1210.4704v3,
especially Eqs. (2.15)–(2.21) and (5.2)–(5.7), only after the ungauged local
composite has been fixed.

### 5.4 Curvatures and dependent connections

Use corrected Özkan--Pang arXiv:1301.6622v4:

- Eqs. (2.5)–(2.7), printed pp. 6–7: $`\omega_\mu{}^{ab}`$,
  $`\phi_\mu{}^i`$, $`\widehat R(Q)`$, $`\widehat R(M)`$, and
  $`\widehat R(V)`$;
- Eqs. (2.9)–(2.10), printed p. 7: $`T_{ab}`$, $`\chi^i`$, $`D`$, and
  $`f_\mu{}^a`$.

Retain the project-derived correction

```math
\widehat R'_{\mu\nu}{}^{ab}(M)\big|_\chi
=+8\bar\psi_{[\mu}e_{\nu]}{}^{[a}\gamma^{b]}\chi,
```

whose audit is recorded in the older source ledger and anchored independently
to the five-dimensional Weyl-multiplet source. It is not classified as a
published erratum.

## 6. Convention boundary

The later construction retains

```math
A^i=\varepsilon^{ij}A_j,
\qquad
A_i=A^j\varepsilon_{ji},
\qquad
\varepsilon_{12}=\varepsilon^{12}=1.
```

Every one-index raising or lowering operation must be shown explicitly. The
2016 paper does not replace any convention correction already certified in
the older project chain.

## 7. Explicit source-anchor boundary

In this document:

- no $`\mathcal F_{AB}`$ derivative is evaluated;
- no component of Eq. (3.14) is specialized;
- no gauged Dilaton-Weyl expression is substituted;
- no density is evaluated;
- no gauge is imposed;
- no action, perturbation, diagonalization, or spectrum is constructed.

Thus `OZKAN1608-FAB-LOCAL-COMPOSITE-SOURCE-v2` remains a source lock only.
The separately derived component map does not retroactively become part of
this source lock.
