---
title: "Clustering Market Regimes Using the Wasserstein Distance"
authors: "Horvath, Blanka; Issa, Zacharia; Muguruza, Aitor"
year: 2021
venue: "arXiv preprint arXiv:2110.11848 (q-fin.CP)"
url: "https://arxiv.org/pdf/2110.11848"
pdf: "sources/01-macro-regime-detection/horvath-2021-clustering-market-regimes-wasserstein.pdf"
access: "full-text"
source_type: "working-paper"
evidence_grade: "C"
topic: "01-macro-regime-detection"
asset_class: "equities"
horizon: "hours"
tags: "clustering, wasserstein-distance, k-means, unsupervised-learning, distributional-regimes, hourly-data, hidden-markov-model"
---

## Key insight
Treat each window of returns as an empirical probability distribution and cluster the distributions with k-means under the Wasserstein distance. This makes no parametric assumption about returns and compares whole distributions, not just mean and variance. On synthetic paths with known regime switches it identifies the stressed regime far better than a Gaussian HMM, which failed almost completely when the regime change involved jumps.

## Method
Slide a window of h1 returns forward in steps so that consecutive windows overlap (offset parameter h2); each window gives an empirical measure. Wasserstein k-means (WK-means): assign each measure to the nearest centroid in p-Wasserstein distance, then update each centroid as the Wasserstein barycenter of its members. For p = 1 on the real line this is cheap: sort each window's returns to get its quantiles; the barycenter is the element-wise median of members' sorted values. Benchmarks: k-means on the first p raw moments of each window, and a Gaussian HMM. Cluster quality on real data is judged with maximum mean discrepancy between and within clusters; on synthetic data with known regimes, by accuracy overall, during the regime change ("regime-on") and outside it ("regime-off").

## Data and sample
Real data: one-hourly log returns of SPY from 2005-01-03 to 2020-12-31, with (h1, h2) = (35, 28), roughly one trading week per window with adjacent windows one day apart, and k = 2. Synthetic data: geometric Brownian motion and Merton jump-diffusion paths with inserted regime changes, 50 runs each.

## Reported results
Accuracy with 95% intervals, total / regime-on / regime-off:
- Geometric Brownian motion: Wasserstein 90.60% / 87.24% / 91.72%; moment k-means 93.23% / 74.83% / 99.38%; HMM 58.16% / 41.51% / 63.72%.
- Merton jump diffusion: Wasserstein 91.28% / 86.87% / 92.76%; moment k-means 66.64% / 27.25% / 79.79%; HMM 75.05% / 0.66% / 99.87%.
- On SPY both clustering methods separate the 2008 crisis and the 2020 pandemic period; only WK-means also tags the 2010 Eurozone episode, the 2011 US downgrade and the 2015/16 China sell-off. The authors report better cluster separation than moment k-means on their discrepancy scores, and describe the HMM result as sitting between the two.
- Runtime between about 0.6 and 1.7 seconds per run across methods.

## Signal construction
Offline: collect trailing windows of bar returns (for example 35 hourly bars), sort each, run WK-means with p = 1 and k = 2 or 3, store the centroid quantile vectors. Online: at each new bar sort the latest window and assign it to the centroid with the smallest mean absolute difference between sorted values. Refit centroids periodically on past data only. Because windows overlap, a bar's label can be taken as the label of the most recent window ending at that bar.

## Relevance to SOL perpetuals at minutes to hours
The real-data experiment is on hourly bars, which is this bot's horizon, and the method is assumption-free and fast, both attractive for fat-tailed crypto returns. The HMM's 0.66% regime-on accuracy under jumps is a warning about Gaussian HMMs on crypto. Limits: the clustering has no persistence term, so labels can flicker (a jump penalty as in [shu-2024](shu-2024-downside-risk-statistical-jump-model.md) could be added); the label describes the last h1 bars and so lags by construction; and distribution shape alone ignores the order of returns within the window, so trend and chop with equal dispersion look alike.

## Caveats
The accuracy tables are on synthetic data designed by the authors, and the HMM benchmark was adapted to their windowed setup. On SPY there is no ground truth and no trading test. The whole sample is clustered at once, so the SPY regime plot is in-sample. One author is affiliated with a trading firm. Not confirmed whether a peer-reviewed version exists.
