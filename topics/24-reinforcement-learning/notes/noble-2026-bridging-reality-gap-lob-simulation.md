---
title: "Bridging the Reality Gap in Limit Order Book Simulation"
authors: "Noble, Patrick; Rosenbaum, Mathieu; Souilmi, Saad"
year: 2026
venue: "arXiv:2603.24137v1"
url: "https://arxiv.org/pdf/2603.24137"
pdf: "sources/24-reinforcement-learning/noble-2026-bridging-reality-gap-lob-simulation.pdf"
access: "full-text"
source_type: "working-paper"
evidence_grade: "B"
topic: "24-reinforcement-learning"
asset_class: "equities"
horizon: "tick"
tags: "market-simulator, queue-reactive, sim-to-real, market-impact, latency-races, fill-probability, self-impact, large-tick, order-book-imbalance"
---

## Key insight
A simulator used to train or test a trading policy must be interactive (the market reacts to the policy's orders) and must reproduce three things that naive replay and simple stochastic models miss: realistic event timing including latency races, fill probability that falls when the signal is strong, and the strategy's own market impact with partial reversion. With those in place, strategies that look increasingly profitable as size and aggressiveness grow in a no-impact simulation instead flatten or decline. The paper gives a calibratable recipe for large-tick assets, co-authored by a practitioner at Jump Trading.

## Method
Starting point: the queue-reactive (QR) model, a Markov jump process where the rates of limit orders, cancellations and market orders depend on the book state. Three modifications:
1. Projection: condition event probabilities on a low-dimensional state (spread and volume imbalance) instead of full per-queue sizes, so every state has enough data.
2. Timing: replace exponential inter-event times with an empirical distribution. This exposes a pronounced mode at the exchange round-trip latency, interpreted as simultaneous reactions to a common trigger. Consequence for fills: when the next event arrives within the round-trip latency of the strategy's order, the strategy is in a race and its fill probability should be below one, and lower for stronger signals.
3. Impact feedback: a state variable `phi_t` accumulates signed trade flow through a power-law decay kernel and biases subsequent trade direction toward mean reversion, producing a concave rise in price during a metaorder and partial reversion afterwards. An exogenous alpha signal can be injected through the same bias term (`b_t = m * phi_t - lambda * alpha_t`).

## Data and sample
Databento MBP-10 data, December 2023 to December 2025, for four large-tick S&P 500 stocks trading near 30 USD: INTC, VZ, T and PFE (results shown for PFE, others in the appendix). First and last 30 minutes of each day excluded. Parameters are re-estimated on four disjoint six-month windows and reported as stable.

## Reported results
- Baseline validation: the simulator reproduces event-type mix, book states at trades, activity levels, volatility and the return distribution (shown graphically).
- The unmodified model shows no concave impact and no reversion, "fundamentally at odds with empirical observations"; the feedback kernel restores both.
- Mid-frequency case study (Ornstein-Uhlenbeck alpha): without impact, P&L rises monotonically with maximum inventory; with impact, P&L flattens or declines beyond a certain inventory.
- High-frequency imbalance strategy: P&L with self-impact flattens earlier and lower than without; a simulator ignoring self-impact "will systematically overstate profitability" most in aggressive parameterizations.

## Signal construction
Not a signal. It specifies what a training or test environment for an execution-aware agent needs:
- book state summarized by spread and top-of-book imbalance;
- event rates and inter-event time distributions estimated conditional on that state;
- a fill-probability haircut for orders sent on signals that competitors also see;
- a decaying signed-flow state that includes the agent's own trades.

## Relevance to SOL perpetuals at minutes to hours
For entry and exit timing at minutes to hours the full simulator is optional; the two cheap lessons are not. First, any backtest that assumes a marketable order always fills at the displayed touch is optimistic exactly when the signal is strongest, because others react to the same Binance move. Second, P&L should be reported with a self-impact term that grows with position relative to book depth; on a thin Kalshi book the binding constraint is likely to be touch depth, as in the paper's case studies. The model is built for large-tick assets; whether the Kalshi contract qualifies depends on its tick size relative to spread and needs measurement.

## Caveats
Four US large-tick equities; no crypto, no perps, no 24-hour market. Validation is against marginal statistics, not against live P&L of a real strategy. Race outcomes cannot be identified from public data, as the authors state, so the fill haircut is a modeling choice. The case-study strategies are stylized. Preprint. No RL agent is trained in the paper; it concerns the environment that determines whether a learned policy transfers.
