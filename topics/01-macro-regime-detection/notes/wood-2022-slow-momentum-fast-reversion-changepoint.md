---
title: "Slow Momentum with Fast Reversion: A Trading Strategy Using Deep Learning and Changepoint Detection"
authors: "Wood, Kieran; Roberts, Stephen; Zohren, Stefan"
year: 2022
venue: "Journal of Financial Data Science 4(1) (read as arXiv:2105.13727v3)"
url: "https://arxiv.org/pdf/2105.13727"
pdf: "sources/01-macro-regime-detection/wood-2022-slow-momentum-fast-reversion-changepoint.pdf"
access: "full-text"
source_type: "peer-reviewed"
evidence_grade: "B"
topic: "01-macro-regime-detection"
asset_class: "futures"
horizon: "daily"
tags: "changepoint-detection, gaussian-process, lstm, deep-momentum-network, time-series-momentum, regime-feature, machine-learning"
---

## Key insight
Instead of using a regime label to switch strategies by rule, feed an online changepoint detector's outputs to a learning model as features and let it learn how to respond. Adding a changepoint score and location to an LSTM trend-following network raised its Sharpe ratio by about one third over 1995 to 2020 across 50 futures, and by about two thirds in 2015 to 2020, when plain momentum struggled. The network learns to hold slow momentum in stable periods and to flip quickly after a detected break. The edge disappears above roughly 2 bp of transaction cost.

## Method
Changepoint module, run per asset per day on a lookback window of l standardised daily returns: fit a Gaussian process with a single Matérn 3/2 kernel, then one with a changepoint kernel that blends two Matérn 3/2 kernels through a sigmoid located at c. From the two negative log marginal likelihoods compute

`severity nu_t = 1 - 1/(1 + exp(-(nlml_changepoint - nlml_matern)))`, `location gamma_t = (c - (t - l)) / l`,

both in (0, 1). These join the usual inputs (normalised returns at daily, monthly, quarterly, biannual and annual offsets, plus MACD indicators) to an LSTM with a tanh output layer that sets position size and is trained to maximise portfolio Sharpe ratio directly. The lookback l in {10, 21, 63, 126, 252} is treated as a hyperparameter. Benchmarks: long only, MACD, time-series momentum blending 252-day and 21-day signs, and the LSTM without the module.

## Data and sample
50 liquid continuous futures contracts (commodities, equities, fixed income, FX) from the Pinnacle Data Corp CLC database, daily, 1990 to 2020. Expanding-window training with out-of-sample testing in five-year blocks from 1995 to 2020.

## Reported results
Average over 1995 to 2020, before costs, raw signal output:
- Sharpe: long only 0.44; MACD 0.77; time-series momentum 0.94 (slow only), 0.89 (blend), 0.48 (fast only); LSTM 1.62; LSTM with changepoint module 1.77 (l = 10), 2.04 (l = 21), 2.08 (l = 63), 1.75 (l = 126), 1.45 (l = 252), 2.16 with l optimised.
- Share of positive-return days: 55.23% without the module, 56.22% with.
- Sortino ratio improved by 35% and Calmar ratio by 25% relative to the LSTM alone.
- 2015 to 2020, five repeated trials: average Sharpe improvement 70% at l = 21.
- Costs: the strategy beats classical ones up to 2 bp average cost, then "rapidly deteriorates" because of the fast-reverting component; longer lookbacks become preferable as costs rise.

## Signal construction
For each instrument and bar: standardise the last l returns, fit the two Gaussian processes, emit (nu_t, gamma_t). Use them as features in whatever model sets the position, or as a gate: high nu with gamma near 1 means a strong, recent break, so shorten momentum lookbacks or permit counter-trend entries. The paper's example flags a changepoint when nu >= 0.9995 with l = 63 for plotting regimes.

## Relevance to SOL perpetuals at minutes to hours
The design transfers well: a changepoint score is a continuous regime feature that a learner can weigh, avoiding hard switches. Two problems for this bot. First, cost: an edge that dies above 2 bp will not survive taker fees on crypto perps, so turnover must enter the loss function, as the authors recommend. Second, compute: two Gaussian-process fits per instrument per bar is heavy at minute frequency, and a cheaper detector such as [adams-2007](adams-2007-bayesian-online-changepoint-detection.md) could supply similar features. Training a network on one instrument's intraday history also risks overfitting that a 50-asset daily panel mitigates.

## Caveats
Headline Sharpe ratios are gross of costs for a diversified 50-asset portfolio and are not comparable to single-asset results. Neural results vary across random seeds; the 2015 to 2020 claim averages five runs. The lookback is tuned on validation data. Journal details are from a search summary of the Oxford repository record, not from the publisher page.
