---
title: "Binance USDS-Margined Futures WebSocket Market Streams: Liquidation Order Streams"
authors: "Binance"
year: 2026
venue: "developers.binance.com (API documentation, fetched 2026-11-22)"
url: "https://developers.binance.com/docs/derivatives/usds-margined-futures/websocket-market-streams/All-Market-Liquidation-Order-Streams"
pdf: "none"
access: "full-text"
source_type: "documentation"
evidence_grade: "B"
topic: "04-open-interest-liquidations"
asset_class: "crypto"
horizon: "seconds"
tags: "binance, liquidation-data, data-quality, websocket, undercounting, forceorder"
---

## Key insight
Binance's public liquidation feed is a sampled snapshot, not a complete record. For each symbol only the most recent liquidation order within each 1000 ms window is pushed. During a cascade, when many liquidations occur per second, the feed therefore drops most events, and any liquidation total or heatmap built from it is a lower bound whose bias grows with the intensity of the event.

## Method
API documentation, read through a fetch-and-summarize tool that returned direct quotations for the key sentences.

## Data and sample
Not applicable.

## Reported results
- Stream name: `<symbol>@forceOrder` for one symbol; `!forceOrder@arr` for all symbols.
- Quoted description: "For each symbol, only the latest one liquidation order within 1000ms will be pushed as the snapshot." and "If no liquidation happens in the interval of 1000ms, no stream will be pushed."
- Update speed: 1000 ms.
- Payload fields: event type, event time, and an order object with symbol, side, order type, time in force, original quantity, price, average price, order status, last filled quantity, accumulated filled quantity and order trade time.

A related data fact from another source in this topic: the early-warning study by Garcia Seuma reports that Binance's per-event `liquidationSnapshot` historical dumps have been discontinued and are no longer served for any date, so intraday liquidation history is not available from Binance's public archive.

## Signal construction
Use the stream as an indicator, not a measurement. Practical handling:
- Treat each message as "at least one liquidation of at least this size occurred on this side in this second". Count of active seconds per minute and the maximum size per second are more robust features than summed notional.
- Estimate true forced flow from quantities that are fully reported: the drop in open interest over the interval combined with signed taker volume from the trade stream. An open interest decline that coincides with one-sided aggressive selling is the signature of long liquidations.
- When aggregating across venues, do not add Binance stream totals to venues that report every liquidation, since the units are not comparable.

## Relevance to SOL perpetuals at minutes to hours
Binance is described in the Chitra paper as the largest centralized exchange, so its liquidation flow is likely the most important for SOL and is also incompletely observed; its share of SOL open interest was not measured in this session. A bot that trains on Binance liquidation totals will see a feature whose scale saturates exactly in the events it most needs to identify. The widely quoted market-wide liquidation totals for events such as October 2025 inherit the same undercount. The open-interest-based proxy has its own reporting problems at one-minute resolution (see the Giagkiozis and Said note), so the two should be cross-checked.

## Caveats
The documentation states the sampling rule but not how the "latest" order is chosen when several fill in the same window, nor whether the rule has changed over time. Other exchanges have different and also changing policies, which were not reviewed here. Vendor aggregates (Coinglass and similar) were not opened in this session, so how they treat this limitation is not confirmed.
