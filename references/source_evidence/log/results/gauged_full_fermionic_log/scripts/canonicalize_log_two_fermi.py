"""Local algebraic reduction of the frozen STEP_06 displayed polynomials.

Writes only the separate canonical_two_fermi evidence and Markdown deliverable.
No differentiation, integration by parts, EOM, or derivative commutation.
"""
from pathlib import Path
from fractions import Fraction
from collections import Counter, defaultdict
from functools import lru_cache
import re, json, hashlib, pickle, time, itertools, math, gzip
import log_step6_projection as p
from sympy.combinatorics import Permutation, PermutationGroup
from sympy.combinatorics.tensor_can import canonicalize, get_minimal_bsgs

b=p.b; A=b.A; C=b.C; Q=b.Q; I=b.I
BASE=p.BASE
OUT=BASE/'sources/canonical_two_fermi'
SOURCE=BASE/'STEP_06_LOG_PROJECTED_MULTIPLET_AND_BOSONIC_ACTION.md'
LABEL=r'(?:\\[A-Za-z]+|[A-Za-z])(?:_\{\d+\})?'
INDEX=re.compile(r'\{\}([\^_])\{('+LABEL+r')\}')
DERIV=re.compile(r'\\mathcal D([\^_])\{('+LABEL+r')\}')
FIELD={r'\widehat F':'hatF',r'\lambda':'lam',r'\chi':'chi',r'\rho':'rho',
       r'\mathsf C':'eps',r'\varepsilon':'suB',r'\epsilon':'volB',
       'R(Q)':'RQ','R(V)':'RV','R(M)':'RMB','Y':'aux','T':'ten','D':'auxD',
       r'\eta':'eta',r'\delta':'del'}

def coeff(s):
    if s.startswith(r'+\left('):
        end=s.index(r'\right)'); inner=s[7:end]
        parts=re.findall(r'[+-]?(?:\\frac\{[^}]+\}\{\d+\}|\d*i?)',inner)
        val=C()
        for t in parts:
            if t: val+=coeff(t+'!')[0]
        return val,s[end+7:]
    m=re.match(r'([+-]?)(?:\\frac\{(\d*)(i?)\}\{(\d+)\}|(\d*)(i?))',s)
    assert m
    sign=-1 if m[1]=='-' else 1
    if m[4]: n=Q(int(m[2] or 1),int(m[4])); imaginary=bool(m[3])
    else: n=Q(int(m[5] or 1)); imaginary=bool(m[6])
    return (I if imaginary else b.coef(1))*sign*n,s[m.end():]

def parse_body(s,slot):
    mapping={}; serial=Counter()
    fixed={'L':{'i':'uI','j':'uJ'},'phi':{r'\alpha':'sE','i':'uI'},'N':{},'E':{'a':'lV'}}[slot]
    def ix(sign,label,kind):
        if label in fixed: name=fixed[label]; assert name[0]==kind
        else:
            if label not in mapping:
                serial[kind]+=1; mapping[label]=kind+str(serial[kind])
            name=mapping[label]; assert name[0]==kind
        return ('+' if sign=='^' else '-')+name
    def indices(kinds):
        nonlocal s
        answer=[]
        for kind in kinds:
            m=INDEX.match(s); assert m, (s,kinds)
            answer.append(ix(m[1],m[2],kind)); s=s[m.end():]
        return tuple(answer)
    fs=[]
    while s:
        wrapped=s.startswith(r'\big(')
        if wrapped:s=s[5:]
        ds=[]
        while (m:=DERIV.match(s)):
            ds.append(ix(m[1],m[2],'l'));s=s[m.end():]
        if s.startswith(r'(\gamma'):
            s=s[7:]; lis=[]
            while (m:=INDEX.match(s)):
                lis.append(ix(m[1],m[2],'l'));s=s[m.end():]
            assert s.startswith(')');s=s[1:]
            n='g'+str(len(lis)); atom=A(n,tuple(lis)+indices('ss'),tuple(ds))
        elif s.startswith(r'\rho^{'):
            m=re.match(r'\\rho\^\{(-?\d+)\}',s);assert m
            atom=A('pow',power=int(m[1]),ds=tuple(ds));s=s[m.end():]
        else:
            token=next((x for x in FIELD if s.startswith(x)),None);assert token,s
            n=FIELD[token];s=s[len(token):]
            kinds=b.spec[n][0]
            if n=='eps':kinds='ss'
            if n=='eta':kinds='ll'
            if n=='del':
                m=INDEX.match(s);assert m
                kind='s' if m[2].startswith('\\') else 'u' if m[2][0] in 'ijklmn' else 'l'
                kinds=kind*2
            atom=A(n,indices(kinds),tuple(ds))
        fs.append(atom)
        if wrapped:assert s.startswith(r'\big)'),s;s=s[5:]
    return tuple(fs)

def read_source():
    text=SOURCE.read_text(); slots={}; summary={}
    for slot in p.WEIGHTS:
        section=text.split('<!-- PROJECTED_'+slot+'_BEGIN -->')[1].split('<!-- PROJECTED_'+slot+'_END -->')[0]
        ts=[]
        for line in section.splitlines():
            if not (line.startswith('&') or line.startswith(r'\boxed')):continue
            line=line.split('&',1)[1].removesuffix('\\\\')
            for raw in re.split(r' (?=[+-])',line):
                if 'high fermi' in raw:continue
                c,body=coeff(raw); fs=parse_body(body,slot)
                assert sum(f.parity for f in fs)<=2,(slot,raw)
                ts.append((c,fs))
        pol=b.P.terms(ts);b.check(pol,p.WEIGHTS[slot],p.FREE[slot]);slots[slot]=pol
        summary[slot]={'input_terms':len(ts),'degrees':dict(Counter(sum(f.parity for f in fs) for c,fs in ts))}
    return slots,summary

def flip(x):return ('-' if x[0]=='+' else '+')+x[1:]

def metric_reduce(c,fs,combine_rho=True):
    """Use inverse-metric contraction, with B's naked epsilon converted first."""
    converted=[]
    for f in fs:
        if combine_rho and f.name=='rho' and not f.ds:f=A('pow',power=1)
        if f.name=='suB':
            if f.ix[0][0]=='-':c=-c
            f=b.replace(f,name='eps')
        converted.append(f)
    terms=b.normalize(b.P.terms([(c,converted)]),True).ts
    if not terms:return C(),()
    c,fs=terms[0];fs=list(fs)
    # Remaining metrics form closed loops, or have free endpoints. Evaluate
    # the loops directly: J^2=-1, tr(1)=dim, tr(J)=0. This avoids treating
    # inverse epsilon as an ordinary twice-raised tensor.
    nodes={i:f for i,f in enumerate(fs) if f.name in ('eps','eta','del')}
    adj=defaultdict(list)
    for j,f in nodes.items():
        for side,x in enumerate(f.ix):adj[x[1:]].append((j,side))
    removed=set();visited=set()
    for root in nodes:
        if root in visited:continue
        component={root};stack=[root]
        while stack:
            j=stack.pop()
            for x in nodes[j].ix:
                for k,side in adj[x[1:]]:
                    if k not in component:component.add(k);stack.append(k)
        visited.update(component)
        if any(len(adj[x[1:]])!=2 for j in component for x in nodes[j].ix):continue
        j=root;side=0;start=nodes[j].ix[0][1:];used=set();sg=1;nj=0;ne=0
        while True:
            f=nodes[j];used.add(j)
            if f.name=='eps':
                nj+=1
                sg*=(-1 if side else 1)
                sg*=(-1 if f.ix[0][0]=='+' else 1) if f.ix[0][1]=='s' else (1 if f.ix[0][0]=='+' else -1)
            elif f.name=='eta':ne+=int(f.ix[0][0]==f.ix[1][0])
            vertex=f.ix[1-side][1:]
            if vertex==start:break
            j,side=next((k,h) for k,h in adj[vertex] if k not in used)
        assert used==component
        dim={'l':5,'s':4,'u':2}[nodes[root].ix[0][1]]
        val=0 if nj%2 else sg*(-1)**(nj//2)*(dim if ne%2==0 else 3)
        c*=val;removed.update(component)
    fs=[f for j,f in enumerate(fs) if j not in removed]
    return c,tuple(fs)

@lru_cache(None)
def symmetry(name,nd,nix):
    rank=nd+nix;gens=[]
    def swap(a,d,sign):
        v=list(range(rank+2));v[nd+a],v[nd+d]=v[nd+d],v[nd+a]
        if sign<0:v[-2:]=v[-2:][::-1]
        gens.append(Permutation(v))
    if name in ('hatF','ten','RV','RQ','RMB','g2'):swap(0,1,-1)
    if name=='RMB':swap(2,3,-1)
    if name=='aux':swap(0,1,1)
    if name=='RV':swap(2,3,1)
    if name in ('g1','g2'):swap(nix-2,nix-1,-1 if name=='g1' else 1)
    if name=='eps':swap(0,1,-1)
    if name=='eta':swap(0,1,1)
    if name=='volB':
        for k in range(4):swap(k,k+1,-1)
    if not gens:gens=[Permutation(list(range(rank+2)))]
    gp=PermutationGroup(gens);base,gs=gp.schreier_sims_incremental()
    return get_minimal_bsgs(base,gs)

@lru_cache(60000)
def _tensor_canon(fs,slot):
    """Butler--Portugal dummy/slot canonicalization, ordered derivative slots."""
    c=b.coef(1)
    for f in fs:
        if f.name in ('hatF','ten','RV','RQ','RMB','g2') and f.ix[0][1:]==f.ix[1][1:]:return C(),()
        if f.name=='RMB' and f.ix[2][1:]==f.ix[3][1:]:return C(),()
        if f.name in ('aux','RV') and f.ix[-2][1:]==f.ix[-1][1:]:return C(),()
        if f.name in ('g1','g2') and f.ix[-2][1:]==f.ix[-1][1:]:return C(),()
        if f.name=='volB' and len(set(x[1:] for x in f.ix))<5:return C(),()
    # Sort factors; crossing two Grassmann odd factors contributes minus.
    key=lambda f:(f.name, len(f.ds),len(f.ix),f.power)
    original=list(enumerate(fs));order=sorted(original,key=lambda t:key(t[1]))
    odd=[n for n,f in order if f.parity]
    c*=(-1)**sum(x>y for i,x in enumerate(odd) for y in odd[i+1:])
    scalars=tuple(f for n,f in order if not b.allix(f))
    fs=tuple(f for n,f in order if b.allix(f));groups=[]
    for k,group in itertools.groupby(fs,key):
        group=list(group);f=group[0];base,gens=symmetry(f.name,len(f.ds),len(f.ix))
        groups.append((base,gens,len(group),f.parity))
    free=p.FREE[slot];orderidx=list(free);dums={k:[] for k in 'lsu'}
    for f in fs:
        for x in b.allix(f):
            if x[1:] not in orderidx and x[1:] not in dums[x[1]]:dums[x[1]].append(x[1:])
    mp={free[k]+k:i for i,k in enumerate(orderidx)}; inv={v:k for k,v in mp.items()};dummy=[]
    for kind in 'lsu':
        start=len(mp)
        for j,name in enumerate(dums[kind]):
            for sign in '+-':
                n=len(mp);mp[sign+name]=n;inv[n]=sign+kind+'c'+str(j)
        dummy.append(list(range(start,len(mp))))
    arr=[mp[x] for f in fs for x in b.allix(f)];rank=len(arr)
    assert sorted(arr)==list(range(rank)),(slot,fs,arr)
    if not groups:return c,scalars
    can=canonicalize(Permutation(arr+[rank,rank+1]),dummy,[0,1,1],*groups)
    if can==0:return C(),()
    if can[-1]==rank:c=-c
    result=[];start=0
    for f in fs:
        nd=len(f.ds);ni=len(f.ix);xs=tuple(inv[j] for j in can[start:start+nd+ni]);start+=nd+ni
        result.append(b.replace(f,ds=xs[:nd],ix=xs[nd:]))
    return c,scalars+tuple(result)

def tensor_canon(c,fs,slot):
    if not c:return C(),()
    sign,fs=_tensor_canon(tuple(fs),slot)
    return c*sign,fs

def collect_tensor(pol,slot):
    out=defaultdict(C);zeros=0
    for j,(c,fs) in enumerate(pol.ts):
        c,fs=metric_reduce(c,fs,combine_rho=False)
        c,fs=tensor_canon(c,fs,slot)
        if not c:zeros+=1
        else:out[fs]+=c
        if j and j%10000==0:print('Tensor',slot,j,len(pol.ts),len(out),flush=True)
    return b.P.terms([(c,fs) for fs,c in out.items() if c]),zeros

def matrix_edge(f,reverse=False):
    """Indexed gamma as sign*C^left*Gamma^(blade)*C^right."""
    left=int(f.ix[-2][0]=='+');right=int(f.ix[-1][0]=='-')
    sign=-1 if left!=right else 1
    # dd=-Gamma C, du=Gamma, ud=C Gamma C, uu=-C Gamma.
    if reverse:
        rank=len(f.ix)-2
        sign*=(-1)**(left+right) * (-(-1)**(rank*(rank-1)//2))
        l,r=right+1,left+1;sign*=(-1)**(l//2+r//2);left,right=l%2,r%2
    return sign,left,tuple(f.ix[:-2]),right

def spin_paths(fs,slot):
    gammas={j:f for j,f in enumerate(fs) if f.name in ('g1','g2')}
    ends=[]
    for j,f in enumerate(fs):
        if f.parity:
            pos=next(k for k,x in enumerate(f.ix) if x[1]=='s')
            ends.append((j,pos,f.ix[pos]))
    adj=defaultdict(list)
    for j,f in gammas.items():
        for side,x in enumerate(f.ix[-2:]):adj[x[1:]].append((j,side))
    todo=set(gammas);result=[]
    def walk(vertex):
        blocks=[];sign=1;left=None;right=0;start=vertex
        while True:
            candidates=[q for q in adj[vertex] if q[0] in todo]
            if not candidates:break
            j,side=candidates[0];todo.remove(j);f=gammas[j]
            sg,l,blade,r=matrix_edge(f,side==1);sign*=sg
            if left is None:left=l
            else:
                assert (right+l)%2==0,('internal C',fs,blocks,f)
                sign*=(-1)**((right+l)//2)
            right=r;blocks.append(blade);vertex=f.ix[-1 if side==0 else -2][1:]
            if vertex==start:break
        return vertex,sign,left,blocks,right
    if ends:
        if slot=='phi': start='sE';begin=None
        else:begin=ends[0];start=begin[2][1:]
        end,sg,l,blocks,r=walk(start)
        endpoint=next(e for e in ends if e[2][1:]==end and e!=begin)
        if begin is not None:
            l0=int(begin[2][0]=='+')
            if l is None:l=l0
            else:
                l+=l0;sg*=(-1)**(l//2);l%=2
        elif l is None:l=0
        er=int(endpoint[2][0]=='+');sg*=(-1)**er
        if not blocks:
            l+=er;sg*=(-1)**(l//2);l%=2;r=0
        else:r+=er;sg*=(-1)**(r//2);r%=2
        assert (l,r)==((0,0) if slot=='phi' else (1,0)),('end C',l,r,fs)
        result.append(('open',sg,tuple(blocks),begin,endpoint))
    while todo:
        j=min(todo);start=gammas[j].ix[-2][1:]
        end,sg,l,blocks,r=walk(start);assert end==start
        assert (l+r)%2==0
        sg*=(-1)**((l+r)//2)
        result.append(('trace',sg,tuple(blocks),None,None))
    return result,set(gammas)

def tidy_blade(blade):
    if len(blade)>5 or len({x[1:] for x in blade})!=len(blade):return 0,()
    key=lambda x:x[1:]
    n=sum(key(x)>key(y) for j,x in enumerate(blade) for y in blade[j+1:])
    return (-1)**n,tuple(sorted(blade,key=key))

@lru_cache(100000)
def clifford_term(blade,metrics,forbidden):
    """Contract internal Lorentz dummy indices immediately, in D=5."""
    blade=list(blade);metrics=list(metrics);factor=1
    while True:
        changed=False
        for j,(x,y) in enumerate(metrics):
            if x[1:]==y[1:]:
                assert x[0]!=y[0];factor*=5;metrics.pop(j);changed=True;break
            if frozenset((x[1:],y[1:])) in forbidden:return 0,(),()
            for a,other in ((x,y),(y,x)):
                match=next((k for k,z in enumerate(blade) if z[1:]==a[1:]),None)
                if match is not None:
                    assert blade[match][0]!=a[0]
                    blade[match]=other;metrics.pop(j);changed=True;break
                found=None
                for k,m in enumerate(metrics):
                    if k==j:continue
                    for side,z in enumerate(m):
                        if z[1:]==a[1:]:found=k,side;break
                    if found:break
                if found:
                    k,side=found;assert metrics[k][side][0]!=a[0]
                    new=tuple(sorted((other,metrics[k][1-side])))
                    metrics=[m for h,m in enumerate(metrics) if h not in (j,k)]+[new]
                    changed=True;break
            if changed:break
        if not changed:break
    sg,blade=tidy_blade(tuple(blade))
    return factor*sg,blade,tuple(sorted(metrics))

def right_vector(terms,x,forbidden=frozenset()):
    out=defaultdict(int)
    def add(c,blade,metrics):
        sign,bb,mm=clifford_term(blade,metrics,forbidden)
        if sign:out[bb,mm]+=c*sign
    for (blade,metrics),c in terms.items():
        add(c,blade+(x,),metrics)
        for j,y in enumerate(blade):
            if frozenset((y[1:],x[1:])) in forbidden:continue
            # Ordered product gamma^[a1...ap] gamma^b.
            mm=tuple(sorted((y,x)));mets=tuple(sorted(metrics+(mm,)))
            add(c*(-1)**(len(blade)-1-j),blade[:j]+blade[j+1:],mets)
    return {k:v for k,v in out.items() if v}

@lru_cache(40000)
def clifford(blocks,forbidden=frozenset()):
    terms={((),()):1}
    for block in blocks:
        old=terms
        for x in block:terms=right_vector(terms,x,forbidden)
        if len(block)==2:
            if frozenset(x[1:] for x in block) in forbidden:continue
            for (blade,metrics),c in old.items():
                mm=tuple(sorted(block));sign,bb,mm=clifford_term(blade,tuple(sorted(metrics+(mm,))),forbidden)
                key=bb,mm;terms[key]=terms.get(key,0)-c*sign
            terms={k:v for k,v in terms.items() if v}
    return tuple((c,blade,metrics) for (blade,metrics),c in terms.items())

def reduce_clifford(c,fs,slot):
    paths,removed=spin_paths(fs,slot)
    forbidden=set()
    for f in fs:
        if f.name in ('hatF','ten','RV','RQ','RMB'):
            forbidden.add(frozenset(x[1:] for x in f.ix[:2]))
            if f.name=='RMB':forbidden.add(frozenset(x[1:] for x in f.ix[2:4]))
        if f.name=='volB':
            forbidden.update(frozenset((x[1:],y[1:])) for x,y in itertools.combinations(f.ix,2))
    forbidden=frozenset(forbidden)
    endpoint_names={j:'sOpen'+str(k) for k,(j,f) in enumerate((j,f) for j,f in enumerate(fs) if f.parity)}
    base=[b.replace(f,ix=tuple('-'+endpoint_names[j] if x[1]=='s' else x for x in f.ix))
          if f.parity else f for j,f in enumerate(fs) if j not in removed]
    # All physical spinor arrays are represented with lower spinor index.
    for k,f in enumerate(base):
        if f.parity:base[k]=b.replace(f,ix=tuple('-'+x[1:] if x[1]=='s' else x for x in f.ix))
    outputs=[(c,tuple(base))]
    for kind,sg,blocks,begin,end in paths:
        terms=[]
        for fac,blade,metrics in clifford(blocks,forbidden):
            cc=b.coef(sg*fac);factors=[A('eta',m) for m in metrics];rank=len(blade)
            if kind=='trace':
                if rank==0:cc*=4
                elif rank==5:cc*=4*I;factors.append(A('volB',blade))
                else:continue
            else:
                # Gamma ranks 3,4,5 dualize to 2,1,0 using gamma^01234=i.
                if rank>=3:
                    new=tuple('+lDual'+str(j) for j in range(5-rank))
                    cc*= {3:-I*Q(1,2),4:I,5:I}[rank]
                    factors.append(A('volB',blade+new));blade=tuple(flip(x) for x in new);rank=len(blade)
                if slot=='phi':
                    spin=('-sE','+'+endpoint_names[end[0]])
                    if rank==0:factors.append(A('del',spin))
                    else:factors.append(A('g'+str(rank),blade+spin))
                else:
                    cc=-cc;spin=('+'+endpoint_names[begin[0]],'+'+endpoint_names[end[0]])
                    if rank==0:factors.append(A('eps',spin))
                    else:factors.append(A('g'+str(rank),blade+spin))
            terms.append((cc,tuple(factors)))
        outputs=[(c*d,a+bb) for c,a in outputs for d,bb in terms]
    return outputs

def epsilon_pairs(c,fs):
    if not c or elementary_zero(fs):return []
    ids=[j for j,f in enumerate(fs) if f.name=='volB']
    if len(ids)<2:return [(c,fs)]
    ia,ib=ids[:2];aa=fs[ia].ix;bb=fs[ib].ix
    if len(set(x[1:] for x in aa))<5 or len(set(x[1:] for x in bb))<5:return []
    shared=[x[1:] for x in aa if any(x[1:]==y[1:] for y in bb)]
    fa=[x for x in aa if x[1:] not in shared];fb=[x for x in bb if x[1:] not in shared]
    def perm_sign(original,free):
        target=[x[1:] for x in free]+shared;order=[target.index(x[1:]) for x in original]
        return (-1)**sum(x>y for j,x in enumerate(order) for y in order[j+1:])
    fac=-math.factorial(len(shared))*perm_sign(aa,fa)*perm_sign(bb,fb)
    rest=tuple(f for j,f in enumerate(fs) if j not in (ia,ib));out=[]
    for perm in itertools.permutations(range(len(fb))):
        sg=(-1)**sum(x>y for j,x in enumerate(perm) for y in perm[j+1:])
        mets=tuple(A('eta',(x,fb[perm[j]])) for j,x in enumerate(fa))
        d,gs=metric_reduce(c*fac*sg,rest+mets)
        out.extend(epsilon_pairs(d,gs))
    return out

def elementary_zero(fs):
    # Cheap consequences of the same symmetries used by tensor_canon.
    # Apply these before expanding an epsilon determinant.
    for f in fs:
        if f.name in ('hatF','ten','RV','RQ','RMB','g2') and f.ix[0][1:]==f.ix[1][1:]:return True
        if f.name=='RMB' and f.ix[2][1:]==f.ix[3][1:]:return True
        if f.name in ('aux','RV') and f.ix[-2][1:]==f.ix[-1][1:]:return True
        if f.name=='volB' and len(set(x[1:] for x in f.ix))<5:return True
    fermions=[f for f in fs if f.parity]
    gammas=[f for f in fs if f.name in ('g1','g2')]
    if len(fermions)==2 and len(gammas)<=1:
        f,g=fermions
        if f.name==g.name and f.name in ('lam','chi') and f.ds==g.ds:
            rank=int(gammas[0].name[-1]) if gammas else 0
            u,v=f.ix[-1],g.ix[-1]
            if u==flip(v) and rank!=2:return True
            if rank==2:
                for h in fs:
                    if h.name in ('aux','RV') and set(h.ix[-2:])=={flip(u),flip(v)}:return True
    return False

def collect_epsilon(pol,slot):
    out=defaultdict(C)
    for c,fs in pol.ts:
        c,fs=metric_reduce(c,fs)
        for d,gs in epsilon_pairs(c,fs):
            d,gs=tensor_canon(d,gs,slot)
            if d:out[gs]+=d
    return b.P.terms([(c,fs) for fs,c in out.items() if c])

def two_form_wedge(c,fs):
    """A_c^d epsilon_abdef A^ef = (eta_bc v_a-eta_ac v_b)/4.

    v_a=epsilon_abdef A^bd A^ef. Apply to exactly two undifferentiated
    copies, avoiding any recursive choice among higher powers of A.
    """
    for name in ('ten','hatF'):
        forms=[j for j,f in enumerate(fs) if f.name==name and not f.ds]
        if len(forms)!=2:continue
        for e,eps in enumerate(fs):
            if eps.name!='volB':continue
            names=[x[1:] for x in eps.ix]
            for j,k in (forms,forms[::-1]):
                f,g=fs[j],fs[k]
                matched=[n for n,x in enumerate(f.ix) if x[1:] in names]
                if len(matched)!=1 or not all(x[1:] in names for x in g.ix):continue
                side=matched[0];d=f.ix[side];cc=f.ix[1-side]
                free=[x for x in eps.ix if x[1:] not in {d[1:],*(x[1:] for x in g.ix)}]
                if len(free)!=2:continue
                target=[x[1:] for x in free]+[d[1:]]+[x[1:] for x in g.ix]
                order=[target.index(x) for x in names]
                sg=(-1 if side==0 else 1)*(-1)**sum(a>b for n,a in enumerate(order) for b in order[n+1:])
                rest=tuple(f for n,f in enumerate(fs) if n not in (j,k,e))
                ids=tuple('lWedge'+str(n) for n in range(4))
                form=(A(name,tuple('+'+x for x in ids[:2])),A(name,tuple('+'+x for x in ids[2:])))
                out=[]
                for a,b,sign in ((free[0],free[1],1),(free[1],free[0],-1)):
                    out.append((c*sg*sign*Q(1,4),rest+form+(A('eta',(b,cc)),A('volB',(a,)+tuple('-'+x for x in ids)))))
                return out
    return [(c,fs)]

def collect_wedge(pol,slot):
    out=defaultdict(C)
    for c,fs in pol.ts:
        for d,gs in two_form_wedge(c,fs):
            d,gs=metric_reduce(d,gs);d,gs=tensor_canon(d,gs,slot)
            if d:out[gs]+=d
    return b.P.terms([(c,fs) for fs,c in out.items() if c])

def collect_clifford(pol,slot,resume=False,checkpoint_suffix=''):
    out=defaultdict(C);expanded=0;zeros=0;start=-1
    checkpoint=OUT/(slot+checkpoint_suffix+'-clifford-progress.pkl')
    if resume and checkpoint.exists():
        with checkpoint.open('rb') as f:start,out,expanded,zeros=pickle.load(f)
        print('Resume',slot,start,flush=True)
    for j,(c,fs) in enumerate(pol.ts):
        if j<=start:continue
        for d,gs in reduce_clifford(c,fs,slot):
            expanded+=1;d,gs=metric_reduce(d,gs)
            for e,hs in epsilon_pairs(d,gs):
                e,hs=tensor_canon(e,hs,slot)
                if not e:zeros+=1
                else:out[hs]+=e
        if j and j%100==0:print('Clifford',slot,j,len(pol.ts),len(out),flush=True)
        if j and j%250==0:
            with (OUT/(slot+checkpoint_suffix+'-clifford-progress.pkl')).open('wb') as checkpoint_file:
                pickle.dump((j,out,expanded,zeros),checkpoint_file)
    result=collect_wedge(collect_epsilon(b.P.terms([(c,fs) for fs,c in out.items() if c]),slot),slot)
    return result,expanded,zeros

def human_term(c,fs,slot,omit_power=True):
    """Replace the final spinor contraction by a Majorana bilinear."""
    p.labels(slot)
    paths,removed=spin_paths(fs,slot);evens=[];contracted=set();squares=[]
    for j,f in enumerate(fs):
        if j in contracted or f.ds or f.name not in ('ten','hatF','aux'):continue
        for k in range(j+1,len(fs)):
            g=fs[k]
            if k in contracted or g.ds or g.name!=f.name:continue
            if set(f.ix)!={flip(x) for x in g.ix}:continue
            if f.name=='aux' and f.ix[0][0]!=f.ix[1][0]:continue
            if tuple(flip(x) for x in g.ix)!=f.ix and f.name!='aux':c=-c
            contracted.update((j,k));squares.append({'ten':r'T^2','hatF':r'\widehat F^2','aux':r'Y^2'}[f.name]);break
    mp=b.a.namemap(tuple(f for j,f in enumerate(fs) if j not in contracted))
    def human_atom(f):
        body=p.texatom(b.replace(f,ds=()),mp)
        if not f.ds:return body
        ds=f.ds;parts=[];j=0
        while j<len(ds):
            if j+1<len(ds) and ds[j]==flip(ds[j+1]):parts.append(r'\Box^c ');j+=2
            else:
                x=ds[j];parts.append((r'\mathcal D^{' if x[0]=='+' else r'\mathcal D_{')+mp[x[1:]]+'}');j+=1
        return r'\big('+''.join(parts)+body+r'\big)'
    for j,f in enumerate(fs):
        if j in removed or j in contracted or f.parity or (omit_power and f.name=='pow'):continue
        if f.name=='eps' and f.ix[0][1]=='u' and f.ix[0][0]=='-':c=-c
        if f.name=='eps' and f.ix[0][1]=='u':f=b.replace(f,name='suB')
        evens.append(human_atom(f))
    count=evens.count('D')
    if count>1:evens=[x for x in evens if x!='D']+['D^{'+str(count)+'}']
    for sq,count in Counter(squares).items():evens.append(sq if count==1 else '('+sq+')^{'+str(count)+'}')
    for kind,sg,blocks,begin,end in paths:
        assert kind=='open' and len(blocks)<=1,(slot,fs,paths)
        c*=sg;blade=blocks[0] if blocks else ()
        matrix=r'\gamma'+''.join(('{}^{' if x[0]=='+' else '{}_{')+mp[x[1:]]+'}' for x in blade) if blade else ''
        def fermion(endpoint):
            f=fs[endpoint[0]];f=b.replace(f,ix=tuple(x for x in f.ix if x[1]!='s'))
            return human_atom(f)
        if begin is not None:evens.append(r'\overline{'+fermion(begin)+'}'+matrix+fermion(end))
        else:evens.append(matrix+fermion(end))
    return c,''.join(evens) or '1'

def grouped(pol,slot):
    out=defaultdict(dict)
    for c,fs in pol.ts:
        power=sum(f.power for f in fs if f.name=='pow');degree=sum(f.parity for f in fs)
        c,body=human_term(c,fs,slot)
        row=out[power,degree];row[body]=row.get(body,C())+c
    return {k:[(c,body) for body,c in v.items() if c] for k,v in out.items()}

def main():
    OUT.mkdir(parents=True,exist_ok=True)
    slots,report=read_source()
    print('Parsed', {k:len(v.ts) for k,v in slots.items()},flush=True)
    with gzip.open(OUT/'parsed.pkl.gz','wb') as f:pickle.dump(slots,f)
    for slot,pol in slots.items():
        start=time.time();result,zeros=collect_tensor(pol,slot)
        b.check(result,p.WEIGHTS[slot],p.FREE[slot])
        with (OUT/(slot+'-tensor.pkl')).open('wb') as f:pickle.dump(result,f)
        report[slot].update(tensor_terms=len(result.ts),symmetry_zeros=zeros,seconds=time.time()-start)
        print(slot,report[slot],flush=True)
        (OUT/'progress.json').write_text(json.dumps(report,indent=2)+'\n')
        final,expanded,zero=collect_clifford(result,slot)
        final,_=collect_tensor(final,slot)
        b.check(final,p.WEIGHTS[slot],p.FREE[slot])
        with (OUT/(slot+'-clifford.pkl')).open('wb') as f:pickle.dump(final,f)
        print(slot,'final',len(final.ts),flush=True)
    from write_log_two_fermi_canonical import write
    write()

if __name__=='__main__':main()
