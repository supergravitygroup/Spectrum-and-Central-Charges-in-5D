# Generic-level polynomials and multiplets

Write nu = nu_f and m = mu ell_s. All expressions below use chi=+1;
chi=-1 acts by D to 2-D. The [independent check targets](../../../computations/gb_ads3_sigma2/closed_forms.py)
contain every coefficient of paper Appendix C (`app:quintic`), including Y, X,
Pi4, Pi3, Pi2 and Pi21, as exact integer polynomials in L,k. The physical
divisors are derived from the action matrices before being compared with
these targets.

```math
\begin{aligned}
Y={}&128-224k+16k^2-80kL+120k^2L+24k^2L^2\\
&-20k^3L^2-6k^3L^3+k^4L^4,\\
m&=\frac{Y}{kP_3P_4},&
\nu&=\frac{16+4k-10kL+k^2L^2}{kP_3},\\
C(D)&=D(D-2)(D-1-m)-M^2(D-1-\nu),\\
\widehat K_2(D)&=-\frac{LkP_3^3}{32P_2^3}\,C(D),&
\widehat K_{Z,+}(D)&=\frac{LkP_3}{2P_2}(D-\nu).
\end{aligned}
```

The quintic, including its constant-level factorization, is

```math
\begin{aligned}
F(D,M^2)&=D^5+f_4D^4+f_3D^3+f_2D^2+f_1D
 +M^2B(D)+M^4\frac{P_4P_5}{P_1^2P_2^2}(D-\nu+1),\\
f_4&=\frac{\Pi_4}{kP_1P_3P_4},&
f_3&=\frac{\Pi_3}{kP_1P_3^2P_4},\\
f_2&=\frac{2P_2\Pi_2}{kP_1P_3^3P_4},&
f_1&=\frac{16L^2(3k-2)P_2^3P_5}{kP_1P_3^3P_4},\\
B(D)&=b_3D^3+b_2D^2+b_1D+b_0,&
b_3&=-1-\frac{P_4P_5}{P_1^2P_2^2},\\
b_2&=\frac{4\Pi_{21}}{kP_1^2P_3},&
b_1&=-\frac{8L(8-8k-4kL+3k^2L)P_5}{kP_1^2P_3^2},\\
b_0&=\frac{16LP_2P_5(2L-8+3kL-kL^2)}{kP_1P_3^3},\\
F(D,0)&=D(D-2)R(D),\\
R(D)&=D^3+(f_4+2)D^2+(f_3+2f_4+4)D+f_2+2f_3+4f_4+8.
\end{aligned}
```

The exact maximal-minor reductions give

```math
\begin{aligned}
\mathscr P_2(D)&=C(D),\\
\mathscr P_1(D)&=C(D+1)F(D-1,M^2)(D-\nu)^2,\\
\mathscr P_0(D)&=F(D,M^2)F(2-D,M^2),\\
\mathscr P_{Z,+}(D)&=D-\nu,&
\mathscr P_{Z,-}(D)&=D-2+\nu,&\mathscr P_{Z,0}&=1.
\end{aligned}
```

Equalities of physical divisors are up to nonzero D-independent units.
The full matrices and propagators retain those units. The paired scalar
roots describe five states, not ten independent scalar states.

For a simple real root, (s,Delta)=(n,D) if D>1 and (-n,2-D) if D<1.
A cubic root has its vector partner at D-1. A quintic root has its vector
partner at D+1. Each of the two neutral roots at nu pairs with a charged
mode. These give the ten long multiplets of paper Table 9 (`tab:generic`).
When partners cross Re D=1, the polynomial pairing persists but a multiplet
interpretation requires an alternative boundary quantization; a bulk
residue test does not select that boundary domain.

Multiplying C and F by k before taking k to zero gives degree two and four,
respectively. The flat equation becomes a nonzero constant: both flat
multiplets decouple. Thus the finite two-derivative spectrum contains two
spin-2 and four (1,0) long multiplets. This is a separate degree limit, not
substitution into a singular monic polynomial.

## Separate-invariant checks in the same paper paragraph

The paragraph after equation (4.9) (`eq:Kform`) also reports two numerical bosonic
comparisons for each of LR+cW, LR+cLOG and LR+cR². The
[bounded calculation](../../../computations/gb_ads3_sigma2/product_checks.py)
constructs each invariant on its own stationary BPS H² background.
The six records are
[W_a](../../../computations/gb_ads3_sigma2/outputs/product_checks/W_a.json),
[W_b](../../../computations/gb_ads3_sigma2/outputs/product_checks/W_b.json),
[LOG_a](../../../computations/gb_ads3_sigma2/outputs/product_checks/LOG_a.json),
[LOG_b](../../../computations/gb_ads3_sigma2/outputs/product_checks/LOG_b.json),
[R2_a](../../../computations/gb_ads3_sigma2/outputs/product_checks/R2_a.json), and
[R2_b](../../../computations/gb_ads3_sigma2/outputs/product_checks/R2_b.json).
Units are g=1, and c is the dimensionless coefficient of the indicated
single invariant; these are finite numerical samples, not assumptions in
the symbolic GB derivation.

| Point | L | c | S | Harmonic interpretation |
|---|---:|---:|---|---|
| a | 1 | 1/10 | 3 | Algebraic continuation on H²; not a principal-series state |
| b | 5/4 | -1/10 | 1/2+13i/10 | H² principal series |

At both points W and LOG have root counts (4,18,28,2,4,2), and R² has
(2,8,16,0,2,0), in sector order (n=2,1,0; Z at n=1,0,-1).
After including the neutral negative-spin sectors and the conjugate
charged field, there are respectively 88 and 40 **raw roots**, including
shadow representatives. Their complete matchings contain respectively
28+16 and 16+4 boson-primary plus fermion-primary raw pairs. These counts
do not count the two shadows as separate physical states.

The matching preserves spin and R-charge: equal-charge bosons differ by
(n,D)→(n+1,D+1), while a fermion-primary pair has equal (n,D) and R-charges
differing by two supercharge units. The computation seeks a complete
one-to-one matching, and fails for any unpaired or reused root. These six
comparisons test the flux-dependent terms stated in the paper. They are
not a symbolic all-coupling spectrum or a global boundary-unitarity claim.
