---
title: "Statistical Testing of DeMark Technical Indicators on Commodity Futures"
authors: "Lissandrin, Marco; Daly, Donnacha; Sornette, Didier"
year: 2015
venue: "Swiss Finance Institute Research Paper No. 15-56 (preprint dated 18 November 2015)"
url: "https://ideas.repec.org/p/chf/rpseri/rp1556.html"
pdf: "sources/15-demark-indicators/lissandrin-2015-statistical-testing-demark-commodity-futures.pdf"
access: "full-text"
source_type: "working-paper"
evidence_grade: "B"
topic: "15-demark-indicators"
asset_class: "futures"
horizon: "multi-day"
tags: "td-sequential, td-combo, tdst, setup-trend, permutation-test, commodity-futures, contract-roll"
---

## Key insight
The only academic test of DeMark indicators found for this topic. On 21 commodity futures over 2004 to 2014, TD Sequential, TD Combo and Setup Trend (a TDST breakout rule) each beat randomized entry timing on some markets, but the signals are sparse and Sequential and Combo often predict a move without predicting its direction. On energy futures a long Sequential signal marked a continuing downtrend more often than a bottom.

## Method
The paper gives pseudocode for all three indicators with parameters n=4, m=9, u=2, p=13, k=8.

- Setup: counter s increases while `C(t) < C(t-4)` on consecutive bars, complete at s=9. The setup range is `[min low, max high]` of its bars. A buy setup sets resistance to its max high; a sell setup sets support to its min low.
- Setup Trend (ST): go long at the next close when `C(t) > res(t)`, short when `C(t) < sup(t)`.
- Countdown: count non-consecutive bars with `C(t) <= L(t-2)` (standard) or `L(t) <= L(t-2)` (aggressive; the authors use the aggressive form). Bar 13 completes only if `L(13) <= C(8)`.
- Combo: count from bar 1 of the setup when all hold: `C(t) <= L(t-2)`, `L(t) <= L(t-1)`, `C(t) <` close of the previous Combo bar, `C(t) < C(t-1)`.
- Cancel or recycle: an opposite setup restarts the countdown in the new direction; `L(t) > res(t)` cancels a buy countdown; a new same-direction setup resets the count only if its range is wider than the old one, and not if its close lies inside the old setup's range.
- Entry: conservative, at the next close after `C(t) > C(t-4)` following the 13.

Testing: conditional versus unconditional return distributions, then Monte Carlo permutation tests with 400 randomized signals that keep the number of trades and the fixed holding period. Metrics are mean return per trade, profit factor and a risk-return ratio, for holding periods of 1 to 14 days. Observed quantiles are adjusted conservatively for the approximation (95% requires an observed 97%).

## Data and sample
Daily bars for 21 futures (grains, softs, energy, industrial and precious metals; CBOT, ICE, NYMEX, COMEX, SHFE), January 2004 to January 2014. Continuous series are back-adjusted by price difference; four roll rules are compared. Transaction and financing costs are not included.

## Reported results
- Entries per market per year (min / mean / max): Sequential 3.0 / 3.9 / 4.6; Combo 1.2 / 1.7 / 2.2; ST 3.4 / 4.5 / 6.1.
- Sequential was statistically significant for long or short entries on every market except platinum, but "does not seem to be able to forecast the correct market direction". It was informative on energy for longs and on other classes for shorts.
- Combo had 30 to 40% fewer trades and more cases significant on both sides (gold, silver).
- ST captured direction correctly but was predictive on only 6 of 21 markets, mainly long.
- Predictive power usually held for a limited range of holding days. In the cocoa example (1.7 long Sequential trades a year) a Kolmogorov-Smirnov test at 14 days gave p = 0.64, and the permutation quantiles of 87 to 95% fell short after the conservative adjustment.
- Rolling on expiry day reduced or removed significance.

## Signal construction
Compute signed setup count, countdown count, Combo count and TDST levels from closed bars with the rules above. Emit events at setup 9, countdown 13, Combo 13 and TDST close-through. The paper supports using these as volatility or continuation flags as much as reversal entries.

## Relevance to SOL perpetuals at minutes to hours
The permutation framework transfers directly and suits sparse signals. The empirical results do not transfer: daily commodity bars, no costs, a period ending in 2014. Perpetuals have no roll, which removes the paper's largest data problem. Direction must be re-tested per timeframe.

## Caveats
In-sample only, no costs, no out-of-sample split. No data-snooping correction across 21 markets, 3 indicators, long and short sides, 14 holding periods and 3 metrics; the authors name this as future work. A RePEc listing reports a later journal version (Journal of Investment Strategies), which I did not read. The copy read is the authors' manuscript.
