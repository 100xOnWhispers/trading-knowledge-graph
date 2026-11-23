---
title: "Numbers Bars"
authors: "Sierra Chart"
year: 2026
venue: "Sierra Chart documentation (undated page, read November 2026)"
url: "https://www.sierrachart.com/index.php?page=doc/NumbersBars.php"
pdf: "none"
access: "full-text"
source_type: "documentation"
evidence_grade: "D"
topic: "17-auction-orderflow-practitioner"
asset_class: "futures"
horizon: "seconds"
tags: "footprint, delta, bid-ask-volume, diagonal-imbalance, point-of-control, absorption, order-flow"
---

## Key insight
A footprint chart (Sierra Chart calls it Numbers Bars) is a bar in which each price row shows volume traded at the bid and at the ask. Everything practitioners read from it (delta, imbalances, absorption, exhaustion) is derived from one input: each trade classified as buyer- or seller-initiated. The page defines the classification and the comparisons exactly and makes no claim about predictive value. The same inputs underlie the formal trade-flow measures of topic 08.

## Method
Definitions as given on the page (read through a summarizing tool over two partial fetches; wording is paraphrased).
- Bid trade and ask trade: a trade is assigned to the bid or ask side from the feed's own flag when available; otherwise a trade at or below the bid is a bid trade, a trade at or above the ask is an ask trade, and trades between are assigned to the nearer side with tick-direction tie-breaks.
- Bid volume and ask volume: summed quantity of bid trades and ask trades at a price row or over a bar. Number of trades is counted separately.
- Delta: the page says Sierra Chart avoids the term as too general; the equivalent is "Ask Volume Bid Volume Difference", ask volume minus bid volume, per row or per bar.
- Dominant side: the larger of bid and ask volume at the same row.
- Diagonal comparison: ask volume at a row is compared with bid volume one row lower, and bid volume at a row with ask volume one row higher. Diagonal differences: ask volume at next higher price minus bid volume at this price; ask volume at this price minus bid volume at previous lower price. The page gives no rationale; mine is that buyers lift the ask one tick above where sellers hit the bid, so the diagonal pair is the like-for-like comparison.
- Dominant side volume percent: ask volume as a share of ask plus bid volume (signed by side).
- Colouring thresholds suggested on the page: absolute differences of 100, 200, 300 contracts; percentages of 0.25, 0.50, 0.75; dominant-side ratios of 1.25, 1.50, 2.0.
- Bar POC: the row with the greatest volume in the bar.
Cumulative delta, stacked imbalances and "unfinished auction" are not defined in the portions retrieved.

## Data and sample
None. Documentation. The study needs trade prints with bid and ask at the time of trade; it does not need market depth.

## Reported results
None.

## Signal construction
From a crypto trade stream that carries the taker side on each trade (to my knowledge the major venues publish it; not checked against venue documentation in this session), per bar and per price bucket:
- delta = ask volume - bid volume; cumulative delta is its running sum over a session or window;
- delta ratio = delta / total volume;
- diagonal imbalance count = number of rows where the diagonal ratio exceeds a threshold (test 1.5 to 3), and the longest run of consecutive such rows ("stacked");
- absorption proxy (practitioner usage, not defined on this page): large absolute delta at a row or bar with little price progress, for example |delta| in the top decile while the bar's range or close-to-close move is in the bottom half;
- exhaustion proxy (same status): shrinking volume and delta at successive new extremes;
- delta divergence: price makes a new high while cumulative delta does not.
Thresholds must be rescaled from futures contracts to SOL notional and to each venue's volume.

## Relevance to SOL perpetuals at minutes to hours
All of this is computable in real time and is the practitioner view of signed trade flow. For a minutes-to-hours bot the row-level detail mostly matters at bar extremes (who was aggressive at the high or low) and at pre-defined levels. Topics 07 and 08 hold the evidence on whether signed flow predicts returns; nothing read for this topic tests absorption or exhaustion patterns as such. Cross-venue aggregation is a design choice with no guidance in the source.

## Caveats
Vendor documentation with no evidence. Where a venue reports the taker side, classification is exact, unlike the inferred classification the page describes for feeds without a flag. Absorption and exhaustion have no agreed definition; any test must fix one in advance and compare against matched bars without the pattern. Only about half of a very long page was retrieved.
