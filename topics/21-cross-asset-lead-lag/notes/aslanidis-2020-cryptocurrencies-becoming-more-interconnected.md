---
title: "Are cryptocurrencies becoming more interconnected?"
authors: "Aslanidis, Nektarios; Bariviera, Aurelio F.; Perez-Laborda, Alejandro"
year: 2020
venue: "arXiv preprint 2009.14561; journal version not confirmed"
url: "https://arxiv.org/abs/2009.14561"
pdf: "sources/21-cross-asset-lead-lag/aslanidis-2020-cryptocurrencies-becoming-more-interconnected.pdf"
access: "full-text"
source_type: "working-paper"
evidence_grade: "B"
topic: "21-cross-asset-lead-lag"
asset_class: "crypto"
horizon: "daily"
tags: "connectedness, spillover, diebold-yilmaz, frequency-domain, pca, bitcoin-dominance, stability"
---

## Key insight
Between 2015 and 2020 the crypto market went from loosely linked coins, with Bitcoin and Litecoin as the main sources of spillovers, to a nearly one-factor market in which every major coin transmits and receives about equally. Return shocks are transmitted mainly at high frequency and die out fast; volatility shocks persist. The "Bitcoin is the dominant transmitter" result of earlier studies is a feature of the early sample, not a constant.

## Method
Three approaches on the same data, each in rolling or yearly windows:
1. Principal component analysis of standardized returns and of log volatilities; share of variance explained by the first component and squared loadings per coin.
2. Average pairwise correlation and Pesaran's cross-sectional dependence test.
3. Diebold-Yilmaz connectedness from a VAR(4) with a 365-day rolling window and a 10-step horizon, plus the Barunik-Krehlik frequency decomposition into a high band (periods of 1 to 7 days) and a low band (longer than 7 days).

Volatility is the Garman-Klass daily range estimator, in logs.

## Data and sample
Daily data from coinmarketcap.com for 17 major coins. Sample 1: seven coins (BTC, DASH, ETH, LTC, XLM, XMR, XRP) from August 2015; Sample 2: ten coins from October 2016; Sample 3: seventeen coins from October 2017. End date July 2020.

## Reported results
- First principal component of returns explains 36% of variance in the first year (about 70% of BTC's and LTC's variance but only 7% of ETH's) and more than 80% in August 2019 to July 2020, with at least 65% of every coin's variance.
- Total return connectedness rises from nearly 25% to 80% over 2016-2020; volatility connectedness from roughly 30% to 76%. It stabilizes near 0.8 from 2019 and jumps in March 2020.
- Directional: in the first year spillovers are driven by Bitcoin and Litecoin; in the last year "all coins are now about equally important in transmitting/receiving return spillovers", with cross-market shocks accounting for 74% to 80% of each coin's return variance.
- Frequency: most return connectedness is created in the high-frequency band, so transmitted return shocks are short-lived; most volatility connectedness is in the low-frequency band, with the high-frequency share rising over time.
- Less than 20% of coin-specific shocks are not transmitted by July 2020.

## Signal construction
Not a directional signal. Two uses. (1) A rolling "market mode" monitor: share of variance of a basket of major coins explained by the first principal component, and SOL's squared loading on it, computed on hourly or 5-minute returns. When the share is above roughly 80%, SOL-versus-BTC relative signals carry little independent information and the bot is effectively trading the crypto factor. (2) Rolling net directional connectedness to check whether BTC is still a net transmitter to SOL in the current regime.

## Relevance to SOL perpetuals at minutes to hours
It sets expectations: among large coins most co-movement is contemporaneous at the daily scale and, by the frequency result, concentrated at the shortest periods. That is consistent with the intraday evidence that liquid coins react to BTC within a minute. For a SOL bot the practical content is that the crypto market factor explains most of SOL's variance, so cross-asset inputs should be built as factor state (trend, flow and volatility of the common factor) more than as lagged BTC returns. SOL is not in the sample.

## Caveats
Daily data ending July 2020, before SOL's rise, the 2021-2022 cycle and spot ETFs. Generalized variance decompositions do not identify who moves first. A short letter-length paper; directional tables are shown only for the first and last year. Earlier studies it builds on (Yi et al. 2018; Ji et al. 2019; and Koutmos 2018, whose abstract was read in this session and reports Bitcoin as the dominant contributor among 18 coins with spillovers rising over time and spiking around news) were not read in full.
