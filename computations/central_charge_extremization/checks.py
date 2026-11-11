#!/usr/bin/env python3
"""Final-paper anomaly and extremization identities. Read-only by default."""
import argparse
import hashlib
import itertools
import json
from pathlib import Path
import sys

import sympy as s

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
sys.path.insert(0, str(ROOT / 'computations/generic_ads5_massless'))
import action_inputs as ads
from derive import derive as massless_result
sys.path.insert(0, str(ROOT / 'computations/gb_ads3_sigma2'))
import model as product
from closed_forms import X


def calculate():
    checks = []

    def equal(name, left, right=0):
        residual = s.factor(s.cancel(left-right))
        if residual != 0:
            raise AssertionError((name, residual))
        checks.append({'identity': name, 'residual': '0'})

    g, L0 = ads.g, ads.L
    alpha, beta, zeta = ads.alpha, ads.beta, ads.zeta
    kap, area, genus = s.symbols('kappa A_Sigma genus', positive=True)
    eps, y, p, r, k = s.symbols('epsilon y p r k', real=True)
    pi, rt2 = s.pi, s.sqrt(2)
    q = s.Rational
    # Ordered epsilon-density slots from G-2D, G-W, G-LOG and G-R2.
    # E contains epsilon*G*G/(8g); bold G -> sqrt(2)*dV for this CS slot.
    density_slots = {(0, 0, 0): -4*g/(8*g),
                     (1, 0, 0): -2*rt2/(8*g),
                     (0, 1, 1): -(alpha+beta)/24-zeta*2/8}
    # epsilon A F F = 4 A wedge F wedge F. Symmetrizing the three
    # slots is integration by parts, before inserting flux or R direction.
    tensor = {}
    for key, coefficient in density_slots.items():
        permutations = set(itertools.permutations(key))
        for indices in permutations:
            tensor[indices] = 4*coefficient/len(permutations)
    tensor[(1, 1, 1)] = s.S.Zero

    def cubic(a, b, c):
        return s.expand(sum(value*a[i]*b[j]*c[l]
                            for (i, j, l), value in tensor.items()))

    M3 = s.Matrix(2, 2, lambda i, j:
                  3*sum(tensor[(i, j, l)]*(p, r)[l] for l in range(2)))
    gb = {alpha: k/g**2, beta: 2*k/g**2, zeta: 0}
    Mgb = M3.subs(gb)
    expected_Mgb = s.Matrix([[-6*p-rt2*r/g, -rt2*p/g-k*r/(2*g**2)],
                            [-rt2*p/g-k*r/(2*g**2), -k*p/(2*g**2)]])
    for i, residual in enumerate(Mgb-expected_Mgb):
        equal('CS reduction / matrix entry '+str(i), residual)

    Rtrial = (eps, -2)
    anomaly3 = 12*pi**2*cubic(Rtrial, Rtrial, Rtrial)/kap**2
    # epsilon C R^{ab}R_ab = -4 C wedge tr(R wedge R).
    anomaly1 = -24*pi**2*alpha*eps/kap**2
    equal('eq:TrR cubic', anomaly3,
          -8*pi**2*eps*(3*eps**2-3*rt2*eps/g+alpha+beta+6*zeta)/kap**2)
    atrial = q(3, 32)*(3*anomaly3-anomaly1)
    ctrial = (9*anomaly3-5*anomaly1)/32
    tau = (beta+6*zeta)*g**2
    ahat = 2*rt2*pi**2*(3*y**2-2*y**3-q(3, 4)*tau*y)/(g**3*kap**2)
    equal('eq:atrial from anomalies', atrial.subs(eps, 2*rt2*y/(3*g)), ahat)
    equal('trial a independent of alpha', s.diff(atrial, alpha))
    equal('stationarity is vacuum polynomial',
          s.diff(ahat, y).subs(y, 1/L0),
          -3*rt2*pi**2*ads.vacuum_polynomial/(2*g**3*kap**2*L0**2))

    # Independently reuse the current action projection, before its vacuum EOM.
    direct = massless_result()
    prefactor = pi**2*(rt2/(g*L0))**3/kap**2
    equal('trial a from current scalar-curvature action',
          (prefactor*direct['a_normalized_before_Q']).subs(L0, 1/y), ahat)
    estar = 2*rt2/(3*g*L0)
    a = prefactor*direct['a_normalized']
    c = prefactor*direct['c_normalized']
    equal('a maximum / current action a', ads.on_vacuum(atrial.subs(eps, estar)), a)
    equal('a maximum / current action c', ads.on_vacuum(ctrial.subs(eps, estar)), c)
    equal('R direction equals graviphoton', estar/-2, -direct['u_mixing'])
    Zu, Zv = direct['vector_Zuv'][0, 0], direct['vector_Zuv'][1, 1]
    CF = s.cancel(q(16, 3)*c*Zu/(4*Zv))
    equal('normalized flavor coefficient', CF, 24*pi**2*rt2*(2-L0)/(g*L0*kap**2))
    equal('a-maximization / flavor two-point coefficient',
          s.diff(atrial, eps, 2).subs(eps, estar), -q(9, 16)*CF)
    equal('trial-y second derivative', s.diff(ahat, y, 2).subs(y, 1/L0), -CF/(2*g**2))
    equal('two-derivative normalization a', a.subs({L0: 1, alpha: 0}),
          2*rt2*pi**2/(g**3*kap**2))

    # Product family: keep g and area symbolic; chi=+1 means ell_s>0.
    L = product.L
    to_local = {product.g: g, product.k: k}
    curvature = product.v.subs(to_local)
    ell = product.ell_s.subs(to_local)
    flux = (g*L/rt2, curvature)
    P2, P4 = product.P2.subs(to_local), product.P4.subs(to_local)
    cL = 12*pi*area*L*X.subs(to_local)*ell/(2*P2*P4*kap**2)
    cR = 12*pi*area*L*(2-3*k)*P2*ell/(P4*kap**2)
    trial2d = 18*pi*area*cubic(flux, Rtrial, Rtrial).subs(gb)/kap**2
    curvature2d = s.diff(trial2d, eps, 2)
    mixing2d = s.cancel(-s.diff(trial2d, eps).subs(eps, 0)/curvature2d)
    equal('2d mixing', mixing2d, ell)
    equal('eq:cLcR / extremized trial', trial2d.subs(eps, mixing2d), cL)
    gravitational_anomaly = 12*pi*area*k*flux[0]/(g**2*kap**2)
    equal('eq:cLcR / gravitational anomaly', cR-cL, gravitational_anomaly)
    for name, value in [('cL', cL), ('cR', cR)]:
        equal('two-derivative '+name, value.subs(k, 0),
              (12*pi*area*L*ell/kap**2).subs(k, 0))

    # The paper explicitly includes the flat trial at k=2/3. Do not divide
    # by the flavor anomaly on that locus.
    equal('k=2/3 / trial independent of mixing', s.diff(trial2d, eps).subs(k, q(2, 3)))
    equal('k=2/3 / trial value', (trial2d-cL).subs(k, q(2, 3)))
    equal('k=2/3 / cR', cR.subs(k, q(2, 3)))

    # Compare to the independently reduced constant-level current pencil.
    constant = json.loads((ROOT/'computations/gb_ads3_sigma2/outputs/constant.json').read_text())['vector']
    loc = {'L': L, 'k': k}
    stored_cs = s.Matrix([[s.sympify(x, locals=loc) for x in row] for row in constant['current_CS']])
    amplitudes = s.diag(1, g/rt2)
    current = 2/g**2*amplitudes*Mgb.subs({p: flux[0], r: flux[1]})*amplitudes/ell
    for i, residual in enumerate(current-stored_cs):
        equal('current pencil / CS entry '+str(i), residual)
    rlevel = s.sympify(constant['extremized_R_level'], locals=loc)
    # V=-2 A_R and V=(g/sqrt2)*V_hat restore the physical charge-one current.
    kR = 8*pi*area*ell*rlevel/kap**2
    equal('R-current level cL=3kR', cL, 3*kR)

    # Universal twist: normalized H2 flux n=(genus-1)*R4, no flavor flux.
    k_vac = 4*(L0-1)/L0**2
    R4, F4 = (estar, -2), (1, 0)

    def anomaly(a0, b0, c0):
        return s.factor(12*pi**2*cubic(a0, b0, c0).subs(gb).subs(k, k_vac)/kap**2)

    RRR = anomaly(R4, R4, R4)
    RRF = anomaly(R4, R4, F4)
    RFF = anomaly(R4, F4, F4)
    aGB = a.subs(alpha, k_vac/g**2)
    cGB = c.subs(alpha, k_vac/g**2)
    dc = s.cancel(-3*(genus-1)*RRF**2/RFF)
    leftUT = 3*(genus-1)*(RRR-RRF**2/RFF)
    rightUT = leftUT+24*pi**2*(genus-1)*k_vac*estar/(g**2*kap**2)
    equal('eq:deltac', dc, q(8, 3)*(genus-1)*(cGB-aGB)**2/cGB)
    equal('eq:UTc left', leftUT, q(16, 3)*(genus-1)*(5*aGB-3*cGB)+dc)
    equal('eq:UTc right', rightUT, q(32, 3)*(genus-1)*aGB+dc)
    einstein_root = 2/(1+s.sqrt(1-k))
    # Only the first-order statement made in the final paper is tested.
    equal('universal twist / no zeroth- or first-order correction',
          s.series(dc.subs(L0, einstein_root), k, 0, 2).removeO())
    return {
        'scope': 'Final paper eq:atrial, eq:LCS, eq:TrR, eq:cLcR, eq:UTc, eq:deltac; exact identities only.',
        'domain': 'g>0; L0,L>0; vacuum Q=0 for AdS5 values; regular product family and chi=+1; the k=2/3 trial is evaluated before division; universal twist c!=0.',
        'checks': checks,
        'results': {name: str(s.factor(value)) for name, value in {
            'TrR3': anomaly3, 'TrR': anomaly1, 'trial_a': atrial,
            'C_F': CF, 'mixing_2d': mixing2d, 'cL': cL, 'cR': cR,
            'universal_twist_delta_c': dc, 'universal_twist_cL': leftUT,
            'universal_twist_cR': rightUT}.items()},
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--write-log', action='store_true')
    args = parser.parse_args()
    manifest = json.loads((HERE/'source_manifest.json').read_text())
    for name, digest in manifest['repository_inputs'].items():
        assert hashlib.sha256((ROOT/name).read_bytes()).hexdigest() == digest, name
    result = calculate()
    result['source_sha256'] = manifest['repository_inputs']
    result['implementation_sha256'] = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    result['sympy_version'] = s.__version__
    output = HERE/'outputs'
    if args.write_log:
        output.mkdir(exist_ok=True)
        (output/'verification.json').write_text(json.dumps(result, indent=2)+'\n')
    else:
        assert result == json.loads((output/'verification.json').read_text()), 'stale verification record'
    message = f"PASS {len(result['checks'])} exact final-paper anomaly/extremization identities; {len(manifest['repository_inputs'])} source fingerprints"
    if args.write_log:
        (output/'verification.log').write_text('python3 -B computations/central_charge_extremization/checks.py\n'+message+'\n')
    print(message)


if __name__ == '__main__':
    main()
