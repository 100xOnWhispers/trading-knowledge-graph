---
title: "Kalshi Help Center: Crypto Markets (crypto event contracts and CF Benchmarks settlement), with the API page on the CF Benchmarks REST passthrough"
authors: "Kalshi"
year: 2026
venue: "help.kalshi.com and docs.kalshi.com"
url: "https://help.kalshi.com/en/articles/13823838-crypto-markets"
pdf: "none"
access: "full-text"
source_type: "documentation"
evidence_grade: "D"
topic: "06-kalshi-venue"
asset_class: "crypto"
horizon: "minutes"
tags: "kalshi, event-contracts, binary-options, implied-probability, cf-benchmarks, information-source, index-data"
---

## Key insight
Kalshi lists short-dated binary contracts on crypto prices, including 15-minute up-or-down markets and hourly range markets, that settle on the same family of CF Benchmarks real-time indices used by its perps. They are a candidate same-venue information source, because their prices are risk-neutral probabilities of the index finishing above a level. The documentation establishes how they settle but offers no evidence that they predict anything.

## Method
The help article was read in full as markdown. The API documentation page for the CF Benchmarks passthrough was read through a page-to-text summariser. No event-contract market data was pulled in this session.

## Data and sample
Product documentation as served on 2026-11-22. The article names Bitcoin and Ethereum as examples; whether SOL event contracts with 15-minute or hourly expiries exist was not confirmed.

## Reported results
- Market types: above or below a level, range at expiry, 15-minute direction, and high or low over a period.
- Settlement: for most crypto price markets the expiration value is "a simple average of the CF Benchmarks index over the 60 seconds before the time named in the market's rules".
- A 15-minute market "compares the average from the minute before it closes with the average from the minute before it opened".
- Kalshi says a one-minute average is "generally less affected by a brief spike or dip".
- CF Benchmarks index values are available through Kalshi's API as a direct pass-through, with revisions possible after expiry.
- Passthrough page (summarised): endpoints under `/trade-api/v2/cfbenchmarks/`, including `/values` and tick-level `/history/values`; authentication with a Kalshi API key plus a specific entitlement; each request costs 50 read tokens against 10 for a normal request. SOLUSD_RTI is not named on the page, though the page says the list of coins is not exhaustive.
- Event contracts sit on the Predictions exchange, a separate account and API namespace from perps.

## Signal construction
A possible feature, untested. For a 15-minute direction market on SOL, if one exists: take the mid price of the "up" contract as probability `p`, subtract 0.5, and normalise by the time remaining and current volatility to get an implied drift signal. For range or above-or-below ladders at one-hour expiry, fit an implied distribution across strikes and extract its mean relative to the current index and its implied volatility. Inputs: Predictions order books over WebSocket; index level from the perps `ticker` channel `reference_price`. Update on every book change.

## Relevance to SOL perpetuals at minutes to hours
The horizon match is unusually close: 15-minute and hourly binaries price exactly the distribution a minutes-to-hours directional bot cares about, and they settle on the same index as the perp. Three uses are plausible. As a feature for a supervised or reinforcement-learning model. As a calibration target for the bot's own probability forecasts. As a hedging or expression instrument with capped loss when perp fees make short holds uneconomic. Each needs testing; binary markets on a retail venue may simply echo the perp price with a lag and a wide spread.

## Caveats
Graded D as evidence because nothing here measures informativeness. Event contracts face state-level legal challenges; a Kalshi emergency filing of November 14, 2026 describes a Louisiana restraining order against event-contract access, so availability can change by state. Event-contract fees and spreads were not examined. The index passthrough requires an entitlement that a retail account may not have. Topic owners for prediction markets or options-implied signals may cover the literature on binary-option information content; none was reviewed here.
