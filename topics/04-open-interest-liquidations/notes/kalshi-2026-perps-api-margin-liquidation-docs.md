---
title: "Kalshi API Documentation: Perps API (margin), risk parameters, market data and price banding"
authors: "Kalshi"
year: 2026
venue: "docs.kalshi.com (developer documentation, fetched 2026-11-22)"
url: "https://docs.kalshi.com/margin.md"
pdf: "none"
access: "full-text"
source_type: "documentation"
evidence_grade: "B"
topic: "04-open-interest-liquidations"
asset_class: "crypto"
horizon: "n/a"
tags: "kalshi, perpetual-futures, open-interest, liquidation, margin, mark-price, venue-mechanics"
---

## Key insight
Kalshi's perps API exposes the venue-level inputs this topic needs: one-sided open interest in contracts and dollars, a liquidation mark price distinct from the settlement mark price, size-dependent leverage estimates, and system-wide liquidation thresholds. Margin is scenario-based and portfolio-aware, with a liquidation margin that grows with position size through an explicit market-impact model. The public trade feed does not flag liquidations, so forced flow on Kalshi cannot be observed directly from public data.

## Method
Developer documentation. Pages read: the Perps API overview, Price Banding, and the OpenAPI definitions for Get Market, Get Trades, Get Risk Parameters, Get Risk and Get Maintenance Margin Metadata, plus the documentation index.

## Data and sample
Not applicable. The documentation describes demo and production environments and states that production perps access is "rolling out member by member".

## Reported results
- "Perps", "margin" and "perpetual futures" refer to the same product; endpoints sit under `/margin`, with REST, WebSocket and FIX access.
- Crypto perps fund every 8 hours at 12:00 AM, 8:00 AM and 4:00 PM US Eastern, so UTC funding times shift with daylight saving. Asset classes listed in the margin metadata schema: Crypto, Equities, Metals, Indices, Energy.
- Get Market returns `open_interest` (one sided), `open_interest_notional_value_dollars`, one-sided volume, `settlement_mark_price` (used for settlement and funding), `liquidation_mark_price` (used for liquidation) and `reference_price` (underlying). The WebSocket `ticker` channel carries price, top-of-book size, volume and open interest.
- `leverage_estimate` is `1 / margin_rate` at a small retail-sized notional; `leverage_estimates` are keyed by notional of 1,000, 10,000, 100,000 and 1,000,000 dollars, with separate long and short versions. Leverage decreases at larger notionals "as the liquidation margin rate grows with size".
- Get Risk Parameters returns `liquidation_margin_ratio_threshold` (margin ratio at which a position is liquidated), `queue_entry_margin_ratio_threshold` (margin ratio at which a position enters the liquidation queue) and a per-market `initial_margin_multiplier` (initial margin equals maintenance margin times this value).
- Maintenance margin metadata exposes tail percentiles of a scenario P&L distribution, a matrix of scenario returns per market, subgroups of markets margined together, and per-market liquidation configs with market-impact volatility, coefficient, exponent, forecasted volume and a spread rate.
- Get Risk returns account leverage (total position notional over total maintenance margin) and a portfolio-aware estimated liquidation price per position.
- Exchange-placed liquidation orders appear to the account holder with `order_source` of `system` and `order_reason` of `liquidation`. Liquidations are not subject to the book price band because they must be able to cross a thin book.
- Public trades carry ticker, count, price, time, `taker_side` and `is_block_trade`; no liquidation flag is listed.

## Signal construction
Inputs a bot can poll or stream: Kalshi SOL open interest in dollars and its change per interval; the gap between `liquidation_mark_price`, `settlement_mark_price` and `reference_price`; the leverage estimate curve as a measure of how much leverage the venue currently permits; and the two liquidation thresholds. Local forced flow must be inferred, for example from an open interest drop coinciding with one-sided taker volume.

## Relevance to SOL perpetuals at minutes to hours
This is the reference venue. Scenario-based margin with size-dependent liquidation margin and low maximum leverage means local liquidation clusters will sit further from the mark than on offshore venues, so local cascades should be rarer and smaller; cascades will mostly arrive through the reference price. A stop-loss placed beyond the estimated liquidation price is rejected, which constrains exit design. Actual threshold values, the SOL leverage estimate, and the open interest level must be read from the live API.

## Caveats
API documentation, not a rulebook: it does not describe the insurance or default-waterfall arrangement, whether auto-deleveraging exists, or how the liquidation queue is executed. No numerical parameter values appear in the pages read. Documentation can change without notice.
