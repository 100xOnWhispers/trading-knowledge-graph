---
title: "The Quarter-Hour Effect: Periodic Algorithmic Trading and Return Predictability in Cryptocurrency Futures"
authors: "Kim, Chan; Hansen, Peter Reinhard"
year: 2026
venue: "arXiv 2607.09426v2 (July 2026)"
url: "https://arxiv.org/pdf/2607.09426"
pdf: "sources/08-trade-flow-toxicity/kim-2026-quarter-hour-effect-crypto-futures.pdf"
access: "full-text"
source_type: "working-paper"
evidence_grade: "B"
topic: "08-trade-flow-toxicity"
asset_class: "crypto"
horizon: "hours"
tags: "signed-order-flow, taker-imbalance, intraday-periodicity, algorithmic-trading, sol, perpetuals, return-predictability"
---

## Key insight
Trading volume and volatility in Binance perpetuals spike at every minute, five-minute and quarter-hour mark, and the share of round-sized trades drops in those bursts, pointing to scheduled algorithms. Signed taker imbalance measured in the first 10 seconds of a quarter-hour predicts cumulative returns over the next 4 to 12 hours, while the same imbalance measured at ordinary times, or at one-minute and five-minute marks, has little predictive content. This is direct evidence that when flow is measured matters as much as how.

## Method
Aggregate trades are binned into 10-second intervals. Signed flow uses the exchange's isBuyerMaker flag: OF_t = sum of V_k * D_k and OI_t = OF_t / sum of V_k in [-1, 1]. An "Autocorrelation Map" displays sign autocorrelations of flow and returns by minute-of-hour phase. Quarter-hour opening returns (first 10 seconds) are forecast out of sample from boundary-aligned lags and 28 technical indicators, re-estimated monthly on a trailing six months. For flow informativeness, direct regressions r_{t,t+l} = a + b*OI_t + b1*OI_t*1{minute open} + b5*OI_t*1{5-minute open} + b15*OI_t*1{quarter-hour open} + controls are run for l from 30 seconds to 24 hours, with HAC errors; the cumulative coefficient for quarter-hour openings is the reported effect. A two-stage decomposition splits opening imbalance into a lagged-flow part, a public-signal part and a residual.

## Data and sample
Binance USDT-margined perpetuals for BTC, ETH, XRP, SOL, DOGE and ADA, aggregate trades with millisecond timestamps, 1 January 2021 to 31 October 2024 (1,400 days).

## Reported results
- The first 10 seconds of quarter-hour minutes have about 26% more trades, 32% more dollar volume and 26% larger absolute returns than the same interval of ordinary minutes.
- Opening-return forecasts: out-of-sample R-squared averages 2.464% for lags alone and 3.37% for lags plus indicators, positive for all six contracts. The predictable component is about 0.5 bp per boundary, roughly one tenth of a 5 bp taker fee.
- Quarter-hour opening imbalance: the predictive slope is negative over the first half hour (short-run reversal), turns positive, and typically peaks between 8 and 12 hours. Between 4 and 12 hours it is significant at 95% for four of six contracts at every horizon. For SOL it is significant at 90% at 4 and 12 hours and insignificant at 8 hours.
- The effect survives excluding funding-settlement quarter-hours and the top of the hour, and using only the sign of imbalance.
- At 4 hours the predictive content comes mainly from the lagged-flow component (58% cross-asset mean share); by 12 hours mainly from the public-signal component (65%). Lagged flow contributes about 5 to 6 bp interquartile effect; the public component grows to 9.8 bp at 8 hours and 16.9 bp at 12 hours.

## Signal construction
For each quarter-hour boundary (minutes 0, 15, 30, 45 UTC), compute OI over seconds 0 to 10 from the Binance SOL (and BTC, ETH) perp trade stream as (taker buy volume - taker sell volume) / total volume. Maintain a smoothed sum of recent boundary imbalances; a positive value tilts the directional bias long for the next 4 to 12 hours and against the move for the next 30 minutes. Refit slopes on a rolling window.

## Relevance to SOL perpetuals at minutes to hours
The horizon and instrument match the bot directly, and SOL is in the sample, although SOL is the weakest of the six. Kalshi's 8-hour funding matches Binance's clock, and the authors show the effect is not a funding artifact. The magnitude is single-digit basis points over hours, so it is a tilt to combine with other signals, not a standalone trade. Re-test on 2025 and 2026 data and check whether the same boundary effect appears on Bybit, OKX and Hyperliquid.

## Caveats
The horizon regressions are estimated on the full sample; only the opening-return forecast is out of sample. No net-of-cost strategy is reported. Part of the 12-hour effect is explained by public price-volume indicators, so it overlaps with momentum. Working paper; one author acknowledges funding from Ripple's university research initiative, stated to have had no role in the research.
