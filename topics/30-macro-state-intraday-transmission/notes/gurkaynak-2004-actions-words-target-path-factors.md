---
title: "Do Actions Speak Louder than Words? The Response of Asset Prices to Monetary Policy Actions and Statements"
authors: "Gurkaynak, Refet S.; Sack, Brian; Swanson, Eric T."
year: 2004
venue: "Finance and Economics Discussion Series 2004-66, Federal Reserve Board (the version read; the published version is usually cited as International Journal of Central Banking, 2005)"
url: "https://www.federalreserve.gov/pubs/feds/2004/200466/200466pap.pdf"
pdf: "sources/30-macro-state-intraday-transmission/gurkaynak-2004-actions-words-target-path-factors.pdf"
access: "full-text"
source_type: "working-paper"
evidence_grade: "A"
topic: "30-macro-state-intraday-transmission"
asset_class: "multi"
horizon: "minutes"
tags: "fomc, monetary-policy-surprise, target-factor, path-factor, fed-funds-futures, event-window, pre-2020"
---

## Key insight
One number is not enough to describe an FOMC announcement. Two factors are needed: a target factor (the surprise in the current policy rate) and a path factor (the surprise in the expected rate path, driven by the statement). The two have different effects: the path factor dominates longer-term yields, while equities respond mainly to the target factor.

## Method
Changes in interest-rate futures are measured in a tight 30-minute window (10 minutes before to 20 minutes after) and a one-hour window around each FOMC announcement. The current-month federal funds futures contract, scaled for days remaining in the month, gives the target surprise. A rank test on the matrix of changes in five near-dated federal funds and eurodollar futures rejects one factor and accepts two. The two principal components are rotated so that the second (path) factor has no effect on the current-month contract; factors are scaled so that a unit of each moves the one-year-ahead eurodollar rate equally. Asset price changes in the same window are regressed on the factors.

## Data and sample
All FOMC announcements, January 1990 to May 2004. Tick data on federal funds futures (Genesis Financial Technologies), eurodollar futures, on-the-run Treasury yields from GovPX (from June 1991), and five-minute S&P 500 index quotes. Pre-2020; no crypto.

## Reported results
- With the 30-minute window, a one percentage point surprise tightening in the target lowers the S&P 500 by a little more than 4 percent (4.3 percent in the two-factor table) and raises two-, five- and ten-year yields by 47, 27 and 12 basis points.
- A one percentage point path-factor innovation raises five- and ten-year yields by 36 and 27 basis points but moves the S&P 500 by only about -1 percent.
- The path factor explains three to ten times as much of the variation in intermediate and long yields as the target factor.
- Moving from daily to intraday windows sharpens the equity regression: R-squared rises from 0.12 to 0.35.
- The path factor is tied to statements: 8 of its 10 largest realisations (22 of the top 25) fall on dates with FOMC statements.
- Tight- and wide-window measures agree closely for the target factor (R-squared 0.98) and less so for the path factor (0.83), meaning markets take longer to digest statements.
- On non-employment-report days the FOMC window captures the bulk of the daily move in federal funds futures.

## Signal construction
At an FOMC release, compute the change from t - 10 min to t + 20 min in (a) the front federal funds or SOFR futures contract, adjusted for days left in the month, and (b) contracts three to four quarters out. Target surprise is (a); path surprise is the part of (b) not explained by (a). These two numbers, available within 20 minutes, are the standard inputs for an expected-response model of a risk asset.

## Relevance to SOL perpetuals at minutes to hours
The decomposition says which piece to feed a crypto response model: if crypto behaves like equities, the target-type surprise matters most and the path surprise less, but that must be re-estimated because post-2008 announcements are dominated by path and balance-sheet news. The slower digestion of statements matches the longer response windows reported for crypto and for the press conference.

## Caveats
Sample ends in 2004, before forward guidance, asset purchases and press conferences; later work adds a third factor and shows the surprises are predictable ex post (see the Bauer and Swanson note). Equity data are index quotes, not futures. Fifteen years of FOMC meetings is a small sample.
