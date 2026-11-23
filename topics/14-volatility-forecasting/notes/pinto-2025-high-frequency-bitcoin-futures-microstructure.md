---
title: "High-frequency dynamics of Bitcoin futures: An examination of market microstructure"
authors: "Pinto, Mateus Gonzalez de Freitas"
year: 2025
venue: "Borsa Istanbul Review 25, 1378-1390"
url: "https://repositorio.usp.br/bitstreams/5533bba1-e96a-453c-bf72-aa7053b2d284"
pdf: "sources/14-volatility-forecasting/pinto-2025-high-frequency-bitcoin-futures-microstructure.pdf"
access: "full-text"
source_type: "peer-reviewed"
evidence_grade: "B"
topic: "14-volatility-forecasting"
asset_class: "crypto"
horizon: "minutes"
tags: "volume-volatility, mixture-of-distributions, trading-invariance, trade-size, perpetual-futures, binance, intraday-pattern"
---

## Key insight
On Binance BTC and ETH perpetual futures, intervals with larger average trade size have higher return variance per trade. That positive relation supports the mixture-of-distributions hypothesis (volatility, volume and trade size all rise with information flow) and rejects the intraday trading invariance hypothesis, which predicts a slope of minus two. Trading activity also follows a persistent intraday cycle tied to the Asia, Europe and Americas sessions.

## Method
All trades are aggregated to 1, 5, 10, 15, 30 and 60 minutes and daily. For each interval the author computes log volume v, log number of trades n, log average trade size q and log return variance s. The test regression is

s_t - n_t = c + beta * q_t + u_t,

where generalized MDH implies beta of zero or more and the invariance hypothesis requires beta = -2. The paper also describes stylised facts by year and by session: Asia 19:00 to 02:00, Europe 02:00 to 08:30, Americas 08:30 to 15:15 and a "transition zone" 15:15 to 19:00, all in US Central time.

## Data and sample
Tick-level trades of BTC and ETH perpetual futures on Binance, January 2020 to December 2024.

## Reported results
- For BTC, the estimated slope on log trade size is about 2.6 to 2.9 from daily down to 5-minute aggregation and about 2.3 at 1 minute, with R-squared near 0.5 except at 1 minute (about 0.17), as read from the paper's Table 1. ETH slopes are similar (about 2.3 to 2.8). The slope is positive and far from -2 at every aggregation level.
- Number of trades and volume are U-shaped across the day, peaking in the Americas session and around session transitions; the transition zone has the lowest volume and volatility.
- Average trade size has trended down over 2020 to 2024 while trade counts have risen; return variance has declined, which the author reads as market maturation.
- The author notes 1-minute data may be too noisy for the test.

## Signal construction
Feature for a volatility model, not a directional signal: over the trailing interval compute N (trade count), V (volume) and Q = V / N (average trade size). Expected variance scales with N and, conditional on N, rises steeply with Q. A simple nowcast is log variance = c + n + beta * q with beta estimated on rolling data. A jump in average trade size at a given trade count flags information-driven flow and higher volatility.

## Relevance to SOL perpetuals at minutes to hours
Directly on point for instrument type and venue: perpetuals on the largest exchange, through 2024. It supports using trade count and trade size from Binance as real-time volatility inputs for SOL, and it gives a session map for expected activity. SOL itself is not in the sample; the slope and the session boundaries need re-estimation, and the relation is contemporaneous, so its forecasting value depends on the persistence of trade size and count.

## Caveats
Contemporaneous regressions, not forecasts; no out-of-sample test. Single author, single venue. Trade size on Binance is affected by order-splitting algorithms and contract tick-size changes, which may drive the downward trend. Coefficients above were read from a table whose text extraction was imperfect; verify against the PDF before relying on exact values.
