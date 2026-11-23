---
title: "Backtesting"
authors: "Harvey, Campbell R.; Liu, Yan"
year: 2015
venue: "Journal of Portfolio Management"
url: "https://people.duke.edu/~charvey/Research/Published_Papers/P120_Backtesting.PDF"
pdf: "sources/26-backtest-overfitting/harvey-2015-backtesting.pdf"
access: "full-text"
source_type: "peer-reviewed"
evidence_grade: "A"
topic: "26-backtest-overfitting"
asset_class: "multi"
horizon: "n/a"
tags: "haircut-sharpe-ratio, multiple-testing, bonferroni, holm, bhy, profit-hurdle"
---

## Key insight
The industry habit of cutting a backtested Sharpe ratio by 50% is a crude rule of thumb. Deriving the haircut from multiple-testing theory shows that it should be nonlinear: marginal Sharpe ratios deserve to be cut almost entirely, while very high Sharpe ratios are penalized only moderately.

## Method
1. Convert the strategy's Sharpe ratio into a t-ratio and a single-test p-value.
2. Adjust the p-value for the number of tests assumed, using Bonferroni, Holm (both control family-wise error) or Benjamini-Hochberg-Yekutieli (BHY, controls false discovery rate). Holm and BHY need the distribution of p-values of other strategies tried; the authors draw these from the structural model of Harvey, Liu and Zhu, which allows for correlation between strategies.
3. Convert the adjusted p-value back to a t-ratio and then to a "haircut Sharpe ratio".
The same machinery inverted gives the minimum average return a strategy must earn to be significant given its volatility, sample length and the number of tests. The Sharpe ratio is first corrected for autocorrelation. Matlab code (Haircut_SR and Profit_Hurdle) is provided.

## Data and sample
Methodological; illustrations use assumed inputs and the 316-factor database of Harvey, Liu and Zhu for the cross-strategy distribution.

## Reported results
- Worked example: annualized Sharpe 1.0 over 120 months, monthly autocorrelation 0.1, 100 tests, average correlation 0.4 among strategies. The autocorrelation-corrected Sharpe is 0.912; under BHY the haircut Sharpe is 0.438, a haircut of 52.0%.
- Profit hurdle example: 240 monthly observations, 10% annual volatility, 300 tests. A single test requires 0.365% per month (4.4% a year); BHY requires 0.616% per month (7.4% a year).
- BHY haircuts are much smaller than Bonferroni or Holm for small Sharpe ratios (below 0.4) and similar for large ones (above 1.0).
- The authors advocate BHY for finance, reasoning that controlling the rate of false discoveries is more sensible than controlling their absolute number.
- They state that a true out-of-sample test (not a historical hold-out) is cleaner where available.

## Signal construction
Not a signal. It is a haircut procedure. Inputs: backtest Sharpe, number of observations and frequency, return autocorrelation, an honest count of tests, and an assumed average correlation among them. Output: the haircut Sharpe to use in sizing and in go/no-go decisions, and the minimum net return per period the strategy must clear.

## Relevance to SOL perpetuals at minutes to hours
Useful as the bridge from "backtest Sharpe" to "Sharpe to plan around". The nonlinearity is the practical message: a crypto intraday strategy with a backtest Sharpe of 1 from a large search is likely worth nothing, while one with a Sharpe of 3 survives most of the adjustment, provided its costs and fills are real. The profit-hurdle form translates naturally into basis points per trade that a signal must clear after fees and funding.

## Caveats
The authors list them: Sharpe ratios mislead for non-normal or option-like payoffs; volatility may not capture risk; the significance level, the adjustment method and above all the number of tests are judgment calls. The cross-strategy distribution comes from monthly equity factors and may not describe intraday crypto strategies. The method adjusts for statistical multiplicity only, not for look-ahead, cost or fill errors.
