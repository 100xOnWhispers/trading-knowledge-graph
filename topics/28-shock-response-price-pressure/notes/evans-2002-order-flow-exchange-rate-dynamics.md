---
title: "Order Flow and Exchange Rate Dynamics"
authors: "Evans, Martin D. D.; Lyons, Richard K."
year: 2002
venue: "NBER Working Paper 7317 (August 1999), the version read; published in the Journal of Political Economy, 2002 (journal version not opened)"
url: "https://www.nber.org/system/files/working_papers/w7317/w7317.pdf"
pdf: "sources/28-shock-response-price-pressure/evans-2002-order-flow-exchange-rate-dynamics.pdf"
access: "full-text"
source_type: "peer-reviewed"
evidence_grade: "A"
topic: "28-shock-response-price-pressure"
asset_class: "fx"
horizon: "daily"
tags: "order-flow, permanent-impact, fx, dealer-market, portfolio-shifts, 24-hour-market"
---

## Key insight
In the 24-hour interdealer currency market, signed order flow explains most of the daily change in the exchange rate, and the price effect does not wash out within the day. Macro variables explain almost nothing at this horizon. The result establishes that in a decentralized, round-the-clock market with no private cash-flow news, order flow still moves price persistently, because it carries dispersed information about portfolio demand that the market must be paid to absorb.

## Method
A "portfolio shifts" model with three trading rounds per day: dealers trade with customers, then with each other, then lay off positions to the public, who must be induced by a price change to hold the net shift. The estimating equation is

`dp(t) = b1 * d(i - i*)(t) + b2 * dx(t) + e(t)`

where `dp` is the daily change in the log spot rate, `d(i - i*)` the change in the overnight interest differential and `dx` interdealer order flow (number of buyer-initiated minus seller-initiated trades). Variants add lagged flow and lagged price changes. Out-of-sample forecasts are compared with a random walk at one day to two weeks, using realized flow.

## Data and sample
All bilateral interdealer trades on the Reuters Dealing 2000-1 system in DM/USD and JPY/USD, 1 May to 31 August 1996, 24 hours a day; 89 trading days. Trades are signed by initiator; trade sizes are not recorded.

## Reported results
- R-squared of 0.64 for DM/USD and 0.45 for JPY/USD. The interest differential alone gives less than 0.01.
- Order-flow coefficient 2.10 (standard error 0.20) for the DM and 2.90 (0.46) for the yen: 1,000 more dollar purchases than sales in a day raises the DM price of the dollar by 2.1 percent. With an average trade of USD 3.9 million, USD 1 billion of net purchases moves the rate about 0.54 percent, or 0.8 pfennig.
- Lagged order flow and lagged price changes are insignificant (0.29 with standard error 0.19 for the DM; -0.20 with 0.35 for the yen). There is no sign of next-day reversal of the flow-driven move.
- Cumulative interdealer order flow does not mean-revert over the four months, even though individual dealers' positions have half-lives as short as 10 minutes (citing Lyons 1998).
- The flow model beats a random walk at short horizons out of sample, but the forecasts use realized future flow.
- Scope record: horizon one day, contemporaneous; conditioning variable signed interdealer flow; sign positive and persistent; costs not charged.

## Signal construction
Not a forecasting signal: the relation is contemporaneous. Its use is as a decomposition. Regress the bar return on signed taker flow aggregated across the lead venues; the fitted part is the flow-explained move and the residual is the move without flow (quote revision on news). A bot can then treat the two parts differently: test whether flow-explained moves or no-flow moves are the ones that reverse. The coefficient also gives a live price-impact estimate per unit of net flow.

## Relevance to SOL perpetuals at minutes to hours
FX is the closest traditional analogue to crypto: continuous trading, many venues, dealers who pass inventory along ("hot potato") and no cash-flow fundamentals. The lesson is a warning against assuming flow-driven moves are transitory. Sustained one-directional flow can represent a real shift in what the market must hold, and its price effect stays. For SOL the distinction that matters is between flow that changes aggregate positions (new longs or shorts opened, spot bought and withdrawn) and flow that is only inventory being passed around or forced out. Makarov and Schoar in topic 05 report the same strong contemporaneous flow-return relation for Bitcoin spot.

## Caveats
Four months, two currency pairs, 1996, one dealing system. Daily aggregation says nothing about intraday paths. Causality could run from price to flow through feedback trading; the authors argue against it but cannot exclude it. Counts of trades, not volumes. The forecasting exercise is not a tradable test.
