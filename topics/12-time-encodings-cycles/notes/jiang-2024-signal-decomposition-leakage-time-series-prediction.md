---
title: "Revisiting the Efficacy of Signal Decomposition in AI-based Time Series Prediction"
authors: "Jiang, Kexin; Wu, Chuhan; Chen, Yaoran"
year: 2024
venue: "arXiv preprint arXiv:2405.06986"
url: "https://arxiv.org/pdf/2405.06986"
pdf: "sources/12-time-encodings-cycles/jiang-2024-signal-decomposition-leakage-time-series-prediction.pdf"
access: "full-text"
source_type: "working-paper"
evidence_grade: "B"
topic: "12-time-encodings-cycles"
asset_class: "multi"
horizon: "n/a"
tags: "data-leakage, empirical-mode-decomposition, wavelets, singular-spectrum-analysis, look-ahead-bias"
---

## Key insight
The large accuracy gains reported for "decompose, then predict" models (EMD, discrete wavelets or singular spectrum analysis feeding an LSTM or Transformer) come mostly from leaking future data. When the decomposition is computed strictly from past observations, the decomposed components give no improvement over the plain model and often make it slightly worse. This is the most direct evidence that cycle-decomposition features are much weaker than the published literature suggests.

## Method
Controlled comparison of two data pipelines that differ in one respect:
1. Leaked: decompose the entire series (train and test together), then slice windows.
2. Non-leaked: for each prediction step, decompose only the observations before the prediction time.

Decomposed components are concatenated with the raw series and fed to the model. Decompositions: empirical mode decomposition (EMD), discrete wavelet transform (DWT), singular spectrum analysis (SSA). Models: LSTM as the main case; MLP and Transformer for robustness, with EMD. Baselines: naive persistence and the same model on the raw series only. Five repeated runs per configuration, two-sided t-tests.

## Data and sample
Six physical time series: significant wave height, wind speed, humidity, solar power, air pressure and temperature. Details are in the paper's supplementary methods, which were not read. No financial data.

## Reported results
- On all six datasets, a plain LSTM beats persistence.
- Adding leaked components cuts error "at an abnormal scale"; SSA is worst, with reductions above 90% (91.4% on significant wave height).
- With causal decomposition, "for all methods on all datasets, a slight performance degradation is observed compared with the vanilla LSTM".
- Leaked versus non-leaked differences are significant at p < 0.001.
- The effect reproduces across MLP, LSTM and Transformer; even an MLP with no notion of time reaches very low error when leakage is present.
- Qualitatively, causal-decomposition models are less responsive to sharp moves; the authors suggest past frequency components push the model to continue old patterns.

## Signal construction
Not a signal. It defines an audit that every decomposition-based feature must pass before entering the feature store:
1. Compute the feature twice at each timestamp: once using data up to that timestamp only, once using the full sample.
2. If the two differ at historical timestamps, the full-sample version is non-causal and must not be used in a backtest.
3. Report model performance with the causal version only, alongside the same model without the feature.
A quick diagnostic is to truncate the series at a random point, recompute, and check that earlier feature values are unchanged.

## Relevance to SOL perpetuals at minutes to hours
Fully relevant as a methodological constraint. Crypto forecasting papers that report large gains from wavelet-LSTM, EMD-LSTM or VMD hybrids should be assumed leaky unless they state that decomposition was done on a rolling, past-only basis. The same audit applies to any zero-phase filter, centred moving average, full-sample normalization or full-sample seasonal fit, including the Fourier seasonal factors discussed elsewhere in this topic.

## Caveats
Preprint. The series are physical, smoother and more predictable than returns, so the result that causal decomposition adds nothing is not proven for finance by this paper; it is the leakage mechanism that generalizes. Only three decomposition methods and one way of using components (concatenation) were tested. Variational mode decomposition and learned decompositions were not covered.
