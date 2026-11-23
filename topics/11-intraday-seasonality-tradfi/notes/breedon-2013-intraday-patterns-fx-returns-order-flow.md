---
title: "Intraday Patterns in FX Returns and Order Flow"
authors: "Breedon, Francis; Ranaldo, Angelo"
year: 2013
venue: "Journal of Money, Credit and Banking (2013); Queen Mary University of London Working Paper 694, April 2012, read"
url: "https://www.qmul.ac.uk/sef/media/econ/research/workingpapers/2012/items/wp694.pdf"
pdf: "sources/11-intraday-seasonality-tradfi/breedon-2013-intraday-patterns-fx-returns-order-flow.pdf"
access: "full-text"
source_type: "peer-reviewed"
evidence_grade: "A"
topic: "11-intraday-seasonality-tradfi"
asset_class: "fx"
horizon: "hours"
tags: "fx, time-of-day, order-flow, local-trading-hours, session-effects, transaction-costs"
---

## Key insight
Currencies tend to depreciate during their own region's trading hours and appreciate outside them. The pattern is mirrored in order flow: market participants are net buyers of foreign currency during their own working day. Because this flow is predictable and carries no private information, the return pattern is evidence that uninformed, scheduled order flow moves prices. After bid-ask costs it was tradable only in the most liquid pair.

## Method
Hourly midquote returns and signed trade counts by hour and by trading session (sessions defined from futures trading hours, in New York time). Three tests: difference in means; an autoregressive model with hourly dummies and GARCH errors; and a sign test. A trading rule goes short the base currency in its own hours and long in the counter-currency's hours, evaluated at firm bid and ask prices. Order-flow regressions and a single market maker's customer-level data are used to corroborate the mechanism.

## Data and sample
EBS transaction data, January 1997 to early June 2007, aggregated to hourly: EUR/USD, USD/JPY, EUR/JPY, GBP/USD, USD/CHF, AUD/USD. The authors estimate that EBS covers roughly half of turnover in EUR/USD, USD/JPY, EUR/JPY and USD/CHF and under 5% in GBP/USD and AUD/USD. A 2013 journal version with the same title is listed on RePEc; the journal name, volume and pages were not re-confirmed in this session.

## Reported results
- Session-return differences are highly significant across pairs; after adjusting for autocorrelation and heteroskedasticity they remain significant at the 1% level in all cases except USD/JPY.
- Net of transaction costs most time-of-day strategies are not profitable. EUR/USD is the exception, with Sharpe ratios of 1.3 for the "morning short" and 0.9 for the "afternoon long" leg.
- Order flow shows the matching pattern. Banks and investment funds have the strongest tendency to sell their own currency in local hours; corporates do not show it.
- Earlier studies cited (Cornett et al. 1995 on futures from 1977 to 1991; Ranaldo 2009 on spot from 1993 to 2005) find the same sign.

## Signal construction
Define regional sessions. For a pair A/B, expected drift is negative for A during A's local hours and positive during B's. Implementation: hourly dummy means estimated on a rolling window, traded only when the session mean exceeds the round-trip cost. A flow-based version: cumulative signed trade count by session as a confirming input.

## Relevance to SOL perpetuals at minutes to hours
The transferable question is whether regional participants are systematic net buyers or sellers of crypto against dollars in their own hours (for example, Asian retail accumulation versus US institutional distribution, or the reverse). Session-level signed flow from large venues answers this directly. In FX the "home currency" logic gives a prior for the sign; for SOL there is no such prior, so the sign must be learned and may flip between regimes.

## Caveats
Sample ends in 2007, before the growth of non-bank market makers; the authors could not study the crisis. Profitability after costs existed in one pair only. Hourly aggregation; the working-paper version was read. Session definitions are a free parameter.
