# LOG building block: physical two-fermion part

The projection $`\Pi_2`$ selects the physical two-fermion coefficient after accounting for every dependent object. Explicit two-fermion blocks alone do not constitute this part. Using the [projection definition and rules](../../common/fermion_order.md),

```math
\ell_{\log}^{(2)}=\Pi_2\!\left[\sum_{r=1}^{40}\mathcal U_{\log,r}\right]+\Pi_2\!\left[\sum_{s=1}^{326}\mathcal V_{\log,s}\right].
```

All **40 blocks** of the first sum are written in the [covariant-core file](covariant_core.md), and all **326 blocks** of the second sum in the [explicit two-fermion file](explicit_two_fermion.md). No block is omitted under an implicit reference to similar terms.

Each monomial in the second sum already contains two explicit degree-one objects, so degree-zero parts of even objects and degree-one parts of odd objects suffice. In the first sum, the two-fermion completion of every even object and derivative operation is retained. The equivalent compact expression obtained by subtracting the bosonic part is therefore

```math
\ell_{\log}^{(2)}=\Pi_{\le2}\bigl(\mathcal U_{\log}+\mathcal V_{\log}-\mathcal B_{\log}\bigr)
```

The [composite-field degree coefficients](../../common/details/composite_fields.md) expand the basic inputs to this projection. The [SUSY check record](../../references/component_records/02_action_family.md) specifies the transformations checked and the fermion degree of each result.
