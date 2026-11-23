---
title: "Bitcoin intraday time-series momentum"
authors: "Shen, Dehua; Urquhart, Andrew; Wang, Pengfei"
year: 2022
venue: "Financial Review 57(2), 319-344"
url: "https://centaur.reading.ac.uk/100181/3/21Sep2021Bitcoin%20Intraday%20Time-Series%20Momentum.R2.pdf"
pdf: "sources/13-momentum-reversal/shen-2022-bitcoin-intraday-time-series-momentum.pdf"
access: "full-text"
source_type: "peer-reviewed"
evidence_grade: "A"
topic: "13-momentum-reversal"
asset_class: "crypto"
horizon: "hours"
tags: "intraday-momentum, bitcoin, first-half-hour, last-half-hour, volume, liquidity-provision"
---

## Key insight
Bitcoin shows the "market intraday momentum" pattern known from equity ETFs: the return from the previous close to the end of the first half-hour of the session predicts the last half-hour return with the same sign. The second-to-last half-hour predicts the last half-hour with a negative sign, so momentum across the day and reversal at the 30-minute lag coexist. The effect is much stronger after high-volume or high-volatility opening sessions, and its magnitude is too small to survive spot fees without leverage.

## Method
Following Gao et al. (2018), predictive regressions of the last half-hour return on (a) the overnight-plus-first-half-hour return and (b) the second-to-last half-hour return. Because Bitcoin trades 24 hours, the session open is set where volume spikes on each exchange and the close is fixed at 5pm EST (the CME Bitcoin futures break). Out-of-sample R-squared uses recursive regressions against the historical mean. Timing strategies go long or short in the last half-hour according to the sign of the predictor; a mean-variance allocation gives certainty-equivalent returns. Breakeven transaction costs are computed.

## Data and sample
Tick BTC/USD trades from Bitfinex, Bitstamp, CEX.IO, Coinbase and Kraken via bitcoincharts.com, aggregated to 1-minute bars, from each exchange's earliest date (Bitstamp from 2013) to 31 December 2020.

## Reported results
- In-sample R-squared: 1.44% using the first half-hour; 2.12% using both predictors. The second-to-last half-hour coefficient is negative and significant.
- Out-of-sample R-squared: 1.09% (first half-hour), 1.40% (second-to-last), 1.61% (both).
- High-volume first sessions: R-squared 3.86% against 1.09% on low-volume days. Predictability is concentrated in days when the first half-hour return is positive (R-squared 1.89% against 0.11% when negative).
- Timing strategy returns: 7.82% a year (first half-hour signal), 17.32% (second-to-last), 16.69% (combined), against 6.54% for always-long in the last half-hour.
- Breakeven costs without leverage are 3, 7 and 10 basis points per trade, below the 25 basis point Bitstamp fee the authors cite.
- The authors attribute the effect to liquidity provision, not late-informed trading.

## Signal construction
Define a session (for example the US cash-equity or CME window). x1 = return from prior session close to 30 minutes after the open; x2 = return of the second-to-last 30 minutes. Forecast last-30-minute return = a + b1*x1 + b2*x2 with b1 > 0, b2 < 0, estimated recursively. Weight the forecast up when opening volume is in its top tercile.

## Relevance to SOL perpetuals at minutes to hours
The horizon matches the bot. The structure worth re-testing on SOL is: open-window return predicts close-window return, conditioned on opening volume, with a contrarian term from the bar immediately before. Session anchors should be re-chosen for 2026 market structure (US equity open and close, CME hours, and the 8-hour funding timestamps are natural candidates). Perpetual taker fees of a few basis points are near the unlevered breakeven, so this is a marginal edge to be combined with others, not a stand-alone strategy.

## Caveats
Bitcoin spot only, sample ends 2020. The paper's claim that leverage raises breakeven cost is not economically meaningful, because fees scale with notional as well; the unlevered breakeven of 3 to 10 basis points is the relevant number. Session definition by volume spike is a free parameter and a data-snooping risk.
