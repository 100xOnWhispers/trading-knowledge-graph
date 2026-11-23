---
title: "Introduction to Online Convex Optimization (Second Edition)"
authors: "Hazan, Elad"
year: 2023
venue: "arXiv 1909.05207 (v3, August 2023); book manuscript"
url: "https://arxiv.org/pdf/1909.05207"
pdf: "sources/29-signal-combination-online-adaptation/hazan-2023-introduction-online-convex-optimization.pdf"
access: "full-text"
source_type: "book"
evidence_grade: "A"
topic: "29-signal-combination-online-adaptation"
asset_class: "multi"
horizon: "n/a"
tags: "expert-advice, hedge, exponential-weights, fixed-share, adaptive-regret, universal-portfolio, regret-bounds"
---

## Key insight
The textbook theory behind "weight experts by exponentiated past performance". It proves that the Hedge algorithm's cumulative loss exceeds that of the best expert in hindsight by a term that grows only with the square root of time and the logarithm of the number of experts, with no statistical assumptions on the data. It also shows why that guarantee is the wrong one when the best expert changes, and gives the fix: fixed-share mixing and "adaptive regret", which bound regret on every sub-interval. Read here: sections 1.3 (expert advice), 4.1 (universal portfolios) and 10.1 to 10.3 (changing environments).

## Method
Hedge: keep weights W_t(i); play expert i with probability x_t(i) = W_t(i)/Σ_j W_t(j); update W_{t+1}(i) = W_t(i) exp(−ε ℓ_t(i)). Theorem 1.5: for non-negative losses and any expert i*, Σ_t x_t'ℓ_t ≤ Σ_t ℓ_t(i*) + ε Σ_t x_t'ℓ_t² + (log N)/ε. With losses bounded and ε tuned this gives regret of order sqrt(T log N).
Deterministic rules cannot do this: Theorem 1.1 shows any deterministic algorithm can be forced to make at least twice the best expert's mistakes, so randomizing or blending is necessary.
Universal portfolios (section 4.1): with loss −log(r_t'x_t) over the simplex, sublinear regret means average log-wealth growth matches the best constant rebalanced portfolio in hindsight; online gradient descent gives O(sqrt(T)) regret and exp-concavity allows better (online Newton step).
Changing environments (chapter 10): dynamic regret against a moving comparator is O(sqrt(T · P)) for online gradient descent, where P is the comparator's path length. Adaptive regret is the maximum regret over any contiguous interval. Fixed Share: after the multiplicative update p̂, set p_{t+1}(i) = (1 − δ) p̂_{t+1}(i) + δ/N. Theorem 10.3: with exp-concave losses and δ = 1/(2T), regret against the best expert on every interval is O((1/α) log(NT)); if the best expert changes k times, total regret is O(k log(NT/k)).

## Data and sample
None; a theory text. Finance appears only as the motivating portfolio example.

## Reported results
Theorems as above. Two remarks that matter in practice: online gradient descent with strongly convex losses and its optimal step schedule, although it has logarithmic standard regret, can have adaptive regret linear in T, meaning it converges to a fixed answer and stops adapting; and a standard low-regret algorithm in a market that is half bear and half bull "is only required to converge to the average of both optimal portfolios".

## Signal construction
For K strategies with per-bar net returns r_k,t scaled to a bounded range: w_k ← w_k exp(η r_k,t); normalise; then w_k ← (1 − δ) w_k + δ/K; trade the weighted position. Starting values suggested by the theory: η of order sqrt(log K / T_eff) and δ of order 1/T_eff, where T_eff is the number of bars over which the best strategy is expected to stay best. Setting η = 0 recovers equal weights, so the equal-weight benchmark is nested.

## Relevance to SOL perpetuals at minutes to hours
The guarantees hold for adversarial sequences, so they survive non-stationarity, fat tails and regime change, which is rare among the tools in this repository. The price is that they are worst-case and relative: regret is measured against the best strategy in the pool, so if every strategy loses after fees the combiner loses too, and the square-root term can exceed a small edge over realistic horizons. The fixed-share step is the cheap, principled way to stop a dormant signal's weight from collapsing to zero.

## Caveats
Theory only; no trading evidence and no transaction costs (switching weights each bar creates turnover the bounds ignore). Bounded-loss assumptions need returns to be clipped or volatility-scaled. Year refers to the second-edition manuscript read; the first edition is earlier.
