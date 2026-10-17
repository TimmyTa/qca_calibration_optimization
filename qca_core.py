"""
qca_core -- the fsQCA building blocks shared by the optimizer and the evaluation.
Pure Python (numpy); no R needed.

  calibrate()               direct method (Ragin 2008), log-odds L at e / i
  crispness()               mean 2|mu - .5|
  truth_table()             row membership, n_r, incl_r, PRI_r (optionally weighted)
  out_rule()                OUT = 1 if n_r >= nu, incl_r >= tau, PRI_r >= pi
  solution_fit()            consistency / coverage of the union of OUT=1 rows
  minimize()                Quine-McCluskey + minimal covers (with a safety cap)
  conservative / parsimonious solutions
  compare_with_truth()      solution vs the true causal model (asf)

Notation for formulas: literals "A" (presence) / "a" (absence), terms joined by
"*", disjunction by "+", outcome after "<->"; e.g. "A*b + C*D <-> Y".
"""
from itertools import combinations
from math import comb

import numpy as np

DASH = -1     # "don't care" position in a term


# ============================================================ calibration ===
def calibrate(x, anchor, L=3.0):
    """Direct method: mu = .5 at c, log-odds +-L at i / e (L = 3.0 -> .953 / .047,
    L = ln 19 -> .95 / .05). Exact 0.5 is nudged to 0.501 (QCA convention)."""
    e, c, i = anchor
    x = np.asarray(x, float)
    with np.errstate(divide="ignore", invalid="ignore"):
        z = np.where(x >= c, L * (x - c) / (i - c), L * (x - c) / (c - e))
    z = np.clip(np.nan_to_num(z, nan=0.0, posinf=50, neginf=-50), -50, 50)
    mu = 1.0 / (1.0 + np.exp(-z))
    return np.where(np.abs(mu - 0.5) < 1e-12, 0.501, mu)


def crispness(mu):
    """Mean 2|mu - .5| (0 = every membership at .5, 1 = fully crisp)."""
    return float(np.mean(2 * np.abs(np.asarray(mu) - 0.5)))


def ecdf(x, v):
    return float(np.mean(np.asarray(x) <= v))


# ============================================================ truth table ===
def row_bits(K):
    """(2^K, K) bool; row r <-> bits, first condition = most significant bit."""
    return np.array([[(r >> (K - 1 - j)) & 1 for j in range(K)] for r in range(2 ** K)], bool)


def row_membership(mu, bits):
    """mu (N, K) -> (N, 2^K): min over conditions of mu or 1 - mu."""
    both = np.where(bits[None, :, :], mu[:, None, :], 1 - mu[:, None, :])
    return both.min(axis=2)


def truth_table(mu, y, bits, W=None):
    """Return m (N, R) and n, incl, PRI, each (b, R) for case-weight rows W
    (W=None -> one row of ones, i.e. the full sample)."""
    m = row_membership(mu, bits)
    W = np.ones((1, len(y))) if W is None else W
    a1 = np.minimum(m, y[:, None])
    a2 = np.minimum(a1, 1 - y[:, None])
    n = W @ (m > 0.5)
    sm, s1, s2 = W @ m, W @ a1, W @ a2
    incl = np.divide(s1, sm, out=np.zeros_like(sm), where=sm > 0)
    pri = np.divide(s1 - s2, sm - s2, out=np.zeros_like(sm), where=(sm - s2) > 0)
    return m, n, incl, pri


def out_rule(n, incl, pri, nu, tau, pi):
    return (n >= nu) & (incl >= tau) & (pri >= pi)


def solution_fit(m, y, positive):
    """Consistency / coverage of s_i = max over OUT=1 rows of m_ir."""
    if not np.any(positive):
        return 0.0, 0.0
    s = m[:, positive].max(axis=1)
    num = np.minimum(s, y).sum()
    return float(num / s.sum()) if s.sum() > 0 else 0.0, float(num / y.sum())


def rule_from_data(mu, y, bits, keep_share=0.8):
    """incl / PRI / n.cut from the data (no ground truth):
      n.cut = largest frequency threshold that keeps >= keep_share of cases
      PRI   = middle of the largest gap in row PRI within [.50, .75]
      incl  = middle of the largest gap in row consistency within [.75, .90]
    (rows below n.cut are ignored for the gaps)."""
    m, n, incl, pri = truth_table(mu, y, bits)
    n, incl, pri = n[0], incl[0], pri[0]
    nu = 1
    for k in sorted(set(n[n > 0].astype(int))):
        if n[n >= k].sum() >= keep_share * len(y):
            nu = int(k)
    keep = n >= nu
    return {"nu": nu, "tau": _gap_cut(incl[keep], .75, .90, .80), "pi": _gap_cut(pri[keep], .50, .75, .50)}


def _gap_cut(vals, lo, hi, default):
    v = np.sort(np.asarray(vals)[(np.asarray(vals) >= lo) & (np.asarray(vals) <= hi)])
    if len(v) < 2:
        return default
    j = int(np.argmax(np.diff(v)))
    return float((v[j] + v[j + 1]) / 2)


# ======================================================= minimization (QMC) ===
def _row_term(r, K):
    return tuple((r >> (K - 1 - j)) & 1 for j in range(K))


def _covers(term, minterm):
    return all(t == DASH or t == m for t, m in zip(term, minterm))


def prime_implicants(terms):
    current, primes = set(terms), []
    while current:
        used, nxt = set(), set()
        cur = list(current)
        for a, b in combinations(cur, 2):
            diff = [i for i in range(len(a)) if a[i] != b[i]]
            if len(diff) == 1 and a[diff[0]] != DASH and b[diff[0]] != DASH:
                t = list(a); t[diff[0]] = DASH
                nxt.add(tuple(t)); used |= {a, b}
        primes += [t for t in cur if t not in used]
        current = nxt
    return primes


def minimal_covers(primes, must_cover, max_checks=200_000):
    """All minimum-size covers (fewest prime implicants; ties broken by fewest
    literals). If exhaustive search would exceed max_checks combinations, fall
    back to one greedy cover and flag it."""
    primes = [p for p in primes if any(_covers(p, m) for m in must_cover)]
    chart = {p: {m for m in must_cover if _covers(p, m)} for p in primes}
    target = set(must_cover)
    essential = {next(iter(hit)) for m in target
                 if len(hit := [p for p in primes if m in chart[p]]) == 1}
    covered = set().union(*(chart[p] for p in essential)) if essential else set()
    rest = target - covered
    if not rest:
        return [tuple(sorted(essential))], False
    others = [p for p in primes if p not in essential]
    checks = 0
    for size in range(1, len(others) + 1):
        checks += comb(len(others), size)
        if checks > max_checks:
            break
        sols = [c for c in combinations(others, size)
                if rest <= set().union(*(chart[p] for p in c))]
        if sols:
            lits = lambda c: sum(sum(v != DASH for v in t) for t in c)
            best = min(map(lits, sols))
            return [tuple(sorted(essential | set(c))) for c in sols if lits(c) == best], False
    # greedy fallback
    chosen, left = set(essential), set(rest)
    while left:
        p = max(others, key=lambda q: (len(chart[q] & left), -sum(v != DASH for v in q)))
        chosen.add(p); left -= chart[p]
    return [tuple(sorted(chosen))], True


def term_label(term, conds):
    """(1, 0, DASH) -> 'A*b' (lower case = absence)."""
    return "*".join(c if v == 1 else c.lower() for v, c in zip(term, conds) if v != DASH)


def minimize(positive_rows, K, conds, outcome, remainders=(), max_checks=200_000):
    """Positive rows (+ remainders as don't-cares) -> list of solution strings
    "A*b+C<->Y", and a flag telling whether the greedy fallback was used."""
    if len(positive_rows) == 0:
        return [], False
    pos = [_row_term(r, K) for r in positive_rows]
    rem = [_row_term(r, K) for r in remainders]
    primes = prime_implicants(pos + rem)
    covers, truncated = minimal_covers(primes, pos, max_checks)
    sols = ["+".join(term_label(t, conds) for t in c) + f"<->{outcome}" for c in covers]
    return sols, truncated


def solutions(positive, n, K, conds, outcome, nu, max_checks=200_000):
    """Conservative (no remainders) and parsimonious (rows with n < nu treated
    as logical remainders) solutions of a truth table."""
    pos = np.flatnonzero(positive)
    rem = np.flatnonzero(n < nu)
    cs, cs_trunc = minimize(pos, K, conds, outcome, (), max_checks)
    ps, ps_trunc = minimize(pos, K, conds, outcome, rem, max_checks)
    return {"conservative": cs, "parsimonious": ps, "truncated": cs_trunc or ps_trunc}


# ==================================================== comparison with truth ===
def terms(formula):
    """'A*b+C<->Y' -> [frozenset({'A','b'}), frozenset({'C'})]"""
    lhs = formula.split("<->")[0].replace(" ", "")
    return [frozenset(t.split("*")) for t in lhs.split("+") if t]


def compare_with_truth(solution, asf, irrelevant=()):
    """Term-level comparison of a QCA solution with the true asf.
      correct      every solution term contains a true path  -> no false
                   sufficiency claim (natural test for conservative solutions)
      sub_correct  every solution term is contained in a true path -> only
                   true causal literals (natural test for parsimonious solutions)
      complete     every true path is found (conservative: some term contains
                   it; parsimonious: some term is contained in it)
      exact        the set of terms equals the set of true paths
      spurious     factors in the solution that appear in no true path
      irrelevant_in  solution mentions a factor that is irrelevant in the truth"""
    sol, tru = terms(solution), terms(asf)
    implies = [any(p <= t for p in tru) for t in sol]
    inside = [any(t <= p for p in tru) for t in sol]
    found_sup = [any(p <= t for t in sol) for p in tru]
    found_sub = [any(t <= p for t in sol) for p in tru]
    true_factors = {f.upper() for p in tru for f in p}
    sol_factors = {f.upper() for t in sol for f in t}
    return {
        "correct": all(implies), "sub_correct": all(inside),
        "term_precision": sum(implies) / len(sol), "term_precision_sub": sum(inside) / len(sol),
        "complete_sup": all(found_sup), "complete_sub": all(found_sub),
        "paths_found_sup": sum(found_sup) / len(tru), "paths_found_sub": sum(found_sub) / len(tru),
        "exact": set(sol) == set(tru),
        "n_terms": len(sol),
        "spurious": sorted(sol_factors - true_factors),
        "irrelevant_in": bool(sol_factors & {f.upper() for f in irrelevant}),
    }


def row_truth(asf, conds, bits):
    """For every truth-table row (a crisp configuration), does the true asf
    say the outcome is present? -> (2^K,) bool."""
    idx = {c: j for j, c in enumerate(conds)}
    out = np.zeros(len(bits), bool)
    for path in terms(asf):
        ok = np.ones(len(bits), bool)
        for lit in path:
            j = idx[lit.upper()]
            ok &= bits[:, j] if lit.isupper() else ~bits[:, j]
        out |= ok
    return out


def row_scores(positive, observed, truth_rows):
    """Row-level check of the OUT coding, independent of minimization:
      precision  share of OUT=1 rows where the true asf holds
      recall     share of observed rows (n >= 1 case) where the asf holds that are coded OUT=1"""
    tp = int((positive & truth_rows).sum())
    n_pos, n_true_obs = int(positive.sum()), int((observed & truth_rows).sum())
    return {"row_precision": tp / n_pos if n_pos else float("nan"),
            "row_recall": tp / n_true_obs if n_true_obs else float("nan"),
            "false_positive_rows": n_pos - tp}
