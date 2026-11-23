---
title: "Intraday Patterns in the Cross-section of Stock Returns"
authors: "Heston, Steven L.; Korajczyk, Robert A.; Sadka, Ronnie"
year: 2010
venue: "Journal of Finance 65(4), 1369-1407 (arXiv:1005.3535 preprint read)"
url: "https://arxiv.org/pdf/1005.3535"
pdf: "sources/11-intraday-seasonality-tradfi/heston-2010-intraday-patterns-cross-section-returns.pdf"
access: "full-text"
source_type: "peer-reviewed"
evidence_grade: "A"
topic: "11-intraday-seasonality-tradfi"
asset_class: "equities"
horizon: "minutes"
tags: "return-periodicity, same-time-of-day, cross-section, reversal, execution-timing, order-flow-persistence"
---

## Key insight
A stock's half-hour return predicts its return in the same half-hour on later days: continuation appears at lags that are exact multiples of one trading day and lasts at least 40 trading days. At non-daily lags the relation is negative (short-term reversal from temporary liquidity imbalances and bid-ask bounce). The authors attribute the periodicity to persistent institutional flows executed on repeating intraday schedules.

## Method
The trading day is split into 13 half-hour intervals. For each lag k, cross-sectional regressions r(i,t) = a(k,t) + g(k,t) * r(i,t-k) + u(i,t) are run every interval (Jegadeesh 1990 style) and the slopes averaged over time; a joint regression with lags 1 to 65 is also estimated. Decile long-short portfolios are formed on the return at the same interval on prior days ("daily" strategy) versus the other intervals of the prior day ("nondaily"). Volume, order imbalance, volatility and spreads are tested as explanations.

## Data and sample
NYSE-listed common stocks matched to TAQ, 1,715 firms, January 2001 to December 2005, half-hour returns 9:30 to 16:00. Overnight moves are excluded.

## Reported results
- Return responses are negative for the first several lags, then positive with peaks at lags 13, 26, 39 and so on.
- Top-minus-bottom decile spread at the same time next day: 3.01 basis points per half-hour. The Day 1 daily spread earns over 11 bp in the opening half-hour and over 8 bp near the close, about 1.75 bp mid-day.
- Excluding low-priced stocks: 1.93 bp (t = 10.34); another filter reported 2.45 bp (t = 18.44).
- Nondaily (reversal) sort loses roughly 1.5 to 3 bp per half-hour.
- After paying spreads the long-short strategies lose money (about -24 bp); the paper frames the value as execution timing, worth roughly the effective spread.
- Volume and changes in order imbalance show the same periodicity but do not explain the return pattern. The effect is not confined to a weekday, month, turn of month, or size group, and is strongest post-decimalization.

## Signal construction
For asset i at bucket b on day d: signal = average of r(i, b, d-1 ... d-K), K from 1 to about 40, cross-sectionally demeaned. A single-asset analogue is the average demeaned return of the same clock bucket over the past K days. Update once per bucket. The reversal leg uses the prior few buckets.

## Relevance to SOL perpetuals at minutes to hours
The mechanism (scheduled algorithmic execution, persistent flows at fixed clock times) plausibly exists in crypto through TWAP bots, funding-time rebalancing and fixed-time ETF or benchmark flows. The paper's effect is cross-sectional and market-neutral; a single-instrument time-series version is a different claim and must be tested directly. The magnitudes (a few bp per half-hour) are below typical perp taker costs, so the realistic use is entry timing or a small tilt, not a stand-alone trade.

## Caveats
Five years of US equities; gross returns only; unprofitable after spreads by the authors' own test. Crypto-specific tests of this pattern belong to topic 10. No evidence here for a single 24-hour instrument.
