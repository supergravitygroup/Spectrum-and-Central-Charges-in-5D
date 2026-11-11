# Confirmed framework for constructing the full fermionic gauged R² action

**2026-09-10 correction:** use [the component derivation guide](../../../../derivations/README.md), lock `R2-VL-GRADIENT-PHASE-v1`. Steps 2–4 use the revised v2 locks. The printed source is preserved; active scalar-gradient coefficients are $`i/4`$. The Gold-gauge endpoint is unchanged.

## 1. Multiplets and the meaning of primes

Use the stated primed/unprimed notation, with the vector component names of the source map:

```math
\begin{aligned}
\text{vector label }1&:\quad (Y'_{ij},\rho',A'_\mu,\lambda'^i),\\
\text{vector label }2&:\quad (Y_{ij},\rho,A_\mu,\lambda^i),\\
\text{original unprimed linear multiplet}&:\quad (L_{ij},\varphi_i,E^a,N),\\
\text{new primed linear multiplet}&:\quad (L'_{ij},\varphi'_i,E'^a,N').
\end{aligned}
```

The primed vector is the composite obtained from the earlier **linear-to-vector** map. The unprimed vector is the defining vector identified by **Gold Eq. (4)**. The primed linear multiplet is the new output of the mixed **vector-to-linear** map, Özkan Eq. (3.20).

The original unprimed linear multiplet entering the earlier linear-to-vector map is the **same** unprimed linear multiplet appearing in Gold Eq. (4). In particular both uses of $`L_{ij}`$ refer to the same field. This does not replace the earlier map's input $`L_{ij}`$ with the new output $`L'_{ij}`$.

The resulting composite expressions use common underlying unprimed fields **after the respective maps are substituted**. Do not identify $`\rho'`$ with $`\rho`$, $`\lambda'^i`$ with $`\lambda^i`$, $`Y'_{ij}`$ with $`Y_{ij}`$, or their field strengths/derivatives before that substitution. Primes distinguish composite roles, not a second set of underlying compensator fields. No additional aliases or invented field names are needed.

The prime on $`\varphi'_i`$ denotes the new linear fermion; $`\lambda'^i`$ denotes the composite vector fermion. The gravitino remains $`\psi_\mu^i`$ and the dependent S connection remains $`\phi_\mu^i`$.

## 2. Fixed vector labels and coefficients

```math
A=1,\qquad B,C\in\{1,2\},\qquad
C_{111}=C_{122}=0,\qquad C_{112}=C_{121}=\frac12.
```

| Ordered pair $`(B,C)`$ | $`B`$ entry | $`C`$ entry | Weight |
|---|---|---|---|
| $`(1,2)`$ | Primed vector | Unprimed vector | $`C_{112}=1/2`$ |
| $`(2,1)`$ | Unprimed vector | Primed vector | $`C_{121}=1/2`$ |
| $`(1,1)`$ | Primed vector | Primed vector | $`C_{111}=0`$ |
| $`(2,2)`$ | Unprimed vector | Unprimed vector | $`C_{122}=0`$ |

The label assignment is the same whether it occurs as $`B`$ or $`C`$. The selected output $`A=1`$ is written with primes on its linear components. Its source output label is not an instruction to sum over $`A`$.

The factors $`2`$ shown in the sketch are source-map factors **before multiplication by $`C_{1BC}`$**. Keep the source factor and the coefficient as separate entries in the future term ledger, and apply each once. No weighted component expression is calculated in this framework note. No additional $`C_{2BC}`$ entries or full action-tensor sum are specified.

## 3. Binding construction sequence

The construction order is specified below. Gold (7) gauge conditions are applied in Step 4 after the unrestricted Gold substitution.

### Step 1 — Write the full BF density with primed components

Use the complete fermionic vector–linear density, with the **primed vector paired with the primed linear multiplet**. The schematic starting density is

```math
e^{-1}\mathcal L_{VL}=L'_{ij}Y'^{ij}+\rho'N'+\cdots.
```

The dots stand for the remaining source BF terms, including all fermionic and constrained-form terms. They are not a truncation. The full density from corrected Özkan–Pang Eq. (3.1) is now transcribed and primed term by term in the Step 1 note. Gold Eq. (3) is a bosonic normalization reference, not a full fermionic replacement.

The BF vector choice is now **settled: it is the primed composite vector**. Retain the source normalization; any eventual conversion to the Gold R² normalization must be recorded and verified. A boundary-representative conversion requires its explicit boundary term and the correct ordinary or supercovariant strength.

### Step 2 — Construct the primed linear multiplet from the mixed vectors

Use all four components of Özkan Eq. (3.20), with the ordered assignments and coefficients in Sec. 2, to construct $`(L'_{ij},\varphi'_i,E'^a,N')`$ from the primed and unprimed vector components.

At this stage retain $`(\rho',\lambda'^i,Y'_{ij},\widehat F'_{ab})`$ and $`(\rho,\lambda^i,Y_{ij},\widehat F_{ab})`$ in the map. Show both ordered mixed contributions before collecting terms. Preserve fermion ordering and the constrained-vector definition. Do not substitute either vector's component map yet.

### Step 3 — Insert the new primed linear multiplet into primed BF

Substitute all four outputs from Step 2 into the full density fixed in Step 1. Keep the expression in **primed and unprimed vector components**. This is the intermediate action represented by the products in the handwritten sketch.

The primed vector appearing explicitly in BF and the primed vector appearing inside the mixed map have the same composite role. Keep their occurrences traceable so the later primed map reaches every occurrence.

### Step 4 — Substitute Gold Eq. (4) for the unprimed vector

Only after the BF insertion, apply Gold's defining-vector map to every unprimed vector occurrence:

```math
\rho=\sigma,\qquad A_\mu=C_\mu,\qquad \lambda^i=\psi^i,
\qquad
Y^{ij}=\frac{i}{4\sigma}\bar\psi^i\psi^j-\frac{g}{2\sigma}L^{ij}.
```

This is an anchored source input, not a new calculation. The $`L^{ij}`$ is the original unprimed compensator specified in Sec. 1. Carry the defining-vector substitution through field strengths, derivatives and dependent expressions without changing its meaning.

### Step 5 — Substitute the earlier linear-to-vector map for the primed vector

Use the earlier complete component map with only its **output vector labels changed to primes**:

```math
(L_{ij},\varphi_i,E_a,N)
\quad\xrightarrow{\text{earlier linear-to-vector map}}\quad
(\rho',\lambda'_i,Y'_{ij},\widehat F'_{\mu\nu}).
```

Keep the input linear fields unprimed and identical to those in Step 4. Use the existing complete scalar, spinor, triplet and supercovariant field-strength slots; do not reconstruct them from the schematic $`Y'`$ term in the sketch. Apply the map to **every** primed vector occurrence in the Step 3 density, including the explicit BF vector and all derivative/composite occurrences.

The earlier map directly anchors the field strength. Any required potential $`A'_\mu`$ representative must be taken from a located source or established through a documented density/boundary conversion; do not invent a local potential from the hatted strength alone.

### Step 6 — Complete the common gauged representation and validate the action

Both vector substitutions use the **gauged Coomans–Özkan** background. This binding applies throughout the construction; when the background slots are explicitly expanded, apply the same gauged definitions everywhere, including inside derivatives, curvatures and dependent connections. The final variables are the original unprimed linear multiplet and unprimed gauged Dilaton-Weyl fields.

Keep $`T_{ab},\chi^i,D`$ tied to Coomans Eqs. (5.6),(5.3),(5.4), with the gauged $`\widehat H`$ of (5.7). Retain the $`gE_{\mu\nu\rho}/2`$ contribution and the gauging terms in $`\chi,D`$. Record the source's omitted higher-fermion orders and recover what is required before claiming the full action.

After constructing the action, check source normalizations, index and spinor conventions, fermion-order completeness, and the bosonic Gold R² result. Gauge fixing, auxiliary elimination, vacuum selection and spectrum analysis are later operations and must not be inserted into Steps 1–5 without an explicitly justified change of scope.

## 4. Source and reusable-map anchors

| Ingredient | Exact anchor | Role and scope |
|---|---|---|
| Construction definition | Sections 1–3 | Distinct primes, common original linear input and the stated $`C_{1BC}`$ |
| Full fermionic BF | Özkan–Pang 2013, corrected v4 ([publication](../../../../../../references/bibliography.md#OzkanPangGB2013)), Eq. (3.1), PDF/printed 10; [supporting ledger](../../../../../../common/README.md) | Primed vector paired with the newly constructed primed linear multiplet |
| Mixed vector-to-linear map | Özkan 2016 ([publication](../../../../../../references/bibliography.md#Ozkan2016)), Eq. (3.20), PDF 10–11 / printed 9–10 | All four primed linear output slots; fixed $`A=1`$ |
| Unprimed defining vector | Gold 2025 ([publication](../../../../../../references/bibliography.md#GoldEtAl2025)), Eq. (4), PDF/printed 5–6 | Step 4 |
| Primed composite vector | [Current earlier-map anchor](../../../../../two_derivative_fermionic/inputs/reference/results/gauged_two_derivative_fermionic_action/03_single_linear_multiplet_linear_map_anchor.md), `OZKAN1608-SINGLE-LINEAR-TO-VECTOR-MAP-v2` | Step 5; complete earlier components, with outputs primed |
| Gauged background | Coomans–Özkan 2013 ([publication](../../../../../../references/bibliography.md#CoomansOzkan2013)), Eqs. (5.2)–(5.8), PDF/printed 16–17 | Every explicit and implicit background occurrence; source-order qualification below (5.6) |
| Future bosonic comparison | [Parent R² starting point](<../../../../../../r2/ads5/background.md>), `R2-GOLD12-OFFSHELL-v1` | Gold Eqs. (12a,b),(25),(26), off shell and un-dualized |

The current earlier-map [calculation file](../../../../../two_derivative_fermionic/inputs/reference/results/gauged_two_derivative_fermionic_action/02_single_linear_multiplet_mapping_construction.md) supplies:

| Primed slot to use later | Existing location in the earlier map |
|---|---|
| $`\rho'`$ | Sec. 7.9 |
| $`\lambda'_i`$ | Secs. 8.7 and 8.11 |
| $`Y'_{ij}`$ | Secs. 9.7 and 9.11 |
| $`\widehat F'_{\mu\nu}`$ | Eqs. (10.11),(10.15), Sec. 10.9 |

## 5. Distinct multiplet roles

The original unprimed linear input and the new primed linear output have
different roles. The latter is not fed back into the earlier map. Source-term
ledgers track the vector label, map occurrence, explicit/implicit fermion order
and boundary representative. Gold's bosonic expression does not determine
omitted fermion coefficients. The construction uses the stated gauges and
normalizations without auxiliary field equations.

## 6. Component derivation chain

Steps 1–3 are complete in [the full primed BF calculation](03_step1_full_primed_BF_density.md), [the mixed linear calculation](04_step2_mixed_primed_linear_multiplet.md), and [the full BF insertion](05_step3_mixed_linear_inserted_in_BF.md). The Step 3 endpoint is Eq. (35), lock `R2-MIXED-BF-INSERTION-v2`, with the full constrained-form relation retained. The [Step 4 Gold substitution and gauge restriction](06_step4_Gold_unprimed_vector_and_gauge.md) is also complete, with endpoint Eq. (47), lock `R2-GOLD4-UNPRIMED-SUBSTITUTION-v2`. [Step 5](08_step5_primed_composite_vector_insertion.md) is now complete: all primed occurrences receive the complete earlier map, and the local Gold (25) potential is derived with full fermionic curl checks. The physical two-fermion completion is given in Step 6 below. The BF pairing, prime labels, coefficients and common original linear input remain settled.

## Gauge stage — Step 4

After displaying all ungauge-fixed Gold substitutions, [Step 4](06_step4_Gold_unprimed_vector_and_gauge.md) applies Gold (7), sigma=1, b_mu=0, psi^i=0, with lock `R2-GOLD7-GAUGE-v1`. The original L_ij remains a triplet. This changes gauge timing only; the primed map still follows Gold in Step 5. The full covariant derivatives of the zero gaugino and the box of the fixed scalar are evaluated, the gravitino completion of hatted G remains, and no auxiliary equation is used. Steps 1–3 and the full pre-gauge Gold substitutions remain available as the unrestrained parent.

## Gauge stage — Step 5

The new derivation preserves the unrestricted triplet map, then uses local Gold (25), L_ij=delta_ij L/sqrt(2), L>0, with its full connection/fermion derivative. The derived potential and complete primed insertion are locked as `R2-COMPOSITE-POTENTIAL-GOLD25-v1` and `R2-PRIMED-COMPOSITE-INSERTION-v1`. The common gauged slots remain implicit for Step 6; no higher-fermion omission is set to zero.

## Intermediate Step 5a: partial insertion

Before Step 6, [insert only rho-prime and lambda-prime](09_step5a_rho_lambda_partial_insertion.md), leaving Y-prime, Fhat-prime and A-prime unexpanded. The completed note distributes products and records 0/2/4 explicit-degree sectors, the omitted degree-six ledger, and a separately simplified actual bosonic restriction. This local truncation does not change the full-fermion target or the untruncated Step 5 parent.

## Step 6: quadratic fermion scope

Step 6 retains two physical fermions in the aligned-triplet gauge. [The derivation](10_step6_gauged_action_through_two_fermions.md) completes that bounded component construction, with Gold7/25, L>0, all hidden two-fermion completions and source qualifications. Four and higher fermion orders are omitted only from this new result. Full nonlinear supersymmetry and reality validation are outside this retained-order construction.
