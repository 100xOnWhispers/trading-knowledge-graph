---
title: "Technical trading and cryptocurrencies"
authors: "Hudson, Robert; Urquhart, Andrew"
year: 2021
venue: "Annals of Operations Research 297, 191-220 (published online 2019)"
url: "https://centaur.reading.ac.uk/85715/8/Hudson-Urquhart2019_Article_TechnicalTradingAndCryptocurre.pdf"
pdf: "sources/16-oscillators-technical-rules/hudson-2021-technical-trading-cryptocurrencies.pdf"
access: "full-text"
source_type: "peer-reviewed"
evidence_grade: "A"
topic: "16-oscillators-technical-rules"
asset_class: "crypto"
horizon: "daily"
tags: "crypto, moving-average, filter, oscillator, channel-breakout, support-resistance, data-snooping, break-even-cost, out-of-sample"
---

## Key insight
The most comprehensive test of classical rules in crypto. Nearly 15,000 rules in five classes show significant in-sample predictability on daily data for Bitcoin, Litecoin, Ripple and Ethereum, and a large share survive multiple-testing corrections with break-even costs above typical crypto fees. The edge comes almost entirely from buy signals, and for Bitcoin the best in-sample rules lose money in the one true out-of-sample window.

## Method
14,919 rules following the Hsu, Taylor and Wang classes: moving averages (7,980 rules across five variants with band x, delay d and holding period k), filter rules, support-resistance, oscillators (overbought and oversold reversal rules), and channel breakouts. Rule return is the prior-day signal times the daily return. Metrics are annualized return, Sharpe, Sortino and Calmar ratios, and the break-even transaction cost. Data snooping is handled with family-wise error control (Bonferroni, Holm) and false-discovery-rate control (Benjamini-Hochberg, Benjamini-Yekutieli), with bootstrapped p-values. The best in-sample rule per coin is then run on a later period.

## Data and sample
Daily prices: Bitcoin from CoinDesk (from 18 July 2010) and Bitstamp (from 1 December 2012); Litecoin, Ripple and Ethereum (from 7 August 2015) from CoinMarketCap. In-sample ends 31 December 2017. Out-of-sample is the first six months of 2018.

## Reported results
- On average every rule class earns a significant annualized return in every coin. Filter and channel breakout rules do best, with class-average annualized returns up to 16.45% (Ripple).
- Average returns after buy signals are positive and significant. Average returns after sell signals are mostly negative but rarely significant: 15 of the 20 class-coin combinations have no rule with a significant sell-signal return. The authors attribute the profits to the buy side.
- Share of rules still significant at 5% after correction ranges from 20.35% to 50.41%. For CoinDesk Bitcoin: Bonferroni 33.61%, Holm 33.61%, BH 50.41%, BY 33.61%, against 57.65% uncorrected.
- Break-even costs: 36.06% of oscillator rules exceed 50 basis points for CoinDesk Bitcoin; 47.35% of channel breakout rules do for Ethereum. Support-resistance rules rarely do.
- Few rules beat buy-and-hold on raw return, but many do on Sortino and Calmar ratios, because the rules avoid long drawdowns.
- Out of sample (first half of 2018): negative annualized return, Sharpe and Sortino for both Bitcoin series; positive for Litecoin, Ripple and Ethereum.

## Signal construction
Generic forms, parameters from the paper's grid:
- MA: long when price (or MA(p)) exceeds MA(q) by x percent for d consecutive bars; q in {2, 5, 10, 15, 20, 25, 50, 100, 200}, x in {0, 0.01, 0.05, 0.1, 0.5, 1, 5} percent, d from 1 to 5.
- Channel breakout: long when price breaks above a time-varying resistance level built from recent highs, short below the matching support level. I read the MA part of the appendix in full but not the exact channel and oscillator definitions.
- Oscillator: fade overbought and oversold readings.
All run on daily closes; no intraday version is tested.

## Relevance to SOL perpetuals at minutes to hours
Supportive in two ways and cautionary in two. Less mature coins held up out of sample where Bitcoin did not, which favors SOL over BTC as a target. And the drawdown-avoidance property is useful for a leveraged product. Against that, the long-side concentration means these rules mostly captured the 2010 to 2017 bull trend, and the sample predates liquid perps, funding costs and the present market structure. Nothing here speaks to minute or hour bars.

## Caveats
Six months is a thin out-of-sample test. Rule returns are highly correlated, so "33% of rules significant" is much less than 5,000 independent discoveries. Break-even cost analysis is not the same as net-of-cost backtesting with spreads. Early Bitcoin prices come from thin, sometimes manipulated venues.
