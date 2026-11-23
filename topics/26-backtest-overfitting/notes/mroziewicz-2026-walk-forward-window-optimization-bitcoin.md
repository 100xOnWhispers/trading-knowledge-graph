---
title: "A Novel Approach to Trading Strategy Parameter Optimization Using Double Out-of-Sample Data and Walk-Forward Techniques"
authors: "Mroziewicz, Tomasz; Slepaczuk, Robert"
year: 2026
venue: "arXiv preprint 2602.10785"
url: "https://arxiv.org/pdf/2602.10785"
pdf: "sources/26-backtest-overfitting/mroziewicz-2026-walk-forward-window-optimization-bitcoin.pdf"
access: "full-text"
source_type: "working-paper"
evidence_grade: "C"
topic: "26-backtest-overfitting"
asset_class: "crypto"
horizon: "minutes"
tags: "walk-forward, window-length, parameter-stability, bitcoin, intraday, transaction-costs"
---

## Key insight
The lengths of the training and testing windows in a walk-forward optimization are themselves influential hyperparameters: the same simple strategy gives very different results depending on them. The paper treats window lengths as parameters to be chosen on a first dataset using a neighbourhood-smoothed ("robust") Sharpe ratio, then evaluates the chosen settings exactly once on a second, untouched period ("double out-of-sample").

## Method
- Strategy: exponential moving average crossover, long when the fast average is above the slow one and short otherwise; EMA parameters re-optimized inside each walk-forward training window and applied to the following test window.
- Meta-search: 81 combinations of walk-forward training and testing lengths (each from 1 to 28 days) at six bar frequencies from 1 to 60 minutes, run on a "global training" period.
- Selection: a robust Sharpe for each cell of the training-length by testing-length grid, computed as a weighted average in which the cell's own Sharpe keeps half the weight and its neighbours share the other half. The two best cells are selected.
- Final evaluation: the two selected settings are run once on the "unseen" period, and the Bitcoin-derived settings are also applied to Ethereum and Binance Coin.
- Costs: 0.1% per transaction (0.2% for a long-to-short reversal), with sensitivity from 0.05% to 0.50%. A block bootstrap that shuffles position blocks is used as a further check.

## Data and sample
Bitcoin intraday prices, global training period February 8, 2018 to September 1, 2019 (19 months); unseen period November 7, 2019 to August 22, 2021 (21 months). Ethereum and Binance Coin for cross-asset checks. Exchange source not confirmed in the text read.

## Reported results
- Performance is highly dependent on window size; one-day testing windows consistently gave the lowest Sharpe ratios, and long training with long testing windows gave the highest in the 60-minute grid.
- In the training period all 81 window combinations beat buy-and-hold on Bitcoin.
- In the unseen period the strategy performed similarly to buy-and-hold but with lower drawdown and a higher information ratio; similar results for Ethereum and Binance Coin.
- A portfolio combining buy-and-hold with the strategies had the best overall performance and a 50% reduction in drawdown.
- Break-even transaction cost was around 0.4% per transaction.
- Of the two selected settings, training 7 days with testing 28 days had the smaller drawdown and higher information ratio.

## Signal construction
The EMA crossover itself is covered by other topics. The methodological contribution a bot can use: (1) treat re-fit frequency and look-back length as searched parameters; (2) pick them by neighbourhood-averaged performance, not the single best cell; (3) reserve a final period that is touched once; (4) report the break-even cost.

## Relevance to SOL perpetuals at minutes to hours
Directly on point for horizon and asset class. Any adaptive bot must decide how often to re-fit and on how much history, and this paper shows that choice is a source of overfitting that standard walk-forward leaves unexamined. The smoothed-grid selection is a cheap guard against picking an isolated lucky cell and applies equally to choosing among neighbouring hyperparameters of a learned model. The move from "beats buy-and-hold in training" to "about equal to buy-and-hold on unseen data" is a realistic picture of decay.

## Caveats
One strategy family, one meta-search, one final window; the unseen period (late 2019 to August 2021) is dominated by a bull market, so comparison with buy-and-hold is regime-specific. Spot prices with a flat proportional cost; no funding, order book or slippage model. No formal multiple-testing correction for the 81 by 6 grid. Not peer reviewed. The single-use hold-out is only as clean as the authors' discipline, and the study period ends in 2021 although the paper is dated 2026.
