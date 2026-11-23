---
title: "Retail Traders in Futures Markets"
authors: "Ferko, Alex; Mixon, Scott; Onur, Esen"
year: 2024
venue: "CFTC Office of the Chief Economist, Staff Papers and Reports No. 2023-002 (February 2024 version)"
url: "https://www.cftc.gov/sites/default/files/2024-02/Retail_Traders_Futures_V2_website_ada.pdf"
pdf: "sources/18-positioning-sentiment/ferko-2024-retail-traders-futures-markets.pdf"
access: "full-text"
source_type: "working-paper"
evidence_grade: "B"
topic: "18-positioning-sentiment"
asset_class: "futures"
horizon: "multi-day"
tags: "retail-futures-traders, contrarian-entry, regulatory-data, micro-contracts, trader-losses, long-short-balance, cme"
---

## Key insight
Regulatory account-level data on US futures show that small retail traders lose money on average, hold positions for only a few days, enter as contrarians (going long after price falls and short after price rises), and are about as likely to be short as long. This contradicts two common assumptions carried into crypto: that retail is structurally long-biased and that retail chases momentum. On a regulated US futures venue, which is what Kalshi's perps are, the retail baseline may look more like this than like offshore perp venues.

## Method
End-of-day positions and required margin for every customer account at one large futures commission merchant known for retail clients, reported to the CFTC. Retail accounts are defined by exclusion: account names containing business or fund words (capital, fund, trading, LLC, farm, grain and similar) are removed, omnibus accounts are dropped, and any account that ever had more than USD 50,000 of initial margin is excluded. Analysis is limited to the 50 most widely held contracts and to futures positions. A "trading event" is a run of consecutive days with a position. Profit and loss per event is estimated from settlement prices. Entry and exit decisions are regressed on contemporaneous and lagged market returns, separately for long and short entries and for first-ever entries versus all entries.

## Data and sample
CME positions, February 2021 to November 2022. 36,538 retail traders across 50 futures markets. The most frequently held contracts are micro equity index futures (Micro E-mini S&P 500, Micro Nasdaq 100), followed by micro gold, Russell 2000, Dow and WTI. Crypto futures are not mentioned in the text read.

## Reported results
- The median trader has 4 trading events and trades 2 markets; half of events last 4 days or less, with about a week between events.
- Retail traders lose money: the median trader's estimated loss is in the range of USD 100 to 200; the 60th percentile of the distribution breaks even; the distribution is left-skewed, with losses in the thousands of dollars in the tail.
- Entries are contrarian: long entries rise after negative returns and short entries after positive returns. For re-entries the relation is with contemporaneous returns; for first entries it is with lagged returns. The short-side result is stronger for contemporaneous than for past returns.
- Exits occur at above-usual rates when price moves against the position.
- Traders enter short nearly as often as long.
- Larger dollar losses on the first trade are significantly associated with leaving the market permanently, though bottom-quintile performers who stay trade as often as top-quintile ones.

## Signal construction
Not a signal as published; the data are confidential. It informs how to read public small-trader proxies on regulated venues: the non-reportable residual in the weekly COT report, and any small-lot flow classification on Kalshi. Hypothesis to encode: on a regulated US venue, small-account net flow is negatively related to same-day returns, so small-trader net long positioning rising during a decline is the normal state and not by itself a capitulation or squeeze signal.

## Relevance to SOL perpetuals at minutes to hours
Relevant because of venue type. Kalshi is CFTC-regulated with low maximum leverage, closer to the micro-futures setting here than to 50x offshore perps. The contrast with Hyperliquid evidence (Jia et al. 2026 in this folder: front-end traders open with recent returns) and with eToro crypto evidence (Kogan et al. 2023: no contrarian rebalancing in crypto) means the sign of retail flow on Kalshi SOL perps is an open empirical question, to be measured once enough Kalshi trade data exist. The data are end-of-day, so nothing here speaks to intraday timing.

## Caveats
One FCM, 22 months, end-of-day snapshots that miss intraday round trips entirely. The retail definition is by exclusion and by margin size, and the authors note some findings are jointly determined with that definition. Equity-index and commodity micros, not crypto. The paper documents behaviour and losses, not whether trading against retail entries is profitable.
