"""Clifford algebra in 5d, mostly-plus signature, in the conventions of the students' repository
(common/conventions.md): gamma^{abcde} = i eps^{abcde} with eps^{01234} = +1, Majorana bar psibar = psi^T C with
C^T = -C and C gamma_a C^{-1} = gamma_a^T, so that the flip signs are t_n = (+,+,-,-) for n = 0,1,2,3.
The matrices are those of gauss_bonnet/ads5/details/fermionic_reduction.md, eq. (FC12).
SU(2) (NW-SE): X^i = eps^{ij} X_j, X_i = X^j eps_{ji}, eps_12 = eps^12 = 1.  J(X^1,X^2) = (-X^2,X^1) is the matrix of
delta^{ij} X_j acting on the upper-index doublet (J^2 = -1).  All checks run on import."""
import sympy as sp, itertools
I=sp.I
s1=sp.Matrix([[0,1],[1,0]]); s2=sp.Matrix([[0,-I],[I,0]]); s3=sp.Matrix([[1,0],[0,-1]]); e2=sp.eye(2)
def kron(A,B): return sp.kronecker_product(A,B)
GU=[-I*kron(s3,e2), kron(s1,s1), kron(s1,s2), kron(s1,s3), kron(s2,e2)]     # gamma^a (upper index)
ETA=[-1,1,1,1,1]
GL=[ETA[a]*GU[a] for a in range(5)]                                         # gamma_a (lower index)
CC=GU[2]*GU[4]
ONE=sp.eye(4); ZERO4=sp.zeros(4)
def perm_sign(p):
    s=1; p=list(p)
    for i in range(len(p)):
        for j in range(i+1,len(p)):
            if p[i]>p[j]: s=-s
    return s
EPSU={p:perm_sign(p) for p in itertools.permutations(range(5))}             # eps^{abcde}, eps^{01234}=+1
def epsU(*idx): return EPSU.get(tuple(idx),0)
def epsL(*idx):                                                             # eps_{abcde} (lowered with eta)
    v=epsU(*idx)
    for a in idx: v*=ETA[a]
    return v
_cache={}
def gam(*idx,lower=False):
    """antisymmetrised product gamma^{a1...an} (unit weight); lower=True gives gamma_{a1...an}"""
    key=(idx,lower)
    if key in _cache: return _cache[key]
    G=GL if lower else GU
    if len(idx)==0: out=ONE
    elif len(set(idx))<len(idx): out=ZERO4
    else:
        out=ZERO4
        for p in itertools.permutations(range(len(idx))):
            M=ONE
            for k in p: M=M*G[idx[k]]
            out=out+perm_sign(p)*M
        out=out/sp.factorial(len(idx))
    _cache[key]=out; return out
EPS2=sp.Matrix([[0,1],[-1,0]])            # eps_{ij} = eps^{ij} numerically
J=sp.Matrix([[0,-1],[1,0]])               # (J X)^i = delta^{ij} X_j
PAIR_NWSE=EPS2.T                          # Xbar^i Y_i = sum_ij Xbar^i Y^j eps_{ji}  -> matrix P_ij = eps_{ji}
PAIR_DELTA=sp.eye(2)                      # delta_{ij} Xbar^i Y^j
SIGMA01=GL[1]*GL[0]/2                     # boost generator on spinors: weight s of gamma_p=gamma_0+gamma_1 is +1

def _checks():
    for a in range(5):
        for b in range(5):
            assert GU[a]*GU[b]+GU[b]*GU[a]==2*ETA[a]*(1 if a==b else 0)*ONE
    assert GU[0]*GU[1]*GU[2]*GU[3]*GU[4]==I*ONE, 'gamma^{01234} = i'
    assert CC.T==-CC
    for a in range(5): assert sp.simplify(CC*GL[a]*CC.inv()-GL[a].T)==ZERO4
    # gamma^{abcde} = i eps^{abcde}
    for p in [(0,1,2,3,4),(1,0,2,3,4),(3,4,0,1,2)]: assert gam(*p)==I*epsU(*p)*ONE
    gp=GL[0]+GL[1]; assert gp*SIGMA01-SIGMA01*gp==gp, 'weight convention'
    assert J*J==-sp.eye(2)
    # delta^{ij}X_j = (J X)^i ; X_i = X^j eps_ji
    X=sp.Matrix(sp.symbols('x1 x2')); Xl=sp.Matrix([sum(X[j]*EPS2[j,i] for j in range(2)) for i in range(2)])
    JX=sp.Matrix([sum((1 if i==j else 0)*Xl[j] for j in range(2)) for i in range(2)])
    assert (JX-J*X).applyfunc(sp.expand)==sp.zeros(2,1)
_checks()
