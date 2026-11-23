---
title: "Modeling and Forecasting Realized Volatility"
authors: "Andersen, Torben G.; Bollerslev, Tim; Diebold, Francis X.; Labys, Paul"
year: 2003
venue: "Econometrica 71(2), 579-625"
url: "https://public.econ.duke.edu/~boller/Published_Papers/ecta_03.pdf"
pdf: "sources/14-volatility-forecasting/andersen-2003-modeling-forecasting-realized-volatility.pdf"
access: "full-text"
source_type: "peer-reviewed"
evidence_grade: "A"
topic: "14-volatility-forecasting"
asset_class: "fx"
horizon: "daily"
tags: "realized-volatility, quadratic-variation, long-memory, var, garch-benchmark, density-forecast"
---

## Key insight
Summing squared intraday returns gives a model-free, effectively observable measure of daily variance (realized volatility), justified by quadratic variation theory. Once volatility is treated as observed, simple time-series models fitted directly to log realized volatility forecast better than GARCH-family models fitted to daily returns. Returns divided by realized volatility are approximately Gaussian, which gives a practical route to density and quantile forecasts.

## Method
Realized variance for day t is the sum of squared intraday returns (here 30-minute returns, 48 per day). The authors document that log realized standard deviations are approximately normal and have long memory, with a common fractional integration parameter d of about 0.401. They fit a fractionally integrated Gaussian vector autoregression (VAR-RV) to the log realized volatilities and compare its one-day and ten-day forecasts with daily GARCH(1,1), RiskMetrics exponential smoothing, FIEGARCH on daily returns, and a deseasonalised intraday FIEGARCH. Evaluation uses Mincer-Zarnowitz style regressions of realized volatility on the forecasts, alone and in pairs.

## Data and sample
DM/USD and JPY/USD spot quotes from Olsen and Associates, 30-minute returns over the 24-hour FX day. In-sample: 1 December 1986 to 1 December 1996 (2,449 days). Out-of-sample: 2 December 1996 to 30 June 1999 (596 days).

## Reported results
- In-sample one-day-ahead R-squared for DM/USD: VAR-RV 0.355, daily GARCH 0.265, RiskMetrics 0.265, daily FIEGARCH 0.256, intraday FIEGARCH 0.324.
- Out-of-sample one-day-ahead R-squared for DM/USD: VAR-RV 0.249, daily GARCH 0.096, RiskMetrics 0.097, intraday FIEGARCH 0.266. For JPY/USD the gap is smaller (VAR-RV 0.329, daily GARCH 0.297).
- In encompassing regressions the VAR-RV coefficient is generally near one and the competitor's near zero; adding the competitor raises R-squared very little.
- A univariate AR-RV does almost as well as the VAR (DM/USD in-sample 0.351 versus 0.355).
- Returns standardized by realized volatility are approximately Gaussian, unlike raw returns.

## Signal construction
Not a directional signal. It is the measurement and forecasting foundation: compute RV_t as the sum of squared intraday log returns over a fixed window, take logs, and forecast with a long-memory autoregression (in practice HAR, see the Corsi note). The forecast feeds position sizing, stop distances and liquidation-distance checks. For quantiles, combine the volatility forecast with a normal distribution for standardized returns, then check that assumption on crypto, where jumps are heavier.

## Relevance to SOL perpetuals at minutes to hours
The principle transfers directly: SOL trades continuously, so a rolling RV built from 1- or 5-minute returns on a liquid venue (Binance or Bybit perp) is available at any moment. What needs re-testing: the sampling interval (30 minutes was chosen for 1990s FX quote noise), the daily horizon (the bot needs 15-minute to 4-hour forecasts), and the near-normality of standardized returns, which jump-heavy crypto may violate.

## Caveats
Two currency pairs, 1986 to 1999. Forecast comparisons are for daily and ten-day horizons only. The authors note that the standard errors in the evaluation regressions ignore parameter estimation error. Out-of-sample advantage over the best intraday GARCH variant is small or absent, so the gain is mostly from using intraday data, not from the specific VAR.
