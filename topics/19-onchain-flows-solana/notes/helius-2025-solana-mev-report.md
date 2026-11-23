---
title: "Solana MEV Report: Trends, Insights, and Challenges"
authors: "Helius (author not stated)"
year: 2025
venue: "Helius blog"
url: "https://www.helius.dev/blog/solana-mev-report"
pdf: "none"
access: "full-text"
source_type: "industry-research"
evidence_grade: "C"
topic: "19-onchain-flows-solana"
asset_class: "crypto"
horizon: "n/a"
tags: "solana, mev, jito, tips, sandwich, arbitrage, validators, activity-proxy"
---

## Key insight
Jito tips are a real-time, on-chain measure of how much traders are paying for fast inclusion on Solana, and they swing by almost two orders of magnitude with speculative activity. Over about a year, tips totalled 3.75 million SOL across more than 3 billion bundles, with daily tips ranging from 781 SOL to 60,801 SOL. Atomic arbitrage on Solana is high-count and low-margin, while sandwiching was concentrated in one program operating a private mempool.

## Method
Descriptive statistics assembled from Jito's explorer and internal analysis, Dune Analytics dashboards, Blockworks Research and Flipside. Tips are measured as transfers to Jito's eight tip accounts. Arbitrage counts use Jito's detection algorithm. Sandwich figures cover one program (called Vpe) over a 30-day window. The publication date is not stated; the latest data point is 5 January 2025.

## Data and sample
Solana mainnet, roughly calendar 2024 for tips, bundles and arbitrage; 7 December 2024 to 5 January 2025 for the sandwich program.

## Reported results
- Jito tips: 3.75 million SOL in total. Daily low 781 SOL (11 January), high 60,801 SOL (19 November), a third-quarter low of 1,661 SOL (7 September).
- Bundles: more than 3 billion; peak of 24.4 million in one day (21 December 2024). Daily tippers rose from about 20,000 at the start of 2024 to nearly 938,000 (10 December).
- Validator adoption of the Jito client: 48 percent of stake in January 2024 (189.5 million SOL), 92 percent at the start of 2025 (373.8 million SOL).
- Arbitrage: 90,445,905 successful arbitrage transactions; average profit USD 1.58; largest single arbitrage USD 3.7 million; total USD 142.8 million, of which 88.7 percent was denominated in SOL.
- Sandwiching by the Vpe program: 1.55 million sandwich transactions in 30 days, 88.9 percent successful; profit 65,880 SOL (USD 13.43 million); 22,760 SOL paid in tips; average profit 0.0425 SOL per sandwich. Jito's internal analysis attributes nearly half of all Solana sandwiches to this program.
- Reverted transactions peaked at 75.7 percent of non-vote transactions in April 2024.

## Signal construction
An activity and urgency gauge, to be tested, not a signal the report validates:
- Inputs: transfers to the Jito tip accounts and priority fees, aggregated per minute.
- Features: `tips_sol_1m` and `priority_fee_median_1m` as z-scores against the same hour of day over a trailing window; the ratio of mean to median fee as a hotspot indicator.
- Hypotheses to test: tip surges coincide with and may slightly lead realised volatility in SOL; sustained high tips mark memecoin-driven demand for SOL as the quote and fee asset.

## Relevance to SOL perpetuals at minutes to hours
Tips and priority fees update every slot and are specific to Solana, which makes them one of the few on-chain series fast enough for this horizon. The 88.7 percent SOL denomination of arbitrage profit and the tip flow itself show that on-chain trading activity translates into transactional demand for SOL, though the amounts are small next to SOL's exchange volume. The report shows levels and episodes only; lead-lag against SOL returns or volatility is untested.

## Caveats
Published by a Solana infrastructure company and reliant on Jito's own data and detection. No link to price is tested. The structure has since changed: Jito closed its public mempool in March 2024, stake pools delisted sandwiching validators through 2025, and [heimbach-2026](heimbach-2026-protected-order-flow-sandwich-attacks.md) shows attacks shifting to cross-block forms. Tip levels from 2024 reflect a memecoin boom that later unwound (see [blockworks-2026](blockworks-2026-solana-tokenholder-report-q2.md)).
