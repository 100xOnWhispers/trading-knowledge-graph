---
title: "Learning from Time-Changing Data with Adaptive Windowing"
authors: "Bifet, Albert; Gavalda, Ricard"
year: 2007
venue: "SIAM International Conference on Data Mining 2007 (technical report version dated 17 October 2006 read)"
url: "https://www.cs.upc.edu/~gavalda/papers/adwin06.pdf"
pdf: "sources/29-signal-combination-online-adaptation/bifet-2007-adwin-adaptive-windowing.pdf"
access: "full-text"
source_type: "peer-reviewed"
evidence_grade: "B"
topic: "29-signal-combination-online-adaptation"
asset_class: "multi"
horizon: "n/a"
tags: "adwin, adaptive-window, change-detection, drift, hoeffding-bound, estimation-window"
---

## Key insight
ADWIN removes the need to choose a window length or decay constant in advance. It keeps the longest recent window that is statistically consistent with a constant mean, and drops the oldest part whenever two sub-windows have averages that differ by more than a threshold derived from a concentration bound. It comes with explicit guarantees on false alarms and missed changes, and a compressed version (ADWIN2) that needs only logarithmic memory and time per observation.

## Method
Input: a confidence δ in (0, 1) and a stream x_t in [0, 1]. Maintain window W of length n. For every split of W into an older part W0 (length n0) and a newer part W1 (length n1), let m = 1/(1/n0 + 1/n1), δ' = δ/n, and ε_cut = sqrt((1/(2m)) ln(4/δ')). If |mean(W0) − mean(W1)| ≥ ε_cut, drop the oldest elements and repeat. Output the mean of W as the current estimate.
Theorem 3.1: (1) if the mean has been constant within W, the probability that the window shrinks at a given step is at most δ; (2) if some split has true means differing by more than 2 ε_cut, then with probability 1 − δ the window shrinks to W1 or shorter.
ADWIN2 stores the window as exponentially growing buckets, checks only O(log W) cut points, and uses O(M log(W/M)) memory with O(log W) amortized update time (M is a bucket parameter; M = 5 in the experiments). A less conservative threshold based on a normal approximation is offered for practice. The authors also combine ADWIN2 with a Naive Bayes predictor and a k-means clusterer as examples of plugging it into learners.

## Data and sample
Synthetic streams: 100,000 stationary Bernoulli bits for the false-alarm test; 10^6-point streams with triangular, square and staircase mean profiles for the estimation test, compared against fixed windows of several sizes and fixed windows flushed on detected change. Real-data experiments with the learners appear later in the paper and were not read in detail.

## Reported results
- False-positive rates on stationary Bernoulli data are below δ in every case and far below it for small means: for example 0.0012 at μ = 0.5 with δ = 0.05, 0.0128 at μ = 0.5 with δ = 0.3, and 0.0000 at μ = 0.01 for all δ tested.
- As an estimator under changing means, ADWIN2 is usually slightly worse than the best fixed window for that change period, often better, and better than any single fixed window when the change period is much larger or much smaller than that window.

## Signal construction
Two uses. (1) Monitor: feed each signal's bounded performance stream (hit indicator, or clipped normalized return mapped to [0, 1]); a window shrink is a drift alarm and the new window length says how much history is still relevant. (2) Estimator: use the ADWIN window instead of a fixed look-back when estimating a signal's recent mean return, hit rate or information coefficient for weighting. Parameter: δ only.

## Relevance to SOL perpetuals at minutes to hours
Addresses the estimation-window question that the forecast-combination literature leaves to judgment (the window-selection paper by Pesaran and Timmermann could not be accessed for this topic). The data-driven window is attractive for signals whose useful history differs: a funding-rate signal may be stable for months while an order-flow signal resets after a fee or tick-size change. The detectable change is the weak point: ε_cut shrinks only as 1/sqrt(m). By the formula above (our arithmetic, not the paper's), with δ = 0.05 and 2,000 observations on each side ε_cut is about 0.08 of the range, and reaching 0.03 takes roughly 16,000 observations per side, which at hourly bars is more than a year. A hit rate falling from 53% to 50% is therefore invisible to the rigorous test on any useful timescale; coarser alarms (edge gone entirely, or sign flipped) are what it can catch.

## Caveats
Guarantees assume independent bounded observations; trading outcomes are serially dependent and heavy-tailed, so real false-alarm rates will exceed δ unless inputs are pre-whitened or aggregated into blocks. It detects changes in the mean only. No financial evidence. The version read is the 2006 report underlying the conference paper.
