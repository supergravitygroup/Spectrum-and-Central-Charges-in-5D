#!/usr/bin/env python3
"""Numerical Einstein/Clifford checks of only the outer tensor simplification.

Unexpanded derivative arguments are independent tensor jets for this check.
Degree-two even jets multiply theta1 theta2; two odd jets contribute
x1 y2-x2 y1. This is not a commuting-spinor or a SUSY-variation test.
"""
import json,math
from pathlib import Path
from itertools import permutations,product
from functools import lru_cache
import numpy as np
import build_step5a_partial_insertion as source
from step6_supercovariant_maps import *
ROOT=Path(__file__).resolve().parents[1]
rng=np.random.default_rng(1120162025)
sig=[np.array([[0,1],[1,0]],complex),np.array([[0,-1j],[1j,0]]),np.diag([1,-1]).astype(complex)]
gamma=np.array([1j*np.kron(sig[2],np.eye(2)),np.kron(sig[0],sig[0]),np.kron(sig[0],sig[1]),np.kron(sig[0],sig[2]),np.kron(sig[1],np.eye(2))])
eta=np.array([-1,1,1,1,1]);J=np.array([[0,1],[-1,0]],float)
def sign(p):return (-1)**sum(p[a]>p[b] for a in range(len(p)) for b in range(a+1,len(p)))
@lru_cache(None)
def gam(indices):
    out=np.zeros((4,4),complex)
    for p in permutations(range(len(indices))):
        z=np.eye(4,dtype=complex)
        for k in p:z=z@gamma[indices[k]]
        out+=sign(p)*z/math.factorial(len(indices))
    return out
DIMS={'G':(5,5),'T':(5,5),'E':(5,),'V':(5,),'D':(),'ftrace':(),'Lt':(2,2),
 'psi':(5,2),'barpsi':(5,2),'vphi':(2,),'barvphi':(2,),
 'chi':(2,),'barchi':(2,),'phi':(5,2),'barphi':(5,2),'RV':(5,5,2,2),'RQ':(5,5,2)}
def dims(name,nd,rank):
    if name in OPS:return (5,)*nd+tuple(2 if su(x) else 5 for x in OPS[name]['free'])
    if name in ('gam','eps5'):return (5,)*rank
    if name in ('eps2','delta'):return (2,)*rank
    return (5,)*nd+DIMS[name]
@lru_cache(None)
def base(name,nd,rank):
    if name=='gam':
        arr=np.zeros((5,)*rank+(4,4),complex)
        for ii in product(range(5),repeat=rank):arr[ii]=np.prod(eta[list(ii)])*gam(ii)
        return arr
    if name=='eps5':
        arr=np.zeros((5,)*5)
        for p in permutations(range(5)):arr[p]=-sign(p)
        return arr
    if name=='eps2':return J
    if name=='delta':return -J
    shape=dims(name,nd,rank)
    degree=OPS[name]['degree'] if name in OPS else int(name in ODD)
    if degree==1:shape+=(2,4)
    arr=rng.normal(size=shape)+1j*rng.normal(size=shape)
    if name=='Lt':arr=np.array([[3.,1.],[1.,2.]])
    if name in ('G','T'):arr=(arr-np.swapaxes(arr,nd,nd+1))/2
    return arr
@lru_cache(None)
def tensor(name,nd,variance):
    rank=len(variance)-nd;arr=base(name,nd,rank).copy()
    for axis,(size,v) in enumerate(zip(dims(name,nd,rank),variance)):
        if v<0:continue
        if size==5:
            shape=[1]*arr.ndim;shape[axis]=5;arr=arr*eta.reshape(shape)
        else:arr=np.moveaxis(np.tensordot(J,arr,axes=(1,axis)),0,axis)
    return arr
def evaluate(fs,c):
    names={a for f in fs for a,v in f.indices()};labels={a:k for k,a in enumerate(sorted(names))}
    odd=[f for f in fs if f.degree==1]
    assert len(odd) in (0,2)
    channels=[((),1)] if not odd else [((0,1),1),((1,0),-1)]
    value=0j
    for chn,sgn in channels:
        args=[];spin=len(labels);seen=0
        for f in fs:
            inds=f.indices();aa=tensor(f.name,len(f.ds),tuple(v for a,v in inds));ll=[labels[a] for a,v in inds]
            if f.degree==1:aa=aa[...,chn[seen],:];seen+=1;ll.append(spin)
            elif f.name=='gam':ll += [spin,spin+1];spin+=1
            args.extend([aa,ll])
        value+=sgn*(np.einsum(*args,[],optimize='greedy') if args else 1)
    return value*complex(c.subs({L:s.sqrt(10),N:Q(7,10),g:Q(1,5)}))
def main():
    checks=[];worst=0.
    for number,raw,terms in source.source_rows():
        p=Poly()
        for row in terms:
            q=poly(row.c)
            for f in row.fs:q*=token(f.tex)
            p+=q
        rows=list(p.terms.items())
        positions=np.unique(np.linspace(0,len(rows)-1,min(16 if number==1 else 4,len(rows)),dtype=int))
        for pos in positions:
            fs,c=rows[pos];q=canonical(Poly({fs:c}))
            lhs=evaluate(fs,c);rhs=sum(evaluate(gs,d) for gs,d in q.terms.items())
            err=float(abs(lhs-rhs)/(1+abs(lhs)+abs(rhs)));worst=max(worst,err)
            checks.append({'group':number,'raw_term':int(pos)+1,'scaled_residual':err,'pass':err<2e-10})
        print(number,'worst',worst,flush=True)
    bad=[x for x in checks if not x['pass']]
    result={'status':'PASS_SCOPED' if not bad else 'FAIL','checks':checks,'passed':len(checks)-len(bad),
       'failed':len(bad),'maximum_scaled_residual':worst,'threshold':2e-10,
       'scope':'Independent numerical Lorentz, SU2 and ordered Clifford/Grassmann contractions; derivative jets retained, no SUSY claim.'}
    (ROOT/'build/step6_supercovariant_tensor_verification.json').write_text(json.dumps(result,indent=2)+'\n')
    print(result['status'],result['passed'],'passed;',len(bad),'failed; maximum',worst)
    return bool(bad)
if __name__=='__main__':raise SystemExit(main())
