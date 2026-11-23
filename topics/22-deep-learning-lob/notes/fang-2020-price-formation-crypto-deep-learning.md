---
title: "Ascertaining price formation in cryptocurrency markets with Deep Learning"
authors: "Fang, Fan; Chung, Waichung; Ventre, Carmine; Basios, Michail; Kanthan, Leslie; Li, Lingbo; Wu, Fan"
year: 2020
venue: "arXiv:2003.00803v1"
url: "https://arxiv.org/abs/2003.00803"
pdf: "sources/22-deep-learning-lob/fang-2020-price-formation-crypto-deep-learning.pdf"
access: "full-text"
source_type: "working-paper"
evidence_grade: "C"
topic: "22-deep-learning-lob"
asset_class: "crypto"
horizon: "tick"
tags: "universal-model, lstm, coinbase, gdax, live-testing, accuracy-decay, walk-forward-retraining, autoencoder, non-stationarity"
---

## Key insight
The Sirignano and Cont test repeated on a crypto exchange gives a split verdict. Pooling currency pairs into one LSTM does beat pair-specific models, so the "universal" part holds. The "stationary" part does not: on live data the pooled model's accuracy decays to roughly chance over the live test window (the examples shown span less than a day), and only frequent retraining on recent data restores it.

## Method
A small LSTM (two LSTM layers, one dense layer, softmax) predicts whether the mid-price will be higher or lower at the next tick, from level-2 book and order features. Pair-specific models are compared with a model trained on all pairs, at several training-set sizes and with 1 to 40 time steps of history. A four-class variant splits moves at plus or minus 0.2% of price, taken from Coinbase Pro fees, to separate moves that could cover costs from those that could not. For live use the authors add an autoencoder (denoising and dimension reduction) and "walkthrough" retraining: after every 196 predictions the model is refitted on newly collected data; a second variant triggers retraining from a drawdown-style rule on accuracy.

## Data and sample
Live WebSocket data from GDAX (Coinbase): ticker, level-2 updates (top 50 bids and asks) and order flow for the listed pairs, recorded from 2 July 2018 17:22 UTC to 3 July 2018 23:32 UTC (about 30 hours; 61.9 million order records, 41.0 million level-2 records). Live tests on BTC-USD on 1 to 2 August and 8 to 9 August 2018.

## Reported results
- The universal model beats the mean of pair-specific models by 3.65% accuracy on average across training sizes; 4.25% after dropping four thinly traded pairs (BCH-EUR, BTC-GBP, ETH-EUR, BTC-EUR).
- More history did not help: accuracy was flat to slightly lower as time steps rose from 1 to 40, and one step was chosen.
- On live data the universal model's accuracy "slowly decays to almost random guessing" over the test period.
- An autoencoder slows the decay; predictions drift toward a down-move bias inherited from the training period.
- With retraining every 196 predictions, live BTC-USD accuracy starts below 50%, rises from 58% to 78% after the first retrains and settles near 76%.
- Most tick-to-tick price changes lie within plus or minus 0.25%, often less than transaction fees.

## Signal construction
P(next mid-price tick is up) from a pooled LSTM on current level-2 features, with the model refitted on a rolling buffer every few hundred predictions. The four-class version adds a filter: act only when the predicted move exceeds the fee threshold.

## Relevance to SOL perpetuals at minutes to hours
Two design lessons carry over. First, pool instruments and venues when training. Second, do not assume a model trained last month still works: build online or frequent retraining, and monitor live accuracy against a decay trigger. The fee-threshold classes are a simple way to tie labels to costs. The next-tick target itself is too short for our horizon.

## Caveats
About 30 hours of training data from one exchange in July 2018, so the "decay" may partly reflect an underfitted model rather than a changing market. The live figure of 76% to 78% is for next-tick direction with retraining on immediately preceding data, where short-run persistence in mid-price moves may account for much of the score; no baseline such as "repeat the last move" or queue imbalance is reported. The finding that history does not help contradicts Sirignano and Cont. No trading results. Several authors are affiliated with a commercial firm (Turing Intelligence Technology).
