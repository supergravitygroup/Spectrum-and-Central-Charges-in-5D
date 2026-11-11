"""Exact verification algebra for notebook Part V. Not a replacement for the hand derivation."""
from pathlib import Path
import re,json,itertools as it,copy,math
from functools import lru_cache
from collections import defaultdict,Counter
import sympy as S
from sympy.tensor.tensor import TensorIndexType,TensorHead,TensorSymmetry,TensorIndex,canon_bp
from sympy.combinatorics import Permutation,PermutationGroup
BASE=Path(__file__).resolve().parents[1]
PH=BASE/'.gpd/phases/02-ozkan-map-and-variation-completion'
SOURCE=json.loads((PH/'H50-COMPLETION-LEDGER.json').read_text())['summation']['rows']

def unbrace(s,at):
 assert s[at]=='{';level=1;i=at+1
 while level:
  level+=(s[i]=='{')-(s[i]=='}');i+=1
 return s[at+1:i-1],i

def parse(row):
 s=row['latex'].replace(r'\epsilon^i','').replace('T^2^2','T^2T^2')
 while r'\overline{' in s:
  a=s.index(r'\overline{');body,end=unbrace(s,a+len(r'\overline'));s=s[:a]+body+s[end:]
 s=s.replace(r'\widehat R(Q)','R').replace(r'\widehat R(V)','V').replace(r'\widehat C','C')
 s=s.replace(r'(\gamma\!\cdot\!T)','K').replace(r'\gamma\!\cdot\!T','K')
 s=s.replace(r'\mathcal D','d').replace(r'\gamma','G').replace(r'\chi','X').replace(r'\eta','m').replace(r'\delta','m').replace(r'\bar','')
 s=s.replace(r'\big(','<').replace(r'\big)','>').replace(r'\,','').replace(' ','')
 factors=[];out=[];inside=[];ferm=[];der=[];at=0;region=False;fresh=0;marks=[]
 def inds():
  nonlocal at
  out=[]
  while at<len(s):
   if s[at:at+2]=='{}':at+=2;continue
   if s[at] not in '_^':break
   up=s[at]=='^';at+=1
   if s[at]=='{':body,at=unbrace(s,at)
   else:body=s[at];at+=1
   for k,ch in enumerate(body):
    if ch.isalpha():out.append([ch,up, '[' if k and body[k-1]=='[' else ']' if k+1<len(body) and body[k+1]==']' else ''])
  return out
 def freshpair():
  nonlocal fresh
  a,b='x'+str(fresh),'x'+str(fresh+1);fresh+=2
  return [[a,False,''],[b,False,'']]
 while at<len(s):
  ch=s[at];at+=1
  if ch=='<':region=True;continue
  if ch=='>':region=False;continue
  if ch in '(){}':continue
  assert ch in 'dGXTDRVCKm',(s,at,ch)
  if ch=='K':
   ix=freshpair();factors.append(('T',copy.deepcopy(ix)));(inside if region else out).append(copy.deepcopy(ix));continue
  if ch=='D' and s[at:at+2]=='^2':
   at+=2;factors.append(('D2',[]));continue
  if ch=='T' and s[at:at+2]=='^2':
   at+=2;ix=freshpair();factors.extend([('T',copy.deepcopy(ix)),('T',copy.deepcopy(ix))]);continue
  ix=inds()
  if ch=='d':der+=ix;continue
  if ch=='G':assert not der;(inside if region else out).append(ix);continue
  if ch in ['X','R']:
   assert region,(row,ch)
   ferm.append((ch,len(der),der+ix));der=[];continue
  if ch=='V':ix=[i for i in ix if i[0] not in ['i','j','k','l']]
  factors.append((ch+('d'+str(len(der)) if der else ''),der+ix));der=[]
 assert not der and len(ferm) in [0,2],row
 allslots=[idx for _,ix in factors for idx in ix]+[idx for ix in out+inside for idx in ix]+[idx for _,_,ix in ferm for idx in ix]
 opens=[idx for idx in allslots if idx[2]=='['];closes=[idx for idx in allslots if idx[2]==']']
 assert len(opens)==len(closes)<=1,(opens,closes)
 terms=[]
 for flip in range(2 if opens else 1):
  data=copy.deepcopy((factors,out,inside,ferm))
  if flip:
   slots=[idx for _,ix in data[0] for idx in ix]+[idx for ix in data[1]+data[2] for idx in ix]+[idx for _,_,ix in data[3] for idx in ix]
   for ix in slots:
    if ix[2]=='[':ix[0]=closes[0][0]
    elif ix[2]==']':ix[0]=opens[0][0]
  f,go,gi,fr=data
  f=tuple((n,tuple(q[0] for q in ix)) for n,ix in f);go=tuple(tuple(q[0] for q in ix) for ix in go);gi=tuple(tuple(q[0] for q in ix) for ix in gi);fr=tuple((n,d,tuple(q[0] for q in ix)) for n,d,ix in fr)
  c=S.Rational(row['coefficient'][0])+S.I*S.Rational(row['coefficient'][1]);c*=(-1)**flip*S.Rational(1,2 if opens else 1)
  count=Counter(x for n,ix in f for x in ix);count.update(x for ix in go+gi for x in ix);count.update(x for n,d,ix in fr for x in ix)
  assert all(v==2 for v in count.values()),(row,count)
  terms.append((c,f,go,gi,fr))
 return terms

# Abstract gamma blades multiplied by repeated use of Gamma_I gamma_b.
def sortblade(ix):
 if len(ix)!=len(set(ix)) or len(ix)>5:return 0,()
 sign=(-1)**sum(ix[a]>ix[b] for a in range(len(ix)) for b in range(a+1,len(ix)))
 return sign,tuple(sorted(ix))
@lru_cache(None)
def blade_right(I,b):
 terms=[];s,J=sortblade(I+(b,))
 if s:terms.append((s,J,()))
 n=len(I)
 for k,a in enumerate(I):terms.append(((-1)**(n-1-k),I[:k]+I[k+1:],(tuple(sorted((a,b))),)))
 return tuple(terms)
@lru_cache(None)
def blade_product(I,J):
 if not J:return ((S.Integer(1),I,()),)
 acc=defaultdict(lambda:S.Integer(0));n=len(J)
 for k,b in enumerate(J):
  for c,L,metrics in blade_product(I,J[:k]+J[k+1:]):
   for d,M,newm in blade_right(L,b):acc[(M,tuple(sorted(metrics+newm)))]+=c*d*S.Rational((-1)**(n-1-k),n)
 return tuple((S.expand(c),I,m) for (I,m),c in acc.items() if c)
@lru_cache(None)
def gamma_chain(chain):
 acc={((),()):S.Integer(1)}
 for blade in chain:
  s,B=sortblade(blade)
  if not s:return ()
  new=defaultdict(lambda:S.Integer(0))
  for (old,met),coef in acc.items():
   for c,ix,m in blade_product(old,B):new[(ix,tuple(sorted(met+m)))]+=coef*s*c
  acc={k:S.expand(c) for k,c in new.items() if c}
 return tuple((c,ix,m) for (ix,m),c in acc.items())

if __name__=='__main__':
 parsed=[parse(r) for r in SOURCE];print('parsed',len(parsed),'terms',sum(map(len,parsed)))
 print('max gamma lengths',max(sum(map(len,t[2])) for ts in parsed for t in ts),max(sum(map(len,t[3])) for ts in parsed for t in ts))

# A term below is a coefficient, commuting tensor factors, exterior/interior
# blades, and the two ordered physical spinors. No such helpers enter the note.
def metric_reduce(factors,go,gi,ferm,metrics=()):
 factors=list(factors);mets=list(metrics)+[ix for n,ix in factors if n=='m'];factors=[(n,ix) for n,ix in factors if n!='m'];mult=S.Integer(1)
 go=tuple(go);gi=tuple(gi);ferm=tuple(ferm)
 while mets:
  a,b=mets.pop()
  if a==b:mult*=5;continue
  sub=lambda ix:tuple(a if x==b else x for x in ix)
  factors=[(n,sub(ix)) for n,ix in factors];go=sub(go);gi=sub(gi);ferm=tuple((n,d,sub(ix)) for n,d,ix in ferm);mets=[sub(ix) for ix in mets]
 so,go=sortblade(go);si,gi=sortblade(gi)
 return mult*so*si,tuple(factors),go,gi,ferm

def trace_reduce(factors,go,gi,ferm):
 # Conventional gamma trace, not an equation of motion.
 if not ferm:return [(S.Integer(1),factors,go,gi,ferm)]
 for side in [1,0]:
  name,nder,ix=ferm[side]
  if name!='R':continue
  for a in ix[nder:]:
   if a not in gi:continue
   at=gi.index(a);rest=gi[:at]+gi[at+1:];n=len(gi)
   rows=[]
   for k,b in enumerate(rest):
    sign=-(-1)**((n-1-at)+(n-2-k)) if side==1 else -(-1)**(at+k)
    J=rest[:k]+rest[k+1:]
    sub=lambda ix:tuple(b if x==a else x for x in ix)
    F=tuple((nm,sub(ix)) for nm,ix in factors);fr=tuple((nm,d,sub(ix)) for nm,d,ix in ferm)
    m,F,G,J,fr=metric_reduce(F,sub(go),J,fr)
    if m:
     for c,F,G,J,fr in trace_reduce(F,G,J,fr):rows.append((sign*m*c,F,G,J,fr))
   return rows
 return [(S.Integer(1),factors,go,gi,ferm)]

def dual_reduce(f,go,gi,ferm):
 f=list(f);coef=S.Integer(1);used={x for _,ix in f for x in ix}|set(go)|set(gi)|{x for _,_,ix in ferm for x in ix}
 def fresh(n):
  out=[];i=0
  while len(out)<n:
   lab='z'+str(i);i+=1
   if lab not in used:out.append(lab);used.add(lab)
  return tuple(out)
 gammas=[]
 for blade in [go,gi]:
  n=len(blade)
  if n>2:
   new=fresh(5-n);f.append(('E',blade+new));coef*=(-S.I/2 if n==3 else S.I);blade=new
  gammas.append(blade)
 return coef,tuple(f),*gammas,ferm

def parity(ix):return (-1)**sum(ix[a]>ix[b] for a in range(len(ix)) for b in range(a+1,len(ix)))
def epsilon_reduce(f,go,gi,ferm):
 eps=[(k,ix) for k,(nm,ix) in enumerate(f) if nm=='E']
 if any(len(set(ix))<5 for _,ix in eps):return []
 if len(eps)<2:return [(S.Integer(1),f,go,gi,ferm)]
 assert len(eps)==2
 (a,A),(b,B)=eps;common=sorted(set(A)&set(B));n=len(common);L=tuple(x for x in A if x not in common);R=tuple(x for x in B if x not in common)
 sign=(-1)**sum((common+list(L)).index(x)>(common+list(L)).index(y) for j,x in enumerate(A) for y in A[j+1:])
 sign*=(-1)**sum((common+list(R)).index(x)>(common+list(R)).index(y) for j,x in enumerate(B) for y in B[j+1:])
 keep=tuple(t for k,t in enumerate(f) if k not in [a,b]);ans=[]
 for perm in it.permutations(range(len(L))):
  metrics=tuple((L[i],R[j]) for i,j in enumerate(perm));c,F,G,J,fr=metric_reduce(keep,go,gi,ferm,metrics)
  if c:ans.append((-sign*math.factorial(n)*parity(perm)*c,F,G,J,fr))
 return ans

LTYPE=TensorIndexType('L',dim=5,dummy_name='ell')
heads={};head_info={}
def gethead(name,parts,swap=None):
 key=(name,tuple(parts),swap)
 if key in heads:return heads[key]
 sym=TensorSymmetry.direct_product(*parts)
 if swap:
  left,grank,right,sgn=swap;n=left+grank+right
  perm=list(range(n+2))
  for k in range(left):perm[k],perm[left+grank+k]=left+grank+k,k
  if sgn<0:perm[n],perm[n+1]=n+1,n
  group=PermutationGroup(list(sym.generators)+[Permutation(perm)]);group.schreier_sims();sym=TensorSymmetry(group.base,group.strong_gens)
 rank=sum(map(abs,parts));head=TensorHead(name,[LTYPE]*rank,sym);heads[key]=head;head_info[name]=(parts,swap)
 return head

def slots(n,d):return [1]*d+([-2] if n=='R' else [])
@lru_cache(None)
def canonical(factors,go,gi,ferm):
 # Canonicalization only uses displayed tensor symmetries and the contracted Majorana flip.
 sign=1;factors=list(factors)
 for n,ix in factors:
  if n.startswith('C') and len(set(ix[-4:]))<4:return S.Integer(0)
 if ferm:
  a,b=ferm
  order=lambda f:(f[1],f[0])
  if order(a)>order(b):a,b=b,a;sign*=(-1 if len(gi) in [0,1,4,5] else 1)
  na,da,ia=a;nb,db,ib=b
  if a[0:2]==b[0:2] and not ia and not ib and len(gi) in [0,1,4,5]:return S.Integer(0)
  nm='B'+na+str(da)+nb+str(db)+'g'+str(len(gi))
  symparts=slots(na,da)+([-len(gi)] if len(gi)>1 else [1]*len(gi))+slots(nb,db)
  sw=(len(ia),len(gi),len(ib),-1 if len(gi) in [0,1,4,5] else 1) if (na,da)==(nb,db) else None
  gethead(nm,symparts,sw);factors.append((nm,ia+gi+ib))
 if go:
  nm='G'+str(len(go));gethead(nm,[-len(go)] if len(go)>1 else [1]);factors.append((nm,go))
 expr=S.Integer(sign);counts=Counter()
 for nm,ix in sorted(factors):
  if nm not in head_info:
   if nm=='E':parts=[-5]
   elif nm in ['T','V']:parts=[-2]
   elif nm=='C':parts=[-2,-2]
   elif nm in ['D','D2']:parts=[]
   elif re.match(r'[TCD]d[12]$',nm):
    nder=int(nm[-1]);base=nm[0];parts=[1]*nder+([-2] if base=='T' else [-2,-2] if base=='C' else [])
   else:raise ValueError((nm,ix))
   gethead(nm,parts)
  head=next(h for k,h in heads.items() if k[0]==nm)
  indices=[]
  for x in ix:
   counts[x]+=1;indices.append(TensorIndex(x,LTYPE,is_up=counts[x]==1))
  expr*=head(*indices)
 assert all(n==2 for n in counts.values()),(factors,counts)
 return canon_bp(expr)

def canonical_parts(expr):
 if expr==0:return 0,()
 coefficient=expr.coeff
 terms=[];indices=expr.get_indices();at=0
 for h in expr.components:
  ix=indices[at:at+h.rank];at+=h.rank;terms.append((h.name,tuple(str(i.name) for i in ix)))
 return coefficient,tuple(terms)

def evaluate_row(row,stage_record=False):
 # Scalar coefficient arithmetic is exact throughout.
 acc=defaultdict(lambda:S.Integer(0));stats=Counter()
 for coef,f,goc,gic,ferm in parse(row):
  for c,go,mo in gamma_chain(goc):
   for d,gi,mi in gamma_chain(gic):
    m,F,G,J,fr=metric_reduce(f,go,gi,ferm,mo+mi)
    if not m:continue
    for n,F,G,J,fr in trace_reduce(F,G,J,fr):
     q,F,G,J,fr=dual_reduce(F,G,J,fr)
     for r,F,G,J,fr in epsilon_reduce(F,G,J,fr):
      for t,F,G,J,fr in trace_reduce(F,G,J,fr):
       v=canonical(F,G,J,fr);stats['canonical_calls']+=1
       if v!=0:
        vcoef,key=canonical_parts(v);acc[key]+=coef*c*d*m*n*q*r*t*vcoef
 return {k:S.expand(v) for k,v in acc.items() if v},stats

def evaluate_parsed(parsed):
 acc=defaultdict(lambda:S.Integer(0));stats=Counter()
 for coef,f,goc,gic,ferm in parsed:
  for c,go,mo in gamma_chain(goc):
   for d,gi,mi in gamma_chain(gic):
    m,F,G,J,fr=metric_reduce(f,go,gi,ferm,mo+mi)
    if not m:continue
    for n,F,G,J,fr in trace_reduce(F,G,J,fr):
     q,F,G,J,fr=dual_reduce(F,G,J,fr)
     for r,F,G,J,fr in epsilon_reduce(F,G,J,fr):
      for t,F,G,J,fr in trace_reduce(F,G,J,fr):
       v=canonical(F,G,J,fr);stats['canonical_calls']+=1
       if v!=0:
        vc,key=canonical_parts(v);acc[key]+=coef*c*d*m*n*q*r*t*vc
 return {k:S.expand(v) for k,v in acc.items() if v},stats

def component_inputs():
 old=json.loads((PH/'HUMAN-NOTATION-LEDGER.json').read_text());new=json.loads((PH/'H50-COMPLETION-LEDGER.json').read_text())
 out=[]
 for block in range(1,12):
  rows=old['blocks'][str(block)]+new['blocks'].get(str(block),[])
  for rownum,row in enumerate(rows):
   if isinstance(row['rank'],int) and row['rank']!=0:continue
   parsed=parse(row)
   if isinstance(row['rank'],int):
    for rank in range(3):
     newparsed=[]
     for c,f,go,gi,fr in parse(rows[rownum+1]):
      assert rows[rownum+1]['rank']==1
      inserted=go[-1];A=go[:-1];assert len(inserted)==1 and gi.count(inserted)==1
      at=gi.index(inserted);free=tuple('out'+str(i) for i in range(rank))
      newparsed.append((c*(-S.Rational(1,2) if rank==2 else 1),f,(free,) if free else (),gi[:at]+((free,) if free else ())+A+gi[at+1:],fr))
     out.append({'block':block,'source':row,'rank':rank,'parsed':newparsed})
   else:out.append({'block':block,'source':row,'rank':None,'parsed':parsed})
 return out
