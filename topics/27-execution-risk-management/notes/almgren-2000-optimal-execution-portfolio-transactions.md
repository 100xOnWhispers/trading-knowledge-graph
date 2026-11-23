---
title: "Optimal Execution of Portfolio Transactions"
authors: "Almgren, Robert; Chriss, Neil"
year: 2000
venue: "Preprint dated December 2000 (later journal publication not confirmed in this session)"
url: "https://www.smallake.kr/wp-content/uploads/2016/03/optliq.pdf"
pdf: "none"
access: "full-text"
source_type: "working-paper"
evidence_grade: "B"
topic: "27-execution-risk-management"
asset_class: "equities"
horizon: "n/a"
tags: "optimal-execution, market-impact, implementation-shortfall, efficient-frontier, trade-scheduling"
---

## Key insight
Executing an order is a trade-off between impact cost, which falls when you trade slowly, and price risk, which rises when you trade slowly. With linear impact the trade-off has a closed-form solution: an efficient frontier of schedules indexed by risk aversion, each decaying exponentially at a rate set by volatility, impact and risk aversion. Every risk-averse trade therefore has an intrinsic "half-life" that does not depend on the deadline.

## Method
Discrete-time model. Holdings `x_k` are run down from `X` to 0 over `N` intervals of length `tau`. Price follows an arithmetic random walk with volatility `sigma`. Permanent impact is linear in trading rate, `g(v) = gamma*v`. Temporary impact is `h(v) = epsilon*sgn(n) + eta*v`, where `epsilon` is a fixed cost (the paper suggests half the bid-ask spread plus fees) and `eta` is the slope of cost in trading rate. The trader minimises `E + lambda*V`, expected shortfall plus `lambda` times its variance.

Solution: `x_j = X * sinh(kappa*(T - t_j)) / sinh(kappa*T)`, with `kappa ~ sqrt(lambda*sigma^2/eta)` for short intervals. The half-life is `theta = 1/kappa`. If `T >> theta` most trading happens early; if `T << theta` the schedule is close to a straight line (equal slices), which is the minimum-expected-cost strategy. A value-at-risk version ("L-VaR") and extensions for drift, serial correlation and scheduled events are also given.

## Data and sample
No empirical data. One numerical example: 1,000,000 shares at $50, 30% annual volatility, bid-ask spread 1/8, daily volume 5 million shares, liquidation over 5 days in 5 daily trades.

## Reported results
- Example parameters: `epsilon` = 0.0625 $/share, `eta` = 2.5e-6, `gamma` = 2.5e-7, `lambda` = 1e-6; these give `kappa` of about 0.6 per day and `kappa*T` of about 3.
- The frontier is smooth and convex. At the minimum-cost (equal-slice) point it is flat, so a first-order reduction in variance costs only a second-order increase in expected cost.
- With linear impact, the optimal schedule's time scale is independent of order size; the authors flag this as an artefact that disappears with super-linear impact.
- Under risk neutrality the half-life is infinite and the schedule is the equal-slice one.
- A sell programme never buys, unless there is drift or serial correlation.

## Signal construction
Not a signal. It is a scheduling rule for working a parent order. Inputs: `sigma` per unit time in price units, `eta` estimated from book slope or own fills, a risk-aversion `lambda`, and the deadline `T`. Compute `kappa = sqrt(lambda*sigma^2/eta)` and slice sizes `n_j = X * 2*sinh(kappa*tau/2)/sinh(kappa*T) * cosh(kappa*(T - t_(j-1/2)))`. Re-estimate `sigma` and `eta` at least daily.

## Relevance to SOL perpetuals at minutes to hours
The half-life is the useful object. When volatility is high relative to impact, `kappa` is large and the answer is "trade now". For clips well inside displayed depth on the Kalshi SOL perp, `eta` is small and slicing buys little; the binding costs are the fixed term `epsilon` (spread plus fees), which the model treats as unavoidable. The framework starts to matter when order size approaches visible depth or when exits must be staged in a thin book. The drift extension is the entry point for signal-aware execution (see the Lehalle and Neuman and Garleanu and Pedersen notes).

## Caveats
Linear, time-invariant impact and a pure random walk; real impact is concave and transient (see topic 09). The fixed cost `epsilon` is exogenous, so the model says nothing on limit versus market orders. The canonical author-hosted copy returned an access error, so the text was read from a third-party mirror of the December 2000 preprint and no PDF is stored. No empirical validation in the paper.
