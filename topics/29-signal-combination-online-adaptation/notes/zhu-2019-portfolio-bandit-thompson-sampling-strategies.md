---
title: "Adaptive Portfolio by Solving Multi-armed Bandit via Thompson Sampling"
authors: "Zhu, Mengying; Zheng, Xiaolin; Wang, Yan; Li, Yuyuan; Liang, Qianqiao"
year: 2019
venue: "arXiv preprint 1911.05309 (v2, November 2019)"
url: "https://arxiv.org/pdf/1911.05309"
pdf: "sources/29-signal-combination-online-adaptation/zhu-2019-portfolio-bandit-thompson-sampling-strategies.pdf"
access: "full-text"
source_type: "working-paper"
evidence_grade: "C"
topic: "29-signal-combination-online-adaptation"
asset_class: "equities"
horizon: "daily"
tags: "thompson-sampling, strategy-selection, bandit, equal-weight-benchmark, meta-strategy, sharpe-reward"
---

## Key insight
A direct test of "use a bandit to choose which strategy to run". The arms are whole portfolio strategies (buy-and-hold, all cash, equal-weighted, value-weighted, mean-variance) and Thompson sampling picks one per period. Against equal weighting, which is one of its own arms, the selector improves the Sharpe ratio modestly on three monthly datasets and is level or slightly worse on two daily datasets. The authors themselves describe it as "not robust enough" at the higher frequency. It is a small but honest data point that strategy-selection bandits do not reliably beat 1/N.

## Method
Five strategic arms: buy-and-hold (keep last weights), sold-all (cash), equally weighted, value-weighted, and mean-variance. Each arm j has a Beta(α_j, β_j) posterior starting at Beta(1, 1). Each period a value is sampled from every posterior and the arm with the largest sample sets the portfolio weights. Success is defined by rank: the chosen arm counts as a success if its historical Sharpe ratio is at least as high as that of at least c of the arms, where c is a risk-preference parameter chosen by cross-validation; success adds 1 to α, failure adds 1 to β. A sliding window of τ = 120 periods initialises the posteriors and estimates inputs, following the rolling design of DeMiguel et al. Comparators also include an orthogonal-bandit portfolio (Shen et al. 2015) and Thompson-sampling blends of two strategies.

## Data and sample
Fama-French portfolios at monthly frequency: FF25 (June 1963 to November 2018), FF49 (July 1969 to November 2018), FF100 (July 1963 to November 2018). Daily data: 608 ETFs (December 2011 to November 2017) and 476 S&P 500 constituents (February 2013 to February 2018), keeping only assets with complete five-year histories. Transaction fees are not modelled; the authors list fees, tax and dividends as future work.

## Reported results
Sharpe ratios from the paper's Table 2 (as printed; units not stated), selector versus equal-weight arm:
- FF25: 22.60 vs 20.02. FF49: 24.20 vs 23.15. FF100: 21.76 vs 20.71.
- ETFs (daily): 194.49 vs 197.22, i.e. below equal weights.
- S&P 500 (daily): 126.88 vs 124.49, and below value-weighted (127.56).
Maximum drawdown is lower for the selector on the monthly data (for example 43.83% vs 54.10% on FF25, 30.76% vs 58.73% on FF100), helped by the cash arm. Mean-variance is far worse than equal weights on FF49 and both daily datasets (for example Sharpe 17.93 vs 197.22 on ETFs). Performance is sensitive to c.

## Signal construction
For a bot: define a handful of complete strategies including "flat" and "equal blend of all signals" as arms. Each evaluation period, mark the played arm a success if its trailing net Sharpe ranks in the top part of the pool, update its Beta posterior, and sample to pick the next arm. Including the flat arm gives the selector a built-in kill switch; including the equal-blend arm guarantees the benchmark is always reachable.

## Relevance to SOL perpetuals at minutes to hours
The design idea (benchmark and cash as arms) transfers. The result is a caution: with slow-moving monthly data the selector added a little; with daily data it added nothing over equal weights before costs. At minutes-to-hours horizons the reward signal per period is noisier still, so expect less, and note that switching between whole strategies incurs full position turnover that this paper does not charge.

## Caveats
Preprint with no significance tests and no costs. The stationary Beta update never forgets, so it is not actually adapted to regime change. The daily universes condition on survival over five years. Only the played arm is updated even though all arms' returns are observable, which wastes information.
