---
title: "Regime-Aware Portfolio Management via Retrieval-Augmented LLM-Guided Expert Switching"
authors: "Asadi, Ahmad; Safabakhsh, Reza"
year: 2026
venue: "arXiv preprint arXiv:2608.28252v1 (cs.AI)"
url: "https://arxiv.org/pdf/2608.28252"
pdf: "sources/01-macro-regime-detection/asadi-2026-regime-aware-llm-expert-switching.pdf"
access: "full-text"
source_type: "working-paper"
evidence_grade: "C"
topic: "01-macro-regime-detection"
asset_class: "multi"
horizon: "multi-day"
tags: "reinforcement-learning, expert-switching, mixture-of-experts, retrieval, regime-conditioned-performance, crypto, large-language-model"
---

## Key insight
A recent example of the "one agent per regime" idea done without explicit regime labels. A pool of deep reinforcement learning portfolio agents is kept, and at each decision the system picks the agent that did best in past market situations most similar to the present one. On daily crypto, stock and currency panels the selector beat both a single fixed agent and "pick whoever did best last week". In crypto the improvement was small, and the selector did not beat the best standalone agents as reported in the paper's own table of individual results.

## Method
Five trained agents (A2C, DDPG, PPO, CrossQ, TQC) act as experts. A dual-stream Transformer variational autoencoder embeds asset-level and market-wide windows of L = 22 trading days. Offline, every historical window is stored with each expert's realised performance over the following H = 5 days. Online, the current embedding retrieves the nearest historical windows, and an instruction-tuned language model reads the retrieved performance records and names the expert to activate; it does not set portfolio weights. A switching threshold keeps the incumbent unless a candidate's estimated advantage exceeds a margin. Baselines: best fixed expert, and gating on the last five days' performance.

## Data and sample
Daily OHLCV for the 30 most liquid assets in each of three markets (cryptocurrencies, stocks, currency pairs), plus market indices; two crypto market indices are constructed by the authors. Stock histories run to 2026-05-29. Test-period dates and transaction-cost assumptions were not found in the sections I read: not confirmed. The per-expert "weeks dominant" counts sum to 55 weeks for crypto and 88 for stocks, which suggests test windows of about one year and 1.7 years (my inference).

## Reported results
Crypto, cumulative return / Sharpe / max drawdown:
- Best fixed 68% / 1.64 / -27%; recent-performance gating 69% / 1.66 / -27%; proposed selector 71% / 1.73 / -26%.
- Standalone experts in the same market: TQC 76.16% / 1.71 / -29%; DDPG 71.26% / 1.74 / -26%; A2C 63.00% / 1.61 / -25%. Which expert was best varied week by week: A2C in 34.5% of weeks, TQC in 32.7%.
Stocks: best fixed 26% / 0.74; recent gating 33% / 0.91; proposed 34% / 0.96.
Currencies: best fixed 3.2% / 0.71; recent gating -0.4% / -0.062; proposed 4.3% / 0.88.
The authors state that each market was evaluated with a single run and that competing methods were not always run under identical protocols.

## Signal construction
Not a ready signal; a design pattern. Keep several simple strategies running in shadow mode; log each one's forward performance together with a feature vector describing market conditions at the time; at decision time retrieve the k most similar past conditions and allocate to the strategy with the best average outcome there, with a hysteresis margin before switching. The language model is not essential to the idea; a nearest-neighbour average does the same job transparently.

## Relevance to SOL perpetuals at minutes to hours
The useful part is the framing: regime-conditioned strategy selection as retrieval of similar past states, with switching hysteresis, instead of naming regimes. The evidence is daily with a five-day hold, so it says nothing about intraday behaviour. The crypto numbers show how small the gain from switching can be when the candidate strategies are similar, and that naive recent-performance gating can be worse than not switching (currencies).

## Caveats
Single run per market; reinforcement-learning results are known to vary across seeds. The "best fixed" baseline in the comparison table (68%) is lower than two standalone experts in the paper's own earlier table (76.16%, 71.26%); the paper does not explain the difference in the sections I read, so the claimed improvement over fixed experts in crypto should be treated as unproven. Costs not confirmed. A language model in the decision loop adds latency and run-to-run variation, a poor fit for an intraday bot (my assessment). Unreviewed preprint.
