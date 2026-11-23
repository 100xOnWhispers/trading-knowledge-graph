---
title: "DeepLOB: Deep Convolutional Neural Networks for Limit Order Books"
authors: "Zhang, Zihao; Zohren, Stefan; Roberts, Stephen"
year: 2019
venue: "IEEE Transactions on Signal Processing 67(11); arXiv:1808.03668v6"
url: "https://arxiv.org/abs/1808.03668"
pdf: "sources/22-deep-learning-lob/zhang-2019-deeplob-cnn-lstm-limit-order-books.pdf"
access: "full-text"
source_type: "peer-reviewed"
evidence_grade: "B"
topic: "22-deep-learning-lob"
asset_class: "equities"
horizon: "seconds"
tags: "deeplob, cnn, lstm, inception, limit-order-book, mid-price-classification, fi-2010, transfer-learning, lime"
---

## Key insight
A CNN plus Inception module plus LSTM fed with the raw 10-level book (40 numbers per update, last 100 updates) classifies smoothed mid-price direction better than earlier models on FI-2010, and holds its accuracy for three months out of sample on London Stock Exchange stocks, including five stocks it never saw in training. It is the reference architecture that almost every later paper benchmarks against. Its profit evidence is a mid-to-mid simulation with no costs, so it shows predictability, not tradability.

## Method
Input X in R^(100x40): for each of the last 100 book updates, ask price, ask size, bid price, bid size at levels 1 to 10. Convolutions with (1x2) filters and stride (1x2) first combine price with size at each level, then bid with ask (the authors note this forms a learned micro-price, weight I = v_b/(v_a+v_b)), then a (1x10) filter merges all levels. An Inception module (parallel 1x1, 3x1, 5x1 convolutions and max-pooling, 32 filters) captures several time scales; a 64-unit LSTM replaces dense layers (about 60k parameters). Output is softmax over down, stationary, up.

Labels: l_t = (m_plus(t) - m_minus(t)) / m_minus(t), with m_minus and m_plus the means of the previous and next k mid-prices; up or down if |l_t| exceeds a threshold alpha. Inputs are z-scored using the previous five days' mean and standard deviation per instrument.

## Data and sample
FI-2010 (five Nasdaq Nordic stocks, ten days) and LSE data for Lloyds, Barclays, Tesco, BT and Vodafone, 3 January to 24 December 2017, 08:30 to 16:00, more than 134 million samples, mean time between events 0.192 seconds. First six months train, next three validate, last three test. Transfer test on HSBC, Glencore, Centrica, BP and ITV.

## Reported results
- FI-2010 setup 2 (seven days train, three test): F1 83.40% (k=10), 72.82% (k=20), 80.35% (k=50), against 77.63%, 66.93% and 78.44% for C(TABL).
- LSE, training stocks: accuracy 70.17% (k=20), 63.93% (k=50), 61.52% (k=100).
- LSE, unseen stocks: 68.62%, 63.44%, 61.46%.
- Forward pass 0.253 ms.
- Simulation (one share, enter five steps after the signal, hold until the opposite signal, flat overnight, mid-price fills, no fees): positive daily profits with significant t-statistics for all ten stocks. Accuracy is lower at longer horizons but cumulative profit is higher.
- LIME sensitivity plots show the model uses a broader part of the input than an earlier CNN.

## Signal construction
Maintain a rolling buffer of the last 100 top-10 book snapshots (event-sampled or fixed-interval), z-score each of the 40 columns with trailing multi-day statistics, run the network, and read the three class probabilities for horizons k of 20 to 100 updates. Use the probability gap (p_up minus p_down) as a short-horizon directional feature rather than a standalone trigger. Retrain on a rolling basis.

## Relevance to SOL perpetuals at minutes to hours
The architecture and labelling transfer directly to Binance or Bybit SOL books. The horizon does not: at 0.19 seconds per event, k=100 is under a minute, and in crypto books 100 updates can be a few seconds. For a minutes-to-hours bot this is at best an entry-timing input computed on a lead venue. The cross-instrument transfer result suggests pooling BTC, ETH and SOL for training is worth testing.

## Caveats
Profits assume mid-price fills and zero fees; the authors say this is not a standalone strategy. The smoothed label uses past prices in m_minus, which makes the target partly a function of information known at prediction time and probably inflates accuracy (our reading, not a claim of the paper). Later independent benchmarks (see prata-2023 and briola-2024 notes) found much lower scores on recent Nasdaq data. Grade B rather than A for that reason.
