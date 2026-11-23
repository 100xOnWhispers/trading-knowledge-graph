---
title: "The Market Maker's Dilemma: Navigating the Fill Probability vs. Post-Fill Returns Trade-Off"
authors: "Albers, Jakob; Cucuringu, Mihai; Howison, Sam; Shestopaloff, Alexander Y."
year: 2025
venue: "arXiv:2502.18625v2"
url: "https://arxiv.org/pdf/2502.18625"
pdf: "sources/07-order-book-imbalance/albers-2025-market-makers-dilemma-fill-probability.pdf"
access: "full-text"
source_type: "working-paper"
evidence_grade: "B"
topic: "07-order-book-imbalance"
asset_class: "crypto"
horizon: "seconds"
tags: "order-book-imbalance, binance, bitcoin-perpetual, live-experiment, fill-probability, adverse-selection, taker-fee, queue-position, reversal"
---

## Key insight
A live experiment on the Binance BTC perpetual shows that top-of-book imbalance does predict the next price move, yet none of the obvious ways to trade it makes money. Taking in the direction of the imbalance earns about 1 basis point per round trip before fees and loses after the taker fee. Posting passively with the imbalance rarely fills; the fills that do occur are the cases where the imbalance was wrong. Fill probability and post-fill return are negatively correlated, so viable maker entries are often contrarian to the imbalance.

## Method
The authors placed real minimum-size maker orders at the best bid and ask, with no signal and no discretionary cancellation (cancel only when the price leaves the order behind), and recorded fills, exact queue position at fill (recovered from Binance's public trade feed identifiers), and markout returns one second after the fill. They then backtest on this order set a naive two-sided maker, an imbalance-conditioned maker (post only when imbalance magnitude exceeds 0.5, with and without cancellation at zero), and an imbalance taker (take when magnitude exceeds 0.5). Finally, logistic regression and random forest models predict "reversals": filled orders posted against the imbalance where the next price change is favorable.

## Data and sample
Binance USDT-margined BTC perpetual. Continuous quoting 12 to 19 February 2024: 232,897 orders, 127,051 filled. Periodic quoting 21 to 31 August 2024: 172,800 orders, 95,998 filled. Fees assumed at the best tier: taker 1.5 bp, maker rebate 0.5 bp. Tick is 0.1 USD (about 0.03 bp); spread almost always one tick.

## Reported results
- Fill probability is well described by top-of-book queue sizes and queue position; about 50% for balanced queues at a one-tick spread.
- With a favorable imbalance (large near-side queue, small opposite queue), average one-second markout is -0.058 bp for front-of-queue fills and -0.775 bp for back-of-queue fills. With both queues large: -0.296 bp and -1.157 bp.
- All imbalance-based strategies have negative net returns. The taker version is about +1 bp per round trip before fees and unprofitable after paying the taker fee on both legs.
- The naive maker loses on average 0.44 bp per round trip net of rebates.
- About 15% of orders are reversals. Posting only when predicted reversal probability exceeds roughly 24% to 26% improves post-fill returns by a statistically significant 0.1 to 0.2 bp over random orders; the resulting strategy is slightly profitable at minimum size and best fees, and judged not scalable.

## Signal construction
For a taker: imbalance `(Q_b - Q_a)/(Q_b + Q_a)` above a threshold gives the direction, but expected edge (about 0.5 bp per leg here) must exceed the venue's taker fee. For a maker: estimate fill probability from queue sizes and position, and require a counter-signal (recent sharp move in the last 100 ms, short top-of-book survival times, recent trade-count shifts) before posting against the imbalance.

## Relevance to SOL perpetuals at minutes to hours
This is the reality check for using raw imbalance on a crypto perp. Compare the per-leg edge with the actual fee on the execution venue: if Kalshi's fees are larger than Binance's best tier, a pure imbalance taker is further under water. For a minutes-to-hours bot, the lesson is to use imbalance to choose between resting and crossing and to evaluate passive fills by markout, not to treat it as alpha. SOL's larger relative tick may raise both the imbalance edge and queue-priority effects; this needs measurement.

## Caveats
One instrument, two short windows, minimum-size orders. Backtests ignore latency. Best-tier fees assumed. Working paper.
