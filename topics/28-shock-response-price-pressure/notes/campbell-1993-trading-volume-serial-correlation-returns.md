---
title: "Trading Volume and Serial Correlation in Stock Returns"
authors: "Campbell, John Y.; Grossman, Sanford J.; Wang, Jiang"
year: 1993
venue: "NBER Working Paper 4193 (October 1992), the version read; published in the Quarterly Journal of Economics, 1993 (journal version not opened)"
url: "https://www.nber.org/system/files/working_papers/w4193/w4193.pdf"
pdf: "sources/28-shock-response-price-pressure/campbell-1993-trading-volume-serial-correlation-returns.pdf"
access: "full-text"
source_type: "peer-reviewed"
evidence_grade: "A"
topic: "28-shock-response-price-pressure"
asset_class: "equities"
horizon: "daily"
tags: "price-pressure, volume, autocorrelation, reversal, liquidity-provision, conditioning-variable"
---

## Key insight
A price move that comes with unusually high volume is more likely to be reversed than a move of the same size on low volume. The reason given is that high volume reveals non-informational selling or buying pressure that risk-averse liquidity providers absorb only at a concession, which they earn back as the price recovers. A move on low volume is more likely to be public news, which needs no trade and no reversal. This is the founding statement of volume as the variable that separates price pressure from information.

## Method
Theory: a model with two groups of investors. One group's risk aversion shifts, creating buying or selling pressure; the other group acts as market makers (in the Grossman and Miller sense) and requires a higher expected return to take the other side. Public news moves price without volume; pressure moves price with volume. Empirics: regress the next day's index return on today's return interacted with day-of-week dummies and with detrended volume:

`r(t+1) = a + (sum of day dummies + b * V(t)) * r(t) + e`

Volume `V` is log turnover (shares traded over shares outstanding) minus its one-year backward moving average. Conditional variance from a QGARCH model is tested as a rival conditioning variable. The scanned working paper was read as page images; pages 1 to 10 were read, tables were not inspected directly.

## Data and sample
Daily returns on the CRSP value-weighted NYSE/AMEX index, 3 July 1962 to 30 September 1987 as the main sample, with subsamples 1962-1974 and 1975-1987 and an extension to end-1988. NYSE share volume from Mulherin and Gerety. Also the Dow Jones index, a pre-1962 index from 1926, and 32 large individual stocks.

## Reported results
- First-order daily autocorrelation of the index exceeds 0.15 in every sample and is nearly 0.3 in 1962-1974.
- The coefficient on volume times return is -0.33 with a heteroskedasticity-consistent standard error of 0.06 (1962-1987). Detrended volume has a standard deviation of about 0.25, so moving volume from two standard deviations below its mean to two above lowers the first-order autocorrelation by about 0.3.
- Adding volume raises the R-squared of the day-ahead regression from 5.7 to 6.5 percent (1962-1987), and from 8.4 percent by more than a point in 1962-1974. In 1975-1987 the gain is small (4.3 to 4.6 percent) but volume stays significant (t = 2.0).
- Volatility does not do the same job: it is insignificant when volume is included.
- Volume measured against a slow one-year trend works better than fast-adjusting detrending; the authors read this as volume relative to market-making capacity.
- Scope record: horizon one day ahead; conditioning variable detrended turnover; sign negative (more volume, more reversal); costs not charged, no trading strategy tested.

## Signal construction
For a 5-minute to 1-hour bar on SOL: `V = log(volume) - mean(log(volume))` over a slow window matched for time of day (for example the same bar over the last 30 days); feature `x = V * r`, where `r` is the bar return. The paper predicts a negative coefficient on `x` for next-bar return. Use aggregated volume across the lead venues. Update each bar. Treat the coefficient as something to estimate, since the base autocorrelation in crypto is already negative at these horizons, unlike the positive index autocorrelation here.

## Relevance to SOL perpetuals at minutes to hours
This is the cleanest theoretical reason to expect reversal after liquidation bursts: forced flow is the textbook non-informational trade and it arrives with a volume spike. What must be re-tested is the horizon (the evidence is daily), the instrument (an index with positive autocorrelation from non-synchronous trading, which a single perp does not have), and whether crypto volume spikes are mostly forced flow or mostly news. The companion study by Llorente et al. in this folder shows the sign flips when informed trading dominates.

## Caveats
Daily index data ending in 1988. The effect weakened in 1975-1987. No costs and no out-of-sample test. Index autocorrelation is partly a non-synchronous trading artifact. Tables could not be read as text because the file is a scan.
