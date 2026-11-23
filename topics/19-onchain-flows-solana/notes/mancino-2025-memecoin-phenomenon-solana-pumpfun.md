---
title: "The Memecoin Phenomenon: An In-Depth Study of Solana's Blockchain Trends"
authors: "Mancino, Davide"
year: 2025
venue: "arXiv preprint arXiv:2512.11850"
url: "https://arxiv.org/pdf/2512.11850"
pdf: "sources/19-onchain-flows-solana/mancino-2025-memecoin-phenomenon-solana-pumpfun.pdf"
access: "full-text"
source_type: "working-paper"
evidence_grade: "C"
topic: "19-onchain-flows-solana"
asset_class: "crypto"
horizon: "n/a"
tags: "solana, memecoins, pump-fun, dex-activity, retail, token-launches, dune"
---

## Key insight
In the fourth quarter of 2024 a single retail launchpad, Pump.fun, accounted for up to 71.1 percent of all tokens minted on Solana and 40 to 67.4 percent of all DEX transactions, yet under 2 percent of its tokens ever reached a major DEX and its share of DEX volume in dollar terms rarely exceeded half. Solana's on-chain activity in that period was a retail memecoin phenomenon: very high transaction counts, small trade sizes, short token lives.

## Method
Descriptive on-chain analysis using SQL queries on Dune Analytics tables for Solana token transfers and DEX trades. Measures: daily tokens minted on Pump.fun versus other platforms; share of DEX transactions and of DEX volume involving Pump.fun-originated tokens across Raydium, Meteora, Orca, Lifinity, Phoenix and Pump.fun; daily "graduation" rate (tokens completing the bonding curve and moving to Raydium); daily unique signers on Pump.fun.

## Data and sample
Solana mainnet, 1 October to 31 December 2024, daily aggregates from Dune Analytics.

## Reported results
- Pump.fun accounted for up to 71.1 percent of tokens minted on Solana.
- Pump.fun-related tokens made up 40 to 67.4 percent of DEX transactions, but Pump.fun-related trading rarely exceeded 50 percent of DEX volume, which the author reads as a retail profile.
- Graduation to Raydium peaked below 2 percent of tokens created.
- Daily unique trading addresses rose from about 60,000 in early October to peaks of 260,000 in November and 224,000 in December.
- The paper does not analyse the SOL price.

## Signal construction
Not a signal. It identifies the activity series behind Solana's 2024 demand story, for testing:
- Inputs: tokens launched per hour on the main launchpads, bonding-curve completions per hour, unique launchpad signers, and launchpad trading volume in SOL.
- Hypothesis: because launchpad tokens are bought and sold against SOL and each trade pays fees and tips in SOL, bursts in launches and graduations add transactional demand for SOL; collapses in these series mark the end of a retail wave.
- These would be slow regime features (hourly to daily) and need deseasonalising by hour of day.

## Relevance to SOL perpetuals at minutes to hours
Context for a SOL-specific regime variable. It documents how concentrated Solana activity was in one application, which means a change in that application's fortunes shifts every on-chain activity metric at once. [blockworks-2026](blockworks-2026-solana-tokenholder-report-q2.md) shows the later unwind: by mid-2026 memecoins were about 17 percent of Solana DEX volume and network revenue had fallen sharply. Relationships between memecoin activity and SOL fitted on late 2024 would be fitted on the peak.

## Caveats
Three months at the height of a boom. Purely descriptive, with no statistical tests and no price analysis. Transaction-count shares are inflated by bots and failed attempts (see [zheng-2025](zheng-2025-failed-transactions-solana-blockchain.md)). Dune table coverage and labelling are not audited. A short conference-style paper, not peer-reviewed in the version read.
