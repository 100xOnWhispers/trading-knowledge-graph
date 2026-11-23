---
title: "A Reality Check for Data Snooping"
authors: "White, Halbert"
year: 2000
venue: "Econometrica"
url: "https://www.ssc.wisc.edu/~bhansen/718/White2000.pdf"
pdf: "sources/26-backtest-overfitting/white-2000-reality-check-data-snooping.pdf"
access: "full-text"
source_type: "peer-reviewed"
evidence_grade: "A"
topic: "26-backtest-overfitting"
asset_class: "equities"
horizon: "daily"
tags: "data-snooping, reality-check, bootstrap, multiple-testing, technical-rules"
---

## Key insight
When many models or trading rules are tried on one history, the best one's apparent significance is overstated. White provides a formal test of the null that the best of m candidates has no predictive superiority over a benchmark, with a p-value that accounts for the whole search and for dependence between candidates.

## Method
For each candidate k define a per-period performance differential f_k,t relative to the benchmark (for example negative squared forecast error difference, or trading return difference). The test statistic is the maximum over k of sqrt(n) times the mean of f_k. Its null distribution is obtained either by simulating the maximum of a multivariate normal with an estimated covariance (the "Monte Carlo Reality Check") or, more practically, by the stationary bootstrap of Politis and Romano applied jointly to all candidates' series so cross-candidate dependence is preserved (the "Bootstrap Reality Check"). The p-value is the share of bootstrap maxima (recentred) exceeding the observed maximum. The test can be updated recursively as each new candidate is added.

## Data and sample
Illustration: one-day-ahead forecasts of daily S&P 500 returns, sample March 29, 1988 to May 31, 1994, with 758 out-of-sample predictions from June 3, 1991. Candidates: 3,654 linear models, each using three of 29 technical indicators (lagged returns, momentum, local trend, relative strength, moving-average oscillators). Benchmark: constant-only model. Bootstrap with 500 resamples and smoothing parameter q = 0.5.

## Reported results
- Mean squared error criterion: the best model has a naive p-value of 0.1068 but a Reality Check p-value of 0.3674.
- Directional accuracy: the best model is correct 54.75% of the time against 50.79% for the benchmark; the naive p-value is 0.0036 but the Reality Check p-value is 0.2040. No superiority is established.
- The p-value drops when a new best model appears and otherwise creeps up as more models are tried; because the forecasts are highly correlated, the erosion is gradual, so trying many correlated models need not destroy significance.
- If the naive p-value is already large, the Reality Check need not be run, since it can only be larger.

## Signal construction
Not a signal. It is a significance test for a universe of rules. Inputs: the synchronized per-period excess performance of every rule in the search universe against a benchmark (flat, or buy-and-hold). Procedure: stationary bootstrap of the whole matrix, recentre, take the maximum per resample, compare with the observed maximum.

## Relevance to SOL perpetuals at minutes to hours
This is the standard tool for the question "is the best of my several thousand indicator-parameter combinations better than doing nothing?" It fits technical-rule and feature searches on intraday bars directly, and the 54.75% directional-accuracy example is the same size of edge often reported for crypto classifiers. For intraday crypto the block length of the bootstrap must cover volatility clustering and the diurnal cycle, and the benchmark should be net of the same costs.

## Caveats
The full universe must be specified, including rules tried and discarded; an understated universe makes the test too lenient. The statistic is not studentized and the null is the least favourable configuration, so including many poor rules lowers power (Hansen 2005 addresses this). It tests only the single best rule; it does not say which other rules are genuine. The empirical example is one index over six years and predates costs entirely.
