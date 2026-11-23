---
title: "Order Block (OB) Statistics: Real Win Rate vs Random Levels"
authors: "algolego (TradingView account)"
year: 2026
venue: "TradingView open-source script description (posted 17 August; year inferred from the data window)"
url: "https://www.tradingview.com/script/yFmy3VBi-Order-Block-OB-Statistics-Real-Win-Rate-vs-Random-Levels/"
pdf: "none"
access: "full-text"
source_type: "practitioner"
evidence_grade: "C"
topic: "17-auction-orderflow-practitioner"
asset_class: "multi"
horizon: "minutes"
tags: "order-block, ict, break-of-structure, placebo-control, random-levels, negative-result"
---

## Key insight
Order blocks, defined as the last opposite candle before a break of structure, did not outperform matched random zones on BTCUSDT, EURUSD or the E-mini S&P future. Across 23 distinct estimates the mean difference in hit rate was slightly negative and every combined confidence interval included zero. A synthetic test also shows how drift alone can make long-side zones "win" about 60% of the time against a 50% benchmark with no edge at all.

## Method
As described on the page (read through a summarizing tool; wording is paraphrased). A swing high or low is confirmed a fixed number of bars after it forms. A break of structure is a close beyond the most recent unbroken swing. The order block is the last candle before the break that moved the other way (last down candle before an upward break, last up candle before a downward break). The zone becomes visible only at the confirmation bar; the first touch test is on the following bar. Inputs include swing length, search depth, full range or body, minimum displacement in ATR. Outcome: target reached before stop, with barriers at a multiple of a risk unit (ATR or zone height); entry at the close of the bar that returns to the zone's near edge; bars touching both barriers count against; time-limited zones are censored and reported separately. Controls: zones at bars without an order-block event, matched in height, direction and distance from price, with the same one-bar delay. Edge = real minus control hit rate, with z-score and 95% interval. The method is also run on synthetic series with no edge, with and without drift.

## Data and sample
BTCUSDT, EURUSD and ES1!; four timeframes, three periods (the 2025-26 rows run 1 January 2025 to 1 August 2026), three barrier widths, eight definition variants; 31 runs giving 23 distinct estimates. One example chart (BTCUSDT 30-minute) scores 1,854 zones; the total event count is not given.

## Reported results
- Baseline hit rate for neutral control levels: 47.3% to 52.3% overall, 43.3% to 54.6% when split by direction.
- Mean of the 23 estimates: -0.87 percentage points (15 negative, 7 positive, 1 zero); the same pipeline on no-edge synthetic data returns -0.44.
- Balanced pool: -2.10 points, z = -1.91, 95% interval -4.3 to +0.1.
- EURUSD 30-minute single run: -4.9 points (z = -2.69); BTCUSDT +0.1; ES +0.8. The EURUSD result did not replicate across its two periods (combined -1.23, z = -0.55).
- Requiring a 2 ATR displacement: 46.7% against 50% looks negative (z = -1.83) but is -0.6 points against its control (z = -0.29).
- Synthetic drift test with no edge: long side 59.6% (z = +5.33), short side 38.8% (z = -5.89) against 50%; difference against matched control 0.0.
- Stated resolution: differences under about 1.2 points cannot be separated from noise in the pooled sample; a single run detects only about 3 points or more.

## Signal construction
Not a signal. It gives a causal, codable order-block definition (useful because the popular Python package leaves the rule vague) and a validation recipe that includes a synthetic no-edge run as a pipeline check. For the bot: distance to the nearest unmitigated order block may be offered as a feature, but the prior from this study is zero incremental value.

## Relevance to SOL perpetuals at minutes to hours
BTCUSDT at intraday bars is in the sample and shows an edge of about zero. The drift result is the practical warning for crypto, which trends strongly: any long-biased zone method will post flattering win rates in a bull phase. A SOL replication should pool several periods with opposite drift and report only real-minus-control.

## Caveats
Pseudonymous TradingView author, not peer-reviewed, tables partly not visible to me. The control does not match recent move strength, so long and short splits differed by up to 10.9 points in trends. Order blocks are rare, so power is limited. Costs excluded. Other order-block definitions (with volume or imbalance filters) are untested. Year not shown on the page.
