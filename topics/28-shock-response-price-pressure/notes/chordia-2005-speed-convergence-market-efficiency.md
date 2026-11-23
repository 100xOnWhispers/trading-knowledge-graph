---
title: "Evidence on the Speed of Convergence to Market Efficiency"
authors: "Chordia, Tarun; Roll, Richard; Subrahmanyam, Avanidhar"
year: 2005
venue: "Journal of Financial Economics 76(2), 271-292; UCLA Anderson working paper version dated 22 June 2004 read"
url: "https://escholarship.org/content/qt8wb6140g/qt8wb6140g.pdf"
pdf: "sources/28-shock-response-price-pressure/chordia-2005-speed-convergence-market-efficiency.pdf"
access: "full-text"
source_type: "peer-reviewed"
evidence_grade: "A"
topic: "28-shock-response-price-pressure"
asset_class: "equities"
horizon: "minutes"
tags: "order-imbalance, intraday-predictability, market-efficiency, decay, price-pressure"
---

## Key insight
Order imbalance is strongly persistent, yet returns are not. The two facts are reconciled inside the trading day: past order imbalance predicts returns for a few minutes, and that predictability is gone within 5 to 30 minutes because other traders step in on the opposite side. The paper measures how long the market takes to absorb flow pressure, and shows the window shrank from 30 minutes to about 5 between 1996 and 2002.

## Method
Sign every trade with the Lee-Ready rule. For each stock and each of several interval lengths between 5 and 60 minutes, compute order imbalance as buys minus sells in number of trades, shares and dollars, and returns from quote midpoints to remove bid-ask bounce. Run stock-by-stock regressions of returns on lagged returns and of returns on lagged imbalance; average coefficients across stocks, with t-statistics adjusted for cross-correlation of residuals. A further test regresses buyer-initiated volume on lagged seller-initiated volume to detect countervailing trades.

## Data and sample
150 large NYSE stocks (three groups of fifty by market capitalization, the smallest still above USD 6.69 billion), all TAQ transactions in three calendar years: 1996, 1999 and 2002. The years bracket the tick-size cuts from one-eighth to one-sixteenth (1997) and to decimals (2001).

## Reported results
- Returns alone show little unconditional serial dependence even at 5 minutes: none of the adjusted t-statistics exceeds 2.0 in absolute value and 13 of 15 are below 1.0.
- Lagged order imbalance does predict returns, with a positive sign, at up to 30 minutes in 1996, up to 10 minutes in 1999 and up to 5 minutes in 2002. Coefficients and t-statistics fall as the interval lengthens.
- In no year does it take more than 30 minutes to remove the predictive content of imbalance.
- Imbalance itself is positively autocorrelated at every interval, and more so at longer intervals; daily autocorrelation of the trade-count imbalance exceeds 0.3 in 1996 and 1999 and is 0.249 in 2002.
- Buyer-initiated orders are followed by seller-initiated orders in the next interval (every coefficient positive and significant), which the authors read as arbitrageurs leaning against the initial imbalance.
- The S&P 500 daily first-order autocorrelation over 1996-2002 was -0.0015.
- Scope record: horizon 5 to 60 minutes; conditioning variable lagged signed order imbalance; sign positive (continuation) for minutes, then zero; costs not charged.

## Signal construction
Signed taker imbalance over the last bar, `OIB = (buy volume - sell volume) / (buy volume + sell volume)`, or the count version, computed from the trade tape of the lead venues. Predict next-bar mid return with a positive coefficient at the shortest bar and estimate the bar length at which the coefficient becomes indistinguishable from zero. That decay time is the quantity of interest: it is the window in which a flow shock is still being absorbed.

## Relevance to SOL perpetuals at minutes to hours
The paper supplies the benchmark timescale for flow-driven continuation in a liquid market: minutes, and shrinking as markets get faster. Crypto venues give the aggressor side directly, so the imbalance is measured without classification error. The implied structure for the bot is a two-phase response to a shock: a short continuation window while one-sided flow persists, followed by no edge from flow alone. What needs testing is the length of that window for SOL today, whether it stretches during liquidation bursts when the flow is mechanical and predictable, and whether a slower venue such as Kalshi shows a longer window than Binance.

## Caveats
Large NYSE stocks only, three sample years, specialist market. Predictability is statistical, not shown to be profitable after spreads. The trend toward faster absorption suggests any raw imbalance edge on a modern electronic venue is very short. Topic 07 covers the order-book version of this signal.
