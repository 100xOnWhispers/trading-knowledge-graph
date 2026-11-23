---
title: "A Deep Reinforcement Learning Framework for the Financial Portfolio Management Problem"
authors: "Jiang, Zhengyao; Xu, Dixing; Liang, Jinjun"
year: 2017
venue: "arXiv:1706.10059v2"
url: "https://arxiv.org/pdf/1706.10059"
pdf: "sources/24-reinforcement-learning/jiang-2017-deep-rl-portfolio-management-crypto.pdf"
access: "full-text"
source_type: "working-paper"
evidence_grade: "C"
topic: "24-reinforcement-learning"
asset_class: "crypto"
horizon: "minutes"
tags: "portfolio-management, policy-gradient, eiie, poloniex, 30-minute, zero-impact-assumption, commission, survivorship"
---

## Key insight
The most cited crypto RL paper frames 30-minute portfolio rebalancing as a policy-gradient problem with an exactly computable reward, and reports spectacular backtest returns on Poloniex. Its lasting contribution is the formulation: when the agent is assumed to have no market impact, prices are exogenous, the reward for any action on any historical step is known in closed form, and the policy can be trained by plain mini-batch gradient ascent on log return. The headline returns rest on zero-slippage fills at the last price in 2016 to 2017 altcoin markets and should be read as an upper bound.

## Method
Policy network: "Ensemble of Identical Independent Evaluators" (EIIE). The same small network (CNN, basic RNN or LSTM variants) scores each asset from its own recent price history (close, high, low, normalized); scores plus a cash bias go through a softmax to give portfolio weights. The previous period's weights are fed in from a Portfolio-Vector Memory so the network can account for the cost of changing them. Reward is the average log portfolio return net of commission, `R = (1/t_f) * sum_t ln( mu_t * y_t . w_{t-1} )`, where `y_t` is the vector of price relatives and `mu_t` is the fraction of value left after commissions. Training uses Online Stochastic Batch Learning: mini-batches of consecutive periods sampled with a bias toward recent data, continued during the backtest. Two stated assumptions: zero slippage (fills at the last price) and zero market impact.

## Data and sample
Poloniex, 30-minute bars. The 11 highest-volume non-cash coins are preselected using volume from before each backtest (to limit survivorship bias), with BTC as cash. Commission 0.25% per trade for both buys and sells. Three backtests of about 50 days each: 2016-09-07 to 2016-10-28, 2016-12-08 to 2017-01-28, 2017-03-07 to 2017-04-27, with training data starting in November 2014, February 2015 and May 2015 respectively.

## Reported results
- Final portfolio value as a multiple of initial (in BTC): CNN 29.7, 8.0, 31.7; basic RNN 13.3, 4.6, 47.1; LSTM 6.7, 4.1, 21.2 across the three backtests.
- Uniform buy and hold: 0.82, 1.03, 2.23. Best single asset: 1.22, 1.40, 4.59.
- Most classical online portfolio algorithms lost money at 0.25% commission in the first two periods.
- The abstract says "at least 4-fold returns in 50 days"; the results section says "in 20 days". The two statements are inconsistent in the source.
- Maximum drawdowns of the EIIE networks are 0.22 to 0.49.

## Signal construction
Not a ready signal. Usable pieces: (1) include current position in the policy input, (2) use log return net of proportional cost as the reward, (3) when the bot is small enough to be a price taker, compute the reward for any candidate action directly from recorded prices and train with supervised-style gradient ascent, with no value function and no exploration, (4) weight recent data more heavily when sampling batches.

## Relevance to SOL perpetuals at minutes to hours
The horizon matches. The single-instrument version of this setup (weights over {SOL perp long, cash, SOL perp short}) is the simplest RL baseline to build. The exogenous-price assumption is reasonable for a small account when signals come from large venues, less so for fills on a thin Kalshi book: the fill-at-last-price assumption has to be replaced with the observed bid or ask plus fees, and funding must be added to the reward.

## Caveats
Working paper; no independent replication at the reported magnitude was found in this session. Returns are measured in BTC. Filling at the last trade price with no spread on 2016 to 2017 Poloniex altcoin books is the assumption most likely to inflate results. Three short test windows, no seed variance reported in the passages read. Gort et al. (2022) criticize the validation scheme used in the authors' earlier work.
