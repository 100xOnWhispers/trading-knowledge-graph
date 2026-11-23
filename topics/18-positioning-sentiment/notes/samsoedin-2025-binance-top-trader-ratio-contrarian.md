---
title: "BTC perp accounts turn heavily long as Binance long/short ratio surges to 3.87"
authors: "Samsoedin, Bryan; Wu, Ivan"
year: 2025
venue: "The Block (data commentary, 25 November 2025)"
url: "https://www.theblock.co/post/380213/btc-perp-accounts-turn-heavily-long-as-binance-long-short-ratio-surges-to-3-87"
pdf: "none"
access: "full-text"
source_type: "practitioner"
evidence_grade: "D"
topic: "18-positioning-sentiment"
asset_class: "crypto"
horizon: "multi-day"
tags: "top-trader-long-short-ratio, binance, account-ratio, contrarian, anecdote, hedging-caveat"
---

## Key insight
A single well-documented episode shows the Binance top-trader long/short account ratio for BTC moving opposite to price at both extremes: below 0.6 (multi-year low) when BTC made an all-time high above USD 126,000, and 3.87 (highest in more than three years) after a decline of more than 35% over the following 45 days. Large-balance accounts were net short into strength and net long into weakness. The article itself warns that this cannot be read as directional conviction because perp legs may hedge spot, options or basis positions.

## Method
Descriptive commentary on one exchange data series. The ratio is described as the share of net long versus net short accounts among the top 20% of Binance users by margin balance; it counts accounts, not position size, so each account weighs equally. Values above 1 mean more large accounts are net long. No statistical test, no forward-return analysis.

## Data and sample
Binance BTC perpetual, top-trader long/short account ratio, roughly October to November 2025. One asset, one venue, one episode. Funding rates and open interest are not discussed.

## Reported results
- Ratio below 0.6 around the all-time high above USD 126,000, described as a multi-year low.
- Ratio 3.87 in the week before 25 November 2025, described as the highest in more than three years, after BTC fell more than 35% in 45 days.
- The authors' summary: "Binance whales were skewed short on BTC perps into strength and are now skewed long on perps into weakness."
- Stated caveats: shorts at the highs could have hedged spot sales or been basis trades; the later long skew could offset short options or off-exchange exposure. The measure shows how leveraged derivatives accounts lean on perps, not total portfolio positioning.
- The article does not report what happened to price after the 3.87 reading.

## Signal construction
Inputs: Binance `topLongShortAccountRatio` for the symbol (see the Binance API note in this folder). Two candidate readings, neither tested here:
- Counter-trend accumulation: `log(ratio)` rising while price falls marks large accounts buying the decline. If these accounts are informed, it is bullish with a lag; if they are trapped dip-buyers, it marks liquidation fuel.
- Extremes: percentile rank of the ratio over a trailing year; flags at the top and bottom 5%.
The episode gives one observation at each extreme and no outcome for the second, so it cannot discriminate between the readings.

## Relevance to SOL perpetuals at minutes to hours
It illustrates that the top-trader account ratio behaves contrarian to price over weeks, consistent with large accounts scaling in against moves (or hedging). For SOL the same series is available at 5-minute resolution, and the relevant test is whether changes in the ratio over hours lead or follow SOL returns. The hedging caveat is stronger for BTC, where spot ETF and options activity is large, than for SOL.

## Caveats
One episode, no test, news commentary. An account ratio rising during a decline can be mechanical: accounts with short positions take profit and leave the denominator, while longs hold. The measure is specific to Binance's user mix. The outcome after the high reading is unknown from this source. Other web commentary found alongside it asserts thresholds (for example a long share above 70% as a top signal) and claims of academic support without citing any study; those claims were not verified and are not relied on.
