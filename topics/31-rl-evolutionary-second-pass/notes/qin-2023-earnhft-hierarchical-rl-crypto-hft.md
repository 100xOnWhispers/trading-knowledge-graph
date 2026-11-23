---
title: "EarnHFT: Efficient Hierarchical Reinforcement Learning for High Frequency Trading"
authors: "Qin, Molei; Sun, Shuo; Zhang, Wentao; Xia, Haochong; Wang, Xinrun; An, Bo"
year: 2023
venue: "arXiv:2309.12891 (the PDF carries a 2024 AAAI copyright line)"
url: "https://arxiv.org/abs/2309.12891"
pdf: "sources/31-rl-evolutionary-second-pass/qin-2023-earnhft-hierarchical-rl-crypto-hft.pdf"
access: "full-text"
source_type: "peer-reviewed"
evidence_grade: "B"
topic: "31-rl-evolutionary-second-pass"
asset_class: "crypto"
horizon: "seconds"
tags: "reinforcement-learning, hierarchical-rl, crypto, order-book, q-teacher, imitation, regime-routing"
---

## Key insight
A three-stage design makes second-level RL trainable on crypto: supervise the agent with the hindsight-optimal action value, train many agents biased toward different market trends, then let a minute-level router pick one agent per minute. On four Binance spot pairs it was the only method with a positive return on all four nine-day test windows. The more durable finding is in the baseline rows: PPO, DQN and two other RL agents lost money on most pairs at a 0.02% fee.

## Method
- Stage I, "Q-teacher". Because a small trader is treated as a price taker, the optimal action value on historical data can be computed by dynamic programming over future prices. The DDQN loss adds a term pulling the learned Q toward this optimal Q. This is imitation of a hindsight oracle, used as a regularizer.
- Stage II, agent pool. Training data are cut into chunks; chunks are sampled with priority proportional to `exp(beta * r)`, where `r` is the chunk's buy-and-hold return, with `beta` in {-90, -10, 30, 100}. 50 epochs per `beta` give 200 agents. A labelling routine (denoise, split at extrema, merge by DTW and slope) assigns each validation segment a trend label, and a small fraction of agents is kept for the pool according to profitability under each label.
- Stage III, router. A minute-level DDQN chooses which second-level agent trades for the next minute.
- Environment: market orders walk the recorded book level by level; position is long or flat only (`P_t >= 0`).

## Data and sample
Binance second-level data with order book snapshots for BTC/TUSD (2023-03-30 to 2023-05-15), BTC/USDT (2022-09-01 to 2022-10-15), ETH/USDT (2022-05-01 to 2022-06-15) and GALA/USDT (2022-07-01 to 2022-08-15), about 3.9 to 4.1 million seconds each. Last 9 days test, previous 9 days validation, rest training.

## Reported results
- Total return on the test window: EarnHFT 0.72% (BTC/USDT), 4.52% (ETH), 0.99% (BTC/TUSD), 19.41% (GALA).
- Baselines on BTC/USDT: DRA -4.56%, PPO -3.61%, CDQNRP -2.83%, DQN -3.48%, MACD -6.07%, order-imbalance rule -2.99%. On ETH: DRA -33.37%, PPO -22.61%, DQN -11.02%, imbalance rule -27.42%.
- On BTC/TUSD (zero fee) plain DQN had a higher Sharpe ratio (4.21 against 1.34) with a 0.66% drawdown.
- The authors state that policy-gradient baselines "converge to a dummy policy" of never changing position because of the fee, and that EarnHFT is "a very radical trader" that ignores risk.
- Fee: 0.02% in the main text (0 for BTC/TUSD); an appendix table lists 0.015%. No seed count or dispersion is reported.

## Signal construction
Not a signal. Two reusable components: (1) the hindsight-optimal Q on replayed data as an auxiliary training target, valid only while the bot's orders do not move the book; (2) trend-conditioned sampling of training chunks to build specialist policies, selected on a labelled validation set.

## Relevance to SOL perpetuals at minutes to hours
The Q-teacher is cheap to compute for a bar-level SOL policy with fee, spread and funding in the transition, and it removes most exploration. The long-only action set does not transfer; a perp bot needs shorts and funding in the dynamic program. Nine-day tests say nothing about hours-scale holding.

## Caveats
One run per method, one nine-day window per asset, no buy-and-hold row, no confidence intervals. The fee is the lowest retail tier and spread is paid only through the level walk. In a later paper from the same group (see [qin-2025-fineft](qin-2025-fineft-ensemble-rl-crypto-futures.md)) EarnHFT lost 69% on BNB futures at 5x leverage over a six-month test, so the result is regime-dependent. Selecting agents on validation labels is itself a search whose trial count (200 agents) is not corrected for.
