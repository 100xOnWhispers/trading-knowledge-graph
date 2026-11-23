---
title: "Foundations of Technical Analysis: Computational Algorithms, Statistical Inference, and Empirical Implementation"
authors: "Lo, Andrew W.; Mamaysky, Harry; Wang, Jiang"
year: 2000
venue: "Journal of Finance (2000); read as NBER Working Paper 7613"
url: "https://www.nber.org/system/files/working_papers/w7613/w7613.pdf"
pdf: "sources/16-oscillators-technical-rules/lo-2000-foundations-technical-analysis.pdf"
access: "full-text"
source_type: "peer-reviewed"
evidence_grade: "B"
topic: "16-oscillators-technical-rules"
asset_class: "equities"
horizon: "multi-day"
tags: "chart-patterns, kernel-regression, head-and-shoulders, conditional-distribution, pattern-recognition"
---

## Key insight
Chart patterns can be defined objectively and detected by algorithm. When that is done, the distribution of returns after a pattern completes differs from the unconditional distribution for most patterns, so the patterns carry information. The authors are explicit that information is not the same as trading profit.

## Method
Prices in a rolling window are smoothed with a Nadaraya-Watson kernel regression (Gaussian kernel). The bandwidth is 0.3 times the cross-validated value, because the cross-validated fit looked too smooth to professional technicians. Local extrema of the smoothed curve are then matched against geometric definitions of ten patterns: head-and-shoulders and its inverse, broadening tops and bottoms, triangle tops and bottoms, rectangle tops and bottoms, double tops and bottoms. Windows span l = 35 trading days plus d = 3 days, the lag ensuring the pattern is recognized only with data available at the time. The one-day return after completion is standardized and its distribution is compared with the unconditional one using a chi-square goodness-of-fit test on deciles and a Kolmogorov-Smirnov test. The tests are repeated conditioning on rising or falling volume.

## Data and sample
Individual NYSE/AMEX and Nasdaq stocks from CRSP, daily, 1962 to 1996, split into seven five-year subperiods and size quintiles.

## Reported results
- Goodness-of-fit: conditional and unconditional return distributions differ significantly for seven of the ten patterns on NYSE/AMEX and for all ten on Nasdaq.
- Kolmogorov-Smirnov: five of ten patterns significant on NYSE/AMEX (p-values from 0.000 to 0.021 for those five); all ten significant at the 5% level on Nasdaq, despite far fewer detected patterns there.
- Volume trend adds little incremental information in most cases.
- The authors conclude that several patterns provide incremental information, especially for Nasdaq stocks, and that this "does not necessarily imply" profitable trading.

## Signal construction
For a bot: on each new bar, fit a kernel smoother to the last 35 to 40 bars, extract alternating local maxima and minima, and test the last five extrema against the pattern inequalities (for head-and-shoulders: the middle peak is the highest, the two shoulders are within 1.5% of their average, and the two troughs likewise). The output is a categorical feature, not a position. Bandwidth and window length are the tunable parameters.

## Relevance to SOL perpetuals at minutes to hours
The method transfers to any bar size. The result does not transfer automatically. Its practical use here is as a feature generator for a classifier, and as a discipline: patterns must be machine-defined before testing. The finding that less liquid Nasdaq stocks showed stronger effects fits the crypto pattern that smaller coins show more rule predictability than Bitcoin (Hudson and Urquhart).

## Caveats
No transaction costs and no trading rule, by design. Thousands of stock-pattern pairs are tested and the test statistics assume independence that pooled stock returns violate, which the authors acknowledge. The bandwidth multiplier of 0.3 was chosen by eye. The pattern definitions themselves are a researcher choice, so data-snooping concerns apply at one remove.
