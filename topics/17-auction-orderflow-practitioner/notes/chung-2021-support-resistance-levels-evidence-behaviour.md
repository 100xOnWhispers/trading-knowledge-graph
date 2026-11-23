---
title: "Evidence and Behaviour of Support and Resistance Levels in Financial Time Series"
authors: "Chung, K.; Bellotti, A."
year: 2021
venue: "arXiv:2101.07410"
url: "https://arxiv.org/abs/2101.07410"
pdf: "sources/17-auction-orderflow-practitioner/chung-2021-support-resistance-levels-evidence-behaviour.pdf"
access: "full-text"
source_type: "working-paper"
evidence_grade: "B"
topic: "17-auction-orderflow-practitioner"
asset_class: "multi"
horizon: "minutes"
tags: "support-resistance, rolling-window, bounce-probability, decay, permutation-test, logistic-regression"
---

## Key insight
A very simple detector (the rolling-window minimum and maximum, with a tolerance band) finds levels on one-minute data in FX, an equity and a commodity where price bounces more often than in return-shuffled data, and more often the more times the level has already held. The effect decays with the length of the lookback window and with time since the last bounce, at asset-specific rates, and cannot be reproduced by a stationary AR(1) process.

## Method
Support is min(X_t) plus or minus gamma and resistance is max(X_t) plus or minus gamma over a rolling window of i minutes, where gamma is the average absolute one-step price change of the whole series (chosen so that a random walk gives a bounce probability of 0.5). Bounce and penetration are defined by which boundary of the band price exits. The number of previous bounces is counted inside the window, and detection freezes while price is inside a band. The conditional bounce probability p(b | b_prev) is estimated with a Beta-binomial posterior, as in Garzarelli et al. Tests: comparison with 1,000 return-shuffled series through a permutation statistic Lambda (the share of shuffles with a lower bounce probability); lag windows from 30 to 1,440 minutes for "macro decay"; logistic regression of bounce on time since the previous bounce for "micro decay" (600-minute window); and simulated AR(1) series with rho of 1, 0.95 and 0.9.

## Data and sample
One-minute prices for 2018: EURUSD (372,607 bars), Lloyds Banking Group on the LSE (127,606) and Brent crude (307,678), from free public sources named in the paper.

## Reported results
- p(b | b_prev) rises with b_prev for all three assets at 60 and 240 minute windows and exceeds the shuffled series; most Lambda estimates are above 0.95. Lloyds estimates for b_prev of 6 to 8 are unreliable (Lambda as low as 0.226) because of small samples.
- EURUSD: the bounce probability for levels with one previous bounce decays to 0.5 at a window of about 350 minutes; with four previous bounces, at about 900 minutes.
- Brent: levels with one previous bounce fall to 0.5 within 300 minutes and then below it, so a single prior bounce predicts penetration at longer windows.
- Lloyds: little visible decay.
- Micro decay: intercepts positive and time coefficients negative for EURUSD, but both significant only for b_prev of 4 and 5.
- AR(1): stationarity raises the bounce probability, but it falls with b_prev, the opposite of real data.

## Signal construction
Features at each band entry: side, window length, b_prev, minutes since last bounce, band width relative to recent range. Label: bounce or penetration at band exit. The paper's logistic model is the minimal learner; the same event table suits gradient-boosted trees or an online logistic model, and the decay curves indicate which window lengths to give the model (roughly under six hours for a liquid 24-hour market).

## Relevance to SOL perpetuals at minutes to hours
EURUSD is a 24-hour market on one-minute bars, the same sampling a SOL bot would use, and the decay horizon of a few hours matches the target holding period. The detector is cheap and has one free parameter. It should be re-run on SOL with shuffled-return and block-bootstrap controls, and with volatility-scaled bands since SOL volatility is not constant across a year.

## Caveats
One calendar year and three instruments. Confidence bands in the figures are one standard deviation. Exact probabilities are given in figures, not in the text. A bounce is a band exit, not a profitable trade; costs are ignored and the band is about one typical one-minute move wide. Preprint; I found no evidence of journal publication in this session.
