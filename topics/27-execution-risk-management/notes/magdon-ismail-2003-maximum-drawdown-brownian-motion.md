---
title: "On the Maximum Drawdown of a Brownian Motion"
authors: "Magdon-Ismail, Malik; Atiya, Amir F.; Pratap, Amrit; Abu-Mostafa, Yaser S."
year: 2003
venue: "Author manuscript dated September 1, 2003 (later journal publication not confirmed in this session)"
url: "https://www.cs.rpi.edu/~magdon/ps/journal/drawdown_journal.pdf"
pdf: "sources/27-execution-risk-management/magdon-ismail-2003-maximum-drawdown-brownian-motion.pdf"
access: "full-text"
source_type: "working-paper"
evidence_grade: "B"
topic: "27-execution-risk-management"
asset_class: "multi"
horizon: "n/a"
tags: "maximum-drawdown, brownian-motion, risk-budgeting, drawdown-control, kill-switch"
---

## Key insight
For a strategy whose profit and loss behaves like a Brownian motion with drift `mu` and volatility `sigma`, the expected maximum drawdown over a horizon `T` has an exact expression, and its growth with time depends only on the sign of the drift: logarithmic for a profitable strategy, square-root for a zero-edge strategy, linear for a losing one. This gives a baseline for what drawdown is normal, and so for when an observed drawdown is evidence that the edge has gone.

## Method
Mathematical derivation. Maximum drawdown is `D(T) = sup over t of [ sup over s <= t of X(s) - X(t) ]` for `X` a Brownian motion with drift. The authors derive an infinite-series representation of its distribution and of its expectation, plus limiting behaviour as `T` grows. With `alpha = mu * sqrt(T / (2 * sigma^2))`:

`E[D] = (2 * sigma^2 / mu) * Q(alpha^2)`,

where `Q` is `Q_p` for positive drift and `-Q_n` for negative drift, two functions tabulated in the paper's appendix.

## Data and sample
None; a probability paper.

## Reported results
- Zero drift: `E[D] = sqrt(pi/2) * sigma * sqrt(T)`, about `1.2533 * sigma * sqrt(T)` (the paper writes this as `2 * gamma * sigma * sqrt(T)` with `gamma = sqrt(pi/8)`, about 0.6267).
- Positive drift, large `T`: `Q_p(x)` tends to `0.25 * log(x) + 0.49088`, so `E[D]` grows like `(sigma^2 / mu) * (0.5 * log(T) + constant)`.
- Negative drift, large `T`: `Q_n(x)` tends to `x + 0.5`, so drawdown grows linearly at the rate of the drift.
- For small `x` both functions tend to `gamma * sqrt(2x)`, recovering the zero-drift case: over short horizons a profitable strategy's drawdown is indistinguishable from a zero-edge one.

## Signal construction
Not a market signal; a monitoring statistic. Estimate the strategy's per-trade (or per-hour) mean `mu` and standard deviation `sigma` of profit and loss from backtest and live data. Compute the expected maximum drawdown for the elapsed live time `T` from the formula, and ideally the distribution by simulation. Compare the realised maximum drawdown with it. A realised drawdown well beyond the high quantiles for the assumed `mu`, or one that grows linearly with time instead of flattening, is the trigger to cut size or halt. Recompute daily.

## Relevance to SOL perpetuals at minutes to hours
Directly usable for setting drawdown limits and a kill switch without guessing. For a profitable strategy the expected drawdown scales with `sigma^2 / mu`, the ratio of variance to edge: halving the edge through extra fees roughly doubles the normal drawdown, which links cost control to drawdown control. With a 12 bp taker fee against a few basis points of gross edge per trade, the net `mu` is fragile, so the drawdown budget should be computed with the pessimistic `mu`. The square-root law gives the worst-case baseline: if the edge is in fact zero, expect about `1.25 * sigma * sqrt(T)`.

## Caveats
Brownian motion: no fat tails, no volatility clustering, no serial correlation, constant position size. Crypto intraday returns violate all four, and real drawdowns will exceed these figures; treat them as a lower bound and prefer a block bootstrap of the bot's own trade returns for limits. The formula is for additive profit and loss; with compounding or drawdown-dependent sizing (Grossman and Zhou) it changes. The expectation alone says little about the tail; the series for the full distribution is in the paper but was not checked numerically here. Manuscript version read.
