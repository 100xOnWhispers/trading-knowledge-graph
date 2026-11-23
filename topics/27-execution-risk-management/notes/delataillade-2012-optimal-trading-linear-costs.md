---
title: "Optimal Trading with Linear Costs"
authors: "de Lataillade, Joachim; Deremble, Cyril; Potters, Marc; Bouchaud, Jean-Philippe"
year: 2012
venue: "arXiv preprint 1203.5957"
url: "https://arxiv.org/pdf/1203.5957"
pdf: "sources/27-execution-risk-management/delataillade-2012-optimal-trading-linear-costs.pdf"
access: "full-text"
source_type: "working-paper"
evidence_grade: "B"
topic: "27-execution-risk-management"
asset_class: "multi"
horizon: "n/a"
tags: "no-trade-band, linear-costs, threshold-rule, turnover-control, ornstein-uhlenbeck"
---

## Key insight
With proportional costs (spread and fees) and a cap on position size, the optimal use of a predictive signal is a hysteresis rule: hold the maximum long or short position and flip only when the predictor crosses a threshold `q*`; do nothing in between. The threshold is not the naive "expected gain exceeds cost" level, because the predictor is autocorrelated and future trading decisions change the value of acting now.

## Method
Single asset, position bounded by `+/- M`, cost `Gamma * |trade|` per unit traded, predictor `p_t` of the next price change. Bellman backward recursion gives the stationary policy: `position = +M if p >= q*`, `-M if p <= -q*`, unchanged otherwise. The threshold solves `g(q*) = Gamma`, where `g(p)` is the expected gain per traded lot including the effect of future flips. Solved explicitly for a discrete Ornstein-Uhlenbeck predictor `p_(t+1) - p_t = -eps * p_t + beta * xi_t`, where `1/eps` is the predictor's autocorrelation time and `beta` its innovation size. Checked by simulation with `eps` = 0.001.

## Data and sample
None. Theory with numerical simulation of the Ornstein-Uhlenbeck case.

## Reported results
- It is always true that `q* <= Gamma`: if the immediate predicted gain alone covers the cost, trade.
- Three regimes for the threshold, as a function of signal innovation `beta`:
  - Weak signal, `beta << Gamma * eps^(3/2)`: `q* = Gamma * eps`, which equals the naive rule (integrated predictability `p/eps` exceeds cost).
  - Intermediate: `q* = (1.5 * Gamma * beta^2)^(1/3)`, so the band scales with the one-third power of cost and does not depend on `eps`.
  - Strong signal, `beta >> Gamma`: `q* = Gamma`.
- For a white-noise predictor (`eps` = 1) the threshold is `Gamma`: trade only when the one-step forecast beats the cost.
- With a quadratic risk penalty in place of the position cap, the same threshold becomes the half-width of the optimal no-trade band.

## Signal construction
Not a signal; it turns a forecast into a position under costs. Inputs: the bot's forecast `p_t` of the next-interval return in price units, per-unit cost `Gamma` (half-spread plus fee, in the same units), and the forecast's fitted AR(1) parameters `eps` and `beta`. Compute `eta = Gamma * eps^(3/2) / beta`, pick the regime, set `q*`, and act only when `|p_t| > q*` against the current position. Refit `eps` and `beta` on a rolling window; recompute `Gamma` whenever the fee tier or spread changes.

## Relevance to SOL perpetuals at minutes to hours
This is the closest theoretical match to the bot's cost structure: small size, linear costs, a leverage cap set by the venue. Two consequences. First, the band widens only with the cube root of cost in the intermediate regime, so moving from a 2 bp maker fee to a 12 bp taker fee widens the threshold by a factor of about 1.8 (the cube root of 6, my arithmetic), not 6, while the cost per flip rises sixfold. Second, slower predictors (small `eps`) justify acting on smaller instantaneous forecasts. The bang-bang shape follows from the position cap; with a risk penalty the position would be graded inside a band.

## Caveats
One asset, one predictor, known and stationary dynamics, linear relation between predictor and return. No impact, no fill uncertainty, no distinction between maker and taker cost. The Ornstein-Uhlenbeck description is stated to be consistent only for weak predictability. Parameter error in `eps` and `beta` moves the threshold, and the paper does not study estimation risk. Authors work at a trading firm; no live results are shown.
