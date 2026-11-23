---
title: "Price discovery in Bitcoin: The impact of unregulated markets"
authors: "Alexander, Carol; Heck, Daniel F."
year: 2020
venue: "Journal of Financial Stability"
url: "https://api.figshare.com/v2/articles/23308262"
pdf: "none"
access: "abstract-only"
source_type: "peer-reviewed"
evidence_grade: "B"
topic: "05-price-discovery-cross-venue"
asset_class: "crypto"
horizon: "minutes"
tags: "price-discovery, perpetual-swaps, futures, bitmex, huobi, okex, cme, spot, regulation"
---

## Key insight
Per the abstract: at the minute level, perpetual swaps and futures on unregulated offshore exchanges (Huobi, OKEx, BitMEX) are by far the strongest instruments for bitcoin price discovery. Regulated CME futures and US-based spot exchanges react to those prices rather than lead them, and may do so relatively slowly.

## Method
Only the abstract and repository record were read. The abstract describes an analysis of "minute-level multi-dimensional information flows within and between bitcoin spot and derivatives", and an examination of "potential determinants of their leadership strength". The specific estimators (information share, component share, VECM specification) are not confirmed from the text I read.

## Data and sample
Minute-level bitcoin spot, futures and perpetual prices. Venues named in the abstract: Huobi, OKEx, BitMEX (unregulated derivatives), CME (regulated futures), and the spot exchanges Bitfinex, Bitstamp and Coinbase. Sample period: not confirmed.

## Reported results
From the abstract only:
- Perpetual swaps and futures on Huobi, OKEx and BitMEX are "much the strongest instruments for bitcoin price discovery".
- Prices on CME futures and US-based spot exchanges "react to, rather than lead, price movements on the unregulated exchanges and they may do so relatively slowly".
- In a multi-dimensional setting with the main leaders from futures, perpetuals and spot, "the CME futures have a very minor effect on price discovery, even less than the spot exchanges Bitfinex, Bitstamp and Coinbase".
- The authors tie this to inconsistent regulation, insufficient price stability and weak resistance to manipulation.
No numerical shares were available in what I read.

## Signal construction
Not a signal in itself. It tells the bot where to look: compute order-flow, momentum and liquidation features on the dominant offshore perpetuals rather than on the regulated US venue the bot trades. A concrete derived feature is the short-horizon return of the leading offshore perp minus the return of the regulated venue over the same window (the "catch-up gap").

## Relevance to SOL perpetuals at minutes to hours
This is the closest historical analogue to Kalshi: a CFTC-regulated venue (CME) listing a product while offshore leveraged perps dominated. The finding that the regulated venue followed, slowly, supports the working assumption that Kalshi's SOL perp will be a price taker relative to Binance, Bybit, OKX and Hyperliquid. What needs re-testing: the offshore leaders have changed (Binance and Hyperliquid now, not BitMEX and Huobi), CME has grown, and US spot ETFs have shifted some discovery to US hours.

## Caveats
Abstract-only: the open-access accepted manuscript exists in the University of Sussex repository (CC BY-NC-ND) but the file download was blocked in this session, so numbers, sample dates and methods are unverified here. The record lists the journal as Journal of Financial Stability, volume 50, article 100776. Evidence grade reflects that I could not check robustness, not the journal's standing. Leadership metrics of the IS/CS family conflate speed with low noise (see the Putnins note).
