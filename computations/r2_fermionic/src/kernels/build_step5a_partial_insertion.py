#!/usr/bin/env python3
"""Explicit ordered polynomial substitution. Formal covariant-slot grading only."""
from pathlib import Path
import sys,re,json,hashlib,itertools
from dataclasses import dataclass
import sympy as S
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'scripts'))
import verify_step4_gold_gauge as old
I=S.I;L,N,g=S.symbols('L N g',real=True);Q=S.Rational
@dataclass(frozen=True)
class F:
    tex:str
    degree:int=0
@dataclass(frozen=True)
class M:
    c:object
    fs:tuple=()
    @property
    def degree(self):return sum(x.degree for x in self.fs)
def atom(t,d=0):return F(t,d)
def mon(c,*fs):return M(S.sympify(c),tuple(fs))
def mul(xs,ys):return [M(S.expand(x.c*y.c),x.fs+y.fs) for x in xs for y in ys]
def texfix(t):
    return t.replace(r'\cdotT',r'\cdot T').replace(r'\mathcalD',r'\mathcal D').replace(r'\widehatG',r'\widehat G').replace(r'\widehatF',r'\widehat F').replace(r'\notE',r'\not E').replace(r'\not\mathcalD',r'\not\mathcal D')
def parse_product(s):
    out=[mon(1)]
    if s.startswith(('+','-')):out=[mon(-1 if s[0]=='-' else 1)];s=s[1:]
    while s:
        if s.startswith(r'\frac'):
            nu,s=old.argument(s[5:]);de,s=old.argument(s)
            out=mul(out,[M(x.c/Q(de),x.fs) for x in parse_product(nu)]);continue
        if s[0]=='[':
            depth=1
            for k in range(1,len(s)):
                depth+=(s[k]=='[')-(s[k]==']')
                if not depth:break
            out=mul(out,parse_sum(s[1:k]));s=s[k+1:];continue
        for t in sorted(old.tokens,key=len,reverse=True):
            if s.startswith(t):
                w=old.tokens[t];d=sum(old.prior.meta.get(z,(0,0))[1] for z in w)
                if 'ps' in w or 'phi' in w:d=max(d,1)
                out=mul(out,[mon(1,atom(texfix(t),d))]);s=s[len(t):];break
        else:
            if s[0].isdigit():
                m=re.match(r'\d+',s);out=mul(out,[mon(int(m[0]))]);s=s[len(m[0]):]
            elif s[0]=='i':out=mul(out,[mon(I)]);s=s[1:]
            elif s[0]=='g':out=mul(out,[mon(g)]);s=s[1:]
            elif s[0] in '().':s=s[1:]
            else:raise ValueError(s)
    return out
def parse_sum(s):return [x for t in old.top_terms(old.prior.clean(s)) for x in parse_product(t)]
def idx(k):return '{'+k+'}'
def rho(k):
    a,b='r_'+str(k),'s_'+str(k)
    return [mon(2*N/L),mon(I/L**3,atom('L_{'+a+b+'}'),atom(r'\bar\varphi^{'+a+'}',1),atom(r'\varphi^{'+b+'}',1))]
def lam(i,k,bar=False):
    j,r,s,a=[v+'_{'+str(k)+'}' for v in ('j','k','l','d')]
    li=atom('L_{'+i+j+'}');lu=atom('L^{'+j+r+'}')
    ph=lambda ix,up=False:atom(r'\varphi'+('^' if up else '_')+'{'+ix+'}',1)
    bp=lambda ix,up=False:atom(r'\bar\varphi'+('^' if up else '_')+'{'+ix+'}',1)
    ga=atom(r'\gamma^{'+a+'}')
    dt=atom(r'\gamma\!\cdot\!T')
    dl=atom(r'(\not{\mathcal D}L_{'+i+j+'})')
    es=atom(r'\not E')
    if not bar:
        return [mon(-2*I/L,atom(r'\not{\mathcal D}\varphi_{'+i+'}',1)),
          mon(16/L,li,atom(r'\chi^{'+j+'}',1)),mon(4/L,dt,ph(i)),
          mon(-2*N/L**3,li,ph(j,True)),mon(2*I/L**3,dl,lu,ph(r)),
          mon(-2*I/L**3,es,li,ph(j,True)),
          mon(2*I/L**3,ph(j,True),bp(i),ph(j)),
          mon(-6*I/L**5,ph(j,True),bp(r),ph(s),atom('L^{'+r+s+'}'),li)]
    return [mon(-2*I/L,atom(r'(\mathcal D_{'+a+r'}\bar\varphi_{'+i+'})',1),ga),
      mon(16/L,li,atom(r'\bar\chi^{'+j+'}',1)),mon(-4/L,bp(i),dt),
      mon(-2*N/L**3,li,bp(j,True)),mon(2*I/L**3,lu,bp(r),dl),
      mon(-2*I/L**3,li,bp(j,True),es),
      mon(2*I/L**3,bp(j,True),bp(i),ph(j)),
      mon(-6*I/L**5,bp(j,True),bp(r),ph(s),atom('L^{'+r+s+'}'),li)]
def derivative(xs,a):
    out=[]
    for x in xs:
        for v in [L,N]:
            c=S.diff(x.c,v)
            if c:out.append(mon(c,atom(r'(\mathcal D_{'+a+'}'+str(v)+')'),*x.fs))
        for k,f in enumerate(x.fs):
            if f.tex.startswith(r'\gamma'):continue
            # Gamma-dot T is differentiated, whereas constant gamma matrices are not.
            out.append(mon(x.c,*x.fs[:k],atom(r'\mathcal D_{'+a+r'}\!\left('+f.tex+r'\right)',f.degree),*x.fs[k+1:]))
    return out
# Correct differentiation of gamma-dot T and slash E explicitly.
def d_full(xs,a):
    out=derivative(xs,a)
    for x in xs:
        for k,f in enumerate(x.fs):
            if f.tex==r'\gamma\!\cdot\!T':
                out.append(mon(x.c,*x.fs[:k],atom(r'\gamma^{mn}(\mathcal D_{'+a+'}T_{mn})'),*x.fs[k+1:]))
    return out
counter=0
def replacement(t):
    global counter
    counter+=1;k=counter
    if t==r"(\rho')^2":
        rr=rho(k);a=rr[1]
        # Use different contracted indices for the second scalar bilinear.
        b=rho(k+10000)[1]
        return [mon(4*N**2/L**2),mon(4*I*N/L**4,*a.fs),mon(-L**-6,*a.fs,*b.fs)]
    if t==r"\rho'":return rho(k)
    if t in [r"(\mathcal D_b\rho')",r"\mathcal D_a\rho'"]:
        return d_full(rho(k),'b' if '_b' in t else 'a')
    if t==r"\Box_c\rho'":
        # A linear operator on fully specified scalar arguments. Operational source definition retained separately.
        return [mon(2,atom(r'\Box_c\!\left(L^{-1}N\right)')),
                mon(I,atom(r'\Box_c\!\left('+render_product(mon(L**-3,*rho(k)[1].fs))+r'\right)',2))]
    if t.startswith(r'\not{\mathcal D}') and r"\lambda'" in t:
        a='q_{'+str(k)+'}'
        return [mon(x.c,atom(r'\gamma^{'+a+'}'),*x.fs) for x in d_full(lam('i',k),a)]
    if r"\lambda'" in t:
        bar=t.startswith(r'\bar');upper='^' in t
        free='j' if '^j' in t else 'i'
        if upper:
            r='r_{'+str(k)+'}'
            return [mon(x.c,atom(r'\varepsilon^{'+free+r+'}'),*x.fs) for x in lam(r,k,bar)]
        return lam(free,k,bar)
    return None

def ctex(c):
    c=S.factor(c)
    # sympy knows L,N,g are commutative but not real; avoid conjugation by using latex of algebraic expression.
    return S.latex(c).replace(r'\frac',r'\frac').replace(r' i ',r' i ')
def render_product(x):
    c=ctex(x.c)
    if c=='1':c=''
    if c=='-1':c='-'
    return c+(' ' if c and x.fs else '')+' '.join(f.tex for f in x.fs)
def combine(xs):
    d={}
    for x in xs:d[x.fs]=S.expand(d.get(x.fs,0)+x.c)
    return [mon(c,*f) for f,c in d.items() if c!=0]
def source_rows():
    ledger=json.loads((ROOT/'notes/step5_insertion_ledger.json').read_text())
    old.tokens[r'\bar\chi^i']=('bchi',)
    return [(x['group'],x['source_tex'],parse_sum(x['source_tex'].replace(r"\bar\chi\lambda'",r"\bar\chi^i\lambda'_i"))) for x in ledger['groups']]
def run():
    global counter
    rows=[];source=[]
    for group,raw,ss in source_rows():
        source.append({'group':group,'tex':raw,'rows':len(ss)})
        for si,x in enumerate(ss,1):
            out=[mon(x.c)]
            for f in x.fs:
                rr=replacement(f.tex)
                out=mul(out,rr if rr is not None else [mon(1,f)])
            for y in combine(out):
                rows.append({'group':group,'source_row':si,'degree':y.degree,'coefficient':str(y.c),'factors':[f.tex for f in y.fs],'tex':render_product(y)})
    return source,rows
if __name__=='__main__':
    source,rows=run()
    report={'parent':'notes/06_step4_Gold_unprimed_vector_and_gauge.md','parent_sha256':hashlib.sha256(old.DOC.read_bytes()).hexdigest(),'grading':'formal explicit covariant-slot degree; hidden completions retained','source':source,'rows':rows}
    out=ROOT/'build/step5a_expansion_ledger.json';out.write_text(json.dumps(report,indent=2)+'\n')
    from collections import Counter
    print('Rows by explicit degree:',dict(Counter(x['degree'] for x in rows)))
