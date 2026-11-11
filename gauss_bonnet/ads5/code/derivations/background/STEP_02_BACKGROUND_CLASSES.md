# Step 2 — Maximally symmetric background class and domains

Input: [Step 1](STEP_01_INPUTS_AND_FIELDS.md), especially its accepted field and curvature definitions. This is the class specified for this analysis, not a truncation imposed on the arbitrary fluctuations.

## 2.1 Geometry and invariant fields

At each point a maximally symmetric five-dimensional Lorentzian geometry has the full Lorentz isotropy group. An invariant vector must obey $`\Lambda^a{}_bX^b=X^a`$ for every Lorentz transformation. Spatial rotations first force $`X^1=X^2=X^3=X^4=0`$; a boost in the $`01`$ plane then gives $`0=X'^1=\sinh\beta\,X^0`$, hence $`X^0=0`$. The invariant tensors available without a preferred direction are $`\eta_{ab}`$ and $`\varepsilon_{abcde}`$. Antisymmetrizing a metric gives $`\eta_{[ab]}=0`$; there is no invariant rank-two or rank-three antisymmetric tensor. A four-form is dual to the already excluded vector. There is no independent five-form field strength in this action.

Consequently the background invariant strengths satisfy

```math
\bar G_2=0,\qquad\bar H_3=0,\qquad\bar P_a=\bar E_a=0,\qquad\bar R_{ab}{}^{ij}(V)=0,\qquad\overline{\mathcal D_aL^{ij}}=0. \tag{2.1}
```

A possible compensating compact internal $`SU(2)`$ rotation cannot preserve a nonzero spacetime two-form under the full noncompact Lorentz isotropy: it would require a nontrivial homomorphism of the simple Lie algebra $`\mathfrak{so}(4,1)`$ into $`\mathfrak{su}(2)`$, whose kernel would have to be either zero or the whole algebra; injectivity is impossible because $`10>3`$. Thus (2.1) also covers symmetry up to the internal gauge group. Lower-symmetry flux backgrounds are outside the selected class.

The constant-curvature tensor and its contractions are

```math
\bar R_{abcd}=k(\eta_{ac}\eta_{bd}-\eta_{ad}\eta_{bc}),\qquad \bar R_{ab}=k(5\eta_{ab}-\eta_{ab})=4k\eta_{ab},\qquad\bar R=4k\,\delta_a{}^a=20k. \tag{2.2}
```

Here $`k<0`$ gives local AdS$`_5`$, $`k=0`$ local Minkowski space, and $`k>0`$ local dS$`_5`$. No sign is chosen in advance. Constant scalars and vanishing fermions give

```math
\bar L=L_0\ne0,\qquad \bar N=N_0,\qquad\bar\psi_\mu^i=\bar\varphi^i=0. \tag{2.3}
```

On a contractible patch the flat potentials can be represented by $`\bar C=\bar V=\bar V'=\bar E_3=\bar B=0`$. In particular $`d\bar E_3=0`$ follows from $`\bar P=0`$ and then $`\bar H_3=d\bar B+g\bar E_3/2=0`$ is compatible with this local representative. This classifies local vacuum geometries; global quotients, flat holonomies and topological form sectors require additional global data and are not counted as distinct local branches.

## 2.2 Domain and boundary scope

Take $`g,\lambda,k,L_0,N_0`$ real and $`0<\kappa_5^2<\infty`$. The accepted scalar coordinate patch is $`L_0\ne0`$, because the source density contains $`L^{-1},L^{-2},L^{-3}`$. We display both signed patches so that no real solution is silently discarded. If one further chooses the positive compensator patch $`L_0>0`$, retain exactly the positive-$`L_0`$ entries explicitly counted in Step 5. No ghost/norm condition is imposed by either choice.

There is no quantized nonzero flux in this local class. We evaluate a local action density; no finite total volume or boundary renormalization is assumed. For stationarity use arbitrary smooth compactly supported fluctuations in a patch. This permits bulk integration by parts without specifying an AdS or dS asymptotic fluctuation boundary condition.

## 2.3 Fluctuations are not restricted by background symmetry

For each field the background plus fluctuation is

```math
\begin{aligned}
g_{\mu\nu}&=\bar g_{\mu\nu}+th_{\mu\nu},\qquad L=L_0+t\ell,\qquad N=N_0+tn,\qquad C_\mu=tc_\mu,\qquad B_{\mu\nu}=tb_{\mu\nu},\\
E_{\mu\nu\rho}&=tu_{\mu\nu\rho},\qquad V_\mu=tv_\mu,\qquad V'_\mu{}^{ij}=tv'_\mu{}^{ij},\qquad\psi_\mu^i=t\zeta_\mu^i,\qquad\varphi^i=t\xi^i .
\end{aligned}\tag{2.4}
```

All functions in (2.4) depend arbitrarily on position; $`h_{\mu\nu}`$ need not be a constant-curvature deformation. The antisymmetric frame variation $`\theta_{ab}`$ in Step 1 remains arbitrary and has a zero tadpole by local Lorentz invariance, as checked in Step 5.

Although $`\bar\sigma=1`$ is constant, $`\mathcal D_a\mathcal D_b\sigma=2f_{ab}+O(\Psi^2)`$ is not zero. Although $`L_0`$ and $`N_0`$ are constant, their conformal boxes have $`K`$-connection contributions. Step 3 evaluates these descendants before using numerical background values. Equations (2.1)–(2.4) do not assert that a full fermionic $`f_{ab}`$ is symmetric.
