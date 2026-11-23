---
title: "Pressure Points: Liquidation Heatmaps & Market Bias"
authors: "Manrique de Lara Martin, Antonio; Glassnode"
year: 2025
venue: "Glassnode Research (Product & Research), 23 September 2025"
url: "https://research.glassnode.com/liquidation-heatmaps/"
pdf: "none"
access: "full-text"
source_type: "industry-research"
evidence_grade: "D"
topic: "04-open-interest-liquidations"
asset_class: "crypto"
horizon: "hours"
tags: "liquidation-heatmap, hyperliquid, positioning, liquidation-levels, vendor-research"
---

## Key insight
Glassnode introduces liquidation heatmaps built from actual on-chain positions on Hyperliquid instead of from assumed leverage tiers. Because every Hyperliquid position is public, the liquidation price of each large position can be placed on a price grid and aggregated into "liquidation walls". The article proposes that these clusters indicate where forced flow will appear on other venues too, but supports the claim only with a visual comparison.

## Method
As described on the page: the largest open BTC positions on Hyperliquid are tracked with their size, average entry price and persistence. Estimated liquidation levels are aggregated by price and displayed over spot candles, with brighter bands marking heavier concentrations of at-risk notional. A cumulative "liquidation walls" profile shows long liquidations below spot and short liquidations above. Companion charts show long-short bias of large traders and cost-basis heatmaps by entry price. The page does not disclose the formula, leverage assumptions or maintenance-margin rules used to estimate liquidation prices.

## Data and sample
Hyperliquid BTC perpetual positions. The article states Hyperliquid holds about 16% of global open interest and that the tracked positions cover about 90% of liquidatable BTC open interest on the venue at the time of writing. Binance, BitMEX, Bybit and OKX appear only as the source of realized short-liquidation totals for comparison. No sample period is stated.

## Reported results
- The only validation is a side-by-side visual comparison of Hyperliquid liquidation clusters with aggregate short liquidations on four centralized exchanges over four shaded periods. The article says larger clusters coincided with larger liquidation spikes and smaller clusters with muted activity.
- No correlation, hit rate, lead-lag analysis or statistical test is reported.
- No test of whether clusters predict price direction or magnitude is presented; one narrated example is shown.
- Language is hedged: the bands "may serve as a useful proxy" for where broader market liquidations occur.

## Signal construction
For SOL on Hyperliquid a bot can build the same object from public data without a vendor: pull open positions for the largest accounts through the public API, compute each position's liquidation price with the venue formula (see the Hyperliquid documentation note), and sum notional into price buckets, for example 0.25% wide. Derived features: liquidatable long notional within x% below mark, liquidatable short notional within x% above mark, and their ratio to current book depth. Refresh every few minutes. For venues without public positions, any heatmap is a model output based on assumed entry prices and leverage tiers and should be treated as a hypothesis.

## Relevance to SOL perpetuals at minutes to hours
The construction is useful; the predictive claim is unproven. Three issues need testing before use: whether Hyperliquid positions represent the positioning on Binance, Bybit and OKX where most SOL open interest sits; whether cross-margin accounts make single-position liquidation prices unstable as other positions move; and whether proximity of a cluster raises the probability that price reaches it or only the size of the move if it does. The branching-ratio study in this topic names the liquidation map as an untested candidate, which is consistent with the question being open.

## Caveats
Vendor article promoting a product, with no disclosed methodology and no quantitative validation. One venue with a minority share of open interest. Position data are public, so large traders can see and trade against the same map. The charts themselves could not be inspected, only the text describing them.
