---
title: "Temporal mixture ensemble for probabilistic forecasting of intraday volume in cryptocurrency exchange markets"
authors: "Antulov-Fantulin, Nino; Guo, Tian; Lillo, Fabrizio"
year: 2020
venue: "arXiv working paper 2005.09356 (v2, December 2020)"
url: "https://arxiv.org/pdf/2005.09356"
pdf: "sources/10-intraday-seasonality-crypto/antulov-fantulin-2020-temporal-mixture-intraday-volume.pdf"
access: "full-text"
source_type: "working-paper"
evidence_grade: "B"
topic: "10-intraday-seasonality-crypto"
asset_class: "crypto"
horizon: "minutes"
tags: "machine-learning, volume-forecasting, deseasonalization, mixture-ensemble, gradient-boosting, order-book, uncertainty"
---

## Key insight
A machine-learning treatment of intraday volume that shows how to handle seasonality inside a forecasting pipeline: divide volume by its time-of-day average (estimated on training data only), model the log of the ratio, and let a neural mixture ensemble combine order-book and trade features from two exchanges. Machine-learning models beat ARMA-GARCH on relative error by up to a factor of two outside the top volume quartile. The intraday pattern in 2018 Bitcoin volume was "small but significant".

## Method
Deseasonalisation: y_t = v_t / a_I(t), where a_I(t) is the mean volume at intraday slot I(t) across training days; the same a is reused for validation and test to avoid leakage. log y_t is modelled as Gaussian (volume log-normal). The Temporal Mixture Ensemble (TME) has one component per data source (trades and order book of each exchange); a latent variable selects the source at each step, each component outputs a mean and variance from time-lagged features, and an ensemble of stochastic-gradient-trained models adds epistemic uncertainty. Baselines: ARMA-GARCH, ARMAX-GARCH (same features), and a gradient boosting machine (GBM). Metrics: RMSE, MAE, normalised negative log-likelihood, prediction-interval width, and relative RMSE and MAPE by volume quartile. Horizons: 1, 5 and 10 minutes.

## Data and sample
BTC/USD on Bitfinex and Bitstamp, 31 May 2018 to 30 September 2018 (UTC). Per-minute features from trades (buy and sell volume, trade counts, imbalances) and from the limit order book (spread, bid and ask volume, imbalance, book slope at several depths).

## Reported results
- Intraday volume quantiles show no abrupt change at stock-exchange opening times, only a small but significant intraday pattern.
- Deseasonalised log-volume is approximately normal with a small negative skew.
- TME has the lowest RMSE in every market and horizon; GBM has the lowest MAE; TME always has the narrowest uncertainty intervals.
- Likelihood: TME is best on Bitfinex at 1 and 5 minutes; econometric models are slightly better on Bitstamp.
- Cross-market features help on Bitfinex in the ARMAX model, less so on Bitstamp, suggesting one-directional information relevance.
- By volume quartile, relative errors are smaller in the top quartile for all models; TME wins mostly in the top quartile and GBM in the lower three, where machine-learning models beat econometric ones by up to a factor of two.

## Signal construction
Not a directional signal; it forecasts volume, which sets expected liquidity, impact and volatility. Recipe: (1) build the slot average a_I for 1- or 5-minute slots on a trailing window that ends before the forecast time; (2) target = log(v_t / a_I(t)); (3) features = lagged trade and book variables from the target venue and the lead venue; (4) fit a boosted-tree model for point forecasts or a mixture network when an uncertainty band is needed; (5) forecast volume = exp(prediction) times a_I. A volume forecast far above the seasonal baseline is itself a regime feature for a directional model.

## Relevance to SOL perpetuals at minutes to hours
The multi-venue design matches the Kalshi problem: predict activity on a small venue from features of large ones. The deseasonalise-then-learn pattern applies to SOL volume, volatility and spread alike. Given later evidence of strong top-of-hour and funding-time bursts (Hansen note), the slot average should be at 1-minute resolution and should include minute-of-hour structure, which a 2018 sample would not show.

## Caveats
Four months of 2018 data, two spot exchanges, one asset. A single time-of-day average ignores day-of-week and regime shifts. The hyper-parameter selection procedure was not checked in detail for this note. The paper does not test whether better volume forecasts improve trading outcomes.
