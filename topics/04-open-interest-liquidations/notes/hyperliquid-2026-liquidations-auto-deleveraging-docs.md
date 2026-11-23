---
title: "Hyperliquid Docs: Liquidations and Auto-deleveraging"
authors: "Hyperliquid"
year: 2026
venue: "hyperliquid.gitbook.io (protocol documentation, fetched 2026-11-22)"
url: "https://hyperliquid.gitbook.io/hyperliquid-docs/trading/liquidations"
pdf: "none"
access: "full-text"
source_type: "documentation"
evidence_grade: "B"
topic: "04-open-interest-liquidations"
asset_class: "crypto"
horizon: "n/a"
tags: "hyperliquid, liquidation-mechanics, auto-deleveraging, backstop, liquidation-price, mark-price"
---

## Key insight
Hyperliquid's documented liquidation waterfall has three stages: market orders to the book, a backstop takeover by the liquidator vault, and auto-deleveraging against the most profitable and most levered opposing traders. Each stage has explicit numerical thresholds and a published liquidation-price formula. Because positions are on-chain, these rules allow an exact liquidation map to be computed for any asset, which is not possible on centralized venues.

## Method
Protocol documentation. Two pages were read in their Markdown versions: "Liquidations" and "Auto-deleveraging" (the second at the same path ending in `/auto-deleveraging`).

## Data and sample
Not applicable.

## Reported results
Liquidations page:
- Liquidation starts when account equity falls below maintenance margin, which is half the initial margin at the asset's maximum leverage. Maintenance margin ranges from 1.25% for 40x assets to 16.7% for 3x assets.
- The trigger uses the mark price, which combines external exchange prices with Hyperliquid's own book state.
- Stage one: the position is sent to the order book as market orders. For liquidatable positions larger than 100,000 USDC only 20% is sent, followed by a 30-second cooldown during which further liquidation orders for that user cover the entire position.
- Stage two: if equity falls below two thirds of maintenance margin without a successful book liquidation, the liquidator vault (a component of HLP) takes over the position and margin. Maintenance margin is not returned to the user in a backstop liquidation.
- Liquidation price: `liq_price = price - side * margin_available / position_size / (1 - l * side)` with `l = 1 / maintenance_leverage`, `side` equal to 1 for long and -1 for short, and `margin_available` equal to account value (cross) or isolated margin (isolated) minus required maintenance margin.
- For cross margin, the liquidation price does not depend on the leverage setting, and it shifts with funding payments and unrealized PnL on other positions.

Auto-deleveraging page:
- ADL applies when an account value or isolated position value becomes negative.
- Opposing traders are ranked by `(mark_price / entry_price) * (notional_position / account_value)`.
- Selected positions are closed at the previous mark price against the underwater user.
- A user with no open positions does not bear socialized losses.

## Signal construction
For each SOL position visible on-chain, compute the liquidation price with the formula above and aggregate notional into price buckets to form a liquidation map; update it as positions, margin and funding change. Two regime flags follow from the rules: large positions unwind in 20% clips with 30-second cooldowns, so forced flow from a single large account arrives in a recognizable cadence; and backstop takeovers remove flow from the book, so visible forced selling understates total forced closing.

## Relevance to SOL perpetuals at minutes to hours
Hyperliquid lists a SOL perp (SOL appears in the Lim and Campbell samples) and is the one large venue in this topic where the map can be exact. The mark-price rule means Hyperliquid liquidations respond to centralized-exchange prices, not only its own book, which links venues during a cascade. The cross-margin dependence is the main practical difficulty: an account's SOL liquidation price moves with its BTC and ETH PnL, so the map must be recomputed at account level, not position level. The Kalshi mechanics differ and are covered in a separate note.

## Caveats
Documentation describes intended behavior; behavior in October 2025 was analysed separately in the Chitra and Campbell notes. Parameters such as margin tiers and thresholds can change. The pages do not report historical ADL usage. For assets with margin tiers the maintenance leverage in the formula depends on the tier at the liquidation price, which the pages read do not tabulate.
