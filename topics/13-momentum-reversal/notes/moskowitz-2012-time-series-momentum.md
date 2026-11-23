---
title: "Time series momentum"
authors: "Moskowitz, Tobias J.; Ooi, Yao Hua; Pedersen, Lasse Heje"
year: 2012
venue: "Journal of Financial Economics 104(2), 228-250"
url: "https://fairmodel.econ.yale.edu/ec439/jpde.pdf"
pdf: "sources/13-momentum-reversal/moskowitz-2012-time-series-momentum.pdf"
access: "full-text"
source_type: "peer-reviewed"
evidence_grade: "A"
topic: "13-momentum-reversal"
asset_class: "futures"
horizon: "multi-day"
tags: "time-series-momentum, trend-following, volatility-scaling, futures, reversal"
---

## Key insight
An asset's own past 1 to 12 month excess return predicts its next-month return with a positive sign across 58 liquid futures and forwards, and the effect partially reverses over the following years. A diversified, volatility-scaled portfolio of these bets earns large abnormal returns with little factor exposure and does best in extreme markets. This is the reference definition of time-series momentum (TSMOM) that later crypto and machine-learning papers benchmark against.

## Method
Pooled panel regressions of volatility-scaled monthly excess returns on returns lagged h = 1..60 months, and on the sign of the lagged return, with standard errors clustered by month. Ex ante volatility is an exponentially weighted moving variance of daily returns with a 60-day centre of mass, annualised with 261 days and lagged one period to avoid look-ahead. The strategy for instrument s is

`r_TSMOM(t,t+1) = sign(r(t-12,t)) * (40% / sigma_t) * r(t,t+1)`

averaged equally across instruments. Look-back k and holding period h are both varied. Returns are decomposed following Lo and MacKinlay into auto-covariance, cross-serial covariance and mean effects. CFTC position data are used to link trend to speculator and hedger positioning.

## Data and sample
24 commodity futures, 12 cross-currency pairs, 9 developed equity index futures and 13 government bond futures. Prices from January 1965 to December 2009; the strategy tests run January 1985 to December 2009, monthly.

## Reported results
- Lag coefficients are positive for each of the first 12 months (nine significant) and mostly negative for lags beyond 12 months, with the strongest reversal in the year after the trend.
- All 58 contracts have a positive 12-month TSMOM return; 52 are significant at the 5% level.
- The diversified TSMOM factor has annualised volatility of about 12%, a Sharpe ratio above 1, and an alpha of about 1.58% per month against the MSCI World, SMB, HML and UMD factors.
- Returns are largest when equity market moves are most extreme in either direction. The strategy lost sharply at the trend reversal in March to May 2009.
- Positive auto-covariance, not cross-asset lead-lag, drives the profits. Speculators trade with the trend and profit at the expense of hedgers.

## Signal construction
Inputs: a return series and an EWMA volatility estimate. Signal = sign of the trailing k-period return; position = target volatility / current volatility estimate. Parameters: look-back k (12 months in the paper, 1 to 12 months all work), volatility half-life, volatility target. Update at the bar frequency chosen.

## Relevance to SOL perpetuals at minutes to hours
The transferable parts are the construction (sign of trailing return times inverse volatility) and the horizon profile (continuation first, reversal later). The paper's horizons are months; whether the same shape holds for SOL at 5-minute to multi-hour look-backs must be tested directly. Volatility scaling is directly useful under Kalshi's low leverage cap, since the cap binds exactly when volatility is low and the formula asks for large size.

## Caveats
Monthly data on diversified futures; a single-asset SOL bot loses the diversification that produces the Sharpe above 1. Gross of transaction costs. Huang et al. (2020) argue the pooled t-statistics overstate the evidence and that much of the profit comes from volatility scaling and from being long high-mean assets. Two authors are affiliated with AQR, which sells trend products.
