# Step 1 — Accepted action, independent fields and expansion order

The background class consists of **maximally symmetric five-dimensional vacua**. The calculation uses the component action and conventions specified below.

## 1.1 Starting point and target

The sole action input is [the full fermionic action](../../../../action/gb_splus_action.md), `GB-FINAL-ACTION` and `GB-FINAL-DENSITY`. Its compact normalization, already established in GB01 and GB16–GB20, is

```math
S=\frac1{2\kappa_5^2}\int d^5x\,e\,[\ell_{2\partial}+\lambda(-2\ell_{W,\mathrm{OP}}-4\ell_{\log})]_{\leq2\text{ physical fermions}},\qquad \lambda:=\lambda_{\mathrm{GB}}. \tag{1.1}
```

All individual terms used below are taken from `GB-FINAL-DENSITY`; (1.1) records normalization only. No separate bosonic GB action, pre-existing vacuum equation or pre-existing vacuum solution is used. The target is the complete local background catalogue within the stated class, obtained from the coefficients of arbitrary fluctuations in the first-order action. No unrestricted nonlinear Euler equations or quadratic mode operators are required.

We solve the displayed finite action exactly in its couplings. A separate small-$`\lambda`$ interpretation is identified in Step 5. Discarding four-fermion interactions cannot change $`S^{(0)}`$ or $`S^{(1)}`$ about a bosonic background.

## 1.2 Accepted convention ledger

The references are [CONVENTIONS.md](../../references/CONVENTIONS.md), lock `GB-FERMION-SPECTRUM-CONVENTIONS-v1`, and [COMPONENT_CONVENTIONS.md](../../references/COMPONENT_CONVENTIONS.md), especially C01–C06, L02–L03, SC7-01–06 and SC7D-05–07. These are given definitions, not objects of a new audit.

| Quantity | Convention used here |
|---|---|
| Indices and signature | $`\mu,\nu,a,b=0,1,2,3,4`$; $`i,j=1,2`$; $`\eta=\mathop{\mathrm{diag}}\nolimits(-,+,+,+,+)`$ |
| Measure and orientation | $`e=\det e_\mu{}^a>0`$; $`\varepsilon^{01234}=+1`$, $`\varepsilon_{01234}=-1`$, $`\varepsilon^{\mu\nu\rho\sigma\tau}=e^{-1}[\mu\nu\rho\sigma\tau]`$ |
| Curvature | $`R_{\mu\nu}{}^{ab}=2\partial_{[\mu}\omega_{\nu]}{}^{ab}+2\omega_{[\mu}{}^{ac}\omega_{\nu]c}{}^b`$; Ricci is GB-C03–04 |
| Constant curvature | $`R_{\mu\nu\rho\sigma}=k(g_{\mu\rho}g_{\nu\sigma}-g_{\mu\sigma}g_{\nu\rho})`$, $`R_{\mu\nu}=4kg_{\mu\nu}`$, $`R=20k`$ |
| Clifford algebra | $`\{\gamma^a,\gamma^b\}=2\eta^{ab}`$, $`\gamma^{a_1\cdots a_p}=\gamma^{[a_1}\cdots\gamma^{a_p]}`$, $`\gamma^{01234}=i`$ |
| Spinors | Odd symplectic Majorana fields; linear bar $`\bar u=u^T\mathsf C`$; left fermionic variations; no Dirac-conjugation replacement |
| Internal indices | NW–SE lowering, $`u_i=u^j\varepsilon_{ji}`$, $`\varepsilon_{12}=\varepsilon^{12}=1`$; unit-weight symmetrization |
| Derivatives | $`\mathcal D`$ is the full conformal/supercovariant derivative; $`\Box^c=\mathcal D^a\mathcal D_a`$; $`\nabla`$ denotes the Levi–Civita derivative derived at the relevant bosonic order |
| Engineering dimensions | $`[\nabla]=[g]=[N]=1`$, $`[k]=[D]=2`$, $`[L]=0`$, $`[\lambda]=-2`$, $`[\kappa_5^2]=-3`$ |
| Source gauge | $`\sigma=1`$, $`b_\mu=0`$, dilatino $`\psi^i=0`$, $`L^{ij}=\delta^{ij}L/\sqrt2`$; differentiated gauge-fixed fields retain their conformal descendants |

## 1.3 Independent variables and dependent objects

| Independent variable | Role | Arbitrary first variation |
|---|---|---|
| $`e_\mu{}^a`$ | Frame | $`\delta e_\mu{}^a=\tfrac12h_\mu{}^\nu\bar e_\nu{}^a+\theta^a{}_b\bar e_\mu{}^b`$, $`\theta_{ab}=-\theta_{ba}`$ |
| $`L,N`$ | Compensator scalars | $`\ell,n`$ |
| $`C_\mu,B_{\mu\nu}`$ | One- and two-form potentials | $`c_\mu,b_{\mu\nu}`$ |
| $`E_{\mu\nu\rho}`$ | Independent constrained-current potential | $`u_{\mu\nu\rho}`$ |
| $`V_\mu,V'_\mu{}^{ij}`$ | Trace and remaining internal connections | $`v_\mu,v'_\mu{}^{ij}`$, with the inherited trace decomposition |
| $`\psi_\mu^i,\varphi^i`$ | Gravitino and compensator spinor | $`\zeta_\mu^i,\xi^i`$ |

The dependent $`\omega,\phi,f,T,\chi,D,Y^{ij}`$ and composite LOG/Weyl multiplets are substituted through their defining relations. Neither $`D`$ nor $`f_{ab}`$ is an additional independent variation. The ordinary current $`P^\mu=e^{-1}\partial_\nu(eE^{\mu\nu})`$, with $`E^{\mu\nu}=-\varepsilon^{\mu\nu\rho\sigma\tau}E_{\rho\sigma\tau}/12`$, is varied through $`u_3`$; it is not an unconstrained vector. These statements use action GB07–GB14 and component L03/SC7-06.

No field is eliminated by assuming that its two-derivative equation remains algebraic in the GB theory. Step 5 solves constant background values only. This says nothing about their quadratic kinetic operators.

## 1.4 Precise expansion and permitted operations

Introduce an even parameter $`t`$ and write

```math
\Phi_B(t)=\bar\Phi_B+tq_B,\qquad \psi_\mu(t)=t\zeta_\mu,\quad\varphi(t)=t\xi,\qquad S(t)=S^{(0)}+tS^{(1)}+O(t^2). \tag{1.2}
```

The only imposed field restrictions are the accepted source gauge and the background ansatz of Step 2. No fluctuation gauge, auxiliary equation, supersymmetry equation or fluctuation constraint is imposed. Compactly supported test variations allow the explicitly displayed total divergences to be dropped from the bulk stationarity test; they are retained as currents in the derivation.

Every odd descendant vanishes when all physical fermions vanish. For example, action GB07 gives

```math
\mathcal D_a\psi^i\big|_{\mathrm P}=t\left(-\frac{gL_0}{2\sqrt2}\delta^{ij}\zeta_{aj}-\phi_a^{i(1)}\right)+O(t^2),\qquad
\chi^{i(1)}=\frac i8\gamma^a(\mathcal D_a\psi^i)^{(1)}+\frac g8\xi^i. \tag{1.3}
```

Thus a coefficient $`A=A_0+tA_1`$ multiplying any two odd factors $`U=tU_1+O(t^2)`$ and $`W=tW_1+O(t^2)`$ obeys

```math
A\bar U W=(A_0+tA_1)(t\bar U_1)(tW_1)+O(t^3)=t^2A_0\bar U_1W_1+O(t^3),\qquad [A\bar UW]_0=[A\bar UW]_1=0. \tag{1.4}
```

The same product evaluation applies to the bilinear corrections inside $`\omega`$, strengths, $`f`$ and $`D`$: their two odd factors are displayed in their defining relations, so neither background value nor first variation receives that bilinear contribution. This order statement does **not** discard any term of the eventual quadratic action.

The first-order stationarity test is

```math
S^{(1)}=\frac1{2\kappa_5^2}\left[\int d^5x\,\bar e\,q^I E_I^{(0)}+\int d^5x\,\partial_\mu(\bar eJ^\mu)\right],\qquad E_I^{(0)}=0\quad\text{for every independent }q^I. \tag{1.5}
```

Step 5 evaluates every coefficient in (1.5), classifying bosonic background solutions. The [selected AdS₅ analysis](../../../README.md) gives the separate Killing-spinor and fluctuation results.
