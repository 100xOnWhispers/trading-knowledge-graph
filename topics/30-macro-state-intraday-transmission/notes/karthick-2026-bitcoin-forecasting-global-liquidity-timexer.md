---
title: "Expert System for Bitcoin Forecasting: Integrating Global Liquidity via TimeXer Transformers"
authors: "Karthick T, Sravan; A, Rakshita; Moharir, Minal"
year: 2026
venue: "arXiv preprint 2512.22326, version 2 (11 January 2026)"
url: "https://arxiv.org/pdf/2512.22326"
pdf: "sources/30-macro-state-intraday-transmission/karthick-2026-bitcoin-forecasting-global-liquidity-timexer.pdf"
access: "full-text"
source_type: "working-paper"
evidence_grade: "C"
topic: "30-macro-state-intraday-transmission"
asset_class: "crypto"
horizon: "multi-day"
tags: "global-liquidity, m2, transformer, exogenous-variable, ablation, bitcoin, long-horizon-forecast, machine-learning"
---

## Key insight
A transformer that takes lagged global M2 as an exogenous input forecasts the Bitcoin price better than the same model without it at horizons of a month or more, and no better at one to three weeks. Read as an ablation, the result says a slow liquidity series adds nothing at the horizons a minutes-to-hours bot trades, and whatever it adds at ten weeks rests on a single 120-day test window.

## Method
TimeXer (patch-wise self-attention on the target series plus cross-attention to exogenous variates) is trained to forecast the daily Bitcoin price level. The exogenous variant, TimeXer-Exog, receives a global liquidity series, M2 aggregated across 18 economies after conversion to US dollars at daily exchange rates, shifted forward 12 weeks and entered as a dense set of lags from 1 to 98 days (the 12-week lead is illustrated with a chart of standardised series). Baselines: TimeXer without the exogenous input, PatchTST, N-BEATS and LSTM. Hyperparameters are tuned on a validation window. Evaluation is mean squared error by horizon (7 to 70 days) with the model confidence set of Hansen et al., using a block bootstrap with block length equal to the horizon and a 10 percent level.

## Data and sample
Daily Bitcoin prices, January 2020 to August 2025 (entirely post-2020). Training to 23 September 2024, validation 24 September 2024 to 21 January 2025, test on the final 120 daily observations, 22 January to 21 May 2025. Bitcoin only. No intraday data, no altcoins or SOL.

## Reported results
- At the 70-day horizon TimeXer-Exog has mean squared error 10.814 (scaled by 10^7 in the paper), more than 89 percent lower than univariate TimeXer.
- At 7 to 14 days, price-only models do well and PatchTST beats TimeXer-Exog. At 14 and 21 days the confidence set contains TimeXer-Exog, TimeXer and LSTM, so they are statistically indistinguishable; the authors state that adding global liquidity does not help much in these windows.
- From 28 days onward TimeXer-Exog has the lowest error.
- The authors cite other work for a long-run elasticity of Bitcoin to M2 of 2.65 and note that the relationship is not perfectly stable.

## Signal construction
If used at all, as a slow bias: global M2 in dollars (sum over major economies converted at spot), lagged roughly 10 to 14 weeks, as one input to a multi-week directional view. The paper gives no rule for turning the forecast into positions, no directional accuracy and no trading result.

## Relevance to SOL perpetuals at minutes to hours
This is the kind of evidence usually cited for the claim that liquidity leads crypto by about three months, in machine-learning form. For this bot it is mainly a negative result: at any horizon under a month the liquidity input is not distinguishable from noise, so it should not be an intraday feature. At most it could inform a weekly risk budget, and that would need the stable-sign and out-of-sample checks this paper does not provide.

## Caveats
One test window of 120 days in early 2025, during which a 70-day forecast has very few independent observations. Targets are price levels, where a model that tracks the trend scores well on squared error without predicting returns. The 12-week shift is motivated by a full-sample chart and cited studies; if it was chosen on data that include the test window, that is look-ahead in the design even though inputs are lagged. The national M2 series are converted to dollars at daily exchange rates, so the aggregate moves mechanically with the dollar and partly proxies for the exchange rate. No discussion of publication lags or data vintages for M2 was seen. Preprint, not peer reviewed; no sign-stability or subsample analysis.
