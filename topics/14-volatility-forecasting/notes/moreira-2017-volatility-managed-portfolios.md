---
title: "Volatility-Managed Portfolios"
authors: "Moreira, Alan; Muir, Tyler"
year: 2017
venue: "Journal of Finance 72, 1611-1644 (read as NBER Working Paper 22208, April 2016, revised June 2016)"
url: "https://www.nber.org/system/files/working_papers/w22208/w22208.pdf"
pdf: "sources/14-volatility-forecasting/moreira-2017-volatility-managed-portfolios.pdf"
access: "full-text"
source_type: "peer-reviewed"
evidence_grade: "A"
topic: "14-volatility-forecasting"
asset_class: "equities"
horizon: "multi-day"
tags: "volatility-timing, volatility-managed, inverse-variance, sharpe-ratio, position-sizing, factors"
---

## Key insight
Scaling exposure by the inverse of last month's realized variance raises Sharpe ratios and produces positive alpha relative to the unscaled portfolio, across the equity market, several equity factors and the currency carry trade. The reason is that volatility is highly forecastable while expected returns do not rise in proportion to it, so the reward per unit of risk is worse when volatility is high. Cutting exposure in high-volatility periods gives up little return and removes a lot of risk.

## Method
The managed return is

f_sigma(t+1) = (c / RV_t^2) * f(t+1),

where RV_t^2 is the realized variance of daily returns in the previous month (22 trading days) and c is a constant that sets the managed portfolio's unconditional volatility equal to the original's (c does not affect the Sharpe ratio). The test is a time-series regression of the managed factor on the original factor; a positive intercept means volatility timing expands the mean-variance frontier. The paper also computes utility gains for a mean-variance investor, checks subsamples and business-cycle behaviour, and examines transaction costs and leverage limits.

## Data and sample
Monthly rebalancing with daily data for realized variance. US market, size, value, momentum, profitability, return-on-equity and investment factors, and the currency carry trade. The market sample runs 1926 to 2015.

## Reported results
- The volatility-managed market portfolio has an annualized alpha of 4.86%, an appraisal ratio of about 0.33 to 0.34, and about a 25% increase in Sharpe ratio over buy-and-hold.
- Appraisal ratios for managed mean-variance-efficient combinations range from 0.33 to 0.91.
- A mean-variance investor restricted to the market gains about 65% in lifetime utility from volatility timing, compared with about 35% from timing expected returns in a cited benchmark.
- The authors state the results survive realistic transaction costs and hard leverage constraints. With weights capped at 1 (no leverage) or 1.5, Sharpe ratios do not change; alphas are lower because average risk weights are lower, but remain statistically significant.
- The strategy takes less risk in recessions and crises yet earns high average returns.

## Signal construction
A sizing rule, not a directional signal: position weight w_t = c / sigma2_hat_t, with sigma2_hat_t a trailing realized variance. Many practitioners use inverse volatility (c / sigma_hat) instead, which is less aggressive. For an intraday bot the analogue is to scale each trade's notional by target risk divided by forecast volatility over the intended holding period, capped by the venue's maximum leverage.

## Relevance to SOL perpetuals at minutes to hours
The mechanism (persistent volatility, expected return not proportional to it) is the right question to ask of any SOL signal: does the signal's edge per trade grow with volatility? For directional signals such as momentum or order-flow, expected profit per trade may scale with volatility, in which case inverse-variance scaling would be too aggressive and inverse-volatility or constant-risk sizing is the better default. This paper is monthly and for long-only factor premia; nothing in it tests minutes-to-hours trading.

## Caveats
The constant c uses the full sample. The Cederburg note shows that across 103 equity strategies the managed versions do not systematically beat the originals in real-time tests, and that the alphas here are not attainable by an investor who must estimate the combination weights. Low leverage caps (as on Kalshi) truncate the up-scaling in calm periods, which is where much of the extra return comes from.
