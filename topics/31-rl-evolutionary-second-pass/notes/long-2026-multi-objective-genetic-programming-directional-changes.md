---
title: "Multi-objective genetic programming-based algorithmic trading, using directional changes and a modified Sharpe ratio score for identifying optimal trading strategies"
authors: "Long, Xinpeng; Kampouridis, Michael; Papastylianou, Tasos"
year: 2026
venue: "Artificial Intelligence Review 59:39"
url: "https://repository.essex.ac.uk/41752/1/s10462-025-11390-9.pdf"
pdf: "sources/31-rl-evolutionary-second-pass/long-2026-multi-objective-genetic-programming-directional-changes.pdf"
access: "full-text"
source_type: "peer-reviewed"
evidence_grade: "A"
topic: "31-rl-evolutionary-second-pass"
asset_class: "equities"
horizon: "daily"
tags: "genetic-programming, nsga-ii, multi-objective, directional-changes, head-to-head, single-objective, trial-count"
---

## Key insight
Evolving trading rules with three separate objectives (total return, expected return per trade, risk) under NSGA-II, then picking one rule from the Pareto front with a weighted score, gave better held-out results than evolving directly on that same weighted score. The comparison is unusually well powered for this literature: 110 price series, 50 independent runs each, a fixed test segment and a transaction cost. It fills the gap left in topic 25, where the multi-objective route had no rigorous trading evidence, although the evidence is daily and long-only.

## Method
- Rules are trees (maximum depth 6) built from technical indicators in ordinary time and from "directional change" indicators. A directional change event is confirmed when price reverses by a threshold `theta` from its last extreme; the move beyond the confirmation point is the overshoot.
- Trading rule: buy when the tree says so; sell after `n` days or when price has risen `r` percent, whichever comes first. No short selling. 0.025% cost on each buy and sell.
- Search: population 500, 50 generations, tournament size 2, crossover probability 0.95. NSGA-II ranks by non-dominated front and crowding distance with (mu + lambda) survival.
- Selection from the front: a "modified Sharpe ratio" with weights `(a, b, c)` on return, expected return per trade and risk; seven weight settings are studied.
- Comparators: a single-objective GP whose fitness is that same modified Sharpe ratio; MACD, on-balance-volume and momentum rules tuned on the same data; a Transformer forecaster; buy-and-hold.
- Protocol: 60% train, 20% validation, 20% test. `n`, `r` and `theta` tuned per series on validation from a 60-point grid with 5 repetitions (33,000 tuning runs per algorithm and scenario), then 50 final runs per series and scenario.

## Data and sample
Daily closing prices, 25 November 2010 to 24 November 2020, for 100 stocks (10 from each of 10 international markets) and the 10 market indices; about 2,500 observations per series. The test segment is the final 20%.

## Reported results
- Test-set total return, multi-objective GP selected for return: mean 61.33%, median 41.68%, minimum -44.63%. Buy-and-hold: mean 41.11%, median 11.44%, maximum 1753.05%, minimum -89.62%.
- Friedman test with Hommel correction: average rank 1.97 for that variant against 4.40 for buy-and-hold (adjusted p = 2.88E-20).
- Against the single-objective GP, the multi-objective version had higher mean and median return in most weight settings; Kolmogorov-Smirnov tests were significant "in several cases". On pure single-objective scenarios the single-objective GP competed well.
- The Transformer ranked last on return; all three technical rules were significantly worse than the GP variants.

## Signal construction
Not a signal. Method for strategy search: keep return, per-trade edge and risk as separate objectives during evolution; choose from the final front with a pre-declared weighted score. Directional-change indicators (time since last event, overshoot length at threshold `theta`) are an event-time feature family that can be computed on any price stream.

## Relevance to SOL perpetuals at minutes to hours
Directional changes are scale-free and suit a 24-hour market, so the feature construction transfers to intraday SOL. The performance evidence does not: daily stocks, long-only with a profit-target exit, in a decade when a time-limited long rule had a tailwind. An intraday test needs realistic costs (0.025% is below a crypto taker fee plus spread), shorts and funding.

## Caveats
`theta`, `n` and `r` were tuned separately per series, so each series contributes its own search on top of the evolutionary one. The buy-and-hold comparison is by median and rank; buy-and-hold has the higher maximum. Stocks were "arbitrarily selected" and all have a full ten-year history, so survivorship bias is possible (the selection date was not found in the parts read). No turnover or capacity analysis was seen.
