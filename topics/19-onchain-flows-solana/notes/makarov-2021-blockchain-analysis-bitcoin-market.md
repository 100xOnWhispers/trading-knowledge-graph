---
title: "Blockchain Analysis of the Bitcoin Market"
authors: "Makarov, Igor; Schoar, Antoinette"
year: 2021
venue: "NBER Working Paper 29396"
url: "https://www.nber.org/system/files/working_papers/w29396/w29396.pdf"
pdf: "sources/19-onchain-flows-solana/makarov-2021-blockchain-analysis-bitcoin-market.pdf"
access: "full-text"
source_type: "working-paper"
evidence_grade: "B"
topic: "19-onchain-flows-solana"
asset_class: "crypto"
horizon: "n/a"
tags: "on-chain-data, entity-clustering, spurious-volume, exchange-flows, ownership-concentration, miners, data-quality"
---

## Key insight
Raw on-chain volume is mostly noise. About 90 percent of Bitcoin transaction volume is not economically meaningful: it is change outputs, self-transfers and deliberate obfuscation. Of the real volume, about three quarters is linked to exchanges and exchange-like entities, and a large share of that is cross-exchange flow. Any flow signal built on unfiltered transfers, or on address counts without entity clustering, measures the wrong thing.

## Method
The authors combine public and proprietary sources (including Crystal Blockchain data) that link addresses to real entities, then build algorithms to (i) filter spurious volume and trace payments between real entities, (ii) rank exchanges by eigenvalue centrality in the network of cross-exchange flows, (iii) link individual miners to the 20 largest pools by tracing reward distributions, with a separate algorithm per pool, and (iv) separate addresses of intermediaries (exchange cold wallets, online wallets) from individual holders using graph analysis.

## Data and sample
The full Bitcoin blockchain with entity labels, with most statistics stated from 2015 to the end of 2020 and a miner case study from the April 2021 Xinjiang power shutdown.

## Reported results
Read from the introduction and abstract; the body sections were not read in full.
- 90 percent of transaction volume is not tied to economically meaningful activity.
- Since 2015, 75 percent of real volume is linked to exchanges or exchange-like entities (online wallets, OTC desks, large institutional traders). Illegal activity, scams and gambling together are under 3 percent.
- Exchanges are the most central nodes; exchanges trading similar currency pairs have higher flows between them, consistent with arbitrage keeping prices aligned.
- Flows from the Hydra darknet market go mainly to non-KYC exchanges, named as including Binance and Huobi, and reach KYC exchanges indirectly.
- Mining capacity: the top 10 percent of miners control 90 percent, and about 50 miners (0.1 percent) control close to 50 percent. Concentration is counter-cyclical to the Bitcoin price. Between 60 and 80 percent of capacity was in China from 2015 until April 2020.
- Holdings: intermediaries held 5.5 million BTC at the end of 2020, about one third of circulation; individuals held 8.5 million. The top 1,000 investors control about 3 million BTC and the top 10,000 about 5 million.

## Signal construction
Not a signal. It is a specification for the data layer under any flow signal:
- Cluster addresses into entities before measuring anything.
- Remove self-transfers, change and peel chains before computing volume.
- Treat exchange-to-exchange flow as arbitrage and inventory rebalancing, separate from wallet-to-exchange deposits.
- Prefer flow measures that are hard to fake (cross-exchange network position) over reported volume.

## Relevance to SOL perpetuals at minutes to hours
The lesson applies with more force on Solana. Account-based transfers are cheap, bots generate most transactions, and large SOL movements include stake delegation, liquid-staking mint and redeem, and program-owned accounts. A "SOL exchange inflow" series is only as good as the vendor's labels for exchange deposit accounts and its treatment of stake accounts. Before testing any SOL flow signal, check how the vendor defines an entity and how often labels are revised.

## Caveats
A measurement paper with no return predictability tests. Bitcoin only, and the sample predates spot ETFs, whose custodians are now among the largest holders. The entity labels rely partly on a commercial provider and cannot be fully reproduced.
