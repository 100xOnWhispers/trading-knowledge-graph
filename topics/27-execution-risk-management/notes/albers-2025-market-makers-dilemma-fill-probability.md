---
title: "The Market Maker's Dilemma: Navigating the Fill Probability vs. Post-Fill Returns Trade-Off"
authors: "Albers, Jakob; Cucuringu, Mihai; Howison, Sam; Shestopaloff, Alexander Y."
year: 2025
venue: "arXiv preprint 2502.18625 (version 2, November 2025)"
url: "https://arxiv.org/pdf/2502.18625"
pdf: "sources/27-execution-risk-management/albers-2025-market-makers-dilemma-fill-probability.pdf"
access: "full-text"
source_type: "working-paper"
evidence_grade: "B"
topic: "27-execution-risk-management"
asset_class: "crypto"
horizon: "seconds"
tags: "limit-orders, fill-probability, adverse-selection, maker-taker, binance-perpetual, queue-position, live-experiment"
---

## Key insight
On the Binance BTC perpetual, a resting order at the touch is likely to fill exactly when the next few seconds go against it and unlikely to fill when they go its way. Fill probability and post-fill return are negatively correlated, so a maker order is not a cheaper version of a taker order: it is a different bet with negative expected short-term drift. Naive quoting to "earn the spread plus rebate" loses money quickly.

## Method
Live trading experiments with real minimum-size orders, which avoids the queue-position guesswork of simulated fills. Continuous mode: always keep one buy at the best bid and one sell at the best ask, cancelling and reposting when the touch moves. Periodic mode: post both sides every ten seconds, cancel if the touch moves away. For each order they record fill or cancel, queue sizes, queue position, and "markout" returns after the terminal state. They then evaluate a basic market-making strategy, imbalance-following maker and taker strategies, and a model (logistic regression among others) that predicts "reversals", cases where imbalance wrongly predicts the next price change.

## Data and sample
Binance USDT-margined BTC perpetual. Continuous mode: 12 to 19 February 2024, 232,897 orders, 127,051 filled. Periodic mode: 21 to 31 August 2024, 172,800 orders, 95,998 filled. Fees assumed at Binance's best tier: taker 1.5 bp, maker -0.5 bp (a rebate). Tick size about 0.03 bp of price.

## Reported results
- Orders with negative subsequent five-second returns are highly likely to fill; those with positive returns much less so. Unconditional expected return of the experiment's orders: about -0.8 bp, or -0.3 bp net of rebate.
- Markout by state: with a large near-side and small opposite-side queue, -0.296 bp for front-of-queue fills and -1.157 bp for back-of-queue fills. With a small near-side and large opposite-side queue, -0.539 bp (front) and -0.763 bp (back).
- Basic market making lost almost 60% in about three days and seven hours including rebates; annualised Sharpe ratio -109; average holding time about 11 seconds; average loss 0.44 bp per round trip net of rebates.
- Imbalance-following taker strategy: about +1 bp per round trip before fees, wiped out by the taker fee on both legs.
- Imbalance-following maker strategies fail on fill probability: they fill mostly on reversals.
- Only about 15% of orders are reversals. Posting only when predicted reversal probability exceeds 0.24 gave 327 round trips per day at an average +0.71 bp and a Sharpe ratio of 11.97; the authors state this is unlikely to persist at larger size or worse fee tiers.

## Signal construction
For the execution layer: before posting passively, compute touch imbalance, near-side and opposite-side queue sizes, and recent price changes; estimate the probability of a fill and the expected markout conditional on a fill. A passive order has positive expected value only if `rebate_or_fee_saving + expected_markout_given_fill > 0` after weighting by fill probability and by the cost of the fallback when it does not fill. Update on every book event.

## Relevance to SOL perpetuals at minutes to hours
This is the most relevant evidence for the maker-or-taker choice. On Kalshi the fee gap for a retail account (2 bp maker against 12 bp taker at the entry tier, per the topic 06 fee note) is far larger than Binance's 2 bp gap, so passive entry can absorb roughly 1 bp of adverse markout and still win. The cost that remains is non-execution: a directional bot's passive orders will miss precisely the moves its signal predicted. The expected-value comparison must include the missed-trade term, and it must be measured with real small orders on Kalshi, as these authors did.

## Caveats
One instrument, one venue, two short windows, minimum order size, best fee tier, latency treated as negligible. The reversal model's test span is about 3.5 days. Kalshi's SOL book has a wider spread (median 4.5 bp in the topic 06 snapshot) and different participants, so magnitudes will differ. Working paper.
