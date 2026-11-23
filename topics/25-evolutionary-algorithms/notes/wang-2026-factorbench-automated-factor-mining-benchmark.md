---
title: "FactorBench: A Portfolio-Aware Benchmark for Automated Factor Mining"
authors: "Wang, Zhuohan; Ventre, Carmine"
year: 2026
venue: "arXiv preprint 2610.06947v1 (King's College London)"
url: "https://arxiv.org/pdf/2610.06947"
pdf: "sources/25-evolutionary-algorithms/wang-2026-factorbench-automated-factor-mining-benchmark.pdf"
access: "full-text"
source_type: "working-paper"
evidence_grade: "B"
topic: "25-evolutionary-algorithms"
asset_class: "equities"
horizon: "multi-day"
tags: "benchmark, factor-mining, genetic-programming, alphagen, llm-agents, out-of-sample-decay, style-exposure, redundancy"
---

## Key insight
An independent comparison of nine automated factor miners, covering genetic programming, reinforcement learning, generative models and LLM agents, on the same data, target and costs. No family consistently wins. Factors that look strong in training lose most of their IC out of sample, much of what remains is ordinary style exposure, and the 2015 Alpha101 formulas are competitive with every mined pool. This is the strongest available evidence against the assumption that newer search methods find better signals.

## Method
Each method runs its own author-released code and objective on a shared data contract; outputs (about 5,000 factors) are executed into date-by-asset matrices and scored at three levels.
- Factor level: daily cross-sectional IC with the 20-day forward return in training, validation and test. The sign of each factor is fixed from training, so a negative test IC is an out-of-sample reversal. Each factor is also regressed on market beta, volatility, momentum, short-term reversal and liquidity; residual IC measures what is left.
- Pool level: Spearman correlation between factors within a method, between methods, and against Alpha101.
- Portfolio level: remove highly correlated candidates, combine by ridge regression using training and validation data, rebalance every 20 days, charge 10 basis points per dollar traded plus borrow cost on shorts.

Methods: a GP baseline; AlphaGen, AlphaQCM, AlphaCFG; AlphaForge, AlphaSAGE; R&D-Agent, AlphaAgent, QuantaAlpha; and Alpha101 as a non-mined reference.

## Data and sample
Daily panels for S&P 100, Hang Seng, CSI 300, FTSE 100 and Nikkei 225 constituents. Training 2017 to 2021, validation 2022 to 2023, test 2024 to 2025.

## Reported results
- Temporal generalization: training IC "generally does not recover in testing". LLM methods show smaller declines only because they start from lower training IC; their held-out IC is not consistently higher. Paired train-to-test degradation is widespread for GP, RL and generative methods, especially in Hong Kong, China and the UK.
- Style overlap: neutralizing reduces IC most for GP. GP and R&D-Agent pools are the most explained by the five style exposures.
- Redundancy: AlphaGen and AlphaQCM pools are the most internally correlated; GP pools are highly correlated in several markets. LLM pools resemble each other and sit closest to Alpha101.
- Test-period composite (IC, rank IC, residual IC; long-short net Sharpe): Alpha101 0.0238, 0.0176, 0.0237; 0.32. GP 0.0165, -0.0058, -0.0067; 0.34. AlphaGen 0.0064, -0.0128, -0.0080; 0.30. AlphaQCM 0.0191, 0.0056, 0.0175; 0.67. R&D-Agent 0.0253, 0.0046, 0.0011; 0.68. AlphaAgent 0.0030, -0.0002, -0.0025; -0.09.
- Long-only portfolios all earned 22.4% to 31.2% a year (Sharpe 1.03 to 1.31) in a rising market, which does not separate the methods.
- Long-short profitability is fragile to costs: most methods approach or fall below zero as costs rise.

## Signal construction
Not a signal. It defines the acceptance tests a mined signal should pass before use: sign fixed in training and held; out-of-sample IC reported next to in-sample IC; residual IC after regressing on known simple predictors; correlation against the existing pool and against a public library; net performance at several cost levels.

## Relevance to SOL perpetuals at minutes to hours
The style-neutralization test has a direct analogue for one instrument: regress any evolved SOL signal on a short list of simple known predictors (lagged return, realized volatility, order-flow imbalance, funding, BTC return) and keep it only if the residual still predicts. The benchmark also sets expectations: on liquid equities, search sophistication has not bought out-of-sample edge, so effort is better spent on inputs and evaluation than on a fancier optimizer.

## Caveats
Equities, daily data and a 20-day horizon; nothing on crypto or intraday. A two-year test period. Results apply to the released implementations under one shared task, as the authors state, and compute budgets differ widely between methods. Preprint, not yet peer reviewed. The portfolio table averages five markets and several seeds, which hides dispersion I did not examine in the appendix.
