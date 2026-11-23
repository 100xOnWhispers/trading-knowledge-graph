---
title: "The Probability of Backtest Overfitting"
authors: "Bailey, David H.; Borwein, Jonathan M.; Lopez de Prado, Marcos; Zhu, Qiji Jim"
year: 2015
venue: "Author preprint (revised February 2015); cited by later work as Journal of Computational Finance"
url: "https://www.davidhbailey.com/dhbpapers/backtest-prob.pdf"
pdf: "sources/26-backtest-overfitting/bailey-2015-probability-backtest-overfitting.pdf"
access: "full-text"
source_type: "peer-reviewed"
evidence_grade: "A"
topic: "26-backtest-overfitting"
asset_class: "multi"
horizon: "n/a"
tags: "pbo, cscv, cross-validation, backtest-overfitting, model-selection"
---

## Key insight
Overfitting is a property of the selection process, not of a single strategy. The paper defines the probability of backtest overfitting (PBO) as the probability that the configuration chosen as best in-sample ranks below the median of all tried configurations out-of-sample, and gives a model-free, nonparametric way to estimate it called combinatorially symmetric cross-validation (CSCV).

## Method
1. Build a T × N matrix M of per-period profit and loss, one column per configuration tried, rows synchronous.
2. Split the rows into an even number S of disjoint blocks of equal length.
3. Form every combination of S/2 blocks as a training set J; the complement is the test set. The count is C(S, S/2).
4. For each combination: compute the performance statistic (for example Sharpe) of every column in-sample and out-of-sample; find the in-sample best n*; compute its relative out-of-sample rank ω = rank/(N + 1); compute the logit λ = ln(ω / (1 − ω)).
5. PBO is the share of combinations with λ ≤ 0 (the in-sample winner is below the out-of-sample median).

The same output gives three further diagnostics: the regression of out-of-sample on in-sample performance ("performance degradation"), the probability of an out-of-sample loss, and stochastic dominance of the selected strategy over a random pick.

## Data and sample
Simulated strategy sets with and without true skill, plus one real investment strategy example. No specific market is the object of study.

## Reported results
- Hold-out validation is argued to be unreliable for backtests because it ignores the number of trials, has high variance across choices of hold-out period, and is inadequate for small samples.
- The authors suggest S = 16 as a reasonable default; the text gives 12,780 combinations for S = 16 (C(16, 8) evaluates to 12,870, so the printed figure appears to be a typo) and states the standard error of the PBO estimate is below 0.0045.
- With more than six years of data, S = 24 gives quarter-length blocks and 2,704,156 logits.
- An overfit example shows PBO of 74%; a real strategy example shows PBO of 0.04%.
- One suggested use is to reject selection processes with PBO above 0.05.
- If in-sample rank carries no information, the logits are approximately standard normal, which gives a baseline.

## Signal construction
Not a signal. It is a validation step applied to the full set of configurations from any search. Inputs: the per-bar or per-day net returns of every configuration evaluated (not just the winner). Output: PBO, the degradation slope and the probability of loss. Run once per search, before any capital decision.

## Relevance to SOL perpetuals at minutes to hours
CSCV is cheap because it reuses returns already produced by the search; no retraining is needed. For a minutes-to-hours bot, aggregate each configuration's net P&L to a common grid (hourly or daily), choose S so that each block spans at least several weeks of crypto regimes, and require a low PBO before promoting a configuration. It applies unchanged to hyperparameter sweeps of machine-learning and reinforcement-learning models and to the final population of a genetic search.

## Caveats
CSCV does not retrain models on each training combination, so it measures overfitting of the selection step only. Blocks are assumed exchangeable; with strong regime dependence the training set straddles the test set and leakage across block boundaries is not purged. PBO says nothing about whether the best strategy is profitable, only whether in-sample ranking transfers. Results depend on N being large and on the pool of configurations; trimming the pool to "top candidates" before running CSCV biases it.
