---
title: "Net Buying Pressure and the Information in Bitcoin Option Trades"
authors: "Alexander, Carol; Deng, Jun; Feng, Jianfen; Wan, Huning"
year: 2023
venue: "Journal of Financial Markets 63, 100764 (arXiv:2109.02776v2, March 2022, is the version read)"
url: "https://arxiv.org/abs/2109.02776"
pdf: "sources/20-options-derived-signals/alexander-2023-net-buying-pressure-bitcoin-option-trades.pdf"
access: "full-text"
source_type: "peer-reviewed"
evidence_grade: "B"
topic: "20-options-derived-signals"
asset_class: "crypto"
horizon: "hours"
tags: "deribit, options-order-flow, net-buying-pressure, implied-volatility, informed-trading, limits-to-arbitrage"
---

## Key insight
Signed Deribit option flow moves bitcoin implied volatility at the hourly horizon, and roughly 40 to 46% of an at-the-money call implied-volatility change reverses in the next hour, which is the signature of market makers charging for inventory rather than learning. At-the-money flow looks like volatility trading; directional information shows up only in out-of-the-money and deep out-of-the-money options, and only from 2019 onward. The paper tests what drives implied volatility, not whether option flow predicts the bitcoin price.

## Method
Each trade is signed by the exchange's buyer or seller flag and weighted by absolute Black-Scholes delta. Net buying pressure `A` for calls and puts in a moneyness bucket is delta-weighted buyer-initiated minus seller-initiated volume. Following Chen and Wang (2017) it is split into
- directional demand `D_C = (A_C - A_P) / 2` (and `D_P = -D_C`),
- volatility demand `V = (A_C + A_P) / 2`.

Hourly regressions of the change in bucket implied volatility on the spot return, spot volume, the pressure measures and the lagged implied-volatility change. A negative coefficient on the lagged change supports limits to arbitrage; equal loadings on call and put pressure support volatility-motivated trading; opposite signs support directional trading. Buckets: five delta ranges (deep out-of-the-money 0.02 to 0.125, out-of-the-money 0.125 to 0.375, at-the-money 0.375 to 0.625, and two in-the-money ranges) and three maturity ranges (1 to 7, 8 to 21, 22 or more days).

## Data and sample
Deribit bitcoin option trades, tick level, 1 January 2017 to 28 July 2021; 3,427,160 trades after cleaning (53.5% calls). Hourly aggregation. Results are reported for 2019, 2020 and January to July 2021. Spot volume from Bitstamp, Coinbase and Gemini.

## Reported results
- The coefficient on the lagged at-the-money call implied-volatility change is -0.458 in 2019 and -0.395 in 2021, against about -0.17 for S&P 500 options and -0.23 for TAIEX options in the studies the authors cite.
- Spot volume raises implied volatility in every bucket and year (1% significance).
- Volatility-motivated demand is significant in all moneyness buckets; directional demand is significant mainly in the two out-of-the-money buckets. Longer-dated options carry less informed flow.
- No learning effects in 2017 and 2018. Results hold at 4-hour and 8-hour aggregation but not at daily aggregation.
- Directional pressure is strongest in Asian hours and volatility-motivated pressure in European hours.
- Options with 1 to 7 days to expiry were 38.09% of Deribit volume in 2021. The call to put volume ratio was about 54:46 after 2019. Realized minus implied volatility was negative in every year shown.

## Signal construction
From the Deribit trade stream (`direction`, `amount`, `iv`, instrument, index price): compute delta per trade, bucket by delta and days to expiry, and sum signed delta-weighted volume per hour. Keep `D_C` for the out-of-the-money buckets with 1 to 21 days to expiry as the directional-flow feature and `V` at the money as the volatility-flow feature. Normalise by total delta-weighted volume in the bucket. The paper supports using these to explain implied-volatility changes; using `D_C` to predict the underlying return is an extension the paper does not test.

## Relevance to SOL perpetuals at minutes to hours
The construction transfers directly to BTC and ETH flow, which can serve as a market-wide input for SOL. It does not transfer to SOL's own options: the Deribit snapshot in [deribit-2026-option-book-summary-sol-liquidity](deribit-2026-option-book-summary-sol-liquidity.md) shows too few SOL trades per hour to fill delta buckets. The fast reversal of flow-driven implied-volatility moves implies that an implied-volatility jump caused by a burst of option buying is a weak volatility forecast.

## Caveats
In-sample regressions; no out-of-sample test and no trading rule. The sample ends in July 2021, before block trades and institutional flow became as large as they are now. A concern of this note, not raised in the pages read: block trades negotiated off the screen carry an exchange-assigned direction that may not identify the initiator. Coefficient tables beyond those quoted were not read line by line.
