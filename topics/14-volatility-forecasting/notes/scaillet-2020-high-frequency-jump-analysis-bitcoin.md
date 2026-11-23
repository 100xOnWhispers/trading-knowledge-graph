---
title: "High-Frequency Jump Analysis of the Bitcoin Market"
authors: "Scaillet, Olivier; Treccani, Adrien; Trevisan, Christopher"
year: 2020
venue: "Journal of Financial Econometrics 18(2), 209-232 (read as arXiv 1704.08175v2, June 2017)"
url: "https://arxiv.org/pdf/1704.08175"
pdf: "sources/14-volatility-forecasting/scaillet-2020-high-frequency-jump-analysis-bitcoin.pdf"
access: "full-text"
source_type: "peer-reviewed"
evidence_grade: "B"
topic: "14-volatility-forecasting"
asset_class: "crypto"
horizon: "minutes"
tags: "jumps, jump-detection, lee-mykland, order-flow-imbalance, spread, clustering, mt-gox"
---

## Key insight
In an early, retail-dominated Bitcoin market, price jumps are frequent (about one jump day a week), cluster in time, and are more often up than down. Jumps are preceded by measurable changes in liquidity and order flow: larger absolute order-flow imbalance, more aggressive traders and a wider bid-ask spread. After a jump, volume and volatility stay elevated for up to an hour while the price change itself persists.

## Method
Jump detection uses the Lee and Mykland (2012) test, which is robust to microstructure noise through pre-averaging, applied to tick data, with false-discovery-rate control at 10% across days. Jump clustering is tested with a runs test. A probit model on 5-minute (and longer) intervals regresses a jump indicator on lagged covariates: absolute order-flow imbalance, a "whale" concentration index built from trader identifiers, the share of aggressive traders, bid-ask spread and microstructure-noise variance. Post-jump effects are measured by comparing statistics in successive 15-minute spans with a pre-jump reference level.

## Data and sample
Leaked Mt. Gox internal database: all BTC/USD trades with trader identifiers, 26 June 2011 to 29 November 2013 (888 days).

## Reported results
- 124 jump days out of 888. Of the detected jumps, 70 are positive and 54 negative; mean size +4.65% and -4.14%; the largest move is 32% within five minutes.
- FDR control discards about 35% of raw rejections, versus up to 95% in a cited study of Dow Jones stocks; a fixed 1% level produces many spurious detections.
- Jump days come in runs, inconsistent with independent Poisson arrivals.
- Illiquidity, order-flow imbalance and the preponderance of aggressive traders are significant predictors of jump occurrence.
- After a jump, realized variance, noise variance, volume, trader count and spread are significantly elevated in the first 15 minutes (realized variance t-statistic 11.2) and decay to insignificance within about an hour. The price level change is persistent.

## Signal construction
Two uses. (1) Jump-risk state: over a short trailing window compute absolute signed-volume imbalance, the share of volume from aggressive (taker) orders and the quoted spread; a rise in all three raises the probability of a jump in the next interval, which argues for smaller size or wider stops, not for a direction. (2) Post-jump regime: after a detected jump (a return exceeding a multiple of local bipower volatility), assume elevated volatility and wider spreads for roughly the next hour and do not assume the move reverts.

## Relevance to SOL perpetuals at minutes to hours
The qualitative results are plausible for SOL, which is thinner and more retail-driven than BTC and subject to liquidation cascades. The probit covariates can be computed from Binance or Bybit trades and top-of-book quotes; the whale index cannot, because trader identifiers are unavailable (Hyperliquid's public address-level data is the nearest analogue). All coefficients and the one-hour decay time need re-estimating on modern data.

## Caveats
Single defunct exchange, 2011 to 2013, with tiny volumes by today's standards and known manipulation and outage episodes. The test identifies at most the largest jump per day. The predictive probit is in-sample; no trading rule or cost analysis is given. Symmetry of up and down jumps may not hold in a perpetual-futures market with leveraged longs.
