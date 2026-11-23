---
title: "Cross-cryptocurrency return predictability"
authors: "Guo, Li; Sang, Bo; Tu, Jun; Wang, Yu"
year: 2024
venue: "Journal of Economic Dynamics and Control 163, 104863"
url: "https://ideas.repec.org/a/eee/dyncon/v163y2024ics0165188924000551.html"
pdf: "none"
access: "abstract-only"
source_type: "peer-reviewed"
evidence_grade: "B"
topic: "21-cross-asset-lead-lag"
asset_class: "crypto"
horizon: "n/a"
tags: "cross-predictability, lagged-returns, adaptive-lasso, pca, machine-learning, long-short, binance, slow-information-diffusion"
---

## Key insight
Lagged returns of other cryptocurrencies predict the return of a given coin, on Binance data, and the predictability survives penalized variable selection and factor extraction. The authors attribute it to slow diffusion of information: common shocks hit many coins, and investors with limited attention do not update all prices at once. This is the main peer-reviewed statement that cross-coin lead-lag exists and is economically meaningful after costs.

## Method
From the abstract only: predictive regressions of a focal coin's return on the lagged returns of other coins, estimated with several methods "notably the adaptive LASSO and principal component analysis". A long-short portfolio sorted on forecasts built from past cross-coin returns is evaluated out of sample net of transaction costs. The return frequency, the lag structure, the number of coins and the sample period are not stated in the abstract and were not confirmed.

## Data and sample
Binance data. Frequency, universe and dates: not confirmed (abstract-only). The Bristol repository lists an open accepted manuscript (CC BY), but the file could not be downloaded in this session because of bot protection, and the publisher version is paywalled.

## Reported results
Only what the abstract states:
- "Strong evidence" of cross-cryptocurrency return predictability.
- Lagged returns of other cryptocurrencies are significant predictors of focal coins.
- Results hold under adaptive LASSO and PCA.
- A long-short portfolio formed on past returns of cryptocurrencies earns a sizable out-of-sample return after transaction costs. The published abstract gives no number.
- Interpretation: a spillover mechanism, with common shocks and limited investor attention producing slow information diffusion across coins.

A search-result snippet describing the 2021 working-paper version mentioned an out-of-sample daily long-short return of 2.16% after costs; that page was not opened, so the figure is unverified and is recorded here only as a lead.

## Signal construction
Generic form implied by the abstract: for target coin i at time t, regress r_i(t+1) on r_j(t) for all other coins j, selecting predictors with adaptive LASSO (LASSO with weights from an initial OLS or ridge fit), or regress on the first few principal components of the lagged cross-section. Refit on a rolling window. For a single-target bot the forecast for SOL is the fitted value; the paper's portfolio is cross-sectional (long high forecasts, short low forecasts). Parameters must be taken from the full text before implementation.

## Relevance to SOL perpetuals at minutes to hours
Supports including lagged returns of a broad set of coins, not only BTC, as candidate predictors of SOL, with sparse selection. Whether it applies at minutes to hours depends on the paper's frequency, which is unknown here. It must be read alongside the Jia, Wu, Yan and Liu note, which finds the intraday cross-predictive sign from large coins is negative, and the Kurihara and Matsumoto note, which finds no one-minute BTC lead for liquid coins.

## Caveats
Abstract-only: no numbers, frequency or sample confirmed. Cross-sectional long-short results in crypto are often driven by small, illiquid coins that cannot be shorted at the assumed cost. An earlier version had a different author list according to a catalogue snippet (not verified). The grade is held at B because the full text was not read.
