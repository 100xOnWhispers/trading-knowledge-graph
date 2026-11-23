---
title: "Freqtrade documentation: Hyperopt"
authors: "Freqtrade project contributors"
year: 2026
venue: "Freqtrade stable documentation (open-source crypto trading bot), page read November 2026"
url: "https://www.freqtrade.io/en/stable/hyperopt/"
pdf: "none"
access: "full-text"
source_type: "documentation"
evidence_grade: "D"
topic: "25-evolutionary-algorithms"
asset_class: "crypto"
horizon: "minutes"
tags: "parameter-optimization, nsga-iii, optuna, loss-functions, crypto-bot, overfitting-guards, practitioner-tooling"
---

## Key insight
Freqtrade, a widely used open-source crypto trading bot, tunes strategy parameters with an evolutionary multi-objective sampler by default: its hyperopt "uses one of optuna's sampler algorithms (currently NSGAIIISampler)". The page shows what practitioner tooling for evolutionary parameter search looks like in crypto, and how little of it addresses overfitting. It contains no performance evidence.

## Method
The user marks strategy parameters as optimizable and chooses which spaces to search: entry and exit signal parameters, the minimal-ROI table, stoploss, trailing-stop settings, maximum open trades, and protections. Each trial ("epoch") is a full backtest scored by a loss function. Built-in losses:
- `ShortTradeDurHyperOptLoss`: legacy default, favors short trades and few losses.
- `OnlyProfitHyperOptLoss`: total profit only.
- `SharpeHyperOptLoss` and `SharpeHyperOptLossDaily`: Sharpe on per-trade or daily returns.
- `SortinoHyperOptLoss` and `SortinoHyperOptLossDaily`: Sortino equivalents.
- `MaxDrawDownHyperOptLoss`, `MaxDrawDownRelativeHyperOptLoss`, `MaxDrawDownPerPairHyperOptLoss`: drawdown-based; the per-pair version scores the worst pair so every pair must perform.
- `CalmarHyperOptLoss`: return over maximum drawdown.
- `ProfitDrawDownHyperOptLoss`: profit against drawdown with an adjustable multiplier.
- `MultiMetricHyperOptLoss`: blends profit, drawdown, profit factor, expectancy and win rate and penalizes runs with too few trades.

The first 30 epochs are random. A `--random-state` option makes runs repeatable, and `--min-trades` (default 1) sets the fewest trades a trial needs to count.

## Data and sample
None. Software documentation.

## Reported results
No empirical results. Guidance stated on the page:
- Results usually stop improving much after 500 to 1,000 epochs, and "running too many epochs at once may not produce greater results".
- Parameter decimals are limited to three places because finer values "will usually result in overfitted results".
- An early-stopping setting of 20% to 30% of total epochs is suggested.
- The default is 100 epochs.
- Hyperopt results should be re-run in the backtester using "the same configuration and parameters (timerange, timeframe, ...) used for hyperopt"; the page lists reasons the two can disagree. This is a consistency check on the same data, not an out-of-sample test.
- The page does not mention walk-forward analysis, a held-out period, or any adjustment for the number of epochs tried.

## Signal construction
Not a signal. It is a template for the parameter-tuning layer of a bot: declare parameter ranges, choose a loss, run an evolutionary sampler for a bounded number of trials, then confirm in an independent backtest.

## Relevance to SOL perpetuals at minutes to hours
Useful as a design reference and as a list of gaps. The loss menu covers the objectives a SOL bot would want (Sharpe, Sortino, Calmar, drawdown, a trade-count penalty). What the page does not provide is the part that matters: no walk-forward or held-out split is described, no trial-count deflation is applied, and the default minimum of one trade lets a single lucky trade win. A bot built for Kalshi should add all three. The worst-pair loss suggests a robust variant for one instrument: score the worst of several time blocks instead of the average.

## Caveats
Documentation of a tool, not research; graded D because it makes no tested claim. I read the page through a fetch tool that returns extracted answers, so wording outside the quoted phrases is paraphrase. The page describes the search as "Bayesian" in one place and names an evolutionary sampler in another, so the exact algorithm should be confirmed in the source code for the version used. Defaults change between releases. Shared defaults also mean many retail bots are tuned the same way on the same exchange data.
