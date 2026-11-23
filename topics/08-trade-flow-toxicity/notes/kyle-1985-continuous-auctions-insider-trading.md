---
title: "Continuous Auctions and Insider Trading"
authors: "Kyle, Albert S."
year: 1985
venue: "Econometrica 53(6), 1315-1336"
url: "https://www.econometricsociety.org/publications/econometrica/1985/11/01/continuous-auctions-and-insider-trading"
pdf: "none"
access: "abstract-only"
source_type: "peer-reviewed"
evidence_grade: "B"
topic: "08-trade-flow-toxicity"
asset_class: "multi"
horizon: "n/a"
tags: "kyle-lambda, informed-trading, signed-volume, market-depth, theory"
---

## Key insight
The abstract describes a dynamic model of insider trading with sequential auctions in which one risk-neutral insider, random noise traders and competitive risk-neutral market makers interact. The insider trades gradually so that noise trading camouflages him, and prices incorporate his information over time. In the continuous-time limit prices follow Brownian motion, market depth is constant, and all private information is in the price by the end of trading. This is the theoretical origin of "Kyle's lambda": price change per unit of net signed order flow.

## Method
Theory only. Only the abstract was read in this session (the Econometric Society page; full text is behind a login), so the derivation is not reproduced here. From the abstract: a sequential-auction model "structured to resemble a sequential equilibrium", solved for the informational content of prices, the liquidity of the market, and the value of private information to the insider. The standard textbook statement of the result, which is not in the abstract and was not confirmed against the paper in this session, is that market makers set price as a linear function of net order flow, delta_p = lambda * (signed volume), with lambda rising in the ratio of information variance to noise-trade variance.

## Data and sample
None. Pure theory.

## Reported results
From the abstract only: (1) the insider exploits monopoly power over time, with noise trading providing camouflage; (2) as the interval between auctions goes to zero, prices follow Brownian motion; (3) market depth is constant over time in that limit; (4) all private information is incorporated into prices by the end of trading.

## Signal construction
Not a signal by itself. It is the justification for the empirical "Kyle lambda" feature used elsewhere in this topic. The version used in [easley-2024-microstructure-dynamics-crypto-markets](easley-2024-microstructure-dynamics-crypto-markets.md) is lambda_t = (p_t - p_{t-W}) / sum_{i=t-W..t} b_i V_i over a rolling window of W bars, with b_i the sign of the bar's price change and V_i dollar volume. With exchange aggressor flags, b_i V_i can be replaced by true signed taker volume. A regression slope of bar returns on signed volume over a rolling window is the other common estimator. Lambda is a liquidity and adverse-selection state variable, not a direction forecast: a high lambda means a given flow imbalance moves price more.

## Relevance to SOL perpetuals at minutes to hours
The useful ideas are (a) signed flow, not gross volume, is what moves price, and (b) informed traders split orders, which is why signed flow is persistent (see [lillo-2004-long-memory-efficient-market](lillo-2004-long-memory-efficient-market.md)). A rolling lambda estimated on Binance or Bybit SOL perp trades can scale how much weight a flow-imbalance signal deserves and can serve as a risk input. The linear, constant-depth result should not be taken literally: the empirical impact literature (topic 09) finds concave impact, and [easley-2024-microstructure-dynamics-crypto-markets](easley-2024-microstructure-dynamics-crypto-markets.md) found Kyle lambda added little predictive power in crypto once Roll and VPIN were included.

## Caveats
Abstract-only access; no open copy was downloaded (the scanned copies found online carry JSTOR copyright stamps and were not used). The model has a single insider, normally distributed values and a batch auction, none of which matches a 24-hour limit order book with many informed parties, liquidations and cross-venue arbitrage. Empirical lambda estimators are noisy at short windows and mechanically correlated with volatility.
