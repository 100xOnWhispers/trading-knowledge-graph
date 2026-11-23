---
title: "Deep Limit Order Book Forecasting: A microstructural guide"
authors: "Briola, Antonio; Bartolucci, Silvia; Aste, Tomaso"
year: 2024
venue: "arXiv:2403.09267v4 (journal publication not confirmed in this session)"
url: "https://arxiv.org/abs/2403.09267"
pdf: "sources/22-deep-learning-lob/briola-2024-deep-lob-forecasting-microstructural-guide.pdf"
access: "full-text"
source_type: "working-paper"
evidence_grade: "B"
topic: "22-deep-learning-lob"
asset_class: "equities"
horizon: "tick"
tags: "lobframe, deeplob, tick-size, large-tick, small-tick, mcc, transaction-probability, evaluation-metrics, lobster"
---

## Key insight
How well a deep LOB model forecasts depends mainly on the instrument's tick size relative to its spread: DeepLOB is strong and stable on large-tick stocks and close to random on small-tick stocks beyond the shortest horizon. Standard classification scores also overstate usefulness. When the authors measure the probability that a sequence of forecasts opens and closes a position at the right times, it is far lower than the classification scores suggest and falls when a confidence threshold is applied.

## Method
Stocks are grouped by average spread in ticks: small-tick if the mean spread is at least about 3 ticks, large-tick if at most about 1.5 ticks, medium in between. DeepLOB is trained per stock with the open-source LOBFrame pipeline on 100 x 40 raw book inputs, with balanced random sampling of up to 5,000 examples per class per day and a five-day rolling normalisation. Horizons are 10, 50 and 100 book updates. Forecast quality is the Matthews correlation coefficient (MCC), also computed after keeping only forecasts whose class probability exceeds 0.5, 0.7 or 0.9.

Transaction metric: map forecasts to positions (open on the first up or down call, hold through stable calls, close and reverse on the opposite call). With PT the number of transactions in the true labels, TT in the predictions and CT those that coincide, p_T = CT / (PT + TT - CT).

## Data and sample
LOBSTER tick data for 15 Nasdaq stocks, 2017 to 2019: six small-tick (CHTR, GOOG, GS, IBM, MCD, NVDA), three medium-tick (AAPL, ABBV, PM), six large-tick (BAC, CSCO, KO, ORCL, PFE, VZ).

## Reported results
- MCC at horizon 10: small-tick 0.11, medium-tick 0.13, large-tick 0.29.
- MCC at horizon 50: small-tick 0.04, medium-tick 0.085, large-tick 0.36.
- MCC at horizon 100: small-tick 0.01 (the authors call this random), medium-tick 0.036.
- For large-tick stocks at horizon 10, 31% of forecasts still pass a 0.9 probability threshold; for small-tick stocks fewer than 1% pass thresholds above 0.6.
- p_T for small-tick stocks at horizon 10 averages 0.06 for one group (CHTR, GOOG, GS) and 0.12 for another (IBM, MCD, NVDA); for thresholds above 0.5 it is essentially zero.
- MCC rises with the probability threshold while p_T falls, because filtering breaks the sequence of signals needed to manage a position.
- The authors argue that a historical-data backtest of such forecasts requires assumptions (always filled, no impact, no costs, no latency) that make it unreliable, and they do not report one.

## Signal construction
Not a signal. Two reusable diagnostics: (1) spread-in-ticks of the instrument as a prior on whether a book-based model can work; (2) p_T computed on out-of-sample forecast sequences as an acceptance test alongside MCC.

## Relevance to SOL perpetuals at minutes to hours
Crypto perps usually have a tick that is small relative to price, so depth can be spread thinly over many levels; whether SOL on a given venue behaves like the paper's large-tick or small-tick case is an empirical question to settle first, by measuring the spread in ticks and best-queue sizes on each venue (this was not checked in this session). Kalshi's contract specification may differ again. The p_T idea matters directly for a directional bot: what counts is getting entries and exits right in sequence, not per-snapshot accuracy.

## Caveats
One model family (DeepLOB) only; the authors argue the conclusions do not depend on it but do not show that. US large caps, 2017 to 2019. p_T treats any timing mismatch as a miss, which is strict, and ignores trade size and price. No cost or profit figures.
