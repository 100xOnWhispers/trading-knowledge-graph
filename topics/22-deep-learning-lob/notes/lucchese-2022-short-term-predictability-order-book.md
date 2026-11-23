---
title: "The Short-Term Predictability of Returns in Order Book Markets: a Deep Learning Perspective"
authors: "Lucchese, Lorenzo; Pakkanen, Mikko S.; Veraart, Almut E. D."
year: 2022
venue: "arXiv:2211.13777v3 (revised October 2023; journal publication not confirmed in this session)"
url: "https://arxiv.org/abs/2211.13777"
pdf: "sources/22-deep-learning-lob/lucchese-2022-short-term-predictability-order-book.pdf"
access: "full-text"
source_type: "working-paper"
evidence_grade: "B"
topic: "22-deep-learning-lob"
asset_class: "equities"
horizon: "tick"
tags: "model-confidence-set, order-flow, volume-representation, deepvol, deepof, multi-horizon, universal-model, predictability-horizon, lobster"
---

## Key insight
With a formal test (model confidence sets) rather than a comparison of F1 scores, order book information predicts mid-price returns for nearly every stock tested, but only out to about 50 to 300 book updates, which is a few milliseconds to about half a second. How the book is represented matters more than the network: models fed raw price and size levels are almost never among the best, while order flow or price-grid volume inputs are.

## Method
All models share the DeepLOB backbone (CNN, Inception, LSTM) and differ in input:
- deepLOB: raw level prices and sizes.
- deepOF: order flow per level (changes in bid and ask queues, as in Cont et al. and Kolm et al.).
- deepVOL: the "volume representation", sizes resting at each tick of a fixed price window around the mid, so every entry has the same unit and a new order at an empty level barely changes the input. An L3 variant splits each price's volume by queue position.

Each is run on L1 or L2 data, in single-horizon and seq2seq or attention multi-horizon form, and in single-stock and pooled ("universal") form. Targets are three classes of the h-step mid-price return, split at empirical terciles, for h in {10, 20, 30, 50, 100, 200, 300, 500, 1000} book updates. Models are compared with the Hansen et al. model confidence set against an unpredictive benchmark, across 11 rolling five-week windows. Predictability at a horizon means the benchmark is rejected from the set.

## Data and sample
LOBSTER Nasdaq data to ten levels, 2 January 2019 to 31 January 2020. Ten stocks chosen from 115 to span liquidity: QRTEA, CHTR, EXC, WBA, AAPL, LILAK, XRAY, PCAR, AAL, ATVI.

## Reported results
- Predictability is found for all stocks at short horizons and persists to 50 to 300 updates depending on the stock.
- Share of predictable stock-horizon cases in which each model is in the superior set (alpha 0.05 / 0.01): deepLOB(L1) 7% / 11%, deepOF(L1) 23% / 22%, deepLOB(L2) 5% / 11%, deepOF(L2) 88% / 89%, deepVOL(L2) 65% / 84%, deepVOL(L3) 77% / 86%.
- L2 data beats L1 clearly; L3 adds nothing for single-stock models and helps only pooled ones.
- Seq2seq multi-horizon versions outperform their single-horizon counterparts for each input type.
- Models trained on five stocks show predictability on five unseen stocks, supporting common patterns.
- The authors state that mid-to-mid returns are not tradable and that whether this predictability can be traded is open.

## Signal construction
Input transformation a bot can reuse: (a) multi-level order flow, the signed change in bid and ask queue sizes at each of the top levels between snapshots; (b) a price-grid volume vector, the size resting at each of W ticks either side of the mid. Standardise with a rolling window. Feed 100 steps to a CNN-LSTM or to a simpler model.

## Relevance to SOL perpetuals at minutes to hours
The representation result should transfer: SOL perp books have small ticks and sparse, shifting levels, exactly the case where level-indexed inputs are unstable. The horizon result is the sobering part. If predictability from the book alone dies within half a second on Nasdaq, a minutes-to-hours bot should not expect a raw-LOB network to carry its direction call; aggregated flow over longer windows is the more plausible input and needs separate testing. The model confidence set procedure is a good template for comparing candidate models on SOL data.

## Caveats
Ten stocks, 13 months, one venue. Horizons are in event time. No costs, spread or latency in the evaluation (latency is discussed in an appendix). Tercile labels differ from the smoothed labels in DeepLOB-style papers, so scores are not comparable across papers.
