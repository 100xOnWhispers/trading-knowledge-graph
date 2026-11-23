---
title: "How to Evaluate Trading Strategies: Single Agent Market Replay or Multiple Agent Interactive Simulation?"
authors: "Balch, Tucker Hybinette; Mahfouz, Mahmoud; Lockhart, Joshua; Hybinette, Maria; Byrd, David"
year: 2019
venue: "arXiv:1906.12010"
url: "https://arxiv.org/abs/1906.12010"
pdf: "sources/31-rl-evolutionary-second-pass/balch-2019-market-replay-versus-interactive-simulation.pdf"
access: "full-text"
source_type: "working-paper"
evidence_grade: "C"
topic: "31-rl-evolutionary-second-pass"
asset_class: "equities"
horizon: "seconds"
tags: "simulator, market-replay, agent-based, market-impact, backtesting, abides"
---

## Key insight
The two ways of testing a strategy fail in opposite directions. Market replay uses real order flow, but that flow never reacts to the strategy, so a large order's price effect fades back to the historical path. An interactive agent-based simulation lets other participants react, so the effect can persist, but nobody knows whether the artificial participants are realistic. The paper shows both inside one simulator and declines to say which is better.

## Method
- Framework: the ABIDES discrete-event simulator (named in the paper only by reference), with an exchange agent using price-time priority.
- Replay experiment: a "market replay agent" re-submits historical orders. An experimental "impact agent" places one market order sized as a multiple of the best quote size (50%, 200%, 300%, 1000%). Each placement is a separate simulation: 100 buys and 100 sells at 5-second spacing between 09:45:00 and 09:53:15 for the 200% case, and 40 simulations per size for the size sweep. Mid-prices are sampled every millisecond and normalized by the replay-only path.
- Interactive experiment: 100 zero-intelligence background agents that hold a noisy Bayesian belief about a mean-reverting fundamental value and arrive by a Poisson process. Each trial is run twice with the same global random seed, once with the impact order and once without, so the difference in mid-price is the order's effect. 100 experimental-control pairs. The impact agent takes all liquidity within 1% of the inside quote (greed 1.0), with a sweep over the greed parameter.

## Data and sample
Replay uses one historical intraday order book file for one US equity session (instrument and date not confirmed in the parts read). The interactive runs are synthetic, 1,000 time units each with one unit treated as 100 milliseconds.

## Reported results
- Replay: an immediate spike in mid-price at the order, followed by decay toward the price observed without the agent; for sells the price returns to baseline and stays, for buys it trends toward baseline. Larger orders give larger spikes.
- Interactive: the mean price "does not return to the baseline" and stabilizes at a new level, which the authors say matches impact models with a permanent component.
- The authors' conclusion: "It is not clear at this stage that one approach is certainly better than the other".

## Signal construction
Not a signal. It defines a check for the bot's backtester: at what order size, relative to touch depth, does a replay result stop being believable because the missing reaction of other traders would have changed subsequent prices?

## Relevance to SOL perpetuals at minutes to hours
On Binance or Bybit SOL perps the bot's size is negligible and replay is a fair counterfactual. On Kalshi the book is thin, market makers will reprice after a fill, and replay will understate cost for anything beyond the top level. The practical response is to cap order size in backtests at a fraction of displayed depth and add a persistent impact term for anything larger, then verify against live fills.

## Caveats
Illustrative experiments with no calibration of the background agents to real data, results shown as figures without tabulated numbers, and a discrete-time zero-intelligence population that the authors themselves plan to replace. A strategy can also "learn to exploit specific price histories" in replay, a point the paper raises but does not test.
