# Primary norms and verification scope

For a simple real massive root D_i and a covariant gauge-invariant probe,
the source-relative primary norm sign is

```math
\mathop{\mathrm{sgn}}\nolimits\mathcal N_i=
\mathop{\mathrm{sgn}}\nolimits\left[(-1)^{|n|}\mathop{\mathrm{sgn}}\nolimits(D_i-1)
\mathop{\rm Res}_{D=D_i}\langle\Phi_n\Phi_{-n}\rangle\right].
```

The vector sign comes from the light-cone metric. The complete signed
prefactors are restored after row normalization. Residues are evaluated
analytically as numerator divided by the derivative of the vanishing
denominator factor and the other factors. Complex energies receive no real
norm sign. This simple-pole formula does not assign the norm of a logarithmic
mode or a D=1 current. Negative weights can produce negative-norm descendants
even for a positive-norm primary; boundary admissibility is a separate question.

## Spin-2 and constant-level norms

The exact TT normalization gives, at M=0,

```math
\begin{aligned}
\widehat K_2(D)&=\frac{P_3^2}{8P_2^2}\kappa_{\rm eff}D(D-2)
 \left(1-\frac{D-1}{m}\right),&
\kappa_{\rm eff}&=\frac{LY}{4P_2P_4},\\
\mathop{\mathrm{sgn}}\nolimits\mathcal N_T&=\mathop{\mathrm{sgn}}\nolimits[\kappa_{\rm eff}(1-1/m)],&
\mathop{\mathrm{sgn}}\nolimits\mathcal N_{\bar T}&=\mathop{\mathrm{sgn}}\nolimits[\kappa_{\rm eff}(1+1/m)],\\
\mathop{\mathrm{sgn}}\nolimits\mathcal N_{\rm TMG}&=\mathop{\mathrm{sgn}}\nolimits[\kappa_{\rm eff}(1-m^2)].
\end{aligned}
```

The first two signs are those of c_L,c_R. The independently reduced current
CS matrix gives the same R-current sign as c_L. Scalar and vector norms at
the constant level follow from the signed kinetic/potential and curl pencils
in [constant.json](../../../computations/gb_ads3_sigma2/outputs/constant.json),
with N eliminated only after retaining its full equation.

More explicitly, in the original Einstein-frame scalar variables let H_E
be the potential Hessian and take its N Schur complement. For a real mass
eigenvector u and a curl-pencil null vector v_c, the complete remaining
constant-level norm prescription is

```math
\begin{aligned}
m_{\rm sc}^2u&=-\tfrac12(K_E^{\rm red})^{-1}H_E^{\rm red}u,&
\mathop{\mathrm{sgn}}\nolimits\mathcal N_{\rm sc}&=\mathop{\mathrm{sgn}}\nolimits(-u^\dagger K_E^{\rm red}u),\\
Q(D_i)v_c&=0,&
\mathop{\mathrm{sgn}}\nolimits\mathcal N_{\rm vec}&=
\mathop{\mathrm{sgn}}\nolimits[(D_i-1)v_c^\dagger Q'(D_i)v_c].
\end{aligned}
```

The saved matrices specify the amplitude scales explicitly; these
congruences do not change the inertia. At a complex mass, repeated root or
singular Einstein-frame chart, these simple-eigenmode formulas require the
corresponding unreduced analysis.

## The double flat root

The charged inverse slope is 2P2/(L k P3), so its primary is negative iff
kL<2. A single neutral component probe sees only one flat direction. The
saved matrix uses h_plus3, C_plus, V_plus, a magnetic three-form combination,
and the transverse projection of h_plus4. Each observable annihilates both
gauge kernels exactly. For chi=+1 the latter is

```math
\Phi_{+4}=h_{+4}-\frac{SP_2}{(D+1)P_3}h_{+2}.
```

Its b partner uses D to 2-D and S to 1-S. Its chart poles D=-1,3 require
other observables when they coincide with a pole under study. Define
Q=L²k-3Lk-2L+8. The two mixed-metric residues at D=nu are equal, their
off-diagonal residue vanishes, and the common value is

```math
\mathcal R_f=-\frac{kP_2^2P_4}
 {16L^2(kL-2)[k(L-1)-2](-P_3)Q}.
```

To recover the real harmonic inner product, multiply the a mixed-metric
probe by 1/S and its b partner by 1/(1-S). This is essential on S² and
makes the H² residue matrix Hermitian. With R_Z the charged residue,

```math
\frac{\mathcal R_f}{S(1-S)\mathcal R_Z}
 =\frac{2P_2^4}{P_3^4M^2(\nu^2-1)}.
```

This exact identity proves that both neutral flat directions have the
charged norm sign for the supersymmetric boson weight h_f>1 and the opposite
sign for 0<h_f<1. The full residue matrix has rank two at each tested generic
level, including both chiralities; its two nonzero eigenvalue signs are
checked rather than inferred from the double factor alone.

## Harmonic-form norms

For chi=+1, the h_plus3 residues of the harmonic one-form block and the
h34 residue of the quadratic-differential block are exactly

```math
\begin{aligned}
\mathop{\rm Res}_{3}G_{h_3h_3}
 &=\frac{P_2^2P_4}{4L^2(kL-2)P_3^2Q},\\
\mathop{\rm Res}_{-1}G_{h_3h_3}
 &=-\frac{P_2^3P_4}{16L^2[k(L-1)-2]P_3^2Q},\\
\mathop{\rm Res}_{2}G_{h_{34}h_{34}}
 &=\frac{P_2^3}{LP_3^2P_4}.
\end{aligned}
```

Since Q/P4 is positive on H², these give the v109 rules: the (2,1) vector
is negative iff kL>2; the (1,2) vector is negative iff
P2[2-k(L-1)]<0; the complex structure modulus is negative iff P2P4<0.
Chirality reflection exchanges the vector helicities. In the regular torus
basis the independently computed residues are

```math
\begin{aligned}
\mathop{\rm Res}_{3}G_{h_3h_3}&=-\frac{L-3}{18L},&
\mathop{\rm Res}_{-1}G_{h_3h_3}&=\frac1{72},&
\mathop{\rm Res}_{2}G_{h_{34}h_{34}}&=\frac{L-3}{18(L^2-6L+12)}.
\end{aligned}
```

They give the same torus light-sector rules. The sphere j=1 current has
the separately verified raw h_plus3 residue

```math
\mathop{\rm Res}_{1}G_{h_3h_3}=
-\frac{(kL-4)P_4}{3L^3(-P_3)
(L^2k^2-2L^2k+2Lk+4L-4k-8)}.
```

Its harmonic inner product contributes 1/[S(1-S)]=-1/2. This is a current
residue at D=1; the massive-mode sign(D-1) prescription must not be applied
there. The right-moving assignment and positive levels at examined points
are the scoped current statement of v109, not a universal positivity claim
from a generic massive residue. Wilson-line and flavor entries left
undetermined in paper Table 10 (`tab:light`) are not promoted to general sign theorems.

## Finite numerical evidence

[norm_samples.json](../../../computations/gb_ads3_sigma2/outputs/norm_samples.json)
repeats every level in the upper block of paper Table 11 (`tab:GBbos`): S² at
(10,1/10), j=2…16 and (5,-1), j=2,3; H² at (6,2), nu_H=0,1,3 and
(3,6/5), nu_H=1/2,2. All real-root norms, flat residue inertia and ordinary
bosonic partner norm relations agree at **80 and 140 decimal digits**.
The four pairs crossing D=1 are checked on the paper's formal connected
branch, with the original fast-branch signs retained separately. They are
scalar roots 0<D<1 at (L,k,S)=(5,-1,3), (6,2,1/2),
(6,2,1/2+i), and (6,2,1/2+3i). Choose the scalar's smaller root and
the vector's larger root, giving the connected formal multiplet

```math
(s_0,\Delta_0)=(0,D),\qquad
(s_v,\Delta_v)=(1,1+D),\qquad h=D/2>0.
```

No kinetic norm is reversed. The scalar lies in -1<m²ell²=D(D-2)<0.
For both independent scalar probes L_0 and N_0, the actual action
propagators obey the checked residue identity

```math
R_0(2-D)=-R_0(D),\qquad
(1-D)R_0(2-D)=(D-1)R_0(D).
```

Thus the pole residue in the mass variable, and its kinetic sign, is
unchanged by exchanging the scalar roots. These identities are evaluated
independently at 80 and 140 digits in all four cases. With h=D/2, the
superalgebra factor 4h(h+1)=D(D+2) is positive, and the independently
calculated vector and scalar norm signs agree in every case.
The output records both energies, h, the scalar mass, both probe residues
and the asserted norm relation. It is a check of the paper's formal
multiplet assignment; it does not construct boundary conditions admitting
that assignment.

At (10,1/10) each tested generic sphere level has one negative spin-2
multiplet, one negative (1,0) multiplet and two negative flat multiplets,
with six positive multiplets. Complex modes at (5,-1) are recorded as such.
[accumulation_norm_samples.json](../../../computations/gb_ads3_sigma2/outputs/accumulation_norm_samples.json)
repeats all 45 finite-level entries in the lower block for the approaching
spin-2 tower and, on S²/H², its scalar counterpart. The two signs agree
whenever both roots are real. These are labelled samples, not a proof from
numerical fitting over arbitrary couplings.

The symbolic negative control deletes the three explicit E_a-dependent
GB terms, preserving the potential E_3 in H_3. The TT matrix is unchanged.
The [numerical deletion check](../../../computations/gb_ads3_sigma2/outputs/product_checks/E_deletion.json)
at L=10, k=1/10, S=3 reconstructs the remaining matrices and finds
D=2.64268548731549969 ± 1.86551157553966163 i in n=1, as quoted after
equation (4.9) (`eq:Kform`). Its TT roots are -2.10796442115015126,
3.55036239262915448 and 10.0607076185831086. None has its D-1 vector
partner, and none of the five scalar modes has its required vector
partner. Every retained root is checked against the rank of the full
matrix at 115 decimal digits. This supplies the spectral negative control
in addition to the matrix-level difference.
The [verification log](../../../computations/gb_ads3_sigma2/outputs/verification.log)
separates the symbolic identities from these numerical checks. Repository
hash/link validation is a separate structural check.
