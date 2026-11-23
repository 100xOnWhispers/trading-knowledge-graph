---
title: "Regime-Switching Models"
authors: "Hamilton, James D."
year: 2005
venue: "Manuscript prepared for the Palgrave Dictionary of Economics (author page, UC San Diego)"
url: "https://econweb.ucsd.edu/~jhamilton/palgrav1.pdf"
pdf: "sources/01-macro-regime-detection/hamilton-2005-regime-switching-models-palgrave.pdf"
access: "full-text"
source_type: "working-paper"
evidence_grade: "B"
topic: "01-macro-regime-detection"
asset_class: "multi"
horizon: "n/a"
tags: "markov-switching, hidden-markov-model, hamilton-filter, filtered-probability, smoothed-probability, methodology"
---

## Key insight
Hamilton's own short statement of the Markov-switching framework he introduced in 1989. A series is described by a small set of parameter regimes whose index follows an unobserved Markov chain, and the probability of each regime given data up to today comes out of a simple recursive filter that also delivers the likelihood. The essay is explicit about which quantities use only past data (filtered) and which use the whole sample (smoothed), and about why choosing the number of regimes is statistically awkward.

## Method
Model: `y_t = c_{s_t} + phi*y_{t-1} + eps_t`, with `s_t` a two-state Markov chain, `Pr(s_t=j | s_{t-1}=i) = p_ij`. The filter takes `xi_{i,t-1} = Pr(s_{t-1}=i | data to t-1)` and the regime densities `eta_jt = f(y_t | s_t=j, past)` and returns

`xi_jt = sum_i p_ij * xi_{i,t-1} * eta_jt / f(y_t | past)`, where `f(y_t | past) = sum_i sum_j p_ij * xi_{i,t-1} * eta_jt`.

Summing `log f(y_t | past)` over t gives the log likelihood, maximised numerically. The vector form handles N regimes and vector observations, and the regime densities need not be Gaussian. Smoothed probabilities `Pr(s_t | all data to T)` use Kim's (1994) algorithm. Extensions covered: transition probabilities that depend on observables, Gibbs-sampling Bayesian estimation, regime-switching GARCH (Gray 1996; Haas, Mittnik and Paolella 2004), and Markov-switching state-space models.

## Data and sample
None. It is an expository essay with no empirical section.

## Reported results
No empirical results. Methodological statements made in the text:
- Most applications use N = 2 or 3 regimes because few transitions are observed, which makes richer transition structures hard to estimate.
- The likelihood-ratio test of N against N+1 regimes does not have the usual chi-squared limit, because parameters are unidentified under the null. Alternatives named: Hansen (1992), Garcia (1998), Carrasco, Hu and Ploberger (2004), Bayesian marginal likelihood, or comparing forecast ability.
- Permanent breaks are the special case `p_22 = 1`; the author argues `p_22 < 1` is usually the more sensible assumption.

## Signal construction
Not a signal. It is the reference for the filter a bot would run. Live use: fit parameters on a trailing window, then at each bar update `xi_t` with the recursion above and act on the filtered probability, optionally pushed one step ahead by multiplying by the transition matrix. Smoothed probabilities must never enter a backtest signal because they condition on future data.

## Relevance to SOL perpetuals at minutes to hours
The recursion is cheap enough to run on every bar at any frequency. What does not transfer is the Gaussian-within-regime assumption: crypto bar returns have fat tails and strong intraday seasonality, so a naive two-state Gaussian model will mostly sort bars by volatility and flip often. The notes on jump models in this folder ([shu-2024](shu-2024-downside-risk-statistical-jump-model.md), [nystrup-2020](nystrup-2020-greedy-online-classification-market-states.md)) address the flipping problem. Number of states, window length and refit cadence all need testing on SOL data.

## Caveats
An encyclopedia entry, so there is no evidence of trading value here. The filter treats parameters as known; in practice they are estimated, and re-estimation on a rolling window changes past regime labels unless the labels are frozen as they were produced.
