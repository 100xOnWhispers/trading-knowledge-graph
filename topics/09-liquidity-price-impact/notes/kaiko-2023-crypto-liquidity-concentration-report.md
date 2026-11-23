---
title: "The Crypto Liquidity Concentration Report"
authors: "Kaiko Research (individual authors not stated on the page)"
year: 2023
venue: "Kaiko Research"
url: "https://www.kaiko.com/resources/the-crypto-liquidity-concentration-report"
pdf: "none"
access: "full-text"
source_type: "industry-research"
evidence_grade: "C"
topic: "09-liquidity-price-impact"
asset_class: "crypto"
horizon: "daily"
tags: "market-depth, liquidity-concentration, exchange-fragmentation, altcoins, order-book"
---

## Key insight
Crypto liquidity is concentrated in a handful of exchanges and has become more concentrated over time. Depth and volume do not concentrate in the same way: one venue can hold most of the volume without holding most of the resting depth. For altcoins, most depth sits offshore and in the top ten assets.

## Method
Kaiko aggregates trade and order-book data across exchanges using its Asset Liquidity Metrics product. Market depth is the sum of bids and asks within a percentage band of the mid price; the order-book data capture orders within 10% of the mid, so depth can be reported at 0.1%, 1%, 2% and 4% bands. The report computes average 1% depth and cumulative trade volume for BTC, ETH and the top 30 assets by market capitalization, converted to US dollars and broken down by exchange. The page was read as extracted text; chart values were not available.

## Data and sample
More than 100 centralized and decentralized exchanges; BTC, ETH and the top 30 altcoins; 2023 figures compared with 2021 and with the previous year. The page shows a date of 07/09/2023 (most likely 7 September 2023).

## Reported results
- In 2023 Binance held 30.7% of global market depth and 64.3% of global trade volume.
- The top 8 platforms held 91.7% of depth and 89.5% of volume.
- Binance's volume share rose from 38.3% in 2021 to 64.3%, which the report links partly to its zero-fee promotion, while its depth share fell from 42% to 30.7%.
- Depth at 0.1% recovered more after the FTX collapse than depth in wider bands; 1%, 2% and 4% depth stayed mostly flat since November (figures only in charts).
- Offshore exchanges' share of altcoin depth rose from 65% to 71% year on year.
- Among exchanges available in the US, altcoin depth is concentrated on Coinbase, Kraken and Bitstamp.
- Binance's altcoin depth fell by more than 10 million US dollars year on year.
- SOL is not discussed individually on the page.

## Signal construction
Not a signal. It defines the depth metrics a bot should record from live books:
1. Depth_x = sum of bid and ask notional within x% of mid, for x in {0.1, 0.5, 1, 2}, per venue, sampled every few seconds and averaged per minute.
2. Depth share by venue = venue depth divided by total across tracked venues.
3. Volume-to-depth ratio per venue, to detect venues where traded volume is large relative to resting liquidity.
Changes in these, relative to same-hour history, are the liquidity-state inputs.

## Relevance to SOL perpetuals at minutes to hours
The gap between volume share and depth share is the practical lesson: a venue's reported volume says little about how much size its book can absorb. For Kalshi, the bot should measure depth directly and expect it to be a small fraction of the depth on Binance, Bybit, OKX or Hyperliquid, where price discovery will happen. The finding that US-accessible altcoin depth sits on a few venues suggests Coinbase is the relevant US spot reference for SOL. All numbers are from 2023 spot markets and are out of date; perps and Hyperliquid are not covered.

## Caveats
Vendor research that promotes the vendor's own data product. No statistical tests. Depth snapshots can be inflated by orders that are cancelled before they can be hit. The figures predate the 2024 to 2026 changes in market structure, including US spot ETFs and regulated US perpetuals. Authors are not named.
