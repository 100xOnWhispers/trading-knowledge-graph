---
title: "Robust estimation of intraweek periodicity in volatility and jump detection"
authors: "Boudt, Kris; Croux, Christophe; Laurent, Sebastien"
year: 2011
venue: "Journal of Empirical Finance"
url: "https://ideas.repec.org/a/eee/empfin/v18y2011i2p353-367.html"
pdf: "none"
access: "abstract-only"
source_type: "peer-reviewed"
evidence_grade: "A"
topic: "12-time-encodings-cycles"
asset_class: "fx"
horizon: "minutes"
tags: "intraweek-periodicity, robust-estimation, jumps, seasonal-adjustment, volatility"
---

## Key insight
Price jumps bias the classical estimators of the periodic volatility pattern, so the seasonal factor should be estimated with robust methods. Once periodicity is accounted for, intraday jump tests find more of the small jumps that occur when volatility is seasonally low and raise fewer false alarms when it is seasonally high. Only the abstract was read; the full text is behind the publisher's paywall and no open copy could be downloaded.

## Method
From the abstract (RePEc record, vol. 18(2), pages 353-367): the authors propose robust alternatives to the classical periodicity estimators and use them inside intraday jump detection. A search-result summary of the KU Leuven repository record for the 2008 working-paper version (FBE Research Report KBI_0825), which was not itself opened, describes the two proposals as a non-parametric weighted standard deviation and a parametric truncated maximum likelihood estimator. The formulas were not read and are not reproduced here.

The periodicity is intraweek, meaning the pattern is indexed by time of week and not only time of day.

## Data and sample
The abstract names EUR/USD, GBP/USD and YEN/USD high-frequency returns. Sample period and sampling frequency: not confirmed.

## Reported results
As stated in the abstract only:
- Opening, lunch and closing of markets induce a periodic component in the volatility of high-frequency returns.
- Jumps bias classical periodicity estimators; robust alternatives are proposed.
- Accounting for periodicity improves the accuracy of intraday jump detection in both directions described above.
- Detected jumps are then used to robustly estimate the long-memory parameter of squared returns for the three currency pairs.
No numbers were available in what was read.

## Signal construction
Not a directional signal. It supplies the seasonal divisor for standardized returns and the scale for jump or shock flags. The paper's exact estimators were not read. A generic robust analogue that a bot could run, stated as an implementation suggestion and not as the paper's method:
1. Standardize each 5-minute return by a local daily volatility estimate that is itself jump-robust (for example bipower variation).
2. Group standardized returns by time-of-week bin (2,016 five-minute bins).
3. Take a robust scale per bin (for example 1.4826 times the median absolute deviation), smooth across neighbouring bins, and normalize so the mean squared factor equals one.
4. Flag a shock when `|r| / (local_vol * seasonal_factor)` exceeds a high quantile.

## Relevance to SOL perpetuals at minutes to hours
Crypto has frequent liquidation cascades and news jumps, so a seasonal factor fitted by OLS on log absolute returns or by plain standard deviations will be contaminated in exactly the bins where the largest events happened to fall. With only a few months of Kalshi history, each time-of-week bin holds few observations and one cascade can dominate it. A robust estimator computed on Binance or Coinbase SOL data is the sensible default. The intraweek framing also fits crypto, where weekends are open but thinner.

## Caveats
Abstract-only access: every methodological detail beyond the abstract is unverified here. The evidence is on major FX pairs, not crypto. Robust scale estimators need many observations per bin, which conflicts with letting the seasonal adapt quickly. The suggested implementation above is not from the paper and needs its own validation.
