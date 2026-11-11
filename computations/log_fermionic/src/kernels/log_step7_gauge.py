"""Covariant-derivative gauge evaluation; read-only inputs, separate step-7 output.

The ordinary derivative on the output includes spin and SU(2) connections.
Q/S/K connection contributions are expanded before imposing the scalar and
dilatino gauges. This is an algebraic cross-check, not a SUSY certificate.
"""
from pathlib import Path
from collections import Counter, defaultdict
from functools import lru_cache
import pickle, json, hashlib, time, inspect
import canonicalize_log_two_fermi as q

b=q.b; p=q.p; A=q.A; P=b.P; Q=b.Q; I=b.I
BASE=q.BASE; SOURCE_OUT=q.OUT; OUT=BASE/'sources/step7'; q.OUT=OUT
F=b.field; up=b.up; dn=b.dn
for n,sp,sy in [
    ('grav',('lsu',Q(1,2),1),r'\psi'),
    ('scon',('lsu',Q(3,2),1),r'\phi'),
    ('fcon',('ll',Q(2),0),'f'),
    ('Lc',('uu',Q(3),0),'L_c'),
    ('gc',('',Q(0),0),'g')]:
    b.spec[n]=sp; b.symbols[n]=sy
b.const.add('gc')
# The independent linear compensator is a symmetric SU(2) triplet.
_old_symmetry=q.symmetry
def _triplet_symmetry(name,nd,nix):
    if name=='Lc':return _old_symmetry('aux',nd,nix)
    # Keep f_ab ordered: master R03/R05 imply f_ab|_chi = bar(psi_a) gamma_b chi.
    # Its antisymmetric part starts at two fermions; only its bosonic body is symmetric.
    if name=='RMB':
        base,gens=_old_symmetry(name,nd,nix)
        arr=list(range(nd+nix+2))
        arr[nd:nd+4]=[nd+2,nd+3,nd,nd+1]
        group=q.PermutationGroup(list(gens)+[q.Permutation(arr)])
        ba,gg=group.schreier_sims_incremental()
        return q.get_minimal_bsgs(ba,gg)
    return _old_symmetry(name,nd,nix)
q.symmetry=_triplet_symmetry
# Permit a tensor with a free spinor and additional free Lorentz indices.
src=inspect.getsource(q.spin_paths)
src=src.replace("slot=='phi'", "any(x.startswith('s') for x in p.FREE[slot])")
src=src.replace("start='sE'", "start=next(x for x in p.FREE[slot] if x.startswith('s'))")
exec(src,q.__dict__)
src=inspect.getsource(q.reduce_clifford)
src=src.replace("slot=='phi'", "any(x.startswith('s') for x in p.FREE[slot])")
exec(src,q.__dict__)

def free_indices(pol):
    found=None
    for c,fs in pol.ts:
        ct=Counter(x[1:] for f in fs for x in b.allix(f))
        fr={x[1:]:x[0] for f in fs for x in b.allix(f) if ct[x[1:]]==1}
        assert all(v in (1,2) for v in ct.values()),ct
        if found is None:found=fr
        assert fr==found,(fr,found)
    return found or {}

def compact(pol,cliff=False):
    if not pol.ts:return pol
    free=free_indices(pol)
    slot='jet:'+str(tuple(sorted(free.items())))
    p.FREE[slot]=free
    pol=q.collect_tensor(pol,slot)[0]
    if cliff and sum(x.startswith('s') for x in free)<=1:
        pol=q.collect_clifford(pol,slot)[0]
    return pol

def alpha_copy(pol,mp):
    free=set(mp)
    names={x[1:] for c,fs in pol.ts for f in fs for x in b.allix(f)}
    mp={**{x:b.fresh(x[0]) for x in names-free},**mp}
    def ix(xs):return tuple(x[0]+mp[x[1:]] for x in xs)
    return P.terms([(c,tuple(b.replace(f,ix=ix(f.ix),ds=ix(f.ds),oddD=ix(f.oddD)) for f in fs)) for c,fs in pol.ts])

def gauge_poly(pol,limit):
    out=P()
    for c,fs in pol.ts:
        if sum(f.parity for f in fs)>limit:continue
        term=P(c)
        for f in fs:
            if not term.ts:break
            others=sum(h.parity for h in fs if h is not f)
            term=p.retained(term*gauge(f,limit-others),limit)
        out+=term
    return out

def gauge(f,limit):
    if limit<0 or f.parity>limit:return P()
    if f.name in b.GEOM:return gauge_poly(b.geometry(f),limit)
    # Stable free labels permit caching independent of dummy-index names.
    mp={};count=Counter()
    for x in b.allix(f):
        if x[1:] not in mp:
            count[x[1]]+=1;mp[x[1:]]=x[1]+'F'+str(count[x[1]])
    def conv(xs):return tuple(x[0]+mp[x[1:]] for x in xs)
    ff=b.replace(f,ix=conv(f.ix),ds=conv(f.ds),oddD=conv(f.oddD))
    res=_gauge(ff,limit)
    return alpha_copy(res,{v:k for k,v in mp.items()})

@lru_cache(None)
def _gauge(f,limit):
    if not f.ds:
        if f.name=='W' or f.name=='pow':return P(1)
        if f.name=='L':return P()
        if f.name=='X':return -F('gc')*A('Lc',f.ix)
        return p.elementary(f)
    a,*rest=f.ds;u=b.replace(f,ds=tuple(rest))
    out=b.vec(a,gauge(u,limit))
    if limit>=1:
        s,k,r=[b.fresh(x) for x in ('s','u','u')]
        # Right lowering: Q_{alpha i}=eps_{ji} nabla_alpha^j.
        conn=F('grav',a,up(s),up(k))*p.project(P(b.eps(dn(k),dn(r))))
        out+=Q(1,2)*conn*gauge_poly(b.D(u,s,r),limit-1)
        s,k,c,d,t=[b.fresh(x) for x in ('s','u','l','l','s')]
        # Raised physical matrix action has the opposite sign to the
        # two-index gamma tensor's upper/lower placement.
        phi=I*F('scon',a,up(s),up(k))+I*Q(1,3)*F('ten',dn(c),dn(d))*F('g2',up(c),up(d),up(s),dn(t))*F('grav',a,up(t),up(k))
        out+=-Q(1,2)*phi*gauge_poly(b.Sgen(u,s,k),limit-1)
    c=b.fresh('l')
    out+=F('fcon',a,up(c))*gauge_poly(b.K(u,c),limit)
    if limit>=2:
        s,t,k=[b.fresh(x) for x in ('s','s','u')]
        conn=F('grav',a,up(s),up(k))*F('g1',up(c),dn(s),up(t))*F('chi',dn(t),dn(k))
        out+=-Q(1,3)*conn*gauge_poly(b.K(u,c),limit-2)
    return compact(p.retained(out,limit),cliff=False)

INVERSE={'rho':('W',1),'lam':('L',-1),'aux':('X',Q(1,2)),
         'hatF':('F',-1),'ten':('w',Q(3,16)),
         'chi':('x',I*Q(3,32)),'auxD':('Y',Q(-3,128)),
         'RQ':('w3a',-I),'RV':('za',I*Q(3,4))}

def inverse(f):
    if f.name in INVERSE:
        name,c=INVERSE[f.name];return c*b.replace(f,name=name)
    if f.name=='RMB':
        a,bb,c,d=f.ix;s,t,u,v=[b.fresh('s') for _ in range(4)]
        out=Q(1,4)*F('S',a,bb,up(s),up(t))*F('S',c,d,up(u),up(v))
        inside=I*F('w4',dn(s),dn(t),dn(u),dn(v))
        for aa,bb,cc,dd in [(s,t,u,v),(s,u,t,v),(s,v,t,u)]:
            inside+=F('ws',dn(aa),dn(bb))*F('ws',dn(cc),dn(dd))
        out*=inside
        for a in reversed(f.ds):out=b.vec(a,out)
        return out
    raise ValueError(('inverse',f))

def projected_gauge(f,limit):
    if f.name=='pow':return P(1)
    if f.name in b.const:return P(f)
    return gauge_poly(P(inverse(f)),limit)

def simple_zero(fs):
    for f in fs:
        if f.name=='lam' and not f.ds:return 'undifferentiated dilatino'
        if f.name=='rho' and len(f.ds)==1:return 'first scalar derivative'
        if f.name=='RMB':
            # Every contraction between curvature pairs is zero.
            if any(x[1:]==y[1:] for x in f.ix[:2] for y in f.ix[2:]):return 'Lorentz curvature trace'
    return None

def build(slot):
    source=pickle.load(open(SOURCE_OUT/(slot+'-clifford.pkl'),'rb'))
    limit=1 if slot=='phi' else 2
    out=P();ledger=[]
    for j,(c,fs) in enumerate(source.ts):
        zero=simple_zero(fs)
        if zero:
            ledger.append({'input':j,'zero':zero});continue
        term=P(c)
        for n,f in enumerate(fs):
            others=sum(x.parity for m,x in enumerate(fs) if n!=m)
            term=p.retained(term*projected_gauge(f,limit-others),limit)
        out+=term
        ledger.append({'input':j,'expanded_terms':len(term.ts)})
        if j%10==0:print(slot,j,len(source.ts),'raw',len(out.ts),'cache',_gauge.cache_info(),flush=True)
        if len(out.ts)>20000:out=compact(out,cliff=True)
    out=compact(out,cliff=True)
    OUT.mkdir(exist_ok=True)
    pickle.dump(out,open(OUT/(slot+'-gauged.pkl'),'wb'))
    (OUT/(slot+'-ledger.json')).write_text(json.dumps(ledger,indent=2)+'\n')
    print('DONE',slot,len(out.ts),flush=True)
    return out

if __name__=='__main__':
    import sys
    for s in sys.argv[1:] or ['L','phi','N','E']:build(s)
