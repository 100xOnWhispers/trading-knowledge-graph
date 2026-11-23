---
title: "TD Setup - Trend | Trading Indicator (Setup & Exit)"
authors: "Oxford Capital Strategies Ltd"
year: 2013
venue: "Oxfordstrat R&D Blog"
url: "https://oxfordstrat.com/indicators/td-setup-trend/"
pdf: "none"
access: "full-text"
source_type: "practitioner"
evidence_grade: "C"
topic: "15-demark-indicators"
asset_class: "futures"
horizon: "multi-day"
tags: "td-setup, momentum, trend-following, backtest, parameter-sweep, futures-portfolio"
---

## Key insight
Reversing the usual reading of a TD Setup and trading with it was profitable on a 42-market futures portfolio. Going long after nine consecutive closes above the close four days earlier (which DeMark calls a sell setup) gave profit factors above 1 over a wide, smooth region of the parameter grid, and the region survives a $100 round-turn cost. The same site's counter-trend Sequential tests lost money.

## Method
The page states: "We reverse the original concept of the TD Setup and trade in the direction of trend."

- Long: at least 9 consecutive closes each above the close 4 trading days earlier. Short: 9 consecutive closes each below. Equality or an opposite close restarts the count.
- Entry: on the close of the day the setup completes.
- Exit: time exit at the close n days later, n from 1 to 40.
- Stop: 6 times the 20-day ATR. Sizing: 1% fixed fractional on $1,000,000.
- Sweep: setup length 5 to 25 by time exit 1 to 40, at $0 costs and at $100 round turn.

Note this is not Perl's "TD Setup Trend" (TDST), which is a price level. It is a streak-length momentum rule.

## Data and sample
42 US futures from commodities, currencies, interest rates and equity indexes; daily bars; 1 January 1980 to 31 May 2013. MATLAB simulation.

## Reported results
Published only as contour charts; values are read from them and approximate.
- $0 costs: profit factor rises with both setup length and holding period. About 1.2 along a band from setup length 9 to 12; 1.4 to 1.6 for setup lengths 13 to 20 with holds of 10 days or more; local peaks near 1.8. Below 1 only at setup lengths near 5 with very short holds.
- $100 round turn: below 1 for holds under about 5 days at any setup length (down to 0.4 to 0.8 at 1 to 2 days). About 1.0 to 1.2 for setup length 9 at holds of 10 to 40 days. About 1.2 to 1.6 for setup lengths 12 to 20 with holds of 15 days or more.

## Signal construction
Signed setup count on closed bars: `up = count of consecutive bars with C[t] > C[t-4]`, `dn` likewise for lower closes. Trend state is +1 when `up >= m`, -1 when `dn >= m`. The sweep suggests m above the canonical 9 and a holding period several times m.

## Relevance to SOL perpetuals at minutes to hours
The rule has the same sign as time-series momentum, so it should be benchmarked against a plain momentum signal before any credit goes to the counting. For SOL the direct question is whether a completed 9 on 5-minute to 1-hour bars is followed by continuation or reversal. The futures evidence here and in Lissandrin et al. says continuation is at least as likely, so a bot should not hard-code "9 means fade". The cost result matters: the edge vanished at short holds once costs were charged, and Kalshi spreads on a new venue may be wide.

## Caveats
Vendor blog, no author named, no significance tests, no out-of-sample split, results read from images. The profit is plausibly generic trend-following return in 1980 to 2013 futures, not something specific to DeMark's counting. The 6-ATR stop and 1% sizing shape the profit factor. The sample ends in May 2013 and nothing later is shown. CFTC Rule 4.41 hypothetical-results notice applies.
