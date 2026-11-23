---
title: "Learning the Spoofability of Limit Order Books With Interpretable Probabilistic Neural Networks"
authors: "Fabre, Timothee; Challet, Damien"
year: 2025
venue: "arXiv:2504.15908v1"
url: "https://arxiv.org/pdf/2504.15908"
pdf: "sources/07-order-book-imbalance/fabre-2025-spoofability-limit-order-books.pdf"
access: "full-text"
source_type: "working-paper"
evidence_grade: "B"
topic: "07-order-book-imbalance"
asset_class: "crypto"
horizon: "seconds"
tags: "spoofing, layering, cancellations, hawkes-features, posting-distance, coinbase, level-3, manipulation, cross-asset"
---

## Key insight
Large limit orders placed away from the best quotes move the short-term price distribution on crypto exchanges, which makes books "spoofable" and makes naive depth imbalance exploitable by manipulators. A model of the one-second mid-price move that uses the size and posting distance of new limit orders flags 31% of large orders on Coinbase as capable of profitable spoofing. Suspicious orders are almost never at the top of the book, so top-of-book imbalance does not see them while deeper-level imbalance is contaminated by them.

## Method
The authors build order flow features inspired by marked Hawkes processes: exponentially decayed sums over past limit and marketable orders, weighted by size and by posting distance from the best price, at several time scales (inverse time scales of 10, 100 and 1000 per second) and distance scales, plus the spread. A small probabilistic neural network maps these features to the parameters of the conditional distribution of the mid-price move over T = 1 second. Spoofing detection takes the view of a manipulator: for each inserted limit order, compare the expected execution cost of a hidden bona fide trade with and without the order, including the risk that the spoof order is filled; flag the order if spoofing lowers expected cost. A cross-asset extension evaluates the effect of BTC orders on ETH and vice versa.

## Data and sample
Level-3 (order-by-order) data for BTC-USD and ETH-USD spot on Coinbase, one week in December 2024; detection run on all limit orders submitted from 4 to 7 December 2024, restricted to orders within 20% of the mid. Fees set at Coinbase's top tier.

## Reported results
- Posting distance is critical: price impact of a limit order vanishes quickly with distance, but orders deep in the book still generate significant short-term impact. Models ignoring distance are described as inadequate.
- Suspicious orders are about 31% of large orders and 7% of all orders in the sample.
- None of the large suspicious orders and only 0.13% of all suspicious orders are at the top of the queue, against 4.20% of large normal orders and 10.14% of all normal orders.
- Large BTC orders move the predicted ETH price distribution much more significantly than ETH orders move BTC.
- Flagged examples show layering patterns. The detection rule runs in under 100 microseconds per order in Python.

## Signal construction
For a trading bot this is a filter, not an alpha. Inputs: order-by-order or incremental L2 feed. (1) Track large resting orders by size, distance from best, and age; down-weight or exclude depth that is large, recent, and beyond the touch when computing multi-level imbalance. (2) Track cancel-to-add ratios of large orders per side as a manipulation indicator. (3) Optionally fit the paper's decayed-flow features to predict the one-second move.

## Relevance to SOL perpetuals at minutes to hours
Multi-level imbalance and book-slope signals computed on crypto venues need a robustness layer: depth away from the touch on less surveilled venues is partly non-bona fide. The cross-asset result suggests that BTC book events can be used to push other coins, so a SOL signal that keys off BTC depth inherits this risk. Kalshi is CFTC-regulated, where spoofing is prosecuted, so its own book may be cleaner, but input signals from offshore venues are not. The effects last on the order of a second, so at minutes-to-hours horizons the main exposure is bad entry timing.

## Caveats
Four days of data on two spot pairs; no ground-truth labels for spoofing, so "suspicious" is model-defined. One-second horizon only. Working paper; one author lists a commercial affiliation (SUN ZU Lab) alongside the university.
