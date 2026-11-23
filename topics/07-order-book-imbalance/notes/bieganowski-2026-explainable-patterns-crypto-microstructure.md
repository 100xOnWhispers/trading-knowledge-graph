---
title: "Explainable Patterns in Cryptocurrency Microstructure"
authors: "Bieganowski, Bartosz; Slepaczuk, Robert"
year: 2026
venue: "arXiv:2602.00776v1"
url: "https://arxiv.org/pdf/2602.00776"
pdf: "sources/07-order-book-imbalance/bieganowski-2026-explainable-patterns-crypto-microstructure.pdf"
access: "full-text"
source_type: "working-paper"
evidence_grade: "B"
topic: "07-order-book-imbalance"
asset_class: "crypto"
horizon: "seconds"
tags: "order-book-imbalance, binance-futures, perpetual, catboost, shap, tick-size, taker-backtest, flash-crash"
---

## Key insight
On Binance perpetuals, the same small set of top-of-book features (order book imbalance, spread, and buy/sell VWAP-to-mid deviations) dominates 3-second return prediction for five coins of very different size, with similar functional shapes. Imbalance has a monotone effect that flattens at extremes, and its strength rises with relative tick size. A taker backtest is profitable for the smaller coins but not for BTC or LTC, and maker execution of the same signal is not significantly profitable for any coin.

## Method
Gradient-boosted trees (CatBoost) predict the 3-second log mid-price return from engineered features: top-of-book metrics, order book and trade imbalances, VWAP-to-mid deviations. Training uses squared error with model selection by a direction-aware loss (GMADL), walk-forward cross-validation with a purge gap, and Optuna tuning inside the training window. SHAP values on held-out data give feature rankings and dependence curves. Backtests: a taker strategy trading the sign of the forecast above a threshold, filled at best bid/ask and marked to the unfavorable side; and a maker strategy posting at the touch with simulated queue fills.

## Data and sample
Binance Futures perpetual order books and trades at 1-second frequency, 1 January 2022 to 12 October 2025, for BTC, LTC, ETC, ENJ and ROSE (market-cap ranks 1, 20, 40, 60 and 100 at the start). A separate spot versus perpetual comparison uses the asset W.

## Reported results
- Order flow imbalance, spreads and VWAP-to-mid deviations have the largest mean absolute SHAP in every asset; feature rankings are highly rank-correlated across assets.
- Imbalance contribution is larger for instruments with larger relative ticks.
- For W, the position of the finer-tick perpetual mid inside the coarser-tick spot spread has correlation 0.94 with the spot order book imbalance.
- Taker backtest (information ratio, strategy versus buy-and-hold): BTC 0.25 vs 1.87; LTC 0.07 vs 0.62; ENJ 6.58 vs -0.59; ETC 8.97 vs -0.12; ROSE 5.28 vs -0.64. Outperformance is significant at 5% only for ETC, ENJ and ROSE.
- Maker backtest: BTC information ratio 5.47, ENJ -0.77, ETC -0.05, LTC 0.07, ROSE 0.32; none statistically significant.
- The ROSE taker result is described as largely due to the 10 October 2025 flash crash; typical holding times are one to two seconds.
- Latency is not modelled; the authors call the results an upper bound.

## Signal construction
Inputs: 1-second snapshots of best bid/ask price and size plus the trade tape. Features: imbalance `(Q_b - Q_a)/(Q_b + Q_a)`, relative spread, signed trade volume, and `(VWAP_buy - mid)/mid`, `(VWAP_sell - mid)/mid` over the last second(s). Fit a boosted-tree regressor to the next 3-second return with walk-forward retraining; trade only when the absolute forecast exceeds a cost-based threshold.

## Relevance to SOL perpetuals at minutes to hours
The strongest recent evidence that an imbalance feature library is portable across crypto perps, so features built for BTC or ETH should work on SOL without redesign. The tick-size result suggests checking SOL's relative tick on each venue before choosing weights. The horizon is seconds, so for this bot the output is an entry-timing and short-term risk input. The W result supports using a coarse-tick venue's imbalance as a proxy for where the fine price sits, which is relevant if Kalshi's tick is coarse relative to Binance.

## Caveats
Working paper. Whether the tabulated returns include taker fees is not clear from the text read. No latency or queue-position realism at 1-second data. Results for small coins are dominated by a single extreme day. SOL is not in the sample.
