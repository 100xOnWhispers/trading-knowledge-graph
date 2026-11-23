---
title: "Is Bitcoin Really Untethered?"
authors: "Griffin, John M.; Shams, Amin"
year: 2020
venue: "Journal of Finance, 75(4), 1913-1964"
url: "https://econpapers.repec.org/RePEc:bla:jfinan:v:75:y:2020:i:4:p:1913-1964"
pdf: "none"
access: "abstract-only"
source_type: "peer-reviewed"
evidence_grade: "B"
topic: "19-onchain-flows-solana"
asset_class: "crypto"
horizon: "n/a"
tags: "stablecoin, tether, issuance, flows, manipulation, bitcoin, on-chain"
---

## Key insight
The founding paper of the stablecoin-flow literature. Using blockchain data from the 2017 boom, it argues that Tether flowing out to exchanges was used to buy Bitcoin after price declines, and that these purchases were followed by sizable Bitcoin price increases. The authors read this as supply-driven: newly printed, possibly unbacked, stablecoin pushed prices up, as opposed to stablecoin being issued passively to meet demand from cash investors.

## Method
Only the abstract and bibliographic record were read in this session (the SSRN and Wiley full texts returned HTTP 403). According to the abstract, the authors use blockchain data to trace Tether flows and relate them to Bitcoin prices, attribute the flow to a single entity, and compare patterns around month-ends. The exact algorithms, regressions and the data frequency could not be confirmed from the abstract.

## Data and sample
Tether and Bitcoin blockchain data covering the 2017 boom (per the abstract). Venues, exact dates and frequency: not confirmed.

## Reported results
From the abstract only:
- Purchases with Tether are timed following market downturns and are associated with sizable increases in Bitcoin prices.
- The flow is attributable to one entity.
- Patterns around month-ends are interpreted as evidence of insufficient Tether reserves.
- The authors conclude the evidence is "most consistent with the supply-based hypothesis" of unbacked digital money inflating prices, not demand from cash investors.

No coefficients or effect sizes were read. Two other papers read in full in this session characterise the result: [saggu-2022](saggu-2022-intraday-bitcoin-tether-minting-burning.md) describes it as Bitcoin responding positively to Tether issuance only after negative price shocks, with months of larger issuance followed by negative Bitcoin returns; [lyons-2020](lyons-2020-what-keeps-stablecoins-stable.md) reports that aggregate issuance shows no systematic effect on Bitcoin and says its own result "does not discount the possibility" of the episode-specific manipulation Griffin and Shams describe. Those are secondary descriptions, not checked against the paper.

## Signal construction
The paper motivates a conditional flow signal, not a formula that could be taken from the abstract:
- Input: net stablecoin transfers from issuer treasury (or a flagged large account) to exchange deposit addresses, per hour.
- Condition: recent negative return on the reference asset.
- Hypothesised direction: positive subsequent return when large stablecoin inflows to exchanges follow a drop.
Thresholds, lags and normalisation would have to be fitted from scratch; none are confirmed here.

## Relevance to SOL perpetuals at minutes to hours
The transferable idea is that stablecoin arriving on exchanges after a sell-off is deployable buying power, and that the identity of the sender matters more than aggregate supply. For SOL the natural analogues are USDT and USDC mints on Solana and Tron, and stablecoin deposits to Binance, Bybit and OKX. Whether any of this holds for SOL, in 2026, at intraday horizons, is untested. The original mechanism (one dominant account on one exchange in 2017) no longer describes the market.

## Caveats
Abstract-only: the grade reflects what could be verified, not the journal. The sample is a single boom in a market that has since changed structure (many issuers, regulated reserves, ETF and CME access). The interpretation is contested: Tether's issuer disputed it publicly, and later work using aggregate issuance finds no systematic price effect. The search results for this paper note that Griffin disclosed ownership of a consulting firm doing cryptocurrency-related work.
