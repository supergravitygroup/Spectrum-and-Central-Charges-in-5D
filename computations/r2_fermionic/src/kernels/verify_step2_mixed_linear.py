#!/usr/bin/env python3
"""Scoped audit of the project-corrected Ozkan (3.20) mixed specialization.

Printed source coefficients remain separate from working coefficients. The
necessary gradient phase follows from the documented Coomans rigid delta-L
sector, not from fitting the final transcription. Full local supersymmetry
is not proved. Odd bilinears use exterior algebra, not commuting spinors.
"""
# ASSERT_CONVENTION: natural_units=hbar=c=1, metric_signature=mostly_plus (-++++), source_repair_lock=R2-VL-GRADIENT-PHASE-v1
from collections import defaultdict
from itertools import permutations
from pathlib import Path
import hashlib
import json
import re
import sympy as s

ROOT = Path(__file__).resolve().parents[1]
DOC = ROOT/'notes/04_step2_mixed_primed_linear_multiplet.md'
H = s.Rational(1, 2)

# id, printed source coefficient, first/second vector slots, symmetry under B<->C,
# input weight contributions, output weight, bosonic survival.
# External backgrounds, gamma strings and outer derivatives stay attached
# to each row, so they are never commuted across spinors by this bookkeeping.
PRINTED_ROWS = [
 ('L-01',2,'rho','Y',False,[1,2],3,True),
 ('L-02',-s.I/2,'bar_lambda_i','lambda_j',True,[H*3,H*3],3,False),
 ('P-01',s.I,'rho','Dslash_lambda',False,[1,1,H*3],H*7,False),
 ('P-02',2,'rho','lambda',False,[1,1,H*3],H*7,False),
 ('P-03',-8,'rho','rho',True,[1,1,H*3],H*7,False),
 ('P-04',-s.Rational(1,4),'F','lambda',False,[2,H*3],H*7,False),
 ('P-05',H,'Dslash_rho','lambda',False,[1,1,H*3],H*7,False),
 ('P-06',-1,'Y','lambda_j',False,[2,H*3],H*7,False),
 ('E-01',-1,'rho','F',False,[1,1,2],4,True),
 ('E-02',8,'rho','rho',True,[1,1,1,1],4,True),
 ('E-03',-s.I/4,'bar_lambda','lambda',True,[1,H*3,H*3],4,False),
 ('E-04',-s.Rational(1,8),'F','F',True,[2,2],4,True),
 ('N-01',1,'rho','Box_rho',False,[1,2,1],4,True),
 ('N-02',H,'Drho','Drho',True,[2,2],4,True),
 ('N-03',-s.Rational(1,4),'F','F',True,[2,2],4,True),
 ('N-04',1,'Y','Y',True,[2,2],4,True),
 ('N-05',8,'rho','F',False,[1,2,1],4,True),
 ('N-06',-4,'rho','rho',True,[1,1,2],4,True),
 ('N-07',-s.Rational(104,3),'rho','rho',True,[1,1,2],4,True),
 ('N-08',-H,'bar_lambda','Dslash_lambda',False,[H*3,1,H*3],4,False),
 ('N-09',s.I,'bar_lambda','lambda',True,[H*3,1,H*3],4,False),
 ('N-10',16*s.I,'rho','lambda',False,[1,H*3,H*3],4,False),
]


# The mixed gradient coefficient follows from delta L = i barepsilon varphi:
# delta L's selected coefficient is (-i/2)*(-i/2) = -1/4.
# Dividing by the linear-rule factor i gives i/4; divide by the user's
# ordered weight 1/2 to recover the general working coefficient i/2.
DELTA_L_GRADIENT = (-s.I/2)*(-s.I/2)
MIXED_GRADIENT = s.simplify(DELTA_L_GRADIENT/s.I)
GENERAL_GRADIENT = s.simplify(MIXED_GRADIENT/H)
ROWS = [(row[0], GENERAL_GRADIENT, *row[2:]) if row[0]=='P-05' else row
        for row in PRINTED_ROWS]


def clean(poly):
    return {k:s.expand(v) for k,v in poly.items() if s.expand(v)!=0}


def add(*polys):
    out=defaultdict(lambda:s.S.Zero)
    for p in polys:
        for k,v in p.items(): out[k]+=v
    return clean(out)


def scale(poly,c):
    return clean({k:c*v for k,v in poly.items()})


def bilinear(species_left, su_left, species_right, su_right, matrix):
    """Upper-SU(2) components; 16 independent odd generators across two spinors."""
    out=defaultdict(lambda:s.S.Zero)
    for a in range(4):
        for b in range(4):
            i=8*species_left+4*su_left+a
            j=8*species_right+4*su_right+b
            if i==j: continue
            out[tuple(sorted((i,j)))]+=(1 if i<j else -1)*matrix[a,b]
    return clean(out)


EPS=s.Matrix([[0,1],[-1,0]])


def contracted(left,right,matrix):
    return add(*(scale(bilinear(left,i,right,j,matrix),EPS[j,i])
                 for i in range(2) for j in range(2)))


def lower_pair(left,i,right,j,matrix):
    return add(*(scale(bilinear(left,k,right,l,matrix),EPS[k,i]*EPS[l,j])
                 for k in range(2) for l in range(2)))


def sign(p):
    return (-1)**sum(p[i]>p[j] for i in range(len(p)) for j in range(i+1,len(p)))


def main():
    checks=[]
    def check(value,label): checks.append({'pass':bool(value),'check':label})

    selection=json.loads((ROOT/'notes/multiplet_selection.json').read_text())
    check(selection['coefficients']=={'111':'0','112':'1/2','121':'1/2','122':'0'},'exact user coefficient slice')
    check(selection['labels']=={'1':'primed composite vector','2':'unprimed defining vector'},'unchanged primed/unprimed roles')
    check([r[0] for old,r in zip(PRINTED_ROWS,ROWS) if old!=r]==['P-05'],
          'only the established gradient phase changes among the 22 printed coefficients')
    check(next(r[1] for r in PRINTED_ROWS if r[0]=='P-05')==H,
          'printed P-05 is explicitly retained as +1/2')
    check(DELTA_L_GRADIENT==-s.Rational(1,4) and s.I*MIXED_GRADIENT==DELTA_L_GRADIENT,
          'Coomans selected delta-L coefficient fixes the mixed phase')
    check(s.I*H/2!=DELTA_L_GRADIENT,
          'printed mixed +1/4 fails the same necessary transformation condition')
    check(GENERAL_GRADIENT==s.I/2 and H*GENERAL_GRADIENT==s.I/4,
          'general repaired +i/2 receives the user weight exactly once')
    for key,c,x,z,symmetric,weights,target,bos in ROWS:
        # Four labels encode the actual source factors. They are noncommuting
        # regardless of parity to prevent accidental algebraic reordering.
        xp,xu,zp,zu=s.symbols('xp xu zp zu',commutative=False)
        direct=sum(weight*c*left*right for weight,left,right in
                   [(0,xp,zp),(H,xp,zu),(H,xu,zp),(0,xu,zu)])
        polarized=H*c*((xp+xu)*(zp+zu)-xp*zp-xu*zu)
        check(s.expand(direct-polarized)==0,key+' direct sum equals independent polarization')
        expected={(1,2):H*c,(2,1):H*c}
        actual={(1,2):s.expand(direct).coeff(xp*zu),(2,1):s.expand(direct).coeff(xu*zp)}
        check(actual==expected,key+' both ordered coefficients')
        collected=defaultdict(lambda:s.S.Zero)
        for pair,coef in actual.items():
            collected[(1,2) if symmetric else pair]+=coef
        check(dict(collected)==({(1,2):c} if symmetric else expected),key+' collected coefficient multiplicity')
        check(sum(weights)==target,key+' exact Weyl weight')
        check(s.expand(direct.xreplace({xp:xu,zp:zu})-c*xu*zu)==0,key+' equal-input working-map normalization')
        check(direct.xreplace({xp:s.S.Zero,zp:s.S.Zero})==0 and
              direct.xreplace({xu:s.S.Zero,zu:s.S.Zero})==0,key+' either zero argument')
        exchanged=direct.xreplace({xp:xu,xu:xp,zp:zu,zu:zp})
        check(s.expand(direct-exchanged)==0,key+' input exchange symmetry before collection')
    check([r[0] for r in ROWS if r[-1]]==['L-01','E-01','E-02','E-04']+[f'N-{i:02d}' for i in range(1,8)],'bosonic survivor ledger')

    # Explicit mostly-plus Clifford representation with product +i identity.
    p1=s.Matrix([[0,1],[1,0]]);p2=s.Matrix([[0,-s.I],[s.I,0]]);p3=s.diag(1,-1)
    I2=s.eye(2);I4=s.eye(4);zero=s.zeros(4);eta=[-1,1,1,1,1]
    g=[s.I*s.kronecker_product(p1,I2),s.kronecker_product(p2,I2),
       s.kronecker_product(p3,p1),s.kronecker_product(p3,p2),-s.kronecker_product(p3,p3)]
    C=s.Matrix([[0,0,0,-1],[0,0,1,0],[0,-1,0,0],[1,0,0,0]])
    check(C.T==-C and C.conjugate().T*C==I4,'antisymmetric unitary charge conjugation')
    check(g[0]*g[1]*g[2]*g[3]*g[4]==s.I*I4,'gamma orientation product +i')
    for a in range(5):
        for b in range(5):
            check(g[a]*g[b]+g[b]*g[a]==(2*eta[a]*I4 if a==b else zero),f'Clifford ({a},{b})')
        check((C*g[a]).T==-C*g[a],f'rank-one C gamma transpose {a}')
        check(contracted(0,1,C*g[a])==scale(contracted(1,0,C*g[a]),-1),f'Grassmann contracted rank-one flip {a}')
    for i in range(2):
        for j in range(2):
            first=scale(add(lower_pair(0,i,1,j,C),lower_pair(0,j,1,i,C)),H)
            second=scale(add(lower_pair(1,i,0,j,C),lower_pair(1,j,0,i,C)),H)
            check(first==second,f'Grassmann symmetric scalar triplet flip ({i},{j})')
    for a in range(5):
        for b in range(a+1,5):
            gab=(g[a]*g[b]-g[b]*g[a])/2
            check((C*gab).T==C*gab,f'rank-two C gamma transpose ({a},{b})')
            check(contracted(0,1,C*gab)==contracted(1,0,C*gab),f'Grassmann contracted rank-two flip ({a},{b})')
    for p in permutations(range(5)):
        swapped=(p[0],p[3],p[4],p[1],p[2])
        check(sign(p)==sign(swapped),'epsilon two-pair exchange '+str(p))

    # Exact independent bosonic contractions with nontrivial Lorentz signs.
    F=s.Matrix(5,5,lambda a,b:(a+2)*(b+1) if a<b else 0);F=F-F.T
    G=s.Matrix(5,5,lambda a,b:a*a+b+3 if a<b else 0);G=G-G.T
    check(sum(eta[a]*eta[b]*F[a,b]*G[a,b] for a in range(5) for b in range(5))==
          sum(eta[a]*eta[b]*G[a,b]*F[a,b] for a in range(5) for b in range(5)), 'mixed Lorentz strength contraction')
    Y=s.Matrix([[2,3],[3,5]]);Z=s.Matrix([[7,-2],[-2,11]])
    raisedY=EPS*Y*EPS.T;raisedZ=EPS*Z*EPS.T
    check(sum(Y[i,j]*raisedZ[i,j] for i in range(2) for j in range(2))==
          sum(Z[i,j]*raisedY[i,j] for i in range(2) for j in range(2)), 'two-epsilon triplet contraction')

    # Closed polynomial field strengths give an exact flat bosonic divergence
    # check independent of the abstract epsilon-pair identity above.
    xx=s.symbols('x0:5')
    A=[(i+1)*xx[(i+1)%5]**2+xx[(i+2)%5]*xx[(i+3)%5] for i in range(5)]
    B=[(i+2)*xx[(i+2)%5]**3+xx[i]*xx[(i+4)%5] for i in range(5)]
    f=s.Matrix(5,5,lambda a,b:s.diff(A[b],xx[a])-s.diff(A[a],xx[b]))
    h=s.Matrix(5,5,lambda a,b:s.diff(B[b],xx[a])-s.diff(B[a],xx[b]))
    rho=1+sum((i+1)*x*x for i,x in enumerate(xx));rhop=2+sum(xx[i]*xx[(i+1)%5] for i in range(5))
    Ee=[]
    for a in range(5):
        curl=sum(s.diff(-H*eta[a]*eta[b]*(rhop*f[a,b]+rho*h[a,b]),xx[b]) for b in range(5))
        top=sum(sign((a,)+p)*h[p[0],p[1]]*f[p[2],p[3]] for p in permutations([b for b in range(5) if b!=a]))
        Ee.append(s.expand(curl-top/8))
    check(s.expand(sum(s.diff(Ee[a],xx[a]) for a in range(5)))==0,'flat bosonic E divergence with closed polynomial strengths')

    # Tie the four actually delivered final equations to this scoped audit.
    text=DOC.read_text(); final=text.split('## 6. Final Result')[1].split('## 7.')[0]
    formulas=re.findall(r'^\$\$\s*\n(.*?)\n\$\$$',final,re.M|re.S)
    check(len(formulas)==4,'four final component equations')
    expected=[
        r"L'_{ij}=\rho'Y_{ij}+\rho Y'_{ij}-\frac i2\bar\lambda'_{(i}\lambda_{j)}.",
        r"\varphi'_i=\frac i2(\rho'\not{\mathcal D}\lambda_i+\rho\not{\mathcal D}\lambda'_i)+\rho'\gamma\!\cdot\!T\lambda_i+\rho\gamma\!\cdot\!T\lambda'_i-8\rho'\rho\chi_i-\frac18(\gamma\!\cdot\!\widehat F'\lambda_i+\gamma\!\cdot\!\widehat F\lambda'_i)+\frac i4\big((\not{\mathcal D}\rho')\lambda_i+(\not{\mathcal D}\rho)\lambda'_i\big)-\frac12(Y'_{ij}\lambda^j+Y_{ij}\lambda'^j).",
        r"E'^a=\mathcal D_b\left[-\frac12(\rho'\widehat F^{ab}+\rho\widehat F'^{ab})+8\rho'\rho T^{ab}-\frac i4\bar\lambda'\gamma^{ab}\lambda\right]-\frac18\varepsilon^{abcde}\widehat F'_{bc}\widehat F_{de}.",
        r"N'=\frac12(\rho'\Box_c\rho+\rho\Box_c\rho')+\frac12\mathcal D_a\rho'\mathcal D^a\rho-\frac14\widehat F'_{ab}\widehat F^{ab}+Y'_{ij}Y^{ij}+4(\rho'\widehat F_{ab}+\rho\widehat F'_{ab})T^{ab}-4\rho'\rho\left(D+\frac{26}{3}T^2\right)-\frac14(\bar\lambda'\not{\mathcal D}\lambda+\bar\lambda\not{\mathcal D}\lambda')+i\bar\lambda'\gamma\!\cdot\!T\lambda+8i(\rho'\bar\chi\lambda+\rho\bar\chi\lambda')."]
    for i,(formula,want) in enumerate(zip(formulas,expected)):
        formula=re.sub(r'\\tag\{\d+\}','',formula).strip()
        formula=formula.removeprefix(r'\boxed{').removesuffix('}')
        formula=formula.replace(r'\begin{aligned}','').replace(r'\end{aligned}','').replace(r'\\','').replace('&','')
        normalize=lambda t:re.sub(r'\s+','',t).replace('{}','')
        check(normalize(formula)==normalize(want),f'final delivered component {i+1} matches audited transcription')
    # Bind the actually printed-source and working maps to distinct equations.
    all_equations={}
    for block in re.findall(r'^\$\$\s*\n(.*?)\n\$\$$',text,re.M|re.S):
        match=re.search(r'\\tag\{(\d+[a-z]?)\}',block)
        if match: all_equations[match.group(1)]=block
    compact=lambda x:re.sub(r'\s+','',x)
    literal=all_equations['3'];working=all_equations['3a']
    converted=literal.replace(r'\left.\varphi_{i,A}\right|_{\rm printed}',r'\varphi_{i,A}').replace(
        r'+\frac12(\not{\mathcal D}\rho^B)\lambda_i^C',
        r'+\frac i2(\not{\mathcal D}\rho^B)\lambda_i^C').replace(r'\tag{3}',r'\tag{3a}')
    check(r'+\frac12(\not{\mathcal D}\rho^B)\lambda_i^C' in literal,
          'Eq. (3) honestly quotes the printed +1/2')
    check(compact(converted)==compact(working),
          'Eq. (3a) changes only the phase of the general gradient tensor')
    # Check each displayed weighting stage rather than only the final formula.
    for token in [r"+\frac i2(\not{\mathcal D}\rho')\lambda_i",
                  r"+\frac i2(\not{\mathcal D}\rho)\lambda'_i"]:
        check(token in all_equations['19'],'Eq. (19) retains repaired ordered term '+token)
    expected_gradient_weighting=r"\frac12\left(\frac i2(\not{\mathcal D}\rho')\lambda_i\right)+\frac12\left(\frac i2(\not{\mathcal D}\rho)\lambda'_i\right)=\frac i4\left((\not{\mathcal D}\rho')\lambda_i+(\not{\mathcal D}\rho)\lambda'_i\right).\tag{24}"
    check(compact(all_equations['24'])==compact(expected_gradient_weighting),
          'Eq. (24) shows both actual i/2 times 1/2 products and their i/4 sum')
    for tag,delim in [('26',r'\left'),('57',r'\big')]:
        check(compact(r"+\frac i4"+delim+r"((\not{\mathcal D}\rho')\lambda_i+(\not{\mathcal D}\rho)\lambda'_i") in compact(all_equations[tag]),
              'Eq. ('+tag+') has the repaired gradient pair')
    check(r'=\fraci2(\not{\mathcalD}\rho)\lambda_i' in compact(all_equations['51']),
          'Eq. (51) includes the corrected coincident-input gradient coefficient')
    check('| $i/2$ (printed: $1/2$) | $i/4$ |' in text,
          'P-05 ledger distinguishes the printed and working coefficients')
    tags=re.findall(r'\\tag\{(\d+[a-z]?)\}',text)
    check(tags==['1','2','3','3a','3b','3c','3d']+[str(i) for i in range(4,60)],
          '59 original equation tags plus four explicit repair tags in order')
    check(all(f'## {i}. {heading}' in text for i,heading in enumerate([
        'Problem and Target','Convention Ledger','Definitions and Required Identities',
        'Detailed Derivation','Consistency Checks','Final Result',
        'Convention Dependence and Remaining Uncertainties'],1)), 'seven required derivation sections')
    check(not any(x in text for x in [r'\[',r'\]',r'\(',r'\)']), 'dollar math delimiters')
    failures=[c['check'] for c in checks if not c['pass']]
    report={'status':'FAIL' if failures else 'PASS','checks':len(checks),'failures':failures,
            'scope':'Project-repaired Eq. (3.20) specialization: explicit printed/working coefficient separation, necessary rigid delta-L coefficient arithmetic, actual displayed repaired weighting stages, weights, ordering, Grassmann flips, polarization, stated limits and flat bosonic constraint',
            'not_checked':['full local supersymmetry','complete source reality and convention audit','full supercovariant constraint','Gold/earlier vector maps','gauged background expansion','BF insertion'],
            'source_rows':len(ROWS),'ordered_contributions':2*len(ROWS),'result_lock':'R2-MIXED-PRIMED-LINEAR-v2','source_repair_lock':'R2-VL-GRADIENT-PHASE-v1','printed_gradient_coefficient':str(H),'working_gradient_coefficient':str(GENERAL_GRADIENT),
            'document':str(DOC.relative_to(ROOT)),'document_sha256':hashlib.sha256(DOC.read_bytes()).hexdigest(),
            'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'sympy_version':s.__version__,'details':checks}
    (ROOT/'build/step2_mixed_linear_verification.json').write_text(json.dumps(report,indent=2)+'\n')
    print(f"{report['status']}: {len(checks)} scoped checks; 22 working rows, 44 ordered contributions; literal source separately retained.")
    for f in failures: print('FAIL:',f)
    return bool(failures)


if __name__=='__main__': raise SystemExit(main())
