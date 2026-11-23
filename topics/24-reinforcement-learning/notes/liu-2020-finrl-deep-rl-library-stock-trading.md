---
title: "FinRL: A Deep Reinforcement Learning Library for Automated Stock Trading in Quantitative Finance"
authors: "Liu, Xiao-Yang; Yang, Hongyang; Chen, Qian; Zhang, Runjia; Yang, Liuqing; Xiao, Bowen; Wang, Christina Dan"
year: 2020
venue: "arXiv:2011.09607v2 (NeurIPS 2020 Deep RL Workshop)"
url: "https://arxiv.org/pdf/2011.09607"
pdf: "sources/24-reinforcement-learning/liu-2020-finrl-deep-rl-library-stock-trading.pdf"
access: "full-text"
source_type: "working-paper"
evidence_grade: "C"
topic: "24-reinforcement-learning"
asset_class: "equities"
horizon: "daily"
tags: "finrl, library, ppo, ddpg, td3, gym-environment, turbulence-index, backtest, benchmark"
---

## Key insight
FinRL is the most widely used open-source scaffold for RL trading experiments: Gym-style market environments, wrappers for standard algorithms (DQN, DDPG, PPO, SAC, A2C, TD3) and a train-validate-trade pipeline with automated backtest reports. The paper is a library description with demonstration results, not evidence that the strategies work. Its value for this project is as a vocabulary of environment design choices; its demonstrations illustrate the weak evaluation habits that later critiques, including one from the same group (Gort et al., 2022), target.

## Method
Three layers: environment, agent, application. The environment exposes state (balance, holdings, prices, technical indicators), action (shares to buy, hold or sell per asset) and a reward chosen by the user: change in portfolio value, Sharpe ratio, or a custom function with risk or cost terms. Transaction cost is an environment parameter, as is a bid-ask spread term. A "turbulence index" serves as a risk switch: `turbulence_t = (y_t - mu) Sigma^{-1} (y_t - mu)'`, the Mahalanobis distance of current returns from their historical distribution; above a threshold the agent stops buying and sells down. Data are split into training, validation (hyperparameter tuning) and trading periods, with optional rolling windows. Backtests are reported through the pyfolio package.

## Data and sample
Daily US equity data. Demonstrations: single-asset PPO on SPY, QQQ, GOOGL, AMZN, AAPL and MSFT; multi-stock trading and portfolio allocation with TD3 and DDPG on Dow Jones 30 constituents. Trading period for all demonstrations: 2019-01-01 to 2020-09-23. Environments are also packaged for NASDAQ-100, S&P 500, HSI, SSE 50 and CSI 300.

## Reported results
- Single-asset PPO: Sharpe ratios 1.10 to 1.49 against 0.74 for the S&P 500 over the same period; maximum drawdowns 20.9% to 28.3%.
- Dow 30 (two values reported per agent, for multi-stock trading and portfolio allocation): TD3 Sharpe 1.38 and 1.03, DDPG 1.28 and 0.98, against 0.44 for minimum variance and 0.48 for the DJIA.
- The authors attribute large drawdowns to the 2020 crash.

## Signal construction
Not a signal. Reusable design elements:
- A Gym-style environment whose step function charges fees and spread, so cost is part of the reward by construction.
- A regime switch computed outside the policy (turbulence above threshold forces risk-off). For a single instrument the Mahalanobis distance reduces to a squared z-score of the current return.
- A fixed train, validate, trade split rolled forward.

## Relevance to SOL perpetuals at minutes to hours
The library's environments are long-only daily equity portfolios; nothing in the reported evidence concerns intraday data, shorting, leverage, funding or order books. Using FinRL (or its successors FinRL-Meta and the crypto environments used by Gort et al.) for SOL perps means writing a new environment, at which point the library contributes mainly the algorithm wrappers. The hard-coded risk switch is a pattern worth copying: keep kill-switch logic outside the learned policy.

## Caveats
One 21-month test window that is mostly a bull market with one crash; long-only agents on large-cap technology stocks would beat the index in that window without skill. No seed variance, no significance tests, no walk-forward repetition, no comparison with simple momentum or volatility-targeting baselines. The validation set is used for tuning with no correction for the number of trials. The authors maintain and promote the library. Workshop paper.
