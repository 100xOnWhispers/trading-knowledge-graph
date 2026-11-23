---
title: "A primer on perpetuals"
authors: "Angeris, Guillermo; Chitra, Tarun; Evans, Alex; Lorig, Matthew"
year: 2022
venue: "arXiv working paper 2209.03307 (a later SIAM journal version exists; journal name not confirmed)"
url: "https://arxiv.org/pdf/2209.03307"
pdf: "sources/03-perp-pricing-funding/angeris-2022-primer-on-perpetuals.pdf"
access: "full-text"
source_type: "working-paper"
evidence_grade: "B"
topic: "03-perp-pricing-funding"
asset_class: "crypto"
horizon: "n/a"
tags: "perpetual-contracts, funding-rate, replication, power-perpetuals, pricing-theory"
---

## Key insight
If a perpetual contract is defined so that the long can always exit at a fixed payoff function of the underlying, then the fair funding rate is fully determined, model-free, by the payoff's convexity and the interest rate, and the short can replicate the contract by delta hedging. For a linear payoff the convexity term vanishes, so fair funding is pure financing. Funding above that level on a real exchange is therefore a price of demand imbalance, not of the contract itself.

## Method
Continuous time, no arbitrage, no transaction costs, continuous positive prices. A "perp with funding" pays `phi(S)` to the long on termination; the long pays `phi(S0)` at inception and a continuous funding rate `F`. Theorem 2 gives

`F = 0.5 * sum_ij (sigma sigma')_ij * S_i * S_j * d_i d_j phi(S) - (phi(S) - sum_i S_i * d_i phi(S)) * r`

and the short replicates with `Delta_i = d_i phi(S)`. A model-free form replaces volatility and the rate with realised quadratic variation of log prices and the log return of the money-market account. A second design discounts the payoff over time and needs no funding. With jumps the rates depend on jump intensity under the pricing measure.

## Data and sample
None. Examples relate specific payoffs to variance swaps, leveraged ETFs and constant-function market maker positions.

## Reported results
- The funding rate can be positive or negative and needs no knowledge of drift or a parametric volatility model.
- Applying Theorem 2 to a payoff proportional to a power of the price (a power perp) gives a funding rate with a realised-variance-times-convexity term plus a financing term. This is my application of their formula; the paper's own worked examples (variance swap, leveraged ETF) were skimmed, not transcribed.
- With jumps the results are only "semi-robust": they do not depend on volatility dynamics but do depend on jump intensity.

## Signal construction
Not a signal. It is used as a benchmark for what funding "should" be absent demand pressure: for an ordinary linear perp, close to the financing rate. Any persistent excess is a sentiment or crowding measure, which is how the empirical papers in this folder use it.

## Relevance to SOL perpetuals at minutes to hours
Limited direct use. The contract studied is one where the exchange stands ready to pay `phi(S)` on exit, which no order-book perp does: on Binance, Hyperliquid or Kalshi the exit price is the market price of the perp and funding responds to the observed premium. Both [Ackerer et al.](ackerer-2023-perpetual-futures-pricing.md) and [He et al.](he-2022-fundamentals-perpetual-futures.md) make this criticism. The paper matters for intuition and for any venue offering power or other convex perps on SOL.

## Caveats
Pure theory, frictionless, no empirical content. Three of the four authors worked at crypto investment or risk firms (Bain Capital Crypto, Gauntlet) at the time. The grade reflects the derivation, not trading evidence.
