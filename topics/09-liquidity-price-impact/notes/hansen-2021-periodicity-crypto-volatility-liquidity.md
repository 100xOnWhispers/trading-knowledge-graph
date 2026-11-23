---
title: "Periodicity in Cryptocurrency Volatility and Liquidity"
authors: "Hansen, Peter Reinhard; Kim, Chan; Kimbrough, Wade"
year: 2021
venue: "arXiv:2109.12142v2 (listed by EconPapers as published in Journal of Financial Econometrics 22(1), 2024, 224-251)"
url: "https://arxiv.org/pdf/2109.12142"
pdf: "sources/09-liquidity-price-impact/hansen-2021-periodicity-crypto-volatility-liquidity.pdf"
access: "full-text"
source_type: "working-paper"
evidence_grade: "B"
topic: "09-liquidity-price-impact"
asset_class: "crypto"
horizon: "minutes"
tags: "intraday-seasonality, liquidity-around-the-clock, funding-times, volatility, volume, amihud"
---

## Key insight
Crypto trades around the clock but its volatility, volume and illiquidity are far from uniform. There are stable patterns by day of week, hour of day and minute of the hour, and they have strengthened over time. Spikes at 00:00, 08:00 and 16:00 UTC line up with perpetual-futures funding times, and bursts at the top of each hour and every 15 and 5 minutes point to algorithmic trading.

## Method
From 1-minute returns and volumes the authors compute relative measures: the share of volatility (sum of absolute returns) or volume falling in a given weekday, hour or minute, divided by its average, so a uniform market gives 1. An hourly relative illiquidity measure follows Amihud: sum of absolute 1-minute returns in the hour divided by volume in the hour, relative to the average of the preceding 24 hours. They also add periodic components to GARCH-type models of daily returns and compare in-sample and out-of-sample log-likelihoods.

## Data and sample
BTC and ETH on Binance (USDT pairs) and Coinbase Pro (USD pairs), and WETH/USDC on Uniswap V2. Detailed sample 1 October 2020 to 1 June 2021; extended sample from 1 January 2019. Volatility models use 1 January 2017 to 31 July 2021, with 2020 onward held out.

## Reported results
- Volatility and volume are lower on weekends, most clearly on Saturdays. Volume varies more than volatility.
- Volatility is highest around 16 UTC and lowest near 5 UTC.
- Volume and volatility spike at 0h and 16h UTC, less so at 8h, on all exchanges for both coins.
- Binance relative illiquidity is about 30% higher during the East Asian night. Coinbase Pro illiquidity peaks at 10:00 UTC and ranges from about 80% to nearly 150% of average. The authors caution that these differences are driven by volume and do not mean price impact is larger on Coinbase at that hour.
- Within the hour: a large volatility burst in the first minute, medium bursts after minutes 15, 30 and 45, and smaller bursts every five minutes. The effect is strongest every fourth hour (00h to 20h) except 08h.
- Adding periodicity to the BTC/USD volatility model improves log-likelihood by about 19 units in-sample and about 34 out-of-sample; for ETH/USD by roughly 15 and 11.
- Uniswap V2 prices lag the centralized exchanges by several minutes.

## Signal construction
Build seasonal multipliers for SOL: for each (weekday, hour, minute-of-hour) cell, the trailing 8 to 12 week average of absolute 1-minute return and of volume, divided by the overall average. Use them to (a) deseasonalize volatility, volume and liquidity features before they enter any model, (b) scale expected impact and stop distances by time of day, and (c) flag known thin windows. Refresh weekly.

## Relevance to SOL perpetuals at minutes to hours
Directly relevant. Kalshi's 8-hour funding puts its settlement times on a clock that may or may not coincide with the 00/08/16 UTC schedule on offshore venues; either way, volatility bursts at those times will arrive through the reference price. A US-regulated venue should have a Coinbase-like hour-of-day liquidity profile, with thin books in the US night, while price discovery continues on Binance. The patterns must be re-estimated for SOL and for 2025 to 2026; funding schedules have changed since 2021 (the paper mentions hourly funding on FTX, which no longer exists).

## Caveats
BTC and ETH only, eight months of detailed data during a bull market. Illiquidity here is an Amihud-type ratio, not spread or depth. The link to funding times and algorithmic trading is conjecture by the authors, not a causal test. The preprint was read, not the journal version.
