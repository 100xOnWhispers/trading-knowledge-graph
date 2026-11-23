---
title: "Thomas DeMark's Approach, Parts I-V: TD-Points and TD-Lines, TD Breakout Qualifiers, TD Price Projections, The DeMarker Indicator, TD Sequential"
authors: "MarketInOut"
year: 2011
venue: "MarketInOut blog (rewritten October 2026)"
url: "https://www.marketinout.com/blog/demark-td-points-and-td-lines"
pdf: "none"
access: "full-text"
source_type: "documentation"
evidence_grade: "D"
topic: "15-demark-indicators"
asset_class: "equities"
horizon: "n/a"
tags: "td-points, td-lines, breakout-qualifiers, price-projections, demarker, intersection, rules"
---

## Key insight
A five-part summary of DeMark's 1994-era methods with rules precise enough to code. It is the best open description found of TD Points, TD Lines, the three breakout qualifiers and the three price projectors, and it gives the DeMarker formula and the original Sequential with the intersection rule. No tests are reported.

## Method
All five parts were read. Rules as stated:

TD Points and TD Lines (Part I)
- TD supply point: a bar whose high is above the highs of the bars immediately before and after. TD demand point: a low below both neighbors. Level 2 and 3 points need 2 or 3 bars on each side.
- Down TD Line: connect the most recent supply point to the next supply point to its left that is higher. Up TD Line: most recent demand point to the next lower demand point on its left. Lines are redrawn as new points form.
- "True" point tests: a demand point's low must be below the close two bars before it (supply: high above that close), and the close of the bar after the point must be on the correct side of the line's rate of advance.

Breakout qualifiers (Part II). A break is valid if any one holds (upside case):
1. The close of the bar before the breakout is below the close before it.
2. The breakout bar opens above the down TD Line.
3. Prior close plus that bar's buying pressure (close minus its low, or minus the close two bars back if lower) is below the breakout level.

Price projectors (Part III). Add to the breakout price the distance from the line to: (1) the lowest low beneath it; (2) the low of the bar with the lowest close; (3) the close of the bar with the lowest low.

DeMarker (Part IV)
- `DeMax = max(H[i]-H[i-1], 0)`, `DeMin = max(L[i-1]-L[i], 0)`, `DeMarker = SMA(DeMax,N) / (SMA(DeMax,N) + SMA(DeMin,N))`, N commonly 14.
- Zones above 0.7 and below 0.3. A stay under 5 bars is "moderate" and usually followed by a reversal on exit; 5 bars or more is "extreme" and usually followed by trend continuation.

Sequential (Part V), 1994 form
- Setup of 9; intersection (high of bar 8 or 9 at or above the low of any of bars 3 to 7); countdown of 13 closes at or below the low two bars earlier.
- Three entries: close of the 13; a close above the high two bars earlier; a close above the close four bars earlier.
- Stop from the extreme bar's true range. Exits: a new setup that fails to exceed the prior setup's extreme, or an opposite signal.
- The text says 15 to 30 bars usually pass between setup end and countdown end.

## Data and sample
None.

## Reported results
None. The series recommends DeMarker and TD Line breaks as filters for Sequential, without evidence.

## Signal construction
TD Line break flag: maintain level-1 supply and demand points on closed bars, extrapolate the active line to the current bar, and flag a close through it with the qualifier results as three booleans. DeMarker: rolling sums as above plus a "bars in zone" counter split at 5.

## Relevance to SOL perpetuals at minutes to hours
Qualifier 2 depends on an opening gap through the line, which continuous crypto bars almost never produce, so it will be inert. Qualifiers 1 and 3 and the DeMarker duration rule remain computable. The MetaTrader 5 help page gives the same DeMarker formula with 30 and 70 bands; the 5-bar duration split here differs from the 6-bar split DeMARK Analytics states for REI.

## Caveats
Secondary retelling by a screening-software vendor, rewritten in 2026, with no citations to page numbers. It reflects the 1994 book and omits later changes (perfection, bar-13 deferral, recycle). Not checked against the original book, which was not accessible.
