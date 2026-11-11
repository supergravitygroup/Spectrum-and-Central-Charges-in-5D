"""Compare the current action/charges with Gold et al. at first order.

Primary sources: arXiv:2309.07637v2, p.4 Eq.(19); Gold et al. 2025,
pp.15-17 Eqs.(30)-(34),(38),(41). Couplings are expanded together about
L0=1 at fixed original g and kappa. This does not certify an all-orders
minimal truncation or the full gauge completion. Read-only: JSON on stdout.
"""
import json
from pathlib import Path
import sympy as s
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "generic_ads5_massless"))
import action_inputs as current
from derive import derive as current_derivation

q = s.Rational
R, Ric2, Riem2, g, gg, L, N = s.symbols('R Ricci2 Riemann2 g g_Gold L N')
alpha, beta, zeta, kap, G, lam1, lam2, lam3, h = s.symbols(
    'alpha beta zeta kappa G lambda1 lambda2 lambda3 h', nonzero=True)
results = []

def verify(name, residual):
    residual = s.factor(residual)
    assert residual == 0, (name, residual)
    results.append({'name': name, 'status': 'PASS_EXACT'})

# Gauge fields set to zero, but arbitrary metric curvature retained. These
# are the manuscript's own invariant normalizations, before scalar elimination.
w = Riem2/8-Ric2/6+R**2/24-g*N*R/3-g**2*L**2*R/12 \
    +4*g**2*N**2/3+2*g**3*N*L**2/3+g**4*L**4/12
log = -Ric2/6+R**2/24+g*N*R/6-g**2*L**2*R/12 \
    -g**2*N**2/6+2*g**3*N*L**2/3+5*g**4*L**4/24
r2 = (-R/2-N**2/L**2)**2-4*g*N**3/L**2 \
    -g**2*L**2*R/4-q(5,2)*g**2*N**2+g**4*L**4/16
minimal = {L:1, N:-q(3,2)*g}
gold_w = Riem2-q(4,3)*Ric2+R**2/3+q(20,3)*gg**2*R+q(200,3)*gg**4
gold_log = R**2-4*Ric2-16*gg**2*R-112*gg**4
gold_r2 = R**2+16*gg**2*R+208*gg**4
for name, factor, manuscript, source in [
    ('Gold2025 Eq32 Weyl normalization', 8, w, gold_w),
    ('Gold2025 Eq33 Log normalization', 24, log, gold_log),
    ('Gold2025 Eq34 R2 normalization', 4, r2, gold_r2),
]:
    verify(name, factor*manuscript.subs(minimal).subs(g,s.sqrt(2)*gg)-source)

conversion = {gg:g/s.sqrt(2), G:kap**2/(8*s.pi),
              lam1:alpha/8, lam2:beta/24, lam3:zeta/4}
agold = s.pi/(8*gg**3*G)-9*s.pi*(lam2+lam3)/(2*gg*G)
cgold = s.pi/(8*gg**3*G)+s.pi*(2*lam1-9*lam2-9*lam3)/(2*gg*G)
# Derive L0's first-order coefficient from the manuscript vacuum polynomial,
# then expand the exact charges. All three couplings scaled together by h.
tau = (beta+6*zeta)*g**2
l1 = s.solve(s.Eq(tau-8*s.Symbol('l1'),0),s.Symbol('l1'))[0]
# Compare the live calculation, rather than two copies of the published answer.
live = current_derivation()
conversion_symbols = {current.L:L, current.N:N, current.g:g, current.alpha:alpha,
                      current.beta:beta, current.zeta:zeta, current.R:R,
                      current.Ricci2:Ric2, current.Riemann2:Riem2}
for name, independent in (("weyl",w),("log",log),("r2",r2)):
    verify("current curvature input / " + name,
           current.curvature_blocks()[name].xreplace(conversion_symbols)-independent)
Qlive = live["vacuum_polynomial"].xreplace(conversion_symbols)
scaled = {alpha:h*alpha, beta:h*beta, zeta:h*zeta}
trial = s.Symbol("first_order_L")
Qfirst = s.expand(Qlive.subs(scaled, simultaneous=True).subs(L,1+h*trial)).coeff(h,1)
verify("current vacuum expansion", Qfirst.subs(trial,l1))
Lfirst = 1+h*l1
pref = 2*s.sqrt(2)*s.pi**2/(g**3*kap**2)
aexact = pref*live["a_normalized"].xreplace(conversion_symbols).subs(scaled, simultaneous=True).subs(L,Lfirst)/Lfirst**3
cexact = pref*live["c_normalized"].xreplace(conversion_symbols).subs(scaled, simultaneous=True).subs(L,Lfirst)/Lfirst**3
afirst = s.series(aexact,h,0,2).removeO().subs(h,1)
cfirst = s.series(cexact,h,0,2).removeO().subs(h,1)
verify('Gold2023 Eq19 versus manuscript a at first order',
       agold.subs(conversion, simultaneous=True)-afirst)
verify('Gold2023 Eq19 versus manuscript c at first order',
       cgold.subs(conversion, simultaneous=True)-cfirst)
# Different field redefinitions in Gold2025 must give the same charges.
ell0 = 1/gg
ell = ell0*(1-4*h*(lam2+lam3)/ell0**2)
sigma = (1/G)*(1-24*h*(lam2+lam3)/ell0**2)
a2025 = s.series(s.pi*ell**3*sigma/8,h,0,2).removeO().subs(h,1)
c2025 = s.series(s.pi*ell**3*sigma*(1+8*h*lam1/ell**2)/8,h,0,2).removeO().subs(h,1)
verify('Gold2025 Eqs38,41 versus Gold2023 a', a2025-agold)
verify('Gold2025 Eqs38,41 versus Gold2023 c', c2025-cgold)

# A plausible but wrong Ricci-square-leading normalization is caught.
wrong = dict(conversion, **{})
wrong[lam2] = -beta/6
residual_wrong = s.factor(agold.subs(wrong, simultaneous=True)-afirst)
assert residual_wrong != 0
payload = {
    'status':'PASS_FIRST_ORDER_EXTERNAL_BENCHMARK',
    'sympy':s.__version__,
    'manuscript':'draft_v109, Eq.(3.63), p.36, line 968',
    'primary_sources':[
        'Gold et al., arXiv:2309.07637v2, p.4 Eq.(19) and rescaling paragraph',
        'Gold et al., On five-dimensional curvature squared supergravity and holography (2025), pp.15-17 Eqs.(30)-(34),(38),(41); references/bibliography.md#goldetal2025'],
    'conversions':{'g_Gold':'g/sqrt(2)','G':'kappa^2/(8 pi)',
                   'lambda1':'alpha/8','lambda2':'beta/24','lambda3':'zeta/4'},
    'scope':'First order about L0=1, minimal truncation, fixed original g and kappa. Not a comparison of field-redefined radii beyond first order. Pure-metric terms determine coupling normalization; full gauge completion not separately rederived here.',
    'a_over_a0':str(s.factor(afirst/pref)),
    'c_over_a0':str(s.factor(cfirst/pref)),
    'records':results,
    'negative_control':{'mutation':'wrong lambda2=-beta/6',
                        'status':'DETECTED','a_residual':str(residual_wrong)},
}
print(json.dumps(payload,indent=2))
