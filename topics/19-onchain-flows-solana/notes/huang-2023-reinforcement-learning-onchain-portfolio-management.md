---
title: "A Scalable Reinforcement Learning-based System Using On-Chain Data for Cryptocurrency Portfolio Management"
authors: "Huang, Zhenhan; Tanaka, Fumihide"
year: 2023
venue: "arXiv preprint arXiv:2307.01599"
url: "https://arxiv.org/pdf/2307.01599"
pdf: "sources/19-onchain-flows-solana/huang-2023-reinforcement-learning-onchain-portfolio-management.pdf"
access: "full-text"
source_type: "working-paper"
evidence_grade: "C"
topic: "19-onchain-flows-solana"
asset_class: "crypto"
horizon: "hours"
tags: "reinforcement-learning, dqn, on-chain-metrics, santiment, feature-selection, pca, backtest"
---

## Key insight
One of the few reinforcement-learning trading systems that takes on-chain metrics as state inputs. A DQN agent fed with price bars plus PCA-compressed on-chain metrics made money in a seven-month backtest during the 2022 bear market while the underlying coins lost. The result shows the plumbing is feasible; it does not show that the on-chain inputs were the reason, because there is no ablation.

## Method
The system (CryptoRLPM) has five units: data feed, data refinement, portfolio agent, live trading and agent updating.
- Feature selection: for each coin, compute Pearson correlations between every available on-chain metric and returns over 12, 24 and 48 periods; take the five highest and five lowest in each group; rank by how often a metric appears; keep the top ten.
- Compression: rolling normalisation and rolling PCA, keeping components that explain at least 80 percent of variance.
- Agent: one "Crypto Module" per coin, each allocating between that coin and cash with a binary action (all in or all out), using a Deep Q-Network with convolutional layers. Portfolio weights are the vote across modules.
- The design allows an upstream signal-generating agent, but in the experiments the refined metrics are fed straight to the allocation agent.

## Data and sample
6-hour OHLCV from Binance and on-chain metrics from Santiment's API (basic plan), which mixes on-chain and social metrics; the authors treat both as on-chain. Coins: BTC, STORJ, BLZ and LINK against USDT, in three portfolios of two, three and four coins. Training October 2020 to December 2021, validation January to February 2022, backtest March to September 2022.

## Reported results
- Accumulated return, daily return and Sortino ratio in the backtest: portfolio (a) 31.26 percent, 0.2485 percent, 0.8709; portfolio (b) 79.87 percent, 0.4386 percent, 1.3877; portfolio (c) 43.71 percent, 0.3140 percent, 0.9311.
- Baselines are buy-and-hold of the underlying coins, all with negative accumulated return. Against Bitcoin the system improves accumulated return by at least 83.14 percentage points, daily return by at least 0.5603 and Sortino by at least 2.1767.
- No transaction costs, slippage or funding are mentioned in the text read.

## Signal construction
A template for using flow features inside a learning agent:
- State: recent n bars of OHLCV plus the leading principal components of the top-ranked on-chain metrics for the asset.
- Action: long or flat (binary), per asset.
- Selection of metrics is asset-specific and re-run at each retraining.
- For a SOL perp bot the action set would need short and size, and the reward would need fees and funding.

## Relevance to SOL perpetuals at minutes to hours
Moderate. The per-asset metric-selection step is a sensible answer to the finding in [chi-2024](chi-2024-return-volatility-forecasting-onchain-flows.md) that flow signals differ by asset. The paper describes itself as a 10-to-30-minute system but tests on 6-hour bars, so the intraday claim is untested. SOL is not included. In a 2022 backtest, any policy that learned to sit in cash would beat buy-and-hold, so the headline numbers say little about predictive skill.

## Caveats
Single seven-month bear-market test window; long-or-cash agent versus long-only baselines; no costs; no ablation without on-chain inputs; no comparison with a simple trend filter; no random-seed variance. Feature selection by correlation on the training period risks overfitting, and vendor metrics may be revised after the fact. Not peer-reviewed.
