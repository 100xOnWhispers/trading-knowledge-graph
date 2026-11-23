---
title: "Price clustering in Bitcoin"
authors: "Urquhart, Andrew"
year: 2017
venue: "Economics Letters, 159, pp. 145-148"
url: "https://ideas.repec.org/a/eee/ecolet/v159y2017icp145-148.html"
pdf: "none"
access: "abstract-only"
source_type: "peer-reviewed"
evidence_grade: "B"
topic: "17-auction-orderflow-practitioner"
asset_class: "crypto"
horizon: "n/a"
tags: "price-clustering, round-numbers, bitcoin, negotiation-hypothesis, psychological-barriers"
---

## Key insight
Bitcoin prices cluster at round numbers, as equity and FX prices do, but the abstract reports no significant pattern in returns after a round number is reached. Clustering is therefore evidence about how participants choose prices, not evidence that round numbers are tradable turning points. This is the main crypto-specific check on the round-number support and resistance claim, and it comes out negative for predictability.

## Method
Only the abstract (RePEc record) was read. It states that the paper studies clustering of Bitcoin prices at round numbers, examines returns following round numbers, and relates clustering to price and volume. The exact clustering statistic, the definition of a round number, the return horizon and the test design were not visible. I graded the note B: peer-reviewed, but read at abstract level only.

## Data and sample
Not confirmed. The abstract does not state the exchange, the period or the sampling frequency, so the horizon field is set to "n/a".

## Reported results
From the abstract only:
- Significant evidence of clustering at round numbers, with over 10% of prices ending in 00 decimals.
- No significant pattern of returns after the round number.
- Price and volume have a significant positive relationship with clustering at whole numbers, which the author reads as support for Harris's (1991) negotiation hypothesis. Harris's abstract (also read on RePEc) says clustering is pervasive in stock prices, increases with price level and volatility, and decreases with capitalization and trading frequency, because traders use a coarse price grid to simplify negotiation.

## Signal construction
Clustering itself is not a directional signal. It defines where to look. Measure for the instrument at hand: the frequency of trade prices and of resting order prices by final digits (for SOL, cents within the dollar and whole-dollar multiples), compared with a uniform benchmark. The resulting "roundness weight" of each price can scale other level features, for example the bounce and cross events of the Osler notes. A direct test of the abstract's negative result at intraday horizon is: conditional on first touch of a round price, compare the forward 5, 15 and 60 minute return distribution with matched non-round prices.

## Relevance to SOL perpetuals at minutes to hours
Two points transfer. First, round-number clustering almost certainly exists in SOL prices and order placement, and it is cheap to measure on Binance and Kalshi data. Second, the absence of a return pattern in Bitcoin warns against assuming that the FX results of Osler carry over. The two findings are not strictly in conflict: Osler measures minute-level conditional behaviour against placebo levels, while this abstract speaks of returns after round numbers without stating horizon. The intraday question on crypto remains open in the sources I could read.

## Caveats
Abstract-only. Published in 2017, so the sample ends no later than that year, before perpetual futures became the main price-discovery instruments. Clustering in decimals of a dollar price may not correspond to the round levels traders watch (hundreds or thousands of dollars). Follow-up papers on day-of-week and futures-introduction effects were seen in search results but not opened.
