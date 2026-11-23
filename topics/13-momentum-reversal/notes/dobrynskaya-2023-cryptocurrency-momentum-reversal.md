---
title: "Cryptocurrency Momentum and Reversal"
authors: "Dobrynskaya, Victoria"
year: 2023
venue: "Journal of Alternative Investments 26(1), 65-76 (SSRN working paper 3913263, 2021)"
url: "https://www.hse.ru/en/news/research/559533243.html"
pdf: "none"
access: "secondary"
source_type: "peer-reviewed"
evidence_grade: "B"
topic: "13-momentum-reversal"
asset_class: "crypto"
horizon: "multi-day"
tags: "crypto-momentum, reversal, cross-sectional, horizon-switch, weekly"
---

## Key insight
In a cross-section of roughly 2,000 coins, momentum is positive only at short horizons of up to two to four weeks and turns into significant reversal beyond about one month. In equities the same switch takes about a year, so the author describes crypto as having a faster "metabolism". The practical message is that the look-back and holding period that work in traditional markets are an order of magnitude too long for crypto.

## Method
Read through a university press summary of the paper and a search-result rendering of the abstract; the paper itself could not be opened (SSRN returned HTTP 403). As described there: cross-sectional momentum portfolios buy the top 30% and sell the bottom 30% of coins ranked by past return. Ranking periods run from 1 week to 2 years, holding periods from 1 to 12 weeks, with rebalancing weekly or every 2 to 8 weeks.

## Data and sample
Nearly 2,000 cryptocurrencies with market capitalisation above USD 1 million, 2014 to 2020 (almost seven years).

## Reported results
From the secondary summary only:
- Momentum is strongest with a 2-week sorting, holding and rebalancing period.
- Reversal appears from about 4 weeks (4 to 6 weeks with less frequent rebalancing) and strengthens as sorting or holding periods lengthen.
- The reversal is driven mainly by past-loser coins.
- The press summary quotes annual returns of about 70% for the 2-week ranking and holding strategy; this figure, and a large negative figure it quotes for long holding periods, were not verified against the paper.
- The strategies reportedly did not lose money during the 2020 COVID-19 crisis.

## Signal construction
Cross-sectional rank of trailing 1 to 2 week return across a coin universe; long top 30%, short bottom 30%; hold up to 2 weeks. For a single-instrument bot, the usable form is SOL's trailing 1 to 2 week return relative to the cross-sectional median, used as a slow directional bias, with the bias dropped or inverted once the look-back exceeds about a month.

## Relevance to SOL perpetuals at minutes to hours
The horizon map is the transferable part: crypto continuation lives at days to a couple of weeks, and long look-backs carry reversal risk. This bounds the slow end of any multi-horizon trend blend for SOL at roughly two to four weeks. The paper is cross-sectional and weekly, so it says nothing directly about a single coin at intraday frequency.

## Caveats
Secondary access; treat all numbers as unverified. The universe includes many small coins that cannot be shorted or traded in size, and the author's own later working paper (Dobrynskaya and Dubrovskiy, 2022, opened in this session) states that the momentum premium "has vanished in the recent years". Returns are gross of costs as far as could be determined. Sample ends 2020.
