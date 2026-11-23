---
title: "TD Sequential | Trading Indicator (Countdown & Exit), with TD Sequential - Adjusted and TD Sequential | Trading Strategy (Setup & Countdown)"
authors: "Oxford Capital Strategies Ltd"
year: 2013
venue: "Oxfordstrat R&D Blog"
url: "https://oxfordstrat.com/indicators/td-sequential-2/"
pdf: "none"
access: "full-text"
source_type: "practitioner"
evidence_grade: "C"
topic: "15-demark-indicators"
asset_class: "futures"
horizon: "multi-day"
tags: "td-sequential, countdown, backtest, parameter-sweep, futures-portfolio, negative-result"
---

## Key insight
The broadest public backtest of TD Sequential as a mechanical reversal system, and it is negative. On 42 futures over 33 years, entering against the trend after a completed countdown produced a profit factor below 1 across almost the whole grid of countdown lengths and holding periods, before costs. The 2008 rule revisions did not help.

## Method
Three related pages, each a MATLAB portfolio simulation with full parameter sweeps.

Page 1 (this URL), original 1994 rules:
- Setup: 9 consecutive closes below the close 4 days earlier (long); equality restarts.
- Intersection: from setup day 8 onward, a day's high at or above the low of a day 3 or more days earlier.
- Countdown: 13 non-consecutive closes below the low 2 days earlier; void if a new setup forms meanwhile or a close exceeds the setup's highest high.
- Entry: on a close above the close 4 days earlier after the countdown completes (the conservative "flip" entry).
- Exit: time exit after n days, n from 1 to 40. Stop at 6 times the 20-day ATR. Sizing 1% fixed fractional on $1,000,000.
- Sweep: countdown length 5 to 25 by time exit 1 to 40.

Page 2, "Adjusted" (Perl 2008): no intersection; countdown uses `close <= low[2]`; bar 13 needs `low(13) <= close(8)`; cancellation on an opposite setup or a true low above the prior setup's resistance; recycle with a 1.000 to 1.618 range multiplier and an 18-bar count. Same entry, exits and sweep.

Page 3, strategy version: sweep of setup length 5 to 25 by countdown length 5 to 25, with a pattern exit and a stop at the pattern extreme.

Each is run with $0 costs and with $100 per round turn.

## Data and sample
42 US futures across commodities, currencies, interest rates and equity indexes, daily bars, 1 January 1980 to 31 May 2013.

## Reported results
Results are published only as contour charts. Values below are read from those charts and are approximate.
- Page 1, $0 costs: profit factor about 0.70 to 0.95 over most of the grid. Values slightly above 1 (about 1.05 to 1.15) appear only for holds of roughly 1 to 3 days with countdown lengths near 17 to 20.
- Page 1, $100 round turn: profit factor about 0.45 to 0.80. Percent profitable trades at $0 costs about 44 to 51%. Every equity curve in the sensitivity plot ends below starting capital.
- Page 2, $0 costs: about 0.65 to 0.95; with costs about 0.40 to 0.65.
- Page 3, $0 costs: mostly 0.8 to 1.0 with isolated pockets of 1.2 to 1.6 at the grid edges; with costs mostly near 0.8.

## Signal construction
Not a tradable signal on this evidence. The useful artifact is the test design: sweep the counting parameters and the holding period together and look for a broad plateau. No plateau above 1 exists here.

## Relevance to SOL perpetuals at minutes to hours
Daily futures results do not settle the intraday crypto question, but they set the prior: a countdown 13 is not a reversal edge by default. The faint positive region at 1 to 3 bars is the only fade horizon worth testing on SOL. In the companion Setup Trend note the same counts traded with the trend were profitable.

## Caveats
Vendor blog; no author named; no significance tests; a fixed 6-ATR stop and time exit that DeMark does not prescribe; no risk-level stop; no perfection or TDST filter. Numbers are read from images. Sample ends in 2013. The page carries a CFTC Rule 4.41 hypothetical-results notice.
