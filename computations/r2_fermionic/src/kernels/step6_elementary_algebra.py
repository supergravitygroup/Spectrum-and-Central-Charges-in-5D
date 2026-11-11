"""Ordered tensor polynomials for the explicit Step-6 substitutions.

Derivatives are even and retain their order. No field equation, integration
by parts, spinor flip or Fierz identity is part of this engine.
"""
from dataclasses import dataclass, replace
from collections import Counter, defaultdict
from itertools import permutations
from functools import lru_cache
import sympy as s

I=s.I; Q=s.Rational
L,N,g=s.symbols('L N g',real=True)
serial=0
def fresh(kind='a'):
    global serial
    serial+=1
    return f'{kind}{serial}'
def up(a):return (a,1)
def dn(a):return (a,-1)
def flip(a):return (a[0],-a[1])
def su(a):return a[0][0] in 'ijklmno'

@dataclass(frozen=True)
class Atom:
    name:str
    ix:tuple=()
    ds:tuple=()
    @property
    def degree(self):return int(self.name in ('psi','barpsi','vphi','barvphi'))
    @property
    def ordered(self):return self.degree or self.name=='gam'
    def indices(self):return self.ds+self.ix
    def rename(self,m):return replace(self,ix=tuple((m.get(a,a),v) for a,v in self.ix),ds=tuple((m.get(a,a),v) for a,v in self.ds))

class Poly:
    def __init__(self,terms=None):self.terms=terms or {}
    def __add__(self,other):
        other=poly(other);d=dict(self.terms)
        for fs,c in other.terms.items():d[fs]=d.get(fs,0)+c
        return Poly({f:s.expand(c) for f,c in d.items() if c!=0})
    __radd__=__add__
    def __neg__(self):return Poly({f:-c for f,c in self.terms.items()})
    def __sub__(self,other):return self+-poly(other)
    def __rsub__(self,other):return poly(other)+-self
    def __mul__(self,other):
        other=poly(other);d=defaultdict(lambda:0)
        for fs,c in self.terms.items():
            names={a for f in fs for a,v in f.indices()}
            deg=sum(f.degree for f in fs)
            for gs,e in other.terms.items():
                if deg+sum(f.degree for f in gs)>2:continue
                cnt=Counter(a for f in gs for a,v in f.indices())
                m={a:fresh('i' if a[0] in 'ijklmno' else 'a') for a,n in cnt.items() if n==2 and a in names}
                hh=fs+tuple(f.rename(m) for f in gs) if m else fs+gs
                d[hh]+=c*e
        return Poly({f:s.expand(c) for f,c in d.items() if c!=0})
    __rmul__=__mul__
    def __truediv__(self,n):return self*(1/s.sympify(n))
    def __pow__(self,n):
        assert n>=0 and isinstance(n,int)
        r=poly(1)
        for _ in range(n):r=r*self
        return r
    def __len__(self):return len(self.terms)

def poly(x):return x if isinstance(x,Poly) else Poly({():s.sympify(x)}) if x else Poly()
def A(name,*ix):return Poly({(Atom(name,tuple(ix)),):s.Integer(1)})
def ga(*ix):return A('gam',*ix)
def eps(*ix):return A('eps2' if len(ix)==2 else 'eps5',*ix)
def lp(i,j):return A('Lt',i,j)
def vf(i):return A('vphi',i)
def ps(a,i):return A('psi',a,i)
def bps(a,i):return A('barpsi',a,i)
def bvf(i):return A('barvphi',i)
def field(name,*ix):return A(name,*ix)
def D(a,p):
    p=poly(p);out=Poly()
    for fs,c in p.terms.items():
        for v in (L,N):
            dc=s.diff(c,v)
            if dc:out+=Poly({(Atom(str(v),(),(a,)),)+fs:dc})
        for k,f in enumerate(fs):
            if f.name in ('gam','eps2','eps5','eta','delta'):continue
            out+=Poly({fs[:k]+(replace(f,ds=(a,)+f.ds),)+fs[k+1:]:c})
    return out
def bar(p):
    out={}
    for fs,c in p.terms.items():
        assert sum(f.degree for f in fs)==1
        new=[]
        for f in reversed(fs):
            if f.name=='gam':c*=(-1)**(len(f.ix)*(len(f.ix)-1)//2)
            if f.name in ('psi','vphi'):f=replace(f,name='bar'+f.name)
            elif f.name in ('barpsi','barvphi'):f=replace(f,name=f.name[3:])
            new.append(f)
        out[tuple(new)]=out.get(tuple(new),0)+c
    return Poly(out)
def raise_spin(fn,i):
    if i[1]<0:return fn(i)
    j=fresh('i');return eps(i,up(j))*fn(dn(j))
def raise_pair(fn,i,j):
    if i[1]<0 and j[1]<0:return fn(i,j)
    k,l=fresh('i'),fresh('i')
    if i[1]>0:return eps(i,up(k))*raise_pair(fn,dn(k),j)
    return eps(j,up(l))*raise_pair(fn,i,dn(l))
def low_pair_from_upper(fn,i,j):
    if i[1]>0 and j[1]>0:return fn(i,j)
    k=fresh('i')
    if i[1]<0:return eps(up(k) if False else dn(k),i)*low_pair_from_upper(fn,up(k),j)
    return eps(dn(k),j)*low_pair_from_upper(fn,i,up(k))

def index_errors(p):
    errors=[]
    for n,(fs,c) in enumerate(p.terms.items()):
        ids=defaultdict(list)
        for f in fs:
            for a,v in f.indices():ids[a].append(v)
        bad={a:vs for a,vs in ids.items() if len(vs)!=2 or sum(vs)!=0}
        if bad:errors.append((n,bad))
    return errors

def _canonical_pass(p):
    """Collect after renaming dummy indices; commute only even scalar atoms.

    Spinor and gamma words remain in their original order. Tensor slot
    symmetries are applied only for G, H, L and the epsilon tensors.
    """
    out=defaultdict(lambda:0)
    for fs,c in p.terms.items():
        fs,c=reduce_su2(list(fs),c)
        fs,c=reduce_gamma_contractions(fs,c)
        if not c:continue
        ordered=[f for f in fs if f.ordered]
        bos=[f for f in fs if not f.ordered]
        # Name dummy indices first along the unaltered spinor/gamma word.
        mapping={};counts={'a':0,'i':0}
        def rename(f):
            for a,v in f.indices():
                if a not in mapping:
                    k='i' if a[0] in 'ijklmno' else 'a';mapping[a]=k+str(counts[k]);counts[k]+=1
            return f.rename(mapping)
        oo=[rename(f) for f in ordered]
        # Prefer bosonic factors joined to already fixed indices. Ties use
        # their original order; this conservative collector never equates
        # different contraction graphs.
        bb=[]
        while bos:
            def rank(f):
                return (f.name,len(f.ds),len(f.ix),tuple((mapping.get(a,'~'),v) for a,v in f.indices()))
            k=min(range(len(bos)),key=lambda k:rank(bos[k]));bb.append(rename(bos.pop(k)))
        combined=bb+oo
        # Normalize which member of each contracted pair carries the upper
        # index. Lorentz metric transfer has sign +; NW--SE symplectic
        # transfer has sign -. Keep mixed tensor slot order in the renderer.
        first={}
        for f in oo+bb:
            for n,(a,v) in enumerate(f.indices()):
                if a in first:continue
                desired=1 if ((a[0]=='i' and f.name.startswith('bar')) or (a[0]=='a' and f.name=='gam')) else -1
                first[a]=(v,desired)
        switched={a for a,(v,w) in first.items() if v!=w}
        c*=(-1)**sum(a[0]=='i' for a in switched)
        combined=[replace(f,ix=tuple((a,-v if a in switched else v) for a,v in f.ix),
                          ds=tuple((a,-v if a in switched else v) for a,v in f.ds)) for f in combined]
        signed=[]
        for f in combined:
            ix=list(f.ix)
            anti=f.name in ('G','H','E3','eps2','eps5') or (f.name=='gam' and len(ix)>1)
            sym=f.name=='Lt'
            if anti and len(set(a for a,v in ix))<len(ix):c=0;break
            if anti or sym:
                perm=sorted(range(len(ix)),key=lambda k:ix[k])
                if anti:c*=(-1)**sum(perm[x]>perm[y] for x in range(len(perm)) for y in range(x+1,len(perm)))
                f=replace(f,ix=tuple(ix[k] for k in perm))
            signed.append(f)
        if c:out[tuple(signed)]+=c
    return Poly({fs:s.factor(c) for fs,c in out.items() if s.expand(c)!=0})

@lru_cache(maxsize=100000)
def canonical_word(fs):
    """Choose one stable representative of the dummy-renaming orbit."""
    seen={};history=[];c=s.Integer(1)
    for _ in range(80):
        if fs in seen:
            start=seen[fs]
            if s.simplify(c-history[start][1])!=0:return (),s.Integer(0)
            return min(history[start:],key=lambda item:repr(item[0]))
        seen[fs]=len(history);history.append((fs,c))
        q=_canonical_pass(Poly({fs:c}))
        if not q.terms:return (),s.Integer(0)
        (fs,c),=q.terms.items()
    raise ValueError('Dummy-index normalization did not close')

def canonical(p):
    out=defaultdict(lambda:0)
    for fs,c in p.terms.items():
        gs,factor=canonical_word(fs)
        if factor:out[gs]+=c*factor
    return Poly({fs:s.factor(c) for fs,c in out.items() if s.expand(c)!=0})

def reduce_su2(fs,c):
    """Apply only explicit NW--SE epsilon and triplet norm identities."""
    changed=True
    while changed and c:
        changed=False
        for k,f in enumerate(fs):
            if f.name=='Lt' and len(f.ix)==2 and f.ix[0][0]==f.ix[1][0]:
                return [],0  # symmetric triplet contracted with epsilon
            if f.name=='eps2' and f.ix[0][1]!=f.ix[1][1]:
                # epsilon^i_j=-delta^i_j, epsilon_i^j=+delta_i^j.
                c*=-f.ix[0][1];fs[k]=replace(f,name='delta');changed=True;break
            if f.name not in ('eps2','delta') or f.ds:continue
            if f.ix[0][0]==f.ix[1][0]:
                if f.name=='eps2':return [],0
                c*=2;fs.pop(k);changed=True;break
            for u,(name,v) in enumerate(f.ix):
                found=False
                for l,h in enumerate(fs):
                    if l==k:continue
                    slots=list(h.ix)
                    positions=[z for z,ix in enumerate(slots) if ix==(name,-v)]
                    if not positions:continue
                    other=f.ix[1-u]
                    if f.name=='eps2':c*=v*(2*u-1)
                    slots[positions[0]]=other
                    fs[l]=replace(h,ix=tuple(slots));fs.pop(k)
                    changed=found=True;break
                if found:break
            if changed:break
        if changed:continue
        # L_ij L^jk = L^2 delta_i^k/2, for undifferentiated
        # symmetric triplets. Differentiate the fields before using this rule.
        for k,f in enumerate(fs):
            if f.name!='Lt' or f.ds or len({v for a,v in f.ix})!=1:continue
            for l in range(k+1,len(fs)):
                h=fs[l]
                if h.name!='Lt' or h.ds or len({v for a,v in h.ix})!=1 or f.ix[0][1]==h.ix[0][1]:continue
                pairs=[(x,y) for x,ix in enumerate(f.ix) for y,jx in enumerate(h.ix) if ix==flip(jx)]
                if not pairs:continue
                x,y=pairs[0];c*=L**2/2
                fs[k]=Atom('delta',(f.ix[1-x],h.ix[1-y]));fs.pop(l);changed=True;break
            if changed:break
    return fs,c

def reduce_gamma_contractions(fs,c):
    """Contract closed Clifford index pairs, in d=5, without spinor flips."""
    changed=True
    while changed:
        changed=False
        pos=[k for k,f in enumerate(fs) if f.name=='gam']
        occurrences=Counter(a for f in fs for a,v in f.indices())
        for p in range(len(pos)-1):
            k,l=pos[p:p+2];f,h=fs[k],fs[l]
            if any(x.degree for x in fs[k+1:l]):continue
            if len(f.ix)==len(h.ix) and set(f.ix)==set(flip(z) for z in h.ix):
                n=len(f.ix)
                perm=[f.ix.index(flip(x)) for x in h.ix]
                sign=(-1)**(n*(n-1)//2+sum(perm[a]>perm[b] for a in range(n) for b in range(a+1,n)))
                c*=sign*s.factorial(5)/s.factorial(5-n)
                fs.pop(l);fs.pop(k);changed=True;break
            if len(f.ix)==1 and flip(f.ix[0]) in h.ix:
                q=h.ix.index(flip(f.ix[0]));c*=(-1)**q*(6-len(h.ix))
                fs[l]=replace(h,ix=h.ix[:q]+h.ix[q+1:]);fs.pop(k);changed=True;break
            if len(h.ix)==1 and flip(h.ix[0]) in f.ix:
                q=f.ix.index(flip(h.ix[0]));c*=(-1)**(len(f.ix)-1-q)*(6-len(f.ix))
                fs[k]=replace(f,ix=f.ix[:q]+f.ix[q+1:]);fs.pop(l);changed=True;break
            if p+2<len(pos):
                m=pos[p+2];last=fs[m]
                if len(f.ix)==len(last.ix)==1 and f.ix[0]==flip(last.ix[0]) and all(a!=f.ix[0][0] for a,v in h.ix):
                    if any(x.degree for x in fs[l+1:m]):continue
                    c*=(-1)**len(h.ix)*(5-2*len(h.ix));fs.pop(m);fs.pop(k);changed=True;break
        fs=[f for f in fs if not (f.name=='gam' and not f.ix)]
    return fs,c

def index_tex(a):
    name,v=a;k='i' if name[0] in 'ijklmno' else 'a';n=int(name[1:])
    letters='ijklmnouvwxyz' if k=='i' else 'abcdefghpqrstuvwxy'
    return letters[n] if n<len(letters) else letters[n%len(letters)]+'_{'+str(n//len(letters))+'}'
def atom_tex(f):
    names={'Lt':'L','vphi':r'\varphi','barvphi':r'\bar\varphi','psi':r'\psi','barpsi':r'\bar\psi','gam':r'\gamma','eps2':r'\varepsilon','eps5':r'\varepsilon','E3':'E','V':'V','eta':r'\eta','delta':r'\delta'}
    root=names.get(f.name,f.name)
    groups=[]
    for ix in f.ix:
        if groups and groups[-1][0]==ix[1]:groups[-1][1].append(ix)
        else:groups.append((ix[1],[ix]))
    for k,(variance,indices) in enumerate(groups):
        root+=('{}' if k else '')+('^' if variance>0 else '_')+'{'+''.join(index_tex(x) for x in indices)+'}'
    for d in reversed(f.ds):root=(r'\nabla' + ('^' if d[1]>0 else '_')+'{'+index_tex(d)+'}')+root
    return '('+root+')' if f.ds else root
def term_tex(c,fs):
    cs=s.latex(c).replace('i',r'i')
    if c==1:cs=''
    elif c==-1:cs='-'
    factors=[];used=set()
    for k,f in enumerate(fs):
        if k in used:continue
        if not f.ordered and not f.ix and not f.ds:
            equal=[j for j,h in enumerate(fs) if h==f];used.update(equal)
            factors.append(atom_tex(f)+('^{'+str(len(equal))+'}' if len(equal)>1 else ''))
        else:factors.append(atom_tex(f))
    return (cs+' '+ ' '.join(factors)).strip()
def json_terms(p,expand_coefficients=False):
    return [{'coefficient':str(piece),'factors':[{'name':f.name,'indices':f.ix,'derivatives':f.ds} for f in fs],
             'degree':sum(f.degree for f in fs),'tex':term_tex(piece,fs)}
            for fs,c in p.terms.items() for piece in (s.expand(c).as_ordered_terms() if expand_coefficients else [c])]
