---
title: "Risk-Based Auto-Deleveraging"
authors: "Campbell, Steven; Hey, Natascha; Moallemi, Ciamac C.; Nutz, Marcel"
year: 2026
venue: "arXiv preprint 2603.15963 (v2, July 2026)"
url: "https://arxiv.org/pdf/2603.15963"
pdf: "sources/04-open-interest-liquidations/campbell-2026-risk-based-auto-deleveraging.pdf"
access: "full-text"
source_type: "working-paper"
evidence_grade: "B"
topic: "04-open-interest-liquidations"
asset_class: "crypto"
horizon: "seconds"
tags: "auto-deleveraging, risk-management, cross-margin, october-2025, hyperliquid, optimization"
---

## Key insight
ADL is posed as an optimization: choose position reductions that minimize the exchange's risk of future equity shortfalls. In a single-asset, isolated-margin setting the optimal rule for every monotone risk measure is "minimax leverage": cut the most levered accounts first and equalize leverage by water-filling. With cross-margined portfolios, gross leverage is misleading and the right ranking uses leverage adjusted for exposure to the dominant risk factor, so well-hedged portfolios are deleveraged less. Measured against this benchmark, Hyperliquid's realized allocation on 10 October 2025 removed about a third of the reducible risk.

## Method
Theory plus an exchange-scale numerical study. The single-asset result is proved for expected loss, CVaR and general monotone risk measures; the policy is shown to be distribution-free, wash-trade resistant, Sybil resistant and path-independent. The multi-asset problem under expected loss separates across accounts via asset-level shadow prices and is solved with ADMM on a sample-average approximation; under a single risk factor the solution is again water-filling in factor-adjusted leverage. For the empirical exercise the authors reconstruct pre-event account states and compare three allocations for the first ADL wave using sampled expected loss over 50 independent sets of 128 geometric Brownian motion price-drop scenarios.

## Data and sample
Hyperliquid, 10 October 2025. Tick-level trades from the public REST API (time, user address, coin, signed size, side, direction label, execution price, liquidation mark price) plus account-level state variables. A 75-coin core universe is used.

## Reported results
- Realized ADL notional on the 75-coin universe: USD 2.047 billion on the day, concentrated in the window 21:16 to 21:21 UTC.
- Three dominant waves began at 21:16:05, 21:16:56 and 21:17:06 UTC. Wave one: USD 176.9 million, dominated by HYPE, PUMP and FARTCOIN. Wave two: USD 93.3 million. Wave three: USD 386.6 million, concentrated in ETH, SOL, BTC and XRP.
- BTC, ETH and SOL fell roughly 10 to 20% relative to their intraday average; several thinner names lost more than half.
- First-wave relative risk reduction: Hyperliquid 0.325, water-filling 0.901, risk-optimal 1.000. Mean sampled loss USD 538.3 million, 532.2 million and 531.2 million respectively. Water-filling ran in 3.70 seconds; the risk-optimal solution took about 115,000 seconds to full convergence, though it reached 0.952 of the improvement by iteration 500.

## Signal construction
Not a directional signal. Two uses: (1) the event timeline gives second-level timestamps for the Hyperliquid ADL waves, useful for labelling the cascade in back-tests; (2) the factor-adjusted leverage idea is a template for the bot's own risk measure, namely exposure to the common crypto factor per unit of equity rather than gross notional.

## Relevance to SOL perpetuals at minutes to hours
SOL was among the main coins in the largest ADL wave, so SOL positions were directly affected. The sequencing matters: thin, highly levered names were deleveraged first, and majors followed about a minute later, which suggests stress in long-tail perps can lead stress in SOL by tens of seconds during a cascade. That ordering comes from one event and should be checked on other episodes. The paper also shows that the queue rule in production does not approximate risk-optimal behavior, so the bot should not assume ADL will spare low-risk hedged accounts.

## Caveats
Preprint. Pre-event account states are reconstructed, not observed. Evaluation uses simulated geometric Brownian motion scenarios rather than realized post-event paths. One author discloses advisory roles with firms in the sector. The comparison covers the first wave in the main text; the third-wave exercise is in an appendix not read here.
