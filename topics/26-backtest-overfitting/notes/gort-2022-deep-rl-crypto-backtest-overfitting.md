---
title: "Deep Reinforcement Learning for Cryptocurrency Trading: Practical Approach to Address Backtest Overfitting"
authors: "Gort, Berend Jelmer Dirk; Liu, Xiao-Yang; Gao, Jiechao; Chen, Shuaiyu; Wang, Christina Dan"
year: 2022
venue: "arXiv preprint 2209.05559 (v6, January 2023)"
url: "https://arxiv.org/pdf/2209.05559"
pdf: "sources/26-backtest-overfitting/gort-2022-deep-rl-crypto-backtest-overfitting.pdf"
access: "full-text"
source_type: "working-paper"
evidence_grade: "C"
topic: "26-backtest-overfitting"
asset_class: "crypto"
horizon: "minutes"
tags: "reinforcement-learning, pbo, combinatorial-cross-validation, hyperparameter-search, crypto"
---

## Key insight
Deep reinforcement learning (DRL) trading agents are selected through large hyperparameter searches, which is a multiple-testing problem. The paper frames overfitting detection as a hypothesis test: estimate the probability of backtest overfitting (PBO) across hyperparameter trials and reject an agent or validation scheme whose PBO exceeds a threshold. It reports that the agent with lower estimated overfitting lost less in a crash-dominated test window.

## Method
- Environment: portfolio of 10 cryptocurrencies, state built from prices and technical indicators, actions are trade sizes, reward is change in portfolio value. Transaction cost assumed at 0.3% of traded value; trades fill at market price with slippage ignored. A crypto volatility index (CVIX) threshold forces liquidation in extreme conditions.
- Validation schemes compared: walk-forward (WF), K-fold cross-validation (KCV), and combinatorial cross-validation with N = 5 groups and k = 2 validation groups, giving J = 10 train-validation splits.
- For each scheme, H = 50 hyperparameter trials are run. The per-trial return series are stacked into a matrix M, split into 14 sub-matrices, and the PBO procedure of Bailey et al. is applied (logit of the out-of-sample rank of the in-sample best).
- Decision rule: reject when PBO exceeds α = 10%.
- Agents: PPO, TD3, SAC.

## Data and sample
Five-minute bars for AAVE, AVAX, BTC, NEAR, LINK, ETH, LTC, MATIC, UNI and SOL from 02/02/2022 to 06/27/2022. Training 02/02/2022 to 04/30/2022 (25,055 points); testing 05/01/2022 to 06/27/2022 (16,704 points), a period with two market crashes. The data vendor or exchange is not confirmed in the text read.

## Reported results
- Estimated PBO: PPO with walk-forward 17.5% (rejected), PPO with K-fold 7.9%, PPO with combinatorial CV 8.0%, TD3 9.6%, SAC 21.3% (rejected).
- Test-period cumulative return: S&P Broad Digital Market index −50.78%, equal-weight −47.78%, PPO walk-forward −49.39%, PPO K-fold −55.54%, PPO combinatorial CV −34.96%, TD3 −59.08%, SAC −59.48%.
- The authors conclude the least overfitted agent (PPO with combinatorial CV) outperforms the others and the benchmarks.

## Signal construction
Not a signal. It is a validation recipe for learned policies: (1) split training data into N blocks and train on every combination of N − k blocks; (2) run H hyperparameter trials; (3) stack the validation return series of all trials; (4) compute PBO by CSCV; (5) discard the configuration family if PBO exceeds the chosen threshold.

## Relevance to SOL perpetuals at minutes to hours
The closest match in this folder to the project's setting: five-minute crypto bars including SOL, and learned policies. The recipe transfers directly to any reinforcement-learning, supervised or evolutionary search. What does not transfer is the evidence. The instruments are spot, long-only and traded as a portfolio; there is no shorting, funding or leverage, and the 0.3% cost is far above perpetual taker fees.

## Caveats
Weak empirical support for the central claim. Every agent lost 35% to 59% in the test window, so "outperforms" means "lost less" over 58 days in one regime. PPO with K-fold has almost the same PBO (7.9%) as the preferred method (8.0%) yet the worst PPO return, so PBO did not rank outcomes within the accepted set. Three months of training data, one test window, no confidence intervals on the return differences. The combinatorial scheme as described does not mention purging or embargo of overlapping samples between adjacent blocks. PBO here is computed over only 50 trials. Treat the method as sound and the performance claim as unproven.
