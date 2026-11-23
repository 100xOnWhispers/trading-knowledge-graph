---
title: "The intraday dynamics of bitcoin"
authors: "Eross, Andrea; McGroarty, Frank; Urquhart, Andrew; Wolfe, Simon"
year: 2019
venue: "Research in International Business and Finance, 49, 71-81"
url: "https://centaur.reading.ac.uk/81745/3/2.R%26R.Manuscript.pdf"
pdf: "sources/10-intraday-seasonality-crypto/eross-2019-intraday-dynamics-bitcoin.pdf"
access: "full-text"
source_type: "peer-reviewed"
evidence_grade: "B"
topic: "10-intraday-seasonality-crypto"
asset_class: "crypto"
horizon: "minutes"
tags: "intraday-seasonality, hour-of-day, volume, realized-volatility, amihud-illiquidity, bitstamp, granger-causality"
---

## Key insight
The first systematic description of Bitcoin's intraday profile. Volume and realised volatility on Bitstamp follow an FX-like shape tied to European and North American business hours, and illiquidity is concentrated in the early GMT morning. The shape was stable across four separate calendar years, while the levels of volume, volatility and liquidity moved a lot.

## Method
Tick trades are aggregated into 5-minute bars. Four variables per bar: log return (times 100), squared log return as realised volatility, traded volume, and the Amihud ratio |r| / dollar volume as illiquidity. Intraday patterns are shown graphically by year and tested with a GARCH(1,1) regression of each variable on 288 five-minute-of-day dummies plus a lagged term. Cross-correlations at leads and lags of up to 10 bars and Granger causality tests with up to ten lags describe how the four variables interact.

## Data and sample
BTC/USD trades on Bitstamp from bitcoincharts.com, 1 January 2014 to 31 December 2017, split into four yearly subsamples, all timestamps in GMT. The authors say BTC-e gives similar results (not reported).

## Reported results
- Volume is low until about 07:00 GMT, rises until about 10:30, peaks again around 14:00 and then decays through the rest of the day. (The abstract says the decline starts "around 4pm"; the conclusion says "around 2pm".)
- Realised volatility is highest from 07:00 and declines after 18:00 GMT.
- Amihud illiquidity is highest at the beginning of the GMT day; liquidity is best from about 10:00 onwards. Liquidity improved each year.
- The patterns are described as consistent across 2014, 2015, 2016 and 2017.
- Mean 5-minute return was negative in 2014 and rose each year to 0.0025 in 2017. Mean 5-minute volume was 48.65, 54.58, 19.50 and 44.81 BTC in 2014 to 2017.
- Bidirectional Granger causality among returns, volatility and volume in every year. The volatility-volume F-statistic rose from 13.17 (2014) to 746.02 (2017). No causality between liquidity and returns or volatility.
- Returns and volatility are negatively correlated from 2015 onward; volume and volatility are positively correlated in all years, which the authors read as support for the mixture-of-distributions hypothesis.

## Signal construction
Not a directional signal. It supplies an expected-activity curve: for each 5-minute slot of the UTC day, keep a rolling median of volume, squared return and |r|/volume over the last N days. Use the ratio of live value to slot baseline as a "surprise" feature, and use the baseline itself to scale stop distances, position size and expected slippage by time of day.

## Relevance to SOL perpetuals at minutes to hours
The qualitative shape (quiet Asian morning, build-up through the European morning, peak around the US open) is the same shape later found on Binance and Coinbase and across hundreds of altcoin pairs (see the Hansen and Brauneis notes), so it very likely applies to SOL. The clock times will have shifted: this sample predates Binance, perpetual futures dominance, CME futures and spot ETFs. Re-estimate on SOL-USDT perp data from the lead venues.

## Caveats
Single spot exchange, 2014 to 2017, a retail-era market. No return seasonality is shown to be tradable; the paper reports patterns only where they were "discernible". Squared 5-minute returns are a noisy volatility measure. No out-of-sample test and no cost analysis.
