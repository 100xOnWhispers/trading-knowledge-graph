---
title: "Greedy Online Classification of Persistent Market States Using Realized Intraday Volatility Features"
authors: "Nystrup, Peter; Kolm, Petter N.; Lindström, Erik"
year: 2020
venue: "Journal of Financial Data Science 2(3), 25-39"
url: "https://orbit.dtu.dk/en/publications/greedy-online-classification-of-persistent-market-states-using-re/"
pdf: "none"
access: "abstract-only"
source_type: "peer-reviewed"
evidence_grade: "C"
topic: "01-macro-regime-detection"
asset_class: "equities"
horizon: "daily"
tags: "statistical-jump-model, online-classification, realized-volatility, intraday-features, persistence, hidden-markov-model"
---

## Key insight
Per the abstract: a classifier that assigns each new observation to a hidden market state as it arrives, without re-processing past data, by clustering temporal features and charging a fixed cost for every switch of state. The switching cost can be set to give whatever persistence the user wants. Adding features built from intraday data improves classification accuracy. It is an explicitly online formulation of the jump-model idea that later strategy papers cite.

## Method
Only the abstract was read. It describes a greedy online classifier that "contemporaneously determines which hidden state a new observation belongs to", built on clustering of temporal features with a fixed-cost regularisation term penalising jumps between states. Evaluation is by a simulation study of returns, comparing against a correctly specified maximum-likelihood estimator (the standard HMM fit), followed by an application to the S&P 500. The exact objective, feature list and penalty-selection rule were not seen; the closely related formulation in [shu-2024](shu-2024-downside-risk-statistical-jump-model.md), which cites this line of work, is the best available description in this folder.

## Data and sample
Simulated return series and the S&P 500 index. Sample period and frequency of the intraday inputs: not confirmed.

## Reported results
From the abstract only, with no numbers available:
- In simulations the classifier is often more accurate than the correctly specified maximum-likelihood estimator.
- It is more robust to model misspecification.
- It yields state sequences that are significantly more persistent, both in and out of sample.
- Accuracy improves further when intraday-based features are included.

## Signal construction
Sketch, to be confirmed against the full text: maintain K centroids in feature space; for each new bar compute features (including realised volatility built from finer-grained data), and assign the bar to the state that minimises distance to centroid plus a fixed penalty if the state differs from the previous one. "Greedy" means the decision for bar t is made once and is not revisited when later data arrive, which is what a live bot needs.

## Relevance to SOL perpetuals at minutes to hours
Directly relevant in design: it is online, it controls flicker with one parameter, and it uses higher-frequency data to sharpen a lower-frequency state estimate. The crypto analogue is to classify the hourly state using realised variance, range and jump measures computed from one-minute or tick data on the venues where SOL price discovery happens. Everything quantitative would need to be measured afresh.

## Caveats
Abstract only. The author manuscript is listed as open on DTU Orbit, but the file was blocked by an automated-access challenge during this session, so no PDF was saved and none of the paper's numbers could be checked. The empirical application is a single equity index. The grade is held at C because nothing could be verified beyond the abstract; the venue and the stated out-of-sample evaluation would otherwise support B.
