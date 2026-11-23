---
title: "How to measure the liquidity of cryptocurrency markets?"
authors: "Brauneis, Alexander; Mestel, Roland; Riordan, Ryan; Theissen, Erik"
year: 2021
venue: "Journal of Banking and Finance 124, 106041"
url: "https://madoc.bib.uni-mannheim.de/62108/"
pdf: "sources/09-liquidity-price-impact/brauneis-2021-measure-liquidity-cryptocurrency-markets.pdf"
access: "full-text"
source_type: "peer-reviewed"
evidence_grade: "A"
topic: "09-liquidity-price-impact"
asset_class: "crypto"
horizon: "hours"
tags: "liquidity-measurement, bid-ask-spread, corwin-schultz, abdi-ranaldo, amihud, kyle-obizhaeva, roll"
---

## Key insight
The paper runs a horse race between cheap liquidity proxies built from bar data and true liquidity measured from order books on crypto exchanges. The high-low based estimators of Corwin and Schultz and of Abdi and Ranaldo track changes in liquidity over time best. The Amihud ratio and the Kyle-Obizhaeva estimator are best for liquidity levels and for ranking venues. The Amihud ratio fails for time variation because, in crypto, volume and trading costs rise together.

## Method
Benchmarks from order-book snapshots and trades: percentage quoted spread, effective spread, price impact (the signed change in the quote midpoint from the snapshot before a trade to the snapshot after it), and the cost of a round-trip trade through the book. Proxies from open, high, low, close, volume and trade counts: number of transactions, dollar volume, Amihud ratio, Roll estimator (price and return versions), Kyle-Obizhaeva volatility-over-volume index, Corwin-Schultz (CS) and Abdi-Ranaldo (AR). Three setups: 1-minute bars aggregated to hourly, hourly bars to daily, daily bars to 15-day. Evaluation by time-series correlation, quantile dependence, RMSE and MAE for levels, and venue ranking.

## Data and sample
BTC/USD and ETH/USD on Bitfinex, Bitstamp and Coinbase Pro, 16 December 2017 to 16 December 2019. Books hold the 50 best bids and asks. 90.7 million BTC and 53.4 million ETH transactions. About 12,500 hourly, 670 daily and 46 fifteen-day intervals.

## Reported results
- Daily BTC benchmarks: mean quoted spread 0.72 bp on Bitfinex, 6.55 bp on Bitstamp, 0.64 bp on Coinbase Pro; mean round-trip cost 3.8, 13.2 and 3.4 bp.
- At the daily frequency CS has the highest and AR the second-highest time-series correlation with quoted spread, effective spread and round-trip cost (0.54 to 0.75), and 0.86 with price impact.
- Trade count and dollar volume correlate positively with the benchmarks (0.82 and 0.80 with price impact): more activity goes with higher costs.
- The Amihud ratio is virtually uncorrelated with the benchmarks over time.
- For levels, Kyle-Obizhaeva has the lowest errors at daily and 15-day frequencies, with Amihud close. CS, AR and Roll give levels that depend strongly on bar frequency.
- A principal-component composite does not beat the best single proxy.
- Results hold across high and low volatility, volume and return regimes; correlations are lower in the second half of the sample.

## Signal construction
Time-varying liquidity state from 1-minute bars over a rolling hour:
AR_i = sqrt(max(4 * (c_i - m_i) * (c_i - m_(i+1)), 0)), with c the log close and m the average of log high and log low; average over adjacent bars.
Venue ranking and impact level: Kyle_t = (mean squared return / dollar volume)^(1/3), or the Amihud ratio, computed per venue.
Use the first to detect when liquidity is deteriorating, the second to compare Kalshi with the large venues.

## Relevance to SOL perpetuals at minutes to hours
This is the most directly usable crypto evidence on which proxy to trust. It supports computing spread-type proxies from Kalshi's own bars when order-book history is missing. Two things need re-testing: the sample is spot BTC and ETH on three venues in 2018 and 2019, and SOL perps have smaller ticks relative to price and different participants. The positive volume-cost relation also means volume spikes should be read as stress, not as improved liquidity.

## Caveats
Spot only, no perpetuals, no SOL. Order-book snapshots are not continuous and there are data gaps. The proxies measure levels poorly at high frequency. The sample predates the growth of perp-dominated price discovery.
