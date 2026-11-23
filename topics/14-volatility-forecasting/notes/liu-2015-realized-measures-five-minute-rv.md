---
title: "Does Anything Beat 5-Minute RV? A Comparison of Realized Measures Across Multiple Asset Classes"
authors: "Liu, Lily Y.; Patton, Andrew J.; Sheppard, Kevin"
year: 2015
venue: "Journal of Econometrics 187(1), 293-311 (read as working paper dated 5 December 2012)"
url: "https://public.econ.duke.edu/~ap172/Liu_Patton_Sheppard_dec12.pdf"
pdf: "sources/14-volatility-forecasting/liu-2015-realized-measures-five-minute-rv.pdf"
access: "full-text"
source_type: "peer-reviewed"
evidence_grade: "A"
topic: "14-volatility-forecasting"
asset_class: "multi"
horizon: "daily"
tags: "realized-variance, sampling-frequency, realized-kernel, truncated-rv, model-confidence-set, estimator-comparison"
---

## Key insight
Across almost 400 realized-variance estimators and 31 assets, plain 5-minute realized variance is very hard to beat significantly. More sophisticated noise-robust estimators help mainly on the most liquid assets. For forecasting, the best input is a jump-truncated RV at 5 or 15 minutes, which is consistent with jumps not being persistent.

## Method
The authors compute roughly 400 estimators per asset: RV at many sampling frequencies, in calendar and tick time, on trades and quotes, with and without subsampling; first-order autocorrelation-adjusted RV; two-scale and multi-scale RV; realized kernels; realized range; jump-robust measures (bipower, truncated RV, MedRV and similar). Estimation accuracy is ranked with a data-based method using a proxy for the latent quadratic variation. Significance is assessed with the Romano-Wolf stepwise test against 5-minute RV as benchmark and with the model confidence set of Hansen, Lunde and Nason when no benchmark is imposed. Forecast usefulness is tested by plugging each measure into a HAR model at horizons of 1 to 50 days.

## Data and sample
Thomson Reuters Tick History, January 2000 to December 2010: 31 assets in five classes (US and UK individual equities, equity index futures, computed equity indices, currency futures, interest rate futures). Average 2,537 trading days per asset.

## Reported results
- With 5-minute RV as benchmark, there is very little evidence that any competitor significantly outperforms it for estimation accuracy on any of the 31 assets.
- Without a benchmark, the model confidence set shows a small number of estimators doing better: 1-minute RV, autocorrelation-adjusted RV, and 1- to 5-second realized kernels and multi-scale RV.
- For forecasting, 5-minute or 15-minute truncated RV performs best on average. 5-minute RV is in about 40% of model confidence sets at short horizons, rising to about 70% at long horizons.
- Gains from sophisticated estimators are concentrated in liquid classes (currency and index futures). For measures near 5 minutes, tick-time sampling and subsampling both generally improve accuracy.

## Signal construction
Not a signal. It is the guide to choosing the volatility input: default to 5-minute RV; add subsampling (average the RV over the five possible 1-minute offsets) at no extra data cost; for the forecasting input, truncate returns above a threshold (a multiple of local volatility) before squaring.

## Relevance to SOL perpetuals at minutes to hours
The headline is reassuring: there is no need for exotic estimators before a bot is profitable. But the study measures daily variance with 78 or more 5-minute bars. An intraday bot needing a 1-hour variance estimate has only 12 such bars, so finer sampling (1 minute, with subsampling or a kernel) on the most liquid SOL perp is likely necessary, and the paper's finding that 1-minute RV sits in the best set for liquid assets supports that. Whether SOL on Binance behaves like a "liquid" asset in this sense, and how far the Kalshi contract itself falls short, needs direct testing.

## Caveats
No crypto assets; sample ends 2010. Forecast rankings are conditional on the HAR model and on a single measure at a time. The version read is the 2012 working paper; journal details were confirmed from another paper's reference list, not from the published article.
