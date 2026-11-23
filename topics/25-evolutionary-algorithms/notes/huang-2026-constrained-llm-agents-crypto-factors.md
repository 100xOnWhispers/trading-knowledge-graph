---
title: "From Hypotheses to Factors: Constrained LLM Agents in Cryptocurrency Markets"
authors: "Huang, Yikuan; Fan, Zheqi; Hu, Kaiqi; Ye, Yifan"
year: 2026
venue: "arXiv preprint 2604.26747v1"
url: "https://arxiv.org/pdf/2604.26747"
pdf: "sources/25-evolutionary-algorithms/huang-2026-constrained-llm-agents-crypto-factors.pdf"
access: "full-text"
source_type: "working-paper"
evidence_grade: "C"
topic: "25-evolutionary-algorithms"
asset_class: "crypto"
horizon: "daily"
tags: "llm-agent, factor-discovery, crypto-cross-section, constrained-dsl, selection-gates, audit-trail, capacity"
---

## Key insight
An LLM agent searching for crypto factors is kept honest by construction: it can only write formulas in a restricted point-in-time language, it cannot touch data splits, costs or pass/fail thresholds, and every hypothesis, including failures, is appended to a permanent trace. Under that protocol a combined long-short portfolio selected on 2020 to 2022 data earned a Sharpe ratio of 1.55 in 2024 onward. The edge sits in small, illiquid tokens and disappears under market-cap weighting.

## Method
Factor discovery is framed as sequential hypothesis search. Each round the agent (GPT-5.4 with a fixed system prompt) reads the trace of earlier candidates and metrics, states a falsifiable hypothesis, and maps it to a recipe in a domain-specific language supporting cross-sectional ranks, time-series transforms, nonlinear transforms and linear combinations. A deterministic engine computes the signal and applies a gate fixed before the round: training-period mean IC and IC t-statistic must exceed preset thresholds. Passing candidates enter a hold pool; the agent curates a smaller "good" pool for strength and diversity of mechanism. After the search stops, the good factors are standardized by date and combined by ridge regression fit on training data only. Validation metrics are recorded but never used for the gate. Target: return from t+1 to t+2, so a signal formed at t is not filled at the same close.

## Data and sample
Daily CoinMarketCap panel (price, volume, market cap), January 2020 to December 2025. Tokens with under 180 days of history or volume below a threshold are removed. Training 2020 to 2022, validation 2023, out of sample 2024 onward. Five search rounds, 25 single factors.

## Reported results
- Ridge-combined equal-weighted long-short portfolio, out of sample, after 5 basis points one-way cost: 44.55% annualized return, Sharpe 1.55.
- The market-cap-weighted version "performs poorly".
- Top single factors by out-of-sample Sharpe range from 2.41 down to 1.70; all combine small size, low volume or low volatility, and high intraday range, some with lagged momentum.
- The agent's own reading of its failures: changes in range and recoveries in volume are noisy; level-based scarcity and attention measures are more stable.
- A fee-sensitivity table lists Sharpe 0.57, 0.52 and 0.46 at fee rates of 0.1%, 0.2% and 0.3%; its return column does not match the headline figures in scale and the paper does not explain the units.

## Signal construction
The headline factors are cross-sectional and cannot be computed for one instrument. What a bot can take is the protocol: (1) a formula language that cannot express look-ahead, (2) gates fixed before search and applied only to training data, (3) an append-only log of every candidate, (4) a final combination fit once, on training data.

## Relevance to SOL perpetuals at minutes to hours
Low for signals: daily data, spot tokens, small-cap effects that SOL does not share. High for process. This is the only crypto-specific source found that pairs an LLM search with a fixed, auditable evaluation contract, and the trace gives the trial count that any later deflation of results requires.

## Caveats
Eight-page paper. CoinMarketCap daily closes are not tradable prices, short-selling small tokens is often impossible, and equal weighting across illiquid names overstates capacity, as the authors concede. Five basis points is a low cost for such tokens. No deflated Sharpe or other multiple-testing adjustment is reported, and the number of candidates that failed the gate is not given in the text I read. The inconsistency in the fee table is unresolved.
