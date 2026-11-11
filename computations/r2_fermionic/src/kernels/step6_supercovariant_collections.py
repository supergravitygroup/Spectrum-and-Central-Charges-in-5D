"""Index and inverse-product-rule collections of the retained-operator action.

Held sums and index symmetrizations are presentation nodes, not new fields.
Every node carries its indexed polynomial expansion for independent checks.
The original insertion engine and its ledger remain the expansion baseline.
"""
from pathlib import Path
from collections import Counter
import json, hashlib
import step6_supercovariant_maps as sc
from step6_supercovariant_maps import *
import build_step5a_partial_insertion as source

ROOT=Path(__file__).resolve().parents[1]
HELD={}; KEYS={}; RAW_GROUPS=[]
original_degree=sc.degree
original_render=sc.render_atom
original_lam=sc.lam
original_Y=sc.Y
original_Fh=sc.Fh
original_bar=sc.barone

def free_indices(p):
    signatures=[]
    for fs,c in p.terms.items():
        count=Counter(n for f in fs for n,v in f.indices())
        signatures.append(tuple(x for f in fs for x in f.indices() if count[x[0]]==1))
    assert signatures and all(set(x)==set(signatures[0]) for x in signatures),signatures
    return signatures[0]

def hold(p,kind='sum',pair=()):
    p=poly(p); free=free_indices(p)
    deg={sum(f.degree for f in fs) for fs in p.terms}
    assert len(deg)==1,deg
    mapping={n:('i' if su((n,v)) else 'a')+'F'+str(k) for k,(n,v) in enumerate(free)}
    norm=[]
    for fs,c in p.terms.items():
        m=dict(mapping);serials={'a':0,'i':0}
        for f in fs:
            for n,v in f.indices():
                if n not in m:
                    k='i' if su((n,v)) else 'a';m[n]=k+'B'+str(serials[k]);serials[k]+=1
        norm.append((tuple(f.rename(m) for f in fs),c))
    pp=Poly(dict(norm)); nf=tuple((mapping[n],v) for n,v in free)
    np=tuple(mapping[n] for n in pair)
    key=(kind,tuple(norm),nf,np)
    if key not in KEYS:
        name='HC'+str(len(HELD));KEYS[key]=name
        HELD[name]={'kind':kind,'p':pp,'free':nf,'pair':np,'degree':deg.pop(),
                    'ordered':any(f.ordered for fs in pp.terms for f in fs)}
    return A(KEYS[key],*free)

def symmetry(p,i,j,anti=False):
    return hold(p,'anti' if anti else 'sym',(i[0],j[0]))

def degree(f):return HELD[f.name]['degree'] if f.name in HELD else original_degree(f)
alg.Atom.degree=property(degree)
alg.Atom.ordered=property(lambda f: HELD[f.name]['ordered'] if f.name in HELD else bool(f.degree or f.name=='gam'))
original_gamma_reduction=alg.reduce_gamma_contractions
def protected_gamma_reduction(fs,c):
    # A held N+i slash(E) matrix is an ordering barrier even at degree zero.
    # Clifford contractions must never jump across it.
    result=[];segment=[]
    for f in fs:
        if f.name in HELD and HELD[f.name]['ordered']:
            part,c=original_gamma_reduction(segment,c);result.extend(part);result.append(f);segment=[]
        else:segment.append(f)
    part,c=original_gamma_reduction(segment,c);result.extend(part)
    return result,c
alg.reduce_gamma_contractions=protected_gamma_reduction

def held_argument(f,ctx=None):
    h=HELD[f.name];m={};variance={}
    for (n,v),(new,w) in zip(h['free'],f.ix):m[n]=new;variance[n]=v*w
    # Internal indices are always fresh, also across nested nodes.
    for fs in h['p'].terms:
        for a in fs:
            for n,v in a.indices():
                if n not in m:
                    k='i' if su((n,v)) else 'a'
                    if ctx is None:m[n]=fresh(k)
                    else:m[n]=k+str(ctx[k]);ctx[k]+=1
    def cv(a):
        def ix(x):return m[x[0]],x[1]*variance.get(x[0],1)
        return replace(a,ix=tuple(map(ix,a.ix)),ds=tuple(map(ix,a.ds)))
    return Poly({tuple(cv(a) for a in fs):c for fs,c in h['p'].terms.items()}),tuple(m[n] for n in h['pair'])

def expanded(p):
    out=Poly()
    for fs,c in p.terms.items():
        row=poly(c)
        for f in fs:
            if f.name in HELD:
                arg,pair=held_argument(f);h=HELD[f.name]
                if pair:
                    vars={n:v for n,v in f.ix};m={pair[0]:pair[1],pair[1]:pair[0]}
                    def swap(a):
                        def ix(x):
                            n,v=x
                            return (m[n],v*vars[m[n]]*vars[n]) if n in m else x
                        return replace(a,ix=tuple(map(ix,a.ix)),ds=tuple(map(ix,a.ds)))
                    swapped=Poly({tuple(swap(a) for a in gs):b for gs,b in arg.terms.items()})
                    arg=(arg+(-swapped if h['kind']=='anti' else swapped))/2
                row*=expanded(arg)
            elif f.name in OPS:
                arg=expanded(sc.instantiate(f));op=OPS[f.name]
                row*=sc.wrap(op['kind'],arg,f.ds[0] if f.ds else None)
            else:row*=Poly({(f,):1})
        out+=row
    return out

def render_atom(f,ctx):
    if f.name not in HELD:return original_render(f,ctx)
    h=HELD[f.name]
    if h['pair']:
        slots=[next(k for k,(n,v) in enumerate(h['free']) if n==p) for p in h['pair']]
        first,second=[f.ix[k] for k in slots]
        if first[1]!=second[1]:
            # SU(2) symmetrization is defined before raising. Do not print
            # misleading parentheses between one upper and one lower index.
            k='i' if su(first) else 'a'
            new=(k+str(ctx[k]),first[1]);ctx[k]+=1
            ix=list(f.ix);ix[slots[1]]=new
            ep=(second,flip(new)) if second[1]>0 else (flip(new),second)
            return original_render(Atom('eps2' if k=='i' else 'eta',ep),ctx)+render_atom(replace(f,ix=tuple(ix)),ctx)
    arg,pair=held_argument(f,ctx);h=HELD[f.name]
    terms=[sc.render_term(c,fs,ctx) for fs,c in arg.terms.items()]
    text=' '.join(t if k==0 or t.startswith('-') else '+'+t for k,t in enumerate(terms))
    if pair:
        # Each symmetrized free index occurs once in the single base monomial.
        # Mark its actual occurrence; other indices between them are excluded.
        labels=[sc.index_tex((n,1)) for n in pair]
        # Render free indices as unique tokens on a second pass, so matching is
        # independent of TeX command spelling and of the chosen dummy alphabet.
        old1=sc.index_tex;old2=alg.index_tex
        tokens={n:'ZZINDEX'+str(k)+'ZZ' for k,n in enumerate(pair)}
        def ix(x):return tokens.get(x[0],old1(x))
        sc.index_tex=alg.index_tex=ix
        try:marked=' '.join(sc.render_term(c,fs,dict(ctx)) for fs,c in arg.terms.items())
        finally:sc.index_tex=old1;alg.index_tex=old2
        order=sorted(range(2),key=lambda k:marked.index(tokens[pair[k]]))
        opening,closing=('[' ,']') if h['kind']=='anti' else ('(',')')
        for k in order:
            marked=marked.replace(tokens[pair[k]],(opening if k==order[0] else '')+labels[k]+(closing if k==order[1] else ''))
        text=marked
    return r'\left('+text+r'\right)'

sc.render_atom=render_atom

def transpose(p):
    """Operational transpose on matrices and one-spinor words, preserving i."""
    out=Poly()
    for fs,c in p.terms.items():
        row=poly(c)
        for f in reversed(fs):
            if f.name in HELD:
                arg,pair=held_argument(f);h=HELD[f.name]
                row*=hold(transpose(arg),h['kind'],pair)
            elif f.name in OPS:
                row*=sc.wrap(OPS[f.name]['kind'],transpose(sc.instantiate(f)),f.ds[0] if f.ds else None)
            elif f.name=='gam':row*=(-1)**(len(f.ix)*(len(f.ix)-1)//2)*Poly({(f,):1})
            elif f.name in ODD:row*=A(f.name[3:] if f.name.startswith('bar') else 'bar'+f.name,*f.ix)
            else:row*=Poly({(f,):1})
        out+=row
    return out

def lam(i):
    if i[1]>0:return raise_spin(lam,i)
    a=fresh();j,k=fresh('i'),fresh('i')
    return (-2*I/L*slashD(vf(i))+16/L*lp(i,dn(j))*ch(up(j))+4/L*slashT()*vf(i)
       -2/L**3*lp(i,dn(j))*hold(N+I*slashE())*vf(up(j))
       +2*I/L**3*ga(up(a))*SC(dn(a),lp(i,dn(j)))*lp(up(j),up(k))*vf(dn(k)))

def Y(i,j):
    if i[1]>0 or j[1]>0:return raise_pair(Y,i,j)
    a=fresh();k,l,m,n=[fresh('i') for _ in range(4)]
    z=box(lp(i,j))/L-SC(dn(a),poly(L))*SC(up(a),lp(i,j))/L**2
    trace=4*A('D')+Q(8,3)*T2()-(N*N+E(dn(a))*E(up(a)))/L**2
    trace+=SC(dn(a),lp(dn(k),dn(l)))*SC(up(a),lp(up(k),up(l)))/(2*L**2)
    z+=lp(i,j)*hold(trace)/L
    spinor_matrix=hold(I*N-slashE())
    z+=symmetry(bvf(i)*spinor_matrix*vf(j),i,j)/L**3
    z-=3/L**5*lp(i,j)*lp(up(k),up(l))*bvf(dn(k))*spinor_matrix*vf(dn(l))
    transport=symmetry(lp(dn(k),i)*SC(up(a),lp(j,up(k))),i,j)
    z+=2/L**3*transport*E(dn(a))
    z-=3/L**5*transport*lp(up(m),up(n))*bvf(dn(m))*ga(dn(a))*vf(dn(n))
    z-=16*I/L*symmetry(bch(i)*vf(j),i,j)
    z+=16*I/L**3*lp(i,j)*lp(up(k),up(l))*bch(dn(k))*vf(dn(l))
    z+=2/L**3*symmetry(lp(dn(k),i)*bvf(up(k))*slashD(vf(j)),i,j)
    z-=symmetry(bvf(up(k))*ga(up(a))*SC(dn(a),lp(dn(k),i))*vf(j),i,j)/L**3
    z+=2*I/L**3*lp(i,j)*bvf(up(k))*slashT()*vf(dn(k))
    return z

def Fh(a,b):
    i,j,k,l=[fresh('i') for _ in range(4)]
    z=4*symmetry(SC(a,E(b)/L),a,b,True)+2/L*lp(dn(i),dn(j))*A('RV',a,b,up(i),up(j))
    z-=2/L**3*lp(dn(i),up(j))*symmetry(SC(a,lp(up(i),up(k)))*SC(b,lp(dn(j),dn(k))),a,b,True)
    z-=2*symmetry(SC(a,lp(dn(i),dn(j))*bvf(up(i))*ga(b)*vf(up(j))/L**3),a,b,True)
    z-=I/L*bvf(up(i))*A('RQ',a,b,dn(i))
    return z

def group_derivative():
    # Split polynomial degree only internally to discard degree four before
    # display. No projected field is introduced into any equation.
    a,b='a','b';arg=Fh(up(a),up(b))+rho()*hold(Gh(up(a),up(b))-16*T(up(a),up(b)))
    grouped=Poly()
    for d in (0,2):
        part=Poly({fs:c for fs,c in arg.terms.items() if sum(f.degree for f in fs)==d})
        grouped+=SC(dn(b),hold(part))
    return -Q(1,2)*Ap(dn(a))*grouped

def build():
    # Deterministic output even if an identity check registered nodes first.
    HELD.clear();KEYS.clear();OPS.clear();OP_KEYS.clear()
    alg.canonical_word.cache_clear();alg.serial=0
    RAW_GROUPS.clear()
    sc.lam=lam;sc.Y=Y;sc.Fh=Fh;sc.barone=transpose
    groups=[];total=Poly();merged={11:[11,12,13,14,15],28:[28,30],5:[5,33],39:[39,40]}
    skip={12,13,14,15,30,33,40}
    for number,raw,terms in source.source_rows():
        if number in skip:continue
        if number==11:p=group_derivative()
        elif number==28:p=-rho()*Fh(dn('a'),dn('b'))*hold(Gh(up('a'),up('b'))-16*T(up('a'),up('b')))/4
        else:
            p=Poly()
            for row in terms:
                q=poly(row.c*(2 if number==5 else 1))
                factors=list(row.fs)
                if number==39:
                    # Replace gamma^a gamma^b by gamma^{ab}; group 40 removes
                    # exactly the metric part, including the gauge restriction.
                    ga1=next(k for k,f in enumerate(factors) if f.tex==r'\gamma^a')
                    assert factors[ga1+1].tex==r'\gamma^b'
                    factors[ga1:ga1+2]=[source.F(r'\gamma^{ab}')]
                for f in factors:q*=sc.token(f.tex)
                p+=q
        assert not index_errors(p),(number,index_errors(p)[:2])
        q=canonical(p);total+=q
        RAW_GROUPS.append((number,p,q))
        groups.append({'sources':merged.get(number,[number]),'rows':sc.records(q),'raw_terms':len(p)})
        print('Collected',groups[-1]['sources'],len(q),flush=True)
    total=canonical(total)
    rows=sc.records(total)
    result={'lock':'R2-PRIMED-SUPERCOVARIANT-COLLECTED-EXPLICIT2-v2',
            'groups':groups,'rows':rows,'terms':len(rows),'degrees':dict(Counter(r['degree'] for r in rows)),
            'source_sha256':hashlib.sha256(source.old.DOC.read_bytes()).hexdigest(),
            'map_sha256':hashlib.sha256((ROOT/'notes/08_step5_primed_composite_vector_insertion.md').read_bytes()).hexdigest(),
            'prior_step6_sha256':hashlib.sha256((ROOT/'notes/10_step6_gauged_action_through_two_fermions.md').read_bytes()).hexdigest()}
    (ROOT/'build/step6_supercovariant_collected_ledger.json').write_text(json.dumps(result,indent=2)+'\n')
    print('FINAL',result['terms'],result['degrees'])
    return result,total

if __name__=='__main__':build()
