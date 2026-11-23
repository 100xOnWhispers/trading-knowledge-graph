---
title: "Hyperliquid Docs: Funding"
authors: "Hyperliquid"
year: 2026
venue: "Hyperliquid documentation (GitBook)"
url: "https://hyperliquid.gitbook.io/hyperliquid-docs/trading/funding"
pdf: "none"
access: "full-text"
source_type: "documentation"
evidence_grade: "C"
topic: "03-perp-pricing-funding"
asset_class: "crypto"
horizon: "hours"
tags: "funding-rate-formula, hourly-funding, premium-index, oracle-price, clamp, hyperliquid"
---

## Key insight
Hyperliquid uses the same clamp-style formula as centralised exchanges, computed as an 8-hour rate, but pays one eighth of it every hour from a premium averaged over that hour only. The premium is measured against an oracle built from centralised-exchange spot prices, and the cap is loose (0.5% per hour), so its funding reacts faster and can go further than an 8-hour venue's.

## Method
Exchange specification (the markdown version of the page was read in full):
- `Funding rate F = average premium index P + clamp(interest rate - P, -0.0005, 0.0005)`.
- The formula gives an 8-hour rate; "funding is paid every hour at one eighth of the computed rate for each hour".
- Interest is fixed at 0.01% per 8 hours, i.e. 0.00125% per hour, "11.6% APR paid to short".
- "The premium is sampled every 5 seconds and averaged over the hour."
- `premium = impact_price_difference / oracle_price`, with `impact_price_difference = max(impact_bid_px - oracle_px, 0) - max(oracle_px - impact_ask_px, 0)`; impact prices are average execution prices for a contract-specific impact notional.
- Oracle prices are a weighted median of centralised-exchange spot prices, weights by liquidity.
- "Funding on Hyperliquid is capped at 0.5%/hour", described as "much less aggressive capping than CEX counterparts"; cap and interval do not depend on the asset.
- Payment is `position_size * oracle_price * funding_rate`, using the oracle price, not the mark price.
- Builder-deployed (HIP-3) perps use a more responsive premium, `0.5*(impact_bid_px + impact_ask_px)/oracle_px - 1`.

## Data and sample
None; a specification with one numerical example.

## Reported results
Worked example: interest 0.01%, impact bid 10,100 against spot 10,000 gives a premium of 1%; the clamped term is -0.05%; the funding rate is 0.95% (on the 8-hour basis, paid at one eighth per hour).

## Signal construction
Inputs: Hyperliquid book (for impact prices), oracle price, and the published hourly funding. Compute the running hourly average premium to predict the next print about an hour ahead; multiply the hourly print by 8 to compare with an 8-hour venue's rate. Features: Hyperliquid 8-hour-equivalent funding minus Binance predicted funding for SOL; the running Hyperliquid premium as a faster-updating read on leveraged demand than the 8-hour average.

## Relevance to SOL perpetuals at minutes to hours
Differences from an 8-hour venue that follow from the rules: (1) no memory beyond one hour, so the print tracks current pressure; [Le](le-2026-funding-aware-market-making-perp-dex.md) estimates a SOL half-life of about 2.3 hours; (2) 24 settlement timestamps a day, so any settlement-clock effect is spread thinly and should be weaker per event than on 8-hour venues, which is untested; (3) the oracle is external spot, so the premium is perp-versus-CEX-spot and partly reflects cross-venue lags (topic 05). For a Kalshi bot with 8-hour funding, Hyperliquid's hourly prints are an early indicator of where slower venues' averaged rates are heading, which also needs testing.

## Caveats
Documentation, not evidence; the grade reflects that. Parameters change: third-party pages found in search still quote an older, higher cap, so anything hard-coded should be re-read from the live docs. The impact notional for SOL is in a separate contract-specification page that was not opened.
