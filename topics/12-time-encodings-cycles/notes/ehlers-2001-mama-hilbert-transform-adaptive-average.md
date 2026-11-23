---
title: "MAMA - The Mother of Adaptive Moving Averages"
authors: "Ehlers, John F."
year: 2001
venue: "MESA Software technical paper (adapted from the book Rocket Science for Traders)"
url: "https://www.mesasoftware.com/papers/MAMA.pdf"
pdf: "sources/12-time-encodings-cycles/ehlers-2001-mama-hilbert-transform-adaptive-average.pdf"
access: "full-text"
source_type: "practitioner"
evidence_grade: "D"
topic: "12-time-encodings-cycles"
asset_class: "equities"
horizon: "daily"
tags: "hilbert-transform, dominant-cycle, homodyne-discriminator, adaptive-moving-average, ehlers"
---

## Key insight
Ehlers measures the "dominant cycle" of a price series bar by bar using a short causal approximation of the Hilbert transform, then uses the rate of change of cycle phase to set the smoothing constant of an exponential moving average. The paper is the most compact published statement of his Hilbert transform homodyne discriminator, with full code. Its evidence for profitability is a single unaudited backtest.

## Method
All steps use only past bars.
1. Smooth: `Smooth = (4*P + 3*P[1] + 2*P[2] + P[3]) / 10`, with P the bar midpoint.
2. Detrend and form quadrature with a 7-tap filter, amplitude-corrected for the last period estimate: `H(x) = (0.0962*x + 0.5769*x[2] - 0.5769*x[4] - 0.0962*x[6]) * (0.075*Period[1] + 0.54)`. `Detrender = H(Smooth)`, `Q1 = H(Detrender)`, `I1 = Detrender[3]`.
3. Phasor averaging: `I2 = I1 - H(Q1)`, `Q2 = Q1 + H(I1)`, each smoothed by an EMA with weight 0.2.
4. Homodyne discriminator (multiply the signal by its one-bar-delayed conjugate): `Re = I2*I2[1] + Q2*Q2[1]`, `Im = I2*Q2[1] - Q2*I2[1]`, both smoothed with weight 0.2; `Period = 360 / arctan(Im/Re)` in degrees.
5. Constrain: period may change by at most a factor of 1.5 up or 0.67 down per bar, is clamped to 6 to 50 bars, and is smoothed again.
6. Phase `= arctan(Q1/I1)`; `DeltaPhase = max(Phase[1] - Phase, 1)`; `alpha = max(FastLimit / DeltaPhase, SlowLimit)` with FastLimit 0.5 and SlowLimit 0.05.
7. `MAMA = alpha*P + (1 - alpha)*MAMA[1]`; `FAMA = 0.5*alpha*MAMA + (1 - 0.5*alpha)*FAMA[1]`. Trade the MAMA and FAMA crossover.

## Data and sample
100 stocks (unnamed), 2 January 1998 to 2 January 2001, daily bars, long side only, one share per stock.

## Reported results
Gross profit of $6,403 on 1,317 trades; 37.5% of trades profitable; average profit per trade $4.86 per share; about 4.4 trades per year per stock. The author assumes a typical transaction cost of about $0.30 per share and concludes the system is net profitable. No benchmark, no risk measure, no out-of-sample split.

## Signal construction
Inputs: a bar series at the chosen frequency (for example 5-minute midpoints from Binance SOL perpetual). Run steps 1 to 7 on each new bar. Outputs usable as features:
- `Period` (dominant cycle length in bars, 6 to 50),
- `Phase` and `DeltaPhase`,
- `MAMA - FAMA` as a trend-state variable,
- `I1`, `Q1` as a detrended in-phase and quadrature pair.
Update every bar; the filters need roughly 50 bars to settle.

## Relevance to SOL perpetuals at minutes to hours
The computation transfers to any bar size. What needs testing is whether the measured period carries information. The estimator always returns a number between 6 and 50 bars, including on a random walk, so the period alone cannot show that a cycle exists. A fair test compares a strategy using the adaptive period against the same strategy with a fixed period, net of fees, on walk-forward data. Ehlers's site also carries a 2026 "Dominant Cycle" code listing that replaces the Hilbert filter with a high-pass plus SuperSmoother band limit (10 to 40 bars), builds the quadrature from a normalized one-bar difference, and clamps the result to 8 to 50 bars; it has no test results.

## Caveats
Practitioner paper by a vendor of cycle software. The backtest covers three years including the 1999 rally, long only, with no comparison to buy and hold. The paper's claim that many trades show the system "was not curve-fitted" is not a statistical argument. The publication year is inferred from the test window and the 2001 book; the PDF itself is undated.
