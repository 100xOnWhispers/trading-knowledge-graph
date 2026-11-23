---
title: "skfolio documentation: CombinatorialPurgedCV (combinatorial purged cross-validation)"
authors: "skfolio developers"
year: 2026
venue: "skfolio library documentation (page accessed 2026-11-22; publication year of the page not confirmed)"
url: "https://skfolio.org/generated/skfolio.model_selection.CombinatorialPurgedCV.html"
pdf: "none"
access: "full-text"
source_type: "documentation"
evidence_grade: "D"
topic: "26-backtest-overfitting"
asset_class: "multi"
horizon: "n/a"
tags: "cpcv, purging, embargo, cross-validation, backtest-paths, machine-learning"
---

## Key insight
Combinatorial purged cross-validation (CPCV) replaces the single historical path of a walk-forward test with many train/test combinations, from which several complete out-of-sample backtest paths can be reassembled. Purging and embargoing remove training observations that would leak information from the test folds. The page documents an open-source implementation and attributes the method to Lopez de Prado, "Advances in Financial Machine Learning" (2018), which was not itself read in this session.

## Method
As documented on the page:
- The sample is cut into `n_folds` consecutive, unshuffled folds (minimum 3; default 10). The first n_folds − 1 folds hold n_samples // n_folds observations each and the last takes the remainder.
- Each split uses `n_test_folds` folds for testing (minimum 2; default 8) and the remaining folds for training. With a single test fold the page recommends ordinary K-fold.
- `purged_size`: number of observations removed from the training set at each boundary adjacent to a test set, on both sides. Purging removes training observations whose labels overlap in time with test labels.
- `embargo_size`: number of observations removed from the start of each training segment that immediately follows a test set, because financial features are serially correlated.
- Unlike K-fold, which yields one recombined test path, the class can recombine multiple test paths from the train/test combinations; helper methods report the number of splits and of test paths and plot the fold layout.

The page does not print the counting formulas. Its docstring example (3 folds, 2 test folds) yields 3 splits, consistent with the number of splits being the binomial coefficient C(n_folds, n_test_folds); Gort et al. (2022, in this folder) likewise report 10 splits for 5 groups with 2 validation groups. The usual statement that the number of paths equals C(N, k)·k/N comes from the cited book and is not confirmed from the page.

## Data and sample
None. Software documentation.

## Reported results
None. The page makes no empirical claims. An independent comparison (Arian, Norouzi and Seco 2024, Knowledge-Based Systems) exists; a web search summary seen in this session described it as finding lower probability of backtest overfitting and better deflated-Sharpe statistics for CPCV than for K-fold, purged K-fold and walk-forward in a synthetic environment, but that paper could not be opened, so this is unverified secondary information.

## Signal construction
Not a signal. It is a validation scheme for any model that is fitted to data (supervised learners, reinforcement-learning policies, parameter-optimized rules):
1. Choose N folds so each spans several distinct market regimes, and k test folds.
2. Set the purge length at least equal to the label horizon plus the longest feature look-back that overlaps the boundary; set the embargo to cover residual serial correlation.
3. Fit on every training combination, predict on the test folds, and reassemble the out-of-sample paths.
4. Judge the model on the distribution of path-level performance (median and lower quantiles), not on one path.

## Relevance to SOL perpetuals at minutes to hours
Purging is essential at intraday frequency: a label defined over the next 30 minutes and features built from the last few hours overlap heavily with neighbouring observations, and unpurged K-fold on such data reports inflated accuracy. For a few years of SOL history, CPCV extracts a distribution of outcomes where walk-forward gives one path dominated by whichever regime came last. It also produces the per-configuration out-of-sample return matrix that PBO and the deflated Sharpe ratio need. Training on data from after the test period is the price: it is acceptable for judging whether a model class generalizes, but it is not a simulation of live deployment, so a final walk-forward or paper-trading stage is still needed.

## Caveats
Documentation, not evidence; grade D reflects the page, not the method. Step 2 and step 4 above are this note's practical reading and are not prescribed on the page. The defaults (10 folds, 8 test folds) train on only a fifth of the data per split, which may be too little for data-hungry models. CPCV does not address non-stationarity: a model can pass on shuffled-order folds and still fail when the future differs from all past folds. Multiple-testing across model variants is a separate correction.
