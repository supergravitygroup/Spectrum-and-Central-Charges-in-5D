# Single-linear-multiplet choice for the Özkan local composite

> **Status:** project specialization source anchor; completed map certified by the successor lock below  
> **Lock:** `OZKAN1608-SINGLE-LINEAR-PROJECT-SOURCE-v3`  
> **Parent source lock:** `OZKAN1608-FAB-LOCAL-COMPOSITE-SOURCE-v2`  
> **Mapping status:** source choice anchored here; all four component slots completed in the calculation and certified by the mapping anchor below

> **Canonical component calculation:**
> `02_single_linear_multiplet_mapping_construction.md`  
> **Active mapping anchor:**
> `03_single_linear_multiplet_linear_map_anchor.md`, lock
> `OZKAN1608-SINGLE-LINEAR-TO-VECTOR-MAP-v2`

## 1. Source equation required by the project

The project will use Mehmet Özkan,
*Off-Shell N = 2 Linear Multiplets in Five Dimensions*,
arXiv:1608.00349v2, Eq. (2.15):

```math
\mathcal F_{AB}=L^{-1}\delta_{AB}.
```

Source location:

- local file:
  `Sources/2016-Ozkan-Off-Shell N=2 Linear Multiplets in Five Dimensions.pdf`;
- PDF p. 6;
- printed p. 5;
- Eq. (2.15).

The paragraph introducing Eq. (2.15) describes it as the non-interacting
choice for $`N`$ linear multiplets.

## 2. Project restriction to one linear multiplet

This project will work with exactly one linear multiplet. Therefore all
multiplet labels take the single value

```math
A=B=C=D=1.
```

Equation (2.15) consequently specializes to

```math
\mathcal F_{11}=L^{-1}.
```

Here the scalar norm is the source norm already recorded below Eq. (2.8):

```math
L^2=L_{ij}L^{ij}.
```

These equations fix the function used by the completed mapping calculation.
They are not themselves an evaluation of its derivatives or a construction
of the composite vector; those derived results belong to the separately
locked calculation and mapping anchor.

The one retained linear multiplet is the existing source multiplet

```math
(L^{ij},\varphi^i,E_a,N).
```

No additional multiplet, field, compensator, parameter, or label is
introduced.

## 3. Consequences for the mapping derivation

The mapping derivation proceeded in this order:

1. start from the general constraints in Özkan 2016 Eqs. (2.5)–(2.11);
2. verify that the Eq. (2.15) single-multiplet choice obeys them;
3. set the multiplet labels to $`A=B=C=D=1`$;
4. calculate the required derivatives of $`\mathcal F_{11}=L^{-1}`$;
5. substitute them into the general local composite of Eq. (3.14).

All five steps have now been carried out in
`02_single_linear_multiplet_mapping_construction.md`.  The resulting four
component slots are certified for downstream use by
`03_single_linear_multiplet_linear_map_anchor.md`, lock
`OZKAN1608-SINGLE-LINEAR-TO-VECTOR-MAP-v2`.  No part of that calculation is
retroactively attributed to this source-only anchor.

The multi-linear-multiplet and off-diagonal choices, including Eq. (2.14),
are outside the active construction. They may be retained only as source
context or cross-checks.

## 4. Supporting-source division remains unchanged

The 2016 paper supplies only:

- the $`\mathcal F_{AB}(L)`$ construction and constraints;
- the single-multiplet function in Eq. (2.15);
- the complete local composite in Eq. (3.14).

The following remain controlled by the older source lock
`OZKAN-GB13-DW-PSI0-v2`:

- vector--linear density and its boundary representative;
- conformal d'Alembertians;
- Standard- and Dilaton-Weyl derivatives;
- vector- and linear-multiplet derivatives;
- supercovariant curvatures;
- dependent connections.

The older canonical ledger is
`results/two_derivative_fermionic_action/03_ozkan_gb_psi_gauge_source_anchor.md`.

## 5. Index convention

The project continues to use

```math
A^i=\varepsilon^{ij}A_j,
\qquad
A_i=A^j\varepsilon_{ji},
\qquad
\varepsilon_{12}=\varepsilon^{12}=1.
```

The multiplet labels $`A,B,\ldots`$ are not $`SU(2)`$ indices. Restricting
them to the single value 1 does not alter any NW--SE raising or lowering rule.

## 6. Certification boundary

This anchor certifies only the intended use of Eq. (2.15) and the choice of a
single linear multiplet.  The separately locked component calculation and
mapping anchor certify the derivative tower and the four component slots.
This source-choice anchor itself does not certify:

- any slot of the local composite;
- gauged composite substitutions;
- a density or action;
- gauge fixing;
- perturbation theory or spectrum analysis.
