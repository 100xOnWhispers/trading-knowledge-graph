---
title: "The Intraday Bitcoin Response to Tether Minting and Burning Events: Asymmetry, Investor Sentiment, and 'Whale Alerts' on Twitter"
authors: "Saggu, Aman"
year: 2022
venue: "Finance Research Letters, 49, 103096 (accepted manuscript, arXiv:2501.05232)"
url: "https://arxiv.org/pdf/2501.05232"
pdf: "sources/19-onchain-flows-solana/saggu-2022-intraday-bitcoin-tether-minting-burning.pdf"
access: "full-text"
source_type: "peer-reviewed"
evidence_grade: "B"
topic: "19-onchain-flows-solana"
asset_class: "crypto"
horizon: "minutes"
tags: "stablecoin, tether, minting, burning, event-study, whale-alert, intraday, sentiment-conditioning"
---

## Key insight
With minute data, Bitcoin does respond to Tether supply changes, but only for about half an hour and only to mints. The response peaks at 30 minutes and is already fading at 60, which explains why studies using hourly or daily data found little. The effect is concentrated in mints that occur during positive sentiment and are broadcast by the Whale Alert account, so it looks like an attention and announcement effect more than a liquidity effect.

## Method
Event study. For every mint or burn, the Bitcoin log return is measured from one minute before the event to n minutes after, for n = 5, 10, 15, 30, 60 and 1,440. OLS with Newey-West errors, with MM-weighted least squares as a robustness check:
- Baseline: `r = a + b1 * dT + e`, where dT is the supply change in billions of USDT.
- Asymmetry: separate slopes for mints and burns.
- State dependence: slopes interacted with positive or negative sentiment, measured three ways (Crypto Fear and Greed Index, Sentix institutional survey, a Lunde-Timmermann bull/bear filter).
- Announcement: mint slopes split by whether Whale Alert tweeted the event.

## Data and sample
All Tether mints and burns on Omni, Ethereum, Tron, EOS, Liquid, SLP and Algorand, collected from block explorers, 6 October 2014 to 9 January 2021. Whale Alert tweeted 222 of 367 mints (60 percent) and 11 of 220 burns (5 percent). One-minute Bitcoin prices from bitcoincharts.com (Bitfinex until 22 December 2016, Bitstamp after). The accidental 5 billion Tron mint of July 2019 is excluded.

## Reported results
- Baseline: a 1 billion USDT supply change moves Bitcoin 0.24 percent in 5 minutes, 0.38 percent in 10, 0.51 percent in 15, 0.68 percent in 30, then 0.57 percent in 60. The 1,440-minute window is weak or insignificant.
- Mints are significant; burns are not, at any window.
- The mint response is significant in positive-sentiment states and larger than in negative-sentiment states under all three sentiment measures.
- Mints tweeted by Whale Alert during positive sentiment drive the result; mints that were not tweeted usually produce no response.

## Signal construction
- Inputs: a real-time feed of issuer mint transactions (Tether Treasury on Tron and Ethereum, Circle on Solana and Ethereum), the Whale Alert feed, and a slow sentiment or trend state.
- Feature: `mint_size_usd` at event time, zero otherwise, gated by `sentiment_state > 0` and optionally `announced == 1`.
- Expected sign: positive on the reference asset for 5 to 30 minutes, with reversal risk after 60.
- Update: event-driven; decay the feature to zero within one hour.

## Relevance to SOL perpetuals at minutes to hours
The horizon matches exactly. What needs re-testing: whether the effect survives after 2021 (mints are now frequent, often pre-announced as inventory replenishment, and widely monitored by bots), whether SOL responds with a beta to the Bitcoin move or independently, and whether USDC mints on Solana carry any SOL-specific information. The effect size is small against costs: 0.68 percent per billion is roughly 7 basis points for a 100 million mint.

## Caveats
In-sample event study with no transaction costs and no trading simulation. Overlapping events and concurrent news are not separated. Sample ends January 2021. A publicly known, bot-readable signal with a 30-minute life is a prime candidate for decay. The author states no prior association with Tether or Whale Alert, though Whale Alert later promoted the paper.
