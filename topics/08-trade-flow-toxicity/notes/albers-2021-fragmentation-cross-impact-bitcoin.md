---
title: "Fragmentation, Price Formation, and Cross-Impact in Bitcoin Markets"
authors: "Albers, Jakob; Cucuringu, Mihai; Howison, Sam; Shestopaloff, Alexander Y."
year: 2021
venue: "arXiv 2108.09750"
url: "https://arxiv.org/pdf/2108.09750"
pdf: "sources/08-trade-flow-toxicity/albers-2021-fragmentation-cross-impact-bitcoin.pdf"
access: "full-text"
source_type: "working-paper"
evidence_grade: "C"
topic: "08-trade-flow-toxicity"
asset_class: "crypto"
horizon: "seconds"
tags: "trade-flow-imbalance, cross-venue, lead-lag, perpetuals, taker-fees, live-trading"
---

## Key insight
Across 14 Bitcoin spot, futures and perpetual markets, signed taker flow on one venue predicts returns on other venues over the next half second, because trade flow arrives on one venue first and "trickles down" to the rest. Linear models on cross-venue trade flow imbalance, past returns and book imbalance explain 10% to 37% of the variance of 500 ms future returns. At default taker fees the associated taker strategies lose money everywhere, and only traders on the lowest fee tier come out ahead on some venues; which venue leads is closely tied to its fee level.

## Method
Features for each market i over lookbacks delta in {100, 250, 500, 1000, 2000} ms: trade flow imbalance TFI = (buy taker volume) - (sell taker volume) in USD; past returns in basis points; and a depth-based order book imbalance. The authors argue for the unnormalized USD imbalance over the ratio (B - S) / (B + S), because the ratio treats a 1 USD one-sided print like a 10 million USD one. A leader-lagger network is built from pairwise R-squared of one market's features on another's future returns. Composite OLS models per target market predict 500 ms returns. Each model is mapped to a threshold taker strategy and its PnL is computed three ways: no fees, default taker fees, lowest (VIP) taker fees. A maker variant was run live.

## Data and sample
Order book snapshots and trades from the 14 most liquid BTC markets in February 2021, including Binance USDT and coin-margined perpetuals, Bybit, BitMEX, Deribit, FTX and OKEx perpetuals, Huobi spot and futures. Models were fitted on 22 to 27 February 2021 and tested on the following two days.

## Reported results
- Explained variance of 500 ms future returns: 10% to 37% depending on the target market.
- The authors' depth-based book imbalance raised R-squared by 0.019 on average over the classical imbalance.
- Without fees, pairwise taker strategies are profitable with mean and median PnL of about 11,000 (in the paper's basis-point units).
- With default taker fees every pairwise PnL is negative. With VIP fees the average is still a loss (9,621 basis points) with exceptions, the best being trading Huobi spot on Binance BTC perpetual signals.
- For the composite per-market models, all PnL values with default fees are negative; with VIP fees some markets are positive, FTX the largest and, unexpectedly, the leading Binance USDT perpetual too; Deribit and BitMEX are lowest. The authors call this a "rich get richer" effect of fee tiers.
- The Binance perpetuals and Huobi quarterly futures were the most useful sources of predictive flow; Bybit was among the most predictable targets.
- A live maker experiment turned over more than 1.5 million USD notional and improved on a naive benchmark run alongside it.

## Signal construction
Inputs: live trade streams with aggressor side from the leading venues. For each venue compute USD-signed taker volume over rolling 100 ms to 2 s windows; apply a concave transform or clipping because the paper finds the return response to TFI is nonlinear; regress the target venue's next-interval return on the cross-section of leader TFIs and returns; refit on a rolling window. Update on every trade.

## Relevance to SOL perpetuals at minutes to hours
The structure maps directly onto the Kalshi case: a small, higher-fee venue should lag Binance, Bybit, OKX and Hyperliquid SOL perps, and cross-venue signed taker flow on the leaders is the first feature to build. Two things do not transfer. The horizon is 500 ms, far below minutes, and the edge at that horizon did not survive taker fees even for the lowest-fee traders on most venues. What needs testing is how much of the leader-flow information remains at 10 seconds to several minutes, and whether Kalshi's lag is long enough to be reachable without colocation.

## Caveats
Eight days of data from a single, strongly trending month; hence grade C despite out-of-sample and live tests. BTC only. Venue landscape has changed (FTX is gone, Hyperliquid did not exist). Snapshot order book data prevented computing full order flow imbalance. The synthetic walk-forward is a simulation; no explicit latency model was found in the text read.
