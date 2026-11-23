---
title: "Are Transformers Effective for Time Series Forecasting?"
authors: "Zeng, Ailing; Chen, Muxi; Zhang, Lei; Xu, Qiang"
year: 2022
venue: "arXiv preprint arXiv:2205.13504"
url: "https://arxiv.org/pdf/2205.13504"
pdf: "sources/12-time-encodings-cycles/zeng-2022-are-transformers-effective-time-series.pdf"
access: "full-text"
source_type: "working-paper"
evidence_grade: "B"
topic: "12-time-encodings-cycles"
asset_class: "multi"
horizon: "n/a"
tags: "transformers, positional-encoding, timestamp-embedding, linear-baseline, forecasting"
---

## Key insight
One-layer linear models beat the Transformer forecasters of the time on nine long-horizon benchmarks. On the one financial dataset, daily exchange rates, simply repeating the last value beat every Transformer. The paper's ablations show that positional and timestamp embeddings do carry information for strongly periodic data but do not rescue these models on aperiodic financial series.

## Method
Three linear baselines (Linear, DLinear with a moving-average trend and remainder split, NLinear with last-value normalization) are compared with FEDformer, Autoformer, Informer, Pyraformer and LogTrans. Two ablations matter for time encodings:
- Order sensitivity: shuffle the look-back window, or swap its two halves, before the embedding layer and measure the change in error.
- Embedding removal: drop the fixed positional embedding, the learnable timestamp embedding (hour, weekday and similar calendar fields), or both.

A naive "Repeat" forecast (last observed value) is included.

## Data and sample
Nine public multivariate benchmarks: ETTh1, ETTh2, ETTm1, ETTm2, Traffic, Electricity, Weather, ILI and Exchange-Rate (daily rates). Forecast horizons 96 to 720 steps (24 to 60 for ILI). Authors confirmed from the arXiv record.

## Reported results
- The abstract states the linear models outperform the Transformer models "in all cases, and often by a large margin".
- Repeat beats all Transformer methods on Exchange-Rate by around 45%, which the authors attribute to Transformers overfitting sudden changes and mispredicting trend.
- On Exchange-Rate, shuffling the input barely changes Transformer error, while the linear model's error rises sharply. The authors read this as Transformers preserving little temporal order on noisy financial data.
- Removing positional embeddings raises Informer's error substantially. Removing timestamp embeddings hurts Informer progressively at longer horizons and makes Autoformer deteriorate quickly; FEDformer suffers less. The embedding-ablation table as extracted appears to be for the Traffic dataset; individual cell values could not be aligned reliably and are not quoted.
- On Traffic, the learned linear weights show peaks at lags of 24 and 168 hours, so the linear model picks up daily and weekly periodicity directly from lagged values.

## Signal construction
Not a signal. Use it as a design rule for any forecasting model fed with time features:
1. Always include a last-value (zero-return) baseline and a regularized linear model.
2. Add cyclical time features to the linear model first; only then test a deep model.
3. Run the shuffle test: if out-of-sample error is unchanged when the input window is shuffled, the model is not using temporal structure.

## Relevance to SOL perpetuals at minutes to hours
Price direction in SOL is closer to Exchange-Rate than to Traffic: little periodicity in the mean and heavy noise. The paper predicts that timestamp embeddings in a Transformer will help where the target is periodic (volatility, volume, spread, funding) and will not create directional skill by themselves. The lag-24 and lag-168 result suggests that for periodic targets, seasonal lags can substitute for explicit clock features.

## Caveats
Benchmarks are long-horizon forecasts of levels, not returns, and none is intraday crypto. Later patch-based Transformers have been reported to beat these linear baselines; that follow-up work was not read here. The Exchange-Rate comparison is in mean squared error on levels, which favours the last-value forecast by construction. The copy read is the arXiv preprint; a conference version was not confirmed from it.
