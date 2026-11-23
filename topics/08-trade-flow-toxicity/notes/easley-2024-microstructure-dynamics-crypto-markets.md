---
title: "Microstructure and Market Dynamics in Crypto Markets"
authors: "Easley, David; O'Hara, Maureen; Yang, Songshan; Zhang, Zhibai"
year: 2024
venue: "Working paper, April 2024 (SSRN 4814346; read from a copy hosted at Cornell)"
url: "https://stoye.economics.cornell.edu/docs/Easley_ssrn-4814346.pdf"
pdf: "sources/08-trade-flow-toxicity/easley-2024-microstructure-dynamics-crypto-markets.pdf"
access: "full-text"
source_type: "working-paper"
evidence_grade: "B"
topic: "08-trade-flow-toxicity"
asset_class: "crypto"
horizon: "daily"
tags: "vpin, roll-measure, kyle-lambda, amihud, random-forest, machine-learning, sol, cross-asset"
---

## Key insight
Standard microstructure measures computed from one-minute Binance bars predict, out of sample, the sign of next-day changes in volatility, serial correlation, kurtosis and the Jarque-Bera statistic for BTC, ETH, SOL, XRP and ADA. The predictability comes almost entirely from the Roll measure and VPIN, and BTC and ETH values of those two measures help predict the other coins. Results were stable through the 2022 "crypto winter". The targets are properties of the return distribution, not the direction of price.

## Method
For each coin, one-minute bars give close price p_t, return r_t and dollar volume V_t. Five features are computed over rolling lookbacks of W = 50 or 100 bars: Roll = 2 * sqrt(|cov(dp_t, dp_{t-1})|); Roll impact = Roll divided by dollar volume; Amihud = mean of |r_i| / (p_i V_i); Kyle lambda = (p_t - p_{t-W}) / sum of b_i V_i with b_i the sign of the bar's price change; VPIN = mean of |V_sell - V_buy| / V_i with V_buy = V_i * Z(dp_i / sigma_dp), which is bulk volume classification. Labels are the signs of the change in each statistic between t and t + h with h = 1,500 bars, "roughly one day". A random forest of 100 bootstrapped trees uses 25 features (five measures for each of five coins). Importance is Mean Decreased Accuracy on held-out data. A logistic regression is the robustness check.

## Data and sample
Binance public one-minute candles (open, high, low, close, volume), BTC, ETH, ADA, SOL and XRP against USDT, January 2021 to July 2023.

## Reported results
- Mean VPIN is 0.45 to 0.47 across the five coins, against 0.22 to 0.23 that the authors cite for E-mini and crude oil futures.
- BTC has a substantially higher Roll measure than the other coins.
- Average out-of-sample accuracy across coins and labels is 0.53 to 0.54 depending on lookback; the introduction reports average AUC above 0.55 and AUC of 0.54 to 0.61 for individual targets, except skewness at 0.50 (no predictability).
- Own Roll and VPIN matter for most targets; Kyle lambda, Amihud and Roll impact have little or no importance.
- BTC and ETH Roll and VPIN have strong cross-predictive power for the other coins.
- No material change in results during crypto winter.

## Signal construction
A volatility and tail-risk regime classifier. Every minute, update the five features for SOL, BTC and ETH on W = 50 and 100 one-minute bars and feed them to a tree model that outputs the probability that realized volatility (or kurtosis) will be higher over the next day than over the last window. Use the output for sizing and stop distance. For a bot with trade feeds, replace bulk classification with true taker-buy volume and compare both versions.

## Relevance to SOL perpetuals at minutes to hours
SOL is in the sample, and the cross-asset finding supports computing flow-toxicity features on BTC and ETH as inputs to a SOL model. Three gaps remain: the paper uses Binance USDT candles without stating whether they are spot or perpetual; the horizon is one day, longer than the bot's; and nothing is said about direction. Re-test at 15 to 240 minute horizons on Binance SOL perp, with trailing realized volatility as a benchmark.

## Caveats
VPIN is computed by bulk classification of one-minute candles even though Binance candles carry taker-buy volume; by the argument in [andersen-2013-order-flow-toxicity-perfect-classification](andersen-2013-order-flow-toxicity-perfect-classification.md) this VPIN may largely be a volatility transform, and the high level (0.45) may reflect the method. No comparison with a simple lagged-volatility benchmark and no trading or cost test. The authors state they did not try to maximize accuracy. Working paper; two of the authors developed VPIN.
