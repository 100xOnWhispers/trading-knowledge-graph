---
title: "What are the main drivers of the Bitcoin price? Evidence from wavelet coherence analysis"
authors: "Kristoufek, Ladislav"
year: 2015
venue: "PLoS ONE (read as arXiv:1406.0268)"
url: "https://arxiv.org/pdf/1406.0268"
pdf: "sources/12-time-encodings-cycles/kristoufek-2015-bitcoin-price-drivers-wavelet-coherence.pdf"
access: "full-text"
source_type: "peer-reviewed"
evidence_grade: "B"
topic: "12-time-encodings-cycles"
asset_class: "crypto"
horizon: "multi-day"
tags: "wavelet-coherence, bitcoin, time-frequency, lead-lag, on-chain"
---

## Key insight
Wavelet coherence shows that the relationships between Bitcoin's price and its candidate drivers are neither constant in time nor the same across horizons. Fundamental variables relate to price mainly at long scales, search interest relates to price most clearly in the long run and amplifies moves in both directions during bubbles and crashes, and most short-scale relationships are brief and may be noise. It is the most cited early application of wavelets to crypto and a template for time-frequency lead-lag analysis.

## Method
Continuous wavelet transform with the Morlet wavelet. For two series the cross wavelet transform is `W_xy(u,s) = W_x(u,s) * conj(W_y(u,s))`, and squared coherence is the smoothed cross-spectrum magnitude squared divided by the product of smoothed individual powers, a number between 0 and 1 read as a local squared correlation in time and scale. The phase difference `atan(Im / Re)` of the smoothed cross-spectrum gives sign and lead or lag. Significance is by Monte Carlo against an AR(1) red-noise null, and a cone of influence marks unreliable edge regions. Partial wavelet coherence controls for a third series. Because the series are multimodal, they are transformed to quantiles before analysis, following Grinsted et al.

## Data and sample
Daily data, 14 September 2011 to 28 February 2014. CoinDesk Bitcoin Price Index (average of major USD exchanges); Blockchain.info series (supply, transactions, trade volume, hash rate, difficulty); exchange volumes; Google Trends and Wikipedia views for "Bitcoin"; Cleveland Fed Financial Stress Index; gold in Swiss francs; USD and CNY market prices and volumes.

## Reported results
- Trade-exchange ratio and price level: relationships with price are at high scales (the most stable around 128 days for the price level); a shorter significant region near one month appears between April and July 2013.
- Money supply: significant regions lie mostly outside the reliable region, with unstable phase.
- Trade transactions lead price positively at long scales, mainly in 2012, weakening afterwards; at lower scales significant regions are "only short-lived and can be due to statistical fluctuations and noise".
- Rising prices draw in miners (hash rate, difficulty), an effect that fades over time.
- Search interest drives prices up in bubbles and down in declines.
- No safe-haven behaviour; no clear evidence that the CNY market leads the USD market.

## Signal construction
Not a directly tradable signal at the paper's horizons. The transferable construction is a rolling coherence and phase feature between two series:
1. Choose a pair, for example Binance SOL perpetual returns and BTC returns, or SOL returns and open-interest changes.
2. Compute Morlet transforms on a trailing window and the coherence and phase at a few scales (for example 15 minutes, 1 hour, 4 hours).
3. Use coherence as a "relationship is on" gate and phase as a lead or lag estimate.
Only values outside the cone of influence are trustworthy, which at the live edge restricts use to scales much shorter than the window.

## Relevance to SOL perpetuals at minutes to hours
The finding that short-scale coherence is patchy and often insignificant is the relevant warning: at intraday scales, expect lead-lag structure to appear and vanish. The method is useful offline to learn at which scales a cross-venue or cross-asset relationship exists and in which periods, before building a simpler causal feature such as a lagged regression at that scale.

## Caveats
Descriptive, in-sample, daily data from 2011 to 2014, an era dominated by Mt. Gox. No forecasting or trading test. Phase interpretation is ambiguous, as the author notes: a lead in phase can be read as a lag in anti-phase. Many driver series are tested without correction for multiple comparisons. Edge effects make real-time use much weaker than the full-sample pictures suggest.
