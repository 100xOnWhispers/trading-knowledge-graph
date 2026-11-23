---
title: "CFTC Regulation 40.2(a) Certification: Listing of the nano Solana Perp Style Futures (Coinbase Derivatives Submission #2025-40)"
authors: "Coinbase Derivatives, LLC"
year: 2025
venue: "CFTC product filing (self-certification), July 31, 2025"
url: "https://www.cftc.gov/filings/ptc/ptc07312527698.pdf"
pdf: "sources/06-kalshi-venue/coinbase-2025-nano-solana-perp-style-futures-filing.pdf"
access: "full-text"
source_type: "documentation"
evidence_grade: "B"
topic: "06-kalshi-venue"
asset_class: "crypto"
horizon: "n/a"
tags: "coinbase-derivatives, sol, perp-style-futures, hourly-funding, competing-venue, regulated-us-perps"
---

## Key insight
Coinbase Derivatives listed a SOL "perp style" future ten months before Kalshi's perp, built as a five-year dated future with hourly funding instead of a true perpetual. Its funding formula, reference index, trading hours and limits all differ from Kalshi's, so the two US SOL contracts are not fungible and their basis to each other carries information about venue-specific pressure.

## Method
A 16-page self-certification with a specification table, core-principle analysis, the index methodology (Appendix A) and the funding "cash adjustment" method (Appendix B).

## Data and sample
One contract: nano Solana Perp Style Futures, code SLP, to trade on or after August 18, 2025, cleared by Nodal Clear.

## Reported results
- Structure: "long dated (5-year expiration), cash-settled"; initial expiry the third Friday of December 2030.
- Size: 5 SOL per contract. Tick $0.01 per SOL ($0.05 per contract).
- Hours: Friday 5:00 PM CT to Friday 4:00 PM CT, a one-hour weekly break.
- Index: MarketVector Coinbase Solana Benchmark Rate, built from Coinbase spot trades only.
- Funding: computed hourly by the clearing house and applied at the mid-day and end-of-day margin runs. `Premium = TWAP([(Futures Mark - Spot Mark) / Spot Mark / 24], 1 hour, 3 min)`, i.e. twenty 3-minute observations averaged and scaled by 1/24. Funding rate `= 0.75 * Premium + 0.25 * previous funding rate`. Payment `= rate * position * multiplier * futures mark * -1`.
- Futures mark: 3-minute VWAP; if no trades, 3-minute TWAP of the best bid/offer midpoint.
- Controls: fair-value limit rejecting orders more than 5% from the spot mid; price fluctuation limit of 10% of the hourly reference price.
- Position limit: 340,000 contracts (1.7M SOL); reportable level 25 contracts.
- Daily settlement at 3:00 PM CT using a 60-second VWAP, then a midpoint TWAP, then an index-based fallback.

## Signal construction
Not a signal by itself. A cross-venue feature can be built from it: the Coinbase SLP premium to Coinbase spot and its hourly funding rate, compared with the Kalshi premium index. Inputs are Coinbase Derivatives market data and Coinbase spot; update hourly for funding and continuously for the premium.

## Relevance to SOL perpetuals at minutes to hours
Three differences matter. Coinbase funding is hourly, smoothed and has no deadband in the filing, so it moves continuously where Kalshi's is zero most of the time; it may be a more sensitive gauge of US positioning. Coinbase references Coinbase spot alone, while Kalshi references a five-venue order-book index. Coinbase closes for an hour each Friday while Kalshi closes on Thursday mornings, so each venue has a window in which it is the only regulated US SOL perp trading. Whether Coinbase leads Kalshi at the minute scale is untested.

## Caveats
The filing dates from July 2025 and terms may have changed; current Coinbase documentation could not be fetched (the site refused automated requests). No leverage, margin or fee figures are given. A third-party article, not a primary source, says Coinbase's US perp access relies on CFTC staff no-action relief; this was not verified. No volume or open-interest data for SLP was obtained, so its relative liquidity against Kalshi is unknown.
