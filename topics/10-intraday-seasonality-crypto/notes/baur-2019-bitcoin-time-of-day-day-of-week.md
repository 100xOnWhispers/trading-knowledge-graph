---
title: "Bitcoin time-of-day, day-of-week and month-of-year effects in returns and trading volume"
authors: "Baur, Dirk G.; Cahill, Daniel; Godfrey, Keith; Liu, Zhangxin (Frank)"
year: 2019
venue: "Finance Research Letters, 31, 78-92"
url: "https://ideas.repec.org/a/eee/finlet/v31y2019icp78-92.html"
pdf: "none"
access: "abstract-only"
source_type: "peer-reviewed"
evidence_grade: "B"
topic: "10-intraday-seasonality-crypto"
asset_class: "crypto"
horizon: "hours"
tags: "time-of-day, day-of-week, month-of-year, return-anomalies, volume, market-efficiency, null-result"
---

## Key insight
The standard reference for the sceptical view. Across seven exchanges and more than 15 million observations, calendar and clock effects in Bitcoin returns come and go and do not persist, so they are not a reliable source of profit. Trading activity is different: it is persistently lower in local evening hours and at weekends on every exchange.

## Method
Only the abstract and the repository record were read. The abstract describes an analysis of intraday time-of-day, day-of-week and month-of-year effects in returns and trading volume across exchanges. The estimator and test design were not confirmed.

## Data and sample
More than 15 million price and trading volume observations from seven continuously traded Bitcoin exchanges (abstract). The exact exchanges, currencies and sample dates were not confirmed in this session. The University of Western Australia repository lists a working-paper version dated 17 December 2017.

## Reported results
From the abstract of the published version:
- Time-specific anomalies in returns exist but do not persist over time.
- Trading activity differs persistently across all exchanges, with lower activity during local evening hours and on weekends.

From the 2017 working-paper abstract on the UWA repository:
- "Time-varying effects but no consistent or persistent patterns", and the conclusion that Bitcoin markets are efficient.

No coefficients, t-statistics or hourly figures were read.

## Signal construction
Not a signal. It is a prior: treat any hour-of-day or day-of-week return effect found in a backtest as unstable until it survives a rolling, out-of-sample test. The volume result supports using time-of-day and weekend indicators as features for expected liquidity and volatility, not for direction.

## Relevance to SOL perpetuals at minutes to hours
The asymmetry it documents (activity patterns persist, return patterns do not) is the main design lesson for a SOL perp bot: clock features belong in the volatility, volume and cost models first, and in the direction model only with strong shrinkage. The sample predates SOL, perpetuals at scale, and ETFs, so it says nothing direct about SOL.

## Caveats
Abstract-only: the full text sits behind the publisher paywall and the SSRN copy could not be fetched. Evidence grade reflects the publication venue and sample size as described, not a reading of the tests. Pre-2019 data. "Efficient" here means no persistent mean-return anomaly; it does not rule out conditional effects (for example hour-of-day returns conditional on volatility state).
