---
title: "Explainable Patterns in Cryptocurrency Microstructure"
authors: "Bieganowski, Bartosz; Slepaczuk, Robert"
year: 2026
venue: "arXiv:2602.00776v1 (University of Warsaw, Faculty of Economic Sciences)"
url: "https://arxiv.org/pdf/2602.00776"
pdf: "sources/23-ml-feature-prediction/bieganowski-2026-explainable-patterns-crypto-microstructure.pdf"
access: "full-text"
source_type: "working-paper"
evidence_grade: "B"
topic: "23-ml-feature-prediction"
asset_class: "crypto"
horizon: "seconds"
tags: "catboost, shap, feature-importance-stability, binance-perpetuals, order-flow-imbalance, walk-forward, purging, taker-backtest, flash-crash"
---

## Key insight
One gradient-boosted tree pipeline, with the same engineered top-of-book and trade-flow features, learns nearly the same feature ranking and the same response shapes on five Binance perpetuals spanning a tenfold range of market capitalisation. Order-flow imbalance, spread and VWAP-to-mid deviation dominate everywhere. This supports building one portable, scale-free feature library for all crypto perps instead of per-asset feature engineering, and it is a recent worked example of walk-forward validation with a purge gap and inner-loop tuning.

## Method
Target: the 3-second log return of the mid price. Features: top-of-book measures (spread, level-1 volumes), order-flow and trade imbalance, and deviations of buy and sell VWAP from the mid; relative measures are preferred so effects are comparable across assets, and features are left unscaled because trees are invariant to monotone transforms. Model: CatBoost, hyperparameters tuned with Optuna (TPE) using inner time-series cross-validation inside each training window. Evaluation uses rolling walk-forward folds with a temporal gap between training and validation. Models are trained with squared error and selected by the Generalized Mean Absolute Directional Loss (GMADL), which rewards correct sign in proportion to the size of the realised move. Attribution uses TreeSHAP on held-out samples; cross-asset agreement is measured by Spearman rank correlation of mean absolute SHAP. Two backtests: a taker test (buy at ask, sell at bid, inventory marked to the unfavourable side, threshold on forecast size; the paper says it reports gross and fee-adjusted returns, and I could not confirm which the summary tables show) and a maker test with simulated queue fills.

## Data and sample
Binance Futures perpetuals, order book and trades at 1-second frequency, 1 January 2022 to 12 October 2025, for BTC, LTC, ETC, ENJ and ROSE (market-cap ranks 1, 20, 40, 60 and 100 at the start).

## Reported results
- The same feature families top the SHAP ranking for every asset, and SHAP dependence shapes match: imbalance has a monotone effect that flattens at extremes; wider spreads weaken predictability.
- The imbalance effect is stronger for assets with larger relative tick size. A spot and perp comparison on one asset shows the finer-tick perp mid's position within the spot spread correlates 0.94 with spot book imbalance.
- Taker backtest, annualised return and information ratio: BTC 0.13 and 0.25 (buy-and-hold 0.83 and 1.87); ENJ 4.06 and 6.58; ETC 5.78 and 8.97; LTC 0.07 and 0.07; ROSE 7.00 and 5.28. Taker results are significantly different from buy-and-hold at 5% only for ETC, ENJ and ROSE.
- Maker backtest: BTC 2.93 and 5.47, but ENJ -0.81, ETC -0.07; no maker result is statistically significant.
- The ROSE taker result is "largely due to the extreme event" of 10 October 2025, when the model shorted into the crash; the maker variant lost in the same event.
- Latency is not modelled; the authors call the taker results "an upper bound in the fastest regime".

## Signal construction
Per second compute spread over mid, level-1 size imbalance, signed trade-flow imbalance over short windows, and buy-VWAP and sell-VWAP minus mid, all in relative units. Fit a boosted-tree regressor to the forward mid return with walk-forward folds and a purge gap, select by a direction-weighted loss, and act only when the absolute forecast exceeds a threshold. Monitor SHAP rankings fold by fold; a change in ranking or sign is a drift alarm.

## Relevance to SOL perpetuals at minutes to hours
The horizon is far shorter than the bot's and the trading results need colocation-grade speed, so the profit figures do not transfer. What transfers is the method: relative-unit features that port across assets (so a model can be trained on Binance SOL or pooled perps and its inputs computed for Kalshi), SHAP stability as a model-health check, a direction-aware selection metric, and the finding that on the most liquid asset (BTC) the taker edge is not distinguishable from buy-and-hold. Whether the same features retain rank at 1 to 60 minute horizons is untested.

## Caveats
Preprint, one model family, one venue, one horizon. No latency or queue-position realism for takers; maker fills are simulated. Large reported returns on small-cap perps are probably capacity-limited. The model is selected by in-sample GMADL after squared-error training, which is an unusual hybrid. Detailed microstructure interpretation belongs to topics 07 and 22.
