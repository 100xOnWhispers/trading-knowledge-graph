---
title: "Dangers of data mining: The case of calendar effects in stock returns"
authors: "Sullivan, Ryan; Timmermann, Allan; White, Halbert"
year: 2001
venue: "Journal of Econometrics 105(1), 249-286 (LSE Financial Markets Group Discussion Paper 304, October 1998, read)"
url: "https://www.fmg.ac.uk/sites/default/files/2020-11/dp304.pdf"
pdf: "sources/11-intraday-seasonality-tradfi/sullivan-2001-dangers-data-mining-calendar-effects.pdf"
access: "full-text"
source_type: "peer-reviewed"
evidence_grade: "A"
topic: "11-intraday-seasonality-tradfi"
asset_class: "equities"
horizon: "daily"
tags: "calendar-effects, data-snooping, reality-check, day-of-week, turn-of-month, multiple-testing, bootstrap"
---

## Key insight
Calendar effects (day of week, week of month, month of year, turn of month, holidays) look overwhelmingly significant one at a time, but they were found by searching the same data repeatedly. When the best calendar rule is evaluated against the full universe of rules it was implicitly selected from, its significance vanishes. This is the standard reference for why any time-of-day or day-of-week table must be corrected for the number of cells examined.

## Method
White's Reality Check bootstrap. A universe of calendar trading rules is defined; each rule is long, neutral or short the index on specified calendar days, benchmarked against always holding the market. The test statistic is the maximum performance across all rules, and its distribution under the null is obtained by a stationary bootstrap applied jointly to all rules, so the p-value accounts for the search. Performance criteria are mean return and Sharpe ratio. Nominal p-values (best rule in isolation) are compared with Reality Check p-values.

## Data and sample
Dow Jones Industrial Average, daily, January 1897 to December 1996 (100 years; 27,567 daily predictions), with seven sub-periods and a 90-year sub-sample (1897 to May 1986) following Lakonishok and Smidt (1988). The method section also mentions S&P 500 futures as a price series; results for it were not read. Full universe: 9,452 calendar rules built from day, week, semi-month, month and holiday frequencies and their two-way combinations. The working-paper version (titled "Dangers of data-driven inference") was read.

## Reported results
- Full sample: the market's mean annualized return was 4.63%; the best rule (neutral on Mondays, long Tuesday to Friday) earned 8.66%.
- The nominal p-value of the best rule is below 0.002 in the full sample and the 90-year sub-sample.
- The Reality Check p-value is 0.24 in the full sample and 0.20 in the 90-year sub-sample.
- In the shorter sub-samples the best rule beats the index by 3.05 to 11.71 percentage points a year with nominal p-values significant at 10% in all seven periods, yet the Reality Check p-value always exceeds 0.21.
- The identity of the best rule changes across sub-samples, which is what a search over noise produces.

## Signal construction
Not a signal. It is the validation procedure for every seasonality claim in this repository: (1) enumerate the full grid of buckets and rules tried, including discarded ones; (2) compute the best rule's performance; (3) bootstrap all rules jointly with a block or stationary bootstrap that preserves volatility clustering; (4) report the max-statistic p-value. Hansen's SPA test and false-discovery-rate methods are later refinements (not read here).

## Relevance to SOL perpetuals at minutes to hours
A 24 x 7 hour-of-week return grid has 168 cells; with a few years of SOL data several cells will show t-statistics above 2 by chance. Session definitions, lookbacks and holding periods multiply the search further. This paper is the reason to demand a mechanism (forced flow, funding, fixing) before trusting a clock pattern, and to run a joint bootstrap over the whole grid. Volatility seasonality, by contrast, is so strong that it survives any such correction.

## Caveats
Daily equity-index data and simple long/neutral/short rules; it does not test intraday patterns or mechanism-conditioned effects. Failing to reject is not proof of absence: the Reality Check loses power when many poor rules are included. One input to the test was proprietary software from a firm the authors acknowledge.
