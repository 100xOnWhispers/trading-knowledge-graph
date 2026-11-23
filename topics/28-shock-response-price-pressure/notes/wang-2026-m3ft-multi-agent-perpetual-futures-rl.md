---
title: "M3FT: Micro-Macro-Micro Reasoning for Multi-Agent Cryptocurrency Perpetual Futures Trading"
authors: "Wang, Jiashun; Wang, Beile; Gan, Guangyan; Zhang, Wentao; Li, Siguang; Sun, Shuo; Lu, Yunbo; Cong, Lin William"
year: 2026
venue: "arXiv:2611.10586v1 (7 November 2026, preprint)"
url: "https://arxiv.org/pdf/2611.10586"
pdf: "sources/28-shock-response-price-pressure/wang-2026-m3ft-multi-agent-perpetual-futures-rl.pdf"
access: "full-text"
source_type: "working-paper"
evidence_grade: "C"
topic: "28-shock-response-price-pressure"
asset_class: "crypto"
horizon: "daily"
tags: "reinforcement-learning, llm-agents, perp-state-features, funding, premium, out-of-sample, negative-baseline"
---

## Key insight
A reinforcement-learning study that feeds perp-state variables (funding, premium, taker-buy activity) to trading policies for four Binance perpetuals and reports a chronological held-out test with fees and funding charged. For this repository the informative result is the baseline, not the proposed system: every numerical-only RL policy given those inputs lost money out of sample. The language-mediated variant the authors propose has positive mean returns, but the spread across four random seeds is larger than the mean, so the improvement is not statistically established.

## Method
Three levels are compared. M1: a language model maps a market summary directly to positions. M2: numerical multi-agent or single-agent RL (MATD3, MADDPG, PPO, an adapted A2C-LSTM) maps numerical states to target exposures. M3: an intermediate "macro" representation is inserted, either rule-based (a Bollinger-band state from a 20-day mean and two standard deviations, or another rule state) or language-based (M3FT: LLM agents write market interpretations, exchange views, review risk and retrieve past cases; the text is embedded into 64 dimensions and joined to the numerical state). The simulator is a shared cross-margin account with a threefold notional budget, a fee rate of 0.0004, mark-price profit and loss, funding payments and a liquidation check. Decisions use information at the end of a UTC day and execute at the first price of the next daily bar. Component ablations remove the communication and review agents, or the experience pool. There is no ablation of the funding or premium inputs.

## Data and sample
Daily Binance USDT-margined perpetual records for BTCUSDT, ETHUSDT, BNBUSDT and DOTUSDT, 31 January 2021 to 31 July 2026 (2,008 days). Training to 18 May 2024, validation to 24 June 2025, test afterwards. State features: price-derived features, volatility, volume change, taker-buy activity, funding, premium, cross-asset dependence and account state. Four seeds per method.

## Reported results
Held-out test, mean plus or minus standard deviation across seeds:
- Numerical RL: MATD3 -9.06% (13.11), MADDPG -7.49% (3.88), PPO -0.85% (2.85), A2C-LSTM -0.89% (15.85); Sharpe ratios -0.67, -0.80, -0.61 and 0.20.
- Rule-based macro state plus MADDPG: Bollinger-state -9.09% (16.00); rule-state -2.41% (14.61).
- Direct LLM: +4.55% (3.26) and +4.55% (16.61); Sharpe 0.34 and 0.23.
- M3FT variants: +4.25% to +9.87% with standard deviations of 10 to 18 points; Sharpe -0.12 to 0.37; maximum drawdown 19% to 30%. The two MADDPG variants sit at the action boundary in about 77% to 81% of decisions with gross leverage near 2.5 to 2.7.
- Removing the experience pool turns the mean return to -6.27%.
- No buy-and-hold or simple-rule benchmark return for the test period was found in the text.
- Scope record: horizon one day; conditioning variables include funding and premium among many features; sign not identifiable (black-box policy); fees and funding charged; chronological out-of-sample test.

## Signal construction
Not a signal. It is evidence on method: a model-free RL policy on daily perp-state features does not find a robust edge, and a contrarian Bollinger state as an intermediate feature does no better. For the bot, perp-state variables are better tested first as explicit conditioning variables in event studies and regressions, where the sign and size can be read, before being handed to a policy learner.

## Relevance to SOL perpetuals at minutes to hours
Limited by frequency and universe: daily decisions, no SOL, no intraday data. The authors list higher-frequency observations and execution-aware simulation as future work. It does show the evaluation standard to require of any ML or RL claim in this area: chronological split, fees and funding charged, several seeds, and dispersion reported. Read with FineFT (Qin et al., noted in topics 03 and 04) and the backtest-overfitting study by Gort et al. in topic 24.

## Caveats
Preprint, days old at the time of reading. Four assets, one test period of about thirteen months, four seeds. Seed dispersion exceeds the differences between methods. No test isolates the contribution of funding or premium. LLM providers and versions affect results. The next-bar execution proxy ignores depth and slippage. Possible LLM look-ahead about the test period is not discussed in the parts read.
