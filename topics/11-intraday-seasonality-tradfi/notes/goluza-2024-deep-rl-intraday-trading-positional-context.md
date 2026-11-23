---
title: "Deep Reinforcement Learning with Positional Context for Intraday Trading"
authors: "Goluza, Sven; Kovacevic, Tomislav; Bauman, Tessa; Kostanjcar, Zvonko"
year: 2024
venue: "arXiv:2406.08013 (q-fin.TR), 12 June 2024"
url: "https://arxiv.org/pdf/2406.08013"
pdf: "sources/11-intraday-seasonality-tradfi/goluza-2024-deep-rl-intraday-trading-positional-context.pdf"
access: "full-text"
source_type: "working-paper"
evidence_grade: "C"
topic: "11-intraday-seasonality-tradfi"
asset_class: "futures"
horizon: "minutes"
tags: "reinforcement-learning, ppo, intraday-trading, time-of-day-feature, futures, transaction-costs, walk-forward"
---

## Key insight
A policy-gradient agent trading one-minute commodity and currency futures performs better when its state includes "positional" context: time left in the session, current position and the open position's running return, in addition to price features. The learned policy shows a time-of-day profile, initiating most trades early in the session and fewer as the close approaches. The reported edge exists only at institutional-level costs.

## Method
Proximal Policy Optimization (actor-critic, model-free) with actions long, flat or short on a single asset and a reward equal to position return net of transaction costs. State: price-based features (returns over 1, 5, 15, 30 and 60 minutes and technical indicators such as RSI, ADX, ultimate oscillator and Williams %R) plus a four-dimensional positional block that includes time left TL = 360 - t (minutes remaining of 360 decision steps per day), position in {-1, 0, 1}, and position return since entry net of costs. Trading is confined to liquid hours 09:30 to 17:00 ET; the agent does not trade in the first hour (first half-hour excluded for volatility, then lookback warm-up) or the final half-hour, and is flat overnight. Walk-forward evaluation uses 27 rolls of one year training (last month for validation) and four months testing. Benchmarks are buy-and-hold, sell-and-hold and a momentum rule. Feature importance is measured by zeroing each feature and recording the drop in Sharpe ratio.

## Data and sample
One-minute OHLCV continuous front-month futures, 2012 to end of 2021 (tests 2013 to 2021; the first year reserved for asset selection): gold, copper, silver, platinum, WTI crude, natural gas, and Australian dollar, British pound, Swiss franc and Mexican peso futures.

## Reported results
- The agent outperforms the benchmarks on every commodity (platinum best) and on two of four currencies; currency Sharpe ratios are lower but positive. Exact per-asset values were not reliably extracted from the table.
- Commission assumed in training and evaluation: 0.08 basis points, with slippage approximated conservatively. The model tends to become unprofitable above about 0.16 bp.
- On average the version with positional features beats the version without them at the higher commission levels; with zero commission the simpler model is better.
- Trades are initiated mostly early in the day, with activity declining toward the close. Holding time lengthens as the day progresses but shortens in the final 15 minutes, which the authors read as the agent learning to exit before the close.
- Every feature contributes except the 30-minute return, which does not improve the model.

## Signal construction
Not a signal; a state-design recipe for a learning agent. Add to the state vector: time to the next session boundary or scheduled event, current position, unrealized return and time in position. For a 24-hour market replace "time left in the day" with cyclic encodings of hour of day and day of week and countdowns to funding timestamps and known events. Train with transaction costs in the reward and evaluate walk-forward.

## Relevance to SOL perpetuals at minutes to hours
Relevant as evidence that time-of-day and position context are worth including in a reinforcement-learning state, which is how a learned policy absorbs intraday seasonality without a hand-coded rule. The cost sensitivity is the main message for Kalshi: an agent whose profit vanishes above 0.16 bp per trade has no edge on a venue where fees and spread are tens of times larger. Any crypto version must be trained with the venue's true costs, which will force far lower turnover.

## Caveats
Preprint as read (a search listing indicates later journal publication in Evolving Systems, not confirmed). No statistical tests against benchmarks, no comparison with a tuned supervised model, a single algorithm and seed sensitivity not reported in the parts read. Costs are unrealistically low for most traders. Excluding the open and close removes the periods where seasonality is strongest. Authors report data-snooping precautions, but asset selection used in-sample liquidity screens.
