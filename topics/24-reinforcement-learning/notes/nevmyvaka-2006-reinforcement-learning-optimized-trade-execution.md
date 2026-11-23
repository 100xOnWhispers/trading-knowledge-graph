---
title: "Reinforcement Learning for Optimized Trade Execution"
authors: "Nevmyvaka, Yuriy; Feng, Yi; Kearns, Michael"
year: 2006
venue: "Proceedings of the 23rd International Conference on Machine Learning (ICML 2006)"
url: "https://www.cis.upenn.edu/~mkearns/papers/rlexec.pdf"
pdf: "sources/24-reinforcement-learning/nevmyvaka-2006-reinforcement-learning-optimized-trade-execution.pdf"
access: "full-text"
source_type: "peer-reviewed"
evidence_grade: "A"
topic: "24-reinforcement-learning"
asset_class: "equities"
horizon: "minutes"
tags: "execution, q-learning, limit-order-book, state-design, private-variables, spread, market-impact, submit-and-leave"
---

## Key insight
The first large-scale test of reinforcement learning on order book data shows that a small tabular policy conditioned on time remaining and inventory remaining cuts execution cost by roughly a quarter to a third against an optimized fixed limit price, and that a few coarse market variables add a further 8 to 13 percent. The gain comes from a structural trick: the agent's private state (time, inventory) is assumed independent of market state during training, so every historical book snapshot can be reused for every private state. Execution is the part of trading where RL has its cleanest evidence.

## Method
Task: sell (or buy) `V` shares within horizon `H`, forced market order for any remainder at the end. State: elapsed time `t` (resolution `T`), remaining inventory `i` (resolution `I`), plus optional discretized market variables. Action: reprice the whole remaining order at `ask - a` (for a sell), where positive `a` crosses the spread. Reward: proceeds measured against the mid price at episode start, in basis points. Learning is backward induction over `t` with a Q-learning-style running-average cost update: `c(x, a) <- n/(n+1) c(x, a) + 1/(n+1) [ c_im(x, a) + best cost at next state ]`. All actions are tried in all states, so the data set is passed `T * I * L` times (`L` actions). Training assumes the agent's orders do not change the subsequent book; testing does not make that assumption and keeps the simulated impact of the agent's own orders. Baseline: "submit and leave", one fixed limit price for the whole horizon, optimized in sample.

## Data and sample
INET (NASDAQ ECN) full limit order data at millisecond resolution, 1.5 years, split into 12 months training and 6 months test. Three stocks: AMZN, NVDA, QCOM. Order sizes 5,000 and 10,000 shares; horizons 2 and 8 minutes. About 45,000 training episodes at the 2-minute horizon. Commissions and exchange fees assumed negligible; no latency.

## Reported results
- With only `t` and `i` as state, cost falls 27.16% to 35.50% relative to submit and leave, depending on `T` and `I`. Finer resolution is strictly better.
- Learned policy shape: price more aggressively as time runs out and as inventory remains.
- Additional cost reduction from adding market variables (averaged over stocks, sizes, horizons): bid-ask spread 7.97%; immediate market order cost 4.26%; signed transaction volume over the last 15 seconds 2.81%; bid-ask volume misbalance 0.13%; spread plus immediate cost 8.69%; spread, immediate cost and signed volume together 12.85%.
- The authors report trying "many others" that did not help, and that total improvement reaches 50% or more over submit and leave.

## Signal construction
Not a directional signal. It is an execution policy: at each decision point (every `H/T`), look up the limit price offset from a table keyed by (time left, inventory left, spread bucket, cost-to-cross bucket, recent signed volume bucket). The table is fit offline by the backward-induction pass over replayed book data, with low/medium/high buckets for each market variable.

## Relevance to SOL perpetuals at minutes to hours
A directional bot still has to enter and exit; this paper says how to decide between resting and crossing. The state design (time left, size left, spread, cost to cross now) is venue-agnostic and small enough to fit from limited Kalshi book history. Two things need re-testing: whether the independence assumption holds on a thin, new book where even small orders are a visible share of depth, and whether top-of-book imbalance, which added almost nothing here, matters more on a venue that follows prices set elsewhere. Fees are not negligible for a retail-scale account and must be put into the reward.

## Caveats
Three liquid US stocks in pre-2006 market structure (exact sample dates not stated in the passages read). Fees and latency ignored. Coarse discretization. The benchmark is a simple one; no comparison with TWAP or VWAP schedules. Authors were at Lehman Brothers.
