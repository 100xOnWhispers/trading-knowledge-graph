---
title: "AutoAlpha: an Efficient Hierarchical Evolutionary Algorithm for Mining Alpha Factors in Quantitative Investment"
authors: "Zhang, Tianping; Li, Yuanqi; Jin, Yifei; Li, Jian"
year: 2020
venue: "arXiv preprint 2002.08245v2"
url: "https://arxiv.org/pdf/2002.08245"
pdf: "sources/25-evolutionary-algorithms/zhang-2020-autoalpha-hierarchical-evolutionary-alpha-mining.pdf"
access: "full-text"
source_type: "working-paper"
evidence_grade: "C"
topic: "25-evolutionary-algorithms"
asset_class: "equities"
horizon: "daily"
tags: "genetic-programming, formulaic-alpha, quality-diversity, gplearn, premature-convergence, information-coefficient"
---

## Key insight
Plain genetic programming (the `gplearn` package) is a poor alpha miner because effective formulas are sparse and the population keeps converging on the same one. AutoAlpha fixes this with three changes: grow formulas depth by depth from a pool of effective sub-expressions, penalize candidates that resemble alphas already found, and replace parents only with their own offspring. On Chinese stocks it found an order of magnitude more distinct alphas above an IC threshold than `gplearn`.

## Method
A formula is a tree with raw fields at the leaves and operators from the Alpha101 set at the nodes. Fitness is the information coefficient, the time average of the daily cross-sectional Pearson correlation between alpha values and forward returns.

- Hierarchy: enumerate all depth-1 alphas, keep the effective ones as a gene pool, then evolve depth 2 from that pool, and so on. Motivation: the authors observed that most good deep alphas contain a good shallow "root gene" (their example is `vwap/close`).
- PCA-QD: represent each alpha by the first principal component of its date-by-stock value matrix; if the correlation of that component with any recorded alpha exceeds 0.9, the candidate's fitness is set to zero. This approximates a pairwise similarity check at lower cost.
- Warm start: generate K times the population and keep the top 1/K by IC.
- Replacement: two offspring replace their two parents only when the better child beats the parents, so one gene family cannot take over the population.

Mined alphas feed LightGBM and XGBoost rankers; the ensemble picks stocks.

## Data and sample
CSI 300 constituents for mining, CSI 800 for backtests. Training 1 January 2010 to 31 August 2017, testing 1 September 2017 to 31 July 2019. Daily bars, holding periods of 1 and 5 days.

## Reported results
- Top-5 alphas at h = 1: training IC 7.74% to 8.36%, test IC 5.55% to 7.10% on CSI 300.
- Number of diverse alphas with IC above 0.05: Alpha101 0, gplearn 35, AutoAlpha 434 (h = 1); 0, 7 and 415 (h = 5). Average IC of the top 50: 1.02%, 6.10%, 7.50% (h = 1).
- Backtest at h = 1 with 0.3% transaction cost: annualized return 90.0% and Sharpe 3.39 for AutoAlpha, 61.8% and 2.34 for gplearn, 29.5% and 1.06 for Alpha101, against a market return of -4.1%.

## Signal construction
Not a signal. To use the method on one instrument, replace cross-sectional IC with the time-series correlation between the alpha and the forward return over the target horizon, and apply the similarity penalty to the alpha's time series directly (no PCA needed with a single asset).

## Relevance to SOL perpetuals at minutes to hours
The three anti-convergence devices address the main practical failure of GP on any market and are independent of asset class. The depth-wise build also limits formula complexity, which is itself an overfitting control. The reported returns do not transfer.

## Caveats
Seven-page workshop-style paper with hyperparameters omitted. The IC counts in the comparison table appear to be measured on training data. The test window is 23 months of one market. The backtest Sharpe of 3.39 at daily turnover with a flat 0.3% cost is not credible as a live expectation. No multiple-testing adjustment for the thousands of formulas evaluated.
