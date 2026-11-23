---
title: "Order Approving KalshiEX LLC BTCPERP Futures Contract"
authors: "U.S. Commodity Futures Trading Commission"
year: 2026
venue: "CFTC order, May 29, 2026"
url: "https://www.cftc.gov/filings/documents/2026/orgdcmkexbtxperporder26601.pdf"
pdf: "sources/06-kalshi-venue/cftc-2026-btcperp-approval-order-perpetual-futures.pdf"
access: "full-text"
source_type: "documentation"
evidence_grade: "B"
topic: "06-kalshi-venue"
asset_class: "crypto"
horizon: "n/a"
tags: "cftc, regulation, perpetual-futures, futures-classification, core-principle-3, funding-mechanism, kalshi"
---

## Key insight
The CFTC approved Kalshi's bitcoin perpetual as a futures contract under Regulation 40.3 and extended the reasoning to "similarly structured perpetual contracts" on digital commodities with deep, continuous spot markets. That scope statement is what allowed Kalshi to self-certify SOL and other crypto perps within days. The order ties the legality of the design to the reliability of the spot reference at every funding interval.

## Method
A nine-page Commission order. It summarises Kalshi's May 28, 2026 submission, restates Kalshi's legal analysis of what makes a contract a future, applies the statutory approval standard, and makes findings.

## Data and sample
Legal document; no data. Subject: BTCPERP, referencing the CF Benchmarks Bitcoin Real Time Index, trading in units of 1/10,000 of a bitcoin, 24 hours a day.

## Reported results
- Kalshi submitted the contract on May 28, 2026; the order is dated May 29, 2026.
- Standard applied: the Commission "shall approve" a new contract unless it finds the contract violates the Commodity Exchange Act.
- Finding: listing BTCPERP "as a futures contract ... would not violate the CEA or the Commission's regulations".
- The Commission describes funding as the substitute for expiry convergence: payments impose "a periodic cost on whichever side is 'trading away' from the spot price".
- Three spot-market properties support the mechanism: 24/7 trading across distributed venues, so the reference is continuously observable; depth, so the reference "cannot be changed at a relatively low cost"; and continuous access for arbitrageurs, without which "price dislocations could grow, triggering liquidations".
- Scope: the analysis is "limited to the BTCPERP Contract and similarly structured perpetual contracts that reference the spot price of bitcoin or other digital commodities that have deep, active, and continuous spot market trading". It "does not extend to underlying asset classes other than digital commodities".
- The order says Kalshi "and other DCMs" may list the contract.

## Signal construction
Not a signal. It is used to assess regulatory durability of the venue and to understand which design features the regulator treats as load-bearing: the index, the funding mechanism and continuous arbitrage access.

## Relevance to SOL perpetuals at minutes to hours
SOL is not named. The SOL perp rests on Kalshi's own judgement, in a self-certification, that SOL is a digital commodity with a deep and continuous spot market. If the CFTC later disagreed, or if SOL spot liquidity on the five index venues deteriorated, the contract terms could change. The order's emphasis on arbitrage access also explains why the venue should track spot closely in normal conditions, and why the Thursday maintenance window and low leverage are the main sources of tracking risk.

## Caveats
The voting summary of the accompanying policy statement lists only Chairman Selig voting in the affirmative and no negative votes; a differently composed Commission could revisit the approach. Kalshi's marketing describes these as the first perpetual futures in America, but the CFTC filing index shows Coinbase Derivatives certified "perp style" futures in June and July 2025 and Bitnomial certified perpetual futures in January and May 2026, before this order. The order is silent on leverage, margin, liquidation and fees.
