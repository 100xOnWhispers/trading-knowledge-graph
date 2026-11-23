---
title: "Pretrained LLM Adapted with LoRA as a Decision Transformer for Offline RL in Quantitative Trading"
authors: "Yun, Suyeol"
year: 2024
venue: "ICAIF 2024 Workshop on LLM and GenAI for Finance; arXiv:2411.17900"
url: "https://arxiv.org/abs/2411.17900"
pdf: "sources/31-rl-evolutionary-second-pass/yun-2024-decision-transformer-offline-rl-trading.pdf"
access: "full-text"
source_type: "working-paper"
evidence_grade: "C"
topic: "31-rl-evolutionary-second-pass"
asset_class: "equities"
horizon: "daily"
tags: "offline-rl, decision-transformer, behavior-cloning, cql, iql, imitation, single-history"
---

## Key insight
Offline RL methods (decision transformer, conservative Q-learning, implicit Q-learning, behavior cloning) can reproduce the test-period performance of an online RL "expert" from its logged trajectories. No offline method is consistently best, and behavior cloning is often as good as the rest. The experiment does not address the single-history problem: the experts were themselves trained on the one historical path, so the offline learners imitate a policy fitted to that path.

## Method
- Five online agents (A2C, DDPG, PPO, TD3, SAC) are trained in the FinRL Dow Jones environment and their trajectories of states, actions and rewards are logged.
- Offline learners are trained on each expert's trajectories: a decision transformer built on GPT-2 with low-rank adaptation (LoRA), the same architecture with random initial weights, CQL, IQL and behavior cloning.
- A decision transformer models a sequence of (return-to-go, state, action) tokens over a window of `K` steps and predicts the next action by minimizing mean squared error against the logged action. At test time the desired return is supplied as a conditioning input.
- Five random seeds per offline method (20742, 55230, 85125, 96921, 67851); results are mean plus or minus standard deviation.

## Data and sample
29 Dow Jones Industrial Average constituents, daily. Expert training 2009-01-01 to 2020-07-01 (about 2,892 trading days); evaluation 2020-07-01 to 2021-10-29 (about 335 trading days).

## Reported results
Cumulative return, test period, by expert whose data was used:
- A2C expert 34.69%: CQL 48.00 +/- 3.75, DT with GPT-2 43.72 +/- 2.04, IQL 40.26 +/- 3.24, BC 40.10 +/- 1.22.
- DDPG expert 48.44%: CQL 48.71, BC 48.49 +/- 0.26, DT with GPT-2 47.98 +/- 1.35, IQL 40.46 +/- 2.12.
- PPO expert 46.09%: IQL 47.30 +/- 4.84, CQL 45.57 +/- 1.87, DT with GPT-2 34.99 +/- 8.03, BC 31.21 +/- 5.44.
- TD3 expert 46.69%: DT with GPT-2 46.62 +/- 0.58, CQL 45.05, BC 43.22 +/- 0.12.
- SAC expert 47.34%: DT with GPT-2 39.59 +/- 3.18, BC 35.10 +/- 1.61, CQL 35.07 +/- 1.20, IQL 31.07 +/- 3.41.
- Pre-trained GPT-2 weights beat random initialization in every expert setting on cumulative return (for example 43.72 against 38.66 under A2C).

## Signal construction
Not a signal. Use: if the bot ever has logs from a rule-based or supervised policy running live on Kalshi, behavior cloning or a decision transformer can compress that behavior into one model, and return conditioning gives a dial for aggressiveness. That is imitation of an existing policy, not discovery of a better one.

## Relevance to SOL perpetuals at minutes to hours
Limited. The evidence is daily, long-only, multi-stock, in a rising market. The transferable point is negative: offline RL on market data inherits whatever the data-generating policy learned, and with price-taker replay a "logged dataset" adds no information beyond the price history. The 8-point standard deviation across seeds for one setting (PPO expert) on a 335-day test shows how noisy such comparisons are.

## Caveats
One test window in a bull market; no buy-and-hold row in the table read; transaction-cost settings are those of the FinRL environment and were not confirmed here. Expert returns show zero variance because each expert is a single trained model. Sole-author workshop paper. Whether the offline learners exceed the expert because of regularization or luck cannot be told from five seeds on one path.
