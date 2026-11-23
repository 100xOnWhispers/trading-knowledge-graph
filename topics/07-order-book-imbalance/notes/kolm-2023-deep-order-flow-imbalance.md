---
title: "Deep order flow imbalance: Extracting alpha at multiple horizons from the limit order book"
authors: "Kolm, Petter N.; Turiel, Jeremy; Westray, Nicholas"
year: 2023
venue: "Mathematical Finance 33(4), 1044-1081"
url: "https://ideas.repec.org/a/bla/mathfi/v33y2023i4p1044-1081.html"
pdf: "none"
access: "abstract-only"
source_type: "peer-reviewed"
evidence_grade: "A"
topic: "07-order-book-imbalance"
asset_class: "equities"
horizon: "seconds"
tags: "order-flow-imbalance, multi-level-ofi, alpha-term-structure, horizon-decay, neural-networks, stationarity"
---

## Key insight
Feeding a forecasting model stationary order flow (multi-level OFI) instead of raw order book states matters more than the choice of network. The abstract also gives a compact statement of how fast book-derived alpha decays: the effective horizon of stock-specific forecasts is about two average price changes.

## Method
Abstract only. The authors use deep learning to forecast high-frequency returns at multiple horizons for Nasdaq stocks using the most granular order book data, comparing models trained on order flow inputs with models trained directly on order book states, and then run cross-sectional regressions of forecasting performance (for an LSTM) on stock microstructure characteristics. The architecture comparison belongs to topic 22; this note records the feature-design and horizon findings.

A secondary description read in this session (Jaddu and Bilokon 2023, see that note) states that the study used a rolling out-of-sample design over 48 weeks (four weeks training, one week validation, one week testing), the first ten levels of OFI, and out-of-sample R2 measured against horizons expressed in units of average price changes; that CNN-LSTM extracted alpha most accurately; and that accuracy falls off after about six horizons. Those details are secondary and were not checked against the article.

## Data and sample
From the abstract: 115 stocks traded on Nasdaq. Period not stated in the abstract.

## Reported results
From the abstract only:
- Off-the-shelf neural networks trained on stationary order flow inputs outperform most models trained directly on order books.
- Forecasting performance is related to microstructure characteristics; "information-rich" stocks are more predictable.
- The effective horizon of stock-specific forecasts is approximately two average price changes.

No numerical R2 values were read.

## Signal construction
Inputs: L2 updates for the top ten levels. Build the 10-dimensional OFI vector per update or per short bucket (see the Xu, Gould and Howison note), keep a rolling window of recent vectors, and feed it to a model that outputs a vector of return forecasts at several event-time horizons (an "alpha term structure"). Measure horizons in units of average price changes for the instrument, not clock time, so that the model is comparable across instruments and volatility regimes.

## Relevance to SOL perpetuals at minutes to hours
Two points transfer. First, use flow features, not raw book snapshots, for any ML or RL model on SOL books. Second, calibrate expectations: if book-derived alpha lasts about two price changes, then for a liquid SOL perp it is exhausted in seconds. For a bot holding minutes to hours, order-book models are an execution-timing and short-term risk tool unless SOL data show materially longer persistence. The useful experiment is to express SOL horizons in price-change units on each venue and see where predictability reaches zero.

## Caveats
Abstract-only access; the paper's numbers, period and cost treatment were not verified. Equities, not crypto. Forecast accuracy is reported without a net-of-cost trading result, as far as the abstract shows.
