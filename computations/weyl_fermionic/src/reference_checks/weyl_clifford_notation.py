import re,sympy as S

def coefficient(c,first=False):
 c=S.sympify(c);imag=c.has(S.I)
 if imag:c=S.simplify(c/S.I)
 sign='-' if c<0 else ('' if first else '+');c=abs(c)
 num='' if c.p==1 else str(c.p)
 if imag:num+='i'
 elif not num:num='1'
 s=r'\frac{'+num+'}{'+str(c.q)+'}' if c.q!=1 else ('' if num=='1' else num)
 return sign+s

def render_parsed(row,coefficient_only=False,antisym=False):
 c,f,go,gi,fr=row
 free=tuple(go[0]) if coefficient_only and len(go)==1 else ()
 names={x:'ab'[k] for k,x in enumerate(free)};alpha=iter('cdefghjklmnpqrstuvwxyz')
 for ix in [*[ix for n,ix in f],*go,*gi,*[ix for n,d,ix in fr]]:
  for x in ix:
   if x not in names:names[x]=next(alpha)
 seen={};pref={}
 # A gamma's first slot occurrence is upper; the corresponding field slot lower.
 for ix in gi+([] if coefficient_only else go):
  for x in ix:pref.setdefault(x,'gamma')
 bracketcount=0
 def scripts(ix,kind='field'):
  nonlocal bracketcount
  out='';buffer='';last=None
  for x in ix:
   count=seen.get(x,0);seen[x]=count+1
   if x in free:up=True
   elif x in pref:
    if x not in firstkind:firstkind[x]=kind
    up=(kind=='gamma') if count==0 else (firstkind[x]!='gamma')
   else:up=count!=0
   if last is not None and last!=up:out+=('^' if last else '_')+'{'+buffer+'}';buffer=''
   lab=names[x]
   if x in free and antisym:
    lab=('['+lab) if bracketcount==0 else (lab+']');bracketcount+=1
   elif antisym and bracketcount==1:lab='|'+lab+'|'
   buffer+=lab;last=up
  if buffer:out+=('^' if last else '_')+'{'+buffer+'}'
  return re.sub(r'(?<=})(?=[_^])','{}',out)
 firstkind={}
 def field(n,d,ix,bar=False):
  deriv=''.join(r'\mathcal D'+scripts((x,)) for x in ix[:d]);rest=ix[d:]
  body=r'\widehat R(Q)'+scripts(rest) if n=='R' else r'\chi'
  return (r'\overline{'+deriv+body+'}') if bar and (n=='R' or d) else r'\bar\chi' if bar else deriv+body
 out=[];vcount=0
 if fr:
  lhs=field(*fr[0],True);gam=''.join(r'\gamma'+scripts(ix,'gamma') for ix in gi);rhs=field(*fr[1]);out.append(r'\big('+lhs+gam+rhs+r'\big)')
 for n,ix in f:
  if n=='E':out.append(r'\varepsilon'+scripts(ix));continue
  if n=='m':out.append(r'\eta'+scripts(ix));continue
  d=int(n[-1]) if 'd' in n else 0;deriv=''.join(r'\mathcal D'+scripts((x,)) for x in ix[:d]);nam={'T':'T','D':'D','C':r'\widehat C','V':r'\widehat R(V)'}[n[0]]
  txt=deriv+nam+scripts(ix[d:]);txt=r'D^2' if n=='D2' else txt
  if n=='V':txt+=('{}^{rs}' if vcount==0 else '{}_{rs}');vcount+=1
  if d:txt='('+txt+')'
  out.append(txt)
 if go and not coefficient_only:out.append(''.join(r'\gamma'+scripts(ix,'gamma') for ix in go))
 return r'\,'.join(out).replace('||','')

def canonical_to_parsed(term):
 f=[];go=[];gi=[];fr=[]
 for n,ix in term['factors']:
  if n.startswith('G'):go=[ix]
  elif n.startswith('B'):
   na,da,nb,db,gr=re.fullmatch(r'B([RX])(\d)([RX])(\d)g(\d)',n).groups();da,db,gr=map(int,[da,db,gr]);left=da+(2 if na=='R' else 0)
   fr=[(na,da,ix[:left]),(nb,db,ix[left+gr:])];gi=[ix[left:left+gr]] if gr else []
  else:f.append((n,ix))
 return [term['coefficient'],f,go,gi,fr]

def rank(term):return next((int(n[1:]) for n,ix in term['factors'] if n.startswith('G')),0)
def render(term,coeffonly=True,antisym=False):return render_parsed(canonical_to_parsed(term),coeffonly,antisym)
def formula(terms,coeffonly=True,antisym=False):
 return '\n'.join('&'+coefficient(t['coefficient'],n==0)+render(t,coeffonly,antisym)+r'\\' for n,t in enumerate(terms)) if terms else '&0'
