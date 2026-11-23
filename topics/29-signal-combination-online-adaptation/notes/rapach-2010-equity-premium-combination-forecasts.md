---
title: "Out-of-Sample Equity Premium Prediction: Combination Forecasts and Links to the Real Economy"
authors: "Rapach, David E.; Strauss, Jack K.; Zhou, Guofu"
year: 2010
venue: "Review of Financial Studies 23(2), 821-862"
url: "https://ideas.repec.org/a/oup/rfinst/v23y2010i2p821-862.html"
pdf: "none"
access: "abstract-only"
source_type: "peer-reviewed"
evidence_grade: "A"
topic: "29-signal-combination-online-adaptation"
asset_class: "equities"
horizon: "multi-day"
tags: "forecast-combination, return-predictability, model-uncertainty, instability, historical-average-benchmark"
---

## Key insight
The reference result that forecast combination rescues return prediction in finance. Welch and Goyal (2008) had shown that individual predictive regressions for the US equity premium, despite in-sample significance, fail to beat the historical average out of sample. This paper argues the failure comes from model uncertainty and instability, and that simply combining the individual forecasts delivers statistically and economically significant out-of-sample gains over the historical average. Only the abstract and bibliographic record were read in this session.

## Method
From the abstract: individual predictive regression forecasts of the equity premium, one per economic variable, are combined into a single forecast and compared out of sample against the historical-average benchmark. The abstract gives two explanations for the gain: combining incorporates information from many variables while substantially reducing forecast volatility, and the combination forecasts are linked to the real economy. The specific combining schemes (the paper is generally cited for the mean, median, trimmed mean and discounted-MSE weights) were not read here and are not confirmed.

## Data and sample
Not stated in the abstract. The setting is US aggregate equity premium prediction with the Welch and Goyal predictor set; frequency and sample dates were not confirmed in this session.

## Reported results
The abstract states only qualitative results: "Combining delivers statistically and economically significant out-of-sample gains relative to the historical average consistently over time." No numbers were read.

## Signal construction
Not a signal by itself. The transferable recipe is: fit one small model per predictor (a univariate regression of next-period return on that signal), and average the resulting return forecasts instead of fitting one multivariate model on all predictors. The combined forecast is far less volatile than any single one, which matters more than its small increase in information content.

## Relevance to SOL perpetuals at minutes to hours
This is the finance-specific counterpart of the forecast-combination puzzle and the natural template for combining weak intraday signals: N univariate recursive regressions, then a mean or trimmed mean. It also supplies the right null: the benchmark is a zero or historical-mean forecast, and the question is whether the combination beats it out of sample after costs. The low-frequency equity setting does not transfer; at minutes-to-hours horizons turnover costs dominate and must be added to the comparison.

## Caveats
Abstract-only. Equity premium at low frequency; no trading costs in the forecast evaluation as far as the abstract shows. The broader literature debates how much of the gain survives in later samples; that debate was not read here.
