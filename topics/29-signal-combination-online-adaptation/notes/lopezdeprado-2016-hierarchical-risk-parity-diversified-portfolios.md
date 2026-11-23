---
title: "Building Diversified Portfolios that Outperform Out of Sample"
authors: "Lopez de Prado, Marcos"
year: 2016
venue: "Journal of Portfolio Management 42(4), 59-69 (as cited by the secondary source)"
url: "https://en.wikipedia.org/wiki/Hierarchical_Risk_Parity"
pdf: "none"
access: "secondary"
source_type: "peer-reviewed"
evidence_grade: "C"
topic: "29-signal-combination-online-adaptation"
asset_class: "multi"
horizon: "n/a"
tags: "hierarchical-risk-parity, clustering, inverse-variance, covariance-instability, allocation, strategy-weights"
---

## Key insight
Hierarchical risk parity (HRP) allocates across correlated return streams using only the covariance matrix and without inverting it. It clusters the streams by correlation, reorders the covariance matrix so similar streams sit together, and splits risk top-down between clusters by inverse variance. It is positioned between 1/N (ignores all covariance information) and mean-variance or minimum-variance optimization (uses all of it and is unstable). The paper itself and its SSRN copy could not be opened in this session; this note is based on the Wikipedia article describing it, which carries a notice that a major contributor has a close connection to the subject.

## Method
As described by the secondary source:
1. Tree clustering. Convert correlations to distances d_ij = sqrt(0.5 (1 − ρ_ij)), compute Euclidean distances between the rows of that distance matrix, and run agglomerative clustering (single linkage in the example).
2. Quasi-diagonalization. Reorder rows and columns of the covariance matrix following the dendrogram so that large covariances lie near the diagonal.
3. Recursive bisection. Start with unit weights; split the ordered list in two; compute each half's variance using inverse-variance weights inside it (V1, V2); scale the first half by α = 1 − V1/(V1 + V2) and the second by 1 − α; recurse until single items remain.
No expected returns are used.

## Data and sample
The secondary source reports a numerical example and a Monte Carlo study on synthetic data: 10 Gaussian series, 520 observations, a 260-observation look-back, rebalancing every 22 observations, 10,000 runs, with random shocks and a correlation structure added.

## Reported results
As reported by the secondary source, not verified against the paper:
- Numerical example: the top five holdings take 92.66% of weight under the minimum-variance critical-line solution versus 62.57% under HRP; the critical-line solution gives zero weight to three assets.
- Monte Carlo out-of-sample variance: critical-line 0.1157, inverse-variance 0.0928, HRP 0.0671; i.e. the critical-line variance is 72.47% above HRP's and inverse-variance is 38.24% above.
No comparison with 1/N is reported in what was read, and the simulation is on generated data.

## Signal construction
An allocator across strategies or signals. Inputs: a matrix of recent per-strategy net returns (or of signal-implied position returns) and its covariance. Output: non-negative weights summing to one. Update at a slow cadence (daily or weekly) with a look-back long enough for stable correlations. Expected-return views, if any, must be layered on separately, for example by scaling HRP weights by a shrunk Sharpe estimate.

## Relevance to SOL perpetuals at minutes to hours
A small signal set for one instrument clusters naturally (trend, mean-reversion, order-flow, funding and positioning, cross-asset lead-lag). HRP stops a family with many near-duplicate variants from dominating the book, which equal weighting across variants would allow, and it needs only second moments, which are estimable from weeks of intraday data. It should be tested against two simpler rules that capture most of the idea: equal weight across families then equal weight within, and plain inverse-variance.

## Caveats
Secondary access only; numbers come from an encyclopedia article flagged for a possible conflict of interest and largely sourced to the author and co-authors. Evidence shown is synthetic and concerns variance, not Sharpe after costs. Single-linkage trees are known to be sensitive to small changes in correlations, so weights can jump between rebalances; that turnover cost is not addressed in what was read. Long-only weights cannot express that a signal should be shorted or switched off.
