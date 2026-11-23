---
title: "Order flow analysis of cryptocurrency markets"
authors: "Silantyev, Eduard"
year: 2019
venue: "Digital Finance 1(1), 191-218"
url: "https://ideas.repec.org/a/spr/digfin/v1y2019i1d10.1007_s42521-019-00007-w.html"
pdf: "none"
access: "abstract-only"
source_type: "peer-reviewed"
evidence_grade: "B"
topic: "07-order-book-imbalance"
asset_class: "crypto"
horizon: "seconds"
tags: "order-flow-imbalance, trade-flow-imbalance, bitmex, xbtusd, perpetual, depth, price-impact"
---

## Key insight
The first peer-reviewed replication of the Cont, Kukanov and Stoikov OFI regression on a crypto perpetual reaches a different ranking from equities: on BitMEX XBTUSD, trade flow imbalance explains contemporaneous price changes better than order flow imbalance. OFI still has a strong linear relation with price change once the interval is long enough. The author attributes the difference to shallow depth and slow book update rates in crypto markets at the time.

## Method
Abstract only. The paper applies order flow analysis, which measures the effect of individual order book events on subsequent price changes, to trade and quote data. It compares an aggregate order flow imbalance measure (quotes and trades at the best levels) with trade flow imbalance (signed trade volume) as explanatory variables for contemporaneous price change. Regression specification, interval lengths and R2 values were not available in the material read.

## Data and sample
BitMEX XBTUSD perpetual contract trade and quote data. The abstract describes BitMEX as the largest crypto exchange by traded volume at the time. Sample dates were not stated in the abstract.

## Reported results
From the abstract only:
- Trade flow imbalance is better at explaining contemporaneous price changes than aggregate order flow imbalance.
- Over sufficiently long intervals, contemporaneous price changes have a strong linear relationship with order flow imbalance.
- Lack of depth and low update arrival rates are identified as the main features distinguishing crypto market microstructure from established markets.

## Signal construction
Inputs: L1 quote updates and the trade tape for the perpetual. Compute, over the same window, (a) OFI as in the Cont et al. note and (b) trade flow imbalance as signed taker volume (buy minus sell). Regress the contemporaneous mid-price change on each and track which has the higher rolling R2. The ratio of the two R2 values is itself a diagnostic of how much of price formation on a venue happens through trades versus quote revisions.

## Relevance to SOL perpetuals at minutes to hours
This is the most direct warning against importing equity results unchanged. Which measure dominates depends on venue microstructure: a thin book with infrequent quote updates (2018 to 2019 BitMEX, and plausibly Kalshi in its first year) is moved by trades, whereas a deep, fast-quoting book (Binance SOL perp today) should look more like the equity case. The bot should compute both measures per venue and let the data choose, and should treat Kalshi-native book imbalance with caution until its update rate and depth are measured. Trade-flow signals themselves belong to topic 08.

## Caveats
Abstract-only access: no numbers, dates or specifications were verified. One contract on one exchange; contract specifications (margining, tick size) were not described in the abstract and should be checked before comparing with linear USDT-margined perps. The crypto market structure of 2019 differs greatly from 2026: market-maker participation, quote update rates and depth have all increased. Contemporaneous explanation, not forecasting.
