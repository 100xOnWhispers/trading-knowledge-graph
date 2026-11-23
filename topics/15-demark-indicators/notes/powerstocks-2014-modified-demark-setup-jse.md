---
title: "Modified DeMark Analysis for the JSE: User Guide V1.1"
authors: "PowerStocks Research"
year: 2014
venue: "PowerStocks Research user guide, hosted by Sharenet"
url: "https://www.sharenet.co.za/v3/powerstocks/pdf/DeMark_UserGuide.pdf"
pdf: "sources/15-demark-indicators/powerstocks-2014-modified-demark-setup-jse.pdf"
access: "full-text"
source_type: "practitioner"
evidence_grade: "D"
topic: "15-demark-indicators"
asset_class: "equities"
horizon: "daily"
tags: "td-setup, setup-count-distribution, price-flip-entry, jse-top40, summation-variant"
---

## Key insight
A vendor guide that modifies the TD Setup after examining about 20 years of the JSE Top 40 index. Three ideas are worth keeping: enter on the price flip that ends an extended setup instead of on bar 9; use different thresholds for buys and sells; and read the setup count against its own historical distribution. The vendor dropped the countdown phase as "not accurate enough". Evidence is chart inspection, not statistics.

## Method
Rules as given, based on Perl's book with changes:

- Buy setup count: after a bearish price flip, count consecutive closes below the close 4 bars earlier. The count runs past 9 for as long as the condition holds.
- Buy signal: the bullish price flip (a close above the close 4 bars earlier) that ends a count of 9 or more.
- Sell signal: the bearish flip that ends a sell-setup count of 11 or more (the text also says "12" in one place).
- "Probability of reversal": the empirical cumulative frequency of terminal setup counts since 1996.
- Buy summation: a count of bars closing below the close 4 bars earlier that is not reset by interruptions, with a threshold of 9. It is meant to catch corrections where brief rallies reset the strict count. The window length is not stated.

## Data and sample
JSE J200 Top 40 index, daily, 1996 to 2014. One S&P 500 illustration.

## Reported results
- A buy count reaching 9 is in the top 6.4% of terminal counts since 1996; a sell count reaching 11 is in the top 10.8%.
- A buy count had never exceeded 18 in the sample; sell counts above 18 occurred 2% of the time; counts as high as 29 are mentioned.
- Threshold comparisons (8, 9 or 10 for buys; 10, 11 or 12 for sells) are made by counting good and bad signals on charts by eye. For example, since March 2008 lowering the buy threshold to 8 added three good and three false signals, and raising it to 10 lost six good signals.
- The introduction cites "a recent back test" showing Sequential signals "around 70% accurate" with no source or definition.

## Signal construction
Two features a bot can compute cheaply:
1. Terminal setup count at the flip: when a flip occurs, record the length of the run that just ended. Signal when the length is at or above a threshold.
2. Percentile of the current running count within the trailing empirical distribution of terminal counts for that instrument and bar size.

## Relevance to SOL perpetuals at minutes to hours
The percentile idea removes the fixed 9 and adapts to each timeframe, which matters because the share of runs reaching 9 will differ between 5-minute SOL bars and daily index bars. Waiting for the flip is the same as Perl's conservative entry applied to the setup. The asymmetric thresholds match the buy and sell asymmetry seen in other notes but were fitted to an equity index with upward drift.

## Caveats
Commercial product documentation. No returns, no hit rate with a definition, no costs, no out-of-sample test; "good" and "bad" signals are judged visually. Thresholds were tuned on the same data used to present them. A long run of lower closes being rare does not by itself mean the next move is up.
