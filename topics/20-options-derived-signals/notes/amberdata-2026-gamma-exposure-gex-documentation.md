---
title: "Amberdata derivatives documentation: Gamma Snapshots (GEX), Gamma Normalized in USD, Decorated Trades and Volatility Index VRP"
authors: "Amberdata"
year: 2026
venue: "Amberdata API documentation (docs.amberdata.io)"
url: "https://docs.amberdata.io/data-dictionary/analytics/derivatives/gamma-normalized-snapshots.md"
pdf: "none"
access: "full-text"
source_type: "documentation"
evidence_grade: "C"
topic: "20-options-derived-signals"
asset_class: "crypto"
horizon: "daily"
tags: "gamma-exposure, gex, dealer-positioning, trade-classification, deribit, vendor-data, variance-risk-premium"
---

## Key insight
The main commercial crypto gamma-exposure series is built from signed trades, not from open interest with a fixed assumption about who is long. Every option trade is classified by aggressor using order-book state around the trade, the passive side is assumed to be a market maker, and a running market-maker position is kept per strike and expiry. This differs from the equity-style calculation in [squeezemetrics-2017-gamma-exposure-gex](squeezemetrics-2017-gamma-exposure-gex.md), whose sign convention has no basis in crypto.

## Method
From four documentation pages read in this session:
- **Decorated Trades**: option time-and-sales "decorated with pre-trade level-1 orderbook data and post-trade level-1 data"; described as "the core dataset of the Amberdata direction and GEX" analysis. The vendor uses order-book impact "to analyze the true aggressor of every trade, while assuming that market-makers (aka 'dealers') are typically the passive trade participants".
- **Gamma Snapshots (GEX)**: aims to calculate "the gamma exposure of Market Makers (MMs) and the resulting number of underlying contracts they must trade to keep their book delta-hedged". Direction comes from a proprietary algorithm "composed of over 30 heuristics", tracking the order book "at millisecond level". Values are aggregated by strike.
- **Gamma Normalized in USD**: GEX expressed as notional in the underlying "for a 1% move in spot prices", summed across dealers.
- **Volatility Index VRP**: the Deribit DVOL index shifted to align with subsequently realized 30-day volatility, the latter measured with the Parkinson high-low estimator; positive means "options were over priced".

Stated interpretation: positive (long) gamma means more stability because dealers "buy low, sell high"; negative (short) gamma means more volatility because they "sell low, buy high".

## Data and sample
Availability table on the page: Deribit from 2019-08-23; Bybit, Lyra, Thalex and OKX from 2024-06-01; granularity listed as daily. Endpoint parameters accept `BTC` and `SOL_USDC` among currencies. The vendor's blog address redirected to a Kaiko news URL whose title announces an acquisition of Amberdata; that page was not opened.

## Reported results
None. The pages define data products and give no validation: no statistics on classification accuracy, and no test relating the series to realized volatility or returns.

## Signal construction
Either buy the series or rebuild it:
1. From the exchange trade feed and top-of-book before and after each trade, assign the aggressor.
2. Market-maker position per instrument: cumulative sum of minus the aggressor's signed size; drop expired instruments.
3. `GEX_usd_per_1pct = sum_i position_i * gamma_i * S^2 * 0.01` (this note's formula, consistent with the page's "notional for a 1% move"; the vendor's exact expression is not published on the pages read).
4. Features: sign of total GEX; GEX divided by recent perpetual volume; strike with the largest absolute GEX in the nearest expiry and its distance from spot.

## Relevance to SOL perpetuals at minutes to hours
The BTC series is the one with a plausible mechanism, supported at abstract level by [atanasova-2025-aggregate-illiquidity-crypto-option-returns](atanasova-2025-aggregate-illiquidity-crypto-option-returns.md). Daily granularity limits it to a regime flag that conditions intraday momentum and reversal rules. The SOL_USDC series exists as a product, but with the open interest measured in [deribit-2026-option-book-summary-sol-liquidity](deribit-2026-option-book-summary-sol-liquidity.md) the implied hedging flow is small against SOL perpetual volume.

## Caveats
Vendor documentation: a description of a product by its seller, with a proprietary classifier that cannot be audited. The passive-side assumption fails when market makers take liquidity or when two customers trade a block. Positions opened on other venues or over the counter are invisible, and inventory errors accumulate over time. The history starts in 2019, when Deribit volume was small.
