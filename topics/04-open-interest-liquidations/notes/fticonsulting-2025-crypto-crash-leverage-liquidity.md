---
title: "The Crypto Crash of October 2025: When Leverage Met Liquidity"
authors: "FTI Consulting (author not named on the page; key contact listed as Kubali, Volkan)"
year: 2025
venue: "FTI Consulting Insights, 24 December 2025"
url: "https://www.fticonsulting.com/insights/articles/crypto-crash-october-2025-leverage-met-liquidity"
pdf: "none"
access: "full-text"
source_type: "industry-research"
evidence_grade: "D"
topic: "04-open-interest-liquidations"
asset_class: "crypto"
horizon: "hours"
tags: "october-2025, case-study, liquidations, auto-deleveraging, usde, collateral, order-book-depth"
---

## Key insight
A consultancy narrative of the 10 October 2025 deleveraging, the largest liquidation event on record. Its account is that elevated leverage met a macro shock, order-book depth collapsed, and venue-specific collateral pricing and auto-deleveraging turned a sell-off into a margin-driven spiral. It is useful as a compact statement of the commonly accepted sequence of events and of the collateral channel, which the academic papers on the event mostly leave aside.

## Method
Descriptive commentary with one timeline chart. No data appendix or methodology is given.

## Data and sample
The 10 October 2025 event and roughly the two months after it. Figures are stated without sources on the page as read.

## Reported results
- More than USD 19 billion of leveraged crypto positions were liquidated in roughly a day.
- The trigger was a threatened 100% tariff on China.
- Before the event, perpetual funding rose from about 10% annualized to nearly 30% by 6 October, and BTC and ETH perpetual open interest was described as elevated, with no figure given.
- A large share of the exposure was concentrated on venues using unified (cross-asset) margin, which ties portfolios to their weakest assets under stress. Frozen exchange interfaces prevented some traders from managing risk or moving capital.
- BTC top-of-book depth shrank by more than 90% on key venues; bid-ask spreads widened from single-digit basis points to double-digit percentages at the extremes.
- Some books effectively operated at 20 to 50x leverage.
- The synthetic dollar USDe traded in the mid-0.60s on Binance, about a 35% discount, while staying much closer to USD 1 elsewhere. Positions that would have been solvent under cross-venue pricing were liquidated because collateral was marked at the local price.
- Auto-deleveraging closed profitable hedged shorts, leaving some hedged portfolios naked.
- About two months later BTC was roughly 30% below its early-October high and open interest more than 40% below October highs.
- Several large venues afterwards tightened leverage caps on selected pairs, raised haircuts on fragile collateral and announced steps toward multi-venue oracle pricing.
- Recommendation: stress-test for market depth shrinking by 90% for short periods.

## Signal construction
Not a signal. It suggests monitoring items that are not standard open interest features: (1) the price of margin-eligible collateral assets on each venue relative to other venues, since a local depeg changes effective leverage instantly; (2) the share of open interest on venues with unified cross-asset margin; (3) the pre-event combination of rising funding and elevated open interest, which is described but not tested as a predictor.

## Relevance to SOL perpetuals at minutes to hours
The collateral channel is the main addition: effective leverage depends on how the collateral basket behaves under stress, so nominal open interest understates fragility when collateral is itself volatile or venue-priced. For a SOL bot this argues for tracking stablecoin and staked-asset collateral dislocations on Binance and other large venues as a cascade accelerant. Kalshi margin is in dollars under a regulated clearing structure, so this channel should not operate locally, but it drives the offshore prices that Kalshi tracks.

## Caveats
Marketing-adjacent commentary from an advisory firm, with unsourced numbers and no quantitative method. The USD 19 billion figure is widely repeated but depends on exchange-reported liquidation feeds that are known to be incomplete (see the Binance documentation note). Causal claims about USDe are debated in other sources seen during search.
