---
title: "SOTA: Stock Options Trading Agents Guided by Option-Implied Return Distributions"
authors: "Xie, Yizhen; Liu, Mengyang"
year: 2026
venue: "arXiv preprint 2610.10407"
url: "https://arxiv.org/abs/2610.10407"
pdf: "sources/20-options-derived-signals/xie-2026-stock-options-trading-agents-implied-distributions.pdf"
access: "full-text"
source_type: "working-paper"
evidence_grade: "C"
topic: "20-options-derived-signals"
asset_class: "options"
horizon: "daily"
tags: "reinforcement-learning, llm-agent, option-implied-distribution, strategy-selection, supervised-fine-tuning, news-ablation"
---

## Key insight
A language-model agent, fine-tuned and then trained with reinforcement learning, selects among option strategy families using a market state built from option-implied measures (the volatility, skewness and kurtosis of the implied return distribution across strikes and maturities). Over one six-month test it was the only tested policy with a positive return. Its most transferable finding is negative: keeping news in the agent's inputs during reinforcement learning turned the result from a gain into a loss.

## Method
The agent does not pick contracts. It chooses one of nine strategy families (grouped as directional, volatility, skewness and curvature trades) and parameters; deterministic code then selects contracts, sizes positions and hedges. The state is constructed from option-implied measures motivated by the Breeden and Litzenberger result that option prices encode the return distribution. Training: a frontier model generates trajectories on anonymised data (stock identity, price levels and dates masked); trajectories above a Sharpe threshold are used for supervised fine-tuning of an open model; reinforcement learning then optimises the policy with transaction costs in the environment. Baselines: equal-weight allocation, a GARCH-based rule, a threshold rule on the same features, gradient-boosted trees and logistic regression mapped to strategies, and a hindsight oracle.

## Data and sample
Options on nine large-capitalisation US stocks and SPY. Supervised phase 3 September to 29 November 2024; reinforcement-learning phase 2 December 2024 to 28 February 2025; test 3 March to 29 August 2025.

## Reported results
- Test period: total return 18.32%, annualised Sharpe ratio 1.60, maximum drawdown 8.96%.
- Every rule-based and supervised baseline lost money; the gradient-boosted and logistic policies lost 49.78% and 55.45%.
- With news kept during reinforcement learning: total return -2.72%, maximum drawdown 31.69%.
- Supervised fine-tuning alone (with news): -10.19% return, Sharpe -1.25; reinforcement learning on the same inputs improved this to -2.72% and -0.16.
- No ablation removes the option-implied features, so their contribution is not isolated.

## Signal construction
Not a signal for a perpetual bot as published. The reusable parts are:
- State design: summarise the option surface as a handful of implied moments per tenor (at-the-money volatility, 25-delta risk reversal, butterfly, term slope) and feed those, not raw chains, to a learning agent.
- Action design: let the learned policy choose among a small set of rule templates and leave sizing and execution to deterministic code.
- Leakage control: mask asset identity, price level and calendar time when generating training trajectories.
- Treat text inputs as a separate experiment; here they hurt out of sample.

## Relevance to SOL perpetuals at minutes to hours
The trading problem differs (multi-leg equity option positions held for days). The design lessons carry to an agent that trades a SOL perpetual with BTC and ETH option-implied moments in its state. The size of the baseline losses is a reminder that mapping return forecasts from implied features to trades through fixed rules performed badly in this environment. Reinforcement learning methods as such are covered in topic 24.

## Caveats
One six-month test window on ten underlyings, a three-month training window for each stage, and a single run reported in the pages read: weak evidence, with high risk that the result reflects one market regime. Costs follow the authors' execution model, which was not examined here. The frontier-model teacher may carry knowledge of the period despite masking. Preprint, not peer reviewed; a specific fine-tuned model that others cannot easily reproduce.
