---
title: "Reinforcement Learning for Optimized Trade Execution"
authors: "Nevmyvaka, Yuriy; Feng, Yi; Kearns, Michael"
year: 2006
venue: "Proceedings of the 23rd International Conference on Machine Learning (ICML)"
url: "https://www.cis.upenn.edu/~mkearns/papers/rlexec.pdf"
pdf: "sources/27-execution-risk-management/nevmyvaka-2006-reinforcement-learning-optimized-trade-execution.pdf"
access: "full-text"
source_type: "peer-reviewed"
evidence_grade: "B"
topic: "27-execution-risk-management"
asset_class: "equities"
horizon: "minutes"
tags: "reinforcement-learning, optimal-execution, limit-order-placement, q-learning, submit-and-leave"
---

## Key insight
The first large-scale empirical test of reinforcement learning for execution. A simple tabular learner that chooses where to place a limit order, given time remaining and inventory remaining, beats an optimised static "submit and leave" limit order by roughly a third, and adding a few market variables brings the improvement to 50% or more. Most of the gain comes from conditioning on the agent's own state, not from predicting the market.

## Method
Task: sell (or buy) `V` shares within horizon `H`. The horizon is split into `T` decision points and inventory into `I` levels. At each decision the agent cancels its resting order and reposts all remaining shares at `ask - a`, where action `a` can be negative (deep in the book) or positive (crossing). Leftover shares at the end go to market. Cost is measured in basis points against the mid price at the start of the episode.

State: private variables (time left, inventory left) plus optional market variables (spread, bid-ask volume imbalance, signed transaction volume over the last 15 seconds, immediate cost of a market order for the remainder), each discretised to a few values. Learning is a backward-induction form of Q-learning that exploits the assumption that the agent's actions do not change the market variables' evolution, so every historical state can be replayed for every action. Fills are simulated by matching against the recorded order book.

## Data and sample
INET (Nasdaq ECN) full order book data at millisecond resolution, 1.5 years, split into 12 months training and 6 months test. Stocks: AMZN, NVDA, QCOM. Order sizes 5,000 and 10,000 shares; horizons 2 and 8 minutes.

## Reported results
- With private variables only, learned policies beat optimised submit-and-leave in every setting; relative improvement 27.16% to 35.50% depending on `T` and `I`.
- Learned shape is the same across stocks: the less time and the more inventory left, the more aggressive the price.
- Additional cost reduction from market variables (average over settings): spread 7.97%; immediate market-order cost 4.26%; signed transaction volume 2.81%; bid-ask volume imbalance 0.13%; spread plus immediate cost plus signed volume 12.85%.
- Many other candidate variables did not help, which the authors read as evidence of market efficiency.
- Larger spread and lower immediate cost both call for more aggressive pricing.
- Overall: 50% or more over submit-and-leave, and several times better than a market order.

## Signal construction
Not a directional signal; an execution policy. State = (decision points left, fraction of order unfilled, spread bucket, cost-to-cross bucket, signed recent volume bucket). Action = limit price offset from the touch. Reward = negative implementation shortfall including fees. Train by replaying recorded book data, with each episode a parent order of bot size. Re-train as fee tiers or book conditions change.

## Relevance to SOL perpetuals at minutes to hours
The problem maps closely: the bot decides to enter, then has a few minutes to get filled, and on Kalshi the taker fee makes the "go to market at the end" penalty large, which is the regime where learned patience pays. The design choice of a tiny discrete state is attractive given only months of Kalshi history. The replay assumption (own orders do not move the market) is reasonable at $1,000 to $20,000 clips against the depth in the topic 06 snapshot, but simulated passive fills are optimistic, as Albers et al. demonstrate with live orders.

## Caveats
2000s US equities; simulated fills against historical books with no reaction from other traders and no queue-position uncertainty beyond the reconstruction; no exchange fees modelled. Top-of-book imbalance added almost nothing here, in contrast to its role elsewhere, possibly because of coarse discretisation. Results are relative costs, not profitability of any strategy.
