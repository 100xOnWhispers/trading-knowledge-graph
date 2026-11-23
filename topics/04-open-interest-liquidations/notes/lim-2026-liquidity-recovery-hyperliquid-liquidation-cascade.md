---
title: "Two-Regime Liquidity Recovery After a Perpetual Futures Liquidation Cascade: Evidence from Hyperliquid and the October-10th-2025 Event"
authors: "Lim, Boon Chuan"
year: 2026
venue: "The Journal of FinTech and Digital Assets, 1(2), 54-68"
url: "https://journals.lincoln.ac.nz/index.php/JFDA/article/download/1395/965/3881"
pdf: "sources/04-open-interest-liquidations/lim-2026-liquidity-recovery-hyperliquid-liquidation-cascade.pdf"
access: "full-text"
source_type: "peer-reviewed"
evidence_grade: "B"
topic: "04-open-interest-liquidations"
asset_class: "crypto"
horizon: "minutes"
tags: "october-2025, liquidity, spread, depth, hyperliquid, sol, post-cascade-recovery"
---

## Key insight
A minute-level record of how the inside market on Hyperliquid behaved through the 10 October 2025 cascade and the weeks after, including SOL. The stress was compressed into about three hours, with spreads peaking in the 21:00 UTC hour and intraday recovery well under way by the end of the day. Afterwards spreads recovered to near pre-event levels within about three weeks, but top-of-book depth kept shrinking. Spread alone therefore understates how impaired liquidity remains after a cascade.

## Method
Descriptive event study against the venue's own pre-event baseline (3 to 9 October 2025). From each L2 snapshot: quoted spread `S = 10000 * (ask - bid) / mid`, inside depth `D = bid_size * bid + ask_size * ask`, simulated round-trip cost at USD 50K, 100K and 500K, and one-minute realized volatility from one-second mid returns. Values are sampled to one-minute bins; daily medians are divided by baseline medians and smoothed with a 7-day rolling median. Recovery is measured as days until the spread ratio falls below 1.5, 1.2 and 1.1. A 23-day "clean window" (11 October to 2 November) excludes a second selloff on 3 to 4 November.

## Data and sample
Hyperliquid public L2 archive (top 20 levels per side, median snapshot gap 0.543 seconds) for BTC, ETH, SOL, XRP and DOGE perpetuals, 15 September to 15 December 2025; 531,305 asset-minute observations. Archive gaps on 17 to 22 October and 18 to 25 November.

## Reported results
- Pre-event baseline for SOL: median spread 0.467 bps, median inside depth USD 444,653, median realized volatility 5.57 bps. BTC: 0.088 bps and USD 1.83 million.
- Pooled across assets, median spread stayed between 0.37 and 0.44 bps through hour 14 UTC, rose from hour 15, and peaked in hour 21 at 9.38 bps median, 87.5 bps at the 95th percentile and 241.8 bps maximum, with median realized volatility 150.6 bps. By hour 23 the median spread was 1.08 bps.
- Clean-window spread recovery for SOL: maximum ratio 1.43, end-of-window ratio 1.19, 14 days to fall below 1.2, and 1.1 not reached. BTC reached 1.07 by the end of the window.
- SOL depth ratio: 0.93 in the first week and 0.90 in days 17 to 23. BTC fell from 0.93 to 0.77 and ETH from 0.88 to 0.79. Over the full 51 days ETH and DOGE depth fell below half of baseline.
- Spreads vary by only about 7% across hours of the day and 6% across days of the week in the baseline.

## Signal construction
Not a directional signal. It defines two state variables for execution and sizing: the ratio of current inside spread to a trailing baseline, and the ratio of current inside depth to a trailing baseline. A bot should carry both, because depth stays impaired after spread has normalized. During a cascade, the 95th-percentile spread (tens of basis points on majors) is the relevant cost assumption for any taker order.

## Relevance to SOL perpetuals at minutes to hours
SOL is in the sample, so the numbers transfer directly as a reference for a large venue. They imply that back-tests using normal-regime spread and depth will overstate the profit from trading a cascade, and that post-cascade impact costs remain elevated for weeks. Kalshi's SOL book is smaller and its makers may hedge on venues like Hyperliquid, so a depth withdrawal there plausibly propagates; this was not tested.

## Caveats
One event, one venue, top 20 levels only, and a single independent author in a new journal. Makers cannot be identified, so the cause of the depth contraction is inferred. The archive gap removes days 7 to 12 after the event. No comparison with centralized venues.
