---
title: "BitCoin meets Google Trends and Wikipedia: Quantifying the relationship between phenomena of the Internet era"
authors: "Kristoufek, Ladislav"
year: 2013
venue: "Scientific Reports 3:3415"
url: "https://www.nature.com/articles/srep03415.pdf"
pdf: "sources/18-positioning-sentiment/kristoufek-2013-bitcoin-google-trends-wikipedia.pdf"
access: "full-text"
source_type: "peer-reviewed"
evidence_grade: "B"
topic: "18-positioning-sentiment"
asset_class: "crypto"
horizon: "multi-day"
tags: "google-trends, wikipedia-views, attention, feedback-loop, asymmetry, bitcoin"
---

## Key insight
Search interest and Bitcoin price drive each other in both directions, and the sign of the attention effect depends on where price sits relative to its short-term trend. Rising interest while price is above trend pushes price higher; rising interest while price is below trend pushes it lower. Attention is therefore an amplifier of the prevailing move, not a directional signal on its own.

## Method
Log-log analysis of price and search series. Stationarity tested with KPSS and ADF; cointegration with Johansen trace and likelihood tests. Bitcoin and Google Trends are not cointegrated, so a VAR(1) on first log differences is used with HAC standard errors. Bitcoin and Wikipedia views are cointegrated, so a VECM with seven lags is used. Impulse-response functions give the reaction to a shock. To separate "positive" from "negative" interest, the search variable is interacted with a dummy equal to one when price is above its moving average (4 weeks for Google, 7 days for Wikipedia).

## Data and sample
Bitcoin/USD on Mt. Gox from bitcoincharts.com, 1 May 2011 to 30 June 2013 (earlier data dropped as illiquid). Google Trends weekly for the query "BitCoin" (113 observations). Wikipedia daily page views (788 observations).

## Reported results
- Log price and log search volume correlate at 0.8786 (Google Trends) and 0.8271 (Wikipedia).
- A 10% shock to Google searches is followed by about a 0.8% price reaction in the first week and 1.2% in the second, then nothing. The reverse channel also holds for two periods, with a total reaction of about 0.8% (0.55% then 0.25%).
- For Google Trends, nearly all of the effect comes from the above-trend state; there is no significant reaction in the below-trend state.
- For Wikipedia, the pooled effect of views on price is insignificant, but once split by state the transmission is about +0.05 above trend and -0.05 below trend, both significant. Price changes raise Wikipedia views permanently (a 10% price change maps to a 0.5% shift in views).

## Signal construction
Inputs: an attention series `A_t` (search index, page views, or a modern substitute such as post counts) and price `P_t`.
1. `trend_t = 1 if P_t > MA_n(P) else -1`, with n equal to 4 weeks or 7 days in the paper.
2. `signal_t = trend_t * max(0, dlog A_t)`.
The signal is a conditional momentum amplifier: it scales up an existing trend-following position when attention is accelerating in the direction of the trend. Update at the frequency of the attention feed.

## Relevance to SOL perpetuals at minutes to hours
The state-dependent sign is the transferable idea and it reconciles the "attention is bullish" and "attention is contrarian" readings: attention during a sell-off is bearish. A bot can test the same interaction intraday using hourly social post counts and a short moving average on SOL. The specific elasticities do not transfer; they come from a 2011 to 2013 market with one dominant exchange.

## Caveats
Small sample (113 weekly points) covering a single bubble. Mt. Gox prices were later shown to be affected by manipulation and the exchange failed in 2014. No out-of-sample test and no trading simulation. The causality is Granger-type only; bidirectional feedback means attention may simply proxy for recent returns.
