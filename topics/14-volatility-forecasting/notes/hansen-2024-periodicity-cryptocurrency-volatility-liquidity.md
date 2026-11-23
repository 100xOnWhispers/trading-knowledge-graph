---
title: "Periodicity in Cryptocurrency Volatility and Liquidity"
authors: "Hansen, Peter Reinhard; Kim, Chan; Kimbrough, Wade"
year: 2024
venue: "Journal of Financial Econometrics 22(1), 224-251 (read as arXiv 2109.12142v2, November 2021)"
url: "https://arxiv.org/pdf/2109.12142"
pdf: "sources/14-volatility-forecasting/hansen-2024-periodicity-cryptocurrency-volatility-liquidity.pdf"
access: "full-text"
source_type: "peer-reviewed"
evidence_grade: "A"
topic: "14-volatility-forecasting"
asset_class: "crypto"
horizon: "minutes"
tags: "intraday-periodicity, day-of-week, minute-of-hour, funding-times, egarch, volume, binance, coinbase"
---

## Key insight
Crypto volatility and volume have strong, stable calendar patterns at three scales: day of week, hour of day, and minute within the hour. The within-hour pattern (a burst in the first minute of each hour, smaller bursts every 15 and every 5 minutes) is new and has grown stronger over time. The authors attribute it to algorithmic trading and to perpetual-futures funding times. Building periodicity into a volatility model improves out-of-sample fit more than adding realized variance does.

## Method
Relative volatility and relative volume are computed for each calendar bin (weekday, hour, minute-of-hour) as the bin's share of the surrounding period, normalised so that a flat pattern equals one, with confidence bands. Minute-of-hour volatility uses absolute 1-minute returns relative to the other minutes of the same hour. For forecasting, daily GARCH, EGARCH and EGARCH-X (with 5-minute realized variance) are extended with day-of-week terms in the variance equation, estimated on an in-sample period and scored by Gaussian log-likelihood out of sample with parameters held fixed.

## Data and sample
BTC and ETH on Binance (USDT pairs) and Coinbase Pro (USD pairs), and WETH/USDC on Uniswap V2. 1-minute OHLCV and trade data. Main sample 1 October 2020 to 1 June 2021; extended centralized-exchange sample from 1 January 2019. GARCH exercise: in-sample 2017 to 2019, out-of-sample 1 January 2020 to 31 July 2021.

## Reported results
- Volatility and volume are lower at weekends, most on Saturdays. Volume is more concentrated than volatility.
- Volatility peaks around 16:00 UTC and bottoms near 05:00 UTC. Spikes in volume and volatility at 00:00 and 16:00 UTC, smaller at 08:00, coincide with Binance funding times.
- Within the hour: a large burst in the first minute, medium bursts after minutes 15, 30 and 45, small bursts every five minutes. The effect is strongest every fourth hour (00h to 20h, except 08h).
- BTC/USD: adding periodicity improves log-likelihood by about 19 units in-sample and about 34 out-of-sample; adding realized variance improves it by about 5 and 18. ETH/USD periodicity gains are about 15 and 11.
- The EGARCH asymmetry (leverage) parameter is insignificant in all models.
- Uniswap V2 prices adjust sluggishly; price formation happens on centralized exchanges.

## Signal construction
Build a multiplicative seasonal factor s(weekday, hour, minute) from trailing data: the average absolute (or squared) 1-minute return in that bin divided by the overall average, re-estimated on a rolling window of several months. Then (a) deseasonalise returns before computing RV, bipower variation or jump tests; (b) multiply the baseline volatility forecast by the factor for the upcoming interval; (c) treat volatility that merely matches the factor as expected, and only volatility in excess of it as news.

## Relevance to SOL perpetuals at minutes to hours
Highly relevant. Kalshi's SOL perp has 8-hour funding, so funding-time bursts should be expected there and on the venues that lead it. The factor table must be re-estimated for SOL, for 2026 market structure, and for the US-hours tilt a CFTC-regulated venue is likely to have (Coinbase showed far less volume during North American night). A hard-coded schedule from 2021 data should not be assumed to hold.

## Caveats
BTC and ETH only, with the core sample covering eight months of a bull market. Forecast evaluation is at the daily level with day-of-week effects only; intraday periodic forecasting is argued for, not tested. The funding-time explanation is a conjecture. Two authors disclose paid consulting for the third author's firm.
