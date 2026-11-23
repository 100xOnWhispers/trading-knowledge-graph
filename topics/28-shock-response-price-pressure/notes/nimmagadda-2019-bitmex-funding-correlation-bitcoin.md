---
title: "BitMEX Funding Correlation with Bitcoin Exchange Rate"
authors: "Nimmagadda, Sai Srikar; Sasanka, Ammanamanchi Pawan"
year: 2019
venue: "arXiv:1912.03270v1 (preprint)"
url: "https://arxiv.org/pdf/1912.03270"
pdf: "sources/28-shock-response-price-pressure/nimmagadda-2019-bitmex-funding-correlation-bitcoin.pdf"
access: "full-text"
source_type: "working-paper"
evidence_grade: "C"
topic: "28-shock-response-price-pressure"
asset_class: "crypto"
horizon: "hours"
tags: "funding-rate, granger-causality, garch, bitmex, perp-state, weak-evidence"
---

## Key insight
An early attempt to test whether the perpetual funding rate leads the Bitcoin price at the 8-hour frequency. Granger tests reject non-causality in both directions: funding helps predict the 8-hour price change and price helps predict funding. The paper does not report the sign or size of the relation, runs no out-of-sample test and no trading rule, so it shows statistical linkage only. It is included because almost nothing else tests funding as a predictor of the perp's own return at this horizon.

## Method
Engle's ARCH test on the differenced funding rate; augmented Dickey-Fuller tests for stationarity; Granger causality tests between first-differenced funding and first-differenced price with lag length chosen by AIC; comparison of GARCH-family models for the funding rate by information criteria. The paper restates the BitMEX funding formula: `F = P + clamp(I - P, 0.05%, -0.05%)`, with the premium `P` an 8-hour time-weighted average of minute premium readings.

## Data and sample
BitMEX XBTUSD inverse perpetual funding rate and Bitstamp BTC/USD price, both at 8-hour frequency, 4 June 2016 to 3 October 2019 (3,649 observations).

## Reported results
- ARCH effects in funding changes are significant (ARCH coefficient 0.284, p = 0.000).
- Funding is stationary in levels; price is stationary only in first differences.
- Granger tests: "8-hour price does not Granger-cause funding" is rejected with F = 4.29 (p about 5e-08); "funding does not Granger-cause 8-hour price" is rejected with F = 7.11 (p about 1e-15).
- EGARCH(1,1) fits funding best by AIC, SIC and HQC.
- The conclusion asserts that extremely high funding would go with high prices; no coefficient or test supporting a direction is shown.
- The authors name a funding-based position rule compared with buy-and-hold as future work.
- Scope record: horizon 8 hours; conditioning variable change in funding rate; sign not reported; costs not applicable (no strategy).

## Signal construction
The paper does not define one. The testable version it points to: at each funding timestamp, regress the perp's return over the next 1, 4 and 8 hours on the funding level, the funding change and an indicator for funding at its clamp or cap, with past returns as controls. Because funding is by construction an average of the past premium, which itself follows past returns, the regression must control for the return over the previous funding window or the "prediction" may only restate momentum or reversal in price.

## Relevance to SOL perpetuals at minutes to hours
The useful content is the bidirectional result: funding is mostly an echo of the recent price path. That is a reason for scepticism about funding as an independent short-horizon predictor. Later and better evidence in this repository points the same way: Kitron and Wengrowicz (2026, topic 08) find that conditioning 15-minute reversal on basis, funding rate and the funding clock adds nothing. What remains untested is the tail: whether funding at extreme levels changes the response to a shock.

## Caveats
Granger causality at lag lengths that are not reported, with no sign, no effect size and no out-of-sample check. The price series is spot from a different exchange. Differencing funding discards the level, which is what traders watch. The sample is BitMEX-dominated 2016-2019, a different market structure from today's. Not peer-reviewed; presentation has errors (for example the funding timestamps are listed as 4:00, 12:00 and 8:00 UTC).
