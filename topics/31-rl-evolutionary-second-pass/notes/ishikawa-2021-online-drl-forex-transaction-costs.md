---
title: "Online Trading Models with Deep Reinforcement Learning in the Forex Market Considering Transaction Costs"
authors: "Ishikawa, Koya; Nakata, Kazuhide"
year: 2021
venue: "arXiv:2106.03035"
url: "https://arxiv.org/abs/2106.03035"
pdf: "sources/31-rl-evolutionary-second-pass/ishikawa-2021-online-drl-forex-transaction-costs.pdf"
access: "full-text"
source_type: "working-paper"
evidence_grade: "C"
topic: "31-rl-evolutionary-second-pass"
asset_class: "fx"
horizon: "minutes"
tags: "reinforcement-learning, head-to-head, supervised-baseline, lightgbm, lstm, transaction-costs, online-learning"
---

## Key insight
One of the few papers that puts an RL trader beside supervised forecasters on the same one-minute data at several cost levels. At the lowest cost an LSTM classifier matched the RL agent; as cost rose, the supervised models stopped trading because a one-step move rarely exceeds the cost, while the RL agent kept trading by holding longer, and at the highest cost everything lost money. The comparison is not equal: the RL agent kept learning through the test period and the baselines were frozen.

## Method
- RL agent: a deep Q-network with LSTM layers. The reward is the one-step profit of the position minus a cost `c` charged when a new position is taken.
- Online learning: one network (`theta`) trains continuously on a rolling buffer of the latest data; a second (`phi`) trades and receives a copy of the weights only when flat, so parameters never change during an open position.
- Supervised baselines: an LSTM and LightGBM predicting the next one-minute move. To make them cost-aware, the target is a four-level classification of whether the price rises or falls by more than the transaction cost; the exact class boundaries and the rule mapping classes to trades are not spelled out in the text read.
- Cost levels: 0.01%, 0.02%, 0.05%, 0.08% and 0.1% of notional.

## Data and sample
USD/JPY one-minute data for calendar 2020. Baselines train on January to June and are evaluated on July to December. The RL agent runs online through the year; reported results are for July to December.

## Reported results
"Sharpe ratio" below is the paper's own measure, mean trade return over its standard deviation (units of the return column are not stated).
- Cost 0.01%: RL 5,892 trades, ratio 2.04; LSTM 5,720 trades, 1.89; LightGBM 4,889 trades, 0.65. Average return per trade 2.93, 2.94 and 2.58.
- Cost 0.02%: RL 3,290 trades, 1.77; LSTM 1,701, 1.31; LightGBM 997, 0.43.
- Cost 0.05%: RL 583 trades, 0.68; LSTM 108, 0.70; LightGBM 129, 0.32.
- Cost 0.1%: RL -0.40; LSTM -1.24; LightGBM -1.98, with 145, 25 and 20 trades (the paper's Table 1 gives 245 trades for the RL agent at this cost; the two tables disagree).
- Average holding time: RL 6.4 to 9.7 steps; baselines 1.2 to 3.2 steps.

## Signal construction
Not a signal. Two devices: (1) a cost-aware supervised target, labelling a bar by whether the forward move exceeds the trading cost; (2) updating a live policy's weights only while flat.

## Relevance to SOL perpetuals at minutes to hours
The result supports the argument recorded in topic 24: for a price taker, the gain from RL over a supervised forecast is in how the position rule handles costs, not in the forecast. The baselines here used a one-step horizon; a supervised model with a multi-bar target and a no-trade band was not tried and would be the fair comparison. At costs of 0.05% and above the one-step supervised design nearly stopped trading (108 and then 25 trades in six months), so if the bot's all-in cost per trade is in that range, a one-minute, one-step target is the wrong design whatever the learner.

## Caveats
One currency pair, one half-year, one run per model, no seeds, no confidence intervals, and very small trade counts at higher costs. The online RL agent had access to test-period data for training (in a causal way) that the frozen baselines did not. Fills are at bar prices with a fixed proportional cost. Preprint, not peer reviewed.
