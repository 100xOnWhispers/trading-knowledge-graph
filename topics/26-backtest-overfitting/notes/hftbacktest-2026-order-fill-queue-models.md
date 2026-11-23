---
title: "HftBacktest documentation: Order Fill (exchange fill models and queue position models)"
authors: "hftbacktest developers"
year: 2026
venue: "hftbacktest library documentation (page accessed 2026-11-22; publication year of the page not confirmed)"
url: "https://hftbacktest.readthedocs.io/en/latest/order_fill.html"
pdf: "none"
access: "full-text"
source_type: "documentation"
evidence_grade: "D"
topic: "26-backtest-overfitting"
asset_class: "crypto"
horizon: "tick"
tags: "fill-modelling, queue-position, limit-orders, market-impact, backtest-realism"
---

## Key insight
Whether a resting limit order would have filled is not observable from historical data, so every backtest embeds a fill model, and the choice determines the result for passive strategies. This documentation page for an open-source tick-level crypto backtester sets out a conservative set of fill rules, a family of queue-position models, and an explicit statement of what a replay-based backtest cannot capture.

## Method
Fill rules described on the page:
- No-partial-fill exchange model (default). A buy limit order fills in full when its price is at or above the best ask, or above the price of a sell trade, or equals a sell trade's price while the order is at the front of the queue. Sells mirror this. Liquidity-taking orders fill in full at the best price regardless of displayed quantity.
- Partial-fill exchange model. Full fill when the order crosses the best quote or a trade prints through its price; partial fill by the remaining trade quantity when the order is at the front of the queue and its price equals the trade price. Taker orders fill against book depth, although the replayed book does not change.

Queue-position models (the library uses market-by-price data, so queue position must be inferred):
- Risk-averse model: quantity decreases from cancellations or modifications are assumed to occur only behind the order (at the tail), so the order advances only when trades occur at its price. This is the most conservative choice.
- Probability models: a decrease at the price level is split probabilistically between ahead of and behind the order, using a function of the order's relative position that must equal 0 at the head of the queue and 1 at the tail. Power-function and log-function variants are provided (the log form is f = log(1 + x) and depends on total quantity at the level). Custom models can be supplied.

## Data and sample
None. Software documentation; the library targets crypto exchange tick and depth feeds.

## Reported results
No empirical results. Statements made:
- The backtest is replay-based, so an order cannot change the simulated market and no market impact is considered; orders must be small enough for that to hold.
- Large liquidity-taking orders may receive unrealistic fills.
- Users "must test it in a live market with real market participants and adjust your backtesting based on the discrepancies."
- The page does not discuss latency (the library handles it elsewhere; not read).

## Signal construction
Not a signal. It is a fill-model specification for the simulator:
- passive orders: count a fill only when a trade prints through the limit price, or at the price after the inferred queue ahead has traded; start with the risk-averse queue model;
- aggressive orders: fill at the far touch plus a slippage allowance tied to displayed depth;
- calibrate the queue model by comparing simulated and live fill rates for small orders, then keep the calibrated model fixed.

## Relevance to SOL perpetuals at minutes to hours
A directional bot at minutes to hours can choose between crossing the spread and resting passively; the second looks far better in a naive backtest that fills at the touch whenever price reaches the limit. The "trade through" rule and risk-averse queue assumption are the standard correction. On a new, thin venue such as Kalshi the no-impact assumption fails quickly as size grows, and queue dynamics learned on Binance or Bybit will not carry over, so the live-calibration advice is the central point. Bar-based backtests cannot represent any of this and should assume taker execution with spread and slippage.

## Caveats
Documentation with no validation data; grade D. The fill rules are heuristics, and the probability queue models have free parameters that can themselves be overfit to make a strategy look good. Adverse selection of passive fills (being filled precisely when price is about to move against the order) is captured only to the extent the replayed trades reflect it. The calibration steps under "Signal construction" are this note's reading of the page's advice, not text from it.
