---
title: "Hyperliquid Docs: Fees"
authors: "Hyperliquid (documentation)"
year: 2026
venue: "Hyperliquid documentation, page as fetched on 2026-11-22"
url: "https://hyperliquid.gitbook.io/hyperliquid-docs/trading/fees"
pdf: "none"
access: "full-text"
source_type: "documentation"
evidence_grade: "B"
topic: "27-execution-risk-management"
asset_class: "crypto"
horizon: "n/a"
tags: "fees, maker-taker, hyperliquid, transaction-costs, break-even, fee-tiers"
---

## Key insight
Hyperliquid, an on-chain perpetuals venue used elsewhere in this repository as a signal source, charges an unstaked, entry-tier account 4.5 bp to take and 1.5 bp to make, with taker fees falling to 2.4 bp and maker fees to zero or a small rebate at high volume. Set beside Kalshi's schedule (topic 06), this shows that the fee a small bot pays is venue-specific by a factor of about three on the taker side, and that fee tier is path-dependent on the bot's own turnover.

## Method
Exchange fee documentation, read as fetched. Tiers are set by rolling 14-day volume, assessed at the end of each UTC day. Volume is perps volume plus twice spot volume; sub-accounts share the master account's tier. Staking the venue's token gives a further discount. Maker rebates at the top maker tiers are paid per trade.

## Data and sample
Fee schedule as published on the date fetched. No historical schedule was retrieved.

## Reported results
Perpetuals, base (unstaked) rates, taker / maker:

| Tier | 14-day weighted volume | Taker | Maker |
|---|---|---|---|
| 0 | none | 0.045% | 0.015% |
| 1 | > $5M | 0.040% | 0.012% |
| 2 | > $25M | 0.035% | 0.008% |
| 3 | > $100M | 0.030% | 0.004% |
| 4 | > $500M | 0.028% | 0.000% |
| 5 | > $2B | 0.026% | 0.000% |
| 6 | > $7B | 0.024% | 0.000% |

- Staking discounts from 5% (more than 10 tokens staked) to 40% (more than 500,000).
- Maker rebate tiers by share of 14-day maker volume: -0.001% above 0.5%, -0.002% above 1.5%, -0.003% above 3.0%.
- Referral discounts and separate terms for some market types (the page describes a "growth mode" for one class of markets that reduces fees by 90%) also apply.

## Signal construction
Not a signal; the fee input to a cost model. A backtest or learned execution policy should take `fee(side, is_maker, venue, tier(t))`, where `tier(t)` is computed from the strategy's own trailing volume in the simulation. Round-trip fee at tier 0: 9 bp taker-taker, 6 bp maker entry with taker exit, 3 bp maker-maker.

## Relevance to SOL perpetuals at minutes to hours
Three uses. First, as a benchmark for the reference instrument: Kalshi's entry-tier retail schedule read in topic 06 is 12 bp taker and 2 bp maker, so a taker round trip costs 24 bp in fees there against 9 bp here, while maker costs are similar (4 bp against 3 bp). Passive execution matters far more on Kalshi than this venue's fee table would suggest. Second, for cross-venue comparisons of published strategy results: a strategy reported as profitable net of 4.5 bp taker fees has not been shown profitable at 12 bp. Third, for sanity-checking published academic assumptions: the Albers et al. experiment assumes Binance's best tier (1.5 bp taker, -0.5 bp maker), which neither this schedule nor Kalshi's offers to a small account.

## Caveats
Documentation can change without notice; this is a snapshot and the schedule in force for any backtest period must be dated. Whether a US-based account may trade on this venue was not checked; it is used here only as a cost benchmark and a signal source. Fees are only one component of cost: spread, impact, funding and, for passive orders, adverse selection are separate. Token staking discounts carry price risk in the staked token. The round-trip figures are my arithmetic from the table.
