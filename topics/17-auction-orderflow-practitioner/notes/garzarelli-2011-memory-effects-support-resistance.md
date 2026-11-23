---
title: "Memory effects in stock price dynamics: evidences of technical trading"
authors: "Garzarelli, Federico; Cristelli, Matthieu; Zaccaria, Andrea; Pietronero, Luciano"
year: 2011
venue: "arXiv:1110.5197 (cited by later work as Scientific Reports 4:4487, 2014)"
url: "https://arxiv.org/abs/1110.5197"
pdf: "sources/17-auction-orderflow-practitioner/garzarelli-2011-memory-effects-support-resistance.pdf"
access: "full-text"
source_type: "working-paper"
evidence_grade: "B"
topic: "17-auction-orderflow-practitioner"
asset_class: "equities"
horizon: "seconds"
tags: "support-resistance, bounce-probability, memory-effect, self-fulfilling, shuffled-returns, tick-data"
---

## Key insight
With a purely algorithmic definition of support and resistance (local extremes with a tolerance stripe), intraday prices bounce off these levels more often than they cross them, and the bounce probability rises with the number of previous bounces. Neither feature appears in return-shuffled series or in an anticorrelated fractional random walk. The authors read this as measurable evidence of a self-reinforcing belief in levels.

## Method
The tick series is subsampled every tau ticks so that levels are defined at one time scale. A support (resistance) is a local minimum (maximum); a stripe of width delta is centred on it, where delta is the average absolute price increment at scale tau for that day. A bounce is an entry into the stripe followed by an exit on the same side; a crossing exits on the other side. The quantity of interest is the conditional probability p(b | b_prev) of a bounce given b_prev earlier bounces on the same level, estimated with a Bayesian binomial model (uniform prior, so the posterior mean is (n+1)/(N+2)). Controls: the same procedure on series with shuffled returns, and on a fractional random walk with the stocks' average Hurst exponent. A chi-squared test checks whether p depends on b_prev. The arXiv version carries four authors; a later citation lists a fifth (Pompa).

## Data and sample
Tick-by-tick prices for nine London Stock Exchange stocks (AZN, BP, GSK, HBOS, RBS, RIO, SHEL, ULVR, VOD) over the 251 trading days of 2002. Time scales of 45, 60, 90 and 180 seconds. Levels are detected within each trading day.

## Reported results
- Bounce probabilities for the real series are well above 0.5 at all scales; for shuffled series they are close to 0.5 (values are shown in figures, not tabulated in the text I extracted).
- p(b | b_prev) increases with b_prev for real data and is flat for shuffled data. The chi-squared test supports the increase at 45, 60 and 90 seconds.
- Average intraday Hurst exponents are below 0.5 for all nine stocks, so returns are anticorrelated. A fractional random walk with that exponent gives p only slightly above 0.5 and no dependence on b_prev, so anticorrelation alone does not explain the result.
- Recurrence times between bounces follow a power law and do not differ between real and shuffled series.

## Signal construction
Online version: keep rolling local extremes at a chosen bar scale; define a band of half-width equal to the mean absolute bar-to-bar change; count completed bounces per level; when price re-enters the band, emit features (side, b_prev, time since last bounce, band width in ticks). The conditional bounce rate by b_prev, updated as a Beta posterior, gives a calibrated probability that can feed a classifier or a bandit that chooses between fade and stand aside.

## Relevance to SOL perpetuals at minutes to hours
The construction needs only trade prices and is trivial to run on SOL perps at 1-minute bars. Whether the effect exists in a 24-hour crypto market with far more algorithmic flow is untested here. The dependence on touch count runs against the saying, common among order-flow traders but not sourced in this repository, that each test weakens a level. The sign of that dependence is therefore a clean, falsifiable test on SOL.

## Caveats
One year, nine large-cap UK stocks, 2002 tick sizes. Bounce probability is not profitability; the stripe is about one typical increment wide, so any gain per event is likely inside the spread. Bid-ask bounce in tick data could inflate the measured effect at the shortest scales. No transaction costs and no out-of-sample trading test.
