# Calibration-Anchor Optimization for fsQCA — Formal Problem Statement

## 1. Notation

- $N$ cases, $i = 1,\dots,N$; $K$ causal conditions, $k = 1,\dots,K$; one outcome $Y$.
- $x_{ik}$: raw value of condition $k$ for case $i$; $y_i^{raw}$: raw outcome value.
- Anchor of condition $k$: $a_k = (e_k, c_k, i_k)$, $e_k < c_k < i_k$
  (e = fully out, c = crossover, i = fully in). Full anchor set: $\mathbf{a} = (a_1,\dots,a_K)$.
  The outcome anchor $a_Y$ is held fixed throughout.
- $\hat F_k$: empirical CDF of $x_{\cdot k}$, $\hat F_k^{-1}$ its empirical quantile function.
  Anchors are expressed in **percentile space**: $q_k = \big(\hat F_k(e_k),\hat F_k(c_k),\hat F_k(i_k)\big)$,
  and recovered by $\mathbf{a}(\mathbf{q}) = \big(\hat F_k^{-1}(q_k)\big)_k$.

## 2. Calibration (direct method)

$$\mu_{ik}(a_k) = \sigma(z_{ik}), \qquad \sigma(z)=\frac{1}{1+e^{-z}}, \qquad
z_{ik} = \begin{cases} L\,\dfrac{x_{ik}-c_k}{i_k-c_k} & x_{ik}\ge c_k\\[2mm]
L\,\dfrac{x_{ik}-c_k}{c_k-e_k} & x_{ik}<c_k \end{cases}, \qquad L=\ln\frac{0.95}{0.05}\approx 2.944$$

so that $\mu=0.05$ at $e_k$, $\mu=0.5$ at $c_k$, $\mu=0.95$ at $i_k$. Outcome membership $y_i=\mu_i^Y(a_Y)$
is computed the same way. Any case with $\mu=0.5$ exactly is nudged to $0.501$.

## 3. Truth-table row membership

Each row $r$ corresponds to a binary vector $s^r\in\{0,1\}^K$, $R=2^K$ rows:

$$m_{ir}(\mathbf{a}) = \min_{k=1,\dots,K}\begin{cases}\mu_{ik} & s^r_k=1\\ 1-\mu_{ik} & s^r_k=0\end{cases}$$

## 4. Row OUT-score (case-weighted)

$w\in\mathbb{R}_{\ge0}^N$: case weights ($w=\mathbf{1}$ for the full sample; a bootstrap replicate uses
the replicate counts of each case). Define

$$n_r(w)=\sum_i w_i\,\mathbb 1[m_{ir}>0.5], \qquad
\text{incl}_r(w)=\frac{\sum_i w_i\min(m_{ir},y_i)}{\sum_i w_i\,m_{ir}}, \qquad
\text{PRI}_r(w)=\frac{\sum_i w_i\min(m_{ir},y_i)-\sum_i w_i\min(m_{ir},y_i,1-y_i)}{\sum_i w_i\,m_{ir}-\sum_i w_i\min(m_{ir},y_i,1-y_i)}$$

$$O_r(\mathbf{a};w)=\mathbb 1\big[\,n_r\ge\nu \;\wedge\; \text{incl}_r\ge\tau \;\wedge\; \text{PRI}_r\ge\pi\,\big],
\qquad \nu=2,\ \tau=0.85,\ \pi=0.60$$

Positive-row set: $\mathcal P(\mathbf{a};w)=\{r: O_r(\mathbf{a};w)=1\}$. The conservative solution is a
deterministic function of $\mathcal P$.

## 5. Stability (the quantity being maximized)

$B=200$ bootstrap weight vectors $w^{(1)},\dots,w^{(B)}\sim\text{Multinomial}(N;\tfrac1N,\dots,\tfrac1N)$ are drawn
**once**, from a seed that is separate from any random seed used by the solver (common random numbers). Hence $S$
is a deterministic function of $\mathbf a$:

$$S(\mathbf a)=\frac1B\sum_{b=1}^B J\big(\mathcal P(\mathbf a;w^{(b)}),\,\mathcal P(\mathbf a;\mathbf 1)\big),
\qquad J(A,B)=\frac{|A\cap B|}{|A\cup B|},\ \ J(\varnothing,\varnothing):=1$$

$S$ measures how much the set of configurations judged to explain the outcome changes under case resampling
(equivalently, how sensitive the conclusion is to the influence of individual cases).

**$S$ depends on the outcome.** Membership of a row in $\mathcal P$ is computed from $\text{incl}_r$ and $\text{PRI}_r$,
which contain $y_i$. The outcome therefore enters $S$ by *defining which conclusion must be stable*; the objective
rewards invariance of that conclusion under resampling, not a better fit of any configuration to $y$.

## 6. Decision variables and expert information

**Parametrization.** For each condition $k$ the decision variables are $\theta_k=(c_k,\,t_{e,k},\,t_{i,k})$, with
$c_k$ the crossover percentile and $t_{e,k},t_{i,k}\in[0,1]$ relative positions of the outer anchors:

$$q_{k,2}=c_k,\qquad
q_{k,1}=\delta+(c_k-2\delta)\,t_{e,k},\qquad
q_{k,3}=c_k+\delta+(1-c_k-2\delta)\,t_{i,k}$$

with minimum percentile gap $\delta=0.05$. This guarantees $q_{k,1}\ge\delta$, $q_{k,2}-q_{k,1}\ge\delta$,
$q_{k,3}-q_{k,2}\ge\delta$, $1-q_{k,3}\ge\delta$ by construction, provided $c_k\in[2\delta,1-2\delta]$.

**Expert information as a box constraint on the crossover.** Expert or literature knowledge enters as an
interval for each crossover in raw units, $c_k^{raw}\in[c_k^{lo},c_k^{hi}]$. Translated to percentile space:

$$c_k\in\mathcal C_k=\big[\hat F_k(c_k^{lo}),\,\hat F_k(c_k^{hi})\big]\cap[2\delta,\,1-2\delta]$$

If no expert interval is available for condition $k$, $\mathcal C_k=[2\delta,\,1-2\delta]$. All decision variables
are therefore box-constrained:

$$\Theta=\prod_{k=1}^K \mathcal C_k\times[0,1]^2 .$$

The width of $\mathcal C_k$ encodes the strength of prior knowledge: a degenerate interval fixes the crossover
at the expert value, and the widest interval leaves it entirely to the data.

**Optional regularization.** A soft pull toward a reference crossover $q_k^{0}$ can be added with weight
$\lambda\ge0$ (default $\lambda=0$):

$$R(\theta)=\frac1K\sum_{k=1}^K \omega\,\big(c_k-q_{k,2}^{0}\big)^2 ,$$

where $q_k^{0}$ is the percentile of a theoretical anchor or of a data-driven reference (e.g. the KDE antimode of
$x_{\cdot k}$ nearest the median, falling back to the median when the distribution is unimodal). With
$\lambda=0$ the expert interval is the only external information used.

## 7. The optimization problem

$$\max_{\theta\in\Theta}\;\; S\big(\mathbf a(\mathbf q(\theta))\big)\;-\;\lambda\,R(\theta)$$

subject to

$$\begin{aligned}
\text{C2 (consistency floor):}\quad & \mathrm{Cons}(\mathbf a)\ge 0.80\\[1mm]
\text{C3 (coverage floor):}\quad & \mathrm{Cov}(\mathbf a)\ge 0.50\\[1mm]
\text{C4 (no degenerate/skewed set):}\quad & 0.30 \le \frac1N\sum_i \mathbb 1[\mu_{ik}>0.5] \le 0.70,\ \ \forall k\\[1mm]
\text{C5 (non-trivial solution):}\quad & \big|\mathcal P(\mathbf a;\mathbf 1)\big|\ge 2
\end{aligned}$$

where

$$s_i=\max_{r\in\mathcal P(\mathbf a;\mathbf 1)} m_{ir}, \qquad
\mathrm{Cons}=\frac{\sum_i\min(s_i,y_i)}{\sum_i s_i}, \qquad
\mathrm{Cov}=\frac{\sum_i\min(s_i,y_i)}{\sum_i y_i}$$

The ordering and gap constraint (C1) is absorbed into the parametrization of §6. C2–C5 are inequality
constraints $g_j(\theta)\ge 0$; a solution is feasible only if all four hold, and feasible solutions are
always preferred to infeasible ones (feasibility rule), so no penalty weights appear in the formulation.

**Role of the outcome.** $y$ enters (i) through $\mathcal P$ inside $S$, as the definition of the conclusion
whose stability is rewarded, and (ii) through C2/C3, as feasibility floors. Exceeding a floor earns no extra
reward, so the objective never trades stability for a better consistency or coverage.

**Rationale for C4.** Without C4, the optimizer can push one condition's crossover toward a distribution tail,
making its negation a near-majority, near-crisp set that is trivially stable under resampling without
reflecting a more robust causal story. The expert interval $\mathcal C_k$ provides a second, theory-based
safeguard against the same failure.

## 8. Properties and solution concept

- $S$ and the constraint functions are piecewise constant in $\theta$ (they contain indicators of row status),
  so the problem has no useful gradient and many near-equivalent local optima.
- The solution concept is therefore a **set**: optimization is repeated over independent solver seeds with the
  bootstrap weights of §5 held fixed, and the distribution of optimal anchors and objective values is reported,
  not a single point.
- **Profile of stability.** For a condition $k$ and a value $c\in\mathcal C_k$, define
  $$S_k^*(c)=\max_{\theta\in\Theta:\ c_k=c,\ \text{C2–C5}} S(\mathbf a(\mathbf q(\theta))).$$
  Plotting $S_k^*(c)$ over $\mathcal C_k$ shows how much stability is sacrificed by choosing a crossover other
  than the maximizer, and flags crossovers at which stability is abnormally sensitive. If the maximizer lies on
  the boundary of $\mathcal C_k$, the result reflects the expert interval rather than the data and should be
  reported as such.
