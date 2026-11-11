#!/usr/bin/env python3
"""Recheck notebook Part V. Requires SymPy; independent component subprocess uses NumPy.
Run with ambient python3. No external network, EOM or nonlinear closure test.
"""
from weyl_clifford_algebra import *
from weyl_clifford_notation import render,rank
import hashlib,subprocess,sys,tempfile,time
start=time.time();ledger=PH/'CLIFFORD-COLLECTION-LEDGER.json';j=json.loads(ledger.read_text());note=(PH/'DERIVATION-fermionic-map.md').read_text();part=note.split('# Part V —',1)[1]
checks={};inputs=component_inputs();assert len(inputs)==len(j['rows'])==602
key=lambda fs:tuple((n,tuple(ix)) for n,ix in fs)
rewrite={key(r['input']):(S.sympify(r['factor']),key(r['output'])) for r in j['schouten_rewrites']}
total=defaultdict(lambda:S.Integer(0))
for n,(src,row) in enumerate(zip(inputs,j['rows'])):
 serialized=json.loads(json.dumps([[str(c),f,go,gi,fr] for c,f,go,gi,fr in src['parsed']]))
 assert serialized==row['projected_input'],row['equation']
 ans,_=evaluate_parsed(src['parsed']);collected=defaultdict(lambda:S.Integer(0))
 for k,c in ans.items():
  if k in rewrite:m,k=rewrite[k];c*=m
  collected[k]+=c
 collected={k:S.expand(c) for k,c in collected.items() if c}
 expect={key(t['factors']):S.sympify(t['coefficient']) for t in row['terms']}
 assert collected==expect,row['equation']
 for k,c in collected.items():total[k]+=c
 assert r'\tag{'+row['equation']+'}' in part
 if n%150==149:print('Exact contribution reductions:',n+1,'/602',flush=True)
total={k:S.expand(c) for k,c in total.items() if c}
expected={key(t['factors']):S.sympify(t['coefficient']) for t in j['terms']};assert total==expected
checks['exact_reduction_and_addition']={'status':'PASS','contributions':602,'final_terms':85,'counts':j['counts'],'arithmetic':'rational complex','source_terms':586}
for t in j['terms']:
 weight=0;cnt=Counter()
 for nm,ix in t['factors']:
  cnt.update(ix)
  if nm.startswith('G') or nm=='E':continue
  if nm.startswith('B'):
   a,da,b,db,gr=re.fullmatch(r'B([RX])(\d)([RX])(\d)g(\d)',nm).groups();weight+=3+int(da)+int(db);assert int(gr)<=2
  elif nm=='D2':weight+=4
  else:weight+={'T':1,'D':2,'C':2,'V':2}[nm[0]]+(int(nm[-1]) if 'd' in nm else 0)
 assert weight==4 and all(v==2 for v in cnt.values())
 assert rank(t)<=2
 assert render(t,True,rank(t)==2) in part.split('## 35. Final Result',1)[1]
checks['weights_indices_and_final_display']={'status':'PASS','all_weights':4,'final_terms':85,'full_ordered_pair_normalization':True}
# Input to a separately implemented NumPy evaluator. No symbolic reducer is imported there.
original=[[str(c),f,go,gi,fr] for r in SOURCE for c,f,go,gi,fr in parse(r)]
blades=[x for n in range(6) for x in it.combinations(range(5),n)];basis=[]
for a,b in it.product(blades,repeat=2):
 ts=blade_product(tuple(map(str,a)),tuple(map(str,b)))
 basis.append({'left':a,'right':b,'terms':[[str(c),list(map(int,g)),[[int(x),int(y)] for x,y in m]] for c,g,m in ts]})
with tempfile.TemporaryDirectory(prefix='weyl_clifford_') as tmp:
 ip=Path(tmp)/'inputs.json';op=Path(tmp)/'checks.json';ip.write_text(json.dumps({'original':original,'reduced':j['terms'],'rows':j['rows'],'basis_products':basis}))
 # Use the existing bundled runtime with NumPy, without installing or changing dependencies.
 np_python=Path(__import__('sys').executable)
 assert np_python.is_file(),'NumPy runtime missing; select an existing Python with NumPy.'
 subprocess.run([str(np_python),str(BASE/'scripts/weyl_clifford_components.py'),str(ip),str(op)],check=True)
 checks.update(json.loads(op.read_text()))
checks['scope']='Clifford/Fierz collection of supplied v5/M08 singlet only; no independent nonlinear closure, curvature-commutator cancellation, multiplet matching, invariant or spectrum claim.'
checks['ledger_sha256']=hashlib.sha256(ledger.read_bytes()).hexdigest();checks['notebook_sha256']=hashlib.sha256((PH/'DERIVATION-fermionic-map.md').read_bytes()).hexdigest();checks['elapsed_seconds']=round(time.time()-start,3)
(PH/'CLIFFORD-COLLECTION-CHECKS.json').write_text(json.dumps(checks,indent=2)+'\n')
print('PASS: complete Clifford collection; 22 scalar + 34 vector + 29 bivector contractions.')
