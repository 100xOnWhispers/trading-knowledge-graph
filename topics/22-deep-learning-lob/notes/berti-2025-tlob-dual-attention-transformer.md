---
title: "TLOB: A Novel Transformer Model with Dual Attention for Price Trend Prediction with Limit Order Book Data"
authors: "Berti, Leonardo; Kasneci, Gjergji"
year: 2025
venue: "arXiv:2502.15757v3"
url: "https://arxiv.org/abs/2502.15757"
pdf: "sources/22-deep-learning-lob/berti-2025-tlob-dual-attention-transformer.pdf"
access: "full-text"
source_type: "working-paper"
evidence_grade: "C"
topic: "22-deep-learning-lob"
asset_class: "multi"
horizon: "seconds"
tags: "transformer, dual-attention, mlp, tlob, mlplob, labelling, spread-threshold, bitcoin-perpetual, binance, fi-2010, predictability-decay"
---

## Key insight
A plain MLP adapted to LOB input (MLPLOB) matches or beats earlier specialised architectures, which questions the value of architectural complexity; a transformer with separate attention over time and over features (TLOB) adds a few F1 points at longer horizons, including on Binance BTC perpetual data. When the label threshold is set to the average spread instead of being tuned for class balance, scores fall sharply, and the authors conclude the models are not ready for live trading.

## Method
Both models read the last T snapshots of a 10-level book. MLPLOB is a stack of fully connected layers mixing along the feature and time axes. TLOB alternates temporal self-attention and spatial (feature) self-attention, four layers each. Baselines include DeepLOB and BiN-CTABL.

Labelling: the paper argues earlier smoothed labels tie the smoothing window to the horizon and proposes separating them. With w_minus the mean of the k+1 mid-prices ending at t and w_plus the mean of the k+1 mid-prices ending at t+h, l(t,h,k) = (w_plus - w_minus) / w_minus; up if l > theta, down if l < -theta. For the equity and BTC data theta is set to the mean percentage change, to balance the classes. In one experiment theta is the average spread as a fraction of the mid-price.

## Data and sample
FI-2010. Tesla and Intel from LOBSTER, 2 to 30 January 2015 (about 24 million samples; 17 days train, 1 validate, 2 test). Binance BTCUSDT perpetual from a Kaggle dataset, 9 to 20 January 2023, 3,730,870 rows; nine days train, one validate, one test. The paper gives the sampling interval as 250 ms in the text and 100 ms in a footnote, and the horizons 10, 20, 50, 100 as 1 s, 2.5 s, 5 s and 10 s.

## Reported results
- FI-2010: TLOB exceeds the previous best by 3.7 F1 points on average; Tesla +1.3, Intel +7.7 (abstract).
- BTC F1 at h = 10 / 20 / 50 / 100: DeepLOB 68.07 / 57.87 / 45.13 / 37.43; BiN-CTABL 73.4 / 61.34 / 47.05 / 40.59; MLPLOB 74.6 / 61.02 / 42.74 / 36.97; TLOB 74.7 / 61.74 / 48.54 / 41.49.
- F1 falls steeply with horizon for every model: from about 75 at roughly one second to about 41 at roughly ten seconds on BTC.
- Intel at horizon 50: F1 66.87 on one day in 2012 versus 60.19 in 2015, read as predictability declining over time.
- Tesla with theta equal to the average spread: F1 41.39 (h = 50), 36.48 (h = 100), 30.82 (h = 200). For Intel the same rule would label 99.99% of observations stationary.

## Signal construction
Compute from a lead-venue book: 10-level snapshots at a fixed interval, a window of T snapshots, and the model's up, stationary and down probabilities at several horizons. For training labels use the decoupled smoothing above with theta set to at least the round-trip cost (spread plus fees), not to the class-balancing value.

## Relevance to SOL perpetuals at minutes to hours
This is one of the few DeepLOB-family papers with perpetual futures data, and the result is informative: on BTC perps the edge over a three-class baseline is large at one second and mostly gone by ten. That supports treating LOB networks as execution-timing tools, not as the source of a minutes-to-hours view. The spread-threshold experiment is the right acceptance test for any SOL model: label only moves that clear costs and see whether anything is left. The MLP result argues for starting simple.

## Caveats
BTC test set is a single day; equities test sets are two days. No backtest, no fees. The sampling interval for the BTC data is stated inconsistently. The 2012 versus 2015 comparison rests on one public sample day. A third-party Kaggle dataset was used and its provenance was not verified here.
