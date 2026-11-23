---
title: "Determining Optimal Trading Rules without Backtesting"
authors: "Carr, Peter P.; Lopez de Prado, Marcos"
year: 2014
venue: "arXiv preprint 1408.1159 (working paper, version of August 2014)"
url: "https://arxiv.org/pdf/1408.1159"
pdf: "sources/27-execution-risk-management/carr-2014-optimal-trading-rules-without-backtesting.pdf"
access: "full-text"
source_type: "working-paper"
evidence_grade: "C"
topic: "27-execution-risk-management"
asset_class: "multi"
horizon: "n/a"
tags: "stop-loss, take-profit, ornstein-uhlenbeck, backtest-overfitting, exit-rules, monte-carlo"
---

## Key insight
Profit-taking and stop-loss thresholds should be derived from an estimated price process by simulation, not tuned on a historical backtest. Under a discrete Ornstein-Uhlenbeck process the best pair of thresholds depends on the half-life of mean reversion and on the expected profit of the position; when the process is close to a random walk there is no optimal pair at all, and anything a backtest "finds" is noise.

## Method
Prices of an open position follow `P_t = (1 - phi) * E[P] + phi * P_(t-1) + sigma * eps_t`, with half-life `-log(2)/log(phi)`. Procedure:
1. Estimate `phi` and `sigma` by regression on the position's price series.
2. Build a 21 by 21 mesh of (profit-taking, stop-loss) pairs, in multiples of `sigma`.
3. Simulate many paths (the paper suggests 100,000) from the fitted process, with a maximum holding period (for example 100 observations) after which the position is closed.
4. Apply each threshold pair to every path and compute the Sharpe ratio of the outcomes.
5. Pick the best pair; or, given a profit target from the strategy, read off the best stop; or, given a mandated maximum stop, read off the best profit target.

Cases are grouped by long-run equilibrium (zero, positive, negative expected profit) and half-life (5, 10, 25, 50, 100 observations).

## Data and sample
Simulated paths only. No market data.

## Reported results
Sharpe ratios are per trade, not annualised.
- Zero expected profit, half-life 5: best region is small profit-taking with large stop-losses, Sharpe around 3.2; the worst rule is a tight stop with a wide profit target; symmetric thresholds are close to neutral. The authors compare this with market-maker behaviour.
- As half-life grows the best region spreads and Sharpe falls; near a random walk no region stands out.
- Positive expected profit, shortest half-life: profit-taking centred around 6 with stops anywhere from 4 to 10, Sharpe around 12. With longer half-lives the reported optimum Sharpe falls to about 9, then 2.7, 0.8 and 0.32.
- Negative expected profit: mirror image, Sharpe around -12 at worst.
- No closed form is derived; the authors conjecture that a unique optimum exists for a discrete Ornstein-Uhlenbeck process.

## Signal construction
Not a signal; an exit-rule calibration. For each trade type, fit `phi` and `sigma` to the path of unrealised profit and loss after entry (pooled over past trades), set the forecast `E[P]` from the signal, simulate, and store the optimal (take-profit, stop-loss, maximum holding time) per bucket of half-life and forecast size. Refit on a schedule. Subtract round-trip costs from each simulated exit, which the paper does not do.

## Relevance to SOL perpetuals at minutes to hours
Useful as a discipline: three exit parameters per strategy are easy to overfit on five months of Kalshi data, and this replaces a search over history with a two-parameter process fit. The qualitative result also matters. For a mean-reverting edge, tight stops are the worst choice; a wide stop with a time limit is better. For a position with positive drift and fast reversion to target, the stop's exact level barely matters over a wide range. If the bot's post-entry paths look like a random walk around the forecast, the honest conclusion is to exit on time or on signal change, not on price thresholds.

## Caveats
Entirely simulation under one assumed process; real intraday paths have jumps, volatility clustering and liquidation-driven tails, which are what stops exist for. No costs, no gap risk through the stop, no fill uncertainty on the take-profit limit. Marked by its authors as a working paper not to be cited without permission. Grade C because there is no empirical test.
