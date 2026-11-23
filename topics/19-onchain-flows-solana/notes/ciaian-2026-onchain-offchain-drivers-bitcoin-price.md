---
title: "On- and off-chain demand and supply drivers of Bitcoin price"
authors: "Ciaian, Pavel; Kancs, d'Artis; Rajcaniova, Miroslava"
year: 2026
venue: "arXiv preprint arXiv:2602.08429"
url: "https://arxiv.org/pdf/2602.08429"
pdf: "sources/19-onchain-flows-solana/ciaian-2026-onchain-offchain-drivers-bitcoin-price.pdf"
access: "full-text"
source_type: "working-paper"
evidence_grade: "C"
topic: "19-onchain-flows-solana"
asset_class: "crypto"
horizon: "daily"
tags: "exchange-netflow, exchange-reserve, whale-netflow, fund-volume, ardl, cryptoquant, bitcoin"
---

## Key insight
In daily data, the flow variables that practitioners watch (exchange netflow, exchange reserve, whale netflow, custodian and fund flows) are related to the Bitcoin price mainly in the short run and mainly contemporaneously or with one-day lags. Demand-side measures (custodian inflows, fund volume, on-chain transaction activity) matter in both the short and long run; supply-side exchange measures matter only in the short run and fade after one lag.

## Method
Autoregressive distributed lag (ARDL) bounds-testing models of the Bitcoin price with an error-correction form, giving long-run coefficients and short-run multipliers. Nine model variants (M1 to M9) combine different sets of regressors. Two hypotheses: off-chain drivers affect price (H1), and whale trading affects price (H2). Controls include the federal funds rate, the Wilshire 5000 and gold.

Variables, all from CryptoQuant:
- Off-chain demand: Bank netflow and Bank reserve ("digital asset banks", meaning custodial institutions), Fund volume (trusts, ETFs, mutual funds).
- Off-chain supply: Exchange netflow and Exchange reserve, all exchanges.
- Whale proxies: Bank whale netflow and Exchange whale netflow, each defined as top-10 inflow transactions minus top-10 outflow transactions.
- On-chain: on-chain BTC transactions, coin days destroyed, total supply.

## Data and sample
Daily, 4 December 2019 to 25 January 2024. Bitcoin only.

## Reported results
- Long run: Bank netflow and Bank reserve are positive and significant in all models that include them except one. On-chain BTC transactions are positive and significant in most models. Exchange netflow and Exchange reserve are largely insignificant.
- Short run: all off-chain drivers are significant in selected models. Demand drivers are significant up to the third lag; supply drivers (exchange netflow and reserve) only up to the first lag. For on-chain activity only the contemporaneous coefficient is significant.
- Whales: Bank whale netflow is positive and Exchange whale netflow negative, as expected, but significant in the long run in only one or two models. Short-run whale effects are more common. The authors call the long-run whale evidence weak.
- Context figure: off-chain volume is roughly five times on-chain volume over the last two sample years.
Coefficient magnitudes were not extracted from the tables.

## Signal construction
- Inputs: daily (or hourly, where the vendor offers it) exchange netflow, exchange whale netflow (top-10 transactions), custodian netflow and fund volume.
- Features: z-scored changes in each; expected signs are negative for exchange netflow and exchange whale netflow, positive for custodian netflow.
- The paper supports use as a same-day state variable, not as a multi-day predictor: supply-side effects are gone after one daily lag.

## Relevance to SOL perpetuals at minutes to hours
Mostly indirect. The useful result is the decay profile: exchange-flow information is absorbed within about a day, which is consistent with the intraday effects in [chi-2024](chi-2024-return-volatility-forecasting-onchain-flows.md) and argues for hourly or finer flow features. The whale definition (top-10 transactions per day) is crude but easy to replicate for SOL. Bitcoin flow variables may still matter for SOL through market beta.

## Caveats
In-sample time-series regressions with many specifications and no out-of-sample or trading test. Significant contemporaneous coefficients do not establish direction: price moves cause deposits as well as the reverse. The "bank" and "fund" categories are vendor constructs. The sample ends two weeks after US spot ETF launch, so it says nothing about the ETF era. Not peer-reviewed.
