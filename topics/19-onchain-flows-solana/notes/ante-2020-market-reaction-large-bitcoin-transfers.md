---
title: "Market Reaction to Large Transfers on the Bitcoin Blockchain - Do Size and Motive Matter?"
authors: "Ante, Lennart; Fiedler, Ingo"
year: 2020
venue: "Blockchain Research Lab Working Paper Series No. 9 (later published in Finance Research Letters 39, 2021)"
url: "https://www.blockchainresearchlab.org/wp-content/uploads/2020/03/Market-Reaction-to-Large-Transfers-on-the-Bitcoin-Blockchain-Do-Size-and-Motive-Matter-BRL-Working-Paper-9.pdf"
pdf: "sources/19-onchain-flows-solana/ante-2020-market-reaction-large-bitcoin-transfers.pdf"
access: "full-text"
source_type: "working-paper"
evidence_grade: "B"
topic: "19-onchain-flows-solana"
asset_class: "crypto"
horizon: "minutes"
tags: "whale-transfers, large-transactions, event-study, exchange-deposits, hot-wallet, cold-wallet, market-efficiency"
---

## Key insight
Large on-chain Bitcoin transfers do move price within minutes, but the effects are measured in hundredths of a percent, they do not grow with transfer size, and the sign by transfer type often contradicts the folklore. In particular, large deposits to exchange hot wallets, which are supposed to signal selling, were followed by price increases in this sample.

## Method
Minute-level event study with a mean-return model. Expected return is the average minute return over t = -141 to -21; abnormal returns are measured over t = -15 to +15 around the confirmation minute. Cumulative average abnormal returns (CAAR) are tested with t-statistics and Wilcoxon signed-rank z-statistics. Transfers are split into size quartiles and into five motive clusters using known exchange addresses: non-exchange transfers, cold wallet deposits, cold wallet withdrawals, hot wallet deposits and hot wallet withdrawals.

## Data and sample
2,132 transactions of at least 500 BTC from blockchain.com, September 2018 to November 2019, totalling 4.3 million BTC (USD 26.4 billion; mean USD 12.4 million). Minute close prices for BTC/USD on Gemini. Hot wallet withdrawals are 42.5 percent of events, hot wallet deposits 28.7 percent (Bitfinex and Binance), non-exchange transfers 20.4 percent, cold wallet withdrawals 6.1 percent, cold wallet deposits 2.4 percent.

## Reported results
- All transfers: average abnormal return of -0.0067 percent in the minute after confirmation (significant). CAAR for 0 to +15 minutes is +0.0264 percent (weakly significant); for -5 to +5 it is -0.0200 percent.
- No size effect: quartile results are not ordered by size.
- Non-exchange transfers: significant -0.0267 percent at t = 2; read as uncertainty.
- Cold wallet deposits: +0.0404 percent in the event minute but a CAAR of -0.3444 percent over the full 31-minute window (n = 51).
- Cold wallet withdrawals: CAAR of +0.0746 percent over the full window.
- Hot wallet deposits: positive effect, contrary to the selling-pressure expectation. The authors suggest deposited coins may be margin collateral.
- Hot wallet withdrawals: -0.0101 percent in the event minute.

## Signal construction
- Inputs: a mempool and block feed filtered for transfers above a size threshold, plus a label set for exchange hot and cold wallets.
- Feature: one categorical event flag per cluster, active for 15 minutes after confirmation.
- Do not scale by size, since the paper finds no monotonic size effect.
- The paper's effect sizes (under 0.1 percent in most windows) are below a taker round trip, so the realistic use is as a short-lived volatility or caution flag, not an entry trigger.

## Relevance to SOL perpetuals at minutes to hours
The design transfers; the estimates do not. Solana transfers confirm in under a second, so the pre-confirmation window studied here (mempool visibility for minutes) does not exist, and any reaction should be faster. Large SOL transfers are also dominated by staking, unstaking, liquid-staking and custody movements that have no Bitcoin analogue. A SOL version needs its own label set (exchange wallets, stake accounts, ETF custodians, treasury companies) before any event study is meaningful.

## Caveats
Fourteen months of data from 2018 to 2019 on one price venue. Many windows and clusters are tested with only weak significance, so multiple-testing risk is high. Small clusters (51 cold wallet deposits). Address labels are incomplete and concentrated in Bitfinex and Binance. No costs. Whale-transfer bots are far more widespread now than in 2019.
