import sympy as s
from collections import defaultdict
I=s.I
L=s.Symbol('L', nonzero=True)
N=s.Symbol('N')
a,b,c=s.symbols('L11 L12 L22')
eps=s.Matrix([[0,1],[-1,0]])
U=s.Matrix([[a,b],[b,c]]); D=eps.T*U*eps
# Matrices multiply epsilon_upper; bilinear coefficients have upper spinor labels.
Nvar={'dphi':-eps/2,'Tphi':-3*I*eps/2,'chi':4*I*D,'eta_phi':-3*I*eps/2}
# delta(2N/L): bar epsilon contracted as bar eps^i phi_i
out={k:2*v/L for k,v in Nvar.items()}
out['phi']= -2*I*N/L**3*D
# phi variation bosonic pieces, Clifford rank supplied explicitly.
def addbil(key, M, rank):
    t=(-1)**(rank*(rank-1)//2)
    # both identical Grassmann-odd phi factors, symmetric D
    val=2*I/L**3*t*M.T*D
    out[key]=out.get(key,s.zeros(2))+val
addbil('phi',N*s.eye(2)/2,0)
addbil('Tphi',U*eps,2)
# eta must be kept as its own parameter.
addbil('eta_phi',-3*U*eps,0)
# gradient L matrix and E coefficient are independent tensor components
u,v,w=s.symbols('dL11 dL12 dL22');dU=s.Matrix([[u,v],[v,w]]); dD=eps.T*dU*eps
addbil('dLphi',I*dU*eps/2,1)
addbil('Ephi',-I*s.eye(2)/2,1)
# lambda_lower (coefficients on independent upper spinors)
lam={
'dphi':2*I*eps/L,
'phi':-2*N*D/L**3,
'Ephi':-2*I*D/L**3,
'dLphi':2*I*dD*U*(-eps)/L**3,
'chi':16*D/L,
'Tphi':-4*eps/L,
}
# target i/2 barepsilon^i lambda_i; eta must cancel
for k in set(out)|set(lam):
    residual=out.get(k,s.zeros(2))-I*lam.get(k,s.zeros(2))/2
    residual=residual.applyfunc(lambda x:s.factor(s.together(x)))
    residual=residual.applyfunc(lambda x:s.factor(x.subs(L**2,2*(a*c-b*b))))
    assert residual==s.zeros(2), (k,residual)
    print(k,residual)
