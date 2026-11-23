---
title: "Designing funding rates for perpetual futures in cryptocurrency markets"
authors: "Kim, Jaehyun; Park, Hyungbin"
year: 2025
venue: "arXiv working paper 2506.08573"
url: "https://arxiv.org/pdf/2506.08573"
pdf: "sources/03-perp-pricing-funding/kim-2025-designing-funding-rates.pdf"
access: "full-text"
source_type: "working-paper"
evidence_grade: "C"
topic: "03-perp-pricing-funding"
asset_class: "crypto"
horizon: "n/a"
tags: "funding-rate-design, path-dependence, eight-hour-averaging, bsde, replication"
---

## Key insight
A funding rule proportional to the gap between a target value and the perp price pins the perp price uniquely to the target, provided the proportionality constant is large enough. Replacing the instantaneous gap with its average over the past 8 hours, as exchanges do, still gives a unique price that is close to the instantaneous-rule price, with an error that shrinks with the square root of the averaging window.

## Method
Arbitrage pricing with path-dependent infinite-horizon backward stochastic differential equations. The instantaneous rule is `Phi = l*(phi - y) + (drift and interest correction terms)`, where `phi` is the target, `y` the perp price and `l` the anchoring coefficient. The practical rule is `Phi_delta(s) = (1/delta) * integral from s-delta to s of Phi(u) du` with `delta = 1/1095` years (8 hours). Existence and uniqueness are proved for both (Theorem 4.3) and replicating portfolios are constructed.

## Data and sample
None. A Black-Scholes illustration uses `r = 0.02`, `sigma = 0.3`.

## Reported results
- Uniqueness needs `l` above a threshold: in the Black-Scholes example `l > 0.26227` for the instantaneous rule and `1.26227 < l < 15.75125` for the 8-hour averaged rule.
- The term that depends on the gap never pays anything in equilibrium (the gap is zero) yet is what enforces uniqueness. If `l` is too small, multiple arbitrage-free prices are consistent with the same funding rule.
- Distance between the two price processes is bounded by `(3.68432*||X|| + 0.84216) * sqrt(delta)`, about `0.11134*||X|| + 0.02545` at 8 hours in the example.
- The authors say this is the first treatment of the averaged funding rule and of non-tradable targets.

## Signal construction
Not a signal. It supports two modelling choices: treat the averaging window as a design parameter that loosens the anchor as it lengthens, and treat weak funding coefficients (or binding caps) as regimes where the premium is not well pinned.

## Relevance to SOL perpetuals at minutes to hours
The square-root dependence on the window gives a rough rule for comparing venues: a 1-hour averaging window (Hyperliquid) should allow about `sqrt(1/8)`, roughly 35%, of the model-implied slack of an 8-hour window (Binance default, Kalshi). That scaling is my reading of the bound, not a result stated for venue comparison, and it would need testing on SOL premium data across venues.

## Caveats
Unreviewed preprint, pure mathematics, complete-market assumptions, no clamp, no cap, no costs, no discrete settlement times. The numerical bounds are worst-case and specific to the illustration. Not evidence about realised premium behaviour.
