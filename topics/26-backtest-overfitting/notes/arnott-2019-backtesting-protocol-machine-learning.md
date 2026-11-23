---
title: "A Backtesting Protocol in the Era of Machine Learning"
authors: "Arnott, Rob; Harvey, Campbell R.; Markowitz, Harry"
year: 2019
venue: "Journal of Financial Data Science"
url: "https://people.duke.edu/~charvey/Research/Published_Papers/P138_A_backtesting_protocol.pdf"
pdf: "sources/26-backtest-overfitting/arnott-2019-backtesting-protocol-machine-learning.pdf"
access: "full-text"
source_type: "peer-reviewed"
evidence_grade: "B"
topic: "26-backtest-overfitting"
asset_class: "multi"
horizon: "n/a"
tags: "research-protocol, machine-learning, data-mining, out-of-sample, trading-costs"
---

## Key insight
Cheap data, free software and machine learning have made it trivial to mine strategies that look excellent and are false. Because financial data are limited and non-stationary, statistical corrections alone are insufficient; the authors propose a seven-category research protocol, a checklist of process discipline, to reduce false positives without rejecting everything.

## Method
A conceptual paper with one constructed demonstration. The protocol's categories and main prescriptions:
1. Research motivation: establish an economic foundation before running the test.
2. Multiple testing: keep track of everything tried, including interactions and the correlation between trials; beware the "parallel universe" problem where choices informed by the same history act as hidden tests.
3. Data and sample choice: define the sample in advance, check data integrity, justify outlier exclusions and transformations beforehand.
4. Cross-validation: acknowledge that hold-out data the researcher has lived through are not truly out of sample; an out-of-sample test that is consulted and followed by model changes is in-sample; include trading costs and fees in both periods.
5. Model dynamics: be aware of structural change and of crowding once a strategy is live; limit tweaking of a live model.
6. Model complexity: beware the curse of dimensionality; prefer the simplest practicable specification; seek interpretability.
7. Research culture: reward the quality of the science, not the finding of a winning backtest; accept that most tests fail.

## Data and sample
The demonstration uses NYSE stocks, January 1963 to December 2015: a long-short strategy chosen by searching combinations of letters in ticker symbols.

## Reported results
- The ticker-letter strategy was developed on 1963 to 1988 and "validated" out of sample on 1989 to 2015 with even stronger results, nearly 6% alpha a year, low turnover, no correlation with known factors, and a gain of nearly 50% in the financial crisis. It is meaningless by construction; thousands of combinations were searched.
- With 20 randomly selected strategies, one is expected to exceed a t-statistic of 2.0 by chance; with 20 variables, pairwise interactions number 190, not 22.
- The authors cite other work stating that with modest transaction costs the significance of many published anomalies essentially vanishes, and that 2.1 million equity models have been examined in one study.
- "The only true out of sample is the live trading experience."

## Signal construction
Not a signal. It is a process checklist to be applied to every research cycle: a written hypothesis before testing, a trial log, a frozen sample definition, a single-use final hold-out, costs in every evaluation, and a rule against modifying a model after it has seen the hold-out.

## Relevance to SOL perpetuals at minutes to hours
Fully transferable and probably the single most actionable source here for a small team or an automated research loop. Two points bite hardest in this project. First, crypto researchers have all lived through 2020 to 2026, so any historical hold-out is contaminated by knowledge of the regimes; only forward paper trading on the target venue is clean. Second, reinforcement-learning and evolutionary searches violate "keep track of what is tried" by default unless every evaluated policy or individual is logged. The demand for an economic rationale is harder to satisfy at minute horizons, where the rationale is microstructural (order flow, liquidation mechanics, funding incentives) and should be stated as such.

## Caveats
Opinion and checklist, not an empirical test that following the protocol improves live results; hence grade B despite the venue. Two authors are affiliated with an asset manager. The insistence on prior economic theory is contested: Chen, Lopez-Lira and Zimmermann (2022, in this folder) find that theory-backed predictors do not hold up better out of sample than data-mined ones.
