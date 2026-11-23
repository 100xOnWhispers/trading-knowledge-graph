---
title: "Aligning Cryptocurrency Derivatives with Spot Markets: Measuring the 24/7 Trading Opportunity"
authors: "CME Group (individual author not named)"
year: 2026
venue: "CME Group article, syndicated on Yahoo Finance, 20 April 2026"
url: "https://finance.yahoo.com/markets/crypto/articles/aligning-cryptocurrency-derivatives-spot-markets-123000728.html"
pdf: "none"
access: "full-text"
source_type: "industry-research"
evidence_grade: "C"
topic: "10-intraday-seasonality-crypto"
asset_class: "crypto"
horizon: "daily"
tags: "cme-gap, weekend-volatility, 24-7-trading, parkinson-estimator, regime-change, weekend-effect"
---

## Key insight
CME announced that its crypto futures and options would trade around the clock from 29 May 2026, ending the Friday-to-Sunday closure that created the "CME gap". The supporting analysis shows that Bitcoin's weekend volatility has run at roughly 75% of weekday volatility since 2020, with occasional weekend shocks far larger than the weekday norm. From mid-2026 the weekend gap is a legacy feature, and any seasonal model built on CME hours needs a structural break at that date.

## Method
Descriptive comparison of Bitcoin volatility in weekday (CME-open) and weekend (CME-closed) intervals, using the Parkinson high-low estimator scaled to a 24-hour equivalent, with yearly means, medians and interquartile ranges, plus one case study of a weekend gap.

## Data and sample
BTC/USD on Bitstamp, 1 January 2020 to 8 March 2026; the gap chart is from TradingView.

## Reported results
- Average daily move 2020 to 2026: 3.10% on weekdays, 2.33% at weekends. Medians: 2.66% and 1.91%. Weekend interquartile range: 1.21% to 2.91%.
- Mean daily volatility peaked in 2021 at 5.27% (weekdays) and 4.46% (weekends); weekend readings have stayed at about 75% of weekday levels.
- 10 October 2025: weekend-interval volatility of 7.83% against 2.14% earlier that day during regulated hours, more than three times the 2025 weekday average of 2.54%.
- 13 March 2020: 36.01% in the weekday session and 17.85% in the weekend interval.
- Gap example: after the US Strategic Crypto Reserve announcement on 2 March 2025, a gap of about $10,000 had opened in Bitcoin futures when trading resumed.
- No statistics on gap frequency, average gap size or gap-fill rates are given. The article states that weekend price discovery "remains robust" while CME is closed.

## Signal construction
Not a signal. It gives two inputs for the bot's calendar: (1) a weekend volatility factor of roughly 0.75 for BTC as a starting prior, to be re-estimated for SOL; (2) a regime date, 29 May 2026, after which features such as "CME closed", "CME Sunday reopen at 22:00 or 23:00 UTC" and "open CME gap above or below price" stop being generated. Any backtest of a gap-fill rule can only use data before that date.

## Relevance to SOL perpetuals at minutes to hours
CME also lists SOL futures, so the same closure applied to SOL until May 2026. For a Kalshi SOL perp bot the consequences are: the Sunday-evening reopen burst (first UTC hour of Monday is especially volatile in the Hansen note) may fade or move; weekend basis and lead-lag relations now include a regulated venue; and weekend liquidity may improve. All three are open empirical questions with only about six months of post-change data.

## Caveats
Written by the exchange to promote a product, with no formal tests. The launch was described as "pending regulatory review" in the article; a separate news report read in this session (BeInCrypto via Yahoo Finance, 31 May 2026) states that 24/7 trading began on 29 May 2026 and cites, without a source, historical gap-fill rates of "70% to more than 90%". That fill-rate claim is folklore-grade: most price levels are revisited eventually, so a high fill rate without a time limit carries little information. CME's own site blocked automated access, so the syndicated copy was read.
