---
title: "The Red Queen's Trap: Limits of Deep Evolution in High-Frequency Trading"
authors: "Chen, Yijia"
year: 2025
venue: "arXiv preprint 2512.15732v1"
url: "https://arxiv.org/pdf/2512.15732"
pdf: "sources/25-evolutionary-algorithms/chen-2025-red-queen-deep-evolution-crypto-hft.pdf"
access: "full-text"
source_type: "practitioner"
evidence_grade: "D"
topic: "25-evolutionary-algorithms"
asset_class: "crypto"
horizon: "minutes"
tags: "post-mortem, evolutionary-population, binance-perpetuals, fees, mode-collapse, survivor-bias, directional-accuracy"
---

## Key insight
A failure report from an independent researcher. A population of 500 evolving agents, steered by LSTM and Transformer price models, showed validation returns above 300% a year and then lost more than 70% of capital in a live simulation on Binance perpetuals. The arithmetic behind the failure is the valuable part: a directional accuracy of about 51% on minute candles cannot pay an 8 basis point round-trip taker fee, and evolutionary selection on short noisy windows rewards luck and then converges the whole population onto one bet.

## Method
Perception: a 2-layer LSTM and a Transformer encoder read 60 bars of z-scored prices, log returns and ATR and output the probability that the next price is higher, trained with binary cross-entropy. Action: each agent carries a genome of three parameters (leverage, take-profit, stop-loss) and trades on the shared model signal. Selection: an agent's remaining lifespan falls by one unit per time step and is extended by 30 seconds for each profitable trade; agents that run out are culled and profitable ones reproduce. A rule kept at least 5% of the population in contrarian phenotypes, and bankrupt agents were recapitalized to hold the population at 500.

## Data and sample
Binance USDT-margined perpetual futures, 1-minute and 15-minute candles, top 20 coins by liquidity. Taker fee 0.04% per side and slippage averaging 0.02%. The live simulation ran for one 4.5-hour window.

## Reported results
- Validation APY above 300%; live capital decay above 70% (abstract).
- Directional accuracy of the deep models about 51.2%. With transaction cost near 0.1% and a 1% profit target the author computes a break-even win rate of about 55%.
- The models "successfully predicted micro-movements of 0.05%" against a round-trip fee of 0.08%.
- About 60% of agents never traded before their lifespan expired.
- Agents initialized as different archetypes ended holding nearly identical long positions in correlated high-beta altcoins; simultaneous stop-outs produced a liquidation cascade.
- The system ledger showed a deficit of $338,427 at four hours because bankrupt agents were refilled.

## Signal construction
Not a signal. It supplies two checks to run before any search: (1) break-even accuracy given fees, W_BE = (1 + C) / (1 + R), with C the cost as a fraction of risk per trade and R the reward-to-risk ratio; (2) the expected move per signal against the round-trip cost. If the forecast magnitude is below the fee, no optimizer can help.

## Relevance to SOL perpetuals at minutes to hours
Same instrument class and bar size as the target. The lessons are specific. Train on a cost-aware objective (net PnL or thresholded moves), not on direction. Do not use a fitness that rewards trade count or fast feedback, because it selects for churn. Check whether "diverse" candidates hold the same position at the same time before treating them as an ensemble. With OHLCV inputs only, the author found no exploitable edge at taker fees.

## Caveats
Six pages, one 4.5-hour session, no statistical tests, no code or data, and the validation protocol behind the 300% figure is not described. The break-even formula is presented loosely. The conclusion that minute-bar OHLCV has no edge generalizes from a single badly designed system. Use it as a checklist of failure modes, not as evidence about market efficiency.
