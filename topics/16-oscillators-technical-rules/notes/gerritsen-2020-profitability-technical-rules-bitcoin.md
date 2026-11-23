---
title: "The profitability of technical trading rules in the Bitcoin market"
authors: "Gerritsen, Dirk F.; Bouri, Elie; Ramezanifar, Ehsan; Roubaud, David"
year: 2020
venue: "Finance Research Letters 34, 101263"
url: "https://dspace.library.uu.nl/bitstream/handle/1874/407735/1_s2.0_S1544612319303770_main.pdf"
pdf: "sources/16-oscillators-technical-rules/gerritsen-2020-profitability-technical-rules-bitcoin.pdf"
access: "full-text"
source_type: "peer-reviewed"
evidence_grade: "B"
topic: "16-oscillators-technical-rules"
asset_class: "crypto"
horizon: "daily"
tags: "bitcoin, rsi, bollinger-bands, macd, trading-range-breakout, rate-of-change, on-balance-volume, sharpe-ratio"
---

## Key insight
A head-to-head test of the indicators retail traders actually use, at their textbook settings, on daily Bitcoin. Only the trading range breakout beats buy-and-hold on Sharpe ratio. The two counter-trend oscillators, RSI(70/30) and Bollinger Bands(20,2), significantly underperform buy-and-hold and sometimes have negative Sharpe ratios. On daily Bitcoin, fading overbought readings was a losing trade.

## Method
Seven rule families with pre-specified, well-publicized parameters, chosen to limit data snooping:
- Moving averages: 1, 2 or 5-day average against 50, 150 or 200-day average.
- Trading range breakout: new high or low over 50, 150 or 200 days.
- MACD: three signals (MACD line, signal line, histogram).
- Rate of change over 10 days.
- On-balance volume with MA rules applied to it.
- RSI: sell above 70, buy below 30.
- Bollinger Bands (20, 2).
Each is applied three ways: long/short on signals; long-only with the risk-free asset otherwise; and a default long position that doubles on a buy signal and exits on a sell signal. Performance is the daily Sharpe ratio, compared with buy-and-hold using the Ledoit and Wolf bootstrap test (1,000 resamples).

## Data and sample
Daily Bitcoin prices from 17 July 2010 to 31 December 2018 (3,084 observations): Mt. Gox initially, CoinMarketCap from 28 April 2013. Rules run from February 2011 after the 200-day warm-up. Volume is available only from end-2013.

## Reported results
- Buy-and-hold daily Sharpe ratio: 0.056 (the paper annualizes this to 1.07).
- Trading range breakout: Sharpe around 0.08 on average across settings and strategies, with a statistically significant difference from buy-and-hold in most cases.
- Moving averages: mostly not different from buy-and-hold. Example: MA(1,200) long/short has a Sharpe of 0.047, p = 0.65.
- MACD and rate of change: significant outperformance only in the long-only strategy.
- RSI and Bollinger Bands: significantly below buy-and-hold, with negative Sharpe ratios in some cases.
- On-balance volume: below buy-and-hold, not significant.
- Subperiod analysis: the breakout rule's advantage appears in strongly trending markets.
- Transaction costs are not included; the authors list this as future work.

## Signal construction
Breakout: long when close exceeds the maximum close of the prior n bars, short (or flat) when below the minimum; n = 50, 150, 200 in the paper. RSI rule (as tested, and as it failed): short when RSI exceeds 70, long when below 30; the RSI look-back length is in the paper's appendix, which I did not read closely. Bollinger rule: fade closes outside the 20-period mean plus or minus two standard deviations.

## Relevance to SOL perpetuals at minutes to hours
The sign of the oscillator result is the useful part, and it conflicts with the intraday evidence. On daily bars in a trending asset, overbought readings marked continuation. At 5-minute bars (Bakker) contrarian Bollinger and RSI rules were the best performers before costs. So the correct sign of an RSI or band signal on SOL probably depends on bar size, with a crossover horizon somewhere between minutes and days that has to be estimated. The breakout result supports using multi-day highs and lows as trend context for intraday decisions.

## Caveats
No costs, no multiple-testing correction beyond using standard settings, one asset, and a sample dominated by a few large bull runs. Short positions in Bitcoin were not actually available for much of the period. Early Mt. Gox prices are unreliable. Sharpe ratios on daily crypto returns are fragile to a handful of extreme days.
