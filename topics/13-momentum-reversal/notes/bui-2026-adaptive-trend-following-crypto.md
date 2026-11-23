---
title: "Systematic Trend-Following with Adaptive Portfolio Construction: Enhancing Risk-Adjusted Alpha in Cryptocurrency Markets"
authors: "Bui, Duc; Nguyen, Thanh"
year: 2026
venue: "arXiv preprint 2602.11708"
url: "https://arxiv.org/pdf/2602.11708"
pdf: "sources/13-momentum-reversal/bui-2026-adaptive-trend-following-crypto.pdf"
access: "full-text"
source_type: "working-paper"
evidence_grade: "C"
topic: "13-momentum-reversal"
asset_class: "crypto"
horizon: "hours"
tags: "trend-following, perpetuals, six-hour-bars, trailing-stop, atr, binance-futures, long-short"
---

## Key insight
A recent practitioner paper claims that trend following on 6-hour bars of Binance perpetual contracts, with a volatility-calibrated trailing stop, monthly re-selection of assets and a 70/30 long-short capital split, earned a Sharpe ratio of 2.41 out of sample over 2022 to 2024. Its most relevant claim for this repository is that an intermediate bar size beats both hourly and daily bars for crypto trend signals once costs are counted. The evidence is thin and the design has several overfitting channels.

## Method
Entry: rate of change over a look-back L, `MOM = (P(t) - P(t-L)) / P(t-L)`, long when MOM exceeds a threshold that is re-optimised monthly, short when MOM is below the negative of that threshold. Exit: a trailing stop `S(t) = max(S(t-1), P(t) - alpha * ATR(t))` for longs, with ATR the average true range over k bars. Monthly, the universe is filtered by market capitalisation (long candidates from the top, short candidates from the bottom), then each asset's parameters are grid-searched on the preceding month and assets are kept only if their trailing Sharpe ratio passes a threshold (a higher one for shorts). Capital is split 70% long, 30% short. Costs: 4 basis points taker fee per trade, a linear slippage model scaled by trade size against 5-minute volume, and funding payments on perpetual positions. Benchmarks: 1-month and 3-month time-series momentum and buy-and-hold portfolios.

## Data and sample
Binance Futures, 150+ perpetual swap contracts, 6-hour OHLCV bars, January 2021 to December 2024. In-sample: 2021. Out-of-sample: January 2022 to December 2024 (36 months). One figure caption refers to a period ending October 2025, an internal inconsistency.

## Reported results
- AdaptiveTrend (70/30): annualised Sharpe 2.41, maximum drawdown -12.7%, Calmar 3.18, annualised return 40.5% (as extracted from the results table).
- The 70/30 split beats a dollar-neutral 50/50 split by 0.29 in Sharpe.
- Ablation: the text says the dynamic trailing stop "contributes the most", improving Sharpe by 0.73, and calls monthly parameter optimisation "second most impactful" with a Sharpe change of 1.07. The two statements are inconsistent as written.
- Bear-market performance is described as near flat (-4.2% annualised).
- Sharpe stays above 2.0 at 8 basis points per trade.
- Bar-size comparison at 4 basis points: 1-hour and 4-hour bars suffer from turnover; 8-hour, 12-hour and daily bars miss short-lived moves; 6-hour is reported as best.

## Signal construction
On each closed bar: compute rate of change over L bars and ATR over k bars. Enter long if rate of change > threshold; maintain a ratcheting stop at price minus alpha times ATR; exit on a close below the stop. Mirror for shorts. Parameters L, threshold, k and alpha are re-fitted on a rolling window.

## Relevance to SOL perpetuals at minutes to hours
One of the few sources that tests trend rules on perpetual contracts, includes funding in costs, and compares bar sizes inside the minutes-to-hours band. The suggestion that multi-hour bars are the trend sweet spot, and that the trailing stop matters more than the entry, is a hypothesis to test on SOL with the bot's own cost model. The paper argues that 6-hour bars align with a four-times-daily funding cycle; that does not match an 8-hour funding schedule such as Kalshi's, so the bar-size conclusion should not be carried over without re-testing.

## Caveats
Grade C. Authors are affiliated with a trading research firm; not peer-reviewed; six pages. Monthly per-asset grid search plus Sharpe-based asset selection is a strong data-mining channel, and the ablation shows most of the performance depends on it. The "optimal" 6-hour bar is itself selected on the test period. Short legs in bottom-capitalisation perpetuals face liquidity and squeeze risk not captured by a linear slippage model. No code or replication seen.
