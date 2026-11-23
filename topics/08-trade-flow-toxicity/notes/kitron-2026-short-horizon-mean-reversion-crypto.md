---
title: "Short-horizon mean reversion in cryptocurrency markets: a matched cross-market measurement"
authors: "Kitron, Nadav A.; Wengrowicz, Jonathan M."
year: 2026
venue: "arXiv 2608.21888v1 (August 2026)"
url: "https://arxiv.org/pdf/2608.21888"
pdf: "sources/08-trade-flow-toxicity/kitron-2026-short-horizon-mean-reversion-crypto.pdf"
access: "full-text"
source_type: "working-paper"
evidence_grade: "B"
topic: "08-trade-flow-toxicity"
asset_class: "crypto"
horizon: "minutes"
tags: "taker-imbalance, mean-reversion, liquidity-provision, out-of-sample, transaction-costs, machine-learning-benchmark"
---

## Key insight
At 15-minute horizons the sign of the next candle is weakly but pervasively predictable from the signs of recent candles across Binance pairs, in the direction of reversal. The reversal concentrates after moves that aggressive taker flow pushed and grows with the size of the taker imbalance, while order-book depth consumed by the move conditions nothing. Taker imbalance tells you when the reversal applies but adds no out-of-sample skill beyond the price path. The gross edge peaks near 1.3 bp per trade and does not cover costs.

## Method
A three-parameter constrained logistic model on the signs of the previous twelve candles (a kernel-tied AR logit), scored by out-of-sample AUC in a walk-forward (train 5,760 candles, test 960, non-overlapping test blocks), with moving-block bootstrap inference, an exact permutation null, false-discovery control, and a frozen six-month holdout. For flow, Binance klines give taker-buy volume, so the bar's taker imbalance is i_t = 2 * V_takerbuy / V - 1. A bar is "flow-driven" when its return and imbalance have the same sign (about 70% of bars) and "flow-opposed" otherwise. Depth consumption uses Binance's roughly 30-second snapshots of notional within 1% to 5% of mid on USDT-M perpetuals. Alternative learners (free AR logit, gradient-boosted trees, a multilayer perceptron) are compared on the same lagged-return inputs.

## Data and sample
183 highest-volume Binance USDT spot pairs and 187 US stocks and ETFs, 15-minute candles, 1 January 2025 to 11 February 2026; multi-year histories back to 2021; refetches from Coinbase, OKX and Bybit; Binance taker-flow, order-book and perpetual series; holdout February to August 2026. Focal coins BTC, ETH, SOL, XRP.

## Reported results
- 90% of 183 crypto pairs show significant directional reversal against 2.7% of 187 US stocks and ETFs.
- Out-of-sample AUC is 0.540 after flow-driven bars versus 0.519 after flow-opposed bars; the pooled flip-rate difference is +0.021 (CI 0.015 to 0.026).
- Adding twelve lags of taker imbalance to the sign path "adds nothing out of sample".
- Depth-consuming versus depth-replenished moves: flip-rate difference -0.002 (CI -0.007 to +0.004).
- The reversal "replicates in full" on USDT-M perpetuals; conditioning on basis, funding rate, funding clock, volatility and session is flat.
- Gross edge peaks near 1.3 bp per trade against a 5 bp cheapest round-trip band; no pair clears it; the median pair earns 0.46 bp; 5-minute bars are worse (0.15 bp).
- Holdout: class-mean AUC gap of +0.011 (CI 0.008 to 0.014) under the most conservative accounting; 77% of the attenuation is decay on a fixed universe.
- Gradient-boosted trees and an MLP lose to the three-parameter model on out-of-sample log-loss in all cells; on BTC 1-hour only the constrained model beat predicting the base rate.

## Signal construction
From 15-minute klines: i_t = 2 * takerBuyVolume / volume - 1 and r_t = close/open - 1. Flag flow-driven bars where sign(r_t) = sign(i_t), and rank |i_t| into trailing quintiles. After a flow-driven bar in a high |i_t| quintile, raise the probability of a next-bar reversal; after a flow-opposed bar, assume no edge. Use it as a filter or as an entry-timing adjustment for limit orders.

## Relevance to SOL perpetuals at minutes to hours
The horizon and data type are exactly what a kline-driven SOL bot uses, SOL is a focal coin, and the effect is reported on perpetuals. The practical reading is defensive: do not chase a 15-minute move that taker flow pushed, and enter passively against it if anything. Whether the same conditional reversal shows up on Kalshi with Binance flow as the conditioning variable is untested. The model-class result argues for small constrained models over deep ones at this signal-to-noise level.

## Caveats
Authors are independent researchers and the paper is unrefereed. The flow-driven label uses the bar's own return sign, so the split is a conditioning, not a treatment, as the authors state. Spot fees are the cost benchmark; perp fees differ. One holdout window shows decay.
