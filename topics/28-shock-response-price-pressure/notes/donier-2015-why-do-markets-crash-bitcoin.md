---
title: "Why Do Markets Crash? Bitcoin Data Offers Unprecedented Insights"
authors: "Donier, Jonathan; Bouchaud, Jean-Philippe"
year: 2015
venue: "arXiv:1503.06704v2 (14 October 2015); journal publication not confirmed in this session"
url: "https://arxiv.org/pdf/1503.06704"
pdf: "sources/28-shock-response-price-pressure/donier-2015-why-do-markets-crash-bitcoin.pdf"
access: "full-text"
source_type: "working-paper"
evidence_grade: "B"
topic: "28-shock-response-price-pressure"
asset_class: "crypto"
horizon: "hours"
tags: "crash-amplitude, liquidity, order-flow-imbalance, square-root-impact, depth, mtgox"
---

## Key insight
The size of a crash is set by the ratio of the sell imbalance to the liquidity available on the buy side, not by the imbalance alone. On Mt. Gox, the net selling on 10 April 2013 was unremarkable in bitcoin terms, yet price fell by more than half because buy-side depth had not kept pace with the price rise. Three liquidity measures, one of them built only from daily volume and volatility, agree closely and predict the amplitude of the largest drops. Timing is not predicted.

## Method
Aggressive order-flow imbalance is the signed sum of market-order volume over 4-hour windows, in BTC and in USD. Three liquidity definitions are compared. (1) Order-book liquidity `L_OB(phi)`: the volume resting between the current price and a price `phi` percent away. (2) Impact liquidity `L_I(phi)`: the meta-order size that moves price by `phi` on average, from measured impact. (3) Theoretical liquidity from the square-root law, `I(Q) = Y * sigma_d * sqrt(Q / V_d)`, which makes `sigma_d / sqrt(V_d)` the illiquidity measure. The expected drop for a sell-off of size `Q` is the inverse liquidity function evaluated at `Q`.

## Data and sample
Mt. Gox BTC/USD trade-by-trade data and full order-book data, December 2011 to January 2014. Mt. Gox held over 80% of BTC/USD spot volume at the time. Liquidity comparison over November 2012 to November 2013.

## Reported results
- On 10 April 2013 the price fell by more than 50% within a few hours. The 4-hour sell imbalance was of order 30,000 BTC, not exceptional in BTC but an outlier in USD, because price had risen from USD 13 in early January to USD 260.
- Typically 30 to 40% of a day's traded volume was already resting in the order book in the morning, against below 1% in conventional markets, so depth was observable.
- For the 14 most extreme negative returns between 1 January and 10 April 2013, the liquidity-adjusted imbalance matches realized drop sizes closely; raw imbalance does not. These events have a characteristic duration of about 4 hours (standard deviation 2.5 hours).
- Order-book illiquidity against the two proxies: R-squared about 0.86 on the same day and 0.83 with a one-day lag. Amihud's `sigma_d / V_d` gives 0.74 and 0.71.
- Large sell episodes are more intense than large buy episodes.
- Scope record: horizon about 4 hours; conditioning variable signed flow relative to buy-side liquidity; outcome the size of the move, not its later direction; no strategy, no costs.

## Signal construction
Illiquidity `ILLIQ = sigma_d / sqrt(V_d)` from trailing daily (or intraday, seasonally adjusted) realized volatility and volume, updated at least hourly. Expected move for a net taker flow `Q` over a few hours: `Y * sigma_d * sqrt(|Q| / V_d)`, with `Y` of order one and calibrated. Where a deep book is visible, also compute bid depth within x% of mid. For the bot's question, replace `Q` with flow that is known to be coming: liquidatable open interest within x% of the mark, or the recent change in open interest.

## Relevance to SOL perpetuals at minutes to hours
This gives the functional form for "open interest change relative to depth", the sub-question topic 04 lists as untested. It predicts a concave, square-root response of the move to forced flow, scaled by volatility and volume. It also suggests a reversal test: compare the realized move in a burst with the move the impact law implies for the observed flow. A move far beyond the implied size may be liquidity withdrawal and a candidate for reversal; a move in line with it is ordinary impact. Nothing in the paper tests that second step.

## Caveats
One venue, 2013, a market where resting depth was unusually visible; modern venues hide most liquidity and quotes are pulled in stress. Fourteen events. The comparison is after the fact, and two of the three measures were rescaled by a constant to match levels. The 4-hour window was chosen from the data. The authors state they cannot predict when a crash occurs.
