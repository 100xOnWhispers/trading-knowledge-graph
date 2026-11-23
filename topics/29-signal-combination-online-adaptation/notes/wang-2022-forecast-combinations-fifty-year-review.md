---
title: "Forecast combinations: an over 50-year review"
authors: "Wang, Xiaoqian; Hyndman, Rob J.; Li, Feng; Kang, Yanfei"
year: 2022
venue: "arXiv preprint 2205.04216 (v2, September 2022)"
url: "https://arxiv.org/pdf/2205.04216"
pdf: "sources/29-signal-combination-online-adaptation/wang-2022-forecast-combinations-fifty-year-review.pdf"
access: "full-text"
source_type: "working-paper"
evidence_grade: "B"
topic: "29-signal-combination-online-adaptation"
asset_class: "multi"
horizon: "n/a"
tags: "forecast-combination-puzzle, stacking, meta-learning, cross-learning, equal-weights, diversity"
---

## Key insight
An up-to-date map of combination methods that extends Timmermann (2006) to learned combiners: stacking, feature-based meta-learning and cross-learning across many series. Its central message for this repository is the "forecast combination puzzle": across decades of studies and competitions, the simple average keeps matching or beating sophisticated weighting, and the accepted explanation is weight-estimation error in finite, unstable samples. Learned combiners have won only where there were very many related series to learn the weights from.

## Method
Narrative review covering simple combinations (mean, median, trimmed and winsorized means), linear combinations (variance-based, regression-based, performance-based, principal-component regression, shrinkage), nonlinear combinations, "combining by learning" (stacking with a meta-model; feature-based weighting), selection of which forecasts to pool (accuracy and diversity), the combination puzzle, and probabilistic combinations (linear and nonlinear pools, Bayesian model averaging, quantile combination).

## Data and sample
No new data. The evidence base is the forecasting literature, including the M competitions (M1 with 1,001 series, M3, M4 with 100,000 series, M5) and macroeconomic panels, mostly at monthly to yearly frequency.

## Reported results
- The review states a "unanimous conclusion that simple combination schemes are hard to beat".
- Explanations of the puzzle: Smith and Wallis (2009) show the simple average is expected to beat estimated weights when the optimal weights are close to equal; Claeskens et al. (2016) show estimated weights add bias and variance; Elliott (2011) bounds the achievable gain from optimal weights and finds it is often too small to cover estimation error. Zischke et al. (2022) dissent, attributing variability to estimation of the constituent models rather than of the weights.
- Structural change is said to hurt sophisticated schemes more than the simple average.
- Learned combiners: FFORMA (Montero-Manso et al. 2020), which uses gradient-boosted trees on 42 time-series features to set weights for nine base methods, placed second in M4; the top three M4 entries all used cross-learning. A study cited (Gastinger et al. 2021) found the winning combiner differs by data source while simple averages gave the most consistent gains.
- Series-by-series stacking "requires long time series" and uses data inefficiently.
- Diversity among pooled forecasts matters as much as individual accuracy.
- Practical guidance given: with limited history use the simple average or weights that ignore covariances; use trimmed means to guard against extreme forecasts; with many forecasts reduce dimension (principal components, clustering) before estimating weights.

## Signal construction
Not a signal. It sets the benchmark order for any combiner experiment: mean, median, trimmed mean, inverse-variance weights, shrunk regression weights, and only then a stacked or feature-conditioned combiner.

## Relevance to SOL perpetuals at minutes to hours
The condition under which learned weighting won (thousands of related series sharing a meta-model) can be approximated in crypto by pooling many perpetual contracts and many time windows, so a cross-sectional meta-learner trained on all liquid perps is more defensible than one fitted to SOL alone. The single-series warning applies directly to a SOL-only stacker. Robust operators (median, trimmed mean) deserve a place because intraday signals occasionally output extreme values.

## Caveats
The review is about forecast accuracy, not trading profit, turnover or costs. Most evidence is low-frequency business and macro data. The arXiv version was read; publication in a journal was not confirmed in this session.
