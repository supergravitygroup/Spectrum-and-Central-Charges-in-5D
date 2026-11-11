# Spectrum notation and source conversions

The root [conventions](details/source_conventions.md) are authoritative. The notation here names source results within a common narrative; it defines no new gauge, background, or field truncation.

| Object | Common notation | Source counterpart |
|---|---|---|
| Weyl², LOG, and R² couplings | $`\alpha,\beta,\zeta`$ | LOG files: alpha → beta; R² files: lambda or lambda_R² → zeta |
| Gauging | $`g`$ | Free sign and magnitude; g=1 is not imposed |
| Background scalars | $`L_0,N_0`$ | Sources may abbreviate them as L,N |
| Scalar fluctuations | $`\delta L,\delta N`$ | l,n,s,lambda_s denote different combinations depending on context |
| Gravitino and spin-1/2 fluctuations | $`\Psi_\mu^i,\vartheta^i`$ | The source spinor zeta must not be confused with the common R² coupling zeta |
| AdS₅ radius | $`\ell_5`$ | $`R_0=-20/\ell_5^2`$ |
| Magnetic-product radii | $`\ell_3,r_2`$ | $`k_3=-\ell_3^{-2},\ k_2=r_2^{-2}`$ |
| Harmonic level | $`n`$ | ell in bReport10, j in the flux report |
| Kinetic coefficient | $`Z_a`$ | Defined in the form $`-Z_a[(\nabla\phi_a)^2+M_a^2\phi_a^2]/2`$ |
| Signed first-order root | $`\mu_a`$ | A fermion mass or curl root is used with its defining operator specified |

Fermion degree and fluctuation degree differ. If $`\ell^{(2)}`$ denotes the two-fermion part, $`S^{[2]}`$ is used separately for the quadratic Hessian term. In $`S[\bar\Phi+t\phi]=S^{[0]}+tS^{[1]}+t^2S^{[2]}+\cdots`$, t is only a grading variable; higher-derivative couplings are not expanded.

Auxiliary symbols are local to each section. The R² kinetic combination $`A=L_0-\zeta z_0`$ differs from $`A=\alpha g^2`$ in the generic product calculation. The tables distinguish them as $`A_R`$ and $`a_W`$, respectively. Source notation is retained in the source records.

Conversion dictionary for the generic-product appendix:

```math
a_W=\alpha g^2,\quad a_{\log}=\beta g^2,\quad a_R=\zeta g^2,
\quad K=k_2/g^2,\quad u=N_0/(gL_0),\quad t_n=n(n+1).
```

These combinations retain free parameter dependence and are not assigned sample values. The source notation $`A,B,Z,\nu,t`$ corresponds to these five objects in order. The spherical multiplicity $`2n+1`$ is kept separate from real local polarizations per harmonic. The BPS signs $`\sigma`$ and $`\varsigma`$ are not identified without specifying their source flux/orientation definitions.

Mass is the physical parameter separated from curvature terms in the wave operator. Squaring a first-order root alone loses helicity and fermion-branch information. Root multiplicity, the number of independent eigenvectors, and Jordan-chain length are recorded separately. A Majorana flip identity does not suffice to define the adjoint for a physical Hermitian norm.
