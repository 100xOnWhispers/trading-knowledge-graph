---
title: "What drives cryptocurrency returns? A sparse statistical jump model approach"
authors: "Cortese, Federico P.; Kolm, Petter N.; Lindström, Erik"
year: 2023
venue: "Digital Finance 5(3), 483-518"
url: "https://ideas.repec.org/a/spr/digfin/v5y2023i3d10.1007_s42521-023-00085-x.html"
pdf: "none"
access: "abstract-only"
source_type: "peer-reviewed"
evidence_grade: "C"
topic: "01-macro-regime-detection"
asset_class: "crypto"
horizon: "daily"
tags: "sparse-jump-model, feature-selection, crypto-regimes, bull-neutral-bear, sentiment, market-activity"
---

## Key insight
Per the abstract: applying a sparse statistical jump model to the largest cryptocurrencies, the authors find that three states (bull, neutral, bear) describe crypto returns best, and that the features carrying the regime information are the first moments of returns, trend and reversal signals, market activity and public attention. The model selects features, estimates parameters and classifies states in one step.

## Method
Only the abstract and repository records were read (IDEAS/RePEc listing and the Lund University publication record). The sparse jump model extends the jump model in [shu-2024](shu-2024-downside-risk-statistical-jump-model.md) by adding feature weights with a sparsity constraint, so that uninformative features get zero weight. Candidate features are drawn from cryptocurrency, sentiment and financial-market series, "some previously studied and some new". A web-search summary of the paper stated that more than four hundred features were considered; I did not confirm that figure in a primary page.

## Data and sample
"The largest cryptocurrencies". Which coins, the sample period, the data frequency and the data vendors: not confirmed.

## Reported results
From the abstract only:
- A three-state model fits best; states are interpreted as bull, neutral and bear regimes.
- Selected drivers: first moments of returns, features representing trends and reversal signals, market activity, and public attention.
No state-conditional return or volatility numbers, no out-of-sample test and no trading result were visible to me. The abstract frames the work as explanation, not prediction.

## Signal construction
Sketch only. Build a wide panel of daily features per coin (return moments at several windows, trend and reversal indicators, volume and activity measures, search or social attention), standardise, and fit a sparse jump model with K = 3. Use the surviving features and centroids for online classification as in the jump-model notes. The selected feature list from the paper should be retrieved before building this.

## Relevance to SOL perpetuals at minutes to hours
This is the most direct crypto evidence for the jump-model family, and its feature groups suggest what a SOL regime classifier should contain beyond returns: activity (volume, and by extension open interest and funding) and attention. Two gaps: it appears to work at a daily horizon, and whether SOL is in the sample is not confirmed. The three-state finding is a useful prior against forcing a two-state split, consistent with the multi-state results in [koki-2020](koki-2020-predictability-cryptocurrencies-bayesian-hmm.md).

## Caveats
Abstract only; Springer's site could not be fetched in this session and no open copy was located, so the grade is held at C despite the peer-reviewed venue. In-sample feature selection across hundreds of candidates carries obvious multiple-testing risk. Nothing here shows the states are predictable in advance or tradable after costs. An earlier conference version reportedly described four states, which suggests the state count is sensitive to specification.
