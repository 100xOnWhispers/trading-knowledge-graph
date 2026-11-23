---
title: "The Recurrent Reinforcement Learning Crypto Agent"
authors: "Borrageiro, Gabriel; Firoozye, Nick; Barucca, Paolo"
year: 2022
venue: "arXiv:2201.04699v4"
url: "https://arxiv.org/pdf/2201.04699"
pdf: "sources/24-reinforcement-learning/borrageiro-2022-recurrent-rl-crypto-agent-perpetual.pdf"
access: "full-text"
source_type: "working-paper"
evidence_grade: "B"
topic: "24-reinforcement-learning"
asset_class: "crypto"
horizon: "minutes"
tags: "perpetual-swap, funding, recurrent-rl, direct-reinforcement, echo-state-network, online-learning, bitmex, quadratic-utility, 5-minute"
---

## Key insight
This is the closest published match to the project's problem: a direct-reinforcement agent that trades a Bitcoin perpetual swap on five-minute data as a price taker, with spread, exchange fees and funding all inside the reward. It learns online over the whole history with no separate training set, and reports a positive net result with an information ratio of 1.46. The decomposition matters as much as the total: gross directional profit was large, execution cost consumed 54 percentage points, and funding contributed 71 percentage points of a 350% total return.

## Method
Features built from BitMEX order book and trade data feed an echo state network (random recurrent reservoir, 100 hidden units, 10 feedback units of past positions, 75% sparsity) whose weights are not trained. The reservoir state `z_t` feeds a single trained layer giving the position `f_t = tanh(w' z_t)` in [-1, 1].

Net return per step: `r_t = dp_t * f_{t-1} - delta_t * |df_t| - kappa_t * f_t`, where `dp_t` is the mid-price change, `delta_t = 0.5 * (ask_t - bid_t)` is the half-spread paid by a price taker (plus 5 bp exchange fee), and `kappa_t` is the funding rate (paid every 8 hours).

Objective: quadratic utility `mu_t - (lambda/2) * sigma_t^2` on exponentially weighted estimates of the mean and variance of `r_t`, with `lambda = 0.00001`. Weights are updated online at every step by an extended-Kalman-filter-style recursive update with decay 0.999 and ridge penalty 1. A gate closes the position whenever the running expected net reward `mu_t` is negative. The authors argue value-function methods mis-assign reward to the flat state after price jumps.

## Data and sample
BitMEX XBTUSD perpetual swap, five-minute samples, 525,600 observations ("365 x 5 x 1440/5"), reported as 1,684 daily P&L observations, a little under five years. Exact start and end dates were not found in the passages read. The entire history is the test set, learned sequentially.

## Reported results
- Total return just under 350% net of costs; annualized information ratio 1.46.
- Daily P&L table sums: execution -0.542, carry (funding) +0.713, total 3.498. The abstract's "71% of which is down to funding profit" corresponds to this 0.713, that is 71 percentage points, about a fifth of the total.
- Average position 0.41 (long bias); the 25th, 50th and 75th percentiles of position are 0, 0 and 0.99, so the agent is flat much of the time.
- Robustness to the random reservoir: 250 Monte Carlo initializations give information ratios from 0.219 to 1.763 (mean 1.16, standard deviation 0.30) and total returns from 65.4% to 502.1%.

## Signal construction
A working template for a perp agent:
- Position `f_t = tanh(w' z_t)` with previous positions among the inputs.
- Reward per step exactly as above, with observed half-spread, venue fee and scheduled funding.
- Online update of `w` each bar toward higher `mu - (lambda/2) sigma^2`.
- Trading gate: flat whenever the exponentially weighted net reward is below zero.

## Relevance to SOL perpetuals at minutes to hours
Same instrument type, same funding interval (8 hours), same bar size. The reward decomposition is the right accounting for Kalshi: with low leverage and probably wider spreads, the `delta_t * |df_t|` term will be larger than on BitMEX and the policy should trade less. The long bias and funding capture reflect Bitcoin's drift and funding regime in that sample and should not be assumed for SOL. The gate on realized net reward is a cheap safeguard worth adopting. Paying exactly the half-spread assumes the touch has enough size, which needs checking on Kalshi.

## Caveats
One instrument, one path. Hyperparameters (`lambda`, decay, reservoir size) are fixed for the run, but how they were chosen is not stated, so the "entire history is test" claim does not rule out selection on this data. Performance across reservoir seeds spans a factor of eight in information ratio. No comparison with buy and hold, a funding-carry rule or a momentum baseline, although the agent averaged 0.41 long in a rising market. No latency or depth model.
