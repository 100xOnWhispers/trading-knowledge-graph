---
title: "Risk Premia in the Bitcoin Market"
authors: "Almeida, Caio; Grith, Maria; Miftachov, Ratmir; Wang, Zijin"
year: 2024
venue: "arXiv preprint 2410.15195 (v2, August 2025)"
url: "https://arxiv.org/abs/2410.15195"
pdf: "sources/20-options-derived-signals/almeida-2024-risk-premia-bitcoin-market.pdf"
access: "full-text"
source_type: "working-paper"
evidence_grade: "B"
topic: "20-options-derived-signals"
asset_class: "crypto"
horizon: "multi-day"
tags: "variance-risk-premium, risk-neutral-density, clustering, volatility-regime, pricing-kernel, deribit, unsupervised-learning"
---

## Key insight
Bitcoin's one-month variance risk premium is large (0.14 in annualised variance units, against roughly 2% for the S&P 500 in the study the authors cite) and it is higher in calm markets than in volatile ones. Across the two volatility regimes the paper identifies, the return premium and the variance premium move in opposite directions, the reverse of the positive relation reported for US equities by [Bollerslev and Zhou](bollerslev-2007-expected-stock-returns-variance-risk-premia.md). Upside states carry far more of the bitcoin premium than they do for equities.

## Method
Risk-neutral densities are estimated non-parametrically from option prices (Breeden and Litzenberger) for 27-day maturity, interpolating between neighbouring expiries. The return premium is the physical mean minus the risk-neutral mean of the return; the variance risk premium is risk-neutral variance minus physical variance. The return premium is decomposed across return states following Beason and Schreindorfer (2022). Regimes come from an unsupervised step: a functional-data clustering algorithm applied to the daily densities, using implied volatility curves at 9, 27 and 45 days. Lower bounds on the return premium follow Martin (2017) and Chabi-Yo and Loudis (2020).

## Data and sample
Deribit transaction-level bitcoin options, July 2017 to December 2022, and daily bitcoin prices from 2014. The text reports 1,992 days and 5,384,537 transactions after filtering, while the note to Table 1 reports 1,301 days and 7,832,590 transactions; the two counts are not reconciled in the pages read.

## Reported results
- Return premium about 66% a year; variance risk premium 0.14 (risk-neutral variance 0.72, physical 0.58); annualised Sharpe ratio about 0.8.
- High-volatility cluster: variances 0.86 and 0.74, premium 0.12. Low-volatility cluster: 0.46 and 0.29, premium 0.17.
- Returns between 20% and 60% account for 39% of the return premium overall and about 52% in the low-volatility regime; in the high-volatility regime large positive and large negative returns contribute about equally (about 30% each).
- Negative returns between one and three standard deviations account for only one third of the premium, whereas mildly negative returns account for most of the S&P 500 premium.
- The pricing kernel is hump-shaped in both regimes, more so when volatility is low. The right wing of the implied volatility curve is steeper in the low-volatility regime.

## Signal construction
Not a short-horizon signal. It supplies a regime variable and a caution:
1. Regime label: cluster the daily implied volatility curves (or simply threshold a 30-day implied variance) into high and low volatility states.
2. Variance premium level: squared 30-day implied volatility minus trailing realized variance, read conditionally on the regime because the premium is larger when volatility is low.
3. Do not import the equity rule "high variance premium, high future return" into crypto without testing; the regime averages here point the other way.

## Relevance to SOL perpetuals at minutes to hours
The regime label, built from BTC options, is a slow conditioning variable for a SOL model: position sizing, stop distances and the choice between momentum and reversal rules can depend on it. The finding that upside tails are priced heavily in calm markets suggests that call-side skew in bitcoin is a normal state, not by itself a bullish signal. Nothing here is tested on SOL or at intraday horizons.

## Caveats
Two regimes estimated on one sample, with no out-of-sample classification test. The negative relation between return and variance premia rests on two cluster averages, not on a predictive regression. The sample ends in December 2022, before spot ETFs and listed ETF options changed who trades bitcoin volatility. Return premium estimates are noisy by the authors' own account.
