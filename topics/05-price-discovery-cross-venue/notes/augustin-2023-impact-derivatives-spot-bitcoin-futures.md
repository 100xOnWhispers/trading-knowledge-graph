---
title: "The impact of derivatives on spot markets: Evidence from the introduction of bitcoin futures contracts"
authors: "Augustin, Patrick; Rubtsov, Alexey; Shin, Donghwa"
year: 2023
venue: "Management Science (read as LawFin Working Paper No. 41, Goethe University Frankfurt, 2022)"
url: "https://econpapers.repec.org/paper/zbwlawfin/41.htm"
pdf: "none"
access: "abstract-only"
source_type: "working-paper"
evidence_grade: "B"
topic: "05-price-discovery-cross-venue"
asset_class: "crypto"
horizon: "daily"
tags: "futures-introduction, cross-exchange, price-synchronicity, arbitrage, difference-in-differences, market-quality"
---

## Key insight
Per the abstract: the selective introduction of BTC-USD futures in December 2017 made bitcoin spot prices across exchanges more synchronized. Relative to other bitcoin-fiat pairs, BTC-USD saw higher cross-exchange price correlations, fewer arbitrage opportunities and lower volatility, along with better price efficiency, market quality and liquidity. A regulated derivative can integrate fragmented spot venues.

## Method
Only the abstract was read. The identification uses the fact that futures were introduced only for bitcoin against the US dollar, so BTC-USD is the treated pair and other exchange-rate pairs are controls. The abstract describes this as finding "a significantly greater increase in cross-exchange price synchronicity for BTC-USD relative to other exchange rate pairs". Regression specifications and event windows are not confirmed.

## Data and sample
Bitcoin spot prices across multiple exchanges and fiat pairs around December 2017. Exchanges, data vendor and exact window: not confirmed.

## Reported results
From the abstract only:
- Greater increase in cross-exchange price synchronicity for BTC-USD than for other pairs, "as demonstrated by an increase in price correlations and a reduction in arbitrage opportunities and volatility".
- "Support for an increase in price efficiency, market quality, and liquidity."
- Mechanism: futures "allowed investors to circumvent trading frictions associated with short sale constraints, arbitrage risk associated with block confirmation time, and market segmentation".
No effect sizes were available in what I read. The published version is Management Science 69(11), 6752-6776 (2023), per the RePEc listing returned by search; I did not open the published article.

## Signal construction
Not a signal. It is context for how a new derivative venue changes cross-venue dynamics: after listing, deviations between spot venues shrink and correlations rise.

## Relevance to SOL perpetuals at minutes to hours
The relevance is indirect but useful for expectations. If onshore perps (Kalshi, and other CFTC venues) give US participants a cheap way to short and to arbitrage without moving coins, deviations between US spot venues and offshore prices should narrow over time, and any Kalshi-versus-offshore lead-lag edge should decay as the venue matures. That argues for measuring the Kalshi lag and basis continuously from launch and treating early estimates as an upper bound on future opportunity.

## Caveats
Abstract-only: both open repositories hosting the working paper returned bot-protection pages in this session. The study concerns dated futures and spot-to-spot synchronicity in 2017-2018, not perpetuals. It does not say which market leads. Makarov and Schoar (2020) document that large cross-country deviations still existed in the weeks after the futures launch, so the improvement is relative, not absolute.
