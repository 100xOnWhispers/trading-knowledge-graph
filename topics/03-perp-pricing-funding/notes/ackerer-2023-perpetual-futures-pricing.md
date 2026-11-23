---
title: "Perpetual Futures Pricing"
authors: "Ackerer, Damien; Hugonnier, Julien; Jermann, Urban"
year: 2023
venue: "arXiv working paper 2310.11771 (v2, September 2024); also NBER Working Paper 32936; a later journal version in Mathematical Finance was reported by a search listing and not opened"
url: "https://arxiv.org/pdf/2310.11771"
pdf: "sources/03-perp-pricing-funding/ackerer-2023-perpetual-futures-pricing.pdf"
access: "full-text"
source_type: "working-paper"
evidence_grade: "B"
topic: "03-perp-pricing-funding"
asset_class: "crypto"
horizon: "n/a"
tags: "perpetual-futures, no-arbitrage, funding-rate, inverse-contracts, quanto, pricing-theory"
---

## Key insight
Under a risk-neutral measure the perpetual futures price is the expected spot price at a random future time whose distribution is set by the funding premium coefficient. A stronger coefficient means a shorter effective maturity and a perp closer to spot. With constant rates the perp-to-spot ratio has a closed form driven by the interest differential between the quote and base currencies.

## Method
Discrete time, two currencies `a` (quote) and `b` (base) with rates `r_a`, `r_b`, spot `x`, perp `f`. Each period the long receives `(f(t+1) - f(t)) - k*(f(t) - x(t)) - i*x(t)`, where `k` is the premium coefficient and `i` the interest factor. Zero cost of entry plus a no-bubble condition gives (Theorem 1) `f(t) = E_Q[ x(t + theta) ]` when `i = 0` and `k` is constant, with `theta` geometric with mean `1/k` periods. With constant parameters (Proposition 1):

`f/x = (k - i)*(1 + r_b) / (r_b - r_a + k*(1 + r_b))`

and with `i = 0`, `f/x = k*(1 + r_b) / (k*(1 + r_b) - d)` where `d = r_a - r_b`. The paper extends this to continuous time, inverse and quanto contracts (with a convexity correction in Black-Scholes) and everlasting options.

## Data and sample
None beyond a descriptive figure of BTC perpetual volume and open interest by venue, January 2019 to December 2023. The paper states that in the first half of 2023 perpetuals were 75% of the 27 billion dollar average daily BTC futures volume and 94% of the 8 billion dollar open interest.

## Reported results
- The perp sits above spot when `r_a > r_b`, equals spot when the rates are equal, and converges monotonically to spot as `k` grows.
- There is a choice of interest factor that makes the perp equal spot at all times, in which case the contract can be replicated with primitive securities. Setting `f = x` in Proposition 1 gives `i = (r_a - r_b)/(1 + r_b)` (my algebra from their formula).
- The authors state that the price formula in the first version of He et al. was incorrect and that the corrected version is a special case of their result.

## Signal construction
Not a signal. It gives the fair-value anchor: the equilibrium premium is of the order of the per-period interest differential divided by `k`. With `k` near 1 per 8 hours and a dollar rate of a few percent a year, the fair premium is a fraction of a basis point, so any premium of several basis points reflects demand pressure, not carry arithmetic.

## Relevance to SOL perpetuals at minutes to hours
Useful for (1) converting a venue's funding parameters into an effective maturity (`1/k` funding periods), which says how quickly a premium should decay, and (2) checking that Kalshi's interest component is or is not set to make the perp equal the index. Staking yield on SOL plays the role of `r_b` and pushes the fair perp price below spot, all else equal; that is my inference from the formula, not a claim in the paper.

## Caveats
Frictionless theory with constant parameters; ignores the clamp used by Binance and Hyperliquid, which [He et al.](he-2022-fundamentals-perpetual-futures.md) argue shifts the benchmark by about 55 annualised percentage points. No empirical test. The grade reflects rigour of derivation, not trading evidence.
