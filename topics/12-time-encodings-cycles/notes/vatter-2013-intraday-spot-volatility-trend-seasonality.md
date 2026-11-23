---
title: "Non-parametric estimation of intraday spot volatility: disentangling instantaneous trend and seasonality"
authors: "Vatter, Thibault; Wu, Hau-Tieng; Chavez-Demoulin, Valerie; Yu, Bin"
year: 2013
venue: "Working paper (SSRN 2330159), dated 22 November 2013"
url: "https://math.ucdavis.edu/~saito/data/synchrosqueezing/vatter-wu-yu_volatility-via-synchrosqueeze.pdf"
pdf: "sources/12-time-encodings-cycles/vatter-2013-intraday-spot-volatility-trend-seasonality.pdf"
access: "full-text"
source_type: "working-paper"
evidence_grade: "B"
topic: "12-time-encodings-cycles"
asset_class: "fx"
horizon: "minutes"
tags: "fourier-flexible-form, time-varying-seasonality, synchrosqueezing, wavelets, spot-volatility"
---

## Key insight
The Fourier flexible form assumes the intraday volatility pattern is constant over the sample. This paper shows that the frequencies of the pattern are stable (integer cycles per day) but the amplitudes drift, and that a static fit can misstate the seasonal factor by roughly a third. It replaces the fixed sines and cosines with amplitude-modulated components estimated by a wavelet-based synchrosqueezing transform.

## Method
Spot volatility is split multiplicatively into a slow trend and a fast periodic part. Log-volatility is `y[n] = 2*log|r[n] - mu|`. The static FFF is the special case

`s(t) = s0 + sum_{k=1..K} [ a_k*cos(2*pi*k*t) + b_k*sin(2*pi*k*t) ]`, t in days.

The generalization is the adaptive harmonic model `s(t) = sum_k a_k(t)*cos(2*pi*phi_k(t))`, with slowly varying amplitudes `a_k(t)` and instantaneous frequencies `phi_k'(t)`. The synchrosqueezing transform (a reassigned continuous wavelet transform) separates the trend (frequencies below 0.95 cycles per day) from components near integer frequencies. As a simpler comparison the authors fit a rolling FFF by OLS on a two-week window and read the amplitude of harmonic k as `sqrt(a_k^2 + b_k^2)`. Confidence bands come from a block bootstrap.

## Data and sample
Dukascopy 5-minute bid and ask quotes for EUR/USD and USD/JPY, 11 March 2012 to 2 November 2012, 34 trading weeks, 170 days, 48,960 observations. The window was chosen to avoid US daylight-saving changes.

## Reported results
- Autocorrelation and power spectrum of log-volatility show seasonality made of components at integer daily frequencies.
- The EUR/USD amplitude of the main daily oscillation ranges between about 0.6 and 1.4 over eight months, against a constant FFF estimate of 1.01. Using 1.01 in place of 0.6 or 1.4 is described as a 30.7% overestimation or 35.7% underestimation of the periodic volatility component.
- A rolling two-week FFF tracks the synchrosqueezed amplitudes closely, though less smoothly.
- After removing seasonality and trend, residual log-volatility autocorrelation is negligible beyond 30 to 50 lags (2.5 to 4.2 hours).

## Signal construction
Not a directional signal. Practical recipe a bot can take from it:
1. Keep the frequencies fixed at k cycles per day, k = 1..K.
2. Re-estimate `a_k, b_k` on a trailing window (about two weeks of 5-minute data) and update daily or hourly.
3. Track amplitude `A_k = sqrt(a_k^2 + b_k^2)` and phase `atan2(b_k, a_k)` as slow state variables; a falling `A_1` means time of day matters less right now.
4. Use the fitted seasonal as the volatility divisor.

## Relevance to SOL perpetuals at minutes to hours
Crypto session structure has shifted with ETF flows, changing venue shares and regional participation, so a time-varying seasonal is more plausible than a constant one. The rolling FFF is cheap and is the version to implement first. The finding that frequencies stay at integers supports fixed-period sine and cosine features over learned periods.

## Caveats
The paper's rolling FFF and the synchrosqueezing estimates use windows centred on the current time, so they look ahead; a live version must use trailing windows and will lag. Eight months, two FX pairs, no forecasting test and no trading result. The copy read is the 2013 working paper; a later journal version (Econometrics, 2015) was seen in search results but not opened.
