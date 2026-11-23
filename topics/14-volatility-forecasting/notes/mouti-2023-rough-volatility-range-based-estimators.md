---
title: "Rough volatility: evidence from range volatility estimators"
authors: "Mouti, Saad"
year: 2023
venue: "arXiv preprint 2312.01426 (v2, September 2024)"
url: "https://arxiv.org/pdf/2312.01426"
pdf: "sources/14-volatility-forecasting/mouti-2023-rough-volatility-range-based-estimators.pdf"
access: "full-text"
source_type: "working-paper"
evidence_grade: "B"
topic: "14-volatility-forecasting"
asset_class: "multi"
horizon: "daily"
tags: "parkinson, garman-klass, rogers-satchell, range-estimators, ohlc, rough-volatility, hurst"
---

## Key insight
Volatility proxies built only from open, high, low and close prices (Parkinson, Garman-Klass) track high-frequency realized volatility closely and show the same "rough" scaling (Hurst exponent well below 0.5) that was first found with realized volatility. Roughness is therefore not an artefact of microstructure noise in tick data. A one-parameter rough-volatility forecaster is competitive with AR, HAR and GARCH on these range-based series. The paper is also a compact, checkable statement of the classic OHLC formulas.

## Method
Per-bar variance estimators, with O, H, L, C the bar's prices:
- Parkinson: (1 / (4 ln 2)) * (ln(H/L))^2.
- Garman-Klass (practical form): 0.5 * (ln(H/L))^2 - (2 ln 2 - 1) * (ln(C/O))^2.
- Rogers-Satchell (drift-independent): ln(H/O) * (ln(H/O) - ln(C/O)) + ln(L/O) * (ln(L/O) - ln(C/O)).
- Yang-Zhang is mentioned but needs multiple bars, so it is not used.

The author compares these with Oxford-Man realized volatility on the S&P 500, then estimates the scaling of log-volatility increments to get the Hurst exponent H, and tests the rough fractional stochastic volatility (RFSV) forecast formula against AR, HAR and GARCH at 1, 5 and 20 days.

## Data and sample
Estimator comparison: S&P 500, January 2000 to April 2015 (3,786 days), benchmark Oxford-Man realized volatility. Scaling analysis: daily Bloomberg range data, 2,521 trading days from 19 April 2005 to 22 April 2015, for equity indices, a commodity index and single stocks. No crypto assets.

## Reported results
- Versus realized volatility on the S&P 500, mean squared error (in units of 1e-4): close-to-close 0.533, Parkinson 0.092, Garman-Klass 0.094, Rogers-Satchell 0.206. All range estimators are biased low relative to realized volatility (proportional bias -0.08 to -0.18).
- Garman-Klass is closest to realized variance and has the smallest standard deviation.
- Efficiency figures quoted from the original papers: Parkinson 2.5 to 5 times close-to-close, Garman-Klass 7.4, Rogers-Satchell 6.0.
- Hurst estimates from range proxies are 0.01 to 0.09 (for example 0.081 for S&P 100 with Garman-Klass).
- RFSV outperforms the other predictors for variance at all tested horizons and is at least as good as HAR at 5 and 21 days for log-volatility.

## Signal construction
Not a directional signal. Use as the fallback volatility input where only OHLC bars are available (some venues' history, or Kalshi's own contract early on): compute Garman-Klass per 1- or 5-minute bar and sum over the window; scale up modestly for the documented downward bias, calibrating the scale against tick-based RV on a venue where both exist.

## Relevance to SOL perpetuals at minutes to hours
Range estimators are attractive for crypto because OHLC bars are free and universal. Their theory assumes continuous trading within the bar and no jumps, so they are biased low when trading is sparse (the true high and low are not observed) and distorted by wicks from liquidation cascades. For a 24/7 market the opening-gap problem that motivates Yang-Zhang largely disappears. The roughness finding implies volatility forecasts should weight the most recent observations heavily. All of this needs re-testing on SOL bars.

## Caveats
Working paper, single author, traditional assets, daily bars. The efficiency numbers are quoted from the original papers, which were not opened in this session (no open copy of the Parkinson, Garman-Klass, Rogers-Satchell or Yang-Zhang papers was found). At the 1-day horizon the paper notes RFSV sometimes underperforms AR and HAR for log-volatility.
