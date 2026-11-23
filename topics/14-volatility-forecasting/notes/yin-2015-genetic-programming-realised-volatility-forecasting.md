---
title: "An Analysis of the Performance of Genetic Programming for Realised Volatility Forecasting"
authors: "Yin, Zheng; O'Sullivan, Conall; Brabazon, Anthony"
year: 2015
venue: "Preprint dated 26 November 2015, University College Dublin (journal publication not confirmed)"
url: "https://ncra.ucd.ie/papers/RV_JAISCR_v9.pdf"
pdf: "sources/14-volatility-forecasting/yin-2015-genetic-programming-realised-volatility-forecasting.pdf"
access: "full-text"
source_type: "working-paper"
evidence_grade: "C"
topic: "14-volatility-forecasting"
asset_class: "futures"
horizon: "daily"
tags: "genetic-programming, evolutionary-algorithms, symbolic-regression, realized-volatility, har-benchmark, microstructure-features"
---

## Key insight
Genetic programming (GP), an evolutionary search over formula trees, can evolve one-day-ahead realized volatility forecasters that beat HAR, GARCH and stepwise linear regression out of sample when it is given microstructure variables (volume, trade count, spread, trade duration) and implied volatility in addition to lagged volatility. The benchmark forecasts still contain information the GP models miss, so a combination is likely better than either alone.

## Method
Target: next-day realized volatility of the index future. Candidate inputs: lagged RV at HAR-style horizons, trading volume, number of transactions, bid-ask spread, average trade duration, price range, and implied volatility from index options. GP evolves expression trees from these inputs and a set of arithmetic functions; fitness is mean squared error against realized RV in the training window. Each run uses a population of 50,000 over 50 generations with maximum tree depth limited to six to curb over-fitting; results are averaged across 10 runs. Benchmarks: HAR, GARCH and a stepwise regression on the same variables. Forecasts are made each day using all data up to the previous day. Tests: three Diebold-Mariano variants (an asymptotic test, the sign test and the Wilcoxon signed-rank test) and forecast-encompassing regressions.

## Data and sample
FTSE 100 index futures trades and quotes (about 26.3 million observations) and FTSE 100 index options (about 75.8 million records) for 2004. First six months for training; out-of-sample testing on the final six months (129 trading days).

## Reported results
- Out-of-sample MAE: HAR 0.014306, GARCH 0.014411, stepwise 0.014189, GP average 0.013060 (GP 8.7% below HAR).
- RMSE: HAR 0.017351, GARCH 0.017442, stepwise 0.017488, GP 0.016081 (7.3% below HAR).
- Mincer-Zarnowitz R-squared: HAR 30.4%, GARCH 29.7%, stepwise 25.4%, GP 39.3%.
- Diebold-Mariano tests reject equal accuracy for GP against each benchmark at 5%; the three benchmarks are not distinguishable from each other.
- GP forecasts are biased (slope 1.28 in the evaluation regression), and encompassing tests show the benchmarks hold information not captured by GP.

## Signal construction
Not a directional signal. A template for evolutionary feature discovery in a volatility model: define a terminal set (lagged RV at several scales, bipower variation, trade count, average trade size, spread, funding rate, open interest change, seasonal factor), a small function set, a depth cap, and an out-of-sample fitness such as QLIKE on a validation block. Keep evolved expressions only if they beat HAR on a later untouched block, and consider averaging the evolved forecast with HAR.

## Relevance to SOL perpetuals at minutes to hours
This is the only evolutionary-algorithm study on realized volatility that could be opened. It shows the approach is feasible and that microstructure inputs are where the gain comes from, consistent with the Barjašić and Pinto notes. It says nothing about crypto, intraday horizons or non-stationary markets, where evolved formulas are prone to over-fit.

## Caveats
One instrument, one calm year (2004), 129 test days. Benchmarks (HAR, GARCH) were not given the microstructure inputs, so part of GP's edge is the richer information set, not the search method. A population of 50,000 over 50 generations is a very large search relative to about 125 training days. No crypto-specific evolutionary volatility study was found with full text in this session.
