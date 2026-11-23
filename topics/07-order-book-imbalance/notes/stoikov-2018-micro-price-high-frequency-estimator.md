---
title: "The micro-price: a high-frequency estimator of future prices"
authors: "Stoikov, Sasha"
year: 2018
venue: "Quantitative Finance 18(12), 1959-1966"
url: "https://ideas.repec.org/a/taf/quantf/v18y2018i12p1959-1966.html"
pdf: "sources/07-order-book-imbalance/stoikov-2018-micro-price-high-frequency-estimator.pdf"
access: "abstract-only"
source_type: "peer-reviewed"
evidence_grade: "B"
topic: "07-order-book-imbalance"
asset_class: "equities"
horizon: "seconds"
tags: "micro-price, weighted-mid, imbalance, spread, markov-chain, fair-value"
---

## Key insight
The micro-price is a fair-value estimate defined as the limit of expected future mid-prices conditional on the current mid, top-of-book imbalance and spread. It is a martingale by construction and, according to the journal abstract, is empirically a better predictor of short-term prices than the mid-price or the size-weighted mid-price. Access note: the journal article was not available; the abstract was read on RePEc and the method below comes from the author's own slide deck for the paper (the PDF saved with this note).

## Method
State is `(M_t, I_t, S_t)`: mid-price, imbalance `I = Q_b / (Q_b + Q_a)`, and spread. The micro-price is `P_micro = lim_i E[M_{tau_i} | F_t]`, where `tau_i` are the times of successive mid-price changes. Assuming the dynamics do not depend on the price level, `P_i = M_t + sum_{k=1..i} g_k(I_t, S_t)`, with `g_1 = E[M_{tau_1} - M_t | I_t, S_t]` and `g_{k+1}` obtained recursively. With discretized imbalance and spread states, one estimates transition matrices Q (no mid change), R1 (mid change, by size) and R2 (mid change, to new state); then `g_1 = (1 - Q)^{-1} R1 k` and `B = (1 - Q)^{-1} R2`, and the adjustment is `G* = P_micro - M = sum_i B^i g_1`. Symmetrizing the estimates guarantees convergence. The slides contrast this with the weighted mid `I*P_a + (1-I)*P_b`, which is noisy, not a martingale, and can move the "fair" price in a counter-intuitive direction when a small order cancels.

## Data and sample
From the slides: best bid and ask quotes for Bank of America (BAC, large-tick) and Chevron (CVX, small-tick), March 2011.

## Reported results
- Abstract: the micro-price is a better predictor of short-term prices than the mid or weighted mid.
- Slides: the adjustment `G*` estimated on the first day of the month is compared with realized average mid-price changes over 1, 5 and 10 minutes, bucketed by imbalance and spread, for the rest of March 2011. The slides present this graphically and conclude that the micro-price is a good predictor, is horizon independent, needs less data than fixed-horizon averaging, fits both tick regimes, and lies between bid and ask. No numerical error statistics were read.

## Signal construction
Inputs: best bid and ask prices and sizes. Offline: discretize imbalance (for example 10 buckets) and spread (in ticks), count transitions, compute `G*(I, S)` as a lookup table, and refresh it periodically. Live: `micro = mid + G*(I_t, S_t)`. The signal is `micro - mid` (or `micro - last trade`), in ticks or basis points.

## Relevance to SOL perpetuals at minutes to hours
The micro-price is the right reference price for marking, for measuring cross-venue basis (Kalshi versus Binance) without bid-ask bounce, and for deciding whether a quoted price is cheap or rich at entry. As a directional forecast it is bounded by roughly half a spread, so it cannot carry a minutes-to-hours position. The Bieganowski and Slepaczuk note gives crypto evidence that imbalance on a coarse-tick instrument tracks the location of a finer-tick price inside the spread, which is the micro-price mechanism.

## Caveats
Only the abstract and the author's slides were read; quantitative results in the article are not confirmed here. Validation covers two stocks and one month. The Markov assumption ignores deeper levels and trade flow. The lookup table must be re-estimated per venue and tick regime.
