"""Independent flat-jet check of the uncontracted D phi identity.

Uses the actual H, its first and second derivatives, the previous scalar
polynomial and the new vector polynomial. Restriction is imposed only after
descent. No assertion about general curved Ward identities is made.
"""
import json,pickle,itertools as it
import numpy as np
import log_step4_covariant_rules as b
import verify_log_step3_spinor as v
from verify_log_step5_vector import keep,BASE,OUT

if __name__=='__main__':
    left=b.P();gradH=b.P()
    for p in b.make_inputs().values():
        left+=b.Q(1,3)*b.eps('-uJ','-uR')*keep(b.dpoly(b.a.deriv(p),'sZ','uT'))
        gradH+=keep(b.vec('-lD',p))
    with open('/private/tmp/log-vector-two-fermi.pkl','rb') as f:vector=sum(pickle.load(f).values(),b.P())
    from pathlib import Path
    cache=Path('/private/tmp/log-scalar-direct.pkl')
    if cache.exists():
        with cache.open('rb') as f:scalar=keep(sum(pickle.load(f).values(),b.P()))
    else:
        import verify_log_step4_scalar as previous
        scalar=keep(sum(previous.build().values(),b.P()))
    F=np.zeros((5,5));F[0,1]=2;F[1,0]=-2;F[2,3]=3;F[3,2]=-3
    X=np.array([[2,3],[3,5]]);grad=np.array([1,2,3,4,5])
    lhs,_=v.evaluate(left,F,X,grad,output=('sZ','uT','sE','uI'))
    h,_=v.evaluate(vector,F,X,grad,output=('lV',))
    f,_=v.evaluate(scalar,F,X,grad,output=())
    dh,_=v.evaluate(gradH,F,X,grad,output=('lD','uI','uJ'))
    # nabla_zeta^t phi_eta^i = -i/2 eps^ti eps_zetaeta F
    #                         +i/2 eps^ti Gamma^a_zetaeta H_a
    #                         +i Gamma^a_zetaeta nabla_a H^ti.
    rhs={}
    for z,t,e,i in it.product(range(4),range(2),range(4),range(2)):
        for (_,pole,mask),value in f.items():
            key=((z,t,e,i),pole,mask)
            rhs[key]=rhs.get(key,0)-.5j*v.E[t,i]*v.C[z,e]*value
        for ((a,),pole,mask),value in h.items():
            key=((z,t,e,i),pole,mask)
            rhs[key]=rhs.get(key,0)+.5j*v.E[t,i]*v.GD[a,z,e]*v.eta[a]*value
        for ((a,j,k),pole,mask),value in dh.items():
            if j==t and k==i:
                key=((z,t,e,i),pole,mask)
                rhs[key]=rhs.get(key,0)+1j*v.GD[a,z,e]*value
    keys=set(lhs)|set(rhs)
    residual=max(abs(lhs.get(k,0)-rhs.get(k,0)) for k in keys)
    assert residual<1e-7,sorted([(abs(lhs.get(k,0)-rhs.get(k,0)),k,lhs.get(k),rhs.get(k)) for k in keys],reverse=True)[:5]
    report={'status':'PASS','scope':'C24 (2.41b) in flat constant F/X/dW jets, all free spinor and SU(2) slots, explicit degrees zero and two. Uses actual prior scalar polynomial and new vector; not the full curved identity.',
        'tensor_components':64,'compared_coefficients':len(keys),'max_absolute_residual':float(residual)}
    OUT.mkdir(exist_ok=True);(OUT/'multiplet_checks.json').write_text(json.dumps(report,indent=2)+'\n')
    print(report)
