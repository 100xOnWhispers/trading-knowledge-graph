---
title: "Currency Orders and Exchange-Rate Dynamics: Explaining the Success of Technical Analysis"
authors: "Osler, Carol L."
year: 2003
venue: "Federal Reserve Bank of New York Staff Report 125 (March 2001 version); later published in the Journal of Finance"
url: "https://www.newyorkfed.org/medialibrary/media/research/staff_reports/sr125.pdf"
pdf: "sources/16-oscillators-technical-rules/osler-2003-currency-orders-technical-analysis.pdf"
access: "full-text"
source_type: "working-paper"
evidence_grade: "B"
topic: "16-oscillators-technical-rules"
asset_class: "fx"
horizon: "minutes"
tags: "stop-loss, take-profit, order-clustering, round-numbers, support-resistance, microstructure, theory"
---

## Key insight
A microstructure explanation for why support and resistance levels work. Take-profit orders cluster at round numbers, which makes prices tend to reverse there. Stop-loss orders cluster just beyond round numbers, which makes prices accelerate once a round number is crossed. Technical levels predict because they mark where conditional order flow is waiting, not because of anything in the chart itself.

## Method
Descriptive analysis of the requested execution rates of stop-loss and take-profit orders in a dealing bank's book. The frequency of the final two digits of each order's rate is tabulated by order type and direction, and differences are tested with a bootstrap in which frequencies are redrawn under the null that the digit pattern is the same across order types. The mechanism is then spelled out. A take-profit order trades against the current move (it sells into a rise), so a cluster acts as a partially reflecting barrier. A stop-loss order trades with the move (it buys after a rise), so a cluster propagates the trend and can set off a cascade.

## Data and sample
Almost 9,700 stop-loss and take-profit orders placed at a large foreign-exchange dealing bank between 1 September 1999 and 11 April 2000, in dollar-yen, dollar-pound and euro-dollar.

## Reported results
- Rates ending in 00 attract roughly 8.7% of orders on average, with smaller clusters at 50, at other rates ending in 0, and at rates ending in 5. There is no special clustering at 25 or 75.
- Take-profit orders cluster at 00 more strongly than stop-loss orders: 9.3% of take-profit orders are executed exactly at 00, against 4.4% of stop-loss orders.
- Stop-loss buy orders are concentrated just above round numbers and stop-loss sell orders just below them. For example, about 4.5% of stop-loss buy orders are executed at levels ending in 10, against about 2.7% of take-profit sell orders.
- Over 70% of orders were deleted or closed within one day, so the book is a short-horizon object.

## Signal construction
Two features a bot can compute from price alone, plus one that needs order-book data:
1. Distance to the nearest round level, in ticks and in units of recent volatility, with the sign of approach.
2. A crossing flag: price has just traded through a round level by more than k ticks. The paper predicts continuation after a crossing and reversal on approach without a crossing.
3. Where available, resting depth and liquidation-price clusters near the level, which are the direct crypto analogue of the bank's stop-loss book.

## Relevance to SOL perpetuals at minutes to hours
The mechanism should be stronger in leveraged perpetuals than in spot FX, because liquidations are forced stop-loss orders whose trigger prices are partly predictable from leverage tiers and entry clusters. Round SOL prices and prior highs and lows are natural candidates. On a low-leverage venue such as Kalshi the local liquidation effect will be weak, so the levels that matter are probably those on Binance, Bybit and Hyperliquid. This needs testing as a conditional effect: does breakout continuation on SOL depend on proximity to round levels and on measured liquidation density?

## Caveats
One bank, seven months, and customer orders only, so representativeness is assumed. The paper documents order placement; the matching price behavior is in companion papers by the same author that I did not read. It gives no trading-rule returns and no costs. Clustering conventions in crypto (which digits count as round at SOL's price level) must be measured, not assumed.
