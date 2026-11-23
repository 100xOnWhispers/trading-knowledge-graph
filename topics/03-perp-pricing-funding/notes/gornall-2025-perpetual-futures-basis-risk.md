---
title: "Perpetual Futures and Basis Risk: Evidence from Cryptocurrency"
authors: "Gornall, Will; Rinaldi, Martin; Xiao, Yizhou"
year: 2025
venue: "Working paper (preliminary draft, 19 May 2025), AEA 2026 conference programme; an earlier version was titled Funding Payments Crisis-Proofed Bitcoin's Perpetual Futures"
url: "https://ftp.aeaweb.org/conference/2026/program/paper/ByyFEfr4"
pdf: "sources/03-perp-pricing-funding/gornall-2025-perpetual-futures-basis-risk.pdf"
access: "full-text"
source_type: "working-paper"
evidence_grade: "B"
topic: "03-perp-pricing-funding"
asset_class: "crypto"
horizon: "hours"
tags: "perpetual-futures, basis-risk, quarterly-futures, stress, funding-payments, liquidity"
---

## Key insight
Frequent funding payments keep perpetual prices much closer to spot than dated futures, especially in crashes. Around large spot moves, quarterly futures overshoot spot by 8 to 10 percent of the move while perpetuals overshoot by about 3 percent, and the perpetual's gap closes within hours. Funding then pays the losing side, so the perp ends up losing less than spot.

## Method
Idealised funding is `payment(t) = delta * (P(t) - S(t))`, with `delta` setting convergence strength; the authors note that standard formulas turn a 2% dislocation into at least 2% a day of arbitrage profit. Empirics compare BitMEX perpetual and quarterly BTC contracts on quoted spreads, liquidations, and returns in event windows around hourly spot moves above 5% (average move 5.8% within two hours). A basis trade (futures hedged with spot) is scaled to 10x leverage with 10% annual financing. A model with market makers, liquidity traders and hedgers under capital constraints rationalises the results.

## Data and sample
BitMEX (trades and top of book from November 2014), Deribit (from February 2017), Kraken Futures (from January 2018), all to 31 December 2023. Spot is the Coin Metrics median of Coinbase, Bitfinex and Bitstamp. Aggregate volume covers 20 futures exchanges.

## Reported results
- Perpetual quoted spreads are 49 to 83% tighter than comparable quarterly futures, and were tighter soon after launch.
- In >5% hourly moves the front quarterly loses 8% more than spot (0.5 points) and the second quarterly 10% more (0.6 points); the perpetual 3% more (0.1 points).
- Within 16 hours of the shock the perpetual position has lost less than spot, because funding flows to the losing side.
- The 10x basis trade loses 4.3 to 4.6% in the two hours around the shock using quarterlies and 1.5% using the perpetual; perpetual losses also revert faster.
- Quarterly spreads widen much more than perpetual spreads in stress.
- Liquidations migrated from quarterly to perpetual contracts after perpetuals launched.

## Signal construction
Not a standalone signal. It supplies two conditional expectations for a bot: after a spot move above roughly 5% in an hour, expect a perp overshoot of a few percent of the move that mean-reverts within hours, and expect funding to turn against the winning side over the next one or two funding windows. Inputs: hourly spot return, perp-minus-index premium, time since shock.

## Relevance to SOL perpetuals at minutes to hours
The overshoot-and-revert pattern is measured on BTC at BitMEX, a deep venue. On a thin venue the overshoot could be larger and slower to close; the paper's own model says divergence grows when market-maker capital is scarce. SOL moves of 5% in an hour are far more common than for BTC, so the event threshold needs rescaling (for example by volatility) before testing.

## Caveats
Preliminary draft. Event-study evidence, one venue for the core result, no trading strategy and no costs. The acknowledgements list funding support from Aquanow (a crypto liquidity firm), MITACS and SSHRC, and a search listing indicates the lead author cited the paper in a CFTC comment letter on perpetuals (letter not opened). Liquidation findings belong to topic 04.
