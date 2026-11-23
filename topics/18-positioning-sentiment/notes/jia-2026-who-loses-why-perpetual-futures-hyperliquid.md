---
title: "Who Loses and Why? Market Microstructure of Perpetual Futures (extended abstract)"
authors: "Jia, Ruizhe; Moallemi, Ciamac C.; Wang, Shouqiao; Zeng, Xinmeng"
year: 2026
venue: "8th Conference on Advances in Financial Technologies (AFT 2026), LIPIcs vol. 395, article 36"
url: "https://drops.dagstuhl.de/storage/00lipics/lipics-vol395-aft2026/LIPIcs.AFT.2026.36/LIPIcs.AFT.2026.36.pdf"
pdf: "sources/18-positioning-sentiment/jia-2026-who-loses-why-perpetual-futures-hyperliquid.pdf"
access: "full-text"
source_type: "peer-reviewed"
evidence_grade: "B"
topic: "18-positioning-sentiment"
asset_class: "crypto"
horizon: "hours"
tags: "hyperliquid, retail-perp-traders, wallet-classification, trader-pnl, opening-trades, liquidations, fees, post-trade-impact"
---

## Key insight
Using every order and trade on Hyperliquid for its ten most active perps, the authors show that manual front-end traders (interpreted as mostly retail) lost USD 1.11 billion over about fifteen months, measured against the midprice two hours after each trade and net of fees. Most of the loss is fees, execution cost and forced liquidations, not adverse selection. For positioning signals the key finding is about direction: front-end traders open positions in the direction of recent returns, while market makers and algorithmic takers open against them, and price impact after front-end trades starts favourable and then decays.

## Method
Wallets are classified per coin-day into algorithmic market makers (two-sided, mostly post-only), algorithmic takers (high-frequency, sustained activity; 69% of volume takes liquidity) and front-end traders (identified mainly by market orders sent through the web interface, recorded by Hyperliquid as FrontendMarket orders). A residual 1.7% of volume is excluded. Each trade is marked to the midprice 120 minutes later, with fees separate. Profit and loss is split into three additive channels: voluntary trading (execution cost, post-trade price impact, maker income), net forced exits (liquidation losses less auto-deleveraging offsets), and fees. Voluntary taker trades are further split by purpose: opening, gain-realizing close, loss-realizing close.

## Data and sample
Hyperliquid on-chain orders, cancellations, trades and liquidations at millisecond resolution, 27 March 2025 to 30 June 2026, ten highest-volume perpetual contracts (not named in the extended abstract). Order and fill data from Allium, top-of-book from Tardis. 729,540 active wallets classified.

## Reported results
- Net of fees at the 120-minute mark: front-end traders -USD 1.11 billion; market makers +USD 208 million; algorithmic takers about break-even.
- Front-end loss by channel: USD 154 million voluntary trading, USD 226 million net forced exits, USD 725 million fees.
- Voluntary channel: USD 501 million execution cost, offset by USD 299 million of favourable post-trade price movement and USD 48 million maker income. Execution cost is 2.43 bps of taker volume for front-end traders, 1.70 for algorithmic takers, 0.70 for market makers.
- Post-trade price impact initially favours all three groups but subsequently declines only for front-end traders.
- By purpose: loss-realizing closes follow recent returns and revert for every group; gain-realizing closes are contrarian for every group; openings differ, with front-end traders opening with recent returns and the other groups opening against them.
- Forced exits: USD 344 million liquidation loss less USD 118 million returned by auto-deleveraging. Front-end traders are 96.0% of three-group liquidation volume. Liquidation trades pay roughly twenty times the voluntary half-spread.
- Fees: 2.99 bps of front-end volume; they cross the spread on 85% of volume against 20% for market makers.

## Signal construction
The paper does not build a signal. What it enables: from Hyperliquid's public data, tag fills as front-end market orders versus algorithmic flow per coin, then compute (a) net front-end opening flow over the last N minutes, signed; (b) front-end loss-realizing close flow; (c) liquidation flow. The findings suggest front-end opening flow is trend-chasing with impact that fades within two hours, so a candidate feature is the gap between front-end net opening flow and algorithmic net opening flow. Horizon to test: 15 minutes to 2 hours. Predictive value is not reported.

## Relevance to SOL perpetuals at minutes to hours
This is the closest evidence to the target problem: a perp venue, wallet-level data, a two-hour evaluation horizon, 2025 to 2026. If SOL is among the ten contracts (likely but not confirmed), the classification can be applied directly. It also quantifies the cost of being an aggressive taker: a bot that crosses the spread in size on most trades inherits the front-end cost profile. Kalshi offers no wallet-level data, so the signal must be computed on Hyperliquid and carried across.

## Caveats
Only the three-page extended abstract was read; the full version is on SSRN (abstract 7270041) and was not accessed. No coin-level results, no standard errors, and no test of whether fading front-end flow is profitable after costs. The 120-minute mark is one choice of horizon. Classification by order type may mislabel API users of the front end and bots using market orders. One venue with a distinctive user base and fee schedule.
