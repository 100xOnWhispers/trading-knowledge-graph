---
title: "The Impact of Volatility Targeting"
authors: "Harvey, Campbell R.; Hoyle, Edward; Korgaonkar, Russell; Rattray, Sandy; Sargaison, Matthew; Van Hemert, Otto"
year: 2018
venue: "Journal of Portfolio Management 45(1), 14-33"
url: "https://people.duke.edu/~charvey/Research/Published_Papers/P135_The_impact_of.pdf"
pdf: "sources/14-volatility-forecasting/harvey-2018-impact-volatility-targeting.pdf"
access: "full-text"
source_type: "peer-reviewed"
evidence_grade: "A"
topic: "14-volatility-forecasting"
asset_class: "multi"
horizon: "daily"
tags: "volatility-targeting, vol-of-vol, tail-risk, leverage-effect, position-sizing, exponential-weighting"
---

## Key insight
Volatility targeting reliably does one thing across more than 60 assets: it stabilises realized risk and thins the left tail. It raises the Sharpe ratio only for "risk assets" (equities and credit), where falling prices coincide with rising volatility, so that scaling down in high volatility acts like a momentum overlay. For bonds, currencies and commodities the effect on Sharpe ratio is negligible. Volatility targeting is a risk-control tool first and a return enhancer only where a leverage effect exists.

## Method
Scaled return on day t:

r_scaled(t) = r(t) * sigma_target / sigma(t-2) * k,

where sigma(t-2) is a volatility estimate using returns up to two days earlier (so the position is known a full day ahead), the target is 10% annualized, and k (about 1) makes the ex-post volatility hit the target for comparability. Volatility is the standard deviation of daily returns with exponentially decaying weights (half-lives from 10 to 90 days, zero mean assumed); results are similar with rolling windows. For S&P 500 and 10-year Treasury futures, a variant uses realized variance from 5-minute returns. Statistics: Sharpe ratio, volatility of volatility, mean shortfall (left tail) and mean exceedance (right tail) at monthly evaluation frequency, gross and net of estimated costs.

## Data and sample
US equities daily from 1926 (reported 1927 to 2017), US bonds from 1963, credit, and 50 liquid futures and forwards (commodities, currencies, equity indices, bonds, rates). Intraday 5-minute data for S&P 500 and Treasury futures from 1988.

## Reported results
- US equities: Sharpe ratio rises from 0.40 unscaled to between 0.48 and 0.51 scaled, with little sensitivity to the half-life; gross and net figures are the same at reported precision.
- US equities: volatility of volatility falls from 4.6% unscaled to 1.8% scaled (20-day half-life); the left tail (mean shortfall) also improves.
- Sharpe improves in all equity subsamples except 1957 to 1987.
- Using 5-minute intraday data for the volatility estimate slightly improves Sharpe, vol of vol and left tail for S&P 500 futures.
- For bonds, currencies and commodities the Sharpe effect is negligible, but extreme returns and vol of vol are consistently reduced across all 60-plus assets.

## Signal construction
A sizing rule: notional = equity * sigma_target / sigma_hat, where sigma_hat is an exponentially weighted volatility (or an RV-based forecast) lagged so it uses only information available at order time, and the result is capped at maximum leverage. Parameters to choose: target, half-life, cap, and a no-trade band to limit resizing turnover.

## Relevance to SOL perpetuals at minutes to hours
This is the most defensible case for volatility-scaled sizing on SOL: expect steadier realized risk and smaller worst losses, not necessarily a higher Sharpe. Whether SOL has an equity-style leverage effect is doubtful; the Hansen note finds no significant asymmetry for BTC and ETH and the Tang note finds it inverted. If volatility rises after rallies instead, targeting will cut longs into strength, which has a different return consequence that needs measuring. The intraday-data result supports using RV-based estimates over daily-return estimates.

## Caveats
Daily data and multi-day holding periods; no crypto. Authors are affiliated with Man Group, which runs volatility-targeted products. The scaling constant k uses the full sample. Costs are estimates. With a low leverage cap, the target must be set low enough that the cap rarely binds, or the "targeting" is one-sided.
