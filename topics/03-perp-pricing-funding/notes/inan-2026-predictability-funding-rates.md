---
title: "Predictability of funding rates"
authors: "Inan, Emre"
year: 2026
venue: "International Review of Financial Analysis 119, article 105464 (citation as given by the secondary source)"
url: "https://www.securities.io/bitcoin-funding-rates-forecasting-trading-costs/"
pdf: "none"
access: "secondary"
source_type: "peer-reviewed"
evidence_grade: "B"
topic: "03-perp-pricing-funding"
asset_class: "crypto"
horizon: "hours"
tags: "funding-rate-forecasting, double-autoregressive, cross-exchange, binance, bybit, transaction-costs"
---

## Key insight
The next 8-hour funding rate on BTC/USDT perps is partly forecastable with a time-series model that captures persistence and changing volatility. The forecast improves a cross-exchange funding trade only once fees are counted, because its value lies in trading less often, not in a higher gross return. This note is based on a news article describing the paper; the paper itself was not opened.

## Method
As described by the secondary source: double autoregressive (DAR) models, in which both the conditional mean and the conditional variance depend on lagged funding, are compared with a no-change benchmark (next rate equals the latest rate). Forecasts drive a strategy that shorts the perp on the exchange with the higher expected funding and buys it on the other, with 100 million dollars at 5x leverage. Estimation variants and test statistics were not described in detail.

## Data and sample
BTC/USDT perpetual funding rates on Binance and Bybit, one observation per 8 hours, 11 January 2024 to 17 March 2025. Out-of-sample period: the last 384 observations, starting 10 November 2024.

## Reported results
All figures are as reported by the secondary source:
- Directional accuracy between 48.70% and 60.16% on Binance and between 49.48% and 62.5% on Bybit, depending on estimation method.
- Raw forecast errors do not consistently favour DAR over no-change; the stronger statistical conclusions appear only after adjusting for parameter-estimation noise.
- Predictability varies over time, more so on Bybit.
- Strategy with modelled fees (0.0090% on Binance, zero on Bybit): DAR 6.258% annualised with 8 trades against 4.258% with 15 trades for the benchmark.
- Strategy with no fees: DAR 10.122% with 59 trades against 16.652% with 78 trades for the benchmark, so the naive benchmark wins gross.

## Signal construction
Inputs: the venue's 8-hour funding history. Fit `F(t) = c + sum_j a_j * F(t-j) + e(t) * sqrt(w + sum_j b_j * F(t-j)^2)` (the generic DAR form; the paper's lag orders were not seen), re-estimate on a rolling window, and forecast one step ahead. Compare against the no-change forecast and against the exchange's own running predicted rate before trusting it. Update at each funding timestamp.

## Relevance to SOL perpetuals at minutes to hours
Expected funding over the next window is a known-unknown cost in the bot's expected-return calculation, and this is the one peer-reviewed forecasting study found. The practical message is modest: persistence is the main forecastable feature, a random-walk forecast is hard to beat, and a model earns its keep by avoiding marginal trades. BTC results on two deep venues will not carry over unchanged to SOL or to a new venue with low leverage; [Le](le-2026-funding-aware-market-making-perp-dex.md) finds SOL funding mean-reverts faster than BTC on Hyperliquid.

## Caveats
Secondary access only; every number should be checked against the article (DOI 10.1016/j.irfa.2026.105464 as given by the source). The backtest covers about four months, uses a fee assumption of zero on one venue, and is period-by-period, so intra-period margin calls are ignored. The grade would be revisited after reading the paper.
