"""Two-derivative two-fermion action, eq. (5.10) of
common/two_derivative_action/details/construction.md,
with the slots (4.19), (4.21), (4.24), (4.30),
(4.32), (5.5) and the dependent connections of Sec. 3.4 (phi_mu, R(Q), f, R'(M) with the corrected chi term).
Evaluated on the supersymmetric AdS3 x Sigma2 background in the zero-momentum engine (fengine.py).

Background (stage-2 variables, background.py): G_34=p, (dV)_34=r with V_3=r/w (V_3=0 on T2), E_{012}=-4h/g,
H_{012}=(g/2)E_{012}, L, N constant, E^a=0, V'=0.  Hence T_34=(p-2h)/8.

Terms that vanish on this background and are therefore not coded (each checked in the comments below):
 * products of two factors whose bosonic parts vanish (D_aL_ij, E_a: both zero on the background);
 * total derivatives with constant coefficients (divergence of D_aL^{ij(2)} in (4.32), the torsion part of R'(M),
   and E^{mu nu}(d_mu E_nu^(2) + d_mu(phibar gamma_nu phi)) which integrate to -(nabla_mu E^{mu nu})(...) = 0);
 * the delta_ij V_a^i_k D^aL^{jk} term of (4.32) (vanishes by symmetry of D^aL^{jk});
 * the two chibar-varphi terms of the triplet slot, which cancel identically after contraction with L^{ij}.
The field-strength block (1/2) F_{mu nu} E^{mu nu} of (5.10) is evaluated in full (fblock='full', default): every D in
it is the full supercovariant derivative, including the one in -sqrt2 D_[mu(L^-2 delta_ij phibar^i gamma_nu] phi^j),
whose Q- and S-connection terms (those of D_mu varphi) are psibar-varphi bilinears.  The pure-curl parts
(d_[mu E^(2)_nu], d_[mu(phibar gamma_nu phi)]) integrate to zero against the covariantly constant E^{mu nu}.
On this background the block vanishes identically (checks.py), as it must: it is the integrated-by-parts form of
A_mu P^mu, with P^mu fermion-free and zero here.  fblock='none' omits it (same K).  fblock='ordinary' keeps only the
ordinary derivative in the phibar-gamma-phi term; that misreading makes F^(2) non-closed and breaks local
supersymmetry (diagnostic only)."""
import numpy as np, symengine as se, sympy as sp, itertools
from clifford import GU, GL, ETA, gam, J, PAIR_NWSE as NW, PAIR_DELTA as DL, epsU, epsL
from fengine import Sp, Frame, bil, build_fields, zarr, ex
R5=range(5)
I=se.I; s2=se.sqrt(2)

def bg_fields(bg):
    # This is the LR summand, also evaluated on a nonzero-k background.
    # Its caller assembles LR + lambda_GB*(-2 W - 4 LOG).
    l,w,g,L,N,p,h,r=[se.sympify(bg[x]) for x in ('l','w','g','L','N','p','h','r')]
    V3=se.Integer(0) if w==0 else se.expand(r/w)
    Elow={}
    for perm in itertools.permutations((0,1,2)):
        Elow[perm]=epsU(*perm,3,4)*(-4*h/g)        # E_{abc}, sign of the permutation of 012
    Eup=[[se.Integer(0)]*5 for _ in R5]
    for a in R5:
        for b in R5:
            x=0
            for (c,d,e),v in Elow.items(): x+=epsU(a,b,c,d,e)*v
            Eup[a][b]=se.expand(-x/12)
    G=[[se.Integer(0)]*5 for _ in R5]; G[3][4]=p; G[4][3]=-p
    Hlow={k:(g/2)*v for k,v in Elow.items()}
    X=[[se.Integer(0)]*5 for _ in R5]
    for a in R5:
        for b in R5:
            x=G[a][b]
            for (c,d,e),v in Hlow.items(): x+=sp.Rational(1,6)*epsL(a,b,c,d,e)*ETA[c]*ETA[d]*ETA[e]*v
            X[a][b]=se.expand(x)
    T=[[X[a][b]/8 for b in R5] for a in R5]
    up=lambda M:[[ETA[a]*ETA[b]*M[a][b] for b in R5] for a in R5]
    return dict(l=l,w=w,g=g,L=L,N=N,p=p,h=h,r=r,V=[0,0,0,V3,0],Eup=Eup,G=G,Gup=up(G),X=X,Xup=up(X),T=T,Tup=up(T))

def K2(bg,n,q,D,S,verbose=False,parts=False,fblock='full'):
    B=bg_fields(bg); fr=Frame(B['l'],B['w'],D,S)
    L,N,g=B['L'],B['N'],B['g']
    psi,phi,ba,bb=build_fields(n,q)
    Na,Nb=len(ba),len(bb)
    Z=lambda: zarr(Nb,Na)
    gT=sp.zeros(4); gX=sp.zeros(4); gG4T=sp.zeros(4)
    for a in R5:
        for b in R5:
            if B['T'][a][b]!=0:
                gT+=sp.sympify(str(B['T'][a][b]))*gam(a,b)
                gG4T+=sp.sympify(str(B['G'][a][b]/4-B['T'][a][b]))*gam(a,b)
    gX=8*gT
    def nab(X,a):           # Lorentz + U(1)_R covariant frame derivative of a doublet spinor
        out=fr.der(X,a)+X.g(fr.Om[a])
        if B['V'][a]!=0: out=out-X.su2(J)*(B['V'][a]/2)
        return out
    def nabvs(Y,a,b):       # nabla_a Y_b for a vector-spinor with lower frame index
        out=nab(Y[b],a)
        for c in R5:
            if fr.Gam[c][a][b]!=0: out=out-Y[c]*fr.Gam[c][a][b]
        return out
    up=lambda Y:[Y[a]*ETA[a] for a in R5]
    psiU=up(psi)
    # R'_ab(Q) (3.15), phi_a (3.16), R_ab(Q) (3.17)
    Rp=[[None]*5 for _ in R5]
    for a in R5:
        for b in R5:
            if a==b: Rp[a][b]=psi[a]*0; continue
            Rp[a][b]=(nabvs(psi,a,b)-nabvs(psi,b,a)+(psi[b].g(GL[a])-psi[a].g(GL[b])).g(gT)*I).expand()
    ph=[]
    for a in R5:
        x=psi[a]*0
        for b in R5: x=x+Rp[a][b].g(GU[b])*(I/3)
        y=psi[a]*0
        for b in R5:
            for c in R5:
                if b!=c: y=y+Rp[b][c].g(gam(b,c))
        ph.append((x-y.g(GL[a])*(I/24)).expand())
    Rh=[[(Rp[a][b]-(ph[b].g(GL[a])-ph[a].g(GL[b]))*I).expand() for b in R5] for a in R5]
    phU=up(ph)
    # d_a = D_a psi^i|_P (4.19), chi (4.21), D_a varphi^i (4.30, raised), lambda^i (5.5, raised)
    d=[(psi[a].g(gG4T)-ph[a]-psi[a].su2(J)*(g*L/(2*s2))).expand() for a in R5]
    dU=up(d)
    chi=psi[0]*0
    for a in R5: chi=chi+dU[a].g(GL[a])*(I/8)   # gamma^mu d_mu = gamma_a d^a
    chi=(chi+phi*(g/8)).expand()
    Dphi=[(nab(phi,a)-psi[a]*(N/2)+psi[a].su2(J).g(gT)*(L/s2)-ph[a].su2(J)*(3*L/s2)).expand() for a in R5]
    DphiU=up(Dphi)
    Dcon=[(-psi[a]*(N/2)+psi[a].su2(J).g(gT)*(L/s2)-ph[a].su2(J)*(3*L/s2)).expand() for a in R5]   # D_a varphi - nabla_a varphi
    sl=phi*0
    for a in R5: sl=sl+Dphi[a].g(GU[a])
    lam=(sl*(-2*I/L)-chi.su2(J)*(8*s2)+phi.g(gX)*(1/(2*L))+phi.su2(J)*(s2*N/L**2)).expand()
    # degree-two composites: G^(2)_ab, H^(2)_abc, X^(2)_ab
    G2=[[None]*5 for _ in R5]
    for a in R5:
        for b in R5:
            G2[a][b]=(bil(psi[a],sp.eye(4),psi[b],NW)-bil(psi[b],sp.eye(4),psi[a],NW))*(I/4)
    def H2(a,b,c):
        x=Z()
        for pm in itertools.permutations(range(3)):
            idx=[(a,b,c)[k] for k in pm]
            sg=1
            for i_ in range(3):
                for j_ in range(i_+1,3):
                    if pm[i_]>pm[j_]: sg=-sg
            x=x+sg*bil(psi[idx[0]],GL[idx[1]],psi[idx[2]],NW)
        return x*se.Rational(-3,4*6)
    H2c={}
    for c,d_,e in itertools.permutations(R5,3):
        if c<d_<e: H2c[(c,d_,e)]=H2(c,d_,e)
    def H2get(c,d_,e):
        if len({c,d_,e})<3: return None
        srt=tuple(sorted((c,d_,e))); pm=[ (c,d_,e).index(x) for x in srt]
        sg=1
        for i_ in range(3):
            for j_ in range(i_+1,3):
                if pm[i_]>pm[j_]: sg=-sg
        return H2c[srt]*sg
    X2=[[None]*5 for _ in R5]
    for a in R5:
        for b in R5:
            x=G2[a][b]
            for c,d_,e in itertools.permutations(R5,3):
                ep=epsL(a,b,c,d_,e)
                if ep: x=x+H2get(c,d_,e)*(sp.Rational(ep,6)*ETA[c]*ETA[d_]*ETA[e])
            X2[a][b]=x
    # contracted primed Lorentz curvature R^(2) (torsion part dropped: total derivative)
    RhU=[[Rh[a][b]*(ETA[a]*ETA[b]) for b in R5] for a in R5]
    def RM2(c,dd,a,b):
        x=Z(); one=sp.eye(4)
        x=x+(bil(ph[c],gam(a,b),psi[dd],NW)-bil(ph[dd],gam(a,b),psi[c],NW))*(I/2)
        for e in R5:
            for f in R5:
                if B['T'][e][f]!=0:
                    x=x+(bil(psi[c],gam(a,b,e,f),psi[dd],NW)-bil(psi[dd],gam(a,b,e,f),psi[c],NW))*(I/2*B['T'][e][f])
        if B['Tup'][a][b]!=0:
            x=x+(bil(psi[c],one,psi[dd],NW)-bil(psi[dd],one,psi[c],NW))*(I*B['Tup'][a][b])
        # psibar_[mu gamma^[a R_nu]^b] : R_nu^b = eta^{bb} R_{nu b}
        Rr=lambda nu,bb_: Rh[nu][bb_]*ETA[bb_]
        x=x+(bil(psi[c],GU[a],Rr(dd,b),NW)-bil(psi[c],GU[b],Rr(dd,a),NW)-bil(psi[dd],GU[a],Rr(c,b),NW)+bil(psi[dd],GU[b],Rr(c,a),NW))*se.Rational(1,4)
        x=x+(bil(psi[c],GL[dd],RhU[a][b],NW)-bil(psi[dd],GL[c],RhU[a][b],NW))*se.Rational(1,4)
        dl=lambda i_,j_: 1 if i_==j_ else 0
        for (s_,mu,nu) in [(1,c,dd),(-1,dd,c)]:
            if dl(nu,a): x=x+bil(psi[mu],GU[b],chi,NW)*(2*s_)
            if dl(nu,b): x=x-bil(psi[mu],GU[a],chi,NW)*(2*s_)
        return x
    R2=Z()
    for a in R5:
        for b in R5:
            if a!=b: R2=R2+RM2(a,b,a,b)
    f2=R2*se.Rational(-1,16)
    one=sp.eye(4)
    # D^(2) (4.24)
    D2=f2*se.Rational(1,2)
    for a in R5:
        for b in R5:
            if B['Gup'][a][b]!=0: D2=D2+G2[a][b]*(-B['Gup'][a][b]/8)+X2[a][b]*(B['Gup'][a][b]/4)
            if B['Xup'][a][b]!=0: D2=D2+X2[a][b]*(-13*B['Xup'][a][b]/48)+G2[a][b]*(B['Xup'][a][b]/4)
    for a in R5:
        D2=D2+bil(psi[a],one,dU[a],NW)*(-I/8)-bil(psi[a],GU[a],phi,NW)*(g/16)
        for b in R5: D2=D2+bil(psi[a],GU[a]*GU[b],d[b],NW)*(-I/16)
    # A1: triplet slot contracted with L^{ij}
    A1=f2*(6*L)
    for a in R5:
        A1=A1+bil(psiU[a],one,Dphi[a],DL)*(-I/s2)-bil(psi[a],GU[a],chi,NW)*(6*L) \
             -bil(phi,gX*GU[a],psi[a],DL)*(1/(8*s2))+bil(phi,GU[a],ph[a],DL)*(1/s2)
    for a in R5:
        for b in R5:
            if B['Xup'][a][b]!=0: A1=A1+X2[a][b]*(L*B['Xup'][a][b]/12)
    A1=A1+D2*(4*L)+bil(phi,one,phi,DL)*(-I*s2*N/L**2)+bil(phi,gX,phi,NW)*(I/(4*L))
    for a in R5: A1=A1+bil(phi,GU[a],Dphi[a],NW)*(1/L)
    # A2, A3: spinor slot
    A2=bil(lam,one,phi,NW)*I
    A3=Z()
    for a in R5: A3=A3+bil(psi[a],GU[a],lam,DL)*(-L/(2*s2))
    # A4: field-strength slot contracted with E^{ab}/2
    A4p={x:Z() for x in 'abcdef'}
    for a in R5:
        for b in R5:
            E=B['Eup'][a][b]
            if E==0: continue
            x=Z()
            for c in R5:
                x=x+bil(psi[a],gam(b,c,lower=True),DphiU[c],NW)*(I/2)
                if B['T'][c][b]!=0: x=x+bil(psi[a],GU[c],phi,NW)*(2*B['T'][c][b])
            x=x+bil(ph[a],GL[b],phi,NW)*2
            A4p['a']=A4p['a']+x*(2*E/L)
            y=bil(ph[a],one,psi[b],DL)*(-3*I)-bil(psi[a],GL[b],chi,DL)*8
            for c in R5:
                for e in R5:
                    if B['T'][c][e]!=0: y=y-bil(psi[a],gam(c,e),psi[b],DL)*(I*B['T'][c][e])
            A4p['b']=A4p['b']+y*(E*s2/2)
            A4p['c']=A4p['c']+bil(phi,one,Rh[a][b],NW)*(-I*E/(2*L))
            A4p['d']=A4p['d']+bil(psi[a],GL[b],lam,NW)*(E/2)
            A4p['e']=A4p['e']+bil(psi[a],one,psi[b],NW)*(-I*N*E/(2*L))
            if fblock=='full':     # Q/S-connection terms of the full D in -sqrt2 D_[mu(L^-2 delta_ij phibar gamma_nu] phi)
                A4p['f']=A4p['f']+bil(phi,GL[b],Dcon[a],DL)*(-s2*E/L**2)
    A4=A4p['a']+A4p['b']+A4p['c']+A4p['d']+A4p['e']+A4p['f']
    # A5 and the defining-vector brace B
    Bb=Z()
    for a in R5:
        Bb=Bb+bil(psi[a],GU[a],phi,NW)*se.Rational(1,2)
        for b in R5:
            if a!=b: Bb=Bb+bil(psi[a],gam(a,b),psi[b],DL)*(I*L/(4*s2))
    A5=Bb*(2*N/L)+bil(phi,one,phi,DL)*(I*N/(s2*L**2))
    tot=(A1+A2+A3+A5+(A4 if fblock in ('full','ordinary') else Z()))*(-2)-Bb*(4*g)
    # Direct conversion preserves a free symbol named S (SymPy's string
    # parser otherwise interprets S as its singleton registry).
    K=sp.Matrix(Nb,Na,lambda i,j: sp.expand(sp.sympify(se.expand(tot[i,j]))))
    if parts:
        return K,ba,bb,dict(A1=A1,A2=A2,A3=A3,A4=A4,A5=A5,B=Bb,**{'A4'+x:v for x,v in A4p.items()})
    return K,ba,bb
