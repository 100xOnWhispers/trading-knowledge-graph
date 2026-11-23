---
title: "A Practical Guide to Wavelet Analysis"
authors: "Torrence, Christopher; Compo, Gilbert P."
year: 1998
venue: "Bulletin of the American Meteorological Society"
url: "https://paos.colorado.edu/research/wavelets/bams_79_01_0061.pdf"
pdf: "sources/12-time-encodings-cycles/torrence-1998-practical-guide-wavelet-analysis.pdf"
access: "full-text"
source_type: "peer-reviewed"
evidence_grade: "A"
topic: "12-time-encodings-cycles"
asset_class: "multi"
horizon: "n/a"
tags: "wavelets, morlet, significance-testing, red-noise, cone-of-influence"
---

## Key insight
Wavelet power spectra are easy to over-read, so the paper supplies the missing statistics: the expected wavelet spectrum of white and red (AR(1)) noise, a chi-square significance test against that background, and the cone of influence that marks where edge effects make results unreliable. It is the standard methodological reference behind nearly all later wavelet and wavelet-coherence work in finance, including the Bitcoin studies. Its central warning is that many real series produce wavelet pictures resembling those of red noise.

## Method
Continuous wavelet transform of a series with a scaled, translated wavelet; the Morlet wavelet is `psi0(eta) = pi^(-1/4) * exp(i*w0*eta) * exp(-eta^2/2)`. Local power is `|W_n(s)|^2`; local phase is `atan(Im W / Re W)`.

Elements a practitioner needs:
- Scale to period: for the Morlet wavelet with `w0 = 6`, Fourier period is `1.03 * s`, from the general relation `lambda = 4*pi*s / (w0 + sqrt(2 + w0^2))`.
- Edge effects: the series is zero-padded before the FFT, which lowers amplitude near the ends. The cone of influence is defined by the e-folding time of the wavelet at each scale (Table 1 of the paper), and grows with scale.
- Null hypothesis: background spectrum of an AR(1) process with lag-1 autocorrelation `alpha` (alpha = 0 gives white noise). Under the null, local wavelet power divided by the background is distributed as chi-square with two degrees of freedom (one for real wavelets), so the 95% level is a multiple of the background spectrum fixed by the 95th percentile of that chi-square distribution.
- Smoothing in time or scale raises the degrees of freedom and tightens confidence intervals.
- Extensions: cross-wavelet spectrum `W_xy = W_x * conj(W_y)`, coherence and phase difference between two series.

## Data and sample
Illustrations use the Nino3 sea-surface-temperature index, 1871 to 1996, and the Southern Oscillation index. The Nino3 background is red noise with lag-1 coefficient 0.72. Monte Carlo checks use 100,000 simulated white-noise and AR(1) series.

## Reported results
- The analytic chi-square levels match the Monte Carlo 95% levels.
- By construction, 5% of wavelet power exceeds the 95% level under the null, so isolated significant patches are expected by chance; the authors rely on clustering in time and period.
- For ENSO, variance in the 2 to 8 year band is significantly elevated in 1875 to 1910 and 1960 to 1990. These climate findings are not relevant here beyond showing the method.

## Signal construction
Not a signal. It is the test any cycle claim must pass:
1. Fit AR(1) to the series being analysed (returns, log-volatility, volume) to get `alpha`.
2. Compute Morlet power on a trailing window.
3. Flag power as significant only where it exceeds the red-noise 95% level.
4. Discard everything inside the cone of influence.
The fourth step matters most for live trading: the newest bar always sits at the edge, so the most recent estimates at scale s are the least reliable, and increasingly so for longer periods.

## Relevance to SOL perpetuals at minutes to hours
Log price is close to a random walk, which is the extreme of red noise, and its raw wavelet or Fourier spectrum will always show large low-frequency power. Testing against a white-noise background would declare cycles everywhere. Apply the method to returns or to detrended series and use the red-noise null. The cone of influence also explains why wavelet features computed on a full historical sample look far better than the same features computed causally at the right edge.

## Caveats
Written for geophysical series that are closer to Gaussian and stationary than crypto returns; heavy tails and volatility clustering will inflate apparent significance. Pointwise tests are not corrected for multiple comparisons across time and scale. The paper has a published errata page that was not consulted.
