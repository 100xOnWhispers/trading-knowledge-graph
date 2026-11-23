---
title: "A Simple Approximate Long-Memory Model of Realized Volatility"
authors: "Corsi, Fulvio"
year: 2009
venue: "Journal of Financial Econometrics 7(2), 174-196"
url: "https://statmath.wu.ac.at/~hauser/LVs/FinEtricsQF/References/Corsi2009JFinEtrics_LMmodelRealizedVola.pdf"
pdf: "sources/14-volatility-forecasting/corsi-2009-har-long-memory-realized-volatility.pdf"
access: "full-text"
source_type: "peer-reviewed"
evidence_grade: "A"
topic: "14-volatility-forecasting"
asset_class: "multi"
horizon: "daily"
tags: "har-rv, realized-volatility, long-memory, volatility-cascade, ols, benchmark"
---

## Key insight
A regression of tomorrow's realized volatility on today's, the last week's average and the last month's average (HAR-RV) reproduces the long memory, fat tails and scaling of volatility without any fractional-integration machinery. It is estimated by OLS and forecasts as well as an ARFIMA model. It has become the standard benchmark that every machine-learning volatility paper in this folder is measured against.

## Method
The model is motivated by a cascade of traders with different horizons: short-term traders react to long-term volatility, but not the reverse. The estimating equation is

RV(d)_{t+1} = c + b_d RV(d)_t + b_w RV(w)_t + b_m RV(m)_t + error,

where RV(w) and RV(m) are averages of daily RV over the last 5 and 22 days. It is a restricted AR(22). Estimation is OLS with Newey-West standard errors. Benchmarks are AR(1), AR(3) and ARFIMA(5,d,0). Out-of-sample forecasts re-estimate daily on a rolling 1,000-day window, at horizons of 1 day, 1 week and 2 weeks, evaluated by RMSE, MAE and Mincer-Zarnowitz R-squared.

## Data and sample
Tick data for USD/CHF (December 1989 to December 2003, 3,599 days), S&P 500 futures (January 1990 to July 2007, 4,344 days) and 30-year US T-bond futures (January 1990 to October 2003, 3,391 days). Daily RV uses the two-scales estimator of Zhang, Ait-Sahalia and Mykland.

## Reported results
- In-sample coefficients for S&P 500: daily 0.372, weekly 0.343, monthly 0.224, all highly significant. For T-bonds the daily coefficient is small (0.039) and weekly and monthly dominate.
- Out-of-sample one-day R-squared: USD/CHF HAR 0.551, ARFIMA 0.546, AR(3) 0.530, AR(1) 0.497. S&P 500 HAR 0.696, ARFIMA 0.651, AR(1) 0.640.
- At two weeks the short-memory models collapse (USD/CHF AR(1) R-squared 0.038) while HAR (0.570) and ARFIMA (0.576) hold up.
- Residuals are visibly heteroskedastic, which the author flags as a reason to model volatility-of-volatility.

## Signal construction
Not a directional signal; it is the baseline volatility forecaster. For an intraday bot the natural adaptation, which is my suggestion and not tested in the paper, is to keep the three-scale idea but shrink the scales: forecast next-hour RV from RV over the last 1 hour, last 4 to 8 hours and last 24 hours to 7 days, each built from 1- or 5-minute returns, fitted by OLS (or on logs) on a rolling window and refitted daily. Inputs: one price series. Output: a variance forecast used for sizing and stop placement.

## Relevance to SOL perpetuals at minutes to hours
The cascade logic suits a 24/7 market with heterogeneous participants. What must be re-tested: the choice of scales at intraday horizons, the need to remove hour-of-day and funding-time periodicity first (see the Hansen note), and whether the log or square-root form handles SOL's jumps better than the level form.

## Caveats
Three traditional instruments ending in 2007. Horizons are one day and longer. The full-sample ARFIMA benchmark is given a small look-ahead advantage (d estimated on the whole sample), so the comparison is conservative for HAR. The open copy used here is the published article hosted on a university course page.
