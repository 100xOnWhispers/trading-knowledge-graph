---
title: "On Upper-Confidence Bound Policies for Non-Stationary Bandit Problems"
authors: "Garivier, Aurelien; Moulines, Eric"
year: 2008
venue: "arXiv preprint 0805.3415 (a conference version is usually cited as ALT 2011; not confirmed in this session)"
url: "https://arxiv.org/pdf/0805.3415"
pdf: "sources/29-signal-combination-online-adaptation/garivier-2008-ucb-policies-non-stationary-bandits.pdf"
access: "full-text"
source_type: "working-paper"
evidence_grade: "B"
topic: "29-signal-combination-online-adaptation"
asset_class: "multi"
horizon: "n/a"
tags: "non-stationary-bandit, discounted-ucb, sliding-window-ucb, exp3s, regret-lower-bound, strategy-selection"
---

## Key insight
The reference analysis of the two simplest ways to make a bandit forget: discount old rewards (D-UCB) or use only the last τ plays (SW-UCB). When reward distributions change abruptly at unknown times, both achieve regret of order sqrt(T × number of breaks) up to logarithmic factors, and the paper proves that no policy can do better than order sqrt(T). A consequence stated by the authors: any policy that achieves the usual logarithmic regret in a stationary world, such as standard UCB-1, cannot also track changes well.

## Method
K arms; rewards bounded by B; the mean of each arm is piecewise constant with Υ_T breakpoints up to time T. Regret is measured against the oracle that plays the currently best arm at each step.
- D-UCB (Kocsis and Szepesvari): discounted count N_t(γ,i) = Σ_s γ^(t−s) 1{I_s = i}; discounted mean X̄_t(γ,i) = (1/N_t(γ,i)) Σ_s γ^(t−s) X_s(i) 1{I_s = i}; play the arm maximising X̄_t(γ,i) + 2B sqrt(ξ log n_t(γ) / N_t(γ,i)), where n_t(γ) = Σ_i N_t(γ,i).
- SW-UCB (introduced here): the same with plain averages over the last τ plays and padding B sqrt(ξ log(min(t,τ)) / N_t(τ,i)).
- Tuning from the theorems: γ = 1 − (4B)⁻¹ sqrt(Υ_T/T) gives suboptimal plays of order sqrt(T Υ_T) log T; τ = 2B sqrt(T log T / Υ_T) gives order sqrt(Υ_T T log T). If breaks occur at a constant rate r per step, γ = 1 − sqrt(r)/(4B) and regret is linear in T with a small constant.
- Lower bound: with abrupt changes no policy has non-stationary regret of smaller order than sqrt(T).

## Data and sample
Two synthetic Bernoulli experiments. (1) Three arms, T = 10,000; arm 3's success probability jumps from 0.4 to 0.9 between t = 3,000 and t = 5,000. (2) Two arms, one fixed at 0.5 and one following 0.5 + 0.4 cos(6πt/T).

## Reported results
- D-UCB performs "almost as well as" SW-UCB; both detect breakpoints far sooner than UCB-1 and than EXP3.S tuned as its theory prescribes.
- UCB-1 reacts quickly to the first break (its confidence interval on the improved arm was still loose) but takes "a very long time" to return to the original arm after the second break.
- In the smoothly cycling environment D-UCB and SW-UCB track the cycle and have nearly equal regret; UCB-1 fails to follow the best arm and EXP3.S accumulates more regret.
- Performance depends on γ or τ, which require a guess of the break frequency; adaptive tuning is left open.

## Signal construction
A strategy selector. Arms are strategies or parameter sets; reward is the per-period net return of the arm that was traded, clipped and rescaled to [0, 1]. Keep discounted sums and counts per arm, compute the index above each period, and allocate to the top arm (or weight arms by a softmax of the indices). The effective memory is 1/(1 − γ) periods; choose it from the expected time between regime changes. In trading every arm's hypothetical return is usually observable, so the full-information update (all arms updated each period) can replace bandit feedback, which removes the need for the exploration bonus except where market impact or fill uncertainty makes paper returns unreliable.

## Relevance to SOL perpetuals at minutes to hours
Gives a principled reading of a familiar heuristic (allocate to what has worked lately, with an optimism bonus) and a formula linking memory length to break frequency. The lower bound is the sober part: with one break every few hundred decisions, the unavoidable regret is a material fraction of any small edge. Intraday P&L violates the bounded, independent-reward assumptions (fat tails, autocorrelated strategy returns), so the constants do not transfer and the ranking of D-UCB against SW-UCB should be re-tested on strategy return streams.

## Caveats
Theory and synthetic simulations only; no financial data, costs or switching penalty. Assumes piecewise-constant means. The arXiv version of 2008 was read.
