---
title: "Trade arrival dynamics and quote imbalance in a limit order book"
authors: "Lipton, Alexander; Pesavento, Umberto; Sotiropoulos, Michael G."
year: 2013
venue: "arXiv:1312.0514v1"
url: "https://arxiv.org/pdf/1312.0514"
pdf: "sources/07-order-book-imbalance/lipton-2013-trade-arrival-quote-imbalance.pdf"
access: "full-text"
source_type: "working-paper"
evidence_grade: "B"
topic: "07-order-book-imbalance"
asset_class: "equities"
horizon: "tick"
tags: "quote-imbalance, top-of-book, diffusion-model, trade-arrival, execution, adverse-selection"
---

## Key insight
Top-of-book quote imbalance predicts the next mid-price move and the waiting time until it, but the expected move is well below the bid-ask spread, so imbalance alone is not a stand-alone arbitrage. Its natural use is deciding whether to post passively or take liquidity. The paper also shows that the expected price move conditional on being filled differs by trade side, which is adverse selection seen through the imbalance lens.

## Method
Imbalance is `I = (q_b - q_a) / (q_b + q_a)` at the best quotes. Empirically, the authors bucket quotes by I and measure the average mid-price move (normalized by the spread) and waiting time to three stopping times: the next mid-price change, the next buy trade, and the next sell trade. They then model the bid queue, the ask queue, and a latent trade-arrival process as three correlated diffusions absorbed at the boundaries of the positive orthant. Event probabilities (up-tick, down-tick, near-side fill) solve a time-independent PDE, handled semi-analytically after a change of variables that removes the correlations. The model is calibrated to the empirical curves.

## Data and sample
Vodafone (VOD.L) on the London market, all trading days in the first quarter of 2012, quote and trade ticks. Authors were at Bank of America Merrill Lynch.

## Reported results
- The average mid-price move to the next tick is approximately linear in imbalance and reaches up to about a third of the spread for a highly imbalanced book.
- Highly imbalanced books are followed by a price move sooner.
- The authors state that imbalance is a good predictor of the next move but "does not by itself offer an opportunity for a straightforward statistical arbitrage".
- The expected price move depends on which trade side defines the stopping time: measured up to the arrival of the next sell trade, the average mid-price move is shifted upwards relative to the move measured up to the next buy trade. The authors read this either as the information advantage of aggressive traders over those posting passively, or mechanically as the impact of the intervening opposite-side trades.
- Queue-depletion processes for bid and ask are typically negatively correlated.

## Signal construction
Inputs: best bid and ask sizes. Compute I per update; estimate from history a lookup of expected mid move (in spread units) and expected waiting time per imbalance bucket. For execution: when I favors your side strongly, a passive order is unlikely to fill before price moves away, so take; when I is against you, post and wait. The diffusion model gives the fill-versus-move probabilities in closed or semi-closed form once calibrated.

## Relevance to SOL perpetuals at minutes to hours
Useful for the execution layer of the bot rather than the alpha layer. On a one-tick-spread SOL perp the "third of a spread" bound means the signal cannot pay taker fees by itself, which matches the live crypto evidence in the Albers et al. note. The side-dependent drift result shows that the price path up to a passive fill is not the unconditional one, so passive entries on Kalshi should be evaluated with fill-conditional markouts rather than mid-price forecasts.

## Caveats
One stock, one quarter. Large-tick setting with a constant one-tick spread assumed in the model. No costs or strategy backtest. A practitioner-authored working paper without out-of-sample testing.
