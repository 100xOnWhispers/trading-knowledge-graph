---
title: "Deep Reinforcement Learning for Trading"
authors: "Zhang, Zihao; Zohren, Stefan; Roberts, Stephen"
year: 2019
venue: "arXiv preprint 1911.10107"
url: "https://arxiv.org/pdf/1911.10107"
pdf: "sources/13-momentum-reversal/zhang-2019-deep-reinforcement-learning-trading.pdf"
access: "full-text"
source_type: "working-paper"
evidence_grade: "B"
topic: "13-momentum-reversal"
asset_class: "futures"
horizon: "daily"
tags: "reinforcement-learning, dqn, policy-gradient, a2c, time-series-momentum, volatility-scaling, transaction-costs"
---

## Key insight
Reinforcement-learning agents given trend features and a volatility-scaled, cost-aware reward learn position policies that beat classical time-series momentum rules on 50 futures out of sample. The agents' advantage is mostly in how they hold and resize positions: they stay with large trends without churning and scale down in consolidations. A discrete-action DQN did best, and the cost rate used in training acts as a regulariser on turnover.

## Method
Trading is posed as a Markov decision process. State: the past 60 observations of normalised close, returns over 1, 2, 3 months and 1 year normalised by an exponentially weighted volatility (60-day span) scaled to the horizon, a normalised MACD, and a 30-day RSI. Actions: the target position, discrete {-1, 0, 1} or continuous in [-1, 1]. Reward (the paper's equation 4): volatility-scaled profit minus a cost on the change in scaled position,

`R(t) = mu * [ A(t-1) * (s_tgt/s(t-1)) * r(t) - bp * p(t-1) * | (s_tgt/s(t-1)) * A(t-1) - (s_tgt/s(t-2)) * A(t-2) | ]`

where s is the ex ante volatility (exponentially weighted, 60-day window), s_tgt the volatility target, p the price and mu = 1, so the agent is paid for volatility-targeted returns and charged bp basis points on turnover. Algorithms: Deep Q-Network (with fixed targets, double and duelling variants), Policy Gradient, and Advantage Actor-Critic. Models are retrained every five years on all data to date and then frozen for the next five. Baselines: long-only, sign of past return (time-series momentum) and a MACD signal, all volatility-scaled.

## Data and sample
50 ratio-adjusted continuous futures from the Pinnacle Data Corp CLC database (commodities, equity indices, fixed income, FX), daily, 2005 to 2019; out-of-sample test 2011 to 2019.

## Reported results
- The RL agents outperform the baselines in most asset classes; the exception is equity indices, where long-only was best during a long bull market.
- Long-only was worst in commodities and FX, where the agents' ability to go short at reasonable times helped.
- DQN performed best overall, A2C second; A2C traded more and earned less per unit of turnover.
- The agents tolerate higher cost rates than the baselines; DQN and A2C stayed profitable at a 25 basis point cost rate, which the authors equate to about USD 3.5 per contract.

## Signal construction
Not a formula but a training recipe. Features: the trend inputs above at the bot's bar size. Action: target position in {-1, 0, 1}. Reward: volatility-scaled next-bar profit minus fee and half-spread times position change (and, for perpetuals, minus funding accrued). Train offline on historical data with walk-forward retraining; deploy the frozen policy.

## Relevance to SOL perpetuals at minutes to hours
Shows that reinforcement learning is most useful here as a position-management layer on top of trend features, with costs inside the reward, not as a price predictor. The reward design transfers to SOL perpetuals with funding added as a holding cost. Using a high training cost rate to force low turnover is a practical trick for a venue with wide spreads.

## Caveats
Daily futures, one out-of-sample decade, no crypto. Value-based RL is sample-hungry and unstable; a single asset at intraday frequency gives correlated samples and invites overfitting to one regime. The baselines are simple. Results come from one training run configuration and one research group, with no independent replication seen.