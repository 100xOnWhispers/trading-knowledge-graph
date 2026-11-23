---
title: "The Accuracy of the Tick Rule in the Bitcoin Market"
authors: "Ma, Donglian; Zhai, Pengxiang"
year: 2021
venue: "SAGE Open 11(2)"
url: "https://ideas.repec.org/a/sae/sagope/v11y2021i2p21582440211014504.html"
pdf: "none"
access: "abstract-only"
source_type: "peer-reviewed"
evidence_grade: "B"
topic: "08-trade-flow-toxicity"
asset_class: "crypto"
horizon: "tick"
tags: "trade-classification, tick-rule, bitcoin, bitstamp, order-imbalance, data-quality"
---

## Key insight
When the tick rule is used to infer which side initiated each Bitcoin trade, it is right only about three times in four. On 11.9 million BTC/USD trades from Bitstamp the overall success rate is 76.87%, and the abstract concludes that order imbalances computed with the tick rule are not accurate enough in the Bitcoin market. Inferred trade signs are a materially worse input than exchange-reported aggressor flags.

## Method
Only the abstract (RePEc listing) was read in this session; the publisher's PDF could not be retrieved. From the abstract: the tick rule, which signs a trade as a buy if the price is above the previous trade price and as a sell if below, is evaluated trade by trade, and the accuracy of the resulting order-imbalance measure is assessed. The benchmark is presumably the initiator side recorded in the Bitstamp data, but this, the treatment of zero ticks and the aggregation windows used for imbalance were not confirmed.

## Data and sample
11.9 million Bitcoin/US dollar trades on Bitstamp. The sample period was not stated in the abstract text read.

## Reported results
From the abstract only:
- Overall success rate of the tick rule: 76.87%.
- The tick rule tends to fail when there is a long gap between consecutive trades.
- Order imbalance computed from tick-rule signs lacks sufficient accuracy in the Bitcoin market.

## Signal construction
Not a signal. It is a data-quality rule for every flow feature in this topic. Priority order for signing trades: (1) the exchange's aggressor flag (for example Binance's isBuyerMaker field; the equivalent field on each other venue should be confirmed from its API documentation); (2) candle-level taker-buy volume where trade prints are unavailable; (3) quote-based rules using the prevailing bid and ask; (4) the tick rule on individual prints as a last resort, with trades after long gaps down-weighted or dropped; (5) never bulk classification of time bars when any of the above is available.

## Relevance to SOL perpetuals at minutes to hours
For signals computed on Binance, Bybit, OKX or Hyperliquid SOL perps this is not a constraint, because those feeds report the taker side. It matters for Kalshi itself and for any venue or historical dataset without a side field: a cumulative volume delta built from tick-rule signs on a thin, new market with long gaps between trades would be unreliable by this paper's finding. The 76.87% figure compares with an 88.4% transaction-level tick-rule accuracy for E-mini futures in [andersen-2013-order-flow-toxicity-perfect-classification](andersen-2013-order-flow-toxicity-perfect-classification.md), so the tick rule appears to work worse in crypto than in a deep futures market. Before trusting any Kalshi-native flow feature, check what the Kalshi trade feed publishes and, if it has a side field, measure tick-rule accuracy against it directly.

## Caveats
Abstract-only. One spot exchange; period unknown; Bitstamp's fine tick size and sparse trading may make it a hard case, and accuracy on a busy perpetual with a coarser tick could be higher. The study does not test the quote rule or Lee-Ready, as far as the abstract shows. No open-access PDF was obtained, although SAGE Open is an open-access journal and a copy should be available from the publisher.
