# Notation: source equations and algebraic checks

The [main conventions](../common/conventions.md) and [derivation appendix](../common/details/convention_conversions.md) use the [component convention reference](../common/details/source_conventions.md).

| Main text | Original source section | Operation |
|---|---|---|
| 1. Dimension, indices and vielbein | 3 | The notation was consolidated; the inverse vielbein and index conversions were written explicitly. |
| 2. Volume element and density | 3 | The determinant relation was derived; the positive vielbein-determinant branch used in the source was made explicit. |
| 3. Symmetrization and epsilon | 4–5 | The antisymmetrization weight and epsilon contraction were derived; the tensor/density distinction was retained. |
| 4. Clifford algebra | 4 | General gamma duality was derived; signs from reversed index order were made explicit. |
| 5. Internal indices and spinors | 4 | The internal-index algebra and contracted flip sign were derived; the open-index flip was distinguished as a pairing definition. |
| 6. Derivatives | 6 and 11.5 | The connection part was distinguished from the full supercovariant derivative; the Lorentz sign was checked by two algebraic methods. |
| 7. Tensor products | 10, notation lines only | The definitions of three distinct contractions were retained. |

- The metric determinant was written explicitly as `det g` to reduce ambiguity with the coupling constant; no physical parameter was redefined.
- The derivation showed that the source expression `e = det(vielbein) = sqrt(-det(metric))` applies on the positive-determinant branch.
- No epsilon orientation was selected. The unit square of the symbolic orientation component was derived from the supplied Clifford and highest-rank gamma relations; both sign branches were retained.
- The factorials and signs relating reversed-order and same-order gamma-duality expressions were displayed explicitly.
- Spinor-pairing definitions were distinguished from the contraction signs derived from them.

## Mathematical verification status

| Item | Status and evidence |
|---|---|
| Dimension, signature, index ranges | Source definitions; not choices of free parameters. |
| Vielbein and metric determinant | Verified by inverse-matrix substitution and determinant multiplication; Appendix A. |
| Antisymmetrization weight | Verified through idempotence of the permutation sum; Appendix B. |
| Epsilon normalization and contractions | Verified using the Clifford volume element and permutation determinants, with the orientation sign kept symbolic; Appendix C. |
| Gamma duality | Verified by complementary-index multiplication, factorial counting and substitution of the endpoint ranks; Appendix D. |
| Internal-index signs | Verified by exact products of the defined epsilon matrix and index-explicit back-substitution; Appendix E. |
| Open-index spinor flip rule | Retained as the source's pairing convention. Relative rank signs and compatibility with Clifford duality were checked; Appendix F. Its use is restricted to that pairing convention. |
| Contracted flip sign | Derived from the supplied open-index pairing definition and independently verified internal-index algebra; Appendix F. |
| Lorentz derivative | The same sign was derived from the tensor's lower indices and the spinor Clifford product rule; Appendix G. |
| Dot, slash and tensor-product notation | Source definitions; no additional physical equality was assumed. |

In addition to the hand-checkable derivations, exact coefficient comparisons were performed in the formal Clifford algebra with the supplied dimension and metric:

| Check | Finite index/basis identity covered |
|---|---:|
| Clifford anticommutators | 25 |
| Independent antisymmetric components of gamma duality | 32 |
| Lorentz gamma commutators | 125 |
| Clifford product coefficient of each independent connection–tensor monomial | 100 |
| Independent antisymmetric components of epsilon contractions | 252 |
| Components of the two internal epsilon contractions | 8 |
| Relative gamma-rank interchange signs | 6 |

These operations used exact rational arithmetic and index algebra. The coefficients of the connection–tensor monomials were extracted; no sample values were assigned to connection or tensor components. No epsilon sign was chosen, no matrices or physical parameters were sampled, and no numerical tolerance was used. These supporting checks do not replace the analytical derivations in the appendix.

## Scope boundary

Since the source does not supply an explicit charge-conjugation matrix, Dirac-bar phase or detailed complex-conjugation rules, these have not been presented as determined or verified. Subsequent calculations requiring that information cannot infer additional reality conditions from this section.

No Fierz identity was used in this section or included among its verified results. Full supercovariant completions, the origins of all Weyl weights and the source file's other calculations also lie outside this record's verification scope. They are not used as established calculations in the main text.

