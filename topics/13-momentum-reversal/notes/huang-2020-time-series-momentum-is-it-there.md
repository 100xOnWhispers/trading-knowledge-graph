---
title: "Time series momentum: Is it there?"
authors: "Huang, Dashan; Li, Jiangyuan; Wang, Liyao; Zhou, Guofu"
year: 2020
venue: "Journal of Financial Economics 135(3), 774-794"
url: "https://down.aefweb.net/WorkingPapers/w717.pdf"
pdf: "sources/13-momentum-reversal/huang-2020-time-series-momentum-is-it-there.pdf"
access: "full-text"
source_type: "peer-reviewed"
evidence_grade: "A"
topic: "13-momentum-reversal"
asset_class: "futures"
horizon: "multi-day"
tags: "time-series-momentum, critique, bootstrap, pooled-regression, volatility-scaling"
---

## Key insight
Re-examining the Moskowitz, Ooi and Pedersen data, the authors find little statistical evidence that the past 12-month return predicts the next month's return asset by asset. The famous pooled t-statistic is below bootstrap critical values, so it does not establish predictability. The TSM strategy is profitable, but a strategy that simply goes long assets with positive historical mean returns performs the same, so the profits do not require return predictability.

## Method
Three stages. (1) Asset-by-asset predictive regressions of monthly return on the past 12-month return, in-sample and with the Campbell-Thompson out-of-sample R-squared. (2) The pooled regression of the original paper, re-evaluated with a parametric wild bootstrap and a nonparametric pairs bootstrap, because volatility scaling without fixed effects and persistent regressors make the pooled test over-reject. (3) Comparison of the TSM strategy with a "time series history" (TSH) strategy that buys assets whose historical mean return is positive and sells the rest, under equal weighting, volatility weighting and other schemes.

## Data and sample
55 futures and forward instruments from the same sources as the original paper (commodities, equity indices, bonds, currencies), monthly, January 1985 to December 2015.

## Reported results
- At the 10% level, 47 of 55 assets have a t-statistic below 1.65 in the in-sample regression.
- Only three assets have a significant out-of-sample R-squared at the 10% level.
- The pooled t-statistic is 4.34, but the bootstrap critical values are 12.53 (wild) and 4.83 (pairs), so it is not significant.
- TSM and TSH perform virtually the same; differences in mean and risk-adjusted returns are indistinguishable from zero under every weighting scheme. Profits come mainly from the long legs; short legs are insignificant.
- The authors cite Kim et al. (2016) that TSM profits are driven by volatility scaling, and Goyal and Jegadeesh (2018) on leverage adjustment.

## Signal construction
Not a signal. It is a testing protocol for any trend signal: (a) test each instrument separately, not only pooled; (b) bootstrap the pooled statistic; (c) benchmark against a no-predictability strategy that is long whenever the historical mean is positive; (d) report results with and without volatility scaling.

## Relevance to SOL perpetuals at minutes to hours
Directly relevant as a discipline. SOL has had a strongly positive drift over much of its history, so any long-biased trend rule will look good against cash. The right benchmark for a SOL trend signal is a volatility-scaled long position and a "long if trailing mean is positive" rule, and the short leg must be evaluated on its own. If the short side adds nothing, the signal is a drift proxy, not a timing signal.

## Caveats
The critique is about the 12-month look-back at monthly frequency; it does not test intraday or daily horizons. It does not say trend following loses money, only that predictability is not proven. Weak power of single-asset tests cuts both ways: failing to reject is not evidence of no effect.
