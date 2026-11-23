---
title: "Towards Understanding Cryptocurrency Derivatives: A Case Study of BitMEX"
authors: "Soska, Kyle; Dong, Jin-Dong; Khodaverdian, Alex; Zetlin-Jones, Ariel; Routledge, Bryan; Christin, Nicolas"
year: 2021
venue: "Proceedings of the Web Conference 2021 (WWW '21)"
url: "https://www.andrew.cmu.edu/user/nicolasc/publications/Soska-WWW21.pdf"
pdf: "sources/04-open-interest-liquidations/soska-2021-cryptocurrency-derivatives-bitmex-case-study.pdf"
access: "full-text"
source_type: "peer-reviewed"
evidence_grade: "B"
topic: "04-open-interest-liquidations"
asset_class: "crypto"
horizon: "daily"
tags: "liquidations, bitmex, leverage, long-short-asymmetry, position-size, descriptive"
---

## Key insight
The first large measurement study of liquidations on a crypto derivatives venue, built from position-level liquidation events. Liquidations are dominated by the long side regardless of instrument, position size or even price trend, and a disproportionate share of liquidated value comes from smaller positions. The authors link liquidation clusters to the abrupt step-like bitcoin moves of 2018 but state that causality is not established.

## Method
A descriptive measurement study. The authors collect every liquidation announced by BitMEX's public "REKT" bot and API feed (instrument, size, direction, engine takeover price, timestamp), combine it with on-chain deposit and withdrawal forensics and chat logs, and tabulate liquidations over time, by instrument, by position size (USD 50,000 buckets), and against weekly price range. For the price-range analysis, history is split into 168-hour windows and liquidated value is regressed linearly on the signed maximum-minus-minimum price move within the window.

## Data and sample
BitMEX, all instruments, with liquidation analysis from January 2017 to about September 2020 (figure through February 2021). Over 425,000 liquidation events on 205 instruments, totalling USD 60 billion. The feed was disabled between November 2020 and January 2021 after the authors contacted the exchange.

## Reported results
- Daily liquidations rose with volume in 2018 and spiked with volatility, reaching as much as USD 1 billion in a single week in November 2018. Most of 2018 saw liquidation events above USD 100 million every few weeks, coinciding with discrete price jumps.
- Long liquidations regularly exceed short liquidations, including during an uptrend (July 2019). Notable short-side exceptions: 1 April 2019, when a 25% spot rise liquidated over USD 400 million of shorts, and 24 to 25 October 2019.
- Half of long liquidation value comes from positions of USD 1.6 million or less; half of short liquidation value from positions of USD 950,000 or less.
- Long liquidation volume rises with weekly price range even when the week's move is upward; the regression slopes for shorts are flatter than for longs.
- Liquidations as a share of traded volume are higher for settled futures than for perpetual swaps in every asset group; the readable table rows show 2.64% for settled Ethereum and 2.13% for settled altcoins against 1.23% for perpetual altcoins.
- Citing a BitMEX blog post, weighted average effective leverage on XBTUSD was about 20 to 35x between May 2018 and April 2019.

## Signal construction
Not a tested signal. It supports three features: signed liquidation flow (long minus short liquidated notional per interval), liquidation value normalized by traded volume as a riskiness gauge, and the prior that long-side forced flow is the larger and more frequent tail.

## Relevance to SOL perpetuals at minutes to hours
The structural facts are likely to persist: retail longs carry more leverage, so downside cascades are larger and more frequent than short squeezes, and volatility in either direction liquidates longs because high-leverage longs are stopped out by intraday dips inside an uptrend. For a directional SOL bot this argues for asymmetric treatment of long and short liquidation signals. The numbers themselves are dated: BitMEX is no longer the dominant venue, contracts were mostly inverse, and SOL did not trade there in the sample.

## Caveats
Single venue, descriptive, weekly aggregation for the only regression. Liquidation data came from a feed the exchange controlled and briefly switched off. BitMEX disputed unspecified statements in the paper. No test of whether liquidations predict subsequent returns.
