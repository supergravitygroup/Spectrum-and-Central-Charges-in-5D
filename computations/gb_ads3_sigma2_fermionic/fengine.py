"""Zero-momentum engine for the quadratic fermion action on AdS3 x Sigma2,
with the same frame and mode ansatz as the item-24 bosonic calculation.

Frame: E_0=(z/l)d_t, E_1=(z/l)d_x, E_2=(z/l)d_z, E_3=w y d_{y1}, E_4=w y d_{y2}; [E_2,E_0]=E_0/l, [E_2,E_1]=E_1/l,
[E_4,E_3]=w E_3 (curvature v=-w^2 of Sigma2; S2 by continuation w -> i sqrt v; T2 is w=0).
Fermions (frame components, upper SU(2) index): phi-side ~ z^D y^S (amplitudes eta_k), chi-side ~ z^(2-D) y^(1-S)
(amplitudes xi_m).  The bilinear part of the quadratic action is  sum_{m,k} xi_m K_mk eta_k  (Grassmann order: xi to
the left), so K is the linearised field-equation operator on these modes. Gauge null directions require a
maximal-minor analysis to extract physical roots; that item-26 analysis is not performed by this package.
A Majorana bilinear  Xbar^i M Y^j P_ij = sum P_ij X^{iT} C M Y^j  contributes
      K += sum_ij P_ij [ Xchi^{iT} (C M) Yphi^j  -  Ychi^{jT} (C M)^T Xphi^i ]
(the minus sign is the reordering of the two odd amplitudes).  Spinors are numpy object arrays of shape (2,4,N)."""
import numpy as np, symengine as se, sympy as sp
from clifford import GU, GL, ETA, CC, gam, J, EPS2, PAIR_NWSE, PAIR_DELTA, SIGMA01, epsL
R5=range(5)
def tose(M): return np.array([[se.sympify(M[i,j]) for j in range(M.shape[1])] for i in range(M.shape[0])],dtype=object)
CSE=tose(CC); JSE=tose(J)
def zarr(*shape):
    a=np.empty(shape,dtype=object); a.fill(se.Integer(0)); return a
def ex(a): return np.vectorize(se.expand,otypes=[object])(a) if a.size else a

class Sp:
    """spinor doublet (upper SU(2) index) linear in the amplitudes: A (2,4,Na) phi-side, B (2,4,Nb) chi-side"""
    __slots__=('A','B')
    def __init__(s,A,B): s.A,s.B=A,B
    def __add__(s,o): return Sp(s.A+o.A,s.B+o.B)
    def __sub__(s,o): return Sp(s.A-o.A,s.B-o.B)
    def __neg__(s): return Sp(-s.A,-s.B)
    def __mul__(s,c):
        c=se.sympify(c); return Sp(s.A*c,s.B*c)
    __rmul__=__mul__
    def g(s,M):  # left-multiply the spinor index by the 4x4 matrix M (sympy or object array)
        Ms=M if isinstance(M,np.ndarray) else tose(M)
        return Sp(np.einsum('ab,ibk->iak',Ms,s.A) if s.A.size else s.A, np.einsum('ab,ibk->iak',Ms,s.B) if s.B.size else s.B)
    def su2(s,M):
        Ms=M if isinstance(M,np.ndarray) else tose(M)
        return Sp(np.einsum('ij,jak->iak',Ms,s.A), np.einsum('ij,jak->iak',Ms,s.B))
    def expand(s): return Sp(ex(s.A),ex(s.B))

class Frame:
    def __init__(s,l,w,D,S):
        s.l,s.w,s.D,s.S=l,w,D,S
        s.ma={2:D/l,4:w*S}; s.mb={2:(2-D)/l,4:w*(1-S)}; s.mab={2:se.Integer(2)/l,4:w}
        C=[[[se.Integer(0)]*5 for _ in R5] for _ in R5]   # C[c][a][b]: [E_a,E_b]=C^c_ab E_c
        C[0][2][0]=1/l; C[0][0][2]=-1/l; C[1][2][1]=1/l; C[1][1][2]=-1/l; C[3][4][3]=w; C[3][3][4]=-w
        s.C=C
        Cl=lambda c,a,b: ETA[c]*C[c][a][b]
        Gl=[[[ (Cl(c,a,b)-Cl(b,a,c)-Cl(a,b,c))/2 for b in R5] for a in R5] for c in R5]   # Gamma_{cab}
        s.Gam=[[[ETA[c]*Gl[c][a][b] for b in R5] for a in R5] for c in R5]                # Gamma^c_{ab}: nabla_a E_b = Gam^c_ab E_c
        # spin connection on spinors: (1/4) omega_a^{cd} gamma_cd with omega_a^{cd}=Gamma^c_{a b} eta^{bd}
        s.Om=[]
        for a in R5:
            M=sp.zeros(4)
            for c in R5:
                for d in R5:
                    om=s.Gam[c][a][d]*ETA[d]
                    if om!=0: M+=sp.sympify(om)*gam(c,d,lower=True)/4
            s.Om.append(M)
        s.OmSE=[tose(M) for M in s.Om]
        s._checks()
    def _checks(s):
        # torsion free: Gam^c_ab - Gam^c_ba = C^c_ab ; metric: Gam_cab = -Gam_bac
        for c in R5:
            for a in R5:
                for b in R5:
                    assert sp.simplify(sp.sympify(s.Gam[c][a][b]-s.Gam[c][b][a]-s.C[c][a][b]))==0
                    assert sp.simplify(sp.sympify(ETA[c]*s.Gam[c][a][b]+ETA[b]*s.Gam[b][a][c]))==0
        # gamma matrices covariantly constant: [Om_a, gamma^b] = -Gam^b_{ae} gamma^e
        for a in R5:
            for b in R5:
                lhs=s.Om[a]*GU[b]-GU[b]*s.Om[a]
                rhs=sp.zeros(4)
                for e in R5: rhs-=sp.sympify(s.Gam[b][a][e])*GU[e]
                assert sp.simplify(lhs-rhs)==sp.zeros(4), 'spin connection sign'
        # divergence of a bilinear current vanishes (scale-invariant weight): mab[a] + Gam^a_{a e} summed
        for e in R5:
            tot=s.mab.get(e,0)+sum(s.Gam[a][a][e] for a in R5)
            assert sp.simplify(sp.sympify(tot))==0, 'total derivatives'
    def der(s,X,c):
        if c not in (2,4): return Sp(X.A*0,X.B*0)
        return Sp(X.A*s.ma[c],X.B*s.mb[c])

def bil(X,M,Y,P):
    """K contribution of sum_ij P_ij Xbar^i M Y^j (P a 2x2 sympy matrix, M a 4x4 sympy matrix)."""
    CM=tose(CC*sp.Matrix(M)); CMt=CM.T
    Na=X.A.shape[2]; Nb=X.B.shape[2]
    K=zarr(Nb,Na)
    for i in range(2):
        for j in range(2):
            pij=P[i,j]
            if pij==0: continue
            pij=se.sympify(pij)
            K=K+pij*(np.dot(np.dot(X.B[i].T,CM),Y.A[j]) - np.dot(np.dot(Y.B[j].T,CMt),X.A[i]))
    return K

def sector_basis(n,q):
    """phi-side components of weight n (boost) and J-eigenvalue i q; returns list of (field, LC index, spinor u, su2 v)."""
    out=[]
    sig=SIGMA01.eigenvects(); jev=J.eigenvects()
    def svecs(s):
        for val,mult,vs in sig:
            if sp.simplify(val-s)==0: return [sp.Matrix(v) for v in vs]
        return []
    def jvec(qq):
        for val,mult,vs in jev:
            if sp.simplify(val-sp.I*qq)==0: return sp.Matrix(vs[0])
    v=jvec(q)
    WT={'p':1,'m':-1,2:0,3:0,4:0}
    for a in ['p','m',2,3,4]:
        for u in svecs(sp.Rational(2*n-2*WT[a],2)):
            out.append(('psi',a,u,v))
    for u in svecs(sp.Rational(n)): out.append(('phi',None,u,v))
    return out

def build_fields(n,q):
    """psi[a] (lower frame index, Cartesian), phi as Sp objects for sector (n,q) (phi-side) and (-n,-q) (chi-side)."""
    ba=sector_basis(n,q); bb=sector_basis(-n,-q)
    Na,Nb=len(ba),len(bb)
    psiA=[zarr(2,4,Na) for _ in R5]; psiB=[zarr(2,4,Nb) for _ in R5]; phA=zarr(2,4,Na); phB=zarr(2,4,Nb)
    CART={'p':{0:sp.Rational(1,2),1:sp.Rational(1,2)},'m':{0:sp.Rational(1,2),1:sp.Rational(-1,2)},2:{2:1},3:{3:1},4:{4:1}}
    for basis,psiX,phX in [(ba,psiA,phA),(bb,psiB,phB)]:
        for k,(f,a,u,v) in enumerate(basis):
            comp=(u*v.T).T   # comp[i,alpha]=v_i u_alpha
            if f=='phi':
                for i in range(2):
                    for al in range(4): phX[i,al,k]+=se.sympify(comp[i,al])
            else:
                for c,cf in CART[a].items():
                    for i in range(2):
                        for al in range(4): psiX[c][i,al,k]+=se.sympify(cf*comp[i,al])
    psi=[Sp(psiA[c],psiB[c]) for c in R5]; phi=Sp(phA,phB)
    return psi,phi,ba,bb
