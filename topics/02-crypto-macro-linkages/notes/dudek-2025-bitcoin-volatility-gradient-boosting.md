---
title: "Multivariate Forecasting of Bitcoin Volatility with Gradient Boosting: Deterministic, Probabilistic, and Feature Importance Perspectives"
authors: "Dudek, Grzegorz; Kasprzyk, Mateusz; Pelka, Pawel"
year: 2025
venue: "arXiv 2511.20105"
url: "https://arxiv.org/pdf/2511.20105"
pdf: "sources/02-crypto-macro-linkages/dudek-2025-bitcoin-volatility-gradient-boosting.pdf"
access: "full-text"
source_type: "working-paper"
evidence_grade: "B"
topic: "02-crypto-macro-linkages"
asset_class: "crypto"
horizon: "daily"
tags: "machine-learning, gradient-boosting, lightgbm, realized-volatility, feature-importance, macro-predictors, quantile-forecast"
---

## Key insight
A LightGBM model with 69 predictors forecasts next-day Bitcoin realized variance much better than HAR, LASSO or random forest benchmarks, but the macro-financial inputs contribute almost nothing. Feature importance is dominated by trading volume, lagged realized variance, Google search interest and market capitalization. This is machine-learning evidence, on the volatility side, that crypto-native variables outrank macro variables at daily frequency.

## Method
Target: daily realized variance of BTC/USD, one day ahead. Predictors in three groups: Bitcoin-specific (volume, transactions, block size, market capitalization, hash rate, unique addresses, Google Trends); financial markets (six equity indices including S&P 500 and Nasdaq Composite, EUR, JPY and CNY exchange rates, the broad dollar index, US 2-year and 10-year yields, oil, gold, natural gas, a commodity index); uncertainty (VIX and other implied volatility indices, newspaper and Twitter-based policy and market uncertainty indices, geopolitical risk). Models: LightGBM with and without "shock indicator" features, single and 32-model ensembles; quantile forecasts by pinball loss and by residual simulation. Benchmarks: HAR, Bayesian model averaging, LASSO, random forest. Feature importance by gain and by permutation, computed across 848 separately trained models, one per test day.

## Data and sample
Daily (Monday to Friday) from 2 August 2017 to 31 March 2023, 1,478 observations, with 848 test samples. Dataset from Fiszeder et al. (2025), published at doi.org/10.18150/SJHAHR (not opened).

## Reported results
- Out-of-sample R-squared: HAR 0.128, Bayesian model averaging 0.143, LASSO 0.283, random forest 0.150, LightGBM 0.674, LightGBM 32-model ensemble 0.688.
- Symmetric MAPE: HAR 47.3, LASSO 39.7, LightGBM about 38.2.
- Permutation importance starts near 35 percent for the top feature (change in volume) and falls below 1 percent by the ninth feature.
- Most influential predictors: trading volume, lagged realized variance, Google searches for Bitcoin, market capitalization. Somewhat less influential: hash rate, the CNY/USD rate, newspaper-based economic policy uncertainty.
- The authors' summary: macro-financial variables such as exchange rates, policy uncertainty indices and capital flows "exhibited negligible predictive power", and Bitcoin volatility is "largely decoupled from conventional macroeconomic drivers".
- Shock-indicator features add nothing measurable.
- Over the test period the importance of lagged realized variance rises and overtakes volume by 2023.

## Signal construction
A volatility forecast, not a direction signal. Minimal version suggested by the importance ranking: gradient-boosted regression of next-period log realized variance on lagged daily, weekly and monthly realized variance, change in traded volume, change in search interest and change in market capitalization, retrained on a rolling basis. Macro series can be omitted at little cost according to this paper. For a minutes-to-hours bot the same feature set can be rebuilt at hourly frequency to scale position size.

## Relevance to SOL perpetuals at minutes to hours
Supports a design choice: do not spend model capacity on daily macro levels (yields, dollar index, VIX) when forecasting crypto volatility; scheduled-announcement timing (see the Kyriazis and Karau notes) is a different and more useful macro input than macro levels. Tested on Bitcoin, daily, weekdays only; SOL and intraday horizons are untested. The weekday-only sample drops weekends, which matter for a 24/7 perpetual.

## Caveats
The large gap between LightGBM and the other benchmarks (R-squared 0.67 against 0.13 to 0.28) is unusually wide for volatility forecasting and deserves replication before being relied on; mean squared error is sensitive to a few spike days. Importance measures say which features the model split on, not that macro has no effect in announcement windows. Sample ends March 2023. Not peer reviewed in the version read.
