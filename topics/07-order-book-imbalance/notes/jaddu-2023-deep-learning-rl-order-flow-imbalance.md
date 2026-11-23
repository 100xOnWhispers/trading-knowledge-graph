---
title: "Combining Deep Learning on Order Books with Reinforcement Learning for Profitable Trading"
authors: "Jaddu, Koti S.; Bilokon, Paul A."
year: 2023
venue: "arXiv:2311.02088v1"
url: "https://arxiv.org/pdf/2311.02088"
pdf: "sources/07-order-book-imbalance/jaddu-2023-deep-learning-rl-order-flow-imbalance.pdf"
access: "full-text"
source_type: "working-paper"
evidence_grade: "C"
topic: "07-order-book-imbalance"
asset_class: "multi"
horizon: "seconds"
tags: "reinforcement-learning, q-learning, dqn, ddqn, order-flow-imbalance, alpha-term-structure, forward-test, latency"
---

## Key insight
A two-stage pipeline (supervised model turns ten-level OFI into return forecasts at six short horizons; a temporal-difference agent turns forecasts into buy or sell decisions) looked profitable in backtests with perfect forecasts, weakened sharply when real forecasts were used, and lost money in live forward testing. The failure was attributed to latency: the agent relied almost entirely on the first forecast horizon, which had expired by the time orders reached the market. It is a useful negative result on OFI plus RL at retail latency.

## Method
Stage one: an MLP regresses mid-price changes over the next six event-time horizons on the ten-level OFI vector (design taken from Kolm, Turiel and Westray). Recurrent and convolutional layers were tried and gave no benefit on this data. Stage two: three agents (tabular Q-learning, DQN, Double DQN) observe the forecast vector and current position and choose to hold or reverse a single always-in-the-market position; reward is PnL net of retail commission and spread. Agents were trained on true future returns ("accurate alphas") and then evaluated with the model forecasts. Selected agents were forward-tested live through a broker platform.

## Data and sample
OFI features recorded from the limit order book of a retail platform (cTrader, FxPro) for GBPUSD, EURUSD, DE40, FTSE100 and XAUUSD: ten weeks between 23 May and 21 August 2023, split 8:1:1 into training, validation and test (five test days). Forward tests ran for one hour per instrument.

## Reported results
- During training with accurate alphas, all agents were very profitable on the two FX pairs; Q-learning earned most, then DDQN, then DQN, roughly in the ratio 15:7:5.
- With model forecasts on the five-day test set, profits turned negative for every agent and instrument except Q-learning on GBPUSD (daily average 2,210 pounds, standard deviation 3,590); Q-learning on EURUSD averaged -120 pounds per day.
- Forward testing lost 2,400 pounds on GBPUSD and 2,640 pounds on EURUSD in one hour each.
- Inspection of learned Q-values showed decisions were driven mainly by the first horizon. The authors report that processing delays caused the bot to skip timesteps, so that horizon had usually elapsed before execution.
- Simple Q-learning outperformed the deep agents throughout.

## Signal construction
Inputs: L2 updates to ten levels. Compute the OFI vector per update; a small regressor outputs expected mid-price change at horizons 1 to 6 (in event time); a tabular or small-network policy maps (forecast vector, current position) to hold or reverse, with the cost of reversing in the reward. The separation is the reusable idea: the forecaster can be retrained and validated independently of the policy.

## Relevance to SOL perpetuals at minutes to hours
The architecture fits the user's interest in RL: keep the order-book model as a forecaster and let a small policy learn when a forecast is worth the cost of trading. The negative result is the more important transfer. A policy trained on perfect foresight learns to act on the shortest horizon, which is the one a non-colocated bot cannot capture. For a minutes-to-hours SOL bot, train the policy on realistic, delayed forecasts, put fees and latency in the environment, and prefer forecast horizons the execution stack can reach. The finding that tabular Q-learning beat deep agents argues for small state spaces.

## Caveats
Ten weeks of data, five test days, one hour of live testing; retail broker book rather than an exchange book; no crypto. Results are in currency units for one-lot trades without risk-adjusted metrics. Not peer reviewed.
