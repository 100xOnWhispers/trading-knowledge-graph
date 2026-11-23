---
title: "The Crypto Crash of October 2025: When Leverage Met Liquidity"
authors: "FTI Consulting (author not named on the page; listed contact: Kubali, Volkan)"
year: 2025
venue: "FTI Consulting Insights"
url: "https://www.fticonsulting.com/insights/articles/crypto-crash-october-2025-leverage-met-liquidity"
pdf: "none"
access: "full-text"
source_type: "practitioner"
evidence_grade: "D"
topic: "09-liquidity-price-impact"
asset_class: "crypto"
horizon: "hours"
tags: "liquidity-crisis, liquidation-cascade, order-book-depth, auto-deleveraging, october-2025, stress-test"
---

## Key insight
On 10 October 2025 a macro shock hit a highly leveraged crypto market and order-book liquidity largely disappeared during the sell-off. The article describes a margin-driven liquidation spiral in which depth fell by an order of magnitude and spreads widened from basis points to percent. Its practical message is that liquidity measured in calm conditions is not available in a cascade.

## Method
A consulting-firm commentary dated 24 December 2025. It is a narrative reconstruction with a timeline chart. It cites "intraday order-book data" for the depth and spread figures but names no data provider, venue or method. No statistical analysis is presented. The page was read as extracted text.

## Data and sample
The event of 10 October 2025 and the two months that followed. Assets mentioned: BTC, ETH, DOGE and the synthetic dollar USDe. Binance is the only venue named, in connection with USDe pricing.

## Reported results
All figures below are as stated in the article, without a named source:
- More than 19 billion US dollars of crypto leverage was liquidated in roughly a day.
- BTC top-of-book depth shrank by more than 90% on key venues.
- Bid-ask spreads widened from single-digit basis points to double-digit percentages at the extremes.
- A threat of 100% tariffs on China preceded the sell-off.
- Funding rates had risen from about 10% annualized to nearly 30% by 6 October.
- USDe traded in the mid-0.60s on Binance while staying much closer to 1 dollar elsewhere.
- Two months later, open interest was down more than 40% from October highs and BTC was about 30% below its early-October peak.
- Some crypto books operate at effective leverage of 20 to 50 times.
- The article recommends stress scenarios in which depth shrinks by 90% for short periods.

## Signal construction
Not a tested signal. It motivates a liquidity circuit breaker for the bot:
1. Track top-of-book and 1% depth and quoted spread on each reference venue against a trailing same-hour median.
2. Define stress when depth falls below a fraction of the median (for example 30%) or spread exceeds a multiple of it (for example 5 times), on two or more venues at once.
3. In stress: stop opening positions with market orders, widen or remove resting stops that would fill at gapped prices, and reduce size.
4. Pre-conditions worth monitoring: funding rate level and open interest relative to recent history.
The thresholds are illustrative and need calibration.

## Relevance to SOL perpetuals at minutes to hours
Liquidity crises are the tail risk for a bot that sizes positions from normal-day depth. Kalshi's low maximum leverage should mean fewer forced liquidations on Kalshi itself, but the SOL reference price is set on offshore venues where the cascade happens, so Kalshi prices will gap with them and its thinner book may dislocate from the reference. The article says nothing specific about SOL. A venue-level price dislocation like the USDe one is a reminder to use a multi-venue reference price.

## Caveats
Unsourced numbers, unnamed author, no methodology, and a publisher that sells risk advisory services. Other accounts of the same event give different magnitudes for the depth collapse, so the 90% figure should be treated as indicative. Rigorous academic studies of this event were not found in this session.
