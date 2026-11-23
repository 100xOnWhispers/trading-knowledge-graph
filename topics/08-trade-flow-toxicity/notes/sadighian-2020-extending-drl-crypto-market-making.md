---
title: "Extending Deep Reinforcement Learning Frameworks in Cryptocurrency Market Making"
authors: "Sadighian, Jonathan"
year: 2020
venue: "arXiv 2004.06985v1 (April 2020)"
url: "https://arxiv.org/pdf/2004.06985"
pdf: "sources/08-trade-flow-toxicity/sadighian-2020-extending-drl-crypto-market-making.pdf"
access: "full-text"
source_type: "working-paper"
evidence_grade: "C"
topic: "08-trade-flow-toxicity"
asset_class: "crypto"
horizon: "seconds"
tags: "reinforcement-learning, trade-flow-imbalance, market-making, perpetuals, bitmex, a2c, ppo, reward-design"
---

## Key insight
Policy-gradient agents (A2C and PPO) given order book levels, order-flow and trade-flow-imbalance features can learn a market-making policy on the BitMEX XBTUSD perpetual, and stepping the environment on price-change events instead of clock time makes learning more stable. The evidence is weak: most experiments lost money, no feature set was clearly best, and the best agent barely beat buy-and-hold in a rising month. It is useful mainly as a worked design of an RL state space built from trade flow and as an honest record of how fragile the results are.

## Method
Observation space (window of 100 snapshots): dollar value at the first 20 bid and ask levels; level-wise book imbalance; order flow (dollar value of limit, cancel and market orders per level between snapshots); trade flow imbalance TFI = (UP - DWN) / (UP + DWN), where UP and DWN are buyer-initiated and seller-initiated traded value over windows of 5, 15 and 30 minutes; a custom RSI; plus the agent's inventory and last action. Features are z-scored against the previous three days and clipped at +/-10. Actions place or skew one bid and one ask, or flatten. Seven reward functions are compared. Two environments: time-based (one-second snapshots with action repeats) and price-based (a step whenever price moves by a threshold). Six feature-set combinations are tried. Simulation rules: maker rebate 0.025%, taker fee 0.075%, queue-position modelling for fills, 0.01% slippage on flattening, inventory cap of 10, flat at end of day.

## Data and sample
BitMEX XBTUSD perpetual, limit order book and trades at about one snapshot per second. Training 27 December 2019 to 3 January 2020 (8 days); testing 4 January to 3 February 2020 (30 days).

## Reported results
- Best result: 17.61% over the test period (A2C, trade-completion reward, feature Set 3) against 16.25% for buy-and-hold.
- Time-based environment: 15 of 84 experiments profitable. Price-based environment: 23 of 84 profitable, with more stable behaviour in large price jumps.
- "No clear trends emerged for the best observation space combination, or reward function."
- On 19 January 2020, when Bitcoin fell more than 5% in under 200 seconds, every experiment lost between 5% and 10%.

## Signal construction
The reusable piece is the multi-window trade flow imbalance as an RL or supervised state feature: TFI_w = (taker buy value - taker sell value) / (taker buy value + taker sell value) over w = 5, 15 and 30 minutes, normalised by a trailing z-score. For an RL agent, combine it with book imbalance and inventory, step on price events, and include fees, queue position and slippage in the simulator.

## Relevance to SOL perpetuals at minutes to hours
The TFI windows (5 to 30 minutes) are at the bot's horizon and the instrument is a perpetual. The paper does not show that TFI helped: the indicator group containing TFI was present in every feature set, so its contribution was never isolated. The lessons that transfer are about RL practice on perps: reward shaping dominates outcomes, eight days of training is far too little, a single fast sell-off wiped out every agent, and a maker rebate was described as crucial, which Kalshi may not offer.

## Caveats
One instrument, eight training days, one test month that happened to trend up, and 168 experiments from which the best is quoted, so selection bias is severe. Simulated fills. Single author, unrefereed. Market making, not directional trading.
