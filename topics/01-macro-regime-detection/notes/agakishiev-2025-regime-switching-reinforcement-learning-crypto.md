---
title: "Regime switching forecasting for cryptocurrencies"
authors: "Agakishiev, Ilyas; Härdle, Wolfgang Karl; Becker, Denis; Zuo, Xiaorui"
year: 2025
venue: "Digital Finance 7(1), 107-131"
url: "https://ideas.repec.org/a/spr/digfin/v7y2025i1d10.1007_s42521-024-00123-2.html"
pdf: "none"
access: "abstract-only"
source_type: "peer-reviewed"
evidence_grade: "C"
topic: "01-macro-regime-detection"
asset_class: "crypto"
horizon: "hours"
tags: "reinforcement-learning, regime-switching, crix-index, crypto-metadata, position-sizing, two-stage-model"
---

## Key insight
Per the abstract: the paper merges two ways of handling complex time series, flexible models such as neural networks and regime-dependent parameters as in hidden Markov models, into a reinforcement-learning model that receives additional variables depending on the state of the series. Applied to deciding what share of wealth to hold in the CRIX crypto index, the authors conclude that the regime-based model "shows potential for investment management, but comes with some caveats", and that cryptocurrency metadata is useful supplementary data for analysing prices.

## Method
Only the abstract (RePEc listing) was read. It describes a reinforcement-learning agent whose inputs include state-dependent variables, tested on an allocation decision between the CRIX index and, implicitly, cash. Details reported by other pages and not confirmed by me in the paper: a web-search summary of the publisher page says there are three regimes defined by volatility and return quantiles, that regime identification and portfolio weighting are separate stages, that "buffer zones" are used to prevent frequent regime flips, and that the reinforcement-learning stage uses hourly CRIX data with Bitcoin metadata for regime detection. A second paper in this folder, [joshi-2025](joshi-2025-regime-specific-interdependencies-crypto-gmm-var.md), cites it as using Bitcoin metadata, hourly CRIX index data and Bitcoin prices. Treat all of these as secondary.

## Data and sample
The abstract says only "cryptocurrency data" and the CRIX index. Period and frequency: not confirmed from a primary page (hourly, per the secondary descriptions above).

## Reported results
The abstract reports no numbers. Qualitative statements only: metadata is useful as supplementary input; the regime-based model shows potential with unnamed caveats.

## Signal construction
Sketch from the secondary descriptions, to be checked against the paper: (1) label each hour as one of three regimes using trailing quantiles of volatility and return; (2) apply a buffer zone, meaning a regime change is accepted only when the classifying statistic moves past the threshold by a margin, so that values hovering at the boundary do not cause flips; (3) pass the regime label, price features and on-chain metadata to an agent that outputs the fraction of capital held in the risky asset.

## Relevance to SOL perpetuals at minutes to hours
On paper this is the closest match in the literature to the bot's design question: hourly crypto data, an explicit regime stage feeding a learning agent, and anti-flicker logic. Two ideas are worth carrying forward even without the numbers. One is the two-stage split, which keeps the regime definition inspectable instead of buried inside a network. The other is quantile-defined regimes with buffer zones, a transparent baseline against which HMM, jump-model and changepoint detectors should be compared. The target is an index weighted toward Bitcoin, not SOL.

## Caveats
Abstract only; the publisher site could not be fetched and no open copy was found, so nothing about performance, costs, sample split or the nature of the "caveats" is known to me. The grade is held at C for that reason. Reinforcement-learning allocation results are generally sensitive to seeds, reward design and the test window. This note should be upgraded or discarded once the full text has been read.
