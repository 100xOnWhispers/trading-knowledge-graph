---
title: "Cross-Impact of Order Flow Imbalance in Equity Markets"
authors: "Cont, Rama; Cucuringu, Mihai; Zhang, Chao"
year: 2023
venue: "Quantitative Finance (read as arXiv:2112.13213v4, June 2023)"
url: "https://arxiv.org/pdf/2112.13213"
pdf: "sources/07-order-book-imbalance/cont-2023-cross-impact-order-flow-imbalance.pdf"
access: "full-text"
source_type: "peer-reviewed"
evidence_grade: "A"
topic: "07-order-book-imbalance"
asset_class: "equities"
horizon: "minutes"
tags: "order-flow-imbalance, multi-level-ofi, integrated-ofi, cross-impact, lasso, forecasting, horizon-decay"
---

## Key insight
Combining OFI from the top ten book levels into one "integrated OFI" (first principal component) explains contemporaneous returns much better than best-level OFI. Once that is done, other assets' OFIs add nothing to the contemporaneous fit. For forecasting, the picture reverses: lagged cross-asset OFIs do improve one-minute-ahead predictions, but the edge decays quickly with horizon.

## Method
Level-m order flow is computed as in Cont, Kukanov and Stoikov, then scaled by average depth across the first M = 10 levels. Integrated OFI is `ofi_I = w1' ofi / ||w1||_1`, where `w1` is the first principal vector of the 10-level OFI vector estimated on historical data. Contemporaneous models (own-asset "PI", cross-asset "CI" with LASSO) are fitted on rolling windows and tested on the following 30 minutes. Forecasting models regress the next f-minute return on lagged OFIs over lags of 1, 2, 3, 5, 10, 20 and 30 minutes, with own-asset (FPI) and cross-asset (FCI) versions and return-based benchmarks (AR, CAR). A forecast-implied portfolio trades only when the forecast exceeds the relative spread.

## Data and sample
Nasdaq ITCH data from LOBSTER for the top 100 S&P 500 constituents, January 2017 to December 2019, one-minute bars built from event data.

## Reported results
- The first principal component explains over 89% of the variance of multi-level OFIs.
- In-sample adjusted R2 for contemporaneous returns: 71.16% with best-level OFI, 87.14% with integrated OFI. Adding cross-asset terms raises the integrated model only to 87.85%.
- Out of sample, best-level cross-impact gives 66.03% against 64.64% without it; with integrated OFI the cross terms add no explanatory power.
- One-minute-ahead forecasts: out-of-sample R2 is negative for every model (about -0.37 for own-asset models and -0.10 for cross-asset models, units as printed in the paper's table), yet the forecast-implied strategies have positive annualized PnL: 0.21 (FPI) against 0.43 (FCI) with best-level OFI, 0.23 against 0.39 with integrated OFI. Trading costs are ignored.
- Over horizons from 1 to 30 minutes, the PnL of cross-asset models falls faster than that of own-asset models.
- For forecasting, integrated OFI does not significantly beat best-level OFI.

## Signal construction
Per instrument and per minute: compute OFI at levels 1 to 10, divide by average depth over those levels, project on PCA weights estimated on a trailing window. For cross-asset use, stack lagged OFIs of related instruments (for SOL: BTC, ETH, and SOL on other venues) and fit a sparse (LASSO) regression of next-interval return, refitting frequently. Trade only when the forecast exceeds the cost threshold.

## Relevance to SOL perpetuals at minutes to hours
This is the closest classic evidence for the bot's horizon: one-minute bars and forecasts out to 30 minutes. The cross-asset finding maps onto crypto, where BTC and ETH flow and the same asset on larger venues plausibly lead a small venue. Expect the lagged effect to be much shorter in crypto than the minutes found in 2017 to 2019 equities, since venues are linked by fast arbitrage. The negative out-of-sample R2 alongside positive PnL is a reminder to judge by strategy outcome with costs.

## Caveats
Costs are excluded from the PnL figures. Stocks only, pre-2020. LASSO cross-impact coefficients are unstable. The predictive edge is small and may have decayed since publication.
