---
title: "Efficient estimation of bid-ask spreads from open, high, low, and close prices"
authors: "Ardia, David; Guidotti, Emanuele; Kroencke, Tim A."
year: 2024
venue: "Journal of Financial Economics 161, 103916"
url: "https://irf.fhnw.ch/bitstreams/e8c469d2-9c64-4004-8e87-53ee091f0cb1/download"
pdf: "sources/09-liquidity-price-impact/ardia-2024-efficient-bid-ask-spread-ohlc.pdf"
access: "full-text"
source_type: "peer-reviewed"
evidence_grade: "A"
topic: "09-liquidity-price-impact"
asset_class: "multi"
horizon: "minutes"
tags: "bid-ask-spread, ohlc, edge-estimator, corwin-schultz, abdi-ranaldo, roll, liquidity-measurement"
---

## Key insight
Existing spread estimators from bar data (Roll, Corwin-Schultz, Abdi-Ranaldo) are biased downward when there are few trades per bar, because they assume prices are observed continuously. The authors derive estimators that correct for this and combine them with minimum-variance weights into one estimator, EDGE. It beats the alternatives on US stocks and gives stable estimates across sampling frequencies on crypto.

## Method
With log open o, high h, low l, close c and mid-range eta_t = (h_t + l_t)/2, EDGE is

S^2 = w1 * E[x1] + w2 * E[x2]

x1_t = (pi_o/2) * (eta_t - o_t)(o_t - eta_(t-1)) + (pi_c/2) * (eta_t - c_(t-1))(c_(t-1) - eta_(t-1))

x2_t = (pi_o/2) * (eta_t - o_t)(o_t - c_(t-1)) + (pi_c/2) * (o_t - c_(t-1))(c_(t-1) - eta_(t-1))

w1 = Var[x2] / (Var[x1] + Var[x2]), w2 = Var[x1] / (Var[x1] + Var[x2])

The correction terms pi_o and pi_c equal -8 divided by the sum of the probabilities that the open (or previous close) differs from the high and from the low, counted over bars with trades. Negative estimates of S^2 are reset to zero. Evaluation is by simulation and by comparison with TAQ effective spreads. The authors publish code (the "bidask" package) and a certified replication package.

## Data and sample
US stocks, CRSP-TAQ merged sample 1993 to 2021 (1,637,621 stock-months), plus longer CRSP history. Crypto: all Binance pairs at minute, hourly and daily frequency, July 2017 to December 2021, 2,163 pairs and 53,865 pair-months.

## Reported results
- Against TAQ effective spreads, EDGE has Pearson correlation 78.86% versus 68.13% for Abdi-Ranaldo (AR) and 45.55% for Corwin-Schultz (CS). It also has the lowest mean absolute percentage error and RMSE and the smallest share of zero estimates.
- In simulations EDGE is unbiased regardless of the number of trades per day; the others shrink toward zero as trading becomes sparse.
- On Binance pairs, AR gives average spreads from 0.18% to 1.85% and CS from 0.02% to 1.45% depending on whether minute, hourly or daily bars are used. EDGE stays between 0.68% and 0.70%.
- For 2021 the average spread across crypto pairs is 0.35% to 0.45%.

## Signal construction
Compute EDGE on 1-minute OHLC bars over a rolling window (for example 60 to 240 bars), updated each minute, per venue. Outputs: an effective-spread estimate in percent. Use it as (a) a transaction-cost input and (b) a liquidity-stress indicator when it rises relative to its same-hour history. It needs no quote data, so it works on a venue that only publishes candles.

## Relevance to SOL perpetuals at minutes to hours
Sparse trading is exactly the Kalshi situation, and it is where Roll, CS and AR fail. EDGE is the best available choice for estimating Kalshi's effective spread from bars, and for building a long liquidity history for SOL on any venue. The crypto analysis has no quote-based benchmark, so accuracy on crypto is shown only through consistency across frequencies; validating it against Kalshi's own book would be needed.

## Caveats
The estimator assumes a constant spread within the window and a random-walk fundamental price with zero-mean returns; trending minutes and jumps violate this. With a small window the estimate is noisy and often zero. Estimates are for effective spread, not depth or impact.
