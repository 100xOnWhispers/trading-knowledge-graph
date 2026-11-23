---
title: "An Empirical Study of DeFi Liquidations: Incentives, Risks, and Instabilities"
authors: "Qin, Kaihua; Zhou, Liyi; Gamito, Pablo; Jovanovic, Philipp; Gervais, Arthur"
year: 2021
venue: "ACM Internet Measurement Conference (IMC '21)"
url: "https://arxiv.org/pdf/2106.06389"
pdf: "sources/04-open-interest-liquidations/qin-2021-empirical-study-defi-liquidations.pdf"
access: "full-text"
source_type: "peer-reviewed"
evidence_grade: "B"
topic: "04-open-interest-liquidations"
asset_class: "crypto"
horizon: "n/a"
tags: "defi, lending, liquidations, liquidation-sensitivity, bad-debt, on-chain"
---

## Key insight
On-chain lending protocols expose every position, so the amount of collateral that becomes liquidatable at any price can be computed exactly rather than estimated. The paper measures two years of liquidations on the four largest Ethereum lending platforms and introduces "liquidation sensitivity": the collateral that would be liquidated for a given percentage fall in a collateral asset. It also shows that fixed-spread liquidation designs sell more collateral than necessary, which favors liquidators over borrowers.

## Method
On-chain measurement of every liquidation event on Aave, Compound, MakerDAO and dYdX (the lending product), a systematization of liquidation mechanisms (auction versus fixed spread), and a snapshot-based stress calculation. For liquidation sensitivity, the authors take all open debt positions at a given block and, for each hypothetical price decline of a collateral asset from 0 to 100%, sum the collateral in positions whose health factor would fall below the liquidation threshold. Bad debt is classified as Type I (under-collateralized) and Type II (collateral too small relative to transaction fees to be worth closing).

## Data and sample
Ethereum mainnet, the full life of the four protocols up to about April 2021 (roughly two years). The platforms are described as over 85% of the Ethereum lending market, with USD 39.88 billion of total value locked at the time of writing.

## Reported results
- Cumulative liquidation proceeds of USD 807.46 million across 28,138 liquidation events and 2,011 unique liquidator addresses.
- 641 auction liquidations were unprofitable for liquidators.
- 73.97% of liquidations paid an above-average transaction fee, indicating competition among liquidators.
- 351 Type I and 3,525 Type II bad debt positions were identified; Aave V2 had accumulated up to USD 87.4 thousand of bad debt by the end of April 2021.
- A 43% ETH price decline, comparable to 13 March 2020, would make up to USD 1.07 billion of collateral liquidatable on MakerDAO at the snapshot block.
- Aave V2 was less sensitive than Compound despite similar size, because its users more often posted multi-asset collateral.

## Signal construction
The liquidation-sensitivity curve is a directly computable input: for each SOL-collateralized lending position on Solana protocols, compute the SOL price at which the health factor reaches the liquidation threshold, then aggregate collateral by price bucket to obtain liquidatable collateral as a function of price decline. Update on each block or every few minutes. This is a ground-truth "liquidation map" for the spot-collateral side of the market, to be combined with estimated perp liquidation levels.

## Relevance to SOL perpetuals at minutes to hours
The method transfers; the data do not. The paper covers Ethereum lending in 2019 to 2021, not Solana and not perps. Forced collateral sales from lending liquidations hit spot markets and can push perp prices through mark-price and index links, so a bot trading SOL perps has reason to track large on-chain SOL collateral clusters. Whether those clusters add predictive power at minutes to hours beyond price and order flow is untested here.

## Caveats
A snapshot stress test assumes an instantaneous price move and no borrower response; in practice borrowers top up or repay. Liquidations were found to be costly and event-driven, so proximity to a threshold is not a prediction that it will be reached. Protocol parameters, liquidator technology and chain congestion behavior have changed since 2021.
