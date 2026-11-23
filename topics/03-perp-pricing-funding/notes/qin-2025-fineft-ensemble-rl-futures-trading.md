---
title: "FineFT: Efficient and Risk-Aware Ensemble Reinforcement Learning for Futures Trading"
authors: "Qin, Molei; Cai, Xinyu; Li, Yewen; Xia, Haochong; Zong, Chuqiao; Sun, Shuo; Wang, Xinrun; An, Bo"
year: 2025
venue: "arXiv working paper 2512.23773; the PDF header carries a KDD 2026 conference line (acceptance not independently confirmed)"
url: "https://arxiv.org/pdf/2512.23773"
pdf: "sources/03-perp-pricing-funding/qin-2025-fineft-ensemble-rl-futures-trading.pdf"
access: "full-text"
source_type: "working-paper"
evidence_grade: "B"
topic: "03-perp-pricing-funding"
asset_class: "crypto"
horizon: "minutes"
tags: "reinforcement-learning, ensemble-q-learning, funding-countdown, funding-fee, leverage, risk-management"
---

## Key insight
A reinforcement-learning system for leveraged crypto perps treats funding in two ways: as a cash cost inside a high-fidelity simulator, and as a clock, by feeding the time remaining to the next funding settlement into the agent's state. The authors justify the clock feature by the periodic behaviour that funding-driven traders create. The paper does not isolate how much the funding inputs contribute.

## Method
Three stages. (1) An ensemble of Q-learners, selectively updated using temporal-difference errors across learners to stabilise training under 5x leverage. (2) Learners are filtered by profitability in each market regime and a variational autoencoder is trained per regime on market states to mark what each learner has seen. (3) At run time a router picks a learner, or a conservative fallback policy when recent states look unfamiliar to every autoencoder. The state has three parts: about 300 technical-indicator features, the current position, and a "funding count down" encoded as hours and minutes to the next settlement. The simulator charges commissions, slippage and funding on the nominal position at each settlement.

## Data and sample
BNB, BTC, DOT and ETH USDT perps, 2022-01-01 to 2024-01-01, 210,241 steps per asset (described as minute-level; the step count matches 5-minute bars). Split: first year training, next six months validation, last six months test. Leverage 5x.

## Reported results
- Against 12 baselines on six metrics, the method has the lowest risk on all four assets, the best risk-adjusted return on three and the highest return on two.
- The abstract states a risk reduction of more than 40% relative to the runner-up.
- Policy-gradient baselines failed to beat a constant-rebalanced portfolio; rule-based baselines were very sensitive to hyperparameters chosen on validation.
- The ablation studies concern the framework's own components. No ablation of the funding countdown or funding fee was found in the parts read.

## Signal construction
The reusable piece is the feature: `minutes_to_next_funding` (and its hour component), recomputed every bar from the venue's funding schedule, concatenated with position and market features. On venues with variable intervals the schedule itself must be tracked (see [Binance specification](binance-2026-funding-rate-specification.md)). Pair it with the predicted funding rate, which this paper does not appear to include as a separate input.

## Relevance to SOL perpetuals at minutes to hours
The horizon and instrument type match the target bot, and the design choice lines up with the measured funding-cycle U-shape in [Ruan and Streltsov](ruan-2024-perpetual-futures-market-quality.md). SOL is not in the test set. A sensible experiment is an ablation the paper omits: train with and without the countdown and predicted-funding features and compare out-of-sample.

## Caveats
Six-month test window per asset, single split, four assets; results for learned policies of this kind are known to be fragile to the split. Funding's contribution is asserted, not measured. Much of the paper concerns ensemble RL mechanics that belong to a machine-learning topic, so this note covers only the funding-related design.
