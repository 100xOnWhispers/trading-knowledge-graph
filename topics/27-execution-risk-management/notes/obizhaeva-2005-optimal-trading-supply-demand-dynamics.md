---
title: "Optimal Trading Strategy and Supply/Demand Dynamics"
authors: "Obizhaeva, Anna; Wang, Jiang"
year: 2005
venue: "NBER Working Paper 11444"
url: "https://www.nber.org/system/files/working_papers/w11444/w11444.pdf"
pdf: "sources/27-execution-risk-management/obizhaeva-2005-optimal-trading-supply-demand-dynamics.pdf"
access: "full-text"
source_type: "working-paper"
evidence_grade: "B"
topic: "27-execution-risk-management"
asset_class: "equities"
horizon: "hours"
tags: "optimal-execution, order-book-resilience, transient-impact, trade-scheduling"
---

## Key insight
What matters for execution cost is how fast the order book refills after being hit (its resilience), not only its static depth. When resilience is finite the optimal schedule is not a smooth flow: it is a block trade at the start, a constant-rate flow matched to the refill rate, and a block trade at the end. Smooth schedules of the Almgren-Chriss type are optimal only in the limit of an instantly refilling book.

## Method
A block-shaped limit order book with density `q` on the ask side. A buy trade eats into the book and displaces the ask from its steady state; the displacement `D_t` decays exponentially at rate `rho` (half-life `log(2)/rho`). Permanent impact is `lambda` per unit traded. The trader buys `X_0` by time `T`, choosing trade times and sizes. Solved first on a fixed grid of `N` trades, then in the limit `N -> infinity`, then in continuous time with both discrete and continuous trades allowed. Extensions: time-varying resilience and risk aversion.

Limit solution (their Proposition 2): initial block `x_0 = X_0/(rho*T + 2)`, final block of the same size, and continuous trading at rate `rho*X_0/(rho*T + 2)` in between. After the first block the strategy holds the book's displacement constant, so new liquidity arrives at a steady rate and is consumed as it arrives.

## Data and sample
No empirical data; numerical examples only. Order `X_0` = 100,000 shares, price $100, depth `q` = 5,000, horizon one trading day of 390 minutes.

## Reported results
- Low resilience (`rho` small): most of the order goes in the two block trades. High resilience: most goes in the continuous flow, as in conventional models.
- Cost saving versus the simple continuous strategy: for `rho` = 2 (half-life 135 minutes) between 4.32% (with `lambda = 1/(2q)`) and 11.92% (with `lambda` = 0). For `rho` = 300 (half-life 0.90 minute) at most 0.33%. For `rho` = 0.001 the saving is minuscule because cost becomes strategy-independent.
- As the horizon `T` grows, the two block trades shrink.
- Results carry over with time-varying `rho_t` by replacing `rho*T` with the integral of `rho_t`.

## Signal construction
Not a signal. It is an execution schedule that needs one extra parameter beyond Almgren-Chriss: book resilience `rho`. Estimate `rho` by measuring how quickly the spread and near-touch depth recover after large trades (regress displacement on its lag at 1 to 10 second sampling). Then set block size `X_0/(rho*T + 2)` and the trading rate `rho*X_0/(rho*T + 2)`.

## Relevance to SOL perpetuals at minutes to hours
Transfers as a design principle for exits in thin books: take available liquidity first, then trade at the pace the book refills, and do not leave a large residual for the deadline. Resilience on a young venue with few market makers is likely slower and more variable than on Binance, and it probably depends on whether the reference venues are moving. For bot-sized clips inside top-of-book depth the model reduces to a single trade. The resilience estimate is also a useful state variable for deciding whether a passive order is likely to be refilled behind.

## Caveats
Stylised block-shaped book with exponential, deterministic recovery; no strategic response from other traders; risk neutrality in the main results. Read in the 2005 working-paper version; a later journal version exists but was not opened. Savings are relative to a specific benchmark under assumed parameters, not measured in markets. Fees and the maker-taker choice are absent.
