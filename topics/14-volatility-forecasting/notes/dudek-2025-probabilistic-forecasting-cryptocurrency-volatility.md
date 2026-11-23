---
title: "Probabilistic Forecasting Cryptocurrencies Volatility: From Point to Quantile Forecasts"
authors: "Dudek, Grzegorz; Orzeszko, Witold; Fiszeder, Piotr"
year: 2025
venue: "arXiv preprint 2508.15922"
url: "https://arxiv.org/pdf/2508.15922"
pdf: "sources/14-volatility-forecasting/dudek-2025-probabilistic-forecasting-cryptocurrency-volatility.pdf"
access: "full-text"
source_type: "working-paper"
evidence_grade: "B"
topic: "14-volatility-forecasting"
asset_class: "crypto"
horizon: "daily"
tags: "quantile-forecast, probabilistic-forecasting, stacking, har, machine-learning, bitcoin, realized-variance"
---

## Key insight
A point forecast of volatility is not enough for risk decisions; what is needed is the distribution of tomorrow's realized variance. The cheapest way to get it, adding the empirical distribution of a model's own past forecast errors to its point forecast, works best when applied to simple linear models on log realized variance. HAR, ARFIMA, ridge and support vector regressions on log RV give the best quantile forecasts for Bitcoin; GARCH, LASSO and LSTM give the worst.

## Method
Base point forecasters of daily realized variance: statistical (HAR, GARCH, ARFIMA) and machine-learning (LASSO, ridge, SVR, MLP, random forest, LSTM and others), each on raw and on log-transformed RV. Three ways of turning point forecasts into conditional quantiles:
- QRS (quantile estimation through residual simulation): add historical residuals of a base model to its current forecast and read off quantiles.
- Quantile regression on the base forecasts (probabilistic stacking), trained with the pinball loss.
- Quantile regression forest on the base forecasts.

Evaluation uses the continuous ranked probability score (CRPS), pinball loss, relative frequency (calibration) and the Winkler score, with pairwise Diebold-Mariano tests on CRPS at the 5% level.

## Data and sample
BTC/USD on Kraken, 2017 to 2021. Daily realized variance from 288 five-minute returns. Base models produce forecasts for 2019 to 2021; the probabilistic layers are trained on forecasts from 2019 onward and tested on 2021.

## Reported results
- The best-performing group is QRS applied to models on log RV: HAR, HAR with robust estimation, ARFIMA, ridge regression, both SVR variants and the median ensemble.
- GARCH-based models, LASSO and LSTM perform worst, being outperformed by most other models.
- QRS on log RV yields lower mean CRPS than QRS on raw RV for every base model except GARCH; forecasts on raw RV have greater variance because of outliers.
- The abstract reports that probabilistic stacking is robust and that QRS on linear log-RV models consistently outperforms more sophisticated alternatives.

## Signal construction
Not a directional signal; a risk input. Recipe: (1) fit HAR on log RV; (2) store the last N out-of-sample residuals e_i; (3) the forecast distribution of log RV is {forecast + e_i}; exponentiate and take quantiles. Use the 90th or 95th percentile of forecast variance, not the mean, when checking distance to liquidation or sizing a stop, and the median for volatility targeting.

## Relevance to SOL perpetuals at minutes to hours
The method is model-agnostic and trivially cheap, so it can sit on top of an intraday HAR for SOL. Sizing against an upper quantile of volatility is a principled way to be conservative when the forecaster has recently been wrong, which is when crypto regimes shift. Needs re-testing at hourly horizons and on SOL, where residuals are likely more skewed.

## Caveats
Bitcoin only, daily horizon, a single test year (2021). Residual-based quantiles assume past errors represent future uncertainty and are not conditional on the volatility level unless done on logs. Preprint from August 2025, not confirmed as peer-reviewed. Only the first pages and results discussion were read in detail; exact score values are not reproduced here.
