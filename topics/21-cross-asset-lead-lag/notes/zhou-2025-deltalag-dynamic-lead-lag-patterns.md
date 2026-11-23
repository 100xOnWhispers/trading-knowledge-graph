---
title: "DeltaLag: Learning Dynamic Lead-Lag Patterns in Financial Markets"
authors: "Zhou, Wanyun; Wang, Saizhuo; Cucuringu, Mihai; Zhang, Zihao; Li, Xiang; Guo, Jian; Zhang, Chao; Chu, Xiaowen"
year: 2025
venue: "6th ACM International Conference on AI in Finance (ICAIF 2025); arXiv:2511.00390"
url: "https://arxiv.org/abs/2511.00390"
pdf: "sources/21-cross-asset-lead-lag/zhou-2025-deltalag-dynamic-lead-lag-patterns.pdf"
access: "full-text"
source_type: "peer-reviewed"
evidence_grade: "B"
topic: "21-cross-asset-lead-lag"
asset_class: "equities"
horizon: "daily"
tags: "lead-lag, deep-learning, cross-attention, dynamic-graph, machine-learning, ranking-loss, stability"
---

## Key insight
Lead-lag pairs and their lag lengths can be learned end to end by a neural network instead of being precomputed from historical correlations. The learned, time-varying leader set beats both fixed-lag models and precomputed statistical lead-lag graphs (including the Bennett-Cucuringu-Reinert meta-flow graph) on US equities. The authors read the gap as evidence that lead-lag relations seen in history "do not reliably persist into the future".

## Method
For each target stock u on each day, a sparsified cross-attention layer scores every other stock at every lag from 1 to l_max (candidate "keys" are other stocks' embedded feature histories; the target's own history is excluded). The top-k (stock, lag) pairs are kept (k = 2). The raw price-volume features of those leaders on the lag-aligned day (price ratios of open, high and low to close, daily return, log volume, turnover) feed a small predictor of the target's next return. Training uses a ranking-based loss (a smooth monotonic logistic loss on pairwise orderings) instead of MSE, to match the long-short use case. Baselines: Lag1Net (fixed lag 1, learned leaders), SelfLagNet and SelfLag1 (own history only), LagAll CorrGraph and Lag1 CorrGraph (leaders chosen offline by Pearson correlation at lags 1 to 10 or lag 1), Meta-flow Graph (Bennett et al.), and a set of sequence and graph deep-learning models (LSTM, PatchTST, TimesNet, RGCN, THGNN and others).

## Data and sample
US equities, daily, 2010 to 2023: train 2010-2018, validation 2019-2021, test 2022-2023. Test universes: S&P 500, NASDAQ (713 stocks above 2B market cap), NYSE (1,140 stocks). Portfolio: long top 10% and short bottom 10% of predicted returns.

## Reported results
- S&P 500 test set (Table 1), IC / annualized return / Sharpe: DeltaLag 0.0261 / 0.247 / 2.12; Lag1Net 0.0221 / 0.166 / 1.30; SelfLagNet 0.0221 / 0.189 / 1.56; SelfLag1 0.0233 / 0.172 / 1.45; LagAll CorrGraph 0.0054 / 0.119 / 0.77; Lag1 CorrGraph 0.0059 / 0.092 / 0.42; Meta-flow Graph return 0.055, Sharpe 0.28. DeltaLag's Sharpe is 2.91 on NASDAQ and 2.57 on NYSE.
- Average across the three test sets for k = 2: annualized return 0.270, Sharpe 2.53; nearly identical for k = 5 and 10.
- About 10 bps per day on average, which the authors compare with "typical transaction costs of 2-5 bpts".
- Learned lags are spread almost uniformly over 1 to 9 days (each about 10-12%).
- Leadership is concentrated: about 38 unique leader stocks per day in the S&P 500, 22 when only the top-ranked leader per target is counted.
- The ranking loss beats MSE on return and Sharpe; raw leader features beat learned temporal embeddings in the prediction stage.

## Signal construction
Intraday adaptation (the authors list an intraday version as future work): universe of liquid crypto perps plus equity-index and FX futures; bars of 1 to 15 minutes; per-bar features of return, range ratios, log volume; cross-attention from the SOL target to all other instruments over the last l_max bars; keep top-k (instrument, lag) keys; predict SOL's next-bar or next-hour return with a ranking or sign loss; retrain on a rolling schedule. Log the selected leaders and lags each bar as an interpretable diagnostic.

## Relevance to SOL perpetuals at minutes to hours
It is the leading machine-learning formulation of the exact problem "which other assets lead SOL right now, and by how much". The ablations support two design choices for a bot: exclude the target's own history from the leader search so the model must find cross-asset information, and let the lag vary by pair and time. The single-target setting (only SOL matters) is easier than the paper's cross-sectional one but has far fewer training labels.

## Caveats
Daily US equities; a two-year test window (2022-2023); costs are discussed, not netted. A near-uniform lag distribution is also what a model fitting noise would produce, and the paper's interpretation of it is an argument, not a test. Many baselines and architecture choices raise the usual deep-learning backtest-overfitting concern. No crypto or intraday evidence.
