---
title: "CME CF Cryptocurrency Real Time Indices Methodology Guide (Version 17.0)"
authors: "CF Benchmarks Ltd"
year: 2026
venue: "CF Benchmarks methodology document (version date 21 September 2026)"
url: "https://docs.cfbenchmarks.com/CME%20CF%20Real%20Time%20Indices%20Methodology.pdf"
pdf: "sources/05-price-discovery-cross-venue/cfbenchmarks-2026-cme-cf-real-time-indices-methodology.pdf"
access: "full-text"
source_type: "documentation"
evidence_grade: "B"
topic: "05-price-discovery-cross-venue"
asset_class: "crypto"
horizon: "seconds"
tags: "index-construction, order-book-index, cf-benchmarks, solusd-rti, constituent-exchanges, reference-price, kalshi"
---

## Key insight
The CME CF real-time indices, including the Solana-Dollar index (SOLUSD_RTI), are computed from the consolidated limit order books of a short list of regulated-leaning USD spot exchanges, not from trades and not from any perpetual or offshore USDT market. The index is a depth-weighted mid price. A venue that funds and settles against this index is anchored to US-accessible spot liquidity, which is not where most crypto price discovery happens.

## Method
Calculation steps in the guide: (1) at each Effective Time the relevant order book of every constituent exchange is added to a joint list; (2) books are aggregated into one consolidated book, with any price level's size capped at a dynamic order-size cap, then uncrossed by removing overlapping bid and ask size; (3) cumulative bid, ask, mid price-volume curves and a mid spread-volume curve are computed at a spacing granularity; (4) "utilized depth" is the largest volume for which the spread-volume curve stays within a set percentage deviation from mid; (5) the mid price-volume curve is weighted by the normalized density of an exponential distribution (parameter lambda) up to the utilized depth; (6) the index is the weighted sum. Data hygiene: an exchange whose book is older than the Retrieval Lag Threshold is dropped for that calculation; unparseable or crossed books are flagged erroneous; books whose implied mid deviates from the cross-exchange median by more than a "potentially erroneous data" parameter are dropped.

## Data and sample
Not empirical. For SOLUSD_RTI the parameter table lists calculation every 200 milliseconds, a 10-second retrieval-lag threshold and dynamic spacing; dissemination is described as approximately every second, year-round. The companion document "CME CF Constituent Exchanges" (https://docs.cfbenchmarks.com/CME%20CF%20Constituent%20Exchanges.pdf, opened in this session) lists the SOLUSD_RTI constituents as Coinbase, Kraken, Gemini, LMAX Digital, Bitstamp and Crypto.com.

## Reported results
- CF Benchmarks' index page for SOLUSD_RTI (https://www.cfbenchmarks.com/data/indices/SOLUSD_RTI, opened in this session) describes it as "a once per 200 millisecond benchmark index price" and states it "is the price input for settlement of event contracts and prediction markets offered by Kalshi, and ForecastEX".
- Version history shows the potentially-erroneous-data parameter for the NEAR index was cut from 25% to 10% in June 2026 and spacing was made dynamic for all indices.
- No accuracy or lead-lag statistics are given.

## Signal construction
Reconstruct a proxy index in real time: pull L2 books for SOL-USD from the constituent exchanges, cap level sizes, merge, uncross, and take an exponentially depth-weighted mid. Even a simple size-weighted mid of Coinbase and Kraken top-of-book should track it closely. Features: (a) index proxy minus Binance SOLUSDT perp mid (US spot versus offshore perp gap; needs a USDT/USD adjustment); (b) the index's short-horizon return minus Binance's return, which shows how fast the index catches up; (c) constituent dispersion as a stress flag.

## Relevance to SOL perpetuals at minutes to hours
If the Kalshi SOL perp references SOLUSD_RTI (the filing was not retrieved, so not confirmed), then Kalshi's funding premium is measured against a blend of six USD spot books. The literature in this topic says those venues follow offshore perps, so the index itself lags Binance by some small interval; Kalshi market makers will quote off the faster offshore price while funding accrues against the slower index. The USDT-USD basis becomes a direct input.

## Caveats
Methodology only; parameter values for cap, lambda and deviation were not all extracted here and can change by version (this is v17.0). The claim that the index lags offshore perps is an inference from other notes, not from this document. CF Benchmarks is owned by Kraken's parent, which is also a constituent.
