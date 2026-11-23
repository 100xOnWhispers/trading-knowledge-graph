---
title: "High Frequency Lead/lag Relationships - Empirical facts"
authors: "Huth, Nicolas; Abergel, Frederic"
year: 2014
venue: "Journal of Empirical Finance (arXiv:1111.7103 version of January 2012 read)"
url: "https://arxiv.org/abs/1111.7103"
pdf: "sources/21-cross-asset-lead-lag/huth-2014-high-frequency-lead-lag-empirical-facts.pdf"
access: "full-text"
source_type: "peer-reviewed"
evidence_grade: "A"
topic: "21-cross-asset-lead-lag"
asset_class: "equities"
horizon: "seconds"
tags: "lead-lag, hayashi-yoshida, cross-correlation, lead-lag-ratio, index-futures, liquidity, intraday-profile"
---

## Key insight
Cross-asset lead-lag at tick frequency is real, asymmetric and explained by liquidity: the more liquid instrument (index future, heavily traded stock) leads the less liquid one by roughly a second. The lead predicts the sign of the lagger's next mid-quote move about 60% of the time, yet a market-order strategy loses money because the predicted move is smaller than the bid-ask spread. The effect vanishes at larger time scales and is strongest after large moves of the leader.

## Method
Hayashi-Yoshida cross-correlation computed on raw, asynchronous ticks: rho(l) is the HY covariance of X with Y shifted by lag l, normalized by realized volatilities, on a lag grid from 0.01 s to 300 s. Lead-lag is summarized by three indicators:

- Lead/Lag Ratio: LLR = sum_i rho^2(l_i) / sum_i rho^2(-l_i) over positive lags; LLR > 1 means X leads Y. The paper derives it from comparing the residual variance of regressing Y on lagged X with the reverse, and links it to Granger causality.
- Maximum lag: the lag at which rho peaks.
- Maximum correlation.

A surrogate test rules out artefacts: synchronous correlated Brownian motions sampled at the true timestamps give LLR = 1. The authors show the previous-tick estimator, unlike HY, is biased toward "the more active asset leads". A thresholded version conditions on leader moves of at least theta ticks. Forecast backtest: predict the sign of the lagger's next mid-quote change from a rho-weighted sum of past leader returns, with rho estimated on the previous 20 trading days.

## Data and sample
Reuters tick data (trades and quotes, millisecond stamps), 1 March to 31 May 2010: CAC40 stocks, a few other European large caps, and CAC40, FTSE100, SMI and DAX index futures. First and last half hour dropped. Backtest: 44 test days (29 March to 31 May 2010).

## Reported results
- CAC40 future versus Total: LLR 2.12, peak at 0.6 s. CAC40 future versus SMI future: LLR 1.26, peak 0.2 s, under 5% correlation at 30 s. Renault versus Peugeot: LLR 1.15, peak 0.95 s. Nestle leads the SMI future (LLR 0.69, peak 17 s, unstable).
- Average LLR about 2.2 for future/stock pairs and about 1.2 for stock/stock pairs.
- Leaders have shorter inter-trade durations, larger turnover per trade, narrower spreads and lower volatility; the highest correlations are between assets of similar liquidity.
- Intraday: the future leads stocks all day; the lag shortens at 14:30 and 16:00 CET (US macro releases) and 15:30 CET (US open).
- LLR and peak correlation rise with the size of the leader's move.
- Forecast accuracy 60.3% (Total) and 63.6% (Essilor) versus 56.7% and 59% using the lagger's own autocorrelation. At mid-quote execution the gain is 0.4 and 0.54 bps per trade; with the spread it is -2.73 and -3.44 bps per trade. Accuracy deteriorates when predicting over larger tick-time scales.

## Signal construction
Offline monitor: for leader L (for example Binance BTCUSDT or SOLUSDT perp, or CME equity index futures) and target T, compute the HY cross-correlation on a lag grid from 50 ms to 300 s over rolling windows, then LLR, peak lag and peak correlation, by hour of day. Live feature: rho-weighted sum of the leader's returns over lags up to the last significant lag, optionally only when the leader has moved more than a threshold. Use it to time passive orders or to skew quotes, not to cross the spread.

## Relevance to SOL perpetuals at minutes to hours
The qualitative laws should transfer: BTC and the largest SOL venues are the liquid leaders, a thin Kalshi SOL perp the lagger, and the lead is likely to concentrate after large leader moves and around US data releases. The main lesson is negative for a minutes-to-hours bot: the paper finds little cross-correlation beyond tens of seconds between liquid instruments, so a pure lead-lag edge sits below the bot's horizon and below the spread.

## Caveats
Three months of 2010 European equity data; markets are faster now. Costs are the spread only, no fees or queue modelling. The 60% hit rate is at next-tick horizon. No crypto data.
