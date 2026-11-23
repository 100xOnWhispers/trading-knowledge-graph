---
title: "Empirical Mode Decomposition: A novel approach for cycle and trend mode detection"
authors: "Ehlers, John F.; Way, Ric"
year: 2009
venue: "MESA Software technical paper"
url: "https://www.mesasoftware.com/papers/EmpiricalModeDecomposition.pdf"
pdf: "sources/12-time-encodings-cycles/ehlers-2009-empirical-mode-decomposition-cycle-trend.pdf"
access: "full-text"
source_type: "practitioner"
evidence_grade: "D"
topic: "12-time-encodings-cycles"
asset_class: "equities"
horizon: "daily"
tags: "bandpass-filter, cycle-mode, trend-mode, regime-detection, ehlers"
---

## Key insight
A two-pole bandpass filter isolates the swing component of price in a chosen period band, and the average of that filtered output over two periods acts as a trend indicator. Comparing the trend line with a fraction of recent cycle peaks and valleys classifies the market as "trend mode" or "cycle mode". Despite the title, this is a fixed linear filter and not the sifting algorithm of Huang et al. that the term empirical mode decomposition normally denotes.

## Method
Bandpass filter centred on `Period` bars with half-bandwidth parameter `delta`:

`beta = cos(360 / Period)`
`gamma = 1 / cos(720 * delta / Period)`
`alpha = gamma - sqrt(gamma^2 - 1)`
`BP = 0.5*(1 - alpha)*(P - P[2]) + beta*(1 + alpha)*BP[1] - alpha*BP[2]`

With Period 20 and delta 0.1 the filter passes roughly 18 to 22 bars; with delta 0.5, roughly 10 to 30 bars. Small delta gives a long memory and the filter "rings".

Trend: `Mean = Average(BP, 2*Period)`.

Mode thresholds: record each local peak and valley of BP, average them over 50 bars, and scale by `Fraction` (0.1 in the code default, 0.25 in the example). If `Mean > Fraction*AvgPeak` the market is in an uptrend; if `Mean < Fraction*AvgValley`, a downtrend; otherwise cycle mode, where swing signals from BP are meant to be used.

## Data and sample
Illustrated on a synthetic chirp and about one year of daily MSFT prices. No systematic sample.

## Reported results
None quantitative. The authors state that the filtered output "clearly identifies cyclic turning points" on the MSFT chart and that threshold choice is "somewhat subjective". No trade statistics, hit rates or comparisons are reported.

## Signal construction
Inputs: bar midpoints at the working frequency. Parameters: Period, delta, Fraction. Each bar:
1. Update BP by the recursion above (two state variables).
2. Update `Mean`, `AvgPeak`, `AvgValley`.
3. Emit `regime` in {up, down, cycle} and the continuous ratio `Mean / AvgPeak`.
4. Optionally emit BP normalized by its rolling RMS as a band-limited oscillator.
The filter is causal and cheap. Its group delay grows as delta shrinks.

## Relevance to SOL perpetuals at minutes to hours
A band-limited oscillator and a trend-versus-range flag are plausible conditioning features for a bot that switches between momentum and mean-reversion logic. Period can be set from a physical clock (for example 96 five-minute bars for an 8-hour funding cycle, or 288 for a day) to test whether price has any band-limited component at those periods, which is a cleaner question than chasing a floating dominant cycle. The classification rule and its Fraction parameter need walk-forward testing against simpler regime measures such as an efficiency ratio or realized-volatility ratio.

## Caveats
No evidence of predictive value. A bandpass filter applied to a random walk produces a smooth oscillation with apparent turning points; visual fit on one chart demonstrates nothing. Three free parameters invite overfitting. The naming may mislead readers looking for true EMD. Year taken from the PDF creation date (October 2009); the magazine publication date was not confirmed.
