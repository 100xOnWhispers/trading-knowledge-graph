---
title: "JAX-LOB: A GPU-Accelerated limit order book simulator to unlock large scale reinforcement learning for trading"
authors: "Frey, Sascha; Li, Kang; Nagy, Peer; Sapora, Silvia; Lu, Chris; Zohren, Stefan; Foerster, Jakob; Calinescu, Anisoara"
year: 2023
venue: "arXiv:2308.13289"
url: "https://arxiv.org/abs/2308.13289"
pdf: "sources/31-rl-evolutionary-second-pass/frey-2023-jax-lob-gpu-limit-order-book-simulator.pdf"
access: "full-text"
source_type: "working-paper"
evidence_grade: "C"
topic: "31-rl-evolutionary-second-pass"
asset_class: "equities"
horizon: "tick"
tags: "simulator, limit-order-book, jax, gpu, reinforcement-learning, execution, market-replay"
---

## Key insight
A limit order book matching engine written in JAX can run thousands of independent books in parallel on one GPU, so an RL agent's own orders can be matched against replayed message data at scale. The paper reports a speed-up of at least 7 times in RL training against a comparable CPU simulator. It makes no claim that an agent trained this way trades well: the authors say outright that they cannot judge their example agent without out-of-sample tests.

## Method
- The book is stored as fixed-size arrays (JAX requires static shapes), not a tree; orders are not kept sorted and the best price is found on demand.
- Messages follow the LOBSTER structure: limit orders, cancellations and market orders, each with price, quantity, order id, trader id and time. Matching is price-time priority. Processing within a book is serial; parallelism comes from `vmap` over many books.
- The simulator is wrapped as a `gymnax` environment. In each step a block of historical messages (100 in the benchmark) is processed together with the agent's orders, so the agent's orders consume real resting liquidity and can rest in the queue. This is replay with direct impact only: the historical flow does not react to the agent.
- Example task: optimal execution with a recurrent PPO agent, continuous action space, 30-minute episodes, 1,000 parallel environments, 10 book levels as input.

## Data and sample
LOBSTER message and book data for AMZN, April 2021. The RL example trains on one day (1 April 2021). Speed tests use an Nvidia 2080 Ti or A40 GPU against a single CPU core or a 32-core CPU with serial collection.

## Reported results
- RL training throughput 550 steps per second against 74 for the CPU equivalent on the same hardware ("at least 7x").
- At least 5 times speed-up for the simulator alone in the configuration the authors summarize in their conclusion.
- The execution agent's training curve passes TWAP in training; the authors write that they "cannot make any claims on the success of this agent without conducting complete out-of-sample tests".
- The related-work section records that an earlier agent trained in an ABIDES-based replay "converges to a TWAP strategy".

## Signal construction
Not a signal. It is infrastructure for training or testing order-placement logic against message-level data with queue position and partial fills.

## Relevance to SOL perpetuals at minutes to hours
Useful only if the bot's execution layer needs queue-aware testing and message-level (market-by-order) data exist for the venue. Crypto venues mostly publish aggregated book updates and trades, not order ids, so a faithful port needs an inferred message stream. For a directional decision every few minutes, bar-level replay with a spread-and-fee cost is adequate; this tool addresses the execution problem.

## Caveats
Equity data, one stock, one training day, no trading result. Each side has a fixed capacity of `N` orders that the user must set large enough that the book never saturates. Replay cannot show how other participants would respond to the agent (see [balch-2019](balch-2019-market-replay-versus-interactive-simulation.md)). A follow-up from the same group, JaxMARL-HFT (arXiv:2511.02136, abstract read only), extends this to multi-agent training on a year of order data and reports up to 240 times shorter training time; it was not noted separately.
