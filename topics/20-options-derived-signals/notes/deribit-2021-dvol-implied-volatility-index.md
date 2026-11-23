---
title: "DVOL - Deribit Implied Volatility Index"
authors: "Deribit"
year: 2021
venue: "Deribit Insights (exchange documentation, published 31 March 2021, updated 20 March 2023)"
url: "https://insights.deribit.com/exchange-updates/dvol-deribit-implied-volatility-index/"
pdf: "none"
access: "full-text"
source_type: "documentation"
evidence_grade: "C"
topic: "20-options-derived-signals"
asset_class: "crypto"
horizon: "n/a"
tags: "dvol, implied-volatility-index, deribit, variance-swap, index-methodology, volatility-futures"
---

## Key insight
DVOL is Deribit's 30-day annualised implied volatility index, computed every second from the option book with a variance-swap method and then smoothed with an exponential moving average over the last 240 values. It is the standard free input for "crypto VIX" features, and its construction details (smoothing, depth-weighted mids, delta cut-off) determine how fast it can react.

## Method
As described on the page (formulas are published there as images and were not read):
- Expiries: the furthest expiry with 30 or fewer days to go and the nearest with more than 30 days. Instruments listed for less than one hour are ignored.
- Prices: a mid of depth-weighted bid and ask (volume-weighted over 2 BTC of depth across 5 levels one tick apart). If the spread is wide the index falls back to the one-minute trade VWAP, then to a mark price from 60 to 90 seconds earlier, then to the current mark price.
- Options with delta below 5% are discarded. Only out-of-the-money options relative to the option-implied forward are used.
- Variance for each expiry is a strike-width-weighted sum (variance-swap replication); the two expiries are interpolated in time to 30 days and the square root is taken.
- The raw value is calculated every second; the published DVOL is an exponential moving average with period 240.
- Parameters are defaults "subject to change by Deribit" with 48 hours' notice.

## Data and sample
A specification, not a study. The page concerns the bitcoin index; it says ETH volatility futures would follow later.

## Reported results
No empirical results. Stated rules of thumb: divide DVOL by 20 for an approximate expected daily move (DVOL 90 gives about 4.5%); dividing by the square root of 365 gives about 4.7%. The page calls the index an "action gauge" because bitcoin options often show positive skew on both calls and puts, so a high reading does not imply fear of a fall. Futures on the bitcoin index (BTCDVOL) are listed.

## Signal construction
Inputs: the DVOL series for BTC and ETH from the Deribit public API (the endpoint name was not verified in this session).
- Level: `sigma_1h = DVOL / 100 * sqrt(1 / (365 * 24))` as a prior for the next hour's volatility.
- Change: `DVOL_t - DVOL_{t-k}` for k from 5 minutes to 4 hours as a volatility-shock feature.
- Premium: `DVOL^2 - RV_30d^2`, read with the regime caveat in [almeida-2024-risk-premia-bitcoin-market](almeida-2024-risk-premia-bitcoin-market.md).
The 240-second smoothing means DVOL lags a jump in option prices by a few minutes; for faster features use mark implied volatility of the nearest weekly at-the-money options.

## Relevance to SOL perpetuals at minutes to hours
There is no DVOL for SOL on the page read. BTC and ETH DVOL are usable as market-wide volatility state for a SOL model. A 30-day index moves slowly compared with a minutes-to-hours horizon, so the level works as a regime variable and only the short-window change has a chance of carrying timely information. Whether DVOL changes lead or lag perpetual realized volatility at these horizons is untested in the sources read here.

## Caveats
Documentation, not evidence; the grade reflects that. Parameters can change. The summary of the page was produced through a fetch tool, and the exact variance formula was not visible. Index methodology changed with the page update in 2023; anything hard-coded should be re-read from the live documentation.
