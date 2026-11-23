---
title: "Intraday Market Return Predictability Culled from the Factor Zoo"
authors: "Aleti, Saketh; Bollerslev, Tim; Siggaard, Mathias"
year: 2025
venue: "Management Science 71(9), 7731-7751 (read as Chapter 4 of Aleti's 2024 Duke dissertation, Essays on High-Frequency Factors)"
url: "https://dukespace.lib.duke.edu/server/api/core/bitstreams/db48671f-3684-4569-ada1-4a4ffb8ed258/content"
pdf: "sources/11-intraday-seasonality-tradfi/aleti-2025-intraday-market-return-predictability-factor-zoo.pdf"
access: "full-text"
source_type: "peer-reviewed"
evidence_grade: "A"
topic: "11-intraday-seasonality-tradfi"
asset_class: "equities"
horizon: "minutes"
tags: "machine-learning, lasso, intraday-predictability, cross-asset-lead-lag, jump-filtering, transaction-costs, etf"
---

## Key insight
The aggregate US equity market's next 15-minute return is predictable out of sample from the lagged 15-minute returns of a large set of characteristic-sorted factor portfolios, selected with LASSO. The edge comes from a handful of liquidity- and turnover-related factors, which the authors read as slow absorption of news across stocks, and it is concentrated in periods of high uncertainty. A simple timing rule on liquid index ETFs remains profitable after transaction costs.

## Method
Predictive regressions of the 15-minute market return on lagged 15-minute returns of more than two hundred high-frequency long-short factors, estimated by LASSO with the penalty chosen on a contiguous training/validation split (expanding in-sample window, first 80% training, last 20% validation) and evaluated on later data. Large "jump" returns are detected in real time and removed from the regressands, and optionally modelled separately as regressors, on the argument that jumps are unpredictable and cause overfitting; an example day shows an AR(1) R-squared moving from 0.69% to 8.96% when one jump interval is dropped. The trading rule enters the market only when the forecast exceeds a cutoff based on the rolling 21-day standard deviation of forecast errors and exits only when the forecast turns negative, to limit turnover. SHAP values attribute performance to predictors.

## Data and sample
US equities, 15-minute intraday returns for the Fama-French market portfolio and the factor set, 1996 to 2020; trading tests on four index ETFs including SPY and IWM, with bid-ask-based cost adjustments. Read from the dissertation chapter; the journal version may differ.

## Reported results
- The intraday market return is close to flat on average (most of the premium is earned overnight) and nearly serially uncorrelated: first-order autocorrelation 3.56%, equivalent to an R-squared of 0.12%.
- Univariate predictors reach R-squared values up to 0.30%; most are below 0.05%.
- LASSO models deliver positive out-of-sample R-squared of the order of 0.1% per 15-minute interval (exact table entries were not reliably extracted), far above the theoretical no-arbitrage bounds the authors compute.
- SPY timing strategy: annualized intraday Sharpe ratio of 0.79 after transaction costs versus 0.09 for intraday buy-and-hold, and a six-factor alpha of 7.99% a year.
- Performance is strongest in high-uncertainty, high-volatility periods and is driven by a few liquidity and tail-risk factors.

## Signal construction
Feature vector at each bar: lagged returns of a broad cross-section of related portfolios (not the target's own lags alone). Fit a sparse linear model on a rolling or expanding window with a time-ordered validation split; exclude bars flagged as jumps from the target. Trade with hysteresis: enter when forecast > k x rolling forecast-error standard deviation, exit when the forecast changes sign.

## Relevance to SOL perpetuals at minutes to hours
The recipe transfers more than the result. For SOL the "factor zoo" analogue is the cross-section of other perps and sector baskets (large caps, Solana-ecosystem tokens, high-turnover versus low-turnover coins), plus equity-index futures; the lead-lag from liquid to less liquid assets is the same economic story. Three implementation details are worth copying: sparse regularized models before deep ones, jump filtering of targets, and a noise-scaled entry threshold with asymmetric exit. The 15-minute horizon matches the bot's range.

## Caveats
R-squared values are tiny, so profitability depends entirely on low costs; SPY's spread is a fraction of a basis point, far below a new perp venue's. The strategy is long-or-flat on an asset with positive drift. Equity factor portfolios have no ready-made crypto equivalent. Published 2025; no post-publication evidence. This is not a seasonality paper: time of day enters only through the restriction to active trading hours.
