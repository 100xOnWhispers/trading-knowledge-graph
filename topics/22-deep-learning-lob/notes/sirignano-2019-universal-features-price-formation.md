---
title: "Universal features of price formation in financial markets: perspectives from Deep Learning"
authors: "Sirignano, Justin; Cont, Rama"
year: 2019
venue: "Quantitative Finance 19(9), 1449-1459 (journal reference as cited by Lucchese et al.; read as arXiv:1803.06917v1, 2018)"
url: "https://arxiv.org/abs/1803.06917"
pdf: "sources/22-deep-learning-lob/sirignano-2019-universal-features-price-formation.pdf"
access: "full-text"
source_type: "peer-reviewed"
evidence_grade: "A"
topic: "22-deep-learning-lob"
asset_class: "equities"
horizon: "tick"
tags: "universal-model, lstm, pooling, stationarity, path-dependence, next-price-move, nasdaq, lobster"
---

## Key insight
One LSTM trained on pooled order book data from about 500 Nasdaq stocks predicts the direction of the next mid-price move better than models fitted to each stock alone, works on stocks it never saw, and keeps its accuracy more than a year after training. The mapping from order book history to the next price move therefore looks common across assets and stable in time, which argues for pooling instruments and using long histories rather than short, asset-specific windows.

## Method
Three LSTM layers followed by a ReLU layer and a softmax; 50 units per layer in the baseline, 150 in the larger model. Input is the state of the order book at each mid-price change; the network state carries the history. Target is P(next mid-price change is up) versus down, a binary problem with no stationary class, sampled in price-change time. Benchmarks: a per-stock linear (VAR-style) model with a logistic output, per-stock LSTMs, and a feed-forward network using only the current book. Training of the universal model used asynchronous SGD over 25 GPU nodes; data were pooled without normalisation.

## Data and sample
All orders, trades and cancellations for about 1,000 Nasdaq stocks, 1 January 2014 to 31 March 2017, reconstructed with LOBSTER. Roughly 500 stocks for training, 500 held out. Typical test period June to August 2015, plus January to March 2017. Mean time between price changes 1.7 seconds.

## Reported results
- Per-stock deep models beat per-stock linear models by 5% to 10% accuracy for most stocks; the universal model beats per-stock linear models by around 10%.
- The universal model beats per-stock deep models, most strongly for stocks with little data.
- A universal model trained on stocks 1 to 464 beats the stock-specific models for all 25 held-out stocks (average +1.45%) and is within 0.15% of a universal model that saw them.
- Accuracy on 500 unseen stocks is stable 18 months after the training period ends.
- Training on 19 months beats training on only the last 1, 3 or 6 months for 100% of 50 stocks, by 7.2%, 3.7% and 1.6% on average.
- LSTM beats the feed-forward (Markovian) network; a 5,000-step history (about two hours) beats a 100-step history.
- Normalising by volatility, price or spread, or splitting by sector or tick size, did not help.
- Depth at levels 5 to 10 affects the predicted probability less than top-of-book depth but still matters.

## Signal construction
Not a signal by itself. It is a training-design result: pool instruments, keep long training histories, give the model long sequence context. The output a bot would use is P(next mid move up) from a pooled recurrent model, refreshed at each price change.

## Relevance to SOL perpetuals at minutes to hours
The pooling idea is directly testable: train one model on BTC, ETH, SOL and other perps across Binance, Bybit, OKX and Hyperliquid, then apply it to the thin Kalshi SOL book, where local data are too scarce for a venue-specific model. The path-dependence finding (two hours of history adds information for the next tick) is the closest link to our horizon. Stationarity needs re-testing: the crypto study in the fang-2020 note found live accuracy decaying toward chance within its test window unless the model was retrained.

## Caveats
Predicts only the next price change (about 1.7 seconds ahead), with no costs, spread or latency considered; a correct next-tick call is typically worth less than the spread. Accuracy levels are shown as histograms, not tables. US equities in 2014 to 2017 only. The released version read here is the 2018 preprint.
