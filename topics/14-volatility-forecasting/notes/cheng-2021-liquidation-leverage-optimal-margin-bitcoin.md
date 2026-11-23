---
title: "Liquidation, Leverage and Optimal Margin in Bitcoin Futures Markets"
authors: "Cheng, Zhiyong; Deng, Jun; Wang, Tianyi; Yu, Mei"
year: 2021
venue: "arXiv preprint 2102.04591 (later in Applied Economics 53(47), 5415-5428)"
url: "https://arxiv.org/pdf/2102.04591"
pdf: "sources/14-volatility-forecasting/cheng-2021-liquidation-leverage-optimal-margin-bitcoin.pdf"
access: "full-text"
source_type: "working-paper"
evidence_grade: "B"
topic: "14-volatility-forecasting"
asset_class: "crypto"
horizon: "hours"
tags: "liquidation, leverage, margin, extreme-value-theory, perpetual-futures, bitmex, tail-risk"
---

## Key insight
How much leverage is survivable on a Bitcoin perpetual is a tail question, and the tail is far heavier than a normal distribution implies. Using extreme value theory on BitMEX perpetual prices, a 1% daily chance of a margin call requires roughly 33% margin for longs (3x leverage) and 20% for shorts (5x). Normal-distribution estimates understate the required margin by at least half. Traders who were actually liquidated ran about 60x.

## Method
The sample is cut into non-overlapping blocks (8, 24 or 48 hours, matched to 5-, 30- and 60-minute sampling); the block maximum and minimum price changes are fitted with the generalized extreme value (GEV) distribution, separately for the left tail (which hurts longs) and the right tail (which hurts shorts). The margin M that keeps the probability of an adverse move beyond M within a block at a chosen level p is obtained in closed form from the fitted GEV parameters. The 8-hour block is chosen because funding is charged every 8 hours. Normal-distribution margins are computed for comparison. A second part uses daily liquidation volumes, open interest and OHLC data to estimate the share of positions liquidated and the implied leverage of liquidated traders.

## Data and sample
BitMEX XBTUSD perpetual: 5-minute prices, 431,346 observations, 1 January 2017 to 6 February 2021. Daily forced-liquidation data from Coinalyze, 29 January 2020 to 3 February 2021 (372 days).

## Reported results
- Perpetual futures, 8-hour holding period: required margin rises from 7.26% (short) and 8.36% (long) at p = 0.1 to 26.34% (short) and 46.98% (long) at p = 0.001. A common two-sided margin at p = 0.001 is 34.81%.
- The abstract's headline: 33% for longs and 20% for shorts for a 1% daily margin-call probability.
- The left tail is heavier than the right for perpetuals, so longs need more margin; the daily left-tail parameter is more than double the right.
- Normality understates optimal margins by at least half.
- Daily forced liquidations averaged 3.51% of open interest for longs and 1.89% for shorts (medians 1.22% and 0.86%); estimated leverage of liquidated traders averaged about 58x to 60x.
- On 12 March 2020 long liquidations on BitMEX reached 843 million USD.

## Signal construction
A leverage constraint, not a signal. For the reference instrument: (1) take a long history of 5-minute returns on a liquid SOL perp; (2) for the intended holding period h (for example 1, 4 or 8 hours), collect the worst adverse excursion in each non-overlapping block of length h; (3) fit a GEV (or use the empirical quantile if the history is long) and compute the move M_p that is exceeded with probability p; (4) require that the liquidation distance implied by the chosen leverage and the maintenance margin exceeds M_p. Do this separately for longs and shorts, and refresh monthly.

## Relevance to SOL perpetuals at minutes to hours
Directly applicable in method. The numbers are for Bitcoin; SOL is considerably more volatile, so the survivable leverage at a given p will be lower. The estimates imply that Kalshi's low maximum leverage is roughly what tail analysis recommends, so the leverage cap may bind less often than a volatility-targeting rule would on an offshore venue. Stops placed well inside the liquidation distance change the calculation from "probability of liquidation" to "probability and cost of gapping through the stop", which this paper does not address.

## Caveats
Sample includes March 2020, which dominates the left tail. Unconditional tails: no adjustment for the current volatility regime, so the margin is too high in calm periods and too low in stressed ones. Leverage of liquidated traders is inferred from daily ranges, not account data. Version read is the arXiv preprint; journal details came from a search listing.
