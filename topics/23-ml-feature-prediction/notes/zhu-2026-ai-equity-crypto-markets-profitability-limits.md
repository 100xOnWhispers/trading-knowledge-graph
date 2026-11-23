---
title: "Artificial Intelligence in Equity and Crypto Markets: Progress, Profitability Evidence, and the Limits of Automated Investing"
authors: "Zhu, Linsen; Cai, Mengqing"
year: 2026
venue: "arXiv:2609.04917v1 (literature cutoff 31 August 2026)"
url: "https://arxiv.org/pdf/2609.04917"
pdf: "sources/23-ml-feature-prediction/zhu-2026-ai-equity-crypto-markets-profitability-limits.pdf"
access: "full-text"
source_type: "working-paper"
evidence_grade: "B"
topic: "23-ml-feature-prediction"
asset_class: "multi"
horizon: "n/a"
tags: "survey, alpha-translation, perpetual-futures, funding, leakage, foundation-models, cost-aware-learning, evaluation-protocol"
---

## Key insight
A critical review of public evidence, through August 2026, on whether machine learning, time-series foundation models, language models, reinforcement learning and agents produce net trading profit in equities and crypto. Its conclusion: there is real progress in prediction, but "no general AI architecture is shown to deliver persistent, cross-regime, capacity-aware net alpha", and the crypto-specific record is thinner than the equity record. It gives the most current checklist of what a perpetual-futures machine-learning backtest must model to be believable.

## Method
A narrative review organised around an "alpha-translation chain": point-in-time information must become a stable signal, then feasible positions, then executable orders, then risk-adjusted return after costs. Each method family is assessed on how far along the chain its evidence reaches. Equities and ETFs, centralised crypto spot, perpetual futures and on-chain markets are treated as separate strata with different profit-and-loss definitions.

## Data and sample
Literature review; no new data.

## Reported results
Points relevant to supervised learning on features:
- Gu, Kelly and Xiu style results show that relatively shallow architectures suit low signal-to-noise financial data; they establish historical out-of-sample prediction, not universal alpha.
- Citing Jensen et al. (2026): prediction-oriented models extract signals that look valuable gross "but trade poorly after costs, particularly when opportunities are fleeting and low scale"; training on the cost-aware decision changes the portfolio. The stated design principle is "train for the decision actually made".
- Time-series foundation models: citing Alonso and Franklin (2026), pretrained models took eight of ten task-level wins on five liquid US equities, but gains over a random walk were "small and sparse", significant in only two model-asset comparisons. Citing a benchmark called FinVerse (116,897 financial series, 43 foundation models): strong generic forecasting rank need not translate to useful financial forecasts. Neither supplies a portfolio with costs.
- Citing Tan et al. (2024): removing or replacing the language-model component of LLM-based forecasters can preserve or improve performance.
- A generic pretrained model may have seen the test period; fine-tuning on a pre-cutoff slice "does not remove information already encoded in the base model".
- Crypto spot: wash trading means a model trained on volume or order flow "can learn venue manipulation as if it were investor demand".
- Perpetuals: the review writes holding-period profit as PnL = q(P1 - P0) - q P0 f - C - liquidation loss, with f the funding rate. "A directional agent that ignores funding can be right about spot direction and wrong about contract P&L." Evaluation needs contract-level funding timestamps, mark-price liquidation simulation, margin mode and fee tier.
- Perp-specific leakage: applying today's contract specification (funding interval, limits) to earlier periods; continuous series that cross listing changes; reconstructing the tradable universe from future liquidity.

## Signal construction
Not a signal. It supplies the evaluation protocol: point-in-time features and model checkpoints, decision-aligned objectives, perp profit and loss with funding and liquidation, separate engines for spot and perp, cost and latency stress, and prospective (paper or live) testing before trusting a backtest.

## Relevance to SOL perpetuals at minutes to hours
High as a design reference. The funding term matters less at minutes to hours on a venue with 8-hour funding, but positions held across a funding stamp must be charged, and funding-interval history differs by venue and date. The leakage list applies directly to any SOL model trained on Binance or Bybit history. The warning about foundation-model contamination applies to any pretrained forecaster evaluated on data before its training cutoff.

## Caveats
A single-version preprint by two authors; a qualitative synthesis with no meta-analysis. It relies on several 2026 preprints I did not open (Jensen et al., Alonso and Franklin, FinVerse), so those findings are second-hand here. It does not cover Kalshi or other regulated US perp venues.
