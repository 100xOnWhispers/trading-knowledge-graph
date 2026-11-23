---
title: "Microstructure in the Machine Age"
authors: "Easley, David; Lopez de Prado, Marcos; O'Hara, Maureen; Zhang, Zhibai"
year: 2021
venue: "Review of Financial Studies 34(7), 3316-3363 (read: February 2019 NBER conference draft)"
url: "https://conference.nber.org/conf_papers/f117415.pdf"
pdf: "sources/08-trade-flow-toxicity/easley-2021-microstructure-machine-age.pdf"
access: "full-text"
source_type: "peer-reviewed"
evidence_grade: "A"
topic: "08-trade-flow-toxicity"
asset_class: "futures"
horizon: "multi-day"
tags: "machine-learning, random-forest, vpin, kyle-lambda, amihud, roll-measure, feature-importance"
---

## Key insight
A random forest fed with classic microstructure measures (Roll, Roll impact, Kyle lambda, Amihud, VPIN, plus volatility and VIX) predicts the sign of changes in spread, volatility, serial correlation, skewness, kurtosis and the Jarque-Bera statistic out of sample across 87 futures. Features that look most important in-sample are not the ones that predict out of sample. VPIN is the most important out-of-sample feature for five of the six targets. None of the targets is the direction of price.

## Method
Tick data are aggregated into dollar-volume bars sized to give roughly 50 bars per day. Each feature is computed over a rolling lookback window of W bars, with W from 25 to 2000. Labels are the signs of changes in six market statistics over a forward horizon described as one week. A random forest classifier is trained per contract. Importance is measured two ways: Mean Decreased Impurity (in-sample) and Mean Decreased Accuracy (out-of-sample, by shuffling one feature in the test fold). Accuracy is computed with 10-fold purged cross-validation.

## Data and sample
87 of the most liquid futures traded globally (equity index, currency, commodity, short rate, fixed income), tick data, 2 July 2012 to 2 October 2017.

## Reported results
- In-sample, Amihud, VIX and VPIN rank highest; out-of-sample, VPIN has the best performance.
- VPIN is the most important out-of-sample predictor for five targets; the Roll measure dominates for the sixth, the sign of the change in sequential correlation.
- For the bid-ask spread target, Amihud and VPIN lead in-sample while VPIN predominates out of sample.
- The follow-up crypto paper cites this study's average predictive accuracy as in the range 0.54 to 0.61.

## Signal construction
A risk-state classifier, not a direction signal. Inputs per instrument: dollar-volume bars. Features over rolling W bars: Roll = 2 * sqrt(|cov(dp_t, dp_{t-1})|); Kyle lambda = price change over the window divided by signed dollar volume over the window; Amihud = mean of |return| / dollar volume; VPIN = mean of |V_buy - V_sell| / V. Label: sign of the change in realized volatility (or spread) over the forward window. Model: random forest with purged cross-validation; rank features by shuffled-feature accuracy loss. Output feeds position sizing and execution urgency.

## Relevance to SOL perpetuals at minutes to hours
The transferable parts are methodological: use out-of-sample importance (MDA), not in-sample importance, to pick flow features; use purged cross-validation because rolling-window features overlap; and sample in dollar-volume bars so that bars carry comparable information across quiet and busy periods. The forecast horizon here is about a week and the targets are second-moment statistics, so the result does not say that VPIN or Kyle lambda predicts SOL direction at minutes to hours. The crypto replication is [easley-2024-microstructure-dynamics-crypto-markets](easley-2024-microstructure-dynamics-crypto-markets.md).

## Caveats
The VPIN here uses bulk volume classification on bars, which [andersen-2013-order-flow-toxicity-perfect-classification](andersen-2013-order-flow-toxicity-perfect-classification.md) argues is mechanically tied to volatility; a feature that proxies volatility will naturally rank high when the targets are changes in volatility-type statistics. The authors address this directly and argue that the weaker performance of VIX relative to VPIN "refutes the notion that VPIN is simply picking up volatility effects"; VIX is an equity implied volatility, though, not each contract's own realized volatility. No trading strategy or cost analysis is given. Three of the authors developed VPIN. The read version is the 2019 draft with four authors; a search listing for the journal version showed an additional author, which was not verified.
