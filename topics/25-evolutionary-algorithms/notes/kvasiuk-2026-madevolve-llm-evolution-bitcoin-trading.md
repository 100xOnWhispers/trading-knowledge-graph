---
title: "MadEvolve: Evolutionary Optimization of Trading Systems with Large Language Models"
authors: "Kvasiuk, Yurii; Li, Tianyi; Colegrove, Owen; Munchmeyer, Moritz"
year: 2026
venue: "arXiv preprint 2605.23007v1"
url: "https://arxiv.org/pdf/2605.23007"
pdf: "sources/25-evolutionary-algorithms/kvasiuk-2026-madevolve-llm-evolution-bitcoin-trading.pdf"
access: "full-text"
source_type: "working-paper"
evidence_grade: "C"
topic: "25-evolutionary-algorithms"
asset_class: "crypto"
horizon: "minutes"
tags: "llm-evolution, map-elites, island-model, bitcoin, minute-bars, execution-optimization, backtest-realism, p-hacking"
---

## Key insight
The closest published match to this repository's use case: LLM-driven evolutionary search over the code of a minute-bar Bitcoin trading system. The authors separate two kinds of target. Evolving execution and position-sizing logic gave gains that held on a later year of data; evolving the return forecaster gave smaller gains with visible overfitting. All of it rests on a simulator the authors themselves call "far from being realistic".

## Method
MadEvolve keeps a population of programs in a MAP-Elites grid plus five islands with ring migration (every five generations, 10% of elites) and a global elite archive. An ensemble of LLMs proposes code edits to a parent given "inspiration" programs; each candidate is scored by a backtest. Fitness is impact-adjusted PnL on the validation year, chosen over Sharpe because Sharpe can be inflated by trading only the highest-confidence signals; a super-linear impact term stops the search from winning by scaling size. Each candidate may declare at most about 15 to 20 named tunable constants, and candidates over the cap are penalized. The cap was adopted after pilot runs without it "fit the validation period strongly but failed to generalize". There is no inner parameter-fitting loop, which keeps the trial count per candidate small.

Base system: a ridge regression on three exponential moving averages of one-minute returns (half-lives 1, 5, 10 minutes) forecasts returns; each minute the strategy posts one passive limit order with a signed size and price; the simulator fills it if the bar's range reaches the price. Five runs evolve, in turn: the position target; the order placement; both; the feature set only; features and strategy together.

## Data and sample
BTCUSD one-minute OHLCV bars from Polygon, aggregated across exchanges. Train 2022 to 2023 (forecaster fitting), validation 2024 (the evolution target), test 1 January to 10 October 2025. Runs evaluated roughly 740 to 1,000 candidate programs each over 125 to 334 generations.

## Reported results
Validation Sharpe / test Sharpe / test impact-adjusted PnL:
- Baseline: 4.81 / 3.82 / $47K.
- Target only: 4.83 / 4.45 / $271K. Order placement only: 6.49 / 5.12 / $1,205K. Joint strategy: 6.51 / 5.11 / $473K. Features plus strategy: 8.85 / 5.65 / $724K.
- The joint features-plus-strategy run kept about 39% of its validation PnL on test, against 49% to 54% for the strategy-only runs, and its win rate fell from 68.6% to 49.8%.
- Feature-only evolution roughly doubled the 10-minute forecast R-squared, from 0.0017 to 0.0034 on test.
- Gains came with 6x to 20x more traded volume; the authors decompose how much is plain up-sizing.
- A plain iterative agent loop (Claude Code with Sonnet 4.6) was run on the same tasks. Results were sensitive to the prompt, and the authors "cannot unambiguously conclude which particular framework performs better". For the forecaster, the plain loop's features did better on test ($235K, Sharpe 5.27, against $160K and 4.15), which the authors partly attribute to limits they placed on feature count and pairwise correlation.

## Signal construction
Not a signal. The base forecaster is reproducible: ridge regression of forward returns at horizons of 1, 10, 100 and 1,000 minutes on EMAs of one-minute returns with half-lives 1, 5 and 10 minutes. The search target is the code that turns a forecast into orders.

## Relevance to SOL perpetuals at minutes to hours
Directly relevant in instrument type and bar size. Three points carry over. Execution and sizing logic has a near-deterministic fitness signal and is a safer thing to evolve than a forecaster. Capping the number of tunable constants was needed to make results hold out of sample. The evolutionary scaffold was not clearly better than a simpler agent loop, so the constraints matter more than the search algorithm. The absolute numbers do not carry over to a thin venue like Kalshi, where passive fills cannot be assumed.

## Caveats
A baseline Sharpe near 4 from three moving averages signals that the fill model is generous: every limit order touched by the bar range is filled in full, with no queue position or adverse selection, on prices no single exchange quoted. The authors list these assumptions and say results "do not directly transfer to live trading". Their argument against p-hacking uses a Gaussian best-of-K null centered on the baseline; it does not address a shared simulator bias that inflates validation and test alike. One asset, one test period of nine months.
