---
title: "Forecasting Cryptocurrencies Financial Time Series"
authors: "Catania, Leopoldo; Grassi, Stefano; Ravazzolo, Francesco"
year: 2018
venue: "CAMP Working Paper 5/2018, BI Norwegian Business School (later version: International Journal of Forecasting 35(2), 2019, 485-501, as 'Forecasting cryptocurrencies under model and parameter instability')"
url: "https://econpapers.repec.org/RePEc:bny:wpaper:0063"
pdf: "sources/29-signal-combination-online-adaptation/catania-2018-forecasting-cryptocurrencies-dynamic-model-averaging.pdf"
access: "full-text"
source_type: "working-paper"
evidence_grade: "B"
topic: "29-signal-combination-online-adaptation"
asset_class: "crypto"
horizon: "daily"
tags: "dynamic-model-averaging, forgetting-factor, time-varying-parameters, bitcoin, ethereum, model-uncertainty"
---

## Key insight
The main crypto application of dynamic model averaging (DMA). Averaging over a very large set of time-varying-parameter regressions, with weights updated each day from predictive likelihoods, gives small but statistically significant point-forecast gains over an AR(1) for Bitcoin and Ethereum at one to two days, while "kitchen sink" regressions with all predictors are erratic and sometimes disastrous. Averaging beats selecting the single most probable model.

## Method
Each candidate model i is a dynamic linear model, y_t = F_t(i)' β_t(i) + ε_t, with random-walk coefficients β_t(i) = β_{t-1}(i) + η_t. The state variance is handled by a forgetting factor λ taken from the grid {0.91, 0.93, 0.95, 0.97, 0.99}. Candidates are all subsets of an intercept, three own lags and 16 lagged predictors, giving 2^19 = 524,288 regressor sets and 2,621,440 models with the forgetting grid. Model probabilities are updated recursively from each model's one-step predictive likelihood; DMA averages forecasts with these probabilities and dynamic model selection (DMS) uses the top model. Estimation uses the eDMA R package. Multivariate competitors are constant and time-varying-parameter vector autoregressions. Tests: Diebold-Mariano against AR(1) and the model confidence set.

## Data and sample
Daily percentage log returns of Bitcoin, Litecoin, Ripple and Ethereum, 8 August 2015 to 28 December 2017 (874 observations). Predictors: other coins' lags, daily high-low range, and macro-financial series (commodities, equity and bond indices, VIX). Horizons 1 to 7 days. The text gives the evaluation period as 1 January 2016 to 28 December 2017; a figure caption gives 6 June 2016 as the start.

## Reported results
MSE relative to AR(1) (below 1 is better), from the paper's Table 4:
- Bitcoin: DMA 0.97 at h=1 and h=2, DMA with own lags only 0.96 and 0.98; described as significant 4% and 2% reductions, and AR(1) falls outside the model confidence set. Gains vanish beyond two days (DMA 1.13 at h=7).
- Ethereum: DMA 0.97 at h=1; lags-only DMA 0.96 to 1.00 across horizons.
- Litecoin and Ripple: averaging does not help (Ripple DMA 1.20 at h=1).
- Kitchen-sink regression: 12.25 times the benchmark MSE for Bitcoin at h=2 and 12.72 for Ethereum at h=2.
- DMS is worse than DMA in almost every cell.
- Density forecasts (log score) favour selected time-varying multivariate models; univariate point gains do not carry over to density gains for Bitcoin and Ethereum.

## Signal construction
For a bot: maintain K small recursive regressions of next-bar return on subsets of signals, each with exponential forgetting λ. After each bar, update model weight π_i ∝ (π_i)^α × predictive density of the realised return (α slightly below 1 is the usual forgetting on model probabilities in the DMA literature; the value used in this paper was not confirmed), renormalise, and output the weighted forecast. The weight path also tells which signals currently matter.

## Relevance to SOL perpetuals at minutes to hours
The mechanism transfers directly because it is recursive and cheap per update when the model set is kept small. The evidence does not: it is daily, ends in 2017, has no SOL, and gains were 3 to 4% of MSE at one day for only two of four coins. Re-test at 5 to 60 minute bars with a curated model set of tens, not millions.

## Caveats
No equal-weight combination benchmark and no trading rule, so neither the 1/N comparison nor costs are addressed. Sample covers a single bull phase. With 2.6 million models the averaging is itself a heavy search. This note describes the 2018 working paper; of the published 2019 version only the abstract was read, which adds that both schemes "deliver sizable directional predictability", a claim not present in the working paper's abstract and not checked here.
