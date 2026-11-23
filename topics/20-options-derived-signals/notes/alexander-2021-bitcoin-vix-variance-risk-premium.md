---
title: "The Bitcoin VIX and Its Variance Risk Premium"
authors: "Alexander, Carol; Imeraj, Arben"
year: 2021
venue: "The Journal of Alternative Investments"
url: "https://api.openalex.org/works/doi:10.3905/jai.2020.1.112"
pdf: "none"
access: "abstract-only"
source_type: "peer-reviewed"
evidence_grade: "B"
topic: "20-options-derived-signals"
asset_class: "crypto"
horizon: "daily"
tags: "bitcoin-vix, implied-volatility-index, variance-risk-premium, deribit, term-structure, variance-swap"
---

## Key insight
The first construction of a VIX-style implied volatility index for bitcoin from Deribit options, with a term structure from one week to three months sampled every 15 minutes, and the first estimates of the bitcoin variance risk premium. Only the abstract and the journal's "key findings" were read; the accepted manuscript in the University of Sussex repository is under embargo.

## Method
From the abstract: option prices sampled every 15 minutes through the Deribit interface; implied volatility indices built with the variance-swap fair-value formula that the CBOE uses for the VIX; variance risk premia computed against realized variance measured on three sampling grids (15 minutes, hourly, daily). The 30-day realized variance, volatility index and variance risk premium are compared with the same quantities for US equities, oil, gold, USD/EUR and the 10-year US Treasury note.

## Data and sample
Deribit bitcoin calls and puts, "over seven million option prices", March 2019 to March 2020, 15-minute frequency. Index maturities from one week to three months.

## Reported results
Abstract and key findings only:
- The short-maturity bitcoin VIX exceeded 200% after the global outbreak of Covid-19.
- The indices give indicative fair values for bitcoin variance swaps.
- Bitcoin's 30-day realized volatility, volatility index and variance risk premium are correlated with those of the other asset classes, and "diversification potential decreased dramatically after the outbreak of Covid-19".

No premium magnitudes are given in the text read. A later paper summarises this one as finding that the bitcoin variance risk premium "spikes before large positive or negative returns" ([almeida-2024-risk-premia-bitcoin-market](almeida-2024-risk-premia-bitcoin-market.md)); that statement was not checked against the original.

## Signal construction
A model-free implied variance for a fixed horizon, built from out-of-the-money option prices across strikes at two bracketing expiries and interpolated in time, minus realized variance over a matching window. Today the Deribit DVOL index supplies the 30-day implied leg directly ([deribit-2021-dvol-implied-volatility-index](deribit-2021-dvol-implied-volatility-index.md)). The useful extension from this paper is the short end: a one-week index reacts faster than a 30-day one and suits an hours-ahead volatility regime feature better. The exact strike selection and interpolation rules were not read.

## Relevance to SOL perpetuals at minutes to hours
Two things transfer. First, the realized leg depends on the sampling grid, so a premium computed from daily closes differs from one computed from 15-minute returns; the grid has to be fixed before any backtest. Second, the reported rise in correlation with equity volatility after March 2020 supports conditioning crypto volatility features on equity implied volatility. A SOL index of this kind cannot be built reliably from SOL options at current liquidity.

## Caveats
Abstract-only note. One year of data ending in the March 2020 crash, so averages are dominated by a single episode. The publication year is listed as 2020 in the metadata record and cited as 2021 by later papers. A descriptive paper: no test of whether the index or the premium predicts returns.
