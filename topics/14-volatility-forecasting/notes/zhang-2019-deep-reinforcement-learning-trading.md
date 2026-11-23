---
title: "Deep Reinforcement Learning for Trading"
authors: "Zhang, Zihao; Zohren, Stefan; Roberts, Stephen"
year: 2019
venue: "arXiv preprint 1911.10107"
url: "https://arxiv.org/pdf/1911.10107"
pdf: "sources/14-volatility-forecasting/zhang-2019-deep-reinforcement-learning-trading.pdf"
access: "full-text"
source_type: "working-paper"
evidence_grade: "B"
topic: "14-volatility-forecasting"
asset_class: "futures"
horizon: "daily"
tags: "reinforcement-learning, dqn, policy-gradient, a2c, volatility-scaling, reward-design, transaction-costs"
---

## Key insight
Volatility scaling can be built into the reward function of a reinforcement-learning trading agent, so the agent learns direction while position size is set by a volatility target. With that reward, a transaction-cost penalty and LSTM-based agents, DQN, policy-gradient and actor-critic methods outperform classical time-series momentum rules on 50 futures out of sample. The paper is the standard reference for combining RL with volatility-targeted sizing.

## Method
State: the past 60 observations of normalised close prices, returns over 1, 2, 3 and 12 months normalised by volatility, MACD and a 30-day RSI. Action: position in {-1, 0, 1} for DQN and policy gradient, or continuous in [-1, 1] for A2C. Reward at t:

R_t = mu * [ A_{t-1} * (sigma_tgt / sigma_{t-1}) * r_t - bp * p_{t-1} * | (sigma_tgt / sigma_{t-1}) * A_{t-1} - (sigma_tgt / sigma_{t-2}) * A_{t-2} | ],

where A is the action, sigma_tgt the volatility target, sigma an ex-ante volatility estimate (exponentially weighted standard deviation, 60-day window), and bp the cost rate. Volatility scaling also normalises rewards across contracts with different price scales. The cost rate used in training (20 basis points in the reported hyperparameters) acts as a turnover regulariser. Networks are two-layer LSTMs. Baselines: long-only, sign of past return and a MACD signal, all with the same volatility scaling. Portfolio-level volatility targeting is applied on top.

## Data and sample
50 liquid ratio-adjusted continuous futures (commodities, equity indices, fixed income, FX) from Pinnacle Data, daily, 2005 to 2019. Out-of-sample testing covers 2011 to 2019.

## Reported results
- All-contract portfolio, annualised Sharpe ratio: DQN 1.288, A2C 1.050, policy gradient 0.754, sign-of-return momentum 0.441, MACD 0.091, long-only 0.058.
- By asset class DQN leads in commodities (0.723), fixed income (0.935) and FX (0.546); in equity indices long-only is best (0.688 versus DQN 0.648).
- DQN and A2C still generate positive profits at a cost rate of 25 basis points.
- A2C has higher turnover and smaller return per unit turnover than DQN.

## Signal construction
A design pattern for an RL sizing layer: let the agent choose a direction or a bounded exposure in [-1, 1]; multiply by sigma_tgt / sigma_hat to get the actual position; charge the reward for the change in the scaled position, including changes caused by volatility moving. For a perpetual, add the funding payment to the reward and cap the scaled position at the venue's leverage limit inside the environment so the agent learns under the constraint.

## Relevance to SOL perpetuals at minutes to hours
The reward construction transfers to any horizon. The evidence does not: it is daily data on diversified futures, where gains come from holding trends across 50 contracts. A single-asset intraday agent faces far noisier rewards (the Qin note discusses this for leveraged crypto futures). The finding that a high training cost rate improves behaviour is a useful regularisation idea for a venue with meaningful fees.

## Caveats
Preprint; a later journal version was not confirmed in this session. One train/test protocol and many unreported design choices. Baselines are simple. The cost model is proportional only, with no slippage or market impact. Out-of-sample period 2011 to 2019 favoured trend following in several asset classes.
