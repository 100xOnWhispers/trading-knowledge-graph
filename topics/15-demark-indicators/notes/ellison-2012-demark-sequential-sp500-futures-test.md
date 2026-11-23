---
title: "Tom Demark Sell Signal - Market Top"
authors: "Ellison, Steve"
year: 2012
venue: "Daily Speculations (blog of Victor Niederhoffer)"
url: "https://dailyspeculations.com/wordpress/?p=7125"
pdf: "none"
access: "full-text"
source_type: "practitioner"
evidence_grade: "C"
topic: "15-demark-indicators"
asset_class: "futures"
horizon: "multi-day"
tags: "td-sequential, sp500-futures, event-study, buy-sell-asymmetry, small-sample"
---

## Key insight
A transparent event study of Sequential 13 signals on daily S&P 500 futures over about 30 years. Buy signals were rare and followed by returns well above the unconditional average, both in the design period and in the later period. Sell signals were more frequent and their forward returns were indistinguishable from the unconditional average. The long-side and short-side behavior of the same symmetric rule differed sharply.

## Method
The author reconstructed the rules from a 1990s article and other sources and says variations exist.

- Setup: 9 consecutive bars closing lower (higher) than 4 bars earlier, with the high (low) of bar 8 or 9 above (below) the low (high) of a bar at least 3 bars earlier (the 1994 "intersection").
- Countdown: count non-consecutive bars whose close is lower (higher) than the close 2 bars earlier. Note this compares close with close, where Perl and DeMARK Analytics compare close with the low or high.
- Cancel if price exceeds the setup's highest high (lowest low). A new same-direction setup resets the count; an opposite setup starts a new countdown.
- Signal: count reaches 13 and the 13th counted bar closes beyond the 8th. If it does not, he cancels (the book rule defers).
- Evaluation: net change 12, 18, 28, 42 and 63 days after each signal against the average of all periods of that length. He picked 28 days from the 1982 to 1989 results and then examined only 28-day changes after later signals.

## Data and sample
Daily S&P 500 futures, 1982 to 1989 for design, 1990 to early 2012 for the later check.

## Reported results
1982 to 1989:
- 5 buy signals. Average change 8.0% at 12 days, 5.4% at 28 days, 7.1% at 63 days, against all-period averages of 0.5%, 1.3% and 2.9%.
- 8 sell signals. Average 28-day change +0.8% against +1.3% for all periods. The author calls the record "decidedly mixed".

Since 1990, 28-day changes:
- 9 buy signals: average +4.1%, median +6.0%, against +0.6% for all 28-day periods. The worst was -14.2% after 12 January 2009.
- 21 sell signals: average +0.7%, median +0.6%, against +0.6%. The author's words: "consistent with randomness".

## Signal construction
A long-only event flag: buy countdown 13 completed on the reference index. At daily frequency this fires about once every two to three years on one market, so it can only be a regime input, not a trading signal for a minutes-to-hours bot.

## Relevance to SOL perpetuals at minutes to hours
Two things transfer as hypotheses. First, test buy and sell signals separately; pooling them hides the asymmetry found here and in Lissandrin et al. Second, the good buy signals cluster after crashes (October 1987, March 2008, October 2011), so the result may be "buy after a large fast decline" and not the count itself. On SOL intraday bars, compare a buy 13 against a simple drawdown-size trigger.

## Caveats
Fourteen buy signals in thirty years; no significance test; no costs; holding period chosen in-sample, though then held fixed for the later period. Equity index futures have a positive drift that flatters long signals and penalizes shorts. The countdown rule differs from the published one, so this is a test of a variant. A reader comment on the post questions why any particular count should work, which the post does not answer.
