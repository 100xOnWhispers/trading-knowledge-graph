---
title: "Why Does My Transaction Fail? A First Look at Failed Transactions on the Solana Blockchain"
authors: "Zheng, Xiaoye; Wan, Zhiyuan; Lo, David; Xie, Difan; Yang, Xiaohu"
year: 2025
venue: "Proceedings of the ACM on Software Engineering, 2(ISSTA), Article ISSTA066 (arXiv:2504.18055)"
url: "https://arxiv.org/pdf/2504.18055"
pdf: "sources/19-onchain-flows-solana/zheng-2025-failed-transactions-solana-blockchain.pdf"
access: "full-text"
source_type: "peer-reviewed"
evidence_grade: "B"
topic: "19-onchain-flows-solana"
asset_class: "crypto"
horizon: "hours"
tags: "solana, congestion, failed-transactions, bots, dex, slippage, daily-cycle, measurement"
---

## Key insight
More than half of all non-vote transactions on Solana failed over a full year, and the failures are a by-product of bot trading, not random network faults. Bots fail 58.43 percent of the time, two error classes tied to price movement ("price or profit not met" and "invalid status") account for 67.18 percent of failures, and the hourly failure rate rises with activity and repeats on a 24-hour cycle. The failure rate is therefore a measurable, chain-native gauge of trading contention.

## Method
A large-scale empirical study. Accounts are classified as bot or human with a classifier built on transaction frequency and timing features, validated on 200 hand-labelled accounts. Macro-level analysis covers who initiates failed transactions, which programs trigger them, hourly volume and failure rate (including autocorrelation), block position and fees. Micro-level analysis codes error messages from transaction logs into ten error types by thematic analysis and maps them to programs and initiator types.

## Data and sample
2,898,175,006 non-vote transactions, of which 1,510,834,168 failed, across 72,123,900 blocks from 1 August 2023 to 31 July 2024. 12,712,516 accounts, of which 803,136 were classified as bots. An illustrative week, 6 to 13 March 2024, is shown at hourly resolution.

## Reported results
- Bot accounts fail on 58.43 percent of transactions; human accounts fail far less often.
- Hourly failure rate is strongly positively correlated with the hourly volume of failed transactions and shows significant autocorrelation, with a recurring pattern most prominent at 24 hours.
- Failed transactions sit later in blocks than successful ones (Wilcoxon rank-sum p below 0.001): they were outcompeted for position.
- Ten error types; "price or profit not met" and "invalid status" make up 67.18 percent of failures. DEX aggregators mostly hit the first, AMMs the second. Slippage errors from Jupiter Aggregator V6 are a named example.
- Failure rates dropped markedly after 16 June 2024, which the authors associate with a validator update introduced on 10 June 2024.
- Half of all programs were involved in fewer than 30 failed transactions; failures concentrate in a few trading programs.

## Signal construction
A contention gauge to be tested, not a validated signal:
- Inputs: per-slot counts of successful and failed non-vote transactions, error codes for the main DEX aggregator and AMM programs.
- Features: `fail_rate_5m`, and specifically the rate of slippage or price-not-met errors, deseasonalised by hour of day because of the 24-hour cycle.
- Interpretation: a jump in price-related failures means on-chain prices are moving faster than bots can land trades, which is a direct, chain-native reading of short-term volatility and one-sided pressure in SOL pairs.

## Relevance to SOL perpetuals at minutes to hours
Three uses. First, as a real-time congestion and volatility proxy available every 400 milliseconds without exchange data. Second, as a data-quality warning: more than half of the transactions in raw Solana data are failed attempts and must be excluded from any volume or flow measure. Third, the 24-hour cycle is another intraday seasonality to control for (see topic 10). The paper does not relate failure rates to SOL returns; that test is open.

## Caveats
The sample ends July 2024, before scheduler changes cut revert rates (the Helius fee-market article opened in this session puts the overall revert rate at 41.2 percent in December 2024, and [blockworks-2026](blockworks-2026-solana-tokenholder-report-q2.md) puts it at 27 percent in the second quarter of 2026), so the levels are regime-dependent. Bot classification is heuristic. A software-engineering study with no market-price analysis.
