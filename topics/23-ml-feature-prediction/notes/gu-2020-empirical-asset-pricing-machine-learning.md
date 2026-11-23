---
title: "Empirical Asset Pricing via Machine Learning"
authors: "Gu, Shihao; Kelly, Bryan; Xiu, Dacheng"
year: 2020
venue: "Review of Financial Studies 33(5), 2223-2273 (NBER Working Paper 25398, September 2019 revision, is the copy read)"
url: "https://www.nber.org/system/files/working_papers/w25398/w25398.pdf"
pdf: "sources/23-ml-feature-prediction/gu-2020-empirical-asset-pricing-machine-learning.pdf"
access: "full-text"
source_type: "peer-reviewed"
evidence_grade: "A"
topic: "23-ml-feature-prediction"
asset_class: "equities"
horizon: "multi-day"
tags: "machine-learning, gradient-boosting, random-forest, neural-network, elastic-net, feature-importance, out-of-sample-r2, benchmark-study"
---

## Key insight
The reference comparison of machine-learning methods for return prediction. Trees and shallow neural networks beat linear models because they capture interactions between predictors, yet the achievable out-of-sample R2 is tiny (well under 1% per month per stock). All methods agree on the same small set of dominant predictors: price trend, liquidity and volatility. Shallow models beat deep ones because the signal-to-noise ratio is very low.

## Method
Thirteen models are fitted to the same panel: OLS, OLS on three characteristics (the benchmark), elastic net, principal components regression, partial least squares, generalized linear model with splines, random forest, gradient-boosted regression trees, and feed-forward networks with one to five hidden layers (NN3 has 32, 16 and 8 neurons). Inputs are 94 stock characteristics interacted with macro variables plus industry dummies, giving 900+ predictors. The sample is split by time: 18 years training (1957 to 1974), 12 years validation (1975 to 1986), 30 years test (1987 to 2016). Models are refit once a year with an expanding training window and a rolling validation window. Performance is the pooled out-of-sample R2 measured against a forecast of zero, plus Sharpe ratios of decile long-short portfolios. Variable importance is the drop in R2 when a predictor is set to zero.

## Data and sample
Nearly 30,000 US stocks (NYSE, AMEX, NASDAQ), monthly returns, March 1957 to December 2016.

## Reported results
- Monthly stock-level out-of-sample R2: benchmark OLS-3 0.16%; OLS on all predictors deeply negative; elastic net 0.11%; PCR 0.26%; PLS 0.27%; boosted trees 0.34%; random forest 0.33%; NN1 0.33%; NN3 0.40% (the peak; four and five layers do not improve).
- Boosted trees and random forests select shallow trees (fewer than six leaves on average).
- The spline GLM, which has nonlinearity but no interactions, does not robustly beat the linear model; interactions are what matter.
- Bottom-up S&P 500 forecasts from trees and networks reach monthly R2 of 1.08% to 1.80%; timing the index on the network forecast gives Sharpe 0.77 against 0.51 for buy-and-hold.
- Long-short decile portfolio on network forecasts: Sharpe 1.35 value-weighted and 2.45 equal-weighted, against 0.61 and 0.83 for OLS-3.
- Top predictors in every model: short-term reversal, 12-month momentum, momentum change, industry momentum, maximum return; then turnover, dollar volume, illiquidity, spread; then return volatility and beta.
- The ranking of the important third of predictors is "remarkably stable" across the 30 recursive training samples.

## Signal construction
Not a signal. It is the template for a model bake-off: a fixed feature set, strict chronological train, validation and test blocks, periodic refitting, R2 against a zero forecast (not against the historical mean, which is too easy to beat), and a portfolio translation of the forecasts.

## Relevance to SOL perpetuals at minutes to hours
The design transfers; the numbers do not. The lessons to carry over: expect predictive R2 well below 1% and treat anything larger as a probable leak; prefer shallow trees and small networks; penalise or reduce dimension before adding features; and check that feature importance is stable across refits. The dominant feature families (recent returns, liquidity, volatility) are exactly what can be computed from perp bar data. The cross-sectional gain from pooling 30,000 stocks is not available for one instrument, though pooling across many perps partly restores it.

## Caveats
Monthly US equities; the headline Sharpe ratios are before trading costs in the sections I read, and the equal-weighted figures lean on small illiquid stocks. Later work (Avramov, Cheng and Metzker; not opened this session) argues the profits concentrate in hard-to-trade stocks. The paper is widely replicated in spirit, which supports the A grade for the method, not for transfer to crypto.
