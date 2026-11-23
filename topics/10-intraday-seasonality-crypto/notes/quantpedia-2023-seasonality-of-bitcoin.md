---
title: "The Seasonality of Bitcoin"
authors: "Quantpedia (author not listed on the page)"
year: 2023
venue: "Quantpedia blog, 13 September 2023"
url: "https://quantpedia.com/the-seasonality-of-bitcoin/"
pdf: "none"
access: "full-text"
source_type: "practitioner"
evidence_grade: "C"
topic: "10-intraday-seasonality-crypto"
asset_class: "crypto"
horizon: "hours"
tags: "hour-of-day-returns, 21-23-utc, day-of-week, trend-filter, volatility-filter, gemini, backtest"
---

## Key insight
A follow-up to the 2022 Quantpedia study of the 21:00 to 23:00 UTC window, extended to mid-2023. The window still produced the highest hourly returns over the full sample, but the simple rule went through a drawdown in 2022 and 2023. The effect is stronger in uptrends, on high-volatility days, and on Fridays, which makes it look like conditional exposure to Bitcoin's drift more than a free-standing anomaly.

## Method
Hourly returns grouped by hour of day (UTC) and by weekday. Base rule: buy at 21:00 UTC, sell at 23:00 UTC. Two conditioning schemes, both fixed at 00:00 UTC and applied to the following 24 hours:
- Trend: price above or below its 10-, 20-, 50- or 200-day moving average of daily bars.
- Volatility: 30-day historical volatility from hourly bars above or below its rolling 365-day median. The filtered strategy trades the window only on high-volatility days.

## Data and sample
Hourly BTC/USD from Gemini, 9 October 2015 to 30 June 2023, UTC.

## Reported results
- The 22:00 and 23:00 hourly returns are significantly higher than other hours; 03:00 and 04:00 are the worst.
- By weekday, the window works best on Friday, then Thursday, then Saturday and Sunday (exact figures only in charts).
- Base rule: 40.64% annualised return, maximum drawdown -22.7% (against more than -70% for holding Bitcoin), Calmar ratio 1.79.
- High-volatility-only rule: 37.26% annualised return, maximum drawdown -18.87%, Calmar ratio 1.97 (given as 1.96 in the conclusion).
- Returns in the window are higher in uptrends than in downtrends (shown in charts only).
- The article states that the strategy "had a rough period in 2022 and 2023 and experienced a drawdown"; no separate figures for those years are given.
- No Sharpe ratio and no transaction costs are reported.

## Signal construction
Feature set for a model, all known in advance:
- window flag: 1 during 21:00 to 23:00 UTC;
- trend state at 00:00 UTC: sign of (close - N-day moving average), N in {10, 20, 50, 200};
- volatility state at 00:00 UTC: 30-day hourly-bar volatility relative to its 365-day median;
- weekday.
Rule version: long during the window only when the volatility state is high (and, optionally, trend is up).

## Relevance to SOL perpetuals at minutes to hours
The conditioning result is the useful part: an hour-of-day return effect that exists mainly in uptrends and high-volatility regimes should be modelled as an interaction (hour times regime), not as a fixed seasonal mean. For SOL the same interaction can be tested with BTC's or SOL's own trend state. The admitted 2022 to 2023 drawdown is a warning that the unconditional effect is not stable across regimes.

## Caveats
In-sample blog backtest, one exchange, no costs, with filters and parameters chosen after seeing the data (four moving-average lengths, one volatility definition). Long-only in an asset with strong positive drift. The page gives two different Calmar values for the same strategy. Ends June 2023, before spot ETFs; no check of whether the window moved to follow the 4pm New York close after 2024.
