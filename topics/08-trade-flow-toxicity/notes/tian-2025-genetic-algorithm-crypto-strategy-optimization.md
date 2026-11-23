---
title: "Agent-Based Genetic Algorithm for Crypto Trading Strategy Optimization"
authors: "Tian, Qiushi; Liang, Churong; Hong, Kairan; Li, Runnan"
year: 2025
venue: "arXiv 2510.07943v1 (October 2025)"
url: "https://arxiv.org/pdf/2510.07943"
pdf: "sources/08-trade-flow-toxicity/tian-2025-genetic-algorithm-crypto-strategy-optimization.pdf"
access: "full-text"
source_type: "working-paper"
evidence_grade: "C"
topic: "08-trade-flow-toxicity"
asset_class: "crypto"
horizon: "minutes"
tags: "evolutionary-algorithms, genetic-algorithm, parameter-optimization, multi-agent, rolling-reoptimization, scalping"
---

## Key insight
The paper wraps a genetic algorithm in a set of cooperating software agents (CGA-Agent) to re-tune the parameters of a simple five-minute crypto strategy every 30 days, and reports higher backtest returns than the untuned strategy on BTC, ETH and BNB. It is included here as the most recent example found of evolutionary optimization on intraday crypto data, and as an illustration of how thin the evidence for such methods is. It does not use trade-flow features despite the abstract's reference to "market microstructure intelligence".

## Method
The object optimized is a parameter vector theta of a fixed strategy, with theta chosen to maximize a fitness score on a rolling window of recent data. Fitness is a weighted sum of eleven backtest metrics (Sharpe ratio, Sortino ratio, annualized return, win rate, return volatility and others). Six agents implement the loop: analysis and generation agents create the initial parameter "genes"; an evaluation agent backtests and scores them; a selection agent keeps the top 20% and samples the rest with probability proportional to shifted fitness; crossover and mutation agents create the next generation from templates. The baseline strategy is a dual-RSI crossover (buy when the fast RSI crosses above the slow RSI, sell on the opposite cross) with three switchable filters: fast moving average, slow moving average and an ATR-normalized slope filter.

## Data and sample
Five-minute candles for BTC, ETH and BNB from 25 December 2024 to 1 September 2025 (252 days), with re-optimization every 30 trading days in a rolling-window backtest. The venue and whether the instruments are spot or perpetual are not stated in the text read.

## Reported results
- Total PnL, baseline versus optimized: BTC 1.68% versus 2.17%; ETH 0.64% versus 4.16%; BNB 3.44% versus 9.27%.
- Sharpe ratio: BTC 1.36 versus 1.26 (lower after optimization); ETH 0.46 versus 2.09; BNB 1.35 versus 2.99.
- Return volatility rose for all three (0.12 to 0.17, 0.14 to 0.20, 0.25 to 0.30).
- The headline "29%, 550% and 169%" improvements are relative changes in these small PnL figures.

## Signal construction
Not a signal. The transferable method is a walk-forward evolutionary parameter search: every N days, run a genetic algorithm over the parameters of a fixed, simple rule using only the trailing window, with a multi-metric fitness function, elitism (top 20%), fitness-proportional sampling, crossover and mutation, then trade the best parameters for the next N days. In this topic's context the parameters would be flow-feature settings such as imbalance lookbacks, volume-bucket size and entry thresholds.

## Relevance to SOL perpetuals at minutes to hours
The five-minute horizon and rolling re-optimization match how a SOL bot would be maintained, and a genetic search is a reasonable tool for non-differentiable objectives such as net Sharpe after fees. Nothing in the results shows that it beats cheaper alternatives. The comparison is against untuned defaults, not against grid search, Bayesian optimization or random search with the same budget, so the gain may reflect tuning in general. [kitron-2026-short-horizon-mean-reversion-crypto](kitron-2026-short-horizon-mean-reversion-crypto.md) is the relevant counterweight: at this signal-to-noise level a three-parameter constrained model beat flexible learners out of sample.

## Caveats
Six pages, unrefereed. Eight months, three assets, one baseline strategy. Transaction costs and slippage are not discussed in the text read. No statistical tests despite the abstract's claim of statistically significant improvement. BTC's Sharpe ratio fell after optimization. A multi-metric fitness function tuned on recent data is a direct route to overfitting, and no comparison against a held-out period beyond the rolling scheme is given.
