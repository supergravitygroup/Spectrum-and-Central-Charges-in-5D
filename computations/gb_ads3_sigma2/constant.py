"""Independent constant-scalar harmonic reduction (fixed magnetic flux).

Adapted from v42 stage1_l0; all g, lambda=k/g**2 and L remain symbolic.
The local exponential harmonic ansatz cannot obtain this level by S=0.
"""
import sympy as s
from model import L,k,g,D,v,ell_s,branch,encode_matrix
from physical import pack_polynomial
from polynomial_matrix import rational,primitive_in_D,rational_inverse,polynomial_rows

def background_density(Lx,Nx,hx,px,rx,vx,ux,lam,gx):
    R=6*ux+2*vx
    two=Lx*(R-px**2+8*hx**2)-2*Nx**2/Lx-2*gx*Lx*Nx-4*gx*Nx+2*gx**2*Lx**2-gx**2*Lx**3/2
    gb=(3*ux*vx+6*ux*px*hx-4*vx*hx**2+8*px*hx**3+2*s.sqrt(2)*gx*Lx*rx*hx-4*gx*Nx*px*hx
        +gx**2*Lx**2*(-(3*ux+vx)/2+px**2/2-px*hx-6*hx**2)+gx**2*Nx**2+2*gx**3*Nx*Lx**2+gx**4*Lx**4/2)
    return two+lam*gb

def scalar():
    psi,A,H,N=s.symbols('psi A H N')
    p0,r0,v0,u,lam=s.symbols('p0 r0 v0 u lam')
    fields=[psi,A,H,N]; exp=s.exp(2*psi)
    P=p0/exp;rho=r0/exp;vv=v0/exp
    kap=exp*(A+lam*P*H-lam*g**2*A**2/4)+lam*v0/2
    U=-(exp*background_density(A,N,H,P,rho,vv,0,lam,g)-(4/g)*(s.sqrt(2)*r0+2*g*p0)*H)
    B=branch(); sub={psi:0,A:L,H:B['h'],N:B['N'],p0:B['p'],r0:v,v0:v,u:-1/ell_s**2,lam:k/g**2}
    def ev(e):return s.factor(e.subs(sub,simultaneous=True))
    kap0=ev(kap);U0=ev(U)
    dk=s.Matrix([ev(s.diff(kap,f)) for f in fields])
    dU=s.Matrix([ev(s.diff(U,f)) for f in fields])
    ddk=s.Matrix(4,4,lambda i,j:ev(s.diff(kap,fields[i],fields[j])))
    ddU=s.Matrix(4,4,lambda i,j:ev(s.diff(U,fields[i],fields[j])))
    assert s.cancel(U0+2*kap0/ell_s**2)==0
    assert (dU-3*U0*dk/kap0).applyfunc(s.cancel).is_zero_matrix
    K=s.zeros(4)
    K[0,0]=ev(exp*(2*A+4*lam*H**2-lam*g**2*A**2/2)+lam*u)
    K[0,1]=K[1,0]=ev(exp*(2-lam*g**2*A))
    K[1,1]=ev(exp*(1/A-lam*g**2/2))
    KE=(K-2*dk*dk.T/kap0).applyfunc(s.factor)
    HE=(ddU-3*(dU*dk.T+dk*dU.T+U0*ddk)/kap0+12*U0*dk*dk.T/kap0**2).applyfunc(s.factor)
    scale=s.diag(1,1,g/s.sqrt(2),g)
    kinetic=(scale*KE*scale).applyfunc(s.factor)
    potential=(2/g**2*scale*HE*scale).applyfunc(s.factor)
    pencil=(-2/(g**2*ell_s**2)*kinetic*D*(D-2)-potential/2).applyfunc(s.factor)
    assert not any(e.has(g) for e in list(pencil)+list(kinetic))
    reduced=(pencil[:3,:3]-pencil[:3,3]*pencil[3,:3]/pencil[3,3]).applyfunc(s.factor)
    return dict(fields=['psi','L','H','N'],kappa=str(kap0),
        kinetic=[[str(e) for e in row] for row in kinetic.tolist()],
        potential_hessian=[[str(e) for e in row] for row in potential.tolist()],
        K=[[str(e) for e in row] for row in pencil.tolist()],
        N_eliminated=[[str(e) for e in row] for row in reduced.tolist()],
        stationary_Einstein_potential=True,curvature_equation=True),reduced

def vector():
    c,e,z,m=s.symbols('c e z m');B=branch();lam=k/g**2
    p,h,r,N,u=B['p'],B['h'],v,B['N'],-1/ell_s**2
    hh=s.Symbol('hh');k0=p*c+g*e/2
    Fh=s.diff(background_density(L,N,hh,p,r,v,u,lam,g),hh).subs(hh,h)
    terms=[(-L/2+lam*(-p*h+g**2*L**2/4))*(-2*m**2*c**2),
        (1/(4*L)-lam*g**2/8)*(-2*m**2*e**2),
        (-2*L+lam*(u+4*h**2+s.Rational(3,2)*g**2*L**2))*k0**2,
        s.sqrt(2)*m*z*e,2*g*m*c*e,-Fh*m*c**2/4,
        lam*(-v+p**2-4*p*h+2*g*N+g**2*L**2/2)*m*k0*c,
        lam*p*m*k0**2/2,-lam*p*m**3*c**2/2,-lam*p*m*z**2/2,
        -lam*r*m*c*z,-s.sqrt(2)*lam*g*L*m*k0*z,
        lam*g*p*m**2*e*c/2,2*lam*g*h*m*e*k0]
    q=sum(terms);Q=s.hessian(q,(c,e,z))/2
    scale=s.diag(1,s.sqrt(2),g/s.sqrt(2))
    Q=(2/g**2*scale*Q.subs(m,(D-1)/ell_s)*scale).applyfunc(s.factor)
    assert not any(x.has(g) for x in Q)
    T=s.Matrix([[1,0],[-L,0],[0,1]])
    assert (Q.subs(D,1)*T).applyfunc(s.cancel).is_zero_matrix
    cs=(T.T*s.diff(Q,D).subs(D,1)*T).applyfunc(s.factor)
    rlevel=s.factor(cs[1,1]-cs[1,0]**2/cs[0,0])
    from closed_forms import kappa,mul
    assert s.cancel(rlevel-kappa*(1-1/mul)/2)==0
    return dict(fields=['c','e','V'],curl='m=(D-1)/ell_s',
                K=[[str(x) for x in row] for row in Q.tolist()],
                current_basis='(c,e,V)=(c,-L*c,V)',
                current_CS=[[str(x) for x in row] for row in cs.tolist()],
                extremized_R_level=str(rlevel),
                R_level_to_Einstein_left_factor='1/2',
                mixing_exception='k=2/3: flavor self and mixed anomalies vanish; retain full matrix',
                term_ids=['C-Maxwell','E-Maxwell','Stueckelberg','EV','EC','flux-CS',
                    'K-curl-C','K-CS','C-third-order','V-CS','CV-CS','KV','EGG','EHH']),Q

def derive():
    from closed_forms import rr,mul,kappa
    sr,KS=scalar();vr,KV=vector()
    # The matrices are small; use the same exact rational determinant engine.
    def determinant(K):
        A,scales=polynomial_rows(K)
        _,d=rational_inverse(A,with_det=True)
        for scale in scales:d=d/rational(scale)
        return d
    ds=determinant(KS);dv=determinant(KV)
    targetS=rational(rr*rr.subs(D,2-D))
    assert primitive_in_D(ds.num)==primitive_in_D(targetS.num)
    targetV=rational((D-1)**2*(D-mul)*rr.subs(D,D-1))
    ratio=dv/targetV
    assert ratio.num.degrees()[2]<=0 and ratio.den.degrees()[2]<=0
    vr['massive_partner_verified']=True
    # Retain the two zero-curl gauge factors in the saved full determinant.
    vr['determinant']={'numerator':pack_polynomial(dv.num),'denominator':pack_polynomial(dv.den)}
    sr['physical_divisor']=pack_polynomial(primitive_in_D(ds.num))
    sr['R_shadow_verified']=True
    assert s.cancel(s.sympify(sr['kappa'])-kappa)==0
    return dict(scalar=sr,vector=vr,
                assumptions='L>0, g>0; regular branch; k kept symbolic')
