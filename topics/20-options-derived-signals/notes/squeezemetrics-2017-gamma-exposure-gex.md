---
title: "Gamma Exposure (GEX): Quantifying hedge rebalancing in SPX options"
authors: "SqueezeMetrics Research"
year: 2017
venue: "SqueezeMetrics white paper (March 2016, revised December 2017)"
url: "https://squeezemetrics.com/monitor/download/pdf/white_paper.pdf"
pdf: "none"
access: "full-text"
source_type: "practitioner"
evidence_grade: "D"
topic: "20-options-derived-signals"
asset_class: "options"
horizon: "daily"
tags: "gamma-exposure, gex, dealer-hedging, open-interest, spx, volatility-regime, practitioner"
---

## Key insight
This eight-page note is the origin of the "GEX" number quoted across trading media. It computes dealer gamma from open interest alone by assuming that dealers are long every call and short every put, and claims that the resulting figure separates next-day S&P 500 volatility regimes better than the VIX does. The claim rests on quartile comparisons, and the sign assumption is specific to US index options.

## Method
Four stated assumptions: (1) every option trade has a delta-hedger on one side; (2) calls are sold by investors and bought by market makers (overwriting); (3) puts are bought by investors and sold by market makers (protection); (4) market makers hedge exactly to delta. Then, per strike:

`GEX_call = gamma * OI * 100`, `GEX_put = gamma * OI * (-100)`

summed over all strikes and expiries, denominated in dollars for the index. Positive GEX implies dealers buy dips and sell rallies, damping volatility; negative GEX implies the opposite; near zero implies no dealer influence.

## Data and sample
SPX options. The sample period, data vendor and number of observations do not appear in the text extracted from the document (figures were not inspected).

## Reported results
- One-day standard deviation of SPX returns after the lowest quartile of VIX closes is 0.51%, and 0.66% after the second-lowest quartile.
- After the highest and second-highest quartiles of GEX it is 0.55% and 0.85%.
- A scatter of SPX returns against prior-day GEX is described as showing volatility rising sharply as GEX falls below zero.
- A stock-selection screen for GEX near zero "yielded excess returns"; no figures are given.

No significance tests, no out-of-sample period, no direction-of-return claim.

## Signal construction
Inputs: open interest and gamma for every listed option, once a day after open interest updates. Compute the signed sum above and scale to dollars per 1% move (`* S^2 * 0.01`). Use as a volatility regime flag for the following session.

For crypto the sign rule has to be replaced. Deribit flow does not follow the equity-index pattern: [alexander-2023-net-buying-pressure-bitcoin-option-trades](alexander-2023-net-buying-pressure-bitcoin-option-trades.md) reports that traders consistently sell out-of-the-money options and buy at-the-money ones, in calls and puts alike, with a call to put volume ratio near 54:46 and a roughly symmetric smile. "Dealers long calls, short puts" is therefore unsupported. Use trade-signed inventory as in [amberdata-2026-gamma-exposure-gex-documentation](amberdata-2026-gamma-exposure-gex-documentation.md).

## Relevance to SOL perpetuals at minutes to hours
The mechanism (dealer hedging damps or amplifies moves depending on the sign of gamma) is the same one tested with proper data by Baltussen and co-authors (topic 11) and, for bitcoin, by [atanasova-2025-aggregate-illiquidity-crypto-option-returns](atanasova-2025-aggregate-illiquidity-crypto-option-returns.md). This document matters mainly as a warning: many crypto "GEX" dashboards copy its open-interest formula, and a bot that ingests them inherits an untested sign assumption. Any GEX input should be checked against subsequent realized volatility before use.

## Caveats
A marketing document from a data vendor; no sample period appears in the text extracted. The four assumptions are strong, and the document itself says the evidence for assumption 2 is partly circular ("(circularly) the effects of GEX"). Volatility clustering alone could produce the quartile result, because GEX correlates with the level of the index relative to put strikes; no control is shown. The file carries a notice restricting redistribution, so no copy is stored in this repository.
