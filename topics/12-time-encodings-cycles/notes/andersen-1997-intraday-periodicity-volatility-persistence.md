---
title: "Intraday periodicity and volatility persistence in financial markets"
authors: "Andersen, Torben G.; Bollerslev, Tim"
year: 1997
venue: "Journal of Empirical Finance"
url: "https://public.econ.duke.edu/~boller/Published_Papers/joef_97.pdf"
pdf: "sources/12-time-encodings-cycles/andersen-1997-intraday-periodicity-volatility-persistence.pdf"
access: "full-text"
source_type: "peer-reviewed"
evidence_grade: "A"
topic: "12-time-encodings-cycles"
asset_class: "multi"
horizon: "minutes"
tags: "fourier-flexible-form, intraday-periodicity, volatility, seasonal-adjustment, garch"
---

## Key insight
Intraday volatility has a strong deterministic time-of-day pattern, and ignoring it makes standard volatility models give contradictory answers across sampling frequencies. The paper shows how to estimate that pattern with a small set of sines and cosines (the Fourier flexible form, FFF) and divide it out, after which intraday volatility dynamics line up with daily ones. This is the origin of the sine and cosine time-of-day regressors used in high-frequency finance.

## Method
Returns for interval n of day t are decomposed as `R[t,n] = E(R[t,n]) + sigma[t] * s[t,n] * Z[t,n] / sqrt(N)`, where `sigma[t]` is a daily volatility factor, `s[t,n]` the periodic component and N the number of intervals per day. Define

`x[t,n] = 2*log|R[t,n] - E(R[t,n])| - log(sigma[t]^2) + log(N) = log(s[t,n]^2) + log(Z[t,n]^2)`

and regress x on the FFF (Appendix B, Eq. A.3):

`f(theta; sigma_t, n) = sum_{j=0..J} sigma_t^j * [ mu0j + mu1j*n/N1 + mu2j*n^2/N2 + sum_i lambda_ij*I(n = d_i) + sum_{p=1..P} ( gamma_pj*cos(2*pi*p*n/N) + delta_pj*sin(2*pi*p*n/N) ) ]`

with `N1 = (N+1)/2` and `N2 = (N+1)(N+2)/6`. Estimation is two-step: get `sigma_t` from a daily MA(1)-GARCH(1,1), then run OLS. The seasonal estimate is `s_hat[t,n] = T * exp(f_hat[t,n]/2) / sum over all intervals of exp(f_hat/2)`, so it averages to one. Dummies `I(n = d_i)` absorb intervals that do not fit the smooth shape.

The scanned copy was read as page images; pages covering the abstract, introduction, Section 4.3, Table 3 and Appendices A and B were read, not the whole paper.

## Data and sample
Deutschemark-dollar interbank quotes (Reuters via Olsen and Associates), 1 October 1992 to 29 September 1993, 288 five-minute returns per day, 260 days, 74,880 observations, weekends removed. S&P 500 futures (CME), 2 January 1986 to 31 December 1989, 80 five-minute returns per day, 991 days, 79,280 observations.

## Reported results
- DM-dollar fit uses J = 0 and P = 6; the shape did not depend on the daily volatility level.
- S&P 500 fit uses J = 1 and P = 2 plus three dummies for the last fifteen minutes of trading.
- For raw intraday DM-dollar returns, GARCH half-lives are about 12.5 trading days at long intraday intervals, fall below 4 hours at half-hour to 1.5-hour sampling, and rise again at 5 to 10 minutes, which the authors attribute to the periodic pattern.
- The daily DM-dollar GARCH(1,1) benchmark is alpha = 0.105, beta = 0.873.

## Signal construction
Not a directional signal. It is the standard recipe for a volatility seasonal factor:
1. Compute 5-minute log returns from a liquid venue.
2. Estimate a daily (or rolling 24-hour) variance.
3. Regress `x` on `cos(2*pi*p*n/N)` and `sin(2*pi*p*n/N)`, p = 1..P, with n the bin index in the day (or week).
4. Use `s_hat` to standardize returns, scale thresholds and size positions by time of day.
Refit on a rolling window, for example weekly.

## Relevance to SOL perpetuals at minutes to hours
Crypto trades all 288 five-minute bins, like the FX series here, so the J = 0, P = 4 to 6 specification is a natural starting point. The quadratic terms exist for markets with an open and a close and can be dropped. Dummies are the right tool for the 8-hour funding timestamps and scheduled US data releases. Whether the SOL shape is stable enough for a static fit needs testing.

## Caveats
One year of FX data and four years of futures from before electronic trading. The seasonal is assumed constant over the sample. Estimates are in-sample. The log-absolute-return regression is sensitive to zero returns and jumps (see Boudt et al.). Nothing here predicts direction.
