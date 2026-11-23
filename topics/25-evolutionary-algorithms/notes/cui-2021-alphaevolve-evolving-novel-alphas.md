---
title: "AlphaEvolve: A Learning Framework to Discover Novel Alphas in Quantitative Investment"
authors: "Cui, Can; Wang, Wei; Zhang, Meihui; Chen, Gang; Luo, Zhaojing; Ooi, Beng Chin"
year: 2021
venue: "SIGMOD 2021 (read: arXiv 2103.16196v2)"
url: "https://arxiv.org/pdf/2103.16196"
pdf: "sources/25-evolutionary-algorithms/cui-2021-alphaevolve-evolving-novel-alphas.pdf"
access: "full-text"
source_type: "peer-reviewed"
evidence_grade: "C"
topic: "25-evolutionary-algorithms"
asset_class: "equities"
horizon: "daily"
tags: "automl-zero, program-evolution, formulaic-alpha, redundancy-pruning, low-correlation, seeding"
---

## Key insight
Instead of evolving a formula tree, AlphaEvolve evolves a small program in the style of AutoML-Zero: a sequence of scalar, vector and matrix operations with its own learned parameters. Starting the search from a human-designed alpha and mutating it gave better results than starting from nothing, from a random program or from a neural network. This 2021 system is unrelated to the 2025 coding agent of the same name that later LLM papers cite.

## Method
An alpha has three functions: `Setup()` initializes operands, `Predict()` maps a feature matrix to a predicted return, `Update()` adjusts parameters after each training sample. Search is mutation-only evolution with tournament selection: sample a tournament from the population, mutate its best member (change an operation, its operands, or insert/delete an operation), add the child, drop the oldest. Settings reported: population 100, tournament size 10, mutation probability 0.9.

Two additions are specific to finance. `RelationOps` let one stock's computation use the rank or mean of the same operand across its sector or industry. A pruning step removes operations that do not affect the prediction, then fingerprints the pruned program so that duplicates are not re-evaluated. Fitness during search is the IC on the validation set.

To build a set of weakly correlated alphas, each round's winner is added to a set A and any later candidate whose portfolio returns correlate with a member of A above a cutoff (15%, the hedge-fund convention the paper cites) is discarded.

## Data and sample
NASDAQ stocks, daily, 2013 to 2017: 1,220 days split 988 / 116 / 116 into training, validation and test; 1,026 stocks after filtering. Thirteen input features: moving averages and volatilities of close over 5, 10, 20 and 30 days, plus open, high, low, close and volume, each normalized by its per-stock maximum.

## Reported results
Sharpe ratio and IC of a long-short portfolio (long top 50, short bottom 50 predicted returns):
- Hand-designed seed alpha: Sharpe 4.11, IC 0.013.
- Evolved from that seed: Sharpe 21.32, IC 0.067. Genetic-algorithm baseline: Sharpe 13.03, IC 0.049.
- In later rounds with correlation cutoffs, the genetic algorithm fell to Sharpe 4.41, then -1.94 and -1.97, and its search was stopped; AlphaEvolve's seeded alphas in the same rounds scored 13.58, 15.07 and 4.90.
- Pruned search evaluated far more candidates in the same budget (for example 309,700 against 19,500 for the first seeded alpha).
- Both Sharpe and IC decline round by round as each new alpha must differ from all earlier ones.

## Signal construction
Not a signal. The transferable parts are (1) seeding the population with existing hand-built signals, (2) pruning and fingerprinting to avoid re-testing equivalent candidates, and (3) a hard correlation cutoff against signals already accepted.

## Relevance to SOL perpetuals at minutes to hours
Seeding from known signals (order-flow imbalance, funding, basis) is a sensible way to start a search on SOL data. Fingerprinting matters for honest accounting as well as speed: it gives a truer count of distinct trials. Relational operators would map to cross-asset inputs such as BTC and ETH features.

## Caveats
The test set is 116 trading days of one market, with no transaction costs, and the reported Sharpe ratios of 10 to 21 are far outside anything achievable live. The features are normalized by each stock's maximum over all time steps, which uses future information. The genetic-algorithm baseline's settings were taken from another study. Treat this as a description of a search architecture, not as performance evidence.
