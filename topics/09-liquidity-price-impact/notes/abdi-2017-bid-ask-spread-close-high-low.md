---
title: "A Simple Estimation of Bid-Ask Spreads from Daily Close, High, and Low Prices"
authors: "Abdi, Farshid; Ranaldo, Angelo"
year: 2017
venue: "Review of Financial Studies 30(12), 4437-4480 (read as University of St. Gallen Working Papers on Finance 2016/04, April 2017 version)"
url: "https://www.alexandria.unisg.ch/server/api/core/bitstreams/dfb85399-5bcf-465c-8b63-9bfc97ad2ee0/content"
pdf: "sources/09-liquidity-price-impact/abdi-2017-bid-ask-spread-close-high-low.pdf"
access: "full-text"
source_type: "peer-reviewed"
evidence_grade: "A"
topic: "09-liquidity-price-impact"
asset_class: "equities"
horizon: "daily"
tags: "bid-ask-spread, abdi-ranaldo, corwin-schultz, roll, high-low, liquidity-measurement"
---

## Key insight
The close price sits half a spread away from the efficient price, while the average of the high and low is a spread-free proxy for the efficient price. Comparing the close with the mid-range of the same bar and of the next bar isolates the squared spread. The estimator uses more information than Roll (closes only) or Corwin-Schultz (highs and lows only), and is more accurate when there is no quote data.

## Method
With log close c_t and mid-range eta_t = (log high + log low)/2:

S = 2 * sqrt( E[ (c_t - eta_t)(c_t - eta_(t+1)) ] )

The formula has the same structure as Roll's autocovariance estimator, with mid-ranges in place of neighbouring closes. The equation glyphs did not extract from the PDF text; the form above is confirmed by the definition given in Brauneis et al. (2021), AR_i = sqrt(max(4(c_i - p_i)(c_i - p_(i+1)), 0)). Two ways to handle negative values are proposed: "monthly corrected" (average first, floor at zero, then take the root) and "two-day corrected" (floor each two-day estimate at zero, take roots, then average). Unlike Corwin-Schultz, no ad hoc overnight adjustment is needed. The paper also derives an efficient-price variance estimate from changes in mid-ranges.

## Data and sample
US stocks. Benchmarks are TAQ effective spreads: Daily (millisecond) TAQ from October 2003 to December 2015 (147 months) and Monthly TAQ from January 1993 to September 2003. Estimates are also produced for NYSE stocks from 1926 and AMEX stocks from 1962 through 2015.

## Reported results
- Monthly average cross-sectional correlation with Daily TAQ effective spreads is 0.74, against 0.37 to 0.65 for the other estimators that use no quote data (high-low, Roll, Gibbs, effective tick, FHT).
- For 1993 to 2003 the figure is 0.86, against 0.61 to 0.83 for the others.
- It gives the most accurate estimates for less liquid stocks.
- The two-day corrected version associates better with the benchmark, at the cost of more bias from zero-flooring.
- End-of-day quoted spreads, when available, can do better in time-series correlation in some periods.

## Signal construction
On bars of any length (1-minute bars work in a 24-hour market):
1. m_i = (ln H_i + ln L_i)/2.
2. a_i = 4 * (ln C_i - m_i) * (ln C_i - m_(i+1)).
3. Spread over window W: either sqrt(max(mean(a_i), 0)) or mean(sqrt(max(a_i, 0))).
Update each bar. The first version is less biased; the second is the one Brauneis et al. validated on BTC and ETH for tracking liquidity through time.

## Relevance to SOL perpetuals at minutes to hours
Brauneis et al. (2021) found this estimator and Corwin-Schultz to be the best bar-based trackers of time-varying liquidity on crypto spot at hourly and daily frequency, so it is a validated input for a SOL liquidity-state variable. Ardia et al. (2024) show it is biased downward with sparse trading and that its level changes about tenfold with bar frequency on Binance pairs. Use it for relative changes, not absolute cost, and prefer EDGE on a thin venue.

## Caveats
Validated on monthly estimates from daily US equity data; intraday crypto use is an extrapolation supported only by later papers. The zero-flooring creates upward bias in short windows. It assumes a constant spread within the window and that the close is equally likely at bid or ask.
