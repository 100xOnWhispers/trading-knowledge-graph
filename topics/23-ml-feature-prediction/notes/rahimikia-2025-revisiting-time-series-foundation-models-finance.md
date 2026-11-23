---
title: "Re(Visiting) Time Series Foundation Models in Finance"
authors: "Rahimikia, Eghbal; Ni, Hao; Wang, Weiguan"
year: 2025
venue: "arXiv:2511.18578v2 (first version November 2025, this version November 2026)"
url: "https://arxiv.org/pdf/2511.18578"
pdf: "sources/23-ml-feature-prediction/rahimikia-2025-revisiting-time-series-foundation-models-finance.pdf"
access: "full-text"
source_type: "working-paper"
evidence_grade: "B"
topic: "23-ml-feature-prediction"
asset_class: "equities"
horizon: "daily"
tags: "foundation-model, chronos, timesfm, catboost, zero-shot, fine-tuning, pretraining-from-scratch, look-ahead-bias, transaction-costs"
---

## Key insight
The most thorough test so far of time-series foundation models for return prediction. Off-the-shelf Chronos and TimesFM forecast daily stock returns poorly, and fine-tuning the public checkpoints does not fix it. Pretraining the same architectures from scratch on financial returns narrows most of the gap to a strong gradient-boosting benchmark, and with enough finance-native data one configuration edges past it. CatBoost on lagged returns is a very hard baseline to beat, and all of the daily-rebalanced strategies are fragile to costs.

## Method
Univariate forecasting of next-day excess return from a window of past daily returns (5, 21, 252 or 512 days). Three regimes: zero-shot use of public checkpoints, fine-tuning those checkpoints, and pretraining from scratch each year on financial data dated up to the training cutoff, which removes look-ahead inherited from public checkpoints. Benchmarks are linear models (OLS, lasso, ridge and elastic net variants, PCR), tree ensembles (XGBoost, CatBoost, LightGBM) and small and large neural networks. Metrics: out-of-sample R2, directional accuracy, and equal-weighted long-short decile portfolios rebalanced daily, reported gross and under position-based cost scenarios of 20 and 40 basis points per day. Further experiments enlarge the pretraining set with global returns, factor series and synthetic series.

## Data and sample
Daily excess returns for stocks in 94 countries and regions over 34 years; the headline comparison is on US stocks, with checks in seven non-US markets.

## Reported results
- CatBoost benchmark: out-of-sample R2 between -0.25% (5-day window) and -0.03% (252 and 512 days), directional accuracy about 51%, gross long-short annualised return 42.35% to 46.98% and Sharpe 5.70 to 6.72.
- Zero-shot Chronos (Large): R2 of -46.86%, -23.84%, -2.49% and -1.37% across the four windows; best gross Sharpe 2.92 at 512 days.
- Fine-tuned Chronos (Large): R2 of -17.02%, -2.30%, -1.85% and -1.89%; best gross Sharpe only 0.07.
- Chronos pretrained from scratch on financial data: accuracy 51.36% at 252 and 512 days; gross Sharpe 4.89 and 5.42.
- TimesFM (20M) pretrained on global returns plus factor series reaches gross Sharpe 7.62 at 512 days, above the US CatBoost figure of 6.39. Adding synthetic series gives comparable gains.
- Under costs, net Sharpe ratios "fall sharply"; some specifications stay positive at 20 bps, all reported specifications are negative at 40 bps.
- A negative R2 coexists with a high long-short Sharpe: ranking quality, not point accuracy, drives the portfolio.

## Signal construction
Not a signal. It defines the benchmark ladder for any pretrained forecaster: compare against boosted trees on the same lagged inputs, report zero-shot, fine-tuned and from-scratch variants separately, and retrain from scratch with a rolling cutoff to rule out contamination.

## Relevance to SOL perpetuals at minutes to hours
The asset class and horizon differ, but the conclusions are about method and transfer cleanly as priors: do not expect a general pretrained time-series model to beat CatBoost or LightGBM on lagged-return features; if a sequence model is wanted, train it on crypto bars from scratch with as much cross-asset data as possible; long input windows helped; and judge by ranking or sign metrics and net profit, not R2. The cost result is a reminder that a daily-rebalanced signal with 51% accuracy does not survive 40 bps, which frames the much tighter budget of an intraday bot.

## Caveats
Preprint. Univariate inputs only, so nothing is learned about volume, funding or order-flow features. The gross Sharpe ratios above 5 come from equal-weighted daily long-short portfolios across thousands of stocks and largely reflect short-term reversal in small stocks; the authors stress these are not implementable strategies. The cost scenarios are position-based, not turnover-based. No crypto data.
