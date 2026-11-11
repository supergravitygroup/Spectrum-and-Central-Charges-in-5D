# LOG convention contract

Source lock: `GAUGED-LOG-CONVENTIONS-v1`; endpoint [LOG action input](../../log/action/details/spectrum_input.md).
Full definitions: [branch conventions](../../log/action/details/component_construction/results/gauged_full_fermionic_log/CONVENTIONS.md),
[LOG bridge](../../log/action/details/component_construction/results/gauged_full_fermionic_log/LOG_CONVENTIONS.md), [procedure](../../log/action/details/component_construction/results/gauged_full_fermionic_log/notes/06_complete_construction_sequence.md).

η=(-,+,+,+,+), a=0,…,4, spinor dimension 4, i=1,2; ε^{01234}=+1,
γ^{01234}=+i; the Majorana bar is linear and fermions are Grassmann-odd;
(anti)symmetrization has unit weight. Preserve right-side SU(2) lowering and
the -MC rule on the second spinor index. The source repair in C24 A.1l fixes
the K coefficients to +i/8, -i/4.

The field D is the auxiliary scalar. 𝒟_a and □^c are fully supercovariant
operators; Q/S/K connections remain inside derivatives. Do not reorder derivatives.
Gauge: σ=1, ψ^i=0, b_μ=0; L_c^{ij}=δ^{ij} L/√2 and V=V′+trace/2.
Apply the gauge after differentiation. Do not set the antisymmetric part of the
full f_ab to zero. The independent compensator L_c and composite L_log are distinct fields.

Even slots retain 0+2 physical fermions; the φ slot retains 1. There is no
truncation before the first derivatives. Before gauge fixing, the weights of
L,φ,N,E are 3,7/2,4,4; after gauge fixing their engineering dimensions have the
same values. The dimensions of g and λ_LOG are 1 and -2, respectively.
ℓ_total=ℓ_2der+λ_LOG ℓ_log. No EFT or on-shell elimination is applied.
