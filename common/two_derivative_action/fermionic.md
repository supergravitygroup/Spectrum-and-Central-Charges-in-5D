# Two-derivative building block: physical two-fermion part

The projection $`\Pi_2`$ selects the physical two-fermion coefficient after accounting for every dependent object. Explicit two-fermion blocks alone do not constitute this part. Using the [projection definition and rules](../fermion_order.md),

```math
\ell_{2}^{(2)}=\Pi_2\!\left[\sum_{r=1}^{11}\mathcal U_{2,r}\right]+\Pi_2\!\left[\sum_{s=1}^{33}\mathcal V_{2,s}\right].
```

All **11 blocks** of the first sum are written in the [covariant-core file](covariant_core.md), and all **33 blocks** of the second sum in the [explicit two-fermion file](explicit_two_fermion.md). No block is omitted under an implicit reference to similar terms.

Each monomial in the second sum already contains two explicit degree-one objects, so degree-zero parts of even objects and degree-one parts of odd objects suffice. In the first sum, the two-fermion completion of every even object and derivative operation is retained. The equivalent compact expression obtained by subtracting the bosonic part is therefore

```math
\ell_{2}^{(2)}=\Pi_{\le2}\bigl(\mathcal U_{2}+\mathcal V_{2}-\mathcal B_{2}\bigr)
```

The [composite-field degree coefficients](../details/composite_fields.md) expand the basic inputs to this projection. The [SUSY check record](../../references/component_records/02_action_family.md) specifies the transformations checked and the fermion degree of each result.
