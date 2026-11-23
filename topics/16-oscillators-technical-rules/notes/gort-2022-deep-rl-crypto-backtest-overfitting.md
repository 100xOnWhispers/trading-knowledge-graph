---
title: "Deep Reinforcement Learning for Cryptocurrency Trading: Practical Approach to Address Backtest Overfitting"
authors: "Gort, Berend Jelmer Dirk; Liu, Xiao-Yang; Gao, Jiechao; Chen, Shuaiyu; Wang, Christina Dan"
year: 2022
venue: "arXiv preprint 2209.05559 (v6, January 2023)"
url: "https://arxiv.org/pdf/2209.05559"
pdf: "sources/16-oscillators-technical-rules/gort-2022-deep-rl-crypto-backtest-overfitting.pdf"
access: "full-text"
source_type: "working-paper"
evidence_grade: "C"
topic: "16-oscillators-technical-rules"
asset_class: "crypto"
horizon: "minutes"
tags: "reinforcement-learning, ppo, backtest-overfitting, combinatorial-cross-validation, rsi, technical-indicators, sol, five-minute"
---

## Key insight
Reinforcement-learning agents fed oscillators at five-minute frequency are highly sensitive to hyperparameters, and the usual walk-forward or k-fold validation lets overfitted agents through. Treating overfitting as a hypothesis test, with a probability of overfitting estimated by combinatorial cross-validation, selects agents that hold up better. "Better" in the test window still means a loss of about 35% against a market loss of about 50%.

## Method
The task is a multi-asset trading Markov decision process. The state holds cash, holdings, close prices and technical indicators; the action is the amount of each coin to buy or sell; the reward is the change in portfolio value. A fee of 0.3% of traded value is charged, and slippage is ignored. Candidate features are OHLCV plus nine indicators: RSI, MACD, CCI, DX, rate of change, Ultimate Oscillator, Williams %R, on-balance volume and the Hilbert Transform dominant cycle. One of any pair with absolute correlation above 0.6 is dropped, leaving volume, RSI, DX, Ultimate Oscillator, OBV and the Hilbert feature. Agents are PPO, TD3 and SAC.

Overfitting test: split the training data into N = 5 groups and form all splits with k = 2 validation groups (10 splits). For each hyperparameter trial, record in-sample and out-of-sample returns over the splits. The probability of overfitting p is the frequency with which the trial that ranks best in sample ranks below the median out of sample (computed from the distribution of rank logits). Agents with p above the significance level of 10% are rejected. Short positions are not allowed. A risk overlay stops buying and sells all holdings when the CVIX crypto volatility index exceeds 90.

## Data and sample
Five-minute data for ten coins: AAVE, AVAX, BTC, NEAR, LINK, ETH, LTC, MATIC, UNI and SOL. Training 2 February to 30 April 2022 (25,055 bars); testing 1 May to 27 June 2022 (16,704 bars), a period with two market crashes. The data source was not confirmed in my reading.

## Reported results
- Probability of overfitting: PPO with walk-forward validation 17.5% (rejected); PPO with k-fold 7.9%; PPO with combinatorial cross-validation 8.0%; TD3 9.6%; SAC 21.3% (rejected).
- Cumulative return over the test window: PPO with combinatorial cross-validation -34.96%; equal-weight portfolio -47.78%; S&P crypto broad market index -50.78%; PPO walk-forward -49.39%; PPO k-fold -55.54%; TD3 -59.08%; SAC -59.48%.
- The selected PPO agent also had the lowest volatility.

## Signal construction
Not a signal. Two reusable pieces:
1. Feature hygiene: compute the indicator set on 5-minute bars and prune by pairwise correlation before modelling. In this data most oscillators were redundant with each other.
2. Model selection: for any tuned strategy (not only reinforcement learning), run combinatorial purged cross-validation over hyperparameter trials and reject configurations whose in-sample winner frequently ranks in the bottom half out of sample.

## Relevance to SOL perpetuals at minutes to hours
SOL at five minutes is in the sample, and the feature set is the oscillator family this topic covers. The paper is weak evidence on profitability and good evidence on process: the same PPO algorithm produced -35% or -56% depending only on how hyperparameters were validated. The probability-of-overfitting check is cheap to add to a research pipeline. The agent is long-only spot with portfolio weights, so the action space would need redesign for a single perp with shorting and funding.

## Caveats
A 58-day test window in one crash regime cannot distinguish skill from lower average exposure; the "outperformance" may simply reflect holding more cash, and no exposure-matched benchmark is reported. TD3 passed the overfitting test and still did worst but one, so the test did not rank agents correctly. The volatility-index stop rule is an untested overlay that affects all results. Preprint, with no independent replication that I confirmed.
