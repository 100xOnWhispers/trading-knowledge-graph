---
title: "One year of bitcoin spot ETPs: A brief market and fund flow analysis"
authors: "Oefele, Nico"
year: 2025
venue: "Economics Letters, 250"
url: "https://ideas.repec.org/a/eee/ecolet/v250y2025ics0165176525001417.html"
pdf: "none"
access: "abstract-only"
source_type: "peer-reviewed"
evidence_grade: "B"
topic: "19-onchain-flows-solana"
asset_class: "crypto"
horizon: "daily"
tags: "spot-etf, etf-flows, return-chasing, reverse-causality, bitcoin"
---

## Key insight
In the first year of US spot Bitcoin exchange-traded products, daily net fund flows were driven mainly by same-day Bitcoin price changes. Investors in these products chase price. This reverses the popular reading in which ETF inflows are an exogenous demand shock that pushes price.

## Method
Only the abstract was read (the article is behind the ScienceDirect paywall and no working-paper version was found). The abstract describes a market-structure summary and a regression of daily net fund flows on Bitcoin price changes and other factors. The specification, controls and lag structure were not confirmed.

## Data and sample
US Bitcoin spot ETPs from their launch in January 2024, about one year. Daily frequency. Data source not confirmed.

## Reported results
From the abstract only:
- The market grew quickly and is concentrated: more than half of assets under management sit in one product.
- Average weekly net fund flows were 1.4 percent.
- Daily Bitcoin price changes are the primary driver of daily net fund flows. A 3.4 percent change in the Bitcoin price is associated with a 0.2 percent net fund flow, other things equal.
- The author concludes that investors in these products base decisions mainly on Bitcoin price movements.

## Signal construction
Not a signal. It is a warning about how to use ETF flow data:
- A large reported inflow on day t is, to a first approximation, a restatement of the return on day t.
- Any test of "flows predict returns" must control for the same-day and lagged return, otherwise it rediscovers momentum.
- The implied residual, `flow(t) - b * return(t)`, is the only part of the flow that could carry new information. The abstract gives the slope: about 0.06 percent of assets per 1 percent price change.

## Relevance to SOL perpetuals at minutes to hours
Useful as a prior. SOL spot ETP flows are reported daily and are small (see [blockworks-2026](blockworks-2026-solana-tokenholder-report-q2.md)), so their information for a minutes-to-hours bot is likely limited to the hour or so after publication, and even then the flow is largely explained by the prior day's return. A SOL test should regress the next-session SOL return on the flow surprise (flow minus the part explained by returns) and check whether anything is left.

## Caveats
Abstract-only. One year of data in a single, strongly trending regime. Daily frequency cannot separate "price moves, then investors buy the fund" from "authorised participants hedge creations intraday, which moves price"; both produce a same-day correlation. The result is for Bitcoin and may not carry over to SOL products, which have a different investor base and include staking variants.
