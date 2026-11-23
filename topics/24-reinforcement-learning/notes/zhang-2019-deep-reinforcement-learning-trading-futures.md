---
title: "Deep Reinforcement Learning for Trading"
authors: "Zhang, Zihao; Zohren, Stefan; Roberts, Stephen"
year: 2019
venue: "arXiv:1911.10107v1"
url: "https://arxiv.org/pdf/1911.10107"
pdf: "sources/24-reinforcement-learning/zhang-2019-deep-reinforcement-learning-trading-futures.pdf"
access: "full-text"
source_type: "working-paper"
evidence_grade: "B"
topic: "24-reinforcement-learning"
asset_class: "futures"
horizon: "daily"
tags: "dqn, policy-gradient, a2c, volatility-scaling, reward-design, time-series-momentum, transaction-costs, futures"
---

## Key insight
On 50 liquid futures, three standard deep RL algorithms trained with a volatility-scaled, cost-aware reward beat time-series momentum baselines out of sample from 2011 to 2019. The design choice that matters is the reward: positions are scaled by target volatility over realized volatility inside the reward, so the agent learns direction and holding behavior while position size is handled by a rule. The discrete-action DQN did best, partly because the continuous-action actor-critic traded more.

## Method
State: 60 past observations of normalized close, returns over 1, 2, 3 months and 1 year (each divided by volatility scaled to the horizon), MACD-style indicators, and a 30-day RSI. Action: target position, {-1, 0, 1} for DQN and policy gradient (PG), continuous in [-1, 1] for A2C. Reward (equation 4):

`R_t = mu * [ A_{t-1} * (sigma_tgt / sigma_{t-1}) * r_t - bp * p_{t-1} * | (sigma_tgt / sigma_{t-1}) * A_{t-1} - (sigma_tgt / sigma_{t-2}) * A_{t-2} | ]`

where `sigma` is an exponentially weighted standard deviation with a 60-day window, `r_t` is the additive price change and `bp` is the cost rate. Networks are two-layer LSTMs (64 and 32 units). DQN uses fixed targets, double and dueling variants. One model per asset class. The cost rate used in training acts as a turnover regularizer.

## Data and sample
50 ratio-adjusted continuous futures from Pinnacle Data Corp CLC: commodities, equity indices, fixed income, FX. Daily data 2005 to 2019. Models are retrained every 5 years on all data to date and then frozen; the out-of-sample period is 2011 to 2019. Baselines: long only, sign of past-year return, MACD signal.

## Reported results
With portfolio-level volatility targeting, all contracts, equal weight (Table 2):
- Sharpe: long only 0.058, Sign(R) 0.441, MACD 0.091, DQN 1.288, PG 0.754, A2C 1.050.
- By asset class, DQN Sharpe: commodities 0.723, equity indices 0.648 (long only was 0.688), fixed income 0.935, FX 0.546.
- RL underperformed the long-only baseline on equity indices, which trended up throughout the test.
- A2C had higher turnover and lower return per unit of turnover than DQN.
- DQN and A2C remained profitable at a cost rate of 25 bp, which the authors equate to about 3.5 USD per contract.

## Signal construction
Template for a single-instrument directional agent:
- Inputs: volatility-normalized returns over several look-backs, trend and oscillator features, a rolling window of each.
- Output: target position in {-1, 0, 1}.
- Size: multiply by `sigma_tgt / sigma_{t-1}` outside the network.
- Reward: equation 4, with the cost term charged on the change in scaled position.
- Refit on an expanding window at fixed intervals and freeze between refits.

## Relevance to SOL perpetuals at minutes to hours
The reward and action design carry over unchanged to intraday bars: replace the 60-day volatility with an intraday estimate (see the volatility-forecasting topic), add funding to the reward, and set `bp` from Kalshi fees plus half-spread. What does not carry over is the evidence. The result is on daily bars across 50 diversifying contracts, where the portfolio Sharpe is much higher than the per-contract Sharpe; the paper's own per-contract box plots (Figure 3, not tabulated in the text) are the relevant comparison for a single instrument. Daily trend features have no direct intraday analogue and must be re-derived.

## Caveats
Two refits only, so the out-of-sample test has effectively two model vintages. No seed variance reported. Costs are proportional with no spread or slippage model. Baselines are simple; a tuned trend-following system is a harder benchmark. Hyperparameter selection procedure is not described in the passages read.
