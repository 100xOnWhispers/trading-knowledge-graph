---
title: "Measuring the engine of a liquidation cascade: subcritical branching inside a first-order transition"
authors: "Garcia Seuma, Ramon Marc"
year: 2026
venue: "arXiv preprint 2608.03616"
url: "https://arxiv.org/pdf/2608.03616"
pdf: "sources/04-open-interest-liquidations/garcia-seuma-2026-branching-ratio-liquidation-cascade.pdf"
access: "full-text"
source_type: "working-paper"
evidence_grade: "C"
topic: "04-open-interest-liquidations"
asset_class: "crypto"
horizon: "minutes"
tags: "liquidation-cascade, branching-ratio, price-impact, forced-flow, hyperliquid, october-2025, negative-result"
---

## Key insight
The popular picture of a cascade as a chain reaction, where each forced sale triggers more than one further forced sale, is tested and rejected for the record October 2025 event. Measured from Hyperliquid's on-chain fills, the branching ratio stayed around 0.1 to 0.2, most forced selling landed within 30 minutes, and the venue backstop absorbed most of it off the order book. Across seven cascades the consistent signature is in liquidity: price impact jumps several-fold and open interest clears, while no scalar measure of pre-cascade leverage or fragility predicts severity.

## Method
The branching model: forced selling of notional `V` moves price by `dp/p = k V`; a relative move sweeps liquidation density `rho_tilde` (forced notional per unit relative move); offspring mean `lambda = k * rho_tilde`, with amplification `V0 / (1 - lambda)`. Impact `k` is estimated by a Kyle-style regression on Binance and read directly from Hyperliquid's quoted impact prices. Two predictions are tested: that `lambda` rises before onset relative to matched placebo declines, and that realized amplification has unit slope on `-log(1 - lambda)`. The cross-asset "fabric" is measured by mean pairwise correlation and its dispersion. For October 2025, `lambda` is measured in flight three ways from the fill log.

## Data and sample
Seven cascades, 2022 to 2025. Binance USDT perpetual panel of 22 to 30 names at 5-minute resolution; Binance BTC one-minute klines; Hyperliquid per-minute asset contexts for five events and the on-chain fill log, which starts 25 May 2025.

## Reported results
- Impact rises in every cascade: 1.2 to 3.5 times baseline on Binance (regressed, six-hour means) and 3.2 to 9.1 times on Hyperliquid (quoted), with cascade-day maxima of 511 to 927 times.
- Open interest falls to 0.30 to 0.55 of baseline on Hyperliquid, against a 24.6% fall for Binance BTC.
- October 2025 structural `lambda`: 0.031 baseline, 0.097 late pre-onset, 0.195 nucleation, 0.140 peak. Nucleation-window forced notional USD 644 million against a full-cascade total of USD 733 million gives amplification 1.14.
- 87.8% of post-onset forced selling occurred in the first 30 minutes and 96.5% within an hour. The backstop absorbed 62.6% of forced-sell notional; in the worst minute (21:19 UTC) USD 641 million was force-sold, of which USD 64 million hit the book.
- Timing prediction not significant (Fisher p = 0.062); `lambda` on placebos correlates -0.38 with trailing 3-day return. Severity slope estimates range from -0.244 to +0.376 across four designs, each with a confidence interval that includes zero and excludes the predicted 1.0, at simulated power of 0.96 or more.
- Mean cross-asset correlation jumps 1.6 to 4.4 baseline standard deviations at onset in six of seven events.

## Signal construction
Two real-time state features: (1) Hyperliquid quoted impact spread per asset relative to its trailing baseline, as a direct liquidity-stress gauge; (2) rolling mean pairwise correlation across the liquid perp universe as a regime flag. A liquidation map (forced notional per price bucket near spot) is named as the one pre-state object the paper could not test.

## Relevance to SOL perpetuals at minutes to hours
If cascades are front-loaded and subcritical, the tradable window is short and the dominant risk is execution into a book whose impact is several times normal. Hyperliquid publishes impact prices for SOL, so the stress gauge can be built directly. The finding that pre-cascade open interest stock does not grade severity argues against sizing a directional bet on leverage level alone.

## Caveats
Single author, not peer-reviewed. Severity designs are BTC-centric; the in-flight measurement is one event on the one venue with a backstop that suppresses the measured quantity. Within-venue subcriticality does not rule out cross-venue amplification, which the author states explicitly.
