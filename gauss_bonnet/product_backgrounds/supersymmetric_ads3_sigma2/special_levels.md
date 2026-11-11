# Restricted harmonics and the constant level

The [harmonic restriction](../../../computations/gb_ads3_sigma2/harmonics.py)
first writes h33=t+u, h44=t-u. It then restricts the quadratic action to the
actual harmonic types, before taking ranks or determinants.

| Level | Restriction and verified physical content |
|---|---|
| S², j=1 | S=-1; traceless tensor harmonics u,h34 are absent. Neutral ranks are 1,7,12; scalar divisor is F(D)F(2-D)/[D(2-D)] at M²=2v ell². The n=1 divisor retains D=1, the SU(2) current. Nine long multiplets remain. |
| H²/Gamma harmonic one-form | S=1; retain surface vector/tensor types in the field-strength representation. Discarded equations vanish exactly. Vector divisor is (D-3)²(D+1)²(D-nu)²; scalar divisor is D⁴(D-2)⁴. |
| H²/Gamma quadratic differential | S=2; retain only traceless surface tensors. Discarded equations vanish exactly. The rank-two matrix has divisor D²(D-2)². |
| Constant T² | Set r=0,w=0 in the field-strength action, then k=2(L-4)/[L(L-3)]. Use the torus amplitude basis; ell=sqrt(2)/(3g). |

The charged vector factors remain those of the [generic level](generic_levels.md).
Charged harmonic global multiplicities require bundle data. Per holomorphic
one-form the neutral light states are the two vector helicities with Delta=3
and four Wilson-line moduli with Delta=2, in addition to the two flat modes.
Each holomorphic quadratic differential supplies a complex structure modulus.

The constant-torus divisors, independently obtained from its matrices, are

```math
\begin{aligned}
\mathscr P_2&=D(D-2)(D-1-m),\\
\mathscr P_1&=(D-3)^2(D-1)^2(D+1)^2(D-m)(D-\nu)^2R(D-1),\\
\mathscr P_0&=D^4(D-2)^4R(D)R(2-D),\\
\mathscr P_{Z,+}&=D-\nu,&\mathscr P_{Z,-}&=D-2+\nu,&\mathscr P_{Z,0}&=1.
\end{aligned}
```

Here m,nu,R are restricted to the torus curve. The full constant-level
matrices, including the light modes and currents, are in the
[output directory](../../../computations/gb_ads3_sigma2/outputs).

## Independent constant-scalar reduction

For S² and H²/Gamma, a charged constant mode is absent in the R flux.
The constant neutral reduction is performed at fixed magnetic flux, using
the four scalar fields (psi,L,H,N). The area scales as exp(2psi), while
P=p0 exp(-2psi), rho=r0 exp(-2psi), v=v0 exp(-2psi).

```math
\begin{aligned}
\mathcal L_3&=\kappa(\Phi)R_3+K_{ij}(\Phi)\partial\Phi^i\partial\Phi^j-U(\Phi),\\
\kappa&=e^{2\psi}\left(L+\lambda PH-\tfrac14\lambda g^2L^2\right)+\tfrac12\lambda v_0,\\
-U&=e^{2\psi}\mathcal L_{\rm bg}(L,N,H,P,\rho,v;u=0)
 -\frac4g(\sqrt2r_0+2gp_0)H,\\
K_{\psi\psi}&=e^{2\psi}(2L+4\lambda H^2-\tfrac12\lambda g^2L^2)+\lambda u,\\
K_{\psi L}&=e^{2\psi}(2-\lambda g^2L),&
K_{LL}&=e^{2\psi}(L^{-1}-\tfrac12\lambda g^2),\\
K^E_{ij}&=K_{ij}-2\kappa_0^{-1}\partial_i\kappa\partial_j\kappa,&
U_E&=(\kappa_0/\kappa)^3U.
\end{aligned}
```

All other entries of K vanish before the Einstein-frame change. The complete
background density and its derivatives are explicit in
[constant.py](../../../computations/gb_ads3_sigma2/constant.py). Its stationary
potential and curvature equation are checked before taking the scalar
Hessian. The saved four-field pencil retains N until its algebraic Schur
complement is taken. The reduced scalar determinant is R(D)R(2-D).
The Einstein-frame chart requires kappa0 nonzero; the underlying density
and Jordan-frame functions above remain available at its zero.

The constant vector curl pencil uses (c,e,V), with curl eigenvalue
m_curl=(D-1)/ell_s, and includes all fourteen grouped terms of the reduction,
in particular the EGG and EHH contributions. Its full determinant is
proportional to (D-1)²(D-m)R(D-1). Only the two generic zero-curl gauge
factors are removed; a further zero at a chiral parameter is retained.

The [constant output](../../../computations/gb_ads3_sigma2/outputs/constant.json)
also gives the CS matrix on the two zero-curl directions (c,e,V)=(c,-Lc,V).
Its R-current Schur coefficient is kappa_eff(1-1/m)/2. The self and mixed
flavor entries vanish at k=2/3, so the undivided matrix is retained there.
This verifies the R-current norm sign inherited from c_L without dividing
through that exceptional flavor coefficient.
