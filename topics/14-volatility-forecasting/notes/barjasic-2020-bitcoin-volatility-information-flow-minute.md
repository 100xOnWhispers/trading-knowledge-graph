---
title: "Time-varying volatility in Bitcoin market and information flow at minute-level frequency"
authors: "Barjašić, Irena; Antulov-Fantulin, Nino"
year: 2020
venue: "arXiv preprint 2004.00550 (v2, January 2021)"
url: "https://arxiv.org/pdf/2004.00550"
pdf: "sources/14-volatility-forecasting/barjasic-2020-bitcoin-volatility-information-flow-minute.pdf"
access: "full-text"
source_type: "working-paper"
evidence_grade: "C"
topic: "14-volatility-forecasting"
asset_class: "crypto"
horizon: "minutes"
tags: "garch-x, minute-data, volume, bid-ask-spread, twitter, transfer-entropy, mixture-of-distributions"
---

## Key insight
At 1-minute frequency, Bitcoin trading volume and bid-ask spread carry information about next-minute volatility beyond what a GARCH model extracts from past returns. Adding them as exogenous terms in the variance equation significantly improves out-of-sample likelihood for GARCH(1,1) and component GARCH(1,1). A Twitter activity signal is much weaker at this time scale.

## Method
The framing is the mixture-of-distributions hypothesis: return variance and volume are both driven by a latent information-flow rate. The authors first measure lagged correlation and transfer entropy between squared 1-minute returns and each external signal (trade volume, bid-ask spread, count of crypto-related tweets), with significance from shuffled series. They then fit several GARCH-family variants with and without the external signal in the variance equation, and compare predictive negative log-likelihood on held-out data using a likelihood-ratio test, with a bootstrap over shorter sub-samples for robustness. Two price definitions are used: mid-quote and 1-minute volume-weighted average price.

## Data and sample
BTC/USD on Bitfinex, 18 April 2019 to 30 May 2019, about 58,000 one-minute observations: 50,000 in-sample and 8,000 out-of-sample. Volume and spread from Bitfinex at one-second resolution, aggregated to minutes.

## Reported results
- Correlation between squared returns and volume peaks when volume leads squared returns by one minute; all correlations are statistically significant. Spread behaves analogously.
- Transfer entropy is significant for all three signals; information transfer from volume and spread to squared returns is stronger than from tweets. The largest transfer entropy runs from squared returns to volume.
- Tweets show no similar raw correlation pattern; a pattern appears only after integrating the tweet series over 30 minutes.
- Out of sample, exogenous variables significantly improve predictive likelihood for GARCH and cGARCH; for other variants improvement is not consistently significant.

## Signal construction
Short-horizon volatility nowcast: sigma2_{t+1} = omega + alpha * r_t^2 + beta * sigma2_t + gamma * x_t, where x_t is the last minute's traded volume (or quoted spread), suitably normalised by its own rolling mean. Update every minute. The same x_t terms can be added to a HAR regression. Inputs are trades and top-of-book quotes from the reference venue.

## Relevance to SOL perpetuals at minutes to hours
This is the right time scale and the inputs are freely available for SOL on Binance, Bybit, OKX and Hyperliquid. The finding that volume and spread lead volatility by about a minute suggests they are most useful for very short-term sizing and stop adjustment, less so for hour-ahead forecasts where their own persistence dominates. Normalising by the calendar pattern (see the Hansen note) is needed so the model does not simply relearn hour-of-day effects.

## Caveats
Six weeks of data from one exchange in 2019, one out-of-sample block of about 5.5 days. Gaussian likelihood on fat-tailed minute returns. Feedback runs both ways (volatility also drives volume), so the relation is predictive, not causal. No economic evaluation. Preprint; journal publication not confirmed in this session.
