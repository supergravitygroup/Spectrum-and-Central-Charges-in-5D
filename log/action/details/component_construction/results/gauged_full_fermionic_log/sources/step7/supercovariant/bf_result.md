### 6.5 BF current and action

The defining vector leg is $`(1,C_\mu,0,-gL_c^{ij}/2)`$. The composite linear leg is exactly the four slots in §§6.1–6.4. The independent $`c`$ multiplet receives the compensator gauge; the LOG triplet does not.

Substitute this defining vector into the full density (master A01, LOG-S1-16). Its $`i\bar\lambda\varphi_{\log}`$ and $`-\bar\psi_a^i\gamma^a\lambda^jL_{\log ij}/2`$ terms vanish because they contain an undifferentiated dilatino. The descendants of that dilatino already present inside the LOG slots remain. The ordinary current and the compact action are

```math
\boxed{P_{\log}^a=\left[E_{\log}^a+\frac i2\bar\psi_b\gamma^{ba}\varphi_{\log}+\frac14\bar\psi_b^i\gamma^{abc}\psi_c^jL_{\log ij}\right]_{\le2}+\text{high fermi terms}.}
\tag{SC7-50}
```

```math
\boxed{e^{-1}\mathcal L_{\log}^{\rm gauged}=\left[N_{\log}-\frac g2L_c^{ij}L_{\log ij}+C_aP_{\log}^a+\frac12\bar\psi_a\gamma^a\varphi_{\log}+\frac i4\bar\psi_a^i\gamma^{ab}\psi_b^jL_{\log ij}\right]_{\le2}+\text{high fermi terms}.}
\tag{SC7-51}
```

Displaying the current contributions and aligned triplet coefficient gives

```math
\begin{aligned}
e^{-1}\mathcal L_{\log}^{\rm gauged}={}&\left[N_{\log}-\frac{gL}{2\sqrt2}\delta^{ij}L_{\log ij}+C_aE_{\log}^a+\frac12\bar\psi_a\gamma^a\varphi_{\log}+\frac i2C_a\bar\psi_b\gamma^{ba}\varphi_{\log}\right.\\
&\left.\qquad+\frac i4\bar\psi_a^i\gamma^{ab}\psi_b^jL_{\log ij}+\frac14C_a\bar\psi_b^i\gamma^{abc}\psi_c^jL_{\log ij}\right]_{\le2}+\text{high fermi terms}.
\end{aligned}\tag{SC7-52}
```

Use the even components through degree two in the first three terms, the one-fermion spinor in the next two, and the degree-zero triplet in the last two. The implicit degree-two parts of the covariants in an explicitly bosonic term remain included. No second projection factor is applied: the established $`(-2,-2i,-1,+1)`$ slot bridge has already been used in the input.

With the present full derivative convention the linear-multiplet constraint has its source form

```math
\boxed{\mathcal D^aE_{\log a}=0\quad\text{through the retained order}.}
\tag{SC7-53}
```

This constraint is now certified by full-primary linearity and the closed-four-form identity with the full R(Q) gamma trace. The proof and its polynomial premises are in the current certification report; it does not claim a separate brute-force expansion of the divergence of every canonical vector term. It includes the Q/S completions of master L02. It is distinct from the ordinary-current statement $`\partial_\mu(eP_{\log}^\mu)=0`$ in the operational potential representation. The generic current/potential interface FORM-01 is resolved by the complete superform pullback; its literal source discrepancy is explicitly recorded in the certification report. No additional connection-completion terms from a separately derivative-expanded constraint are to be added to (SC7-53).

The bosonic density is $`\ell_{\log}^{(0)}=N_{\log}^{(0)}-gL_c^{ij}L_{\log ij}^{(0)}/2+C_aE_{\log}^{a(0)}`$. Its covariant derivatives still contain bosonic S/K-descendant structure; for example $`\Box^c\sigma|_{\rm bosonic,gauge}=2f_a{}^a=-R/8`$. The independent compensator is kept off shell. The later independent complete bosonic reduction reproduces LOG-CORR05 with the explicit boundary current; see the certification report and its exact equation transcript.

## 7. Convention Dependence and Remaining Uncertainties

The active derivative convention is the fermionic Weyl-squared GC21 convention, evaluated with the gauged composites. It is not a new gauge-preserving Poincaré derivative obtained by silently removing the S/K generators. The gauge evaluation applies after every ordered derivative, as defined explicitly in §3.1.

All algebraic $`Y,T,\chi,D`$ occurrences have been substituted before that evaluation. The full connection dependence of the curvatures, strengths, $`\Box^c\sigma`$ and differentiated dilatino remains implicit by the stated instruction. It must be included when a later component expansion, variation or spectrum calculation is carried out. The dependent-connection solutions are in this same file, (SC7-06).

Canonicality and the performed checks have the algebraic scope stated in §§1 and 5. The generic FORM-01 interface, retained-order reality and complete bosonic comparison are certified in the later audit. Full defining-projector equality, all-order primary constraints and retained-order BF supersymmetry through the linear-multiplet/superform theorem are certified separately in [the current report](../../../CERTIFICATION_LOG_TWO_FERMI_2026-09-25.md). Unrestricted higher-fermion action terms and any spectrum calculation remain outside this retained-order result.
