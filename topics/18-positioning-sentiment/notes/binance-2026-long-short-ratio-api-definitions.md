---
title: "Binance Futures market-data API: Long/Short Ratio, Top Trader Long/Short Ratio (Accounts and Positions), Taker Buy/Sell Volume"
authors: "Binance"
year: 2026
venue: "Binance developer documentation (fetched 2026-11-22)"
url: "https://developers.binance.com/docs/derivatives/usds-margined-futures/market-data/rest-api/Top-Trader-Long-Short-Ratio"
pdf: "none"
access: "full-text"
source_type: "documentation"
evidence_grade: "B"
topic: "18-positioning-sentiment"
asset_class: "crypto"
horizon: "minutes"
tags: "long-short-ratio, top-trader-ratio, account-ratio, position-ratio, taker-volume, binance-api, data-definition"
---

## Key insight
Binance publishes three different "long/short ratios" that are often conflated. The global ratio counts accounts. The top-trader account ratio counts accounts among the top 20% of users by margin balance. The top-trader position ratio weights by position size within that same group. Only the last is a size-weighted positioning measure; the first two are head-counts. Every perp contract has a long and a short, so none of these can describe the whole market's net position: they describe how one class of accounts is distributed.

## Method
Definitions as stated in the documentation (USDⓈ-M REST API section, confirmed in the documentation's full-text export):

Top Trader Long/Short Account Ratio, `GET /futures/data/topLongShortAccountRatio`: "The proportion of net long and net short accounts to total accounts of the top 20% users with the highest margin balance. Each account is counted once only."
- Long Account % = accounts of top traders with net long positions / total accounts of top traders with open positions
- Short Account % = accounts of top traders with net short positions / total accounts of top traders with open positions
- Long/Short Ratio (Accounts) = Long Account % / Short Account %

Top Trader Long/Short Position Ratio, `GET /futures/data/topLongShortPositionRatio`: "The proportion of net long and net short positions to total open positions of the top 20% users with the highest margin balance."
- Long Position % = long positions of top traders / total open positions of top traders
- Short Position % = short positions of top traders / total open positions of top traders
- Long/Short Ratio (Positions) = Long Position % / Short Position %

Global Long/Short Ratio, `GET /futures/data/globalLongShortAccountRatio`: described only as "Query symbol Long/Short Ratio"; response fields are `symbol`, `longShortRatio`, `longAccount`, `shortAccount`, `timestamp`. No calculation method is given on the page.

Taker Buy/Sell Volume, `GET /futures/data/takerlongshortRatio`: total volume of buy orders and of sell orders filled by takers within the period.

## Data and sample
Per symbol on Binance USDⓈ-M futures (COIN-M equivalents exist). For the global ratio the page lists `period` values 5m, 15m, 30m, 1h, 2h, 4h, 6h, 12h and one further value not visible in the rendered page; `limit` up to 500; only the latest 30 days are available; rate limit 1000 requests per 5 minutes per IP. The same period and retention terms for the two top-trader endpoints were not confirmed from the text read.

## Reported results
None. This is a data definition, not a study. No evidence of predictive power is offered by the exchange.

## Signal construction
Poll each endpoint every 5 minutes for SOLUSDT and store the series locally (history beyond 30 days cannot be recovered later). Candidate features:
- `g = log(global longShortRatio)`: retail-weighted crowd lean.
- `ta = log(top account ratio)`, `tp = log(top position ratio)`.
- `div_size = tp - ta`: within large accounts, whether the biggest positions lean differently from the head-count.
- `div_class = tp - g`: large-account size-weighted lean minus crowd lean.
- Changes in each over 1 to 24 hours, conditioned on the sign of price change and on open-interest change (topic 04).

## Relevance to SOL perpetuals at minutes to hours
These are the most accessible positioning series for SOL at 5-minute resolution, from the venue where most SOL perp price discovery occurs. They are inputs for a Kalshi SOL-perp bot, not Kalshi data. Whether any of the features above predicts SOL returns is untested in any source read for this topic; the contrarian reading of the global ratio and the smart-money reading of the top-trader ratio are both practitioner conventions.

## Caveats
"Top 20% by margin balance" is venue-wide, not per symbol as far as the text states, and includes hedgers and basis traders whose perp leg offsets spot or options. Accounts hedged across sub-accounts or venues look directional. The ratio is undefined for accounts without positions and can jump when accounts open or close. Thirty-day retention means any backtest needs self-collected or vendor data. Documentation can change without notice.
