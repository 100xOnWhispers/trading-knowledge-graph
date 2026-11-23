---
title: "Time-of-day effects in the Bitcoin options market"
authors: "Hoang, Lai Trung; Phan, Trang Thu"
year: 2026
venue: "Finance Research Letters, 101"
url: "https://ideas.repec.org/a/eee/finlet/v101y2026ics1544612326005374.html"
pdf: "none"
access: "abstract-only"
source_type: "peer-reviewed"
evidence_grade: "B"
topic: "10-intraday-seasonality-crypto"
asset_class: "options"
horizon: "hours"
tags: "deribit, options-expiry, 08-utc-settlement, nyse-open, time-of-day, rollover"
---

## Key insight
Bitcoin options trading on Deribit clusters in two windows of the day. One is 08:00 to 09:00 GMT, the hour after Deribit's daily 08:00 expiry and settlement, driven by traders rolling and re-establishing expiring positions; it appears on weekdays and weekends alike. The other is 14:00 to 15:00 GMT, the New York Stock Exchange open, and it largely disappears at weekends. Exchange conventions and equity-market hours both shape the crypto derivatives clock.

## Method
Only the abstract was read. It describes a comparison of options trading activity in each hour against other hours of the day using "a comprehensive dataset from Deribit", with splits by weekday versus weekend, by the number of expiring contracts, and by contract maturity. The estimator was not confirmed.

## Data and sample
Bitcoin options on Deribit. Sample period and frequency are not stated in the abstract and were not confirmed.

## Reported results
From the abstract:
- Trading is concentrated in 08:00 to 09:00 GMT and in 14:00 to 15:00 GMT relative to other hours.
- The 08:00 to 09:00 concentration persists on weekdays and weekends, is stronger on days with more expiring contracts, and is stronger for shorter-maturity contracts. The authors attribute it to rollover around the 08:00 GMT settlement.
- The 14:00 to 15:00 concentration coincides with the NYSE open and is largely absent at weekends, which the authors read as a spillover from equity markets.
- The authors describe this as the first systematic evidence of intraday patterns in Bitcoin options trading.
No magnitudes were available.

## Signal construction
Not a directional signal. It defines two scheduled-event flags for the feature set: (1) the Deribit expiry window, 08:00 to 09:00 UTC, weighted by the notional expiring that day (daily, weekly on Fridays, monthly and quarterly on the last Friday); (2) the US cash equity open, 09:30 New York, on NYSE trading days. A bot can raise expected volatility around both and test whether spot or perp returns before 08:00 UTC on large-expiry days show pinning or a post-expiry release.

## Relevance to SOL perpetuals at minutes to hours
Deribit also lists SOL options, with far less open interest than BTC, so any SOL-specific expiry effect would be small; the BTC expiry matters to SOL through BTC's price. The abstract says nothing about effects on the underlying price, so "max pain" or pinning effects around 08:00 UTC remain practitioner folklore that this paper does not confirm. The 08:00 UTC window also coincides with a funding timestamp on most perpetual venues, so the two effects need to be separated in testing.

## Caveats
Abstract-only; the article is behind the publisher paywall. The findings concern options volume, not underlying returns or volatility. Sample dates unknown, so it is unclear how much of the data is post-ETF. Daylight saving shifts the NYSE open between 13:30 and 14:30 UTC, so a fixed 14:00 to 15:00 GMT window is an approximation.
