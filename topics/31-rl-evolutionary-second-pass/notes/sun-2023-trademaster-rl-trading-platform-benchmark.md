---
title: "TradeMaster: A Holistic Quantitative Trading Platform Empowered by Reinforcement Learning"
authors: "Sun, Shuo; Qin, Molei; Zhang, Wentao; Xia, Haochong; Zong, Chuqiao; Ying, Jie; Xie, Yonggang; Zhao, Lingxuan; Wang, Xinrun; An, Bo"
year: 2023
venue: "NeurIPS 2023 Datasets and Benchmarks Track"
url: "https://personal.ntu.edu.sg/boan/papers/NeurIPS_23_TradeMaster.pdf"
pdf: "sources/31-rl-evolutionary-second-pass/sun-2023-trademaster-rl-trading-platform-benchmark.pdf"
access: "full-text"
source_type: "peer-reviewed"
evidence_grade: "B"
topic: "31-rl-evolutionary-second-pass"
asset_class: "multi"
horizon: "daily"
tags: "reinforcement-learning, benchmark, platform, head-to-head, seeds, rank-distribution, environment"
---

## Key insight
When eight RL methods are run in one pipeline with the same data, tuning budget and seeds, the methods designed specifically for trading do not beat generic RL algorithms on profit. The paper also introduces a better way to report such comparisons: the probability that a method takes each rank across seeds and test periods, in place of a single mean. Its headline benchmark is daily US equities, so it is evidence about evaluation practice more than about intraday crypto.

## Method
- Platform: environments for six tasks (crypto trading, portfolio management, intraday trading, order execution, market making and high-frequency trading), 15 RL algorithms, 13 datasets across stocks, futures, FX and crypto at daily and minute granularity, and evaluation tools. Environments include commission, slippage, and options for leverage, shorting and stop loss.
- Benchmark shown in the paper: portfolio management on Dow Jones 30 stocks with A2C, DDPG, TD3, PG and PPO against three trading-specific methods (EIIE, IMIT, SARL).
- Protocol: three rolling splits, each with the last year as test and the previous year as validation; five random seeds per method; grid search over batch size, hidden size and learning rate for every method.
- Reporting: eight metrics (return, Sharpe, Calmar, Sortino, volatility, drawdown, two diversification measures); a rank distribution plot giving, for each method, the share of the 15 seed-period runs in which it took rank 1 to 8; a separate "extreme market" test month.

## Data and sample
Daily prices for 29 Dow Jones stocks, 2012 to 2021, from Yahoo Finance, with 11 price-based features. The extreme-market window is September 2021. The platform's dataset table also lists a Binance BTC order-book dataset, which the main-text benchmark does not use.

## Reported results
- TD3 had the best total return and Sharpe, Calmar and Sortino ratios; DDPG was close behind.
- The three trading-specific methods "fail to outperform properly tuned classic RL algorithms such as TD3 in terms of profitability"; they did better on volatility, drawdown and diversification.
- Rank distribution: TD3 was ranked first in 24% of runs on total return and 27% on Sharpe ratio, so no method dominates.
- "No existing algorithm achieves dominating results on all financial metrics."

## Signal construction
Not a signal. Two practices to adopt: report rank distributions over seeds and test windows when comparing model families, and keep one pipeline in which every candidate gets the same tuning budget.

## Relevance to SOL perpetuals at minutes to hours
A winner that ranks first in only a quarter of runs is a warning about choosing an RL algorithm on one backtest. The platform's crypto and high-frequency environments could serve as a starting scaffold, but perp funding and liquidation were not described in the parts read, and the benchmark evidence is daily and long-only across 29 stocks.

## Caveats
The paper states that features are z-score normalized using the mean and standard deviation "of train, validation and test set, respectively", which for the test set uses information from the whole test period. The algorithms compared are from the platform authors' own implementations, two of them re-implemented without official code. No buy-and-hold or equal-weight row was seen in the main comparison.
