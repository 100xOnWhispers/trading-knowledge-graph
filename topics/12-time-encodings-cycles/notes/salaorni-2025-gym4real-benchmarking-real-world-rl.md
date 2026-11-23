---
title: "Gym4ReaL: A Suite for Benchmarking Real-World Reinforcement Learning"
authors: "Salaorni, Davide; De Paola, Vincenzo; Delpero, Samuele; Dispoto, Giovanni; Bonetti, Paolo; Russo, Alessio; Calcagno, Giuseppe; Trovo, Francesco; Papini, Matteo; Metelli, Alberto Maria; Mussi, Marco; Restelli, Marcello"
year: 2025
venue: "arXiv preprint arXiv:2507.00257"
url: "https://arxiv.org/pdf/2507.00257"
pdf: "sources/12-time-encodings-cycles/salaorni-2025-gym4real-benchmarking-real-world-rl.pdf"
access: "full-text"
source_type: "working-paper"
evidence_grade: "C"
topic: "12-time-encodings-cycles"
asset_class: "fx"
horizon: "minutes"
tags: "reinforcement-learning, state-representation, cyclical-encoding, intraday-trading, ppo-dqn"
---

## Key insight
In this benchmark's intraday trading environment, the state given to a reinforcement-learning agent is a vector of recent returns plus the cosine and sine of the time of day plus the current position. With that state, off-the-shelf PPO and DQN did not consistently beat buy-and-hold or sell-and-hold on a held-out year. It is a concrete, documented example of how clock time enters an RL trading state, and a sober data point on what it buys.

## Method
One of six environments in the suite, TradingEnv, is an episodic intraday task. Each episode is a trading day from 8:00 to 18:00 EST; the position must be flat at the end. The state is

`s_t = ( d_t, cos(phi_t), sin(phi_t), z_t )`

where `d_t` holds the last 60 one-minute relative mid-price changes `d[k,t] = (p[t-k] - p[t-k-1]) / p[t-k-1]`, `phi_t` in `[0, 2*pi]` is the angular position of the current time within the trading period, and `z_t` is the previous action. Actions are short, flat or long on a fixed notional. Reward is `r_t = a[t-1]*(p_t - p[t-1]) - lambda*|a_t - z_t|`, with `lambda` a fixed fee per position change. The agent acts every 5 minutes.

Optional temporal inputs are month, day and day of week. The appendix states that cyclic sine and cosine encoding is preferred with neural function approximators and "not recommended" with tree-based models, where it can obscure the natural ordering of the feature.

## Data and sample
EUR/USD tick data from histdata.com resampled to one minute; Monday to Friday, 8:00 to 18:00 EST. Gaps up to 5 minutes forward-filled, days with wider gaps removed. Capital 100k per trade, fee 1 per position change. Training and test years: not confirmed from the pages read. Six random seeds.

## Reported results
"As expected, neither PPO nor DQN is able to consistently outperform the baselines." The authors add that RL reduces the day-to-day variability of profit and loss relative to the passive strategies. No ablation with and without the time features is reported, and no numeric performance table for this environment was found in the text read.

## Signal construction
Not a signal. It gives the state layout for an RL agent:
1. `phi_day = 2*pi * (seconds since 00:00 UTC) / 86400`; include `cos(phi_day)`, `sin(phi_day)`.
2. For a 24/7 market add `phi_week = 2*pi * (seconds since Monday 00:00 UTC) / 604800` and a funding-cycle angle with period 28,800 seconds.
3. Concatenate with the return window, the current position and time since last trade.
4. Include the fee term in the reward so the agent learns not to churn.
If the policy is tree-based (for example fitted Q-iteration with gradient-boosted trees), pass integer minute-of-day and day-of-week instead.

## Relevance to SOL perpetuals at minutes to hours
The state design and the 5-minute decision cadence match the target horizon. The environment forces a daily flat, which a perpetual does not need; funding payments and liquidation risk are absent and would have to be added to the reward. The negative result is on EUR/USD with only price history and clock time as inputs, which is the least favourable feature set; it says that clock features plus lagged returns are not enough, not that RL cannot work with richer inputs.

## Caveats
A benchmark paper whose purpose is to provide environments, not to study trading. One currency pair, fixed fee, no market impact, no spread model beyond mid-prices. No time-feature ablation, so the contribution of the sine and cosine inputs is unmeasured. Preprint.
