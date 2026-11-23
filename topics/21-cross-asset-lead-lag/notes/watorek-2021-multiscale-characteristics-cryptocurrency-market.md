---
title: "Multiscale characteristics of the emerging global cryptocurrency market"
authors: "Watorek, Marcin; Drozdz, Stanislaw; Kwapien, Jaroslaw; Minati, Ludovico; Oswiecimka, Pawel; Stanuszek, Marek"
year: 2021
venue: "Physics Reports 901, 1-82 (arXiv:2010.15403v2 read)"
url: "https://arxiv.org/abs/2010.15403"
pdf: "sources/21-cross-asset-lead-lag/watorek-2021-multiscale-characteristics-cryptocurrency-market.pdf"
access: "full-text"
source_type: "peer-reviewed"
evidence_grade: "B"
topic: "21-cross-asset-lead-lag"
asset_class: "multi"
horizon: "minutes"
tags: "detrended-cross-correlation, multiscale, lagged-correlation, crypto-equity, sp500, covid, regime-change, epps-effect"
---

## Key insight
Cross-correlations in crypto build up with time scale much more slowly than in FX, they are weaker for large returns than for typical ones, and they depend on liquidity: the more frequently a pair trades, the faster it synchronizes with others. Crypto was uncorrelated with equities, currencies and commodities in 2018-2019 and became significantly correlated with them from 2020, first in the March crash and then persistently, including at a 10-minute scale.

## Method
A long review. The relevant tool is the q-dependent detrended cross-correlation coefficient rho(q, s): fluctuation functions of two series are computed after removing polynomial trends in windows of length s; q weights the size of fluctuations (q = 1 no emphasis, q = 4 emphasizes large returns). A lagged version rho(q, s, tau) shifts one series by tau to test who leads. Minimal spanning trees and eigenvalue spectra describe the cross-sectional structure.

## Data and sample
Tick and 10-second to 1-minute data: Bitstamp BTC history; Kraken and Binance exchange rates among BTC, ETH, XRP, USD, USDT and EUR for 2018 and other periods; Dukascopy FX for comparison. For the cross-market part: 1-minute returns of BTC/USD and ETH/USD against 20 conventional assets (13 currencies, the Dow Jones, NASDAQ100 and S&P500, and four commodities: gold, silver, copper and crude oil; Dukascopy data), January 2018 to September 2020, Monday to Friday, at scales s = 10 min and s = 360 min.

## Reported results
- Lagged analysis for the same rate on two venues (2018): BTC/ETH on Binance is "advanced by 1-2 min with respect to Kraken" at s of about 10 min; Binance leads by 1 minute for the other 11 cross-listed rates at q = 1. The authors attribute this to higher trading frequency on Binance. (Same-asset cross-venue; reported here as evidence on time scale and on the liquidity mechanism.)
- Summary rule: "the more frequently traded cryptocurrencies are, the faster is the synchronization of their fluctuations"; synchronization delays are "vastly longer" than in FX or stocks.
- Crypto versus traditional assets: no significant cross-correlation in 2018 and 2019. In 2020 four episodes: negative BTC/S&P500 correlation for large returns in late January; strong positive correlation in the March 2020 panic; again in June; and from late August 2020 BTC and ETH positively correlated with all considered assets on all scales.
- rho is larger at s = 360 min than at s = 10 min but significant at both, which the authors explain by cross-correlations needing time to build up.
- NASDAQ100 and DJIA behave like the S&P500 against BTC.

## Signal construction
Not a signal. A diagnostic: compute rho(q, s, tau) between SOL and each candidate leader (BTC, ETH, ES or NQ futures) for s from 5 minutes to a day, q in {1, 4}, and tau from -5 to +5 minutes. The scale at which rho saturates is the horizon over which the two assets carry the same information; an asymmetry in tau is a lead. A rolling rho(q = 1, s = 10 min) between SOL and equity index futures is a regime flag for "crypto is trading as a risk asset today".

## Relevance to SOL perpetuals at minutes to hours
Three points transfer. Lead-lag times in crypto in 2018 were minutes, not milliseconds, for less active venues, which is the regime a new, thin Kalshi market may resemble. Correlation with equities is regime-dependent and can be switched on by macro stress, so equity-futures features should be gated by a rolling correlation estimate. Large moves synchronize more slowly than typical ones in less liquid pairs, which is where a follower venue is most likely to lag.

## Caveats
Descriptive physics-style analysis, no forecasting or trading test. The lag evidence is from 2018 and cross-venue; crypto markets are far faster now. The equity analysis ends in September 2020 and does not test who leads. SOL is not covered.
