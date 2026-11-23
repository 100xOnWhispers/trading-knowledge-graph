---
title: "Good and bad properties of the Kelly criterion"
authors: "MacLean, Leonard C.; Thorp, Edward O.; Ziemba, William T."
year: 2010
venue: "Working paper dated 1 January 2010, written as a chapter of an edited volume on the Kelly criterion (volume title not confirmed)"
url: "https://www.stat.berkeley.edu/~aldous/157/Papers/Good_Bad_Kelly.pdf"
pdf: "sources/14-volatility-forecasting/maclean-2010-good-bad-properties-kelly-criterion.pdf"
access: "full-text"
source_type: "book"
evidence_grade: "B"
topic: "14-volatility-forecasting"
asset_class: "multi"
horizon: "n/a"
tags: "kelly-criterion, fractional-kelly, position-sizing, log-utility, overbetting, estimation-error"
---

## Key insight
Betting the Kelly fraction (maximising expected log wealth) maximises long-run growth, but the bets are large and the short-run ride is rough. Betting more than Kelly is strictly worse: risk rises and growth falls, reaching zero excess growth at twice Kelly. Because the Kelly bet is extremely sensitive to errors in the estimated mean, and means are the hardest input to estimate, practitioners should bet a fraction of Kelly.

## Method
A survey by three of the criterion's principal developers, listing proven properties with citations, illustrated by a blackjack example and investor case studies. Key formulas:
- Two-outcome bet: Kelly fraction equals edge divided by odds.
- Continuous time, lognormal asset: optimal fraction X = (mu - r) / sigma^2, with growth rate r + (mu - r)^2 / (2 sigma^2).
- Growth at leverage Y: g = r + (mu - r) Y - 0.5 sigma^2 Y^2, which returns to r at Y = 2X (derivation in the appendix).
- Fractional Kelly with fraction alpha is equivalent, for lognormal assets, to maximising negative power utility with parameter delta where alpha = 1 / (1 - delta); half Kelly corresponds to delta = -1 and quarter Kelly to delta = -3. The equivalence is only approximate for other distributions.

## Data and sample
Mostly theoretical. Illustrations: blackjack with a 2% edge (p = 0.51), and a table from Chopra and Ziemba on the cost of input errors.

## Reported results
- Blackjack table: at full Kelly the probability of doubling before halving is 0.67 with relative growth 1.00; at half Kelly 0.89 and 0.75; at 0.3 Kelly 0.98 and 0.51; at 1.5 Kelly 0.56 and 0.75; at 2.0 Kelly 0.50 and 0.00.
- Errors in means are roughly 20 times as costly as errors in covariances and 10 times as costly as errors in variances at a risk tolerance of 50; the ratios grow as risk aversion falls, and log utility has very low risk aversion.
- Good properties include: maximal asymptotic growth, minimal expected time to large goals, no risk of total ruin in the ideal model, and a myopic policy (no need to forecast future opportunities).
- Bad properties listed: bets can be a very large fraction of wealth when the wager is favourable and the perceived risk of loss is small (an example cites a 64% optimal wager); with any fixed fraction f, an equal number of wins and losses leaves the bettor behind, at W0 (1 - f^2)^n after n wins and n losses; and the unweighted average return converges to half the arithmetic rate, so the bettor regularly wins less than expected.
- The closing discussion stresses the extreme sensitivity of expected-log calculations to errors in mean estimates and recommends reducing wager size to be safe; it notes practitioners who want to protect capital cut risk sharply as drawdown grows.

## Signal construction
A sizing rule, not a signal. For a trade with estimated expected return mu over the holding period and forecast variance sigma^2, full-Kelly leverage is mu / sigma^2. Apply a fraction (commonly one quarter to one half) and a hard leverage cap. With the edge held roughly constant per unit of volatility, this collapses to inverse-volatility sizing; with a constant expected return it collapses to inverse-variance sizing as in Moreira and Muir.

## Relevance to SOL perpetuals at minutes to hours
The asymmetry around the optimum is the practical lesson: half Kelly gives up a quarter of growth for a large gain in safety, while overestimating the edge by a factor of two erases all growth. A new bot's edge estimate on a new venue is highly uncertain, which argues for a small fraction. The lognormal, continuous-rebalancing model has no jumps, funding payments or liquidation; with a liquidation threshold, "never risks ruin" no longer holds, and leverage must also satisfy a tail-based liquidation constraint (see the Cheng note).

## Caveats
A summary chapter, not new empirical work. Results assume known distributions and frictionless continuous rebalancing. Kelly's original 1956 paper and Thorp's longer treatment were not opened in this session. The open copy is hosted on a university course page.
