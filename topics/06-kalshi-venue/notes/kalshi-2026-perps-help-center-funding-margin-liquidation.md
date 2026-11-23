---
title: "Kalshi Help Center: Perpetual Futures collection (How Funding Works; How Margin Works; Understanding Liquidation; Order Types; BTC Contract Specifications; Risks; Applying for Access; Your Margin Account; Perps Fees Explained)"
authors: "Kalshi"
year: 2026
venue: "help.kalshi.com"
url: "https://help.kalshi.com/en/articles/15357613-how-funding-works"
pdf: "none"
access: "full-text"
source_type: "documentation"
evidence_grade: "C"
topic: "06-kalshi-venue"
asset_class: "crypto"
horizon: "n/a"
tags: "kalshi, funding, isolated-margin, liquidation, order-types, maintenance-window, fcm, retail-documentation"
---

## Key insight
The retail documentation confirms the starting facts for funding (8-hour intervals at 12:00 AM, 8:00 AM and 4:00 PM ET, zero below 0.01%, cap of 2% per interval) and describes margin, liquidation and account structure in plain terms. It gives no SOL-specific leverage number, and it describes the funding average differently from the CFTC filing and the API reference.

## Method
Nine help articles downloaded as markdown from the help center index (`help.kalshi.com/llms.txt`) and read in full. The front-matter URL is the funding article; the others sit in the same "Perpetual Futures" collection.

## Data and sample
Product documentation as served on 2026-11-22. Articles carry no dates or version numbers. A SOL contract-specification article does not exist in the index; only BTC has one.

## Reported results
- Funding: "a time-weighted average price (TWAP) of 1-minute candlestick premiums over the 480 candles" per 8-hour period. Clamp +2% / -2%. Zero threshold 0.01%. If the CF Benchmarks feed is unavailable, funding is paused. Funding is a transfer between traders, not a fee.
- Margin: isolated margin is the only mode in the app; portfolio margin is available via API. Initial margin follows the leverage selected. Variation margin is settled at about 12:00 PM and 4:00 PM ET, marked to "a fresh Volume Weighted Average Price".
- Leverage table in "Order Types" runs from 1x to 6x; 6x is described as about a 17% adverse move to liquidation. No per-asset caps are listed.
- Liquidation: triggered when equity falls below maintenance margin; Kalshi Klear "places opposing market orders"; a deficit goes to the clearinghouse waterfall, which includes a default fund. Liquidation references the mark price.
- Maintenance: Thursdays about 3:00 to 5:00 AM ET; the exchange is offline, the mark price does not change, and no liquidation occurs.
- Order types described: market and limit only; stop-loss and take-profit are covered in a separate article not read in full. A position cannot be closed while a resting limit order exists on it.
- Access: US users with KYC apply for a margin account; most retail users trade through Kalshi Prime, a registered FCM; institutions may become self-clearing members.
- Fees: charged on notional, on open and on close, tiered by volume; no rates are printed.
- Interest on margin: one article says about 3.25% APY, another says 3.50% APY and up to 7% on qualifying positions.
- BTC specification: index BRTI, 1-second updates, contract 0.0001 BTC, linear USD-margined.

## Signal construction
Not a signal. Used to configure the bot's venue model: funding timestamps, the Thursday maintenance blackout, the settlement times at which variation margin moves cash, and the rule that resting orders block position closes.

## Relevance to SOL perpetuals at minutes to hours
The maintenance window is a scheduled period when the bot cannot exit while offshore markets keep trading; positions held across it carry gap risk. Settlement at 12:00 PM and 4:00 PM ET uses a 60-second VWAP, so those minutes may attract price-setting flow. Collateral earning 3.25% to 3.50% offsets part of the opportunity cost of low leverage.

## Caveats
This is marketing-adjacent documentation and conflicts with primary sources in three places. First, the funding average: "TWAP of 480 one-minute candles" here, linearly weighted per-second premium in the CFTC filing, "time-weighted average of the premium index" in the API reference. Second, the APY figure differs between two articles. Third, the 1x to 6x table is generic and does not match the SOL leverage of about 3.1x to 3.6x reported by the API. Where they conflict, the CFTC filing and live API values should govern. The description of liquidation by market orders also differs from the API overview, which says exit triggers place limit orders.
