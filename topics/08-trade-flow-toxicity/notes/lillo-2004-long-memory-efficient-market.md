---
title: "The Long Memory of the Efficient Market"
authors: "Lillo, Fabrizio; Farmer, J. Doyne"
year: 2004
venue: "arXiv cond-mat/0311053v2 (journal version in Studies in Nonlinear Dynamics and Econometrics; journal details not confirmed in this session)"
url: "https://arxiv.org/pdf/cond-mat/0311053"
pdf: "sources/08-trade-flow-toxicity/lillo-2004-long-memory-efficient-market.pdf"
access: "full-text"
source_type: "peer-reviewed"
evidence_grade: "A"
topic: "08-trade-flow-toxicity"
asset_class: "equities"
horizon: "tick"
tags: "trade-sign-autocorrelation, long-memory, order-splitting, hurst-exponent, market-efficiency"
---

## Key insight
The signs of orders (buy = +1, sell = -1) are a long-memory process: their autocorrelation decays as a power law so slowly that it is not summable. Future order signs are therefore quite predictable from past signs. Returns are nevertheless close to unpredictable, because order size and available liquidity adjust in the opposite direction. Predictable flow does not imply predictable price.

## Method
Each market order, limit order and cancellation is labelled +1 or -1 and the series is studied in event time. Long memory is tested with the classical and Lo-modified R/S statistics, and the Hurst exponent H is estimated four ways (periodogram, R/S, detrended fluctuation analysis, direct fit of the autocorrelation function), with alpha = 2 - 2H the decay exponent of the autocorrelation tau^(-alpha). They then model the price response to a market order as depending on sign, size and a time-varying liquidity parameter, and show which of these must co-move to whiten returns. Institution codes are used to check whether individual participants show long memory.

## Data and sample
London Stock Exchange electronic order book, 20 stocks continuously traded over 1999 to 2002, full record of orders and cancellations. A similar analysis is reported for NYSE stocks.

## Reported results
- Autocorrelation of order signs decays roughly as tau^(-alpha) with alpha about 0.6, in the range 0.36 to 0.77 across stocks; positive autocorrelation is statistically significant over lags of many thousands of events, spanning many days.
- Mean Hurst exponent by periodogram: 0.695 +/- 0.039 for market orders, 0.716 +/- 0.054 for limit orders, 0.768 +/- 0.059 for cancellations; R/S gives 0.696 +/- 0.032 for market orders.
- NYSE market-order signs show similar exponents.
- If liquidity were fixed, the sign memory would make returns strongly predictable. Efficiency is restored because when buy orders become more likely, buy market orders tend to be smaller relative to volume at the best ask, and liquidity is skewed against the expected flow.
- Some institutions display long memory in their own order signs and others do not, which the authors discuss as consistent with splitting of large orders.

## Signal construction
Two uses. (1) Flow-persistence forecast: predict the next-interval signed flow from an exponentially or power-law weighted sum of past trade signs, E[sign_{t+k}] proportional to sum_j w_j * sign_{t-j} with w_j decaying as j^(-alpha). (2) Surprise decomposition: split observed signed volume into the part predicted by past signs and the unexpected part. The paper's logic implies that only the unexpected part should move price, so a flow signal should be measured against its own forecast, not against zero. Parameters: alpha fitted per instrument on trade-sign autocorrelation at lags 1 to several thousand trades.

## Relevance to SOL perpetuals at minutes to hours
Trade-sign persistence is expected on SOL perps, where execution algorithms and liquidation engines slice large orders. The direct lesson is negative for naive signals: a high taker-buy ratio over the last minutes mostly predicts more taker buying, which liquidity providers already expect and price. What to test on SOL is whether flow surprise (signed volume minus its forecast from lagged signs) predicts returns at 1 to 60 minutes better than raw cumulative volume delta, and whether sign-memory exponents shift before large moves.

## Caveats
Equities from 1999 to 2002, before modern high-frequency market making. Event time, not clock time. The paper measures linear efficiency only and does not test a trading rule or costs. The order-splitting explanation was developed and tested in later work not covered by a note here.
