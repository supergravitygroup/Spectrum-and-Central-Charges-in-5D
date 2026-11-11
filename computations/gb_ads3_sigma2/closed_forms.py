"""v109 eq:spin2cubic, eq:quintic and Appendix C, independent check targets.
These expressions do not construct the Hessian; physical.py derives its divisor.
"""
import sympy as s
from model import L, k, D, M2, P1, P2, P3, P4, P5, g, v, ell_s
Y=128-224*k+16*k**2-80*k*L+120*k**2*L+24*k**2*L**2-20*k**3*L**2-6*k**3*L**3+k**4*L**4
X=64-128*k+16*k**2-48*k*L+72*k**2*L+20*k**2*L**2-14*k**3*L**2-6*k**3*L**3+k**4*L**4
nuf=(16+4*k-10*k*L+k**2*L**2)/(k*P3)
mul=Y/(k*P3*P4)
kappa=L*Y/(4*P2*P4)
Pi4=-256-256*k+448*k*L+64*k**2+352*k**2*L-368*k**2*L**2-64*k**3*L-120*k**3*L**2+136*k**3*L**3+24*k**4*L**3-24*k**4*L**4+k**5*L**5
Pi3=2048*L+2048*k-2560*k*L-3328*k*L**2-3840*k**2*L+4736*k**2*L**2+2048*k**2*L**3+256*k**3*L+1280*k**3*L**2-2208*k**3*L**3-816*k**3*L**4-208*k**4*L**3+440*k**4*L**4+232*k**4*L**5-24*k**5*L**5-42*k**5*L**6+3*k**6*L**7
Pi2=2048+512*L**2-1024*k-1024*k*L-1280*k*L**2-1024*k*L**3+2048*k**2*L-1664*k**2*L**2+2048*k**2*L**3+1056*k**2*L**4-320*k**3*L**2+384*k**3*L**3-784*k**3*L**4-688*k**3*L**5-32*k**4*L**4+144*k**4*L**5+244*k**4*L**6-8*k**5*L**6-44*k**5*L**7+3*k**6*L**8
Pi21=32+24*k+12*k**2-56*k*L-28*k**2*L+38*k**2*L**2+5*k**3*L**2-11*k**3*L**3+k**4*L**4
f4=Pi4/(k*P1*P3*P4)
f3=Pi3/(k*P1*P3**2*P4)
f2=2*P2*Pi2/(k*P1*P3**3*P4)
f1=16*L**2*(3*k-2)*P2**3*P5/(k*P1*P3**3*P4)
rr=D**3+(f4+2)*D**2+(f3+2*f4+4)*D+f2+2*f3+4*f4+8
ratio=P4*P5/(P1**2*P2**2)
b3=-1-ratio
b2=4*Pi21/(k*P1**2*P3)
b1=-8*L*(8-8*k-4*k*L+3*k**2*L)*P5/(k*P1**2*P3**2)
b0=16*L*P2*P5*(2*L-8+3*k*L-k*L**2)/(k*P1*P3**3)
F=D**5+f4*D**4+f3*D**3+f2*D**2+f1*D+M2*(b3*D**3+b2*D**2+b1*D+b0)+M2**2*ratio*(D-nuf+1)
cubic=D*(D-2)*(D-1-mul)-M2*(D-1-nuf)
torus=2*(L-4)/(L*(L-3))
def generic_targets():
    return {"spin2": cubic, "scalar": F*F.subs(D,2-D), "vector": cubic.subs(D,D+1)*F.subs(D,D-1)*(D-nuf)**2, "Z+": D-nuf, "Z-": D-2+nuf}

def target_divisor(name):
    from polynomial_matrix import rational,primitive_in_D
    from model import S
    level=4*L*(2*L-8+3*k*L-k*L**2)*P2**2*S*(S-1)/(P4*P3**2)
    value=rational(generic_targets()[name].subs(M2,level))
    assert value.den.degrees()[2]==0
    return primitive_in_D(value.num)
