---
title: "The Red Queen's Trap: Limits of Deep Evolution in High-Frequency Trading"
authors: "Chen, Yijia"
year: 2025
venue: "arXiv:2512.15732v1"
url: "https://arxiv.org/abs/2512.15732"
pdf: "sources/22-deep-learning-lob/chen-2025-red-queens-trap-deep-evolution-hft.pdf"
access: "full-text"
source_type: "working-paper"
evidence_grade: "D"
topic: "22-deep-learning-lob"
asset_class: "crypto"
horizon: "minutes"
tags: "negative-result, evolutionary-algorithm, lstm, transformer, binance-perpetuals, ohlcv, transaction-costs, breakeven-win-rate, overfitting, post-mortem"
---

## Key insight
A post-mortem of a system that paired LSTM and Transformer direction models with an evolving population of 500 trading agents on Binance USDT perpetuals. Validation looked excellent (annualised yield above 300%) and the live simulation lost more than 70% of capital. The author's diagnosis: a directional accuracy of about 51% on candle data cannot pay a round-trip cost near 0.1%, and neither deeper models nor evolutionary selection can create information that the inputs do not contain.

## Method
Perception: a two-layer LSTM and a Transformer encoder take a 60-step window of z-scored prices, log returns and ATR from OHLCV candles and output the probability that the next price is higher (binary cross-entropy). Action: each agent has a genome of leverage, take-profit and stop-loss; an agent's lifespan shrinks each step and is extended by 30 seconds per profitable trade ("Time-is-Life"); profitable agents reproduce, bankrupt ones are culled, and at least 5% of the population is kept as contrarian types to preserve diversity. Costs: taker fee 0.04% per side plus slippage averaging 0.02%.

Breakeven arithmetic given in the paper: net PnL = (P_exit - P_entry) x Q - 2 x (P x Q x fee); expected value EV = W x R x Risk - (1 - W) x Risk - C; with C about 0.1% and a 1% profit target the required win rate is about 55%.

## Data and sample
Binance USDT-margined perpetual futures, 1-minute and 15-minute OHLCV candles for the top 20 coins by liquidity. The live simulation ran for one continuous 4.5-hour window in a volatile session. No order book or trade-level data were used.

## Reported results
- Validation yield above 300% annualised against live capital decay above 70% (abstract).
- Directional accuracy of the deep models about 51.2%, below the roughly 55% breakeven.
- The models correctly called moves of about 0.05% while the round-trip fee was 0.08%, so agents showed positive floating profit and negative net profit.
- About 60% of agents never traded before their lifespan expired, because model confidence was too low for their risk settings.
- Surviving agents converged on the same leveraged long positions in correlated high-beta coins, and a reversal triggered simultaneous stop-outs.
- Replacing bankrupt agents to hold the population at 500 kept fee-paying losers alive; the central ledger showed a deficit of 338,427 dollars at four hours.

## Signal construction
Not a signal. It supplies a pre-trade filter that any model should pass: required win rate W_BE = (1 + C_ratio) / (1 + R) as printed in the paper, where R is the reward-to-risk ratio and C_ratio is the round-trip cost relative to the amount risked (the paper does not define it more precisely). Train on a target that includes move size relative to cost, not direction alone.

## Relevance to SOL perpetuals at minutes to hours
The setting is ours (crypto perps, minute bars, taker execution) and the failure modes are the ones to design against: direction-only labels that ignore magnitude, selection among many strategy variants on a short noisy window, hidden concentration in market beta, and leverage shortening time to ruin. Kalshi's low leverage cap limits the last of these but not the first three. The author's closing recommendation is to seek edge in order flow or on-chain data or at longer horizons, which matches the scope of this repository.

## Caveats
One 4.5-hour run by an independent author; no code, no statistical tests, no ablations, and the validation procedure that produced the 300% figure is not described. Several quantities (accuracy, breakeven) are stated without tables. The "live" environment is described as a live simulation, so fills are modelled. The paper shows that this design failed once; it does not show that evolutionary or deep methods cannot work with better inputs. Overlaps with the reinforcement learning and evolutionary topics (24 and 25); filed here as a deep-learning failure case with cost arithmetic.
