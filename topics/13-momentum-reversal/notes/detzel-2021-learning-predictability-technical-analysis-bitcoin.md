---
title: "Learning and predictability via technical analysis: Evidence from bitcoin and stocks with hard-to-value fundamentals"
authors: "Detzel, Andrew; Liu, Hong; Strauss, Jack; Zhou, Guofu; Zhu, Yingzi"
year: 2021
venue: "Financial Management 50(1), 107-137"
url: "https://ideas.repec.org/a/bla/finmgt/v50y2021i1p107-137.html"
pdf: "none"
access: "abstract-only"
source_type: "peer-reviewed"
evidence_grade: "B"
topic: "13-momentum-reversal"
asset_class: "crypto"
horizon: "daily"
tags: "moving-average, technical-analysis, bitcoin, rational-learning, out-of-sample"
---

## Key insight
For assets whose fundamentals are hard to value, such as Bitcoin, the ratio of price to its moving average forecasts daily returns in and out of sample. The authors give this a theoretical basis: in their equilibrium model, technical analysis arises endogenously from rational learning, so trend rules are not necessarily evidence of irrationality. The same predictability appears in small-cap, young-firm and low-analyst-coverage stocks and in NASDAQ stocks during the dot-com era.

## Method
Only the abstract was read. It describes (1) an equilibrium model in which technical analysis arises endogenously via rational learning (model details not confirmed), (2) predictive regressions of daily Bitcoin returns on price-to-moving-average ratios, in-sample and out-of-sample, and (3) trading strategies based on the ratio compared with buy-and-hold. The moving-average windows used were not confirmed from the abstract.

## Data and sample
Daily Bitcoin returns, plus US equity subsamples (small-cap, young, low coverage, NASDAQ in the dot-com period). Dates and data source not confirmed.

## Reported results
From the abstract only:
- Ratios of price to moving average forecast daily Bitcoin returns in-sample and out-of-sample.
- Trading strategies based on the ratio earn economically meaningful alpha and raise the Sharpe ratio relative to buy-and-hold.
- Similar results hold for the hard-to-value equity groups listed above.
No numerical magnitudes were seen.

## Signal construction
For each window L, compute x_L = P_t / MA_L(P) (or its log). Use x_L as a continuous predictor of the next-bar return, or as a rule: long when P_t > MA_L, flat otherwise. The paper works at daily frequency; window lengths should be taken from the full text before use. A bot can compute the same ratios on intraday bars, but that is an extrapolation.

## Relevance to SOL perpetuals at minutes to hours
Supports moving-average distance as a trend state variable for crypto and gives a reason to expect it to work better in assets with uncertain fundamentals, a description that fits SOL at least as well as Bitcoin. Because the effect is linked to learning under valuation uncertainty, it should be stronger when uncertainty is high (new narratives, protocol events) and may weaken as the asset matures. The daily horizon means this is a regime filter for the intraday bot, to be re-tested on SOL.

## Caveats
Abstract-only. The long-or-flat construction benefits from Bitcoin's large positive drift and from avoiding crashes, so performance relative to buy-and-hold partly reflects volatility timing, not sign prediction (compare Huang et al. 2020). Transaction costs and the sample end date were not confirmed.
