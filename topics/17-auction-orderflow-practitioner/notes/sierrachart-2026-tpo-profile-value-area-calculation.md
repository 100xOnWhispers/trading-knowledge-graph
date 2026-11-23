---
title: "TPO (Time Price Opportunity) Profile Charts, including How Point of Control and Value Area Are Calculated"
authors: "Sierra Chart"
year: 2026
venue: "Sierra Chart documentation (undated page, read November 2026)"
url: "https://www.sierrachart.com/index.php?page=doc/StudiesReference/TimePriceOpportunityCharts.html"
pdf: "none"
access: "full-text"
source_type: "documentation"
evidence_grade: "D"
topic: "17-auction-orderflow-practitioner"
asset_class: "futures"
horizon: "hours"
tags: "market-profile, tpo, volume-profile, point-of-control, value-area, initial-balance, single-prints"
---

## Key insight
Market Profile and volume profile are precise, reproducible transforms of trade data, and this vendor page states the algorithms exactly: the point of control (POC) is the modal price row by time or by volume, and the value area is the contiguous band around it holding 70% of the total. The page offers no evidence that these levels predict anything. It is used here as the definitional source, because the original Steidlmayer and Dalton texts and the CBOT handbook could not be opened in this session.

## Method
Definitions as given on the page (read through a summarizing tool, so wording is paraphrased).
- TPO: one letter or block marks that price traded during one sub-period. Default sub-period is 30 minutes; default profile period is one day. Prices are grouped into rows of a set number of ticks.
- TPO POC: the row with the most TPOs. Ties go to the row nearest the middle of the profile; if still tied, the lower row. Volume POC: the same rule on volume per price level.
- Value area (TPO or volume): target = total count times the value-area percentage (default 70%). Start at the POC. Compare the row above with the row below, add the larger to the value area and carry the other into the next comparison against the next row beyond the one just added. Stop when the included total reaches the target. Equal rows are both added. The top and bottom rows included are the value area high (VAH) and low (VAL). A "two levels at a time" variant exists but its steps are not described.
- Initial balance: the range of the first N sub-periods (N = 2 with 30-minute letters gives the first hour), with optional percentage extensions.
- Single prints: the first TPO in a sub-period that makes a new profile extreme and is not revisited in the following sub-period(s); confirmed only after the next sub-period closes.
- Poor high or low: a profile high or low equal to a previous TPO high or low (optionally within one price increment).
- TPO midpoint: either the mid of the range or the row with equal TPOs above and below.

## Data and sample
None. Documentation of a charting study.

## Reported results
None. No statistics, backtests or claims of predictive accuracy appear in the portions read. Naked or virgin POC was not covered in the text retrieved.

## Signal construction
All inputs are trades (price, size, time) from the lead venue.
1. Choose the profile period. For a 24-hour perp there is no natural session, so compute several: UTC day, 8-hour funding window, rolling 24 hours, and the US cash session.
2. Build a volume histogram by price bucket (bucket about 2 to 5 basis points for SOL). Compute POC, VAH and VAL with the algorithm above.
3. Features: (price - POC) and distance to VAH and VAL in volatility units; in-value flag; value-area width over recent range; position of the developing POC within the range; prior-period POC, VAH, VAL as static levels; initial-balance break flags; counts of single-print rows.
4. Update each minute for developing profiles; freeze at period end.
The auction-theory reading that practitioners attach (accept outside value means trend, reject means return to POC) can be cast as a labelled event: value-area exit, outcome within M bars.

## Relevance to SOL perpetuals at minutes to hours
Fully computable from public trade data and relevant to the target horizon. The open issues are specific to crypto: no session boundary, volume split across venues and between spot and perp, and wash or incentive-driven volume on some venues that can distort a POC. Whether POC or value-area edges attract or repel SOL price beyond what a rolling VWAP band already captures is untested in any source read here.

## Caveats
Vendor documentation, no evidence. The 70% figure and 30-minute letters are conventions from pit-session futures. Tie rules and the one-versus-two-level expansion differ across platforms, so "the" value area is not unique. Read through a summarizer over two fetches of a long page; parts of the page were not retrieved.
