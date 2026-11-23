---
title: "Price Discovery in Cryptocurrency Markets"
authors: "Plazuelo Pascual, Juan; Tardon Rubio, Carlos; Toro Cebada, Juan; Hernando Veciana, Angel"
year: 2025
venue: "arXiv preprint 2506.08718"
url: "https://arxiv.org/pdf/2506.08718"
pdf: "sources/05-price-discovery-cross-venue/plazuelo-2025-price-discovery-cryptocurrency-markets.pdf"
access: "full-text"
source_type: "working-paper"
evidence_grade: "C"
topic: "05-price-discovery-cross-venue"
asset_class: "crypto"
horizon: "seconds"
tags: "cex-vs-dex, uniswap, binance, cme-futures, information-share, gonzalo-granger, hayashi-yoshida, gas-fees, arbitrage"
---

## Key insight
Applying three standard tools side by side (Hasbrouck information share, Gonzalo-Granger permanent-transitory decomposition, Hayashi-Yoshida lead-lag), the authors find that the centralized exchange (Binance) leads an on-chain AMM (Uniswap v2) for ETH on essentially every date studied, while for BTC the CME futures lead Binance spot more often than not but far less decisively, and not on a high-volatility day. On-chain arbitrage that would close CEX-DEX gaps is frequently unprofitable after gas.

## Method
A 92-page report from a project on decentralized oracles. Chapter 2 sets out cointegration and VECM estimation, Hasbrouck's information share, the Gonzalo-Granger common-factor weights, Granger causality, and the Hayashi-Yoshida cross-correlation with its lead-lag ratio (LLR, the ratio of squared cross-correlations at positive versus negative lags; above 1 means the first series leads). Chapter 3 applies them to a one-year span and to five event days in 2024 (March 5, April 30, May 20, August 5, September 6), and prices a simple CEX-DEX arbitrage net of gas fees. I read the executive summary, methodology outline, conclusions and summary table, not every chapter.

## Data and sample
ETH: Binance at one-second intervals versus Uniswap v2 pool transactions from Etherscan; a long span of September 2023 to September 2024 plus the five event days. BTC: Binance spot versus CME bitcoin futures on the same five days.

## Reported results
Summary table (Table 3.36), by event day March / April / May / August / September:
- Centralized (Binance) Hasbrouck share versus Uniswap v2: 0.959, 0.965, 0.628, 0.986, 0.995; centralized leads on all five.
- Gonzalo-Granger for CEX versus DEX: centralized leads on four days, "neither" in August.
- Hayashi-Yoshida LLR for CEX versus DEX: 1.86, 1.47, 1.22, 1.20, 1.11; centralized leads on all five.
- CME futures Hasbrouck share versus Binance spot: 0.563, 0.552, 0.521, 0.158, 0.539; futures lead on four days, not on August 5, 2024.
- Gonzalo-Granger for futures versus spot: "neither" on four days, spot in August.
- Hayashi-Yoshida for futures versus spot: LLR 1.11, 1.15, 1.36, 0.97, 1.94 with lags of 0.055, 0.066, 0.063, -0.571, 0.15 seconds.
- Arbitrage example (March 5, 2024): mean loss about $45.30 per attempt after gas, before slippage.

## Signal construction
Not a signal. It is a worked template for running IS, GG and HY together on the same pair and reporting where they disagree. For the bot: treat on-chain AMM prices (for SOL, pools on Solana DEXs) as followers of Binance unless current data show otherwise, and do not use AMM spot as a leading input by default.

## Relevance to SOL perpetuals at minutes to hours
Two points transfer. First, CEX leads AMM, so on-chain SOL spot prices are unlikely to lead Binance perps; on-chain data are more useful as flow and positioning information than as a price lead. Second, the August 5, 2024 result (spot leads, futures share 0.158, on a crash day) echoes Shen et al.: leadership flips under stress. What does not transfer: Uniswap v2 on Ethereum, with 12-second blocks and high gas, is a poor proxy for Solana DEXs with sub-second blocks and negligible fees, where the result could differ.

## Caveats
Not peer reviewed; five hand-picked event days; in-sample; CME trades limited hours. Uniswap v2 was no longer the main ETH pool by 2024, as the authors note. The three metrics disagree on BTC (GG says "neither"), which the authors read as weak futures leadership.
