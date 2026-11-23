---
title: "Financial Time Series Analysis and Forecasting with HHT Feature Generation and Machine Learning"
authors: "Leung, Tim; Zhao, Theodore"
year: 2021
venue: "arXiv preprint arXiv:2105.10871"
url: "https://arxiv.org/pdf/2105.10871"
pdf: "sources/12-time-encodings-cycles/leung-2021-hht-feature-generation-machine-learning.pdf"
access: "full-text"
source_type: "working-paper"
evidence_grade: "B"
topic: "12-time-encodings-cycles"
asset_class: "multi"
horizon: "daily"
tags: "empirical-mode-decomposition, hilbert-huang-transform, look-ahead-bias, end-effect, machine-learning"
---

## Key insight
Empirical mode decomposition and the Hilbert transform use data on both sides of each point, so features built by decomposing a whole series and then splitting into train and test sets leak the future. The authors say most earlier EMD forecasting studies have this flaw. They propose a rolling, strictly backward-looking procedure with an explicit correction for the end effect, and report that Hilbert-Huang features still reduce one-step forecast error, by a modest margin.

## Method
Complementary ensemble EMD (CEEMD) decomposes a series into intrinsic mode functions (IMFs) `c_j(t)` plus a residual. The Hilbert transform of each IMF gives an imaginary part `c_hat_j(t)`, from which instantaneous amplitude `a_j = sqrt(c_j^2 + c_hat_j^2)` and instantaneous frequency (the time derivative of phase) follow. Feature sets tested: IMFs only; complex IMFs `(c, c_hat)`; and the full set `(c, c_hat, a, f)`. Learners: regression tree ensemble, support vector machine, LSTM. Target: next-step change in the series.

Two protocols:
1. Standard: decompose once, then split train and test. The authors state this leaks future information.
2. Extrapolating: for each t, run CEEMD and the Hilbert transform on the trailing window `[t-T, t-1]` only, and add an "end effect factor" (the relative position of a point within the decomposition window) as a predictor, because decomposition error rises towards the window ends.

## Data and sample
Daily S&P 500 (log price), VIX, the GLD gold ETF (log price) and the 10-year Treasury yield. Standard protocol: training 1 April 2010 to 31 March 2018, test 1 April 2018 to 31 March 2020. Rolling extrapolation shown for 1 January to 29 October 2020.

## Reported results
- Under the leaky standard protocol, the largest feature set gives "much reduced errors"; complex IMFs do about as well as the full set; high-frequency IMFs matter more than low-frequency ones.
- Under the extrapolating protocol, tree and SVM models perform poorly because the feature distribution shifts, and only LSTM results are reported.
- With end-effect correction, HHT feature sets lower out-of-sample mean squared error relative to both the plain series and the naive last-value forecast. In the extracted Table 6, one series shows a naive benchmark of 1.5698 against roughly 1.33 to 1.39 with HHT features (units of 1e-4); the assignment of rows to assets could not be confirmed from the text extraction.
- No directional accuracy, trading rule or cost analysis is reported.

## Signal construction
Inputs: a trailing window of T bars. Each bar:
1. Run CEEMD on the window only.
2. Hilbert-transform each IMF; take the last available values of `c_j`, `c_hat_j`, and optionally amplitude and frequency, for the first four or five IMFs.
3. Append the end-effect factor.
4. Feed to a sequence model retrained on windows processed the same way.
CEEMD is costly (an ensemble of noise-perturbed siftings per window), so update at 5-minute or slower cadence.

## Relevance to SOL perpetuals at minutes to hours
The protocol transfers and is the minimum standard for any decomposition feature in this repository: decompose only the trailing window, at every step, in both training and testing. The reported gains are small, on daily index data, in mean squared error. Whether they survive at intraday crypto frequencies, in directional terms and after fees, is untested.

## Caveats
Preprint. Four daily series, one test period that includes the 2020 crash. Improvement is measured in MSE, not in profit. Values at the window's right edge are where EMD is least accurate, and those are the only values a live system can use. Noise-assisted EMD is stochastic, so features are not exactly reproducible without fixing seeds.
