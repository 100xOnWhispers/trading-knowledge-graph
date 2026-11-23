---
title: "Trading Costs"
authors: "Frazzini, Andrea; Israel, Ronen; Moskowitz, Tobias J."
year: 2018
venue: "AQR Capital Management working paper, August 23, 2018"
url: "https://www.aqr.com/Insights/Research/Working-Paper/Trading-Costs"
pdf: "none"
access: "abstract-only"
source_type: "working-paper"
evidence_grade: "B"
topic: "27-execution-risk-management"
asset_class: "equities"
horizon: "daily"
tags: "transaction-costs, price-impact, live-execution-data, cost-model, institutional-trading"
---

## Key insight
Costs measured from a large manager's own live executions are, according to the abstract, an order of magnitude smaller than earlier academic estimates built from public trade data. The practical lesson is methodological: realised cost depends on how the trader trades, so a cost model must be calibrated on the trader's own fills, and models fitted to the average market participant can be badly wrong in either direction.

## Method
From the abstract and the publisher's summary page only. The authors measure real-world trading costs and the price-impact function of one large trader from live execution records. They describe how costs vary with trade type, stock characteristics, trade size, time and exchange, and use this to test theories of price impact. They fit a cost model to the distribution of realised costs across trade size, stocks and time, and compare it out of sample with other models from the literature, using independent broker cost estimates and the realised costs of traded index funds as targets. The functional form of the model and its coefficients were not read.

## Data and sample
From the abstract: $1.7 trillion of live trade execution data from one large institutional money manager, 21 developed equity markets, a 19-year period. Exact dates not confirmed.

## Reported results
From the abstract only:
- "We find actual trading costs to be an order of magnitude smaller than previous studies suggest".
- A model calibrated to the realised cost distribution "outperforms other models from the literature in out of sample tests" against broker-reported costs and index fund realised costs.
- The authors "describe the trading process leading to these costs"; details not read.

No cost figures in basis points, no impact exponent and no breakdown by trade size were read; none are reported here.

## Signal construction
Not a signal; a template for the bot's cost model. Log every order with arrival mid price, decision time, order type, limit price, fill price, fill time, fee paid, size relative to displayed depth, spread and volatility at arrival. Compute implementation shortfall per order against the arrival mid. Regress shortfall on size relative to depth, volatility, spread and order type. Use the fitted model, not exchange fee tables plus an assumed slippage, in backtests and in the reward of any learned policy. Refit monthly and after any fee-schedule change.

## Relevance to SOL perpetuals at minutes to hours
The direction of the paper's surprise does not transfer. This is a patient institutional trader in liquid developed equities, largely providing liquidity over days; a small account taking liquidity on a five-month-old perpetuals venue faces explicit fees that alone exceed typical equity impact costs (12 bp taker at Kalshi's entry retail tier, per topic 06). What does transfer is the approach: live fills are the only trustworthy cost data, and the gap between assumed and realised cost can be an order of magnitude. Albers et al. make the same point for crypto with a live experiment. The bot should run a small-size live cost-measurement phase before any strategy is judged on backtest returns.

## Caveats
Abstract-only: the publisher's page offered a one-page summary, and the full paper on SSRN could not be retrieved. The data come from the authors' employer, whose business benefits from the conclusion that costs are low; the abstract's own disclaimer says the document is not research in the regulatory sense. One trader's costs reflect that trader's style and cannot be assumed for others. Equities at daily horizons; nothing on derivatives, leverage or intraday trading.
