---
title: "LOB-Based Deep Learning Models for Stock Price Trend Prediction: A Benchmark Study"
authors: "Prata, Matteo; Masi, Giuseppe; Berti, Leonardo; Arrigoni, Viviana; Coletta, Andrea; Cannistraci, Irene; Vyetrenko, Svitlana; Velardi, Paola; Bartolini, Novella"
year: 2023
venue: "arXiv:2308.01915v2 (preprint, under review at the time; journal publication not confirmed in this session)"
url: "https://arxiv.org/abs/2308.01915"
pdf: "sources/22-deep-learning-lob/prata-2023-lob-deep-learning-benchmark-lobcast.pdf"
access: "full-text"
source_type: "working-paper"
evidence_grade: "B"
topic: "22-deep-learning-lob"
asset_class: "equities"
horizon: "tick"
tags: "benchmark, reproducibility, generalizability, lobcast, fi-2010, lobster, overfitting, binctabl, deeplob, attention"
---

## Key insight
An independent re-implementation of fifteen deep LOB models shows that the scores reported on FI-2010 do not survive a change of data. On recent Nasdaq stocks every model lands at 48% to 61% F1, the ranking changes, and a cost-free trading simulation makes money only on stocks that happened to rise. This is the main reproducibility critique of the field.

## Method
The authors built LOBCAST, an open-source pipeline for preprocessing, training, evaluation and backtesting. They test robustness (can the published FI-2010 score be reproduced with their code and hyperparameter search) and generalizability (does the model work on new data built the same way). The fifteen models are thirteen published between 2017 and 2022 (including DeepLOB, DeepLOB-Attention, TransLOB, Axial-LOB, BiN-CTABL, CTABL, DAIN, DLA, CNN-LSTM, TLONBoF, ATNBoF) plus plain MLP and CNN baselines. All take the 40 raw LOB features. New datasets follow the FI-2010 recipe: ten levels, one record per ten events, z-score normalisation, six, two and two days for train, validation and test, ternary labels at horizons of 1, 2, 3, 5 and 10 records, five seeds.

Backtest: Backtesting.py on the LOB-2021 test days (13 to 15 July 2021); one share per trade, buy on an up signal, sell on a down signal when long, fills at the next open of a ten-event bar, no fees.

## Data and sample
FI-2010, plus LOBSTER data for six Nasdaq stocks (SOFI, NFLX, CSCO, WING, SHLS, LSTR) over 1 to 15 July 2021 (LOB-2021) and 1 to 15 February 2022 (LOB-2022, a more volatile period).

## Reported results
- All models show a significant performance drop on new data.
- On LOB-2021 and LOB-2022, F1 ranges from 48% to 61%; LOB-2022 is worse.
- BiN-CTABL, the best model on FI-2010, loses about 19.6% F1 on average across horizons (generalizability score 73.5%).
- The best models on both datasets use attention.
- Some models that originally used engineered features did better with raw features only: CNN-LSTM improved by 20.9% on average over its published FI-2010 score.
- Performance varies strongly by stock; CSCO, the most stationary, is easiest, and models are consistently best on the stationary class.
- In the backtest only LSTR and NFLX, the two stocks with the highest positive daily returns in the test window, were profitable; the two stocks with the most negative returns (SOFI, SHLS) lost for most models. Strategy return tracked the stock's own drift.
- Models are sensitive to hyperparameters and random seed.

## Signal construction
Not a signal. It is a protocol: before trusting any LOB model, retrain it on a second dataset built the same way, run several seeds, report per-instrument and per-class scores, and compare strategy return with the instrument's own return over the test window.

## Relevance to SOL perpetuals at minutes to hours
The warning transfers fully. A model that scores well on one fortnight of SOL book data should be assumed overfit until it holds on a different fortnight in a different volatility regime, and a long-only signal that profits in a rising week has shown nothing. LOBCAST can be reused as scaffolding for a crypto benchmark. The finding that easy "stationary" predictions dominate accuracy matters more in crypto, where class balance shifts quickly with volatility.

## Caveats
Each new dataset is only ten trading days, so the generalization test is itself short; the authors say longer training periods might have helped the models. The hyperparameter search may under-serve some models. The backtest is three days, long-only, mid-price fills and no costs. Co-authors include J.P. Morgan AI Research staff; the paper carries the bank's research disclaimer.
