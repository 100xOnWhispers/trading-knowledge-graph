---
title: "Currency Orders and Exchange Rate Dynamics: An Explanation for the Predictive Success of Technical Analysis"
authors: "Osler, Carol L."
year: 2003
venue: "Journal of Finance, 58(5), pp. 1791-1819 (read as FRBNY Staff Report 125, 2001)"
url: "https://www.newyorkfed.org/medialibrary/media/research/staff_reports/sr125.pdf"
pdf: "sources/17-auction-orderflow-practitioner/osler-2003-currency-orders-exchange-rate-dynamics.pdf"
access: "full-text"
source_type: "peer-reviewed"
evidence_grade: "A"
topic: "17-auction-orderflow-practitioner"
asset_class: "fx"
horizon: "minutes"
tags: "stop-loss, take-profit, order-clustering, round-numbers, support-resistance, liquidity-sweep"
---

## Key insight
The practitioner claim that "levels are where orders rest" is literally true in a dealer's order book. Take-profit orders cluster exactly on round numbers, which makes those prices partially reflecting barriers. Stop-loss orders cluster just beyond round numbers (buy stops just above, sell stops just below), which makes price accelerate once a round number is crossed. This asymmetry explains both "levels hold" and "breakouts run", and is the best documented basis for the stop-run or liquidity-sweep idea.

## Method
Descriptive analysis of the requested execution rates of conditional orders, by their last two digits, split into four types: stop-loss buy, stop-loss sell, take-profit buy, take-profit sell. Uniformity is tested with Anderson-Darling; differences between order types are tested with bootstrap procedures. A simulation then drives a log exchange rate with order flow, x(t+1) - x(t) = beta * O(t), where O(t) is fundamental (random), arbitrage and conditional order flow, the last calibrated to the observed digit distributions. I read the staff-report version; the journal text may differ in detail.

## Data and sample
9,667 stop-loss and take-profit orders at a large dealing bank, 1 September 1999 to 11 April 2000: dollar-yen 43%, euro-dollar 33%, dollar-pound 24%. Mean size $5.8 million, median $3.0 million. About one third were executed; over 70% were deleted or closed within one business day; median time open 0.4 days.

## Reported results
- Uniform distribution of final digits rejected at better than the 0.01% level for all three pairs.
- About 8.7% of orders sit at rates ending in 00 (uniform: 1%), with weaker clusters at 50, other multiples of 10, then 5. No special clustering at 25 or 75.
- 9.3% of take-profit orders are executed exactly at 00 against 4.4% of stop-loss orders (bootstrap significance 1.1%).
- When price rises to a 00 level, about 10.5% of take-profit sells are triggered against 2.8% of stop-loss buys, so order flow at the level opposes the move.
- 14.4% of stop-loss buys sit at endings 01-10 against 7.4% at 90-99; stop-loss sells mirror this. Take-profit orders show no such asymmetry.
- Simulated rates calibrated to these distributions reverse at round numbers and trend after crossing them.

## Signal construction
Two state features around any round number R: (1) approach state, when price is within a tolerance of R from one side, where the prior is a modest fade; (2) breach state, when price has traded beyond R by a small offset, where the prior is continuation as stops fire. In crypto the analogue of the stop distribution can be partly observed: resting depth near R on Binance, Bybit and OKX books, and estimated liquidation prices beyond R. Features: distance to nearest round number in ticks and in volatility units, side of approach, resting depth at R against depth just beyond it, and time since last touch.

## Relevance to SOL perpetuals at minutes to hours
The mechanism should transfer because it depends on human order placement and quoting conventions, both present in crypto. The relevant grid for SOL has to be found empirically (whole dollars, 5 and 10 dollar multiples). Forced liquidations add a second, mechanical source of price-contingent flow beyond round numbers that FX in 1999 did not have. Kalshi's low leverage means the clusters that matter sit on offshore venues, not on Kalshi itself.

## Caveats
One bank, seven months, 1999-2000, telephone-era market. The paper documents order placement, not profits. Clusters are visible to dealers, not to the public; a bot infers them. Published and widely known, so sophisticated participants now trade against these clusters.
