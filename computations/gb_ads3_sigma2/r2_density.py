"""Bosonic G-R2 in the compensator gauge, for the six paper spot checks.

Input tensors belong to action.build. This is a direct implementation of
generic_combination/action.md G-D12, G-D13 and G-R2, modulo integration by
parts of L^{ij} nabla^2 L_ij. No auxiliary equation is used.
"""
import symengine as se
from algebra import P, EPS


def density(t):
    idx=range(5); add=t['psum']; deriv=t['Ed']; gi=t['gi']; conn=t['Gm']; Q=se.Rational
    L,N,iL=t['Lf'],t['Nf'],t['iL']; Z,Zbar=t['Zf'],t['Zb']
    E,Elow=t['Eup'],t['Elow']; g=t['g']; I=se.I
    def gradient(x):return [deriv(a,x) for a in idx]
    def divergence(oneform,charge=0):
        cov=add([gi[a][b]*(deriv(a,oneform[b])-
            add([conn[c][a][b]*oneform[c] for c in idx])) for a in idx for b in idx])
        if charge:
            cov-=add([x*y for x,y in zip(t['up1'](t['Vf']),oneform)])*(I*charge)
        return cov
    box=divergence(gradient(L))
    # Y is its neutral triplet component. X and Xbar retain the charged
    # connection derivative of L Z, and therefore the entire Y^{ij}Y_ij.
    Y=(-t['Rs']*Q(1,2)+t['G2']*Q(1,4)-2*t['H2']-iL*iL*(N*N+t['E2'])
       +iL*box-iL*iL*t['dL2']*Q(1,2)-2*t['ZZ'])
    X=se.sqrt(2)*add([E[a]*Z[a] for a in idx])+I*divergence([L*z for z in Z],1)
    Xbar=se.sqrt(2)*add([E[a]*Zbar[a] for a in idx])-I*divergence([L*z for z in Zbar],-1)
    de=t['d1']([iL*x for x in Elow])
    strength=[[2*de[a][b]+se.sqrt(2)*t['dV'][a][b] for b in idx] for a in idx]
    raised=t['up2'](strength)
    contract=t['dot2']; ratio=N*iL; dn=gradient(ratio)
    kinetic_ratio=add([x*y for x,y in zip(dn,t['up1'](dn))])
    cs=add([sg*t['Cf'][a]*strength[b][c]*strength[d][e]
            for (a,b,c,d,e),sg in EPS.items()])*t['isq']
    mixed=[[t['Gu'][a][b]-4*t['Hu'][a][b] for b in idx] for a in idx]
    # nabla L^{ij} nabla L_ij=(dL)^2+4 L^2 Z.Zbar. Thus the
    # integrated G-R2 derivative bracket is -3(dL)^2/4-L^2 Z.Zbar.
    gauged=(L*L*(-t['Rs']*Q(1,4)-t['H2']+t['G2']*Q(1,8)-t['ZZ'])
            -t['dL2']*Q(3,4)-N*N*Q(5,2)-t['E2']*Q(1,2))*g**2
    return (Y*Y+4*iL*iL*X*Xbar-2*kinetic_ratio-cs*Q(1,8)
            +ratio*contract(strength,mixed)-ratio*ratio*contract(t['G'],mixed)
            -contract(strength,raised)*Q(1,4)+gauged-4*g*N*ratio*ratio+g**4*L*L*L*L*Q(1,16))
