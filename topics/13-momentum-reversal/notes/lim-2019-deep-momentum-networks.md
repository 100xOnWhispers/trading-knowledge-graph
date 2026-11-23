---
title: "Enhancing Time Series Momentum Strategies Using Deep Neural Networks"
authors: "Lim, Bryan; Zohren, Stefan; Roberts, Stephen"
year: 2019
venue: "arXiv preprint 1904.04912 (v3, 2020)"
url: "https://arxiv.org/pdf/1904.04912"
pdf: "sources/13-momentum-reversal/lim-2019-deep-momentum-networks.pdf"
access: "full-text"
source_type: "working-paper"
evidence_grade: "B"
topic: "13-momentum-reversal"
asset_class: "futures"
horizon: "daily"
tags: "machine-learning, deep-momentum-network, lstm, sharpe-loss, time-series-momentum, turnover"
---

## Key insight
Instead of hand-specifying a trend estimator and a position-sizing rule, a neural network can learn both jointly by outputting a position directly and being trained to maximise the Sharpe ratio of the resulting volatility-scaled returns. On 88 futures, the Sharpe-optimised LSTM more than doubled the Sharpe ratio of the classic sign-of-return rule before costs. The advantage shrinks quickly with costs because the learned signal trades faster, which the authors address with a turnover penalty in the loss.

## Method
Deep Momentum Networks keep the time-series momentum framework, position = X_t * (sigma_target / sigma_t) with a 15% volatility target, and replace X_t with a network output in [-1, 1]. Architectures compared: linear, MLP, WaveNet, LSTM. Losses compared: mean-squared error and binary classification on returns (predict, then map to a position) versus direct optimisation of average return or Sharpe ratio. Inputs per asset per day: returns over the past 1 day, 1, 3, 6 and 12 months, each normalised by volatility scaled to the horizon, plus volatility-normalised MACD trend estimates with short spans {8, 16, 32} and long spans {24, 48, 96}. Training uses Adam, dropout, early stopping on the most recent 10% of each training block, and random hyperparameter search. Models are refitted every five years on an expanding window, with all reported tests out-of-sample.

## Data and sample
88 ratio-adjusted continuous futures contracts from the Pinnacle Data Corp CLC database, covering commodities, fixed income, equity indices and currencies, daily, 1990 to 2015.

## Reported results
- Without costs, the Sharpe-optimised LSTM beats every benchmark: 44% better than the best other network (Sharpe-optimised MLP) and more than two times the best reference rule (sign of 12-month return).
- Models trained with regression or classification losses generally underperform those trained directly on Sharpe.
- The LSTM keeps outperforming for transaction costs up to about 2 to 3 basis points; beyond that its higher turnover erodes the edge.
- A turnover regularisation term added to the loss lets the network adapt to higher-cost settings.

## Signal construction
Features at each bar: volatility-normalised returns at several look-backs and normalised MACD at several span pairs. Model: small LSTM mapping the feature sequence to a position in [-1, 1]. Loss: negative Sharpe of position * scaled next-bar return, minus cost * |change in position|. Refit on an expanding or rolling window; never tune on the test block.

## Relevance to SOL perpetuals at minutes to hours
This is the template for applying machine learning to trend signals in this repository: learn the position, not the price, train on the trading objective, and include costs in the loss. For SOL the training set should be a panel of liquid perpetuals at the chosen bar size so the network sees enough regimes. The cost sensitivity is the key number: an edge that disappears above 2 to 3 basis points on liquid futures will not survive taker fees on crypto perpetuals unless the turnover penalty is active from the start.

## Caveats
Daily futures, not crypto or intraday. Gains concentrate where costs are lowest. Deep models on a few thousand daily observations per asset are prone to overfitting; results depend on pooling 88 assets. Sample ends 2015; the follow-up by Wood et al. reports that these networks underperformed in later years.
