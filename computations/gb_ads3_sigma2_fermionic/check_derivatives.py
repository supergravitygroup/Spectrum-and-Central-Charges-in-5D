"""Numerical component identities at the order required by the Hessian.

Adapted from the donor's test_ferm, test_bos, test_D, test_second and
test_second2. Comparisons share some engine operations; they are consistency
checks, not an independent nonlinear supersymmetry proof.
"""
import numpy as np
from ferm2 import bl, ein, gm, su2, GL, GUP, ETA, ETAI, EPS_LOW, EPS2, DL, JM, I, s2
from bderiv2 import antisym, CurvVar


def run(result, check):
    c, eng = result['context'], result['engine']
    o, e, v, S = eng.o, eng.e, eng.v, eng.S
    br, bv = S.br, S.bv
    d1 = S.d1
    lin = lambda X: np.concatenate((X.A.ravel(), X.B.ravel()))
    E = o['psi']
    extra = lambda dp: gm(-c.gG/32+c.gT/4, dp)-su2(JM, dp)*(c.g*c.L/(16*s2))
    for tag, dD, dphi, ddil, dchi in (
            ('Q', v.dQ_Dpsi, v.dQ_varphi, v.dQ_dil, v.dQ_chi),
            ('S', v.dS_Dpsi, v.dS_varphi, v.dS_dil, v.dS_chi)):
        composite = ein('ast,...aitn->...isn', GUP[1], dD(E))*(I/8)+dphi(E)*(c.g/8)+extra(ddil(E))
        check('chi variation '+tag, lin(composite), lin(dchi(E)))
    check('Dchi rule vs SC7-17', lin(o['Dchi']), lin(o['Dchi_SC717']))
    check('gamma trace RQ', lin(ein('ast,abitn->bisn', GUP[1], o['RQ'])), 0)
    check('gamma trace D RQ', lin(ein('ast,cabitn->cbisn', GUP[1], o['DRQ'])), 0)
    check('G Bianchi', antisym(d1['DG'], [0, 1, 2]), 0)
    check('composite T variation', bv.XiQ_T(E, 'c'), bv.XiQ_T_W03(E, 'c'))
    H3up = np.einsum('cpqrmn,px,qy,rz->cxyzmn', d1['DH3'], ETAI, ETAI, ETAI)
    check('dual H derivative', -np.einsum('abxyz,cxyzmn->cabmn', EPS_LOW, H3up)/12, d1['DHd'])

    # Independent ordinary-current identity P^(2)=0, not the H Bianchi
    # definition used internally by Second.Ehat2.
    Eup = -I/2*bl(o['psi'], 'b', o['varphi'], '', G=GUP[2], gf='ba', out='a')
    Eup -= c.L/(4*s2)*bl(o['psi'], 'b', o['psi'], 'c', G=GUP[3], gf='abc', P=DL, out='a')
    Elower = np.einsum('ab,bmn->amn', ETA, Eup)
    Ehat, _ = S.Ehat2()
    check('Ehat from ordinary current vs gauged Bianchi', Ehat, Elower)
    GG = np.einsum('ab,cdmn->abcdmn', c.G, e['G'])
    check('gauged H Bianchi', antisym(d1['DH3'], [0,1,2,3]),
          1.5*antisym(GG, [0,1,2,3])+c.g/4*np.einsum('abcde,emn->abcdmn', EPS_LOW, Eup))
    check('DDsigma commutator', e['DDsigma']-np.swapaxes(e['DDsigma'], 0, 1), 0)

    def lor(X0, X2):
        R2 = np.einsum('xypemn,ez->xypzmn', e['C'], ETAI)
        R0 = np.einsum('xype,ez->xypz', c.Cw, ETAI)
        return (np.einsum('xypemn,eq->xypqmn', R2, X0)+np.einsum('xype,eqmn->xypqmn', R0, X2)
                +np.einsum('xyqemn,pe->xypqmn', R2, X0)+np.einsum('xyqe,pemn->xypqmn', R0, X2))
    DDG, DDH = eng.even[('dd','G^')], eng.even[('dd','H^')]
    check('G derivative commutator', DDG-np.swapaxes(DDG,0,1), -br.Xi_G(o['RQ'],'xy',br.F0)+lor(c.G,e['G']))
    check('H derivative commutator', DDH-np.swapaxes(DDH,0,1), -br.Xi_Hd(o['RQ'],'xy',br.F0)+lor(c.H,e['H']))
    bil = bl(o['Dpsi'],'b',o['Dpsi'],'a',G=GL[2],gf='cd',out='abcd')
    DDT = (DDG/8-DDH/4
           -(np.einsum('abmn,cd->abcdmn',e['DDsigma'],c.G)+np.einsum('ab,cdmn->abcdmn',2*c.f,e['G']))/8
           +(np.einsum('abmn,cd->abcdmn',e['DDsigma'],c.H)+np.einsum('ab,cdmn->abcdmn',2*c.f,e['H']))/2
           +I/32*(bil+np.swapaxes(bil,0,1)))
    check('DDT composite vs W03 derivative', DDT, eng.even[('dd','T')])
    DDN, DDL = S.DDN(), S.DDL()
    check('N derivative commutator', DDN-np.swapaxes(DDN,0,1),
          -br.Xi_N(o['RQ'],'xy',br.F0)-br.Sg_N(o['RS'],'xy',br.F0))
    RVm = np.einsum('xyilmn,lk->xyikmn',e['RV'],EPS2)
    u = np.einsum('xyikmn,jk->xyijmn',RVm,c.Lij)
    check('L derivative commutator', DDL-np.swapaxes(DDL,0,1), -br.Xi_L(o['RQ'],'xy',br.F0)+u+np.swapaxes(u,2,3))
    first, box, div, E2 = S.DE_box()
    check('supercovariant current conservation', div, 0)
    sec = (c.nabK(first,2)-br.vary_first(S.Xi_E,S.Sg_E,None,4,1,o['psi'],'x','Q')
           -br.vary_first(S.Xi_E,S.Sg_E,None,4,1,o['phi_mu'],'x','S')+bv.Kterm(np.zeros(5,complex),E2,4,1))
    rhs = (-S.Xi_E(o['RQ'],'xy',br.F0)-S.Sg_E(o['RS'],'xy',br.F0)
           +np.einsum('xype,ez,zmn->xypmn',c.Cw,ETAI,E2))
    check('E derivative commutator', sec-np.swapaxes(sec,0,1), rhs)

    up2 = lambda X: np.einsum('ab,ax,by->xy',X,ETAI,ETAI)
    sc719 = (eng.even[('dB','sigma')]/4+5/48*np.einsum('ab,eabmn->emn',up2(c.G),d1['DG'])
             +(np.einsum('ab,eabmn->emn',up2(c.H),d1['DG'])+np.einsum('ab,eabmn->emn',up2(c.G),d1['DHd']))/24
             -13/12*np.einsum('ab,eabmn->emn',up2(c.H),d1['DHd'])+c.g/4*d1['DN']
             +c.g**2/8*(c.L/s2)*np.einsum('eijmn,ij->emn',d1['DL'],np.eye(2)))
    sc719 += 3/8*bl(o['Dpsi'],'e',o['Dpsi'],'a',G=GUP[1],gf='a',out='e')-I*c.g/2*bl(o['Dpsi'],'e',o['varphi'],'',out='e')
    check('third descendant D(auxiliary D)', eng.even[('d','D')], sc719)

    # Q/S variations of the full composite scalar, including the dilatino
    # terms before its gauge is evaluated.
    def Kq(E, ef, kind):
        dR = S.cv.dRp_Q(E,ef) if kind == 'Q' else S.cv.dRp_S(E,ef)
        return 2*CurvVar.ricci_f_C(dR)[1]
    def composite(box, XG, XH, XN, XL, dil):
        t = box/4+5/48*np.einsum('ab,xabmn->xmn',up2(c.G),XG)
        t += (np.einsum('ab,xabmn->xmn',up2(c.H),XG)+np.einsum('ab,xabmn->xmn',up2(c.G),XH))/24
        t += -13/12*np.einsum('ab,xabmn->xmn',up2(c.H),XH)+c.g/4*XN
        t += c.g**2/8*(c.L/s2)*np.einsum('xijmn,ij->xmn',XL,np.eye(2))
        return t-bl(dil,'x',o['Dpsi'],'a',G=GUP[1],gf='a',out='x')/8-4*I*bl(dil,'x',o['chi'],'',out='x')
    boxQ = np.einsum('xacmn,ac->xmn',br.vary_first(br.Xi_Ds,br.Sg_Ds,None,0,1,E,'x','Q',Kterm=Kq),ETAI)
    check('auxiliary D Q variation', composite(boxQ,bv.XiQ_G(E,'x'),bv.XiQ_Hd(E,'x'),bv.XiQ_N(E,'x'),bv.XiQ_L(E,'x'),v.dQ_dil(E)),bv.XiQ_D(E,'x'))
    boxS = np.einsum('xacmn,ac->xmn',br.vary_first(br.Xi_Ds,br.Sg_Ds,None,0,1,E,'x','S',Kterm=Kq),ETAI)
    z = np.zeros_like(bv.XiQ_G(E,'x'))
    check('auxiliary D S variation', composite(boxS,z,z,bv.XiS_N(E,'x'),np.zeros_like(bv.XiQ_L(E,'x')),v.dS_dil(E)),bv.XiS_D(E,'x'))
