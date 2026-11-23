---
title: "AutoQuant: An Auditable Expert-System Framework for Execution-Constrained Auto-Tuning in Cryptocurrency Perpetual Futures"
authors: "Deng, Kaihong"
year: 2025
venue: "arXiv working paper 2512.22476 (v3, August 2026; marked as submitted to Expert Systems with Applications)"
url: "https://arxiv.org/pdf/2512.22476"
pdf: "sources/03-perp-pricing-funding/deng-2025-autoquant-execution-constrained-tuning.pdf"
access: "full-text"
source_type: "working-paper"
evidence_grade: "C"
topic: "03-perp-pricing-funding"
asset_class: "crypto"
horizon: "hours"
tags: "backtesting, funding-alignment, look-ahead, bayesian-optimization, genetic-algorithm, differential-evolution, sol"
---

## Key insight
In perp backtests, leaving out funding and slippage inflates results substantially, and parameter search (Bayesian or evolutionary) readily finds configurations that look good in training and are degenerate out of sample. The paper's contribution is a set of strict rules for when a funding rate is "visible" to the strategy and how it is charged, plus a two-stage screen across windows and cost scenarios.

## Method
A pre-specified rule-based signal family on 4-hour bars (a main family with entry thresholds and ATR stops, plus an auxiliary volatility-momentum family) is tuned with a tree-structured Parzen estimator (40 to 60 trials), then candidates are re-tested under strict rules: orders fill at `t+1`; the 8-hour funding series is carried forward as a step function onto the 4-hour grid with no backfill from future prints; funding accrues on notional each bar; cost grid of taker fee 3, 4 or 6 bp and funding multiplier 0.5, 1.0 or 1.5. A soft funding gate raises the long entry threshold when carry is expensive: `tau_long(t) = tau_base + kappa * max(|fr(t)| - theta_bias/10000, 0)`. The same budget is given to random search, differential evolution, a simple genetic algorithm and Gaussian-process Bayesian optimisation for comparison.

## Data and sample
BTC/USDT perps from Binance, Bybit and OKX records (one continuous venue stream per asset), 2019-09-08 to 2025-10-14; ETH from 2021-12-31 to 2025-11-24; SOL and AVAX from 2021-01-01 to 2025-12-16. Post-2024 hold-out for replications.

## Reported results
- Cost ladder for one fixed BTC configuration (Table 16): annual growth 2.726 with fees, slippage and funding; 4.308 with fees only; 5.225 with no costs. Sharpe 2.05, 2.51, 2.71. The author treats these as cost-sensitivity diagnostics, not profitability claims.
- Disabling the funding gates while still charging funding barely changed the tuned candidate (training monthly geometric return 0.218 against 0.219).
- With 60 evaluations each, every optimiser's best training candidate was degenerate on the 2021 to 2022 validation window (zero return, drawdown reported as 1.000). Post-2024 monthly returns ranged from -0.0151 (differential evolution) to 0.0400 (Gaussian-process), with the genetic algorithm at -0.0003.
- Two-stage screening did not raise returns; it more often selected lower-drawdown configurations.

## Signal construction
Not a signal. It is a checklist for the bot's research pipeline: timestamp every funding print, expose only prints at or before the decision bar, charge funding on the position held across the timestamp, stress fees and funding by multipliers, and never accept an optimiser's best training candidate without an untouched window.

## Relevance to SOL perpetuals at minutes to hours
SOL/USDT is one of the replication assets, though on 4-hour bars. The alignment rules matter more at minute horizons, where a position opened seconds before a funding timestamp pays the full 8-hour charge. The weak result for funding gates is one data point against using raw funding level as an entry filter for trend strategies.

## Caveats
Single-author preprint; small-account simulation with linear costs and no market impact; one signal family; tiny optimiser budgets, so the comparison between evolutionary and Bayesian search is not informative about which is better. Several headline tables report degenerate validation results.
