---
title: "Short-term bitcoin market prediction via machine learning"
authors: "Jaquart, Patrick; Dann, David; Weinhardt, Christof"
year: 2021
venue: "The Journal of Finance and Data Science 7, 45-66"
url: "https://publikationen.bibliothek.kit.edu/1000150665/149388567"
pdf: "sources/23-ml-feature-prediction/jaquart-2021-short-term-bitcoin-prediction-machine-learning.pdf"
access: "full-text"
source_type: "peer-reviewed"
evidence_grade: "A"
topic: "23-ml-feature-prediction"
asset_class: "crypto"
horizon: "minutes"
tags: "bitcoin, lstm, gru, gradient-boosting, random-forest, direction-classification, permutation-importance, transaction-costs, minute-bars"
---

## Key insight
The cleanest published test of machine learning on bitcoin at exactly the 1 to 60 minute horizon. Every model beats a coin flip, but only just: accuracy runs from 50.9% to 56.0%, rising with the horizon. Lagged bitcoin returns dominate feature importance. A long-short strategy on the most confident predictions looks profitable gross and loses money for every model once 30 basis points round-trip is charged.

## Method
Binary classification: does the return over the next m minutes (m = 1, 5, 15, 60) exceed the training-set median m-minute return. Six models: LSTM, GRU, feed-forward network, logistic regression, gradient-boosted classifier (XGBoost) and random forest, plus an equal-weight ensemble. Sequence models receive 15 series of the last 120 one-minute values. Tabular models receive 169 features: each of 14 inputs aggregated over twelve lookback buckets, (0,1], (1,2], (2,3], (3,4], (4,5], (5,10], (10,20], (20,40], (40,60], (60,80], (80,100], (100,120] minutes, plus the one-week bitcoin return. Inputs are bitcoin returns, returns of MSCI World, S&P 500, VIX, gold, WTI, EUR, CNY and JPY, bitcoin transaction count, mempool growth, tweet count and two tweet-sentiment sums. Chronological split: about 5 months training, 1 month validation, 3 months test. Feature importance is permutation importance averaged over 10 seeds. The trading rule goes long or short only when the predicted class probability exceeds the 99% quantile of training-set probabilities, and exits at the horizon.

## Data and sample
Bloomberg minute prices, Blockchain.com and Twitter, 4 March to 10 December 2019; usable sample 11 March to 10 December 2019. Weekends are excluded. The 1-minute test set has 94,834 observations.

## Reported results
- Test accuracy (1, 5, 15, 60 min): GRU 51.8, 52.5, 53.6, 55.7%; LSTM 51.9, 52.5, 53.2, 56.0%; feed-forward 50.9, 52.2, 52.1, 53.0%; logistic 51.1, 51.8, 52.0, 53.9%; boosting 51.1, 52.9, 53.7, 55.7%; random forest 51.2, 52.7, 53.5, 55.6%; ensemble 51.5, 52.6, 53.8, 55.8%.
- The chosen boosting depth was 1 (stumps); the random forest chose a 20% minimum leaf fraction. The best trees were very shallow.
- For the tree models the most important feature is always a bitcoin return bucket, and the relevant bucket moves back in time as the horizon grows: last minute for 1 min, 5 to 10 minutes back for 5 min, 10 to 20 back for 15 min, 20 to 40 back for 60 min. Transaction count, mempool growth and tweet count are the next most useful; cross-asset returns matter little.
- Gross strategy returns over the 3-month test range widely by model, from negative (logistic regression at 60 min: -87%) to +116% (LSTM at 60 min); buy-and-hold returned -29.6%. Higher accuracy did not reliably mean higher trading return.
- With 30 bps round-trip costs every model's return is negative. The strategies made roughly 400 to 2,800 trades in three months.

## Signal construction
Compute returns over the twelve lookback buckets above for the target and for a few leading instruments, standardise with training-set moments, fit a depth-1 gradient-boosted classifier or small GRU to the sign of the forward return relative to its median, refit periodically, and trade only on extreme predicted probabilities.

## Relevance to SOL perpetuals at minutes to hours
Directly on horizon. It sets a realistic prior for bar-feature models: 52 to 56% directional accuracy at 5 to 60 minutes, increasing with horizon, and an edge per trade smaller than taker costs. Replacing macro and Twitter inputs with perp-native inputs (funding, open interest, liquidations, cross-venue basis, BTC and ETH lead returns) is the obvious untested extension. The cost result argues for longer holds, maker execution, or stricter trade selection.

## Caveats
Nine months of 2019 data, one asset, one train-test split, weekends dropped. The 30 bps cost is high for a liquid perp; results at 4 to 10 bps were not reported. Trade selection used a single probability threshold with no sizing.
