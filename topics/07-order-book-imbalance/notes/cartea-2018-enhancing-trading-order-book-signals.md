---
title: "Enhancing Trading Strategies with Order Book Signals"
authors: "Cartea, Alvaro; Donnelly, Ryan; Jaimungal, Sebastian"
year: 2018
venue: "Applied Mathematical Finance 25(1), 1-35"
url: "https://ora.ox.ac.uk/objects/uuid:006addde-3a03-4d75-89c1-04b59026e1c0/files/me4008e0ecca779b45d59231ebca3e69c"
pdf: "sources/07-order-book-imbalance/cartea-2018-enhancing-trading-order-book-signals.pdf"
access: "full-text"
source_type: "peer-reviewed"
evidence_grade: "A"
topic: "07-order-book-imbalance"
asset_class: "equities"
horizon: "tick"
tags: "volume-imbalance, market-orders, adverse-selection, stochastic-control, market-making, regime"
---

## Key insight
Top-of-book volume imbalance predicts the sign of the next market order and the size of the price move right after it. A liquidity provider who ignores it loses money to adverse selection even while earning the spread; one who conditions quoting on a coarse imbalance regime turns the same strategy profitable out of sample. Three or five imbalance regimes capture nearly all of the benefit.

## Method
Imbalance is `rho = (V_b - V_a) / (V_b + V_a)` at the best quotes, bucketed into regimes (sell-heavy below -1/3, neutral, buy-heavy above 1/3, or five buckets). Price, spread, limit and market order arrivals, and the imbalance regime are modelled as a Markov-chain-modulated pure jump process. An agent maximizes terminal wealth with a running inventory penalty by choosing when to post limit orders at the best bid and ask; the optimal feedback control is solved numerically. A "zero-intelligence" maker that always quotes both sides is the benchmark.

## Data and sample
Nasdaq message data for 11 equities (including INTC, ORCL, CSCO, EBAY, AMAT). Calibration on January to June 2014; out-of-sample test on July to December 2014 in half-hour trading periods (1,375 intervals), parameters forecast from preceding intervals, with inventory liquidated by crossing the spread at the end of each period.

## Reported results
- Depending on the stock, 91.6% to 99.9% of market orders are filled entirely at the best price, so quotes deeper than the touch are rarely hit.
- In a buy-heavy regime the next market order is very likely a buy, and the mid-price change measured 10 ms after a market order is larger in the direction of the imbalance (robust up to 100 ms).
- The always-quoting maker has negative expected earnings for every inventory limit tested, even when allowed to liquidate at the mid.
- Using imbalance regimes (nZ = 3 or 5) gives a large rise in annualized Sharpe ratio relative to both the naive maker and the spread-only strategy (nZ = 1); 3 and 5 regimes perform about the same. Higher inventory penalties raise the Sharpe ratio.
- With a pessimistic fill model (fills only when a market order clears the whole best queue), Sharpe ratios fall but remain well above the naive strategy; several stocks still show negative values in that table.

## Signal construction
Inputs: best bid and ask sizes. Compute `rho`, map to a regime, and estimate per regime (on a rolling half-hour to daily window) the arrival intensity of buy and sell market orders and the distribution of the post-trade mid move. Rule of thumb from the solved control: withdraw the quote on the side that the imbalance says will be run over, keep or add the quote on the other side, and use market orders when inventory is wrong-sided in a strong regime.

## Relevance to SOL perpetuals at minutes to hours
Directly useful for how the bot enters and exits. If the bot works entries with limit orders on Kalshi or a larger venue, it should not rest a bid when the book is sell-heavy. The finding that a coarse three-state signal suffices suggests a robust, low-parameter implementation. The magnitude of the benefit needs re-testing on crypto fee schedules and on a book where queue priority and cancellation behavior differ.

## Caveats
Assumes front-of-queue fills in the main results; the fill-adjusted table is weaker. No exchange fees or rebates and no latency. Large-tick US stocks in 2014. The Albers et al. note reports that simple imbalance-conditioned quoting lost money in a live crypto experiment.
