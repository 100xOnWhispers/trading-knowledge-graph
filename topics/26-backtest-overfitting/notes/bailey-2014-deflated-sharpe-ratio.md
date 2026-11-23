---
title: "The Deflated Sharpe Ratio: Correcting for Selection Bias, Backtest Overfitting and Non-Normality"
authors: "Bailey, David H.; Lopez de Prado, Marcos"
year: 2014
venue: "Journal of Portfolio Management (forthcoming 2014 per the preprint read)"
url: "https://www.davidhbailey.com/dhbpapers/deflated-sharpe.pdf"
pdf: "sources/26-backtest-overfitting/bailey-2014-deflated-sharpe-ratio.pdf"
access: "full-text"
source_type: "peer-reviewed"
evidence_grade: "A"
topic: "26-backtest-overfitting"
asset_class: "multi"
horizon: "n/a"
tags: "deflated-sharpe-ratio, selection-bias, multiple-testing, non-normality, effective-trials"
---

## Key insight
The Sharpe ratio of the best of many backtests is inflated by two things at once: selection among trials and non-normal returns. The deflated Sharpe ratio (DSR) is the probability that the true Sharpe is positive after raising the null threshold to the Sharpe one would expect from the best of N skill-less trials and after adjusting the standard error for skewness, kurtosis and sample length.

## Method
Expected maximum Sharpe among N independent trials whose estimated Sharpes have cross-trial variance V:

SR0 = sqrt(V) · [ (1 − γ) Z⁻¹(1 − 1/N) + γ Z⁻¹(1 − 1/(N e)) ],  γ ≈ 0.5772.

Deflated Sharpe ratio of the selected strategy (non-annualized SR, T observations, skewness γ3, kurtosis γ4):

DSR = Z[ (SR − SR0) · sqrt(T − 1) / sqrt(1 − γ3·SR + ((γ4 − 1)/4)·SR²) ].

DSR is the probabilistic Sharpe ratio evaluated at the threshold SR0 instead of zero. An appendix addresses correlated trials by estimating an implied number of independent trials from the average pairwise correlation, and notes the limits of average-correlation shortcuts. The paper also suggests planning trials in advance and invokes the secretary-problem (1/e) stopping rule.

## Data and sample
Analytical, with numerical experiments checking the expected-maximum approximation and one worked example. No market dataset.

## Reported results
Worked example: a strategy with annualized Sharpe 2.5 on 5 years of daily data (T = 1250), selected from N = 100 independent trials with cross-trial variance of annualized Sharpe of 1/2, skewness −3 and kurtosis 10. The paper computes SR0 ≈ 0.1132 (non-annualized, 250 observations per year) and DSR ≈ 0.9004, below the 0.95 level, so the discovery is rejected. Had the same result come after only N = 46 trials, DSR would have been 0.9505. With normal returns (skewness 0, kurtosis 3) DSR would be 0.9505 after N = 88 trials.

## Signal construction
Not a signal. It is an acceptance test. For each candidate promoted from a search, record: per-bar net returns of the winner (for SR, T, skewness, kurtosis), the Sharpe of every trial (for V), and the count of effectively independent trials N. Compute DSR and require, for example, DSR above 0.95. The same formula with SR0 fixed at a benchmark gives a live-monitoring statistic.

## Relevance to SOL perpetuals at minutes to hours
The inputs are all available from a logged search, so DSR is practical for a bot's research pipeline. Three points need care at intraday frequency. First, T should count roughly independent observations; overlapping or autocorrelated minute returns overstate T, so compute on trade-level or daily net returns. Second, crypto strategy returns are strongly skewed and fat-tailed, and the kurtosis term can dominate. Third, N must reflect everything tried, including optimizer iterations, feature variants and the generations of an evolutionary search, clustered to an effective count.

## Caveats
Assumes trial Sharpes are normally distributed across trials and that N independent trials can be identified; estimating effective N from correlated trials is the weak link and the appendix is explicit about that. Returns are assumed IID within a strategy; serial correlation is not handled (see Lo 2002). A high DSR does not validate fills or costs; it only addresses statistical selection.
