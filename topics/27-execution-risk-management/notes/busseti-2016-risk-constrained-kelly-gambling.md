---
title: "Risk-Constrained Kelly Gambling"
authors: "Busseti, Enzo; Ryu, Ernest K.; Boyd, Stephen"
year: 2016
venue: "arXiv preprint 1603.06183"
url: "https://arxiv.org/pdf/1603.06183"
pdf: "sources/27-execution-risk-management/busseti-2016-risk-constrained-kelly-gambling.pdf"
access: "full-text"
source_type: "working-paper"
evidence_grade: "B"
topic: "27-execution-risk-management"
asset_class: "multi"
horizon: "n/a"
tags: "kelly-criterion, drawdown-probability, leverage, risk-of-ruin, position-sizing, convex-optimization"
---

## Key insight
Full Kelly sizing maximises long-run growth but carries a large probability of deep drawdown. This paper adds an explicit constraint on the probability of ever falling to a fraction `alpha` of starting wealth and shows that a single convex condition guarantees it. The resulting bets beat fractional Kelly: more growth for the same drawdown risk.

## Method
Repeated bets with i.i.d. return vector `r` and a fixed bet vector `b` (fractions of wealth, summing to one, including a risk-free "cash" bet). Wealth is the product of `r_t' b`. Let `W_min` be the lowest wealth ever reached. Drawdown risk is `Prob(W_min < alpha)`.

Bound: for `lambda = log(beta) / log(alpha)`,

`E[(r' b)^(-lambda)] <= 1  implies  Prob(W_min < alpha) < beta`.

The risk-constrained Kelly problem maximises `E[log(r' b)]` subject to this condition, which is convex in `b`. `lambda` acts as a risk-aversion parameter; `lambda = 0` recovers Kelly. A quadratic approximation of the problem is shown to be closely related to Markowitz mean-variance selection. Solved with standard convex solvers for finite outcomes and stochastic methods otherwise.

## Data and sample
Synthetic. A finite-outcome example and a continuous example with returns drawn from a mixture of two log-normal distributions; drawdown risk checked by Monte Carlo (10,000 simulated trajectories of 100 periods in the continuous case).

## Reported results
Target: at most 10% probability of a 30% drawdown (`alpha` = 0.7, `beta` = 0.1, `lambda` = 6.456).

Finite-outcome example:

| Bet | Growth rate | Prob(W_min < 0.7) |
|---|---|---|
| Kelly | 0.062 | 0.397 |
| Risk-constrained, lambda 6.456 | 0.043 | 0.073 |
| Risk-constrained, lambda 5.500 | 0.047 | 0.099 |

Continuous example: Kelly 0.077 growth with 0.569 drawdown probability; risk-constrained (lambda 6.456) 0.039 growth with 0.080.

- The bound is conservative but close: guaranteed 10%, realised about 7 to 8%.
- At matched 10% drawdown risk, the quadratic approximation achieves growth of about 0.044 and fractional Kelly about 0.035, against 0.047 for the risk-constrained bet.

## Signal construction
Not a signal; a leverage rule. Inputs: an empirical distribution of per-trade (or per-period) returns of the strategy per unit of leverage, net of costs and funding. For candidate leverage `L`, compute `E[(1 + L * r)^(-lambda)]` over the sample with `lambda = log(beta)/log(alpha)`; the largest `L` for which this is at most 1 and growth `E[log(1 + L * r)]` is positive is the cap. For a single strategy this is a one-dimensional search. Recompute as the return sample grows.

## Relevance to SOL perpetuals at minutes to hours
This turns "risk of ruin with leverage" into a calculation the bot can run on its own trade history. Two features suit the setting. The condition uses the whole return distribution, so fat left tails from liquidation events are penalised directly through the negative-power moment, where a variance-based rule would under-react. And Kalshi's low maximum leverage (about 3x in the topic 06 snapshot) is likely above what this rule allows for a realistic edge, so the bot's own cap, not the venue's, should bind. Note that any return with `1 + L * r <= 0` makes the moment infinite: leverage must be below the level at which the worst plausible move wipes out equity.

## Caveats
Assumes i.i.d. returns and a fixed bet; real strategy returns are serially dependent and the edge is estimated with error, which Kelly-type rules are sensitive to (see the Kelly note in topic 14). The drawdown is measured from initial wealth, not from a running peak. The empirical distribution will not contain the worst future event. Synthetic examples only.
