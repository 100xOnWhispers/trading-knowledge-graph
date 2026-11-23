---
title: "When Does Order Flow Matter? State-Dependent L2 Liquidity-State Transitions in Crypto Futures"
authors: "Jeon, Joohyoung"
year: 2026
venue: "arXiv:2607.09230v1"
url: "https://arxiv.org/pdf/2607.09230"
pdf: "sources/07-order-book-imbalance/jeon-2026-order-flow-state-dependent-crypto-futures.pdf"
access: "full-text"
source_type: "working-paper"
evidence_grade: "B"
topic: "07-order-book-imbalance"
asset_class: "crypto"
horizon: "minutes"
tags: "liquidity-state, top-20-imbalance, depth, spread, binance-futures, macro-events, order-flow, gradient-boosting, permutation-test"
---

## Key insight
Around scheduled macro releases on Binance BTC and ETH perpetuals, the state of the L2 book before the event (spread, top-20 depth, top-20 imbalance) is the first-order predictor of the book's liquidity regime one and five minutes later. Linear models on continuous book features do not beat a coarse three-state label; a shallow nonlinear model does. Trade flow adds value only on top of the book-state model, and only robustly for ETH, most strongly when the pre-event book is stressed. The target is the liquidity regime, not price direction.

## Method
Each contract-minute gets a liquidity state (calm, mixed, stressed) from terciles of relative spread, negated top-20 depth, and absolute top-20 imbalance, with thresholds fitted per symbol on training folds only. The task is to predict the post-event state from pre-event information. Layers are admitted only if they improve on the previous one: marginal baseline, coarse pre-event state, multinomial and ordered logit on continuous L2 features, a histogram gradient-boosted "L2-shape" model, and an order-flow overlay. Evaluation uses 40 rolling monthly out-of-sample folds, event-clustered bootstrap, and blocked permutation (flow-shuffle) nulls. Scores are joint improvements in negative log-likelihood and Brier score.

## Data and sample
Binance BTCUSDT and ETHUSDT perpetuals, January 2023 to mid-2026; top-20 book snapshots once per minute from a vendor archive, aggregate trade-flow records, and a commercial macro calendar (timestamps only). 47,513 windows per horizon, of which 18,631 are event windows, from 9,773 scheduled events.

## Reported results
- Coarse pre-event state against the marginal baseline: +0.034 (1 minute) and +0.045 (5 minutes).
- Multinomial and ordered logit are worse than the coarse state (about -0.05 at 1 minute, intervals entirely below zero).
- Nonlinear L2-shape model against the coarse state: +0.044 and +0.060.
- Order-flow overlay against L2-only: pooled +0.010 at both horizons; ETH +0.020 and +0.016 (clears the null); BTC +0.001 and +0.003 (not established).
- The combined three-descriptor state is more predictive than any single descriptor (0.048 against 0.033 at five minutes).
- Pre-event states are calm, mixed and stressed in shares of about 0.21, 0.54 and 0.25.
- The author states that the study reports no trading policy or profit and that a price-direction target on the same panel is untested.

## Signal construction
Not a directional signal. It is a regime classifier: each minute compute relative spread, summed top-20 depth, and absolute imbalance over 20 levels (the paper's exact formula was not confirmed; the standard form is `|sum bid size - sum ask size| / (sum bid size + sum ask size)`); convert each to a tercile using trailing training data; count how many are in the "illiquid" tercile (capped at two) to label calm, mixed or stressed. Use the label to condition position size, execution style, and the weight given to flow-based signals.

## Relevance to SOL perpetuals at minutes to hours
The horizon, venue type and period match the bot better than most microstructure papers. The practical design rule is "state first": measure the book regime, then ask whether flow adds anything in that regime. The asymmetry between ETH and BTC implies the SOL result cannot be assumed either way and should be tested with the same layered protocol. The regime label is also a natural gate around macro releases, which are handled in other topics.

## Caveats
Single-author preprint. Two assets; one-minute snapshots cannot see queue dynamics. Liquidity-state target, so nothing here shows that imbalance predicts SOL returns. Effect sizes are in proper-score units and not translated into basis points.
