---
title: "Kalshi Perps API documentation: overview, REST reference, WebSocket channels, FIX gateway, price banding, rate limits and tiers"
authors: "Kalshi"
year: 2026
venue: "docs.kalshi.com"
url: "https://docs.kalshi.com/margin.md"
pdf: "none"
access: "full-text"
source_type: "documentation"
evidence_grade: "B"
topic: "06-kalshi-venue"
asset_class: "crypto"
horizon: "n/a"
tags: "kalshi, api, rest, websocket, fix, rate-limits, price-banding, order-types, margin-model, historical-data"
---

## Key insight
Kalshi exposes perps through a REST, WebSocket and FIX surface under a `/margin` namespace that mirrors its event-contract API. Public market data, including funding history, a per-second premium index, order books, trades and candles, is readable without authentication. The reference also reveals mechanics the help center omits: scenario-based margin, a liquidation queue threshold, price bands and exit-trigger behaviour.

## Method
Read as raw markdown: the Perps overview, about twenty REST endpoint pages (markets, order book, candlesticks, trades, funding estimate, historical funding, premium index, risk parameters, create order, fee tiers, API limits), the WebSocket ticker page, price banding, rate limits, the maintenance-margin metadata page and the changelog index.

## Data and sample
Documentation as served on 2026-11-22. Production hosts are described as "rolling out member by member".

## Reported results
- Hosts: REST `external-api.kalshi.com/trade-api/v2/margin/`; WebSocket `external-api-margin-ws.kalshi.com`; a lower-latency host for `fill` and `user_orders`; FIX (FIXT.1.1 / FIX50SP2) order entry, drop copy and market data on separate hosts. Demo equivalents exist.
- WebSocket channels: `orderbook_delta`, `ticker`, `trade`, `fill`, `user_orders`, `order_group_updates`, `market_lifecycle_v2`. `ticker` carries reference price, settlement mark, liquidation mark and funding rate with `next_funding_time_ms`. Timestamps are Unix milliseconds.
- Not available on margin: batch orders, queue positions, RFQs, "Historical data endpoints", exchange schedule.
- Orders: time in force `good_till_canceled`, `immediate_or_cancel`, `fill_or_kill`; `post_only`; `reduce_only` only with IOC or FOK; self-trade prevention modes; stop-loss, take-profit and trailing-stop exit triggers. A fired trigger places a reduce-only IOC limit order, which "can fill partially or not at all".
- Market fields: `tick_size`, `contract_size`, `minimum_quantity`, `funding_cap`, `funding_deadband`, `funding_invalid_premium_handling` (`dampen` counts a missing bar as zero), leverage estimates by side and by notional ($1k to $1M).
- Risk: initial margin equals maintenance margin times a per-market multiplier; a position enters the liquidation queue at one margin-ratio threshold and is liquidated at another. Maintenance margin uses a lower-tail percentile of a scenario P&L distribution over calibrated return matrices.
- Price banding: a crossing bid may be at most the higher of twice the best ask or 1,000 ticks above it. Liquidations are exempt from the book band.
- Candlesticks: 1, 60 or 1,440 minute periods with bid, ask and trade OHLC, volume and open interest. Premium index: per second, windows of at most one hour, limited retention.
- Rate limits: token buckets, 10 tokens per default request. Perps budgets per second, read/write: Basic 400/200, Advanced 600/600, Expert 600/1,200, Premier 1,000/3,000, up to Prestige 6,000/24,000. Cancels cost 1 token. WebSocket connections: 200 per user through Expert.
- Funding times move by an hour in UTC at daylight-saving changes; read `next_funding_time` instead of hard-coding.

## Signal construction
Not a signal. It defines the bot's observable state and action space. State: L2 book via `orderbook_delta`, trades with taker side, `reference_price` (SOLUSD_RTI scaled per contract), two mark prices, live funding estimate, per-second premium index. Actions: limit or IOC orders in whole contracts of 0.1 SOL at a $0.0001 tick, optional post-only, bracket exits.

## Relevance to SOL perpetuals at minutes to hours
A Basic-tier write budget of 200 tokens per second allows 20 order placements per second, ample for this horizon. For machine-learning work, the venue supplies a ready feature feed and a demo exchange that can serve as a paper-trading environment for a reinforcement-learning agent before live capital.

## Caveats
Documentation changes often; the changelog lists many perps changes within months. The demo host returned 404 for the SOL market when probed without credentials, so demo coverage is not confirmed. Authenticated endpoints (fees, risk, margin metadata) were read only as schemas, not as live values. The statement that historical data endpoints are unavailable is narrower than it sounds: candles, trades and funding history do go back to launch.
