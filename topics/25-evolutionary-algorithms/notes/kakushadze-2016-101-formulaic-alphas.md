---
title: "101 Formulaic Alphas"
authors: "Kakushadze, Zura"
year: 2016
venue: "arXiv preprint 1601.00991 (dated 9 December 2015)"
url: "https://arxiv.org/pdf/1601.00991"
pdf: "sources/25-evolutionary-algorithms/kakushadze-2016-101-formulaic-alphas.pdf"
access: "full-text"
source_type: "industry-research"
evidence_grade: "C"
topic: "25-evolutionary-algorithms"
asset_class: "equities"
horizon: "daily"
tags: "formulaic-alpha, operator-grammar, worldquant, price-volume, alpha-correlation, turnover"
---

## Key insight
The paper publishes 101 real trading signals from WorldQuant as explicit formulas over daily price and volume data. Its lasting effect on this topic is the vocabulary: almost every later alpha-mining system (genetic programming, reinforcement learning, LLM agents) searches the operator grammar defined in its appendix and benchmarks against "Alpha101". It gives aggregate statistics for the 101 signals but no per-signal performance.

## Method
Each alpha is an expression built from inputs (`open, close, high, low, volume, vwap, returns, adv{d}`, market cap, industry labels) and operators: cross-sectional `rank`, `scale`, industry neutralization; time-series `delay`, `delta`, `ts_min`, `ts_max`, `ts_rank`, `ts_argmax`, `correlation`, `covariance`, `stddev`, `sum`, `decay_linear`; and elementwise arithmetic, `sign`, `signedpower`, conditionals. Examples as printed:

- Alpha#101: `((close - open) / ((high - low) + .001))`, described as delay-1 momentum.
- Alpha#12: `(sign(delta(volume, 1)) * (-1 * delta(close, 1)))`.
- Alpha#42: `(rank((vwap - close)) / rank((vwap + close)))`, a delay-0 mean-reversion signal traded near the close.

"Delay-d" means the newest data used is d days older than the trading time. The paper then regresses log return on log volatility and log turnover across the 101 alphas and tests whether turnover explains pairwise correlations.

## Data and sample
Proprietary WorldQuant data on the 101 alphas, 4 January 2010 to 31 December 2013, 1,006 daily observations: Sharpe ratio, turnover, cents-per-share, and the sample covariance matrix of alpha returns. The instrument universe is not disclosed.

## Reported results
- Average holding period ranges from about 0.6 to 6.4 days.
- Average pairwise correlation of the alphas is 15.9% (median 14.3%).
- Alpha return scales with alpha volatility as R ~ V^X with X about 0.76.
- Returns show no statistically significant dependence on turnover, and turnover has poor explanatory power for alpha correlations.
- Four alphas (42, 48, 53, 54) are delay-0; the rest are delay-1.
- No individual Sharpe ratios, costs or capacity figures are given.

## Signal construction
The formulas are cross-sectional: `rank` and neutralization compare many stocks on one date. For a single instrument they must be rewritten, replacing cross-sectional `rank` with a rolling time-series rank or z-score. The time-series operators carry over unchanged to any bar size. As a search space for a SOL bot: inputs are OHLCV and VWAP bars plus perp-specific fields (funding, open interest, basis); operators are the list above; window lengths become bar counts.

## Relevance to SOL perpetuals at minutes to hours
Useful as a ready-made, widely tested operator set and as a seed population for evolutionary search, not as a source of working signals. The low pairwise correlation matters for the design goal: mine many weak, different signals and combine them, instead of hunting for one strong rule. Whether any of the 101 has predictive content on SOL intraday bars is an open test.

## Caveats
Daily US-style equity signals, selected by the author for simplicity, with no out-of-sample evidence and no costs. The formulas have been public since 2015 and are the standard benchmark, so any edge is likely gone. A 2026 benchmark (`wang-2026-factorbench-automated-factor-mining-benchmark.md`) still found the implementable subset competitive with mined factor pools on 2024 to 2025 equity data, which says more about the mined pools than about Alpha101.
