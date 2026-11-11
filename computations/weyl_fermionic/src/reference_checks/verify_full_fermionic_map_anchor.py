"""Check the anchored four-component map against the derived master formulas.
Verifies literal L/varphi tensors and exact N=2p, E=2it coefficients.
This is a transcription check, not a new multiplet-closure test.
"""
from pathlib import Path
from fractions import Fraction
import re,json,hashlib
B=Path(__file__).resolve().parents[1]
P=B/'.gpd/phases/02-ozkan-map-and-variation-completion'
master=(B/'.gpd/CONVENTIONS.md').read_text();anchor=(B/'notes/04_full_fermionic_weyl_linear_map.md').read_text()
def equation(text,tag):
 before=text.split('\\tag{'+tag+'}',1)[0]
 assert len(before)<len(text)
 block=before.rsplit('\\begin{aligned}',1)[1].split('\\end{aligned}',1)[0]
 block=re.sub(r'\\hspace\{[^}]*\}','',block)
 block=block.replace('\\\\','').replace('&','')
 block=re.sub(r'\s+','',block)
 block=block.split('=',1)[1]
 if block.startswith('{}'):block=block[2:]
 return block.rstrip('.')
def split_sum(s):
 depth=0;start=0;out=[]
 for i,c in enumerate(s):
  if c in '{[(':depth+=1
  if c in '}])':depth-=1
  assert depth>=0,(s,i)
  if c in '+-' and depth==0 and i>start:
   out.append(s[start:i]);start=i
 out.append(s[start:]);assert depth==0
 return out
def atom(s):
 if s[0]=='{':
  end=s.index('}');return s[1:end],s[end+1:]
 return s[:1],s[1:]
def coefficient(term):
 sign=-1 if term[0]=='-' else 1
 if term[0] in '+-':term=term[1:]
 imag=0
 if term.startswith('\\frac'):
  a,term=atom(term[5:]);b,term=atom(term)
  if 'i' in a:imag=1;a=a.replace('i','') or '1'
  value=Fraction(a)/Fraction(b)
 else:
  m=re.match(r'\d+',term)
  value=Fraction(m[0]) if m else Fraction(1)
  if m:term=term[len(m[0]):]
 if term.startswith('i'):imag+=1;term=term[1:]
 return (sign*value,imag),term
def multiply_i(c,n,phase):
 r,k=c;k+=phase
 return (r*n*(-1)**(k//2),k%2)
report={'status':'PASS','reference_id':'UNG-WEYL2-FERMIONIC-MAP-v1','convention_lock':'UNG-WEYL2-OP58-CONVENTIONS-v5','checks':{}}
for old,new,label in [('M01','FM01','L'),('M08','FM02','varphi')]:
 a=equation(master,old);b=equation(anchor,new)
 assert a==b,(label,a,b)
 report['checks'][label]={'status':'PASS','tensor_and_coefficient_equality':'literal modulo whitespace, display braces and composite component label','terms':len(split_sum(a))}
for old,new,label,n,phase in [('M13c','FM04','N',2,0),('M14c','FM03','E',2,1)]:
 a=split_sum(equation(master,old));b=split_sum(equation(anchor,new));assert len(a)==len(b),(label,len(a),len(b))
 rows=[]
 for j,(x,y) in enumerate(zip(a,b),1):
  co,body=coefficient(x);cn,newbody=coefficient(y)
  if label=='E' and body.startswith('\\mathcalD_b\\Big['):
   assert co==cn==(Fraction(1),0)
   aa=split_sum(body.split('\\Big[',1)[1].rsplit('\\Big]',1)[0]);bb=split_sum(newbody.split('\\Big[',1)[1].rsplit('\\Big]',1)[0]);assert len(aa)==len(bb)==6
   for k,(v,w) in enumerate(zip(aa,bb),1):
    cv,bv=coefficient(v);cw,bw=coefficient(w)
    assert bv==bw,(label,j,k,bv,bw)
    assert multiply_i(cv,n,phase)==cw,(label,j,k,cv,cw)
    rows.append({'outer_term':j,'inside_product_derivative':k,'source_coefficient':[str(cv[0]),cv[1]],'map_coefficient':[str(cw[0]),cw[1]]})
  else:
   assert body==newbody,(label,j,body,newbody)
   assert multiply_i(co,n,phase)==cn,(label,j,co,cn)
   rows.append({'outer_term':j,'source_coefficient':[str(co[0]),co[1]],'map_coefficient':[str(cn[0]),cn[1]]})
 report['checks'][label]={'status':'PASS','multiplier':'2i' if phase else '2','tensor_bodies_and_derivative_order':'identical','coefficient_comparisons':len(rows),'details':rows}
assert anchor.count('$$')%2==0
for b in anchor.split('$$')[1::2]:
 level=0
 for c in re.sub(r'\\[{}]','',b):
  level+=(c=='{')-(c=='}');assert level>=0
 assert level==0
for label in ['FM01','FM02','FM03','FM04','FM05','FM06','FM07']:assert anchor.count('\\tag{'+label+'}')==1
report['document_checks']={'status':'PASS','unique_equations':7,'math_delimiters_and_braces':'balanced','pending_laws_explicit':all(x in anchor for x in ['FM06 is the **target law**','**not newly proved identities**'])}
report['anchor_sha256']=hashlib.sha256((B/'notes/04_full_fermionic_weyl_linear_map.md').read_bytes()).hexdigest()
report['scope']='Consolidation and exact transcription/normalization check only. No new independent supersymmetry or divergence verification.'
(P/'FULL-FERMIONIC-MAP-ANCHOR-CHECKS.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({k:v for k,v in report.items() if k!='checks'},indent=2))
print({k:(v.get('terms',v.get('coefficient_comparisons'))) for k,v in report['checks'].items()})
