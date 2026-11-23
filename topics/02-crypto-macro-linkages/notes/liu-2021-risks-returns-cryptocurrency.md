---
title: "Risks and Returns of Cryptocurrency"
authors: "Liu, Yukun; Tsyvinski, Aleh"
year: 2021
venue: "Review of Financial Studies 34(6), 2689-2727 (read here as NBER Working Paper 24877, August 2018)"
url: "https://www.nber.org/system/files/working_papers/w24877/w24877.pdf"
pdf: "sources/02-crypto-macro-linkages/liu-2021-risks-returns-cryptocurrency.pdf"
access: "full-text"
source_type: "peer-reviewed"
evidence_grade: "A"
topic: "02-crypto-macro-linkages"
asset_class: "crypto"
horizon: "daily"
tags: "macro-exposure, factor-loadings, time-series-momentum, investor-attention, baseline"
---

## Key insight
In data through mid-2018, Bitcoin, Ripple and Ethereum returns had essentially no exposure to stock-market factors beyond a CAPM beta, and none to major currencies, precious metals or macroeconomic factors. What did predict returns was crypto-specific: time-series momentum and investor attention. This is the baseline "crypto is disconnected from macro" result that later papers (see the Copestake and Borri notes) show broke down after 2020.

## Method
Standard empirical asset pricing. Time-series regressions of coin returns on (i) CAPM and Fama-French factors plus 155 other published anomalies, (ii) five major currencies (AUD, CAD, EUR, SGD, GBP), (iii) gold, platinum and silver, (iv) macro factors (non-durable and durable consumption growth, industrial production growth, personal income growth). Predictive regressions of future returns on lagged returns (momentum), Google search volume, Twitter post counts, and a negative-attention ratio ("Bitcoin hack" searches relative to "Bitcoin" searches).

## Data and sample
CoinDesk price series. Bitcoin 1 Jan 2011 to 31 May 2018; Ripple from 4 Aug 2013; Ethereum from 7 Aug 2015. Daily, weekly and monthly returns. Macro series from FRED.

## Reported results
- Weekly Bitcoin mean return 3.79 percent with standard deviation 16.64 percent; daily mean 0.52 percent, standard deviation 5.55 percent. Sharpe ratios 0.09 daily, 0.23 weekly, 0.31 monthly.
- A daily 20 percent loss on Bitcoin occurs with probability 0.5 percent.
- CAPM betas are "sizable" but alphas stay large and significant; Fama-French five-factor exposures are low and insignificant.
- Currency exposures are small and insignificant. Metal exposures are insignificant except Ethereum to gold. Macro-factor exposures are insignificant for Bitcoin and Ripple; Ethereum loads somewhat on durable consumption growth.
- Momentum: a one-standard-deviation rise in today's Bitcoin return predicts a 0.33 percent higher return the next day. Sorting weeks by prior-week return, the top quintile averages 11.22 percent the following week against 2.60 percent for the bottom quintile.
- Attention: a one-standard-deviation rise in Google searches for "Bitcoin" predicts a 2.3 percent higher return two weeks ahead; Twitter post counts predict 2.50 percent one week ahead.

These numbers are from the 2018 NBER version. The published 2021 version was not opened; its abstract (seen only through a search summary) adds that returns load on network factors but not production factors.

## Signal construction
Two usable ideas, both at daily or slower frequency.
1. Time-series momentum: sign and size of the previous day's (or week's) return of the coin itself, standardized by its rolling volatility, as a directional prior.
2. Attention: standardized change in Google Trends or social post counts for the coin name, with the hack-to-name search ratio as a negative-attention flag.
Neither is an intraday signal as tested. The macro-exposure regressions are "Not a signal": they are a baseline for how much macro conditioning to expect.

## Relevance to SOL perpetuals at minutes to hours
The paper sets the null hypothesis: before 2018, macro variables told you nothing about crypto returns at daily frequency. A bot design that leans on macro inputs must rest on the post-2020 evidence, not this one. The momentum result is the part that most plausibly transfers to SOL, but it was tested on three coins at daily and weekly horizons, not on SOL and not intraday. Re-test daily and intraday time-series momentum on SOL perpetual data directly.

## Caveats
Sample ends May 2018, before institutional entry, spot ETFs, and the 2022 tightening cycle. Three coins only. No transaction costs. The predictability magnitudes come from a period of extreme mean returns and are unlikely to persist at that size. Macro factors are monthly series, so the test has little power against announcement-window effects (the Pinchuk note addresses that).
