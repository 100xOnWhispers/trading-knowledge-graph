---
title: "Time-related feature engineering (scikit-learn example gallery, version 1.7)"
authors: "scikit-learn developers"
year: 2025
venue: "scikit-learn documentation"
url: "https://scikit-learn.org/1.7/_sources/auto_examples/applications/plot_cyclical_feature_engineering.rst.txt"
pdf: "none"
access: "full-text"
source_type: "documentation"
evidence_grade: "C"
topic: "12-time-encodings-cycles"
asset_class: "multi"
horizon: "hours"
tags: "cyclical-encoding, sine-cosine, periodic-splines, one-hot, gradient-boosting"
---

## Key insight
How time of day should be encoded depends on the model. Gradient-boosted trees did best with raw integer hour and weekday. For a linear model, a single sine and cosine pair per period was only slightly better than raw integers and worse than one-hot encoding; periodic splines matched one-hot with a smooth, order-preserving basis. A single sine and cosine pair is too rigid for a pattern with several peaks.

## Method
A worked example comparing encodings of hour, weekday and month under time-ordered cross-validation.

Trigonometric encoding, as given in the code:

`sin_transformer(period): x -> sin(x / period * 2 * pi)`
`cos_transformer(period): x -> cos(x / period * 2 * pi)`

applied with period 24 to hour, 7 to weekday and 12 to month. Each ordinal feature becomes two features with no jump between the last and first value.

Periodic splines: `SplineTransformer(degree=3, n_knots=n_splines+1, knots=linspace(0, period, n_knots), extrapolation="periodic", include_bias=True)`.

Further variants add spline-by-workingday interactions with `PolynomialFeatures`, and a Nystroem polynomial kernel approximation. Cross-validation is `TimeSeriesSplit(n_splits=5, gap=48, max_train_size=10000, test_size=1000)`. The year of the version-1.7 release is taken as the publication year; the page itself carries no date.

## Data and sample
Bike Sharing Demand from OpenML: hourly, 17,379 rows, target is hourly count divided by its maximum. Not financial data.

## Reported results
Mean absolute error, as a fraction of maximum demand, mean plus or minus standard deviation over five folds:

| Model and encoding | MAE | RMSE |
|---|---|---|
| Gradient boosting, raw time features | 0.044 +/- 0.003 | 0.068 +/- 0.005 |
| Ridge, raw ordinal (min-max scaled) | 0.142 +/- 0.014 | 0.184 +/- 0.020 |
| Ridge, one-hot time | 0.099 +/- 0.011 | 0.131 +/- 0.011 |
| Ridge, sine and cosine | 0.125 +/- 0.014 | 0.166 +/- 0.020 |
| Ridge, periodic splines | 0.097 +/- 0.011 | 0.132 +/- 0.013 |
| Ridge, splines plus hour-by-workingday interactions | 0.078 +/- 0.009 | 0.104 +/- 0.009 |
| Splines plus Nystroem kernel | 0.053 +/- 0.002 | 0.076 +/- 0.004 |
| One-hot plus Nystroem kernel | 0.082 +/- 0.006 | 0.111 +/- 0.011 |

The text calls the sine and cosine outcome "disappointing" and notes that splines scale to minute resolution without adding features, which one-hot encoding cannot do.

## Signal construction
Not a signal. It is the encoding recipe:
- Tree models (LightGBM, XGBoost): pass integer minute-of-day and day-of-week, or a few binned versions. Sine and cosine add little.
- Linear models and neural networks: use several harmonics, `sin(2*pi*k*x/period)` and `cos(2*pi*k*x/period)` for k = 1..K, or 8 to 12 periodic cubic splines per day.
- Add explicit interactions (hour by weekend flag), since additive time features cannot express a different daily shape on weekends.

## Relevance to SOL perpetuals at minutes to hours
The mechanics transfer directly. The ranking of encodings is a property of model class and target shape, so the main lesson holds: do not expect one sine and cosine pair to carry a multi-peaked intraday pattern such as Asia, Europe and US session opens plus funding times. The size of the gains does not transfer. Bike demand is dominated by time of day; conditional expected returns in crypto are not.

## Caveats
One dataset with very strong seasonality and high signal-to-noise. No statistical tests across datasets. It is a tutorial, not a study. Version-specific numbers may change between releases.
