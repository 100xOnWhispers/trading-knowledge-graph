---
title: "Rise of the Machines? Intraday High-Frequency Trading Patterns of Cryptocurrencies"
authors: "Petukhina, Alla A.; Reule, Raphael C. G.; Härdle, Wolfgang Karl"
year: 2021
venue: "The European Journal of Finance, 27(1-2), 8-30 (arXiv 2009.04200 post-print)"
url: "https://arxiv.org/pdf/2009.04200"
pdf: "sources/10-intraday-seasonality-crypto/petukhina-2021-rise-machines-intraday-crypto.pdf"
access: "full-text"
source_type: "peer-reviewed"
evidence_grade: "C"
topic: "10-intraday-seasonality-crypto"
asset_class: "crypto"
horizon: "minutes"
tags: "intraday-seasonality, generalized-additive-model, splines, altcoins, weekend-effect, proof-of-human"
---

## Key insight
If algorithms ran the crypto market, activity should not depend on the clock. It does: absolute returns and volume of eleven coins follow the human working day and working week, with a trough at night and a drop at weekends. The authors call this "proof of human" and conclude that, in 2018, most trading was initiated by people, not machines. The paper is also an early use of a semi-parametric learner (a generalised additive model) to fit intraday and intraweek seasonality.

## Method
A generalised additive model with identity link, y_i = f_1(time of day) + f_2(day of week) + e_i, where y is absolute log return, return, or volume on 5-minute bars. Daily seasonality uses cubic regression splines, weekly seasonality uses P-splines; smoothing parameters are chosen by generalised cross-validation (R package mgcv). Summary statistics, autocorrelations, and return correlations with the CRIX index on up and down days are also reported.

## Data and sample
5-minute data for BCH, BTC, DASH, ETC, ETH, LTC, REP, STR, XMR, XRP and ZEC from European sources (timestamps GMT+1), 1 July 2018 to 31 August 2018, plus the CRIX index.

## Reported results
- The smooth terms are highly significant but explain little: coefficients of determination are around 1%.
- Daily pattern: a pronounced low during European sleeping hours, growth through the morning, a flattening around lunch, and for most coins a peak between 17:00 and 20:00 local time, followed by a decline.
- Weekly pattern: absolute returns peak from Tuesday to about Thursday and fall steeply at weekends; volume is lower at weekends than on Thursdays and Fridays.
- First-order autocorrelation of 5-minute returns is close to zero and mostly negative (from 0.01 for DASH to -0.09 for STR); squared and absolute returns are positively autocorrelated.
- Excess kurtosis is large for every coin (largest for BTC at 49.44).
- Results are described as similar across all eleven coins.

## Signal construction
Not a directional signal. It is a method for the seasonal baseline: fit a GAM (or any spline or tree model) of |return| and volume on time of day and day of week, refit on a rolling window, and use the fitted value as the expected level. Deviation from the fit is the tradable "surprise". A spline fit is smoother and less noisy than 288 separate slot means.

## Relevance to SOL perpetuals at minutes to hours
Shows that altcoins share the BTC seasonal shape, which supports pooling coins when estimating SOL's seasonal curve. The 17:00 to 20:00 European-time peak (roughly 16:00 to 19:00 GMT in this GMT+1 dataset) agrees with the afternoon-UTC peak in larger studies. The "humans dominate" conclusion is dated: later evidence (Hansen note) shows machine-like bursts at round clock times that grew after 2019.

## Caveats
Two summer months in a bear market, a single data vendor, no venue breakdown, and very low explanatory power. The inference from "activity follows the clock" to "humans dominate" is weak, since algorithms also follow liquidity and news that arrive on a human schedule. No out-of-sample test and no trading application.
