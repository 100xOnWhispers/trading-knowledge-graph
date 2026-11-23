---
title: "What survives honest evaluation? Leakage-safe, search-aware assessment of LLM-driven trading strategy discovery"
authors: "Gencay, Eray"
year: 2026
venue: "arXiv preprint 2608.27734v1 (independent researcher; marked as submitted to Elsevier)"
url: "https://arxiv.org/pdf/2608.27734"
pdf: "sources/25-evolutionary-algorithms/gencay-2026-honest-evaluation-llm-strategy-discovery.pdf"
access: "full-text"
source_type: "working-paper"
evidence_grade: "B"
topic: "25-evolutionary-algorithms"
asset_class: "equities"
horizon: "daily"
tags: "trial-ledger, deflated-sharpe, look-ahead, llm-strategy-search, pbo, negative-result, statistical-power"
---

## Key insight
When an automated search records every backtest it runs and its best result is deflated by that count, none of the strategies discovered by frontier LLM agents in this study can be told apart from luck, including some that were profitable out of sample. Separately, statistical deflation cannot detect look-ahead: a deliberately leaky strategy with a Sharpe ratio of 35 passes every test. The two protections do different jobs and a search system needs both built in.

## Method
A strategy-discovery agent may act only through a registry of validated tools whose features are point-in-time by construction. Every evaluation the search performs is written to a trial ledger. Reported performance is then judged with:
- Deflated Sharpe ratio. The threshold a winner must beat is SR0 = sqrt(V) * [(1 - g) * Phi^-1(1 - 1/N) + g * Phi^-1(1 - 1/(N e))], with N the ledger's trial count, V the variance of the trials' Sharpe ratios and g the Euler-Mascheroni constant.
- Probability of backtest overfitting from combinatorially symmetric cross-validation.
- A stationary-bootstrap confidence interval on the held-out Sharpe ratio, and a paired test against buy-and-hold.
- An "evaporation curve": best in-sample Sharpe so far plotted against the rising threshold as trials accumulate.

Experiments include a planted look-ahead oracle, autonomous searches of up to about 100 candidates with two models (gpt-4.1 and claude-sonnet-5), five repeated runs, a pre-registered human hypothesis and a ported human production system.

## Data and sample
A 453-stock point-in-time US equity universe (design 2017 to 2021, evaluation 2022 to 2025) and 39 multi-asset ETFs (design 2007 to 2016, evaluation 2017 to 2025). Costs: 1 bp commission, 2 bp spread, square-root market impact, 50 bp annual borrow.

## Reported results
- Look-ahead oracle: design Sharpe 34.7, evaluation Sharpe 51.5, deflated Sharpe 1.00. It is not caught.
- Main autonomous search, 102 recorded trials: best design Sharpe 1.69; threshold 1.21; deflated Sharpe 0.86, below the 0.95 bar. Held-out Sharpe 0.18 (+4.7% over four years, interval -0.80 to +1.14) while buy-and-hold returned +40.8%.
- Five repeated searches (18 trials each): held-out Sharpe 0.59 to 0.70, deflated Sharpe 0.15 to 0.29; none certified.
- ETF universe: the agent's best find went from +0.37 in design to -0.23 held out; the search's overfitting probability, computed on design data alone, was 0.80.
- A random-weights null earned +23% over nine held-out years.
- Passive benchmarks are certified, so the procedure is not a blanket rejector.
- Power: a true Sharpe of 0.6 needs roughly eleven years of out-of-sample data to reach t of about 2. A search of 10,000 candidates faces a bar about 1.5 times higher than one of 100 at equal dispersion.
- Three of five repeated runs with one model composed nearly identical strategies.

## Signal construction
Not a signal. It specifies evaluation infrastructure for any search, evolutionary or LLM: (1) one entry point for backtests that logs every call, (2) features that cannot see the future by construction, (3) a rising acceptance threshold computed from the log, (4) a held-out window opened once.

## Relevance to SOL perpetuals at minutes to hours
The power arithmetic is more favorable intraday: a strategy trading many times a day accumulates evidence in months, as the paper notes for high-frequency operations. The trial count grows just as fast, though, because an evolutionary run evaluates thousands of candidates. A SOL search should log every fitness evaluation and compute this threshold from the log. Leakage checks matter more with multi-venue inputs, where timestamp misalignment between exchanges is an easy source of look-ahead.

## Caveats
Single independent author, preprint, daily equity and ETF data, searches capped near 100 candidates with a restricted price-feature action space. Nominal trial counts overstate independent trials when candidates are near-duplicates; the author's follow-up (arXiv 2611.14539, which I opened but did not note) reports 100 nominal trials collapsing to 6 to 8 effectively independent return streams and shows that a threshold computed inside the loop can be gamed by flooding the log with mediocre near-duplicates. General theory of these statistics belongs to topic 26.
