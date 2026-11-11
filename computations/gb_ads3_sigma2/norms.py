"""Residues of certified gauge-invariant propagators, with precision checks.

Core matrices keep all couplings symbolic. The rational sample points below
are explicitly the numerical checks in v109 Table GBbos, not assumptions used
to derive any matrix or polynomial. Complex roots receive no real norm sign.
"""
import functools
import json
import mpmath as mp
import sympy as s
from flint import fmpq_mpoly,fmpq
from polynomial_matrix import CTX,expr
from model import HERE,L,k,D,S,M2,g,v,ell_s,P2,P3
from closed_forms import cubic,F,nuf

OUT=HERE/'outputs'
LOC={str(x):x for x in (L,k,D,S)}

def unpack_polynomial(p):
    return s.Rational(p['coefficient'])*s.Mul(*(expr(parsed(f))**m for f,m in p['factors']))

@functools.lru_cache(maxsize=None)
def parsed(text):return fmpq_mpoly(text,CTX)

def unpack_fraction(p):
    return unpack_polynomial(p['numerator'])/unpack_polynomial(p['denominator'])

def exact_rational(p):
    from polynomial_matrix import Fraction
    def packed(q):
        value=CTX.constant(fmpq(q['coefficient']))
        for text,power in q['factors']:value*=parsed(text)**power
        return value
    return Fraction(packed(p['numerator']),packed(p['denominator']))

def symbolic_residue(p,root):
    from polynomial_matrix import Fraction,rational
    r=rational(root);value=exact_rational(p)*rational(D-root)
    def at_root(poly):
        grouped={}
        for monomial,c in poly.to_dict().items():
            a=list(monomial);degree=a[2];a[2]=0
            grouped.setdefault(degree,{})[tuple(a)]=c
        out=Fraction(0)
        for degree in range(max(grouped,default=0),-1,-1):
            out=out*r+Fraction(CTX.from_dict(grouped.get(degree,{})))
        return out
    return at_root(value.num)/at_root(value.den)

@functools.lru_cache(maxsize=None)
def exact_coeffs(text,point):
    p=parsed(text).subs({'L':fmpq(point[0]),'k':fmpq(point[1])})
    sig=s.sympify(point[2],locals=LOC)
    grouped={}
    for monomial,c in p.to_dict().items():
        grouped.setdefault(monomial[2],[]).append(s.Rational(str(c))*sig**monomial[3])
    return tuple(s.expand(s.Add(*grouped.get(degree,[]))) for degree in range(max(grouped,default=0),-1,-1))

def number(x):
    re,im=s.sympify(x).expand(complex=True).as_real_imag()
    return mp.mpc(str(re.evalf(mp.mp.dps)),str(im.evalf(mp.mp.dps)))

def coefficients(text,point):return [number(x) for x in exact_coeffs(text,point)]

def polynomial_value(p,point,x):
    value=number(p['coefficient'])
    for text,power in p['factors']:value*=mp.polyval(coefficients(text,point),x)**power
    return value

def residue(p,point,root):
    """Analytic N(r)/[q'(r)*other factors], never a finite difference."""
    den=number(p['denominator']['coefficient']);zeros=0
    for text,power in p['denominator']['factors']:
        coeff=coefficients(text,point);value=mp.polyval(coeff,root)
        scale=sum(abs(c)*max(1,abs(root))**(len(coeff)-1-i) for i,c in enumerate(coeff))
        if abs(value)<mp.mpf(10)**(-mp.mp.dps//2)*max(1,scale):
            assert power==1,'multiple pole requires a separate collision analysis'
            degree=len(coeff)-1
            value=mp.polyval([c*(degree-i) for i,c in enumerate(coeff[:-1])],root)
            zeros+=1
        den*=value**power
    if zeros==0:return mp.mpf(0)
    assert zeros==1,'colliding denominator factors'
    return polynomial_value(p['numerator'],point,root)/den

def roots(expr,point):
    sub={x:s.sympify(value,locals=LOC) for x,value in zip((L,k,S),point)}
    coeff=[number(c) for c in s.Poly(expr.subs(sub),D).all_coeffs()]
    out=mp.polyroots(coeff,maxsteps=1000,extraprec=250,error=False)
    for root in out:
        error=abs(mp.polyval(coeff,root))/sum(abs(c)*max(1,abs(root))**(len(coeff)-1-i) for i,c in enumerate(coeff))
        assert error<mp.mpf(10)**(-mp.mp.dps//2)
    return sorted(out,key=lambda x:(float(mp.re(x)),float(mp.im(x))))

def sign(value):
    assert abs(mp.im(value))<mp.mpf(10)**(-mp.mp.dps//3)*max(1,abs(value)),('non-real norm',value)
    return int(mp.sign(mp.re(value)))

def probe_sign(rec,point,root,spin,probes=None):
    choices=probes or list(rec['probes'])
    values=[residue(rec['probes'][p],point,root) for p in choices]
    nonzero=[x for x in values if abs(x)>mp.mpf(10)**(-mp.mp.dps//3)]
    assert nonzero,('probe has no overlap',choices,root)
    signs={sign((-1)**abs(spin)*mp.sign(mp.re(root)-1)*x) for x in nonzero}
    assert len(signs)==1,('different probe signs',choices,root,signs)
    return signs.pop()

def flat_inertia(rec,point,root):
    names=rec['probe_names'];sig=number(s.sympify(point[2],locals=LOC))
    G=mp.matrix(len(names))
    for i,pa in enumerate(names):
        for j,pb in enumerate(names):
            value=residue(rec['propagator'][i][j],point,root)
            if pa in ('h_p3','h_p4_transverse'):value/=sig
            if pb in ('h_p3','h_p4_transverse'):value/=(1-sig)
            G[i,j]=-mp.sign(mp.re(root)-1)*value
    scale=max(1,mp.norm(G))
    assert mp.norm(G-G.H)<mp.mpf(10)**(-mp.mp.dps//3)*scale, 'harmonic Gram matrix is not Hermitian'
    eig=mp.eighe((G+G.H)/2,eigvals_only=True)
    out=[int(mp.sign(x)) for x in eig if abs(x)>mp.mpf(10)**(-mp.mp.dps//3)*scale]
    assert len(out)==2,('flat residue rank',out)
    return sorted(out)

def numerical_level(Lv,kv,Sv,chi=1,dps=80):
    mp.mp.dps=dps;point=tuple(map(str,(Lv,kv,Sv)))
    prefix='physical_minus_' if chi==-1 else 'physical_'
    recV=json.loads((OUT/(prefix+'n1.json')).read_text())
    recS=json.loads((OUT/(prefix+'n0.json')).read_text())
    recT=json.loads((OUT/'physical_n2.json').read_text())
    recZ=json.loads((OUT/'physical_n1Z.json').read_text())
    level=s.cancel(v*ell_s**2)*S*(S-1)
    output={'L':str(Lv),'k':str(kv),'S':str(Sv),'chi':chi,'spin2':[],'scalar':[]}
    for family,pol in (('spin2',cubic),('scalar',F)):
        for aroot in roots(pol.subs(M2,level),point):
            entry={'D_chi_plus':mp.nstr(aroot,24)}
            if abs(mp.im(aroot))>mp.mpf(10)**(-dps//2):
                entry['norm']='complex energy';output[family].append(entry);continue
            root=aroot if chi==1 else 2-aroot
            partner=(aroot-1 if family=='spin2' else aroot+1)
            if chi==-1:partner=2-partner
            if family=='spin2':
                # TT(-,D)=TT(+,2-D); both the derivative and D-1 reverse.
                norm=probe_sign(recT,point,aroot,2)
            else:norm=probe_sign(recS,point,root,0)
            vn=probe_sign(recV,point,partner,1,probes=['C_p','V_p'])
            alternate=(mp.re(root)-1)*(mp.re(partner)-1)<0
            # In the four crossing cases choose the scalar's smaller root
            # d, and the vector's larger root d+1. Keep the kinetic signs
            # from the action unchanged; no sign is imposed by SUSY.
            h=mp.re(aroot)/2 if alternate or mp.re(aroot)>1 else -mp.re(aroot)/2
            expected=norm*int(mp.sign(h*(h+1)))
            assert vn==expected,('bosonic partner norms',family,point,root,norm,vn,expected)
            entry.update(norm=norm,vector_partner_norm=vn,alternative_quantization=alternate,
                         superalgebra_norm_check='PASS (formal branch)' if alternate else 'PASS')
            if alternate:
                assert family=='scalar' and chi==1 and 0<mp.re(aroot)<1
                reflections={}
                for name in ('L_0','N_0'):
                    lo=residue(recS['probes'][name],point,aroot)
                    hi=residue(recS['probes'][name],point,2-aroot)
                    assert abs(lo+hi)<mp.mpf(10)**(-dps//2)*max(1,abs(lo),abs(hi))
                    # The mass-variable pole residue, hence the kinetic
                    # sign, is invariant under the scalar root exchange.
                    assert sign((aroot-1)*lo)==sign((1-aroot)*hi)==norm
                    reflections[name]={'at_d':mp.nstr(lo,24),'at_2_minus_d':mp.nstr(hi,24),
                                       'residue_reflection':'PASS','mass_residue_norm':norm}
                entry['formal_branch']={
                    'scalar_spin':0,'scalar_energy':mp.nstr(aroot,24),
                    'vector_spin':1,'vector_energy':mp.nstr(1+aroot,24),
                    'supersymmetric_weight_h':mp.nstr(aroot/2,24),
                    'scalar_mass_squared_ell_squared':mp.nstr(aroot*(aroot-2),24),
                    'norm_factor_sign':int(mp.sign(h*(h+1))),
                    'relation':'N_vector = sign[4 h(h+1)] N_scalar; kinetic signs unchanged',
                    'scalar_probe_checks':reflections,
                    'scope':'formal paper branch; no boundary-condition theorem'}
            output[family].append(entry)
    flat=number(nuf.subs({L:Lv,k:kv}));root=flat if chi==1 else 2-flat
    charged=probe_sign(recZ,point,flat,1)
    inertia=flat_inertia(recV,point,root)
    expected=charged*int(mp.sign(mp.re(flat)**2-1))
    assert inertia==[expected,expected]
    assert charged==-int(s.sign(2-s.sympify(Lv)*s.sympify(kv)))
    output['flat']={'D_chi_plus':mp.nstr(flat,24),'charged_norm':charged,'neutral_inertia':inertia}
    return output

def sample_points():
    Q=s.Rational
    return ([(10,Q(1,10),s.Integer(j+1),1) for j in range(2,17)]+
            [(5,-1,s.Integer(j+1),1) for j in (2,3)]+
            [(6,2,Q(1,2)+s.I*nu,1) for nu in (0,1,3)]+
            [(3,Q(6,5),Q(1,2)+s.I*nu,-1) for nu in (Q(1,2),2)])

def verify_samples():
    result=[]
    for point in sample_points():
        a=numerical_level(*point,dps=80);b=numerical_level(*point,dps=140)
        assert a==b,('precision instability',point)
        if point[0:2]==(10,s.Rational(1,10)):
            assert [x['norm'] for x in a['spin2']].count(-1)==1
            assert [x['norm'] for x in a['scalar']].count(-1)==1
            assert a['flat']['neutral_inertia']==[-1,-1]
        result.append(a);print('norms',*point,'80/140 digits PASS',flush=True)
    return {'precision_digits':[80,140],'method':'analytic residues; Hermitian flat residue inertia',
            'scope':'v109 Table GBbos upper block; finite samples do not prove global unitarity',
            'levels':result}

def accumulation_samples():
    """v109 lower Table GBbos: the two towers tending to the flat weights."""
    Q=s.Rational
    groups=[('S2',10,Q(1,10),[10,30,100]),('S2',12,Q(1,20),[10,30,100]),
        ('S2',5,-1,[10,30,100]),('H2',3,Q(1,10),[10,100,1000]),
        ('H2',Q(3,2),Q(1,2),[10,100,1000]),('T2',5,Q(1,5),[10,100,1000]),
        ('T2',8,Q(1,5),[10,100,1000]),('H2',5,1,[100,1000,10000]),
        ('H2',3,2,[100,1000,10000]),('H2',Q(7,2),1,[100,1000,10000]),
        ('H2',Q(7,4),Q(12,5),[100,1000,10000]),('H2',3,Q(1,2),[100,1000,10000]),
        ('H2',5,Q(3,10),[100,1000,10000]),('H2',4,Q(9,20),[100,1000,10000]),
        ('H2',4,Q(11,20),[100,1000,10000])]
    out=[];vell=s.cancel(v*ell_s**2)
    for surface,Lv,kv,levels in groups:
        vals={L:Lv,k:kv};chi=int(s.sign((P3/P2).subs(vals)))
        nu=number(nuf.subs(vals));pref=(-L*k*P3**3/(32*P2**3)).subs(vals)
        rec=json.loads((OUT/('physical_'+('minus_' if chi==-1 else '')+'n0.json')).read_text())
        for level in levels:
            Mval=s.factor(vell.subs(vals))*level*(level+1) if surface=='S2' else s.Integer(level)**2
            sig=s.Integer(level+1) if surface=='S2' else s.Rational(1,2)+s.I*s.sqrt(Mval/(-vell.subs(vals))-s.Rational(1,4)) if surface=='H2' else s.Integer(0)
            point=tuple(map(str,(Lv,kv,sig)));at=[]
            for dps in (80,140):
                mp.mp.dps=dps;nu=number(nuf.subs(vals))
                row={'surface':surface,'L':str(Lv),'k':str(kv),'chi':chi,'level':level,'M2':str(Mval)}
                for family,p,target in (('spin2',cubic,nu+1),('scalar',F,nu-1)):
                    if family=='scalar' and surface=='T2':continue
                    pol=p.subs(M2,Mval);root=min(roots(pol,point),key=lambda a:abs(a-target))
                    if abs(mp.im(root))>mp.mpf(10)**(-dps//2):
                        row[family]={'norm':'complex energy','D_chi_plus':mp.nstr(root,24)};continue
                    if family=='spin2':
                        deriv=s.diff(pol,D).subs(vals)
                        cf=[number(x) for x in s.Poly(deriv,D).all_coeffs()]
                        norm=sign(mp.sign(mp.re(root)-1)/(number(pref)*mp.polyval(cf,root)))
                    else:norm=probe_sign(rec,point,root if chi==1 else 2-root,0)
                    row[family]={'norm':norm,'D_chi_plus':mp.nstr(root,24)}
                if all(x in row and row[x]['norm'] in (1,-1) for x in ('spin2','scalar')):
                    assert row['spin2']['norm']==row['scalar']['norm'],row
                at.append(row)
            assert at[0]==at[1],('accumulation precision',point)
            out.append(at[0])
        print('accumulation norms',surface,Lv,kv,'80/140 digits PASS',flush=True)
    return {'precision_digits':[80,140],'scope':'v109 Table GBbos lower block; finite levels', 'levels':out}

if __name__=='__main__':
    from derive import save
    save('norm_samples',verify_samples())
    save('accumulation_norm_samples',accumulation_samples())
