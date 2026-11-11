"""Boost-weight sectors of the bosonic metric/form action; provenance in source_manifest.json."""
import symengine as se, itertools, time, sys, os
from algebra import Engine, P, ZERO
from action import build, zeros
LC=['p','m',2,3,4]; WT={'p':1,'m':-1,2:0,3:0,4:0}
CART={0:{'p':se.Rational(1,2),'m':se.Rational(1,2)},1:{'p':se.Rational(1,2),'m':se.Rational(-1,2)},2:{2:1},3:{3:1},4:{4:1}}
def comps(rank,kind,n):
    out=[]
    if rank==0: return [()] if n==0 else []
    if kind=='sym': it=itertools.combinations_with_replacement(LC,rank)
    else: it=itertools.combinations(LC,rank)
    for c in it:
        if sum(WT[x] for x in c)==n: out.append(c)
    return out
def lc_to_cart(rank,kind,amp):
    """amp: dict LC-tuple(sorted per LC order) -> (a_expr,b_expr). returns nested list of P (Cartesian)."""
    def lcval(idx):  # value of LC component with arbitrary index order
        if kind=='sym':
            key=tuple(sorted(idx,key=LC.index)); sgn=1
        else:
            if len(set(idx))<len(idx): return (0,0)
            order=sorted(range(len(idx)),key=lambda i: LC.index(idx[i]))
            key=tuple(idx[i] for i in order)
            # permutation sign
            sgn=1; o=list(order)
            for i in range(len(o)):
                for j in range(i+1,len(o)):
                    if o[i]>o[j]: sgn=-sgn
        if key in amp: A,B=amp[key]; return (sgn*A,sgn*B)
        return (0,0)
    if rank==0:
        A,B=amp.get((),(0,0)); return P(0,A,B,0)
    shape=[5]*rank
    def build_(prefix):
        if len(prefix)==rank:
            a=0;b=0
            for choice in itertools.product(*[list(CART[c].items()) for c in prefix]):
                coef=1; idx=[]
                for (lab,cf) in choice: coef=coef*cf; idx.append(lab)
                A,B=lcval(idx); a=a+coef*A; b=b+coef*B
            return P(0,se.expand(a),se.expand(b),0)
        return [build_(prefix+[i]) for i in range(5)]
    return build_([])
FIELDS=[('h',2,'sym'),('C',1,'f'),('V',1,'f'),('B',2,'f'),('E',3,'f'),('L',0,'f'),('N',0,'f')]
def sector(bg,n,D,S,fields=FIELDS,verbose=True,charged=False,model='GB',alpha=0,beta=0,zeta=0,fs=False):
    pert={}; avars=[]; bvars=[]
    if charged:
        fields=[('Z',1,'f')]
    for name,rank,kind in fields:
        ca=comps(rank,kind,n); cb=comps(rank,kind,-n)
        amp={}
        for c in ca:
            s_=se.Symbol('a_%s_%s'%(name,''.join(map(str,c)) or '0')); avars.append(s_); amp.setdefault(c,[0,0])[0]=s_
        for c in cb:
            s_=se.Symbol('b_%s_%s'%(name,''.join(map(str,c)) or '0')); bvars.append(s_); amp.setdefault(c,[0,0])[1]=s_
        amp={k:tuple(v) for k,v in amp.items()}
        pert[name]=lc_to_cart(rank,kind,amp)
    if charged:
        Zp=pert['Z']
        pert['Z']=[P(0,x.a,0,0) for x in Zp]; pert['Zb']=[P(0,0,x.b,0) for x in Zp]
    for name,rank,kind in FIELDS+[('Z',1,'f'),('Zb',1,'f')]:
        if name not in pert:
            pert[name]=P() if rank==0 else (zeros(5) if rank==1 else (zeros(5,5) if rank==2 else [[[ZERO]*5 for _ in range(5)] for _ in range(5)]))
    eng=Engine(bg,D,S)
    t=time.time(); tot,diag=build(eng,pert,verbose=verbose,model=model,alpha=alpha,beta=beta,zeta=zeta,fs=fs)
    if verbose: print(' build time %.1fs'%(time.time()-t),flush=True)
    K=[[se.expand(se.diff(se.diff(tot.ab,bj),ai)) for ai in avars] for bj in bvars]
    return dict(K=K,avars=avars,bvars=bvars,lin_a=tot.a,lin_b=tot.b,tot=tot)
