---
title: "End-of-Day Reversal"
authors: "Baltussen, Guido; Da, Zhi; Soebhag, Amar"
year: 2026
venue: "Working paper, September 2026 version (author page, University of Notre Dame)"
url: "https://www3.nd.edu/~zda/EOD.pdf"
pdf: "sources/11-intraday-seasonality-tradfi/baltussen-2026-end-of-day-reversal.pdf"
access: "full-text"
source_type: "working-paper"
evidence_grade: "B"
topic: "11-intraday-seasonality-tradfi"
asset_class: "equities"
horizon: "hours"
tags: "end-of-day, intraday-reversal, cross-section, retail-attention, short-sellers, close"
---

## Key insight
In the cross-section of individual US stocks the last half-hour does the opposite of what it does at the index level: stocks that fell earlier in the day outperform in the final 30 minutes and earlier winners lag. The pattern is distinct from market intraday momentum, comes mainly from buying pressure on intraday losers, and is itself reversed by the next morning. The authors attribute it to attention-driven "buy the dip" retail trading near the close and to risk management by short sellers, not to liquidity or gamma hedging.

## Method
Same day partition as Baltussen et al. (2021). Predictor: ROD3 = overnight + first half-hour + middle of day, deliberately skipping the second-to-last half-hour to avoid bid-ask bounce. Outcome: last half-hour (LH) return. Evidence comes from decile portfolio sorts, value-weighted panel regressions with stock and time fixed effects and controls including lagged LH (seasonality) returns, midquote versus trade-price returns, and a version that skips the final 5 minutes to exclude the closing price. Only the abstract and introduction (first eight pages) were read in detail.

## Data and sample
US individual stocks, intraday data since 1993 (exact end date and filters not confirmed).

## Reported results
- ROD3 negatively predicts LH in the cross-section, with t-statistics "typically exceeding 10" in portfolio sorts.
- Long-short intraday strategies earn 3.55 to 6.15 basis points per day (8.9% to 15.4% annualized) depending on weighting and price filter, before costs.
- Present in almost every 5-year rolling window and among the largest, most liquid and most traded stocks.
- Both the overnight-plus-first-half-hour and the mid-day components predict LH negatively with similar weight.
- The predictability disappears when the horizon is extended to include the next day's overnight and first half-hour, so the last-half-hour move is transitory.

## Signal construction
Cross-sectional: at close minus 60 minutes rank assets by return since the previous close; at close minus 30 minutes go long the bottom decile and short the top decile until the close; do not hold overnight (or fade the LH move into the next open). For a single asset the analogue is its return relative to a peer basket over the session.

## Relevance to SOL perpetuals at minutes to hours
The useful lesson is the split: index-level end-of-session flow is trend-following (hedgers), asset-specific end-of-session flow is contrarian (retail dip buyers, short covering). For SOL this suggests testing SOL-minus-BTC or SOL-minus-basket relative returns into session boundaries separately from market-wide moves, and expecting opposite signs. Retail attention cycles in crypto (US evening, Asian morning) may define the relevant "end of day". The 3 to 6 bp per day magnitude is too small for a taker strategy on its own.

## Caveats
Unpublished working paper, read in part. Equity-specific mechanisms (short-sale risk limits, retail broker flows) may not transfer. Gross of costs. Authors include asset-management affiliates. A single perp cannot run the cross-sectional sort without a basket of other perps.
