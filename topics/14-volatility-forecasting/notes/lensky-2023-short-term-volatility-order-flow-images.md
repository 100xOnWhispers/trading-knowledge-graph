---
title: "Learning to Predict Short-Term Volatility with Order Flow Image Representation"
authors: "Lensky, Artem; Hao, Mingyu"
year: 2023
venue: "arXiv preprint 2304.02472 (v2, March 2024)"
url: "https://arxiv.org/pdf/2304.02472"
pdf: "sources/14-volatility-forecasting/lensky-2023-short-term-volatility-order-flow-images.pdf"
access: "full-text"
source_type: "working-paper"
evidence_grade: "C"
topic: "14-volatility-forecasting"
asset_class: "crypto"
horizon: "seconds"
tags: "cnn, order-flow, limit-order-book, short-term-volatility, perpetual-futures, binance, deep-learning"
---

## Key insight
The realized volatility of the Binance BTC/USDT perpetual over the next 60 seconds can be predicted better from the last four minutes of order flow (trade sizes, trade directions and limit order book) than from the last minute's volatility alone or from a GARCH model. A small convolutional network reading the order flow as an image, supplemented with hand-crafted aggregate features, gave the lowest error. Persistence is a strong baseline that is sometimes hard to beat.

## Method
Order flow over a fixed window is rasterised into a 240 by 240 image: the horizontal axis is time in seconds (four minutes), the vertical axis is price offset (a 240 USDT range), and colour channels encode executed trade size by direction and resting limit order book quantities. Images are generated walk-forward every 10 seconds, so neighbours overlap by 230 seconds. Models: a simple 3-layer CNN, pretrained ResNet-18 and ConvMixer, each optionally concatenated with per-second hand-crafted features (volume-weighted trade price, trade count, traded volume and similar); an MLP on the features alone; a 1-D CNN on raw data; GARCH; and a naive forecast equal to the last minute's realized volatility. Target: realized volatility over the next 60 seconds. Metric: root mean square percentage error (RMSPE). Data are split in time order 3:1:1 into train, validation and test.

## Data and sample
Binance public historical data for the BTC/USDT perpetual futures contract: tick-level trades and 20 levels of the limit order book on each side, January 2021.

## Reported results
- CNN with aggregated features: RMSPE 0.85 plus or minus 1.1. CNN without the feature supplement: 1.0 plus or minus 1.4. ConvMixer with features follows closely.
- Naive last-minute forecast: RMSPE 1.4 plus or minus 3.0, with much higher dispersion.
- The naive guess sometimes outperforms more complex models, which the authors attribute to minute-level volatility being stable for stretches of the day.
- The MLP on hand-crafted features beats the naive guess but not the image-based CNN.
- The pretrained image networks did not clearly beat the small CNN trained from scratch.

## Signal construction
A very-short-horizon volatility nowcast: inputs are the last 240 seconds of trades (signed size, price) and book depth around the mid from the reference perp; output is expected realized volatility over the next 60 seconds; update every 10 seconds. A cheaper approximation suggested by the results is a gradient-boosted or linear model on the per-second aggregates (trade count, volume, signed volume, spread, depth), benchmarked against the persistence forecast.

## Relevance to SOL perpetuals at minutes to hours
Useful mainly at the execution layer: deciding whether the next minute is calm enough to enter passively, or setting a stop buffer. It confirms that order-flow and book information adds to price-only volatility forecasts on a perpetual contract. The 60-second target is shorter than the bot's holding period, the 240 USDT fixed price range is specific to BTC's price level in 2021, and the image approach is heavy for the gain shown.

## Caveats
One month of data in one of the most volatile periods on record, one instrument, and error bars as large as the means. No comparison with HAR on intraday RV. RMSPE penalises errors in quiet periods heavily. Overlapping samples make the effective test size much smaller than the image count. Preprint.
