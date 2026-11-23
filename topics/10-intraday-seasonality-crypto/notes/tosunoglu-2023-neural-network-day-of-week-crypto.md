---
title: "Artificial neural network analysis of the day of the week anomaly in cryptocurrencies"
authors: "Tosunoğlu, Nuray; Abacı, Hilal; Ateş, Gizem; Saygılı Akkaya, Neslihan (author list may be incomplete: the page truncated it)"
year: 2023
venue: "Financial Innovation, 9, article 88"
url: "https://link.springer.com/article/10.1186/s40854-023-00499-x"
pdf: "none"
access: "full-text"
source_type: "peer-reviewed"
evidence_grade: "C"
topic: "10-intraday-seasonality-crypto"
asset_class: "crypto"
horizon: "daily"
tags: "machine-learning, neural-network, day-of-week, diebold-mariano, out-of-sample-r2, bitcoin, ethereum, cardano"
---

## Key insight
A template for testing a calendar effect with a machine-learning model instead of dummy regressions: train one neural network on lagged returns and a second on lagged returns plus weekday dummies, and ask whether the second forecasts better out of sample. By this test, weekday information helps for Bitcoin but not for Ethereum or Cardano. The gain for Bitcoin is small and the paper has internal inconsistencies.

## Method
Three-layer feedforward networks (one hidden layer with sigmoid activation, linear output), trained by Levenberg-Marquardt backpropagation in MATLAB, with hidden sizes of 5 to 30 neurons tried. Model 1 has 7 inputs: daily log returns at lags 1 to 7. Model 2 has 13 inputs: the same lags plus six weekday dummies (Monday to Saturday, Sunday as the base). Forecasts are compared by MSE, RMSE, MAE, Theil's U1 and out-of-sample R-squared, and by the Diebold-Mariano test with the Harvey-Leybourne-Newbold small-sample correction.

## Data and sample
Daily closing prices from CoinMarketCap for BTC, ETH and ADA, 1 January 2018 to 31 May 2022. In-sample to 11 March 2020 (801 observations, split 70/15/15 into training, validation and test); out-of-sample 12 March 2020 to 31 May 2022 (811 observations). The split date was chosen after a large break in the return series.

## Reported results
- BTC: out-of-sample R-squared 0.0681 without weekday dummies and 0.0828 with them; MAE and Theil's U1 are lower with dummies; the Diebold-Mariano test rejects equal accuracy at the 1% level. The authors conclude a day-of-week anomaly exists.
- ETH: out-of-sample R-squared is negative for both models; no anomaly.
- ADA: out-of-sample R-squared 0.0297 without dummies and 0.0043 with them; equal accuracy is not rejected; no anomaly.
- Descriptive averages: the lowest average return is on Thursday for all three coins; the highest is on Monday for BTC, Sunday for ETH and Wednesday for ADA.

## Signal construction
The test design is the reusable part. For any clock feature (hour of day, weekday, minutes to funding): fit model A without it and model B with it on the same training window; compare out-of-sample forecast losses with a Diebold-Mariano test; keep the feature only if B wins by a significant margin on data after the training window. Apply the same procedure with boosted trees or any other learner, and repeat on rolling windows.

## Relevance to SOL perpetuals at minutes to hours
Daily bars are outside the bot's horizon and SOL is not in the sample. The paper matters as a caution and a method: a flexible learner found weekday information useful for only one of three coins, and adding weekday dummies made ADA forecasts worse. Clock features should enter a SOL model only if they pass an ablation test of this kind.

## Caveats
The paper contradicts itself on which weekday is best for BTC (descriptive section: Monday highest, Thursday lowest; conclusion: Thursday highest, Friday lowest), reports 1,611 observations against 801 + 811, and gives two dates for coin selection. An out-of-sample R-squared of about 7% for daily Bitcoin returns from lagged returns alone is implausibly high and may reflect the evaluation design. One split, no costs, no trading rule, and a split date chosen after inspecting the data. Only the first 100,000 characters of the open-access HTML were read; no PDF could be saved.
