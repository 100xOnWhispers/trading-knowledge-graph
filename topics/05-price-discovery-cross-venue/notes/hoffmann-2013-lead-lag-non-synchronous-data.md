---
title: "Estimation of the lead-lag parameter from non-synchronous data"
authors: "Hoffmann, Marc; Rosenbaum, Mathieu; Yoshida, Nakahiro"
year: 2013
venue: "Bernoulli"
url: "https://arxiv.org/pdf/1303.4871"
pdf: "sources/05-price-discovery-cross-venue/hoffmann-2013-lead-lag-non-synchronous-data.pdf"
access: "full-text"
source_type: "peer-reviewed"
evidence_grade: "B"
topic: "05-price-discovery-cross-venue"
asset_class: "futures"
horizon: "seconds"
tags: "lead-lag, hayashi-yoshida, non-synchronous, estimator, tick-data, methodology"
---

## Key insight
Lead-lag between two assets can be defined as a time shift theta such that (X_t, Y_{t+theta}) is a semimartingale, and theta can be estimated consistently from raw, irregularly spaced ticks without resampling to a common grid. The estimator maximizes a shifted Hayashi-Yoshida covariation over candidate lags. This is the estimator practitioners now use for sub-second cross-venue lead-lag in crypto (see the Nayyar note).

## Method
For observation intervals I of X and J of Y, the shifted Hayashi-Yoshida contrast is

U_n(theta) = sum over (I, J) of X(I) * Y(J) * 1{ I overlaps J shifted by -theta },

that is, the sum of products of increments whose intervals overlap after shifting one series by theta. The estimator is theta_hat = argmax over a grid of |U_n(theta)|. The authors prove consistency and a convergence rate governed by the sparsity of sampling. The model has no microstructure noise; the empirical recipe is to subsample trades until the signature plot flattens, then scan a coarse grid followed by a fine grid.

## Data and sample
Simulations (Bachelier model with known theta) and one real illustration: DAX index futures (FDAX) versus Euro-Bund futures on Eurex, December 2010 maturity, every trading day of October 2010, trade data from QuantHouse.

## Reported results
- Simulation: with true theta = 0.1 and correlation 0.75 on non-synchronous data, estimates fall on 0.099, 0.1 or 0.101 across 300 samples.
- Real data: after keeping 1 trade in 20, on October 13, 2010 (2,018 Bund and 3,037 FDAX trades) the contrast peaks at about -0.8 second, meaning FDAX leads the Bund. Over October 2010 the estimated lags are "systematically negative" and of the order of one second.
- The authors caution the values are small and offer tick-size differences as a speculative explanation.

## Signal construction
Not a signal by itself; it measures the usable delay. Implementation for a bot: take trade or mid-quote update streams for the leader candidate (Binance SOLUSDT perp) and the target (Kalshi SOL perp), compute U_n(theta) on a grid (for example -5 s to +5 s in 50-100 ms steps), normalize by the product of realized volatilities to get a cross-correlation curve, and record the argmax and the asymmetry between positive and negative lags (the lead-lag ratio). Re-run hourly or daily. The peak lag tells the bot how stale Kalshi quotes are; the peak height tells it how much of Binance's move is transmitted.

## Relevance to SOL perpetuals at minutes to hours
The estimator is asset-agnostic and suits a thin venue because it does not need Kalshi to trade on a regular grid. If Kalshi lags by seconds rather than milliseconds, a taker with a few hundred milliseconds of latency could still act on Binance moves; if the lag is comparable to the bot's latency, the edge is only available to faster participants and the bot should use larger-venue signals for direction at minute horizons instead.

## Caveats
Theory assumes no microstructure noise and a single constant lag; real lags vary with volatility and liquidity. Clock offsets between venues bias theta directly (see the Lim and Young notes on event-time versus receive-time). The empirical example is cross-asset futures in 2010, not same-asset cross-venue crypto.
