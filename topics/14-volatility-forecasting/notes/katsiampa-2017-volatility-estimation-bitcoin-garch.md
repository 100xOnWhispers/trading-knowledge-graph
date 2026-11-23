---
title: "Volatility estimation for Bitcoin: A comparison of GARCH models"
authors: "Katsiampa, Paraskevi"
year: 2017
venue: "Economics Letters 158, 3-6 (read as accepted manuscript)"
url: "https://shura.shu.ac.uk/16526/1/Katsiampa-VolatilityEstimationforBitcoin%28AM%29.pdf"
pdf: "sources/14-volatility-forecasting/katsiampa-2017-volatility-estimation-bitcoin-garch.pdf"
access: "full-text"
source_type: "peer-reviewed"
evidence_grade: "C"
topic: "14-volatility-forecasting"
asset_class: "crypto"
horizon: "daily"
tags: "garch, cgarch, bitcoin, conditional-variance, in-sample-fit, component-volatility"
---

## Key insight
Among six first-order GARCH-type models fitted to daily Bitcoin returns, the component GARCH with an AR(1) mean (AR-CGARCH) fits best by every information criterion. The practical message is that Bitcoin's conditional variance has both a transitory and a slow-moving long-run component, the same two-speed structure that HAR captures with averages over different windows.

## Method
Mean equation: autoregressive, r_t = c + sum of phi_i r_{t-i} + u_t, with u_t = h_t z_t. Variance equation: one of GARCH, EGARCH, TGARCH, APARCH, CGARCH and asymmetric CGARCH, all first order. Model selection by Akaike, Bayesian and Hannan-Quinn criteria, plus log-likelihood, with ARCH(5) and Q-squared(10) diagnostics on the residuals. This is an in-sample goodness-of-fit comparison only; no forecasts are evaluated.

## Data and sample
Daily closing values of the CoinDesk Bitcoin Price Index, 18 July 2010 to 1 October 2016, 2,267 observations.

## Reported results
- Daily mean return 0.5778%, standard deviation 0.0617, skewness 0.857, kurtosis 15.1. Maximum daily log return 0.529, minimum -0.388.
- ARCH effects are strongly present (ARCH(5) statistic 54.4, significant at 1%).
- AR(1)-CGARCH(1,1) maximises the log-likelihood and is selected by all three criteria; all its parameters are significant and no ARCH effects or squared-residual autocorrelation remain.
- Standardized residuals still depart from normality.

## Signal construction
Not a signal. It informs model choice for a parametric volatility forecaster. A component GARCH splits variance into a long-run level q_t that mean-reverts slowly and a short-run deviation h_t - q_t that decays quickly. A bot can mimic this cheaply with two exponentially weighted variances (fast and slow half-lives) rather than fitting CGARCH by maximum likelihood.

## Relevance to SOL perpetuals at minutes to hours
Limited direct transfer. The data are daily, end in 2016 (before perpetuals, institutional flows and the current market structure) and cover Bitcoin only. What carries over is the qualitative two-component structure, which later crypto studies with intraday data also find (see the Barjašić note, where cGARCH is among the two models that benefit most from volume and spread information at 1-minute frequency). The Hansen note finds no significant leverage-type asymmetry for BTC and ETH, and the Tang note finds an inverted asymmetry, so asymmetric GARCH variants designed for equities should not be assumed to help on SOL.

## Caveats
In-sample fit only, with no out-of-sample forecast evaluation, no loss function such as QLIKE, and Gaussian likelihood on clearly non-Gaussian residuals. The search results in this session pointed to a later replication study that reports results differing in part from this paper; that replication was not opened. Treat the specific ranking as weak evidence and the two-component finding as a hypothesis to test.
