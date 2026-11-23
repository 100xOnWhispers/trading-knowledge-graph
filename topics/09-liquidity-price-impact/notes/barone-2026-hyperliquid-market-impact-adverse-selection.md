---
title: "Trading in the Sunshine or in the Shade: Market Impact and Adverse Selection on Hyperliquid"
authors: "Barone, Davide; Lillo, Fabrizio"
year: 2026
venue: "arXiv:2606.15715v1 (q-fin.TR)"
url: "https://arxiv.org/pdf/2606.15715"
pdf: "sources/09-liquidity-price-impact/barone-2026-hyperliquid-market-impact-adverse-selection.pdf"
access: "full-text"
source_type: "working-paper"
evidence_grade: "B"
topic: "09-liquidity-price-impact"
asset_class: "crypto"
horizon: "hours"
tags: "price-impact, metaorder, hyperliquid, perpetual-futures, twap, square-root-law, adverse-selection, order-book-depth"
---

## Key insight
On Hyperliquid perpetuals, where every trade carries an address and native TWAP orders are publicly visible while they run, impact can be measured for millions of real metaorders. A single square-root law does not describe the data: visible TWAPs follow a power law with exponent near 0.3, while hidden metaorders follow a curved, saturating relation. Announced flow is cheaper to execute and leaves less permanent impact, and the order book visibly adds depth to absorb it.

## Method
Hidden ("statistical") metaorders are reconstructed by grouping same-sign market orders from one address. Native TWAPs are identified directly. Temporary impact is the signed relative price change from start to end of execution, divided by daily volatility estimated with the Parkinson high-low estimator over a rolling 24 hours. Order size is the traded fraction phi = Q / V_24h, decomposed as phi = eta * F (participation rate times volume-time duration). Impact curves are fitted to binned means; cost comparisons use matched samples and regressions on common support. Book responses use one-minute snapshots.

## Data and sample
All 201 Hyperliquid perpetual markets, 28 July 2025 to 23 March 2026: about 4.3 million hidden metaorders and 465,000 visible TWAP executions, completing within 24 hours. Order-book snapshots: 15 December 2025 to 23 March 2026 at one-minute frequency.

## Reported results
- Visible TWAPs: impact proportional to phi^0.303 (exponent 0.303 +/- 0.002), well below one half.
- Hidden metaorders: an arctangent-shaped curve in log-log space (R-squared 0.968), flat at small phi, steep in the middle, saturating at high phi.
- Pooled surface: I = Y * eta^delta * F^gamma with Y = 0.186, delta = 0.118, gamma = 0.306, R-squared 0.886. Duration in volume time matters more than participation rate.
- Median participation rate is about 3.4% for hidden metaorders and about 0.45% for TWAPs.
- Visible TWAPs have about 9 basis points lower temporary impact than comparable hidden metaorders, and about 5 basis points less post-execution price displacement.
- Hidden metaorders trading alongside same-direction visible TWAP flow pay 0.8 to 0.9 basis points more permanent cost per 10 percentage point increase in same-side TWAP dominance.
- In the 30 minutes before hidden metaorders start, price has moved against them by 7.0 basis points on average (they are contrarian); TWAPs start with the trend (+18.2 basis points, 58.4% in the same direction).
- While a TWAP is active, displayed depth rises and the book tilts toward the absorbing side, more so for larger announced orders.

## Signal construction
1. Visible-TWAP pressure: from Hyperliquid's public data, sum the remaining notional of active TWAPs per side for SOL, as a share of 24-hour volume. This is known future flow.
2. Expected drift from that flow: about 0.186 * sigma_daily * eta^0.118 * F^0.306 at completion, with partial reversion afterward since announced flow has smaller permanent impact.
3. Depth tilt: change in displayed depth on each side while TWAPs are active.
Update every minute.

## Relevance to SOL perpetuals at minutes to hours
This is the only large-sample impact study on crypto perpetuals found for this topic, and the instrument type and horizon match the bot's. Hyperliquid is an input venue: its transparent TWAP flow is a pre-announced order-flow signal that cannot be seen on centralized venues. The low exponents imply that small orders cost relatively more than the square-root rule predicts and large patient ones relatively less. Per-asset results for SOL are not broken out in the parts read, so SOL-specific fits are needed.

## Caveats
A single-version preprint from June 2026, not yet peer-reviewed. Hidden metaorders are inferred by a splitting heuristic, and one trader can use many addresses. Results pool 201 markets of very different liquidity. Eight months of data in one market regime. Whether TWAP flow can be traded on profitably after costs is not tested.
