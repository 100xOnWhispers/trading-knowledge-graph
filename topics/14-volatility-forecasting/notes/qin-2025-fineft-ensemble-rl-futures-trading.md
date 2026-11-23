---
title: "FineFT: Efficient and Risk-Aware Ensemble Reinforcement Learning for Futures Trading"
authors: "Qin, Molei; Cai, Xinyu; Li, Yewen; Xia, Haochong; Zong, Chuqiao; Sun, Shuo; Wang, Xinrun; An, Bo"
year: 2025
venue: "arXiv preprint 2512.23773; header indicates KDD 2026"
url: "https://arxiv.org/pdf/2512.23773"
pdf: "sources/14-volatility-forecasting/qin-2025-fineft-ensemble-rl-futures-trading.pdf"
access: "full-text"
source_type: "peer-reviewed"
evidence_grade: "C"
topic: "14-volatility-forecasting"
asset_class: "crypto"
horizon: "minutes"
tags: "reinforcement-learning, ensemble-q-learning, leverage, liquidation-risk, out-of-distribution, vae, crypto-futures"
---

## Key insight
Leverage makes reinforcement learning for futures harder in two specific ways: it amplifies reward noise so training fails to converge, and it makes mistakes in unfamiliar market states far more expensive. FineFT addresses both with an ensemble of Q-learners updated selectively and a novelty detector that hands control to a conservative, position-closing policy when the current market state is unlike anything seen in training. On minute-level crypto futures at 5x leverage the main benefit is lower drawdown.

## Method
The agent trades one asset at minute frequency. The action is a target position chosen from a finite pool of signed leverage levels; a market order closes the gap to the target. The simulated environment includes commission, order-book slippage and funding fees. Three stages:
1. Train an ensemble of Q-learners, updating only the learner with the smallest temporal-difference error on each sample, which specialises learners to different market dynamics and stabilises training.
2. Back-test each learner by market regime on validation data, keep the profitable ones, and train a variational autoencoder (VAE) per regime on market-state features to mark each learner's "capability boundary".
3. At run time, score recent market states under each VAE; if the best score is below a risk threshold the state is treated as out-of-distribution and a conservative policy takes over. That policy never opens positions: it holds the current position unless the trade's drawdown exceeds 5%, then closes it.

## Data and sample
BNB, BTC, DOT and ETH against USDT, minute-level futures data with order book, 1 January 2022 to 1 January 2024 (210,241 steps each as listed). Split: one year training, six months validation, final six months testing. 5x leverage. Twelve baselines including DQN, PPO, ensemble, distributional and hierarchical RL methods and rule-based MACD.

## Reported results
- The authors report the lowest risk (maximum drawdown and volatility) on all four datasets, the highest risk-adjusted return on three, and the highest total return on two.
- Hierarchical RL baselines earn high returns but with high maximum drawdowns.
- Rule-based baselines (MACD and a second rule) were extremely sensitive to hyperparameters chosen on validation data.
- In the test period the conservative policy is selected in most periods, and more often as time moves further from the training window.
- Removing the risk threshold lowers performance; the ensemble without it still beats any single learner.

## Signal construction
Not a signal; a risk architecture for a learning-based trader. The transferable component is the novelty gate: fit a density or reconstruction model on the feature vectors seen in training and validation; in live trading compute a smoothed novelty score; when the score says the state is unfamiliar, stop opening positions and manage existing ones with a fixed drawdown stop. This can wrap any model, including a non-RL one.

## Relevance to SOL perpetuals at minutes to hours
Relevant for instrument type, horizon and the explicit treatment of leverage, costs and funding. SOL is not among the tested assets. A new venue such as Kalshi is by construction out-of-distribution relative to any training set from offshore venues, so a gate of this kind would initially keep the bot conservative, which is arguably the correct behaviour. The fixed 5% per-trade stop at 5x leverage is a design choice, not an optimised or volatility-scaled one.

## Caveats
Six-month test window per asset; four assets; results depend on a simulator. The model spent most of the test period in the conservative policy, so the low drawdown partly reflects not trading. Many components and hyperparameters were tuned on validation data. Result tables were only partly legible in text extraction, so specific figures are not reproduced here. The authors state code is released; that was not checked.
