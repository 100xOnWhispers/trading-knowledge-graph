---
title: "Deep reinforcement learning for the optimal placement of cryptocurrency limit orders"
authors: "Schnaubelt, Matthias"
year: 2020
venue: "FAU Discussion Papers in Economics No. 05/2020"
url: "https://www.econstor.eu/handle/10419/216206"
pdf: "sources/27-execution-risk-management/schnaubelt-2020-deep-rl-cryptocurrency-limit-order-placement.pdf"
access: "full-text"
source_type: "working-paper"
evidence_grade: "B"
topic: "27-execution-risk-management"
asset_class: "crypto"
horizon: "minutes"
tags: "reinforcement-learning, ppo, ddqn, limit-order-placement, exchange-fees, implementation-shortfall, crypto-spot"
---

## Key insight
On crypto spot exchanges, most of the cost of executing a moderately sized order is the exchange fee, not price impact, so the main job of an execution policy is to get filled as a maker. A deep reinforcement learning agent (proximal policy optimisation) learns to do this better than static rules and better than deep Q-learning, out of sample, and becomes more aggressive when it expects price to move against it.

## Method
Extends the Nevmyvaka et al. set-up. An agent must sell `v0` units within `T` = 4 one-minute steps. At each step it chooses a limit price; unfilled volume at the end is sold by market order. A "virtual limit order exchange" matches the agent's order against recorded trades and book states. Reward is realised implementation shortfall relative to the starting mid price, including maker and taker fees. Algorithms: backward-induction Q-learning (the 2006 method), deep double Q-networks (DDQN) and proximal policy optimisation (PPO), each trained for 10 million time steps. Benchmarks: immediate market order (IM), time-weighted market orders (TW), and submit-and-leave (S&L). Evaluation uses four rolling train-test splits with non-overlapping validation periods.

## Data and sample
January 2018 to June 2019, about 300 million trades and more than 3.5 million order book states sampled each minute. BitFinex (BTC/USD, ETH/USD, ETH/BTC), Kraken (BTC/USD) and Coinbase (BTC/USD). Fees used, maker / taker in bp: BitFinex 10 / 20, Kraken 16 / 26, Coinbase 0 / 30. Order sizes 10, 20 and 50 BTC, or 100 and 200 ETH, about 25% to 300% of average one-minute volume.

## Reported results
- PPO has the lowest mean total shortfall and is best in 89.06% of train-test splits and exchange-market combinations.
- Against a single market order, PPO cuts total shortfall by 37.71% for 10 BTC, 26.95% for 20 BTC and 23.72% for 50 BTC.
- Example: selling 20 BTC on BitFinex costs 24.98 bp by immediate market order and 21.66 bp time-weighted.
- S&L improves on TW by 11.45% on average; backward-induction Q-learning adds 3.51% over S&L; DDQN 3.61%; PPO 8.53%, roughly 2 bp.
- For 10 BTC, only about ten percent of cost is raw price shortfall; the rest is fees. For larger sizes fees are still well over half.
- Most informative features: current liquidity cost and queue imbalance.
- Hyperparameters were not tuned because training was too expensive.

## Signal construction
Not a directional signal. Execution policy inputs: time left, volume left, spread, cost to cross for the remaining size, queue imbalance, recent returns and volume. Output: limit price offset. Reward must include the venue's actual maker and taker fees, since the fee term dominates. A sensible ladder for the bot: fixed S&L offset first, then a tabular learner, then PPO only if the first two leave measurable cost on the table.

## Relevance to SOL perpetuals at minutes to hours
The fee structure is the transferable part. Kalshi's entry-tier retail schedule (2 bp maker, 12 bp taker, topic 06) has an even larger maker-taker gap relative to the spread than the 2018 spot venues here, so the same conclusion should hold: a policy's value is mostly its maker fill rate. The specific gains do not transfer: these are spot markets at one-minute resolution with order sizes far above what the bot will trade.

## Caveats
One-minute book snapshots cannot resolve queue position, so passive fills are approximated and probably optimistic; Albers et al. show that real passive fills carry adverse selection that this kind of simulator misses. No market impact of the agent's own orders. 2018 to 2019 data from a different market structure. The discussion-paper version was read; a later journal version was not opened. Single author, no independent replication found.
