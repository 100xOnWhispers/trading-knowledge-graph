---
title: "Dynamic Multi-Pair Trading Strategy in Cryptocurrency Markets with Deep Reinforcement Learning"
authors: "Lebiedz, Damian; Slepaczuk, Robert"
year: 2026
venue: "arXiv:2606.04574 (v3, 31 October 2026)"
url: "https://arxiv.org/abs/2606.04574"
pdf: "sources/31-rl-evolutionary-second-pass/lebiedz-2026-drl-execution-overlay-crypto-pair-trading.pdf"
access: "full-text"
source_type: "working-paper"
evidence_grade: "B"
topic: "31-rl-evolutionary-second-pass"
asset_class: "crypto"
horizon: "hours"
tags: "reinforcement-learning, head-to-head, perpetual-futures, pair-trading, seed-variance, block-bootstrap, shielding"
---

## Key insight
This is the cleanest head-to-head of an RL policy against a rule on crypto perpetual data in the repository: same pairs, same fees, same leverage, same hard stops, one year held out. The headline agent beat the rule by a wide margin, but that was one seed out of five; another seed lost money, and the block-bootstrap p-value for the difference was about 0.06 before any correction for the number of configurations tried. The design lesson is to confine RL to timing inside fixed, rule-based risk limits.

## Method
- Baseline: monthly pair selection by a "filter then rank" cointegration procedure (Engle-Granger p-value among the criteria), z-score entry and exit thresholds, stop loss, a stop-loss lockout, and forced liquidation at month end. Parameters were chosen on 2024 only, preferring flat regions of the parameter surface over peaks.
- RL overlay: PPO with an LSTM layer decides entries and early exits per pair. Observations exclude capital, margin and leverage. Fixed take-profit, stop loss, time limit and margin-exhaustion liquidation stay outside the policy ("deterministic shielding"). Training is at 1x leverage on 240 pair-month episodes from 2024.
- Frictions: 0.05% fee per execution (0.10% in a stress case), 10x leverage in testing with liquidation when net loss reaches 100% of margin. Funding payments, spreads, impact, partial fills and latency are not simulated; the authors say so.
- Statistics: five training seeds (0, 1, 42, 100, 999); stationary circular block bootstrap, 10,000 draws, 168-hour blocks.

## Data and sample
Binance USD-M futures, one-hour bars. In-sample 2024, out-of-sample 2025 (8,760 bars per asset; 20 pairs times 12 months). Delisted assets are kept and force-closed at the last quote.

## Reported results
- Reported agent (seed 42): Sortino ratio 3.2494 against 0.5360 for the rule; win rate 73.18% against 60.23%; maximum drawdown 35.27% against 34.13%; CAGR 199.45%.
- Across five seeds: mean CAGR 64.36% with standard deviation 69.91%; mean Sortino 1.0958; worst seed CAGR -3.00%. Baseline CAGR 30.40%.
- Bootstrap p-values for the seed-42 agent beating the baseline: 0.0603 (Sharpe) and 0.0593 (Sortino); both 95% intervals include zero. The authors note the tests were not corrected for multiple configurations (the paper refers to at least 18 agent variants).

## Signal construction
Not a signal. Pattern for the bot: keep entries eligible only when a rule fires or inside rule-defined bounds, let a learned policy choose timing and early exit, and keep stops, time limits and liquidation logic deterministic. Evaluate against the rule alone with identical costs, several seeds and a block bootstrap on the return difference.

## Relevance to SOL perpetuals at minutes to hours
Directly comparable instrument class and bar size. The seed dispersion (CAGR from -3% to 199% for one configuration) sets expectations for any learned SOL policy: report the mean and worst seed, not the best. Pair trading is market-neutral, so the result does not show directional skill.

## Caveats
One out-of-sample year. No funding in a strategy that holds perps for days at 10x leverage, which is a material omission. Fee-only costs at hourly bars ignore spread on less liquid pairs. The selected configuration was chosen after seeing 2025 results for several variants. Working paper, not peer reviewed.
