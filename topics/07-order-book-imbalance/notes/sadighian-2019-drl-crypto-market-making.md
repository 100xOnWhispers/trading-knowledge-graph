---
title: "Deep Reinforcement Learning in Cryptocurrency Market Making"
authors: "Sadighian, Jonathan"
year: 2019
venue: "arXiv:1911.08647v1"
url: "https://arxiv.org/pdf/1911.08647"
pdf: "sources/07-order-book-imbalance/sadighian-2019-drl-crypto-market-making.pdf"
access: "full-text"
source_type: "working-paper"
evidence_grade: "C"
topic: "07-order-book-imbalance"
asset_class: "crypto"
horizon: "seconds"
tags: "reinforcement-learning, a2c, ppo, market-making, order-flow-imbalance, trade-flow-imbalance, coinbase, reward-design"
---

## Key insight
An early crypto example of putting order-flow-imbalance features directly into the state of a deep RL agent. Policy-gradient agents (A2C, PPO) that observe a stationary transform of the book plus per-level OFI and multi-window trade flow imbalance learned to quote and manage inventory with small positive test returns. Reward design mattered more than the algorithm: a clipped "trade completion" reward gave larger and steadier returns than mark-to-market PnL. The evidence is thin (two test days).

## Method
Environment state: a window of snapshots containing 15 book levels per side (stationary transform, z-scored with the previous day's statistics), order flow imbalance per level and side, trade flow imbalance, and agent state (inventory, PnL, order distances). OFI per level is the notional of limit orders added minus cancellations minus market orders between snapshots, a 30-value vector. TFI measures buyer- versus seller-initiated volume scaled to [-1, 1] over 5, 15 and 30 minute windows. Actions choose bid and ask quote levels or flatten inventory. The policy is a multilayer perceptron trained with A2C and PPO. Two rewards are compared: positional PnL (change in unrealized value plus realized PnL) and trade completion (clipped, goal-based reward for closing trades at a target profit-to-loss ratio).

## Data and sample
Level-3 tick data recorded from Coinbase for BTC-USD, ETH-USD and LTC-USD, replayed to rebuild the book; 1-second snapshots. Training on 27 September to 4 October 2019 (8 days); testing on 1 and 2 November 2019.

## Reported results
- Average daily return over the two test days with the trade-completion reward: A2C 3.3063% (BTC), 0.0643% (ETH), 1.5078% (LTC); PPO 0.4051%, 0.0650%, 1.4223%.
- With positional PnL reward: A2C 0.0934%, -0.0851%, -0.1836%; PPO -0.1094%, 0.1320%, 0.3462%.
- Average per-trade PnL is tiny in every case (at most 0.0034%).
- Results are sensitive to the action-repeat setting at test time.
- Limit order fees and rebates are not modelled; market orders are charged 0.20% per side. A new quote at an occupied price is assumed to jump ahead of the queue.

## Signal construction
State vector for an RL agent, updated each second: (a) stationary book transform over N levels; (b) per-level OFI notional = adds - cancels - trades, by side; (c) TFI over several windows; (d) inventory and unrealized PnL. Normalize each feature with the prior day's mean and standard deviation. Reward: realized PnL of completed round trips, clipped to [-1, 1] around a target, to discourage holding losing inventory.

## Relevance to SOL perpetuals at minutes to hours
Relevant mainly as a template for including OFI and multi-window TFI (5 to 30 minutes, the bot's horizon) in an RL state, and for the finding that clipped, completion-based rewards train more stably than raw PnL. The reported returns should not be relied on: the queue-jumping fill assumption and missing maker fees flatter the result, and two test days prove nothing. A directional SOL bot would replace the quoting action set with position targets and should use a simulator with realistic fills and funding.

## Caveats
Eight training days and two test days from 2019. Optimistic fill model, no maker fees, no latency. Spot Coinbase pairs, not perpetuals. Single-author preprint. No comparison against a non-RL baseline using the same features.
