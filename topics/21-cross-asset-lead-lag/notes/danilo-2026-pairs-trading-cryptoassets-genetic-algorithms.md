---
title: "Pair trading strategies in the cryptoassets market: a cointegration framework with optimized thresholds using genetic algorithms"
authors: "Danilo, Lorette; Jamhamed, Fayssal; Martin, Franck"
year: 2026
venue: "Quantitative Finance 26(5), 799-821"
url: "https://econpapers.repec.org/RePEc:taf:quantf:v:26:y:2026:i:5:p:799-821"
pdf: "none"
access: "abstract-only"
source_type: "peer-reviewed"
evidence_grade: "B"
topic: "21-cross-asset-lead-lag"
asset_class: "crypto"
horizon: "n/a"
tags: "pairs-trading, cointegration, genetic-algorithm, evolutionary, threshold-optimization, clustering, out-of-sample"
---

## Key insight
Cointegration-based pairs trading across a broad set of crypto assets is profitable on average, and a genetic algorithm can be used to optimize entry and exit thresholds per pair, but the edge is modest once measured out of sample. The journal version reports an average annual Sharpe ratio of 0.69 per pair out of sample for its best strategy, against 1.53 "over the backtest" in the earlier working paper. The gap between the two versions is itself the most useful number for anyone planning to tune cross-asset rules with evolutionary search.

## Method
From the two abstracts only (journal version on EconPapers; working-paper version, CREM Working Paper 2024-11, on IDEAS): cointegration tests and error-correction models identify tradable pairs; a genetic algorithm and pair clustering are used to build four strategies, some with standard thresholds and some with optimized thresholds. The authors describe the approach as combining econometrics with machine learning. Data frequency, data source, fitness function, the encoding of thresholds, and transaction-cost assumptions are not stated in either abstract.

## Data and sample
A broad set of crypto assets (209 in the working-paper abstract), 1 August 2021 to 31 January 2024; 229 pairs identified as suitable. Frequency and venue not confirmed. Both the working-paper PDF (University of Rennes repository) and a HAL copy were blocked by bot protection in this session, and the journal version is paywalled.

## Reported results
- Journal abstract: profitable cointegrating relationships exist, indicating short-term inefficiencies; the strategy with the best risk-return trade-off, "though still risky", had a median maximum drawdown of 15.29% and an average annual Sharpe ratio of 0.69 per pair in the out-of-sample period.
- Working-paper abstract (2024): for the strategy with the best risk-return balance, median maximum drawdown of 29% and an average annual Sharpe ratio of 1.53 per pair over the backtest.
- No per-strategy comparison of standard versus GA-optimized thresholds is available from the abstracts.

## Signal construction
Generic form: for a cointegrated pair (for example SOL and another large coin, or SOL against a BTC-ETH basket), compute the error-correction residual z(t). Trade when |z| crosses an entry threshold and close at an exit threshold. A genetic algorithm searches over (entry, exit, stop, look-back) to maximize a risk-adjusted fitness on a training window; candidate parameter vectors are selected, recombined and mutated over generations. Any implementation must hold out data the GA never sees and compare against fixed textbook thresholds. The paper's own fitness and operators were not read.

## Relevance to SOL perpetuals at minutes to hours
Pairs relations are the mean-reverting counterpart of lead-lag: instead of predicting SOL from BTC's last move, the bot fades SOL's deviation from a cross-asset equilibrium. This is the only peer-reviewed evolutionary-algorithm source found for cross-asset crypto relations. The out-of-sample Sharpe of 0.69 per pair, with double-digit drawdowns, is a realistic prior for what threshold tuning on a single SOL pair might deliver before Kalshi-specific costs. A single-venue bot can only trade one leg, which converts the strategy into a directional bet conditioned on the spread.

## Caveats
Abstract-only. Frequency unknown; if daily, the relevance to minutes-to-hours trading is limited. The halving of Sharpe between the backtest figure and the out-of-sample figure is consistent with overfitting by the optimizer, though the two versions may also differ in sample or specification (not confirmed). The period 2021-2024 includes the 2022 collapse of several tokens, when cointegration relations broke. Shorting small crypto assets is often infeasible at the assumed cost. General evolutionary-search methods are owned by topic 25.
