---
title: "Downside Risk Reduction Using Regime-Switching Signals: A Statistical Jump Model Approach"
authors: "Shu, Yizhan; Yu, Chenyu; Mulvey, John M."
year: 2024
venue: "arXiv preprint arXiv:2402.05272v3 (q-fin.PM)"
url: "https://arxiv.org/pdf/2402.05272"
pdf: "sources/01-macro-regime-detection/shu-2024-downside-risk-statistical-jump-model.pdf"
access: "full-text"
source_type: "working-paper"
evidence_grade: "B"
topic: "01-macro-regime-detection"
asset_class: "equities"
horizon: "daily"
tags: "statistical-jump-model, jump-penalty, hidden-markov-model, online-inference, cross-validation, transaction-costs, trading-delay"
---

## Key insight
A statistical jump model, which is k-means clustering of features plus a fixed penalty for every change of state, gives more persistent and more tradable regimes than a hidden Markov model. In a realistic test on three equity indices over 1990 to 2023, with online inference, a one-day trading delay and 10 bp costs, the jump-model strategy beat both buy-and-hold and the HMM strategy on Sharpe ratio and drawdown with a fraction of the HMM's turnover. The paper is also a template for doing the whole pipeline without look-ahead.

## Method
Two-state jump model on D standardised features `x_t`:

`minimise over centroids theta and states s:  sum_t l(x_t, theta_{s_t}) + lambda * sum_t 1{s_{t-1} != s_t}`

with `l` the scaled squared Euclidean distance. Features, all computed from the excess-return series with exponential weighting: downside deviation (halflife 10 days) and Sortino ratio (halflives 20 and 60 days). Centroids are refitted every six months on a 3000-day window. Online inference: at the end of day t, solve the state-sequence problem over a lookback window with centroids fixed and keep only the last state. The jump penalty lambda is chosen monthly by time-series cross-validation: for each candidate, simulate the online strategy over the previous eight years and pick the lambda with the best Sharpe ratio. The HMM benchmark gets the same treatment for its smoothing hyperparameter. Strategy: 100% index in the bull state, 100% risk-free in the bear state; a signal from day t is applied from day t+2.

## Data and sample
Daily returns of the S&P 500, DAX and Nikkei 225. Data from 1970; test period 1990 to 2023 after 12 years of training and 8 of validation.

## Reported results
Buy-and-hold / HMM / jump model, 1990 to 2023, net of 10 bp one-way:
- S&P 500: Sharpe 0.48 / 0.54 / 0.68; max drawdown -55.2% / -28.9% / -26.6%; annual turnover 0% / 141% / 44%.
- DAX: Sharpe 0.30 / 0.35 / 0.44; max drawdown -72.7% / -40.5% / -39.4%; turnover 0% / 246% / 170%.
- Nikkei: Sharpe 0.12 / 0.19 / 0.31; max drawdown -79.1% / -48.6% / -45.3%; turnover 0% / 290% / 72%.
- Annual return: jump model 11.2%, 8.6%, 4.7% against buy-and-hold 10.2%, 6.8%, 0.8%. The HMM strategy's return was below buy-and-hold for the S&P 500 (8.5%) and DAX (6.4%).
- S&P 500 online jump model: 19.7% of days labelled bear, 30 regime shifts in 34 years.
- Online regime shifts per year on the S&P 500, 1982 to 2023, with fixed hyperparameters: HMM 8.5 unsmoothed and still 2.0 after a 20-day rolling mean; jump model 9.7 at lambda = 0 (plain k-means), 2.7 at lambda = 5, 0.8 at lambda = 35.
- Delays of 5 and 10 days: S&P 500 jump-model Sharpe 0.71 and 0.70; DAX falls to 0.38 and 0.29.
- The authors note regimes are identified with some latency at the start and end of crashes, and that the HMM produces many short-lived regimes.

## Signal construction
Inputs: bar returns. Compute EWM downside deviation and EWM Sortino ratios at two or three halflives, standardise using training-window statistics only, fit two centroids with a jump penalty, classify online with centroids frozen, and re-select lambda periodically on a trailing validation window using net strategy performance. Output: a binary favourable/unfavourable state, lagged by at least one bar before use.

## Relevance to SOL perpetuals at minutes to hours
The method transfers; the parameters do not. Halflives in bars, window lengths and lambda must be re-tuned for intraday crypto, and the features could be extended with funding, open interest and cross-venue flow. The long/flat rule maps naturally to "allow longs only in the favourable state" or to position scaling. The jump penalty has the same units as the loss, so it must be re-scaled when the bar size or feature set changes.

## Caveats
Three equity indices with strong positive drift; 30 regime shifts is a small number of independent bets. Feature choice was made with knowledge of equity history. Code is published by the first author, which helps replication, but I saw no independent replication. The related sparse-jump-model crypto study is [cortese-2023](cortese-2023-cryptocurrency-returns-sparse-jump-model.md).
