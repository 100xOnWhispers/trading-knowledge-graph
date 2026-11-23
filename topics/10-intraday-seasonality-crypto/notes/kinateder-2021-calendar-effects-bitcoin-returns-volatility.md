---
title: "Calendar effects in Bitcoin returns and volatility"
authors: "Kinateder, Harald; Papavassiliou, Vassilios G."
year: 2021
venue: "Finance Research Letters, 38, 101420 (accepted version dated November 2019)"
url: "https://researchrepository.ucd.ie/server/api/core/bitstreams/3fe12e0f-f1c4-4226-937e-b7fc034dfcd9/content"
pdf: "sources/10-intraday-seasonality-crypto/kinateder-2021-calendar-effects-bitcoin-returns-volatility.pdf"
access: "full-text"
source_type: "peer-reviewed"
evidence_grade: "B"
topic: "10-intraday-seasonality-crypto"
asset_class: "crypto"
horizon: "daily"
tags: "day-of-week, weekend-volatility, month-of-year, halloween-effect, gjr-garch, null-result"
---

## Key insight
Once volatility clustering and fat tails are modelled properly, Bitcoin has no classical day-of-week effect in returns and no Halloween effect. The calendar shows up in risk instead: conditional volatility is significantly higher on Mondays and Tuesdays and significantly lower from Friday through Sunday. This contradicts the simpler Monday-return finding of Caporale and Plastun.

## Method
An AR(6)-GJR-GARCH(1,1) model with one calendar dummy at a time in both equations:

R_t = v + sum of rho_i R_(t-i) + lambda_1 D_t + e_t
h_t = omega + alpha e_(t-1)^2 + delta e_(t-1)^2 I(e_(t-1) < 0) + beta h_(t-1) + lambda_2 D_t

Dummies are estimated separately for each weekday and month (to avoid the dummy trap), with Bollerslev-Wooldridge quasi-maximum-likelihood standard errors because of high kurtosis. Ljung-Box tests check the specification.

## Data and sample
Daily Bitcoin closing prices in USD from CoinMarketCap, 28 April 2013 to 8 September 2019, 2,325 daily log returns, all seven days of the week.

## Reported results
- Mean daily return 0.19%; kurtosis 10.60.
- Mean equation: only Wednesday is (weakly, 10% level) significant, with a negative coefficient of -0.4441. Monday's coefficient is 0.3277 with p = 0.1521, not significant.
- Variance equation: volatility is significantly higher on Mondays and Tuesdays; significantly lower from Friday to Sunday (weak on Friday, stronger over the weekend).
- No Halloween effect in returns or variance.
- Month effects: weakly significant negative returns in January and March; markedly lower volatility in September, weaker reductions in April and July.
- The lagged variance coefficient exceeds 0.8; no significant asymmetric (leverage) response.
- The authors conclude that Bitcoin returns are mostly weak-form efficient and warn that the volatility effects may disappear once known.

## Signal construction
Not a directional signal. Use a weekday multiplier on forecast volatility: estimate lambda_2 for each weekday (or a seven-level seasonal factor on realised variance) on a rolling window, and scale position size and stop width by it. Expect higher risk Monday and Tuesday, lower Friday to Sunday.

## Relevance to SOL perpetuals at minutes to hours
The weekday volatility ordering matches intraday studies (Hansen, Petukhina, Wang et al.) and industry data on thin weekends (Kaiko, CME notes), so a weekday volatility factor is a safe feature for SOL. The exact ranking should be re-estimated: since 2024 US ETF flows concentrate activity on US weekdays, and SOL has its own event calendar.

## Caveats
Daily closes from an aggregator, Bitcoin only, sample ends 2019. One dummy per regression means the weekday effects are each measured against the pooled other days, not jointly. Weekend volatility is lower on average, but weekend liquidity is lower too, so price impact per unit traded can be higher; the paper does not address this.
