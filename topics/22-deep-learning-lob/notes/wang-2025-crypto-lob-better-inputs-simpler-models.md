---
title: "Exploring Microstructural Dynamics in Cryptocurrency Limit Order Books: Better Inputs Matter More Than Stacking Another Hidden Layer"
authors: "Wang, Haochuan (Kevin)"
year: 2025
venue: "arXiv:2506.05764v2"
url: "https://arxiv.org/abs/2506.05764"
pdf: "sources/22-deep-learning-lob/wang-2025-crypto-lob-better-inputs-simpler-models.pdf"
access: "full-text"
source_type: "working-paper"
evidence_grade: "D"
topic: "22-deep-learning-lob"
asset_class: "crypto"
horizon: "seconds"
tags: "bybit, btc-usdt, deeplob, xgboost, logistic-regression, denoising, savitzky-golay, kalman-filter, model-complexity, look-ahead-risk"
---

## Key insight
On Bybit BTC/USDT snapshots, logistic regression and XGBoost match DeepLOB and CNN-LSTM variants at predicting mid-price direction 100 ms to 1 second ahead, at far lower latency. The paper attributes most of the achievable accuracy to preprocessing (smoothing, depth selection, labelling) rather than network depth. The evidence is thin and one preprocessing step looks like it leaks future data, so treat it as a hypothesis that agrees with stronger work, not as proof.

## Method
Six models: logistic regression, XGBoost, CatBoost on CNN embeddings, XGBoost on CNN embeddings, a one-layer CNN plus bidirectional LSTM, and a DeepLOB-style network (three convolution blocks plus LSTM(64), focal loss). Inputs are raw book levels (5, 10 or 40 per side), optionally smoothed feature by feature with a Kalman filter (random-walk state) or a Savitzky-Golay filter (cubic polynomial over a 21-point window written as j = -10..10). Targets are binary (up or down) or ternary (with a flat band tuned for balanced classes) at 100 ms, 500 ms and 1,000 ms. Hand-built features listed include first-level and five-level size imbalance and a weighted mid-price change.

## Data and sample
Bybit public historical BTC/USDT book snapshots at 100 ms with up to 200 levels per side, for a single day (30 January 2025). Main experiments use the first 100,000 snapshots, split 80/20; one experiment uses 1 million snapshots. Snapshots missing any required level are dropped (only 5,442 test rows remain when 40 levels are required).

## Reported results
- Across horizons and filters, Savitzky-Golay smoothing generally improves accuracy and "there is no significant differences across models".
- XGBoost, binary task, smoothed data: accuracy falls from 0.715 with 40 levels (5,442 test rows) to 0.580 with 5 levels (18,336 test rows); requiring deep books raises accuracy while discarding most of the sample.
- Feeding ten consecutive snapshots instead of one adds about 2% accuracy for both XGBoost and logistic regression, at several times the training time.
- Conclusion: adding a convolution layer to a CNN-LSTM did not produce the expected gain; data quality and training method drive performance.

## Signal construction
The cheap version: at each 100 ms snapshot compute I1 = (Qb1 - Qa1)/(Qb1 + Qa1), the same ratio summed over five levels, and a weighted mid-price change; feed these plus raw top levels to logistic regression or gradient-boosted trees to predict the sign of the mid-price change over the next 0.1 to 1 second. Any smoothing must be one-sided (trailing window only).

## Relevance to SOL perpetuals at minutes to hours
Useful mainly as a prompt: before building a deep model on SOL books, check that it beats logistic regression and boosted trees on the same inputs. Bybit's public book archive is a free data source for that test. The sub-second horizons are far below ours.

## Caveats
A centred Savitzky-Golay window uses the next ten observations; the paper does not say the filter was applied causally, and the accuracy gain from smoothing may be look-ahead. One day, one instrument, a single 80/20 split (whether it is chronological is not stated), no walk-forward, no seeds, no significance tests, no costs. Dropping snapshots without full depth is a selection effect whose direction is unknown. Single-author preprint; the text refers to the work as a project. The accuracy tables did not extract cleanly from the PDF, so only numbers quoted in the running text are reported here.
