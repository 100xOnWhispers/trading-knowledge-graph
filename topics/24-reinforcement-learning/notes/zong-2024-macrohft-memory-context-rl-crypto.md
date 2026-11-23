---
title: "MacroHFT: Memory Augmented Context-aware Reinforcement Learning On High Frequency Trading"
authors: "Zong, Chuqiao; Wang, Chaojie; Qin, Molei; Feng, Lei; Wang, Xinrun; An, Bo"
year: 2024
venue: "arXiv:2406.14537v1 (KDD 2024)"
url: "https://arxiv.org/pdf/2406.14537"
pdf: "sources/24-reinforcement-learning/zong-2024-macrohft-memory-context-rl-crypto.pdf"
access: "full-text"
source_type: "peer-reviewed"
evidence_grade: "B"
topic: "24-reinforcement-learning"
asset_class: "crypto"
horizon: "minutes"
tags: "hierarchical-rl, ddqn, regime-conditioning, minute-level, binance, market-decomposition, episodic-memory, long-only, baselines-fail"
---

## Key insight
The current state of the art in the academic "RL for minute-level crypto" line trains a set of regime-specialized DDQN sub-agents and a hyper-agent that blends them, with an episodic memory to react to sudden moves. It reports positive returns on four coins in a 2023 test window. The more informative result for this project is in the baseline rows: standard DQN, DDQN, PPO and a prior hierarchical method mostly lost money on the same data at a 0.02% fee, which is the paper's own evidence that off-the-shelf deep RL does not work on one-minute crypto bars.

## Method
Single-asset, long-only: the action is a target position in {0, 1}; orders are market orders of a fixed size. Reward is the change in net value between steps after a transaction cost. State combines features from a 5-level order book snapshot and OHLCV, technical indicators over a 60-step window, and the current position.

Phase 1, market decomposition: training data are cut into chunks (length chosen per dataset from 360 or 4,320 minutes, that is 6 hours or 3 days). Each chunk gets a trend label (slope of a linear fit to the smoothed price) and a volatility label, each split at quantiles into three classes. A separate DDQN sub-agent is trained on each class, with a conditional adapter that injects context and position, and with supervision from an optimal action value computed by dynamic programming on the training data.

Phase 2: a hyper-agent outputs softmax weights that mix the six sub-agents' Q-values into a meta-policy. Its loss adds a term pulling Q toward a value retrieved from an episodic memory of similar past states. Hyperparameters are chosen on the validation set per dataset.

## Data and sample
BTCUSDT, ETHUSDT, DOTUSDT and LTCUSDT at one-minute frequency with 5-level order book data; fees follow Binance (whether the data are spot or futures was not confirmed in the passages read; the strategy is long-only). Train roughly February or March 2022 to early 2023; validation February or March to May or June 2023; test 2023-06-01 to 2023-10-31 (BTC: 2023-06-22 to 2023-10-15). Commission 0.02% per trade.

## Reported results
Test-period total return (TR) and annualized Sharpe ratio (ASR), Table 1:
- MacroHFT: BTC 3.03% (ASR 0.61), ETH 39.28% (3.89), DOT 13.79% (0.97), LTC 18.16% (1.50).
- On BTC every baseline lost money: DQN -10.41%, DDQN -9.14%, PPO -9.15%, CLSTM-PPO -10.67%, EarnHFT -11.16%, MACD rule -18.99%, order-imbalance rule (IV) -9.24%.
- On ETH, EarnHFT made 18.02%; DQN, DDQN and PPO were negative. On DOT and LTC the simple order-imbalance rule (10.58% and 7.75%) beat every RL baseline.
- MacroHFT made about 19 to 20 trades on BTC and ETH over the test window; some baselines made several hundred.
- Ablation (Table 3): removing the conditional adapter or the memory lowers return on all four datasets (for example LTC -6.71% without the adapter and -8.66% without the memory, against 18.16%).

## Signal construction
Not a single signal. The reusable recipe: label rolling windows by trend slope and realized volatility terciles; train one policy per regime; blend their action values with weights from a top-level model that sees the same regime features.

## Relevance to SOL perpetuals at minutes to hours
Matching horizon and asset class, but long-only: no shorting, funding or leverage, so half of a perp strategy's action space is untested. The regime-decomposition idea is testable on SOL without the full architecture. The low trade count means the strategy in effect holds for days; its "minute-level" label describes decision frequency, not holding period.

## Caveats
One test window of about four to five months per coin; with roughly 20 trades, the Sharpe ratios have very wide error bands. No seed variance or confidence intervals reported in the passages read. Chunk length and loss weights are tuned per coin on validation data. Fill at close price with a 0.02% fee and no spread or slippage. The benchmark set omits buy and hold. Same group as the EarnHFT baseline.
