"""Numerical polynomial-matrix extraction and projected determinantal roots.

This module has no knowledge of bosonic predictions or expected mode counts.
Results are finite-point numerical evidence, not an all-coupling certificate.
"""
import math
import numpy as np
from scipy.linalg import eig
from scipy.optimize import linear_sum_assignment

def value(C, z):
    out = np.zeros_like(C[0])
    for a in C[::-1]:
        out = out*z+a
    return out

def derivative(C,z):
    return sum(j*a*z**(j-1) for j,a in enumerate(C) if j)

def scaled_error(A,B):
    return float(np.max(np.abs(A-B))/max(1.,np.max(np.abs(A)),np.max(np.abs(B))))

def fit(evaluator, count=5, phase=.23, radius=1.7):
    """DFT interpolation about D=1, converted to powers of D.

    The over-resolved high coefficients are recorded before degree reduction.
    No roots or bosonic values are used to choose the degree.
    """
    angles=2*np.pi*(np.arange(count)+phase)/count
    x=radius*np.exp(1j*angles)
    samples=np.array([evaluator(1+z) for z in x])
    centered=np.array([np.mean(samples*np.exp(-1j*j*angles)[:,None,None],axis=0)/radius**j
                       for j in range(count)])
    monomial=np.zeros_like(centered)
    for j in range(count):
        for r in range(j+1):
            monomial[r]+=centered[j]*math.comb(j,r)*(-1)**(j-r)
    sizes=np.max(np.abs(monomial),axis=(1,2))
    threshold=2e-11*max(sizes)
    degree=int(np.flatnonzero(sizes>threshold)[-1])
    if degree >= count-1:
        raise ArithmeticError("Interpolation degree reaches grid capacity")
    C=monomial[:degree+1]
    holdouts=[]
    for z in [.21+.87j,2.83-.44j]:
        error=scaled_error(evaluator(z),value(C,z))
        if error>2e-9:
            raise ArithmeticError(("polynomial holdout",error,z))
        holdouts.append(dict(D=[z.real,z.imag],scaled_error=error))
    return C,dict(nodes=count,phase=phase,radius=radius,coefficient_maxima=sizes.tolist(),
                  discarded_relative_size=float(max(sizes[degree+1:],default=0)/max(sizes)),
                  holdouts=holdouts)

def evaluation_scale(C,z):
    """Coefficient-based backward-error scale, valid even when K(z)=0."""
    return max(sum(float(np.linalg.norm(c))*abs(z)**j for j,c in enumerate(C)),1e-300)

def singular_values(C,z):
    return np.linalg.svd(value(C,z),compute_uv=False)/evaluation_scale(C,z)

def action_rank_certificate(C,z,rank,multiplicity,source_singular_values,disagreement):
    """Resolve rank loss to interpolation, root-solve and rounding errors.

    The unreduced source-action singular values are supplied separately.
    This is a numerical backward-error certificate, not an exact rank proof.
    """
    scale=evaluation_scale(C,z)
    retained=rank-multiplicity
    polynomial_values=np.linalg.svd(value(C,z),compute_uv=False)
    solve_error=float(polynomial_values[retained])
    budget=max(4*(disagreement+solve_error)+128*np.finfo(float).eps*scale,1e-13)
    sv=np.asarray(source_singular_values)
    resolved_rank=int((sv>budget).sum())
    gap=float(sv[retained-1]/budget) if retained else None
    diagnostic=local_rank_drop(C,z,rank)
    if (disagreement/scale>2e-9 or solve_error/scale>2e-8
            or not diagnostic['accepted'] or resolved_rank!=retained
            or (gap is not None and gap<20)):
        raise ArithmeticError(("direct action backward rank separation",z,
                               disagreement/scale,solve_error/scale,
                               resolved_rank,retained,gap))
    return dict(root=[z.real,z.imag],coefficient_scaled_disagreement=disagreement/scale,
                action_interpolant_disagreement=disagreement,
                polynomial_rank_defect_residual=solve_error,
                coefficient_scaled_root_solve_residual=solve_error/scale,
                coefficient_evaluation_scale=scale,singular_values=sv.tolist(),
                rank_threshold_absolute=budget,retained_gap_over_error_budget=gap,
                resolved_extra_nullity=rank-resolved_rank)

def local_rank_drop(C,z,rank):
    """Distinguish a localized rank drop from an ill-conditioned large-D chart.

    A tiny singular value at a huge D is insufficient: leading coefficient
    rank loss can make the same value tiny throughout its neighborhood.
    Both the backward residual and its ratio to four nearby probes are kept.
    The probes are diagnostics, not a bound excluding arbitrary finite roots.
    """
    sv=singular_values(C,z)
    radius=1e-4*max(1.,abs(z))
    neighbors=[float(singular_values(C,z+radius*direction)[rank-1])
               for direction in (1.,-1.,1j,-1j)]
    baseline=float(np.median(neighbors))
    relative=float(sv[rank-1]/max(baseline,1e-300))
    if not np.isfinite(sv).all() or not np.isfinite(relative):
        raise ArithmeticError(("nonfinite rank diagnosis",z))
    return dict(accepted=bool(sv[rank-1]<2e-8 and relative<1e-5),
                backward_singular_value=float(sv[rank-1]),
                neighboring_singular_values=neighbors,
                localization_ratio=relative,probe_radius=radius)

def refined_root(C,z):
    # Jacobi determinant identity: d log det M / dz = tr(M^-1 M').
    for _ in range(35):
        try:
            slope=np.trace(np.linalg.solve(value(C,z),derivative(C,z)))
        except np.linalg.LinAlgError:
            break
        if not np.isfinite(slope) or abs(slope)<1e-300:
            break
        step=1/slope
        z-=step
        if abs(step)<2e-15*(1+abs(z)):
            break
    return z

def pencil_roots(C,scale):
    """Generalized companion pencil, with D=scale*x.

    Homogeneous pairs unresolved at machine precision are reported, not
    described as a rigorous exclusion of very large finite roots.
    """
    A=np.asarray([c*scale**j for j,c in enumerate(C)])
    A=A/max(np.max(np.abs(A)),1e-300)
    degree=len(A)-1;size=A.shape[1]
    left=np.zeros((degree*size,degree*size),complex)
    right=np.eye(degree*size,dtype=complex)
    for i in range(degree-1):
        left[size*i:size*(i+1),size*(i+1):size*(i+2)]=np.eye(size)
    left[-size:,:]=-np.concatenate(A[:-1],axis=1)
    right[-size:,-size:]=A[-1]
    alpha,beta=eig(left,right,right=False,homogeneous_eigvals=True)
    threshold=128*np.finfo(float).eps*max(1,degree*size)
    resolved=np.abs(beta)>threshold*np.maximum(np.abs(alpha),np.abs(beta))
    roots=[refined_root(C,scale*a/b) for a,b in zip(alpha[resolved],beta[resolved])]
    return roots,dict(unresolved_homogeneous_pairs=int((~resolved).sum()),
                      pair_tolerance=threshold,D_scale=float(scale))

def distance_multiset(A,B):
    if len(A)!=len(B):return np.inf
    if not A:return 0.
    costs=np.abs(np.asarray(A)[:,None]-np.asarray(B)[None,:])
    i,j=linear_sum_assignment(costs)
    return float(costs[i,j].max())

def extract(C,seed=25,projections=4,scale=1.):
    ranks=[];probes=[.37+.11j,-1.2+.8j,1.9-.7j]
    for z in probes:ranks.append(int((singular_values(C,z)>1e-10).sum()))
    rank=max(ranks);m=C.shape[1]
    rng=np.random.default_rng(seed)
    candidates=[];pencils=[];nonlocal_candidates=[]
    for _ in range(projections):
        if rank==m:P=Q=np.eye(m)
        else:
            P=np.linalg.qr(rng.normal(size=(m,rank))+1j*rng.normal(size=(m,rank)))[0]
            Q=np.linalg.qr(rng.normal(size=(m,rank))+1j*rng.normal(size=(m,rank)))[0]
        projected=np.asarray([P.conj().T@c@Q for c in C])
        roots,meta=pencil_roots(projected,scale)
        # Keep rank-lowering candidates from every projection. Extraneous
        # projection roots do not lower the rank of the unreduced matrix.
        physical=[]
        for z in roots:
            if not np.isfinite(z):
                raise ArithmeticError(("nonfinite refined finite-pencil root",z))
            diagnostic=local_rank_drop(C,z,rank)
            if diagnostic['accepted']:
                physical.append(complex(z))
            elif diagnostic['backward_singular_value']<2e-8:
                nonlocal_candidates.append(dict(projection=len(candidates),
                                                root=[z.real,z.imag],**diagnostic))
        candidates.append(physical);pencils.append(meta)
    # An extraneous projected root can converge to a physical root under
    # Newton iteration, producing an extra copy in one projection. Intersect
    # as multisets, retaining the minimum supported multiplicity.
    pools=[list(x) for x in candidates[1:]]
    roots=[];uncertainties=[];spread=0.
    for z in candidates[0]:
        indices=[]
        for pool in pools:
            distances=np.abs(np.asarray(pool)-z)
            if not len(distances) or distances.min()>2e-6:break
            indices.append(int(distances.argmin()))
        if len(indices)!=len(pools):continue
        partners=[pool.pop(i) for pool,i in zip(pools,indices)]
        uncertainty=max(abs(z-w) for w in partners)
        spread=max(spread,uncertainty)
        roots.append(sum([z]+partners)/len(candidates))
        uncertainties.append(uncertainty)
    if not roots:
        raise ArithmeticError(("no common physical roots",rank,[len(x) for x in candidates]))
    # A rank-lowering root absent from the common set must not disappear
    # merely because the final count happens to match a prediction.
    unmatched=[]
    for projection,roots_here in enumerate(candidates):
        for z in roots_here:
            distance=min(abs(z-w) for w in roots)
            if distance>2e-6:
                unmatched.append(dict(projection=projection,root=[z.real,z.imag],
                                      distance_to_common=distance))
    if unmatched:
        raise ArithmeticError(("unresolved unique rank-lowering candidates",unmatched))
    # Resolve a close pair whenever its separation exceeds the measured
    # cross-projection uncertainty. A fixed 2e-6 cluster radius would turn
    # the exact roots 1.5 and 1.5000001 into a spurious midpoint double root.
    groups=[]
    for z,error in sorted(zip(roots,uncertainties),key=lambda t:(t[0].real,t[0].imag)):
        for group in groups:
            center=sum(w for w,_ in group)/len(group)
            radius=max(128*np.finfo(float).eps*(1+abs(center)),
                       8*(error+max(e for _,e in group)))
            if abs(z-center)<=radius:
                group.append((z,error));break
        else:groups.append([(z,error)])
    records=[]
    for group in groups:
        z=sum(w for w,_ in group)/len(group);s=singular_values(C,z)
        diagnostic=local_rank_drop(C,z,rank)
        extra=rank-int((s>1e-8).sum())
        if not diagnostic['accepted'] or extra<len(group):
            raise ArithmeticError(("unresolved root cluster or unsupported multiplicity",
                                   z,len(group),extra,diagnostic))
        records.append(dict(root=[z.real,z.imag],multiplicity=len(group),
                            normalized_singular_values=s.tolist(),
                            threshold_nullity_increase=extra,local_rank_drop=diagnostic,
                            cluster_spread=max(abs(z-w) for w,_ in group)))
    distinct=[complex(*x['root']) for x in records]
    separation=min((abs(a-b) for i,a in enumerate(distinct) for b in distinct[i+1:]),default=None)
    return records,dict(generic_rank=rank,dimension=m,probe_ranks=ranks,
                        projection_seed=seed,projections=projections,projection_spread=spread,
                        rank_filtered_candidate_counts=[len(x) for x in candidates],
                        discarded_unmatched_candidates=[len(x)-len(roots) for x in candidates],
                        discarded_candidate_interpretation="extra Newton copies of retained roots only; unique unmatched rank-lowering candidates fail",
                        singular_value_normalization="sum_j Frobenius_norm(C_j)*abs(D)^j",
                        rejected_nonlocal_rank_candidates=nonlocal_candidates,
                        numerical_limit="finite-pencil candidates without a localized rank drop are rejected; unresolved homogeneous pairs and ill-conditioned large-D neighborhoods are not an analytic root exclusion",
                        minimum_distinct_root_separation=separation,pencils=pencils)
