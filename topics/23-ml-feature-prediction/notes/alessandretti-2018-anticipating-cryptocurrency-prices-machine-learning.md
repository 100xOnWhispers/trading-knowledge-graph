---
title: "Anticipating cryptocurrency prices using machine learning"
authors: "Alessandretti, Laura; ElBahrawy, Abeer; Aiello, Luca Maria; Baronchelli, Andrea"
year: 2018
venue: "Complexity 2018 (arXiv:1805.08550v4 is the copy read)"
url: "https://arxiv.org/pdf/1805.08550"
pdf: "sources/23-ml-feature-prediction/alessandretti-2018-anticipating-cryptocurrency-prices-machine-learning.pdf"
access: "full-text"
source_type: "peer-reviewed"
evidence_grade: "C"
topic: "23-ml-feature-prediction"
asset_class: "crypto"
horizon: "daily"
tags: "xgboost, lstm, cross-sectional, daily, short-training-window, frictionless-backtest, cautionary"
---

## Key insight
An early and heavily cited study showing that XGBoost and LSTM models trained on a few days of daily data pick next-day winners among 1,681 coins far better than a moving-average baseline. Its two durable findings are that very short training windows worked best because "the market evolves across time", and that the last few days of price and return are the leading features. Its headline returns are a frictionless theoretical exercise and should be read as a warning about backtest realism, not as an estimate of edge.

## Method
Three models forecast each coin's next-day return on investment. Method 1 is a single XGBoost regression pooled across coins; features are the mean, standard deviation, median, last value and trend of price, market cap, market share, rank, volume and return over a window of w days. Method 2 is one XGBoost model per coin that also sees other coins' features. Method 3 is one LSTM per coin on its own price history. Each day capital is split equally among the top n coins with positive predicted return (long-only). Window w, training length and n are re-chosen every day to maximise either the Sharpe ratio or the geometric mean return achieved up to the previous day. The baseline is a simple moving average rule. Prices are expressed in bitcoin to remove the market trend.

## Data and sample
Daily CoinMarketCap data (volume-weighted average price across exchanges, market cap, volume) for 1,681 coins, 11 November 2015 to 24 April 2018. Only coins with daily volume above 100,000 USD are tradable on a given day. Trading runs from 1 January 2016.

## Reported results
- Selected parameters: for Method 1 the median feature window is 7 days and the median training period 5 to 10 days; for Method 2 the window is 3 days and training period 10 days; the LSTM worked best with about 50 days of history.
- "Larger training windows do not necessarily lead to better results".
- Cumulative return by 24 April 2018 under Sharpe optimisation, as reported in BTC: baseline about 65 BTC, Method 1 about 1.1 x 10^3, Method 2 about 95, Method 3 about 1.2 x 10^9. The authors call some figures "exaggerated" and note that picking the best coin every day would give 6 x 10^123.
- With fees up to 0.2% all methods remain positive on average; the LSTM remains positive with fees up to 1%.
- All methods work better with prices in bitcoin than in USD.

## Signal construction
Pooled gradient-boosted regression on rolling summary statistics (mean, dispersion, median, last value, trend) of price, volume and return over a 3 to 10 bar window, retrained every bar on only the most recent 5 to 20 bars of cross-sectional data, with hyperparameters re-selected each period on trailing realised performance.

## Relevance to SOL perpetuals at minutes to hours
Two ideas transfer as hypotheses: short, frequently refreshed training windows as a response to non-stationarity, and walk-forward re-selection of hyperparameters on trailing performance. Both need testing at intraday frequency, where far more data is available per window. The cross-sectional design could be mirrored on a panel of perps. The return figures do not transfer.

## Caveats
The authors state that they assume unlimited liquidity and no market impact, ignore intraday prices, and use a daily volume-weighted average price that is not a tradable quote. The universe is dominated by small illiquid coins during the 2017 bubble, where a 100,000 USD daily volume floor is far too low for execution at the modelled prices. Daily re-optimisation of parameters on past performance adds a layer of selection. No short side. The grade reflects the backtest design, not the venue.
