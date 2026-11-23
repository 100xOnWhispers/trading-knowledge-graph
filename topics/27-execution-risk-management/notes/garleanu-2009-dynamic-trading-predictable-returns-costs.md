---
title: "Dynamic Trading with Predictable Returns and Transaction Costs"
authors: "Garleanu, Nicolae B.; Pedersen, Lasse H."
year: 2009
venue: "NBER Working Paper 15205"
url: "https://www.nber.org/system/files/working_papers/w15205/w15205.pdf"
pdf: "sources/27-execution-risk-management/garleanu-2009-dynamic-trading-predictable-returns-costs.pdf"
access: "full-text"
source_type: "working-paper"
evidence_grade: "B"
topic: "27-execution-risk-management"
asset_class: "futures"
horizon: "daily"
tags: "transaction-costs, alpha-decay, turnover-control, dynamic-portfolio, partial-adjustment"
---

## Key insight
When signals decay at different speeds and trading has quadratic cost, the optimal policy has two parts: move only a fixed fraction of the way from the current position toward a target each period, and make that target an "aim portfolio" that down-weights fast-decaying signals. A signal's value under costs depends on its persistence as much as on its strength.

## Method
Infinite-horizon linear-quadratic problem. Returns are linear in factors `f` that mean-revert at rates `Phi`. Trading `dx` costs `0.5 * dx' * Lambda * dx`. The investor maximises discounted expected return minus `gamma/2` times variance minus costs. Under their Assumption A (`Lambda = lambda * Sigma`, cost proportional to risk):

- Trade partially toward the aim: `x_t = (1 - a/lambda) * x_(t-1) + (a/lambda) * aim_t`, where the trading rate `a/lambda < 1` falls with cost `lambda` and rises with risk aversion `gamma`.
- Aim in front of the target: `aim_t = z * Markowitz_t + (1 - z) * E_t[aim_(t+1)]` with `z = gamma/(gamma + a)`. With independent factor decay rates `phi_k`, the aim is the Markowitz portfolio with each factor scaled by `1/(1 + phi_k * a/gamma)`.

The static alternative, one-period cost optimisation, trades partially toward the Markowitz portfolio itself and ignores decay.

## Data and sample
15 commodity futures (LME metals, ICE gasoil, NYMEX energy, COMEX gold and silver, NYBOT softs), daily, 01/01/1996 to 01/23/2009. Predictors: own past returns over 5 days, 1 year and 5 years, scaled by volatility. Cost parameter calibrated from equity price-impact estimates in other papers; a second run uses a cost twice as high.

## Reported results
- Estimated signal half-lives: 2.4 days (5-day signal), 206 days (1-year), 700 days (5-year).
- The no-cost Markowitz strategy has the best gross Sharpe ratio but "incurs enormous trading costs".
- The dynamic strategy has the best net Sharpe ratio, about 20% above the best of ten static partial-adjustment strategies.
- The gain comes from putting less weight on the 5-day signal, not from trading more slowly overall.
- After a shock to the fast signal the optimal position builds slowly, never reaches the Markowitz size, and exits slowly.

## Signal construction
Not a signal; it is the layer between forecasts and orders. For a single-asset bot: (1) estimate each signal's decay rate `phi_k` from the autocorrelation of the signal; (2) scale each signal's contribution by `1/(1 + phi_k * a/gamma)`; (3) each decision step, move a fraction `a/lambda` of the gap between current and aim position. `a` has a closed form in `gamma`, `lambda` and the discount rate. Recompute at the bot's decision frequency.

## Relevance to SOL perpetuals at minutes to hours
The principle transfers directly: a one-minute order-flow signal with a half-life of seconds deserves little position under a 12 bp taker fee, while a slower basis or funding signal deserves more, even if its instantaneous predictive power is lower. The quadratic-cost assumption does not transfer. Costs for a small account are close to linear (spread and fees per unit), which produces a no-trade band, not smooth partial adjustment; see the de Lataillade et al. note. A practical hybrid is to use decay-weighted aims here and a band around them.

## Caveats
Working-paper version read; a later journal version was not opened. Costs are quadratic and calibrated from equity studies, not measured in the commodity markets traded. Predictive coefficients and covariances use the full sample, so the comparison is in-sample. One author is affiliated with an asset manager, as disclosed in the paper. Daily data; nothing intraday.
