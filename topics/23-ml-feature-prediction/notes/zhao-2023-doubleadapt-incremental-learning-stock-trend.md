---
title: "DoubleAdapt: A Meta-learning Approach to Incremental Learning for Stock Trend Forecasting"
authors: "Zhao, Lifan; Kong, Shuming; Shen, Yanyan"
year: 2023
venue: "KDD '23, ACM SIGKDD Conference on Knowledge Discovery and Data Mining, August 2023 (arXiv:2306.09862v3 read)"
url: "https://arxiv.org/pdf/2306.09862"
pdf: "sources/23-ml-feature-prediction/zhao-2023-doubleadapt-incremental-learning-stock-trend.pdf"
access: "full-text"
source_type: "peer-reviewed"
evidence_grade: "B"
topic: "23-ml-feature-prediction"
asset_class: "equities"
horizon: "daily"
tags: "online-learning, incremental-learning, concept-drift, meta-learning, rolling-retraining, non-stationarity, qlib"
---

## Key insight
Under distribution shift there are two standard ways to keep a model current: retrain from scratch on all data at intervals (rolling retraining), or fine-tune on only the newest block (incremental learning). Plain incremental learning is fast but often worse on rank correlation; rolling retraining is a strong baseline but slow. DoubleAdapt adds two small learned adapters, one that transforms features and labels toward a locally stationary distribution and one that provides good initial weights, and reports better rank correlation and backtest return than either, at a small fraction of retraining time.

## Method
Time is cut into tasks of r trading days (20 in the experiments). For each task the model is updated on the newest block and predicts the next block. A data adapter applies learned multi-head transforms to the features and labels of the incoming data and to the features of the test data, so that the two look more alike (I did not re-derive the exact transform and its inverse from the equations). A model adapter holds meta-learned initial parameters from which a one-step gradient update produces task-specific weights. Both adapters are trained by first-order model-agnostic meta-learning on the test error of each past task, and keep updating online once true labels arrive. Baselines are rolling retraining, DDG-DA (reweights history to match a predicted future distribution), naive incremental learning, and two generic continual-learning methods. Base forecasters are Transformer, LSTM, attention LSTM and GRU. Each experiment is run 10 times.

## Data and sample
Chinese A-shares, CSI 300 and CSI 500 universes, daily data via Qlib's Alpha360 feature set (60 days of six price and volume fields per stock). Training 2008 to 2014, validation 2015 to 2016, test January 2017 to July 2020.

## Reported results
With a GRU on CSI 300 (IC, annualised excess return, information ratio):
- Rolling retraining: 0.0629, 9.33%, 1.14.
- Naive incremental learning: 0.0633, 11.66%, 1.32.
- DoubleAdapt: 0.0687, 12.96%, 1.51.
With a GRU on CSI 500: rolling retraining 0.0669, 12.00%, 1.86; naive incremental 0.0637, 16.26%, 2.34; DoubleAdapt 0.0686, 17.48%, 2.46.
- Naive incremental learning beat rolling retraining on portfolio return in seven of the eight model and universe combinations (the exception is the Transformer on CSI 300), even where its rank-correlation stability (ICIR) was lower.
- Online time cost with a GRU on CSI 300: rolling retraining 6,064 units against 58 for incremental learning and 61 for DoubleAdapt (units as tabulated in the paper).
- An ablation separates gradual from abrupt shifts and finds the data adapter matters most under gradual shift, which the authors call the main issue in stock data.

## Signal construction
Not a signal. It is an update policy for whatever model produces the signal: every r bars, take one or a few gradient steps on the newest labelled block starting from the previous weights, instead of retraining from scratch; optionally learn an affine re-normalisation of features and labels per block. For tree models the analogue is warm-started boosting or periodic refits on a rolling window with recency weights.

## Relevance to SOL perpetuals at minutes to hours
Non-stationarity is the central problem for a crypto intraday model, and this is the clearest controlled comparison of update schemes I found. The finding that frequent cheap updates on recent data matched or beat full retraining in backtest return supports running an online-updated model in the bot, and intraday crypto offers far more blocks per month than daily equities, so adaptation can be evaluated quickly. Whether the gain holds for boosted trees, for a single instrument, and across crypto regime breaks (for example October 2025) is untested.

## Caveats
Daily Chinese equities, cross-sectional ranking, long-only top-k backtests under Qlib defaults whose cost assumptions I did not verify in the text read. Improvements in IC are in the third decimal place. Neural base models only. The paper warns that the meta-learners themselves can forget and suggests combining with periodic retraining. No crypto evidence.
