---
title: "Bitcoin intraday time-series momentum"
authors: "Shen, Dehua; Urquhart, Andrew; Wang, Pengfei"
year: 2022
venue: "Financial Review, 57(2), 319-344"
url: "https://centaur.reading.ac.uk/100181/3/21Sep2021Bitcoin%20Intraday%20Time-Series%20Momentum.R2.pdf"
pdf: "sources/10-intraday-seasonality-crypto/shen-2022-bitcoin-intraday-time-series-momentum.pdf"
access: "full-text"
source_type: "peer-reviewed"
evidence_grade: "A"
topic: "10-intraday-seasonality-crypto"
asset_class: "crypto"
horizon: "minutes"
tags: "intraday-momentum, first-half-hour, last-half-hour, session-definition, cme-close, breakeven-costs, out-of-sample"
---

## Key insight
Bitcoin has no open or close, but if a "trading day" is defined by the daily volume spike (open) and the 5pm New York CME futures break (close), the first half-hour return predicts the last half-hour return with the same sign, as in equity index ETFs. The second-to-last half hour predicts the last half hour with the opposite sign. The effect is concentrated on high-volume and high-volatility days and is too small to survive spot fees without leverage.

## Method
Following Gao et al. (2018). For each day t:

r_ONFH = p(open + 30 min, t) / p(close, t-1) - 1, r_SLH = p(c-30) / p(c-60) - 1, r_LH = p(c) / p(c-30) - 1.

Pooled predictive regressions r_LH = a + b1 r_ONFH + b2 r_SLH + e with Newey-West errors; recursive out-of-sample R-squared against the historical mean; sorts on first-half-hour volume and volatility; sign-based timing strategies; mean-variance utility gains; breakeven transaction costs; tests of late-informed trading versus liquidity provision.

## Data and sample
Tick BTC/USD trades from Bitfinex, Bitstamp, CEX.IO, Coinbase and Kraken (bitcoincharts.com), aggregated to 1 minute, from each exchange's earliest date (Bitstamp from 2013) to 31 December 2020. The close is 5pm EST; the open is exchange-specific, set where volume spikes.

## Reported results
- First half hour predicts last half hour: slope 0.968, Newey-West t = 4.38, R-squared 1.44%. With the second-to-last half hour added (negative coefficient) R-squared is 2.12%.
- Out-of-sample R-squared: 1.09% (first half hour), 1.40% (second-to-last), 1.61% (both).
- Significant on high and medium first-half-hour volume days (R-squared 3.86% on high-volume days), insignificant on low-volume days. Significant only on high-volatility days (R-squared 2.83%).
- Timing strategy annual returns: 7.82% (first-half-hour signal), 17.32% (second-to-last), 16.69% (combined), versus 6.54% for always long in the last half hour. Strongest relative to buy-and-hold in down years (2014, 2015, 2018).
- Mean-variance use of both predictors: 13.95% a year, Sharpe 1.15, certainty-equivalent gain 8.09%.
- Stronger after positive first-half-hour returns (R-squared 1.89% versus 0.11%).
- Breakeven costs are 3, 7 and 10 bps per trade for the three strategies, below Bitstamp's 25 bps fee; with 10:1 leverage the authors compute 29, 64 and 96 bps.
- US market hours account for 56.12% of BTC/USD volume. The authors attribute the effect to liquidity provision, not late-informed trading.

## Signal construction
Inputs: 1-minute mid or last price on the lead venue. At 21:30 UTC (16:30 New York; shifts with daylight saving), compute r_ONFH from the prior 22:00 UTC close to 30 minutes after the session open, and r_SLH over 21:00 to 21:30. Score = sign(r_ONFH) - sign(r_SLH); trade the last half hour in the direction of the score when both agree, and only when first-half-hour volume or volatility is in its top tercile. One decision per day.

## Relevance to SOL perpetuals at minutes to hours
The session definition is the transferable idea: anchor windows on the US equity session and the CME close. Perpetual fees of a few bps make 7 to 10 bps breakeven borderline, not hopeless. Untested on SOL, on perps, or after 2020; CME's daily break no longer exists in the same form now that CME trades 24/7 (see the CME note).

## Caveats
The "open" is chosen per exchange by looking at volume, a researcher degree of freedom. Half-hour R-squared of 1 to 2% means a thin edge. Sample ends 2020. The leverage argument raises breakeven per unit of capital, not the edge per unit of notional.
