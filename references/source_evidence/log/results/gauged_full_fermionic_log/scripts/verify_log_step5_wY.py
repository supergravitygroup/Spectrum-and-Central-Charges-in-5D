"""Curved bosonic coefficient probes of W^{a}{}_{b} nabla^b Y and Y nabla_b W^{ab}."""
import json,pickle,itertools as it
from collections import defaultdict
import numpy as np
import log_step4_covariant_rules as b
import verify_log_step3_spinor as v
from verify_log_step5_vector import BASE,OUT
original=v.arr
Wab=np.zeros((5,5));dW=np.zeros((5,5,5));dy=np.zeros(5);Y=0

def arr(f,F,X,g):
    if f.name not in ['w','ws','Y']:return original(f,F,X,g)
    if f.name=='Y':
        if len(f.ds)>1:return None
        value=dy.copy() if f.ds else np.array(Y)
    elif f.name=='w':
        if len(f.ds)>1:return None
        value=dW.copy() if f.ds else Wab.copy()
    else:
        if len(f.ds)>1:return None
        value=np.einsum('cduv,bcd->buv',v.SD,dW)/2 if f.ds else np.einsum('cduv,cd->uv',v.SD,Wab)/2
    for axis,index in enumerate(f.ds+f.ix):
        if index[0]=='-':continue
        if index[1]=='l':value=value*np.reshape(v.eta,[5 if q==axis else 1 for q in range(value.ndim)])
        else:value=np.moveaxis(np.tensordot(v.U,value,axes=(1,axis)),0,axis)
    return value

v.arr=arr

def sector(p):
    p=b.normalize(p)
    p=b.P.terms([(c,fs) for c,fs in p.ts if sum(f.power for f in fs if f.name=='pow')==0
        and all(f.name in b.const|{'pow','w','ws','Y','T','RS'} for f in fs)
        and sum(f.name=='Y' for f in fs)==1])
    p=b.normalize(b.expand_geometry(p),True)
    return b.P.terms([(c,fs) for c,fs in p.ts if all(f.name in b.const|{'w','ws','Y'} for f in fs)
        and sum(f.name in ['w','ws'] for f in fs)==1 and sum(len(f.ds) for f in fs)==1])

def evaluate(p):
    got,_=v.evaluate(p,np.zeros((5,5)),np.zeros((2,2)),np.zeros(5),output=('lV',))
    result=np.zeros(5,complex)
    for ((a,),pole,mask),val in got.items():
        assert pole==0 and mask==0
        result[a]+=val
    return result

if __name__=='__main__':
    with open('/private/tmp/log-vector-two-fermi.pkl','rb') as f:polys=pickle.load(f)
    secs={key:sector(p) for key,p in polys.items()};pol=sum(secs.values(),b.P())
    cases=[];parts={}
    for kind in ['W_dY','Y_dW']:
        for c,d in it.combinations(range(5),2):
            Wab[:]=0;dW[:]=0;dy[:]=0;Y=0
            if kind=='W_dY':Wab[c,d]=1;Wab[d,c]=-1;dy[d]=1
            else:Y=1;dW[d,c,d]=1;dW[d,d,c]=-1
            expected=np.zeros(5);expected[c]=3/32*v.eta[c]*v.eta[d]
            got=evaluate(pol);assert np.max(abs(got-expected))<1e-10,(kind,c,d,got,expected)
            cases.append({'sector':kind,'W_slot':[c,d],'derivative_slot':d,'vector':got.real.tolist(),'status':'PASS'})
            if (c,d)==(1,2):
                parts[kind]={key:float(evaluate(p)[1].real) for key,p in secs.items() if abs(evaluate(p)[1])>1e-12}
    report={'status':'PASS','scope':'Coefficients of the two W-Y first-derivative tensor structures only; all ten two-form planes for each structure. Finite Clifford contractions, absolute tolerance 1e-10; not a complete curved constraint or SUSY test.',
        'source_comparison':'C24 supplement 2.2.3, PDF121, first two terms','contributions':len(pol.ts),'by_primary_at_W12_or_d2W12_1':parts,'checks':cases}
    OUT.mkdir(exist_ok=True);(OUT/'wY_checks.json').write_text(json.dumps(report,indent=2)+'\n')
    with open('/private/tmp/log-vector-wY.pkl','wb') as f:pickle.dump(secs,f)
    print({k:report[k] for k in ['status','contributions','by_primary_at_W12_or_d2W12_1']})
