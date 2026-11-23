---
title: "Artificial Intelligence in Equity and Crypto Markets: Progress, Profitability Evidence, and the Limits of Automated Investing"
authors: "Zhu, Linsen; Cai, Mengqing"
year: 2026
venue: "arXiv:2609.04917v1"
url: "https://arxiv.org/pdf/2609.04917"
pdf: "sources/24-reinforcement-learning/zhu-2026-ai-equity-crypto-profitability-limits.pdf"
access: "full-text"
source_type: "working-paper"
evidence_grade: "C"
topic: "24-reinforcement-learning"
asset_class: "multi"
horizon: "n/a"
tags: "critical-review, profitability-evidence, reinforcement-learning, perpetual-futures, funding, liquidation, simulation-gap, baselines, look-ahead, evaluation"
---

## Key insight
A critical review of public research through 31 August 2026 on machine learning, RL, language models and agents in equities and crypto (spot, perpetuals, on-chain). Its conclusion: technical progress is real but mostly upstream (prediction, text processing, portfolio design); evidence for durable net performance is thin; and no general AI architecture is shown to deliver persistent, cross-regime, capacity-aware net alpha. For RL specifically it argues that repeated interaction with a fixed historical tape is not interactive market evidence, and that perpetual futures need their own P&L accounting (funding and liquidation) before any backtest is meaningful.

## Method
Narrative critical review organized around an "alpha-translation chain": point-in-time information must yield a stable signal, feasible positions, executable orders and risk-adjusted returns after costs, and a claim is only as strong as the weakest link. The authors state it is not a systematic review: no registered protocol, no complete database retrieval, no formal risk-of-bias scoring, no pooled estimates. Markets are treated as four strata: equities and ETFs, centralized crypto spot, perpetual futures, and decentralized markets.

## Data and sample
No original data. 32 pages. Literature cutoff 31 August 2026.

## Reported results
Statements read in the RL and perpetuals sections:
- RL is appropriate "when current actions change future states or opportunities": inventory affecting later execution, trading changing costs, leverage changing liquidation risk.
- RL "magnifies the simulation problem". A typical backtest environment assumes a price taker filled at the next bar with a Markov state built from historical variables; under those assumptions an algorithm can learn simulator shortcuts, such as trading at a bar price unavailable in real time or exploiting a reward normalization fitted with future data.
- Crypto RL evidence is mixed: Borrageiro et al. (2022) is cited as a positive result; a PPO study on BTC/USDT minute data (Mahayana et al., 2022, not opened in this session) is cited as failing to beat buy and hold. The review adds that buy and hold is a high-beta, regime-dependent comparator, so beating it does not identify alpha.
- Recommended baselines for crypto RL: volatility-matched exposure, cash, momentum and carry, and a statement of whether funding and liquidation are modeled.
- Simplified perp P&L: `PnL = q_t (P_{t+1} - P_t) - q_t P_t f_t - C_t - LiqLoss`. Liquidation loss is discontinuous; a backtest on last-traded prices can report a path a margined account could not survive. A directional agent that ignores funding "can be right about spot direction and wrong about contract P&L".
- Perp-specific leakage: applying current contract specifications (funding interval, limits) to earlier periods; selecting the tradable universe with future liquidity.
- Repeated runs are required when RL training is stochastic; confidence intervals should respect time dependence.

## Signal construction
Not a signal. It supplies a reporting standard for the bot's backtests: gross and net return, volatility, drawdown, turnover, leverage, beta to the underlying, tail loss, and separate lines for funding, fees and liquidation; contract-level funding timestamps; mark-price based liquidation simulation; fee tier; venue downtime.

## Relevance to SOL perpetuals at minutes to hours
Directly on target as a checklist. Kalshi's contract is new, so the warning about back-applying current specifications matters in reverse: history from Binance or Bybit SOL perps has different funding caps, fees and margin rules and cannot be used as a proxy for Kalshi P&L without re-computing each term under Kalshi's rules. The baseline list (cash, volatility-matched long, momentum, carry) should be the standing comparison set for any RL policy in this repository.

## Caveats
A non-systematic review by two authors, not peer-reviewed; selection of studies is at the authors' discretion and the paper declares use of generative AI tools for literature discovery and drafting. The RL section is short and cites few primary RL studies; it is an argument about evidence standards more than a survey of RL results. Claims about individual cited papers were not verified against those papers here, except Borrageiro et al.
