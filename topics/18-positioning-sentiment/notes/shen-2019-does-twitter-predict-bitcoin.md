---
title: "Does twitter predict Bitcoin?"
authors: "Shen, Dehua; Urquhart, Andrew; Wang, Pengfei"
year: 2019
venue: "Economics Letters (accepted manuscript deposited on Zenodo)"
url: "https://zenodo.org/record/3404138"
pdf: "sources/18-positioning-sentiment/shen-2019-does-twitter-predict-bitcoin.pdf"
access: "full-text"
source_type: "peer-reviewed"
evidence_grade: "B"
topic: "18-positioning-sentiment"
asset_class: "crypto"
horizon: "daily"
tags: "twitter-volume, investor-attention, realized-volatility, trading-volume, granger-causality, bitcoin"
---

## Key insight
The number of tweets mentioning Bitcoin predicts next-day realized volatility and trading volume, but not next-day returns. Tweet volume is a risk and activity forecast, not a direction forecast. The paper is the main peer-reviewed counterweight to claims that social attention predicts price direction at the daily horizon.

## Method
Three bivariate VAR(k) models, each pairing log tweet count with one of: log realized volatility, log trading volume, log return. Lag length chosen by the Schwarz criterion. Linear Granger causality tests and the nonlinear Diks-Panchenko test are applied to each pair. Realized volatility is the sum of squared 5-minute log returns within the day. A Bai-Perron break test splits the sample for a stability check.

## Data and sample
Daily count of tweets containing "Bitcoin" from bitinfocharts.com, 4 September 2014 to 31 August 2018. Bitstamp tick data from bitcoincharts.com aggregated to 5-minute and daily bars. Subsamples: 4 September 2014 to 8 October 2017, and 9 October 2017 to 31 August 2018.

## Reported results
- Previous-day tweets significantly raise next-day realized volatility; both linear and nonlinear tests reject non-causality. The relation is bilateral: realized volatility also predicts tweets.
- Previous-day tweets significantly predict next-day trading volume, again bilaterally.
- For returns, the VAR coefficient is only weakly significant (10% level); the text describes it as weak evidence "that less tweets have a relationship [with] next day returns", which suggests a negative sign but the coefficient table was not legible in the copy read. The Granger tests do reject non-causality. The conclusion section states plainly that tweets drive volatility and volume "but not returns". Past returns do not predict tweets.
- Subsamples: in the first period tweets predict volume but not volatility; in the second period (from October 2017) tweets predict both.
- The authors argue tweet volume reflects more informed attention than Google Trends, which they associate with uninformed attention. This is asserted, not tested.

## Signal construction
Inputs: hourly or daily count of posts mentioning the asset. Compute `a_t = log(count_t)` and its change or z-score against a trailing window. Use as a feature in a volatility and volume forecast (for position sizing, stop distance, and expected slippage), not as a directional input. Update at the feed frequency.

## Relevance to SOL perpetuals at minutes to hours
Directly useful for risk: a spike in SOL-related post volume should widen expected range for the next period. The paper tests daily data only, so the hourly lead from posts to volatility needs re-testing; the bilateral causality suggests that at short horizons posts mostly react to moves. The X (Twitter) API changed materially after this sample, so the data source must be replaced and re-validated.

## Caveats
Four-page letter with in-sample tests only. Raw counts include bots and spam (see Kraaijeveld and De Smedt 2020 in this folder). The return result is internally mixed between the coefficient test and the Granger test, and the significant volatility relation is confined to the subsample from October 2017, which covers the bubble peak and its aftermath.
