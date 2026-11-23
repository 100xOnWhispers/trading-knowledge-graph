---
title: "Periodicity in Cryptocurrency Volatility and Liquidity"
authors: "Hansen, Peter Reinhard; Kim, Chan; Kimbrough, Wade"
year: 2021
venue: "arXiv working paper 2109.12142 (v2, November 2021)"
url: "https://arxiv.org/pdf/2109.12142"
pdf: "sources/10-intraday-seasonality-crypto/hansen-2021-periodicity-crypto-volatility-liquidity.pdf"
access: "full-text"
source_type: "working-paper"
evidence_grade: "B"
topic: "10-intraday-seasonality-crypto"
asset_class: "crypto"
horizon: "minutes"
tags: "periodicity, minute-of-hour, funding-timestamps, hour-of-day, day-of-week, binance, coinbase, uniswap, periodic-egarch"
---

## Key insight
Volatility and volume in BTC and ETH are periodic at three scales: day of week, hour of day, and minute (even second) within the hour. The within-hour pattern is the new finding: a burst in the first minute of every hour, smaller bursts after minutes 15, 30 and 45, and ripples every five minutes, strongest at the hours when perpetual futures pay funding. The patterns grew stronger from 2019 to 2021, and adding day-of-week periodicity to a GARCH model improves out-of-sample fit.

## Method
Relative measures: for each slot, the ratio of absolute return (or volume) to its average over the preceding week, day or hour, averaged across the sample, so a value of one means "no pattern". For example, minute-of-hour volatility within a given hour is

R_h(m) = average over days of |y(h,m)| / ((1/60) * sum over the 60 minutes of that hour of |y(h,i)|).

An hourly Amihud ratio (sum of absolute 1-minute returns over volume) relative to its trailing 24-hour mean measures illiquidity. A periodic EGARCH and EGARCH-X (with realised variance) add weekday effects to the variance equation; estimated on 2017 to 2019 and scored by log-likelihood on January 2020 to July 2021.

## Data and sample
1-minute OHLCV and trade data for BTC/USDT and ETH/USDT (Binance), BTC/USD and ETH/USD (Coinbase Pro), and per-block WETH/USDC (Uniswap V2). Main sample 1 October 2020 to 1 June 2021 UTC; extended CEX sample from 1 January 2019; second-by-second data for the CEX pairs.

## Reported results
- Volatility and volume are lower on weekends, most of all on Saturdays; volume varies more than volatility.
- Volatility is highest around 16 UTC and lowest near 5 UTC on all three venues. Spikes in volume and volatility at 00h and 16h, weaker at 08h, on every exchange and both assets.
- The first hour of the UTC day is especially volatile on Mondays.
- Binance illiquidity is about 30% above average during the East Asian night; Coinbase illiquidity peaks at 10:00 UTC and ranges from about 80% to nearly 150% of average. Uniswap never deviates more than 5%.
- First minute of the hour has the largest volatility burst; peaks every 15 minutes, smaller every 5. The effect is most pronounced every fourth hour (00h to 20h) except 08h. Funding occurred at 00/08/16h on Binance, hourly on FTX, and 04/12/20h on BitMEX.
- Second-level data: a volume spike at the first second of the hour that fades over minutes; on Binance a similar spike at the half hour in 2020 and 2021; on Coinbase the largest spike 20 minutes into the hour.
- Periodic model improves log-likelihood for BTC/USD by about 19 units in-sample and 34 out-of-sample; ETH/USD about 15 and 11.
- CEX returns predict Uniswap returns up to about 12 minutes ahead.

## Signal construction
Not a directional signal by itself. Build three multiplicative volatility seasonals for the target contract: weekday factor, hour-of-day factor, minute-of-hour factor (each as the ratio above, estimated on a rolling window). Deseasonalised volatility = realised |r| / (product of factors). Use the factors to (a) normalise any breakout or z-score trigger so a top-of-hour burst is not mistaken for news, (b) widen stops and reduce size in the first one to two minutes after :00, :15, :30, :45 and around funding hours, (c) feed a periodic volatility forecast.

## Relevance to SOL perpetuals at minutes to hours
Directly relevant: bar-close and funding-time clustering is a property of how participants and algorithms schedule trades, so it should appear on SOL perps at Binance, Bybit, OKX and Hyperliquid (hourly funding) and leak to Kalshi. Kalshi's 8-hour funding timestamps may differ from offshore venues; check whether SOL volatility bursts follow offshore funding hours, Kalshi's own, or both.

## Caveats
Eight-month main sample in a bull market; BTC and ETH only; FTX no longer exists. The funding explanation is a conjecture, not tested. No return predictability is claimed. The first two authors disclose paid consulting for the third author's firm.
