---
title: "Price Transmission from Bitcoin to Altcoins: High-Frequency Evidence and Implications for Trading Strategy"
authors: "Kurihara, Tomoki; Matsumoto, Takuji"
year: 2026
venue: "Asia-Pacific Financial Markets"
url: "https://t2r2.star.titech.ac.jp/rrws/file/CTT100941776/ATD100000413/"
pdf: "sources/21-cross-asset-lead-lag/kurihara-2026-price-transmission-bitcoin-altcoins.pdf"
access: "full-text"
source_type: "peer-reviewed"
evidence_grade: "B"
topic: "21-cross-asset-lead-lag"
asset_class: "crypto"
horizon: "minutes"
tags: "bitcoin, altcoins, lead-lag, granger-causality, liquidity, lightgbm, machine-learning, one-minute"
---

## Key insight
At one-minute resolution on Binance, Bitcoin leads only illiquid altcoins. ETH and LTC move with BTC inside the same minute and show no lagged response, while small-cap coins keep responding for one to several minutes. Across the whole Binance universe the speed of response rises with trade count. A long-only machine-learning rule driven by the previous minute's BTC return beat buy-and-hold on the small caps in one-week out-of-sample tests.

## Method
- Cross-correlation of 1-minute log returns between BTC and each altcoin at lags -5 to +5.
- Immediate Sensitivity Indicator: ISI = rho_0 - (1/5) * sum_{i=1..5} rho_{-i}, the contemporaneous correlation minus the mean correlation at the five lags where the altcoin follows BTC. High ISI means fast response. ISI is regressed on log trade count across all listed coins.
- Pairwise Granger tests with one lag, both directions.
- VAR(3) on eight coins and orthogonalized impulse responses to a BTC shock (ordering BTC, ETH, LTC, then small caps).
- Trading: two LightGBM binary classifiers per altcoin (an entry model and a hold model) with inputs r_BTC(t-1) and r_ALT(t-1); labels are whether the next-minute return exceeds a threshold; thresholds chosen by grid search in sample; long or flat; fee 0.02% per trade.

## Data and sample
Binance API, 1-minute closes and trade counts. Regimes: Bull (25 Feb to 25 Mar 2024, 369 coins), Bear (22 Jun to 19 Jul 2024, 381 coins), Sideways (24 Aug to 24 Sep 2024), Crash (30 Jan to 1 Mar 2025). Detailed tests on BTC, ETH, LTC and five small caps from the 50 least-traded pairs (BIFI, CITY, PIVX, GNO, QKC). First three weeks of each regime in sample, final week out of sample.

## Reported results
- ETH and LTC: very high lag-0 correlation with BTC and no significant correlation at other lags, in both Bull and Bear regimes.
- QKC, BIFI and CITY: correlation at lag -1 slightly above lag 0 in the Bull regime. Lag-0 correlations are higher and lagged ones lower in the Bear regime (faster reaction in downturns).
- ISI versus log trade count: correlation 0.561 (Bull) and 0.483 (Bear), both p < 1e-16.
- Granger: BTC to altcoin significant for every pair; the reverse mostly not (exceptions GNO in Bull; ETH and PIVX in Bear).
- VAR: BTC(t-1) coefficients of 0.1 or more for PIVX and QKC, 0.05 or less for others; negative own-lag coefficients for small caps (GNO -0.22); effects essentially gone by lags 2 and 3.
- Selected thresholds: hold -0.0001 in all regimes; entry 0 (Bull, Crash) and 0.0001 (Sideways).
- The lag strategy's final cumulative return exceeded buy-and-hold for the small caps in each regime; returns on ETH and LTC "remained relatively low"; the Sideways regime was weakest. Numerical returns are in figures and were not extracted.

## Signal construction
Per target coin: features r_BTC(t-1) and r_target(t-1) at 1-minute bars (extendable to several lags and to ETH); gradient-boosted classifier for "next-minute return above threshold"; separate entry and hold thresholds so that fees create hysteresis. Monitor ISI per coin weekly as a measure of how much lag remains.

## Relevance to SOL perpetuals at minutes to hours
The headline is a warning for SOL: SOL is a large, heavily traded coin and should behave like ETH and LTC here, reacting to BTC within the minute on the major venues, leaving no one-minute BTC lead to trade. The liquidity law suggests where a lag could still exist: on a thin venue. A Kalshi SOL perp with few trades per minute may have a low ISI against Binance BTC and Binance SOL even though SOL itself does not. That is testable with the paper's exact tools.

## Caveats
Spot, long-only, on the 50 least-traded Binance pairs, where quoted spreads and depth are poor; the backtest charges 0.02% fees but no spread or slippage and uses 1-minute closes, so stale-price effects may inflate results. Thresholds were tuned on five coins. Each out-of-sample window is one week. Regimes were chosen around BTC-specific events. SOL is not analysed.
