---
title: "Lead-lag detection and network clustering for multivariate time series with an application to the US equity market"
authors: "Bennett, Stefanos; Cucuringu, Mihai; Reinert, Gesine"
year: 2022
venue: "Machine Learning 111(12), 4497-4538 (arXiv:2201.08283 preprint read)"
url: "https://arxiv.org/abs/2201.08283"
pdf: "sources/21-cross-asset-lead-lag/bennett-2022-lead-lag-detection-network-clustering.pdf"
access: "full-text"
source_type: "peer-reviewed"
evidence_grade: "B"
topic: "21-cross-asset-lead-lag"
asset_class: "equities"
horizon: "daily"
tags: "lead-lag, directed-network, spectral-clustering, hermitian, unsupervised-learning, distance-correlation, stability"
---

## Key insight
Pairwise lead-lag scores across a large universe form a directed, skew-symmetric network, and directed spectral clustering on that network finds groups of assets that lead other groups. Averaging within clusters removes noise, so cluster-to-cluster prediction works where pair-to-pair prediction is too weak. The lead-lag structure found in US equities is statistically significant but only weakly persistent from year to year, and the resulting signal's performance decays after 2012.

## Method
Pipeline with two interchangeable components.

1. Pairwise lead-lag metric S_ij, from which a skew-symmetric matrix A - A^T is built. Options tested:
   - ccf-lag1: ccf_ij(1) - ccf_ij(-1).
   - ccf-auc: signed, normalized area under the cross-correlation function over lags -L to L, comparing the mass at positive lags with the mass at negative lags.
   - Correlation choices inside the ccf: Pearson, Kendall, distance correlation, mutual information.
   - Signature method: the difference of the cross-terms of the level-2 path signature of the two log-price paths (Levy area).
2. Directed clustering: Hermitian random-walk clustering on the complex matrix i(A - A^T) (Cucuringu et al. 2020), compared with naive symmetrization, bibliometric symmetrization and DI-SIM co-clustering.

A "meta-flow" matrix records net flow between clusters; a permutation test on the leading eigenvalues of the Hermitian matrix tests for any lead-lag cluster structure. Synthetic experiments use a lagged latent-factor model with linear and nonlinear dependence. Chosen configuration for real data: ccf-auc with distance correlation, lags -5 to 5, Hermitian RW clustering.

Trading test: every 2 months, using a 1-year look-back, recompute clusters and flow graph; for each ordered cluster pair fit an OLS of the lagging cluster's mean daily return on an exponentially weighted average (alpha = 0.4, 92% of weight on lags 1 to 5) of the leading cluster's mean returns; keep only pairs above the 90th percentile of flow; signal is the sign of the summed forecasts; positions scaled to 10% annual volatility with a 21-day estimator.

## Data and sample
CRSP daily closes for NYSE equities, 4 January 2000 to 31 December 2019; 434 stocks after liquidity and missing-data filters.

## Reported results
- On synthetic data, ccf-auc and signature metrics with Hermitian RW or DI-SIM clustering recover clusters best; with nonlinear dependence ccf-auc with distance correlation or mutual information is best and ccf-lag1 and signatures do poorly.
- US equities: the permutation test rejects "no lead-lag structure"; data-driven clusters overlap only partly with SIC industries.
- Adjusted Rand Index between yearly clusterings is low and falls over time; the association between leadership and market cap or volume is "not stable throughout time".
- Out-of-sample signal: annualized Sharpe 0.62 (one-sided p < 0.004) versus 0.40 for the S&P 500, correlation 0.04 with the market, mean daily return 2.4 bps; a Monte Carlo test against random cluster labels gives probability 1/201. Performance decays after 2012.
- Transaction costs are not included.

## Signal construction
For a crypto universe (say the 50 most liquid perps plus equity and FX futures): on a rolling window of 5-minute or hourly returns compute S_ij by ccf-auc over a small number of lags, cluster with Hermitian RW, identify which cluster SOL sits in and which clusters have the largest net flow into it, then use the EWMA of the leading clusters' mean returns as a feature for SOL's next-bar return. Recompute clusters on a schedule much shorter than the paper's 2 months, because crypto structure moves faster.

## Relevance to SOL perpetuals at minutes to hours
This is the cleanest template for a cross-sectional lead-lag feature that does not assume in advance that BTC is the leader. It lets the data say whether SOL is led by BTC, by an ETH/L1 cluster, by meme coins, or by equity futures in US hours. The weak persistence result is the central warning: any such map must be re-estimated often and tested walk-forward.

## Caveats
Daily US equities, no costs, modest Sharpe, decay after 2012. Many pipeline choices (metric, lags, number of clusters, thresholds) invite data snooping. No intraday or crypto test in the paper.
