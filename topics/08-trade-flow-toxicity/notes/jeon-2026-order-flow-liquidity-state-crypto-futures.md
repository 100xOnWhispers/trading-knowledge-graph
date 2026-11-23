---
title: "When Does Order Flow Matter? State-Dependent L2 Liquidity-State Transitions in Crypto Futures"
authors: "Jeon, Joohyoung"
year: 2026
venue: "arXiv 2607.09230v1 (July 2026)"
url: "https://arxiv.org/pdf/2607.09230"
pdf: "sources/08-trade-flow-toxicity/jeon-2026-order-flow-liquidity-state-crypto-futures.pdf"
access: "full-text"
source_type: "working-paper"
evidence_grade: "B"
topic: "08-trade-flow-toxicity"
asset_class: "crypto"
horizon: "minutes"
tags: "order-flow, liquidity-regime, incremental-value, machine-learning, permutation-test, perpetuals, macro-events"
---

## Key insight
In windows around scheduled macro events on Binance BTC and ETH futures, the liquidity state of the book before the event is the main predictor of the liquidity state after it. Trade-flow features add value only when layered on top of an order-book state model, never as a replacement, and the gain is not robust across symbols: it is present for ETH, largest under stressed pre-event liquidity, and not established for BTC. The paper proposes a "state-first" rule: any flow, reinforcement-learning or language-model layer should be credited only for what it adds over a book-state baseline.

## Method
The target is a discrete post-event liquidity state (calm, mixed, stressed) built from terciles of relative spread, top-20 depth and top-20 imbalance, at 1-minute and 5-minute horizons. It is not a price-direction label. Models are staged on one panel: marginal baseline, coarse pre-event state, multinomial and ordered logits on continuous L2 features, a shallow nonlinear L2-shape model, and an order-flow overlay. Each layer must beat the one below under rolling monthly out-of-sample folds, event-clustered bootstrap and blocked permutation tests; the flow overlay is compared against a flow-shuffle null. Scores are joint improvements in negative log-likelihood and Brier score.

## Data and sample
Binance BTCUSDT and ETHUSDT futures, 2023 to 2026, top-20 L2 order book data, trade-flow records and macro-event windows with matched non-event controls.

## Reported results
- Coarse pre-event state versus marginal: +0.034 (1 minute) and +0.045 (5 minutes).
- Multinomial and ordered logits on continuous L2 features are worse than the coarse state (about -0.05 at 1 minute), with intervals entirely below zero.
- The nonlinear L2-shape model adds +0.044 (1 minute) and +0.060 (5 minutes) over the coarse state.
- Order-flow overlay, pooled: +0.010 at both horizons against a null 95th percentile of +0.004 and +0.003.
- BTC: +0.001 and +0.003 against null thresholds of +0.002, reported as not established. ETH: +0.020 and +0.016 against +0.006 and +0.003, clears the null.

## Signal construction
Not a direction signal. It defines a liquidity-regime feature and an evaluation rule. Regime: classify each minute as calm, mixed or stressed from terciles of relative spread, top-20 depth and top-20 imbalance on the leading venue. Evaluation rule: fit the book-state model first, then add taker-flow features and keep them only if out-of-sample log-loss improves by more than a flow-shuffled placebo.

## Relevance to SOL perpetuals at minutes to hours
Two points transfer. First, the incremental value of flow features is asset-specific, so a result on BTC or ETH cannot be assumed for SOL; the same staged test should be run on SOL directly. Second, flow information was most useful when the book was already stressed, which suggests interacting flow imbalance with a liquidity-state variable rather than using it unconditionally. The flow-shuffle null is a cheap, reusable placebo for any SOL flow feature. Because the target here is liquidity state, the paper says nothing about whether flow predicts SOL returns.

## Caveats
Single author, unrefereed. Two assets, event windows only, and a liquidity target. The trade-flow feature definitions were not examined in detail in this session. The order-book layers belong to topic 07; this note covers the incremental-flow result only.
