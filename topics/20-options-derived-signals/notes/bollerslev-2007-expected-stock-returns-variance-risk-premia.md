---
title: "Expected Stock Returns and Variance Risk Premia"
authors: "Bollerslev, Tim; Zhou, Hao"
year: 2007
venue: "Finance and Economics Discussion Series 2007-11, Federal Reserve Board (published with George Tauchen in the Review of Financial Studies, 2009)"
url: "https://www.federalreserve.gov/pubs/feds/2007/200711/200711pap.pdf"
pdf: "sources/20-options-derived-signals/bollerslev-2007-expected-stock-returns-variance-risk-premia.pdf"
access: "full-text"
source_type: "working-paper"
evidence_grade: "A"
topic: "20-options-derived-signals"
asset_class: "equities"
horizon: "multi-day"
tags: "variance-risk-premium, implied-variance, realized-variance, return-predictability, vix, risk-aversion"
---

## Key insight
The gap between option-implied variance and realized variance predicts the US equity market's return a quarter ahead: a high premium is followed by high returns. It is the reference result for using the variance risk premium as a directional signal, and its horizon is a quarter, not hours. The authors read the premium as a proxy for time-varying risk aversion.

## Method
Variance risk premium = model-free implied variance (risk-neutral expectation of future variance, computed from option prices without a pricing model) minus realized variance computed from high-frequency intraday returns. Predictive regressions of quarterly excess market returns on the premium, alone and with standard predictors (P/E ratio, dividend yield, default spread, term spread, risk-free rate, consumption-wealth ratio). Robustness checks replace the model-free implied variance with Black-Scholes implied variance and the intraday realized variance with one built from daily returns.

## Data and sample
US aggregate stock market, 1990 to 2005, quarterly return horizon. The exact intraday sampling interval and the index data source were not confirmed in the pages read.

## Reported results
- The premium explains more than 15% of the variation in quarterly excess returns, more than any of the standard predictors.
- Adding the P/E ratio raises the R-squared above 25% (the abstract says more than twenty-five percent, the introduction more than twenty-six).
- The result "depend[s] crucially" on model-free implied variance and on realized variance from intraday data; with Black-Scholes implied variance or daily-return realized variance the conclusions weaken.
- Cross-sectional tests give little support for the premium as a priced risk factor in the linear sense.

## Signal construction
`VRP_t = IV_t^2 - RV_t^2`, both for a 30-day window in annualised variance units: implied leg from a VIX-style index (for bitcoin, [deribit-2021-dvol-implied-volatility-index](deribit-2021-dvol-implied-volatility-index.md)), realized leg as the sum of squared 5-minute returns over the trailing 30 days. Update daily. In the equity setting the feature is a slow tilt toward long exposure when the premium is high.

## Relevance to SOL perpetuals at minutes to hours
Little transfers directly. The horizon is two orders of magnitude longer than the bot's, and the one crypto study that looks at the relation finds the opposite sign across regimes ([almeida-2024-risk-premia-bitcoin-market](almeida-2024-risk-premia-bitcoin-market.md)). What is worth keeping is the measurement lesson: the predictive content came only with a model-free implied variance and an intraday realized variance, so a crypto premium built from at-the-money implied volatility and daily closes is a different and noisier object. If tested on BTC or SOL, treat it as a multi-day regime variable and expect either sign.

## Caveats
Sixteen years of quarterly returns is about 64 observations; return-predictability results of this kind are sensitive to sample period, and the sample ends before 2008. The working-paper version (two authors, December 2006 draft) was read, not the published article. The realized leg is backward-looking, so the "premium" mixes a true risk premium with a volatility forecast error. No trading costs or implementation test.
