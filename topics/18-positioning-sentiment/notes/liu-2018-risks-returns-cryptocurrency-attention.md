---
title: "Risks and Returns of Cryptocurrency"
authors: "Liu, Yukun; Tsyvinski, Aleh"
year: 2018
venue: "NBER Working Paper 24877 (cited by later papers as Liu and Tsyvinski 2021)"
url: "https://www.nber.org/system/files/working_papers/w24877/w24877.pdf"
pdf: "sources/18-positioning-sentiment/liu-2018-risks-returns-cryptocurrency-attention.pdf"
access: "full-text"
source_type: "working-paper"
evidence_grade: "B"
topic: "18-positioning-sentiment"
asset_class: "crypto"
horizon: "multi-day"
tags: "investor-attention, google-trends, twitter-volume, negative-attention, time-series-momentum, bitcoin"
---

## Key insight
Abnormal investor attention, measured as Google searches or Twitter post counts relative to their own four-week average, positively predicts Bitcoin returns one to two weeks ahead. Attention is therefore a confirming (momentum-like) signal at the weekly horizon, not a contrarian one. The exception is negative attention: a rising share of "Bitcoin hack" searches predicts lower returns. Attention itself is driven by contemporaneous and prior-week returns, so part of the effect overlaps with time-series momentum.

## Method
Predictive time-series regressions of future weekly returns on a standardized attention deviation:

`Google_t = (searches_t - mean(searches_{t-4..t-1}))`, normalized to unit variance.

The same construction is applied to Twitter post counts for "Bitcoin". Negative attention is the ratio of searches for "Bitcoin hack" to searches for "Bitcoin", normalized. Quintile sorts on the attention deviation are reported with mean next-week return, t-statistic and Sharpe ratio. One table sets quintile cut-offs using only the first two years of data to avoid look-ahead.

## Data and sample
Bitcoin daily prices from CoinDesk, 1 January 2011 to 31 May 2018; Ripple from 4 August 2013; Ethereum from 7 August 2015. Google search series from Google; Twitter post counts for "Bitcoin" from Crimson Hexagon. Weekly frequency for the attention tests. This note covers only the attention sections (4.2 and 4.3); the momentum and factor-exposure results are covered in other topics.

## Reported results
- A one-standard-deviation rise in the Bitcoin Google deviation is followed by +1.84% (t = 2.17) at one week and +2.30% (t = 2.81) at two weeks; coefficients at three to seven weeks are insignificant. R-squared is 0.01 to 0.02.
- Quintile sort, full sample: top attention quintile earns 11.20% the next week (Sharpe 0.48) against 1.07% for the bottom quintile (Sharpe 0.08). With cut-offs fixed from the first two years, the top quintile earns 8.10% against 0.70%.
- Twitter post-count deviation: +2.50% at one week (t = 2.96).
- "Bitcoin hack" ratio: a one-standard-deviation rise is followed by a 2.75% lower return the next week, and the paper states significance at one to five weeks.
- Google deviations load positively on the same-week and prior-week Bitcoin return (R-squared up to about 0.10).
- Ripple: Google proxy predicts one week ahead. Ethereum: one, three and six weeks.

## Signal construction
Inputs: a search-interest or post-count series per asset. Compute `z_t = (x_t - mean(x_{t-4..t-1})) / sd`, updated weekly (the paper) or on a rolling daily or hourly basis (extension, untested here). Long bias when `z_t` is high and price is not already falling; a separate negative-attention ratio (hack, exploit, outage terms over the asset name) acts as a bearish flag.

## Relevance to SOL perpetuals at minutes to hours
The horizon is one to two weeks, so this is a regime or bias input rather than an entry trigger. It supports treating attention spikes as confirming in crypto. SOL was not in the sample, and SOL attention is entangled with memecoin and network-outage news, which makes the negative-attention ratio the more interesting part to re-test. Hourly Google Trends data exist but are sampled and rescaled per request, so an intraday version needs its own validation.

## Caveats
Sample ends May 2018 and is dominated by the 2013 and 2017 bubbles, when attention and returns both exploded. No transaction costs. Weekly returns of 11% for the top quintile reflect that era, not a current expectation. The attention measure is partly a transformation of past returns. Later replication on post-2018 data was not examined in this session.
