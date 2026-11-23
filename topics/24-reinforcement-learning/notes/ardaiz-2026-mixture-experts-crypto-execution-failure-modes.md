---
title: "Mixture-of-Experts for Cryptocurrency Order Execution: Training Stability, Tail Risk, and Failure Modes"
authors: "Ardaiz, Alexander; Budati, Varun; Habibnia, Ali"
year: 2026
venue: "arXiv:2610.03369v2"
url: "https://arxiv.org/pdf/2610.03369"
pdf: "sources/24-reinforcement-learning/ardaiz-2026-mixture-experts-crypto-execution-failure-modes.pdf"
access: "full-text"
source_type: "working-paper"
evidence_grade: "B"
topic: "24-reinforcement-learning"
asset_class: "crypto"
horizon: "minutes"
tags: "execution, ddqn, mixture-of-experts, seed-variance, policy-collapse, negative-result, implementation-shortfall, twap, btc, exploration-schedule"
---

## Key insight
A carefully reported negative result for deep RL execution on crypto. Across 100 independently trained runs per configuration, no learned policy (double deep Q-learning, mixtures of DDQL experts, or parameter-matched dense networks) beat TWAP or immediate liquidation on BTC/USDT, and about one in nine plain DDQL runs collapsed into never trading until forced liquidation. Small changes to the training specification (exploration annealing, reward alignment) flipped collapse rates from 12% to 0% and back up to 48%, and conclusions drawn from 30 seeds changed at 100. Architectural "improvements" in RL trading papers are often training-luck artifacts.

## Method
Task: sell-side execution of a parent order over an episode, scored by implementation shortfall (IS) in basis points. Agents: vanilla DDQL (five-layer fully connected network); mixture of experts (MoE) with K in {2, 4, 8} DDQL experts and a K-means router on episode-level features; dense networks matched in parameter count to K = 4 and K = 8. Each configuration is trained in 100 independent runs (300 warm-up, 2,500 training and 500 evaluation episodes per run) and evaluated on a common set of 500 out-of-sample episodes. Baselines: TWAP and immediate liquidation on the same episodes. Statistics: confidence intervals on mean differences, exact tests on collapse counts, per-run CVaR-95. A further decomposition varies exploration annealing, reward alignment and replay retention.

## Data and sample
Binance BTC/USDT limit order book, 10 levels per side, sourced from Kaggle, 9 to 20 January 2023. Training window 9 to 14 January; evaluation window 16 to 20 January; the days between are held out. Snapshots are mean-aggregated to five-minute bars. Replay is frictionless: the agent's trades do not affect later prices or books, and only the bid side is modeled.

## Reported results
- MoE (K = 8) versus DDQL mean IS difference: -0.03 bps, 95% CI [-0.15, +0.09]; equivalence not established.
- Baselines beat every learned configuration under the specification as reported: TWAP 0.39 bps mean IS, immediate liquidation 0.21 bps.
- Complete-run collapse (inactive before forced liquidation in all 500 evaluation episodes): 11 of 100 DDQL runs; none for MoE at K = 4 or K = 8 (Fisher p = 0.0007 each).
- Estimated per-episode inactivity rises from 11.1% (DDQL) to 24.9% (K = 8).
- Annealed exploration alone cuts DDQL collapse from 12/100 to 0/100; adding the aligned reward restores collapse in 19 of 30 runs; all three changes together give 48/100.
- Tail risk worsens with K: per-run CVaR-95 at K = 8 is +11.5 bps versus DDQL, 95% CI [+3.7, +19.7].
- Across-seed dispersion is lowest at K = 8 (0.37 versus 0.50 bps) but does not survive family-wise adjustment.

## Signal construction
Not a signal. Protocol to copy when evaluating any learned execution or trading policy:
1. Always include TWAP and immediate execution (for a directional bot: cross now) on identical episodes and costs.
2. Train on the order of 100 seeds; report the distribution, collapse rate and tail (CVaR) per seed, not the mean of a few.
3. Check for degenerate policies explicitly (never trades, always trades at once).
4. Treat exploration schedule and reward shaping as first-order experimental factors.

## Relevance to SOL perpetuals at minutes to hours
Same asset class, same five-minute bar size, same algorithm family most open-source stacks default to. It says the default expectation for a DQN-style execution layer on crypto is no improvement over a schedule, with a material chance of a degenerate policy. For the bot, start with a rule (cross when the signal is fresh, otherwise rest with a timeout) and require any learned replacement to beat it across seeds.

## Caveats
Twelve days of data and a five-day test window in a single regime. Frictionless replay on time-averaged five-minute books makes early liquidation nearly costless, as the authors note, which favors the simple baselines; the result is about this specification, not a proof that RL cannot help with real impact. Kaggle-sourced data. Some inactivity figures come from a proxy. Preprint, October 2026.
