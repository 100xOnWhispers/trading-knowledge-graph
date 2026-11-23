---
title: "Perpetual Futures Contracts and Cryptocurrency Market Quality"
authors: "not confirmed (anonymized conference draft)"
year: 2025
venue: "American Finance Association conference submission (draft dated June 2025)"
url: "https://afajof.org/management/viewp.php?n=169764"
pdf: "sources/10-intraday-seasonality-crypto/anonymous-2025-perpetual-futures-funding-cycle-market-quality.pdf"
access: "full-text"
source_type: "working-paper"
evidence_grade: "B"
topic: "10-intraday-seasonality-crypto"
asset_class: "crypto"
horizon: "hours"
tags: "funding-timestamps, eight-hour-cycle, perpetual-futures, volume, quoted-spread, vpin, informed-trading"
---

## Key insight
The eight-hour funding clock of perpetual futures imprints a U-shape on both perpetual and spot markets. In the hour around each funding settlement, volume is about 50% higher, quoted spreads are about 3% wider and order-flow toxicity (VPIN) is about 17% higher than mid-cycle, and the effect grows with the size of the funding rate. Funding timestamps are therefore scheduled bursts of informed and arbitrage trading, not noise.

## Method
Hourly panel regressions of market-quality measures on a funding-window indicator with exchange-token and eight-hour-window fixed effects, standard errors clustered by exchange-token:

MarketQuality(e,i,t) = b D_t + g(e,i) + eta_t + error,

where the outcome is measured relative to the non-funding average just before the funding time and D_t marks the first hour after funding, or windows of one or two hours either side. Measures: dollar volume, time-weighted percentage quoted spread from order-book snapshots, order imbalance, and VPIN on 5-minute buckets (5-, 12- and 24-bucket windows). Further tests: funding-rate quintiles, the October 2021 termination of perpetuals on Huobi (synthetic-control difference-in-differences), and 95 staggered perpetual listings.

## Data and sample
Kaiko trades and order-book snapshots for more than 100 USDT pairs on ten exchanges (Coinbase, Binance, Huobi, OKEX, Bybit, KuCoin, Bibox, Bitfinex, BitMEX, HitBTC), July 2017 to July 2023.

## Reported results
- Perpetual volume rises by more than 50% in the hour before and after funding times relative to mid-cycle; a uniform distribution of volume over the cycle is rejected at 1%.
- Spot market, first hour after funding: dollar volume +50.4%, quoted spread +3.1%, VPIN +17.4% (5-bucket) and +13.6% (12-bucket), order imbalance -4.5%. All significant at 1%.
- Windows of one and two hours either side: volume +37.3% and +37.8%; spread +2.4% and +3.0%.
- Effects are stronger in the lowest and highest funding-rate quintiles than in the middle one. A one percentage point larger funding-rate magnitude is associated with 3.9 and 12.2 percentage point larger funding-time effects on informed-trading probability and spread.
- Perpetual markets average $8.8 million per exchange-token-hour against $128,000 in spot, with 14% wider percentage spreads and 31% higher VPIN.
- Listing a perpetual raises spot volume and widens spot spreads; Huobi's termination did the reverse.

## Signal construction
Inputs: the funding timestamps of the lead venues (00:00, 08:00, 16:00 UTC on Binance and most others; hourly on Hyperliquid) and the current predicted funding rate. Features: minutes to next funding, minutes since last funding, and |predicted funding rate| interacted with a funding-window flag. Use them to raise expected volatility, expected spread and adverse-selection risk within about one hour of settlement, more so when |funding| is large. The paper does not test a directional rule.

## Relevance to SOL perpetuals at minutes to hours
Directly relevant: the sample is a broad altcoin panel, and Kalshi's SOL perpetual has its own 8-hour funding. Two things need testing: whether Kalshi's funding times coincide with offshore times, and whether price drifts against the paying side before settlement (the paper measures activity and toxicity, not return direction).

## Caveats
The copy read is an anonymized conference draft; the author names do not appear in the file and could not be confirmed in this session (SSRN returned an access error). No return predictability or strategy is shown. 00:00 and 16:00 UTC funding times coincide with the UTC day roll and the US afternoon, which the fixed effects only partly separate. Sample ends July 2023.
