---
title: "Cryptocurrency Market Consolidation in 2020-2021"
authors: "Kwapien, Jaroslaw; Watorek, Marcin; Drozdz, Stanislaw"
year: 2021
venue: "Entropy (arXiv:2112.06552 version read)"
url: "https://arxiv.org/abs/2112.06552"
pdf: "sources/21-cross-asset-lead-lag/kwapien-2021-cryptocurrency-market-consolidation.pdf"
access: "full-text"
source_type: "peer-reviewed"
evidence_grade: "B"
topic: "21-cross-asset-lead-lag"
asset_class: "crypto"
horizon: "minutes"
tags: "bitcoin, ethereum, altcoins, lagged-cross-correlation, one-minute, minimal-spanning-tree, market-mode, crypto-equity, stability"
---

## Key insight
On one-minute Binance data for 80 liquid coins, the cross-correlation of altcoins with BTC and ETH is far larger contemporaneously than at a one-minute lag in either direction; a small, statistically significant excess when BTC or ETH is advanced by one minute suggests the rest of the market absorbs their information within about a minute, and no flow from the less liquid coins back to BTC and ETH is detectable. The authors add that autocorrelation in BTC and ETH returns could produce the same pattern, so they do not claim the question is settled. BTC or ETH is the stable hub of the correlation network at 10-minute scales, but at an hour or longer the hub is unstable.

## Method
q-dependent detrended cross-correlation coefficient rho_q(s) for all 3,160 pairs, with q = 1 (all fluctuations) and q = 4 (large fluctuations) and scales s = 10, 60, 180 and 360 minutes, in a 7-day moving window stepped daily. From the correlation matrix: largest eigenvalue lambda_1 and the Shannon entropy of its eigenvector (market mode), and minimal spanning trees (hub identity, maximum degree, mean path length). Lead-lag test: rho_q(s, tau) for pairs (BTC, X) and (ETH, X) with the BTC or ETH series shifted by tau = -1 or +1 minute, averaged over all other coins X, at s = 10 min. Cross-market part: rho_q(s) between BTC and currencies, commodities and stock indices.

## Data and sample
One-minute prices in USDT for 80 of the most actively traded coins on Binance, 1 January 2020 to 1 October 2021 (921,600 points per series). Traditional assets from Dukascopy: 13 currencies, crude oil, copper, silver, gold, and the S&P500, NASDAQ100, Russell 2000, DJIA, FTSE, DAX and NIKKEI. A text search of the ticker table found no SOL entry.

## Reported results
- Averaged over altcoins, rho at tau = 0 is "significantly larger" than at tau = +1 or -1 minute for both BTC and ETH.
- For q = 1 the advanced BTC series gives a larger average coefficient than the lagged one, and the difference is statistically significant; for q = 4 the two shifts are comparable in most windows. ETH behaves similarly.
- Authors' reading: the market absorbs BTC and ETH information "with a time needed for this absorption being as long as a minute"; the reverse transfer "cannot be detected"; but BTC and ETH autocorrelation longer than one minute can create the same asymmetry, so the question is not answered decisively.
- Market-wide correlation was flat until about October 2020, rose strongly to mid-2021, then levelled off; correlations now saturate at shorter scales than before (an Epps-type effect weakening over time).
- Network: star-like with BTC or ETH as hub on short scales; on scales of an hour or more the hub "frequently switches among the most liquid cryptocurrencies".
- BTC versus traditional assets: strongest correlation with the S&P500 and other stock indices, weaker with oil, copper and most currencies, negative with JPY; inter-market correlation is high in the same turbulent periods when intra-crypto correlation is high, weaker for large fluctuations, and needs long time scales to build up.

## Signal construction
Diagnostic first: for target SOL, compute the lagged correlation of SOL's bar return with BTC's and ETH's returns at lags of -5 to +5 bars for bar lengths of 10 seconds to 5 minutes, and subtract what SOL's own and the leader's autocorrelation would predict (for example by pre-whitening both series with short AR models). Only a residual asymmetry is a usable lead. Secondary feature: the first eigenvalue share of a rolling correlation matrix of major coins at 10-minute scale as a consolidation index.

## Relevance to SOL perpetuals at minutes to hours
This is the most direct cross-sectional evidence in the set, and it bounds the effect: across liquid Binance coins in 2020-2021 the BTC and ETH lead was at most about a minute and small next to the contemporaneous link. For SOL in 2026, a top-five asset, the lead on major venues is likely shorter still. The unstable hub at hourly scales argues against hard-coding BTC as the only driver for hour-horizon features.

## Caveats
One-minute sampling cannot resolve sub-minute leads. The lead-lag test uses only lags of one minute, one scale, and averages over coins, with no forecasting or trading test. The authors themselves flag the autocorrelation confound. Sample ends October 2021; SOL not included.
