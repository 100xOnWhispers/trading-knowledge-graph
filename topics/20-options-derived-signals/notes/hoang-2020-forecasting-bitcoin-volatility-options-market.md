---
title: "Forecasting bitcoin volatility: Evidence from the options market"
authors: "Hoang, Lai T.; Baur, Dirk G."
year: 2020
venue: "Journal of Futures Markets 40(10), 1584-1602"
url: "https://ideas.repec.org/a/wly/jfutmk/v40y2020i10p1584-1602.html"
pdf: "none"
access: "abstract-only"
source_type: "peer-reviewed"
evidence_grade: "B"
topic: "20-options-derived-signals"
asset_class: "crypto"
horizon: "multi-day"
tags: "implied-volatility, volatility-forecasting, deribit, har, forecast-combination, information-content"
---

## Key insight
Bitcoin option-implied volatility is a worse forecast of next-day volatility than simple time-series models, a better forecast at 7 to 15 days, and a useful addition at every horizon when combined with a model forecast. The options market therefore holds information that the price history does not, but the edge is at horizons longer than the ones this repository trades.

## Method
From the abstract: implied volatility is computed from Deribit bitcoin option trades and compared with ARMA and Heterogeneous Auto-Regressive (HAR) forecasts of bitcoin volatility at several horizons; forecast combinations are then evaluated. The realized-volatility measure, the implied-volatility construction (at-the-money, model-free or other), the loss functions and the tests used were not read.

## Data and sample
"A large number of bitcoin (BTC) options traded on the options exchange Deribit." Period and frequency are not stated in the abstract.

## Reported results
Abstract only:
- Implied volatility "is less accurate than AutoRegressive-Moving-Average or Heterogeneous Auto-Regressive model forecasts in predicting short-term BTC volatility (1 day ahead)".
- It is "superior in predicting long-term volatility (7, 10, 15 days ahead)".
- "A combination of IV and model-based forecasts provides the highest accuracy for all forecasting horizons revealing that the BTC options market contains unique information."

No error statistics are given in the abstract.

## Signal construction
For a volatility feature that uses options: regress future realized variance over horizon h on (a) the HAR terms from topic 14 and (b) implied variance for a maturity near h. For h of a day or less the abstract implies that the weight on implied volatility will be small, so the short-dated Deribit expiries (daily and weekly) are the ones to test, not the 30-day index. Update the implied leg every minute from mark implied volatility; re-estimate weights on a rolling window.

## Relevance to SOL perpetuals at minutes to hours
The one-day result is the relevant one, and it is negative for implied volatility used alone. What remains worth testing is whether the change in short-dated BTC or ETH implied volatility over the last hour adds to a SOL realized-volatility model, since the paper's combination result says the two sources are not redundant. Realized-volatility modelling itself belongs to topic 14.

## Caveats
Abstract-only note. The sample predates one-day and two-day Deribit expiries becoming a large share of volume, so the weak one-day result may not hold for an implied volatility taken from a matching one-day option. Bitcoin only. Implied volatility includes a variance risk premium, which biases it upward as a forecast unless the regression has an intercept and slope ([almeida-2024-risk-premia-bitcoin-market](almeida-2024-risk-premia-bitcoin-market.md)).
