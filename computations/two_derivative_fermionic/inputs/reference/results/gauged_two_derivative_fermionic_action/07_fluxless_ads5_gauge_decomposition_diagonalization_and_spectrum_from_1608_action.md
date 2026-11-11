# Fluxless AdS5 gauge fixing, diagonalization, equations, and spectrum

> **Spectrum lock:** `2DER-GDW-FLUXLESS-ADS5-SPECTRUM-OZKAN1608-v2`  
> **Quadratic parent lock:** `2DER-GDW-FLUXLESS-ADS5-S0S1S2-OZKAN1608-v2`  
> **Quadratic parent:** `06_fluxless_ads5_zeroth_first_second_order_actions_from_1608_action.md`, Eq. (15.4)  
> **Status:** local fluxless-AdS5 spectrum derived from the active 2016-map action, exact at the quadratic order certified by the parent

<!-- ASSERT_SPECTRUM_LOCK: 2DER-GDW-FLUXLESS-ADS5-SPECTRUM-OZKAN1608-v2 -->
<!-- ASSERT_PARENT_LOCK: 2DER-GDW-FLUXLESS-ADS5-S0S1S2-OZKAN1608-v2 -->
<!-- ASSERT_BACKGROUND: L=1, N=-3g/2, k=-g^2/2, ell^2=2/g^2 -->
<!-- ASSERT_FORWARD_DIAGONALIZATION: representation_not_used_as_input=true -->
<!-- ASSERT_DIAGONAL_SPINOR: kinetic=-2/3, mass=+1/3 -->

## 1. Aim and certification boundary

1. vary the raw action before imposing a fluctuation gauge;
2. display the algebraic and constraint equations;
3. complete the $`N^{(1)}`$ square;
4. diagonalize the metric--scalar block locally;
5. fix the diffeomorphism, one-form, two-form, and local-supersymmetry gauges;
6. complete the gravitino--spinor square with all NW--SE signs visible;
7. derive the diagonal equations and their AdS masses;
8. compare those independently derived values with the relevant
   $`SU(2,2|1)`$ representations.

No inverse differential operator, transverse projector, auxiliary kinetic
term, or higher-derivative equation is introduced.  The symbols used for
diagonal combinations and irreducible pieces are temporary components of
the original fields, not additional physical fields.

The conclusion is a local particle-spectrum statement.  The standard
normalizable supersymmetric AdS boundary conditions are used when assigning
representations.  Possible global harmonic forms and alternative boundary
conditions are outside this local count.

## 2. Source and provenance ledger

| Item | Exact source and location |
| --- | --- |
| nonlinear gauged action | `05_gauged_two_derivative_full_fermionic_action_from_1608_map.md`, lock `2DER-GDW-P-PSI0-OZKAN1608-QUADRATIC-FERMION-v2` |
| zeroth-, first-, and raw second-order action | `06_fluxless_ads5_zeroth_first_second_order_actions_from_1608_action.md`, Eq. (15.4), lock `2DER-GDW-FLUXLESS-ADS5-S0S1S2-OZKAN1608-v2` |
| fluxless AdS background | same file, Sections 5--7 and 16.1 |
| form definitions and target normalization | Gold et al., `Sources/2025-Gold-On five-dimensional curvature squared supergravity and holography.pdf`, Eqs. (25)--(27), PDF p. 14 |
| on-shell two-form duality and supersymmetry combinations | Coomans--Özkan, `Sources/2013-Coomans-Ozkan-Internally-Gauged-D5-N2-Supergravity.pdf`, Eqs. (5.17) and (5.30), PDF pp. 18 and 20 |
| modern $`4d\;\mathcal N=1`$ current-multiplet labels | Córdova--Dumitrescu--Intriligator, [arXiv:1612.00809](https://arxiv.org/pdf/1612.00809), Eq. (5.89), §5.5.1, printed pp. 122–123 / PDF pp. 123–124; directly inspected 2026-09-08 |

The representation-classification source is used only after the action
eigenvalues have been obtained.  The local component sources do not tabulate
the modern $`A\bar A[j;\bar j]_{\Delta}^{(r)}`$ notation; this is the precise
missing item for which the external classification is used.

The exact SHA-256 hashes of the active inputs are

```text
05_gauged_two_derivative_full_fermionic_action_from_1608_map.md
6a05742d1c2bb798fcb10b973fa6045165f4ff77a302f02f42b23c3a20b7d2fe

06_fluxless_ads5_zeroth_first_second_order_actions_from_1608_action.md
8bead154d98c1aa9c805708d97a445a846dd05de778079d762703d7c8d87657c

verify_fluxless_ads5_s0_s2_from_1608_action.py
7a0516ac59824ba91d87cb96e34a0353a33b1d5b216e0579c1df1f6de644cd01
```

## 3. Conventions and identities

### 3.1 AdS geometry

The signature and curvature convention are

```math
\eta_{ab}=\mathop{\mathrm{diag}}\nolimits(-,+,+,+,+),
\qquad
[\bar\nabla_\mu,\bar\nabla_\nu]\zeta
=\frac14\bar R_{\mu\nu}{}^{ab}\gamma_{ab}\zeta.
\tag{3.1}
```

The background is

```math
\bar R_{\mu\nu\rho\sigma}
=k\left(
\bar g_{\mu\rho}\bar g_{\nu\sigma}
-\bar g_{\mu\sigma}\bar g_{\nu\rho}
\right),
\tag{3.2}
```

```math
\bar R_{\mu\nu}=4k\bar g_{\mu\nu},
\qquad
\bar R=20k,
\qquad
k=-\frac{g^2}{2}=-\frac1{\ell^2}.
\tag{3.3}
```

Thus

```math
\ell^2=\frac2{g^2},
\qquad
\ell^{-1}=\frac{|g|}{\sqrt2}.
\tag{3.4}
```

The displayed charge formulas use the orientation (g>0).  Reversing (g)
interchanges the two conjugate charge branches and leaves all absolute masses
and dimensions unchanged.

Equality modulo a covariant boundary term is denoted by $`\doteq`$. Such
terms vanish for compactly supported fluctuations or for the standard AdS
falloffs used below.

### 3.2 Linearized curvature

For a metric fluctuation $`h_{\mu\nu}^{(1)}`$,

```math
R^{(1)}(h)
=\bar\nabla_\mu\bar\nabla_\nu h^{\mu\nu}
-\bar\Box h-4kh.
\tag{3.5}
```

Since $`-4k=2g^2`$, Eq. (3.5) is the same definition used in the parent.
The cosmological linearized Einstein tensor is

```math
\mathcal G_{\mu\nu}^{(1)}(h)
=R_{\mu\nu}^{(1)}(h)
-\frac12\bar g_{\mu\nu}R^{(1)}(h)
-4k h_{\mu\nu}.
\tag{3.6}
```

It satisfies

```math
\bar\nabla^\mu\mathcal G_{\mu\nu}^{(1)}(h)=0,
\tag{3.7}
```

```math
\int d^5x\,\bar e\,
X^{\mu\nu}\mathcal G_{\mu\nu}^{(1)}(Y)
\doteq
\int d^5x\,\bar e\,
Y^{\mu\nu}\mathcal G_{\mu\nu}^{(1)}(X),
\tag{3.8}
```

and

```math
\bar g^{\mu\nu}\mathcal G_{\mu\nu}^{(1)}(h)
=-\frac32R^{(1)}(h).
\tag{3.9}
```

For a pure trace perturbation $`\bar g_{\mu\nu}s`$, direct substitution
gives

```math
R^{(1)}(\bar g s)
=-4\bar\Box s-20ks,
\tag{3.10}
```

```math
\mathcal G_{\mu\nu}^{(1)}(\bar g s)
=\frac32\left(
\bar g_{\mu\nu}\bar\Box
-\bar\nabla_\mu\bar\nabla_\nu
+4k\bar g_{\mu\nu}
\right)s.
\tag{3.11}
```

To verify Eq. (3.10) by hand, use

```math
\bar\nabla_\mu\bar\nabla_\nu
(\bar g^{\mu\nu}s)=\bar\Box s,
\qquad
\bar g^{\mu\nu}\bar g_{\mu\nu}=5,
\qquad
h=5s.
\tag{3.12}
```

Then Eq. (3.5) gives

```math
\bar\Box s-5\bar\Box s-4k(5s)
=-4\bar\Box s-20ks.
\tag{3.13}
```

### 3.3 NW--SE and Majorana rules

The $`SU(2)`$ convention is

```math
A^i=\varepsilon^{ij}A_j,
\qquad
A_i=A^j\varepsilon_{ji},
\qquad
\varepsilon_{12}=\varepsilon^{12}=1.
\tag{3.14}
```

Useful consequences are

```math
\varepsilon^{ir}\varepsilon_{ki}
=-\delta^r{}_k,
\qquad
\varepsilon^{ik}\delta_{kj}\varphi^j
=-\delta^{ij}\varphi_j.
\tag{3.15}
```

The source uses the Majorana bar (transpose times C), as stated in
Appendix A (A.4) of the 5D Weyl-multiplet convention paper. It does not
reverse an epsilon or complex-conjugate a commuting coefficient:

```math
\overline{A_i}=\bar A^j\varepsilon_{ji}.
\tag{3.15a}
```

Consequently,

```math
\begin{aligned}
\delta^{ij}\bar A_jB_i
&=\delta^{ij}\varepsilon_{kj}\varepsilon_{\ell i}
\bar A^kB^\ell\\
&=+\delta_{k\ell}\bar A^kB^\ell.
\end{aligned}
\tag{3.15b}
```

Use this sign together with the explicit gamma transpose, not an
antilinear bar rule borrowed without its symplectic-Majorana conversion.

For fixed upper indices,

```math
\bar\alpha^i\gamma_{(n)}\beta^j
=t_n\bar\beta^j\gamma_{(n)}\alpha^i,
\qquad
t_0=t_1=+1,
\qquad
t_2=t_3=-1.
\tag{3.16}
```

For an NW--SE contraction, the epsilon exchange gives another minus sign:

```math
\bar\alpha^i\gamma_{(n)}\beta_i
=-t_n\bar\beta^i\gamma_{(n)}\alpha_i.
\tag{3.17}
```

The two rules are not interchangeable.  The five-dimensional Clifford
identities used in the fermionic square are

```math
\gamma^{\mu\nu\rho}\gamma_\rho
=3\gamma^{\mu\nu},
\qquad
\gamma_\mu\gamma^{\mu\nu\rho}
=3\gamma^{\nu\rho},
\tag{3.18}
```

```math
\gamma^{\mu\nu}\gamma_\nu=4\gamma^\mu,
\qquad
\gamma_\mu\gamma^{\mu\nu}=4\gamma^\nu,
\qquad
\gamma_\mu\gamma^{\mu\nu}\gamma_\nu=20.
\tag{3.19}
```

## 4. The sole input: the active raw quadratic action

Write $`s=L^{(1)}`$ only inside prose calculations below; every boxed action
retains the original symbol $`L^{(1)}`$. The raw action is

```math
\boxed{
\begin{aligned}
\bar e^{-1}\mathcal L^{(2)}\doteq{}&
-\frac12h^{\mu\nu}\mathcal G_{\mu\nu}^{(1)}(h)
+L^{(1)}R^{(1)}(h)
+(\bar\nabla L^{(1)})^2\\
&-4g^2(L^{(1)})^2
-8gL^{(1)}N^{(1)}
-2(N^{(1)})^2\\
&-\frac12G_{\mu\nu}^{(1)}G^{(1)\mu\nu}
-\frac13H_{\mu\nu\rho}^{(1)}H^{(1)\mu\nu\rho}\\
&-2E_a^{(1)}E^{(1)a}
-2\sqrt2E^{(1)a}V_a^{(1)}
-4gE^{(1)a}C_a^{(1)}\\
&+2V_a^{\prime(1)ij}V^{\prime(1)a}_{ij}\\
&-\bar\psi_\mu^{(1)i}\gamma^{\mu\nu\rho}
\bar\nabla_\nu\psi_{\rho i}^{(1)}\\
&+2\bar\varphi^{(1)i}\not{\bar\nabla}\varphi_i^{(1)}\\
&+2i\sqrt2\delta_{ij}\bar\varphi^{(1)i}
\gamma^{\mu\nu}\bar\nabla_\mu\psi_\nu^{(1)j}\\
&-\frac{3ig}{2\sqrt2}\delta_{ij}
\bar\psi_\mu^{(1)i}\gamma^{\mu\nu}\psi_\nu^{(1)j}\\
&-4g\bar\psi_\mu^{(1)i}\gamma^\mu\varphi_i^{(1)}\\
&+\frac{7ig}{\sqrt2}\delta_{ij}
\bar\varphi^{(1)i}\varphi^{(1)j}.
\end{aligned}}
\tag{4.1}
```

Here

```math
G_{\mu\nu}^{(1)}=2\bar\nabla_{[\mu}C_{\nu]}^{(1)},
\tag{4.2}
```

```math
H_{\mu\nu\rho}^{(1)}
=3\bar\nabla_{[\mu}B_{\nu\rho]}^{(1)}
+\frac g2E_{\mu\nu\rho}^{(1)},
\tag{4.3}
```

```math
E^{(1)a}
=-\frac1{12}\bar\varepsilon^{abcde}
\bar\nabla_bE_{cde}^{(1)}.
\tag{4.4}
```

Equation (4.1), including the forward-derived coefficient (+7), is the
only dynamical input to the following diagonalization.

## 5. Vary before fixing a fluctuation gauge

### 5.1 Metric, scalar, and (N)

Using self-adjointness (3.8), variation with respect to $`h^{\mu\nu}`$
gives

```math
\delta\left[-\frac12h\mathcal G(h)\right]
\doteq
-\delta h^{\mu\nu}\mathcal G_{\mu\nu}^{(1)}(h).
\tag{5.1}
```

For the mixed term,

```math
\delta_h\left[L^{(1)}R^{(1)}(h)\right]
\doteq
\delta h^{\mu\nu}
\left(
\bar\nabla_\mu\bar\nabla_\nu
-\bar g_{\mu\nu}\bar\Box
-4k\bar g_{\mu\nu}
\right)L^{(1)}.
\tag{5.2}
```

Therefore

```math
\boxed{
-\mathcal G_{\mu\nu}^{(1)}(h)
+\left(
\bar\nabla_\mu\bar\nabla_\nu
-\bar g_{\mu\nu}\bar\Box
-4k\bar g_{\mu\nu}
\right)L^{(1)}=0.}
\tag{5.3}
```

The scalar kinetic term varies as

```math
\delta\left[(\bar\nabla L^{(1)})^2\right]
\doteq
-2\delta L^{(1)}\bar\Box L^{(1)}.
\tag{5.4}
```

Hence the scalar and (N) equations are

```math
\boxed{
R^{(1)}(h)
-2\bar\Box L^{(1)}
-8g^2L^{(1)}
-8gN^{(1)}=0,}
\tag{5.5}
```

```math
\boxed{-8gL^{(1)}-4N^{(1)}=0.}
\tag{5.6}
```

### 5.2 Vector, forms, and (R)-connections

The vector variation is

```math
\delta\left[-\frac12G_{\mu\nu}G^{\mu\nu}\right]
\doteq
2\bar\nabla_\mu G^{\mu\nu}\delta C_\nu.
\tag{5.7}
```

Together with $`-4gE^\nu\delta C_\nu`$, it gives

```math
\boxed{
\bar\nabla_\mu G^{(1)\mu\nu}
-2gE^{(1)\nu}=0.}
\tag{5.8}
```

Since

```math
\delta_BH_{\mu\nu\rho}^{(1)}
=3\bar\nabla_{[\mu}\delta B_{\nu\rho]}^{(1)},
\tag{5.9}
```

integration by parts gives

```math
\boxed{\bar\nabla_\mu H^{(1)\mu\nu\rho}=0.}
\tag{5.10}
```

The trace and traceless (R)-connection equations are algebraic:

```math
\boxed{E_a^{(1)}=0,}
\tag{5.11}
```

```math
\boxed{V_a^{\prime(1)ij}=0.}
\tag{5.12}
```

For the three-form, first note

```math
\delta_EH_{\mu\nu\rho}^{(1)}
=\frac g2\delta E_{\mu\nu\rho}^{(1)}.
\tag{5.13}
```

The $`H^2`$ term therefore contributes

```math
\delta_E\left[-\frac13H^2\right]
=-\frac g3H^{\mu\nu\rho}\delta E_{\mu\nu\rho}.
\tag{5.14}
```

The curl terms contribute after one integration by parts.  The complete row
is

```math
\boxed{
\begin{aligned}
0={}&-\frac g3H^{(1)\rho\sigma\lambda}\\
&+\frac1{12}\bar\varepsilon^{\mu\nu\rho\sigma\lambda}
\bar\nabla_\nu\left(
-4E_\mu^{(1)}
-2\sqrt2V_\mu^{(1)}
-4gC_\mu^{(1)}
\right).
\end{aligned}}
\tag{5.15}
```

### 5.3 Coupled fermion equations

For the derivative mixing, integrate by parts first:

```math
\begin{aligned}
&\delta_{ij}\bar\varphi^i\gamma^{\mu\nu}
\bar\nabla_\mu\delta\psi_\nu{}^j\\
&\qquad\doteq
-\delta_{ij}(\bar\nabla_\mu\bar\varphi^i)
\gamma^{\mu\nu}\delta\psi_\nu{}^j.
\end{aligned}
\tag{5.16}
```

Apply the fixed-index rank-two flip (3.16), then restore the NW--SE
ordering using (3.17).  The Majorana-conjugate variation gives the same row,
so its common factor of two cancels against the same factor in the kinetic
and algebraic bilinears.  The gravitino equation is

```math
\boxed{
\begin{aligned}
0={}&-\gamma^{\mu\nu\rho}
\bar\nabla_\nu\psi_{\rho i}^{(1)}\\
&-i\sqrt2\delta_{ij}\gamma^{\mu\nu}
\bar\nabla_\nu\varphi^{(1)j}\\
&-\frac{3ig}{2\sqrt2}\delta_{ij}
\gamma^{\mu\nu}\psi_\nu^{(1)j}
-2g\gamma^\mu\varphi_i^{(1)}.
\end{aligned}}
\tag{5.17}
```

The spinor equation is

```math
\boxed{
\begin{aligned}
0={}&2\not{\bar\nabla}\varphi_i^{(1)}\\
&+i\sqrt2\delta_{ij}\gamma^{\mu\nu}
\bar\nabla_\mu\psi_\nu^{(1)j}\\
&+2g\gamma^\mu\psi_{\mu i}^{(1)}\\
&+\frac{7ig}{\sqrt2}\delta_{ij}
\varphi^{(1)j}.
\end{aligned}}
\tag{5.18}
```

These coupled equations are a later reconstruction check; they are not used
to choose the diagonal coefficients.

## 6. Algebraic and constraint fields

### 6.1 Complete the $`N^{(1)}`$ square

The three terms containing $`N^{(1)}`$ are

```math
-4g^2(L^{(1)})^2
-8gL^{(1)}N^{(1)}
-2(N^{(1)})^2.
\tag{6.1}
```

Add and subtract the required scalar term:

```math
\begin{aligned}
(6.1)
={}&-2\left[
(N^{(1)})^2
+4gL^{(1)}N^{(1)}
+4g^2(L^{(1)})^2
\right]\\
&+4g^2(L^{(1)})^2.
\end{aligned}
\tag{6.2}
```

Thus

```math
\boxed{
(6.1)
=-2\left(N^{(1)}+2gL^{(1)}\right)^2
+4g^2(L^{(1)})^2.}
\tag{6.3}
```

Its equation is exactly

```math
\boxed{N^{(1)}=-2gL^{(1)}.}
\tag{6.4}
```

No derivative acts on $`N^{(1)}`$, so it carries no local mode.

### 6.2 What the (R)-connections do

Equation (5.11) is imposed only after it has been derived.  Since

```math
E^{(1)a}
=-\frac1{12}\bar\varepsilon^{abcde}
\bar\nabla_bE_{cde}^{(1)},
\tag{6.5}
```

it says locally

```math
dE_3^{(1)}=0.
\tag{6.6}
```

In the topologically trivial normalizable sector, $`E_3^{(1)}`$ is pure
gauge.  Equation (5.12) eliminates the traceless connection algebraically.
The divergence is already a Bianchi identity, not an additional equation:
$`\bar\nabla_aE^{(1)a}\equiv0`$, because (6.5) is the Hodge dual of
dE3 and d²E3=0. In components the antisymmetrized two derivatives reduce
to the curvature action on E3, whose contraction vanishes by the first
Bianchi identity. This does not require E3=0.

Taking $`\bar\nabla_\rho`$ of (6.7) makes its curl side identically
zero. For g nonzero, its integrability condition is precisely
$`\bar\nabla_\rho H^{(1)\rho\sigma\lambda}=0`$, the B equation.
Thus it neither supplies another propagating vector nor removes a
physical B polarization. At g=0 this implication cannot be divided by g;
the original B equation must be retained independently.

The trace connection $`V_\mu^{(1)}`$ has no independent quadratic kinetic
term; after Eq. (5.11), Eq. (5.15) determines only its curl:

```math
\boxed{
\begin{aligned}
\frac g3H^{(1)\rho\sigma\lambda}
={}&\frac1{12}\bar\varepsilon^{\mu\nu\rho\sigma\lambda}
\bar\nabla_\nu\\
&\times\left(
-2\sqrt2V_\mu^{(1)}-4gC_\mu^{(1)}
\right).
\end{aligned}}
\tag{6.7}
```

This constraint supplies no extra wave equation and no local degree of
freedom.

## 7. Metric--scalar diagonalization

### 7.1 Find the shift coefficient from the cross term

Use the temporary local combination

```math
\boxed{
H_{\mu\nu}^{(1)}
=h_{\mu\nu}^{(1)}
+\frac23\bar g_{\mu\nu}L^{(1)}.}
\tag{7.1}
```

Equivalently,

```math
h_{\mu\nu}^{(1)}
=H_{\mu\nu}^{(1)}
-\frac23\bar g_{\mu\nu}L^{(1)}.
\tag{7.2}
```

The coefficient is not guessed.  To see how it is fixed, temporarily write

```math
h_{\mu\nu}^{(1)}
=H_{\mu\nu}^{(1)}+c\bar g_{\mu\nu}L^{(1)}.
\tag{7.3}
```

Self-adjointness and Eq. (3.9) give

```math
\begin{aligned}
-\frac12h\mathcal G(h)
\doteq{}&-\frac12H\mathcal G(H)
-cH^{\mu\nu}\mathcal G_{\mu\nu}(\bar gL)\\
&-\frac{c^2}{2}\bar g^{\mu\nu}L
\mathcal G_{\mu\nu}(\bar gL),
\end{aligned}
\tag{7.4}
```

and

```math
H^{\mu\nu}\mathcal G_{\mu\nu}(\bar gL)
\doteq
-\frac32L R^{(1)}(H).
\tag{7.5}
```

The total $`L^{(1)}R^{(1)}(H)`$ coefficient is therefore

```math
1+\frac{3c}{2}.
\tag{7.6}
```

It vanishes only for

```math
1+\frac{3c}{2}=0,
\qquad
c=-\frac23,
\tag{7.7}
```

which is Eq. (7.2).

### 7.2 Expand every scalar term

Substitute Eq. (7.2).  The Einstein square becomes

```math
\begin{aligned}
-\frac12h\mathcal G(h)
={}&-\frac12H\mathcal G(H)
+\frac23H^{\mu\nu}\mathcal G_{\mu\nu}(\bar gL)\\
&-\frac29\bar g^{\mu\nu}L
\mathcal G_{\mu\nu}(\bar gL).
\end{aligned}
\tag{7.8}
```

The cross term is

```math
\frac23H^{\mu\nu}\mathcal G_{\mu\nu}(\bar gL)
\doteq
-L^{(1)}R^{(1)}(H).
\tag{7.9}
```

The original mixing becomes

```math
\begin{aligned}
L^{(1)}R^{(1)}(h)
={}&L^{(1)}R^{(1)}(H)
-\frac23L^{(1)}R^{(1)}(\bar gL)\\
={}&L^{(1)}R^{(1)}(H)
+\frac83L^{(1)}\bar\Box L^{(1)}\\
&+\frac{40}{3}k(L^{(1)})^2.
\end{aligned}
\tag{7.10}
```

The first term in Eq. (7.10) cancels Eq. (7.9).  The pure-trace Einstein
piece is

```math
\begin{aligned}
-\frac29\bar g^{\mu\nu}L^{(1)}
\mathcal G_{\mu\nu}(\bar gL)
={}&\frac13L^{(1)}R^{(1)}(\bar gL)\\
={}&-\frac43L^{(1)}\bar\Box L^{(1)}
-\frac{20}{3}k(L^{(1)})^2.
\end{aligned}
\tag{7.11}
```

After integrating $`L^{(1)}\bar\Box L^{(1)}`$ by parts, the scalar kinetic
coefficient is

```math
\frac43-\frac83+1=-\frac13.
\tag{7.12}
```

The curvature-generated scalar coefficient is

```math
-\frac{20}{3}k+\frac{40}{3}k
=\frac{20}{3}k.
\tag{7.13}
```

Adding the $`+4g^2(L^{(1)})^2`$ remainder of Eq. (6.3),

```math
\frac{20}{3}k+4g^2
=-\frac{10}{3}g^2+4g^2
=\frac23g^2.
\tag{7.14}
```

Thus the complete block is

```math
\boxed{
\begin{aligned}
\bar e^{-1}\mathcal L_{H,L,N}^{(2)}\doteq{}&
-\frac12H^{(1)\mu\nu}
\mathcal G_{\mu\nu}^{(1)}(H)\\
&-\frac13\bar\nabla_\mu L^{(1)}
\bar\nabla^\mu L^{(1)}\\
&+\frac23g^2(L^{(1)})^2\\
&-2\left(N^{(1)}+2gL^{(1)}\right)^2.
\end{aligned}}
\tag{7.15}
```

### 7.3 Equations and the scalar mass

Varying Eq. (7.15) gives

```math
\boxed{\mathcal G_{\mu\nu}^{(1)}(H)=0,}
\tag{7.16}
```

```math
\frac23\bar\Box L^{(1)}
+\frac43g^2L^{(1)}=0.
\tag{7.17}
```

Hence

```math
\boxed{
\left(\bar\Box+2g^2\right)L^{(1)}=0
=\left(\bar\Box+\frac4{\ell^2}\right)L^{(1)}=0.}
\tag{7.18}
```

With $`(\bar\Box-m_0^2)L^{(1)}=0`$,

```math
\boxed{m_L^2=-2g^2,
\qquad
m_L^2\ell^2=-4.}
\tag{7.19}
```

This is the AdS5 Breitenlohner--Freedman bound, not an instability.

## 8. Diffeomorphism gauge and the graviton

### 8.1 The gauge is imposed on the diagonal metric

Choose de Donder gauge on $`H_{\mu\nu}^{(1)}`$:

```math
\boxed{
\bar\nabla^\mu H_{\mu\nu}^{(1)}
-\frac12\bar\nabla_\nu H^{(1)}=0.}
\tag{8.1}
```

Since

```math
H^{(1)}=h^{(1)}+\frac{10}{3}L^{(1)},
\tag{8.2}
```

Eq. (8.1) is, in the original variables,

```math
\boxed{
\bar\nabla^\mu h_{\mu\nu}^{(1)}
-\frac12\bar\nabla_\nu h^{(1)}
=\bar\nabla_\nu L^{(1)}.}
\tag{8.3}
```

It is not de Donder gauge with a zero right-hand side on the original
metric.

Under

```math
\delta H_{\mu\nu}^{(1)}
=2\bar\nabla_{(\mu}\xi_{\nu)},
\tag{8.4}
```

the gauge functional changes by

```math
\delta\left(
\bar\nabla^\mu H_{\mu\nu}
-\frac12\bar\nabla_\nu H
\right)
=\left(\bar\Box+4k\right)\xi_\nu.
\tag{8.5}
```

Thus residual diffeomorphisms satisfy

```math
\left(\bar\Box+4k\right)\xi_\nu=0.
\tag{8.6}
```

### 8.2 Irreducible decomposition

For hand bookkeeping one may decompose locally

```math
\begin{aligned}
H_{\mu\nu}^{(1)}={}&H_{\mu\nu}^{TT}
+2\bar\nabla_{(\mu}X_{\nu)}^T\\
&+\left(
\bar\nabla_\mu\bar\nabla_\nu
-\frac15\bar g_{\mu\nu}\bar\Box
\right)\tau
+\frac15\bar g_{\mu\nu}H^{(1)},
\end{aligned}
\tag{8.7}
```

with

```math
\bar\nabla^\mu H_{\mu\nu}^{TT}=0,
\qquad
\bar g^{\mu\nu}H_{\mu\nu}^{TT}=0,
\qquad
\bar\nabla^\mu X_\mu^T=0.
\tag{8.8}
```

Equation (8.7) is an existence decomposition; no inverse operator is being
defined.  The vector $`X_\mu^T`$, scalar $`\tau`$, and trace are gauge or
constraint pieces.  The trace of Eq. (7.16) gives

```math
R^{(1)}(H)=0.
\tag{8.9}
```

Using Eq. (8.1),

```math
R^{(1)}(H)
=-\frac12\bar\Box H^{(1)}-4kH^{(1)}.
\tag{8.10}
```

The residual scalar diffeomorphism obeys the same local trace equation and
removes the normalizable trace mode.  The remaining metric is transverse and
traceless.

### 8.3 TT equation

For $`H_{\mu\nu}^{TT}`$, commute the derivatives in $`R_{\mu\nu}^{(1)}`$:

```math
\bar\nabla_\rho\bar\nabla_\mu
H_\nu^{TT\,\rho}
=5kH_{\mu\nu}^{TT},
\tag{8.11}
```

and similarly for the term with $`\mu\leftrightarrow\nu`$. Hence

```math
R_{\mu\nu}^{(1)}(H^{TT})
=-\frac12\bar\Box H_{\mu\nu}^{TT}
+5kH_{\mu\nu}^{TT}.
\tag{8.12}
```

Since $`R^{(1)}(H^{TT})=0`$, Eq. (3.6) gives

```math
\mathcal G_{\mu\nu}^{(1)}(H^{TT})
=-\frac12\left(\bar\Box-2k\right)
H_{\mu\nu}^{TT}.
\tag{8.13}
```

Therefore

```math
\boxed{
\left(\bar\Box-2k\right)H_{\mu\nu}^{TT}=0,
\qquad
\bar\nabla^\mu H_{\mu\nu}^{TT}=0,
\qquad
H^{TT}=0.}
\tag{8.14}
```

The (2k) shift is the curvature term of a massless AdS graviton; it is not
a Fierz--Pauli mass.

## 9. Vector and form sectors

### 9.1 Maxwell field

After Eq. (5.11), Eq. (5.8) is

```math
\bar\nabla_\mu G^{(1)\mu\nu}=0.
\tag{9.1}
```

Choose Lorenz gauge

```math
\bar\nabla^\mu C_\mu^{(1)}=0.
\tag{9.2}
```

Then

```math
\begin{aligned}
0&=\bar\nabla_\mu
\left(\bar\nabla^\mu C^{(1)\nu}
-\bar\nabla^\nu C^{(1)\mu}\right)\\
&=\bar\Box C^{(1)\nu}
-\bar R^\nu{}_{\mu}C^{(1)\mu}.
\end{aligned}
\tag{9.3}
```

Thus

```math
\boxed{
\left(\bar\Box-4k\right)C_\mu^T=0,
\qquad
\bar\nabla^\mu C_\mu^T=0.}
\tag{9.4}
```

This is the massless Maxwell equation in AdS5.

### 9.2 Three-form gauge and the physical two-form

The linearized gauge transformations are

```math
\delta E_{\mu\nu\rho}^{(1)}
=3\bar\nabla_{[\mu}\Xi_{\nu\rho]},
\tag{9.5}
```

```math
\delta B_{\mu\nu}^{(1)}
=2\bar\nabla_{[\mu}\Lambda_{\nu]}
-\frac g2\Xi_{\mu\nu}.
\tag{9.6}
```

They leave Eq. (4.3) invariant.  In the local sector selected after
Eq. (6.6), choose

```math
E_{\mu\nu\rho}^{(1)}=0.
\tag{9.7}
```

This is a gauge choice, not an additional field equation for $`B_{\mu\nu}`$.
It gives

```math
H_{\mu\nu\rho}^{(1)}
=3\bar\nabla_{[\mu}B_{\nu\rho]}^{(1)}.
\tag{9.8}
```

Choose the two-form Lorenz gauge

```math
\bar\nabla^\mu B_{\mu\nu}^{(1)}=0.
\tag{9.9}
```

Expanding Eq. (5.10) gives

```math
\begin{aligned}
0={}&\bar\Box B^{(1)\nu\rho}
+\bar\nabla_\mu\bar\nabla^\nu B^{(1)\rho\mu}\\
&+\bar\nabla_\mu\bar\nabla^\rho B^{(1)\mu\nu}.
\end{aligned}
\tag{9.10}
```

The last two terms are commutators because of Eq. (9.9).  On a constant
curvature background their sum is $`-6kB^{\nu\rho}`$. Therefore

```math
\boxed{
\left(\bar\Box-6k\right)B_{\mu\nu}^{T}=0,
\qquad
\bar\nabla^\mu B_{\mu\nu}^{T}=0.}
\tag{9.11}
```

This is the gauge-invariant massless two-form equation.

## 10. Fermionic diagonalization from the raw action

### 10.1 The lower-index shift and its raised form

Use the local combination

```math
\boxed{
\Psi_{\mu i}^{(1)}
=\psi_{\mu i}^{(1)}
+\frac{i\sqrt2}{3}\delta_{ij}
\gamma_\mu\varphi^{(1)j}.}
\tag{10.1}
```

Raise the index step by step:

```math
\begin{aligned}
\Psi_\mu^{(1)i}
&=\varepsilon^{ik}\Psi_{\mu k}^{(1)}\\
&=\psi_\mu^{(1)i}
+\frac{i\sqrt2}{3}
\varepsilon^{ik}\delta_{kj}
\gamma_\mu\varphi^{(1)j}\\
&=\psi_\mu^{(1)i}
-\frac{i\sqrt2}{3}\delta^{ij}
\gamma_\mu\varphi_j^{(1)}.
\end{aligned}
\tag{10.2}
```

Thus

```math
\boxed{
\Psi_\mu^{(1)i}
=\psi_\mu^{(1)i}
-\frac{i\sqrt2}{3}\delta^{ij}
\gamma_\mu\varphi_j^{(1)}.}
\tag{10.3}
```

The upper- and lower-index shifts have opposite signs.  The inverse
relations are

```math
\psi_{\mu i}^{(1)}
=\Psi_{\mu i}^{(1)}
-\frac{i\sqrt2}{3}\delta_{ij}
\gamma_\mu\varphi^{(1)j},
\tag{10.4}
```

```math
\psi_\mu^{(1)i}
=\Psi_\mu^{(1)i}
+\frac{i\sqrt2}{3}\delta^{ij}
\gamma_\mu\varphi_j^{(1)}.
\tag{10.5}
```

### 10.2 Why the coefficient is $`i\sqrt2/3`$

Temporarily replace $`i\sqrt2/3`$ in Eq. (10.1) by a commuting number $`a`$.
Since the source Majorana bar is linear and gamma-one transposes with a
plus sign, barring the upper-index shift gives

```math
\bar\Psi_\mu{}^i
=\bar\psi_\mu{}^i
-a\delta^{ij}\bar\varphi_j\gamma_\mu.
\tag{10.5a}
```

The cross term in which the derivative acts on $`\varphi`$ is

```math
-3a\delta_{ij}\bar\psi_\mu{}^i
\gamma^{\mu\nu}\bar\nabla_\nu\varphi^j.
\tag{10.5b}
```

Integrate it by parts:

```math
\begin{aligned}
(10.5b)
&\doteq
+3a\delta_{ij}
(\bar\nabla_\nu\bar\psi_\mu{}^i)
\gamma^{\mu\nu}\varphi^j\\
&=-3a\delta_{ij}\bar\varphi^j
\gamma^{\mu\nu}\bar\nabla_\nu\psi_\mu{}^i\\
&=+3a\delta_{ij}\bar\varphi^i
\gamma^{\mu\nu}\bar\nabla_\mu\psi_\nu{}^j.
\end{aligned}
\tag{10.5c}
```

The second line uses the fixed-index rank-two flip $`t_2=-1`$. The third
line interchanges $`\mu,\nu`$, uses
$`\gamma^{\nu\mu}=-\gamma^{\mu\nu}`$, and relabels the symmetric
$`\delta_{ij}`$ contraction.

The cross term from the conjugated parenthesis is

```math
+3a\delta^{ij}\bar\varphi_j
\gamma^{\nu\rho}\bar\nabla_\nu\psi_{\rho i}.
\tag{10.5d}
```

Lowering both spinors with Eqs. (3.15a)--(3.15b) leaves a positive
fixed-index delta contraction:

```math
(10.5d)
=+3a\delta_{ij}\bar\varphi^i
\gamma^{\mu\nu}\bar\nabla_\mu\psi_\nu{}^j.
\tag{10.5e}
```

Thus the two terms add. Their sum is

```math
2(3a)\,\delta_{ij}\bar\varphi^i
\gamma^{\mu\nu}\bar\nabla_\mu\psi_\nu{}^j.
\tag{10.6}
```

Matching the raw coefficient $`2i\sqrt2`$ requires

```math
6a=2i\sqrt2,
\qquad
a=\frac{i\sqrt2}{3}.
\tag{10.7}
```

No field equation or AdS representation has entered this step.

### 10.3 Complete the kinetic square

The pure-spinor term in the Rarita--Schwinger square contains

```math
\gamma_\mu\gamma^{\mu\nu\rho}\gamma_\rho
=12\gamma^\nu.
\tag{10.8}
```

Keeping the NW--SE order fixed gives the coefficient

```math
-12a^2
=-12\left(\frac{i\sqrt2}{3}\right)^2
=\frac83.
\tag{10.9}
```

Therefore the exact reverse expansion is

```math
\boxed{
\begin{aligned}
&-\bar\Psi_\mu{}^i\gamma^{\mu\nu\rho}
\bar\nabla_\nu\Psi_{\rho i}\\
&\quad\doteq
-\bar\psi_\mu{}^i\gamma^{\mu\nu\rho}
\bar\nabla_\nu\psi_{\rho i}\\
&\qquad
+2i\sqrt2\delta_{ij}\bar\varphi^i
\gamma^{\mu\nu}\bar\nabla_\mu\psi_\nu{}^j\\
&\qquad
+\frac83\bar\varphi^i
\not{\bar\nabla}\varphi_i.
\end{aligned}}
\tag{10.10}
```

The original spinor kinetic coefficient is (+2), so the diagonal
remainder is fixed by

```math
\frac83+c_{1/2}=2,
\qquad
\boxed{c_{1/2}=-\frac23.}
\tag{10.11}
```

### 10.4 Complete the algebraic gravitino square

Expand the completed gravitino mass square back into the original fields.
The two cross terms add, rather than cancelling. The contracted rank-one
flip and the explicit epsilon give

```math
\begin{aligned}
\varepsilon^{ij}\bar\varphi^j\gamma^\mu\psi_\mu{}^i
&=\bar\varphi^j\gamma^\mu\psi_{\mu j}\\
&=-\bar\psi_\mu{}^j\gamma^\mu\varphi_j.
\end{aligned}
\tag{10.12}
```

Each cross term consequently has coefficient -4a. Therefore

```math
\begin{aligned}
\delta_{ij}\bar\Psi_\mu^i\gamma^{\mu\nu}\Psi_\nu^j
={}&\delta_{ij}\bar\psi_\mu^i\gamma^{\mu\nu}\psi_\nu^j\\
&-8a\bar\psi_\mu^i\gamma^\mu\varphi_i
+20a^2\delta_{ij}\bar\varphi^i\varphi^j.
\end{aligned}
\tag{10.13}
```

The pure-spinor term uses

```math
\gamma_\mu\gamma^{\mu\nu}\gamma_\nu=20.
\tag{10.14}
```

Its coefficient is

```math
\left(-\frac{3ig}{2\sqrt2}\right)\left(20a^2\right)
=\left(-\frac{3ig}{2\sqrt2}\right)\left(-\frac{40}{9}\right)
=\frac{20ig}{3\sqrt2}.
\tag{10.15}
```

The same mass square reproduces the raw mixed coefficient:

```math
\left(-\frac{3ig}{2\sqrt2}\right)(-8a)=-4g.
\tag{10.15a}
```

The raw algebraic spinor coefficient was $`7ig/\sqrt2`$. Therefore the
diagonal remainder is not inferred from a desired mass; it is the difference

```math
\frac{7ig}{\sqrt2}
-\frac{20ig}{3\sqrt2}
=\boxed{\frac{ig}{3\sqrt2}}.
\tag{10.16}
```

The full reconstruction is

```math
\frac{20}{3}+\frac13=7.
\tag{10.17}
```

### 10.5 Diagonal fermionic action

Combining Eqs. (10.10)--(10.17) gives

```math
\boxed{
\begin{aligned}
\bar e^{-1}\mathcal L_{F,\mathrm{diag}}^{(2)}\doteq{}&
-\bar\Psi_\mu^{(1)i}\gamma^{\mu\nu\rho}
\bar\nabla_\nu\Psi_{\rho i}^{(1)}\\
&-\frac{3ig}{2\sqrt2}\delta_{ij}
\bar\Psi_\mu^{(1)i}\gamma^{\mu\nu}
\Psi_\nu^{(1)j}\\
&-\frac23\bar\varphi^{(1)i}
\not{\bar\nabla}\varphi_i^{(1)}\\
&+\frac{ig}{3\sqrt2}\delta_{ij}
\bar\varphi^{(1)i}\varphi^{(1)j}.
\end{aligned}}
\tag{10.18}
```

This is a forward square completion of Eq. (4.1).  In particular, the
coefficient $`+ig/(3\sqrt2)`$ has not been solved backward from
$`SU(2,2|1)`$.

## 11. Charge branches and fermionic equations

### 11.1 Charge convention

Resolve the real symplectic-Majorana doublet into conjugate complex charge
branches by

```math
\boxed{
i\delta_{ij}X^{(q)j}
=-qX_i^{(q)},
\qquad
q=\pm1.}
\tag{11.1}
```

This sign convention makes the background Killing equation agree directly
with the Coomans--Özkan transformation orientation.  Choosing the opposite
definition only relabels $`q\leftrightarrow-q`$. The two branches are the
complex description of one symplectic-Majorana field and are not counted
twice.

### 11.2 Spin one-half equation

Varying the last two lines of Eq. (10.18) gives

```math
-\frac23\not{\bar\nabla}\varphi_i^{(q)}
-\frac{qg}{3\sqrt2}\varphi_i^{(q)}=0.
\tag{11.2}
```

Multiplication by (-3/2) gives

```math
\boxed{
\left(
\not{\bar\nabla}+\frac q{2\ell}
\right)\varphi_i^{(q)}=0.}
\tag{11.3}
```

Therefore

```math
\boxed{|m_{1/2}\ell|=\frac12.}
\tag{11.4}
```

### 11.3 Rarita--Schwinger equation and its gauge symmetry

The gravitino equation is

```math
\boxed{
\gamma^{\mu\nu\rho}\bar\nabla_\nu
\Psi_{\rho i}^{(q)}
-\frac{3q}{2\ell}\gamma^{\mu\nu}
\Psi_{\nu i}^{(q)}=0.}
\tag{11.5}
```

The coefficient is the massless AdS5 Rarita--Schwinger value.  Indeed,
Eq. (11.5) is invariant under

```math
\boxed{
\delta\Psi_{\mu i}^{(q)}
=\left(
\bar\nabla_\mu+\frac q{2\ell}\gamma_\mu
\right)\epsilon_i^{(q)}.}
\tag{11.6}
```

The derivative terms cancel because

```math
3\left(+\frac q{2\ell}\right)
-\frac{3q}{2\ell}=0.
\tag{11.7}
```

The remaining algebraic terms cancel by

```math
[\bar\nabla_\mu,\bar\nabla_\nu]\epsilon
=-\frac1{2\ell^2}\gamma_{\mu\nu}\epsilon,
\tag{11.8}
```

together with

```math
\gamma^{\mu\nu\rho}\gamma_{\nu\rho}
=-12\gamma^\mu,
\qquad
\gamma^{\mu\nu}\gamma_\nu=4\gamma^\mu.
\tag{11.8a}
```

Indeed, the curvature contribution is

```math
\begin{aligned}
\gamma^{\mu\nu\rho}\bar\nabla_\nu
\bar\nabla_\rho\epsilon
&=\frac12\gamma^{\mu\nu\rho}
[\bar\nabla_\nu,\bar\nabla_\rho]\epsilon\\
&=-\frac1{4\ell^2}
\gamma^{\mu\nu\rho}\gamma_{\nu\rho}\epsilon\\
&=+\frac3{\ell^2}\gamma^\mu\epsilon.
\end{aligned}
\tag{11.8b}
```

The product of the algebraic Rarita--Schwinger term with the gamma part of
Eq. (11.6) is

```math
\begin{aligned}
-\frac{3q}{2\ell}\gamma^{\mu\nu}
\left(+\frac q{2\ell}\gamma_\nu\epsilon\right)
&=-\frac{3}{4\ell^2}
\gamma^{\mu\nu}\gamma_\nu\epsilon\\
&=-\frac3{\ell^2}\gamma^\mu\epsilon.
\end{aligned}
\tag{11.8c}
```

Equations (11.8b) and (11.8c) cancel exactly.  Equation (11.6) also shows that the
background Killing spinors obey

```math
\boxed{
\bar\nabla_\mu\epsilon_i^{(q)}
=-\frac q{2\ell}\gamma_\mu\epsilon_i^{(q)}.}
\tag{11.9}
```

Its integrability condition is

```math
[\bar\nabla_\mu,\bar\nabla_\nu]\epsilon_i^{(q)}
=-\frac1{2\ell^2}\gamma_{\mu\nu}
\epsilon_i^{(q)},
\tag{11.10}
```

which is precisely Eq. (3.1) with $`k=-1/\ell^2`$.  There is no projector,
so all eight real supercharges are preserved.

### 11.4 Gamma-trace gauge and constraints

Use local supersymmetry to impose

```math
\boxed{\gamma^\mu\Psi_{\mu i}^{(q)}=0.}
\tag{11.11}
```

In the original fields this is

```math
\boxed{
\gamma^\mu\psi_{\mu i}^{(q)}
+\frac{5i\sqrt2}{3}\delta_{ij}
\varphi^{(q)j}=0.}
\tag{11.12}
```

It is not the condition $`\gamma\mathbin{\cdot}\psi=0`$ on the unshifted
gravitino.  The residual supersymmetry parameter satisfies

```math
\boxed{
\left(
\not{\bar\nabla}+\frac{5q}{2\ell}
\right)\epsilon_i^{(q)}=0.}
\tag{11.13}
```

Gamma-tracing Eq. (11.5) gives

```math
3\gamma^{\mu\nu}\bar\nabla_\mu\Psi_{\nu i}^{(q)}
-\frac{6q}{\ell}\gamma^\nu\Psi_{\nu i}^{(q)}=0.
\tag{11.14}
```

Using Eq. (11.11),

```math
\gamma^{\mu\nu}\bar\nabla_\mu\Psi_{\nu i}^{(q)}=0.
\tag{11.15}
```

But

```math
0=\not{\bar\nabla}
(\gamma^\nu\Psi_{\nu i})
=\gamma^{\mu\nu}\bar\nabla_\mu\Psi_{\nu i}
+\bar\nabla^\nu\Psi_{\nu i},
\tag{11.16}
```

so

```math
\boxed{\bar\nabla^\mu\Psi_{\mu i}^{(q)}=0.}
\tag{11.17}
```

Under Eqs. (11.11) and (11.17), Eq. (11.5) reduces to

```math
\boxed{
\left(
\not{\bar\nabla}+\frac{3q}{2\ell}
\right)\Psi_{\mu i}^{(q)}=0.}
\tag{11.18}
```

Thus

```math
\boxed{|m_{3/2}\ell|=\frac32,}
\tag{11.19}
```

with the gamma-trace and divergence constraints.  This is a massless gauge
gravitino, not a member of a long massive spin-(3/2) representation.

## 12. Complete diagonal action

Before using algebraic or constraint equations, the diagonal action is

```math
\boxed{
\begin{aligned}
\bar e^{-1}\mathcal L_{\mathrm{diag}}^{(2)}\doteq{}&
-\frac12H^{(1)\mu\nu}
\mathcal G_{\mu\nu}^{(1)}(H)\\
&-\frac13(\bar\nabla L^{(1)})^2
+\frac23g^2(L^{(1)})^2\\
&-2\left(N^{(1)}+2gL^{(1)}\right)^2\\
&-\frac12G_{\mu\nu}^{(1)}G^{(1)\mu\nu}
-\frac13H_{\mu\nu\rho}^{(1)}H^{(1)\mu\nu\rho}\\
&-2E_a^{(1)}E^{(1)a}
-2\sqrt2E^{(1)a}V_a^{(1)}
-4gE^{(1)a}C_a^{(1)}\\
&+2V_a^{\prime(1)ij}V^{\prime(1)a}_{ij}\\
&-\bar\Psi_\mu^{(1)i}\gamma^{\mu\nu\rho}
\bar\nabla_\nu\Psi_{\rho i}^{(1)}\\
&-\frac{3ig}{2\sqrt2}\delta_{ij}
\bar\Psi_\mu^{(1)i}\gamma^{\mu\nu}
\Psi_\nu^{(1)j}\\
&-\frac23\bar\varphi^{(1)i}
\not{\bar\nabla}\varphi_i^{(1)}\\
&+\frac{ig}{3\sqrt2}\delta_{ij}
\bar\varphi^{(1)i}\varphi^{(1)j}.
\end{aligned}}
\tag{12.1}
```

After using only

```math
N^{(1)}=-2gL^{(1)},
\qquad
E_a^{(1)}=0,
\qquad
V_a^{\prime(1)ij}=0,
\tag{12.2}
```

and the local gauge $`E_3^{(1)}=0`$, the propagating representative is

```math
\boxed{
\begin{aligned}
\bar e^{-1}\mathcal L_{\mathrm{prop}}^{(2)}\doteq{}&
-\frac12H^{TT\,\mu\nu}
\mathcal G_{\mu\nu}^{(1)}(H^{TT})\\
&-\frac13\bar\nabla_\mu L^{(1)}
\bar\nabla^\mu L^{(1)}
+\frac23g^2(L^{(1)})^2\\
&-\frac12G_{\mu\nu}^{(1)}G^{(1)\mu\nu}\\
&-\frac13
\left(3\bar\nabla_{[\mu}B_{\nu\rho]}^{(1)}\right)
\left(3\bar\nabla^{[\mu}B^{(1)\nu\rho]}\right)\\
&-\bar\Psi_\mu^{(1)i}\gamma^{\mu\nu\rho}
\bar\nabla_\nu\Psi_{\rho i}^{(1)}\\
&-\frac{3ig}{2\sqrt2}\delta_{ij}
\bar\Psi_\mu^{(1)i}\gamma^{\mu\nu}
\Psi_\nu^{(1)j}\\
&-\frac23\bar\varphi^{(1)i}
\not{\bar\nabla}\varphi_i^{(1)}\\
&+\frac{ig}{3\sqrt2}\delta_{ij}
\bar\varphi^{(1)i}\varphi^{(1)j}.
\end{aligned}}
\tag{12.3}
```

The gauge conditions associated with Eq. (12.3) are Eqs. (8.1), (9.2),
(9.9), and (11.11), together with their residual equations.

## 13. Independent reconstruction checks

### 13.1 Scalar equation without the metric shift

Trace Eq. (5.3) and use Eq. (3.9):

```math
\frac32R^{(1)}(h)
-4\bar\Box L^{(1)}
-20kL^{(1)}=0.
\tag{13.1}
```

Use $`N^{(1)}=-2gL^{(1)}`$ in Eq. (5.5):

```math
R^{(1)}(h)
-2\bar\Box L^{(1)}
+8g^2L^{(1)}=0.
\tag{13.2}
```

Eliminating $`R^{(1)}(h)`$ and using $`k=-g^2/2`$ gives

```math
\left(\bar\Box+2g^2\right)L^{(1)}=0,
\tag{13.3}
```

in agreement with Eq. (7.18).

### 13.2 Reconstruct the raw fermionic action

Equations (10.10) and (10.15) show separately that the completed gravitino
square contributes

```math
\frac83\bar\varphi\not{\bar\nabla}\varphi
+\frac{20ig}{3\sqrt2}\delta_{ij}
\bar\varphi^i\varphi^j.
\tag{13.4}
```

Adding the diagonal spinor terms gives

```math
\frac83-\frac23=2,
\tag{13.5}
```

```math
\frac{20}{3}+\frac13=7.
\tag{13.6}
```

The derivative mixing is $`2i\sqrt2`$ by Eq. (10.7), and the algebraic
gravitino--spinor cross term is -4g by Eq. (10.15a). Therefore Eq. (10.18)
reconstructs all six fermionic structures in Eq. (4.1).

### 13.3 Reconstruct the coupled fermion equations

The change of variables (10.1)--(10.5) is local and invertible.  Varying the
diagonal action and applying the chain rule gives one row from
$`\delta\bar\Psi/\delta\bar\psi`$ and a second row from
$`\delta\bar\Psi/\delta\bar\varphi`$. Expanding the first row gives
Eq. (5.17).  In the second row the two required coefficient sums are exactly
Eqs. (13.5)--(13.6), giving Eq. (5.18).  No diagonal equation is substituted
into the other.

## 14. AdS energies derived from the action masses

### 14.1 Bosons

To derive the indicial equations, use a Poincaré patch
$`ds^2=\ell^2z^{-2}(dz^2+\eta_{mn}dx^m dx^n)`$.
For the scalar radial power $`L^{(1)}\sim z^r`$,

```math
\begin{aligned}
\ell^2\bar\Box L^{(1)}
&=z^2\partial_z^2L^{(1)}-3z\partial_zL^{(1)}
+z^2\partial_m\partial^m L^{(1)},\\
(\bar\Box-m_0^2)L^{(1)}=0
&\quad\Longrightarrow\quad r(r-4)=m_0^2\ell^2.
\end{aligned}
\tag{14.0a}
```

For a tangential transverse p-form in radial gauge, its radial equation is

```math
\begin{aligned}
z^2\partial_z^2 A_{m_1\cdots m_p}
+(2p-3)z\partial_z A_{m_1\cdots m_p}
-m_p^2\ell^2 A_{m_1\cdots m_p}&=0,\\
r(r+2p-4)&=m_p^2\ell^2.
\end{aligned}
\tag{14.0b}
```

Here A denotes only the generic component for this indicial argument:
p=1 means the already defined C; p=2 means B. No additional bulk field
is introduced. The response exponent is r=Delta−p, giving (14.5).
For the graviton the fractional tangential metric perturbation
$`z^2H_{mn}/\ell^2`$ obeys the massless scalar radial equation, with
response exponent four. This gives (14.4), independently of multiplets.

For a scalar in AdS5,

```math
m_0^2\ell^2=\Delta(\Delta-4).
\tag{14.1}
```

Equation (7.19) gives

```math
\Delta(\Delta-4)=-4,
\qquad
(\Delta-2)^2=0,
\tag{14.2}
```

so

```math
\boxed{\Delta_L=2.}
\tag{14.3}
```

The massless graviton and Maxwell systems give

```math
\boxed{\Delta_H=4,
\qquad
\Delta_C=3.}
\tag{14.4}
```

For a (p)-form potential in AdS5,

```math
m_p^2\ell^2
=(\Delta-p)(\Delta+p-4).
\tag{14.5}
```

For the massless two-form, $`p=2`$, so

```math
(\Delta_B-2)^2=0,
\qquad
\boxed{\Delta_B=2}
\tag{14.6}
```

in the un-dualized potential description.  Its locally dual Maxwell frame
has the standard current dimension (3); the difference records the choice
of electric or magnetic AdS boundary data, not a different local bulk mode.

### 14.2 Fermions

In the same frame, the spinor radial equation is

```math
\left[\gamma^{\hat z}(z\partial_z-2)
+z\gamma^{\hat m}\partial_m-m\ell\right]\varphi=0.
\tag{14.6a}
```

Resolving the two radial gamma eigenvalues gives powers
$`r=2\pm m\ell`$. The standard response branch therefore has
$`\Delta=2+|m\ell|`$. For the transverse gamma-traceless gravitino,
use tangent components and radial gauge; the extra vector-connection term
is proportional to the radial component or the gamma trace and vanishes.
The leading radial equation has the same spinor form, now with the mass
read from (11.18). This supplies the missing argument for (14.9), not
merely a representation-theory assertion.

For a Dirac-type spinor equation in AdS5,

```math
\Delta_{1/2}=2+|m_{1/2}\ell|.
\tag{14.7}
```

Equation (11.4) gives

```math
\boxed{\Delta_\varphi=\frac52.}
\tag{14.8}
```

The massless Rarita--Schwinger gauge system, not the algebraic term by itself,
gives

```math
\boxed{\Delta_\Psi=\frac72.}
\tag{14.9}
```

Thus every energy in Eqs. (14.3)--(14.9) follows from a diagonal action
equation before any representation label is applied.

## 15. Degrees of freedom

The five-dimensional massless little-group counts are

```math
\begin{array}{c|c|c}
\text{field} & \text{calculation} & \text{real local DoF}\\ \hline
H_{\mu\nu}^{TT} & \frac{5(5-3)}2 & 5\\
L^{(1)} & 1 & 1\\
C_\mu^T & 5-2 & 3\\
B_{\mu\nu}^T & \binom{5-2}{2} & 3
\end{array}
\tag{15.1}
```

and

```math
\begin{array}{c|c}
\text{field} & \text{real local DoF}\\ \hline
\Psi_{\mu i} & 8\\
\varphi_i & 4
\end{array}.
\tag{15.2}
```

Therefore

```math
\boxed{
5+1+3+3=12,
\qquad
8+4=12.}
\tag{15.3}
```

The fields $`N^{(1)}`$, $`E_3^{(1)}`$, $`V_\mu^{(1)}`$, and
$`V_\mu^{\prime(1)ij}`$ add no local modes for the reasons displayed in
Section 6.

## 16. Multiplet structure: representation as an output check

The fluxless vacuum preserves eight real supercharges by Eq. (11.10), so its
superisometry algebra is $`SU(2,2|1)`$, equivalently the $`4d\;\mathcal N=1`$
superconformal algebra.

### 16.1 Which vector belongs to which multiplet

The action contains two locally massless three-degree-of-freedom gauge
sectors: $`C_\mu`$ and the field locally dual to $`B_{\mu\nu}`$.  Degree
counting alone cannot decide which combination is the graviphoton.

Coomans--Özkan Eq. (5.17) gives the local on-shell dualization of $`H_3`$.
Writing the dual vector strength as

```math
\widetilde G_{\mu\nu}
=2\partial_{[\mu}\widetilde C_{\nu]},
\tag{16.1}
```

the source transformations in their Eq. (5.30), at unit compensator, contain

```math
G_{\mu\nu}+\partial_{[\mu}\widetilde C_{\nu]}
=G_{\mu\nu}+\frac12\widetilde G_{\mu\nu}
\tag{16.2}
```

in the gravitino transformation, and

```math
G_{\mu\nu}-2\partial_{[\mu}\widetilde C_{\nu]}
=G_{\mu\nu}-\widetilde G_{\mu\nu}
\tag{16.3}
```

in the matter-spinor transformation.  The change of basis is invertible:

```math
\det
\begin{pmatrix}
1&\frac12\\
1&-1
\end{pmatrix}
=-\frac32\ne0.
\tag{16.4}
```

Thus one vector combination belongs to the gravity multiplet and the other
to the matter current multiplet.  Equations (16.1)--(16.4) are used only for
the final on-shell multiplet assignment; the diagonal bulk action (12.3)
remains in the original un-dualized variables.

### 16.2 Gravity or stress-tensor multiplet

The action-derived energies organize as

```math
\begin{array}{c|c|c|c}
\text{bulk field / boundary operator} & \Delta
& (j_L,j_R) & r\\ \hline
\text{gravity vector / }R\text{-current} & 3
& (\frac12,\frac12) & 0\\
\Psi_{\mu\alpha}\text{ / supercurrent} & \frac72
& (1,\frac12) & -1\\
\bar\Psi_{\mu\dot\alpha}\text{ / conjugate supercurrent} & \frac72
& (\frac12,1) & +1\\
H_{\mu\nu}^{TT}\text{ / stress tensor} & 4
& (1,1) & 0
\end{array}.
\tag{16.5}
```

This is

```math
\boxed{
A_1\bar A_1[1;1]_{3}^{(0)},
\qquad
(n_B,n_F)=(8,8).}
\tag{16.6}
```

The primary is the dimension-three (R)-current.  Its supercurrent and
stress-tensor descendants have exactly the energies found from the diagonal
Maxwell, Rarita--Schwinger, and graviton equations.

### 16.3 Matter or flavor-current multiplet

With the standard supersymmetric boundary condition and the dual-current
frame for the two-form sector, the remaining fields give

```math
\begin{array}{c|c|c|c}
\text{bulk field / boundary operator} & \Delta
& (j_L,j_R) & r\\ \hline
L^{(1)} & 2 & (0,0) & 0\\
\varphi_\alpha & \frac52 & (\frac12,0) & -1\\
\bar\varphi_{\dot\alpha} & \frac52 & (0,\frac12) & +1\\
\text{dual matter vector / flavor current} & 3
& (\frac12,\frac12) & 0
\end{array}.
\tag{16.7}
```

This is

```math
\boxed{
A_2\bar A_2[0;0]_{2}^{(0)},
\qquad
(n_B,n_F)=(4,4).}
\tag{16.8}
```

Córdova--Dumitrescu--Intriligator Eq. (5.89), with $`j=\bar j=0`$,
identifies this $`A_2\bar A_2`$ representation as the $`4+4`$ flavor-current
multiplet.  The representation predicts

```math
\Delta=2,
\qquad
\Delta+\frac12=\frac52,
\qquad
\Delta+1=3,
\tag{16.9}
```

which agrees with Eqs. (14.3), (14.8), and the dual Maxwell equation.

### 16.4 Meaning of “massless multiplet”

Both multiplets are massless in the AdS shortening sense.  This does not
mean that every covariant wave equation has zero algebraic curvature term.
In particular,

```math
m_L^2\ell^2=-4,
\qquad
|m_{1/2}\ell|=\frac12,
\qquad
|m_{3/2}\ell|=\frac32.
\tag{16.10}
```

These are precisely the shortened AdS values.  The vector, two-form,
graviton, and gravitino still possess their gauge symmetries.

## 17. Final spectrum table

```math
\begin{array}{c|c|c|c|c}
\text{mode} & \text{physical equation}
& \text{mass datum} & \Delta & \text{DoF}\\ \hline
H_{\mu\nu}^{TT}
& (\bar\Box-2k)H_{\mu\nu}^{TT}=0
& m_2^2=0 & 4 & 5\\
L^{(1)}
& (\bar\Box+4/\ell^2)L^{(1)}=0
& m_0^2\ell^2=-4 & 2 & 1\\
C_\mu^T
& (\bar\Box-4k)C_\mu^T=0
& m_1^2=0 & 3 & 3\\
B_{\mu\nu}^T
& (\bar\Box-6k)B_{\mu\nu}^T=0
& m_2^2=0 & 2\text{ or dual }3 & 3\\
\Psi_{\mu i}^{(q)}
& (\not{\bar\nabla}+3q/(2\ell))\Psi_\mu^{(q)}=0
& |m_{3/2}\ell|=3/2 & 7/2 & 8\\
\varphi_i^{(q)}
& (\not{\bar\nabla}+q/(2\ell))\varphi^{(q)}=0
& |m_{1/2}\ell|=1/2 & 5/2 & 4
\end{array}
\tag{17.1}
```

The complete local spectrum is therefore

```math
\boxed{
\mathcal H_{\rm local}
=A_1\bar A_1[1;1]_{3}^{(0)}
\oplus
A_2\bar A_2[0;0]_{2}^{(0)},}
\tag{17.2}
```

```math
\boxed{12\ \text{bosonic}+12\ \text{fermionic local DoF}.}
\tag{17.3}
```

There is no additional pole from $`N`$, $`E_3`$, $`V_\mu`$, or $`V'_\mu`$,
and no higher-derivative massive multiplet is present in this two-derivative
Hessian.

## 18. Norm, limits, and scope

The bosonic kinetic signs are the standard signs relative to the positive
Einstein term of the nonlinear parent. The diagonal fermionic kinetic
coefficients are -1 and -2/3 in the source Majorana convention. Their
displayed signs alone do not establish positive physical norms.
This document establishes
the pole equations and the local gauge count; it does not replace a full
holographically renormalized symplectic-norm or boundary two-point-function
calculation.

The AdS calculation assumes $`g\ne0`$. The limit $`g\to0`$ sends
$`\ell\to\infty`$ and smoothly removes all algebraic AdS fermion terms and
the scalar curvature mass.  Equation (6.7) should not be divided by (g)
before taking that limit; the zero-(g) constraint branch must be read from
Eq. (5.15) itself.

At the scalar BF bound, a logarithmic asymptotic solution exists.  The
irreducible unitary current multiplet in Eq. (16.8) uses the standard
supersymmetric boundary condition that excludes the logarithmic partner.

## 20. Final statement

Starting forward from Eq. (4.1), the unique local diagonalizations are

```math
H_{\mu\nu}^{(1)}
=h_{\mu\nu}^{(1)}
+\frac23\bar g_{\mu\nu}L^{(1)},
\tag{20.1}
```

```math
\Psi_{\mu i}^{(1)}
=\psi_{\mu i}^{(1)}
+\frac{i\sqrt2}{3}\delta_{ij}
\gamma_\mu\varphi^{(1)j},
\tag{20.2}
```

with the raised gravitino combination carrying the opposite sign shown in
Eq. (10.3).  They lead to the diagonal action (12.1), the physical equations
in (17.1), and the short massless multiplets (17.2).  The action and the
representation theory independently give the same scalar, spinor,
Rarita--Schwinger, vector, and graviton values.
