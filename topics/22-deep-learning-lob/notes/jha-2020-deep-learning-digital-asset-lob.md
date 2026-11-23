---
title: "Deep Learning for Digital Asset Limit Order Books"
authors: "Jha, Rakshit; De Paepe, Mattijs; Holt, Samuel; West, James; Ng, Shaun"
year: 2020
venue: "arXiv:2010.01241v1"
url: "https://arxiv.org/abs/2010.01241"
pdf: "sources/22-deep-learning-lob/jha-2020-deep-learning-digital-asset-lob.pdf"
access: "full-text"
source_type: "working-paper"
evidence_grade: "C"
topic: "22-deep-learning-lob"
asset_class: "crypto"
horizon: "seconds"
tags: "temporal-cnn, tcn, coinbase, btc-usd, walk-forward, book-depth, training-window, horizon-decay"
---

## Key insight
A temporal convolutional network on 100 ms Coinbase BTC-USD book snapshots classifies two-second mid-price movement with about 71% walk-forward accuracy on a class-balanced sample. More useful than the headline are three side findings: levels beyond the top ten add nothing, accuracy keeps improving as the training window grows to the full seven days available, and some predictability remains out to about a minute.

## Method
Input: price and size for the top levels of bid and ask at 100 ms intervals, standardised with the previous day's mean and standard deviation. Model: a temporal CNN with causal padding (kernel size 2, six dilation levels), trained with Adam (learning rate 0.01, batch 128, early stopping). Labels follow the smoothed scheme with k = 20 snapshots (two seconds): compare the mean of the previous 20 mid-prices with the mean of the next 20, threshold alpha = 0.002, three classes. Because most 100 ms intervals show no change, stable examples were randomly removed to balance classes (4,219,932 samples reduced to 1,681,407). Evaluation is walk-forward: train on 1 to 7 days, test on the following day.

## Data and sample
Coinbase BTC-USD spot, 50 levels each side, snapshots every 100 ms, nine consecutive days from 12 to 20 June 2019. Code and data are stated to be public (Globe-Research/deep-orderbook on GitHub).

## Reported results
- 71% walk-forward accuracy at a two-second horizon (abstract).
- With seven days of training and one day of testing: about 61% accuracy on down moves and 66% on up moves; the stable class is easier.
- Performance does not improve beyond 10 book levels and declines slightly with more, which the authors attribute to noise features.
- Accuracy increases with the number of training days and was still rising at seven days.
- Accuracy did not visibly wear off during the test day.
- Predictability of mid-price movement persists "often for up to a minute".
- The authors infer that the model mostly captures the persistence and strength of imbalance over roughly the top five levels, and that the book has a memory of at least ten seconds.

## Signal construction
Sample the top 10 levels each side at 100 ms; standardise with the prior day's statistics; feed the last few seconds (the receptive field of the TCN) to the network; output probabilities of up, stable and down for the next two seconds, or for longer horizons up to a minute. Retrain daily on a window of at least a week.

## Relevance to SOL perpetuals at minutes to hours
This is the closest early template for a crypto book model: fixed-interval snapshots, ten levels, walk-forward by day, multi-day training. The claim that predictability lasts up to a minute on a crypto venue, far longer in clock time than the sub-second horizons reported for Nasdaq, is the most relevant point for our horizon and the one most in need of re-testing on 2026 SOL perp data, where markets are faster and more competitive than Coinbase spot was in 2019.

## Caveats
Nine days of data from one venue in 2019. Random down-sampling of the stable class inflates accuracy relative to live conditions, where most intervals are stable; it is not stated whether the test day was also balanced. The label compares past and future averages, so part of the target is known at prediction time (our reading). The 0.002 threshold was chosen by search on the same data. No costs, no trading simulation, no comparison with a linear imbalance baseline (the authors say they did not check that deep models beat simpler ones on crypto). Two authors are affiliated with Globe Research; the nature of that organisation was not confirmed.
