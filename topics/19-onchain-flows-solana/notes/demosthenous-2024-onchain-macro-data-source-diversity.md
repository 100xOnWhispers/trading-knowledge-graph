---
title: "From On-chain to Macro: Assessing the Importance of Data Source Diversity in Cryptocurrency Market Forecasting"
authors: "Demosthenous, Giorgos; Georgiou, Chryssis; Polydorou, Eliada"
year: 2024
venue: "VLDB 2024 Workshop: Foundations and Applications of Blockchain (arXiv:2506.21246)"
url: "https://arxiv.org/pdf/2506.21246"
pdf: "sources/19-onchain-flows-solana/demosthenous-2024-onchain-macro-data-source-diversity.pdf"
access: "full-text"
source_type: "peer-reviewed"
evidence_grade: "C"
topic: "19-onchain-flows-solana"
asset_class: "crypto"
horizon: "daily"
tags: "machine-learning, random-forest, xgboost, feature-importance, shap, on-chain-metrics, stablecoin, usdc, data-diversity"
---

## Key insight
A feature-importance exercise over 429 daily metrics from five categories finds that on-chain metrics, from Bitcoin and from the USDC stablecoin, are the most important category for predicting a broad crypto index at every horizon from 1 to 180 days, and that models improve when categories are combined. Supply-distribution and supply-activity measures dominate; stablecoin flow and supply variables rank among the useful ones.

## Method
- Target: "Crypto100", an index built by the authors from the market capitalisation of the top 100 coins, scaled to be comparable with the Bitcoin price.
- Features: technical indicators (from BTC), on-chain metrics for BTC and for USDC, sentiment and interest metrics, traditional market indices, macroeconomic indicators.
- Feature reduction: a custom algorithm that keeps features ranked highly and persistently across four importance methods: Pearson correlation, mean decrease in impurity, permutation importance and SHAP, computed with Random Forest and XGBoost models tuned by 5-fold cross-validated grid search.
- Evaluation: percentage decrease in mean squared error when a category's features are combined with the others, by prediction window (1, 7, 30, 90, 180 days) and by sample start (2017 or 2019).

## Data and sample
Daily data, January 2017 to June 2023, from Coin Metrics (free API), CoinGecko, the ECB and others. Two sample sets: from 2017 (192 metrics after cleaning) and from 2019 (283 metrics). USDT was deliberately excluded in favour of USDC.

## Reported results
- On-chain metrics are described as of "paramount importance" for both short-term and long-term prediction windows; traditional indices and macro indicators gain importance at longer windows.
- Combining data categories improved the Random Forest model's error by 455.67 percent (2017 set) and 426.67 percent (2019 set) on average under the authors' improvement measure; XGBoost by 399.67 and 468 percent.
- Bitcoin on-chain metrics gained least from being combined with other categories (12.09 and 17.51 percent), which the authors read as on-chain data already containing much of the information.
- Long-term moving averages (EMA100, EMA200) are important even for short windows; USDC inflow and outflow information is flagged as useful.

## Signal construction
Not a signal. It is a feature-selection procedure and a ranking of candidate inputs:
- Compute importance four ways (correlation, impurity, permutation, SHAP) on two tree models and keep only features that rank well under several.
- Repeat per horizon, since rankings change with the prediction window.
- Candidate on-chain inputs it favours: active supply over various look-backs, supply held by address-size bands, stablecoin supply and transfer flows.

## Relevance to SOL perpetuals at minutes to hours
Limited to method. The shortest window is one day, the target is a price level of a market index, and no Solana data are used. What transfers is the practice of ranking flow features with several importance measures and discarding those that are unstable across methods and sample starts, before any of them reach a model. Stablecoin on-chain features deserve a place in the candidate set.

## Caveats
Predicting a price level, not a return, inflates apparent accuracy and makes slow-moving supply variables look important because they trend with price. K-fold cross-validation on time series leaks future information. Improvement figures above 100 percent come from the authors' own measure and are hard to interpret. No trading test, no costs. A workshop paper.
