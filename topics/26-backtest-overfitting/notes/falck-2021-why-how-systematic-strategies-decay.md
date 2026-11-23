---
title: "Why and How Systematic Strategies Decay"
authors: "Falck, Antoine; Rej, Adam; Thesmar, David"
year: 2021
venue: "arXiv preprint 2105.01380"
url: "https://arxiv.org/pdf/2105.01380"
pdf: "sources/26-backtest-overfitting/falck-2021-why-how-systematic-strategies-decay.pdf"
access: "full-text"
source_type: "working-paper"
evidence_grade: "B"
topic: "26-backtest-overfitting"
asset_class: "equities"
horizon: "multi-day"
tags: "alpha-decay, overfitting-proxies, sharpe-decay, publication-year, robustness"
---

## Key insight
The out-of-sample drop in a strategy's Sharpe ratio is partly predictable in advance from features of the backtest itself. Across published equity anomalies, the publication year and a small set of overfitting proxies (how many operations define the signal, and how sensitive the in-sample Sharpe is to outliers) explain close to half of the cross-sectional variance in decay, while proxies for arbitrage capital add little.

## Method
The authors replicate published anomalies, define a discount ratio q = SR_out-of-sample / SR_in-sample, and measure it in three out-of-sample settings: after publication, on large-capitalization US subsets, and on international stock pools. They then regress Sharpe decay on ex-ante covariates:
- arbitrage-related: liquidity, signal speed, size of the stocks traded, cost of the short leg;
- overfitting-related: a dummy for in-sample t-statistic below 3; "log quantile span" (dispersion of in-sample Sharpe across choices of portfolio quantile from 5% to 35%); deviation of the best quantile's Sharpe from the baseline; dummies for more than two data fields and more than two operations in the signal definition; and two measures of sensitivity of in-sample Sharpe to removing extreme observations;
- publication year.

## Data and sample
72 stock-return anomalies from the finance and accounting literature, built from CRSP and Compustat (factors published after 2010 excluded); data to December 2018; eight international pools for external tests.

## Reported results
- Mean in-sample Sharpe of the 72 factors is 0.98.
- Post-publication Sharpe is approximately linear in in-sample Sharpe with slope 0.57, an average drop of 43%; the median discount ratio is 0.55.
- Sharpe decay is 33% on the largest 1,000 US stocks and 20% on the largest 500 after size adjustment; across international pools the discount ratio is close to 0.4.
- Publication year alone explains 30% of the variance in Sharpe decay; each later publication year adds 5 percentage points of decay.
- The number of operations and the two outlier-sensitivity measures together add another 15% of explanatory power.
- The in-sample t-statistic is only a weak predictor of decay, contrary to the authors' expectation.
- Arbitrage-related variables are sometimes significant but add marginal predictive power.

## Signal construction
Not a signal. It suggests a pre-deployment scorecard. For each candidate strategy compute: (1) the spread of in-sample Sharpe across reasonable variations of construction parameters; (2) the gap between the chosen parameter's Sharpe and the neighbourhood average; (3) the change in Sharpe when the best few days or trades are removed; (4) the count of inputs and operations in the signal. Apply a larger haircut to strategies that score badly.

## Relevance to SOL perpetuals at minutes to hours
The asset class and horizon differ, but the diagnostics are generic and cheap. Parameter-neighbourhood sensitivity and outlier sensitivity are especially apt for crypto, where a handful of liquidation cascades can supply most of a backtest's profit. The complexity result bears directly on evolved or machine-generated signals with deep expression trees: more operations predicted more decay. The finding that newer discoveries decay more is consistent with easier mining and faster arbitrage, both more extreme in crypto.

## Caveats
Seventy-two monthly equity anomalies is a small cross-section and the explanatory regressions are themselves a specification search. Decay is measured on Sharpe before costs. Publication year cannot separate "more mining" from "faster arbitrage". Not peer reviewed in the version read. Transfer to intraday crypto is by analogy only.
