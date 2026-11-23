---
title: "Detecting overreaction in the Bitcoin market: A quantile autoregression approach"
authors: "Chevapatrakul, Thanaset; Mascia, Danilo V."
year: 2019
venue: "Finance Research Letters 30, 371-377 (accepted version dated October 2018 read)"
url: "https://eprints.whiterose.ac.uk/id/eprint/144484/1/Chevapatrakul%20and%20Mascia.pdf"
pdf: "sources/28-shock-response-price-pressure/chevapatrakul-2019-detecting-overreaction-bitcoin-quantile.pdf"
access: "full-text"
source_type: "peer-reviewed"
evidence_grade: "B"
topic: "28-shock-response-price-pressure"
asset_class: "crypto"
horizon: "daily"
tags: "quantile-autoregression, tail-dependence, continuation, sharp-declines, asymmetry, bitcoin"
---

## Key insight
Bitcoin's average daily return has no memory, but its tails do. In the lowest quantiles of the daily return distribution, returns depend positively on the previous day's return: a sharp fall makes a further sharp fall more likely. At the weekly horizon the upper quantiles show the same positive dependence. The mean hides an asymmetry: bad days tend to continue, and good weeks tend to continue.

## Method
A first-order quantile autoregression,

`q_tau(R(t) | info(t-1)) = alpha_tau + beta_tau * R(t-1)`

estimated for quantiles `tau` from 0.05 to 0.95 on daily, weekly and monthly log returns, alongside an ordinary AR(1). Confidence bands come from inverting a rank test. Wald tests check whether slopes are equal across quantiles (for example `beta(0.10) = beta(0.90)`).

## Data and sample
Bitcoin volume-weighted closing prices from CoinMarketCap, 28 April 2013 to 3 July 2018: 1,892 daily, 270 weekly and 62 monthly returns.

## Reported results
- AR(1) at the mean: returns behave as white noise at all three frequencies.
- Daily: `beta` is positive and significant at the 10th quantile, where the daily return is about -4.00%. Around the median there is a statistically significant but economically small negative autocorrelation.
- Weekly: no persistence below the median; positive dependence from the median upward, strengthening toward the highest quantiles.
- Monthly: no dependence anywhere, with the caveat of a small sample.
- Wald tests reject equal slopes between the 10th and 90th quantiles and between the 10th quantile and the median at daily and weekly frequencies.
- The exact coefficient values in Table 2 were not extracted in this session.
- Scope record: horizon one day and one week; conditioning variable the previous period's return, evaluated in the tails of the next return's distribution; sign continuation in the left tail (daily) and right tail (weekly), slight reversal at the daily median; no trading strategy and no costs.

## Signal construction
Not a mean forecast. It is a statement about conditional tail risk: after a negative return, the lower quantiles of the next return shift down by more than a symmetric model implies. For a bot this enters risk management: fit rolling quantile regressions of the next-bar return on the last-bar return at `tau = 0.05, 0.10, 0.90, 0.95` and use the fitted lower quantile as the stop distance or size limit for a long taken after a sharp fall. Refit on a rolling window.

## Relevance to SOL perpetuals at minutes to hours
The paper qualifies the reversal evidence in a way that matters for a mean-reversion bot. An average tendency to revert (De Nicola) is compatible with a fatter left tail after a fall: most dips bounce, and the ones that do not are large. That is the payoff profile of liquidity provision described by Nagel, and it is the profile one would expect if some declines trigger liquidation cascades. The quantile method is easy to port to 5-minute to 4-hour bars on SOL, and the comparison of `beta` across quantiles is a direct test of whether fading sharp declines is paid for by tail losses.

## Caveats
Daily and weekly data only; nothing intraday. The sample ends in mid-2018 and includes the 2017 bubble and its collapse, which may drive the tail results. The authors call the pattern overreaction, but continuation after falls is also what slow information diffusion or forced selling would produce. No out-of-sample evaluation.
