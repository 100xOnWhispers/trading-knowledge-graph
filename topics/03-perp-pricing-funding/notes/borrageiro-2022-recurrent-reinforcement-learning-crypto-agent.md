---
title: "The Recurrent Reinforcement Learning Crypto Agent"
authors: "Borrageiro, Gabriel; Firoozye, Nick; Barucca, Paolo"
year: 2022
venue: "arXiv working paper 2201.04699 (v4, May 2022; formatted as a journal article, journal not confirmed)"
url: "https://arxiv.org/pdf/2201.04699"
pdf: "sources/03-perp-pricing-funding/borrageiro-2022-recurrent-reinforcement-learning-crypto-agent.pdf"
access: "full-text"
source_type: "working-paper"
evidence_grade: "B"
topic: "03-perp-pricing-funding"
asset_class: "crypto"
horizon: "minutes"
tags: "reinforcement-learning, echo-state-network, funding-in-reward, online-learning, bitmex, carry"
---

## Key insight
A direct reinforcement-learning agent whose reward includes execution cost and the funding payment learns, online and without a separate funding model, to hold the side of the BitMEX XBTUSD perp that collects funding when its price forecast is weak. Funding is a material share of what the agent earns, and including it in the reward stops over-trading.

## Method
Order-book and trade features feed an echo state network (100 hidden units, 10 feedback units, 75% sparsity). Its state `z` feeds a direct recurrent reinforcement learner with position `f(t) = tanh(w' z(t))` in [-1, 1]. The per-step reward is position times mid-price change, minus half-spread execution cost and a 5 bp exchange fee on position changes, plus or minus funding, which the paper defines as the basis premium `b` plus the interest differential minus the premium, clamped at a cap of 5 bp, i.e. `k = b + clamp(e - b, -5bp, 5bp)` (the equation is partly garbled in the text extraction; this is the standard BitMEX form it describes). Utility is quadratic (mean minus risk aversion times variance, `lambda = 0.00001`). Weights are updated at every step by an extended Kalman filter with exponential forgetting (`tau = 0.999`). The agent is flattened when its expected net reward turns negative.

## Data and sample
BitMEX XBTUSD inverse perpetual, 5-minute samples, about five years (525,600 observations stated; 1,684 daily P&L rows). The whole history is processed sequentially as a test set, so every decision uses only past data.

## Reported results
- Total return just under 350% net of costs; annualised information ratio 1.46.
- Average position 0.41 (long bias in a rising market).
- Funding ("carry") contributes a cumulative 71 percentage points (Table 1 sum 0.713). The abstract words this as "71% of which is down to funding profit", which does not match the table; the table reading is used here.
- Execution cost and fees total -54 percentage points.
- A Monte Carlo over random reservoir initialisations shows "reasonable variability" of returns and information ratio.

## Signal construction
Not a single indicator. It is a recipe for putting funding into the learning objective: reward at step `t` equals `position(t-1) * dPrice(t) - cost * |dPosition(t)| - position(t-1) * funding(t)` when a funding timestamp falls in the step, with funding and basis also available as input features. Any learner (policy gradient, Q-learning, evolutionary search over rule parameters) can use the same reward.

## Relevance to SOL perpetuals at minutes to hours
The horizon (5-minute bars, taker execution) matches the target bot. The lesson that transfers is structural: optimise net of funding and costs and let the learner discover carry-aware positioning. What does not transfer is the level of funding income: BitMEX in 2016 to 2021 had persistently positive funding, while a low-leverage venue such as Kalshi may pay far less. The split between funding and directional P&L should be re-estimated on SOL.

## Caveats
One instrument, one backtest path, long-biased in a bull market, so the 350% is hard to separate from beta. No comparison against a buy-and-hold-plus-funding benchmark was seen. The reward-versus-abstract inconsistency on the funding share should be kept in mind. Hyperparameters appear fixed in advance but their selection process is not described in the parts read.
