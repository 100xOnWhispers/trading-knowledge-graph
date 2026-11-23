---
title: "Explainable Patterns in Cryptocurrency Microstructure"
authors: "Bieganowski, Bartosz; Slepaczuk, Robert"
year: 2026
venue: "arXiv 2602.00776v1 (January 2026)"
url: "https://arxiv.org/pdf/2602.00776"
pdf: "sources/08-trade-flow-toxicity/bieganowski-2026-explainable-patterns-crypto-microstructure.pdf"
access: "full-text"
source_type: "working-paper"
evidence_grade: "C"
topic: "08-trade-flow-toxicity"
asset_class: "crypto"
horizon: "seconds"
tags: "machine-learning, gradient-boosting, shap, trade-imbalance, vwap-deviation, perpetuals, adverse-selection, flash-crash"
---

## Key insight
A single gradient-boosted tree pipeline on a small set of top-of-book and trade-flow features predicts 3-second mid-price returns on five Binance perpetuals of very different size, and the ranking and shape of feature effects (from SHAP) are nearly the same across assets. Flow imbalance has a monotone effect that flattens at extremes, wide spreads weaken predictability, and deviations of buy and sell VWAP from mid show asymmetric, mean-reverting effects. During the 10 October 2025 crash the taker version of the strategy profited while the maker version was run over by one-sided flow.

## Method
Features: spread and relative prices, level-1 volumes, order book imbalance, net traded volume and signed trade flow, and deviations of buy-trade and sell-trade VWAP from mid, all in relative units. Target: log mid-price return over the next 3 seconds. Model: CatBoost trained with a direction-aware loss (Generalized Mean Absolute Directional Loss) and with squared error as a baseline, hyperparameters tuned by Optuna inside training folds only, evaluated by walk-forward cross-validation with a purge gap. Explanations: TreeSHAP on held-out samples; Spearman correlation of mean absolute SHAP across assets. Backtests: a taker strategy that trades when |prediction| exceeds a threshold, buying at ask and selling at bid with inventory marked to the unfavorable side; and a maker strategy posting at the touch with simulated queue priority.

## Data and sample
Binance Futures perpetual order books and trades at 1-second frequency for BTC, LTC, ETC, ENJ and ROSE (market-cap ranks 1, 20, 40, 60 and 100 at the start), 1 January 2022 to 12 October 2025.

## Reported results
- Order flow or book imbalance, spreads and VWAP-to-mid deviations dominate mean absolute SHAP for every asset; importance rankings are highly rank-correlated across assets.
- The imbalance effect is stronger for instruments with larger relative tick size.
- Taker backtest annualized return on capital: BTC 0.13, LTC 0.07, ENJ 4.06, ETC 5.78, ROSE 7.00, against buy-and-hold of 0.83, 0.53, -0.67, -0.10 and -0.71; information ratios 0.25, 0.07, 6.58, 8.97 and 5.28.
- Maker backtest: BTC 2.93 annualized return, the other four between -0.81 and 0.27.
- Typical taker trades last one to two seconds. In the 10 October 2025 crash the BTC taker model held a short for about 20 seconds and profited; the maker strategy accumulated a long position as its bids were repeatedly hit and took large losses.

## Signal construction
Per second, from top-of-book and the trade stream: spread / mid; (bid size - ask size) / (bid size + ask size); net signed traded volume over the last second and trailing windows; (buy VWAP - mid) / mid and (sell VWAP - mid) / mid. Train a boosted-tree regressor on the next 3-second mid return with walk-forward refits; act only when the prediction exceeds a threshold set relative to spread and fees.

## Relevance to SOL perpetuals at minutes to hours
The cross-asset stability supports training one flow-feature model on several liquid perps and applying it to SOL without bespoke feature engineering. The VWAP-to-mid deviation of buys and sells is a trade-tape feature worth adding to a SOL feature set. The 3-second horizon is far from the bot's, so this is evidence about which features carry information, not about tradable edge at minutes to hours. The crash episode is a concrete warning for any passive entry logic on SOL: resting bids are adversely selected exactly when flow becomes one-sided.

## Caveats
Latency is not modelled and the authors say results are an upper bound in the fastest regime; small-cap information ratios above 5 at one-to-two-second holding periods are not credible as achievable returns. The paper's top feature is order book imbalance, which belongs to topic 07; the contribution of trade-flow features alone is not isolated. The text says gross and fee-adjusted returns are reported, but it was not clear from the tables read which columns are net of taker fees. SOL is not in the sample. Unrefereed.
