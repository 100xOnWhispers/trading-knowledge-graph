---
title: "Microstructure and Market Dynamics in Crypto Markets"
authors: "Easley, David; O'Hara, Maureen; Yang, Songshan; Zhang, Zhibai"
year: 2024
venue: "Working paper, April 2024 (SSRN abstract 4814346)"
url: "https://stoye.economics.cornell.edu/docs/Easley_ssrn-4814346.pdf"
pdf: "sources/09-liquidity-price-impact/easley-2024-microstructure-dynamics-crypto-markets.pdf"
access: "full-text"
source_type: "working-paper"
evidence_grade: "B"
topic: "09-liquidity-price-impact"
asset_class: "crypto"
horizon: "hours"
tags: "machine-learning, random-forest, roll-measure, vpin, amihud, kyle-lambda, volatility-prediction, solana"
---

## Key insight
Five bar-based microstructure measures of liquidity and toxicity (Roll, Roll impact, Kyle lambda, Amihud, VPIN) predict changes in volatility and other return-distribution statistics about a day ahead for major cryptocurrencies, including SOL. A random forest finds that the Roll measure and VPIN carry most of the predictive power, with BTC and ETH measures helping to predict the other coins. Predictability is modest but similar to that found in futures, and it survived the 2022 "crypto winter".

## Method
One-minute bars. Each feature is computed over a lookback of W = 50 or 100 bars:
- Roll: 2 * sqrt(|cov(dP_t, dP_(t-1))|)
- Roll impact: Roll divided by dollar volume
- Amihud: mean of |r_i| / (p_i V_i)
- Kyle lambda: (p_t - p_(t-W)) / sum(b_i V_i), with b_i the sign of the bar's price change
- VPIN: mean of |V_sell - V_buy| / V, with buy volume assigned by bulk volume classification, V_buy = V * Z(dP / sigma_dP)

Labels are the sign of the change, over a look-ahead of h = 1,500 bars (roughly one day), in realized volatility, Jarque-Bera statistic, first-order return autocorrelation, absolute skewness and kurtosis. A random forest classifier is trained per coin on 25 features (five measures for each of five coins). Importance is measured by Mean Decreased Accuracy on a disjoint test set. Robustness: sub-period split and logistic regression.

## Data and sample
Binance public 1-minute candles for BTC, ETH, XRP, SOL and ADA, January 2021 to July 2023.

## Reported results
- Average out-of-sample accuracy across coins and labels is 0.53 to 0.54, with AUC in the same range. Excluding skewness the range is 0.52 to 0.58.
- The sign of the change in realized volatility is the most predictable label: 0.56 to 0.58.
- Skewness is not predictable (0.50).
- The Roll measure is the most important feature for every label, VPIN second and Roll impact third. In almost every case a coin's own Roll measure ranks first; BTC and ETH Roll and VPIN rank next for other coins.
- The authors describe the levels of the Roll measure and VPIN in crypto as "surprisingly high".
- The introduction quotes somewhat higher figures (AUC above 0.55 on average) than the results section; I report the results-section numbers.

## Signal construction
Every minute, for SOL and for BTC and ETH on the reference venue, compute the five features over 50 and 100 bars. Feed them to a tree ensemble that predicts whether realized volatility over the next block will be higher than now. Retrain on a rolling basis with purged, non-overlapping labels. Output is a volatility-regime probability, used to scale position size, stop distance and signal thresholds.

## Relevance to SOL perpetuals at minutes to hours
SOL is in the sample and the inputs are free candles, so this can be replicated exactly. It is evidence that liquidity conditions predict volatility, not direction: none of the labels is the sign of the return. The look-ahead is about a day, longer than the bot's horizon, so shorter look-aheads need testing. The paper does not say, in the parts read, whether the Binance candles are spot or futures; features would need to be recomputed on perp data. It also covers the machine-learning part of this topic: a simple non-linear model on five hand-built liquidity features, with importance scores that are interpretable.

## Caveats
Working paper, not peer-reviewed in this version. Accuracy of 0.53 to 0.58 on a binary label is statistically meaningful but small, and no trading strategy or cost analysis is given. Bulk volume classification from 1-minute bars is a rough proxy for signed flow. Labels built from overlapping windows need careful purging to avoid leakage. The authors state that they did not try to maximize accuracy.
