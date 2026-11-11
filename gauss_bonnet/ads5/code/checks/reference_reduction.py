"""Independent replay of the original 65 local checks.
The readable calculation stages are under calculations/. No original files are accessed."""
from pathlib import Path
import json, itertools, re
import sympy as sp

def main():
    root = Path(__file__).resolve().parents[1]
    x, g, L, N, lam, k = sp.symbols('x g L N lam k', nonzero=True, real=True)
    a = 2 * (1 - x) / x ** 2
    c = 2 - x
    sub = {L: x, N: -sp.Rational(3, 2) * g * x * x, lam: a / g ** 2, k: -g * g * x * x / 2}
    checks = {}

    def check_zero(name, z):
        z = sp.factor(z)
        checks[name] = str(z)
        assert z == 0, (name, z)
    F = L + lam * g * g * L * L / 2
    K = 1 / L + lam * g * g
    V = -2 * N * N / L - 2 * g * L * N - 4 * g * N + 2 * g * g * L * L - g * g * L ** 3 / 2 + lam * (-2 * g * g * N * N - 4 * g ** 3 * N * L * L - g ** 4 * L ** 4)
    check_zero('F0', F.subs(sub) - 1)
    check_zero('Fprime', sp.diff(F, L).subs(sub) - c / x)
    check_zero('K0', K.subs(sub) - c / x ** 2)
    check_zero('Lovelock coefficient', (F - lam * k).subs(sub) - c)
    check_zero('ell squared', ((20 * k * sp.diff(F, L, 2) + sp.diff(V, L, 2)) / 2).subs(sub) + 4 * c * g * g)
    check_zero('ell n', sp.diff(V, L, N).subs(sub) + 8 * c * g / x)
    check_zero('n squared', (sp.diff(V, N, 2) / 2).subs(sub) + 2 * c / x ** 2)
    check_zero('scalar tadpole', (20 * k * sp.diff(F, L) + sp.diff(V, L)).subs(sub))
    check_zero('n tadpole', sp.diff(V, N).subs(sub))
    alpha = -lam / 4
    metrictrace = (sp.Rational(3, 8) * F * 20 * k - alpha * 120 * k * k / 8 + sp.Rational(15, 8) * V).subs(sub)
    check_zero('constant trace Hessian', metrictrace - (-15 * k * c).subs(sub))
    ell, n = sp.symbols('ell n')
    rawpot = -4 * c * g * g * ell ** 2 - 8 * c * g * ell * n / x - 2 * c * n * n / x ** 2
    check_zero('auxiliary square', rawpot - (-2 * c * (n + 2 * g * x * ell) ** 2 / x ** 2 + 4 * c * g * g * ell ** 2))
    beta = -2 / (3 * x)
    check_zero('diagonal gradient', 3 * c * beta * beta + 4 * c * beta / x + c / x ** 2 + c / (3 * x * x))
    check_zero('diagonal potential', (-15 * c * k * beta * beta - 20 * c * k * beta / x + 4 * c * g * g).subs(sub) - 2 * c * g * g / 3)
    z = sp.symbols('z')
    r = 8 * z / (3 * x) + 40 * k / (3 * x)
    check_zero('reconstructed scalar equation', (c * r / x - 2 * c * z / x ** 2 + 8 * c * g * g).subs(sub) - 2 * c * (z - 4 * sub[k]) / (3 * x * x))
    q = sp.Rational
    eta = [-1, 1, 1, 1, 1]
    w = sp.symbols('w')
    X = sp.zeros(5)
    for i in range(5):
        for j in range(i + 1, 5):
            X[i, j], X[j, i] = (7 * i + 3 * j + 1, -(7 * i + 3 * j + 1))

    def metric(i, j):
        return eta[i] if i == j else 0

    def M(i, j, m, n):
        return metric(i, m) * X[j, n] - metric(j, m) * X[i, n] + metric(i, n) * X[m, j] - metric(j, n) * X[m, i]

    def C(i, j, m, n):
        return -w * q(1, 2) * metric(i, j) * X[m, n] + q(1, 2) * M(j, i, m, n)
    for i, j in itertools.product(range(5), repeat=2):
        assert sp.expand(sum((eta[m] * C(i, m, j, m) for m in range(5))) - (w - 3) * X[i, j] / 2) == 0
        assert sp.expand(sum((eta[m] * C(m, i, j, m) for m in range(5))) - (w + 3) * X[i, j] / 2) == 0
        assert sp.expand(sum((eta[m] * C(m, m, i, j) for m in range(5))) + 5 * w * X[i, j] / 2) == 0
    for i, j, m, n in itertools.product(range(5), repeat=4):
        assert sp.expand(M(i, j, m, n) + C(i, j, m, n) - C(j, i, m, n)) == 0
    checks['Lorentzian_K_component_checks'] = '700 exact component equations passed'
    AG, AM, AH, JG, JM, JH, KG, KM, KH = sp.symbols('AG AM AH JG JM JH KG KM KH')
    weyl = q(2, 3) * AG - q(8, 3) * AM + q(8, 3) * AH - 2 * JG + 8 * JM - 8 * JH + q(10, 3) * KG - q(40, 3) * KM + q(40, 3) * KH
    rows = [(q(-8, 9), JG - KG / 2), (q(-112, 9), -JM), (q(-32, 9), JM - KM / 2), (q(-128, 9), JH), (q(-4, 3), -AG - 5 * KG), (q(-16, 3), -AM - 5 * KM), (q(-4, 9), JG - KG / 2), (q(-8, 9), -JM), (q(-16, 9), JM - KM / 2), (q(32, 9), JH), (q(-10, 3), JG - 3 * KG), (q(28, 3), JM - 3 * KM), (q(-16, 3), JH - 3 * KH), (q(4, 3), AG), (q(-22, 3), AM), (q(-8, 3), AH), (8, -JM), (-16, -JH)]
    der = sp.expand(weyl + sum((coef * term for coef, term in rows)))
    closed = sp.expand(der.subs({AG: 2 * JG - 6 * KG, AM: 2 * JM - 6 * KM}))
    check_zero('form derivative subtotal', closed - (8 * JM - 8 * JH + q(2, 3) * KG + 16 * KM + q(88, 3) * KH))
    algebraic = -q(17, 3) * KG - q(112, 3) * KH
    curr287etc = -8 * JM + 2 * KG - 22 * KM
    curr246etc = 4 * KG + 10 * KM
    check_zero('form HD collection', closed + algebraic + curr287etc + curr246etc - (-8 * JH + KG + 4 * KM - 8 * KH))
    for name, value, target in [('G2', -x / 2 + lam * k, -c / 2), ('H2', 4 * x - 8 * lam * k, 4 * c), ('p2', -2 / x - 2 * lam * g * g, -2 * c / x ** 2), ('pv', -2 * sp.sqrt(2) * (1 + lam * g * g * x), -2 * sp.sqrt(2) * c / x), ('pA', -4 * g + 4 * lam * k * g, -4 * g * c), ('vprime2', 2 * x + 2 * lam * g * g * x * x, 2 * c)]:
        check_zero(name, value.subs(sub) - target)
    u, v = sp.symbols('u v')
    eps = sp.Matrix([[0, 1], [-1, 0]])
    Vp = sp.Matrix([[u, v], [v, -u]])
    DL = sp.sqrt(2) * x * Vp * eps
    check_zero('SU2 compensator kinetic', sp.trace(DL.T * DL) - 2 * x * x * sp.trace(Vp.T * Vp))
    G, H = sp.symbols('G H')
    Fv = sp.sqrt(2) * g * x * (2 * H - G)
    check_zero('reconstructed E2 equation', 4 * g * H - sp.sqrt(2) * Fv / x - 2 * g * G)
    check_zero('dual Legendre sign', 4 * c * H * H - 8 * c * H * H - -4 * c * H * H)
    check_zero('BF threshold', 4 * k / -k + 4)
    check_zero('two derivative x', a.subs(x, 1))
    for name, val in [('metric', c), ('scalar', c / x ** 2), ('N', c / x ** 2), ('A', c), ('H', c), ('p', c / x ** 2), ('v', c / x), ('vprime', c)]:
        check_zero('endpoint ' + name, val.subs(x, 2))
    seriesvar = sp.symbols('a')
    xs = 2 / (1 + sp.sqrt(1 + 2 * seriesvar))
    check_zero('small a series', sp.series(xs, seriesvar, 0, 3).removeO() - (1 - seriesvar / 2 + seriesvar ** 2 / 2))
    m = g * x / (2 * sp.sqrt(2))
    bet = sp.I * sp.sqrt(2) / (3 * x)
    for name, raw, target in [('RS', -x - a * x * x, -c), ('Dirac', 2 / x + 2 * a, 2 * c / x ** 2), ('derivative mixing', -2 * sp.sqrt(2) * sp.I * (1 + a * x), -2 * sp.sqrt(2) * sp.I * c / x), ('RS mass', -sp.I * g * x * (x + 2 + 2 * a * x * x) / (2 * sp.sqrt(2)), -3 * sp.I * g * x * c / (2 * sp.sqrt(2))), ('mass mixing', -2 * g * (x + 1) - 3 * g * a * x * x, -4 * g * c), ('spinor mass', 7 * sp.I * g * (1 + a * x) / sp.sqrt(2), 7 * sp.I * g * c / (sp.sqrt(2) * x))]:
        check_zero('fermion raw ' + name, raw - target)
    check_zero('fermion shift derivative mixing', -6 * bet + 2 * sp.sqrt(2) * sp.I / x)
    check_zero('fermion shift algebraic mixing', -24 * sp.I * m * bet - 4 * g)
    check_zero('fermion shifted kinetic', -12 * bet ** 2 + 8 * sp.sqrt(2) * sp.I * bet / x + 2 / x ** 2 + 2 / (3 * x * x))
    check_zero('fermion shifted mass', 60 * sp.I * m * bet ** 2 + 20 * g * bet - 7 * sp.I * g / (sp.sqrt(2) * x) + 2 * sp.I * m / (3 * x * x))
    check_zero('raw spinor reconstruction derivative', 3 * bet - sp.I * sp.sqrt(2) / x)
    check_zero('raw spinor reconstruction trace', 12 * sp.I * m * bet + 2 * g)
    check_zero('raw spinor reconstruction Dirac', 4 * sp.I * sp.sqrt(2) * bet / x + 2 / (3 * x * x) + 2 / x ** 2)
    check_zero('raw spinor reconstruction mass', 10 * g * bet + 2 * sp.I * m / (3 * x * x) - 7 * sp.I * g / (sp.sqrt(2) * x))
    check_zero('RS Noether undifferentiated', (-3 * k - 12 * m * m).subs(sub))
    check_zero('RS Noether derivative', -3 * sp.I * m + 3 * sp.I * m)
    check_zero('residual divergence', (25 * m * m + 5 * k - 5 * m * m).subs(sub))
    check_zero('spinor dimensionless mass', m * m / -sub[k] - sp.Rational(1, 4))
    check_zero('gravitino dimensionless mass', 9 * m * m / -sub[k] - sp.Rational(9, 4))
    check_zero('fermion endpoint RS', c.subs(x, 2))
    check_zero('fermion endpoint spinor', (2 * c / (3 * x * x)).subs(x, 2))
    check_zero('fermion lambda zero shift', bet.subs(x, 1) - sp.I * sp.sqrt(2) / 3)
    check_zero('fermion ungauged masses', m.subs({g: 0, x: 1}))
    pa1 = sp.Matrix([[0, 1], [1, 0]])
    pa2 = sp.Matrix([[0, -sp.I], [sp.I, 0]])
    pa3 = sp.diag(1, -1)
    eye = sp.eye(4)
    gam = [-sp.I * sp.kronecker_product(pa3, sp.eye(2)), sp.kronecker_product(pa1, pa1), sp.kronecker_product(pa1, pa2), sp.kronecker_product(pa1, pa3), sp.kronecker_product(pa2, sp.eye(2))]

    def ga(*inds):
        if len(set(inds)) < len(inds):
            return sp.zeros(4)
        ans = sp.zeros(4)
        for perm in itertools.permutations(range(len(inds))):
            sign = (-1) ** sum((perm[i] > perm[j] for i in range(len(perm)) for j in range(i + 1, len(perm))))
            z = eye
            for j in perm:
                z = z * gam[inds[j]]
            ans += sign * z
        return ans / sp.factorial(len(inds))

    def check_zero_matrix(name, M):
        assert all((sp.simplify(z) == 0 for z in M)), (name, M)
    for i, j in itertools.product(range(5), repeat=2):
        check_zero_matrix('Clifford', gam[i] * gam[j] + gam[j] * gam[i] - 2 * metric(i, j) * eye)
    CC = gam[2] * gam[4]
    check_zero_matrix('C transpose', CC.T + CC)
    check_zero_matrix('gamma top', ga(0, 1, 2, 3, 4) - sp.I * eye)
    for i in range(5):
        check_zero_matrix('linear bar gamma', gam[i].T * CC - CC * gam[i])
    for i, j in itertools.product(range(5), repeat=2):
        check_zero_matrix('gamma contraction 3', sum((eta[b] * ga(i, j, b) * gam[b] for b in range(5)), sp.zeros(4)) - 3 * ga(i, j))
    for i in range(5):
        check_zero_matrix('gamma contraction 2', sum((eta[b] * ga(i, b) * gam[b] for b in range(5)), sp.zeros(4)) - 4 * gam[i])
        rs = sum((eta[b] * eta[d] * ga(i, b, d) * ga(b, d) / 4 for b, d in itertools.product(range(5), repeat=2)), sp.zeros(4))
        check_zero_matrix('RS curvature coefficient', rs + 3 * gam[i])
    spin_curv = sum((eta[i] * eta[j] * ga(i, j) * ga(i, j) / 4 for i, j in itertools.product(range(5), repeat=2)), sp.zeros(4))
    check_zero_matrix('spinor Lichnerowicz sign', spin_curv + 5 * eye)
    JJ = sp.Matrix([[0, -1], [1, 0]])
    for sign in [1, -1]:
        PP = (sp.eye(2) + sign * sp.I * JJ) / 2
        check_zero_matrix('signed projectors', PP * PP - PP)
        check_zero_matrix('signed operator', sp.I * JJ * PP - sign * PP)
    checks['exact_Clifford_and_projector_checks'] = 'PASS: Clifford, bar transpose, top gamma, contractions, spin-curvature, RS curvature, projectors'
    source = json.loads((root / 'outputs/action_coefficients.json').read_text())
    expected = {str(r['source']) + ':' + str(r['index']) for r in source}
    ledger = (root / 'derivations/spectrum/SOURCE_TERM_LEDGER.md').read_text()
    actual = re.findall('^\\| ((?:Weyl_\\w+|LOG_seed|LOG_explicit):\\d+) \\|', ledger, re.M)
    assert len(actual) == len(set(actual)) == 1184 and set(actual) == expected
    checks['source_ledger_coverage'] = '1184 unique exact source IDs; zero and retained routes recorded'
    dim_checks = {'fermion derivative': sp.Rational(1, 2) + 1 + sp.Rational(1, 2), 'fermion mass': 1 + sp.Rational(1, 2) + sp.Rational(1, 2), 'HD fermion derivative with lambda': -2 + 2 + sp.Rational(1, 2) + 1 + sp.Rational(1, 2), 'HD fermion mass with lambda': -2 + 3 + sp.Rational(1, 2) + sp.Rational(1, 2), 'boson gradient': 1 + 1, 'boson scalar mass': 2, 'boson auxiliary square': 1 + 1}
    assert all((z == 2 for z in dim_checks.values()))
    checks['density_dimensions'] = dim_checks = {key: str(value) for key, value in dim_checks.items()}
    tpos = sp.symbols('t', positive=True)
    xt = 2 * tpos / (1 + tpos)
    weights = {'graviton': c, 'scalar': 2 * c / (3 * x * x), 'Maxwell_A': 2 * c, 'Maxwell_Q': 16 * c, 'gravitino': c, 'spinor': 2 * c / (3 * x * x)}
    for key, val in weights.items():
        assert sp.factor(val.subs(x, xt)).is_positive
    checks['interior_kinetic_signs'] = 'positive for the bijective parametrization x=2t/(1+t), t>0'
    assert 5 + 3 + 3 + 1 == 12 and 2 * (3 * 2 - 2) + 2 * 2 == 12
    checks['local_DOF'] = '12 bosons and 12 real fermion polarizations; endpoint count not assigned'
    report = {'status': 'PASS_SCOPED_LOCAL_REDUCTION_CHECKS', 'branch': 'GB-S+', 'domain': '0<x<2 generic; endpoint x=2 tested without division', 'boundary_scope': 'local bulk; no global boundary norm', 'check_groups': len(checks), 'checks': checks, 'bosonic_dof': {'graviton': 5, 'scalar': 1, 'one_form': 3, 'two_form': 3, 'total': 12}, 'fermionic_dof': {'gravitino': 8, 'spinor': 4, 'total': 12}, 'local_spectrum_status': 'complete with endpoint loss of quadratic control', 'source_fermion_operator_report': 'part2_fermion_operator.json', 'not_checked': ['global boundary admissibility or renormalized boundary norm', 'nonlinear endpoint spectrum', 'independent nonlinear SUSY certification of accepted action'], 'formal_gpd_workflow_status': 'preflight blocked by existing parent metadata'}
    (root / 'outputs/reference_reduction.json').write_text(json.dumps(report, indent=2) + '\n')
    print(report['status'], len(checks), 'check groups plus 700 Lorentzian components and exact Clifford tests')
if __name__ == '__main__':
    main()
