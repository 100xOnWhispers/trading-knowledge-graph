---
title: "Intraday periodicity and volatility persistence in financial markets"
authors: "Andersen, Torben G.; Bollerslev, Tim"
year: 1997
venue: "Journal of Empirical Finance 4(2-3), 115-158"
url: "https://public.econ.duke.edu/~boller/Published_Papers/joef_97.pdf"
pdf: "sources/11-intraday-seasonality-tradfi/andersen-1997-intraday-periodicity-volatility-persistence.pdf"
access: "full-text"
source_type: "peer-reviewed"
evidence_grade: "A"
topic: "11-intraday-seasonality-tradfi"
asset_class: "multi"
horizon: "minutes"
tags: "intraday-periodicity, volatility, seasonality-filter, fourier-flexible-form, garch, fx, index-futures"
---

## Key insight
Intraday return volatility has a strong, stable time-of-day shape (a U in exchange-traded index futures, a multi-hump 24-hour cycle in FX tied to regional sessions), while mean returns show no comparable pattern. Ignoring this deterministic shape distorts every high-frequency volatility estimate: GARCH persistence estimated on raw 5-minute to hourly returns is erratic and contradicts temporal-aggregation theory. Dividing returns by an estimated periodic factor restores sensible dynamics.

## Method
Returns are decomposed as R(t,n) = E[R(t,n)] + sigma(t) * s(t,n) * Z(t,n) / sqrt(N), where sigma(t) is the daily volatility level, s(t,n) is the periodic factor for intraday interval n, Z is i.i.d. and N is the number of intervals per day. s(t,n) is estimated with a Fourier flexible functional form (sinusoids plus low-order polynomial terms, allowed to interact with the daily volatility level). Filtered returns are R(t,n) / s_hat(t,n). MA(1)-GARCH(1,1) models are then compared across sampling frequencies on raw and filtered series.

## Data and sample
Five-minute DM/USD spot returns, 1 October 1992 to 30 September 1993 (74,880 observations, 288 intervals per day); five-minute S&P 500 futures returns, 2 January 1986 to 31 December 1989 (79,280 observations, 80 intervals per day). Daily series are used for comparison.

## Reported results
- FX mean 5-minute returns: the time-varying 5% band is violated in 13 of 288 intervals, as expected by chance. The authors conclude there is little evidence of systematic appreciation or depreciation over the day.
- FX average absolute 5-minute return ranges from about 0.01% near 04:00 GMT (Tokyo lunch) to about 0.05% near 15:00 GMT (Europe/US overlap).
- First-order autocorrelation of absolute 5-minute DM/USD returns is 0.309; Ljung-Box Q(10) = 36,680.
- S&P 500 futures show the classic U (J-shaped on the highest-volatility days); 5-minute standard deviation 0.104% versus 0.047% for DM/USD.
- Intraday GARCH persistence on raw data is lowest at half-hour to 1.5-hour sampling; filtered returns behave much closer to theory and point to several volatility components.

## Signal construction
Not a directional signal. It is the standard preprocessing step: estimate s(n) per time-of-day bucket (rolling mean of absolute or squared returns per bucket, or the Fourier form), then express every volatility, volume, order-flow or return-surprise feature relative to its bucket norm. Use for volatility forecasts, position sizing, stop widths, and z-scoring of any feature that inherits the diurnal shape.

## Relevance to SOL perpetuals at minutes to hours
SOL trades 24 hours like FX, so the multi-session shape (Asia, Europe, US, plus funding timestamps and US equity open/close) is the relevant template, not the equity U. The finding that means carry no time-of-day pattern while volatility does is a useful prior. The periodic factor must be re-estimated on crypto data, and it must be allowed to depend on the volatility level and to shift with daylight saving, which the paper flags.

## Caveats
One year of FX and four years of futures from 1986-1993. No trading test. The shape is assumed stable; in crypto it drifts as venue mix changes. Announcement spikes are not removed here (handled in the authors' 1998 Journal of Finance paper, not noted).
