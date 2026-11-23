---
title: "The crypto world trades at tea time: intraday evidence from centralized exchanges across the globe"
authors: "Brauneis, Alexander; Mestel, Roland; Theissen, Erik"
year: 2025
venue: "Review of Quantitative Finance and Accounting, 64(1), 275-304 (published online June 2024)"
url: "https://link.springer.com/article/10.1007/s11156-024-01304-1"
pdf: "none"
access: "full-text"
source_type: "peer-reviewed"
evidence_grade: "A"
topic: "10-intraday-seasonality-crypto"
asset_class: "crypto"
horizon: "hours"
tags: "hour-of-day, tea-time, altcoins, cross-exchange, volatility, volume, corwin-schultz-spread, commonality"
---

## Key insight
The broadest study of crypto time-of-day effects: 1,940 pairs on 38 exchanges on five continents share one intraday profile. Trading activity, volatility and illiquidity all peak between 16:00 and 17:00 UTC regardless of where the exchange sits or which coins are traded. Local time zones shift volume a little, but a global component dominates, which points to common information flow and concentrated liquidity trading instead of local trader habits.

## Method
Hourly measures per pair: log return, Garman-Klass volatility, Corwin-Schultz high-low spread estimate, log volume, number of trades, average trade size. Each series is detrended, demeaned and scaled to unit variance, then regressed on 24 hour-of-day dummies. The 24-coefficient profiles are compared across all pairs (a 1,940 by 1,940 correlation matrix), clustered hierarchically, and the pairwise correlations are regressed on venue and pair characteristics (same continent, same venue, same pair, shared currency, venue reliability, time-zone distance).

## Data and sample
Hourly OHLC, volume and trade counts from Cryptotick, 1 July 2018 to 1 January 2022 (30,744 hours). Filters: at least 75% hourly coverage, and exclusion of unrated venues and venues rated below 2/10 by CoinMarketCap and CoinGecko. Final sample 1,940 pairs, 38 exchanges (10 Americas, 19 Asia and Oceania, 9 Europe), 386 coins or tokens.

## Reported results
- Returns are below average from about 01:00 to 05:00 UTC, peak between 15:00 and 16:00 UTC, and are positive in the last three hours of the UTC day.
- Volatility, spread, volume and trade count are below average for the first two thirds of the UTC day (the first hour excepted), then climb to a peak at 16:00 to 17:00 UTC. The spread estimate peaks an hour earlier.
- Illiquidity peaks with volume: liquidity is worst when activity is highest.
- Volume and trade counts bottom out at local night on each continent, yet the afternoon-UTC peak is present on all continents.
- Volatility profiles are highly similar everywhere: the predicted pairwise correlation never falls below 45.3% even for unrelated pairs on different continents. Return profiles are the least similar.
- Same pair on different venues raises profile correlation by 0.06 (trade size) to 0.58 (returns); same venue by 0.05 to 0.26.
- All measures still peak in the UTC afternoon in each of three subperiods (2018 to 2019, 2019 to 2020, 2020 to 2021).
- The authors note that the peak coincides with the calculation of CME CF reference rates and suggest futures settlement and ETF conventions as candidate drivers. Weekday versus weekend is not analysed.

## Signal construction
Context, with one weak directional prior. For each hour of the UTC day keep standardised dummy coefficients for volatility, volume and spread on the target contract; use them as expected-state features. The return profile (weak 01:00 to 05:00, strong 15:00 to 16:00 and late UTC evening) can be coded as an hour-of-day prior, but only after re-estimation with costs.

## Relevance to SOL perpetuals at minutes to hours
The strongest evidence that the intraday profile transfers to altcoins: the sample is dominated by non-BTC pairs and the pattern holds with and without BTC or stablecoins in the pair. Expect SOL volatility and volume to peak near 15:00 to 17:00 UTC and execution cost to be highest then. Whether the hour moved after US spot ETFs (2024) and CME's 24/7 trading (2026) needs testing.

## Caveats
Hourly spot data, no perpetuals, sample ends January 2022. Spreads are estimated from high-low prices, not quotes. Return-profile effects are small and no trading strategy or cost test is given. No PDF could be saved; the note is based on the open-access HTML full text (first 100,000 characters read).
