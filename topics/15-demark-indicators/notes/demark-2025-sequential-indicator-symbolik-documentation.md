---
title: "DeMARK Sequential Indicator (Symbolik help center), with The DeMARK Indicator List and DeMARK Indicators School: TD REI"
authors: "DeMARK Analytics"
year: 2025
venue: "Symbolik Help Center and demark.com"
url: "https://help.symbolik.com/hc/en-us/articles/37782822323987-DeMARK-Sequential-Indicator"
pdf: "none"
access: "full-text"
source_type: "documentation"
evidence_grade: "D"
topic: "15-demark-indicators"
asset_class: "multi"
horizon: "n/a"
tags: "td-sequential, recycle, cancellation, risk-level, td-rei, duration-analysis, vendor-documentation"
---

## Key insight
The originator's own current description of Sequential. It confirms the public rules for setup, perfection, countdown, deferral and cancellation, and states recycle thresholds that differ from Perl's 2008 book. The companion REI article gives DeMark's "duration" reading of oscillators: a short stay at an extreme precedes reversals, a long stay signals trend strength.

## Method
Vendor documentation, no tests. Rules as stated:

- Setup: 9 consecutive closes below (buy) or above (sell) the close four bars earlier.
- Perfected setup: the 9 is complete and bars 6 and 7 "have been exceeded".
- TDST: reference levels from the lowest true low and highest true high of recent setups.
- Countdown: close compared with the high or low two bars earlier; counts need not be consecutive; 13 completes it.
- Deferral: for a buy, the low of bar 13 must be at or below the close of bar 8 (sell: high at or above). A "+" marks a deferred bar. The 8-versus-5 comparison is elective.
- Risk level: generated at a completed 13; the 13 stays active while price holds it.
- 12-bar rule: a reversal should occur within 12 bars of a 13, otherwise the trend is likely to continue.
- Recycling: a same-direction setup either extends to a count of 22, or its size (highest true high minus lowest true low) is between 100% and 200% of the prior setup.
- Cancellation: an opposite setup completes before the 13, or a true high prints below TDST downside (true low above TDST upside). A completed countdown is never altered.

The indicator list page (fetched from the same help center) gives one-paragraph descriptions of 85 studies and outputs, including Combo, Aggressive Sequential, D-Wave, DeMarker 1 and 2, Differential, Lines, Moving Average 1 and 2, Pressure, REI and Propulsion. It gives no formulas. It states the studies are proprietary and licensed to Bloomberg, CQG and Thomson Reuters.

The REI article (demark.com, 1 March 2021) says REI compares true highs and lows with those two bars earlier and with prices up to eight bars earlier, is arithmetic and not exponential, and is computed in five steps that the page does not show. Six or fewer bars at an extreme is "mild"; more than six signals a strong trend. The ideal reversal follows an extreme, a return to neutral, then a mild re-entry.

## Data and sample
None.

## Reported results
No statistics. The demark.com TradingView page (also fetched) describes a paid "DeMARK 9-13" script at $29.99 a month covering 9s, 13s, TDST, perfected setups and risk levels, and says it applies to crypto and all intervals.

## Signal construction
Use this note to choose defaults where sources conflict. Recycle: Perl 2008 gives 18 bars and a 1.0 to 1.618 range ratio; this page gives 22 bars and 100 to 200%. Treat both as parameters. For REI, add a "bars in extreme zone" counter and treat more than six as a continuation flag.

## Relevance to SOL perpetuals at minutes to hours
The vendor claims universality across intervals and assets but shows no evidence. The duration idea is cheap to test on SOL: compare forward returns after short and long stays of REI or DeMarker beyond their bands.

## Caveats
Marketing material from the seller of the indicators. Formulas for most studies are withheld. The Symbolik HTML page returned a bot challenge; I read the same article through the help center's public JSON endpoint. The REI and TradingView pages were read at demark.com.
