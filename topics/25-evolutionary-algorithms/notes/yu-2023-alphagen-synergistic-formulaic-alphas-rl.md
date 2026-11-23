---
title: "Generating Synergistic Formulaic Alpha Collections via Reinforcement Learning"
authors: "Yu, Shuo; Xue, Hongyan; Ao, Xiang; Pan, Feiyang; He, Jia; Tu, Dandan; He, Qing"
year: 2023
venue: "KDD 2023 (read: arXiv 2306.12964v1)"
url: "https://arxiv.org/pdf/2306.12964"
pdf: "sources/25-evolutionary-algorithms/yu-2023-alphagen-synergistic-formulaic-alphas-rl.pdf"
access: "full-text"
source_type: "peer-reviewed"
evidence_grade: "B"
topic: "25-evolutionary-algorithms"
asset_class: "equities"
horizon: "multi-day"
tags: "alphagen, formulaic-alpha, reinforcement-learning, alpha-pool, combination-model, gplearn-baseline"
---

## Key insight
AlphaGen changes the objective of alpha mining. Earlier miners scored each formula alone and filtered near-duplicates afterwards; AlphaGen rewards a new formula by how much it improves the combined signal of the pool it joins. With that objective a reinforcement-learning generator beat genetic programming out of sample on Chinese stocks, and the paper shows that the usual "drop anything correlated above 0.7" filter can discard formulas that help the combination.

## Method
A formula is written as a token sequence in reverse Polish notation over six raw fields (`open, close, high, low, volume, vwap`), constants, time windows and operators. A policy network (LSTM encoder, trained with PPO) emits one token at a time; an action mask allows only tokens that keep the expression well formed. When a formula is complete it is added to a pool, the linear combination weights of the pool are refit by gradient descent on mean squared error against the target, the weakest member is dropped if the pool is over size, and the reward is the IC of the combined signal. The generator therefore learns to propose formulas that add something to what is already held.

## Data and sample
Chinese A-shares, CSI 300 and CSI 500 constituents, daily. Target: 20-day forward return. Training 2009 to 2018, validation 2019, test 2020 to 2021. Ten random seeds per method. Baselines: `gplearn` genetic programming and single-formula PPO, each with top-k and correlation-filtered pools; XGBoost, LightGBM and MLP on 60 days of raw features.

## Reported results
Test-set IC of the combined signal, mean (standard deviation over 10 seeds):
- CSI 300: AlphaGen 0.0725 (0.0105); GP with correlation filter 0.0183 (0.0190); GP top-k 0.0078 (0.0218); XGBoost 0.0404; LightGBM 0.0259.
- CSI 500: AlphaGen 0.0438 (0.0064); GP filter 0.0117 (0.0083); GP top-k 0.0200 (0.0112); XGBoost 0.0353.
- Combination IC keeps rising with pool size for AlphaGen and barely moves for the baselines.
- Case study: a 10-alpha pool where most pairs have mutual IC above 0.7 reaches test IC 0.0458, and removing a member with standalone IC of only 0.0011 lowers the pool to 0.0447.
- A top-50 / swap-5 backtest in 2020 to 2021 shows the highest net worth for AlphaGen (figure only).

## Signal construction
Not a signal. The transferable rule is the fitness function: score a candidate by the out-of-pool improvement it brings to a regularized linear combination, not by its standalone statistic.

## Relevance to SOL perpetuals at minutes to hours
For a single instrument the IC becomes the time-series correlation between the combined signal and the forward return over the trading horizon. Marginal-contribution fitness is the right objective for a bot that will blend many weak inputs. The wide seed-to-seed spread of the genetic-programming baseline (standard deviation as large as the mean) is a warning that one GP run tells little; run several seeds.

## Caveats
Daily data, 20-day horizon, one country, two test years. The backtest reports no cost figure. Independent re-evaluation is mixed: `wang-2026-factorbench-automated-factor-mining-benchmark.md` ran AlphaGen on five markets in 2024 to 2025 and measured a composite IC of 0.0064 with negative rank IC and negative IC after removing style exposures, and found its pools among the most internally redundant. Reinforcement learning as a trading method in general is covered in topic 24.
