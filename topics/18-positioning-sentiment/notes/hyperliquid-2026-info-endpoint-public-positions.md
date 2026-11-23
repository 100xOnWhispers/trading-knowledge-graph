---
title: "Hyperliquid Docs: Info endpoint, Perpetuals (clearinghouseState and related queries)"
authors: "Hyperliquid"
year: 2026
venue: "hyperliquid.gitbook.io (API documentation, fetched 2026-11-22)"
url: "https://hyperliquid.gitbook.io/hyperliquid-docs/for-developers/api/info-endpoint/perpetuals"
pdf: "none"
access: "full-text"
source_type: "documentation"
evidence_grade: "B"
topic: "18-positioning-sentiment"
asset_class: "crypto"
horizon: "minutes"
tags: "hyperliquid, public-positions, clearinghousestate, wallet-level-data, leverage, liquidation-price, api"
---

## Key insight
Hyperliquid exposes any wallet's perpetual positions through a public, unauthenticated API call. For a given address the response includes position size and direction, entry price, leverage, liquidation price, margin used, unrealized profit and cumulative funding. This makes true wallet-level positioning observable, which no centralized exchange offers, and is the data foundation for cohort-based positioning measures (by account size, by past profitability, by trader type).

## Method
All queries are POST requests to `https://api.hyperliquid.xyz/info` with a `type` field. Relevant request types documented on the page:
- `clearinghouseState` (requires `user`): returns `assetPositions`, each with `coin`, `szi` (signed size), `entryPx`, `leverage` (`type`, `value`, `rawUsd`), `liquidationPx`, `marginUsed`, `maxLeverage`, `positionValue`, `returnOnEquity`, `unrealizedPnl`, `cumFunding`; plus `marginSummary` and `crossMarginSummary` (`accountValue`, `totalMarginUsed`, `totalNtlPos`, `totalRawUsd`), `crossMaintenanceMarginUsed`, `withdrawable`, `time`.
- `metaAndAssetCtxs`: per-asset `markPx`, `midPx`, `oraclePx`, `funding`, `openInterest`, `premium`, `impactPxs`, `dayNtlVlm`, `prevDayPx`.
- `userFunding` and `userNonFundingLedgerUpdates`: a wallet's funding payments and deposits, withdrawals and transfers.
- `activeAssetData` (requires `user` and `coin`): leverage, maximum trade sizes, available to trade, mark price.
- `fundingHistory`, `predictedFundings` (per coin, per venue including Binance and Bybit perps), `perpsAtOpenInterestCap`.
The page notes that for unified-account or portfolio-margin users the spot balances endpoint should be used instead for balances.

## Data and sample
Live state of the Hyperliquid perp clearinghouse, per wallet and per asset. The page does not provide a list of all wallets or a historical position archive; address discovery (from the trade stream, leaderboard, or third-party indexers) and snapshot storage are the user's responsibility. Rate limits are not stated on this page.

## Reported results
None. This is an interface specification. No evidence about predictive value is given.

## Signal construction
1. Build an address universe for SOL from public sources such as the trade feed, leaderboard or an indexer (whether the trade stream exposes counterparty addresses must be confirmed against the WebSocket documentation, which was not read here).
2. Poll `clearinghouseState` for each address on a schedule (for example every 5 to 15 minutes for the top few thousand by account value).
3. Tag wallets into cohorts: account value buckets, realized-profit history, and behaviour type (market maker, algorithmic taker, manual front-end) following Jia et al. (2026).
4. Per cohort compute net SOL exposure `sum(szi * markPx)`, long share of wallets, mean leverage, and the distribution of `liquidationPx` relative to mark.
5. Features: cohort net exposure change over 15 minutes to 4 hours; divergence between profitable-cohort and unprofitable-cohort net exposure; divergence between large-account and small-account net exposure.

## Relevance to SOL perpetuals at minutes to hours
High potential, unproven. Positions update continuously and can be read per wallet for any listed perp including SOL, so cohort positioning can be measured at the bot's horizon. The liquidation-price distribution overlaps with topic 04 and should be shared, not duplicated. The measure covers only Hyperliquid; a wallet's hedges on Binance or in spot are invisible, and price discovery for SOL is led by Binance (topic 05), so Hyperliquid positioning is a sample of the market, not the market.

## Caveats
One entity can spread positions across many wallets and sub-accounts, and vaults pool many users. Large traders know they are watched and can stage positions. Polling thousands of addresses may hit rate limits not documented on this page. Cohort ratios of the "smart money versus retail" kind are marketed by third-party dashboards; no independent test of their predictive power was found in this session. Documentation can change without notice.
