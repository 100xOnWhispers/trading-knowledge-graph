---
title: "Predictive Power of DeMark Indicator"
authors: "Steversteves (TradingView user)"
year: 2022
venue: "TradingView Ideas (educational post, AMEX:SPY)"
url: "https://www.tradingview.com/chart/SPY/hb60N5RF-Predictive-Power-of-DeMark-Indicator/"
pdf: "none"
access: "full-text"
source_type: "practitioner"
evidence_grade: "D"
topic: "15-demark-indicators"
asset_class: "equities"
horizon: "hours"
tags: "demarker, reversal-points, intraday, spy, hit-rate, binomial-test, small-sample"
---

## Key insight
A small hand-counted study of a DeMark-style reversal script on hourly SPY that reports a 68.8% success rate and a significant binomial test. It is included because intraday evidence is scarce and because it shows the typical weakness of retail tests: the success definition has a high base rate, so the significance claim does not establish an edge.

## Method
- Indicator: the community script "DeMark Reversal Points" by the TradingView author cheatcountry. The post describes it as based on the DeMarker oscillator "also known as Demark or Demark 9". The script's exact rules are not given in the post.
- Success definition: after a sell signal, price trades below the signal level within 48 hours; after a buy signal, price trades above it within 48 hours.
- Entry "guesstimated" at the upper end of the signal candle; exit at "the most commonly tested area" beyond the signal price.
- Test: one-sample binomial test on the success count. The null proportion is not stated.

## Data and sample
SPY, 1-hour chart, the six months before 18 April 2022. 48 signals: 22 buys and 26 sells.

## Reported results
- Overall success rate 68.8%; binomial p = 0.014.
- Buy success 68%, sell success 69%.
- The post says 19 signals (39.6%) succeeded only on the second day after initial trend continuation and 15 (31.3%) on the same day. These sum to 34 of 48, or 70.8%, which does not match the 68.8% headline.
- Average move after buys +4.40 points (SD 3.76); after sells -3.49 points (SD 2.60).
- The author's own limits: one ticker, one timeframe, short period, "should not be construed as rigorous"; many signals saw sizeable adverse moves first. One sentence refers to "over a 20% fail rate", which also conflicts with 68.8%.

## Signal construction
Not reproducible from the post. The transferable part is the evaluation template, corrected:
1. Define success with a symmetric barrier (for example, +k ATR before -k ATR) so the chance rate is near 50%.
2. Estimate the base rate by applying the same test to randomly timed entries in the same period.
3. Compare the signal's rate with that base rate, as Lissandrin et al. do with permutation tests.

## Relevance to SOL perpetuals at minutes to hours
The horizon matches, the asset does not. The useful observation is that roughly 40% of "successful" reversals came only after further continuation. A SOL bot that fades an hourly exhaustion signal needs either a wide stop or a confirmation trigger, and both cut the edge. That matches the deferral and price-flip logic in the published Sequential rules.

## Caveats
With a touch-within-48-hours criterion on hourly bars, price will cross a level near the signal bar most of the time by chance, so 68.8% may be at or below the true base rate. Signals within a six-month window overlap in time and are not independent. Counting was manual. Entry and exit prices were estimated by eye. No costs. Internal figures are inconsistent. A period of six months ending April 2022 covers one market regime.
