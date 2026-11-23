---
title: "Forecasting Bitcoin volatility using machine learning techniques"
authors: "Huang, Zih-Chun; Sangiorgi, Ivan; Urquhart, Andrew"
year: 2024
venue: "Journal of International Financial Markets, Institutions and Money 97, 102064"
url: "https://centaur.reading.ac.uk/118950/9/1-s2.0-S1042443124001306-main.pdf"
pdf: "sources/14-volatility-forecasting/huang-2024-forecasting-bitcoin-volatility-machine-learning.pdf"
access: "full-text"
source_type: "peer-reviewed"
evidence_grade: "B"
topic: "14-volatility-forecasting"
asset_class: "crypto"
horizon: "daily"
tags: "machine-learning, lstm, cnn-lstm, har, garch, bitcoin, realized-volatility, pre-averaging"
---

## Key insight
For Bitcoin realized volatility, neural networks clearly beat GARCH-type models at every horizon from 1 day to 2 months, but the margin over HAR is small and inconsistent. An LSTM given the same inputs as HAR beats HAR at all horizons; a hybrid CNN-LSTM fed high-frequency RV plus image encodings of the series helps most at the 7-day horizon. HAR remains a hard benchmark.

## Method
Daily realized volatility is built from intraday returns with pre-averaging to handle microstructure noise; the authors choose a 10-minute sampling frequency after examining how average RV changes with frequency. Benchmarks: GARCH-type models and HAR. Neural models: a single-layer LSTM with dropout, and a CNN-LSTM in which the CNN reads Markov Transition Field images of the RV series and the LSTM reads the raw series. Horizons: 1, 7, 14, 30 and 60 days. Evaluation by forecast error relative to the benchmark, the Superior Predictive Ability test and the model confidence set. Data split 90% training and 10% testing, with 80/20 and 70/30 splits as robustness checks.

## Data and sample
Tick-level BTC/USD trades on Bitstamp, 13 November 2011 to 31 December 2021 (60.5 million trades); modelling uses 2014 to 2021 because earlier years are too illiquid. The base out-of-sample period is about 290 days.

## Reported results
- LSTM and CNN-LSTM improve on GARCH-type models by 5% to 15%.
- Versus HAR, only the LSTM using HAR's inputs outperforms at all horizons. The hybrid CNN-LSTM is best at 7 days, 9.77% better than HAR.
- Adding the image inputs improves on the LSTM with the same frequency of RV inputs.
- High-frequency RV inputs beat daily data for both short and long horizons.
- An LSTM trained on ordinary (not pre-averaged) 10-minute RV failed to train properly: in-sample RMSE was about 75 times out-of-sample RMSE.
- The neural model underperforms mainly when a sudden large volatility jump occurs, and does better when jumps cluster.

## Signal construction
Not a directional signal. Recipe for a volatility forecaster: compute noise-robust RV per day (or per hour for an intraday variant), feed the same lagged features HAR uses (last period, weekly average, monthly average) to a small LSTM, and compare against HAR by QLIKE or MSE on a rolling out-of-sample window. Deploy the network only if it beats HAR out of sample by a margin that survives a model-confidence-set test.

## Relevance to SOL perpetuals at minutes to hours
The main transferable lessons are about process: clean the RV input before giving it to a network, keep the architecture small, and always benchmark against HAR. The horizons (1 day and longer) are longer than the bot's, and the asset is spot BTC on one exchange. Whether the modest gain over HAR appears at 15-minute to 4-hour horizons on SOL is untested here.

## Caveats
One asset, one exchange, a single test window of roughly 290 days that sits in 2021. Many hyperparameter combinations were searched, which raises data-snooping risk. No economic evaluation (sizing, value-at-risk, trading costs). Gains over HAR depend on architecture and horizon.
