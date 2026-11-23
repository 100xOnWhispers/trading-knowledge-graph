---
title: "Markov-switching Asset Allocation: Do Profitable Strategies Exist?"
authors: "Bulla, Jan; Mergner, Sascha; Bulla, Ingo; Sesboüé, André; Chesneau, Christophe"
year: 2010
venue: "MPRA Paper 21154 (IDEAS lists a later version in Journal of Asset Management 12(5), 2011)"
url: "https://mpra.ub.uni-muenchen.de/21154/1/MPRA_paper_21154.pdf"
pdf: "sources/01-macro-regime-detection/bulla-2010-markov-switching-asset-allocation-profitable.pdf"
access: "full-text"
source_type: "working-paper"
evidence_grade: "B"
topic: "01-macro-regime-detection"
asset_class: "equities"
horizon: "daily"
tags: "hidden-markov-model, volatility-regime, rolling-window, median-filter, transaction-costs, out-of-sample, de-risking"
---

## Key insight
A deliberately simple test of whether a two-state hidden Markov model on daily index returns is tradable after costs. Moving to cash whenever the model predicts the high-variance state cut volatility by about 41% on average across five equity indices and slightly raised returns, out of sample and net of 10 basis points per trade. The gain is risk reduction; the return pick-up is small. A median filter on the predicted state was needed to keep turnover down.

## Method
Two-state HMM fitted to daily returns on a rolling window of n = 2000 observations (about eight years). At each day t: fit the model, compute the Viterbi path, and get the one-step-ahead state from the last decoded state and the transition matrix. The predicted state sequence is then smoothed with a median filter of lag k = 6 (current and five past predictions): `s_filtered(t+1) = median(s(t-k+2), ..., s(t+1))`. Strategy: hold the index in the low-variance state, hold a riskless asset at 3% per year in the high-variance state. One-way cost 10 bp.

## Data and sample
Daily returns of the DAX, DJIA and S&P 500 from January 1976, Nikkei 225 from January 1983 and NASDAQ 100 from October 1985; the sample end is not stated in the sections I extracted (the introduction refers to "the last four decades"). Out-of-sample forecasts number between 3,383 (NASDAQ) and 5,834 (S&P 500).

## Reported results
Out of sample, net of costs (index versus strategy; annualised mean %, standard deviation %, Sharpe):
- DAX: 7.24 / 22.0 / 0.292 versus 7.76 / 13.0 / 0.437, 84 transitions.
- DJIA: 8.93 / 16.8 / 0.417 versus 9.82 / 11.2 / 0.646, 60 transitions.
- NASDAQ: 6.82 / 32.0 / 0.272 versus 8.63 / 14.0 / 0.464, 31 transitions.
- Nikkei: -4.30 / 22.6 versus -2.28 / 13.9, 89 transitions.
- S&P 500: 8.37 / 16.5 / 0.390 versus 8.56 / 10.3 / 0.577, 46 transitions.

Annual excess return ranged from 18.5 bp (S&P 500) to 201.6 bp (Nikkei). The median filter cut state changes from 188 to 84 (DAX), 207 to 89 (Nikkei) and 134 to 46 (S&P 500). In-sample results were much stronger than out-of-sample.

## Signal construction
Inputs: return series only. Per bar: refit (or periodically refit) a two-state HMM on the trailing window, decode, predict the next state, apply a k-bar median filter, then set exposure to 1 in the calm state and 0 (or reduced) in the turbulent state. Parameters to tune: window length, filter length k, refit cadence.

## Relevance to SOL perpetuals at minutes to hours
This is a volatility-avoidance overlay, not a directional signal: it never goes short. For a directional perp bot it is a candidate gate ("trade smaller or stand aside in the turbulent state"). The median filter is the transferable trick, and its lag is the price. A 10 bp cost per switch is of the same order as taker fees plus spread on large perp venues (my assessment; Kalshi's fee schedule was not checked), but switching frequency on minute bars would be far higher and must be re-measured.

## Caveats
Equity indices only, long-only, and equity high-volatility states coincide with falling prices, which is not guaranteed for crypto. Window length and filter lag were chosen by the authors; they state that k = 6 "produces good results", which invites data-snooping concern. Later work in this folder ([shu-2024](shu-2024-downside-risk-statistical-jump-model.md)) finds that a tuned HMM strategy over 1990 to 2023 improved Sharpe only modestly and trailed buy-and-hold on return for the S&P 500 and DAX.
