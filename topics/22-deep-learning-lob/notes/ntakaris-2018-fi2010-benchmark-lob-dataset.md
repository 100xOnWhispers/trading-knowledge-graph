---
title: "Benchmark Dataset for Mid-Price Forecasting of Limit Order Book Data with Machine Learning Methods"
authors: "Ntakaris, Adamantios; Magris, Martin; Kanniainen, Juho; Gabbouj, Moncef; Iosifidis, Alexandros"
year: 2018
venue: "Journal of Forecasting 37(8), 852-866; arXiv:1705.03233v5"
url: "https://arxiv.org/abs/1705.03233"
pdf: "sources/22-deep-learning-lob/ntakaris-2018-fi2010-benchmark-lob-dataset.pdf"
access: "full-text"
source_type: "peer-reviewed"
evidence_grade: "B"
topic: "22-deep-learning-lob"
asset_class: "equities"
horizon: "tick"
tags: "fi-2010, benchmark-dataset, nasdaq-nordic, labelling, normalisation, ridge-regression, anchored-cross-validation"
---

## Key insight
FI-2010 is the first public limit order book dataset for mid-price prediction and the benchmark on which most deep LOB models report their headline scores. Knowing exactly what it contains explains why those scores do not carry over: it is ten days of five Finnish stocks from 2010, down-sampled, pre-normalised and labelled with one fixed threshold.

## Method
The authors rebuilt order books from the Nasdaq Nordic ITCH feed, kept continuous trading between 10:30 and 18:00, and sampled one record every 10 events. Each record is a 144-dimensional vector following Kercheval and Zhang (2015): the raw 10-level book (40 values), features describing the book state, and time-sensitive features such as intensities and derivatives. Three normalised versions are provided (z-score, min-max, decimal precision).

Labels: l = (mean of the next k mid-prices minus the current mid-price) / current mid-price, for k = 1, 2, 3, 5, 10 records. Class "up" if l >= 0.002, "down" if l <= -0.002, otherwise stationary.

Protocol: day-based anchored forward validation in nine folds (train on days 1..i, test on day i+1). Baselines are ridge regression and a single-hidden-layer feed-forward network (SLFN).

## Data and sample
Kesko, Outokumpu, Sampo, Rautaruukki and Wartsila on the Helsinki exchange, 1 June to 14 June 2010 (ten trading days). About four million events, giving 394,337 ten-event records.

## Reported results
- The two baselines reach an average out-of-sample F1 of about 46%.
- With z-score data, ridge regression F1 across the five horizons is 0.410, 0.440, 0.433, 0.427, 0.416; SLFN is 0.327, 0.327, 0.389, 0.459, 0.410.
- For the SLFN at the fifth label horizon, F1 is 33% on raw data against 46%, 43% and 43% with z-score, min-max and decimal normalisation, so normalisation choice moves results materially.
- The authors note the feature set lacks order flow information (the message sequence).

## Signal construction
Not a signal. It is the standard test bed. Use it only to check that an implementation reproduces published numbers before moving to real data.

## Relevance to SOL perpetuals at minutes to hours
Little transfers directly. The stocks are illiquid large-tick equities from 2010 with a day session; SOL perps trade continuously with a much smaller relative tick and far higher update rates. What does transfer is the template (event sampling, smoothed ternary labels, anchored walk-forward folds) and the lessons from its weaknesses: choose the label threshold from costs rather than class balance, normalise with trailing statistics only, and build a much longer sample.

## Caveats
Ten days cannot contain more than one regime. The single 0.002 threshold was applied to all stocks. The public files are already normalised, so raw prices cannot be recovered for cost-aware backtests. Later papers quote horizons of 10, 20, 30, 50 and 100 on the same data, where this paper states 1, 2, 3, 5 and 10; the two appear to be the same labels counted in events rather than ten-event records (DeepLOB's table quotes this paper's label-1 ridge scores, 48.0% accuracy and 41.0% F1, as "k = 10"). Benchmarks that compare 15 models on FI-2010 and on newer Nasdaq data find that top FI-2010 scores drop sharply (see prata-2023 note).
