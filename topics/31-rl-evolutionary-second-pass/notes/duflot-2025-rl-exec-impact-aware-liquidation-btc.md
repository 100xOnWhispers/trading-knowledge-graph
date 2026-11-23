---
title: "RL-Exec: Impact-Aware Reinforcement Learning for Opportunistic Optimal Liquidation, Outperforms TWAP and a Book-Liquidity VWAP on BTC-USD Replays"
authors: "Duflot, Enzo; Robineau, Stanislas"
year: 2025
venue: "arXiv:2511.07434"
url: "https://arxiv.org/abs/2511.07434"
pdf: "sources/31-rl-evolutionary-second-pass/duflot-2025-rl-exec-impact-aware-liquidation-btc.pdf"
access: "full-text"
source_type: "working-paper"
evidence_grade: "B"
topic: "31-rl-evolutionary-second-pass"
asset_class: "crypto"
horizon: "minutes"
tags: "reinforcement-learning, execution, ppo, market-impact, twap, bitcoin, replay-simulator, statistical-testing"
---

## Key insight
A PPO agent selling BTC over 30 to 120 minutes beat TWAP and a depth-weighted schedule by 2 to 23 basis points on one out-of-sample month, in a replay simulator that adds transient impact, partial fills, fees and latency. The paper's main value for this repository is its evaluation protocol: paired comparison on identical windows and costs, the day as the unit of inference, multiplicity correction and bootstrap intervals. It is the opposite sign to the negative BTC execution result in topic 24, and the difference is the environment specification.

## Method
- Environment: historical one-second book snapshots are replayed; the agent's own sells add a parametric transient impact that decays with a resilience half-life; fills can be partial; maker and taker fees and latency apply.
- Agent: PPO; observations are depth-20 book features plus microstructure indicators (imbalance, short-horizon returns and volatility) and state variables (time to go, inventory). Action is the fraction of remaining inventory to execute. Reward is implementation shortfall with a penalty for leftover inventory.
- Evaluation: for each test day, 10 start times are run and averaged into one daily score. RL minus baseline daily differences are tested with a one-sided Wilcoxon signed-rank test, Benjamini-Hochberg correction across horizons, and 10,000-draw bootstrap confidence intervals.
- Baselines: TWAP, and a "VWAP-like" schedule weighting by opposite-side displayed depth over the top 20 levels.

## Data and sample
BTC-USD order book at one-second resolution, 20 levels per side. Training January 2020 (31 days), test February 2020 (27 usable days). The data came from the Sadighian crypto market-making project.

## Reported results
Mean daily gap, RL minus baseline, in basis points with 95% bootstrap interval:
- 1,800 s: +2.25 [+0.95, +3.60] against TWAP; +2.68 [+1.36, +4.05] against the depth-weighted schedule; win rate 67% to 70% of days.
- 3,600 s: +7.59 [+4.71, +10.74] and +7.70 [+4.88, +10.84]; win rate 85% to 89%.
- 7,200 s: +22.96 [+18.04, +28.35] and +23.02 [+18.05, +28.49]; win rate 96%.
- A sensitivity run halving and doubling the impact half-life and coefficient kept the 3,600 s and 7,200 s results significant.

## Signal construction
Not a signal. For the bot: an execution policy template (state: time left, inventory left, top-of-book features; action: fraction to send now) and a test protocol for any execution change: same timestamps and cost model for candidate and baseline, aggregate to days, paired non-parametric test, correct across horizons.

## Relevance to SOL perpetuals at minutes to hours
The bot's orders will be small against Binance depth but possibly not against Kalshi depth, so an impact-aware replay is the right kind of simulator for Kalshi entries and exits. The gain grows with the execution window, which is consistent with the agent timing the market over one or two hours; for a directional bot that already has a view, that timing overlaps with the signal itself.

## Caveats
One asset, sell-only, one test month that follows the training month, PPO only, and the paper does not report dispersion across training seeds. The impact model is parametric and was not calibrated to live fills, and the agent may be exploiting the simulator's own resilience rule. The parts read do not report the price path over the test month, and the gain of a sell-only agent from delaying depends on it, so the result is not regime-neutral. The VWAP comparator is not a traded-volume VWAP.
