---
title: "Reinforcement Learning Pair Trading: A Dynamic Scaling Approach"
authors: "Yang, Hongshen; Malik, Avinash"
year: 2024
venue: "Journal of Risk and Financial Management 17(12), 555"
url: "https://arxiv.org/abs/2407.16103"
pdf: "sources/21-cross-asset-lead-lag/yang-2024-reinforcement-learning-pair-trading-dynamic-scaling.pdf"
access: "full-text"
source_type: "peer-reviewed"
evidence_grade: "C"
topic: "21-cross-asset-lead-lag"
asset_class: "crypto"
horizon: "minutes"
tags: "reinforcement-learning, pairs-trading, cointegration, a2c, ppo, dqn, sac, one-minute, binance"
---

## Key insight
A reinforcement-learning agent that observes the z-scored spread of a cointegrated crypto pair and chooses when, and how much, to trade can beat a fixed-threshold pairs rule in a one-month test, but the outcome depends almost entirely on which RL algorithm is used: one learner (A2C) wins while PPO, DQN and SAC lose most of the capital on the same data. The paper is useful mainly as a template for wrapping a cross-asset relative-value signal in an RL environment and as a demonstration of how fragile the result is.

## Method
Pair selection by correlation and the Engle-Granger two-step cointegration test over a moving window. Spread s is the residual of a rolling regression between the two prices, normalized to a z-score with the window mean and standard deviation. A grid search on the training period picks window size and open/close thresholds for the rule-based benchmark (Gatev et al. style). RL environment:
- Observation: (current position, spread z-score, zone), where the zone is one of five regions defined by the open and close thresholds.
- Action: RL1 decides only the timing of opening and closing; RL2 chooses a continuous target position A in [-1, 1] (for example 0.5 means half the portfolio in the long leg), so it also sizes the trade.
- Reward: realized portfolio change on closing, plus an action reward that encourages the conventional action in each zone, minus a transaction penalty.
- Algorithms: PPO, A2C and DQN for RL1; PPO, A2C and SAC for RL2. Benchmarks: the rule-based method and the threshold-adapting RL method of Kim and Kim (2019).

## Data and sample
Binance 1-minute data (n = 263,520 per the abstract). Candidate pairs are BTC quoted in EUR, GBP, RUB and USD; the selected pair is BTCEUR-BTCGBP. Formation and training October to November 2023; test 1 to 31 December 2023. Transaction cost 0.02%; best grid parameters: open 1.8 z, close 0.4 z, window 900 one-minute intervals.

## Reported results
Table 5, December 2023, cumulative return:
- Rule-based: 8.33% (490 actions, win/loss ratio 1.38).
- RL1: A2C 9.94% (249 actions, win/loss ratio 26.67); PPO 1.89%; DQN -31.99%.
- RL2: A2C 31.53% (229 actions); PPO -77.81%; SAC -87.12%.
- Kim and Kim method: -0.16% (PPO), -35.16% (A2C), -35.79% (DQN).
- Reported annualized Sharpe ratios are 25.91 (rule), 32.74 (RL1 A2C) and 94.34 (RL2 A2C).
- With zero fees RL1's cumulative profit is slightly below the rule-based method; all methods do better at lower fee tiers (0%, 0.01%) and worse at 0.05%.
The abstract describes the 8.33%, 9.94% and 31.53% figures as annualized, while the table and conclusion present them as returns for the one-month trading period.

## Signal construction
State for a SOL-centred version: z-score of the residual of SOL perp price regressed on BTC and ETH perp prices (rolling window), current position, and threshold zone. A policy maps the state to a target position in [-1, 1]; reward is PnL net of fees with a penalty on position changes. Train with an actor-critic method on one-minute bars and evaluate walk-forward across many months and several random seeds before believing any ranking of algorithms.

## Relevance to SOL perpetuals at minutes to hours
The traded pair is the same asset in two fiat quotes, which is closer to a triangular FX relation than to cross-asset lead-lag, so the profit source does not transfer to SOL versus BTC. What transfers is the framing: treat the cross-asset spread as the state and let the policy learn entry, exit and size under fees, instead of fixing thresholds. On Kalshi a single-leg version (trade only SOL, use the spread as a signal) is the realistic form, since the other leg would sit on a different venue.

## Caveats
One pair, one test month, no seeds or confidence intervals, and extreme dispersion across algorithms, which is what selection on noise looks like. Sharpe ratios above 25 indicate a near-arbitrage on thin BTCEUR and BTCGBP books that would not survive spread and depth; the backtest charges a flat fee only. The best algorithm was chosen on the test period. The benchmark's thresholds were also grid-searched. Treat as a design reference, not as evidence of an edge.
