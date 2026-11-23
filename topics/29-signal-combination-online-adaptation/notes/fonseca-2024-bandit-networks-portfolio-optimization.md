---
title: "Improving Portfolio Optimization Results with Bandit Networks"
authors: "Fonseca, Gustavo de Freitas; Coelho e Silva, Lucas; de Castro, Paulo Andre Lima"
year: 2024
venue: "arXiv preprint 2410.04217 (v2, October 2024)"
url: "https://arxiv.org/pdf/2410.04217"
pdf: "sources/29-signal-combination-online-adaptation/fonseca-2024-bandit-networks-portfolio-optimization.pdf"
access: "full-text"
source_type: "working-paper"
evidence_grade: "C"
topic: "29-signal-combination-online-adaptation"
asset_class: "equities"
horizon: "daily"
tags: "thompson-sampling, discounted-bandit, sliding-window, non-stationary, portfolio-selection, equal-weight-benchmark"
---

## Key insight
A recent applied test of non-stationary bandits (discounted and sliding-window Thompson sampling and UCB) on real daily stock data, with equal weighting included among the benchmarks. The proposed two-stage "bandit network" reports an out-of-sample Sharpe ratio of 1.59 against 1.32 for equal weights. The comparison is useful mainly as a template and as a warning: within the same paper the plain stationary UCB-1 has a higher Sharpe than every non-stationary variant in the single-stock task, and the test universe is a hand-picked set of 44 stocks with no trading costs.

## Method
Adaptive Discounted Thompson Sampling (ADTS): each arm keeps a Beta posterior that is discounted by γ only when that arm is played (a "relaxed" discount), plus a second Beta posterior built from the last w rewards of the arm. Each round one sample is drawn from each, an aggregation function f (min, average or max) combines them, and the arm with the highest score is played. Reward is binary: 1 if the chosen arm had the best value of a financial metric (mean return or Sharpe over a window) that step. A combinatorial version (CADTS) picks k arms. "Bandit networks" chain two stages: a first bandit shortlists stocks using mean return over a 100-day window, a second allocates among the shortlist using a 60-day Sharpe criterion, with shortlist sizes of 4, 10 or 15.

## Data and sample
Daily prices of 44 stocks chosen from the S&P 500, April 2020 to July 2024. Benchmarks: a CAPM-based portfolio, equal weights, risk parity, Markowitz, and the S&P 500 index. Results for stochastic policies are averaged over 30 simulations. No transaction costs, slippage or turnover figures were found in the text.

## Reported results
Single-stock selection (paper's Table 6; total return, Sharpe):
- ADTS (mean aggregation) 13.72, 1.76; UCB-1 10.62, 1.91; SW-UCB 7.51, 1.86; classical Thompson sampling 6.77, 1.35; D-UCB 5.10, 1.21; discounted TS 3.63, 1.51; S&P 500 1.20, 1.12.
Portfolio task (Table 8; total return, Sharpe, drawdown):
- Two-layer ADTS (n=4) 4.92, 1.59, 0.90; SW-UCB with CADTS (n=4) 4.73, 1.37, 1.78; ADTS with CADTS (n=4) 3.82, 1.30, 1.70; two-layer ADTS (n=15) 2.55, 1.58, 0.55.
- CAPM 1.79, 1.29, 0.69; equal weights 1.59, 1.32, 0.59; risk parity 1.38, 1.31, 0.50; S&P 500 1.28, 1.17, 0.49; Markowitz 0.15, 0.40, 0.22.
The headline claim is a Sharpe 20% above the best classical model (equal weights). One bandit configuration (Sharpe 1.30) is below equal weights. The highest-return configurations carry 1.5 to 3 times the drawdown figure of equal weights (0.90, 1.78 and 1.70 against 0.59).

## Signal construction
For strategy selection: for each strategy keep (α, β) discounted on use and a second (α_w, β_w) from its last w outcomes, where an outcome is 1 if the strategy was the best (or in the top c) of the pool over the evaluation window. Each period sample both posteriors per strategy, combine with min for a conservative selector or mean for a balanced one, and allocate to the top k. Parameters: γ, w, k, the evaluation window and the aggregation function.

## Relevance to SOL perpetuals at minutes to hours
Shows how to turn continuous, noisy P&L into the bounded reward a Beta-Bernoulli sampler needs, and that mixing a long discounted memory with a short window is a simple way to hedge the choice of memory length. The evidence itself does not transfer: daily equities in a strong bull market, a selected universe, long-only, gross of costs.

## Caveats
Preprint. The 44 stocks were selected by the authors, which invites survivorship and selection bias, and the period is one regime. No costs despite concentrated, frequently changing holdings. Equal weights have the best Sharpe among classical models, and the margin over it rests on one of five configurations; no significance test is reported. Winner-take-all binary rewards discard magnitude information.
