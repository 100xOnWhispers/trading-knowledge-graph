---
title: "Assessing Measures of Order Flow Toxicity via Perfect Trade Classification"
authors: "Andersen, Torben G.; Bondarenko, Oleg"
year: 2013
venue: "CREATES Research Paper 2013-43, Aarhus University (November 2013 version; later journal publication not confirmed in this session)"
url: "https://repec.econ.au.dk/repec/creates/rp/13/rp13_43.pdf"
pdf: "sources/08-trade-flow-toxicity/andersen-2013-order-flow-toxicity-perfect-classification.pdf"
access: "full-text"
source_type: "working-paper"
evidence_grade: "B"
topic: "08-trade-flow-toxicity"
asset_class: "futures"
horizon: "hours"
tags: "vpin, trade-classification, tick-rule, bulk-volume-classification, aggressor-flag, critique"
---

## Key insight
Using best-bid-offer data to sign nearly every E-mini trade exactly, the authors show that bulk volume classification (BVC) is much less accurate than the ordinary tick rule applied trade by trade. VPIN built from true aggressor signs behaves in the opposite way to BVC-VPIN: it is negatively correlated with future volatility. BVC-VPIN forecasts volatility only because its classification errors are correlated with volume and volatility. After controlling for volume and realized volatility, no VPIN variant has incremental forecast power.

## Method
Trades are signed by comparing each trade price with the prevailing bid and ask from the CME BBO files; the authors report identifying the aggressor for over 99.95% of trades in the electronic session. A grid of VPIN variants is built from three aggregation schemes (individual transactions, time bars, volume bars) and five classification rules (true sign, tick rule, BVC with unconditional sigma, BVC with rolling sigma, random). Volume buckets are detrended to handle growth in volume over the sample. Misclassification is measured per contract and per volume bucket, and variants are entered into predictive regressions for future realized volatility with volume and volatility controls.

## Data and sample
E-mini S&P 500 futures, 10 February 2006 to 22 March 2011, trades and best bid and offer.

## Reported results
- The tick rule applied contract by contract to individual transactions misclassifies 11.6% over the five-year sample; at the volume-bucket level its error falls to 2.3%.
- Tick rule applied to one-second bars misclassifies 24.8%; applied to 60-second and 300-second bars, 38.7% and 43.1%, "barely improving on random classification".
- The best time-bar BVC variant misclassifies 23.2% at the transaction level, and 8.3% at the bucket level for 60-second bars.
- VPIN based on actual order imbalance, or on the transaction-level tick rule, is negatively correlated with future return volatility.
- BVC-VPIN's forecasting power comes from classification errors correlated with innovations in volume and volatility; with volume and volatility controls it has no incremental explanatory power.
- Stated conclusion: "VPIN is not suitable for capturing order flow toxicity."

## Signal construction
Not a signal. It is a rule for building flow features: never aggregate before signing. Sign each trade first (exchange aggressor flag, or tick rule if no flag exists), then aggregate signed volume into bars or buckets. If only candles are available, prefer candles that carry taker-buy volume over price-based bulk classification.

## Relevance to SOL perpetuals at minutes to hours
Binance, Bybit, OKX and Hyperliquid trade feeds carry the aggressor side, so a SOL bot starts where this paper ends, with near-perfect classification. That makes the paper's uncomfortable result the relevant prior: with true signs, absolute-imbalance VPIN did not signal rising volatility in E-mini. Several crypto papers still compute VPIN by BVC on one-minute candles (for example [easley-2024-microstructure-dynamics-crypto-markets](easley-2024-microstructure-dynamics-crypto-markets.md)); by this paper's logic such a VPIN is largely a transformed volatility measure. A direct test on SOL is easy: compute VPIN both ways and compare their correlation with trailing realized volatility and their incremental forecast power.

## Caveats
Working-paper version. One market, where trade size shrinks in volatile periods; that composition effect may differ in crypto. For Kalshi, check whether its trade feed publishes the taker side; if not, the tick rule on individual prints is the fallback, and [ma-2021-accuracy-tick-rule-bitcoin](ma-2021-accuracy-tick-rule-bitcoin.md) suggests it is noticeably less accurate in crypto than here.
