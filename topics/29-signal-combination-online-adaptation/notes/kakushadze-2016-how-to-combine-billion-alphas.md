---
title: "How to Combine a Billion Alphas"
authors: "Kakushadze, Zura; Yu, Willie"
year: 2016
venue: "arXiv preprint 1603.05937 (v2, June 2016)"
url: "https://arxiv.org/pdf/1603.05937"
pdf: "sources/29-signal-combination-online-adaptation/kakushadze-2016-how-to-combine-billion-alphas.pdf"
access: "full-text"
source_type: "practitioner"
evidence_grade: "C"
topic: "29-signal-combination-online-adaptation"
asset_class: "equities"
horizon: "daily"
tags: "alpha-combination, sample-covariance, factor-model, regression-weights, inverse-variance, shrinkage"
---

## Key insight
When the number of signals N far exceeds the number of return observations M, Sharpe-maximizing signal weights cannot use the sample covariance matrix because it is singular. The authors show that with any factor-model or shrinkage repair of that matrix, and absent a clean clustering of signals, the optimization collapses to a weighted cross-sectional regression: weights are the residuals of regressing volatility-normalized expected returns on the normalized, demeaned history of signal returns, divided by volatility. Correlations enter only through that regression; nothing needs to be inverted.

## Method
Start from w = η C⁻¹ E with Σ|w_i| = 1, where E is the vector of expected signal returns and C their covariance. Replace C by a factor model Γ = diag(ξ²) + Ω Φ Ω'. When N is large and loadings are not clustered, w_i ≈ η ε_i / ξ_i², where ε are residuals of a regression of E on the loadings with weights 1/ξ². Shrinkage (Ledoit-Wolf) is shown to be a special case of a factor model, so the same reduction applies. Prescription:
1. Take realized signal returns R_is for s = 1..M+1; compute only variances σ_i².
2. Normalize R̃_is = R_is/σ_i; demean cross-sectionally and serially to get Y_is; keep M−1 columns.
3. Normalize expected returns Ẽ_i = E_i/σ_i.
4. Regress Ẽ on Y with unit weights and no intercept; take residuals ε̃.
5. Set w_i = η ε̃_i/σ_i and normalize.
Cost is O(M²N), linear in N, with no iterations. Removing the cross-sectional mean factors out the "market mode" common to all signals. R source code is given in an appendix.

## Data and sample
None. This is a derivation with code. The motivating setting is very large libraries of daily equity alphas with roughly one year of history (M ≈ 250).

## Reported results
No backtest. Stated findings are analytical or asserted from experience:
- Style factors for alphas (log volatility, log turnover, momentum) add little: they are described as poor predictors of pairwise correlations, and including momentum as a factor partly removes the alpha itself.
- Allocating to alphas is called inherently a momentum bet, because expected return is an average of realized return.
- The number of usable risk factors is capped by the number of observations unless position-level data on the underlying instruments is used to build more.
- Trading costs and position bounds are explicitly left out of the main result.

## Signal construction
A combiner, not a signal. For a bot with tens of signals and thousands of bars the binding condition (N much larger than M) does not hold, so the full prescription is unnecessary; the useful pieces are: (a) scale each signal's expected return and history by its own volatility; (b) remove the average signal return each bar before measuring co-movement, so that the common "all signals win or lose together" mode does not drive weights; (c) take weights from regression residuals so that a signal is paid only for the part of its expected return not explained by the others; (d) the zero-information fallback is inverse-variance weights.

## Relevance to SOL perpetuals at minutes to hours
Relevant where a search process (topics 23 and 25) emits hundreds of candidate features with short live history, which recreates the N greater than M problem at small scale. It is also a clear statement of why correlated signals should not each receive a full weight. Expected returns E are assumed known; in practice they are the noisiest input, and the paper offers no protection against that.

## Caveats
No empirical evidence, no equal-weight comparison, no costs. Authors are commercial practitioners. The "no clustering" assumption is questionable for a small hand-built signal set that clearly groups into momentum, order-flow and funding families; with real clusters, grouping first (see the hierarchical risk parity note) is the alternative.
