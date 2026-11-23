---
title: "Identifying and evaluating horizontal support and resistance levels: an empirical study on US stock markets"
authors: "Zapranis, Achilleas; Tsinaslanidis, Prodromos E."
year: 2012
venue: "Applied Financial Economics, 22(19), pp. 1571-1585"
url: "https://ideas.repec.org/a/taf/apfiec/v22y2012i19p1571-1585.html"
pdf: "none"
access: "abstract-only"
source_type: "peer-reviewed"
evidence_grade: "B"
topic: "17-auction-orderflow-practitioner"
asset_class: "equities"
horizon: "daily"
tags: "support-resistance, turning-points, rule-based-detection, efficient-market, buy-and-hold, negative-result"
---

## Key insight
A rule-based detector of horizontal support and resistance, built to imitate what chartists do by eye, finds levels that have some ability to predict trend interruptions (support more than resistance) but that do not produce returns above buy-and-hold. This is the cleanest statement of the gap that runs through this topic: levels can be statistically "real" and still not be a profitable trading rule.

## Method
Only the abstract (RePEc record) was read. It states that the authors propose a rule-based identification of horizontal support and resistance levels that follows principles in well-known technical-analysis manuals, using historical price turning points instead of the highest or lowest price over a fixed window. They then test whether the levels predict trend reversals and whether trading on them yields abnormal returns. The turning-point algorithm, the bounce definition and the benchmark construction were not visible.

## Data and sample
From the abstract: daily closing prices, adjusted for dividends and splits, of NASDAQ and NYSE stocks over roughly two decades. The number of stocks and exact dates were not visible.

## Reported results
From the abstract only:
- Results are consistent with the efficient market hypothesis.
- Support levels outperform resistance levels in predicting trend interruptions.
- Neither generates excess returns relative to a simple buy-and-hold strategy.

No magnitudes were visible.

## Signal construction
The useful element is the detection idea: derive levels from clusters of past turning points, not from window extremes. A workable online version for intraday data: (1) mark turning points with a zigzag or local-extreme filter whose threshold is a multiple of recent volatility; (2) cluster turning-point prices with a tolerance (for example, by merging points within a fraction of the average bar range); (3) score each cluster by the number and recency of its points; (4) treat clusters above a score threshold as levels. This differs from the rolling minimum and maximum of Chung and Bellotti in allowing several levels inside the current range. Feed level distance and score as features; do not trade the level alone.

## Relevance to SOL perpetuals at minutes to hours
The horizon (daily) and asset class (US equities with a strong upward drift) differ from SOL perps, and the abstract's asymmetry between support and resistance may simply reflect that drift. What transfers is the discipline of the conclusion: a bounce-prediction result must be converted into a net-of-cost return test against a passive or random-entry benchmark before it counts. For SOL the benchmark should be direction-neutral (random entry with matched holding time), since buy-and-hold is not a meaningful benchmark for a minutes-to-hours bot.

## Caveats
Abstract-only, so the size of the predictive effect and the trading rule are unknown. Daily closes cannot see intraday touches, which is where practitioners claim levels act. Equity-specific drift affects both the asymmetry and the buy-and-hold comparison. The authors' choice of detector is one of many; a negative profitability result for one detector does not rule out others, though it shifts the burden of proof.
