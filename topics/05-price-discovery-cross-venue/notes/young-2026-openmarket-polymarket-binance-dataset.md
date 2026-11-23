---
title: "OpenMarket: A Synchronized Polymarket-Binance Dataset for High-Frequency Prediction-Market Research"
authors: "Young, Gregory"
year: 2026
venue: "arXiv preprint 2607.26245"
url: "https://arxiv.org/pdf/2607.26245"
pdf: "sources/05-price-discovery-cross-venue/young-2026-openmarket-polymarket-binance-dataset.pdf"
access: "full-text"
source_type: "working-paper"
evidence_grade: "B"
topic: "05-price-discovery-cross-venue"
asset_class: "crypto"
horizon: "seconds"
tags: "machine-learning, null-result, polymarket, binance, lead-lag, small-venue, walk-forward, clock-synchronization"
---

## Key insight
A small venue that visibly follows Binance is not automatically exploitable. Polymarket's BTC 15-minute binary quotes respond to large Binance moves with a median delay of about 347 ms, yet a walk-forward machine-learning model on 43 Binance and Polymarket microstructure features fails to beat the probability already implied by Polymarket's own mid, and simulated trading loses money after fees and slippage. It is a documented negative result on the "trade the lagging small venue using the leader" idea.

## Method
A Rust pipeline records both venues on one collector clock at millisecond resolution and pairs events. Timing is studied two ways: source-clock lead-lag (with drift bounded and an unresolved constant offset) and a synchronization-free event study that detects Binance moves of at least 5 bps within 1 s and times the first directionally consistent one-tick change in the Polymarket UP-token best bid within 2 s, all on the collector clock. Forecasting: walk-forward logistic regression per market with Platt scaling over 43 features, compared against the naive prior (Polymarket mid) on AUC, Brier score and expected calibration error; a simulator applies 1% fees and 0.5% slippage.

## Data and sample
Polymarket BTC 15-minute binary markets and Binance BTC/USDT, February 12 to May 15, 2026 (54 Polymarket days, 57 Binance days); 727,098,247 deduplicated rows; 2,936,031 lead-lag pairs; 2,251 markets; 559 walk-forward windows.

## Reported results
- Apparent source-clock median lag 16 ms, with drift at most 6 ms and a constant-offset ambiguity of about +/-99 ms.
- Event study: 15,148 large Binance moves, 4,272 matched; median Polymarket quote response 347 ms.
- Out-of-sample: model AUC 0.8377, Brier 0.165, ECE 0.026 versus naive mid prior AUC 0.8405, Brier 0.163, ECE 0.014. The model "slightly underperforms the market prior".
- An apparent full-timeline lift of 0.0014 AUC includes training rows and "does not survive walk-forward evaluation".
- Simulated positive-expected-value trading: -0.116 normalized payoff units per attempted trade.
- Raw order-flow imbalance fails; lag is uncorrelated with move size.

## Signal construction
Use as a test protocol, not a signal. (1) Measure the target venue's response time to leader moves with a single-clock event study: trigger on leader moves above a threshold (for example 5 bps in 1 s) and time the first consistent quote change on the target. (2) Benchmark any cross-venue model against the target venue's own mid as the naive forecast, strictly walk-forward. (3) Include full fees and slippage before believing an edge.

## Relevance to SOL perpetuals at minutes to hours
Kalshi is a prediction-market operator and its new perp is, like Polymarket's crypto markets, a small venue priced off Binance by market makers. The lesson transfers: market makers already embed the leader's information within a few hundred milliseconds, so a latency-ordinary bot should not expect to profit from the raw lag. Any edge must come from information the makers do not already price (slower-moving order-flow, positioning, funding and liquidation features at minute-to-hour horizons). What does not transfer: binary 15-minute payoffs and 1% fee assumptions.

## Caveats
Single author; the instrument is a binary option, not a perp; logistic regression only (no trees or deep models were tried in what I read); one collector vantage point; fee and slippage assumptions are stated rather than measured. A null result on one model class does not prove no edge exists.
