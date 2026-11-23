---
title: "A Hybrid Genetic-Programming Swarm-Optimisation Approach for Examining the Nature and Stability of High Frequency Trading Strategies"
authors: "Funie, Andreea-Ingrid; Salmon, Mark; Luk, Wayne"
year: 2014
venue: "13th International Conference on Machine Learning and Applications (ICMLA 2014)"
url: "https://www.doc.ic.ac.uk/~wl/papers/14/icmla14if.pdf"
pdf: "sources/07-order-book-imbalance/funie-2014-genetic-programming-swarm-hft-rules.pdf"
access: "full-text"
source_type: "peer-reviewed"
evidence_grade: "C"
topic: "07-order-book-imbalance"
asset_class: "fx"
horizon: "tick"
tags: "genetic-programming, particle-swarm, evolutionary-algorithms, order-book-inputs, rule-stability, alpha-decay, fpga"
---

## Key insight
Evolutionary search can assemble trading rules from order-book and price inputs, and the rules it found on tick-level FX data were profitable in 2003. Applied to 2008 data the same machinery did not produce statistically significant conditional profitability, which the authors read as the market becoming more efficient as electronic high-frequency trading grew. Evolved rules are regime-specific and their edge decays; the paper's contribution is the framework for testing rule stability, not a durable rule.

## Method
Genetic programming evolves tree-structured rules. Terminals include market variables updated on each tick: prices, logs, moving averages, maxima and minima over several periods, constants, and order book quantities such as volume on the bid and depth on the ask. Functions are arithmetic, max and min, comparisons, logical operators, absolute value and sign change. Fitness is cumulative return from buying or selling a fixed 1 million GBP on each signal, executed at best bid or ask so the spread is paid. An inertia filter k requires price to move k units from the last transaction before trading again, to limit turnover. Particle swarm optimisation is layered on the best half of each generation to select groups of rules that trade by majority vote. Fitness evaluation is accelerated on FPGA hardware. Stability tests: whether the best rule from one month ranks in the top 15% in other months; how often failed rules are re-accepted; behavior under added noise; and the Anatolyev-Gerko test of conditional profitability.

## Data and sample
Tick-level foreign exchange data (a GBP pair; the exact pair was not confirmed in the text read) for January to March of 2003 and 2004, with further comparisons on 2008 data. Population of 150 rules per run with varying iteration counts.

## Reported results
- In January to March 2003, least-fit strategies are re-accepted between 21.08% and 50.88% of the time, rising with the number of iterations; re-acceptance is higher in 2004, which the authors take as a sign that patterns were harder to find.
- Profitability increases with the number of search iterations.
- Anatolyev-Gerko statistics are all positive for 2003; for 2008 two are negative (at k = 0 and k = 4), meaning the conditioning information did worse than random trading.
- The authors conclude that the hybrid algorithm did not deliver statistically significant conditional profitability in 2008 although it did in 2003.

## Signal construction
Not a fixed signal. It is a search procedure: define a terminal set of normalized book features (queue imbalance, multi-level OFI, depth ratios, spread, micro-price deviation, their moving averages and extrema), a small function set, and a fitness that is net-of-cost PnL with a turnover penalty. Evolve on a rolling window, keep an ensemble that votes, and require candidates to rank well on adjacent out-of-sample months before deployment.

## Relevance to SOL perpetuals at minutes to hours
This is the only evolutionary-algorithm source on order-book inputs verified in this session, so it is included for the method. For a SOL bot, genetic programming or symbolic regression over the imbalance features in this topic is a reasonable way to discover nonlinear combinations and interaction terms, provided the stability tests here (cross-period rank persistence, re-acceptance rate, noise injection) are part of the pipeline. The 2003 versus 2008 contrast is the same alpha-decay story seen elsewhere in this topic.

## Caveats
FX, not crypto; data from 2003 to 2008. Six-page conference paper with limited detail on inputs and costs beyond the spread. Search over a large rule space with few independent test periods carries high data-snooping risk. No evidence that order-book terminals, as opposed to price terminals, drove the results.
