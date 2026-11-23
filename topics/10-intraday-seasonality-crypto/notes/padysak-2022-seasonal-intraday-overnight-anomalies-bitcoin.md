---
title: "Are There Seasonal Intraday or Overnight Anomalies in Bitcoin?"
authors: "Padyšák, Matúš; Vojtko, Radovan"
year: 2022
venue: "Quantpedia blog, 18 February 2022"
url: "https://quantpedia.com/are-there-seasonal-intraday-or-overnight-anomalies-in-bitcoin/"
pdf: "none"
access: "full-text"
source_type: "practitioner"
evidence_grade: "C"
topic: "10-intraday-seasonality-crypto"
asset_class: "crypto"
horizon: "hours"
tags: "hour-of-day-returns, overnight-effect, nyse-session, 21-23-utc, gemini, backtest"
---

## Key insight
The best-known claim of a tradable hour-of-day return effect in Bitcoin: over 2015 to early 2022 the two hours from 21:00 to 23:00 UTC carried a disproportionate share of Bitcoin's positive drift. The authors also show that the equity-style split between "overnight" and "intraday" returns behaves differently on days when the NYSE is open and days when it is closed.

## Method
Hourly BTC bars are grouped by hour of day (UTC) and average returns per hour are tested for significance. Each day is also split, by analogy with equities, into an "intraday" part (10:00 to 16:00 New York, which the authors map to 15:00 to 21:00 UTC, dropping the first half hour so that hourly bars can be used), an "overnight" part (16:00 to 10:00 next day), and a full 16:00-to-16:00 day, separately for NYSE-open days and for weekends and holidays. A simple rule is backtested: buy at 21:00 UTC, sell at 23:00 UTC, every day.

## Data and sample
Hourly BTC/USD from the Gemini exchange, 9 October 2015 to 3 February 2022, UTC timestamps.

## Reported results
- The 22:00 and 23:00 hourly bars (returns from 21:00 to 23:00 UTC) have the largest and most significant average returns; 03:00 and 04:00 are the weakest.
- Several positive hourly returns are significant at the 5% level; no hour has a significantly negative return.
- The buy-21:00, sell-23:00 rule: 33% annualised return, 20.93% annualised volatility, maximum drawdown -22.45%.
- On NYSE-open days, overnight returns dominate and intraday (US session) returns are small and volatile. On weekends and holidays the pattern reverses: the 15:00 to 21:00 UTC component is the stronger and more stable one.
- The authors' interpretation: the strong window is the time when the major traditional exchanges (New York, Tokyo, Hong Kong, India, Australia, London, continental Europe) are all closed. They state that the cause is not clear.
- Hour-by-hour averages and t-statistics are shown only in charts and were not read.

## Signal construction
Inputs: hourly close on a lead venue. Rule: long at 21:00 UTC, flat at 23:00 UTC, daily. As a feature: a dummy for 21:00 to 23:00 UTC, optionally interacted with a NYSE-open-day flag. Because the window is defined in UTC while the claimed cause is tied to New York hours, test both a UTC-fixed and a New-York-fixed (post-close) definition; the two differ by one hour for about eight months a year.

## Relevance to SOL perpetuals at minutes to hours
A two-hour hold fits the bot's horizon and perpetual fees are small relative to the claimed edge, but on a perp the 00:00 UTC funding settlement follows shortly after the window, so the position is exited before funding. The effect has not been shown for SOL. Brauneis et al. report independently that returns are "positive in the last three hours of the day" UTC across 1,940 pairs, which is weak corroboration. The 2023 follow-up (separate note) reports a drawdown in 2022 to 2023.

## Caveats
A blog backtest: in-sample, one exchange, no transaction costs, no multiple-testing correction across 24 hours, and a sample in which Bitcoin rose strongly, so any long-only window earns a positive return (33% a year against 20.93% volatility is partly beta to a bull market concentrated in two hours). Quantpedia sells strategy research. Post-ETF data (2024 onward) are not covered.
