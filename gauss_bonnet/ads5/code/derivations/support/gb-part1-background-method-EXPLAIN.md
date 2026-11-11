---
concept: Maximally symmetric GB backgrounds from the zeroth- and first-order actions
date: 2026-09-29
mode: project-context
project_context: Full fermionic gauged GB action; Part I, Steps 1–5
citation_status: Exact local action and convention anchors inspected; external literature not used
status: Method explanation; no background-branch result asserted
convention_lock: GB-FERMION-SPECTRUM-CONVENTIONS-v1
---

# Why the first-order action determines the background branches

## Executive Summary

The specified calculation classifies maximally symmetric five-dimensional bosonic vacua of the accepted full fermionic gauged GB action. The background is symmetric, but the fluctuations used to test it remain arbitrary. Evaluating the action gives $`S^{(0)}`$; collecting the coefficient of each independent fluctuation in $`S^{(1)}`$ gives all background equations in the chosen source gauge. Solving those equations over every allowed parameter case produces Part I's branch catalogue. Fermionic tadpoles vanish on this bosonic background because the action is Grassmann even. Full conformal derivatives still require their defining connections, even when a compensator is constant. This note explains the method used in the [background catalogue](../../../details/background_branches.md).

## Why This Matters Here

The sole action input is [the full fermionic gauged GB action](../../../../action/gb_splus_action.md), GB01 and GB-FINAL-DENSITY. Its bosonic terms and its covariant definitions are evaluated directly. No separately sourced bosonic GB action is needed. In the notation of GB01, the accepted total density is

```math
\ell_{\rm tot}^{(0+2)}=\big[\ell_{2\partial}^{\rm inherited}+\lambda_{\rm GB}(-2\ell_{\rm W,OP}^{\rm inherited}-4\ell_{\log}^{\rm inherited})\big]_{\leq2}.
\tag{E01}
```

Equation E01 is quoted starting data, not a new construction. The superscript $`(0+2)`$ in its source denotes retained **physical-fermion degree**. The superscripts in $`S^{(0)}`$ and $`S^{(1)}`$ below denote **fluctuation order**. Confusing these counts would obscure why an action with two-fermion interactions can have a purely bosonic first-order fluctuation action.

The [shared procedure](../../WALKTHROUGH.md), Part I, Steps 1–5, specifies the method. The accepted action and conventions are inputs. The perturbative calculation checks its expansion and its solutions; it does not reopen their certification or require unrestricted nonlinear Euler equations.

## Prerequisites and Dependencies

Three distinctions organize the calculation:

1. **Independent fields and composites.** Vary the source-gauge independent fields. Expand $`T`$, $`D`$, $`\chi`$, $`Y`$ and dependent connections through their existing definitions. A conventional curvature constraint defining a dependent connection is not an auxiliary equation derived from the GB action.
2. **Background restrictions and variations.** A background condition such as $`\bar C_\mu=0`$ does not imply $`\delta C_\mu=0`$. Background geometry determines where the variation is evaluated, not which independent variations exist.
3. **Stationarity and dynamics.** $`S^{(1)}`$ tests whether the candidate background is stationary. $`S^{(2)}`$ determines the dynamics of its infinitesimal excitations. Only the former is part of this request.

The [anchored conventions](../../references/CONVENTIONS.md), GB-C01–GB-C14, give the fields and geometry. The [component reference](../../references/COMPONENT_CONVENTIONS.md), L02, SC7-04, SC7-06 and SC7D-05–SC7D-07, gives the relevant descendants. These inspected local anchors are sufficient for the explanation below.

## Core Explanation

### Problem and target

The target is the entire solution set within **maximally symmetric five-dimensional bosonic vacua**, including exceptional couplings and disconnected branches. It is not a choice of an AdS vacuum in advance. The sign of the solved curvature parameter determines the geometry. Supersymmetry is a separate property to test with the gauge-preserving fermion transformations if a supersymmetry claim is made.

The background class concerns the full physical configuration, including gauge-covariant matter data. A maximally symmetric metric by itself does not establish that an arbitrary matter configuration is a maximally symmetric vacuum. Step 2 must therefore state its symmetry conditions on the matter fields and derive any resulting zero background strengths. This is distinct from imposing a fluxless truncation on the fluctuating fields. Topological identifications, flat-connection holonomies and global boundary data require an explicit scope statement; local curvature data alone do not classify them.

### Convention ledger

<!-- ASSERT_CONVENTION: natural_units=true, metric_signature=(-,+,+,+,+), source_lock=GB-FERMION-SPECTRUM-CONVENTIONS-v1, fourier_convention=not_used, derivative=full_supercovariant, source_gauge_evaluation=after_ordered_differentiation -->

Use five Lorentzian dimensions, $`a,\mu=0,1,2,3,4`$ and $`i=1,2`$. The retained gauge is $`\sigma=1`$, $`b_\mu=0`$, dilatino $`\psi^i=0`$, and $`L^{ij}=\delta^{ij}L/\sqrt2`$; the gravitino $`\psi_\mu^i`$ and compensator fermion $`\varphi^i`$ remain independent. In particular, the source gauge does not fix $`L`$ to unity. The Majorana bar is linear and all physical fermions are Grassmann odd. The bookkeeping parameter $`t`$ is real, dimensionless and Grassmann even. These are GB02–GB06 and assumptions A1–A3 of the accepted action.

The accepted curvature convention in GB04 is

```math
\bar R_{\mu\nu\rho\sigma}=k(\bar g_{\mu\rho}\bar g_{\nu\sigma}-\bar g_{\mu\sigma}\bar g_{\nu\rho}),\qquad \bar R_{\mu\nu}=4k\bar g_{\mu\nu},\qquad \bar R=20k.
\tag{E02}
```

Here $`k`$ is an unknown background parameter, not an already solved function of $`g`$ and $`\lambda_{\rm GB}`$. The engineering dimensions from GB05 are $`[k]=2`$, $`[g]=1`$, $`[L]=0`$, $`[N]=1`$, $`[\lambda_{\rm GB}]=-2`$ and $`[\kappa_5^2]=-3`$.

### Why arbitrary fluctuations are essential

Write every independent bosonic variable collectively as $`\Phi_B`$, and the two independent fermion species as $`\Psi=(\psi_\mu,\varphi)`$. A bosonic background has $`\bar\Psi=0`$. The fluctuation definition and Taylor coefficients are

```math
\Phi_B=\bar\Phi_B+tq_B,\qquad \Psi=tq_F,\qquad S[\bar\Phi_B+tq_B,tq_F]=S^{(0)}+tS^{(1)}+O(t^2).
\tag{E03}
```

The first-order action contains derivatives of the arbitrary $`q_B`$ until integrations by parts collect their coefficients. For example, consider one term $`\int_M\bar e\,b^\mu\bar\nabla_\mu q`$, where $`q`$ is an even scalar and $`b^\mu`$ is an even background vector coefficient. The ordinary torsion-free product rule gives

```math
\bar\nabla_\mu(b^\mu q)=(\bar\nabla_\mu b^\mu)q+b^\mu\bar\nabla_\mu q.
\tag{E04}
```

Subtract its first term and multiply by the measure. The density divergence identity is $`\bar e\,\bar\nabla_\mu(b^\mu q)=\partial_\mu(\bar e\,b^\mu q)`$, so the actual derivative term becomes

```math
\bar e\,b^\mu\bar\nabla_\mu q=\partial_\mu(\bar e\,b^\mu q)-\bar e\,(\bar\nabla_\mu b^\mu)q.
\tag{E05}
```

Integrating gives its surface contribution and its bulk coefficient:

```math
\int_Md^5x\,\bar e\,b^\mu\bar\nabla_\mu q=\int_{\partial M}d\Sigma_\mu\,b^\mu q-\int_Md^5x\,\bar e\,(\bar\nabla_\mu b^\mu)q.
\tag{E06}
```

For compactly supported $`q`$, the displayed surface term is zero. No Grassmann sign occurs: both factors and the derivative are even. This example explains the operation; Step 5 must perform the actual transfers for the GB terms, including tensor and form indices and the retained boundary representative.

Once all derivative transfers have been displayed, the first-order action has the form

```math
S^{(1)}=\int_Md^5x\,q^I\mathbf E_I^{(0)}+\int_{\partial M}\Theta^{(1)}.
\tag{E07}
```

Each $`\mathbf E_I^{(0)}`$ is the computed densitized coefficient of an independent fluctuation. With compactly supported variations, choose one field component $`q^J`$ freely and set the others to zero. Equation E07 then reduces to $`S^{(1)}=\int q^J\mathbf E_J^{(0)}`$. Stationarity for every such test function implies $`\mathbf E_J^{(0)}=0`$. Repeat that choice for each independent component. This is a test at the background and does not require the full nonlinear Euler system.

To see the limitation of $`S^{(0)}`$ alone, parameterize the background by constants $`p^A`$. A variation restricted to the ansatz has $`q^I=(\partial\bar\Phi^I/\partial p^A)\delta p^A`$. Insert that expression into E07, with the corresponding boundary term kept separate:

```math
\delta S^{(0)}=\int_Md^5x\,\frac{\partial\bar\Phi^I}{\partial p^A}\,\delta p^A\,\mathbf E_I^{(0)}+\delta S_{\partial M}^{(0)}.
\tag{E08}
```

For a field $`\bar\Phi^J=0`$ throughout the ansatz, $`\partial\bar\Phi^J/\partial p^A=0`$. Its contribution to E08 is explicitly $`0\times\delta p^A\times\mathbf E_J^{(0)}=0`$, irrespective of the value of $`\mathbf E_J^{(0)}`$. Reduced stationarity therefore contains no information about that coefficient. Keeping its arbitrary fluctuation in E07 prevents this loss. Even when symmetry eventually forces a coefficient to vanish identically, the calculation records that zero rather than removing the variation beforehand.

### Why there is no fermionic tadpole

A term of physical-fermion degree two contains two odd factors, which may include derivatives or odd composites. Write an individual such bilinear as $`\bar\Psi_r\mathcal K^{rs}(\Phi_B)\Psi_s`$; this is illustrative degree bookkeeping, not a replacement for the displayed action. The bar is linear, so $`\overline{tq_r}=t\bar q_r`$. Since $`t`$ is even, moving it past either odd factor produces no minus sign. Substitution gives

```math
\overline{tq_r}\,\mathcal K^{rs}(\bar\Phi_B+tq_B)\,tq_s=t^2\bar q_r\mathcal K^{rs}(\bar\Phi_B+tq_B)q_s.
\tag{E09}
```

Here $`r,s`$ label fermion components; $`\Phi_B`$ and $`q_B`$ keep their collective bosonic meanings. Expanding the bosonic coefficient around the background gives $`\mathcal K(\bar\Phi_B+tq_B)=\mathcal K(\bar\Phi_B)+O(t)`$. Therefore E09 has leading order $`t^2`$ and contributes exactly zero to the coefficients of $`t^0`$ and $`t^1`$. An omitted physical-fermion quartic term starts at $`t^4`$, so it also cannot change $`S^{(0)}`$ or $`S^{(1)}`$.

This count applies after the dependent objects are interpreted through their full definitions. A boson-looking hatted object can contain a fermion bilinear, but that bilinear still has two physical fermions and begins at $`t^2`$. Vanishing fermionic tadpoles establish stationarity in odd directions; they do **not** establish unbroken supersymmetry. That claim requires the distinct Killing-spinor calculation.

### Why a constant compensator has nontrivial descendants

The accepted derivative is the full superconformal derivative GB06. Its outer action on a first derivative contains the transformation laws of that descendant. Consequently, the statement $`\mathcal D_a\sigma|_{\rm P}=0`$ in the source gauge cannot be differentiated as an identity of ordinary scalar functions.

The inspected component relation SC7D-05 states $`\delta_K(\Lambda_K)\mathcal D_b\sigma|_{\rm P}=-2\Lambda_{Kb}`$. The full outer derivative contains $`-\delta_K(f_a)`$; substituting the actual parameter gives

```math
-\delta_K(f_a)\mathcal D_b\sigma\big|_{\rm P}=-(-2f_{ab})=+2f_{ab}.
\tag{E10}
```

This is the surviving bosonic connection contribution in GB08 or SC7D-06. At zero physical fermions, those equations reduce to

```math
\mathcal D_a\mathcal D_b\sigma\big|_{{\rm P},\Psi=0}=2f_{ab},\qquad \Box^c\sigma\big|_{{\rm P},\Psi=0}=2f_a{}^a.
\tag{E11}
```

Use the **given** dependent-connection solution SC7-06, $`f_{ab}=-\mathcal R_{ab}/6+\eta_{ab}\mathcal R/48`$. Its explicit trace is

```math
f_a{}^a=-\frac16\mathcal R+\frac{5}{48}\mathcal R=\left(-\frac8{48}+\frac5{48}\right)\mathcal R=-\frac3{48}\mathcal R=-\frac1{16}\mathcal R.
\tag{E12}
```

The bosonic primed Ricci scalar is the ordinary scalar curvature in this source gauge. Insert E12 in E11, then E02:

```math
\Box^c\sigma\big|_{{\rm P},\Psi=0}=2\left(-\frac1{16}R\right)=-\frac18R,\qquad \overline{\Box^c\sigma}=-\frac18(20k)=-\frac52k.
\tag{E13}
```

This is a descendant evaluation at arbitrary $`k`$, not a vacuum equation or solved curvature. In contrast, the Levi–Civita Laplacian on the numerical constant one gives $`\nabla_a1=0`$ and hence $`\nabla^a\nabla_a1=\nabla^a0=0`$. The difference is accounted for by E10. Applying the wrong Laplacian would erase curvature contributions already present in the accepted action.

There is a second, distinct issue for the independent compensator $`L^{ij}`$. GB09 gives

```math
\mathcal D_aL^{ij}\big|_{\rm P}=\frac{\delta^{ij}}{\sqrt2}\partial_aL+\frac L{\sqrt2}\big(V'_a{}^i{}_k\delta^{jk}+V'_a{}^j{}_k\delta^{ik}\big)-i\bar\psi_a^{(i}\varphi^{j)}.
\tag{E14}
```

At constant $`L=L_0`$ and zero fermions, insert $`\partial_aL_0=0`$ and $`\bar\psi_a^{(i}\varphi^{j)}=0`$ into E14:

```math
\mathcal D_aL^{ij}\big|_{\partial L=0,\Psi=0}=\frac{\delta^{ij}}{\sqrt2}\,0+\frac{L_0}{\sqrt2}\big(V'_a{}^i{}_k\delta^{jk}+V'_a{}^j{}_k\delta^{ik}\big)-i\,0=\frac{L_0}{\sqrt2}\big(V'_a{}^i{}_k\delta^{jk}+V'_a{}^j{}_k\delta^{ik}\big).
\tag{E15}
```

Thus constancy alone does not remove the R-symmetry connection. The background symmetry conditions determine its background value. Even if that value vanishes, its arbitrary fluctuation still enters the descendant expansion. One cannot classify its dynamical status from this observation alone; that requires Part II.

## Formal Structure / Equations

Part I implements the following order, with a separate calculation file for each numbered step:

| Step | Mathematical task | What the output establishes |
|---|---|---|
| 1 | Record E01, the accepted source gauge, fields and composite definitions | Which variables may vary independently |
| 2 | Declare the maximally symmetric background and arbitrary fluctuations | The scope in which branch completeness can be claimed |
| 3 | Expand the source ingredients through $`t^1`$ | Every contribution capable of entering $`S^{(0)}`$ or $`S^{(1)}`$ |
| 4 | Evaluate $`S^{(0)}`$ with background parameters free | The background density, with volume and boundary scope stated |
| 5 | Evaluate $`S^{(1)}`$, impose every coefficient in E07 and solve all cases | The branches, their existence domains, background critical loci and limits |

On infinite-volume backgrounds, a local density or explicitly volume-factored $`S^{(0)}`$ is meaningful without assigning a finite value to the unregulated total action. For bulk stationarity, compactly supported fluctuations make the local tadpole test precise. Boundary free energies and mode boundary conditions are separate questions.

The constrained compensator current requires its independent three-form potential. GB-C14 gives its bosonic ordinary-current relation $`P^a=-e_\mu{}^a\epsilon^{\mu\nu\rho\sigma\lambda}\partial_\nu E_{\rho\sigma\lambda}/12`$. Thus varying an arbitrary unconstrained vector in its place changes the variational problem. Step 5 must retain the potential variation or declare and prove an equivalent constrained formulation.

### All branches, exceptional cases and critical loci

Suppose a solved background equation contains a factor $`A`$ multiplying an expression $`F`$. The logical decomposition is $`AF=0\Rightarrow(A=0)\lor(A\ne0\ \text{and}\ F=0)`$. Dividing by $`A`$ preserves only the second case. The first case must be substituted into **every original tadpole equation**; it can describe no solution, a special isolated solution, or a continuous family. This is the reason for the case ledger, not a numerical claim about GB.

The same bookkeeping applies to the gauge coupling, higher-derivative coupling, leading polynomial coefficients and factors introduced by algebraic elimination. A singularity of an input expression, such as a boundary of its admitted compensator patch, is recorded as an input-domain restriction; it is not automatically a missed finite branch that division concealed.

Background critical loci concern the stationary solutions: branch mergers, changes in real-solution count, rank changes of the background equations, new moduli and existence boundaries. Spectral critical loci concern $`S^{(2)}`$: kinetic rank, colliding fluctuation modes, vanishing norms and stability thresholds. A background-equation Jacobian and a spacetime fluctuation operator answer different questions. Part I does not infer the latter from the former.

An exact branch of the accepted finite action need not have a regular $`\lambda_{\rm GB}\to0`$ limit. Keep it in the exact catalogue and record its limiting behavior. A controlled EFT interpretation requires a separately stated small-curvature/small-coupling regime; failure of that regime is not an algebraic proof that the exact finite-action branch is absent.

## Consistency Checks

The displayed explanatory identities have the following explicit checks. The complete source-term and branch-residual checks belong to the calculation files and their verification report.

For E03, $`[t]=0`$ implies $`[q_B]=[\Phi_B]`$ and $`[q_F]=[\Psi]`$. Multiplication by $`t`$ changes fluctuation degree without changing mass dimension or Grassmann parity. For E09, two odd fluctuations give an even product, while two factors of $`t`$ give degree two; there is no degree-one contribution.

For the integration by parts E05, $`[\bar\nabla]=1`$. Therefore $`[b^\mu\bar\nabla_\mu q]=[b]+1+[q]`$, $`[(\bar\nabla_\mu b^\mu)q]=([b]+1)+[q]`$, and $`[\partial_\mu(b^\mu q)]=1+[b]+[q]`$. The dimensions agree term by term. Both sides are scalar densities after multiplication by $`\bar e`$. Its boundary term has been displayed, and compact support is the stated reason for setting it to zero in the bulk test.

For E13, $`[\Box^c\sigma]=2+0=2`$, $`[R]=2`$ and $`[k]=2`$. At $`k=0`$, E13 gives $`-(5/2)\times0=0`$, agreeing with the zero trace of the background dependent K connection from E12. This is a check of the descendant formula, not evidence that a flat solution exists for any particular coupling.

For E15, $`[L_0]=0`$ and $`[V'_a]=1`$, so the remaining connection term has dimension one, equal to $`[\mathcal D_aL^{ij}]=1+0`$. At $`V'_a{}^{ij}=0`$, the two displayed connection contributions vanish separately and E15 is zero. Constancy without this connection condition does not produce that cancellation.

No Fierz rearrangement, spinor interchange, auxiliary elimination, Killing-spinor solution or numerical branch root is used in this explanation. It makes no dimensionally unsupported mass or stability claim.

## Final Result

The method establishes the following operational statement, conditional on the stated background class and accepted input definitions:

```math
\boxed{\text{Background branches are the solutions of all evaluated coefficients }\mathbf E_I^{(0)}=0\text{ in }S^{(1)}.}
\tag{E16}
```

The words “evaluated coefficients” are essential. Equation E16 specifies the calculation. The evaluated GB tadpoles and solutions of their undivided system are given in the [background catalogue](../../../details/background_branches.md).

## Project-Specific Connection

The [background derivation](../background/README.md) gives the inputs and fields, background scope, ingredient expansion, zeroth-order action and branch catalogue. This note supplies their methodological context.

The source equations and retained fermion order are specified in the action’s §7. The background derivation evaluates the fluctuation expansion, collects first-order coefficients, partitions the solution cases and substitutes the branches into the tadpole equations. The two-derivative auxiliary solution and known AdS branches serve as limiting comparisons rather than inputs to those equations.

## Common Confusions and Failure Modes

| Confusion | Consequence | Correct operation |
|---|---|---|
| “The background field is zero, so its variation is zero.” | A tadpole equation can be lost | Keep the independent fluctuation and calculate its coefficient |
| “The compensator is constant, so every covariant derivative vanishes.” | Conformal or R-symmetry connection terms disappear incorrectly | Apply the accepted descendant definitions before evaluating the gauge and background |
| “No fermionic tadpole means the vacuum is supersymmetric.” | A stationarity result becomes an unsupported SUSY claim | Solve the gauge-preserving Killing-spinor conditions separately if claiming SUSY |
| “The two-derivative auxiliary solution must still hold.” | Higher-derivative branches can be excluded prematurely | Solve the actual first-order tadpole system |
| “A denominator is usually nonzero.” | Exceptional coupling solutions or moduli are missed | Split its zero and nonzero cases in the original equations |
| “A branch merger is a ghost-free critical point.” | Background and dynamical questions are conflated | Reserve kinetic signs and spectral degeneracies for Part II |
| “One acceptable AdS solution finishes the classification.” | Other curvatures, signs and disconnected solutions are omitted | Exhaust the declared maximally symmetric domain |

## Literature Guide

The reading path follows the specified action and conventions through their component expansion. These source equations determine the calculation.

1. **Starting data:** [Full fermionic gauged GB action](../../../../action/gb_splus_action.md), GB01–GB09 and GB-FINAL-DENSITY. Read the coupling normalization, retained fermion degree and descendant definitions before the long density.
2. **Working conventions:** [Anchored conventions](../../references/CONVENTIONS.md), GB-C01–GB-C14. Use the field table, source gauge, curvature sign and independent form-current definitions.
3. **Component details:** [Extracted component reference](../../references/COMPONENT_CONVENTIONS.md), L02, SC7-04, SC7-06 and SC7D-05–SC7D-07. These locate the explicit compensator derivatives, dependent K connection and scalar conformal box used in E10–E15.
4. **Method:** [Shared spectrum procedure](../../WALKTHROUGH.md), Part I, Steps 1–5 and the Part I completion gate.



## Convention Dependence and Scope

The signs in E10–E15 use the fixed component derivative, curvature and K-connection definitions. They must not be transplanted into a convention with a different Riemann sign or conformal-connection normalization without conversion. No conversion is made here.

The [background catalogue](../../../details/background_branches.md) gives $`k`$, $`L`$ and $`N`$, the branch domains, exceptional loci and limiting relations within its local maximally symmetric background class. The [selected AdS₅ spectrum](../../../README.md) gives the supersymmetry and fluctuation analysis on the chosen branch.


