---
title: "FinRL-Meta: Market Environments and Benchmarks for Data-Driven Financial Reinforcement Learning"
authors: "Liu, Xiao-Yang; Xia, Ziyi; Rui, Jingyang; Gao, Jiechao; Yang, Hongyang; Zhu, Ming; Wang, Christina Dan; Wang, Zhaoran; Guo, Jian"
year: 2022
venue: "arXiv:2211.03107 (NeurIPS-formatted with checklist; track not confirmed)"
url: "https://arxiv.org/abs/2211.03107"
pdf: "sources/31-rl-evolutionary-second-pass/liu-2022-finrl-meta-market-environments-benchmarks.pdf"
access: "full-text"
source_type: "documentation"
evidence_grade: "C"
topic: "31-rl-evolutionary-second-pass"
asset_class: "multi"
horizon: "n/a"
tags: "reinforcement-learning, environment, gym, dataops, benchmark, survivorship-bias, sim-to-real"
---

## Key insight
FinRL-Meta is a library of gym-style market environments built by an automated data pipeline, with reproductions of earlier papers offered as benchmarks. It names three sources of the simulation-to-reality gap for trading RL: low signal-to-noise data, survivorship bias in historical universes, and overfitting during backtesting. It documents what the most widely used open environments do and do not model, which is what a reader needs before trusting results produced with them.

## Method
- A "DataOps" pipeline pulls data from many providers (the paper's table lists Binance and CCXT among them, with one-minute crypto data), cleans it, adds features and emits an environment with `reset`, `step` and `reward`.
- Frictions in the standard environments: a proportional transaction cost (0.1% per trade in the examples), optional margin and short selling as account settings, a non-negative balance constraint, and a market-crash switch using the VIX in place of the earlier turbulence index because VIX is available immediately.
- Training speed: vectorized environments on GPU in the style of Isaac Gym, so hundreds of environment copies generate transitions in parallel.
- A separate order-book market simulator is described in the appendix: playback of historical book data with a matching mechanism, one-minute steps, market and limit orders, temporary market impact and order delay modelled; permanent impact of limit orders and a non-resilient book are not.
- Benchmarks are reproductions: multi-stock trading, portfolio allocation, ten-coin crypto trading, an ensemble strategy, population-based training on cloud GPUs, and a multi-agent liquidation task.

## Data and sample
The reproduced stock benchmark uses the 30 Dow Jones constituents as listed on 2020-07-01, trained 2009-01-01 to 2020-06-30 and tested 2020-07-01 to 2022-05-31. The ensemble reproduction trains from 2009-04-01 to 2019-06-30 and tests 2020-07-01 to 2022-03-31 with a quarterly rolling window.

## Reported results
- Ensemble reproduction: Sharpe ratio 1.53 and maximum drawdown -11.4% for the ensemble; A2C 1.37 and -11.8%; PPO 0.99 and -14.9%; DDPG 0.88 and -14.9%; the DJIA index 1.32 and -11.3%.
- No crypto benchmark numbers appear in the main text read; the crypto item is a notebook reproduction.

## Signal construction
Not a signal. It is tooling: a reference for how to structure a data-to-environment pipeline and a list of frictions the default environments include.

## Relevance to SOL perpetuals at minutes to hours
The standard environments are spot-style: proportional cost, optional short flag, no funding payments, no mark price, no maintenance margin or liquidation, fills at bar prices. A SOL perp environment needs those added (see [qin-2025-fineft](qin-2025-fineft-ensemble-rl-crypto-futures.md) for one that has them). The paper's own stock benchmark picks constituents as of the end of the training period, which is the survivorship problem it warns about; a crypto universe chosen today has the same flaw.

## Caveats
A software paper from the group that maintains the library. Benchmarks are single reproductions without seed dispersion in the main text. Two of three individual agents trail the index on Sharpe ratio in the authors' own table, and the ensemble's edge over the index (1.53 against 1.32, with a slightly larger drawdown) is within what one test window can produce by chance.
