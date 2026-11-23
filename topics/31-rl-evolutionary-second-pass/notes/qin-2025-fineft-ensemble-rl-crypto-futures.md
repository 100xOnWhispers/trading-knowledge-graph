---
title: "FineFT: Efficient and Risk-Aware Ensemble Reinforcement Learning for Futures Trading"
authors: "Qin, Molei; Cai, Xinyu; Li, Yewen; Xia, Haochong; Zong, Chuqiao; Sun, Shuo; Wang, Xinrun; An, Bo"
year: 2025
venue: "arXiv:2512.23773; KDD 2026 (per the PDF header)"
url: "https://arxiv.org/abs/2512.23773"
pdf: "sources/31-rl-evolutionary-second-pass/qin-2025-fineft-ensemble-rl-crypto-futures.pdf"
access: "full-text"
source_type: "peer-reviewed"
evidence_grade: "B"
topic: "31-rl-evolutionary-second-pass"
asset_class: "crypto"
horizon: "minutes"
tags: "reinforcement-learning, perpetual-futures, leverage, funding, liquidation, ensemble, out-of-distribution, environment"
---

## Key insight
Among the RL sources read for topics 24 and 31, this is the only one whose training environment models crypto perpetual mechanics end to end: leverage, margin, funding payments, level-by-level slippage and forced liquidation. (The paper is also noted in topics 03, 04 and 14 for its funding-countdown feature and liquidation handling; this note covers the environment and the head-to-head table.) Under 5x leverage most published agents, including two earlier state-of-the-art methods from the same group, lost more than half their capital on at least one of four assets over a six-month test. The method that survived did so mainly by switching to a conservative policy when recent market states looked unlike anything seen in validation.

## Method
- Stage I: an ensemble of Q-learners in which only the learner with the smallest temporal-difference error on a sample is updated, so learners specialize in different market dynamics.
- Stage II: learners are filtered by profitability per labelled market dynamic on the validation set; a variational autoencoder is fitted to the state representations of each dynamic.
- Stage III: at trade time, each VAE scores recent states; scores pass through an empirical CDF and an exponential moving average. If the best score is below a threshold `tau`, the agent uses a conservative policy; otherwise it uses the learner for that dynamic.
- Environment (appendix): actions are target positions from a leverage pool (the environment supports up to 125x); market orders walk the book; funding fee `rate x position value` is deducted from cash; when margin balance falls below maintenance margin the position is liquidated and the episode ends.

## Data and sample
Binance USDT-margined futures for BNB, BTC, DOT and ETH, 2022-01-01 to 2024-01-01, 210,241 steps per asset (five-minute spacing by my arithmetic; the text says "minute-level"). One year training, six months validation, last six months test. Transaction cost 0.02%, leverage 5x.

## Reported results
- FineFT total return and maximum drawdown: BNB 83.70% / 15.49%, BTC 76.90% / 23.51%, DOT 18.39% / 21.87%, ETH 39.05% / 16.96%.
- MacroHFT (noted in topic 24): BNB -50.42%, BTC -25.85%, DOT +220.44%, ETH -75.16%.
- EarnHFT: BNB -69.32%, BTC +33.44%, DOT +89.00%, ETH +48.72%.
- DQN: -55.85%, -82.13%, -64.89%, -73.15%. PPO: -59.58%, +19.68%, -65.65%, -46.08%.
- MACD rule: -82.85%, -26.28%, +26.07%, -73.93%. Order-imbalance rule: -71.00%, -17.26%, -66.24%, -50.53%.
- Baseline drawdowns are mostly 58% to 89%.
- The authors claim risk reduced "by more than 40%" against the runner-up. No seed count or dispersion appears in the parts read.

## Signal construction
Not a signal. Reusable pieces: (1) the per-step perp accounting (mark-to-market P&L, fee, funding at settlement, margin check, terminal liquidation); (2) an "am I in familiar territory" gate: fit a density model to the feature vectors of each validated regime, and go flat or conservative when the recent smoothed likelihood rank falls below a threshold.

## Relevance to SOL perpetuals at minutes to hours
The environment specification maps directly onto a Kalshi SOL perp simulator; only fee, funding interval, leverage cap and maintenance margin change. With Kalshi's low leverage the liquidation term matters less, but the test shows how quickly directional agents fail once leverage multiplies drawdown. The novelty gate is independent of RL and can wrap any model.

## Caveats
Single test window (second half of 2023), apparently one run per method, and the proposed method's thresholds were tuned on validation data adjacent to the test. Baselines were run with FineFT's hyperparameters "if included", which may disadvantage them. Fee of 0.02% is below typical taker rates. Rule baselines are long/short technical rules, not a volatility-matched buy-and-hold. The simulator replays history, so self-impact beyond the visible book is absent.
