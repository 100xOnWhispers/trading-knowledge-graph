---
title: "A Complete History of Solana Outages: Causes, Fixes, and Lessons Learnt"
authors: "Helius (author not stated)"
year: 2025
venue: "Helius blog"
url: "https://www.helius.dev/blog/solana-outages-complete-history"
pdf: "none"
access: "full-text"
source_type: "practitioner"
evidence_grade: "C"
topic: "19-onchain-flows-solana"
asset_class: "crypto"
horizon: "hours"
tags: "solana, outages, network-halt, congestion, client-bugs, event-risk, validator-restart"
---

## Key insight
Solana has had seven full network halts in about five years, totalling roughly 68 hours of downtime, each lasting between 4.5 and 19 hours. Five were client bugs and two were transaction floods from bots. The last one listed was in February 2024. For a trader this defines a rare, SOL-specific event class in which the chain stops while SOL derivatives on other venues keep trading.

## Method
A chronological engineering post-mortem compiled by a Solana infrastructure provider. For each incident it gives the date, downtime, root cause and fix. It is not a market study and contains no price analysis. The publication date is not stated on the page; the year in the front matter is not confirmed.

## Data and sample
Solana mainnet incidents from December 2020 to August 2024, drawn from public incident reports.

## Reported results
Halts, with stated downtime and cause:
- December 2020: about 6 hours. Block propagation bug in Turbine (two blocks for one slot).
- September 2021: 17 hours. Memory overflow from bot transaction flooding during the Grape Protocol IDO.
- April/May 2022: 8 hours. Bot spam during Candy Machine NFT mints exhausted validator memory.
- June 2022: 4.5 hours. Durable nonce bug causing consensus failure.
- September 2022: 8.5 hours. Fork-choice bug.
- February 2023: almost 19 hours. Deduplication failure in shred forwarding after an oversized block; manual restart.
- February 2024: almost 5 hours. Infinite recompile loop in the JIT cache.

Not counted as outages:
- January 2022: no downtime, but severe congestion; transaction success rates fell by as much as 70 percent.
- August 2024: no downtime; a coordinated patch for a vulnerability.

The article does not report SOL price reactions.

## Signal construction
An event flag, not a continuous signal:
- Inputs: slot height and time since last confirmed slot from two or more independent RPC providers; the Solana status page; validator restart announcements.
- Halt flag: no new confirmed slot for N seconds (N to be set well above normal jitter, for example 30 to 60 seconds) across all providers.
- Degradation flag: rising transaction failure rate and priority fees with slots still advancing (see [zheng-2025](zheng-2025-failed-transactions-solana-blockchain.md)).
- Response is a design decision the source does not test: at minimum, stop relying on Solana on-chain inputs (DEX prices, on-chain perp data, flow features) while the flag is set.

## Relevance to SOL perpetuals at minutes to hours
Directly relevant as tail-risk handling. During a halt, SOL cannot be deposited to or withdrawn from exchanges, so spot-perp and cross-venue arbitrage is impaired and basis can dislocate, while a cash-settled perp referenced to an index of exchange prices keeps trading (how Kalshi's contract behaves in a halt belongs to topic 06 and was not checked here). Whether a halt predicts a tradable price move is not established here. Press coverage found in a search during this session (a Blockworks news piece, not opened because the page returned HTTP 403) describes early halts as preceding 10 to 15 percent falls within twelve hours and later halts as having much smaller effects; that is secondary and unverified. With seven events, no statistical claim is possible.

## Caveats
Written by a company whose business depends on Solana. Seven events. No price data. The halt class may be obsolete: the list ends in February 2024, and a second validator client and later consensus upgrades change the failure modes. Degraded performance without a halt, which is more frequent and arguably more relevant to trading, is covered only anecdotally.
