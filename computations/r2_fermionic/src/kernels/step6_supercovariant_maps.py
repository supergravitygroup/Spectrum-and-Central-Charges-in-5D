"""First-level primed substitutions only; preserve supercovariant operators.

Reuses ordered tensor bookkeeping, not the elementary component maps.
The derivative wrapper applies linearity, never a Leibniz or connection expansion.
"""
import json
from collections import Counter
from dataclasses import replace
import step6_elementary_algebra as alg
from step6_elementary_algebra import *

OPS={}
OP_KEYS={}
ODD={'psi','barpsi','vphi','barvphi','chi','barchi','phi','barphi','RQ','barRQ'}
BASE_ATOM_TEX=alg.atom_tex

def degree(f):
    return OPS[f.name]['degree'] if f.name in OPS else int(f.name in ODD)
alg.Atom.degree=property(degree)

def wrap(kind,p,a=None):
    """Keep each fully inserted monomial inside its differential operator."""
    out=Poly()
    for fs,c in poly(p).terms.items():
        cnt=Counter(n for f in fs for n,v in f.indices())
        free=[]
        for f in fs:
            for ix in f.indices():
                if cnt[ix[0]]==1:free.append(ix)
        mapping={};n={'a':0,'i':0}
        for name,v in free:
            k='i' if su((name,v)) else 'a';mapping[name]=k+'F'+str(n[k]);n[k]+=1
        n={'a':0,'i':0}
        for f in fs:
            for name,v in f.indices():
                if name not in mapping:
                    k='i' if su((name,v)) else 'a';mapping[name]=k+'B'+str(n[k]);n[k]+=1
        gs=tuple(f.rename(mapping) for f in fs)
        normfree=tuple((mapping[x],v) for x,v in free)
        # Numeric coefficients can be pulled through a linear operator;
        # L,N-dependent coefficients must stay inside it.
        outside,inside=s.expand(c).as_independent(L,N,as_Add=False)
        key=(kind,inside,gs,normfree)
        if key not in OP_KEYS:
            name='SC'+str(len(OPS))
            OP_KEYS[key]=name
            OPS[name]={'kind':kind,'coefficient':inside,'factors':gs,'free':normfree,
                       'degree':sum(f.degree for f in fs)}
        name=OP_KEYS[key]
        out+=Poly({(Atom(name,tuple(free),() if a is None else (a,)),):outside})
    return out

def SC(a,p):return wrap('D',p,a)
def box(p):return wrap('box',p)
def ch(i):return A('chi',i)
def bch(i):return A('barchi',i)
def T(a,b):return A('T',a,b)
def E(a):return A('E',a)
def Gh(a,b):return A('G',a,b)
def ph(a,i):return A('phi',a,i)
def T2():
    a,b=fresh(),fresh();return T(dn(a),dn(b))*T(up(a),up(b))
def slashT():
    a,b=fresh(),fresh();return ga(up(a),up(b))*T(dn(a),dn(b))
def slashE():
    a=fresh();return ga(up(a))*E(dn(a))
def slashD(p):
    a=fresh();return ga(up(a))*SC(dn(a),p)

def rho():
    i,j=fresh('i'),fresh('i')
    return poly(2*N/L)+I/L**3*lp(dn(i),dn(j))*bvf(up(i))*vf(up(j))

def lam(i):
    if i[1]>0:return raise_spin(lam,i)
    a=fresh();j,k=fresh('i'),fresh('i')
    return (-2*I/L*slashD(vf(i))+16/L*lp(i,dn(j))*ch(up(j))
      +4/L*slashT()*vf(i)-2*N/L**3*lp(i,dn(j))*vf(up(j))
      +2*I/L**3*ga(up(a))*SC(dn(a),lp(i,dn(j)))*lp(up(j),up(k))*vf(dn(k))
      -2*I/L**3*slashE()*lp(i,dn(j))*vf(up(j)))

def barone(p):
    """Operational transpose, including an unexpanded D on a spinor."""
    out=Poly()
    for fs,c in p.terms.items():
        assert sum(f.degree for f in fs)==1
        row=poly(c)
        for f in reversed(fs):
            if f.name in OPS and f.degree==1:
                op=OPS[f.name]
                # Reconstitute argument with this occurrence's free indices.
                arg=instantiate(f)
                q=barone(arg)
                row*=wrap(op['kind'],q,f.ds[0] if f.ds else None)
            elif f.name=='gam':
                row*=(-1)**(len(f.ix)*(len(f.ix)-1)//2)*Poly({(f,):1})
            elif f.name in ODD:
                name=f.name[3:] if f.name.startswith('bar') else 'bar'+f.name
                row*=Poly({(replace(f,name=name),):1})
            else:row*=Poly({(f,):1})
        out+=row
    return out

def instantiate(f):
    op=OPS[f.name];m={};var={}
    for (name,v),(new,w) in zip(op['free'],f.ix):m[name]=new;var[name]=v*w
    for h in op['factors']:
        for name,v in h.indices():
            if name not in m:m[name]=fresh('i' if su((name,v)) else 'a')
    def convert(h):
        def ix(x):return (m[x[0]],x[1]*var.get(x[0],1))
        return replace(h,ix=tuple(map(ix,h.ix)),ds=tuple(map(ix,h.ds)))
    return Poly({tuple(convert(h) for h in op['factors']):op['coefficient']})

def Y(i,j):
    if i[1]>0 or j[1]>0:return raise_pair(Y,i,j)
    a=fresh();k,m,l=[fresh('i') for _ in range(3)]
    z=box(lp(i,j))/L-lp(i,j)*(N*N+E(dn(a))*E(up(a)))/L**3
    z+=Q(8,3)/L*lp(i,j)*T2()+4/L*lp(i,j)*A('D')
    for x,y in [(i,j),(j,i)]:
        z-=lp(up(k),up(m))*SC(dn(a),lp(dn(k),x))*SC(up(a),lp(y,dn(m)))/(2*L**3)
        z+=E(dn(a))*lp(dn(k),x)*SC(up(a),lp(y,up(k)))/L**3
        z+=I*N/(2*L**3)*bvf(x)*vf(y)-bvf(x)*slashE()*vf(y)/(2*L**3)
        z-=8*I/L*bch(x)*vf(y)
        z+=lp(dn(k),x)*bvf(up(k))*slashD(vf(y))/L**3
        z-=Q(3,2)/L**5*lp(dn(k),x)*lp(up(l),up(m))*bvf(up(k))*ga(up(a))*SC(dn(a),lp(y,dn(l)))*vf(dn(m))
        z+=bvf(up(l))*ga(up(a))*SC(dn(a),lp(dn(l),x))*vf(y)/(4*L**3)
    z-=3*I*N/L**5*lp(i,j)*lp(up(k),up(l))*bvf(dn(k))*vf(dn(l))
    z+=3/L**5*lp(i,j)*lp(up(k),up(l))*bvf(dn(k))*slashE()*vf(dn(l))
    z+=16*I/L**3*lp(i,j)*lp(dn(k),dn(l))*bch(up(k))*vf(up(l))
    z+=bvf(up(m))*ga(up(a))*SC(dn(a),lp(i,j))*vf(dn(m))/(2*L**3)
    z+=2*I/L**3*lp(i,j)*bvf(up(k))*slashT()*vf(dn(k))
    return z

def Fh(a,b):
    i,j,k,l=[fresh('i') for _ in range(4)]
    z=2*SC(a,E(b)/L)-2*SC(b,E(a)/L)
    z+=2/L*A('RV',a,b,up(i),up(j))*lp(dn(i),dn(j))
    z-=lp(dn(i),up(j))*(SC(a,lp(up(i),up(k)))*SC(b,lp(dn(j),dn(k)))-SC(b,lp(up(i),up(k)))*SC(a,lp(dn(j),dn(k))))/L**3
    z-=SC(a,lp(dn(i),dn(j))*bvf(up(i))*ga(b)*vf(up(j))/L**3)
    z+=SC(b,lp(dn(i),dn(j))*bvf(up(i))*ga(a)*vf(up(j))/L**3)
    z-=I/L*bvf(up(i))*A('RQ',a,b,dn(i))
    return z

def Ap(a):
    i,j=fresh('i'),fresh('i')
    return 2/L*E(a)+s.sqrt(2)*A('V',a)-lp(dn(i),dn(j))*bvf(up(i))*ga(a)*vf(up(j))/L**3-I/L*bvf(up(i))*ps(a,dn(i))

def token(t):
    a,b,c,d,e='abcde';i,j='ij'
    if t==r"\rho'":return rho()
    if t==r"(\rho')^2":return rho()**2
    if t==r"Y'^{ij}":return Y(up(i),up(j))
    if t==r"Y'_{ij}":return Y(dn(i),dn(j))
    if t==r'L_{ij}':return lp(dn(i),dn(j))
    if t==r"\bar\lambda'^i":return barone(lam(up(i)))
    if t==r"\lambda'_i":return lam(dn(i))
    if t==r"\lambda'^j":return lam(up(j))
    if t==r'\chi_i':return ch(dn(i))
    if t==r'\bar\chi^i':return bch(up(i))
    if t==r"\not{\mathcal D}\lambda'_i":return slashD(lam(dn(i)))
    if t==r"A'_a":return Ap(dn(a))
    if t==r"(\mathcal D_b\rho')":return SC(dn(b),rho())
    if t==r"\Box_c\rho'":return box(rho())
    if t==r'f_a^a':return A('ftrace')
    if t==r'D':return A('D')
    if t==r'T^2':return T2()
    if t==r'T^{ab}':return T(up(a),up(b))
    if t==r'\gamma\cdot T':return slashT()
    if t==r'\gamma\cdot\widehat G':
        x,y=fresh(),fresh();return ga(up(x),up(y))*Gh(dn(x),dn(y))
    if t==r'\mathcal D_bT^{ab}':return SC(dn(b),T(up(a),up(b)))
    if t==r'\mathcal D_b\widehat G^{ab}':return SC(dn(b),Gh(up(a),up(b)))
    if t==r"\mathcal D_b\widehat F'^{ab}":return SC(dn(b),Fh(up(a),up(b)))
    if t in [r'\widehat G^{ab}',r'\widehat G_{ab}',r'\widehat G_{de}']:
        return Gh(up(a),up(b)) if '^' in t else Gh(dn(a),dn(b)) if t.endswith('{ab}') else Gh(dn(d),dn(e))
    if t in [r"\widehat F'_{ab}",r"\widehat F'_{bc}"]:return Fh(dn(a),dn(b)) if t.endswith('{ab}') else Fh(dn(b),dn(c))
    if t==r'\varepsilon^{abcde}':return eps(*map(up,'abcde'))
    if t.startswith(r'\gamma^'):return ga(*map(up,t.split('^',1)[1].strip('{}')))
    if t.startswith(r'\bar\psi_'):return bps(dn(t[len(r'\bar\psi_')]),up(i))
    if t.startswith(r'\phi_'):return ph(dn(t[len(r'\phi_{')]),dn(i))
    if t==r'\phi^a_i':return ph(up(a),dn(i))
    if t in [r'\psi^a_i',r'\psi^{aj}']:return ps(up(a),dn(i) if t.endswith('_i') else up(j))
    if t in [r'\psi_{ai}',r'\psi_{bi}',r'\psi_{ci}']:return ps(dn(t[len(r'\psi_{')]),dn(i))
    if t in [r'\psi_a^j',r'\psi_b^j',r'\psi_c^j']:return ps(dn(t[len(r'\psi_')]),up(j))
    raise ValueError(t)

def render_atom(f,ctx):
    if f.name=='ftrace':
        a=index_tex(('a'+str(ctx['a']),-1));ctx['a']+=1
        return 'f_{'+a+'}{}^{'+a+'}'
    if f.name in OPS:
        op=OPS[f.name];m={};vmap={}
        for (name,v),(new,w) in zip(op['free'],f.ix):m[name]=new;vmap[name]=v*w
        for h in op['factors']:
            for name,v in h.indices():
                if name not in m:
                    k='i' if su((name,v)) else 'a';m[name]=k+str(ctx[k]);ctx[k]+=1
        def convert(h):
            def ix(x):return (m[x[0]],x[1]*vmap.get(x[0],1))
            return replace(h,ix=tuple(map(ix,h.ix)),ds=tuple(map(ix,h.ds)))
        inner=render_term(op['coefficient'],tuple(convert(h) for h in op['factors']),ctx)
        prefix=r'\Box_c' if op['kind']=='box' else ''
        for a in f.ds:prefix+=r'\mathcal D'+('^' if a[1]>0 else '_')+'{'+index_tex(a)+'}'
        return prefix+r'\!\left('+inner+r'\right)'
    names={'G':r'\widehat G','RV':r'\widehat R(V)','RQ':r'\widehat R(Q)',
           'chi':r'\chi','barchi':r'\bar\chi','phi':r'\phi','barphi':r'\bar\phi','ftrace':r'f_a{}^a'}
    out=BASE_ATOM_TEX(replace(f,name=names.get(f.name,f.name)))
    return out.replace(r'\nabla',r'\mathcal D')

def render_term(c,fs,ctx=None):
    if ctx is None:
        ctx={'a':0,'i':0}
        for f in fs:
            for name,v in f.indices():
                k='i' if su((name,v)) else 'a';ctx[k]=max(ctx[k],int(name[1:])+1)
    cs='' if c==1 else '-' if c==-1 else s.latex(c)
    return (cs+' '+ ' '.join(render_atom(f,ctx) for f in fs)).strip()

def records(p):
    return [{'coefficient':str(c),'factors':[{'name':f.name,'ix':f.ix,'ds':f.ds} for f in fs],
             'degree':sum(f.degree for f in fs),'tex':render_term(c,fs)}
            for fs,coeff in p.terms.items() for c in s.expand(coeff).as_ordered_terms()]

def op_records():
    return {name:{**op,'coefficient':str(op['coefficient']),
        'factors':[{'name':f.name,'ix':f.ix,'ds':f.ds} for f in op['factors']]}
        for name,op in OPS.items()}
