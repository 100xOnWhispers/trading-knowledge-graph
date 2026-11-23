---
title: "BTC ETFs' Impact on Spot Market Structure"
authors: "Kaiko Research (individual author not listed)"
year: 2024
venue: "Kaiko Data Blog, 27 June 2024"
url: "https://www.kaiko.com/resources/btc-etfs-impact-on-spot-market-structure"
pdf: "none"
access: "full-text"
source_type: "industry-research"
evidence_grade: "C"
topic: "10-intraday-seasonality-crypto"
asset_class: "crypto"
horizon: "hours"
tags: "spot-etf, benchmark-fixing, us-close, weekend-volume, market-depth, coinbase, regime-change"
---

## Key insight
US spot Bitcoin ETFs (January 2024) changed the clock of the Bitcoin spot market. Volume concentrated on US venues, on weekdays, and in the 3pm to 4pm New York window when ETF benchmark prices are fixed, while the weekend share of volume fell to a record low. Seasonal profiles estimated on pre-2024 data are therefore out of date.

## Method
Descriptive statistics from Kaiko's trade and order-book data: share of BTC volume by hour and by weekday versus weekend, average 1% market depth, and bid-ask spreads, compared across quarters. No formal tests and no detailed methodology are given.

## Data and sample
BTC spot markets on the exchanges that feed US ETF benchmarks (named as Bitstamp, Coinbase, itBit, Kraken, Gemini and LMAX Digital) plus Binance. Mostly Q4 2023 versus Q1 2024, with multi-year comparisons back to 2019 for the weekend share.

## Reported results
- The 3pm to 4pm New York fixing window accounted for over 6.7% of all BTC volume in Q1 2024, up from 4.5% in Q4 2023.
- Weekday volume between 20:00 and 21:00 UTC exceeded $17.6 billion in Q1 2024, making it the second most active hour after 15:00 UTC.
- On benchmark exchanges the US close was over 6.6% of weekday volume and just over 4% at weekends, with no clear clustering at weekends.
- Coinbase volume in the fixing window rose to an average of $220 million.
- Weekend share of BTC volume was 16% in 2024, down 12 percentage points from a 28% peak in 2019; the decline accelerated after the ETF launch.
- US exchanges' share of 1% market depth rose to 45% from 35% a year earlier.
- Spreads on Coinbase, Bitstamp and Kraken narrowed after launch, widened in March 2024, and declined again in Q2.
- Kaiko warns that concentration could raise volatility outside US hours.

## Signal construction
Not a directional signal as published. Two features follow from it: (1) a flag for the US benchmark window (15:00 to 16:00 New York, converted to UTC with daylight saving) on NYSE trading days, with expected volume and volatility raised; (2) a weekend or US-holiday flag with lower expected depth. A testable extension is to measure whether ETF creation or redemption days (known after the close) leave a signed footprint in the fixing window on the next day.

## Relevance to SOL perpetuals at minutes to hours
SOL follows BTC at these horizons, so the BTC fixing window is a scheduled volatility event for SOL as well. Spot SOL ETFs came later than this report, so a SOL-specific fixing effect has to be measured, not assumed. The weekend finding matters for Kalshi: thin weekend books on lead venues mean larger moves per unit of flow and less reliable lead-lag signals.

## Caveats
A vendor blog with thin methodology, no significance tests and a short post-launch window that coincided with a strong rally and record volumes, so some of the Q1 2024 shift may be cyclical. Kaiko sells the data. The post covers BTC spot only: no perpetuals, no altcoins. Figures were read from the web page text; charts were not examined.
