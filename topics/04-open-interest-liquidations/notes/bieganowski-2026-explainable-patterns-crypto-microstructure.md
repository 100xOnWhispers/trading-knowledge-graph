---
title: "Explainable Patterns in Cryptocurrency Microstructure"
authors: "Bieganowski, Bartosz; Slepaczuk, Robert"
year: 2026
venue: "arXiv preprint 2602.00776"
url: "https://arxiv.org/pdf/2602.00776"
pdf: "sources/04-open-interest-liquidations/bieganowski-2026-explainable-patterns-crypto-microstructure.pdf"
access: "full-text"
source_type: "working-paper"
evidence_grade: "B"
topic: "04-open-interest-liquidations"
asset_class: "crypto"
horizon: "seconds"
tags: "machine-learning, catboost, shap, october-2025, flash-crash, taker-vs-maker, adverse-selection"
---

## Key insight
A gradient-boosted model trained on order-book and trade features of Binance perpetuals is stress-tested through the 10 October 2025 liquidation cascade. The same signal produced opposite outcomes depending on execution style: a liquidity-taking version shorted into the collapse and profited, while a passive market-making version was filled repeatedly on the bid and suffered large losses. For this topic the paper's value is as evidence of how a machine-learning strategy behaves inside a cascade; its feature analysis belongs with the order-flow literature.

## Method
CatBoost regression with a direction-aware GMADL objective predicts the 3-second log mid-price return from engineered features: top-of-book metrics, order-book imbalance, trade flow and VWAP-to-mid deviations, kept in scale-free ratio form. Evaluation uses rolling walk-forward cross-validation with a purge gap between training and validation, hyperparameters tuned only inside the training window, and SHAP for feature attribution. Two back-tests share the signal: a taker test (enter when the absolute prediction exceeds a threshold, buy at ask and sell at bid, inventory marked to the unfavorable side) and a maker test (post passive quotes at the touch). Latency is not modelled.

## Data and sample
Binance Futures perpetuals for BTC, LTC, ETC, ENJ and ROSE (market-cap ranks 1, 20, 40, 60 and 100 at the start), order book and trades at 1-second frequency, 1 January 2022 to 12 October 2025. Open interest and liquidation data are not used as features.

## Reported results
- Feature rankings and SHAP dependence shapes are reported as stable across the five assets.
- Taker back-test annualized return on capital: BTC 0.13, ENJ 4.06, ETC 5.78, LTC 0.07, ROSE 7.00; maximum drawdown 0.24 to 0.64. Mean returns differ significantly from buy-and-hold only for ETC, ENJ and ROSE.
- Maker back-test: BTC 2.93, ENJ -0.81, ETC -0.07, LTC 0.10, ROSE 0.27; no asset is significant.
- On 10 October 2025 the taker model's predictions reached levels far outside their normal range and it held a short for about 20 seconds, roughly ten times its usual one-to-two-second holding period, with a significant profit.
- The maker strategy accumulated a growing long position as bids were hit with no offsetting ask fills, with equity collapsing around 23:20 on the chart (time zone not stated).
- A single large shallow bid at about 23:27 triggered a sharp upward prediction, which the authors flag as a manipulation risk.

## Signal construction
For cascade handling specifically: monitor the model's own prediction magnitude relative to its historical distribution. Values far outside the usual range identify an abnormal regime in which (a) passive quoting should be withdrawn or widened and (b) directional taking has positive expectancy only if latency and spread costs are survivable. The underlying alpha signal is order-book imbalance at seconds horizon, covered in the order-flow topic.

## Relevance to SOL perpetuals at minutes to hours
The lesson transfers even though the horizon and assets differ: a directional bot that also rests passive orders must have a cascade switch, because adverse selection on resting orders is what destroyed the maker variant. The taker profit should be treated as an upper bound, since spreads on Hyperliquid majors reached tens of basis points at the peak (see the Lim note) and the back-test does not model latency or venue disruption. SOL is not in the sample. On Kalshi, thinner books make the resting-order risk larger.

## Caveats
Back-test without latency, queue position or outage modelling, and the authors state results are an upper bound. The flash-crash analysis is a single event shown through charts, not a statistical test. Extreme annualized returns on small-cap contracts are unlikely to be capturable at size. The model was trained on data ending two days after the event, so the crash is near the end of the sample.
