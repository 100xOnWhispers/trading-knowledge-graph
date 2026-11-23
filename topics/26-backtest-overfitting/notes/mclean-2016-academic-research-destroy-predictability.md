---
title: "Does Academic Research Destroy Stock Return Predictability?"
authors: "McLean, R. David; Pontiff, Jeffrey"
year: 2016
venue: "Journal of Finance"
url: "https://api.openalex.org/works/doi:10.1111/jofi.12365"
pdf: "none"
access: "abstract-only"
source_type: "peer-reviewed"
evidence_grade: "A"
topic: "26-backtest-overfitting"
asset_class: "equities"
horizon: "multi-day"
tags: "alpha-decay, post-publication, data-mining, crowding, anomalies"
---

## Key insight
Published return predictors lose a large share of their performance after the sample period ends and more again after publication. The design separates two causes of decay: statistical bias (data mining), measured by the drop between the original sample and publication, and informed trading by investors who learn of the anomaly, measured by the additional drop after publication.

## Method
Per the abstract: the authors study the out-of-sample and post-publication return predictability of 97 variables shown in the literature to predict cross-sectional stock returns, comparing three periods for each predictor: the original in-sample period, the period after the sample but before publication, and the post-publication period. They relate the size of the decline to predictor characteristics and examine correlations between predictor portfolios after publication. Further details of portfolio construction were not read.

## Data and sample
97 cross-sectional stock return predictors from the academic literature. Exact sample dates and data sources were not confirmed in this session (the abstract does not give them; the publisher page was not accessible).

## Reported results
From the abstract only:
- Portfolio returns are 26% lower out-of-sample and 58% lower post-publication.
- The out-of-sample decline is described as an upper bound on data-mining effects.
- The authors estimate a 32% (58% minus 26%) lower return attributable to publication-informed trading.
- Post-publication declines are greater for predictors with higher in-sample returns.
- Returns are higher for portfolios concentrated in stocks with high idiosyncratic risk and low liquidity.
- Predictor portfolios show post-publication increases in correlations with other published-predictor portfolios.
- The authors conclude investors learn about mispricing from academic publications.

These headline numbers are quoted consistently by two papers read in full in this session (Jensen, Kelly and Pedersen 2021; Falck, Rej and Thesmar 2021).

## Signal construction
Not a signal. It is the empirical basis for a decay prior. A practical use: when taking a signal from a published paper or a widely read industry report, plan on roughly a quarter of the reported edge having been statistical luck and roughly a further third disappearing once the signal is public, and size the expected edge accordingly before costs.

## Relevance to SOL perpetuals at minutes to hours
The quantities are for monthly US equity anomalies, so the exact percentages do not transfer. The mechanism does, and probably acts faster in crypto: signals built from public exchange data (funding extremes, open-interest changes, order-book imbalance) are published on social media and vendor dashboards within days, capital is mobile, and there are few limits to arbitrage on liquid perpetuals. The finding that decay is smaller where trading is costly and risky suggests the edges that survive in crypto will sit in less liquid instruments or need speed, which a low-leverage venue with a thin book partly reproduces. Every signal in this repository drawn from a published study should be re-estimated on data after its publication date.

## Caveats
Abstract-only note; no full-text PDF could be obtained from an open source. The split between data mining and informed trading rests on the assumption that nothing else changes at the sample end. Later work argues the attenuation is what Bayesian shrinkage would predict even without a replication problem (Jensen, Kelly and Pedersen 2021). The relevance section's claim that crypto decay is faster is this note's inference, not evidence from the paper.
