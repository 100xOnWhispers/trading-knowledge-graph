---
title: "Optimal Investment Strategies for Controlling Drawdowns"
authors: "Grossman, Sanford J.; Zhou, Zhongquan"
year: 1993
venue: "Mathematical Finance, vol. 3, no. 3, pp. 241-276"
url: "https://ideas.repec.org/a/bla/mathfi/v3y1993i3p241-276.html"
pdf: "none"
access: "abstract-only"
source_type: "peer-reviewed"
evidence_grade: "B"
topic: "27-execution-risk-management"
asset_class: "multi"
horizon: "n/a"
tags: "drawdown-control, portfolio-insurance, position-sizing, high-water-mark, risk-management"
---

## Key insight
If an investor must never lose more than a fixed fraction of the highest wealth reached so far, the optimal policy for constant relative risk aversion is to hold risky exposure in proportion to the "surplus": current wealth minus the drawdown floor. Exposure therefore shrinks automatically as the drawdown deepens and reaches zero at the floor. Because the floor ratchets up with every new high, behaviour at a new high differs from classic portfolio insurance with a fixed floor.

## Method
From the abstract only. Let `M_t` be the maximum wealth attained up to time `t`. The constraint is `W_t >= alpha * M_t` at all times, with `alpha` between 0 and 1. The authors solve the optimal risky investment policy under this constraint for constant relative risk aversion utility. The asset price model, the objective (the abstract does not say whether it is long-run growth or finite-horizon utility) and the derivation were not read.

## Data and sample
None reported in the abstract; a theoretical paper.

## Reported results
From the abstract:
- The optimal policy invests in risky assets "in proportion to the 'surplus'" `W_t - alpha * M_t`.
- It resembles constant-proportion portfolio insurance, but with a stochastic floor `alpha * M_t` in place of a fixed floor.
- At a new high (`W_t = M_t`) the floor is expected to grow faster than wealth, so risky investment can be expected to fall.
- When wealth is close to the floor, risky investment can be expected to rise.
- The authors conjecture that in equilibrium this would create "resistance" levels as the market approaches an all-time high.

The constant of proportionality (how much leverage per unit of surplus) is not given in the abstract and is not confirmed here.

## Signal construction
Not a signal; a position-sizing overlay. Track account equity `W_t` and its running maximum `M_t`. Choose a maximum tolerated drawdown `1 - alpha`. Scale every position by `k * (W_t - alpha * M_t) / W_t`, where `k` is the multiplier appropriate to the strategy's edge and volatility (from the bot's Kelly or volatility-target calculation, topic 14). Update `M_t` on every mark-to-market. In discrete time with gaps, add a buffer, because the continuous-time guarantee assumes exposure can be cut continuously.

## Relevance to SOL perpetuals at minutes to hours
A direct and simple way to make "never lose more than X% from peak" a mechanical property of the bot instead of a hope. It complements, and partly replaces, per-trade stop-losses: the rule reduces size smoothly as losses accumulate, without the round-trip cost and whipsaw of stopping out individual positions. Three practical issues are specific to perps. Price can gap through the floor during a liquidation cascade, so the guarantee is approximate. Exposure near the floor becomes too small to recover, which is by design but means the bot effectively stops trading; a reset policy is needed. Funding and fees keep draining equity even at small size.

## Caveats
Abstract-only; the full text is behind the publisher's paywall and no open copy was found without search access. The result is for continuous trading without costs or jumps. A proportional rule trades more when volatile markets move equity quickly, and those trades pay the spread. The related discrete-time drawdown bound in the Busseti, Ryu and Boyd note, and the expected-drawdown formulas in the Magdon-Ismail et al. note, were read in full and are better sources for numbers.
