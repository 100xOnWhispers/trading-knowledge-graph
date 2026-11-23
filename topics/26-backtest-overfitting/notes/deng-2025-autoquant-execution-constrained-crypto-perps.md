---
title: "AutoQuant: An Auditable Expert-System Framework for Execution-Constrained Auto-Tuning in Cryptocurrency Perpetual Futures"
authors: "Deng, Kaihong"
year: 2025
venue: "arXiv preprint 2512.22476 (v3, August 2026; marked as submitted to Expert Systems with Applications)"
url: "https://arxiv.org/pdf/2512.22476"
pdf: "sources/26-backtest-overfitting/deng-2025-autoquant-execution-constrained-crypto-perps.pdf"
access: "full-text"
source_type: "working-paper"
evidence_grade: "C"
topic: "26-backtest-overfitting"
asset_class: "crypto"
horizon: "hours"
tags: "perpetual-futures, funding-alignment, look-ahead-bias, cost-modelling, pbo, bayesian-optimization"
---

## Key insight
In perpetual-futures backtests, the result is as much a product of execution timing, funding alignment and cost assumptions as of the signal. The paper encodes these as hard rules in the backtest engine (signal at bar close, execution one bar later, only funding values already visible, fees plus slippage plus funding) and shows that fee-only or zero-cost runs materially inflate performance. Even with those rules, repeated parameter search leaves a high probability of backtest overfitting.

## Method
- "STRICT4H" semantics: a signal computed at the close of 4-hour bar t sets the exposure held during bar t+1; turnover costs are proportional to the change in exposure; funding accrues on notional using the 8-hour funding series aligned to the 4-hour grid by carry-forward, with no backfill from later updates.
- Signal family: momentum (EMA spans), mean-reversion (Bollinger), volatility and risk overlays, and a funding-bias rule that raises entry thresholds when carry is adverse.
- Stage I: Bayesian (TPE) search of 40 or 120 trials on a training window. Stage II: re-evaluation of candidates across windows and a cost-scenario grid (taker fee 3, 4 or 6 basis points; funding multiplier 0.5, 1.0, 1.5; further 2x and 3x cost stresses), keeping only configurations that pass pre-set robustness rules.
- Diagnostics: a deflated-Sharpe-style check and CSCV/PBO on the Stage I pool. Optimizer comparison includes random search, differential evolution, a simple genetic algorithm and Gaussian-process Bayesian optimization.

## Data and sample
BTC/USDT perpetual (Binance, Bybit and OKX data) from 2019-09-08 to 2025-10-14 (13,368 four-hour returns); ETH/USDT 2021-12-31 to 2025-11-24; SOL/USDT and AVAX/USDT 2021-01-01 to 2025-12-16. Four-hour OHLCV bars with matched 8-hour funding rates. Small-account simulation with linear costs; market impact excluded.

## Reported results
- Cost ladder for one fixed BTC configuration: fees plus slippage plus funding gives Sharpe 2.049 and CAGR 2.726 (decimal); fee-only gives Sharpe 2.506 and CAGR 4.308; zero-cost gives Sharpe 2.711 and CAGR 5.225.
- CSCV/PBO on the top-40 Stage I candidates: PBO = 0.586 (8 segments, 70 combinatorial splits). The deflated-Sharpe-style check with an effective trial count between 360 and 3,240 is described as consistent with non-negligible search risk.
- SOL/USDT under stricter costs: one-stage top-1 Sharpe 2.625 in training, 3.398 in validation, 1.747 post-2024; two-stage selection 3.013, 4.208 and 2.301, with lower training drawdown (0.152 against 0.319).
- Two-stage screening does not guarantee higher returns; it more often selects lower-drawdown configurations.
- The Gaussian-process optimizer was strongest on the training window, but its candidates failed the validation screens.

## Signal construction
Not a signal; a backtest specification. The rules a bot's simulator should enforce: decide on closed bars only; fill no earlier than the next bar; apply funding only at settlement times using rates known at that time; charge fee and slippage on every change in exposure; re-run every candidate under a grid of worse cost assumptions; log all trials.

## Relevance to SOL perpetuals at minutes to hours
The only source here that treats perpetual-specific backtest errors on SOL itself. The funding-alignment rule maps directly to Kalshi's 8-hour funding. The cost ladder is the useful quantitative message: on 4-hour bars, omitting slippage and funding raised Sharpe by roughly a fifth to a third; at minute horizons, where turnover is far higher, the inflation will be larger. The PBO of 0.586 after a modest Bayesian search is a realistic picture of what an automated tuner produces.

## Caveats
Single-author preprint, not peer reviewed. Reported Sharpe ratios of 2 to 4 and triple-digit annual returns for simple EMA and Bollinger rules are implausibly high for live trading and should be read as diagnostics, as the author states. Bar-level fills with linear costs; no order book, queue or impact. Offshore USDT-margined contracts, not a US venue. Post-2024 results are still within the period the author could observe while designing the study.
