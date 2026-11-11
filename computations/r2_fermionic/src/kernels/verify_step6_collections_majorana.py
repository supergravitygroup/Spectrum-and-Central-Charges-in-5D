"""Independent Majorana-aware tensor check of the collected triplet map.

This evaluator supplies actual antisymmetric C and odd Grassmann channels.
It does not treat a barred field as an independent jet when testing flips.
"""
import json,hashlib
from functools import lru_cache
from collections import defaultdict
import numpy as np
import step6_supercovariant_collections as c
from step6_supercovariant_collections import *
import verify_step6_supercovariant_tensors as ev

C=ev.gamma[2]@ev.gamma[4]
original_base=ev.base
ev.DIMS['L']=()
ev.DIMS['Probe']=(2,2)
jets={};probe=np.eye(2)

def jet(key,shape):
    if key not in jets:jets[key]=ev.rng.normal(size=shape)+1j*ev.rng.normal(size=shape)
    return jets[key]

@lru_cache(None)
def base(name,nd,rank):
    if name=='Probe':return probe
    if name in ['barvphi','barchi']:
        f=base(name[3:],nd,rank)
        return np.einsum('...x,xy->...y',f,C)
    if name in OPS:
        op=OPS[name];fs=op['factors']
        if len(fs)==1 and fs[0].name=='Lt':
            shape=(5,)*nd+(2,2)
            arr=jet(('Lt',op['kind']),shape)
            return (arr+arr.swapaxes(-1,-2))/2
        if not fs and op['coefficient']==L and op['kind']=='D':
            arr=jet(('Lt','D'),(5,2,2));arr=(arr+arr.swapaxes(-1,-2))/2
            S=original_base('Lt',0,2);Sup=ev.J@S@ev.J.T
            return np.einsum('ij,aij->a',Sup,arr)/np.sqrt(10.)
        if len(fs)==1 and fs[0].name in ['vphi','barvphi']:
            arr=jet(('vphi',op['kind']),(5,)*nd+(2,2,4))
            return np.einsum('...x,xy->...y',arr,C) if fs[0].name.startswith('bar') else arr
    return original_base(name,nd,rank)

ev.base=base

def evaluate(p):return sum(ev.evaluate(fs,cc) for fs,cc in p.terms.items())

def main():
    global probe
    checks=[]
    def ck(x,label,residual=None):checks.append({'check':label,'pass':bool(x),'residual':residual})
    ck(np.max(np.abs(C.T+C))==0,'C is antisymmetric')
    for a in range(5):ck(np.max(np.abs(ev.gamma[a].T@C-C@ev.gamma[a]))==0,f'gamma {a}: transpose rule t1=+1')
    result,total=c.build()
    # All final collections are checked at the tensor level. Exact duplicate
    # rendered words cancel first; the remaining nontrivial index orbits are
    # independently contracted using explicit SU(2), Clifford and odd arrays.
    remainders=[]
    for n,p,q in c.RAW_GROUPS:
        diff=canonical(expanded(p)-expanded(q));buckets={}
        for fs,cc in diff.terms.items():
            key=sc.render_term(s.Integer(1),fs)
            old=buckets.get(key,(fs,0));buckets[key]=(fs,old[1]+cc)
        remainders.append((n,Poly({fs:s.expand(cc) for fs,cc in buckets.values() if s.expand(cc)!=0})))
    oldY=original_Y(dn('i'),dn('j'))
    newY=expanded(Y(dn('i'),dn('j')))
    for trial in range(3):
        ev.rng=np.random.default_rng(5112026+trial);jets.clear();base.cache_clear();original_base.cache_clear();ev.tensor.cache_clear()
        for component in [(0,0),(0,1),(1,1)]:
            probe=np.zeros((2,2));probe[component]=1
            base.cache_clear();ev.tensor.cache_clear()
            spectator=A('Probe',up('i'),up('j'))
            lhs=evaluate(oldY*spectator);rhs=evaluate(newY*spectator)
            err=float(abs(lhs-rhs)/(1+abs(lhs)+abs(rhs)))
            ck(err<2e-10,f'trial {trial}: full triplet map component {component}, Majorana bars linked',err)
        for n,diff in remainders:
            val=evaluate(diff) if diff.terms else 0
            scale=sum(abs(ev.evaluate(fs,cc)) for fs,cc in diff.terms.items())
            err=float(abs(val)/(1+scale))
            ck(err<2e-10,f'trial {trial}: complete expanded outer-contraction equality, source group {n}',err)
    failed=[q for q in checks if not q['pass']]
    out={'status':'PASS_SCOPED' if not failed else 'FAIL','passed':len(checks)-len(failed),'failed':len(failed),'checks':checks,
         'ledger_sha256':hashlib.sha256((ROOT/'build/step6_supercovariant_collected_ledger.json').read_bytes()).hexdigest(),
         'threshold':2e-10,'maximum_scaled_residual':max(x['residual'] or 0 for x in checks),
         'scope':'Majorana-aware full triplet-map equality in all symmetric components; every collected outer group before/after simplification. General polynomial identities are verified separately. No SUSY/reality certification.'}
    (ROOT/'build/step6_collection_majorana_verification.json').write_text(json.dumps(out,indent=2)+'\n')
    print(out['status'],out['passed'],'passed;',out['failed'],'failed; max',out['maximum_scaled_residual'])
    if failed:print(failed[:10])
    return bool(failed)
if __name__=='__main__':raise SystemExit(main())
