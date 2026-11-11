"""Read-only regression checks with independently specified polynomial roots."""
import json
import numpy as np
from polynomial import extract, distance_multiset, local_rank_drop


def diagonal(roots, gauge=2):
    size=len(roots)+gauge
    C=np.zeros((2,size,size),complex)
    for i,root in enumerate(roots):
        C[0,i,i]=-root
        C[1,i,i]=1
    return C


def flatten(records):
    return [complex(*r["root"]) for r in records for _ in range(r["multiplicity"])]


def run():
    cases=[
        ("simple roots and two gauge zeros", diagonal([-.7,1.2,2.5,4.7]),[-.7,1.2,2.5,4.7]),
        ("semisimple double",diagonal([1.5,1.5,3.5,4.5]),[1.5,1.5,3.5,4.5]),
        ("resolvable separation 1e-5",diagonal([1.5,1.50001,3.5,4.5]),[1.5,1.50001,3.5,4.5]),
        ("resolvable separation 1e-7",diagonal([1.5,1.5000001,3.5,4.5]),[1.5,1.5000001,3.5,4.5]),
        ("complex pair",diagonal([1+.3j,1-.3j,3.5,4.5]),[1+.3j,1-.3j,3.5,4.5]),
        ("whole physical block vanishes",diagonal([1.3,1.3]),[1.3,1.3]),
    ]
    # K=U(D) diag(D-2,D+3) V(D)^T has rank two except at 2 and -3.
    # Its generic square projections have additional, nonphysical roots.
    U=np.array([[[1,0],[0,1],[0,0],[0,0]],
                [[0,0],[0,0],[1,0],[0,1]]],complex)
    V=np.array([[[1,0],[0,1],[0,0],[0,0]],
                [[0,0],[0,0],[.7,0],[0,-.4]]],complex)
    A=np.array([np.diag([-2,3]),np.eye(2)],complex)
    C=np.zeros((4,4,4),complex)
    for i in range(2):
        for j in range(2):
            for k in range(2):
                C[i+j+k]+=U[i]@A[j]@V[k].T
    cases.append(("extraneous projection roots",C,[2,-3]))
    # Leading coefficient has lower rank than generic K. Its tiny scaled
    # singular value at large D must not be mistaken for an actual rank drop.
    high=np.zeros((4,4,4),complex)
    high[0,0,0]=-2;high[1,0,0]=1
    high[0,1,1]=1;high[3,1,1]=1
    cases.append(("unequal polynomial degrees",high,
                  [2,-1,.5+np.sqrt(3)*.5j,.5-np.sqrt(3)*.5j]))
    records=[]
    for label,C,expected in cases:
        for seed in (25,109):
            found,info=extract(C,seed=seed)
            error=distance_multiset(flatten(found),expected)
            if error>1e-10:
                raise AssertionError((label,seed,error,found))
            if "resolvable separation" in label and any(r["multiplicity"]!=1 for r in found):
                raise AssertionError(("distinct roots were merged",label,found))
            if label in ("semisimple double","whole physical block vanishes"):
                if not any(r["multiplicity"]==2 and r["threshold_nullity_increase"]>=2 for r in found):
                    raise AssertionError(("semisimple multiplicity lost",label,found))
            records.append(dict(check=label,seed=seed,maximum_error=error,
                                distinct_roots=len(found),roots_with_multiplicity=len(expected)))
    diagnostic=local_rank_drop(high,1e12+2e11j,2)
    if diagnostic["accepted"]:
        raise AssertionError("Nonlocalized large-D rank ceiling accepted")
    records.append(dict(check="large-D numerical rank ceiling rejected",**diagnostic))
    # Direct, exact LR polynomial at the exceptional constant torus level.
    # This is the actual matrix input, not a bosonic prediction.
    import sympy as sp
    from backend import lr_polynomial
    _,K,_,_,_=lr_polynomial("4","0","1","1/2",1,"0")
    D=sp.Symbol("D")
    generic=K.subs(D,sp.Rational(37,100)).rank()
    repeated=K.subs(D,sp.Rational(5,2)).rank()
    if (generic,repeated)!=(8,6):
        raise AssertionError(("constant T2 exact rank",generic,repeated))
    degree=max(sp.degree(v,D) for v in K if v!=0)
    C=np.array([np.array(K.applyfunc(lambda v:sp.expand(v).coeff(D,j)).tolist(),complex)
                for j in range(int(degree)+1)])
    found,_=extract(C)
    doubled=[r for r in found if abs(complex(*r["root"])-2.5)<1e-10]
    if len(doubled)!=1 or doubled[0]["multiplicity"]!=2 or doubled[0]["threshold_nullity_increase"]<2:
        raise AssertionError(("constant T2 repeated mode",found))
    records.append(dict(check="constant T2 semisimple multiplicity",
                        generic_rank=generic,rank_at_D_five_halves=repeated,
                        numerical_multiplicity=doubled[0]["multiplicity"]))
    return records


if __name__=="__main__":
    result=run()
    print(json.dumps(dict(status="PASS",checks=result,count=len(result)),indent=2))
