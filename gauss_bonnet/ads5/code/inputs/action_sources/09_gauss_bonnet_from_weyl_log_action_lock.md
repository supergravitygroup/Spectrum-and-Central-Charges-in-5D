---
title: Definition-derived Gauss-Bonnet action from Weyl minus four Log
date: 2026-08-21
status: source-frozen bosonic off-shell action
lock_id: GB-WEYLOG-DEF-v1
---

# Problem and target

The four-derivative invariant is defined only by

```math
\ell_{\rm GB}^{\rm def}
:=\ell_{\rm Weyl^2}^{\rm def}-4\ell_{\rm Log}^{\rm def},
```

where the two inputs are the corrected, definition-derived Eqs. (51) and
(52) of `results/pdfs/weyl_squared/weyl_and_log_superinvariants_definition_derived.pdf`.
Gold et al.'s printed Gauss--Bonnet density and all earlier Gold-GB vacuum or
spectrum reductions are not inputs.  In particular, the corrected Log
invariant has no explicit
$`R_{abcd}G^{ab}G^{cd}`$,
$`R_{abcd}G^{ab}H^{cd}`$, or
$`R_{abcd}H^{ab}H^{cd}`$ term after its displayed L10--L12 cancellation.

The total bosonic action is

```math
S_{\rm tot}=\frac1{16\pi G_5}\int d^5x\,e\,
\left(\ell_{2\partial}+\lambda_{\rm GB}\ell_{\rm GB}^{\rm def}\right),
\qquad [\lambda_{\rm GB}]=-2.
```

The common two-derivative density is the independently cross-checked
gauge-fixed Poincare density; using it does not import any printed
four-derivative Gauss--Bonnet coefficient:

```math
\begin{aligned}
\ell_{2\partial}={}&L\left(R-\frac12G_{ab}G^{ab}
 +4H_{ab}H^{ab}+2V_a^{\prime ij}V_{ij}^{\prime a}\right)
 +L^{-1}\nabla_aL\nabla^aL-2L^{-1}E_aE^a\\
&-2\sqrt2E_aV^a-2L^{-1}N^2-4gE_aC^a
 -2gLN-4gN-\frac12g^2L^3+2g^2L^2.
\end{aligned}
```

# Convention ledger and independent fields

The tangent metric is mostly plus, antisymmetrization has unit weight, and

```math
[\nabla_a,\nabla_b]X_c=R_{ab c}{}^dX_d,
\qquad R_{ab}=R_{ca}{}^c{}_b,
\qquad
H^{ab}=-\frac1{12}\epsilon^{abcde}{\cal H}_{cde}.
```

The inherited source gauge and connection split are

```math
\sigma=1,\qquad b_\mu=0,\qquad
L^{ij}=\frac{\delta^{ij}}{\sqrt2}L,\qquad
V_a{}^{ij}=V_a^{\prime ij}+\frac12\delta^{ij}V_a,
\qquad \delta_{ij}V_a^{\prime ij}=0.
```

The independent bosonic potentials/fields are

```math
g_{\mu\nu},\ L,\ N,\ C_\mu,\ B_{\mu\nu},\ E_{\mu\nu\rho},\
V_\mu,\ V_\mu^{\prime ij}.
```

Their constrained descendants are

```math
G_{ab}=2\partial_{[a}C_{b]},
```

```math
{\cal H}_{abc}=3\partial_{[a}B_{bc]}
 +\frac32C_{[a}G_{bc]}+\frac g2E_{abc},
\qquad
H^{ab}=-\frac1{12}\epsilon^{abcde}{\cal H}_{cde},
```

```math
E^a=-\frac1{12}\epsilon^{abcde}\nabla_bE_{cde},
\qquad
\nabla_bH^{ab}=-\frac1{16}\epsilon^{abcde}G_{bc}G_{de}
 +\frac g2E^a.
```

Thus $`G,H,E`$ are not independent unconstrained two-/one-forms in a
variation.  The compensator derivative must be expanded before a constant
background is imposed:

```math
(\nabla_aL^{ij})(\nabla^aL_{ij})
=(\partial_aL)(\partial^aL)+2L^2V_a^{\prime ij}V_{ij}^{\prime a}.
```

# Frozen definition-derived four-derivative density

In the common boundary-equivalent representative of the two source
invariants,

```math
\begin{aligned}
\ell_{\rm GB}^{\rm def}\simeq_\partial{}&
-\frac18\epsilon^{abcde}C_aR_{bc}{}^{fg}R_{de\,fg}
+\frac12\epsilon^{abcde}C_aV_{bc}^{ij}V_{de\,ij}\\
&-\frac14R_{abcd}R^{abcd}+R_{ab}R^{ab}-\frac14R^2\\
&+\frac13R_{abcd}G^{ab}G^{cd}
-R_{abcd}H^{ab}G^{cd}
-\frac23R_{abcd}H^{ab}H^{cd}\\
&-\frac23R_{ab}G^{ac}G^b{}_c
+4R_{ab}G^{ac}H^b{}_c
+\frac{16}{3}R_{ab}H^{ac}H^b{}_c
-R\,G_{ab}H^{ab}
+\frac12g^2R L^{ij}L_{ij}\\
&+\frac16(G_{ab}G^{ab})^2
+(G_{ab}G^{ab})(G_{cd}H^{cd})
-\frac{14}{3}(G_{ab}H^{ab})^2
+4(H_{ab}H^{ab})^2\\
&-\frac13G_{ab}G^{bc}G_{cd}G^{da}
-2G_{ab}G^{bc}G_{cd}H^{da}
+\frac{28}{3}G_{ab}H^{bc}G_{cd}H^{da}\\
&-8G_{ab}H^{bc}H_{cd}H^{da}
-8H_{ab}H^{bc}H_{cd}H^{da}\\
&-\frac13(\epsilon^{abcde}G_{bc}G_{de})
 (\epsilon_a{}^{fghi}H_{fg}H_{hi})\\
&+4gN\,G_{ab}H^{ab}
-\frac12g^2L^{ij}L_{ij}\,G_{ab}G^{ab}
+g^2L^{ij}L_{ij}\,G_{ab}H^{ab}\\
&+6g^2L^{ij}L_{ij}\,H_{ab}H^{ab}
-2g^2N^2-4g^3N L^{ij}L_{ij}-g^4(L^{ij}L_{ij})^2\\
&-\frac13(\nabla_aG_{bc})(\nabla^aG^{bc})
+\frac23(\nabla_bG^{ab})(\nabla^cG_{ac})\\
&-\frac83(\nabla_aH_{bc})(\nabla^bH^{ca})
-\frac83(\nabla_aH_{bc})(\nabla^cH^{ab})
+g^2(\nabla_aL^{ij})(\nabla^aL_{ij})\\
&-2\epsilon^{abcde}H_b{}^f(\nabla_aH_{cf})G_{de}
-\frac18\epsilon^{abcde}(\nabla^fG_{af})G_{bc}G_{de}\\
&-\frac{10}{3}g^2E_aE^a
+\frac{7g}{12}\epsilon^{abcde}E_aG_{bc}G_{de}
+2g\epsilon^{abcde}E_aH_{bc}H_{de}\\
&-4gV_{ab}^{ij}L_{ij}H^{ab}.
\end{aligned}
```

The two displayed $`\nabla H`$ cross-contractions are equal after a dummy
$`b\leftrightarrow c`$ relabeling and two-form antisymmetry, but both are
retained to preserve the literal `Weyl - 4 Log` source sum.  No equation of
motion has been used.

# Exact construction checks

The following slots cancel exactly in `Weyl - 4 Log`:

```math
V_{ab}^{ij}V^{ab}_{ij},\quad RH^2,\quad gRN,\quad
G^2H^2,\quad (G\!\cdot H)H^2,\quad
G_{ab}G^{bc}H_{cd}H^{da},
```

```math
gN G^2,\quad gN H^2,\quad (\nabla H)^2,\quad
\epsilon HH\nabla G,\quad \epsilon H(\nabla G)G,\quad
gE\nabla G,\quad gVLG.
```

The pure-curvature sector is exactly

```math
-\frac14\left(R_{abcd}R^{abcd}-4R_{ab}R^{ab}+R^2\right),
```

but this Lovelock identity does not justify replacing the remaining
off-shell completion by Gold's printed Gauss--Bonnet density.

# Boundary, scope, and verification contract

If the two input representatives differ from their local BF densities by
$`\nabla_aJ_{\rm W}^a`$ and $`\nabla_aJ_{\rm Log}^a`$, then this lock differs
by

```math
J_{\rm GB}^a=J_{\rm W}^a-4J_{\rm Log}^a.
```

Bulk variations use compact support; the AdS spectrum later uses
normalizable/source-free data with vanishing normal flux of this current.
Other boundary ensembles require restoring the current and rechecking the
variational principle.

This lock is exact at fermion number zero and off shell in the displayed
bosonic potentials.  It does not provide the fermionic quadratic action.

Check the coefficient assembly against the retained action from the repository root with

```bash
python3 -B gauss_bonnet/ads5/code/calculations/assemble_action.py --check
```
