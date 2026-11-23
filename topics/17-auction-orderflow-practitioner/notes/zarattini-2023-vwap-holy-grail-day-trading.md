---
title: "Volume Weighted Average Price (VWAP): The Holy Grail for Day Trading Systems"
authors: "Zarattini, Carlo; Aziz, Andrew"
year: 2023
venue: "Working paper dated 13 November 2023 (SSRN 4631351; copy hosted by Concretum Research)"
url: "https://concretumgroup.com/volume-weighted-average-price-vwap-the-holy-grail-for-day-trading-systems/"
pdf: "sources/17-auction-orderflow-practitioner/zarattini-2023-vwap-holy-grail-day-trading.pdf"
access: "full-text"
source_type: "working-paper"
evidence_grade: "C"
topic: "17-auction-orderflow-practitioner"
asset_class: "equities"
horizon: "minutes"
tags: "vwap, intraday-trend, day-trading, qqq, session-anchor, moving-average-comparison"
---

## Key insight
The side of the session VWAP on which price trades carried directional information for QQQ in 2018-2023: minutes that began above VWAP summed to large gains and minutes that began below to large losses. A stop-and-reverse rule on one-minute closes across VWAP produced strong backtested returns and beat the same rule built on simple moving averages. It is the only quantitative test of "VWAP as a reference level" found for this topic, and the authors themselves call it exploratory.

## Method
VWAP = sum(HLC_t * Volume_t) / sum(Volume_t), with HLC the average of the minute's high, low and close, accumulated from the 9:30 ET open (pre-market excluded). At 9:31 go long if the first one-minute close is above VWAP, short if below. Reverse whenever a one-minute candle closes on the other side. Flat at the 16:00 close. Size is 100% of equity, no leverage (the TQQQ variant gets 3x through the product). Commission $0.0005 per share; slippage assumed zero. A "placebo" comparison replaces VWAP with SMA 9, 20, 100 and 200.

## Data and sample
One-minute OHLCV for QQQ and TQQQ, 2 January 2018 to 28 September 2023 (IQFeed and Interactive Brokers), regular hours.

## Reported results
- About 56% of one-minute candles closed above VWAP. Summed one-minute changes: about +$320 per share while above VWAP and about -$280 while below.
- QQQ strategy: $25,000 to $192,656; total return 671%; 43% a year; volatility 18%; Sharpe 2.1; maximum drawdown 9.4%. Buy and hold: 126%, 15% a year, Sharpe 0.7, drawdown 37%.
- Annualized alpha 38% (t above 5); beta not different from zero.
- TQQQ: 8,242% total, 116% a year, volatility 54%, drawdown 36.1%, Sharpe 1.7.
- About 22,000 trades; hit ratio about 17%; average gain 5.5 times average loss. Commissions $6,547 (QQQ) and $400,616 (TQQQ).
- Worst day -5.1% (QQQ), on a mean-reverting day with many false crosses.
- The VWAP version beat all four SMA versions on return and drawdown.

## Signal construction
Session VWAP needs an anchor. For a 24-hour perp, candidates are 00:00 UTC, the 8-hour funding timestamps, and the US cash open. Compute VWAP_a(t) for each anchor from one-minute typical price and volume on the lead venue. Features: sign and volatility-scaled size of (price - VWAP_a), time since anchor, number of crosses since anchor (a chop measure). Anchored VWAP from an event bar (a swing extreme, a liquidation flush) uses the same formula with a different start; the practitioner page I read on it (StockCharts ChartSchool) gives no evidence. Anchor choice is a free parameter and an obvious target for a bandit or a small evolutionary search, with the placebo comparison against plain moving averages kept as a guard.

## Relevance to SOL perpetuals at minutes to hours
The idea transfers; the economics do not. The idea transfers; the economics do not. By my arithmetic the backtest makes roughly fifteen trades a day (22,000 trades over about 1,450 sessions) with a 17% hit rate, which is viable only when the cost per trade is near zero. At 5 basis points per round trip, 22,000 trades would sum to about 1,100% of traded equity, enough to overwhelm the reported edge. On SOL perps the rule would need a wide no-trade band around VWAP, or use as a regime feature and not as an entry trigger. Crypto has no session open or close, and the institutional VWAP-benchmarked flow that the authors cite as a reason VWAP matters in equities is probably much smaller.

## Caveats
Single underlying, in-sample, less than six years, no slippage, no spread. Authors are a research boutique and a day-trading educator, both with commercial interest. The title overstates; the paper says it is not a finished system. No multiple-testing adjustment.
