---
title: "... and the Cross-Section of Expected Returns"
authors: "Harvey, Campbell R.; Liu, Yan; Zhu, Heqing"
year: 2014
venue: "NBER Working Paper 20592 (published in Review of Financial Studies 29(1), 2016, per later citations)"
url: "https://www.nber.org/system/files/working_papers/w20592/w20592.pdf"
pdf: "sources/26-backtest-overfitting/harvey-2014-cross-section-expected-returns.pdf"
access: "full-text"
source_type: "peer-reviewed"
evidence_grade: "A"
topic: "26-backtest-overfitting"
asset_class: "equities"
horizon: "multi-day"
tags: "multiple-testing, t-statistic-hurdle, false-discovery-rate, factor-zoo, publication-bias"
---

## Key insight
After hundreds of factors have been tested on the same data, the conventional t-statistic of 2.0 is no longer a meaningful hurdle. Treating the literature as one large multiple-testing exercise, the authors conclude that a newly proposed factor should clear a t-ratio of about 3.0, and that most claimed findings in this area are likely false.

## Method
The authors catalogue published factors and apply three standard multiple-testing adjustments to the sequence of reported t-ratios: Bonferroni and Holm (which control the family-wise error rate, FWER) and Benjamini-Hochberg-Yekutieli (BHY, which controls the false discovery rate, FDR). They then build a new structural framework, estimated on the observed t-ratios, that allows for correlation among tests and for unobserved (unpublished) tests, and produce a time series of significance cutoffs from 1967 forward, with a projection to 2032.

## Data and sample
313 papers published in leading journals plus selected working papers, yielding 316 factors for the cross-section of US equity returns; reported t-ratios from 1967 to 2012.

## Reported results
- Bonferroni benchmark t-ratio rises from 1.96 to 3.78 by 2012 and reaches 4.00 in 2032; Holm tracks it closely.
- BHY at 1% FDR stabilizes at 3.39 after 2010; at 5% FDR the benchmark is 2.78 in 2012. The authors summarize the minimum threshold for 5% significance as about 2.8 (p-value 0.5%).
- Allowing for correlation and missing tests, a t-ratio of 3.9 controls FWER at 5% and 3.0 controls FDR at 1%.
- The recommended hurdle of 3.0 corresponds to a p-value of 0.27%, and the authors argue it is probably too low because their count of tried factors is an underestimate.
- A factor derived from first principles may deserve a lower hurdle than a purely empirical one, but 2.0 is not appropriate even then.
- Higher correlation among tests lowers the required adjustment; with perfectly correlated tests no adjustment is needed.

## Signal construction
Not a signal. It supplies a significance hurdle. For any candidate predictor, convert the backtest into a t-statistic of mean net return (t = Sharpe × sqrt(years) for an annualized Sharpe) and require it to exceed a multiple-testing-adjusted threshold; 3.0 is the paper's floor for a field with hundreds of prior tests.

## Relevance to SOL perpetuals at minutes to hours
The numbers are specific to monthly US equity factors, but the logic transfers fully: crypto technical and order-flow signals have been mined by thousands of participants on the same public data, and an in-house feature search adds its own multiplicity. A t-statistic of 3 on a few years of SOL history requires an annualized Sharpe near 1.5 to 2, a far higher bar than "positive after costs". The FWER-versus-FDR distinction matters for design: a bot that trades one strategy cares about FWER; one that ensembles many weak signals can tolerate FDR control.

## Caveats
Equity cross-section only; no trading costs; the hurdle depends on an estimated count of unobserved tests. Later work disputes the conclusion that most findings are false (see Jensen, Kelly and Pedersen 2021 and Chen, Lopez-Lira and Zimmermann 2022 in this folder). The t-statistic framing assumes roughly normal, weakly dependent returns. The Sharpe-to-t conversion in the relevance section is standard arithmetic, not a result of this paper.
