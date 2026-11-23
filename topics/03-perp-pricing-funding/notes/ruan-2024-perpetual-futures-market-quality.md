---
title: "Perpetual Futures Contracts and Cryptocurrency Market Quality"
authors: "Ruan, Qihong; Streltsov, Artem"
year: 2024
venue: "Working paper, Cornell University; the copy read is an anonymised AFA conference submission with no date printed (other papers cite it as 2022 or 2024)"
url: "https://afajof.org/management/viewp.php?n=169764"
pdf: "sources/03-perp-pricing-funding/ruan-2024-perpetual-futures-market-quality.pdf"
access: "full-text"
source_type: "working-paper"
evidence_grade: "B"
topic: "03-perp-pricing-funding"
asset_class: "crypto"
horizon: "hours"
tags: "funding-cycle, seasonality, settlement-timestamp, vpin, spreads, volume, informed-trading"
---

## Key insight
Trading activity and liquidity follow a U-shape inside each 8-hour funding cycle, in the perp market and in the spot market. Volume rises by more than half in the hour before and after a funding timestamp, spreads widen and order-flow toxicity rises. The effect grows with the size of the funding rate, in either direction.

## Method
Market-quality measures in 5-minute bins: dollar volume, percent quoted spread, order imbalance, and VPIN (volume-synchronised probability of informed trading) with windows of 25 minutes, 1 hour and 2 hours. Panel regression `Quality(e,i,t) = b*D(t) + exchange-token FE + 8-hour-window FE`, where `D` marks hours around funding times. Dose-response versions replace `D` with the lagged average funding-rate proxy or its absolute value, and split by funding quintile. Causal designs: Huobi's forced termination of perps in October 2021 (synthetic control) and 95 staggered perp listings on Binance, OKEX and Huobi from December 2019 to September 2022 (Callaway-Sant'Anna).

## Data and sample
Kaiko trades and order-book snapshots, more than 100 USDT pairs on 10 exchanges (Coinbase, Binance, Huobi, OKEX, Bybit, KuCoin, Bibox, Bitfinex, BitMEX, HitBTC), July 2017 to July 2023.

## Reported results
- Perp volume is more than 50% higher one hour before and after funding times than mid-cycle; a test rejects uniform volume at the 1% level.
- Spot volume rises by over 50% in settlement hours, spot spreads widen 3.2% and VPIN rises 17.4%. Order imbalance falls around settlement.
- Effects are strongest in the lowest and highest funding quintiles. A one-percentage-point rise in funding magnitude is associated with 3.9 points more informed-trading probability and 12.2 points wider spreads.
- Informed-trading probability is 31% higher in perp than in spot markets.
- Removing perps (Huobi) lowers spot volume and narrows spreads; listing perps does the reverse.

## Signal construction
Clock features, not a direction signal: minutes to next funding timestamp (00:00, 08:00, 16:00 UTC on 8-hour venues), an indicator for the hour either side, and the interaction with the absolute predicted funding rate. Use them to scale expected spread, slippage and volatility, and to gate entries.

## Relevance to SOL perpetuals at minutes to hours
Directly relevant to execution on an 8-hour venue: liquidity is worse and flow more informed around settlement, more so when funding is extreme. The paper does not report signed returns around the timestamp, so "price drifts against the paying side before settlement" remains an untested hypothesis. Whether Kalshi's settlement times coincide with offshore timestamps, and whether the U-shape appears there, must be measured. Hourly-funding venues (Hyperliquid) are not in the sample.

## Caveats
Working paper. The time-of-day confound is addressed only by the global mix of exchanges. Results are averages over 100 tokens and six years; SOL-specific estimates are not reported. Interpretation as "informed trading" rests on VPIN, a contested measure.
