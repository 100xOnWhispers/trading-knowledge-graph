---
title: "Funding-Aware Optimal Market Making for Perpetual DEXs"
authors: "Le, Nam Anh"
year: 2026
venue: "arXiv working paper 2605.06405"
url: "https://arxiv.org/pdf/2605.06405"
pdf: "sources/03-perp-pricing-funding/le-2026-funding-aware-market-making-perp-dex.pdf"
access: "full-text"
source_type: "working-paper"
evidence_grade: "C"
topic: "03-perp-pricing-funding"
asset_class: "crypto"
horizon: "minutes"
tags: "funding-rate-dynamics, ornstein-uhlenbeck, jumps, hyperliquid, hourly-funding, sol, stochastic-control"
---

## Key insight
On Hyperliquid, where funding is paid hourly, the funding rate behaves like a fast mean-reverting process with half-lives of a few hours (shortest for SOL) plus occasional jumps, and it is essentially uncorrelated with price changes. Treating funding as a state variable in an inventory-control problem changes optimal quotes, but the measured benefit for SOL is weak once risk is matched.

## Method
A market maker's value function depends on inventory and a cash-scaled funding state `f = S * F`. The Hamilton-Jacobi-Bellman equation is solved by a monotone finite-difference scheme and quotes are recovered from inventory value differences. Funding is modelled as Gaussian Ornstein-Uhlenbeck with exact discrete transition `m = theta + (F - theta)*exp(-kappa*dt)`, `v = sigma^2/(2*kappa) * (1 - exp(-2*kappa*dt))`; half-life is `ln(2)/kappa`. A Bernoulli-normal jump mixture is fitted as a diagnostic. Backtests replay one-minute mid prices with simulated fills and hourly funding, without any price forecast, against Avellaneda-Stoikov baselines.

## Data and sample
Hyperliquid hourly funding and a one-minute L2 panel for ETH, BTC and SOL perps. Holdout window 26 November to 31 December 2025, 100 simulation seeds. The start date of the calibration sample was not confirmed from the text read.

## Reported results
Calibration (Table 1):

| Asset | OU half-life (hours) | Jump probability per hour | Funding-price correlation |
|---|---|---|---|
| ETH | 5.560 | 2.05% | 0.0026 |
| BTC | 4.071 | 1.24% | 0.0278 |
| SOL | 2.310 | 0.16% | -0.0151 |

- Adding jumps raises the training log-likelihood for every asset, most for SOL (gain 7,149.78 against 2,816.34 for ETH and 4,417.03 for BTC); standardised OU residuals are heavy-tailed.
- The funding-aware policy improves mean ETH and BTC performance and lowers inventory variability against Avellaneda-Stoikov. For SOL the gain is positive against the unscaled baseline but "not a Pareto improvement" against a risk-scaled one.

## Signal construction
Fit OU to the venue's funding series on a rolling window: regress `F(t+1)` on `F(t)`, `kappa = -ln(slope)/dt`, long-run mean `theta = intercept/(1 - slope)`. Forecast `E[F(t+h)] = theta + (F(t) - theta)*exp(-kappa*h)` and integrate over the intended holding period to get expected funding cost or income. Flag a jump when the innovation exceeds a multiple of the OU standard deviation and stop trusting the forecast for a few half-lives. Update hourly.

## Relevance to SOL perpetuals at minutes to hours
This is the only source in the folder with SOL-specific funding dynamics. A 2.3-hour half-life means an extreme hourly print on Hyperliquid carries little information about funding 8 hours ahead, so expected carry over a Kalshi 8-hour window should be shrunk hard toward the mean. The near-zero funding-price correlation is contemporaneous and hourly; it says nothing about whether funding leads returns.

## Caveats
Single-author preprint. Five-week holdout, simulated fills, one venue. Half-lives will vary by regime and the calibration window is short. The jump model is diagnostic only and not used in the policy. Results concern market making, not directional trading.
