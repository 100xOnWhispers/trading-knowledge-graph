---
title: "Deep Reinforcement Learning for Cryptocurrency Trading: Practical Approach to Address Backtest Overfitting"
authors: "Gort, Berend Jelmer Dirk; Liu, Xiao-Yang; Sun, Xinghang; Gao, Jiechao; Chen, Shuaiyu; Wang, Christina Dan"
year: 2022
venue: "arXiv:2209.05559v6"
url: "https://arxiv.org/pdf/2209.05559"
pdf: "sources/24-reinforcement-learning/gort-2022-drl-crypto-backtest-overfitting.pdf"
access: "full-text"
source_type: "working-paper"
evidence_grade: "C"
topic: "24-reinforcement-learning"
asset_class: "crypto"
horizon: "minutes"
tags: "backtest-overfitting, pbo, combinatorial-cross-validation, ppo, td3, sac, hyperparameter-sensitivity, 5-minute, sol"
---

## Key insight
Deep RL trading agents are so sensitive to hyperparameters that selecting the best of many trials on one validation split routinely produces an overfitted agent. The paper proposes treating agent acceptance as a hypothesis test: estimate the probability of backtest overfitting (PBO) from combinatorial cross-validation across hyperparameter trials, and reject any agent class whose PBO exceeds a threshold. The validation of the idea is thin: in the one test window, every agent lost a third or more of its capital, and one of the two "accepted" agents was among the worst.

## Method
Environment: long-only portfolio of 10 coins, state = cash, holdings, OHLCV and 9 technical indicators per coin; reward = change in portfolio value net of a 0.3% fee per trade; trades assumed filled at market price with no slippage; a volatility index (CVIX) above 90 forces liquidation. Agents: PPO, TD3, SAC, each with 50 hyperparameter trials.

PBO estimation (following Bailey et al.): build a matrix of returns with one column per hyperparameter trial; split rows into blocks (the paper uses 14 sub-matrices) and form all combinations of half the blocks as in-sample (IS), the rest as out-of-sample (OOS). For each combination, find the trial that is best IS, take its relative OOS rank `omega`, and compute the logit `lambda = ln( omega / (1 - omega) )`. PBO is the fraction of combinations with `lambda <= 0`, that is, where the IS winner is below the OOS median. Reject if PBO exceeds `alpha = 10%`. Training itself uses combinatorial cross-validation over 5 equal-sized groups of the training data, compared against walk-forward (WF) and K-fold (KCV) variants of PPO.

## Data and sample
Five-minute bars, 02/02/2022 to 06/27/2022, for AAVE, AVAX, BTC, NEAR, LINK, ETH, LTC, MATIC, UNI and SOL. Training 02/02 to 04/30 (25,055 bars); testing 05/01 to 06/27 (16,704 bars), a period with two market crashes. Benchmarks: equal weight and the S&P Cryptocurrency Broad Digital Market index.

## Reported results
- PBO: PPO with walk-forward 17.5% (rejected), PPO with K-fold 7.9%, PPO with combinatorial CV 8.0%, TD3 9.6%, SAC 21.3% (rejected).
- Test-period cumulative return: index -50.78%, equal weight -47.78%, PPO WF -49.39%, PPO KCV -55.54%, PPO (combinatorial CV) -34.96%, TD3 -59.08%, SAC -59.48%.
- The authors conclude the least overfitted agent outperforms the others and the benchmarks.

## Signal construction
Not a signal. It is an acceptance gate for any tuned strategy:
1. Run N hyperparameter trials; record each trial's per-period returns.
2. Partition time into S blocks; for every half-and-half combination, rank trials IS and OOS.
3. PBO = share of combinations where the IS-best trial ranks at or below the OOS median.
4. Reject the whole model family if PBO > 10%.
Recompute at each retraining.

## Relevance to SOL perpetuals at minutes to hours
Directly applicable: 5-minute crypto bars, SOL in the sample, and the same PPO, TD3 and SAC agents most open-source stacks provide. The gate applies equally to non-RL strategies in this repository and should sit in the common backtest harness. The trading environment is weaker than what the bot needs: long-only spot, a flat 0.3% fee, no spread, no funding, no shorting.

## Caveats
One 58-day test window in a single crash regime; no confidence intervals on the return differences. TD3 passed the gate (PBO 9.6%) and returned -59.08%, worse than both benchmarks, so a low PBO did not predict good performance; the claim rests on one agent. The best agent's -35% may reflect holding more cash, which the paper does not separate from skill. PBO measures rank instability across trials, not profitability; a family of uniformly bad trials can have a low PBO. The estimate depends on the block count and number of trials. Same research group as FinRL. The author list follows the arXiv record; the title page of the v6 PDF omits Sun. Abstract and body spell the benchmark both "DBM" and "BDM".
