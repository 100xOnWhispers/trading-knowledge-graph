---
title: "Forecasting Volatility with Machine Learning and Rough Volatility: Example from the Crypto-Winter"
authors: "Tang, Siu Hin; Rosenbaum, Mathieu; Zhou, Chao"
year: 2023
venue: "arXiv preprint 2311.04727 (v2, February 2024)"
url: "https://arxiv.org/pdf/2311.04727"
pdf: "sources/14-volatility-forecasting/tang-2023-lstm-rough-volatility-crypto-winter.pdf"
access: "full-text"
source_type: "working-paper"
evidence_grade: "B"
topic: "14-volatility-forecasting"
asset_class: "crypto"
horizon: "daily"
tags: "lstm, rough-volatility, universal-model, pooled-training, inverted-asymmetry, binance, altcoins"
---

## Key insight
A single "universal" LSTM trained on pooled data from many coins forecasts next-day volatility better than HAR or AR models fitted to each coin separately. A five-parameter rough-volatility model with coin-independent parameters does about as well. Volatility dynamics therefore look largely common across coins, so a model for one coin can borrow strength from the rest. The LSTM's sensitivities also show that in crypto, positive returns raise next-day volatility, the opposite of equities.

## Method
Daily realized variance is the sum of squared 5-minute returns. Benchmarks are AR(7), AR(30) and HAR (with lags adapted to seven-day weeks) fitted per coin. LSTMs take the last 7 or 30 days of realized variance, optionally with daily returns, and are trained once on the pooled panel. The parametric alternative combines the rough fractional stochastic volatility forecast with a quadratic rough Heston form that captures the Zumbach effect (dependence of volatility on past price trends); the Hurst parameter is calibrated on the pooled set. Evaluation is out-of-sample mean squared error per coin, reported as a ratio to HAR. Gradients of the LSTM output with respect to lagged variance and lagged returns give interpretable sensitivities.

## Data and sample
5-minute prices from Binance for 213 coins quoted in USDT, after removing stablecoins, leveraged tokens and illiquid or short-history coins. Training set 1 January 2020 to 31 December 2021; test set 1 January to 30 June 2022, the start of the "crypto winter".

## Reported results
- AR(7) underperforms HAR; AR(30) is on par with HAR; LSTMs outperform HAR in general.
- The rough-volatility model outperforms HAR, is slightly better than one LSTM variant and close to the others.
- Pooled (universal) models outperform linear models calibrated to each coin.
- Sensitivity to lagged variance is positive and decays with lag, as in equities. Sensitivity to lagged returns is an order of magnitude smaller, decays with lag, and is positive for crypto, whereas the companion equity study found it negative.

## Signal construction
Not a directional signal. Two implementable ideas: (1) train the volatility forecaster on a pooled panel of liquid perps (BTC, ETH, SOL and others), normalising each coin's variance by its own long-run level, then apply it to SOL; (2) include the signed recent return as a feature and let the sign be estimated, because the equity convention (down moves raise volatility) appears reversed.

## Relevance to SOL perpetuals at minutes to hours
Pooling is directly useful: SOL alone offers a short history, and a brand-new Kalshi contract offers almost none. The inverted asymmetry matters for sizing after sharp rallies. Open points: the paper forecasts daily variance, not intraday; the test window is six months in one bear phase; and whether the asymmetry is still inverted in the 2024 to 2026 market with ETF and institutional flows is unknown.

## Caveats
Preprint. Results are presented mainly as boxplots of MSE ratios; no significance tests or economic evaluation were seen in the pages read. A single train/test split. The 213-coin universe is conditioned on survival to mid-2022.
