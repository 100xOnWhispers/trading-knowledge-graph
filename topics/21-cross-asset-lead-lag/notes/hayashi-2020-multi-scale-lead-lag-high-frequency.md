---
title: "Multi-scale analysis of lead-lag relationships in high-frequency financial markets"
authors: "Hayashi, Takaki; Koike, Yuta"
year: 2020
venue: "arXiv preprint 1708.03992 (v4, May 2020); journal version not confirmed"
url: "https://arxiv.org/abs/1708.03992"
pdf: "sources/21-cross-asset-lead-lag/hayashi-2020-multi-scale-lead-lag-high-frequency.pdf"
access: "full-text"
source_type: "working-paper"
evidence_grade: "B"
topic: "21-cross-asset-lead-lag"
asset_class: "equities"
horizon: "tick"
tags: "lead-lag, wavelet, multi-scale, non-synchronous, hayashi-yoshida, estimator, methodology"
---

## Key insight
Two price series can have different leaders at different time scales, and a single lead-lag number hides this. The paper gives an estimator of a scale-by-scale lead-lag time that works on raw non-synchronous ticks with no interpolation. On real quote data it separates a sub-millisecond lead in one direction from a millisecond-scale lead in the opposite direction, which the single-lag Hoffmann-Rosenbaum-Yoshida (HRY) estimator blends together.

## Method
Model: two Brownian motions whose cross-spectral density on the dyadic frequency band j (time scales between 2^-j and 2^-j+1) is R_j * exp(-i * theta_j * lambda). R_j is the correlation at scale j and theta_j the lead-lag time at that scale. Prices are volatility-modulated versions of these processes observed at irregular, asynchronous times.

Estimator: build the empirical cross-covariance function of the two tick series (a Hayashi-Yoshida-type sum over overlapping increments, shifted by a candidate lag), then apply a Daubechies wavelet filter of level j to that cross-covariance function instead of to the raw data. theta_j-hat is the lag, on a finite grid, that maximizes the level-j filtered cross-covariance. Consistency is proved as the finest resolution shrinks with a fixed observation window. The paper compares against the HRY estimator (see the topic 05 note) and the Dobrev-Schaumburg (DS) estimator based on counts of near-simultaneous activity. The foundation is Hayashi and Yoshida (2005, Bernoulli 11, 359-379), cited but not opened in this session.

## Data and sample
Monte Carlo experiments, then quote updates for the 108 component stocks of the NASDAQ-100, NASDAQ versus BATS, Daily TAQ with microsecond stamps, all 21 trading days of August 2015, 9:45 to 15:45. Log prices are built from micro-prices. The empirical example is same-asset cross-venue; the method is what matters for this topic.

## Reported results
- At the finest levels j = 1 to 3 (0.1 to 0.8 ms) the estimates peak at small positive values, meaning NASDAQ leads BATS; DS estimates concentrate at 0.3 ms with SIP timestamps and 0.1 ms with participant timestamps, which the authors attribute to reporting latency and to the transit time between the Carteret and Secaucus data centres.
- At coarser levels j = 4 to 7 (0.8 to 12.8 ms) the estimates are bimodal, and the negative ones (BATS leads) are rank-correlated with the HRY estimates.
- Conclusion: fast traders produce one lead-lag at the finest scale, slower traders a different one at millisecond scales.

## Signal construction
Not a signal. It is a measurement tool: for a pair (leader candidate, target) take raw trade or quote timestamps, compute the shifted HY cross-covariance on a lag grid, wavelet-filter it at levels corresponding to, say, 100 ms, 1 s, 10 s, 1 min and 10 min, and record the arg-max lag and correlation per level. Re-estimate daily. The output is a table of "who leads at which scale" that tells the bot which leader features are worth using at its own horizon.

## Relevance to SOL perpetuals at minutes to hours
The multi-scale idea is directly useful. BTC may lead SOL at sub-second scales because of liquidity, while SOL-specific flow (Solana ecosystem news, on-chain activity) could lead at minute scales, and equity index futures could lead both at multi-minute scales during US hours. A single HY peak would be dominated by the fastest effect. Applying the level-j estimator to BTC/SOL, ES/BTC and Binance-SOL/Kalshi-SOL would show whether any lead survives at 1 to 60 minutes.

## Caveats
Theory assumes Gaussian drivers and no microstructure noise. Timestamp conventions change the answer by fractions of a millisecond in the paper, and by far more across crypto venues with unsynchronized clocks. One month of 2015 US equity data; no crypto, no forecasting test, no trading results.
