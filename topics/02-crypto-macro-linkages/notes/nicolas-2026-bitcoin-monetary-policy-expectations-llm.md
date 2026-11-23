---
title: "Is Bitcoin A Hedge Against Central Banking? Evidence from AI-Driven Monetary Policy Expectations"
authors: "Nicolas, Maxime L. D.; Sicard, Francois; Laboure, Marion; Sun, Zixin; Rodriguez-Martinez, Anahi"
year: 2026
venue: "arXiv 2604.08825 (v2, August 2026)"
url: "https://arxiv.org/pdf/2604.08825"
pdf: "sources/02-crypto-macro-linkages/nicolas-2026-bitcoin-monetary-policy-expectations-llm.pdf"
access: "full-text"
source_type: "working-paper"
evidence_grade: "B"
topic: "02-crypto-macro-linkages"
asset_class: "crypto"
horizon: "multi-day"
tags: "machine-learning, lstm, shap, llm-sentiment, monetary-policy-expectations, granger-causality, feature-importance"
---

## Key insight
An LLM-built weekly index of hawkish versus dovish monetary-policy talk on social media carries some linear predictive information for Bitcoin returns at lags of two to six weeks. Inside an LSTM with 18 macro-financial inputs, the index ranks sixth of nineteen features by SHAP importance, behind Google searches for inflation, the fed funds rate and gold. The LSTM's out-of-sample forecast accuracy is not statistically better than ARIMA, which the authors state plainly; the model is used for interpretation, not as a forecasting system.

## Method
- Monetary Policy Expectations (MPE) index: 118,562 StockTwits messages tagged $FED and $MACRO, September 2014 to March 2025, classified by an open-weight 7-billion-parameter LLM (Qwen2.5-7b, run locally through ollama) on a five-point scale from very hawkish (-2) to very dovish (+2); weekly weighted average. Validated against 1,095 hand-labelled messages.
- Granger causality tests (lags 1 to 6) of Bitcoin returns on differenced MPE and other indicators, plus a variational mode decomposition to test by frequency band.
- LSTM on weekly data with expanding-window walk-forward evaluation in four folds (training anchored in September 2014, each with a 12-month out-of-sample test set), compared with ARIMA using Diebold-Mariano tests.
- SHAP values averaged across folds, runs and lags for global and lag-specific feature importance.

## Data and sample
Weekly, September 2014 to March 2025. Eighteen macro-financial indicators in three groups (macro conditions, monetary policy and financial conditions, global risk and sentiment), including S&P 500, jobless claims, fed funds rate, 5-year inflation expectations, gold, Google Trends for inflation and recession, and a news sentiment index.

## Reported results
- Granger tests: changes in MPE predict Bitcoin returns at lags 2, 3, 5 and 6 (p below 0.10), at 5 percent for lags 2 and 5. The S&P 500 and the fed funds rate do not Granger-cause Bitcoin returns. Gold is significant at lags 1 to 5; Google searches for recession at all lags.
- Forecasting: mean one-step RMSE 0.0850 for the LSTM against 0.0873 for ARIMA, a 2.6 percent reduction; lower in two of four folds. Diebold-Mariano differences are insignificant in the first three folds; in the fourth the difference is significant (p = 0.016) but ARIMA is the better model.
- Adding MPE to ARIMA lowers pooled RMSE from 0.0902 to 0.0895.
- SHAP ranking: Google inflation searches first, fed funds rate second, then gold, Google recession searches and 5-year inflation expectations; MPE sixth with mean absolute SHAP 0.003. News sentiment and jobless claims rank last in every fold.
- Importance is concentrated at the current week's lag.
- Hawkish narratives are associated with negative Bitcoin responses not accounted for by realized rate changes.

## Signal construction
Weekly hawk-dove index: collect policy-tagged messages, classify each with a small local LLM on the five-point scale, take the engagement-weighted weekly mean (the paper's index is oriented so that higher means more dovish), and use its first difference as a feature. The same pipeline could run daily or hourly on a news or social feed around FOMC speeches. The paper gives the prompt and code repository (github.com/maximenc/Bitcoin-Monetary-Policy-Expectations, not opened).

## Relevance to SOL perpetuals at minutes to hours
This is the machine-learning entry for this topic and its lesson is sobering: with a decade of weekly data, a tuned LSTM on macro features barely matches a univariate ARIMA. Macro features are better used as low-dimensional regime context than as inputs to a high-capacity return forecaster. The LLM classification idea transfers to intraday use (scoring Fed speaker headlines in real time), but that was not tested. Bitcoin only, weekly only.

## Caveats
Predictive gains are small and mostly insignificant. Granger results at the 10 percent level across six lags and many variables invite multiple-testing concerns. StockTwits users are a narrow retail population; one author is at Deutsche Bank. Four folds with one year each is a thin out-of-sample record. SHAP importance in an under-performing model shows what the model uses, not what drives prices.
