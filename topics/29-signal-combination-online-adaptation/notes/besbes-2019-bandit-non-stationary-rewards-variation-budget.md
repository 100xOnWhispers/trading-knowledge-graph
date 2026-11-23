---
title: "Optimal Exploration-Exploitation in a Multi-Armed-Bandit Problem with Non-Stationary Rewards"
authors: "Besbes, Omar; Gur, Yonatan; Zeevi, Assaf"
year: 2019
venue: "arXiv 1405.3316 (v2, 2019; marked to appear in Stochastic Systems; extended abstract dated 2014)"
url: "https://arxiv.org/pdf/1405.3316"
pdf: "sources/29-signal-combination-online-adaptation/besbes-2019-bandit-non-stationary-rewards-variation-budget.pdf"
access: "full-text"
source_type: "peer-reviewed"
evidence_grade: "B"
topic: "29-signal-combination-online-adaptation"
asset_class: "multi"
horizon: "n/a"
tags: "non-stationary-bandit, variation-budget, minimax-regret, exp3-restart, dynamic-oracle, forgetting"
---

## Key insight
Quantifies the price of non-stationarity in one number. If the arms' mean rewards can drift by a total amount V_T over T rounds (the "variation budget"), the best achievable regret against an oracle that always plays the currently best arm is of order (K V_T)^(1/3) T^(2/3). Even a fixed, small amount of total drift pushes regret from the stationary sqrt(T) (or log T) rate to T^(2/3); if drift grows in proportion to T, no policy can achieve sublinear regret. Only the abstract, introduction and main theorems were read.

## Method
K arms whose mean reward sequences are arbitrary except that their cumulative period-to-period change over the horizon is bounded by V_T (the exact norm used was not transcribed here). Regret is measured against the dynamic oracle. Lower bound (Theorem 1): any policy has regret at least C K^(1/3) V_T^(1/3) T^(2/3). The construction splits the horizon into batches of length about (T/V_T)^(2/3), with a different randomly chosen "good" arm in each batch so that nothing learned carries over. Upper bound (Theorem 2): Rexp3, which runs the adversarial-bandit algorithm Exp3 and restarts it every Δ = (K log K)^(1/3) (T/V_T)^(2/3) rounds, achieves regret at most C̄ (K log K)^(1/3) V_T^(1/3) T^(2/3). A continuously updating variant (Exp3.S-style) attains the same rate up to a (log T)^(1/3) factor. Exploration must be much heavier than in the stationary case: of order V_T^(1/3) T^(2/3) exploration rounds against order sqrt(T).

## Data and sample
Theory with illustrative numerical experiments on synthetic reward sequences; no market data.

## Reported results
- Minimax regret is of order V_T^(1/3) T^(2/3), giving a continuum from T^(2/3) (bounded drift) to linear regret (drift proportional to T).
- The policy needs the variation budget in advance to set its restart length. The authors state they could not prove a rate-optimal policy for an unknown budget; they describe an envelope of subordinate policies with different guesses and report that numerical results make the conjecture plausible.
- Restarting (abrupt forgetting) and continuous discounting are both rate-optimal ways to balance "remembering and forgetting".

## Signal construction
Not a signal. Two design rules follow. (1) Memory length for any adaptive allocator should scale as (T/V)^(2/3): halving the expected drift lengthens the optimal window by a factor of about 1.6, not 2. (2) A periodic hard reset of a bandit or weighting scheme is theoretically as good as smooth discounting, and it is easier to reason about operationally (the schedule is known and can be aligned with re-fits of the underlying models).

## Relevance to SOL perpetuals at minutes to hours
A direct argument for humility about adaptive strategy selection. Crypto strategy edges drift continuously, so V_T plausibly grows with T, which is the regime where the theory says tracking the best arm cannot be done with vanishing average regret. The implication is to keep the arm set small (regret grows with K^(1/3)), prefer blending to winner-take-all selection, and judge any selector by its realised regret against equal weighting, not against the hindsight-best strategy. The variation budget can be estimated empirically from rolling strategy Sharpe ratios to pick a memory length.

## Caveats
Worst-case theory with bounded rewards; real strategy returns are heavy-tailed and autocorrelated. Bandit feedback is assumed, whereas a trading system usually observes hypothetical returns of all strategies, which makes the problem easier than modelled. No costs of switching arms. The numerical section was not read in detail.
