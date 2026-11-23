---
title: "M3FT: Micro-Macro-Micro Reasoning for Multi-Agent Cryptocurrency Perpetual Futures Trading"
authors: "Wang, Jiashun; Wang, Beile; Gan, Guangyan; Zhang, Wentao; Li, Siguang; Sun, Shuo; Lu, Yunbo; Cong, Lin William"
year: 2026
venue: "arXiv preprint 2611.10586, version 1 (7 November 2026)"
url: "https://arxiv.org/pdf/2611.10586"
pdf: "sources/30-macro-state-intraday-transmission/wang-2026-m3ft-micro-macro-micro-perpetual-futures.pdf"
access: "full-text"
source_type: "working-paper"
evidence_grade: "C"
topic: "30-macro-state-intraday-transmission"
asset_class: "crypto"
horizon: "daily"
tags: "reinforcement-learning, multi-agent, language-model, market-state-layer, perpetual-futures, ablation, regime-gate"
---

## Key insight
Inserting an explicit market-state layer between raw numerical features and a reinforcement-learning policy improved held-out returns on crypto perpetuals in this study, but only when the layer was a language-model interpretation; hand-built rule-based state layers did not help. The word macro in the title means a market-level abstraction of exchange and account data. The authors say explicitly that it is not macroeconomic news. It is included in this topic as the closest available ablation of a regime layer on top of an RL trader for perpetual futures, and as a reminder of how weak such evidence still is.

## Method
Three stages. Deterministic code builds numerical states per asset and across assets (returns, volatility, volume change, taker-buy activity, funding, premium, cross-asset dependence, account state). Language-model agents (a market interpreter, an asset communicator, a risk reviewer, with an experience pool of past inferences and outcomes) write market-level assessments, refreshed at scheduled checkpoints or when volatility, correlation or aggregate funding change substantially. Encoded text is concatenated with numerical states to condition one actor per asset; centralised critics see the joint portfolio (MADDPG and MATD3). The environment charges a fee rate of 0.0004, funding payments and a conservative liquidation proxy; leverage multiplier 3. Comparisons: direct language-model trading, numerical-only RL (MADDPG, MATD3, PPO, an adapted CPTS core), and RL with two deterministic state layers (a nine-dimensional quartile rule state and a Bollinger state).

## Data and sample
Daily Binance USD-margined perpetual records for BTCUSDT, ETHUSDT, BNBUSDT and DOTUSDT, 31 January 2021 to 31 July 2026; training to 18 May 2024, validation to 24 June 2025, test afterwards. Six fixed 120-step test episodes per seed, four seeds. Post-2020. Daily bars, not intraday. SOL is not included. No external news or macro data.

## Reported results
- Numerical-only RL lost money on the test period: MATD3 -9.06 percent, MADDPG -7.49, PPO -0.85, CPTS core -0.89 (mean test return).
- Language-conditioned variants: DeepSeek+MADDPG +9.87, GPT+MADDPG +6.21, GPT+MATD3 +5.64 (Sharpe 0.34, drawdown 19.40 percent), DeepSeek+MATD3 +4.25. Direct language-model trading: +4.55.
- Rule-state + MADDPG -2.41; Bollinger-state + MADDPG -9.09.
- Dispersion across seeds is large: the best configuration is +9.87 with a standard deviation of 16.22 across four seeds, with action saturation of 81 percent and gross leverage 2.68. The authors state that cross-seed variation limits conclusions.
- Removing the experience pool turns the mean return negative; removing communication and review lowers it to +7.02 with a standard deviation of 25.07.

## Signal construction
Not a signal. A design pattern: compute market-state descriptors deterministically, then pass a compressed regime representation to the policy as extra state. The rule-state baseline (quartile bins of market variables estimated on the training period) is the cheap version a bot would build first; in this study it reduced losses relative to no state layer but stayed negative.

## Relevance to SOL perpetuals at minutes to hours
It bears on whether a regime gate should be an input to a learned policy. The honest reading is that the experiment cannot tell: four seeds, standard deviations larger than the means, daily bars and four coins. The numerical-only RL baselines losing money out of sample on perpetuals with realistic fees and funding is the more reliable finding and matches the caution in topic 24. No study was found that feeds macroeconomic state or event features to an RL or evolutionary trader at intraday frequency with an ablation.

## Caveats
Preprint. The language models may have seen the test period in training data, which is a look-ahead risk the paper's protocol cannot rule out. No statistical test of the differences. Mean test returns of a few percent over the test span with drawdowns near 20 to 40 percent. Daily data cannot speak to minutes-to-hours execution.
