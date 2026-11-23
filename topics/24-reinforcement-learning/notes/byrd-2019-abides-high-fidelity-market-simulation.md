---
title: "ABIDES: Towards High-Fidelity Market Simulation for AI Research"
authors: "Byrd, David; Hybinette, Maria; Balch, Tucker Hybinette"
year: 2019
venue: "arXiv:1904.12066v1"
url: "https://arxiv.org/pdf/1904.12066"
pdf: "sources/24-reinforcement-learning/byrd-2019-abides-high-fidelity-market-simulation.pdf"
access: "full-text"
source_type: "working-paper"
evidence_grade: "C"
topic: "24-reinforcement-learning"
asset_class: "equities"
horizon: "tick"
tags: "market-simulator, agent-based, multi-agent, market-impact, latency, counterfactual, sim-to-real, abides"
---

## Key insight
Replaying history cannot answer "what would the market have done if I had traded", because recorded prices do not react to the agent. ABIDES is an open agent-based discrete-event simulator built to supply that reaction: an exchange agent with a real matching engine, thousands of background agents, and per-agent latency. It is the reference open-source environment for RL research where the agent's own impact matters, and the base for later RL wrappers such as ABIDES-Gym. Its realism depends entirely on how the background agents are specified.

## Method
A simulation kernel delivers timestamped messages between agents at nanosecond resolution. The exchange agent keeps limit order books and speaks a message protocol modeled on NASDAQ ITCH and OUCH. A pairwise latency matrix plus noise model and per-agent computation delays determine when each message arrives. Agents see the market only through messages. Background agents are zero-intelligence-style traders whose value belief mixes a prior with a noisy observation of the most recent historical trade supplied by a "data oracle", and who place limit orders that arbitrage the simulated price toward that belief; the simulated price therefore tracks a chosen historical day while still reacting to injected orders. An experimental agent is added on top.

## Data and sample
Simulations anchored to single historical days (examples shown: IBM on 30 September 2008, MSFT on 24 June 2016). The impact study uses sixty experimental trials. No large-sample calibration is reported.

## Reported results
- Simulated trade prices from the background population closely follow the historical intraday path on the two example days (shown graphically).
- Market impact case study: one "impact agent" places a single large market order at 10:00, sized as a fraction ("greed") of near-touch liquidity. Price impact grows with order size and persists well after the order. Average profit rose from 2,633 USD at greed 0.3 to 12,502 USD at greed 1.9, while profit per share fell from 2.14 USD to 1.60 USD; correlation between profit per share and trade size was -0.31 across sixty trials.
- The paper lists intended uses: latency and co-location studies, impact of large orders, and training ML-based trading agents.

## Signal construction
Not a signal. It is infrastructure for testing whether a policy survives its own footprint. A bot-building workflow would use it (or a comparable simulator) to: (1) replay a day with background agents anchored to recorded prices, (2) inject the candidate policy's orders with realistic latency, (3) compare P&L with and without the policy's impact.

## Relevance to SOL perpetuals at minutes to hours
For a small directional account trading at minutes to hours on signals from large venues, pure replay with observed bid and ask is usually an adequate first approximation, and a multi-agent simulator is more machinery than the problem needs. It becomes relevant on Kalshi specifically: the book is thin, so even modest orders can consume the touch, and a replay backtest will overstate fills. ABIDES is equity-specific (ITCH-style messages, one symbol per background agent, no funding, margin or liquidation), so crypto perps would require new exchange and agent code. The transferable idea is the with-impact versus without-impact comparison.

## Caveats
The background agents are anchored to historical trades, so the simulator reproduces the price path by construction; that is not validation of microstructure realism (spread, depth, order flow autocorrelation), which the paper does not test. Impact results come from sixty trials with zero-intelligence counterparties and are illustrative. Later work (for example Noble, Rosenbaum and Souilmi, 2026) shows that fill and impact realism requires calibration this paper does not attempt. Preprint; the authors describe the results as preliminary.
