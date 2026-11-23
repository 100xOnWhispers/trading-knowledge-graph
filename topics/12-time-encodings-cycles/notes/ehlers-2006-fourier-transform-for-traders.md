---
title: "Fourier Transform for Traders"
authors: "Ehlers, John F."
year: 2006
venue: "MESA Software technical paper"
url: "https://mesasoftware.com/papers/FourierTransformForTraders.pdf"
pdf: "sources/12-time-encodings-cycles/ehlers-2006-fourier-transform-for-traders.pdf"
access: "full-text"
source_type: "practitioner"
evidence_grade: "D"
topic: "12-time-encodings-cycles"
asset_class: "equities"
horizon: "daily"
tags: "discrete-fourier-transform, periodogram, dominant-cycle, spectral-analysis, ehlers"
---

## Key insight
A rolling discrete Fourier transform over a 50-bar window has too little resolution to pick out market cycles of 8 to 50 bars, a point Ehlers concedes at the outset. He then sharpens the display with a nonlinear rescaling of the normalized spectrum and extracts a single "dominant cycle" as a centre of gravity. The rescaling changes how the spectrum looks, not how much information the window contains, as the paper itself acknowledges when citing Kay and Demeure.

## Method
1. Detrend with a high-pass filter (40-bar cutoff): `alpha1 = (1 - sin(360/40)) / cos(360/40)`; `HP = 0.5*(1 + alpha1)*(P - P[1]) + alpha1*HP[1]`.
2. Remove 2 to 4 bar components with a 6-tap FIR: `Cleaned = (HP + 2*HP[1] + 3*HP[2] + 3*HP[3] + 2*HP[4] + HP[5]) / 12`.
3. For each period T from 8 to 50 bars over a window of W = 50 bars: `C(T) = sum_n Cleaned[n]*cos(360*n/T)`, `S(T) = sum_n Cleaned[n]*sin(360*n/T)`, `Pwr(T) = C^2 + S^2`.
4. Normalize by the maximum power and convert with the transformation borrowed from Kay and Demeure (`S_music = 1 / (1 - S_bartlett)`): `DB(T) = -10*log10( 0.01 / (1 - 0.99*Pwr(T)/MaxPwr) )`, capped at 20.
5. Dominant cycle as centre of gravity over periods within 3 dB of the peak: `DC = sum T*(3 - DB(T)) / sum (3 - DB(T))` for `DB(T) < 3`.

The stated use is to tune other indicators to the measured period, for example an RSI computed over half the dominant cycle.

## Data and sample
Illustrated on a daily IBM chart. No systematic sample.

## Reported results
None quantitative. The paper states, from visual inspection of the heat map, that only one strong cycle is present most of the time and that the centre-of-gravity estimate is the "smoothest and most reliable" in the author's experience. It also states the author's opinion that a measured period above 50 bars means the market is trending and cycle measurement is of little help. No backtest, hit rate or significance test is given.

## Signal construction
Inputs: bar midpoints. Each bar, run steps 1 to 5 on the trailing 50 bars. Outputs:
- `DC`, the dominant period in bars,
- peak-to-mean spectral ratio (`MaxPwr / mean Pwr`), a cheap measure of how concentrated the spectrum is,
- the phase at the dominant period, `atan2(S(DC), C(DC))`.
The last two are natural extensions and are not in the paper. Cost is about 43 periods times 50 bars of multiply-adds per update.

## Relevance to SOL perpetuals at minutes to hours
The code is frequency-agnostic and runs on 1-minute or 5-minute bars. The main use for this repository is as a testable hypothesis generator: does adapting an oscillator's look-back to `DC` beat a fixed look-back out of sample? The spectral concentration ratio may be more useful than the period itself as a regime feature (cycling versus trending). Any peak should be compared with what a random walk passed through the same high-pass and FIR filters produces, since those filters by themselves create a spectral hump inside the 8 to 50 bar band.

## Caveats
Practitioner source from a software vendor; no evidence of predictive value is offered. A 50-bar window cannot resolve periods near 50 bars. The band-limiting filters guarantee a peak somewhere in the band on pure noise. The year is taken from the code's 2006 copyright line; the PDF is otherwise undated.
