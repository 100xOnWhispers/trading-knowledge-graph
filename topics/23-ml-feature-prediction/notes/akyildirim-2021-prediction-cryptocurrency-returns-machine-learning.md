---
title: "Prediction of cryptocurrency returns using machine learning"
authors: "Akyildirim, Erdinc; Goncu, Ahmet; Sensoy, Ahmet"
year: 2021
venue: "Annals of Operations Research 297, 3-36"
url: "https://repository.bilkent.edu.tr/bitstreams/a209e6d2-ab87-4de6-9295-09e994d36ccc/download"
pdf: "sources/23-ml-feature-prediction/akyildirim-2021-prediction-cryptocurrency-returns-machine-learning.pdf"
access: "full-text"
source_type: "peer-reviewed"
evidence_grade: "B"
topic: "23-ml-feature-prediction"
asset_class: "crypto"
horizon: "minutes"
tags: "svm, logistic-regression, random-forest, neural-network, technical-indicators, direction-classification, intraday, bitfinex"
---

## Key insight
Four standard classifiers fed with lagged returns and technical indicators predict the sign of the next bar's return for twelve liquid coins at 15-minute, 30-minute, 60-minute and daily frequency with average out-of-sample accuracy above 50% in almost every case, while ARIMA sits at 50%. The paper is the usual citation for "crypto direction is predictable intraday", but it reports accuracy only: no trading strategy and no costs.

## Method
Target: +1 if the next bar closes above its open, otherwise -1. Features are transformations of past OHLC and volume: the last five lagged log returns, exponential and weighted moving averages of the close, RSI at 9 and 14 periods with buy and sell flags at 20% and 80%, MACD, a momentum indicator, an Aroon stochastic oscillator and related indicators. Models are logistic regression, support vector machine, a multi-layer neural network and random forest in scikit-learn, with no per-coin tuning. Splits are chronological: 80/20 for daily data, 90/10 for intraday data, plus three sub-period tests with 200, 400 and 600 out-of-sample observations. Benchmarks are a simulated random walk and AIC-selected ARIMA. Model differences are tested with t-tests, Wilcoxon signed-rank tests and the Model Confidence Set of Hansen, Lunde and Nason at 75% confidence with a 0/1 sign loss.

## Data and sample
Bitfinex USD pairs from Kaiko trade data. Twelve coins (BCH, BTC, DSH, EOS, ETC, ETH, IOT, LTC, OMG, XMR, XRP, ZEC) from 10 August 2017 to 23 June 2018. The daily sample has 318 days.

## Reported results
- The abstract states 55 to 65% average predictive accuracy at daily or minute frequencies, with the support vector machine "best and consistent".
- Logistic regression out-of-sample accuracy is "often around 55%" with little variation across time scales.
- Best single figures: 69% for ETH and XMR at the daily scale with the support vector machine.
- The neural network is slightly worse than logistic regression and the support vector machine; the authors attribute this to small samples.
- Random forest has the highest in-sample fit and "drastically lower" out-of-sample performance.
- ARIMA accuracy is "scattered around 0.5".
- The Model Confidence Set retains only logistic regression and random forest as best models, with random forest best in six of thirteen settings. This sits awkwardly with the abstract's claim for the support vector machine.
- The authors state trading strategies "are not considered in detail".

## Signal construction
On each closed bar compute the indicator set above, fit a regularised logistic regression (the most stable performer here) on a trailing window to the sign of the next bar's open-to-close return, and use the predicted probability as a directional score. Refit on a schedule.

## Relevance to SOL perpetuals at minutes to hours
The frequencies match. The useful takeaways are relative: simple linear classifiers were as good as or better than a neural network and far less overfit than a random forest on roughly 10 months of 15-minute bars, and accuracy was similar across 15, 30 and 60 minutes. The absolute accuracy levels should not be used as a planning number until re-tested on perp data with costs.

## Caveats
The sample covers the late-2017 boom and the 2018 collapse only. The daily out-of-sample block is about 64 days (20% of 318), so a 69% hit rate there is weak evidence. No costs, no strategy returns, no check that accuracy is concentrated in tradable moves. Open-to-close sign on thin 15-minute bars can pick up bid-ask bounce. The authors' claim that tuning "can easily achieve over 70%" is not tested.
