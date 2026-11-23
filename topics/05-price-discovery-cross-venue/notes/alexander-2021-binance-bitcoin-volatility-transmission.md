---
title: "The Role of Binance in Bitcoin Volatility Transmission"
authors: "Alexander, Carol; Heck, Daniel F.; Kaeck, Andreas"
year: 2021
venue: "arXiv preprint 2107.00298 (v3, August 2021)"
url: "https://arxiv.org/pdf/2107.00298"
pdf: "sources/05-price-discovery-cross-venue/alexander-2021-binance-bitcoin-volatility-transmission.pdf"
access: "full-text"
source_type: "working-paper"
evidence_grade: "B"
topic: "05-price-discovery-cross-venue"
asset_class: "crypto"
horizon: "minutes"
tags: "volatility-spillover, binance, perpetual, usdt-margined, coinbase, bybit, intraday, logmem"
---

## Key insight
Among the main bitcoin spot and perpetual instruments, the tether-margined perpetual on Binance is the dominant source of volatility: it transmits strongly to every other instrument and receives almost nothing back. Volume flows behave differently, originating mainly from spot, especially Coinbase. Spillovers are strongest when European and US markets are open.

## Method
Second-by-second trade data are turned into 5-minute realised volatility with a pre-averaging estimator (intervals with too few active seconds are set to zero volatility). Spillovers are estimated with univariate and multivariate Logarithmic Multiplicative Error Models (LogMEM), first within instrument groups and then jointly across the most important instruments; insignificant parameters are set to zero. The same model is re-run on 5-minute volume, and the day is split into Asian, European and US sessions.

## Data and sample
January 1 to March 31, 2021. USD spot on Coinbase, Bitstamp, Kraken; USDT spot on Binance and Huobi; perpetuals: Binance USDT-margined, Binance USD (inverse), Bybit USD. Futures are excluded.

## Reported results
- The Binance USDT perpetual sends "strong, positive volatility spillovers to all other instruments" and receives only weak (negative) flows from Binance spot, less from Coinbase and nothing significant from others.
- Bybit and Huobi are receivers of volatility, not transmitters.
- Total spillover is about 30% higher during European and US trading hours than during Asian hours.
- Volume flows run mainly from spot (Coinbase, Binance spot) and the Bybit perpetual, with negligible volume outflow from the Binance USDT perpetual; Coinbase is the main source of volume transmission.
- An increase in volatility is preceded by an increase in volume in the previous 5-minute interval, with the relation reversing in the following interval.
- Activity: Coinbase trades in 84% of one-second intervals; the USDT instruments in more than 95%; Bitstamp and Kraken in about one second in four.

## Signal construction
Volatility-regime input, not a direction signal. Compute 5-minute realised volatility of the Binance SOLUSDT perpetual (pre-averaged from 1-second returns) and use its change as a leading indicator of volatility on the target venue: widen stops, shrink size, or expect larger follow-through on Kalshi in the next 5 to 15 minutes. A second feature is the session flag (Asia, Europe, US), since transmission strength is session-dependent.

## Relevance to SOL perpetuals at minutes to hours
The hierarchy (Binance USDT perp as source, smaller perp venues as receivers) is the default prior for SOL. A small US venue should behave like Bybit and Huobi in this study or weaker: a pure receiver. The US-hours amplification matters because Kalshi's user base is American; the lag between Binance volatility and Kalshi volatility may be shortest when US market makers are active and longest overnight US time.

## Caveats
Three months in a strong bull market, bitcoin only, pre-FTX-collapse and pre-Hyperliquid. Volatility transmission is not the same as price leadership. In-sample model fit with no trading test. The authors' policy discussion of tether is outside the evidence.
